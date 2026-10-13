# NOMOS Specification

> **Document info**: Version v0.5.0 (2026-10-07) | Status: enterprise control plane delivered | Author: NOHN AI
> **Basis**: README-zh / GLOSSARY / CHANGELOG / IMDA_AI_Verify_Causal_Audit_Report
> 中文版本：[`SPECIFICATION-zh.md`](./SPECIFICATION-zh.md)
>
> This specification describes the public specification surface of the **NOMOS second-order causal decision framework** — an auditable deterministic decision kernel with LLM guardrails: REST interface, second-order causal semantics, invariants, human gate and hash-chain report. The engine never outputs a final conclusion — the conclusion is signed by a human.

## 1. Scope and Positioning

### 1.1 Positioning

A **deterministic decision kernel** embedded behind existing ERP / CRM / risk-control / compliance / investment-decision / HR systems; it unifies structured evaluation, fine-grained algorithmic auditing, declarative assumption interaction (second-order causal composition), bounded three-layer reconstruction, counterfactual re-selection, stress testing, cognitive challenge, information ranking and human governance into a single hash-chain report.

### 1.2 Non-goals

- Does not output a final conclusion (the conclusion is signed by a human);
- The engine never estimates missing interaction strength, weights, probabilities or responsible parties;
- LLM never adjudicates; the cognitive scanner does not diagnose people, does not read motives, and does not replace legal, medical, financial or security professionals;
- Domain control packs only observe, never tamper with engine conclusions.

## 2. Terms and Definitions

| Term | Definition |
|---|---|
| First-order failure | Failure caused by a single factor |
| Second-order interaction | Two-factor combined effect: conjunctive (Δ>0) / disjunctive (Δ<0) / degenerate (Δ=0) |
| Δ interaction strength | Must be **explicitly declared** by the responsible party; the engine never estimates or learns it |
| Three-layer causal reconstruction | Bounded formal reconstruction, with deterministic convergence proof |
| DeltaVar | Assumption-rewrite path, three forms: `"A2"` / `"criteria.K1.weight"` / `"alternatives.S1.metrics.cost"` |
| LLM Gate | T1 labelling / T2 proposal / T3 narrative, never adjudicates |
| session_root_hash | Hash-chain root of a single analysis session |

## 3. Core Specification

### 3.1 REST Interface (v0.5)

| Endpoint | Method | Description |
|---|---|---|
| `/health` | GET | Health check |
| `/v1/auth/me` | GET | Current principal |
| `/v1/hub/analyze` | POST | Session analysis |
| `/v1/hub/reports/{hub_run_id}` | GET | Session report |
| `/v1/decisions/evaluate` | POST | Decision evaluation |
| `/v1/decisions/{decision_id}` | GET | Decision detail |
| `/v1/decisions/{decision_id}/approval` | POST | Human-approval gate |
| `/v1/decisions/{id}/history` | GET | Decision history |
| `/v1/metrics` | GET | Metrics |

### 3.2 Authentication and Context

- Auth: `Authorization: Bearer <SP_API_KEY>`.
- Tenant context: `X-Tenant-Id` (or OIDC `tid`).
- Response headers: `X-Nomos-Kms-Signature`, `X-Process-Time-Ms`.
- Environment variables: `SP_ENV`, `SP_API_KEY`, `SP_DATABASE_DSN`, `SP_OIDC_ISSUER`, `SP_AUTHZ_ENFORCE`, `SP_KMS_SECRET`, `SP_RATE_LIMIT`, `SP_PUBLIC_BASE_URL`.

### 3.3 Second-Order Causal Semantics

- Interaction declaration: `DecisionRequest.interaction_declaration` (optional, default None, backward compatible). When not provided, behaviour is identical to v0.4.
- Invariants I-1..I-4: non-speculation / order conservation / bounded effect / monotonic.
- I-3 bounded effect: cumulative interaction effect ≤ `amplification_ceiling` × Σ|first-order|; redundant (negative) interactions are not lower-clamped.
- Five convergence states: `FIXED_POINT` / `NO_GAIN` are true convergence; `BUDGET_EXHAUSTED` / `DIVERGED` / `BLOCKED` are non-convergence. `BUDGET_EXHAUSTED` must be reported as non-convergence (`is_true_convergence` guards against misjudgement).

### 3.4 Human Gate

- `advance()` executes exactly one round then stops at `AWAITING_HUMAN`.
- T2 proposals require explicit human approval to take effect; T3 narrative is stripped from the decision graph; no LLM output may flip an assumption state or alternative ranking.

### 3.5 Audit and Reporting

- Hash-chain algorithmic audit + append-only `DomainEvent` event stream (`InMemoryEventStore` / `PostgresEventStore`) + append-only `DecisionRecord`.
- KMS-separated HMAC-SHA256 signing (transparent no-op before configuration).
- Response fields: `counterfactuals`, `algorithm_audit`, `algorithm_audit_root_hash`.

## 4. Boundaries and Prohibitions

- LLM never adjudicates (three fences: T2 human approval / T3 stripping / output must not flip state or ranking).
- All v0.5 new capabilities are environment-variable gated, off by default.
- Domain control packs only observe, never tamper with engine conclusions.
- The cognitive scanner only challenges **structural risk**.

## 5. Audit and Compliance

- IMDA AI Verify: 95/100 (causal-audit track), audit report `IMDA_AI_Verify_Causal_Audit_Report.pdf`.
- Compliance documents: PRC (Shanghai compliance note, privacy policy CN, data-processing agreement CN); international (EU AI Act, GDPR, Singapore PDPA); framework alignment (NIST AI RMF 1.0, ISO/IEC 42001:2023).

## 6. Conformance Statement

An implementation conforming to this specification should satisfy:

1. Endpoints / auth / context semantics consistent with §3.1–§3.2;
2. Interaction declaration validated by I-1..I-4; when no interaction declared, behaviour equals v0.4;
3. Human-gate semantics: no LLM output may flip any state or ranking;
4. Hash-chain report verifiable, event stream append-only.

## 7. Version and Changes

- v0.5.0 (2026-10-07): enterprise control plane; v0.4.0 (2026-09-22): second-order causal framework; v0.3.0 (2026-09-19).
- Follows SemVer and Keep a Changelog; tests: 402 passed 0 failed (at v0.4 release), now 412 passed.
- Production-hardening TODO (unbundled): shared rate-limit store, cloud KMS envelope encryption, document-level tenant partitioning, multi-region HA, SLA tooling.

## 8. License and References

- Non-open dual-track license: within China → Shanghai Linming Junhua Technology Co., Ltd. + PRC law; outside China → NOHN AI TECHNOLOGY PTE. LTD. + Singapore law + SIAC arbitration.
- References: README-zh / GLOSSARY / CHANGELOG / `export_openapi.py` (OpenAPI schema export).
