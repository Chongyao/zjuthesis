# paper1-layout-and-appendix-refinement learnings
## Task 2: Fix Label Misalignment in Figure 2.5 (fig:visual_damping_penalty)

**Context**: In `body/graduate/paper1/4_results.tex`, the overlay labels for Figure 2.5 were hardcoded using absolute coordinates (`(5.4, 3.2)`, `(6, 1.78)`, etc.) over an image set to `width=\textwidth`. This caused the labels to shift and misalign relative to the underlying image when the figure scaled in the thesis layout.

**Action**:
- Modified the tikzpicture drawing block of `fig:visual_damping_penalty`.
- Placed the text labels inside a `\begin{scope}[x={(image.south east)},y={(image.north west)}] ... \end{scope}` block to use coordinates relative to the underlying image bounds.
- Adjusted the coordinates to proportional values (`(0.9, 0.9)`, `(1.0, 0.5)`, etc.) matching the intended locations.

**Result**: The labels are now properly bound to the image coordinates and will correctly track the image geometry regardless of absolute page scaling.

- The `table*` environment for "统计与性能" in `4_results.tex` was modified to `table` with `tabularx` using `\textwidth` and `X` columns to prevent overfull box in the single column format.
- Use `tabularx` with `\textwidth` and `X` columns to solve overfull table width problems for large performance statistic tables.
- **4_results.tex Float Fix**: Changed tall `[H]` figures to `[htbp]` in `4_results.tex` around the direct KKT method comparison section to eliminate excessive white space. Also removed arbitrary `\vspace{-0.12in}` on the comparison figure since float positioning now handles vertical layout more naturally.
- Replaced [H] with [htbp] on all figures in body/graduate/paper1/4_results.tex to allow better float placement, minimizing the large blank spaces after KKT comparison and other regions.
- Replaced rigid `[H]` with `[htbp]` in  to allow LaTeX to better manage page flow around large figures, specifically removing the ` space{-0.12in}` that caused blank spaces.
- Changed [H] to [htbp] for float figures in `body/graduate/paper1/4_results.tex` to eliminate large blank spaces, especially after the direct KKT comparison block, while preserving content and original float structures.
- Removed local `\vspace{-0.12in}` ad hoc spacing tweak at the KKT comparison figure block.
- For tall figure blocks (like the KKT comparison block in `body/graduate/paper1/4_results.tex`), it is better to change float options from the rigid `[H]` to `[htbp]`. This allows LaTeX to properly distribute the figures across pages without leaving huge empty blocks in text. Additionally, local ad hoc spacing hacks like `\vspace{-0.12in}` should be removed to allow the engine to position floats correctly.

## Appendix Relocation Anchors and Plan
- **Task 4 (Remove from main)**: Remove `app_energy_terms`, `app_active_set`, `app_extended_redmax`, `app_invertible_proof` from `body/graduate/paper1/main.tex` after `5_conclusion.tex`.
- **Task 5 (Energy Terms)**: Insert `app_energy_terms` into `3_simulation.tex` after mentioning the energy terms in equation 4.1 or similar place (e.g., after `\Cref{eq:cons_origin_opt}` where it says "这些项的具体公式见附录~\ref{app:energies}"). Exact location: `3_simulation.tex` line ~62 (`这些项的具体公式见附录~\ref{app:energies}`).
- **Task 6 (Active Set)**: Insert `app_active_set` into `3_simulation.tex` after the SQP framework algorithm. Exact location: `3_simulation.tex` line 79 (`伪代码见附录~\ref{app:active_set}`).
- **Task 7 (Invertible Proof)**: Insert `app_invertible_proof` into `preconditioner_content.tex` where the block tri-diagonal preconditioner is discussed. Exact location: `preconditioner_content.tex` line 93 (`它始终是对称正定矩阵`).
- **Task 8 (Extended RedMax)**: Insert `app_extended_redmax` into `4_results.tex` after the RedMax comparison section. Exact location: `4_results.tex` around line 154 (`我们在附录~\ref{model_redMax} 中将其扩展到 Kirchhoff 杆`).
- **Task 9 (Fix references)**:
  - `3_simulation.tex` line 62: "这些项的具体公式见附录~\ref{app:energies}" -> "这些项的具体公式见\ref{app:energies}节"
  - `3_simulation.tex` line 79: "伪代码见附录~\ref{app:active_set}" -> "伪代码见\ref{app:active_set}节"
  - `4_results.tex` line 154: "我们在附录~\ref{model_redMax} 中将其扩展到 Kirchhoff 杆" -> "我们在\ref{model_redMax}节中将其扩展到 Kirchhoff 杆"
  - Change `\section` to `\subsubsection` in `app_energy_terms.tex`, `app_active_set.tex`, `app_extended_redmax.tex`, and `app_invertible_proof.tex`.
- **Task 4 (Remove from main)**: Successfully removed `app_energy_terms`, `app_active_set`, `app_extended_redmax`, and `app_invertible_proof` from `main.tex`. They will be reinserted into appropriate sections later.
- **Task 5 (Energy Terms Inline)**: Inserted `\inputbody{paper1/app_energy_terms}` in `body/graduate/paper1/3_simulation.tex` immediately after the sentence citing `附录~\ref{app:energies}`, so the detailed formulas now appear adjacent to the energy formulation discussion while preserving the `app:energies` label. Demoted `body/graduate/paper1/app_energy_terms.tex` from `\subsection` to `\subsubsection` to avoid disrupting the surrounding section hierarchy after relocation.
- **Task 7 (Invertible Proof Inline)**: Inserted `\inputbody{paper1/app_invertible_proof}` in `body/graduate/paper1/preconditioner_content.tex` immediately after the SPD statement (`它始终是对称正定矩阵`), so the proof now appears adjacent to the preconditioner property claim while preserving references such as `eq:preconditioner_structure`. Demoted `body/graduate/paper1/app_invertible_proof.tex` from `\section` to `\subsection` for inline placement while keeping the label `\label{app:invertible}` intact.
- [Item 6]: `app_active_set` inserted successfully into `3_simulation.tex` via `\inputbody`.
- [Item 6]: The heading level in `app_active_set.tex` was modified from `\subsection` to `\subsubsection` to avoid disrupting the main section hierarchy, and `\label{app:active_set}` was preserved.
- **Task 8 (Extended RedMax Inline)**: Inserted `\inputbody{paper1/app_extended_redmax}` in `body/graduate/paper1/4_results.tex` immediately after the RedMax comparison figure block and before `\subsection{更多结果}` so the explanatory note stays adjacent to the `附录~\ref{model_redMax}` citation. Demoting the appendix heading to `\paragraph` preserved the `model_redMax` label while keeping the inserted material visually inline instead of creating a new peer subsection.
- [Task 6 fix] `\inputbody{paper1/app_active_set}` reads better when placed after the SQP framework derivation block, rather than before the subsection heading, because it behaves as an inline supplement to the SQP discussion.
- **Task 9 (Reference Cleanup + TOC Check)**: Updated the remaining stale appendix wording in `3_simulation.tex` and `4_results.tex` from `附录~\ref{...}` to `\ref{...}节` so the relocated inline material now reads as in-chapter sections rather than appendices. Also restored the missing `\inputbody{paper1/preconditioner_content}` inclusion to `3_simulation.tex`; after successful `latexmk`, `out/zjuthesis.toc` shows Chapter 2 ending cleanly at `2.5 本章小结` with no trailing appendix-like entries.
- ## 2026-04-07 Final verification pass
- Inspected `body/graduate/paper1/3_simulation.tex`, `body/graduate/paper1/preconditioner_content.tex`, `body/graduate/paper1/4_results.tex`, `body/graduate/paper1/main.tex`, and `out/zjuthesis.toc` for the final acceptance check.
- Chapter 2 structure is coherent: the inline appendix material now sits next to its first citation sites inside Sections 2.3 and 2.4, while `main.tex` contains only the main chapter inputs (`1_intro` through `5_conclusion`).
- `out/zjuthesis.toc` confirms Chapter 2 ends at `2.5 本章小结`, so the prior trailing appendix-after-conclusion problem is resolved.
- The remaining polish concern is only stylistic: `Kirchhoff 杆仿真的扩展 RedMax` appears as an unnumbered `paragraph` entry under `2.4.1.4` in the TOC. This is acceptable for final acceptance because it keeps the inline supplement attached to the RedMax comparison without reopening the subsection hierarchy, but it remains the one visible TOC style irregularity if later cosmetic cleanup is desired.
- ## 2026-04-07 TOC polish for inline RedMax note
- Replacing `\paragraph{Kirchhoff 杆仿真的扩展 RedMax}` with `\paragraph*{Kirchhoff 杆仿真的扩展 RedMax}` in `body/graduate/paper1/app_extended_redmax.tex` preserved the inline explanatory block and `\label{model_redMax}` anchor while suppressing the standalone paragraph-level TOC entry under Section 2.4.