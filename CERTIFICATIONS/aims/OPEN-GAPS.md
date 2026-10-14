# Open Gaps and Nonconformities — Clauses 10.1 / 10.2

> Published deliberately. An unlisted gap is an unobservable risk; a listed one can be closed.
> **Severity** is the consequence if the gap is discovered by an external auditor rather than by us.

| Legend | |
|---|---|
| **High** | Blocks an external claim or invalidates historical evidence |
| **Medium** | Weakens a claim; survivable if disclosed |
| **Low** | Housekeeping |

---

| ID | Gap | Clauses | Severity | Compensating control | Owner | Target |
|---|---|---|---|---|---|---|
| **G-01** | **Cross-version chain-root comparison (V18) not implemented.** `verify.py` verifies same-version reproducibility only. An engine upgrade can invalidate all historical roots without any check failing. | 7.5, 9.1 | **High** | Every record stores `engine_version` + `operator_set_hash` + `pipeline_order` + `input_digest` (mandatory, see `AUDIT-RECORD-TEMPLATE.md`); manual re-verification on upgrade | `eng-01` | Before any external commitment |
| **G-02** | **`OpenAIProvider` / `AuditConfigLoader` unverified** (~62 lines; one self-reference each, zero coverage in `verify.py`). If enabled, data leaves the machine — contradicting the "core offline" claim. | 8.4, 8.5 | Medium | Excluded from the AIMS scope; off by default; any use must be declared in the record | `eng-01` | Smoke test or removal |
| **G-03** | **No independent third-party verification of the engine.** Correctness is self-attested by `verify.py`, which we wrote. | 9.2 | Medium | Engine-free evidence package published for external recomputation: `second-perspective-verify/evidence/` (`recompute.py --tamper`) | `audit-01` | When a certification path is chosen |
| **G-04** | **No statistical fairness / bias measurement.** `bias_metrics` implements B1 only — an upstream *declaration* gate for provenance and representativeness. B2 (demographic parity / equalised odds / subgroup slices) is not implemented and needs protected-attribute data plus its own compliance basis. | 6.1, 8.3, 8.5 | Medium | Explicit non-claims: never represent the engine as covering ISO/IEC TR 24027, NYC LL 144, or any bias-audit obligation | `founder-01` | Accepted limitation |
| **G-05** | **Change-management documentation incomplete.** Per invariant `I-5`, registering a new operator changes the chain root, so a routine extension silently breaks reproducibility. | 6.3, 10.2 | Medium | `lineage` generation tracking; change authority fixed in `AI-POLICY.md` §3; version binding in every record | `eng-01` | Before v1.3 |
| **G-06** | **Licence key rotation is a pre-release blocker.** Signing keys must be finalised before public release; rotation invalidates every issued licence. | 8.6 | **High** | Pre-release checklist item; never treat key generation as a post-release task | `eng-01` | Before first commercial release |
| **G-07** | **Clause 7 not established.** Resource allocation, competence, training and awareness records do not exist. | 7.1–7.3 | Medium | None — this is a genuine gap, not a documentation lag | `founder-01` | Next quarter |
| **G-08** | **No ISO/IEC 42001 certification, and none sought.** | all | — | Status declared at the top of `README.md` §0; must never be implied otherwise | `founder-01` | Decision pending |
| **G-09** | **Document-scope inconsistency.** `../compliance/COMPLIANCE_ISO_42001.md` is written for **NOMOS**, while this repository's trust layer is presented as belonging to the Second Perspective Engine (SPE) — two distinct products. | 4.3, 7.5 | Medium | Discrepancy recorded here rather than silently edited; resolution requires an owner decision on repository scope | `founder-01` | Next review |
| **G-10** | **Annex A control identifiers not verified against the standard text.** Numbering was omitted from `AIMS-CLAUSE-MAP.md` rather than guessed. | 4–10 | Low | Control areas named in prose only; numbers must be checked against the purchased standard before any external submission | `audit-01` | Before external use |

---

## Closed gaps

_None yet. A gap moves here only when its closure has a date, an owner and evidence._

## Notes on honest disclosure

Two of the entries above (G-04, G-08) are **permanent limitations, not defects**. They are listed
anyway, because an auditor who finds them before we disclose them will reasonably ask what else was
omitted. The cost of disclosure is a smaller claim; the cost of concealment is the whole claim.

---

## Change history

| Date | Change |
|---|---|
| 2026-10-15 | Initial register, ten gaps |
| 2026-10-15 | Corrected the Clause-8.6 gap reference; recorded that all deployments are on-premise, so no DPA is required |
