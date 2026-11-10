"""
Service tests for Provenance Guard — units 7 and 8.

    python -m unittest discover -s tests -v

These never load GPT-2: `detector.model_signal` is replaced with a stub, so
the tests check the route, the logging, the limiter and the label mapping
rather than the model. Each test writes to its own temporary audit log, so
`logs/audit.jsonl` is never touched.
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import config  # noqa: E402
import audit  # noqa: E402
import detector  # noqa: E402
import scoring  # noqa: E402
import app as appmod  # noqa: E402

NINE_FIELDS = {"timestamp", "content_id", "creator_id", "guess", "model_score",
               "style_score", "combined_score", "label", "status"}

SAMPLE = ("The committee met on Tuesday to review the proposal. Several members "
          "raised concerns about the budget, and the vote was postponed.")


class ServiceTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._saved = (config.LOG_DIR, config.AUDIT_LOG, detector.model_signal)
        config.LOG_DIR = Path(self._tmp.name)
        config.AUDIT_LOG = config.LOG_DIR / "audit.jsonl"
        detector.model_signal = lambda text: 0.5
        if hasattr(appmod.limiter, "reset"):
            appmod.limiter.reset()
        appmod.app.config["PROPAGATE_EXCEPTIONS"] = False
        self.client = appmod.app.test_client()

    def tearDown(self):
        config.LOG_DIR, config.AUDIT_LOG, detector.model_signal = self._saved
        self._tmp.cleanup()

    def submit(self, text=SAMPLE, creator_id="tester", **kwargs):
        if kwargs:
            return self.client.post("/submit", **kwargs)
        return self.client.post("/submit", json={"text": text, "creator_id": creator_id})

    def decisions(self):
        return [e for e in audit.read_entries() if e.get("status") == "decided"]

    def rejections(self):
        return [e for e in audit.read_entries() if e.get("status") == "rejected"]


class TestHealthAndSubmit(ServiceTestCase):
    def test_health_reports_rate_limiting(self):
        body = self.client.get("/health").get_json()
        self.assertTrue(body["ok"])
        self.assertEqual(body["rate_limiting"], config.RATE_LIMITING_ENABLED)

    def test_successful_submit_returns_all_fields_and_logs_nine(self):
        response = self.submit()
        self.assertEqual(response.status_code, 200)
        body = response.get_json()
        for field in ("content_id", "guess", "confidence", "label",
                      "model_score", "style_score"):
            self.assertIn(field, body)

        decisions = self.decisions()
        self.assertEqual(len(decisions), 1)
        entry = decisions[0]
        self.assertTrue(NINE_FIELDS <= set(entry))
        for field in NINE_FIELDS:
            self.assertIsNotNone(entry[field], field)
        self.assertEqual(entry["content_id"], body["content_id"])

    def test_submitted_text_is_never_written_to_the_log(self):
        secret = "UniqueCanaryPhrase " + SAMPLE
        self.submit(text=secret)
        self.submit(text=secret, creator_id="")          # rejected
        raw = config.AUDIT_LOG.read_text(encoding="utf-8")
        self.assertNotIn("UniqueCanaryPhrase", raw)


class TestInvalidInput(ServiceTestCase):
    """Criterion 5: ten invalid requests, all 400, no submission records."""

    INVALID = [
        {"text": "", "creator_id": "bad_1"},
        {"text": "   \n\t ", "creator_id": "bad_2"},
        {"creator_id": "bad_3"},                          # no text field
        {"text": None, "creator_id": "bad_4"},
        {"text": 12345, "creator_id": "bad_5"},
        {"text": ["a", "list"], "creator_id": "bad_6"},
        {"text": {"nested": "object"}, "creator_id": "bad_7"},
        {"text": SAMPLE},                                 # no creator_id
        {"text": SAMPLE, "creator_id": ""},
        {"text": SAMPLE, "creator_id": 42},
    ]

    def test_ten_invalid_requests_return_400_and_log_rejections_only(self):
        for body in self.INVALID:
            with self.subTest(body=body):
                self.assertEqual(self.submit(json=body).status_code, 400)

        self.assertEqual(self.decisions(), [])
        rejections = self.rejections()
        self.assertEqual(len(rejections), len(self.INVALID))
        for entry in rejections:
            self.assertTrue(NINE_FIELDS <= set(entry))
            self.assertIsNone(entry["content_id"])
            self.assertIn(entry["reason"], {"invalid_text", "invalid_creator_id"})

    def test_unparseable_json_is_a_logged_400(self):
        response = self.submit(data='{"text": ', content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.rejections()[-1]["reason"], "invalid_text")


class TestFailuresAreLogged(ServiceTestCase):
    def test_detector_failure_is_logged_not_silent(self):
        def unavailable(text):
            raise detector.DetectorUnavailable("model missing")
        detector.model_signal = unavailable

        response = self.submit(creator_id="detector_down")
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json()["error"], "internal_error")
        self.assertEqual(self.decisions(), [])
        entry = self.rejections()[-1]
        self.assertEqual(entry["reason"], "internal_error")
        self.assertEqual(entry["error_type"], "DetectorUnavailable")
        self.assertEqual(entry["creator_id"], "detector_down")
        self.assertNotIn("model missing", json.dumps(entry))


@unittest.skipUnless(config.RATE_LIMITING_ENABLED, "rate limiting is off")
class TestRateLimit(ServiceTestCase):
    def test_limit_then_429_and_each_rejection_logged(self):
        codes = [self.submit(creator_id="flooder").status_code
                 for _ in range(config.RATE_LIMIT_PER_MINUTE + 5)]
        self.assertEqual(codes, [200] * config.RATE_LIMIT_PER_MINUTE + [429] * 5)

        limited = [e for e in self.rejections() if e["reason"] == "rate_limited"]
        self.assertEqual(len(limited), 5)
        self.assertTrue(all(e["creator_id"] == "flooder" for e in limited))
        self.assertEqual(len(self.decisions()), config.RATE_LIMIT_PER_MINUTE)

    def test_limit_is_per_creator(self):
        for _ in range(config.RATE_LIMIT_PER_MINUTE):
            self.submit(creator_id="busy_writer")
        self.assertEqual(self.submit(creator_id="busy_writer").status_code, 429)
        self.assertEqual(self.submit(creator_id="other_writer").status_code, 200)


class TestAppeal(ServiceTestCase):
    """Criterion 4: valid appeals are recorded and move status to under_review."""

    def test_ten_appeals_recorded_as_under_review(self):
        ids = []
        for i in range(10):
            ids.append(self.submit(creator_id=f"appealer_{i}").get_json()["content_id"])
        for content_id in ids:
            response = self.client.post("/appeal", json={
                "content_id": content_id, "reasoning": "I wrote this myself."})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json()["status"], "under_review")

        for content_id in ids:
            entries = audit.entries_for(content_id)
            self.assertEqual([e["status"] for e in entries], ["decided", "under_review"])

    def test_unknown_or_invalid_appeal_is_rejected_and_logged(self):
        missing = self.client.post("/appeal", json={"content_id": "does-not-exist",
                                                    "reasoning": "please"})
        self.assertEqual(missing.status_code, 404)
        no_reason = self.client.post("/appeal", json={"content_id": "x"})
        self.assertEqual(no_reason.status_code, 400)
        reasons = [e["reason"] for e in self.rejections()]
        self.assertEqual(reasons, ["appeal_not_found", "invalid_reasoning"])
        # A rejected appeal must not attach itself to a submission.
        self.assertEqual(audit.entries_for("does-not-exist"), [])


class TestLabelBoundaries(unittest.TestCase):
    """Criterion 3: just below and just above both thresholds."""

    def test_boundaries(self):
        h, a = config.HUMAN_THRESHOLD, config.AI_THRESHOLD
        cases = [(h - 0.0001, "human"), (h, "unsure"), (h + 0.0001, "unsure"),
                 (a - 0.0001, "unsure"), (a, "unsure"), (a + 0.0001, "ai"),
                 (0.0, "human"), (1.0, "ai")]
        for score, expected in cases:
            with self.subTest(score=score):
                self.assertEqual(scoring.score_to_label(score)[0], expected)

    def test_combine_is_weighted_average(self):
        self.assertEqual(scoring.combine_signals(0.406, 0.5733), 0.4897)


if __name__ == "__main__":
    unittest.main()
