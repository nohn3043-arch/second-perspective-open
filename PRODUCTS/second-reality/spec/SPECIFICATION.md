# Second-Reality (SPL-Virtual-World-Base) Specification

> **Document info**: Version 1.x | Status: runnable infrastructure; geo-distribution is horizon-2 | Author: NOHN AI
> **Basis**: README-zh / GLOSSARY / `system/protocol.py` (JSON-Schema) / Reality Baseline Standard V3.0 / Identity Standard V2.2 / Original Framework Specification
> 中文版本：[`SPECIFICATION-zh.md`](./SPECIFICATION-zh.md)
>
> This specification describes the public specification surface of the **virtual-world and metaverse infrastructure base**: the "constitution—law—bridge" three-tier stack, the reality baseline, account tiers, consensus and audit semantics.

## 1. Scope and Positioning

### 1.1 Positioning

End-to-end account and world runtime: hash-chain ledger, ≥2/3 referendum consensus, demand-driven agents, headless tick loop, REST + WebSocket API; the second-perspective cognitive auditor acts as a neutral referee; AR / edge access; rule genesis locked as a read-only trust root.

### 1.2 Design Boundaries

- Structural reality, not numerical reality;
- True randomness is forbidden: the genesis seed is a public integer, same seed → same world;
- Illusion is only allowed in the representation layer, never enters the execution layer;
- Samsara is implemented as "conservation law + chained causal closure", **never** as a loop (otherwise `trace_chain(depth=-1)` never terminates).

## 2. Terms and Definitions

| Term | Definition |
|---|---|
| Constitution and genesis lock | Genesis rules read-only; anyone can re-run and re-verify |
| Reality Baseline R1–R5 | Reality baselines: genesis lock / global consistency / causal closure / publish-is-execute / complete reaction table |
| Soul hash | Individual identity hash (constant length, see `NOHN_LAW_AXIOMS`) |
| Referendum consensus | ≥2/3 supermajority |
| Original Framework six rules | The six original laws of Chapter −1 (spec in the fifth standard) |
| M1 law-entry discipline | Four requirements for a law to enter the code: producer / consumer / recomputable / boundary clause |
| Conservation residual | Residual measure of economic and energy conservation |

## 3. Core Specification

### 3.1 REST / WebSocket Interface

`GET /health`, `GET /world`, `POST /world/tick`, `GET /world/snapshot`, `GET /audit`, `GET /audit/full`, `POST /agent/spawn`, `POST /protocol/validate`, `/auth/*`, `/credentials/*`, `/aa/*`, `/keys/*`, `POST /identity/root/generate`, `/roaming/*`, `/recovery/*`, `/economy/*`, `/ws/world`.

### 3.2 Storage and Backend

- STORAGE four backends: `sqlite / memory / redis / postgres`.
- Environment: Python ≥ 3.8, depends only on `cryptography` (Ed25519).

### 3.3 Reality Baseline (entry gate, mandatory)

R1 genesis lock / R2 global consistency / R3 causal closure / R4 publish-is-execute / R5 complete reaction table — enforced at entry by `ProtocolValidator`.

### 3.4 Account Tiers (five layers L0–L4)

- L0 identity root → L1 credential → L2 session → L3 graded authorisation → L4 social recovery (3-of-5 + 7-day cancellable time lock).
- Private keys never leave the device; the ledger stores only public keys and hashes.

### 3.5 Law and Constants

- `NOHN_LAW_AXIOMS` is the single authoritative source for shared constants: gravity, time dilation, unit scale, soul-hash length, oracle minimum source count, genesis-entropy seed length, conservation tolerance.
- Five law standards: communication / economy / identity (V2.2 credential recovery) / reality baseline (V3.0) / original-framework specification; machine-readable JSON-Schema in `system/protocol.py`.

### 3.6 Economy and Consensus

- Periodic economy: UBI every 10 ticks, wealth tax every 30 ticks, inflation every 50 ticks, wealth hard cap.
- Consensus: ≥2/3 supermajority referendum.

### 3.7 Geo-Distribution (horizon-2)

- HLC (Hybrid Logical Clock), spatial sharding, AOI incremental sync, Merkle diff merge, layered consensus (real TCP).

## 4. Boundaries and Prohibitions

- Raw data (soul / assets / memory / world state) never leaves the data centre; the protocol layer exchanges only verifiable proofs.
- True randomness is forbidden; samsara must not be implemented as a loop; illusion must not enter the execution layer.
- The bridge only does: semantic cleansing / physical-constant verification / identity verification.
- Disclosed production-hardening gaps: `/keys/rotate` and `/keys/revoke` have no role model, cluster TCP has no TLS and no node auth, default KMS is a file backend, API trusts `X-Forwarded-For` — must be hardened before production deployment.

## 5. Audit and Compliance

- Second-perspective cognitive audit: the compliance-review dimension is 24 dimensions per README/GLOSSARY + NOMOS's 25th dimension second-order causal audit (the architecture diagram states 19 dimensions; there is a discrepancy between documents — the specification follows the README/GLOSSARY wording, and the ambiguity must be resolved in implementation).
- The authentication-security dimension is functionally executed within the isolated in-memory world rather than as a probed property.
- `expert_report.py`: exports the audit verdict and hash anchors into a re-runnable report.

## 6. Conformance Statement

An implementation conforming to this specification should satisfy:

1. Passes `reality_smoke` (40 items) and `frames_smoke` (56 items) validation;
2. Entry enforces the R1–R5 reality baselines;
3. Account tiers and identity / credential / recovery semantics are consistent with §3.4;
4. `NOHN_LAW_AXIOMS` constants are the single authority, not forkable.

## 7. Version and Changes

- Reality Baseline Standard V3.0; Identity Standard includes V2.2 credential-recovery clause; Original Framework Specification is the fifth standard.
- Geo-distribution is a horizon-2 subsystem.

## 8. License and References

- Non-open dual-track license: free for personal non-commercial research; government / enterprise require a written paid license.
- References: README-zh / GLOSSARY / `system/protocol.py` / five law standards.
