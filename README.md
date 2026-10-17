# Second-Perspective Open — Public Trust Layer for Trusted Computing

> Specifications, verifiers, and self-declared compliance records — in the open.
> This repository is the **public trust layer** of the NOHN AI "Second-Perspective" trusted-computing stack: anyone may verify our deliverables without prior authorization — and cannot obtain the core engine implementation from it.
> The engine it documents — **SPE (Second Perspective Engine) — is the brake system for AI**, built for foundation-model vendors, governments and regulators, and enterprises that control an AI system. It is not a benchmarking or certification service.

<p align="center">
  <a href="README-zh.md">简体中文</a> | English
</p>

## What this repository is

Trust in trusted computing comes from **third-party offline verification**, not from publishing all source code.
This repository follows the mature path already taken by TPM / Intel SGX / ARM TrustZone: **specs public · implementation private · certification as backstop**.

| Layer | Content | Visibility |
|-------|---------|-----------|
| Public layer (this repository) | Language standard, verifiers, papers, compliance mappings and self-assessment records (no third-party certification) | 🔓 Open |
| Implementation layer (other repositories) | Engine core, LLM adapters, hardware RTL, product implementations | 🔒 Private / licensed delivery |

## Directory structure

```
second-perspective-open/
├── PRODUCTS/                   # 🏷️ One folder per product: public spec in spec/ — no implementation internals
│   ├── Antares/                        # GFSIP v1.0 federated interoperability protocol
│   ├── ai-draw-cue-word-project/       # AI-drawing prompt console
│   ├── second-perspective/             # SPE (Second Perspective Engine) — the brake system for AI
│   └── second-reality/                 # Virtual-world substrate
├── STANDARD/                   # 📐 Decision-structure language standard (EBNF grammar + reference interpreter)
│   ├── grammar.md / grammar-zh.md    # Grammar specification (EN / ZH)
│   ├── decision.ebnf                 # Decision-structure grammar (EBNF)
│   ├── topology.ebnf                 # Topology-structure grammar (EBNF)
│   ├── dsl.py                        # Reference interpreter (executable definition of the standard)
│   ├── 2026.md                       # Dated standard snapshot (version 2026)
│   └── examples/                     # Valid / invalid samples (4 .spd files)
├── PRODUCTS/second-perspective/verify/  # ✅ Second Perspective Engine (SPE) verifiers — see §A below
│   ├── verify.py                        # zero-dependency, offline (python3, stdlib only)
│   ├── verify_convergence_fix.py        # convergence-logic regression (S1–S6)
│   ├── verify-output.log                # full output of the v1.0 snapshot (Zenodo)
│   └── evidence/                        # ✅ frozen audit chain + engine-free recomputation — no engine, no licence needed
├── PRODUCTS/nomos/verify/               # ❌ NOMOS third-party verification guide — a different product, see §B below
│   └── VERIFICATION_GUIDE.md            # verifies NOMOS, NOT this engine
├── PAPERS/                     # Papers and white papers (reproducible citation)
│   ├── paper.pdf / paper.md
│   └── why-ai-needs-brakes.md  # Position paper: why capable AI needs a brake layer
└── CERTIFICATIONS/             # Compliance mappings · self-declared AIMS · provider-submitted AI Verify material
    ├── IMDA_AI_Verify_Causal_Audit_Report.pdf   # AI Verify self-assessment: 95/100 (provider self-test, not an IMDA certification)
    ├── compliance/                          # EU AI Act / ISO 42001 / NIST AI RMF / Shanghai compliance
    └── aims/                                # 🧭 NOHN AI's own AIMS (ISO/IEC 42001) — self-built, unaudited, evidence recomputable
```

## How to verify (third-party, offline)

Verification assets are split by product, one folder each: `PRODUCTS/second-perspective/verify/` and `PRODUCTS/nomos/verify/`. Confirm which one you are working from before running anything.

### A. Second Perspective Engine (SPE) — ✅ the engine's own verifier, in `PRODUCTS/second-perspective/verify/`

`PRODUCTS/second-perspective/verify/verify.py` **is the independent verification suite of the Second-Perspective Engine** (SPE). It loads the engine core (`Second Perspective Engine.py`, a licensed-delivery artifact) and reports **PASS / FAIL / WARN** honestly — it never relaxes an assertion to look good. A `FAIL` is a current defect of the product and must be fixed before any external commitment.

The engine's **public specification** is [`PRODUCTS/second-perspective/spec/SPECIFICATION.md`](./PRODUCTS/second-perspective/spec/SPECIFICATION.md); the verification-and-evaluation methodology is the [TESTING guide](./PRODUCTS/second-perspective/TESTING.md). Note the split: `verify.py` cannot run from a clone of *this* repository — it loads the engine core — so the licence-free, clone-and-run entry point is the engine-free **evidence package** described below.

| File | Role |
|------|------|
| `PRODUCTS/second-perspective/verify/verify.py` | Zero-dependency, offline, pure-stdlib verifier. **19 checks:** V1–V9 cover the engine kernel, V10–V13 the four topology-layer capabilities, V14 the binary fact check, V15 the single extension seam, V16 the ∞ limit reconstructor, V17 the meta-causal ledger plus the autonomous-evolution layer — and V3b and V7b |
| `PRODUCTS/second-perspective/verify/verify_convergence_fix.py` | Convergence-logic regression (S1–S6) against the same engine |
| `PRODUCTS/second-perspective/verify/verify-output.log` | Full output of the v1.0 snapshot, archived for the Zenodo deposit |

```bash
# 0 dependencies, Python 3 standard library only (run inside an authorized engine deployment)
python PRODUCTS/second-perspective/verify/verify.py --root    # print the chain root, compare with the fixed value below
python PRODUCTS/second-perspective/verify/verify.py           # full suite: the script prints its own PASS / FAIL / WARN totals
```

**On the counts — read this before quoting a number.** The suite prints its own totals at the end of every run, and **those totals, not any frozen figure, are authoritative**. The **v1.0 snapshot baseline is `PASS 9 · FAIL 0 · WARN 2` over 11 checks**; the two WARNs are pre-registered disclosures (V3b, V9), not failures. The suite has since been extended to 19 checks, so any count taken from the baseline must be labelled a **v1.0 snapshot value**. The shipped `verify-output.log` records that snapshot and lets you cross-check the chain root and the PASS / FAIL counts independently.

**Runtime note.** `PRODUCTS/second-perspective/verify/verify.py` is a **publicly auditable verifier**: its logic is fully visible, zero-dependency and offline-runnable. A complete run loads the engine core — a private implementation, included in the licensed delivery.

Fixed chain root (v1.0 snapshot):
`f5713f49481a80f82356ba1255c0292ddb0d17a235a35348bcff0eef49d6a801`

**Engine-free evidence package — start here.** `PRODUCTS/second-perspective/verify/evidence/` holds a frozen audit chain, its expected root, and a zero-dependency recomputation script. It runs **without the engine and without a licence**:

```bash
python PRODUCTS/second-perspective/verify/evidence/recompute.py --tamper
```

This is the one place in this repository where "verify without trusting the vendor" is executable by an outside reader today. It runs six checks that bind the published input, the published report view and the frozen chain to each other and to the published root — input digest → report hash → chain root — and demonstrates that an edit to any of the three is detected.

### B. NOMOS Intelligent Decision Hub — ❌ a separate product, in `PRODUCTS/nomos/verify/`, NOT the engine's verifier

`PRODUCTS/nomos/verify/VERIFICATION_GUIDE.md` is the third-party verification guide for **NOMOS** ([nohn3043-arch/NOMOS](https://github.com/nohn3043-arch/NOMOS), v0.5.0, 2026-10-08). NOMOS is a **different product** from the Second-Perspective Engine, and this guide does **not** verify the engine.

- Method: `pytest` release evidence (baseline: 507 tests, 91% coverage) plus one replayable evaluation run.
- Its own chain root: `adacff1bd647b7691cf153b5800185b1afbb449de779bebc2847ac1988090a68`.
- Use it only when you are evaluating NOMOS. To evaluate the Second-Perspective Engine, use §A.

### C. NOHN AI's own AI Management System — 🧭 in `CERTIFICATIONS/aims/`

Neither §A nor §B certifies anything. `CERTIFICATIONS/aims/` is different in kind: it is the
**management system NOHN AI runs for itself**, aligned to ISO/IEC 42001:2023, with its evidence
generated by the engine. It is **self-built, unaudited and carries no certificate** — published so
that its records are independently recomputable and its gaps are visible rather than implied away.

Note the standing distinction: ISO/IEC 42001 certifies an **organisation's AIMS**, never a product.
The engine appears in that folder as a control and evidence generator, not as a certified object.

Start at [`CERTIFICATIONS/aims/README.md`](./CERTIFICATIONS/aims/README.md); read
[`CERTIFICATIONS/aims/OPEN-GAPS.md`](./CERTIFICATIONS/aims/OPEN-GAPS.md) before quoting any claim.

## License

Works in this repository are licensed in tiers under the Software License Agreement (`LICENSE`):

- **Individual non-commercial research**: free (download, copy, run, modify, academic citation — with attribution)
- **Government / enterprise / institution**: prior written paid license required

Commercial licensing — International: <ai@nohnlins.com> ｜ China: <lin@secondai.top>

## Product documentation

Each product has one folder under `PRODUCTS/` (index: [PRODUCTS/README.md](./PRODUCTS/README.md)). Its **public specification** lives in a `spec/` subfolder — positioning and boundaries, interfaces / protocols / formats, audit and compliance, conformance statements. Beyond the specification, a product folder keeps only what can be published without disclosing implementation: its glossary, and — where the engine's own verifier can only run against a licensed engine — the verification guide. **Architecture and source-level notes are published only where the implementation itself is public**; where the implementation is a confidential deliverable, this layer carries none. The one standard that is not a product document, the decision-structure language (together with its reference interpreter `dsl.py`), lives under [`STANDARD/`](./STANDARD/).

## Related

- Papers and metadata: Zenodo (see the DOI in the paper)
- Core implementation: private repositories / offline licensed delivery
- Web portal: https://www.nohnlins.com

---
© 2026 Shanghai Linming Junhua Technology Co., Ltd. and NOHN AI TECHNOLOGY PTE. LTD. All rights reserved.
