# PAGES Specification

> **Document info**: Version 1.x | Status: static site, no build step | Author: NOHN AI
> **Basis**: README.md
> 中文版本：[`SPECIFICATION-zh.md`](./SPECIFICATION-zh.md)
>
> This specification describes the public specification surface of the **official landing page for the NOHN AI technology ecosystem**: site architecture, visual language, deployment and navigation conventions.

## 1. Scope and Positioning

### 1.1 Positioning

A unified entry point for the NOHN AI technology ecosystem, presenting the ecosystem's core projects in a minimalist white-luxury visual language, providing a zero-cost, high-readability project navigation portal.

### 1.2 Ecosystem Cards (six)

SPL Virtual-World Base (online demo `/second-reality/`), SPL-G1 processor (hardware causal-audit TCU, `/spl-g1/`), Anthropomorphic Agent Engine (`/your-soulmate/` demo), NOMOS (IMDA AI Verify 95/100), Story Engine, Antares · GFSIP (v1.0, implementation-ready).

### 1.3 Feature Zones

- SPL cognitive-audit engine: neutral, offline, decision-independent, 100% client-side in the browser (`/audit/`), "no data leaves the machine";
- AI drawing composition templates (`/ai-draw/`).

## 2. Terms and Definitions

| Term | Definition |
|---|---|
| White-luxury | white-luxury: minimalist white + gold-accent visual language |
| Deep Mode | Deep mode: switches to professional second-perspective causal terminology (deterministic execution kernel / immutable invariant set / append-only ledger / SHA-256 provenance), accent colour shifts to purple |
| Second-perspective causal terminology | The ecosystem-wide deterministic / audit terminology set |

## 3. Core Specification

### 3.1 Tech Stack and Deployment

- Pure static HTML + CSS; no build step, no framework.
- Local run: `python serve.py [PORT]` (default 8000), or any static server.
- Deployment targets: GitHub Pages / SourceForge Pages (incl. CNAME).

### 3.2 Theme and Styles

- Fonts: Cormorant Garamond / Noto Serif SC (serif); Manrope / Noto Sans SC (sans).
- Accent colour: `--gold: #b8954a` (defined in `:root`).

### 3.3 Interaction Conventions

- In-page EN / ZH toggle with persistence;
- Deep Mode switch (toggles professional terminology and purple accent).

### 3.4 Site Structure (Cloudflare Pages)

- `functions/`: Cloudflare Pages Functions (API + OAuth);
- `worker/`: background worker;
- `schema/`: data schemas; `seed/`: seed data;
- `wrangler.toml`: Cloudflare Pages configuration.

### 3.5 Information Architecture

Sub-project directories: `ai-draw/`, `audit/`, `nomos/`, `second-reality/`, `spl-g1/`, `story-engine/`, `your-soulmate/`, `docs/`, `forum/`, `login/`, `contact/`, `tax-audit/`, `agents.html`.
Privacy companion pages: `character-studio-privacy.html`, `story-engine-privacy.html`.

## 4. Boundaries and Prohibitions

- Static site: no build step, no framework;
- Cognitive-audit engine is decision-independent, fully client-side (offline, data does not leave the machine).

## 5. Audit and Compliance

- Site content and design language are original works;
- Underlying projects follow the dual-track license model (free personal research / paid commercial); see each project's LICENSE;
- Licensing channels: international / global `ai@nohnlins.com`; China `lin@secondai.top`.

## 6. Conformance Statement

A page conforming to this specification should satisfy:

1. Based on the white-luxury visual language, with accent colour and fonts per §3.2;
2. Displays the ecosystem cards and feature zones (§1.2 / §1.3);
3. Supports bilingual toggle with persistence, and Deep Mode;
4. No build step; hostable by any static server.

## 7. Version and Changes

- Ecosystem-member status tracks upstream projects (Second-Perspective GCAE five operators, NOMOS, Antares GFSIP v1.0, Anthropomorphic-Agent-Engine SPL Pure Core V8.0).

## 8. License and References

- Site original content follows the dual-track license; underlying project licenses are in their respective LICENSE files.
- References: README.md / site directory structure.
