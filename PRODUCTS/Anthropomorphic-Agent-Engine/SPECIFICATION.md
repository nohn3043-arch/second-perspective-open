# Anthropomorphic-Agent-Engine Specification

> **Document info**: Version SPL Pure Core V8.0 | Status: kernel stable; minor-protection variant compliance in progress | Author: NOHN AI
> **Basis**: README-zh / GLOSSARY / `docs/agent-standard.md` (interoceptive-vector contract §4.1, §4.5)
> 中文版本：[`SPECIFICATION-zh.md`](./SPECIFICATION-zh.md)
>
> This specification describes the public specification surface of a **deterministic anthropomorphic psychological engine**: the interoceptive-vector contract, the eight-dimensional emotion fluid, clock and reproducibility, and the minor-protection variant.

## 1. Scope and Positioning

### 1.1 Positioning

A **deterministic anthropomorphic psychological engine** built on SPL Pure Core V8.0: it models emotion, mood, memory, trauma, trust, self-esteem, sleep and expectation as deterministic continuous-state subsystems within a single kernel (`SPL-anthropic-engine.py`). **No LLM, no randomness, fully bitwise replayable** (prerequisite: injected virtual clock).

### 1.2 Core Design Goals

- Eight-dimensional emotion fluid: joy / anger / fear / trust / detachment / tension / guilt / shame;
- V8.0 extensions: slow-variable mood layer, independent shame dimension, self-esteem dynamics, sleep / dreams (REM consolidation + fear extinction + sleep debt), expectation system (hope / anxiety / disappointment), cognitive dissonance, extended defence mechanisms;
- Token metering (`TokenUsage` / `TokenStats`, JSON export) + `AuditLogger` automatically records every LLM call.

## 2. Terms and Definitions

| Term | Definition |
|---|---|
| SPL pure kernel | Randomness-free, replayable deterministic kernel |
| Interoceptive vector | The engine's input-contract vector (see `docs/agent-standard.md` §4.1) |
| Virtual clock | Prerequisite for reproducibility; falls back to `time.time()` if not injected |
| Trauma reconsolidation | Iteration-driven weakening mechanism of traumatic memory |
| Trust-ceiling erosion | Negative clamping of the trust dimension |
| L0–L3 | Four-layer minor-protection guard |

## 3. Core Specification

### 3.1 Kernel Interface

- The core file is a library, no `__main__`; must be loaded via `importlib`.
- `SPLPureCoreV7_3().process_vector({...}, time)`: advance state;
- `core.snapshot()`: state snapshot;
- `core.set_clock(t)`: inject virtual clock;
- `NarrativeMapper.map_event("insult", intensity=1.0)`: event mapping;
- Interoceptive-vector contract: see `docs/agent-standard.md` §4.1.

### 3.2 Reproducibility

- **"Fully replayable" holds only after a virtual clock is injected**; without injection it falls back to `time.time()`.
- Any reproducibility claim must state this prerequisite; `tests/` S1–S4 assertions include reverse tests (non-reproducibility under the natural clock is expected behaviour).

### 3.3 Minor-Protection Variant

- Mechanism-level risk reduction + four-layer protection L0–L3, zero third-party dependencies:
  - L0 age verification + guardian consent;
  - L1 input gating (red-line keyword library → `gate_crisis`);
  - L2 engine mitigation;
  - L3 crisis signal (`protective.risk_level == HIGH` → caring script + guardian notification + webhook + referral statistics).
- API (default `http://localhost:8788`): `/api/chat`, `/api/consent`, `/api/guardian/register`, `/api/guardian/block`, `/api/state`, `/api/export`, `/api/delete`, `/api/logout`, `/api/terms`, `/api/referrals`, `/api/complain`.
- Environment variables: `SPL_MINOR_CRISIS_HOTLINE` (default 12356), `AI_DISCLOSE_INTERVAL` (default 3600).
- Differences from the main engine: trauma removal; shame-erosion gain ×0.4 (threshold raised to 0.7); negative clamp 0.75; attachment / trust ceiling 0.8; self-esteem floor 0.15; personality excludes intimacy / antagonism classes.

## 4. Boundaries and Prohibitions

- `feature-guide/` extension modules (Goal / Identity / bias / value / world) are not wired into the kernel; their `tension_base` key is outside the interoceptive-vector contract (spec §4.5).
- The minor variant's age / guardian consent is self-reported + declared, without authoritative verification.
- Pre-deployment obligations: legal review, DPIA / security assessment / algorithm filing, integration of real guardian notification and crisis resources.

## 5. Audit and Compliance

- Runtime audit log: `logs/` JSONL (.gitignore).
- Minor-protection compliance checklist mapped by clause / jurisdiction: COPPA, EU Measures Art. 8–21, GDPR Art. 17, CA SB 243, etc.
- IMDA AI Verify causal-audit report: `IMDA_AI_Verify_Causal_Audit_Report.pdf` (repo root).
- Dual-track license: personal non-commercial free; government / enterprise paid; evaluation use 60-day exception (LICENSE clause 1.3).

## 6. Conformance Statement

An implementation conforming to this specification should satisfy:

1. Interoceptive-vector contract consistent with `docs/agent-standard.md` §4.1;
2. Bitwise replayable once a virtual clock is injected; explicit fallback semantics if not injected;
3. Minor variant's four-layer protection L0–L3 and differential parameters (§3.3) consistent;
4. Audit log append-only and traceable.

## 7. Version and Changes

- SPL Pure Core V8.0 (class name `SPLPureCoreV7_3`).
- PyPI package `spl-agent-engine`: latest 0.4.0 (2026-09-02), not tracking the repo source; 0.4.1 not uploaded.
- Online demo: www.nohnlins.com/your-soulmate/.

## 8. License and References

- Non-open dual-track license: free for personal non-commercial research; written paid license for government / enterprise.
- References: README-zh / GLOSSARY / `docs/agent-standard.md` / LICENSE (clause 1.3 evaluation exception).
