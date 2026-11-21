# aiverify-plugin — Second Perspective Gate (interface draft)

> Status: **scaffold / interface draft**. This folder packages the Second Perspective
> Engine's gate verdict as an AI Verify test-plugin component. It is *not yet*
> aligned with the official cookiecutter templates in
> [`aiverify-developer-tools`](https://github.com/aiverify-foundation/aiverify-developer-tools)
> (v2.x alpha, `aiverify-test-engine==2.0.0a1`); alignment is planned before any PR
> upstream — see the pending question in our issue.

## What it does

Maps the SPE audit level to an explicit gate decision, fail-closed:

| SPE ACC verdict level | Gate decision |
|---|---|
| `AUDIT_PASS` | `RELEASE` |
| `AUDIT_WARN` | `HOLD` |
| `AUDIT_HALT` | `BLOCK` |
| missing / malformed | `BLOCK` (fail-closed) |

## Two modes

- **post-hoc (shipped here)** — verifies an engine-produced credential view and
  extracts the gate decision. Runs engine-free, stdlib-only, fully offline, and is
  deterministic: identical input → identical output, byte-stable `gate_digest`.
  Try it: `python -m unittest discover -s tests` (Python 3.10+, no dependencies).
- **inline (licensed delivery)** — with the private SPE engine available, the
  operator runs the engine *before* an output acts on the world and feeds its
  report here. The mapping above is identical in both modes.

## Layout

```
aiverify-plugin/
├── plugin.meta.json              # plugin metadata (official v2 contract)
├── pyproject.toml                # Apache-2.0, zero runtime dependencies
├── second_perspective_gate/      # algorithm component
│   ├── __init__.py
│   ├── algo.py                   # Plugin class w/ generate(); gate logic is deterministic, stdlib-only
│   ├── algo_init.py              # input_arguments wiring (official v2 contract, draft)
│   ├── plugin_init.py            # CLI arguments wiring (official v2 contract, draft)
│   ├── input.schema.json         # custom arguments (official v2 semantics)
│   ├── report.schema.json        # data schema: SPE credential-view report
│   └── output.schema.json        # gate verdict record
├── second_perspective_widget/    # widget component (placeholder, pending template)
├── data/                         # frozen samples copied from ../../verify/evidence/
│   ├── sample_decision_input.json
│   └── sample_report.json
└── tests/
    └── test_gate.py              # determinism · fail-closed · tamper sensitivity
```

Run the tests: `python -m unittest discover -s tests -v` (stdlib; also passes
under `pytest tests` per the official template's test convention).

## Alignment with the official template

| Official contract (aiverify-algorithm-template) | This scaffold |
|---|---|
| cookiecutter-generated project | hand-written draft with the same file layout; cookiecutter pass pending |
| `plugin.meta.json` + `pyproject.toml` | ✅ present |
| `Plugin.generate()` fills `self._results` | ✅ implemented (host-injected instances via `setup()`) |
| `input.schema.json` = custom arguments | ✅ (`require_anchor`) |
| `algo_init.py` / `plugin_init.py` wiring | ✅ drafted |
| data schema for the input payload | ✅ `report.schema.json` (SPE credential view) |
| e2e tests under `tests/e2e` | ⏳ pending (needs the `aiverify-test-engine` host) |
| license choice | Apache Software License 2.0 |

## Licensing layers

| Layer | License |
|---|---|
| This plugin scaffold (gate interface, schemas, tests, samples) | intended **Apache-2.0** (required for AI Verify ecosystem contribution) |
| SPE engine core, LLM adapters | private / licensed delivery (dual-track, see root `LICENSE`) |
| Public specs, language standard, frozen evidence | see root `LICENSE` of this repository |

The split follows the repository's standing model: specs public, implementation
private, certification as backstop. Only the plugin interface layer is intended to
move under Apache-2.0.

## Disclosure

All published evaluation figures for the engine (including the 95/100 AI Verify
self-assessment referenced in `CERTIFICATIONS/`) are **provider self-tests**.
There is **no third-party certification** of SPE today, and nothing in this folder
should be read as an IMDA-issued statement.
