# Task 3: Empty Short-Caption Hotspots Audit

**Date:** 2026-05-09
**Scope:** Active thesis files under `body/graduate/`

---

## Summary

2 empty `\caption[]{}` hotspots found in 2 active intro files. No empty-caption issues in paper2 active files.

---

## Hotspot Inventory

### H1: `body/graduate/intro/1_background.tex` — Line 40

```latex
\caption[]{数值模拟过程与网格离散示意图}
```

| Field | Detail |
|-------|--------|
| **File** | `body/graduate/intro/1_background.tex` |
| **Line** | 40 (within figure env, lines 11–42) |
| **Figure label** | `fig:numerical_simulation_process` |
| **Fixability class** | **source-fixable** — empty short-caption `[]` can be filled with a shorter version of the long caption text |
| **Nearby `\Cref`** | Line 6: `\Cref{fig:numerical_simulation_process}` — **FORWARD reference** (text mentions figure at line 6, but figure appears at lines 11–42). The sentence flow is: "如\Cref{fig:numerical_simulation_process}所示" followed by "全局系统的组装过程..." — this is acceptable forward-looking prose but the empty short caption should be repaired. |
| **Reference flow assessment** | Minor concern: forward `\Cref` before the figure appears. However, the sentence naturally introduces the figure to come, so it's not broken — just flagged for Task 8 consideration. |
| **Needs manual layout verification** | No — caption text change only, no float reflow expected. |

### H2: `body/graduate/intro/3_contributions_and_organization.tex` — Line 121

```latex
\caption[]{论文组织结构示意图}
```

| Field | Detail |
|-------|--------|
| **File** | `body/graduate/intro/3_contributions_and_organization.tex` |
| **Line** | 121 (within figure env, lines 14–123) |
| **Figure label** | `fig:intro_organization` |
| **Fixability class** | **source-fixable** — empty short-caption `[]` can be filled with "论文组织结构" or similar shorter text |
| **Nearby `\Cref`** | Line 125: `\Cref{fig:intro_organization}` — **backward reference** (natural flow: figure at lines 14–123, reference at line 125). The sentence reads: "本文的结构组织为\Cref{fig:intro_organization}, 核心内容包括：" which is natural in-context flow. |
| **Reference flow assessment** | No concern — post-figure reference is natural. |
| **Needs manual layout verification** | No — caption text change only. |

---

## Confirmed: No Empty Captions in Paper2 Active Files

Search for `\caption[]` in `body/graduate/paper2/` returned **0 matches**. All figures in paper2 use proper short-caption forms (e.g., `\caption[Thingi10k 基准测试]{...}` in `5_results.tex:37`).

---

## Reference Flow Summary (all `\Cref` in intro)

| File | Line | `\Cref` Target | Figure Line | Direction |
|------|------|----------------|-------------|-----------|
| `1_background.tex` | 6 | `fig:numerical_simulation_process` | 42 | Forward (text before fig) |
| `2_related_and_problems.tex` | 114 | `fig:intro_coarsening` | 121 | Forward |
| `2_related_and_problems.tex` | 130 | `fig:intro_rod_representation` | 128 | Backward |
| `2_related_and_problems.tex` | 138 | `fig:intro_stiff_soft_rod` | 136 | Backward |
| `2_related_and_problems.tex` | 181 | `fig:intro_sliver_condition` | 172 | Backward |
| `2_related_and_problems.tex` | 206 | `fig:intro_cms_partition` | 199 | Backward |
| `3_contributions_and_organization.tex` | 125 | `fig:intro_organization` | 123 | Backward |

**Assessment:** All intro `\Cref` references have natural flow. The two forward references (`1_background.tex:6` and `2_related_and_problems.tex:114`) use the standard "如\Cref{...}所示" (as shown in...) pattern which is idiomatic in Chinese academic writing and does not require reordering.

---

## Verification

- All hotspots confirmed via direct source read.
- No backup/preview files included.
- Paper2 active files confirmed clean of empty `\caption[]`.
