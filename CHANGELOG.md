# Changelog — second-perspective-open

Notable changes to **this repository** (the public trust layer). Implementation-layer changes
are recorded in the respective product repositories.

## [2026-10-13]

### Added

- `second-perspective-verify/evidence/` — a frozen evidence package verifiable **without the
  engine and without a licence**: canonical input, canonical report view, frozen audit chain,
  published expectations, and a zero-dependency `recompute.py`. Six checks bind
  input → report hash → chain root; edits to the input, the report view and the chain are each
  demonstrated as detected.
- `SPEC/README.md` — index of the public specification surface, one folder per product.
- `SECURITY.md` — scope and reporting route.
- Scope notes on the licensed-deliverable `clone` instructions in the product READMEs.

### Changed

- **Specifications moved** from `PRODUCTS/<product>/` to `SPEC/<product>/`. `PRODUCTS/` now
  holds introductions, glossaries, changelogs and architecture/test notes only. Cross-links
  updated throughout, including both top-level READMEs.
- `second-perspective-verify/verify.py` — the V3b check no longer reports a hard-coded WARN.
  It decides from its own measurement, and its probe now uses a field **that no operator
  observes**, so it tests input binding rather than operator sensitivity.
  Result: `PASS 19 · FAIL 0 · WARN 0`.
- Ecosystem tables in the product READMEs no longer point at repositories a reader cannot
  reach; where the implementation is a licensed deliverable, they point at the corresponding
  public specification in this repository.

### Known

- `nomos-verify/VERIFICATION_GUIDE.md` describes NOMOS verification. It is published here for
  reference; it does not run from this repository (see the scope note at its head).
- `PAPERS/paper.md` records the results of the v1.0 snapshot run (`PASS 18 · FAIL 0 · WARN 1`).
  That is a historical record of that snapshot and is left as published.
