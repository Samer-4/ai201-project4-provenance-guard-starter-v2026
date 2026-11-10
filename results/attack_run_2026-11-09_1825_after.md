# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 18:25
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `b71b3721-f5e4-45c0-889d-cc16add9faec` | human | 0.335 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `2d64a8ad-8262-4543-af46-1cdb34a154b2` | unsure | 0.200 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `5ae3ef57-9747-4b31-9021-defe430c1298` | unsure | 0.052 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `0853c5a5-aea7-4efe-945a-1146c9072bed` | unsure | 0.100 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `25994bcb-cf96-48ca-8400-cb243810f74f` | human | 0.370 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `0cef271d-c277-4d24-8715-e4945ebc9796` | unsure | 0.185 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `79156258-9aa2-4dd4-8b92-753ec45b07c2` | unsure | 0.081 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `a29ed100-5f1f-4503-8498-05d22208069f` | human | 0.401 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `5ac191c6-0ef5-4ca9-b510-077fe14264d1` | unsure | 0.088 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `2d9d441d-af77-4526-827b-25ba6a4e6327` | ai | 0.668 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `1ead45d1-9d32-4526-9842-7128d0308455` | unsure | 0.086 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `718e5a9e-001d-4ff2-b9d1-7173ff0ee21e` | unsure | 0.288 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `1fc127ad-de4f-46f0-83d9-a1254eb71423` | ai | 0.329 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `bcafc4c5-3be1-4146-b198-86d23e71670d` | unsure | 0.274 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `ea626d29-c54f-4720-b786-ed8763388bfc` | ai | 0.370 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `6010657a-ade2-4b43-bdbd-66b1715be507` | ai | 0.307 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `95bf66c0-3c32-4c71-8ef5-e2cc627c904e` | ai | 0.304 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `f9fac7b4-cc15-4791-b964-6c9c6aa07475` | human | 0.451 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `f3089d8a-0912-4e7a-af30-32aedac8a12d` | unsure | 0.250 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `15bded25-c709-4926-9c89-959dd227868c` | human | 0.557 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `e14684ec-df04-4040-a963-ccc76030abec` | unsure | 0.033 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c5cf1729-f423-43ee-ac0a-abf88e1a2aaa` | unsure | 0.069 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `86d438f9-f6b4-4c76-9761-89c87aef42c2` | unsure | 0.135 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `0984446a-f4d4-4432-9f84-1a59d487f998` | unsure | 0.032 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 200 | `f2efb622-1355-4f06-9682-91557b4d8595` | ai | 0.749 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c226d3e4-0cc7-4641-af17-53a69f607cda` | human | 0.645 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d2f9739a-58ee-4516-bf4f-ec459d879222` | human | 0.645 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bac7b5e7-cde6-4212-b5fe-63827f7ea112` | human | 0.645 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `03c8e729-69cb-4ad4-b513-c92bd1c13aa0` | human | 0.645 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1f287ade-fe86-45ad-aef3-f4705bd280cf` | human | 0.645 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `acb19fdf-8bdb-4372-b8b7-dd7b3b6fddb6` | human | 0.645 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `070c9668-fc32-4811-85c6-2dd6b62579d8` | human | 0.645 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2d997049-3d9f-47e7-ad8e-6d52595000ba` | human | 0.645 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `93ea0f6f-8d87-46c8-aa8c-b11fe79ae9b7` | human | 0.645 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d2aa8302-fe8e-433d-b7e5-6283a216f5b6` | human | 0.645 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "b71b3721-f5e4-45c0-889d-cc16add9faec",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3354,
  "model_score": 0.1635,
  "style_score": 0.5012,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "2d64a8ad-8262-4543-af46-1cdb34a154b2",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.1996,
  "model_score": 0.5943,
  "style_score": 0.2061,
  "label": "There is not enough evidence to determine whether this writing was generated by AI or written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "5ae3ef57-9747-4b31-9021-defe430c1298",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.0524,
  "model_score": 0.6662,
  "style_score": 0.3862,
  "label": "There is not enough evidence to determine whether this writing was generated by AI or written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "0853c5a5-aea7-4efe-945a-1146c9072bed",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.1,
  "model_score": 0.6114,
  "style_score": 0.4886,
  "label": "There is not enough evidence to determine whether this writing was generated by AI or written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "25994bcb-cf96-48ca-8400-cb243810f74f",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.37,
  "model_score": 0.3212,
  "style_score": 0.3088,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "0cef271d-c277-4d24-8715-e4945ebc9796",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.1854,
  "model_score": 0.5727,
  "style_score": 0.242,
  "label": "There is not enough evidence to determine whether this writing was generated by AI or written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "79156258-9aa2-4dd4-8b92-753ec45b07c2",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.081,
  "model_score": 0.5862,
  "style_score": 0.3327,
  "label": "There is not enough evidence to determine whether this writing was generated by AI or written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "a29ed100-5f1f-4503-8498-05d22208069f",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.4012,
  "model_score": 0.2452,
  "style_score": 0.3535,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "5ac191c6-0ef5-4ca9-b510-077fe14264d1",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.0884,
  "model_score": 0.7042,
  "style_score": 0.3842,
  "label": "There is not enough evidence to determine whether this writing was generated by AI or written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "2d9d441d-af77-4526-827b-25ba6a4e6327",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.6678,
  "model_score": 0.9792,
  "style_score": 0.6886,
  "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "1ead45d1-9d32-4526-9842-7128d0308455",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.0864,
  "model_score": 0.6175,
  "style_score": 0.4688,
  "label": "There is not enough evidence to determine whether this writing was generated by AI or written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "718e5a9e-001d-4ff2-b9d1-7173ff0ee21e",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.2882,
  "model_score": 0.7387,
  "style_score": 0.5495,
  "label": "There is not enough evidence to determine whether this writing was generated by AI or written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "1fc127ad-de4f-46f0-83d9-a1254eb71423",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.3286,
  "model_score": 0.8051,
  "style_score": 0.5234,
  "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "bcafc4c5-3be1-4146-b198-86d23e71670d",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.2744,
  "model_score": 0.8329,
  "style_score": 0.4415,
  "label": "There is not enough evidence to determine whether this writing was generated by AI or written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "ea626d29-c54f-4720-b786-ed8763388bfc",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.3696,
  "model_score": 0.8005,
  "style_score": 0.5692,
  "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "6010657a-ade2-4b43-bdbd-66b1715be507",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.307,
  "model_score": 0.8814,
  "style_score": 0.4256,
  "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "95bf66c0-3c32-4c71-8ef5-e2cc627c904e",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.3044,
  "model_score": 0.8816,
  "style_score": 0.4229,
  "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "f9fac7b4-cc15-4791-b964-6c9c6aa07475",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.451,
  "model_score": 0.3223,
  "style_score": 0.2268,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "f3089d8a-0912-4e7a-af30-32aedac8a12d",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.25,
  "model_score": 0.4625,
  "style_score": 0.2875,
  "label": "There is not enough evidence to determine whether this writing was generated by AI or written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "15bded25-c709-4926-9c89-959dd227868c",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.5572,
  "model_score": 0.2044,
  "style_score": 0.2385,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "e14684ec-df04-4040-a963-ccc76030abec",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.0328,
  "model_score": 0.5943,
  "style_score": 0.4385,
  "label": "There is not enough evidence to determine whether this writing was generated by AI or written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "c5cf1729-f423-43ee-ac0a-abf88e1a2aaa",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.0692,
  "model_score": 0.4998,
  "style_score": 0.4309,
  "label": "There is not enough evidence to determine whether this writing was generated by AI or written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "86d438f9-f6b4-4c76-9761-89c87aef42c2",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.135,
  "model_score": 0.6401,
  "style_score": 0.2248,
  "label": "There is not enough evidence to determine whether this writing was generated by AI or written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "0984446a-f4d4-4432-9f84-1a59d487f998",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.0322,
  "model_score": 0.5583,
  "style_score": 0.4738,
  "label": "There is not enough evidence to determine whether this writing was generated by AI or written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "f2efb622-1355-4f06-9682-91557b4d8595",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.749,
  "model_score": 0.9876,
  "style_score": 0.7614,
  "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "c226d3e4-0cc7-4641-af17-53a69f607cda",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6454,
  "model_score": 0.0287,
  "style_score": 0.3259,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "d2f9739a-58ee-4516-bf4f-ec459d879222",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6454,
  "model_score": 0.0287,
  "style_score": 0.3259,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "bac7b5e7-cde6-4212-b5fe-63827f7ea112",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6454,
  "model_score": 0.0287,
  "style_score": 0.3259,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "03c8e729-69cb-4ad4-b513-c92bd1c13aa0",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6454,
  "model_score": 0.0287,
  "style_score": 0.3259,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "1f287ade-fe86-45ad-aef3-f4705bd280cf",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6454,
  "model_score": 0.0287,
  "style_score": 0.3259,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "acb19fdf-8bdb-4372-b8b7-dd7b3b6fddb6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6454,
  "model_score": 0.0287,
  "style_score": 0.3259,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "070c9668-fc32-4811-85c6-2dd6b62579d8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6454,
  "model_score": 0.0287,
  "style_score": 0.3259,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "2d997049-3d9f-47e7-ad8e-6d52595000ba",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6454,
  "model_score": 0.0287,
  "style_score": 0.3259,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "93ea0f6f-8d87-46c8-aa8c-b11fe79ae9b7",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6454,
  "model_score": 0.0287,
  "style_score": 0.3259,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "d2aa8302-fe8e-433d-b7e5-6283a216f5b6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6454,
  "model_score": 0.0287,
  "style_score": 0.3259,
  "label": "This writing shows patterns associated with human writing, but authorship cannot be confirmed.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
