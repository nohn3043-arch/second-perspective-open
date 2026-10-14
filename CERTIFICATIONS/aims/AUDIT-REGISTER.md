# Audit Register — Clauses 9.2 / 9.3

> Running register of engine runs on real decisions. Primary input to internal audit and management
> review. One row per record; full records follow [`AUDIT-RECORD-TEMPLATE.md`](./AUDIT-RECORD-TEMPLATE.md).

**Status:** 🔧 no records yet. The three rows below are **illustrative examples** (`record_id`
prefixed `EX-`) showing the intended shape — they are not real runs and must be deleted or replaced
at the first real entry.

---

## Register

| record_id | date | type | subject (redacted) | clauses | engine_version | chain_root (short) | terminal_state | reviewed_by |
|---|---|---|---|---|---|---|---|---|
| `EX-001` | — | `DECISION` | `market-entry-APAC` | 6.1, 8.3 | — | — | — | — |
| `EX-002` | — | `DECISION` | `operator-addition-review` | 6.3, 10.2 | — | — | — | — |
| `EX-003` | — | `SELF_AUDIT` | `aims-document-set` | 9.2 | — | — | — | — |
| _(next)_ | | | | | | | | |

---

## Suggested first real runs

Drawn from decisions the organisation is actually making; each maps cleanly onto a clause and
produces evidence that would otherwise be written by hand.

| # | Decision | Clauses | Why it earns its place |
|---|---|---|---|
| 1 | Year-2 market entry (Japan) | 6.1, 8.3 | A real strategic decision with real assumptions; the assumption register is the risk register |
| 2 | Residency / funding application | 6.1, 9.3 | External scrutiny; the interruption list is the honest part of the application |
| 3 | Whether to register a new operator | 6.3, 10.2 | Directly exercises `I-5` and the chain-root consequence |
| 4 | Dual-entity cross-border data handling | 8.5, 8.6 | Forces the data-flow question into the open |
| 5 | Pricing model | 6.1 | Fragility analysis on revenue assumptions |

## Quarterly self-audit

The AIMS document set in this folder is itself fed into the engine as a `decision_context`. The
implicit-assumption list it returns **is** the internal audit finding.

| Quarter | Performed by | Findings | Actions | Status |
|---|---|---|---|---|
| 2026-Q4 | `audit-01` | _pending_ | _pending_ | ⬜ |

## Management review

| Date | Participants | Inputs reviewed | Decisions | Status |
|---|---|---|---|---|
| _pending_ | `founder-01`, `founder-02`, `founder-03` | Register · [`OPEN-GAPS.md`](./OPEN-GAPS.md) · clause map | — | ⬜ |

> A management review with no recorded decision is not a management review. If the first review
> produces only "continue", record that — the absence of change is itself a decision and must be
> traceable.

---

## Change history

| Date | Change |
|---|---|
| 2026-10-15 | Register created; three illustrative rows, no real records |
