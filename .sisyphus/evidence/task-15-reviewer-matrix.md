# Task 15 Reviewer Matrix

Date: 2026-05-10  
Plan: `blind-review-direct-fixes`

## Source of truth

- Direct-fix subset: [`blind-review-comments.md`](../../blind-review-comments.md)
- Scope lock: [`task-1-build-surface.md`](task-1-build-surface.md), [`task-1-exclusions.md`](task-1-exclusions.md)
- Residual / fallout verification: [`task-13-fallout-scope.md`](task-13-fallout-scope.md), [`task-14-residual-matrix.md`](task-14-residual-matrix.md), [`task-14-scope-drift.md`](task-14-scope-drift.md)
- EXT exclusions: [`blind-review-direct-fixes-exclusions.md`](blind-review-direct-fixes-exclusions.md)

## Reviewer-item matrix

| Item ID | Reviewer issue | Status | Classification | Evidence | Changed source / anchor | Rationale |
|---|---|---|---|---|---|---|
| 一.1 | 图和表的文字调整；图中文字字号不应大于正文字体 | **partial** | Mixed: repo-local TEX/FLT scope identified, major plot issues remain EXT | [`task-5-figure-triage.md`](task-5-figure-triage.md), [`task-5-exclusion-inputs.md`](task-5-exclusion-inputs.md), [`blind-review-direct-fixes-exclusions.md`](blind-review-direct-fixes-exclusions.md) | [`../../body/graduate/intro/1_background.tex`](../../body/graduate/intro/1_background.tex), [`../../body/graduate/paper1/4_results.tex`](../../body/graduate/paper1/4_results.tex), [`../../body/graduate/paper3/4_results.tex`](../../body/graduate/paper3/4_results.tex) | The pass cleanly separated TeX-fixable text layers from external plot typography, but the auditable closure artifact is exclusion-heavy; do **not** claim full figure-font resolution. |
| 一.5 | 留白较多，需做版式调整 | **partial** | In-repo FLT only | [`task-5-figure-triage.md`](task-5-figure-triage.md), [`blind-review-direct-fixes-exclusions.md`](blind-review-direct-fixes-exclusions.md), [`task-13-fallout-scope.md`](task-13-fallout-scope.md) | [`../../body/graduate/intro/3_contributions_and_organization.tex`](../../body/graduate/intro/3_contributions_and_organization.tex) | Evidence supports a local float/reference-neighborhood tightening around the intro organization figure, but there is no artifact proving a thesis-wide whitespace/leave-blank cleanup. |
| 二.1 | 基函数表示符号字体不一致 | **deferred** | In-repo TEX candidate, but not evidentially closed | [`task-5-figure-triage.md`](task-5-figure-triage.md), [`task-14-residual-matrix.md`](task-14-residual-matrix.md) | [`../../body/graduate/paper2/4_method.tex`](../../body/graduate/paper2/4_method.tex) | Task 5 classified this as source-fixable inline-math inconsistency, but the available task-1..14 evidence set does not contain a dedicated closure artifact proving the normalization was completed. |
| 二.2 | 图 1-2 的引用位置需要调整 | **fixed** | In-repo FLT | [`task-3-empty-caption-hotspots.md`](task-3-empty-caption-hotspots.md), [`task-5-figure-triage.md`](task-5-figure-triage.md), [`blind-review-direct-fixes-exclusions.md`](blind-review-direct-fixes-exclusions.md) | [`../../body/graduate/intro/3_contributions_and_organization.tex`](../../body/graduate/intro/3_contributions_and_organization.tex) | The direct-fix evidence consistently maps this complaint to the intro organization figure neighborhood, and the exclusion note explicitly records that the local float/reference issue was addressed in source. |
| 二.6 | 参考文献格式混乱、类型不准确、页码缺失、格式不统一 | **partial** | In-repo bib fixes with explicit deferred rows | [`task-4-bib-scope.md`](task-4-bib-scope.md), [`task-13-fallout-scope.md`](task-13-fallout-scope.md), [`task-14-scope-drift.md`](task-14-scope-drift.md) | [`../../body/ref.bib`](../../body/ref.bib) | The bounded bibliography pass was real and repo-local, but Task 4 explicitly marked some reviewer-linked entries as needing external verification, so full closure cannot be claimed. |
| 三.2 | 全文不应以“我们”为主语，应统一为第三者客观表述 | **fixed** | In-repo source fix | [`task-2-first-person-inventory.md`](task-2-first-person-inventory.md), [`task-14-residual-matrix.md`](task-14-residual-matrix.md), [`task-13-fallout-scope.md`](task-13-fallout-scope.md) | [`../../body/graduate/intro/2_related_and_problems.tex`](../../body/graduate/intro/2_related_and_problems.tex), [`../../body/graduate/intro/3_contributions_and_organization.tex`](../../body/graduate/intro/3_contributions_and_organization.tex), [`../../body/graduate/paper2/1_intro.tex`](../../body/graduate/paper2/1_intro.tex), [`../../body/graduate/paper2/3_background.tex`](../../body/graduate/paper2/3_background.tex), [`../../body/graduate/paper2/4_method.tex`](../../body/graduate/paper2/4_method.tex), [`../../body/graduate/paper2/5_results.tex`](../../body/graduate/paper2/5_results.tex), [`../../body/graduate/paper3/2_foundation.tex`](../../body/graduate/paper3/2_foundation.tex), [`../../body/graduate/paper3/3_simulation.tex`](../../body/graduate/paper3/3_simulation.tex), [`../../body/graduate/paper3/4_results.tex`](../../body/graduate/paper3/4_results.tex) | Task 14 records no remaining high-priority authorial narration in active target prose; only low-priority caption/technical remnants remain, and those are explicitly called out rather than hidden. |
| 三.3 | 章节标题编号形式不宜使用带冒号的写法 | **fixed** | In-repo source fix | [`task-3-title-hotspots.md`](task-3-title-hotspots.md), [`task-14-residual-matrix.md`](task-14-residual-matrix.md), [`task-14-scope-drift.md`](task-14-scope-drift.md) | [`../../body/graduate/intro/2_related_and_problems.tex`](../../body/graduate/intro/2_related_and_problems.tex), [`../../body/graduate/paper2/main.tex`](../../body/graduate/paper2/main.tex) | Task 14 reports zero active title-colon hits in targeted heading commands; remaining matches are backup-only. |
| 四.1 | 部分表格引用的图不在附近，需要调整图表与正文的对应位置或引用位置 | **partial** | In-repo FLT only | [`task-5-figure-triage.md`](task-5-figure-triage.md), [`blind-review-direct-fixes-exclusions.md`](blind-review-direct-fixes-exclusions.md) | [`../../body/graduate/intro/3_contributions_and_organization.tex`](../../body/graduate/intro/3_contributions_and_organization.tex) | Evidence shows at least one concrete repo-local float/reference neighborhood fix, but no artifact proves that every reviewer-observed non-nearby figure/table case across the thesis was resolved. |
| 五.1 | 图表格式问题（轴标签、量纲、对数标注、图例遮挡、子图图例/colorbar 缺失、字体过小、流程排版缩进混乱、变量引用不统一） | **partial** | Split: EXT exclusions + limited in-repo TEX/FLT scope | [`task-5-figure-triage.md`](task-5-figure-triage.md), [`task-5-exclusion-inputs.md`](task-5-exclusion-inputs.md), [`blind-review-direct-fixes-exclusions.md`](blind-review-direct-fixes-exclusions.md) | [`../../body/graduate/paper1/4_results.tex`](../../body/graduate/paper1/4_results.tex), [`../../body/graduate/paper2/4_method.tex`](../../body/graduate/paper2/4_method.tex), [`../../body/graduate/paper3/3_simulation.tex`](../../body/graduate/paper3/3_simulation.tex) | Most reviewer-mentioned plot-label/legend/font issues are explicitly documented as EXT and excluded; only some algorithm/layout / overlay classes are TeX-fixable. Full closure would overclaim. |
| 五.6 | 参考文献格式不符合标准，包括期刊名/书名格式、出版地、页码、会议论文起止页码等问题 | **partial** | In-repo bib fixes with explicit deferred rows | [`task-4-bib-scope.md`](task-4-bib-scope.md), [`task-13-fallout-scope.md`](task-13-fallout-scope.md) | [`../../body/ref.bib`](../../body/ref.bib) | Same bounded-bibliography conclusion as 二.6: directly fixable local metadata was in scope, but page/venue gaps requiring external verification remain deferred by evidence. |

## Fixed in-source vs excluded EXT assets

### Clearly fixed in-source

- **三.2** first-person narration normalization in active prose: see [`task-14-residual-matrix.md`](task-14-residual-matrix.md).
- **三.3** title-colon normalization in active headings: see [`task-3-title-hotspots.md`](task-3-title-hotspots.md) and [`task-14-residual-matrix.md`](task-14-residual-matrix.md).
- **二.2** intro organization figure reference neighborhood: see [`blind-review-direct-fixes-exclusions.md`](blind-review-direct-fixes-exclusions.md).

### Explicitly excluded as EXT / asset-regeneration work

- **一.1 / 五.1** plot-internal typography for paper1/paper3 rendered PDF/PNG assets: see [`blind-review-direct-fixes-exclusions.md`](blind-review-direct-fixes-exclusions.md).
- Representative exclusions: 图2.2, 图2.4, 图4.5, 图4.7, 图4.9 and hybrid background PNG portions in paper1.

## No-overclaim notes

1. This matrix does **not** claim that every reviewer concern in **一.1**, **一.5**, **二.1**, **二.6**, **四.1**, **五.1**, or **五.6** was fully resolved.
2. Bibliography items needing external page/venue verification remain deferred exactly as recorded in [`task-4-bib-scope.md`](task-4-bib-scope.md).
3. External PDF/PNG plot typography is **excluded**, not fixed, unless a row explicitly cites a repo-local TeX/TikZ source adjustment.
4. The verification basis here is restricted to task-1..14 evidence, the exclusion note, and touched source paths; it intentionally avoids inventing unrecorded completion claims.
