# Security Policy

## Scope

This repository holds **specifications, verification assets, and documentation** — no
product implementation source, no service, and no runtime. The implementation layer is a
licensed deliverable and lives elsewhere.

The attack surface here is therefore narrow. In scope:

- A defect in a published specification that would lead a correct implementation to behave
  unsafely.
- A flaw in the verification assets (`PRODUCTS/second-perspective/verify/`, `STANDARD/dsl.py`),
  **including any case where a tampered artifact is not detected**. The evidence package is
  designed to fail loudly; a silent pass is a security issue.
- A broken integrity claim: any published hash, chain root, or evidence file that does not
  reproduce as documented.
- Credentials, personal data, or third-party confidential material committed here by mistake.

Out of scope: the behaviour of the private implementation; anything requiring access to it;
and reports that amount to "the specification is not an implementation".

## Reporting

Email **ai@nohnlins.com** with the subject `SECURITY: second-perspective-open`.

Include what you observed, the exact file(s) and commit, the command you ran, and the result
you got versus the result you expected. If a verification check passed when it should have
failed, that is the most useful report we can receive.

We aim to acknowledge within five working days. Corrections are published as new artifacts
with the prior evidence left in the history — we do not edit sealed evidence quietly.

## Please do not

- Open a public issue for an undisclosed defect before we have responded.
- Include real customer data, credentials, or third-party confidential documents in a report.

## No bounty

There is no paid bounty programme. Reports are credited unless you ask otherwise.
