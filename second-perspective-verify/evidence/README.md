# Frozen Audit-Chain Evidence — Second-Perspective Engine (GCAE)

This folder lets an outside reader verify **one real audit chain without the engine,
without a licence, and without network access**.

It exists for a single reason: the repository's first sentence is that you should not have
to trust our description. Everywhere else in this repository that promise requires the
engine — which is a licensed-delivery artifact and is **not** here. Here it does not.

---

## Contents

| File | What it is |
|---|---|
| `audit_chain.jsonl` | The frozen chain, one JSON event per line, exported from a real engine run |
| `expected.json` | Expected values: chain root, event count, the hash recipe, the frozen clock and account nonce |
| `recompute.py` | Engine-free recomputation. Zero dependencies, Python 3 standard library only |

---

## Run it

```bash
python recompute.py            # recompute the chain and compare against expected.json
python recompute.py --tamper   # edit one byte on a temporary copy and show it is detected
python recompute.py --json     # machine-readable result
```

Expected output of `python recompute.py --tamper`:

```
events          : 1 (expected 1)
computed root   : 5b0ad8d15c6dfc326758335cd8d58d01ec223abe2f045c5cd93c4a90a21d8ffd
expected root   : 5b0ad8d15c6dfc326758335cd8d58d01ec223abe2f045c5cd93c4a90a21d8ffd
root matches    : True
tamper check    : detected: content tampered at 0
result          : PASS
```

Exit code `0` means the chain reproduced and is intact. Exit code `1` means a mismatch,
a tamper, or a malformed chain.

---

## What this proves

- Every event's content still hashes to the value that was **sealed at append time**.
- Every link points at its predecessor, starting from the sentinel `ROOT`.
- The recomputed root equals the root published in `expected.json`.
- All three, computed by third-party code using the Python standard library only —
  no engine import, no licence check, no clock, no network.

## What this does NOT prove — read before quoting

- **Disclosed limitation V3b: the chain does not bind to the raw input.** It covers the
  derived audit report, not the original decision document. A reader can verify that
  the chain was not altered, but **cannot** independently confirm that it corresponds to
  any particular input. This is stated rather than left for a reader to assume the
  opposite, and it is why the certificate is described as covering the report.
- It is not a statement that the engine is correct or free of defects.
- It is not a certification, an audit opinion, or a warranty.
- No claim about LLM behaviour is verified here.

---

## How the chain is defined

Each event is hashed over exactly five fields:

```python
sha256(json.dumps({
    "event_type": event_type,
    "payload":    payload,
    "prev_hash":  prev_hash,
    "timestamp":  timestamp,
    "nonce":      nonce,
}, sort_keys=True, ensure_ascii=False, default=str).encode("utf-8")).hexdigest()
```

- `index` and `sealed_hash` are **outside** the hashed body — they are chain bookkeeping.
- `prev_hash` starts at the sentinel `ROOT`.
- `sealed_hash` is written once, at append time. The recomputation compares the freshly
  computed hash against it; if an event is edited afterwards, the two differ and the
  chain is rejected.
- The **root** is the last event's `sealed_hash`; an empty chain yields `ROOT`.
- `nonce` is derived deterministically from the previous hash, the event type and the
  index, so the same declared inputs produce the same root.

---

## Provenance

- Exported from a real engine run with frozen clock `1700000000.0` and frozen account
  nonce `deadbeef`, both recorded in `expected.json`.
- The root in `expected.json` is the same value `TESTING.md` documents as the expected
  output of `python verify.py --root` (SPE_VERSION 1.2.2 generation) — the frozen
  evidence reproduces a **previously published** number rather than introducing a new one.
- The chain root is independent of the Python minor version, but it changes with the
  engine's code generation. Recompute it in lockstep with `SPE_VERSION`.
