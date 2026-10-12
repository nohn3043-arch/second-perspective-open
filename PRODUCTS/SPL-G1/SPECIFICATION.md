# SPL-G1 Specification

> **Document info**: Version v1.0 (public specification) | Status: Phase A delivered; specification evolves with implementation | Author: NOHN AI
> **Basis**: `SPL-Core.json` (ISA v1.0.0-Commercial: SPL-TCU-G1), `State_Anchor.pdl`, `Materica-specification`, README-zh, IMPROVEMENT_PLAN v5.1
> 中文版本：[`SPECIFICATION-zh.md`](./SPECIFICATION-zh.md)
>
> This specification describes the public specification surface of the SPL-G1 **hardware causal-audit Trusted Compute Unit (TCU)**: instruction set, data structures, arbitration protocol, audit semantics and fusing behaviour. The core-engine RTL and process-library implementation are confidential deliverables and are not disclosed in this specification.

## 1. Scope and Positioning

### 1.1 What it is / is not

| ✅ Is | ❌ Is not |
|---|---|
| Hardware causal-audit Trusted Compute Unit (TCU) | A desktop CPU running Linux / x86 applications |
| Verifiable compute primitive with full-lifecycle P→Q traceability | A GPU with thousands of cores and a CUDA ecosystem |
| Tri-mode PIM array (SCALAR / VECTOR / MATRIX), every operation auditable | A data-centre-grade NPU accelerator for LLM inference |
| Embedded security root for compliance computing, safety-critical auditing and proof-class workloads | A replacement for any mainstream microprocessor |

### 1.2 Scope of Application

Applies to security scenarios requiring hardware-level causal auditing: industrial safety-audit nodes, compliance computing, supply-chain traceability, provable-compute workloads. No tape-out within two years; the design deliverable is an M4 synthesis-evaluation report and supporting toolchain.

## 2. Terms and Definitions

| Term | Definition |
|---|---|
| TCU | Trusted Compute Unit |
| PIM | Processing-In-Memory |
| P→Q causal pair | The auditable causal pair output by every operation: precondition P holds, postcondition Q follows from P |
| RA-BUS | Unified-address bus, four targets: PIM / Audit / Identity / External |
| dep_mask | 56-bit dependency mask, characterising inter-instruction dependencies |
| Cascading failure | Any audit failure on a dependency chain triggering downstream cascading failure |
| SBC fuse | Self-Breaking Circuit, irreversible fuse; on audit failure it fuses and output is permanently zeroed |
| Materica #4 | Material causal-mapping rule 4: audit failure → fuse blows → output zeroed |
| Identity anchor | 256-bit hardware identity, 64-cycle bit-by-bit handshake verification |

## 3. Core Specification

### 3.1 Instruction Set (ISA)

- Authoritative definition: `SPL-Core.json`, v1.0.0-Commercial, processor model `SPL-TCU-G1`.
- A restricted C subset compiled by `splcc` v0.1 into microcode CONFIG words (`int` variables, `for` / `while` / `if-else`, arithmetic, comparison).
- Sequencer v4: 256-entry program memory; control-flow instructions `JMP / JZ / JNZ / CALL / RET / HALT`; 8-level return stack; out-of-bounds protection.

### 3.2 Compute Array

- 2D PIM array: 4×4 grid (scale ladder L0), expandable to L1 (16×16 = 256 cells), L3 (262144 cells).
- Cell v2: 64-bit local storage + 32-operand ALU; 8-bit neighbour interconnect; per-column `vec_sum`; full-array `mat_total` reduction.
- Three execution modes: `SCALAR / VECTOR / MATRIX`.
- True FP16 (IEEE 754 half precision): sign / 5-bit exponent / 10-bit mantissa; subnormals, NaN, ±Inf; rounding `roundTiesToEven`; semantics `FP16_ADD / SUB / MUL / CMP / MAC`.

### 3.3 RA-BUS Arbitration Protocol

- v1: 4-target address-decode bus (PIM / Audit / Identity / External).
- Transaction types: `READ / WRITE / EXECUTE / CONFIG`.
- Audit-constraint mask, 64-bit CONFIG programmable: bit0 integer ALU / bit1 FP16 / bit2 VECTOR / bit3 MATRIX; default all 1 (bridge pass-through mode, backward compatible).

### 3.4 Identity and Fusing

- Identity anchor v1: 256-bit hardware identity, 64-cycle bit-by-bit handshake.
- SBC fuse: audit failure → `fuse_blown` latch → `ra_rdata` forced to zero → output permanently zeroed; only hardware reset `rst_n` can recover.
- Audit is a hardware property, not a software feature: in bridge pass-through mode `constraint_bits` all 1 → always passes.

### 3.5 Causal-Constraint Verification

- `spl_cim_causal_unit` (v2) hard-constraint check:
  `constraint_pass = (constraint_bits == 64'hFFFF_FFFF_FFFF_FFFF)`
- 56-bit `dep_mask` dependency check, including cascading-failure propagation.

### 3.6 Materials and Process (PDK)

- PDK values are literature-calibrated reference values; must be replaced by a foundry PDK before tape-out.
- Three PDK packages: `silicon_cim_v1.json` (28nm CIM, 3 variants), `optical_mzi_photonics_v1.json` (photonics, 3 variants), `rram_crossbar_v1.json` (RRAM, 3 variants).

## 4. Boundaries and Prohibitions

- Does not replace general-purpose microprocessors; provides no software-stack compatibility.
- No tape-out within two years; deliverables stop at M4 synthesis evaluation.
- Output is unrecoverable after fusing (except hardware reset); the designer must not provide a bypass path.

## 5. Audit and Compliance

- Audit failure → SBC fuse → PIM output cut; the audit channel and identity channel remain readable (e.g. Test 9 closed loop: forbid FP16 → execute FP16_ADD → audit reject → `fuse_blown=1`).
- Attestation: remote attestation supported.
- RTL simulation baseline: Icarus Verilog, Phase-A full suite 0 errors, 7/7 tests PASS.
- Toolchain: EDA (parse → map → export → RTL generation, incl. SVA assertions and TCL synthesis scripts).

## 6. Conformance Statement

An implementation conforming to this specification should satisfy:

1. Implements the SPL-TCU-G1 instruction set defined in `SPL-Core.json` and the `State_Anchor.pdl` identity-anchor protocol;
2. RA-BUS four-target addressing and four transaction-type behaviours are consistent;
3. Causal-constraint verification, cascading failure and SBC fuse semantics are consistent with §3.4/§3.5;
4. Passes the corresponding Phase-A test cases (A1 control-flow / A2 true FP16 / A3 splcc / A4 data-channel / A5 causal-constraint / A6 SBC fuse).

## 7. Version and Changes

- Phase A capability milestones all complete; IMPROVEMENT_PLAN v5.1 (2026-08-25); EDA toolchain v1.1.
- Milestones: M1 baseline → M2 splcc → M3 16×16 Tile → M4 Yosys synthesis evaluation (L1 level 16×16=256 cells, 32-operator industrial audit pipeline fully mapped, delay=22.7ns).

## 8. License and References

- Dual-track license (non-open): free for personal non-commercial research; government / enterprise require a written paid license; patent applied (PCT).
- References: README-zh / GLOSSARY / IMPROVEMENT_PLAN / `SPL-Core.json` / `State_Anchor.pdl` / `Materica-specification`.
