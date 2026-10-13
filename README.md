# Second-Perspective Open — Public Trust Layer for Trusted Computing

> Specifications, verifiers, and independent certification assets — in the open.
> This repository is the **public trust layer** of the NOHN AI "Second-Perspective" trusted-computing stack: anyone may verify our deliverables without prior authorization — and cannot obtain the core engine implementation from it.

<p align="center">
  <a href="README-zh.md">简体中文</a> | English
</p>

## What this repository is

Trust in trusted computing comes from **third-party offline verification**, not from publishing all source code.
This repository follows the mature path already taken by TPM / Intel SGX / ARM TrustZone: **specs public · implementation private · certification as backstop**.

| Layer | Content | Visibility |
|-------|---------|-----------|
| Public layer (this repository) | Language standard, verifiers, papers, independent certification reports | 🔓 Open |
| Implementation layer (other repositories) | Engine core, LLM adapters, hardware RTL, product implementations | 🔒 Private / licensed delivery |

## Directory structure

```
second-perspective-open/
├── PRODUCTS/                   # 🏷️ Portal for all product docs (README/GLOSSARY/compliance/public SPECIFICATION)
│   ├── Antares/                        # GFSIP v1.0 federated interoperability protocol
│   ├── Anthropomorphic-Agent-Engine/   # Anthropomorphic psychology engine
│   ├── ai-draw-cue-word-project/       # AI-drawing prompt console
│   ├── DMU/                            # Robot motion platform
│   ├── HuM/                            # Humanoid system
│   ├── nomos/                          # Second-order causal decision framework (95/100)
│   ├── PAGES/                          # Official web portal
│   ├── second-perspective/             # GCAE global cognitive audit engine (the engine)
│   ├── second-reality/                 # Virtual-world substrate
│   ├── SPL-G1/                         # Hardware causal-audit TCU
│   └── Story-engine/                   # Long-form narrative consistency engine
├── SPEC/                       # Decision-structure language standard (public)
│   └── language-standard/
│       ├── grammar.md / grammar-zh.md    # Grammar specification (EN / ZH)
│       ├── decision.ebnf                 # Decision-structure grammar (EBNF)
│       ├── topology.ebnf                 # Topology-structure grammar (EBNF)
│       ├── dsl.py                        # Reference interpreter (executable definition of the standard)
│       └── examples/                     # Valid / invalid samples (19 diagnostic-code demos)
├── second-perspective-verify/  # ✅ Second-Perspective Engine (GCAE) verifiers — see §A below
│   ├── verify.py                        # zero-dependency, offline (python3, stdlib only)
│   ├── verify_convergence_fix.py        # convergence-logic regression (S1–S6)
│   ├── verify-output.log                # full output of the v1.0 snapshot (Zenodo)
│   └── evidence/                        # ✅ frozen audit chain + engine-free recomputation — no engine, no licence needed
├── nomos-verify/               # ❌ NOMOS third-party verification guide — a different product, see §B below
│   └── VERIFICATION_GUIDE.md            # verifies NOMOS, NOT this engine
├── PAPERS/                     # Papers and white papers (reproducible citation)
│   └── paper.pdf / paper.md
└── CERTIFICATIONS/             # Independent certification and compliance
    ├── IMDA_AI_Verify_Causal_Audit_Report.pdf   # Singapore IMDA AI Verify: 95/100
    └── compliance/                          # EU AI Act / ISO 42001 / NIST AI RMF / Shanghai compliance
```

## How to verify (third-party, offline)

Verification assets are split by product, one folder each: `second-perspective-verify/` and `nomos-verify/`. Confirm which one you are working from before running anything.

### A. Second-Perspective Engine (GCAE) — ✅ the engine's own verifier, in `second-perspective-verify/`

`second-perspective-verify/verify.py` **is the independent verification suite of the Second-Perspective Engine** (shipped publicly as GCAE). It loads the engine core (`Second Perspective Engine.py`, a licensed-delivery artifact) and reports **PASS / FAIL / WARN** honestly — it never relaxes an assertion to look good. A `FAIL` is a current defect of the product and must be fixed before any external commitment.

| File | Role |
|------|------|
| `second-perspective-verify/verify.py` | Zero-dependency, offline, pure-stdlib verifier. **19 checks:** V1–V9 cover the engine kernel, V10–V13 the four topology-layer capabilities, V14 the binary fact check, V15 the single extension seam, V16 the ∞ limit reconstructor, V17 the meta-causal ledger plus the autonomous-evolution layer — and V3b and V7b |
| `second-perspective-verify/verify_convergence_fix.py` | Convergence-logic regression (S1–S6) against the same engine |
| `second-perspective-verify/verify-output.log` | Full output of the v1.0 snapshot, archived for the Zenodo deposit |

```bash
# 0 dependencies, Python 3 standard library only (run inside an authorized engine deployment)
python second-perspective-verify/verify.py --root    # print the chain root, compare with the fixed value below
python second-perspective-verify/verify.py           # full suite: the script prints its own PASS / FAIL / WARN totals
```

**On the counts — read this before quoting a number.** The suite prints its own totals at the end of every run, and **those totals, not any frozen figure, are authoritative**. The **v1.0 snapshot baseline is `PASS 9 · FAIL 0 · WARN 2` over 11 checks**; the two WARNs are pre-registered disclosures (V3b, V9), not failures. The suite has since been extended to 19 checks, so any count taken from the baseline must be labelled a **v1.0 snapshot value**. The shipped `verify-output.log` records that snapshot and lets you cross-check the chain root and the PASS / FAIL counts independently.

**Runtime note.** `second-perspective-verify/verify.py` is a **publicly auditable verifier**: its logic is fully visible, zero-dependency and offline-runnable. A complete run loads the engine core — a private implementation, included in the licensed delivery.

Fixed chain root (v1.0 snapshot):
`f5713f49481a80f82356ba1255c0292ddb0d17a235a35348bcff0eef49d6a801`

**Engine-free evidence package — start here.** `second-perspective-verify/evidence/` holds a frozen audit chain, its expected root, and a zero-dependency recomputation script. It runs **without the engine and without a licence**:

```bash
python second-perspective-verify/evidence/recompute.py --tamper
```

This is the one place in this repository where "verify without trusting the vendor" is executable by an outside reader today. It confirms the frozen chain is intact and reproducible; it does not bind the chain to the original input — see the disclosed limitation V3b in that folder's README.

### B. NOMOS Intelligent Decision Hub — ❌ a separate product, in `nomos-verify/`, NOT the engine's verifier

`nomos-verify/VERIFICATION_GUIDE.md` is the third-party verification guide for **NOMOS** ([nohn3043-arch/NOMOS](https://github.com/nohn3043-arch/NOMOS), v0.5.0, 2026-10-08). NOMOS is a **different product** from the Second-Perspective Engine, and this guide does **not** verify the engine.

- Method: `pytest` release evidence (baseline: 507 tests, 91% coverage) plus one replayable evaluation run.
- Its own chain root: `adacff1bd647b7691cf153b5800185b1afbb449de779bebc2847ac1988090a68`.
- Use it only when you are evaluating NOMOS. To evaluate the Second-Perspective Engine, use §A.

## License

Works in this repository are licensed in tiers under the Software License Agreement (`LICENSE`):

- **Individual non-commercial research**: free (download, copy, run, modify, academic citation — with attribution)
- **Government / enterprise / institution**: prior written paid license required

Commercial licensing — International: <ai@nohnlins.com> ｜ China: <lin@secondai.top>

## Product documentation

Each product's **introduction** (README), **glossary** (GLOSSARY), **compliance and conformance** documents, **protocol specifications** (such as the Antares GFSIP protocol spec) and **public specification** (one `SPECIFICATION-zh.md` per product, covering positioning and boundaries, interfaces / protocols / formats, audit and compliance, and conformance statements) are collected under `PRODUCTS/` (index: [PRODUCTS/README.md](./PRODUCTS/README.md)), organised by product for easy retrieval and citation. Each product directory holds introductory and normative documents only — no implementation source.

## Related

- Papers and metadata: Zenodo (see the DOI in the paper)
- Core implementation: private repositories / offline licensed delivery
- Web portal: https://www.nohnlins.com

---
© 2026 Shanghai Linming Junhua Technology Co., Ltd. and NOHN AI TECHNOLOGY PTE. LTD. All rights reserved.
