# Anthropomorphic Agent Engine (AAE) — Specification

> **Document info**: Version 1.0 (draft) | Status: Draft for evaluation | Prepared by NOHN AI TECHNOLOGY PTE. LTD.
> **Basis**: the engine data contract (`docs/agent-standard.md`) and acceptance methodology (`docs/EVALUATION.md`); both are implementation-layer documents and are not in this public repository.
>
> **This specification describes the interface contract surface only**: input contract, state contract, engine entry points, audit contract, and determinism preconditions. Dynamic coefficients, tuning rationale, and source-level identifiers are confidential deliverables and are not described here — a specification answers "what must hold", not "how we tuned it".
>
> **This specification contains no implementation.** A conforming implementation MAY be written independently by any party. No usage rights are granted; see [`LICENSE`](../LICENSE).
>
> 中文版本：[`SPECIFICATION-zh.md`](./SPECIFICATION-zh.md)

---

## 1. Scope and Positioning

### 1.1 Positioning

**AAE is the continuous inner-state layer of an AI character.**

It models emotion, mood, memory, trauma, trust, self-esteem, sleep, and anticipation as a **deterministic continuous-state subsystem**, providing three properties:

| Property | Statement |
|---|---|
| Continuous | The character does not forget, drift, or lose thread across long interactions |
| Deterministic | Identical declared inputs produce identical state; the core has no randomness and no LLM calls |
| Replayable | Every state transition carries an attribution `delta`; the audit chain is recomputable across machines |

**Deployment shape**: AAE is not part of model weights. It runs as a **state-layer sidecar** of the dialogue system:

```
event → AAE core → state snapshot + style directive → injected into LLM prompt → utterance
```

It is therefore model-vendor independent: a character's state snapshot can migrate between GPT / Claude / domestic vendors without the personality breaking.

### 1.2 Variants

| Variant | Tag | Target scenario |
|---|---|---|
| Main engine | **[main]** | General dialogue assistant, emotional companionship, game NPC |
| Minor variant | **[minor]** | Products for minors; mechanism-level risk reduction (see §4.6) |

### 1.3 What it is not

- **Not an utterance generator** — utterances come from the downstream LLM; AAE supplies internal state and style directives only.
- **Not psychological diagnosis** — it borrows psychological constructs but outputs behavioural consistency constraints, not assessments of real people.
- **Not a safety filter** — the minor variant's protection is **mechanism-level reduction** (no trauma modelling, no defense compartment), not output-side keyword filtering.
- **No claim of behavioural correctness** — conformance tests prove "behaviour has not drifted", not "the psychological conclusions are right" (see §9.2).

---

## 2. Terminology

| Term | Definition |
|---|---|
| AAE | Anthropomorphic Agent Engine |
| Interoceptive vector | An event's felt expression inside the character, 5 fields (§3.1) |
| fluid | Eight-dimensional emotion fluid submodel (§4.2) |
| mood | Three-dimensional mood submodel, a forced-damped system (§4.3) |
| Snapshot | The complete state dictionary returned by `snapshot()` |
| delta | Per-field attribution of a single state transition (§6.3) |
| Audit chain | The JSONL sequence of record envelopes, recomputable entry by entry |

---

## 3. Input Contract (Normative)

### 3.1 Interoceptive Vector Fields **[shared]**

A conforming implementation **MUST** accept a dictionary containing **any subset** of:

| Field | Type | Range | Meaning |
|---|---|---|---|
| `threat` | float | [-1, 1] | Perceived danger; positive raises fear |
| `belonging` | float | [-1, 1] | Social acceptance; negative means rejection |
| `autonomy` | float | [0, 1] | Sense of agency / control |
| `fatigue` | float | [0, 1] | Physical or mental fatigue input |
| `shame_trigger` | float | [0, 1] | Negative evaluation directed at the self |

The core **MUST** ignore unknown keys (see §3.5).

### 3.2 Narrative Event Vocabulary **[shared]**

| Event | Main vector (intensity 1.0) | Minor variant vector |
|---|---|---|
| `compliment` | `{"belonging": 0.3, "autonomy": 0.1}` | same |
| `insult` | `{"belonging": -0.4, "threat": 0.3}` | `{"belonging": -0.24, "threat": 0.18}` |
| `betrayal` | `{"belonging": -0.6, "threat": 0.5}` | `{"belonging": -0.36, "threat": 0.3}` |
| `alone` | `{"belonging": -0.3}` | `{"belonging": -0.18}` |
| `rest` | `{"fatigue": -0.5}` | same |
| *(any other)* | `{"belonging": 0.0, "threat": 0.0}` | same |

The minor variant scales negative intensity for insult / betrayal-class events to 60% of the main engine.

> **Note**: unknown event names fall into the all-zero branch; `arousal` is 0, so there is neither forcing nor relaxation-rate elevation on mood. Downstream systems **MUST NOT** assume any event name is valid.

### 3.3 Intensity Scaling **[shared]**

`raw_intensity` is a non-negative scalar (default `1.0`) that linearly scales the vector before appraisal. Implementations **MUST** accept `0.0` (no-op) and values greater than `1.0`.

### 3.4 event_id **[shared]**

An optional identifier. When supplied, it **MAY** trigger surprise computation in the anticipation system.

### 3.4 Unknown Key Handling **[shared]**

The core **MUST** ignore keys not defined in §3.1. An implementation **MUST NOT** claim such keys produced any effect.

> **Known trap**: in the reference implementation the Goal / Identity modules under `feature-guide/` emit a `tension_base` key that is outside the §3.1 contract, so goal-frustration and identity-conflict vectors **do not enter the core**. Those modules are guidance documents by design, not wired runtime components.

---

## 4. State Contract (Normative)

### 4.1 Snapshot Top-Level Key Set **[shared]**

A conforming implementation **MUST** make `snapshot()` return the following key sets. Both key count and key names are strong constraints; the implementation **MUST NOT** add or remove top-level keys without a major version bump.

**[main]** (23 keys):

```
fluid, mood, self_esteem, energy, fatigue, excitation, max_trust,
suppression_load, denial_load, rationalization_load, latent_pressure,
cognitive_dissonance, sleep_debt, arousal_recent, trauma, memory_count,
expected_count, last_perceived, llm_call_count, llm_failed_count,
total_prompt_tokens, total_completion_tokens, total_tokens
```

**[minor]** (15 keys):

```
fluid, mood, self_esteem, energy, fatigue, excitation, max_trust,
latent_pressure, cognitive_dissonance, sleep_debt, arousal_recent,
memory_count, expected_count, last_perceived, protective
```

- **[main]** only: `suppression_load` / `denial_load` / `rationalization_load` (defense compartment), `trauma` (trauma nodes), five `llm_*` / `total_*` metering fields
- **[minor]** only: `protective` (compliance protection report, §4.6)

Machine-readable definition: [`schema/snapshot.schema.json`](./schema/snapshot.schema.json)

### 4.2 fluid Submodel **[shared]**

`fluid` **MUST** contain exactly these 8 keys, each in `[0, 1]`:

| Key | Emotion | Initial |
|---|---|---|
| `喜悦` | Joy | 0.0 |
| `愤怒` | Anger | 0.0 |
| `恐惧` | Fear | 0.0 |
| `信任` | Trust | 0.5 |
| `疏离` | Alienation | 0.2 |
| `张力` | Tension | 0.2 |
| `愧疚` | Guilt | 0.0 |
| `羞耻` | Shame | 0.0 |

> **Initial value ≠ baseline steady state.** The initial value is the state at the character's birth; the baseline is the target used when rebuilding steady-state attraction each step. The two **may differ**, and this specification **does not fix** baseline values — that is implementation-layer tuning.
>
> `信任` **MUST NOT** exceed `max_trust`.

### 4.3 mood Submodel **[shared]**

`mood` **MUST** contain exactly these 3 keys, each in `[0, 1]`:

| Key | Meaning | Initial **[main]** | Initial **[minor]** |
|---|---|---|---|
| `愉悦` | Pleasantness | 0.5 | 0.5 |
| `紧张` | Tension | 0.3 | 0.2 |
| `精力` | Vigor | 0.7 | 0.7 |

### 4.4 trauma State **[main]**

`trauma` is a dictionary keyed by trauma-type identifier, each value in `[0, 1]`. An empty object `{}` denotes no active trauma.

The **[minor]** variant **MUST NOT** model trauma accumulation (see §4.6).

### 4.5 Memory Traces **[shared]**

Memory is an ordered list of trace objects. The core exposes only `memory_count`; an implementation **MAY** expose full traces, which **MUST** contain at least:

| Field | Type | Meaning |
|---|---|---|
| `vector` | object | The interoceptive vector at encoding time |
| `strength` | float [0,1] | Trace strength (subject to forgetting) |
| `valence` | float | `belonging - threat` at encoding time |
| `timestamp` | float | Unix time of last reinforcement |
| `age` | float | Seconds since last reinforcement |
| `count` | int | Number of reinforcements |

> **Capacity bound**: traces are represented as 5-dimensional interoceptive vectors with a cosine-similarity reconsolidation criterion. Semantically distinct events in 5-dimensional space **may cross that threshold and be treated as the same memory, overwriting each other**. Implementations **SHOULD** record the impact of such collisions on memory fidelity.

### 4.6 protective Submodel **[minor]**

`protective` is the compliance protection report unique to the minor variant and **MUST** contain at least:

| Field | Meaning |
|---|---|
| `risk_level` | `LOW` / `MEDIUM` / `HIGH` |
| `crisis_flags` | Deterministic reasons that triggered high risk |
| `rest_hint` | Whether the anti-addiction duration threshold is reached |
| `session_seconds` | Cumulative seconds of this session |
| `emotion_ceil_neg` | Negative-emotion clamp ceiling |
| `attach_max` | Attachment / trust ceiling |
| `minor_mode` / `age_group` | Minor mode and age group |
| `guardian_consent` / `guardian_contact` | Guardian consent and contact |
| `exit_requested` | Whether exit has been requested |
| `overuse_hint` | Whether the overuse threshold is reached |
| `ai_disclosure_required` | Whether the AI-identity disclosure interval is due |
| `reality_reminder_due` | Whether the reality-reminder interval is due |

This variant **MUST NOT** contain a `trauma_state` field and **MUST NOT** contain the defense-mechanism layer (`suppression_load` / `denial_load` / `rationalization_load` / suppression-rebound / latent-pressure avalanche / denial-reality intrusion). **This is mechanism-level risk reduction, not output-side filtering.**

### 4.7 Scalar State Variables **[shared]**

| Field | Range | Initial | Meaning |
|---|---|---|---|
| `self_esteem` | [0.05, 0.95] | 0.5 | Global sense of self-worth, slow-varying |
| `energy` | [0, 100] | 100.0 | Physical energy |
| `fatigue` | [0, 1] | 0.0 | Fatigue |
| `excitation` | [0, 1] | 0.3 | Arousal / novelty |
| `max_trust` | [0.1, 1.0] | 1.0 | Trust capacity, eroded under chronic neglect |
| `latent_pressure` | [0, ∞) | 0.0 | Latent pressure (avalanche precursor) |
| `cognitive_dissonance` | [0, 1] | 0.0 | Belief-behaviour conflict |
| `sleep_debt` | [0, 1] | 0.0 | Accumulated sleep debt |
| `arousal_recent` | [0, 1] | 0.0 | Slow memory of recent event arousal; drives mood relaxation rate |

**[main]** only: `suppression_load` / `denial_load` / `rationalization_load`, each `[0, ∞)`, initial 0.0.

### 4.8 Expected Events **[shared]**

`expected_events` maps `event_id` to `{valence: float [-1,1], confidence: float [0,1], time: float}`. `confidence` decays over time; entries are removed below a threshold.

### 4.9 Audit Requirements on the Snapshot **[shared]**

Every state quantity exposed by `snapshot()` **MUST** fall within the delta coverage of §6.3, or be explicitly declared a pure-output quantity. Quantities that drive the dynamics (e.g. `arousal_recent`) **MUST NOT** be unobservable hidden variables — otherwise the audit chain breaks.

---

## 5. Engine Entry Points (Normative)

A conforming implementation **MUST** expose:

| Method | Signature | Behaviour |
|---|---|---|
| `process_vector` | `(vector, raw_intensity=1.0, event_id="")` | Apply an interoceptive vector; change state; append an audit record |
| `process_event` | `(event, intensity=1.0)` | Map through the persona layer, then delegate to `process_vector` |
| `idle` | `(seconds)` | Advance `seconds` of time with no external stimulus |
| `sleep` | `(hours)` | Sleep-debt clearance, dream emotion processing, fear extinction, energy recovery, wake reset |
| `expect` | `(event_id, valence, confidence=0.5)` | Register anticipation of a future event |
| `induce_dissonance` | `(magnitude, belief_domain="")` | Inject a belief-behaviour conflict |
| `snapshot` | `() -> Dict` | Return the complete state defined in §4 |
| `set_clock` | `(t: Optional[float])` | Inject virtual time; pass `None` to restore wall clock |
| `advance_clock` | `(dt)` | Advance the virtual clock by `dt` seconds |

**Time bound**: a single step **MUST** be capped at 86400 seconds (24 h).

> **`idle` and `sleep` do not produce audit records in the reference implementation.** Callers needing a complete trace **MUST** record them themselves; an implementation **SHOULD** record them.

---

## 6. Audit Contract (Normative)

### 6.1 Record Envelope **[shared]**

Each audit record is one line of JSON (JSONL). The envelope **MUST** contain:

| Field | Type | Meaning |
|---|---|---|
| `seq` | int | Monotonic sequence number within the session |
| `ts` | string | ISO 8601 timestamp with millisecond precision |
| `engine` | string | Engine version tag; main engine `"SPL-V8.0"` |
| `session` | string | Session identifier |
| `event` | string | Event type (§6.2) |
| `input` | object | Sanitised input parameters |
| `snapshot` | object | State summary (key set of §6.4) |
| `delta` | object | State-transition attribution (§6.3) |

### 6.2 Canonical Event Types **[shared]**

| `event` value | Triggered by |
|---|---|
| `process_vector` | Each vector application |
| `sleep` | One `sleep()` call |
| `expect` | One `expect()` call |
| `induce_dissonance` | One `induce_dissonance()` call |
| `llm_call` | One language-model call (§6.5) |
| `llm_usage_recorded` | One token-usage registration |

### 6.3 State-Transition Attribution `delta` (Normative Algorithm) **[shared]**

`delta` is computed by `AuditLogger.snapshot_delta(before, after)`; **both variants MUST use the same algorithm**.

**Steps**

1. For each key `k` in `DELTA_SCALARS`: take `b = before[k]`, `a = after[k]`. If both are missing, skip.
2. For each submodel `g` in `DELTA_NESTED`: if both `before[g]` and `after[g]` are dictionaries, take the union of their keys, expand each into the dotted path `"g.k"`, with `b = before[g].get(k)`, `a = after[g].get(k)`.
3. For each candidate `(key, b, a)`: if `b == a`, skip.
4. **Numeric entries** (both sides int/float and neither is bool): `{"before": b, "after": a, "delta": round(a - b, 6)}`.
5. **Non-numeric entries**: `{"before": b, "after": a}`, **MUST NOT** carry a `delta` key.

**Booleans** **MUST NOT** be treated as numeric. "A crisis flag was added" is itself an audit event even though it has no arithmetic difference — an implementation **MUST NOT** fabricate a difference for it.

**Coverage sets**

| | `DELTA_SCALARS` | `DELTA_NESTED` |
|---|---|---|
| **[main]** (14) | `self_esteem, energy, fatigue, excitation, max_trust, suppression_load, denial_load, rationalization_load, latent_pressure, cognitive_dissonance, sleep_debt, arousal_recent, memory_count, expected_count` | `fluid, mood, trauma` |
| **[minor]** (10) | `self_esteem, energy, fatigue, excitation, max_trust, latent_pressure, cognitive_dissonance, sleep_debt, arousal_recent, memory_count, expected_count` | `fluid, mood, protective` |

The `DELTA_SCALARS` difference reflects variant reduction (§4.6) and **MUST NOT** be forcibly aligned.

### 6.4 Snapshot Summary **[shared]**

The `snapshot` field of an audit record is a **subset** of the complete state, with key sets:

**[main]** (17 keys): `fluid, mood, self_esteem, energy, fatigue, excitation, max_trust, suppression_load, denial_load, rationalization_load, latent_pressure, cognitive_dissonance, sleep_debt, arousal_recent, trauma, memory_count, expected_count`

**[minor]** (14 keys): `fluid, mood, self_esteem, energy, fatigue, excitation, max_trust, latent_pressure, cognitive_dissonance, sleep_debt, arousal_recent, memory_count, expected_count, protective`

### 6.5 LLM Call Records **[shared]**

An `llm_call` record **MUST** additionally contain:

| Field | Type | Meaning |
|---|---|---|
| `model` | string | Model identifier |
| `prompt_preview` | string | First 200 characters of the prompt |
| `success` | bool | Whether generation succeeded |
| `duration_ms` | float | Wall-clock duration of the call |
| `usage` | object \| null | Token usage, `null` when unavailable |
| `error` | string \| null | Error message, `null` on success |

When non-null, `usage` **MUST** contain `prompt_tokens` / `completion_tokens` / `total_tokens` (integers).

### 6.6 Failure Policy **[shared]**

Audit writes **MUST NOT** alter core state evolution. On write failure the engine **MUST** continue silently and **MAY** retry on the next record. A conforming implementation **MUST** document its failure policy in the same way.

---

## 7. Determinism Preconditions (Normative)

### 7.1 Determinism Condition **[shared]**

A conforming implementation **MUST** produce identical state given identical:

```
(vector sequence, intensity sequence, event_id sequence, initial state, clock schedule)
```

The core **MUST NOT** contain randomness and **MUST NOT** contain LLM calls. All randomness **MUST** reside in the replaceable persona layer or language layer.

### 7.2 Mood Dynamics Form **[shared]**

Mood **MUST** be implemented as a **forced-damped system**; it **MUST NOT** be implemented as "advance a fixed step on each call".

> **Step-size consistency**: an implementation **MUST NOT** claim to be "step-size independent". Forced-damped discretisation leaves a non-zero residual; assertion tolerances **MUST** account for that residual bound.

### 7.3 Clock Injection Precondition **[shared]**

Every replay assertion **MUST** inject a virtual clock (`set_clock`) first; without injection the implementation **MUST NOT** claim reproducibility.

> **Known trap**: after injecting the clock, `last_time` **MUST** be synchronised; otherwise the first time advance returns early on a negative `dt` — the "wall clock to synthetic origin" interval is not settled. Any external claim of reproducibility **MUST** carry this precondition.

---

## 8. Conformance Levels

| Level | Requirement | May claim |
|---|---|---|
| **L0 — Interface** | Satisfies the §3 input contract and §5 entry points | "AAE interface compatible" |
| **L1 — State** | L0 + snapshot key sets and ranges satisfy §4 | "AAE state compatible" |
| **L2 — Audit** | L1 + delta algorithm satisfies §6.3, audit chain recomputable across machines | "AAE conformant" |

> Conformance **excludes** correctness. See §9.2.

---

## 9. Verification and Boundaries

### 9.1 Verification Entry Point

Third-party verification methods: [`../verify/TESTING-zh.md`](../verify/TESTING-zh.md).

### 9.2 Nature of the Baseline

The conformance baseline and the object under acceptance are **same-origin**. Therefore:

- The suite proves "**behaviour has not drifted and the contract is satisfied**" — it is a change detector;
- It does **not** prove "the psychological conclusions are correct" — that requires external adjudication;
- Assertions written by the author **do not constitute independent third-party evidence**. Real acceptance evidence comes from tests the evaluator designs itself.

---

## 10. Versioning and Compatibility

- Adding or removing top-level snapshot keys **MUST** bump the major version;
- Narrowing a range **MUST** bump the major version;
- New optional fields or new event vocabulary **MAY** be introduced in a minor version.

---

## 11. License and Contact

- This specification text may be freely cited with attribution.
- It grants **no** license to any implementation. The engine core is a licensed deliverable.
- International / Global: [ai@nohnlins.com](mailto:ai@nohnlins.com) · China: [lin@secondai.top](mailto:lin@secondai.top)

*Copyright © NOHN AI TECHNOLOGY PTE. LTD.*
