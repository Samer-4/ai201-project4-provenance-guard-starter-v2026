# Provenance Guard — System Design

## 1. Submission Flow

1. Receive text and creator_id through POST /submit.
2. Generate a unique content_id for tracking.
3. Run the GPT-2 detector to measure text predictability.
4. Run stylometry to measure structural writing patterns.
5. Normalize and combine both signals with equal initial weights.
6. Convert the combined score into a human, AI, or unsure label.
7. Record the decision in the audit log and return the API response.

## 2. Signals and Limitations

### Signal 1: GPT-2 Perplexity
Measures how predictable the word sequences are.

Limitation: Simple or predictable human writing may resemble
AI-generated writing, creating false positives.

### Signal 2: Stylometry
Measures sentence-length variation, vocabulary diversity,
and punctuation patterns.

Limitation: Formatting, paraphrasing, or minor edits can change
these features without changing who authored the text.

Initial weighting: 50% GPT-2, 50% stylometry.
Weights will be evaluated using test samples.

## 3. False Positive Scenario

A human writer submits original writing that receives a
high-confidence AI classification.

The submission is held for human review rather than
automatically rejected or publicly accused.

The writer may submit an appeal, which immediately changes
the submission status to under_review.

A human reviewer evaluates the appeal.
No additional AI system determines whether the appeal is valid.

Trade-off: This reduces the risk of unfair accusations but
can delay publication and increase human review workload.

## 4. API Contracts

### POST /submit

Request:
{
  "text": "Original writing",
  "creator_id": "writer_001"
}

Response (proposed):
{
  "content_id": "unique_identifier",
  "guess": "unsure",
  "confidence": 0.58,
  "label": "The system could not confidently determine authorship."
}

Individual signal scores remain internal for auditing.

### POST /appeal

Request:
{
  "content_id": "unique_identifier",
  "reason": "I wrote this myself and can provide drafts."
}

Response (proposed):
{
  "content_id": "unique_identifier",
  "status": "under_review",
  "message": "Your appeal has been recorded for review."
}
