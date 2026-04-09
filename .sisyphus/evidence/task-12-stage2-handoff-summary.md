# Stage 2 Handoff Summary

This document consolidates Stage 1 findings to enable immediate line editing in Stage 2/3.

## 1. Terminology Baseline (MANDATORY)
See `body/graduate/paper3/terminology.md`.
Key terms: 模态综合法 (CMS), 界面模态缩减法 (IMR), 交错划分 (staggered partitions), 相位补足 (phase complement), 无 Schur 补和特征求解的 IMR (SE-free IMR), 自适应位移 (adaptive shifting).

## 2. Style Guidelines
See `style_guidelines_paper3.md`.
Rule: Plain, rigorous academic Chinese. No metaphors ("浩瀚天堑", "铁锁"). State mechanism before conclusion. 

## 3. File Execution Plans

### `1_intro.tex`
- **Input:** `.sisyphus/evidence/task-9-intro-risk-checklist.md` (or `1_intro_provenance.md`)
- **Action:** Rewrite P1-P3 (Tone down), P8-P12 (Restore phase/Fourier mechanism), P13 (Tone down contributions).

### `5_conclusion.tex`
- **Input:** `.sisyphus/evidence/task-11-conclusion-risk-checklist.md`
- **Action:** Rewrite to match original English constraints. Keep thesis transition but use sober tone.

### `2_representation.tex`, `3_simulation.tex`, `4_results.tex`
- **Input:** `.sisyphus/evidence/task-10-sim-results-risk-checklist.md` & `alignment_matrix.md`
- **Action:** Search and replace terminology drift. Verify appendix-forward content (e.g., Schur complement math, Error Analysis details) is fully integrated.

## 4. Traceability
All claims above are backed by evidence files in `.sisyphus/evidence/` generated during Wave 1 & 2 of Stage 1.