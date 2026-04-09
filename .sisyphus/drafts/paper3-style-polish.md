# Draft: paper3-style-polish

## Requirements (confirmed)
- 用户当前优先目标：先完成 paper3 的风格问题分析与规划，不直接修改正文。
- 目标风格：严谨、朴实。
- 精修类型：翻译层面的精修，而非自由改写。
- 对照来源：`/home/zcy/workspace/records/primal-dual_modes`
- 质量要求：必须非常精确、完整，不漏掉任何内容。
- 计划粒度：逐节逐段对照。
- 用户要求：将当前分析完整保留为 Markdown，并开始建立 `paper3-refine-stage1` 计划。

## Technical Decisions
- 先建立 thesis 版 paper3 与英文原文的文件/章节/段落对应关系。
- 精修时以英文原文为准绳，中文 thesis 视为待校订译稿。
- 按原文功能结构组织校订：abstract / intro / related work / background / method / implementation / results / conclusion / appendix。
- 由于任务复杂，采用分阶段计划；当前先建立 Stage 1 计划。
- 写计划时采用增量写入：先 skeleton，后续补充任务批次。

## Research Findings
- 已确认原文主入口为 `/home/zcy/workspace/records/primal-dual_modes/paper-tog.tex`。
- 已确认原文正文主控为 `/home/zcy/workspace/records/primal-dual_modes/paper-body/document.tex`。
- 已确认原文核心正文文件包括：
  - `abstract.tex`
  - `1.0-introduction.tex`
  - `2.0-related_work.tex`
  - `3.0-background.tex`
  - `4.0-method-new.tex`
  - `4.1-implementation.tex`
  - `4.1.1-alg-adaptive-shifting.tex`
  - `5.0-results.tex`
  - `5.1-statistics.tex`
  - `6.0-conclusion.tex`
  - `7.0-appendix.tex`
  - `teaser.tex`
- 已确认 thesis 版核心文件包括：
  - `body/graduate/paper3/1_intro.tex`
  - `body/graduate/paper3/2_representation.tex`
  - `body/graduate/paper3/3_simulation.tex`
  - `body/graduate/paper3/4_results.tex`
  - `body/graduate/paper3/5_1_alg_adaptive_shifting.tex`
  - `body/graduate/paper3/5_conclusion.tex`
- 已确认 thesis 版存在结构重组：
  - abstract merged into intro
  - conclusion renamed to 本章小结
- 已确认高风险风格偏差区：
  - `body/graduate/paper3/1_intro.tex`
  - `body/graduate/paper3/5_conclusion.tex`
- 已确认原文风格基线：问题导向、机制解释充分、语气克制、结论明确但不过度修辞。

## File Mapping (confirmed)

### 章节入口
- thesis: `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/main.tex`
- original: `/home/zcy/workspace/records/primal-dual_modes/paper-body/document.tex`
- 关系：正文装配入口对应，thesis 去掉投稿 front matter。

### 引言部分
- thesis: `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/1_intro.tex`
- original 来源：
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/abstract.tex`
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/1.0-introduction.tex`
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/2.0-related_work.tex`
- 关系：三文件合并；且首段加入 thesis 特有的前两章承接。

### 背景 + 方法前半
- thesis: `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/2_representation.tex`
- original 来源：
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/3.0-background.tex`
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/4.0-method-new.tex` 前半
- 关系：background 与 phase-complement 前半合并。

### 方法后半 + 实现细节 + 附录前移
- thesis: `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/3_simulation.tex`
- original 来源：
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/4.0-method-new.tex` 后半
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/4.1-implementation.tex`
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/2.0-related_work.tex` 中 singular matrix pencil
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/7.0-appendix.tex` 中 Schur Complement
- 关系：最复杂混编文件。

### 算法子文件
- thesis: `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/5_1_alg_adaptive_shifting.tex`
- original: `/home/zcy/workspace/records/primal-dual_modes/paper-body/4.1.1-alg-adaptive-shifting.tex`
- 关系：基本单独对应。

### 结果部分
- thesis: `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/4_results.tex`
- original 来源：
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/5.0-results.tex`
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/5.1-statistics.tex`
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/teaser.tex`
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/7.0-appendix.tex` 中两个实验细节部分
- 关系：结果主干 + 统计表 + teaser 正文化 + appendix 实验细节前移。

### 结论 / 本章小结
- thesis: `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/5_conclusion.tex`
- original: `/home/zcy/workspace/records/primal-dual_modes/paper-body/6.0-conclusion.tex`
- 关系：明确对应，但 thesis 版为扩写后的章小结，不是逐段直译。

## Section Mapping (condensed)

### `1_intro.tex`
- 开篇长段：对应 `abstract.tex` + thesis contextual rewrite
- `\section{引言}`：对应 `1.0-introduction.tex`
- `\subsection{相关工作}` 及其子节：对应 `2.0-related_work.tex`
- `\subsection{本章方法与贡献}`：对应 original introduction 后半贡献段

### `2_representation.tex`
- `划分与子结构`：对应 `Partition`
- `Craig-Bampton (CB) 方法`：对应 `Craig-Bampton (CB) method`
- `计算代价分析`：对应 `Analysis of computational cost`
- `多重划分的相位补足`：对应 `Phase-complement by Multiple Partitions`
- `一维拉普拉斯问题的分析`：对应 `Analysis of the 1D Laplacian problem`
- `CMS 的多重划分`：对应 `Multiple partitions for CMS`

### `3_simulation.tex`
- `无 Schur 补的界面模态缩减`：对应 `Schur- and eigen-free IMR`
- `Schur 补的数学结构`：对应 appendix `Schur Complement`
- `低频界面模态的近似`：对应 `Approximation of Low-frequency interface modes`
- `实现细节`：对应 `Implementation`
- `奇异矩阵束与正则化背景`：对应 `Singular matrix pencil`
- `正则化`：对应 `Regularization`
- 后续子节：对应 `Fast Reduced Matrix Assembly` / `Hybrid MPI/OpenMP Framework` / `Partition by METIS`

### `4_results.tex`
- `实验结果`：对应 `Results`
- 模型统计表：对应 `5.1-statistics.tex`
- `精度与性能评估`：对应 `Evaluation of accuracy and performance`
- `可扩展性`：对应 `Scalability`
- `方法对比`：对应 `Comparison`
- `时间 vs. 准确模态数量`：对应 `Timing vs. Number of Accurate Modes`
- `超大规模模型性能`：对应 `Performance on Large-Scale Model` + `teaser.tex`
- `积分误差分析的实验细节`：对应 appendix 节
- `可扩展性基准的代价分解`：对应 appendix 节

### `5_conclusion.tex`
- `本章小结`：对应 `Conclusion`，但存在明显 thesis 化扩写

## Style Baseline
- 原文英文风格：强问题意识、强机制解释、强证据支撑、语气克制而结论鲜明。
- 当前 thesis 偏差最大处：
  - `1_intro.tex`
  - `5_conclusion.tex`
- 主要偏差形式：过度修辞化、文学化、情绪化、句子过长、信息边界被修辞稀释。

## Priority Risk Areas
### 第一优先级
1. `body/graduate/paper3/1_intro.tex`
2. `body/graduate/paper3/5_conclusion.tex`

### 第二优先级
3. `body/graduate/paper3/3_simulation.tex`
4. `body/graduate/paper3/4_results.tex`

### 第三优先级
5. `body/graduate/paper3/2_representation.tex`
6. `body/graduate/paper3/5_1_alg_adaptive_shifting.tex`

## Open Questions
- appendix 中是否还有未被 thesis 正文承载、但必须保留的段落，需要段落级核查。
- `5_conclusion.tex` 中哪些 thesis 扩写是允许保留的章级总结，哪些已经超出原文信息边界，需要在 Stage 2 处理时细化。

## Scope Boundaries
- INCLUDE: `body/graduate/paper3` 与 original `primal-dual_modes` 的文本对应分析与翻译精修计划
- EXCLUDE: 立即修改正文、扩大到 paper1/paper2
