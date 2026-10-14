# AIMS Scope — Clause 4 (Context of the Organisation)

> Status: 🔧 draft, self-declared, unaudited. Scope decided 2026-10-15 (see change history).

---

## 4.1 Understanding the organisation

| Item | Value |
|---|---|
| Legal entities in scope | **NOHN AI TECHNOLOGY PTE. LTD.** (Singapore, UEN 202624632Z) · **Shanghai Linming Junhua Technology Co., Ltd.** (PRC) |
| AIMS governing entity | **NOHN AI TECHNOLOGY PTE. LTD.** (Singapore) — the AIMS is legally anchored here. Shanghai Linming Junhua Technology Co., Ltd. participates as a controlled affiliate, not as the governing entity |
| Headcount in scope | 3 (founding team) |
| Nature of activity | Design, development and licensed delivery of causal-audit and deterministic decision software |
| Operating jurisdictions | Singapore · PRC (Shanghai) · target: Japan (Year 2), EU, US |

## 4.2 Needs and expectations of interested parties

| Interested party | Expectation | How it is met | Evidence |
|---|---|---|---|
| Enterprise / government customers | Auditable, reproducible decision evidence for their own AIMS | Engine output + evidence package | `second-perspective-verify/evidence/` |
| Accredited certification bodies | Verifiable, non-overstated claims | Published gap register | [`OPEN-GAPS.md`](./OPEN-GAPS.md) |
| Regulators (IMDA Singapore; PRC CAC / TC260; EU market authorities) | Lawful data handling, human oversight, traceability | Core-offline design; human-in-the-loop invariants | `AI-POLICY.md`; `../compliance/COMPLIANCE_SHANGHAI.md` |
| Investors / residency programme (Antler) | Governance maturity proportionate to stage | This AIMS | this folder |
| Individual researchers | Free non-commercial use with attribution | Tiered licence | `../../LICENSE` |

## 4.3 Scope of the AIMS

**In scope** — AI systems and AI-enabled products designed or operated by NOHN AI:

| System | Role | In scope from |
|---|---|---|
| Second Perspective Engine (SPE) | AI decision control infrastructure, independent of AI providers — acts at the decision-execution boundary, upstream of actuation | 2026-10 |

**Not in scope (decided 2026-10-15).** Explicitly excluded from this AIMS at this stage:

| System | Status |
|---|---|
| NOMOS Intelligent Decision Hub | Not in scope — separate product, separate governance |
| Anthropomorphic Agent Engine (SPL Pure Core) | Not in scope |
| SPL-G1 (hardware TCU) | Not in scope |

Adding any of them later is a scope revision (Clause 4.3 / 6.3) and requires the self-audit to be
re-run before the change may be claimed as covered.

**Boundary — read this carefully.** The AIMS covers **NOHN AI's own** development and operation of
AI systems. It does **not** extend to:

- A customer's own AIMS. Each deploying organisation remains responsible for its own policy, roles,
  internal audit and management review — the engine supplies technical controls and evidence, never
  the management-system layer.
- Certification of any product. See the status box in [`README.md`](./README.md) §0.
- Runtime safety domains the engine explicitly disclaims (flight control, dispatch commands, network
  defence, clinical decision-making).

## 4.4 AIMS processes

| Process | Mechanism | Clause |
|---|---|---|
| Decision audit | `engine.audit()` — ten operators, fixed `PIPELINE_ORDER` | 8.1, 8.3 |
| Risk and assumption register | ⊕IAP + ⊿LCH ΔD + ⚙CCS output | 6.1 |
| Measurement | META five ledgers (measure, never block) | 9.1 |
| Traceability | Hash chain + `operator_manifest` in `report_hash` | 7.5, 9.2 |
| Change and improvement | `evolve()` proposals (never self-applied) + `lineage` | 6.3, 10.2 |
| Self-audit | AIMS document set re-fed into the engine, quarterly | 9.2 |
| Management review | Quarterly review of `AUDIT-REGISTER.md` and `OPEN-GAPS.md` | 9.3 |

## 4.5 Exclusions

| Excluded | Reason |
|---|---|
| Third-party data processing | All deployments are on-premise; customer data never leaves the customer environment, so no DPA is required (Clause 8.6) |
| Hardware RTL (SPL-G1) | Out of AIMS scope since 2026-10-15; confidential deliverable, not published |
| Customer identities, contracts, pricing | Commercial confidentiality |
| Pending patent subject matter | Pre-publication |
| Engine source | Private implementation; this repository carries no implementation (see root `README.md`) |

---

## Change history

| Date | Change |
|---|---|
| 2026-10-15 | Initial scope statement |
| 2026-10-15 | Scope decided: AIMS anchored to the Singapore entity; NOMOS / Anthropomorphic Agent Engine / SPL-G1 explicitly out of scope; SPE repositioned as AI decision control infrastructure |
