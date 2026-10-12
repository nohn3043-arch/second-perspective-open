# Story Engine Specification

> **Document info**: Version v2.2 (`engine_for_business.py`) | Status: robustness hardening complete (2026-08) | Author: NOHN AI
> **Basis**: README-zh / GLOSSARY
> 中文版本：[`SPECIFICATION-zh.md`](./SPECIFICATION-zh.md)
>
> This specification describes the public specification surface of **two products** in the repository: the **long-form narrative-consistency engine** for creators / the general public, and the **offline document-compliance review engine** for enterprises.

## 1. Scope and Positioning

### 1.1 Narrative-Consistency Engine (Creator)

Automatically audits character settings, causal timelines and memory lines (character / timeline / memory consistency), turning intuitive proofreading into a structured process.

### 1.2 Document-Compliance Review Engine (Business)

Performs clause-level rule scanning and document-level auditing on contracts, regulations, official documents and general text, outputting a traceable report. **Fully LLM-independent**: pure JSON rule library, zero third-party dependencies, runs offline.

## 2. Terms and Definitions

| Term | Definition |
|---|---|
| Consistency audit | Consistency audit (character / timeline / memory) |
| ResponsibilityAccount | Responsibility-closure anchor: each conclusion is tied to a named responsibility node (who / role / phase) |
| CausalNode | Causal node carrying `implicit_assumptions` and `vulnerability_score` |
| OOC | Out Of Character, character break |
| SPL four-stage | `STRIP_NARRATIVE → SCAN_ASSUMPTION → HEDGE_RISK → LOCK_RESPONSIBILITY` |
| RuleEngine / Hit=verdict | Rule engine: a hit is a verdict, no probabilistic output |
| TraceLog | Full-chain traceable log |

## 3. Core Specification

### 3.1 Narrative Editing Pipeline (SPL four-stage)

- `STRIP_NARRATIVE` (strip narrative) → `SCAN_ASSUMPTION` (scan assumptions) → `HEDGE_RISK` (hedge risk) → `LOCK_RESPONSIBILITY` (lock responsibility).
- Stages defined by the `SPLStage` enum.

### 3.2 Node States

- Five node states: `RAW / STRIPPED / AUDITED / PRUNED / ACTIVE`.

### 3.3 Compliance-Review Engine Interface (CLI)

- `python -m compliance_engine audit --type contract --input … --output …`
- `python -m compliance_engine list-rules`
- `python -m compliance_engine demo`
- External rule-library extension: `--rules-dir <dir>`; rule-library files `rules/*.json`, four categories: `contract / regulation / official_doc / common`.

### 3.4 Risk and Reporting

- Four risk levels: `SAFE / WARNING / CRITICAL / FATAL`.
- Three report formats: HTML / JSON / Markdown.
- Document-level audit four dimensions: element completeness / consistency / responsibility symmetry / format.

### 3.5 Engine Isolation

- `_ENGINE_FINGERPRINT` + `check_engine_isolation()`: mixing the two engines in the same process triggers an immediate warning, preventing same-name heterogeneous data classes from overwriting each other.

### 3.6 LLM Backend

- Replaceable LLM backend: `DeepSeekProvider` / `MockLLM`.

## 4. Boundaries and Prohibitions

- The enterprise branch does not depend on LLM, runs offline, deterministic verdict (hit = verdict, no probabilistic output).
- Name extraction "rather miss than noise": exclude pronouns / verb phrases / weather-scene words.
- Worldview extraction by longest-suffix whole-word matching; connectives are not swallowed.
- Fixes include full skip-word repair and full-text revision replacement (abrupt transition words: 突然 / 莫名 / 鬼使神差, etc.).

## 5. Audit and Compliance

- Responsibility-closure anchor: each conclusion traceable to a named responsibility node.
- TraceLog full-chain traceability: every judgement step can be traced back to its original basis.
- Document-level audit four dimensions + scoring.

## 6. Conformance Statement

An implementation conforming to this specification should satisfy:

1. The four-stage pipeline order and `SPLStage` semantics are consistent;
2. Rule-library format consistent with the `--rules-dir` protocol, hit = verdict;
3. Risk grading and report formats (HTML / JSON / Markdown) are consistent;
4. Engine-isolation detection is effective.

## 7. Version and Changes

- `engine_for_business.py` v2.2; robustness-hardening fixes (2026-08).
- Command entry points: `Story Engine for Creator.py`, `engine for business.py`.

## 8. License and References

- Non-open dual-track license: within China → Shanghai Linming Junhua Technology Co., Ltd.; outside China → NOHN AI TECHNOLOGY PTE. LTD., SIAC arbitration.
- References: README-zh / GLOSSARY / `rules/` (four rule-library categories).
