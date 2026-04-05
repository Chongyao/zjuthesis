# Draft: chapter2-structure-adjustment

## Requirements (confirmed)
- 用户希望先聚焦第二章（paper1）的结构调整，而不是立即改文稿细节。
- 目标章节框架拟定为：章标题+摘要混合、研究背景、软硬耦合分析、基函数变换、实验结果与分析、本章小结。
- 原论文中的 introduction + related work 若与绪论重复，应先注释而不是删除。
- 技术部分可能需要从当前 section/subsection 结构重排到“基函数变换”及其子节之下。

## Technical Decisions
- 先做结构调整计划，再决定具体文件改写与注释策略。
- 结构调整优先保持现有文件拆分，避免一开始就大规模合并文件。
- 第二章开头应默认读者已经在第一章理解“软硬耦合/谱分离/表征重构”的总框架。

## Research Findings
- `body/graduate/paper1/main.tex` 当前顺序为：1_intro -> 2_representation -> 3_simulation -> 4_results -> 5_conclusion -> appendices。
- `body/graduate/paper1/2_representation.tex` 当前主节为“不可伸长 Cosserat 杆的表示方法”，天然可映射到“软硬耦合分析 + 基函数变换”的核心部分。
- `body/graduate/paper1/3_simulation.tex` 当前主节为“仿真算法”，更像“基函数变换后的求解框架/算法实现”。
- `body/graduate/intro/2_related_and_problems.tex` 已系统写过“不可伸长弹性细杆的刚度失配问题”，包括软硬模式、谱分离、传统方法局限。
- `paper1/1_intro.tex` 中与绪论重叠的主要是：软硬耦合定义、细杆作为典型例子的总背景、表征重构优于纯代数修补的总论述。
- `paper1/1_intro.tex` 中应保留的局部背景包括：Cosserat 杆模拟领域中的具体方法比较、Penalty/KKT/Bishop/Super-Helices/RedMax 的局部技术定位、本章自身贡献。

## Keep / Comment Strategy
- KEEP: `paper1/1_intro.tex` 中与本章局部技术生态直接相关的 related work。
- KEEP: `paper1/1_intro.tex` 中“本章方法与贡献”部分，但后续可压缩为研究背景末段。
- COMMENT/REDUCE: 重复解释“什么是软硬耦合、为什么细杆是典型例子、为什么要做表征重构”的宏观铺垫。
- COMMENT/REDUCE: 与第一章已经讲过的“拉伸硬、弯扭软、谱分离、原空间中处理约束导致病态”的总述性段落。

## Open Questions
- “章标题+摘要混合”是否保留 `paper1/1_intro.tex` 为独立文件承载，还是希望直接在 `main.tex` 中内嵌一段章首摘要？
- “软硬耦合分析”是希望只放问题定义，还是同时放传统方法局限？
- “基函数变换”下面是否要把当前 `仿真算法` 的一部分改名并纳入，还是保留独立算法小节名称？

## Scope Boundaries
- INCLUDE: 第二章结构重排、与绪论的重复判断、注释保留策略、section/subsection 级别的重命名建议。
- EXCLUDE: 立即改正文、全章措辞精修、附录重构。
