# Audit Record Template — Clauses 7.5 / 9.1

> One record per engine run on a real decision. If a run has no record, it did not happen as far as
> the AIMS is concerned.

---

## ⚠️ Mandatory chain-of-custody fields (read before filling this in)

Cross-version chain-root comparison (**V18**) is **not implemented** — see
[`OPEN-GAPS.md`](./OPEN-GAPS.md) **G-01**. `verify.py` checks that three runs of the *same* version
agree; it does **not** check that a *new* version reproduces an *old* root.

Consequence: **an engine upgrade can silently invalidate every historical record.** Until V18 ships,
the following four fields are the compensating control and are **not optional**:

| Field | Why it is mandatory |
|---|---|
| `engine_version` | A chain root is meaningless without the version that produced it |
| `operator_set_hash` | The root depends on the operator set; recomputation requires it |
| `pipeline_order` | Order participates in the hash |
| `input_digest` | Binds this certificate to *this* input |

**On upgrade:** re-verify open records against the new version and record the outcome
(`REPRODUCED` / `NOT_REPRODUCED`) in `AUDIT-REGISTER.md`. A `NOT_REPRODUCED` result is a
nonconformity under Clause 10.1 and goes into `OPEN-GAPS.md`.

---

## Template

```yaml
record_id:            AUD-YYYY-NNN
date:                 YYYY-MM-DD
record_type:          DECISION | SELF_AUDIT | MANAGEMENT_REVIEW | CHANGE_REVIEW

# --- subject (redacted) ---
subject_descriptor:   "market-entry-APAC"      # descriptor only; never the decision text
clause_refs:          [6.1, 8.3]               # ISO/IEC 42001 clauses this record evidences

# --- responsibility (codes only) ---
account:
  organization:       nohnai
  role:               founder
  stage:              review
  owner:              founder-01               # code only — no names, no employee IDs

# --- chain of custody (mandatory, see above) ---
engine_version:       SPE 1.2.1
operator_set_hash:    <hex>
pipeline_order:       [GA, NS, IAP, LCH, LFT, BFC, CCS, GRF, META, ACC]
input_digest:         <sha256 of canonical-JSON input>
report_hash:          <hex>
chain_root:           <hex>

# --- outcome ---
terminal_state:       BLOCKED | AWAITING_HUMAN | CONVERGED | LIMIT_REACHED |
                      FLAT_SPIRAL | NOT_MONOTONE | ORIGIN_DRIFT | SUPERPOSITION_VIOLATION |
                      BUDGET_EXHAUSTED
signals:              [EVIDENCE_VACUUM, ...]   # verbatim; do not paraphrase
delta_d_items:        <count>                  # fragile assumptions scored

# --- follow-up ---
actions:              [ ... ]                  # what a human must supply or decide
reviewed_by:          founder-01
review_date:          YYYY-MM-DD
```

---

## What makes a record admissible

| Rule | Reason |
|---|---|
| Hashes published in full | Redaction applies to *content*, never to *evidence* |
| `terminal_state` copied verbatim | Paraphrasing a verdict is how "blocked" becomes "passed" |
| `actions` must be non-empty when `terminal_state` is `BLOCKED` or `AWAITING_HUMAN` | An interruption with no listed remedy is not an audit result |
| `reviewed_by` must differ from the decision owner where possible | Segregation of duties |

## What must never appear in a published record

Customer names · pricing or financial figures · real personal names or employee identifiers ·
undisclosed patent subject matter · the raw decision text · anything whose publication would breach
an NDA.

---

## Change history

| Date | Change |
|---|---|
| 2026-10-15 | Initial template; chain-of-custody section added as G-01 compensating control |
