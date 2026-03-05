# 计划：小论文3（Primal-Dual Modes）迁移与精确翻译

## 1. 目标与范围 (Goal & Scope)
将位于 `/home/zcy/workspace/records/primal-dual_modes` 的英文论文无损迁移并精确翻译到当前博士论文的第三篇小论文目录 `body/graduate/paper3/` 中。

## 2. 翻译与排版核心原则 (CRITICAL RULES)
1. **结构平移**：原有的 `\section`、`\subsection`、`\subsubsection` 保持不变（无需降级）。
2. **精准无损翻译**：**绝对不要总结，不要遗漏任何段落或内容！** 必须逐字逐句进行对应翻译。
3. **LaTeX 标签保留**：所有的公式块、图表引用（`\autoref`、`\ref`）、文献引用（`\cite`）必须原封不动保留原始标记。
4. **专业术语对照**：
   - Component Modes Synthesis (CMS) -> 模态综合法 (CMS)
   - Interface Mode Reduction (IMR) -> 界面模态缩减法 (IMR)
   - 遇到不确定的专业词汇时，请按照 `中文翻译(English Term)` 的格式保留英文对照，并在旁边加上注释 `% TODO: 待确认术语: xxx`。
5. **特殊结构调整**：
   - 原文的 Abstract 不再使用独立环境，而是作为本章 `\chapter` 标题后的引导段落（引言之前）。
   - 原文的 Conclusion (`6.0-conclusion.tex`) 改名为 `\section{本章小结}`。
6. **章标题**：暂时定为 `\chapter{基于多重划分的模态综合法求解大规模特征值问题}`。

## 3. 执行步骤 (Execution Steps)

### 阶段 1：资源迁移 (Resources Migration)
- [ ] 复制 `/home/zcy/workspace/records/primal-dual_modes/figures/` 下的所有内容到 `body/graduate/paper3/figures/`。
- [ ] 读取 `/home/zcy/workspace/records/primal-dual_modes/all.bib/all.bib`，在去重的前提下合并至 `body/ref.bib`。

### 阶段 2：框架搭建 (Structure Setup)
- [x] 重写 `body/graduate/paper3/main.tex`，设定章标题并按顺序 `\inputbody` 引入子文件。
- [x] 在 `body/graduate/paper3/` 创建对应的空 .tex 分节文件（`1_intro.tex` 到 `7_summary.tex`）。

### 阶段 3：精确翻译 (Precise Translation)
（执行器需按文件逐个读取英文原文，严格遵循核心原则翻译后写入中文文件）
- [x] 翻译 `abstract.tex` 和 `1.0-introduction.tex` -> `1_intro.tex`
- [x] 翻译 `2.0-related_work.tex` -> `2_related.tex`
- [x] 翻译 `3.0-background.tex` -> `3_background.tex`
- [x] 翻译 `4.0-method-new.tex` -> `4_method.tex`
- [x] 翻译 `4.1-implementation.tex` -> `5_implementation.tex`
- [x] 翻译 `5.0-results.tex` -> `6_results.tex`
- [x] 翻译 `6.0-conclusion.tex` -> `7_summary.tex`

### 阶段 4：编译与验证 (Verification)
- [x] 运行 `latexmk` 进行编译。
- [x] 检查控制台输出，修复由于图表路径、宏包缺失或引用导致的编译错误。
