# 计划：小论文 2（agFEM）迁移与精确翻译

## 1. 目标与范围 (Goal & Scope)
将位于 `/home/zcy/workspace/records/agFEM_draft/body` 下的英文源论文无损迁移并精确翻译到当前博士论文的第二篇小论文目录 `body/graduate/paper2/` 中。

## 2. 翻译与排版核心原则 (CRITICAL RULES)
1. **结构对齐**：保持原论文逻辑结构，但为适应博士论文框架进行合理归并。
2. **精确朴实**：翻译要求准确、朴实，不使用过度修饰的词藻。不使用英文中英混合括号注脚。
3. **保留 LaTeX 标签**：所有的公式块、图表引用（`\autoref`、`\ref`）、文献引用（`\cite`）必须原封不动保留原始标记。若遇到标签冲突，统一添加 `p2:` 前缀。
4. **章标题**：维持 `\chapter{有限元方法中病态网格单元的处理：数值感知细化与聚合}`。
5. **特殊结构调整**：
   - **Abstract**：不设独立小节，直接翻译后作为本章引言（1_intro.tex）的首段引导内容。
   - **Teaser**：由于原论文结果部分会重新引用 teaser，将 `0.3-teaser.tex` 的图片与文本内容整体后移，并入结果章节（5_results.tex）的开头或相应位置。
   - **Appendix**：原 `appendix.tex` 内容不设独立附录，直接并入正文相关章节（方法或结果）末尾。
   - **Conclusion**：`5-conclusion.tex` 改名为 `\section{本章小结}`。
6. **宏与配置隔离**：为保持三篇小论文结构一致，提取论文 2 专属数学宏与命令至 `config/paper2_macros.tex`。

## 3. 执行步骤 (Execution Steps)

### 阶段 1：资源迁移与宏配置 (Resources & Macros)
- [x] 解析 `0.0preamble.tex` 和 `0.1package_def.tex`，提取所有自定义数学宏（如特殊算子、粗体记号），写入 `config/paper2_macros.tex`。
- [x] 在 `zjuthesis.cls` 或 `config/packages.tex` 中正确引入 `paper2_macros.tex`。
- [x] 复制原论文中用到的所有图片到 `body/graduate/paper2/figures/` 目录，保持原有的子目录结构（如 data/lattice 等）。
- [x] 提取原论文的 `.bib` 参考文献，去重后合并至 `body/ref.bib`。

### 阶段 2：框架搭建 (Structure Setup)
- [x] 重写 `body/graduate/paper2/main.tex`，清除占位内容，按顺序 `\inputbody` 引入以下子文件：
  - `paper2/1_intro`
  - `paper2/2_related`
  - `paper2/3_background`
  - `paper2/4_method`
  - `paper2/5_results`
  - `paper2/6_summary`
- [x] 在 `body/graduate/paper2/` 目录下创建上述 6 个空的 `.tex` 文件。

### 阶段 3：精确翻译 (Precise Translation)
*(执行要求：逐段读取对应源文件，严格按“准确、朴实”原则翻译至目标文件)*

- [ ] **Chunk 1**: 翻译 `0.2-abstract.tex` 和 `1.0-introduction.tex` $\rightarrow$ 写入 `1_intro.tex`。
- [ ] **Chunk 2**: 翻译 `1.1-relatedWork.tex` $\rightarrow$ 写入 `2_related.tex`。
- [ ] **Chunk 3**: 翻译 `2-background.tex` $\rightarrow$ 写入 `3_background.tex`。
- [ ] **Chunk 4**: 翻译 `3-method.tex` $\rightarrow$ 写入 `4_method.tex`。
  *(注意：若 `appendix.tex` 中包含方法补充推导，请在此阶段将其并入 `4_method.tex` 相应小节末尾)*
- [ ] **Chunk 5**: 翻译 `0.3-teaser.tex`、`4-results.tex` 和 `4.1-statistics.tex` $\rightarrow$ 统合写入 `5_results.tex`。
  *(注意：将 teaser 图表与描述平滑融入结果分析的开篇或对应实验节)*
- [ ] **Chunk 6**: 翻译 `5-conclusion.tex` $\rightarrow$ 写入 `6_summary.tex`，标题设为 `\section{本章小结}`。

### 阶段 4：图表整合与编译验证 (Verification)
- [ ] 翻译整理 `6-figures.tex` 中的浮动体（图表），将它们精确安插到翻译后的各个小节 `.tex` 中对应的引用位置。
- [ ] 运行 `make safe` (或 `latexmk -xelatex`) 进行全量编译。
- [ ] 检查编译日志，修复因图表路径错位、宏包冲突或 `\ref` 未定义导致的报错。
