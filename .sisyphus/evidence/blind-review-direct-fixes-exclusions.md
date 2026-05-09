# Blind Review Direct Fixes — Exclusions Evidence

**Date:** 2026-05-10  
**Plan:** `blind-review-direct-fixes`  
**Task Closure:** Task 12 missing exclusion-note follow-up

## Purpose

This note records the reviewer-linked figure-format issues that remain **excluded** from the direct-fix pass because they are embedded in externally generated PDF/PNG assets rather than controllable TeX/TikZ source. It is derived from `.sisyphus/evidence/task-5-exclusion-inputs.md`, `.sisyphus/evidence/task-5-figure-triage.md`, and the current repository state.

## Excluded EXT Issues

### EXCL-001 — R1 `一.1` — 图4.9 临界模态数量
- **Target:** 图4.9 `fig:critical-qb`
- **Active TeX anchor:** `body/graduate/paper3/4_results.tex`
- **Asset:** `body/graduate/paper3/figures/critical-qb/combined_scaling.pdf`
- **Current repo state:** `body/graduate/paper3/figures/critical-qb/plot.py` exists; the directory also contains timing-record text files under `strong-*` / `weak-*` subdirectories.
- **Why in-repo TeX edits cannot fix it:** tick labels, axis labels, and legend text are baked into the rendered PDF. LaTeX only places the finished graphic; it cannot selectively resize or restyle the internal text layer.
- **Suggested future path:** update `critical-qb/plot.py` to use thesis-compatible font sizing and regenerate `combined_scaling.pdf` from the existing timing data files.

### EXCL-002 — R5 `五.1` — 图2.2 预处理方法对比
- **Target:** 图2.2 `fig:compare_preconditioner`
- **Active TeX anchor:** `body/graduate/paper1/preconditioner_content.tex`
- **Assets:** `body/graduate/paper1/figures/sheet/pdf/single_chain_preconditioner_A.pdf`, `single_chain_preconditioner_B.pdf`, `single_chain_preconditioner_C.pdf`
- **Current repo state:** the rendered PDFs are present, but no plotting/regeneration scripts were found under `body/graduate/paper1/figures/`.
- **Why in-repo TeX edits cannot fix it:** axis labels, units, and log-axis annotations are part of the rendered PDFs, and these figures have no TikZ text layer in thesis source.
- **Suggested future path:** recover the original plotting pipeline and data from the external paper1 workspace (`/home/zcy/workspace/records/ConsManifold` per `paper1/AGENTS.md`), then regenerate the PDFs with corrected labels and units.

### EXCL-003 — R5 `五.1` — 图2.4 PCG 迭代次数对比
- **Target:** 图2.4 `fig:PCG_iter_Young`
- **Active TeX anchor:** `body/graduate/paper1/preconditioner_content.tex`
- **Assets:** `body/graduate/paper1/figures/sheet/pdf/pcg_mu_our.pdf`, `pcg_mu_blk.pdf`
- **Current repo state:** the rendered PDFs are present, but no paper1 plot scripts were found in-repo.
- **Why in-repo TeX edits cannot fix it:** the problematic axis text and unit formatting are embedded in the finished PDF assets, with no source-level overlay available in TeX.
- **Suggested future path:** same as EXCL-002 — locate the original plotting scripts/data in the external paper1 workspace and regenerate the plots.

### EXCL-004 — R5 `五.1` — 图4.5 原始对偶划分示例
- **Target:** 图4.5 `fig:primal-dual-partition-example`
- **Active TeX anchor:** `body/graduate/paper3/3_simulation.tex`
- **Assets:** `body/graduate/paper3/figures/pd-partition-demo/partition-p.png`, `partition-d.png`, `dual-eig-1.png`, `primal-eig.png`, `dual-eig-2.png`, plus `body/graduate/paper3/figures/frequency-vs-phase/fixed-vs-complete-eig-error.pdf`
- **Current repo state:** `pd-partition-demo/` contains `render_batch.py`, `data_config.py`, and `render_config.json`; `frequency-vs-phase/` contains multiple Python plotting scripts and cached numeric files.
- **Why in-repo TeX edits cannot fix it:** the subfigure typography and readability issues are baked into the PNG/PDF panels themselves. TeX controls only panel arrangement and captioning, not the internal labels or rendered plot text.
- **Suggested future path:** regenerate the PNG/PDF panels from the available scripts with larger labels and more consistent styling; if readability remains poor, split the current six-panel composition into fewer/larger panels.

### EXCL-005 — R5 `五.1` — 图4.7 正则化参数敏感性
- **Target:** 图4.7 `fig:mu-and-sigma-sensitivity`
- **Active TeX anchor:** `body/graduate/paper3/3_simulation.tex`
- **Asset:** `body/graduate/paper3/figures/mu_and_sigma/mu_and_sigma_plot.pdf`
- **Current repo state:** `mu_and_sigma/plot.py` exists, and the directory also contains CSV/TXT input files including `测试数据mu_and_sigma_clean.csv`.
- **Why in-repo TeX edits cannot fix it:** axis labels, legend placement, and curve styling are generated inside the matplotlib output and cannot be repaired by `\includegraphics` usage alone.
- **Suggested future path:** edit `mu_and_sigma/plot.py` to add explicit axis labels, clarify curve styling/legend placement, and regenerate the PDF from the checked-in CSV inputs.

### EXCL-006 — R5 `五.1f` — 多个外部结果图的坐标轴字体过小
- **Targets:** cross-cutting issue affecting 图2.2、图2.4、图4.5、图4.7 and similar external plots
- **Assets involved:** external paper1/paper3 PDF/PNG result figures
- **Current repo state:** paper3 includes several plot scripts and data files; paper1 includes only rendered assets, not the plotting pipeline.
- **Why in-repo TeX edits cannot fix it:** scaling a graphic with `\includegraphics` uniformly scales the whole asset. LaTeX cannot enlarge only the tick/axis text inside an already-rendered PDF/PNG.
- **Suggested future path:** regenerate the affected figures with larger base font sizes (roughly 14–16 pt before LaTeX scaling) or migrate plot output to a PGF/TikZ/LaTeX-integrated backend where practical.

### EXCL-007 — R1 `一.1` / R5 `五.1` — Paper1 混合图中的背景 PNG 部分
- **Targets:** 图2.5 `fig:visual_damping_penalty` and 图2.11 `fig:timestep_limit` — specifically the background `render.png` portions
- **Active TeX anchor:** `body/graduate/paper1/4_results.tex`
- **Assets:** `body/graduate/paper1/figures/helix_vs_penalty/render.png`, `body/graduate/paper1/figures/redMax/render2.png`
- **Current repo state:** the thesis source contains TikZ overlays for visible labels, but no paper1 rendering pipeline was found under `body/graduate/paper1/figures/`.
- **Why in-repo TeX edits cannot fix it:** any text baked into the raster backgrounds is part of the external render. TeX can adjust only the foreground TikZ overlay, not the embedded background pixels.
- **Suggested future path:** if the PNGs contain embedded labels, regenerate them from the original rendering workflow in the external paper1 workspace; keep as much visible annotation as possible in TikZ overlays so future font fixes remain source-local.

## TEX / FLT Items Already Addressed in Repo Source

The direct-fix pass did address several **repo-local** figure-adjacent items that are not part of the exclusions above:

- **FLT — intro organization figure neighborhood:** `body/graduate/intro/3_contributions_and_organization.tex` now introduces `\Cref{fig:intro_organization}` before the figure block and keeps the organization figure immediately adjacent to the surrounding discussion, tightening the reviewer-linked local float/reference neighborhood.
- **TeX caption repair — intro background figure:** `body/graduate/intro/1_background.tex` now uses a non-empty short caption for `fig:numerical_simulation_process`.
- **TeX caption repair — intro organization figure:** `body/graduate/intro/3_contributions_and_organization.tex` now uses a non-empty short caption for `fig:intro_organization`.

These source-local fixes are transparent, auditable, and distinct from the unresolved **EXT** items listed above.

## Closure Summary

Task 12 exclusion closure is now complete: all remaining reviewer-linked external-source-only figure issues are explicitly documented, each row identifies why TeX-only editing is insufficient, and the note also distinguishes already-addressed repo-local TEX/FLT fixes from deferred asset-regeneration work.
