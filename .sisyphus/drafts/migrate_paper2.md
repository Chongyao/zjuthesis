# Draft: migrate_paper2

## Requirements (confirmed)
- 任务：为论文2制定迁移与精确翻译计划
- 源路径：`/home/zcy/workspace/records/agFEM_draft/body`
- 目标路径：`body/graduate/paper2/`
- 参考模式：沿用小论文1与小论文3的分段迁移方式
- 资源要求：迁移对应图片内容
- 风格要求：文件结构清晰
- 翻译要求：准确、朴实

## Technical Decisions
- 暂未确定：章节拆分粒度
- 暂未确定：摘要与结论的落位方式
- 暂未确定：是否存在附录、宏、局部包依赖

## Research Findings
- 现状：`body/graduate/paper2/main.tex` 仍是占位内容，尚未按源论文结构落地
- 参考计划：`.sisyphus/plans/migrate_paper1.md` 与 `.sisyphus/plans/migrate_paper3.md` 已存在

## Open Questions
- 论文2的章标题最终采用什么中文标题？当前占位标题是否保留？
- 源论文的 abstract / conclusion / appendix 应如何映射到 thesis 章节结构？
- 是否需要抽取 paper2 专属宏到 `config/paper2_macros.tex`？

## Scope Boundaries
- INCLUDE: 源论文结构梳理、图片迁移、参考文献迁移、分段翻译计划、目标文件结构设计
- EXCLUDE: 立即执行全文翻译与资源复制（当前阶段仅做计划）
