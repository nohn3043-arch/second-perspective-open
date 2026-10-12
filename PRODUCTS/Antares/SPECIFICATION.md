# Antares — GFSIP v1.0 Specification

> **Document info**: Version v1.0 (interface frozen, 2026-07-16) | Status: implementation-ready candidate specification | Author: NOHN AI
> **Basis**: `GFSIP_v1.0_protocol_spec.md` (33 sections, authoritative in full), CONFORMANCE-zh, README-zh / GLOSSARY
> 中文版本：[`SPECIFICATION-zh.md`](./SPECIFICATION-zh.md)
>
> This file is the specification index and conformance-declaration entry point for **GFSIP (Global Federated Stable Interoperability Protocol) v1.0**. **The normative text is `GFSIP_v1.0_protocol_spec.md`**; where machine-readable artifacts (JSON Schema / registry / checklist) conflict with the normative text, the normative text prevails.

## 1. Scope and Positioning

### 1.1 Positioning

Provides **encrypted, multiplexed, recoverable cross-domain communication** for services, AI agents, devices and organisations, without a central authority. Uses QUIC as the mandatory transport with deterministic CBOR serialisation; built-in session resumption, idempotent de-duplication and optional causal auditing.

### 1.2 Objectives (eight, §1)

1. Encrypted mutual-authentication Session;
2. Multi-channel isolated multiplexing;
3. Offline recovery;
4. Windowed de-duplication;
5. Structured errors;
6. Optional signed causal events;
7. Multi-trust-root cross-domain interoperability;
8. Single-domain fault isolation.

### 1.3 Non-goals (explicitly listed in §2)

- Does not replace IP / BGP / DNS / QUIC / TLS;
- Provides no globally unique control right; makes no zero-failure promise; provides no communication without a physical path;
- Provides no unbounded-time Exactly Once; does not automatically determine legal liability;
- **Does not automatically interpret temporal order as causality**;
- Requires no globally unique identity root or directory.

## 2. Terms and Definitions

| Term | Definition |
|---|---|
| GFSIP | Global Federated Stable Interoperability Protocol |
| 44-byte fixed header | Wire-format frame header: Magic "GFS1" / Major=1 / Minor=0 / Type / Flags / Header Length / Reserved / Payload Length / 128-bit Session ID / 64-bit Sequence / 32-bit Channel ID |
| Deterministic CBOR | Big-endian, shortest encoding, rejects duplicate Map keys, forbids indefinite-length strings |
| Causal predecessor | Earlier in time / arriving first on the network / same Trace ID do **not** automatically constitute a parent event |
| DomainDescriptor | Domain descriptor, federation-join credential |
| Trust anchor | Set of trust roots for cross-domain interoperability |
| Tier | Core/1 (mandatory), Audit/1 (optional), Federation/1 (optional) |

## 3. Core Specification

### 3.1 Transport and Carriage

- Mandatory: QUIC, ALPN `gfsip/1`; optional: TCP + TLS 1.3.
- Cleartext carriage across hosts: **MUST NOT**.
- `frame_length = 44 + header_length + payload_length`.

### 3.2 Messages and Flags

- 18 standard message types `0x01`–`0x16` (CLIENT_HELLO … STATE_SYNC); `0x17–0x7F` reserved; `0x80–0xFF` private experiment.
- 8-bit Flags: `ACK_REQUIRED / AUDIT_PRESENT / END_CHANNEL / IDEMPOTENT / COMPRESSED / EARLY_DATA`.
- Error registry `gfsip-error-registry.json`: 35 numeric error codes (code is the wire-stable identifier; name is diagnostic only).
- Message schemas: `gfsip-state-machine.json` / `gfsip-message-schema.json`.

### 3.3 Session State Machine

- 8 states: `NEW → NEGOTIATING → AUTHENTICATING → ESTABLISHED → DEGRADED → RESUMING → DRAINING → CLOSED`, with 9 mandatory invariants.
- 0-RTT permits only `PING` and read-only queries; 0-RTT side-effects are forbidden (`EARLY_DATA_REJECTED`).

### 3.4 Channel Rules

- Initiator odd / Responder even; 0 is the control channel; not reused.
- Default resource limits (incl. max negotiated values): max_header 32KiB / max_frame 1MiB / max_channels 128 / max_inflight 64 / max_parent_events 8 / unauthenticated_lifetime 10s / descriptor_size 64KiB / route_max_hops 8.

### 3.5 Authentication and Compression

- Auth methods: `mtls` / `signed-token` / `psk` (closed domains only) / `hardware-attested`.
- Compression: `none` mandatory, `zstd` optional.

## 4. Boundaries and Prohibitions

- A signature only proves the key signed the byte representation; it does not prove a real-world event is true;
- EVENT does not record Payload plaintext by default;
- Gateway must not read end-to-end encrypted business payloads;
- Logs must not record recovery tokens / credentials / private keys;
- Shared credentials may only be anchored to a credential, never to a natural person; recovery must not escalate privileges.

## 5. Audit and Compliance

- Audit/1: signed EVENT (actor / rule_version / state_before / after_hash / logical_clock); rejects self-loops and known loops; default max parent events 8; missing parent event marked `unresolved`.
- §27 conformance statement: the 6 hard requirements to claim `Core Conformant` (fixed frame header / deterministic CBOR / QUIC + gfsip/1 / pass all Core Mandatory tests / publish version and test report / no known unremediated Critical security issue); Audit/1 and Federation/1 must be declared independently.
- §28 nine minimum test vectors (lower bound, not a metric).
- `gfsip-conformance-checklist.csv`: 34 all-Mandatory items (Core 24: CORE-001…024 + FED 6 + AUDIT 4).
- §30 responsibility closure: minimum responsibility unit for 9 decision classes (protocol objective / wire format / state machine / security config / default limits / reference implementation / security conclusion / conformance conclusion / release); where indistinguishable, emit a "responsibility ambiguity zone" statement.
- §29 SPL mapping: E1→E2 state transition, Guard+Action, Hᵢ preconditions, ΔD observable-metric change.

## 6. Conformance Statement (Summary)

Full conformance requirements are in `gfsip-conformance-checklist.csv` (34 Mandatory items). Reference implementation Python `reference-impl/gfsip`: 9/9 conformance passed (author self-test 2026-10-08, Python 3.13.14 / Windows). Independent second implementation in progress; public interoperability report and production pilot domains are TODO.

## 7. Version and Changes

- v1.0 interface frozen (2026-07-16); 9 frozen items in v1.0 (§31, incl. 44-byte frame header, Channel parity rule, 0x01–0x16 semantics, etc.); changes must bump Major.
- 10 known limitations (§32); 12-step implementation order (§33).

## 8. License and References

- **Open license** (distinct from other projects in the ecosystem): code Apache-2.0; specification documents CC BY 4.0; versions up to and including v1.0 are already published in full under CC BY 4.0, irrevocably.
- PyPI package: `gfsip`.
- References: `GFSIP_v1.0_protocol_spec.md` (authoritative), `gfsip-error-registry.json`, `gfsip-state-machine.json`, `gfsip-message-schema.json`, `gfsip-conformance-checklist.csv`.
