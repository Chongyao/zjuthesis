# Problems - blind-review-direct-fixes

## Task 5: Unresolved Dependencies (2026-05-09)

### P1: External Figure Assets Without Source Scripts (paper1)
- **Issue**: All paper1 result figures (图2.1–2.16) are external PDF/PNG without tracked generation scripts.
- **Impact**: 7 exclusion rows (EXCL-002, EXCL-003, EXCL-007 plus cross-cutting issues) cannot be fixed without access to original plotting pipeline.
- **Hint**: AGENTS.md mentions `/home/zcy/workspace/records/ConsManifold` as original source. Plotting scripts may reside there.
- **Blocked Tasks**: Task 12 cannot fully address R5 五.1 complaints for paper1 figures.

### P2: Paper3 Figure Regeneration Requires Data Files
- **Issue**: Paper3 generation scripts exist (e.g., `plot_new_benchmarks.py`, `plot.py`) but regeneration requires raw simulation data (JSON, NPY, CSV) that may not be in the repo.
- **Impact**: EXCL-001, EXCL-004, EXCL-005 classified as external-source-only because LaTeX cannot modify the embedded typography.
- **Blocked Tasks**: Task 12. A future asset-regeneration workflow could resolve these if data files are available.

### P3: Ambiguous Reviewer Reference "图1-2"
- **Issue**: Reviewer 二.2 says "图1-2在引用该图的文字前". The notation "图1-2" likely means "Figure 1-2" (i.e., the second figure in Chapter 1), but based on content context (organization diagram), it may actually refer to 图1.9 (fig:intro_organization), the final figure in the chapter.
- **Resolution**: Classified as FLT (float placement) regardless. TikZ source is in `3_contributions_and_organization.tex`.
- **Blocked Tasks**: None — Task 11 (float cleanup) can address this regardless of exact figure number.

### P4: Hybrid Figure Background Render Quality
- **Issue**: paper1 图2.5 and 图2.11 use `render.png` (raster) as background with TikZ text overlay. If the PNG contains embedded text, that text is external-source-only.
- **Impact**: EXCL-007. The TikZ overlay is fixable (TEX) but any baked-in text in the PNG is not.
- **Blocked Tasks**: Task 12 — can fix TikZ overlay text but not background render content.
