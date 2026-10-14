# AI Policy and Roles — Clauses 5.2 / 5.3

> Status: 🔧 draft. Five articles, each bound to an **enforced engine invariant**, not to an aspiration.
> A policy article that no mechanism enforces is a declaration, not a control.

---

## 1. AI Policy

### Article 1 — No guessing
Where a fact, weight, threshold, responsible person or interaction strength is missing, the system
**interrupts and lists what must be supplied**. It does not estimate, interpolate or default.

*Invariant:* `I-1` · *Engine behaviour:* `BLOCKED` +补齐条件清单 · *Clause:* 6.1, 8.2

### Article 2 — The origin does not drift
Once the origin event and target state are anchored, changing the target is detected and the run
halts. Optimising toward a silently replaced goal is treated as a defect, not as progress.

*Invariant:* `I-2` · *Engine behaviour:* `ORIGIN_DRIFT` → immediate halt · *Clause:* 8.1

### Article 3 — Superposition does not overwrite
A converged subgraph is frozen and may only grow. Reopening it is a violation.

*Invariant:* `I-3` · *Engine behaviour:* `SUPERPOSITION_VIOLATION` · *Clause:* 8.4

### Article 4 — The system does not evolve itself
Automated discovery may **propose**. It may never apply. Changing an adjudication rule is a human act.

*Invariant:* `I-5` · *Engine behaviour:* `applies_automatically = False` · `requires_human = True` ·
`auto_applied = 0` · *Clause:* 6.3, 10.2 · *External alignment:* EU AI Act Art. 14 (human oversight)

### Article 5 — Measurement never adjudicates, and no model ever adjudicates
Metrics — however bad — do not block. Only missing input blocks. Language models hold annotation,
proposal and narration permissions only; they never decide, never rank, never change state.

*Invariants:* `I-6`, `L-1`–`L-3` · *Engine behaviour:* META pinned to `T2_SIGNAL`; `FORBIDDEN_LLM_KEYS`
stripped recursively at any nesting depth · *Clause:* 9.1

---

## 2. Roles and responsibilities

Published with **codes only** (see `README.md` §5). Real names and employee identifiers are held in
the private register and are never published.

| Code | Role | Clause responsibility | Engine binding |
|---|---|---|---|
| `founder-01` | AIMS owner · accountable for the management system | 5.1, 9.3 | — |
| `founder-02` | Product / anthropomorphic engine line | 8.1 | `ResponsibilityAccount.role` |
| `founder-03` | Part-time; commercial and partnership governance | 4.2, 8.6 | — |
| `eng-01` | Engine owner · sole authority over adjudication-rule change (Art. 4) | 6.3, 8.4 | `engine_version`, `lineage` |
| `audit-01` | Internal audit execution · self-audit run, quarterly | 9.2 | `ResponsibilityAccount.stage = review` |
| `dpo-01` | Data protection contact (PRC + Singapore) | 8.5 | — |

**Single-point rule.** `ResponsibilityAccount.owner` must be non-empty. An empty owner is not a
warning — it raises `RESPONSIBILITY_CLOSURE` and blocks. Accountability is a structural
precondition, not a reporting field.

## 3. Authority over adjudication rules

| Change | Who may authorise | Mechanism |
|---|---|---|
| New operator registered | `eng-01` | `register_operator()` — four gates; external operators may never emit `BLOCKED` |
| Change to an adjudication rule | `eng-01` + `founder-01` | `approve_evolution_proposal()` records the generation bump; returns `applied_to_code = False` |
| Change to this policy | `founder-01` | Version bump in this file; re-run self-audit |

> ⚠️ Registering a new operator **changes the chain root** (consequence of `I-5`). Before any
> engine version change, open records must be re-verified — see `OPEN-GAPS.md` **G-01**.

## 4. Acknowledgement and awareness

All persons in scope acknowledge this policy. Record of acknowledgement is held privately; the
control itself is enforced structurally (Articles 1–5 are code invariants, so non-compliance is
either impossible or visible).

*Clause 7.2 / 7.3 — see `OPEN-GAPS.md` **G-07**: competence and training records not yet established.*

---

## Change history

| Date | Change | Authorised by |
|---|---|---|
| 2026-10-15 | Initial policy, five articles | `founder-01` |
