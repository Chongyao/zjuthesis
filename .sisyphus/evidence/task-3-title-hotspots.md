# Task 3: Title Punctuation Hotspots Audit

**Date:** 2026-05-09
**Scope:** Active thesis title commands (`\chapter`, `\section`, `\subsection`, `\subsubsection`, `\paragraph`) containing full-width colon `：`.

---

## Summary

4 active-title hotspots found across 2 active files. 1 additional sub-critical hotspot in paper3 `\paragraph` noted but lower priority.

---

## Hotspot Inventory

### T1: `body/graduate/paper2/main.tex` — Line 3 (CHAPTER LEVEL)

```latex
\chapter{有限元方法中病态网格单元的处理：局部基空间重构与隔离}
```

| Field | Detail |
|-------|--------|
| **File** | `body/graduate/paper2/main.tex` |
| **Line** | 3 |
| **Heading level** | `\chapter` |
| **Title text** | 有限元方法中病态网格单元的处理：局部基空间重构与隔离 |
| **Colon position** | Separates problem domain ("有限元方法中病态网格单元的处理") from solution approach ("局部基空间重构与隔离") |
| **Fixability class** | **source-fixable** — colon can be replaced with whitespace/dash or the title can be rephrased. Change is local to the `\chapter{}` argument. |
| **Config dependency** | **None** — `config/format/general/heading.tex` controls presentation (zihao, beforeskip, etc.) but colon styling is purely in source text. No config-level change needed. |
| **Needs manual layout verification** | Yes — chapter title appears in TOC and page header; verify post-change that line breaks, widows, and page headers remain acceptable. |
| **Reviewer alignment** | Maps to plan's "reviewer items `二.2`, `三.3`, `四.1`" re: title punctuation. |

### T2: `body/graduate/intro/2_related_and_problems.tex` — Line 5 (SUBSECTION LEVEL)

```latex
\subsection{物理量的离散表达：基函数}
```

| Field | Detail |
|-------|--------|
| **File** | `body/graduate/intro/2_related_and_problems.tex` |
| **Line** | 5 |
| **Heading level** | `\subsection` |
| **Title text** | 物理量的离散表达：基函数 |
| **Colon position** | Separates topic ("物理量的离散表达") from specific focus ("基函数") |
| **Fixability class** | **source-fixable** — colon can be removed or replaced. Simple alternatives: "物理量的离散表达——基函数" (em-dash) or restructured. |
| **Config dependency** | None |
| **Needs manual layout verification** | Low priority — short subsection title unlikely to cause TOC or page header issues. |

### T3: `body/graduate/intro/2_related_and_problems.tex` — Line 67 (SUBSECTION LEVEL)

```latex
\subsection{缓解病态性的代数路线：预处理技术}
```

| Field | Detail |
|-------|--------|
| **File** | `body/graduate/intro/2_related_and_problems.tex` |
| **Line** | 67 |
| **Heading level** | `\subsection` |
| **Title text** | 缓解病态性的代数路线：预处理技术 |
| **Colon position** | Separates approach ("缓解病态性的代数路线") from technique ("预处理技术") |
| **Fixability class** | **source-fixable** — same pattern as T2. |
| **Config dependency** | None |
| **Needs manual layout verification** | Low priority. |

### T4: `body/graduate/intro/2_related_and_problems.tex` — Line 81 (SUBSECTION LEVEL)

```latex
\subsection{缓解病态性的表征路线：基函数变换与能量景观重塑}
```

| Field | Detail |
|-------|--------|
| **File** | `body/graduate/intro/2_related_and_problems.tex` |
| **Line** | 81 |
| **Heading level** | `\subsection` |
| **Title text** | 缓解病态性的表征路线：基函数变换与能量景观重塑 |
| **Colon position** | Separates approach from technique, mirroring T3's structure |
| **Fixability class** | **source-fixable** — same pattern as T2/T3. |
| **Config dependency** | None |
| **Needs manual layout verification** | Low priority. |

---

## Additional Observation (Lower Priority)

### T5: `body/graduate/paper3/4_results.tex` — Line 48 (PARAGRAPH LEVEL)

```latex
\paragraph{性能评估：误差--时间曲线}
```

| Field | Detail |
|-------|--------|
| **File** | `body/graduate/paper3/4_results.tex` |
| **Line** | 48 |
| **Heading level** | `\paragraph` |
| **Assessment** | `\paragraph` headings are inline/run-in per ctexrep default. Colon between "性能评估" and "误差--时间曲线" is acceptable as inline punctuation. **Not classified as a hotspot** — `\paragraph` titles are body-text-adjacent and the colon functions naturally as separator within a single compound phrase. |
| **Recommended action** | Monitor only; fix if Task 7 specifically targets paper3 `\paragraph` titles. Otherwise defer. |

---

## Excluded (Backup/Inactive Paths)

| File | Title | Reason Excluded |
|------|-------|-----------------|
| `paper2_backup/main.tex:3` | `\chapter{有限元方法中病态网格单元的处理：数值感知细化与聚合}` | **Backup directory** — not in active build surface |
| `paper3_backup/2_representation.tex:1` | `\section{背景知识：模态综合法与多重划分}` | **Backup directory** |
| `paper3_backup/4_results.tex:66` | `\paragraph{性能评估：误差--时间曲线}` | **Backup directory** |

---

## Config Reference Context

`config/format/general/heading.tex` confirms:
- **Thesis degree** (graduate/dcotor) chapter format: `number=\arabic{chapter}`, `aftername=\space`, `beforeskip=18pt`, `afterskip=18pt`
- Section/subsection numbering: `\arabic{chapter}.\arabic{section}` / `\arabic{chapter}.\arabic{section}.\arabic{subsection}`
- No colon-insertion logic exists in heading config — all colons are in source text.
- **Source-local fixes are the correct approach** — heading config does not inject or style punctuation.

---

## Verification

- [x] All active-title `：` hotspots confirmed via direct source read.
- [x] No backup-only occurrences treated as blockers.
- [x] Config/class heading files confirmed to NOT inject colons.
- [x] Fixability classification applied per hotspot.
