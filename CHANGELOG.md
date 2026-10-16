# Changelog — second-perspective-open

Notable changes to **this repository** (the public trust layer). Implementation-layer changes
are recorded in the respective product repositories.

## [0.1.1] - 2026-10-14

### Changed

- **Specifications and introductions merged into one folder per product.** The parallel tree is
  gone: each product now holds its description at `PRODUCTS/<product>/` and its public
  specification at `PRODUCTS/<product>/spec/`. Previously they sat in two sibling trees
  (`PRODUCTS/<product>/` and `SPEC/<product>/`), which made it unclear which one to read.
- **Top-level `SPEC/` renamed to `STANDARD/`.** It carries the decision-structure language
  standard only — the one specification that is not a product document, published together with
  its reference interpreter (`dsl.py`). The old name competed with the per-product `spec/`
  folders.

### Removed

- `PRODUCTS/Anthropomorphic-Agent-Engine/` and its specification: this product's core design and
  implementation parameters are not published. The index records it under "not in the public
  layer" rather than leaving a dead link.
- Empty directories left behind by the moves.

## [0.1.0] - 2026-10-13

### Added

- `second-perspective-verify/evidence/` — a frozen evidence package verifiable **without the
  engine and without a licence**: canonical input, canonical report view, frozen audit chain,
  published expectations, and a zero-dependency `recompute.py`. Six checks bind
  input → report hash → chain root; edits to the input, the report view and the chain are each
  demonstrated as detected.
- `SECURITY.md` — scope and reporting route.
- Scope notes on the licensed-deliverable `clone` instructions in the product READMEs.

### Changed

- `second-perspective-verify/verify.py` — the V3b check no longer reports a hard-coded WARN. It
  decides from its own measurement, and its probe now uses a field **that no operator observes**,
  so it tests input binding rather than operator sensitivity.
  Result: `PASS 19 · FAIL 0 · WARN 0`.
- Ecosystem tables in the product READMEs no longer point at repositories a reader cannot reach;
  where the implementation is a licensed deliverable they point at the corresponding public
  specification in this repository.

### Known

- `nomos-verify/VERIFICATION_GUIDE.md` describes NOMOS verification. It is published here for
  reference; it does not run from this repository (see the scope note at its head).
- `PAPERS/paper.md` records the results of the SPE 1.2.0 run of 2026-10-10 (`PASS 18 · FAIL 0 · WARN 1`).
  That is a historical record of that generation and is left as published. The current suite (SPE 1.2.2)
  reports `PASS 19 · FAIL 0 · WARN 0`, chain root `5b0ad8d1…` — see `PRODUCTS/second-perspective/TESTING.md`.
