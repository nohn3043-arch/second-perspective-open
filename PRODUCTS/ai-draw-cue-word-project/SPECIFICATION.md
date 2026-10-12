# AI Drawing Composition Detail Template Specification

> **Document info**: Version v2.8 | Status: data standard separated from workbench | Author: NOHN AI
> **Basis**: README-zh / GLOSSARY / 21 CSV sub-tables
> 中文版本：[`SPECIFICATION-zh.md`](./SPECIFICATION-zh.md)
>
> This specification describes the public specification surface of the **AI drawing composition detail template — weight & ratio precision-control edition**: data-table structure, weight semantics, five-step workflow and cross-model syntax red lines. The 21 CSV tables are the single source of truth.

## 1. Scope and Positioning

### 1.1 Positioning

A quality-control workbook for building high-consistency character prompts across five major prompt-grammar systems (originally a Tencent-Docs online spreadsheet, now a versioned export saved as plain CSV):
Natural-language flow (Flux / DALL·E 3 / SD3), conversational (GPT-4o / Gemini), Midjourney / Niji, Stable Diffusion, domestic APIs (Jimeng / Kling / Doubao / Tongyi Wanxiang).

### 1.2 Setup

- The setting layer is common; the grammar layer differs by model;
- Adaptable to all models.

## 2. Terms and Definitions

| Term | Definition |
|---|---|
| Hard anchor | Immutable feature with weight ≥ 1.6 |
| Core feature | Weight 1.3–1.5 |
| Negative word library | Negative-prompt list |
| Temporal consistency | Character / clothing / lighting unchanged between two images |
| P0 / P1 / P2 | Validation priority: P0 hard gate, P1 one retry allowed, P2 record for next-round improvement |
| Iteration log | 3 consecutive failures of the same kind → switch model or parameter route |
| Ratio baseline | Head-to-body ratio standard, tolerance ≤ 5% |

## 3. Core Specification

### 3.1 Data Tables (21 CSV)

Core sub-tables: `CharacterAnchors.csv`, `NaturalLanguagePromptTemplate.csv`, `Checklist.csv`, `GenerationIterationLog.csv`, `AspectRatioBaselines.csv`, `TemporalConsistencyChecklist.csv`, `PanelLayoutRules.csv`, `SpeechBubblePositioning.csv`, `StoryboardSkeletonTemplate.csv`, `ChangeLog.csv`, etc. (full list in README "sub-table overview").

### 3.2 Weight Semantic Ranges (SD / MJ numeric system)

| Range | Semantics |
|---|---|
| 1.6 – 2.0 | Hard anchor (immutable feature) |
| 1.3 – 1.5 | Core feature |
| 1.0 – 1.2 | Baseline |
| 0.7 – 0.9 | Atmosphere aid |
| < 0.7 | Weak prompt |

### 3.3 Ratio Baseline (head-to-body)

Q-version 2–3; loli 4–5; girl 6–6.5; youth 6.5–7; adult 7–8; realistic 7.5+.

### 3.4 Consistency Validation

- `TemporalConsistencyChecklist.csv`: 6 categories, 13 checks (incl. severity / check timing / pass criteria / fix protocol).
- Shot continuity: 180-degree axis / 30-degree rule / eyeline match.

### 3.5 Workflow (five steps)

Anchor character → choose model and reference strategy → assemble prompt → P0 / P1 / P2 validation → record iteration.

### 3.6 Online Workbench

- www.nohnlins.com/ai-draw/; from v2.8 supports dragging Word / TXT + mammoth.js to parse .docx;
- Enterprise IP preset library JSON import / export; localStorage persistence.

## 4. Boundaries and Prohibitions (cross-model syntax red lines)

- Weight syntax `(word:1.3)` valid only for SD;
- MJ `--no` limited to 4–6 words; MJ `--cref` v6 only;
- DALL·E 3 has no reference image, and deprecates multi-image series;
- Natural-language models forbid bracketed weights; forbid anchor synonym substitution;
- FLUX.2 and Gemini 3 Pro Image do not support negative prompts at all.

## 5. Audit and Compliance

- `ChangeLog.csv` records template revision history.
- License: Apache License 2.0; Copyright (c) 2026 NOHN AI TECHNOLOGY PTE LTD.

## 6. Conformance Statement

A template conforming to this specification should satisfy:

1. The 21 CSV table structures and the semantics described here are consistent;
2. The weight semantic ranges and red-line rules (§3.2, §4) are consistent;
3. P0 failure voids the image → must regenerate (hard gate).

## 7. Version and Changes

- v2.8 (current); history: v2.3 (domestic API family / DALL·E 3 deprecation note) → v2.4 (pose–emotion cross-reference table) → v2.5 (video / multi-character / LoRA / 3D / conversational editing, +5 tables) → v2.6 (storyboard skeleton) → v2.7 (comic mode, +3 tables) → v2.8; table count 12 → 17 → 18 → 21.

## 8. License and References

- Apache License 2.0.
- References: README-zh / GLOSSARY / 21 CSV sub-tables.
