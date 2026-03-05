# 计划：小论文1（ConsManifold）迁移与精确翻译

## 1. 目标与范围 (Goal & Scope)
将位于 `/home/zcy/workspace/records/ConsManifold` 下巨大且复杂的 LaTeX 源文件（特别是 `EGauthorGuidelines-body.inc`，共 1355 行）结构化拆分、无损翻译并迁移到博士论文模板 `body/graduate/paper1/` 目录下。

## 2. 核心挑战与应对 (Critical Challenges & Strategies)
- **挑战 1：单体巨型文件**。应对：将其按照原论文层级拆分为 7 个常规翻译 Chunk，并在 `main.tex` 中拼装。
- **挑战 2：重度数学与自定义 TikZ 宏**。应对：在翻译前，先抽离所有前置宏包和自定义符号（如 `\LowerTri` 等）到全局配置 `config/paper1_macros.tex`。
- **挑战 3：附录分散与外部依赖**。应对：原有的附录（Energy Terms, Active Set, Extended RedMax）和外部依赖（`jacobian-pattern.tex`, `preconditioner.tex`）将被翻译后，以 `\inputbody{paper1/X}` 的方式平滑且自然地**嵌入到本章正文相关的推导小节末尾**。
- **挑战 4：公式标签冲突风险**。应对：对于原文中出现的大量通用 `\label{eq:XXX}`，如果发现冲突，统一采用添加 `p1:` 前缀策略。

## 3. 翻译与排版核心原则 (Translation Rules)
1. **精准无损翻译**：绝不跳过任何数学论证，绝不擅自使用一句话总结。逐句对应。
2. **专有名词**：
   - Inextensible Cosserat Rods -> 不可伸长 Cosserat 杆
   - Compact Representation -> 紧凑表示
   - SQP framework -> SQP (序列二次规划) 框架
   - Preconditioner -> 预条件子
   - Active Set Method -> 有效集法 (Active Set Method)
   - 如果遇到极偏门的词汇，保持 `中文(English)` 的混合格式。
3. **保留所有引用**：`\cite`, `\autoref`, `\Cref` 及所有图表与公式标签。

## 4. 执行步骤 (Execution Steps)

### 阶段 1：资源与宏环境配置 (Environment Setup)
- [x] 将源目录的 `figs/` 下的所有内容及独立 PDF 图片复制到 `body/graduate/paper1/figures/`。
- [x] 将源目录的 `egbibsample.bib` 合并到博士论文的 `body/ref.bib` (去除冗余项)。
- [x] 从源文件头部提取所有的数学宏、`\DeclareMathOperator`（如 `\TriDiag`）、自定义缩写（如 `\DOT`, `\FPP`），创建 `config/paper1_macros.tex` 并将其挂载到 `zjuthesis.cls` 中。

### 阶段 2：框架搭建与附录重组 (Structure & Restructuring)
- [x] 创建 `body/graduate/paper1/main.tex`，设定章标题为 `\chapter{基于紧凑表示的不可伸长 Cosserat 杆高效稳定仿真}`。
- [x] 创建 `body/graduate/paper1/` 目录下的空分解文件（`1_intro.tex`, `2_representation.tex`, `3_simulation.tex`, `4_results.tex`, `5_conclusion.tex`）。
- [x] 创建游离依赖与附录专用的空文件：`app_energy_terms.tex`, `app_active_set.tex`, `app_extended_redmax.tex`, `jacobian_pattern.tex`, `preconditioner.tex`。并在 `main.tex` 合适位置（推导章节后）用注释锚定它们的引入位置。

### 阶段 3：分块精确翻译 (Chunked Translation Pipeline)
（以下每一步均由专门的后台大模型代理逐段读取大文件 `EGauthorGuidelines-body.inc` 对应的行，翻译并输出）
- [x] **Chunk 1**: 翻译 Abstract + Introduction (对应源文件行 116-311) -> 写入 `1_intro.tex`
- [x] **Chunk 2**: 翻译 Representation (对应行 312-421) -> 写入 `2_representation.tex`
- [x] **Chunk 3**: 翻译 Simulation (对应行 422-599) -> 写入 `3_simulation.tex`
- [x] **Chunk 4**: 翻译 Comparisons & Results (对应行 600-1089) -> 写入 `4_results.tex`
- [x] **Chunk 5**: 翻译 Conclusions (对应行 1090-1125) -> 写入 `5_conclusion.tex`
- [x] **Chunk 6**: 翻译外部依赖与附录（`jacobian-pattern.tex`, `preconditioner.tex`, 行 1147-1355 的三大附录），并修改 `main.tex` 将它们 `\inputbody` 到正文中。

### 阶段 4：编译与微调 (Final Validation)
#XB|- [x] 运行 `latexmk -xelatex`。
#JY|- [x] 捕捉错误日志，修复可能由于 `algorithm` 环境或者特殊的 TikZ 公式绘图（`\TriDiag`）导致的不兼容问题。
