# Paper3 Refine Stage 3: Core Chapters Terminology & Style Alignment

## TL;DR

> **Quick Summary**: 对 `paper3` 的核心技术与实验章节（`2_representation.tex`, `3_simulation.tex`, `4_results.tex`, `5_1_alg_adaptive_shifting.tex`）以及刚才改写过的 `1_intro.tex`/`5_conclusion.tex` 进行全盘扫描，强制统一术语表达，消除风格残余（translation-ese），确保 thesis 全文专业术语的唯一性。
>
> **Deliverables**:
> - 术语严格一致的 `paper3` 完整章节
> - 最终本地编译检查
>
> **Estimated Effort**: Medium
> **Parallel Execution**: YES (Independent terminology sweeps can run in parallel waves)
> **Critical Path**: 统一相位/交错划分术语 $\rightarrow$ 统一 IMR/CMS 术语 $\rightarrow$ 语句通顺与编译检查

---

## Context

### Preceding Stage (Stage 2)
- 完成了 `1_intro.tex` (引言) 和 `5_conclusion.tex` (本章小结) 的重写，消除了“浩瀚天堑”、“逆转乾坤”等过度文学化、情绪化的 AI-slop 修辞。
- 重构了“Fourier 相位限制”与“静力平衡映射”的机理论述，恢复了学术朴实风格。
- **现存问题**：在核心章节（第 2、3、4 节）及刚改完的部分中，存在同一专业词汇的多种变体（如“相角互补” vs “相位互补”，“免 Schur 补” vs “无 Schur 补及解绑特征运算”等）。

### Work Objectives
- **Target 1**: 实施零容忍的术语替换（Terminology Enforcement），确保所有核心词汇全篇唯一。
- **Target 2**: 对核心章节的方法推导（`2_representation`、`3_simulation`）和实验结果（`4_results`）进行轻度平滑处理，解决长难句和翻译腔问题。

---

## Terminology Enforcement (Strict Baseline)

| 概念 | 统一中文术语 (必须使用) | 禁用的变体 |
|------|-------------------------|------------|
| Phase complement / complementary | **相位补足** (动/名词) / **相位互补** (形) | 相角互补、相位补充 |
| Staggered partitions | **交错划分** | 交错的划分、错位划分、错位多重网格划分 |
| Schur- and eigen-free IMR | **无 Schur 补和特征求解的 IMR** (或 SE-free IMR) | 免 Schur 补、解绑局部特征运算的 IMR |
| Adaptive shifting | **自适应位移** | 自适应移位 |
| Phase-complete basis | **相位完备基** | 完备相位基函数 |
| Fixed-interface / boundary | **固定界面** / **固定边界** | 固支边界 |

---

## Execution Tasks

- [ ] **Task 1: Unify "Phase" and "Staggered Partition" Terminology**
  - **What to do**: 搜索全部 6 个 `tex` 文件，将所有的“相角互补”、“错位划分”、“交错的划分”等变体，强制替换为 `相位补足 / 相位互补` 和 `交错划分`。
  - **Files to touch**: `1_intro.tex`, `2_representation.tex`, `5_conclusion.tex` 等。

- [ ] **Task 2: Unify "SE-free IMR" and "CMS" Terminology**
  - **What to do**: 搜索全部文件，统一无 Schur 补界面的描述。强制使用 `无 Schur 补和特征求解的 IMR`。
  - **Files to touch**: `1_intro.tex`, `3_simulation.tex`, `5_conclusion.tex`.

- [ ] **Task 3: Refine `2_representation.tex` and `3_simulation.tex` sentences**
  - **What to do**: 通读这两节，修复翻译腔（translation-ese），将生硬的被动语态和定语从句改为流畅的中文学术表达。
  - **Focus**: 确保伪代码 `5_1_alg_adaptive_shifting.tex` 中引用的变量名称在正文解释中完全对应。

- [ ] **Task 4: Refine `4_results.tex` (Scalability and Metrics)**
  - **What to do**: 确保所有的图表引用（Fig. X）、Error-Time 曲线描述、强弱扩展（strong/weak scaling）、局部更新（local update）等词汇准确、朴实。

- [ ] **Task 5: Final Read-through and Compilation Check**
  - **What to do**: 运行 `latexmk`，确保所有交叉引用、数学公式宏（特别是 `\DET` 和 `\FPP`）无错误，整体 PDF 生成正常。

---

## Commit Strategy
- 对每个替换任务进行精确的 line-by-line `Edit`。
- 本阶段结束后，`paper3` 的精修工作彻底完成。