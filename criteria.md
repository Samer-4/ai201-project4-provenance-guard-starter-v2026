# Acceptance Criteria — Provenance Guard

These five criteria define what a working Provenance Guard service
should achieve. All targets are established before implementation.

---

## 1. False Positive Rate

Of 20 known human-written samples, no more than 2 may receive
a high-confidence AI label (maximum 10% false-positive rate).
An "unsure" classification does not count as a false positive.

**Why this target:**

Incorrectly accusing a human writer is more harmful than missing
some AI-generated content. A 10% maximum provides a measurable
initial target while prioritizing the protection of human writers.

---

## 2. Score Separation

Across 20 AI-generated and 20 human-written samples, the average
combined AI-likelihood score for AI samples must exceed the
human-written average by at least 0.20 on a 0-to-1 scale.

**Why this target:**

The detector should meaningfully distinguish AI-generated writing
from human writing. A 0.20 separation provides a measurable target
for evaluating whether the two signals are useful together.

---

## 3. Label Coverage and Threshold Boundaries

All three labels must be reachable:
- High-confidence AI
- High-confidence human
- Unsure

Automated tests must also verify classification immediately below
and above both decision thresholds.

**Why this target:**

The system should not force every submission into an AI or human
classification. Testing threshold boundaries helps ensure uncertain
cases are handled consistently.

---

## 4. Appeal Reliability

All 10 valid test appeals must be recorded in the audit trail
and update their corresponding submission status to
`under_review` (100% success).

**Why this target:**

Writers need a dependable way to challenge automated decisions.
Appeals should be recorded and routed toward human review
without requiring another AI-generated judgment.

---

## 5. Invalid Input Handling and Audit Safety

All 10 invalid POST /submit requests must return HTTP 400.

Test cases must include:
- Empty text
- Missing creator_id
- Non-string text

None of the rejected requests may create submission audit records.

**Why this target:**

Invalid requests should fail predictably without generating
misleading classifications or contaminating the audit trail.

---

## Unit 8 Evaluation Note

These targets will be evaluated across three trials in Unit 8.
A criterion must meet its target in every trial to count as met.
Unmet targets will be documented and investigated rather than
silently lowered.
