# Draft: paper3-retranslation

## Requirements (confirmed)
- 用户计划将当前第四章（paper3）基本全部丢弃并重新翻译。
- 原论文位置：`/home/zcy/workspace/records/primal-dual_modes`
- 需要按“逐章逐段”方式翻译，做到一点不漏。
- 现阶段先不要开始翻译正文。
- 当前阶段先建立章节/段落对应关系。
- 然后构建一个完整计划，用于重新完成翻译。
- 最后需要整体校对，确保术语前后一致。
- 博士论文章节的开头和结尾暂时保留不变，用于过渡。
- 语言风格要求：朴素、严谨、不夸张、准确。

## Technical Decisions
- 暂未确定段落映射粒度（按 section/subsection/paragraph）。
- 暂未确定“保留不变”的具体范围（仅 chapter opening/ending 还是特定文件）。

## Research Findings
- 当前 thesis 第四章目录：`body/graduate/paper3/`
- 原论文主体目录：`/home/zcy/workspace/records/primal-dual_modes/paper-body/`

## Open Questions
- 章节开头/结尾“保留不变”的精确文件范围。
- 对应关系表的目标粒度与输出形式。
- 是否包含附录、related work、abstract 等原论文部分。

## Scope Boundaries
- INCLUDE: 建立映射、制定完整翻译计划、术语统一校对规划
- EXCLUDE: 立即开始正文重译

## Updated Findings (From Background Agent)
- **保留不变的精确范围**：
  - 开头锚点：`1_intro.tex` 的第1行（`\section{引言}`之前的一段过渡文字：“前两章分别讨论了...”）。
  - 结尾锚点：`5_conclusion.tex` 的全部内容（共3段，包含了与前两章的串联和博士论文特定的限制/展望）。
- **翻译风险与术语控制**：保留段落中使用了特定术语（如 软硬耦合、降维特征子空间、交错划分策略、无 Schur 补和特征求解的界面模态缩减法）。在翻译中间正文时，必须严格遵守这些术语，否则会导致前后逻辑断裂。
