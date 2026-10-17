# AAE — Third-Party Verification Guide

**Document ID:** AAES-2026-003
**Version:** 0.1.0
**Status:** Draft for evaluation
**Applies to:** the interface contract defined in [`../spec/SPECIFICATION.md`](../spec/SPECIFICATION.md)
**Maintainer:** NOHN AI TECHNOLOGY PTE. LTD.
**Contact:** ai@nohnlins.com · lin@secondai.top

> This document is **informative**: it adds no normative requirements. It answers one question only — "for a given public claim, how does a third party verify it, and to what depth?" The normative contract is [`../spec/SPECIFICATION.md`](../spec/SPECIFICATION.md).

---

## 0. Audience, Purpose, Preconditions

**Audience**: teams building dialogue assistants or emotional-companionship products that intend to integrate AAE; QA and architecture review groups; accredited testing bodies.

**Purpose**: let the evaluator **design its own** tests and issue **its own** report, so acceptance never depends on vendor self-description. **The bundled suite is a runnable example and comparison baseline only: author self-tests do not constitute third-party evidence (§5).**

**Preconditions**:

- The object of verification is the **interface contract** in [`../spec/SPECIFICATION.md`](../spec/SPECIFICATION.md), not any particular implementation;
- The engine core (`SPL-anthropic-engine.py`) is a licensed deliverable and is **not** in this public repository;
- This guide describes a technical verification path; its executability and permitted scope follow [`../LICENSE`](../LICENSE).

---

## 1. Four Verification Zones

| Zone | Self-provable | Tool / basis | Boundary |
|---|---|---|---|
| **A Contract conformance** (key sets, types, ranges, entry signatures) | Yes | validate snapshots and vectors against [`schema/`](../spec/schema/) | Conclusion covers "shape matches the contract" only |
| **B Kernel behaviour** (determinism, dynamics, audit fields) | Requires license | engine-side S+R suites | Conclusion covers "behaviour matches the contract" |
| **C LLM layer** (utterance adapter) | No | independent red team / benchmark | Output is inherently non-reproducible |
| **D Compliance endpoint** (minor-serving layer) | Partly | compliance statement + legal review | Production deployment also needs DPIA / security assessment / algorithm filing |

> **In one line**: zones A / B prove "**behaviour has not drifted and the contract is satisfied**" — not "the psychological conclusions are correct". The former is a detector; the latter needs external adjudication.

---

## 2. Zone A — Contract Conformance (engine-free)

Any party may execute this without a license:

1. Build an input vector conforming to [`schema/vector.schema.json`](../spec/schema/vector.schema.json);
2. Inject a virtual clock;
3. Apply an event sequence;
4. Take `snapshot()` and validate it against [`schema/snapshot.schema.json`](../spec/schema/snapshot.schema.json):
   - the top-level key set matches specification §4.1 exactly (no more, no fewer);
   - `fluid` has exactly 8 keys and `mood` exactly 3;
   - each scalar lies within the range in specification §4.7;
   - `信任 ≤ max_trust`.
5. Validate audit records line by line against [`schema/audit-record.schema.json`](../spec/schema/audit-record.schema.json) and recompute `delta` per specification §6.3.

### 2.1 Writing assertions (five rules)

1. **Observe behaviour, do not restate the formula.** Do not read an implementation constant, recompute the formula, and assert the formula holds — that is vacuously true under formula changes. Only observe "given this input, how does the state change".
2. **Include at least one negative test that "must fail to pass".** For example: without clock injection, two runs **must** yield different hashes; unknown keys must not change state.
3. **Self-check the discriminative power of key assertions.** "Test passes" is evidence only if "breaking the behaviour turns the test red". Break one line on your own copy, confirm it goes red, then revert.
4. **Baseline discipline.** Updating a baseline is for **newly added vectors** only — never to turn a failing old vector green; that is equivalent to deleting the test.
5. **Clock discipline.** Always inject the clock before any replay assertion; after injection, `last_time` **must** be synchronised, or the first time advance returns early on a negative `dt`. Any external claim of reproducibility **must** carry this precondition.

### 2.2 Turning your scenario into a vector

1. Add one entry following the vector format in specification §3.1;
2. Run your suite to generate a baseline; `git diff` **should** show only the new vector's fields — if old vectors' hashes also changed, the engine has drifted; find out why before continuing;
3. Re-run for a fully green result and archive: a copy of the vector file + the result file (which records python / platform and other environment metadata).

The artifact is "the engine's reproducibility certificate on *your* event sequence".

---

## 3. Zone B — Engine Kernel Verification (license required)

The engine-side suite has two layers:

| Layer | Content |
|---|---|
| **S group** | Determinism and replayability (including a negative assertion that "must differ to pass") |
| **R group** | Semantic contracts: defence mechanisms, audit attribution, mood dynamics, minor-variant alignment, documentation consistency, mutation guard |

> **Why the mutation guard matters**: after injecting defective variants, the corresponding test **must** turn red. This is the precondition for every other assertion being credible.

**Cross-environment note**: snapshot hashes are sensitive to interpreter and platform. For heterogeneous re-verification, use the scalar layer (tolerance `1e-9`) and declare the acceptance environment in the archive.

---

## 4. Non-Self-Proving Claims (External Adjudication)

| Claim | Why it cannot self-prove | External path |
|---|---|---|
| "Behaviour is correct" (correctness) | Baseline and acceptance object are same-origin; it is a change detector | External counterfactual experiment: compare full kernel / mechanism-reduced / output-filter-only under one scripted sequence, then human adjudication |
| Minor-compliance capability | Technical endpoints can be smoke-tested; legal obligations cannot | Compliance statement + legal review + DPIA / security assessment / algorithm filing |
| Provider self-assessment against IMDA AI Verify: 95/100 | Provider-run self-assessment (not third-party, not an IMDA certification) | `IMDA_AI_Verify_Causal_Audit_Report.pdf` in this repository |

---

## 5. Nature of the Bundled Suite (read first)

`tests/` is written by the author of the work — its **execution** is third-party (you run it), but its **assertion design** comes from the author. It therefore provides a comparison of "behaviour consistent with the author's claims", and **does not constitute independent evidence**; real acceptance evidence comes from the tests you design yourself per §2.

Sound uses: a runnable example, a reference for assertion style, a regression baseline.

---

## 6. Reporting and Archival (procurement)

Suggested structure: object and environment (contract version / environment metadata) → the test list and criteria you designed → results and raw artifact paths → coverage boundaries and unverified items.

| Item | Source |
|---|---|
| Contract version | version number in the specification header |
| Acceptance environment (python / platform) | recorded automatically in your result file |
| Custom vectors + baseline | your vector file copy (§2.2) |
| Audit log sample | the JSONL produced by the smoke script with auditing enabled |

**Re-test triggers**: engine version change (semantic versioning), contract version change, deployment-shape change.

---

## 7. Common Misuse (Evaluation Red-Flag List)

1. Refreshing a baseline to turn a failing old vector green;
2. Claiming reproducibility without clock injection, or claiming it without stating the clock precondition;
3. Treating a snapshot hash as "proof of correctness" (it only proves "unchanged");
4. Folding LLM-layer output into a determinism conclusion;
5. Depending on the output of extension modules that are not wired into the core (e.g. `tension_base`);
6. Assuming any event name is valid (unknown events fall into the all-zero branch);
7. Substituting output filtering for mechanism-level reduction and claiming equivalence;
8. Comparing hashes across environments without declaring the environment or using the scalar layer as fallback.

---

## 8. Related Documents

| Document | What it answers |
|---|---|
| [`../spec/SPECIFICATION.md`](../spec/SPECIFICATION.md) | Normative contract: input / state / entry / audit / determinism |
| [`../spec/SPECIFICATION-zh.md`](../spec/SPECIFICATION-zh.md) | 中文规范 |
| [`../spec/schema/`](../spec/schema/) | Machine-readable schemas (snapshot / vector / audit-record) |
| [`../LICENSE`](../LICENSE) | Permitted scope |

---

*Copyright © NOHN AI TECHNOLOGY PTE. LTD. This document is provided for evaluation and interoperability review; the permitted scope for running and deploying is governed by [`../LICENSE`](../LICENSE).*
