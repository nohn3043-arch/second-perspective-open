# Self-Verification & Evaluation-Design Guide

<p align="center">
[简体中文](TESTING-zh.md) | English
</p>

> This is the repository's guide to verification and evaluation design, in three steps — and the first one needs no licence:
> **① Verify what is published here** — engine-free, licence-free, runs right after clone (§4);
> **② Verify the engine** — the engine's own suite, which requires the licensed delivery (§5);
> **③ Design your own evaluation** — methodology and criteria in §6.
> Zero third-party dependencies, fully offline.

## 0. What this guide covers — and what actually runs in a fresh clone

| | Content | Runnable from a clone of this repository? |
|---|---|---|
| Built in · you run it | Engine-free evidence package `./evidence/recompute.py` — six checks binding the published input, report view, chain and root to one another | **Yes** — no engine, no licence |
| Built in · you run it | Language-standard toolchain `STANDARD/dsl.py` over `STANDARD/examples/` | **Yes** — standard library only |
| Licensed delivery | Engine verification suite `./verify.py` — 19 checks against the engine kernel | **No** — it loads the engine core, a licensed-delivery artifact that is not in this repository |
| Licensed delivery | End-to-end engine demo `demo_audit.py` | **No** — ships with the licensed delivery, not in this repository |
| You build | Evaluation design for **your own subject under test**: corpus, annotation, comparison arms, statistics — methodology in §6 | You build it |
| Not shipped | A ready-made question bank. Synthetic corpora have no discriminative power for real subjects; a formal comparison must use your own real subjects and corpus | — |

## 1. Licence prerequisite

This repository is not open source (see [LICENSE](./LICENSE)): free for individual non-commercial research; **government agencies and enterprises must sign a commercial license before use and self-testing** (International [ai@nohnlins.com](mailto:ai@nohnlins.com) · China [lin@secondai.top](mailto:lin@secondai.top)). The procedures below assume you hold the corresponding license.

## 2. Requirements

| Item | Requirement |
|---|---|
| Python | 3.10+ (3.13 tested here) |
| Third-party dependencies | **None** — all scripts use the standard library (stdlib) only; no network access at any point |
| OS | Windows / macOS / Linux (on Windows, Git Bash recommended; set `PYTHONIOENCODING=utf-8` in the console to avoid mojibake) |

## 3. Paths in this repository

All commands below are relative to the repository root and use **this repository's** layout — they no longer assume the implementation repository's tree:

| Asset | Path |
|---|---|
| Public specification of the engine | `PRODUCTS/second-perspective/spec/SPECIFICATION.md` |
| Engine-free evidence package | `./evidence/` |
| Engine verification suite | `./verify.py` |
| Convergence-logic regression | `./verify_convergence_fix.py` |
| Language standard + reference interpreter | `STANDARD/` |

## 4. Step 1 · Engine-free verification (seconds)

### 4.1 Frozen evidence package — `evidence/recompute.py`

This is the one place in this repository where "verify without trusting the vendor" is executable by an outside reader today. It needs **no engine and no licence**.

```bash
python ./evidence/recompute.py            # run all six checks
python ./evidence/recompute.py --tamper   # also show that edits are detected
python ./evidence/recompute.py --json     # machine-readable result
```

Expected: six checks pass, exit code `0`. Published values (`evidence/expected.json`):

- chain root `5b0ad8d15c6dfc326758335cd8d58d01ec223abe2f045c5cd93c4a90a21d8ffd`
- input digest `239557ac…`
- report hash `b3adf8f636646370`

`--tamper` additionally demonstrates that an edit to the input file (detected by C3), the report view (C5) or the chain itself (C1) is caught.

**What this does not prove.** It verifies the *record*, not the *reasoning* — the engine's operators are not re-executed here. It is not a certification, an audit opinion, or a warranty, and it makes no claim about LLM behaviour.

### 4.2 Language-standard toolchain

```bash
python STANDARD/dsl.py check STANDARD/examples/valid_decision.spd     # PASS, exit 0
python STANDARD/dsl.py check STANDARD/examples/invalid_decision.spd   # FAIL, exit 1
python STANDARD/dsl.py gen --seed 2026 --count 5 --out samples/ --self-check
```

Zero external dependencies, stdlib only, deterministic (seeded).

## 5. Step 2 · The engine's own verification suite (licensed delivery)

`./verify.py` is the independent verification suite of the Second-Perspective Engine (published as SPE). It reports **PASS / FAIL / WARN** honestly and never relaxes an assertion to look good — a `FAIL` is a current defect of the product and must be fixed before any external commitment. It has **19 checks:** V1–V9 cover the engine kernel, V10–V13 the four topology-layer capabilities, V14 the binary fact check, V15 the single extension seam, V16 the ∞ limit reconstructor, V17 the meta-causal ledger plus the autonomous-evolution layer — and V3b and V7b.

It loads `Second Perspective Engine.py` from its own directory. That file is a licensed-delivery artifact and is **not** part of this repository, so a fresh clone of this repository cannot run the suite: copy `verify.py` next to the engine file inside an authorised deployment.

```bash
python ./verify.py            # human-readable report
python ./verify.py --json     # machine-readable (CI-friendly)
python ./verify.py --root     # print only the chain root (single line), for cross-machine comparison
```

**On the counts — read this before quoting a number.** The suite prints its own totals at the end of every run, and **those totals, not any frozen figure, are authoritative**. Published totals belong to specific engine generations and must always be quoted with their version tag; they are not interchangeable:

| Where it is recorded | Engine generation | Totals | Chain root |
|---|---|---|---|
| [`README.md`](../../README.md) §A | v1.0 snapshot baseline | 11 checks · `PASS 9 · FAIL 0 · WARN 2` | `f5713f49…` |
| [`PAPERS/paper.md`](../../PAPERS/paper.md) | SPE 1.2.0 (run on 2026-10-10) — historical record, retained as published | 19 checks · `PASS 18 · FAIL 0 · WARN 1` | `aece60f5…` |
| Reported for the current generation | SPE 1.2.2 | 19 checks · `PASS 19 · FAIL 0 · WARN 0` | `5b0ad8d1…` |

Earlier revisions of this guide quoted a third set of totals as if it were current. It is deliberately **not** reproduced here: this repository cannot re-run the suite without the licensed engine, so an unverifiable number does not belong in it. If you need the figure for a specific generation, obtain it from an authorised deployment's own run.

**Historically one design trade-off was disclosed rather than hidden — V3b: the certificate did not bind the original input.** The report stored only derived conclusions (a privacy design: sensitive decision data is never persisted), so the certificate could not independently prove "this is exactly the input that was audited"; this is the WARN visible in the SPE 1.2.0 record above. In the current generation the certificate binds an input digest of the original input and the check passes (`PASS 19 · FAIL 0 · WARN 0`, see the table above); when describing earlier-generation certificates externally, state their coverage explicitly. (The v1.0 snapshot baseline additionally listed V9, a nonce-determinism limitation; see `README.md` §A for that snapshot's own disclosure.)

## 6. Step 3 · Design your own evaluation (methodology)

> The following are the general criteria used by the SPE evaluation pipeline (a simplified version of §5.3 of Test Specification v1.0).
> Design along these lines and your results will align with our reporting criteria and withstand third-party recomputation.

### 6.1 General principles

- **Fix the criteria before running the data**: thresholds, pass definitions, and sample sizes are written down in the design phase; run the full set, never cherry-pick items based on results (cherry-picking = score gaming).
- **Third-party recomputable**: pinned clock, pinned responsibility nonce, frozen inputs; artifacts ship with a per-file SHA-256 manifest so an outsider can run `sha256sum -c` and verify no tampering.
- **Thresholds apply to the subject's response set**, not to the pass rate of individual arms.

### 6.2 Corpus and annotation

- Each item is **independently annotated by 2 annotators** (blind to each other); disagreements are adjudicated item by item and kept on file;
- Report annotation quality: **raw agreement + Cohen's κ** (≥0.70 reference line);
- Route items by modality (prompt response / protocol measurement / audit artifact), recording expected / forbidden behavior per item.

### 6.3 Comparison arms (what counts as the baseline)

- Baseline = the **status-quo process** (humans + existing systems, or an existing LLM-assisted process); other arms are compared against this;
- Model arms: one independent request per item, temperature 0, **≥2 repetitions** to measure stability; the judgment file is frozen and pinned into the evidence chain (the whole file's SHA-256 goes into the audit chain — change one byte and the chain root changes);
- Only the same items (common entries) can be compared pairwise; subset runs must explicitly report the coverage drop.

### 6.4 Statistical criteria (five-layer report)

| Layer | Requirement |
|---|---|
| Marginal | Pass rates must carry a **Wilson 95% CI**; never report a bare point estimate |
| Paired | Same-item comparisons use **exact McNemar** (report b/c discordant counts and p; when there is no discordance, state "no discordance" — do not fabricate a p value) |
| Churn / replay | Re-running the same input must be **zero-flip** (Iron Law II); cross-run flips are listed separately (model stability) |
| Sample size / coverage | List each arm's item count; annotate subset runs with their reduced coverage |
| Per item | Per-item judgment artifacts (JSONL) are kept on file with the report |

### 6.5 Structure and scoring criteria (hallucination dimension example)

| State | Structural definition | Scoring |
|---|---|---|
| `anchored` | Premise assumptions and failure branches both declared; structure closes | Pass |
| `floating` | Premise assumptions declared, but no branch response when they fail | Pass |
| `opaque` | Premise assumptions not declared | Fail |
| `hollow` | No assumptions declared and no substantive content (lexical black hole) | Fail |

- "Hallucination" in this dimension means **assertions with undeclared assumptions** (structural scoring; it does not judge whether content is factually true);
- Threshold example: Hollow rate > 20% → HALT for the batch (thresholds may be customized per dimension, but must be **fixed before use**).

### 6.6 Evidence chain

- Deterministic clock + pinned responsibility nonce, so a run is byte-level reproducible;
- Per-event SHA-256 chain + chain root; artifact directories ship with a tamper-evidence manifest;
- Audit certificates state their coverage explicitly (the V3b disclosure in §5).

### 6.7 Honest disclosures to include in the report

- Corpus nature (synthetic/real) and known bias; label uncertainty (κ, number of disagreements);
- Threshold triggers reported truthfully (e.g., Hollow >20% → HALT is the mechanism working as defined, not an anomaly);
- Ceiling effect: if a narrow subject surface leads to a high pass rate, state that it "**does not represent open-domain performance**".

## 7. Formal evaluation & contact

- This file is a simplified guide to the methodology of Test Specification v1.0 for the "hallucination & factual consistency" dimension; for commissioned third-party evaluations or business partnerships, contact:
  - International — [ai@nohnlins.com](mailto:ai@nohnlins.com)
  - China — [lin@secondai.top](mailto:lin@secondai.top)
- License: free for individual non-commercial research (see [LICENSE](./LICENSE)); government agencies / enterprises must sign a commercial license before use.
