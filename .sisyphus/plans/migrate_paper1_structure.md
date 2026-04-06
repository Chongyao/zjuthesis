# Paper 1 (Chapter 2) 结构重组执行计划

## TL;DR

> 将第二章从“独立论文结构”重组为“博士论文递进章节”结构，使其与第一章中“软硬耦合病态系统与表示空间重构”的主线严格对齐。
>
> 目标目录结构应为：章首摘要混合段 → 研究背景 → 软硬耦合分析 → 基函数变换 → 实验结果与分析 → 本章小结。

---

## Context

### Active Files
- `body/graduate/paper1/main.tex`
- `body/graduate/paper1/1_intro.tex`
- `body/graduate/paper1/2_representation.tex`
- `body/graduate/paper1/3_simulation.tex`
- `body/graduate/paper1/preconditioner_content.tex`
- `body/graduate/paper1/4_results.tex`
- `body/graduate/paper1/5_conclusion.tex`
- `body/graduate/intro/2_related_and_problems.tex`

### Current Structure Snapshot
- `main.tex` currently contains `\chapter{...}` followed by `\inputbody{paper1/1_intro}`, `2_representation`, `3_simulation`, `4_results`, `5_conclusion`, then appendices.
- `1_intro.tex` currently contains the intended chapter-opening transition paragraph, then `\section{引言}` and two subsections.
- `2_representation.tex` currently contains `\section{不可伸长 Cosserat 杆的表示方法}` plus `\subsection{紧凑表示}`.
- `3_simulation.tex` currently contains `\section{仿真算法}` and already uses transformed coordinates `\mathbf{s}` and `\mathcal{T}`.
- `preconditioner_content.tex` is actively included from `3_simulation.tex`; `preconditioner.tex` is not the active include.
- Intro overlap source is `body/graduate/intro/2_related_and_problems.tex`, especially `\subsection{不可伸长弹性细杆的刚度失配问题}`.

### Guardrails
- Overlap with Chapter 1 must be **commented out, not deleted**.
- Commented text should use `% [Covered in Intro] ...` style markers for traceability.
- Keep existing labels/equation references stable where possible; if heading text changes, labels should remain valid or be repaired in the same task.
- Compile verification must use `latexmk`, never plain `xelatex`.

---

## Execution Strategy

### Wave 1 — structure anchors
1. Move chapter-opening summary into `main.tex`
2. Refactor `1_intro.tex` into `研究背景`
3. Reframe `2_representation.tex` into `软硬耦合分析`

### Wave 2 — technical narrative migration
4. Extract compact-representation material from `2_representation.tex`
5. Rebuild `3_simulation.tex` as `基函数变换`
6. Verify `preconditioner_content.tex` still attaches at the correct narrative position

### Wave 3 — consistency and verification
7. Repair/verify cross-references and section logic
8. Confirm `4_results.tex` and `5_conclusion.tex` remain structurally correct
9. Run `latexmk` and verify TOC / references

---

## TODOs

- [x] 1. 将章首摘要从 `1_intro.tex` 迁移到 `main.tex`

  **目标文件**：`body/graduate/paper1/main.tex`、`body/graduate/paper1/1_intro.tex`
  **要做什么**：
  - 在 `\chapter{...}` 之后插入当前 `1_intro.tex` 首段作为无 `\section` 标题的章首摘要。
  - 从 `1_intro.tex` 删除这段重复的章首摘要，只保留正式节内容。
  - 保证 `main.tex` 的 include 顺序不变。
  **验证**：
  - `main.tex` 在 `\chapter{...}` 后直接出现过渡段，而非立即 `\inputbody{paper1/1_intro}`。
  - `1_intro.tex` 不再重复包含同一承上启下摘要。
  - 编译后目录中不新增多余节标题。
  **依赖**：无

- [x] 2. 将 `1_intro.tex` 重构为“研究背景”并注释绪论已覆盖内容

  **目标文件**：`body/graduate/paper1/1_intro.tex`、参考 `body/graduate/intro/2_related_and_problems.tex`
  **要做什么**：
  - 将 `\section{引言}` 改为 `\section{研究背景}`。
  - 以 `% [Covered in Intro] ...` 形式注释掉与绪论重复的大段宏观背景：软硬模态、长度约束导致谱分离、Penalty/KKT/DER/Super-Helices/RedMax 的宏观综述。
  - 保留本章局部应用背景和“本章方法与贡献”列表。
  - 不删除被裁剪段落，必须保留为可追踪注释。
  **验证**：
  - `1_intro.tex` 顶层节标题为 `研究背景`。
  - 被去重内容以注释形式保留。
  - 该文件仍保留本章方法与贡献清单。
  **依赖**：任务 1

- [x] 3. 将 `2_representation.tex` 改写为“软硬耦合分析”问题分析节

  **目标文件**：`body/graduate/paper1/2_representation.tex`
  **要做什么**：
  - 将 `\section{不可伸长 Cosserat 杆的表示方法}` 改为 `\section{软硬耦合分析}`。
  - 重组前半段为两个明确小节：
    - `\subsection{传统笛卡尔表示与冗余自由度}`
    - `\subsection{局部硬约束引发的病态性}`
  - 保留对 `\mathbf{x}=[\mathbf{p}^T,\mathbf{q}^T]^T` 和三类约束（式 2.1–2.3）的数学描述。
  - 新增/调整过渡句，明确长度约束等如何引入高频硬模式并恶化条件数。
  **验证**：
  - `2_representation.tex` 的主标题与两个小节标题都已更新。
  - 数学约束定义仍存在且引用未断裂。
  - 本节阅读目标从“提出表示”变为“解释病态来源”。
  **依赖**：任务 2

- [x] 4. 从 `2_representation.tex` 抽离“紧凑表示”核心变换内容

  **目标文件**：`body/graduate/paper1/2_representation.tex`、`body/graduate/paper1/3_simulation.tex`
  **要做什么**：
  - 将原 `\subsection{紧凑表示}` 中的轴角表示、链式结构、式 2.4–2.8 等内容从 `2_representation.tex` 移出。
  - 确保 `2_representation.tex` 结束于问题分析，不再承载完整方法主体。
  - 为后续粘贴到 `3_simulation.tex` 保留公式、图、标签的一致性。
  **验证**：
  - `2_representation.tex` 中不再保留完整的 `紧凑表示` 方法主体。
  - 被移动的公式/图/标签在迁移后仍只定义一次。
  - `2_representation.tex` 的逻辑闭合于“为何病态”。
  **依赖**：任务 3

- [x] 5. 将 `3_simulation.tex` 重构为“基函数变换”主节

  **目标文件**：`body/graduate/paper1/3_simulation.tex`
  **要做什么**：
  - 将 `\section{仿真算法}` 改为 `\section{基函数变换}`。
  - 在本节开头插入从任务 4 迁移来的紧凑表示内容，并命名为 `\subsection{向轴角链式空间的广义坐标变换}`（或等价标题）。
  - 让本节整体叙事变为：先完成坐标/基函数变换，再引出变换后优化问题与求解。
  **验证**：
  - `3_simulation.tex` 新主标题为 `基函数变换`。
  - 变换小节位于求解框架之前。
  - 读者能在本节中先看到坐标变换，再看到算法。
  **依赖**：任务 4

- [x] 6. 重组 `3_simulation.tex` 后续小节，使其成为变换后的自然推论

  **目标文件**：`body/graduate/paper1/3_simulation.tex`、`body/graduate/paper1/preconditioner_content.tex`
  **要做什么**：
  - 增加过渡段或新小节，说明在新坐标空间 `\mathbf{s}` 下，原问题转化为无显式距离约束的优化域。
  - 将 `SQP 框架` 重命名为类似 `新表示下的 SQP 求解框架`。
  - 将矩阵-向量乘法小节重命名为类似 `\texorpdfstring{$\mathcal{O}(n)$}{O(n)} 时间复杂度的算子评估`。
  - 保持 `\inputbody{paper1/preconditioner_content}` 正常挂靠在本节末尾的叙事位置。
  **验证**：
  - `3_simulation.tex` 中每个子节都服务于“变换后的求解与算子结构”。
  - `preconditioner_content.tex` 仍然从 `3_simulation.tex` 被正确 include。
  - 叙事不再像孤立算法章，而像变换后的技术展开。
  **依赖**：任务 5

- [x] 7. 检查并修复 Chapter 2 内部引用、标签和目录一致性

  **目标文件**：`body/graduate/paper1/*.tex`（重点 `2_representation.tex`、`3_simulation.tex`、`4_results.tex`、附录）
  **要做什么**：
  - 检查所有 `\ref{...}`、`\Cref{...}`、`\cref{...}` 是否因节标题调整、内容搬移、标签位置变化而失效。
  - 保持核心公式标签和跨节引用稳定；如必须改动，连同引用处一并修复。
  - 特别检查 `4_results.tex` 中对方法节、公式和附录的引用。
  **验证**：
  - 不存在悬空引用或重复标签。
  - 结果章节能正确引用方法部分和附录。
  - TOC 与正文标题层级一致。
  **依赖**：任务 6
- [x] 8. 确认 `4_results.tex` 与 `5_conclusion.tex` 无需结构性改写，仅保持新主线一致

  **目标文件**：`body/graduate/paper1/4_results.tex`、`body/graduate/paper1/5_conclusion.tex`
  **要做什么**：
  - 保持 `4_results.tex` 的 `\section{实验结果与分析}` 不变。
  - 复核实验章节表述是否仍自然承接新的“软硬耦合分析 → 基函数变换”主线。
  - 确认 `5_conclusion.tex` 继续保持 `\section{本章小结}`，并能呼应绪论与第三章过渡。
  **验证**：
  - 实验结果节标题不变且逻辑承接顺畅。
  - 本章小结标题不变。
  - 无需额外拆分目录层级。
  **依赖**：任务 7

- [x] 9. 运行 `latexmk` 并做最终结构验证

  **目标文件**：全章与总 thesis 编译输出
  **要做什么**：
  - 在仓库根目录运行 `latexmk`。
  - 检查编译是否成功，引用是否收敛，目录是否体现目标章结构。
  - 人工核对第二章目录顺序是否为：章首摘要（不进目录）→ 研究背景 → 软硬耦合分析 → 基函数变换 → 实验结果与分析 → 本章小结。
  **验证**：
  - `latexmk` 成功完成。
  - PDF 目录结构符合目标。
  - 无明显引用错误、标题错位或残留重复摘要。
  **依赖**：任务 8

## Final Verification
- Full thesis compile succeeds with `latexmk`
- Chapter 2 TOC sequence matches the target structure
- No duplicated large-scale background exposition remains uncommented in `1_intro.tex`
- `2_representation.tex` ends as analysis/problem framing, not full method dump
- `3_simulation.tex` clearly presents the coordinate/basis transform before solver details
- Cross-references and equation references resolve without breakage

## Success Criteria
- Chapter 2 reads as a dissertation chapter, not a standalone imported paper
- Introductory redundancy with Chapter 1 is reduced by commenting, not deletion
- The method narrative shifts from “representation proposal” to “basis / generalized-coordinate transform for isolating pathological stiffness”
- The plan is executable by checkbox-driven workflow tools
