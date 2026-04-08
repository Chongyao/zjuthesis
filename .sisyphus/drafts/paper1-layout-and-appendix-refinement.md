# Draft: paper1-layout-and-appendix-refinement

## Requirements (confirmed)
- Improve Paper 1 presentation issues before further refinement.
- Investigate table width problem for "统计与性能".
- Investigate Figure 2.5 caption/text placement issue for "重力作用下的螺旋线".
- Investigate large blank area after "与直接 KKT 方法的比较" and likely float behavior.
- Re-plan appendix-like materials placement inside Chapter 2:
  - 能量项详细推导
  - 碰撞的有效集法
  - 预条件器正定性证明
  - Kirchhoff 杆仿真的扩展 RedMax
- Preserve overall thesis structure; do not break chapter flow.
- User wants a plan first, not immediate implementation.

## Technical Decisions
- No implementation yet; perform context gathering and planning only.
- Use parallel local exploration + PDF/layout evidence gathering before proposing task order.

## Research Findings
- `body/graduate/paper1/4_results.tex:205-219` uses `\begin{table*}[] ... \end{table*}` for “统计与性能”. It still follows a double-column paper pattern, and the compiled log reports an overfull width of about `312pt`, so this is a real layout bug rather than a viewer issue.
- `body/graduate/paper1/4_results.tex:13-27` defines Figure 2.5 with a TikZ overlay on `helix_vs_penalty/render.png`, but all labels use hard-coded absolute coordinates such as `(5.4, 3.2)` and `(6, 1.78)`. After scaling the image to `\textwidth`, those coordinates no longer track the image reliably, which strongly explains the mispositioned labels.
- `body/graduate/paper1/4_results.tex:104-134` places a very tall multi-panel figure immediately after `与直接 KKT 方法的比较` using `[H]`. Combined with nearby large `[H]` floats, this is the strongest local cause of the large blank area.
- `body/graduate/paper1/main.tex:11-15` still appends former paper appendix materials after `5_conclusion.tex`: `app_energy_terms`, `app_active_set`, `app_extended_redmax`, `app_invertible_proof`.
- `out/zjuthesis.toc:41-45` confirms the current compiled Chapter 2 order is `2.5 本章小结` followed by `2.5.1 能量项详细推导`, `2.5.2 碰撞的有效集法`, `2.5.3 Kirchhoff 杆仿真的扩展 RedMax`, and `2.6 预条件器正定性证明`, so the chapter ending is visibly broken at the thesis-structure level.
- Structurally, the most natural destinations appear to be: `能量项详细推导` near transformed optimization / energy formulation in Section 2.3, `碰撞的有效集法` near the active-set SQP discussion in Section 2.3, `预条件器正定性证明` immediately after the mixed-preconditioner discussion in Section 2.3, and `Kirchhoff 杆仿真的扩展 RedMax` inside the results arc near `与 RedMax 的比较` in Section 2.4.

## Open Questions
- Whether appendix material should become fully integrated subsections inside method/results, or remain 'appendix-flavored' but be relocated before the chapter conclusion.
- Whether the user wants a minimal-risk refinement pass (fix floats + relocate sections with minimal wording changes) or a deeper narrative cleanup in the same plan.
- For `预条件器正定性证明`, is it acceptable to demote the current top-level `\section` to a subordinate subsection/subsubsection under Section 2.3, as long as theorem/proof flow and references remain intact?

## Scope Boundaries
- INCLUDE: Chapter 2 / Paper 1 layout, float placement, appendix-material relocation planning.
- EXCLUDE: Immediate TeX edits until plan is confirmed.
