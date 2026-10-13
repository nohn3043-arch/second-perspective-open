# Second-Perspective (GCAE) Specification

> **Document info**: Version 1.x (evolves with `SPE_VERSION`) | Status: passed IMDA AI Verify evaluation (total score 95) | Author: NOHN AI
> **Basis**: README-zh / ARCHITECTURE / TESTING-zh / GLOSSARY / language-standard 2026.1–2026.3
> 中文版本：[`SPECIFICATION-zh.md`](./SPECIFICATION-zh.md)
>
> This specification describes the public specification surface of the **GCAE Global Cognitive Audit Engine**: the ten-operator pipeline, the decision-structure language, states and signals, invariants and convergence semantics. The engine kernel is a single-file implementation (6496 lines, no `plugins/` package); core logic is a confidential deliverable.

## 1. Scope and Positioning

### 1.1 Positioning

A neutral, core-offline, decision-independent cognitive-bias audit engine: provides **third-party structural auditing** for AI systems and enterprise decisions, without offering suggestions, rankings or scores.

### 1.2 Non-goals

- Does not detect "bias": no statistical fairness testing, no group-difference measurement, no training-data audit;
- Does not make the model error-free; does not make medical / legal / financial / security professional judgements; does not handle runtime safety;
- Does not turn unsolvable into solvable; `AWAITING_HUMAN` is the norm, the engine never autonomously generates fixes.

## 2. Terms and Definitions

| Term | Definition |
|---|---|
| GCAE | Global Cognitive Audit Engine |
| Ten operators | ⊙GA→⊗NS→⊕IAP→⊿LCH→⊞LFT→BFC→⚙CCS→⇄GRF→META→⊚ACC, order uniquely defined by `PIPELINE_ORDER` |
| BFC | Binary Fact Check, binary fact verification, **no third truth value** |
| META | Meta-causal ledger: five meta-bases 混沌 / 无极 / 虚幻 / 天道 / 轮回 (chaos / wuji / illusion / heaven-tao / samsara) |
| `.spd` | Decision-structure language (`decision.ebnf`, ISO/IEC 14977) |
| `.tpg` | Topology language (`topology.ebnf`, grammar extension 2026.3) |
| ΔD | Observable-metric change of a decision; causal semantics `¬A ⇒ ΔD` |
| Audit certificate | SHA-256 hash chain, recomputable across machines |

## 3. Core Specification

### 3.1 Operator Pipeline

- Ten operators execute in `PIPELINE_ORDER` order; the semantic-topology base runs four classes of parallel validation (□ / → / ⦿ / △ / ◇).
- Orchestration semantics:
  - `reconstruct()`: linear coverage;
  - `spiral()`: superimposed spiral, freezes converged sub-graphs;
  - `limit_reconstruct()`: infinite convergence to S∞ = S*;
  - `evolve()`: proposes only, not autonomous.

### 3.2 Extension API

- Sole extension entry `register_operator()`, four gates: ASCII name not colliding with official operators; permission layer limited to `T2_SIGNAL` / `T3_NARRATIVE`; `after` required; `_register()` is the convergence point.
- `report['operator_manifest']` and `operator_set_hash` participate in the hash chain.

### 3.3 Decision-Structure Language

- `.spd`: decision-structure language (`decision.ebnf`, ISO/IEC 14977); `.tpg`: topology language (`topology.ebnf`, 2026.3).
- Validator `dsl.py`: subcommands `check / gen / codes`, 20 diagnostic codes.
- Topology-layer diagnostic codes T101–T308: T303 causal paradox, T305 fork, T307 order inversion, T308 order unassignable.

### 3.4 States and Signals

- Decision-context input fields: origin / goal / resources / decision / assumptions / outcome / dependencies / branches / facts / observations / gray_levels / commit_ratio / feedback.
- States and signals: `BLOCKED`, `SKIPPED`, `VERDICT_UNDECLARED`, `AWAITING_HUMAN`, `EVIDENCE_VACUUM`, `ORIGIN_DRIFT`, `SUPERPOSITION_VIOLATION`, `BUDGET_EXHAUSTED`, `LIMIT_REACHED` / `FLAT_SPIRAL` / `NOT_MONOTONE`.

### 3.5 Convergence Semantics

- Convergence rank = lexicographic (risk-set size, whether there is a pending assumption).
- Halting-criterion parameter thresholds: `limit_layers >= 2`, `plateau_layers >= 1`, `is_static` fixed at 3 layers.
- Five convergence states C-1..C-3 defined in the TESTING document (five states: true convergence / non-convergence judgement).

### 3.6 Invariants

- I-1..I-6: non-guessing / origin-no-drift / superposition-no-overwrite / time-not-strippable / evolution-not-autonomous / metric-not-blocking.
- L-1..L-3: LLM three-tier permission T1 (labelling) / T2 (proposal) / T3 (narrative), **never adjudicates**.
- `AWAITING_HUMAN` is the norm; META never blocks; external operators must not emit `BLOCKED`.

## 4. Boundaries and Prohibitions

- `binary=None` only means undeclared, never a third truth value.
- Does not give fixes, does not re-rank alternatives, does not flip assumption states.
- LLM augmentation off by default; enabling requires a domestic endpoint + desensitisation + consent.

## 5. Audit and Compliance

- IMDA AI Verify evaluation 95 points (causal-audit track).
- Reproducible certificate: same input + same nonce + same clock → same chain root, independent of any model vendor.
- V3b WARN: the certificate does not bind the original input; the coverage scope must be actively declared.
- Hash-chain event types, 10 kinds (AUDIT / DELTA_APPLIED, etc.); hash input includes the event index idx; changing event count / order invalidates it.
- Clean-room statement: presumed substantial-derivative infringement.
- Test methodology v1.0: Wilson 95% CI, exact McNemar, Cohen's κ ≥ 0.70, Hollow rate > 20% → HALT.

## 6. Conformance Statement

An implementation conforming to this specification should satisfy:

1. Pipeline order consistent with `PIPELINE_ORDER`, ten-operator semantics consistent with §3.1;
2. `.spd` / `.tpg` parsing consistent with `dsl.py` validator output (20 diagnostic codes);
3. All I-1..I-6 and L-1..L-3 invariants hold;
4. Audit certificate recomputable across machines (same input → same chain root).

## 7. Version and Changes

- `SPE_VERSION` 1.2.1; chain root `ca07e5e4…` (effective after the 1.2.1 generational change, replacing 1.2.0's `aece60f5…`).
- Language standard: 2026.1 (five operators) / 2026.2 (topology) / 2026.3 (meta-causal).
- `CognitiveAuditEngine` retained as an alias (v1 compatible).

## 8. License and References

- Non-open dual-track license: free for personal non-commercial research; government / enterprise require a written paid license.
- References: README-zh / ARCHITECTURE / TESTING-zh / GLOSSARY / `language-standard/` (grammar, decision.ebnf, topology.ebnf, dsl.py, examples).
