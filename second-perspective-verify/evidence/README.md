# Frozen Evidence Package — Second-Perspective Engine (GCAE)

This folder lets an outside reader verify one real audit chain **without the engine,
without a licence, and without network access**.

It exists for a single reason: this repository's first sentence is that you should not
have to trust our description. Everywhere else that promise needs the engine — a
licensed-delivery artifact that is **not** here. Here it does not.

---

## Contents

| File | What it is |
|---|---|
| `decision_input.json` | The frozen input, stored in canonical form |
| `report_credential_view.json` | The frozen report, reduced to its credential view |
| `audit_chain.jsonl` | The frozen chain, one JSON event per line |
| `expected.json` | Published expectations: chain root, input digest, report hash, recipes |
| `recompute.py` | Engine-free verification. Zero dependencies, Python 3 standard library only |

---

## Run it

```bash
python recompute.py            # run all six checks against expected.json
python recompute.py --tamper   # also show that edits to each artifact are detected
python recompute.py --json     # machine-readable result
```

Expected output:

```
events          : 1 (expected 1)
chain root      : 5b0ad8d15c6dfc326758335cd8d58d01ec223abe2f045c5cd93c4a90a21d8ffd
input digest    : 239557acd02723e4a43c6d7e33d195ea5d829bd466666b62bce245e7bf82ac92
report hash     : b3adf8f636646370

  C1_chain_integrity     pass
  C2_chain_root          pass
  C3_input_binding       pass
  C4_input_in_report     pass
  C5_report_binding      pass
  C6_report_on_chain     pass

  tamper input file   detected: C3_input_binding
  tamper report view  detected: C5_report_binding
  tamper chain file   detected: C1 content tampered at 0

result          : PASS
```

Exit code `0` means every check passed. Exit code `1` means a mismatch, a tamper, or a
malformed chain.

---

## What the six checks establish

| Check | Question it answers |
|---|---|
| C1 | Does every event still hash to the value sealed at append time, with every link pointing at its predecessor? |
| C2 | Does the last sealed hash equal the published root? |
| C3 | Does `decision_input.json` hash to the digest published in `expected.json`? |
| C4 | Does the published report view carry that same input digest, at `analysis.ACC.certificate.input_digest`? |
| C5 | Does `report_credential_view.json` hash to the report hash published in `expected.json`? |
| C6 | Does the chain itself carry that same report hash? |

Together they bind four artifacts — **input, report view, chain, published root** — to one
another, and every one of those links is recomputable by third-party code using the
standard library alone.

---

## What this does NOT prove — read before quoting

- It does **not** show that the report was derived honestly from the input. It verifies
  the record, not the reasoning. The engine's operators are not re-executed here.
- It is not a statement that the engine is correct or free of defects.
- It is not a certification, an audit opinion, or a warranty.
- No claim about LLM behaviour is verified here.

---

## How the artifacts are defined

**Input digest.** `sha256` of the bytes of `decision_input.json`, which is stored in
canonical form (keys sorted, UTF-8, no trailing newline). This digest is computed by the
engine over the input it was handed, written into the report at `analysis.ACC.certificate.input_digest`, which sits in the
credential view — so it reaches the chain root without the input itself ever being written
to the chain.

**Report hash.** The report is reduced to its **credential view** — the report with
`llm_calls`, `narrative_hash` and `analysis.llm_narrative` removed — and hashed:

```python
sha256(json.dumps(credential_view, sort_keys=True, ensure_ascii=False,
                  default=str).encode("utf-8")).hexdigest()[:16]
```

The removal is unconditional, which is what makes the chain root identical whether or not
LLM enhancement is enabled. `report_credential_view.json` is published as the exact
canonical text that was hashed.

**Event hash.** Each event is hashed over exactly five fields:

```python
sha256(json.dumps({
    "event_type": event_type,
    "payload":    payload,
    "prev_hash":  prev_hash,
    "timestamp":  timestamp,
    "nonce":      nonce,
}, sort_keys=True, ensure_ascii=False, default=str).encode("utf-8")).hexdigest()
```

`index` and `sealed_hash` are outside the hashed body. `prev_hash` starts at the sentinel
`ROOT`. `sealed_hash` is written once at append time; the recomputation compares the
freshly computed hash against it, so any later edit is rejected. The **root** is the last
event's `sealed_hash`; an empty chain yields `ROOT`.

**Binding path.**

```
decision_input.json  →  input_digest  →  report  →  credential view  →  report_hash
                                                                              ↓
                                                                    chain event payload
                                                                              ↓
                                                                         chain root
```

---

## Provenance

- Frozen from a real engine run with clock `1700000000.0` and account nonce `deadbeef`,
  both recorded in `expected.json`.
- The chain root changes whenever the engine's code generation changes, and it changed
  when input binding was added. Recompute it in lockstep with `SPE_VERSION`.
- The chain root is independent of the Python minor version.
