# Clause Map — ISO/IEC 42001:2023 Clauses 4–10

> Status: 🔧 draft. **"Engine-produced" means the engine generates the evidence as a byproduct of a
> real run.** "Manual" means a human must write it. Nothing here is machine-verified.

**Legend** — ✅ engine-produced · 🔧 manual, compensating control exists · ⬜ not yet established

---

## ⚠️ On Annex A numbering

Annex A control identifiers are **not enumerated in this document**. Numbering must be checked
against the purchased standard text before any external submission; a mis-cited control number is
the kind of error that costs credibility in the first hour of an audit. Control **areas** are named
in prose below. This is a deliberate omission, tracked as `OPEN-GAPS.md` **G-10**.

---

## Clause 4 — Context of the organisation

| Requirement | Source | Status | Evidence |
|---|---|---|---|
| 4.1 Organisation | Manual | ✅ | [`AIMS-SCOPE.md`](./AIMS-SCOPE.md) §4.1 |
| 4.2 Interested parties | Manual | ✅ | [`AIMS-SCOPE.md`](./AIMS-SCOPE.md) §4.2 |
| 4.3 AIMS scope | Manual | ✅ | [`AIMS-SCOPE.md`](./AIMS-SCOPE.md) §4.3, §4.5 |
| 4.4 AIMS processes | Engine + manual | ✅ | [`AIMS-SCOPE.md`](./AIMS-SCOPE.md) §4.4; [`README.md`](./README.md) §4 |

## Clause 5 — Leadership

| Requirement | Source | Status | Evidence |
|---|---|---|---|
| 5.1 Leadership commitment | Manual | ✅ | [`AI-POLICY.md`](./AI-POLICY.md) §2 (accountable owner) |
| 5.2 AI policy | Manual, invariant-bound | ✅ | [`AI-POLICY.md`](./AI-POLICY.md) §1 — five articles |
| 5.3 Roles & responsibilities | Engine-enforced | ✅ | `ResponsibilityAccount` (org / role / stage / owner); empty owner → `BLOCKED` |

## Clause 6 — Planning

| Requirement | Source | Status | Evidence |
|---|---|---|---|
| 6.1 Risks & opportunities | **Engine-produced** | ✅ | ⊕IAP implicit assumptions · ⊿LCH ΔD collapse · ⚙CCS counterfactual & black-hole — a structural risk register, not a subjective score |
| 6.2 AI objectives | Manual | ✅ | [`AI-POLICY.md`](./AI-POLICY.md) §1 |
| 6.3 Changes to the AIMS | Engine-produced + manual | 🔧 | `evolve()` proposals + `lineage`; change authority in [`AI-POLICY.md`](./AI-POLICY.md) §3. **Gap G-05** |

## Clause 7 — Support

| Requirement | Source | Status | Evidence |
|---|---|---|---|
| 7.1 Resources | Manual | ⬜ | Not documented. **Gap G-07** |
| 7.2 Competence | Manual | ⬜ | Training records not established. **Gap G-07** |
| 7.3 Awareness | Manual | ⬜ | **Gap G-07** |
| 7.4 Communication | Manual | 🔧 | This repository is the communication channel; no internal communication procedure documented |
| 7.5 Documented information | **Engine-produced** | ✅ | Hash chain; `input_digest` bound into the certificate; `operator_manifest` inside `report_hash` |

## Clause 8 — Operation

| Requirement | Source | Status | Evidence |
|---|---|---|---|
| 8.1 Operational planning & control | Engine-produced | ✅ | Deterministic, declared inputs only; `PIPELINE_ORDER` fixed |
| 8.2 AI risk treatment | Engine-produced | ✅ | ⊞LFT four parallel checks (fatal / void severity classes); ⇄GRF fallback-path ΔD |
| 8.3 AI system impact assessment | **Engine-produced** | ✅ | Full audit output = impact assessment record (aligned to ISO/IEC 42005:2025). **Boundary: no statistical fairness assessment — Gap G-04** |
| 8.4 AI system lifecycle | **Engine-produced** | ✅ | BFC binary fact check (no third truth value); ⊞LFT verification. **Gap G-02** (LLM provider path unverified) |
| 8.5 Data management | Engine-produced + manual | 🔧 | `bias_metrics` B1 upstream supply gate (provenance & representativeness as a **declaration**). **B2 not implemented — Gap G-04** |
| 8.6 Third-party relationships | Manual | ✅ | Tiered licence; **all deployments are on-premise** — no third-party data processing, therefore no DPA required |

## Clause 9 — Performance evaluation

| Requirement | Source | Status | Evidence |
|---|---|---|---|
| 9.1 Monitoring & measurement | **Engine-produced** | ✅ | META five ledgers — A6 narrative entropy, A10 audit entropy, gap ledger, parallel convergence, succession integrity. Measures; never adjudicates. |
| 9.2 Internal audit | **Engine-produced** | ✅ | Tamper-evident chain; quarterly **self-audit** (AIMS re-fed as input). **Gap G-03: no independent third-party verification** |
| 9.3 Management review | Manual | 🔧 | Quarterly review of [`AUDIT-REGISTER.md`](./AUDIT-REGISTER.md) + [`OPEN-GAPS.md`](./OPEN-GAPS.md). **Cadence not yet evidenced — first review pending** |

## Clause 10 — Improvement

| Requirement | Source | Status | Evidence |
|---|---|---|---|
| 10.1 Nonconformity & corrective action | Manual | ✅ | [`OPEN-GAPS.md`](./OPEN-GAPS.md) — each gap carries severity, compensating control and owner |
| 10.2 Continual improvement | **Engine-produced** | ✅ | `evolve()` emits candidate proposals; `lineage` records generation. Never self-applied (Art. 4) |

---

## Annex A control areas contributed to (prose, no numbering)

| Control area | Engine contribution |
|---|---|
| AI policy & governance | Policy bound to enforced invariants |
| Internal organisation | `ResponsibilityAccount` — accountability as a blocking precondition |
| AI risk management | Structural risk register: assumptions, ΔD, counterfactual, black holes |
| Impact assessment | Full audit output; no fairness statistics |
| AI system lifecycle | BFC + LFT verification and validation evidence |
| Data management | Upstream supply provenance gate (B1); no subgroup metrics |
| Third-party & customer responsibility | Tiered licence; engine cannot alter a customer's verdict |
| Transparency & information for interested parties | Bilingual reports; reproducible certificate |
| Record retention & traceability | `input_digest` → `report_hash` → `chain_root`; recomputable off-engine via `second-perspective-verify/evidence/` |
| Human oversight / controllability | `AWAITING_HUMAN` is the normal terminal state; `requires_human = True` |

## Areas the engine does **not** contribute to

Statistical fairness and bias metrics · model correctness · content safety · runtime safety ·
robustness or adversarial testing · clinical / legal / financial professional judgement.
Claiming any of these would be an overstatement — see [`README.md`](../README.md) capability
boundary and `OPEN-GAPS.md` **G-04**.

---

## Change history

| Date | Change |
|---|---|
| 2026-10-15 | Initial clause map |
