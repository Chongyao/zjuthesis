# Paper 1 Layout and Appendix Refinement Plan

## TL;DR

> **Quick Summary**: Refine Chapter 2 of Paper 1 to fix three visible PDF layout defects and relocate four appendix-like blocks so the chapter ends cleanly with `本章小结` instead of trailing paper-era supplementary sections.
>
> **Deliverables**:
> - Fix the width/layout of the table `统计与性能`
> - Fix label placement in Figure 2.5 `重力作用下的螺旋线`
> - Eliminate or materially reduce the large blank space after `与直接 KKT 方法的比较`
> - Relocate `能量项详细推导` / `碰撞的有效集法` / `预条件器正定性证明` / `Kirchhoff 杆仿真的扩展 RedMax` into logically appropriate places in Chapter 2
> - Preserve cross-references, TOC consistency, and thesis-wide structure
>
> **Estimated Effort**: Medium
> **Parallel Execution**: YES - 3 waves
> **Critical Path**: Task 1 → Task 3 → Task 5 → Task 7 → Task 9

---

## Context

### Original Request
Refine the first small paper in Chapter 2 by addressing a too-wide performance table, mispositioned text in Figure 2.5, excessive blank space after the direct KKT comparison, and poor placement of appendix-like materials after the chapter conclusion. Create a plan first; do not implement yet.

### Interview Summary
**Key Discussions**:
- The user explicitly observed visible PDF defects, so the work must be driven by compiled-output behavior rather than source-only assumptions.
- The user wants a work plan first, then Atlas can execute it.
- The chapter should keep a thesis-style arc instead of preserving imported paper appendix ordering.

**Research Findings**:
- `body/graduate/paper1/4_results.tex:205-219` uses `\begin{table*}[]` with eight non-wrapping `l` columns for `统计与性能`; build evidence indicates a major width overflow.
- `body/graduate/paper1/4_results.tex:13-27` overlays Figure 2.5 labels using hard-coded TikZ coordinates on a scaled image, making misplacement highly likely after layout changes.
- `body/graduate/paper1/4_results.tex:104-134` inserts a very tall `[H]` figure immediately after `与直接 KKT 方法的比较`, which is a strong local cause of the blank region.
- `body/graduate/paper1/main.tex:11-15` still places `app_energy_terms`, `app_active_set`, `app_extended_redmax`, and `app_invertible_proof` after `5_conclusion.tex`.
- `out/zjuthesis.toc` confirms the current compiled structure is undesirable: `2.5 本章小结` is followed by appendix-like subsections and then `2.6 预条件器正定性证明`.

### Metis Review
**Identified Gaps** (addressed):
- Need explicit guardrails against turning this into thesis-wide layout cleanup.
- Need PDF-based acceptance criteria, not just TeX-source edits.
- Need to acknowledge that the four appendix-like blocks may require different relocation destinations rather than one uniform strategy.
- Need to treat TOC / numbering shifts and float-distance regressions as explicit edge cases.

---

## Work Objectives

### Core Objective
Repair the visible layout defects in Chapter 2 and restore a coherent thesis-style chapter ending by relocating paper-era supplementary material to positions near their first conceptual use.

### Concrete Deliverables
- `body/graduate/paper1/4_results.tex` updated so the `统计与性能` table fits cleanly within thesis page width.
- Figure 2.5 in `body/graduate/paper1/4_results.tex` updated so overlay labels align correctly in the compiled PDF.
- Float placement in the KKT / nearby comparison region adjusted to remove the large blank area without causing worse float drift.
- `body/graduate/paper1/main.tex` and related Chapter 2 files reorganized so no appendix-like block trails after `本章小结`.
- Cross-references, TOC, and numbering remain coherent after relocation.

### Definition of Done
- [ ] `latexmk` completes successfully from the repo root.
- [ ] The `统计与性能` table no longer visibly overflows the page width.
- [ ] Figure 2.5 overlay text is visibly aligned to the correct graphic regions.
- [ ] The blank region after `与直接 KKT 方法的比较` is removed or materially reduced.
- [ ] Chapter 2 ends at `本章小结` rather than trailing paper-era appendix sections.
- [ ] Relocated sections appear near the method/results content that references them.

### Must Have
- Preserve thesis-wide structure and avoid changes to `zjuthesis.cls` or global formatting unless absolutely necessary.
- Preserve labels, equation references, figure references, and citation integrity.
- Keep the chapter narrative coherent: background → analysis → basis transform / solver / preconditioner → results → conclusion.

### Must NOT Have (Guardrails)
- No thesis-wide float-policy refactor.
- No scientific rewriting of math/results beyond what is needed to relocate and reconnect sections.
- No broad redesign of tables/figures beyond solving the specified layout problems.
- No appendix-like sections remaining as children of `本章小结` unless explicitly justified.
- No `[]` empty float placement specifiers.

---

## Verification Strategy

### Test Decision
- **Infrastructure exists**: N/A (LaTeX thesis project)
- **Automated tests**: None
- **Framework**: `latexmk`
- **Primary verification**: compile + targeted PDF / TOC inspection

### QA Policy
Every task includes agent-executed verification using:
- `latexmk` for compile validation
- file inspection (`Read`, `Grep`) for placement/order/reference correctness
- PDF evidence inspection where possible via generated TOC/log/artifact checks

Evidence should be captured in `.sisyphus/evidence/` if Atlas execution policy uses artifact recording.

---

## Execution Strategy

### Parallel Execution Waves

Wave 1 (diagnose + local layout fixes):
- Task 1: Fix the `统计与性能` table structure
- Task 2: Fix Figure 2.5 overlay positioning
- Task 3: Relax problematic float placement around KKT comparison

Wave 2 (chapter structure cleanup):
- Task 4: Re-route appendix includes out of chapter tail
- Task 5: Integrate `能量项详细推导` near transformed formulation
- Task 6: Integrate `碰撞的有效集法` near SQP / active-set discussion
- Task 7: Integrate `预条件器正定性证明` near preconditioner discussion
- Task 8: Integrate `Kirchhoff 杆仿真的扩展 RedMax` near RedMax comparison

Wave 3 (stitching + verification):
- Task 9: Repair section hierarchy, TOC behavior, and references after relocation
- Task 10: Run final `latexmk` verification and inspect target PDF regions

Critical Path: Task 1 → Task 3 → Task 5 → Task 7 → Task 9 → Task 10

### Dependency Matrix
- **1**: blocked by none; blocks 10
- **2**: blocked by none; blocks 10
- **3**: blocked by none; blocks 10
- **4**: blocked by none; blocks 5, 6, 7, 8, 9
- **5**: blocked by 4; blocks 9, 10
- **6**: blocked by 4; blocks 9, 10
- **7**: blocked by 4; blocks 9, 10
- **8**: blocked by 4; blocks 9, 10
- **9**: blocked by 4, 5, 6, 7, 8; blocks 10
- **10**: blocked by 1, 2, 3, 5, 6, 7, 8, 9

### Agent Dispatch Summary
- **Wave 1**: T1-T3 → `quick`
- **Wave 2**: T4-T8 → `quick`
- **Wave 3**: T9-T10 → `quick`

---

## TODOs

---
- [x] 1. 修复表 `统计与性能` 的宽度超出版心问题

  **What to do**:
  - 打开 `body/graduate/paper1/4_results.tex`，定位到 `205-219` 行的 `\begin{table*}[]`。
  - 将 `table*` 替换为单栏适用的 `table`，并将空放置参数 `[]` 换为 `[htbp]` 或 `[tbp]`。
  - 原有 8 列全是 `l`，表头极长（如“平均梯度/海森评估耗时(ms)”），这会导致单栏爆宽。建议使用 `tabularx` 环境（设为 `\textwidth`），将部分长列（或所有列除第一列外）改为 `X`，或手动指定 `p{...}` 宽度以允许表头文字自动折行。
  - 也可以考虑加入 `\small` 或 `\footnotesize`。
  **QA Scenarios**:
  - 编译后，`latexmk` 日志中对该表格不再报 `Overfull \hbox (312.xxx pt too wide)` 的极宽警告。
  - **Category**: `visual-engineering`
  - **Parallelization**: YES, Wave 1

- [x] 2. 修复图 2.5 `重力作用下的螺旋线` 的文字标签错位问题

  **What to do**:
  - 打开 `body/graduate/paper1/4_results.tex`，定位到 `13-27` 行的 `fig:visual_damping_penalty`。
  - 当前的 `\node at (5.4, 3.2)` 等是硬编码绝对坐标，当底图按 `\textwidth` 缩放时，文字会错位。
  - 请引入 `scope` 环境并将坐标系绑定到图片边界（例如 `x={(image.south east)},y={(image.north west)}`），然后把绝对坐标改写为相对百分比坐标（如 `(0.9, 0.5)`），使文字能随图片一同缩放。
  - 或者，若嫌麻烦/难以精确调参，也可考虑移除 TikZ 覆盖，直接在外部把文字合并到图片上（如果环境允许），但优先推荐改写相对坐标。
  **QA Scenarios**:
  - 编译 PDF 后，文字不再飞出图片外或重叠在错误区域。
  - **Category**: `visual-engineering`
  - **Parallelization**: YES, Wave 1

- [x] 3. 消除 `与直接 KKT 方法的比较` 后面的巨大空白

  **What to do**:
  - 打开 `body/graduate/paper1/4_results.tex`，定位到 `104-135` 行。
  - 这里的 `fig:compare_direct_method` 是一个极高的堆叠多子图结构，且强制使用了 `[H]`，导致它塞不下当前页时强行换页并留下大片空白。
  - 将该图（以及它后面紧跟的几个也用了 `[H]` 的类似大图，如 `fig:compare_to_super_helix` 和 `fig:timestep_limit`）的浮动参数从 `[H]` 放宽为 `[htbp]` 或 `[tbp]`。
  - 去掉为了凑版面而强加的无意义的 `\vspace{-0.12in}`。
  **QA Scenarios**:
  - 编译 PDF 后，这几个比较小节的文字能自然顺流，不再被死钉位置的大图切断而产生大片白页。
  - **Category**: `visual-engineering`
  - **Parallelization**: YES, Wave 1

- [x] 4. 将附录类文件从 Chapter 2 结尾的 `main.tex` 中移出

  **What to do**:
  - 打开 `body/graduate/paper1/main.tex`。
  - 移除原先在 `\inputbody{paper1/5_conclusion}` 之后的 4 个 input：`app_energy_terms`, `app_active_set`, `app_extended_redmax`, `app_invertible_proof`。
  - 这一步先切断它们，不急着删文件。
  **QA Scenarios**:
  - `main.tex` 以 `5_conclusion` 结束。
  - **Category**: `quick`
  - **Parallelization**: YES, Wave 2

- [x] 5. 将 `能量项详细推导` 就近融入 `3_simulation.tex`

  **What to do**:
  - 能量推导是对优化问题 $E(\mathbf{x})$ 的补充。打开 `body/graduate/paper1/3_simulation.tex`，找到提及能量项的地方（约 `61-62` 行或 `78` 行后，即 `\subsection{向轴角链式空间的广义坐标变换}` 的末尾）。
  - 在此处加上 `\inputbody{paper1/app_energy_terms}`。
  - 确保 `app_energy_terms.tex` 里面的标题层级是 `\subsubsection`（原先可能是 `\subsection`），避免打乱主目录层级。
  **QA Scenarios**:
  - 编译后能量推导跟在能量公式提出之后。
  - **Category**: `quick`
  - **Blocked By**: Task 4
- [x] 6. 将 `碰撞的有效集法` 就近融入 `3_simulation.tex`

  **What to do**:
  - 有效集法是 SQP 求解的延伸。在 `3_simulation.tex` 中找到 `\subsection{新表示下的 SQP 求解框架}` 及其算法伪代码（约 115-127 行）。
  - 在这部分末尾（或该小节结尾处）加上 `\inputbody{paper1/app_active_set}`。
  - 确保 `app_active_set.tex` 里面的标题层级是 `\subsubsection`，作为 SQP 框架的补充细节。
  **QA Scenarios**:
  - 编译后有效集法紧跟在 SQP 讨论之后。
  - **Category**: `quick`
  - **Blocked By**: Task 4
- [x] 7. 将 `预条件器正定性证明` 就近融入 `preconditioner_content.tex`

  **What to do**:
  - 打开 `body/graduate/paper1/app_invertible_proof.tex`，把顶层的 `\section` 改为 `\subsubsection` 或 `\paragraph`。
  - 打开 `body/graduate/paper1/preconditioner_content.tex`，在讲完“它始终是对称正定矩阵”之后（文件末尾处）加上 `\inputbody{paper1/app_invertible_proof}`。
  - （如果原证明里有引用 `eq:preconditioner_structure`，现在两部分紧挨着，引用依然成立，但需检查编号是否跳跃）。
  **QA Scenarios**:
  - 证明不再作为单独的节，而是依附于预条件器小节之下。
  - **Category**: `quick`
  - **Blocked By**: Task 4
- [x] 8. 将 `Kirchhoff 杆仿真的扩展 RedMax` 就近融入 `4_results.tex`

  **What to do**:
  - 此部分是为了对比实验构建的扩展模型。打开 `body/graduate/paper1/4_results.tex`，找到 `\subsubsection{与 RedMax 的比较}` 这一节（约 152-186 行）。
  - 可以在该小节内容之后、进入 `\subsection{更多结果}` 之前，加上 `\inputbody{paper1/app_extended_redmax}`。
  - 将 `app_extended_redmax.tex` 的标题改为无编号的 `\paragraph{附注：Kirchhoff 杆仿真的扩展 RedMax}`，或者保持为 `\subsubsection`（若目录允许这种深度），以免破坏结果展示的主线。
  **QA Scenarios**:
  - 关于 RedMax 的扩展说明紧跟在 RedMax 对比实验处，不跑到整章最后。
  - **Category**: `quick`
  - **Blocked By**: Task 4
- [x] 9. 修复所有相关的引用、标签、及最终 `latexmk` 验证

  **What to do**:
  - 由于附录文件移动，原来正文中写的“见附录~\ref{app:energies}”、“见附录~\ref{model_redMax}”等文字描述需要做稍微修改，比如改为“详细推导见~\ref{app:energies}”或“我们在~\ref{model_redMax}节中将其扩展到...”。
  - 跑一次全量 `latexmk`，确认没有任何交叉引用失效。
  - 检查生成的 `out/zjuthesis.toc`：第二章现在必须干净地以 `2.5 本章小结` 结束，没有任何多余的拖尾 2.6 或后续 `2.5.x` 附录结构。
  **QA Scenarios**:
  - TOC 干净无误。
  - 无引用报错。
  - **Category**: `quick`
  - **Blocked By**: 5, 6, 7, 8
## Final Verification
- Full thesis compile succeeds with `latexmk`
- Chapter 2 TOC sequence remains coherent and no longer places appendix-like material after `本章小结`
- `统计与性能` no longer produces visible width overflow
- Figure 2.5 overlay labels are correctly positioned
- Large blank area after `与直接 KKT 方法的比较` is gone or substantially reduced
- No broken labels/citations are introduced by relocation

## Success Criteria
- Chapter 2 looks like a thesis chapter, not an imported paper with leftover appendix tail
- The visible PDF defects the user reported are resolved
- Appendix-like material is moved to conceptually appropriate positions without harming readability
- The plan is executable by Atlas as checkbox-driven work
