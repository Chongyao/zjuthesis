# Task 1 — Active Build Surface

**Date:** 2026-05-09
**Source:** Direct inspection of `zjuthesis.tex`, `body/graduate/content.tex`, and all chapter `main.tex` files.

## Build Configuration (from `zjuthesis.tex`)

| Option | Value | Source |
|--------|-------|--------|
| Degree | `graduate` | `zjuthesis.tex:33` |
| Type | `thesis` | `zjuthesis.tex:34` |
| GradLevel | `doctor` | `zjuthesis.tex:40` |
| BlindReview | **`true`** | `zjuthesis.tex:36` |
| ShowCVInBlindReview | `true` | `zjuthesis.tex:37` |
| Language | `chinese` | `zjuthesis.tex:38` |
| MajorFormat | `general` | `zjuthesis.tex:32` |

## Page-Level Inputs (from `\inputgraduate` in `zjuthesis.tex:154-170`)

These are included BEFORE and AFTER the chapter content:

| File | Role | Source |
|------|------|--------|
| `page/graduate/cover.tex` | Cover page | `zjuthesis.tex:157` |
| `page/graduate/previous.tex` | Front matter | `zjuthesis.tex:160` |
| `page/graduate/toc.tex` | Table of contents | `zjuthesis.tex:161` |
| `body/graduate/post.tex` | Post-body content | `zjuthesis.tex:169` |

> Note: `\inputbody{post}` resolves to `body/graduate/post.tex` via the template's `\inputbody` macro convention (`body/graduate/{arg}.tex`).

## Chapter-Level Inputs (Active Build Surface)

All chapters are included via `\inputbody{content}` at `zjuthesis.tex:165`, which resolves to `body/graduate/content.tex`.

### `body/graduate/content.tex` (complete, lines 1-17)

| Line | Directive | Chapter | Status |
|------|-----------|---------|--------|
| 5 | `\inputbody{intro/main}` | Chapter 1: 绪论 | **ACTIVE** |
| 8 | `\inputbody{paper1/main}` | Chapter 2: Cosserat Rod | **ACTIVE** |
| 11 | `\inputbody{paper2/main}` | Chapter 3: 病态网格单元 | **ACTIVE** |
| 14 | `\inputbody{paper3/main}` | Chapter 4: 模态综合法 | **ACTIVE** |
| 17 | `\inputbody{conclusion}` | Chapter 5: 总结与展望 | **ACTIVE** |

### Chapter Sub-Inputs (transitive closure of active `\inputbody` calls)

#### Chapter 1: `body/graduate/intro/main.tex` (lines 1-19)

| Line | Directive | Source File |
|------|-----------|-------------|
| 17 | `\inputbody{intro/1_background}` | `body/graduate/intro/1_background.tex` |
| 18 | `\inputbody{intro/2_related_and_problems}` | `body/graduate/intro/2_related_and_problems.tex` |
| 19 | `\inputbody{intro/3_contributions_and_organization}` | `body/graduate/intro/3_contributions_and_organization.tex` |

#### Chapter 2: `body/graduate/paper1/main.tex` (lines 1-11)

| Line | Directive | Source File |
|------|-----------|-------------|
| 7 | `\inputbody{paper1/1_intro}` | `body/graduate/paper1/1_intro.tex` |
| 8 | `\inputbody{paper1/2_representation}` | `body/graduate/paper1/2_representation.tex` |
| 9 | `\inputbody{paper1/3_simulation}` | `body/graduate/paper1/3_simulation.tex` |
| 10 | `\inputbody{paper1/4_results}` | `body/graduate/paper1/4_results.tex` |
| 11 | `\inputbody{paper1/5_conclusion}` | `body/graduate/paper1/5_conclusion.tex` |

> Plus any `\inputbody` calls within these sub-files (e.g., appendix files referenced from `paper1/3_simulation.tex` or `paper1/4_results.tex`).

#### Chapter 3: `body/graduate/paper2/main.tex` (lines 1-10)

| Line | Directive | Source File | Status |
|------|-----------|-------------|--------|
| 5 | `\inputbody{paper2/1_intro}` | `body/graduate/paper2/1_intro.tex` | **ACTIVE** |
| 6 | `%\inputbody{paper2/2_related}` | `body/graduate/paper2/2_related.tex` | **COMMENTED OUT** |
| 7 | `\inputbody{paper2/3_background}` | `body/graduate/paper2/3_background.tex` | **ACTIVE** |
| 8 | `\inputbody{paper2/4_method}` | `body/graduate/paper2/4_method.tex` | **ACTIVE** |
| 9 | `\inputbody{paper2/5_results}` | `body/graduate/paper2/5_results.tex` | **ACTIVE** |
| 10 | `\inputbody{paper2/6_summary}` | `body/graduate/paper2/6_summary.tex` | **ACTIVE** |

#### Chapter 4: `body/graduate/paper3/main.tex` (lines 1-8)

| Line | Directive | Source File |
|------|-----------|-------------|
| 3 | `\inputbody{paper3/1_intro}` | `body/graduate/paper3/1_intro.tex` |
| 4 | `\inputbody{paper3/2_foundation}` | `body/graduate/paper3/2_foundation.tex` |
| 5 | `\inputbody{paper3/2_representation}` | `body/graduate/paper3/2_representation.tex` |
| 6 | `\inputbody{paper3/3_simulation}` | `body/graduate/paper3/3_simulation.tex` |
| 7 | `\inputbody{paper3/4_results}` | `body/graduate/paper3/4_results.tex` |
| 8 | `\inputbody{paper3/5_conclusion}` | `body/graduate/paper3/5_conclusion.tex` |

#### Chapter 5: `body/graduate/conclusion.tex`

| Directive | Source File |
|-----------|-------------|
| `\inputbody{conclusion}` (standalone) | `body/graduate/conclusion.tex` |

> No further sub-inputs verified; transitive `\inputbody` calls within this file have not been enumerated.

## Summary: Approved Build Surface

Every `.tex` file transitively reachable from the `\inputbody` directives listed above is part of the active build surface and may be edited. This includes:

1. **Page files:** `page/graduate/{cover,previous,toc}.tex`, `body/graduate/post.tex`
2. **Intro:** `intro/{1_background,2_related_and_problems,3_contributions_and_organization}.tex`
3. **Paper 1:** `paper1/{1_intro,2_representation,3_simulation,4_results,5_conclusion}.tex` + transitively included sub-files
4. **Paper 2:** `paper2/{1_intro,3_background,4_method,5_results,6_summary}.tex` (EXCLUDING `2_related`)
5. **Paper 3:** `paper3/{1_intro,2_foundation,2_representation,3_simulation,4_results,5_conclusion}.tex`
6. **Conclusion:** `conclusion.tex`
7. **Config:** `config/paper1_macros.tex`, `config/paper3_macros.tex`, `config/format/`, `config/packages.tex`
8. **Bibliography:** `body/ref.bib`
