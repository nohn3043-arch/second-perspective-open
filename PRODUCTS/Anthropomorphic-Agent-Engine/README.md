# Anthropomorphic Agent Engine (AAE) — Public Layer

> English | [简体中文](./README-zh.md)

## What this folder is

AAE is the **anthropomorphic psychology engine** — it gives an AI character a continuous, deterministic, replayable inner-state layer.

This folder is its **public specification layer**: anyone may read the contract, implement it independently, and verify it offline, without a licence. The engine core (`SPL-anthropic-engine.py`) is a licensed deliverable and is **not** in this repository.

| Layer | Content | Visibility |
|---|---|---|
| Public layer (this folder) | Interface contract, machine-readable schemas, third-party verification guide | 🔓 Public |
| Implementation layer (private repo) | Engine core, dynamic coefficients and tuning rationale, test suites | 🔒 Licensed delivery |

## Open boundary

**Open** — the *shape* of the interface:

- Input contract: interoceptive vector fields and ranges, narrative event vocabulary
- State contract: snapshot top-level key sets (main 23 / minor 15), `fluid` 8 keys, `mood` 3 keys, scalar ranges
- Engine entry points: signatures and behaviour of 9 methods
- Audit contract: JSONL envelope, event types, `delta` attribution algorithm
- Determinism preconditions: determinism condition, mood-dynamics form, clock-injection precondition

**Not open** — the *feel* of the implementation:

- Dynamic coefficients, weights and thresholds
- Tuning rationale and calibration method
- Source-level module decomposition and identifiers

> A specification answers "what must hold", not "how we tuned it".

## Layout

```
Anthropomorphic-Agent-Engine/
├── spec/
│   ├── SPECIFICATION-zh.md          # Normative contract (中文)
│   ├── SPECIFICATION.md             # Normative contract (EN)
│   └── schema/
│       ├── snapshot.schema.json     # State contract
│       ├── vector.schema.json       # Input contract
│       └── audit-record.schema.json # Audit contract
├── verify/
│   ├── TESTING-zh.md                # Verification guide (中文)
│   └── TESTING.md                   # Verification guide (EN)
├── GLOSSARY.md                      # Glossary
└── LICENSE                          # Permitted scope
```

## How to verify

1. Read [`spec/SPECIFICATION.md`](./spec/SPECIFICATION.md) for the contract;
2. Validate your implementation's output against [`spec/schema/`](./spec/schema/);
3. Design your own tests and issue your own report per [`verify/TESTING.md`](./verify/TESTING.md).

**Contract conformance (zone A) is verifiable without the engine. Kernel behaviour (zone B) requires a licence.**

## Conformance levels

| Level | Requirement | May claim |
|---|---|---|
| **L0 — Interface** | Satisfies the input contract and entry points | "AAE interface compatible" |
| **L1 — State** | L0 + snapshot key sets and ranges | "AAE state compatible" |
| **L2 — Audit** | L1 + delta algorithm, audit chain recomputable across machines | "AAE conformant" |

> Conformance excludes correctness. The suite is a change detector, not a verdict on psychological validity.

## License

This specification text may be freely cited with attribution. This folder grants **no** licence to any implementation. Commercial / government use requires prior written paid authorisation; see [`LICENSE`](./LICENSE).

**Contact:** International / Global — [ai@nohnlins.com](mailto:ai@nohnlins.com) · China — [lin@secondai.top](mailto:lin@secondai.top)

*Copyright © NOHN AI TECHNOLOGY PTE. LTD.*
