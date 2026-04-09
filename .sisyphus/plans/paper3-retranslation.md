# Paper3 全文重译计划 (Retranslation Plan)

## TL;DR

> **Quick Summary**: 彻底推翻并重新翻译博士论文第四章（paper3），实现源论文与目标论文的严格“逐章逐段、一点不漏”映射。保留现有的章节首尾过渡段落，其余内容采用严谨、准确、不夸张的学术中文进行重译。
> 
> **Deliverables**: 
> - 提取并确认全局术语表
> - 重译 `1_intro.tex`
> - 重译 `2_representation.tex`
> - 重译 `3_simulation.tex`
> - 重译 `4_results.tex`
> 
> **Estimated Effort**: Large
> **Parallel Execution**: NO - sequential (需要前后文术语与语境高度连贯，按顺序翻译为佳，或并行但依赖统一的术语库)
> **Critical Path**: 术语表确认 → 各小节逐段翻译 → 整体通读校对

---

## Context

### Original Request
用户对当前博士论文第四章（对应 paper3）的翻译质量不满意，要求全部丢弃当前正文（保留博士论文章节特有的开头过渡段与结尾总结），对照源论文（位于 `/home/zcy/workspace/records/primal-dual_modes/`）进行逐章逐段的彻底重新翻译。

### Interview Summary
**Key Discussions**:
- **映射关系**：要求一点不漏，原论文的各 sections、appendices 等需要合并到博士论文现有的文件结构中。
- **文风要求**：朴素、严谨、不夸张、准确的学术语言。
- **保留策略**：
  - 开头保留：`1_intro.tex` 在 `\section{引言}` 之前的过渡段。
  - 结尾保留：`5_conclusion.tex` 全文（包含与前两章的串联和未来展望）。

**Research Findings**:
- **源文件构成**：
  - `1.0-introduction.tex`, `2.0-related_work.tex`
  - `3.0-background.tex`, `4.0-method-new.tex`
  - `4.1-implementation.tex`, `5.0-results.tex`
  - `7.0-appendix.tex`, `abstract.tex` 等
- **目标文件构成**：
  - `1_intro.tex` (引言与相关工作)
  - `2_representation.tex` (背景与划分方法)
  - `3_simulation.tex` (算法与实现细节)
  - `4_results.tex` (实验与附录数据)

---

## Work Objectives

### Core Objective
完成 Paper3 源论文向博士论文第四章的高质量、全覆盖学术级中文重译，同时无缝接入博士论文现有的上下文语境。

### Concrete Deliverables
- 统一的 `terminology.md` 术语对照表。
- 重新翻译并替换内容的 `1_intro.tex`。
- 重新翻译并替换内容的 `2_representation.tex`。
- 重新翻译并替换内容的 `3_simulation.tex`。
- 重新翻译并替换内容的 `4_results.tex`。

### Definition of Done
- [ ] 所有源论文的段落均在目标 `.tex` 中有对应的严谨中文翻译。
- [ ] 编译通过，无未定义的宏（如 `\FPP`, `\DET`, `\DOT` 需正确使用）或交叉引用错误。
- [ ] 术语全局一致，且与保留的首尾段落完全契合。

### Must Have
- 严格遵循原论文段落结构，一点不漏（包括 Appendix 的关键内容需合理安置）。
- 维持原有数学公式的 LaTeX 代码（需适当调整 label 或格式以适应 `ctexrep`）。
- 强制使用 `\DET{M}` 等预设宏，不可引入相冲的宏。

### Must NOT Have (Guardrails)
- 严禁删减原论文的数学推导或理论分析段落。
- 严禁修改 `1_intro.tex` 首段及 `5_conclusion.tex`。
- 严禁使用浮夸、营销性质或不符合中国大陆学术规范的用语（如将“robust”翻成“牛逼的”，应为“鲁棒的”或“稳健的”）。

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** - ALL verification is agent-executed. No exceptions.

### Test Decision
- **Infrastructure exists**: YES (LaTeX `latexmk` build)
- **Automated tests**: None (Documentation update)
- **QA Policy**: 
  执行代理需通过 `latexmk -c && latexmk -xelatex -outdir=out zjuthesis` 验证编译。使用 `grep` 工具验证术语是否前后一致。

---

## Execution Strategy

### Parallel Execution Waves
Wave 1: 构建术语表与基础宏对齐
Wave 2: 按顺序依序执行四个主要 tex 文件的逐段翻译
Wave 3: 全局格式修复与最终编译验证

### Dependency Matrix
- T1 (术语表) 必须在所有翻译任务前完成。
- T2, T3, T4, T5 可以理论上并行，但为保证文风一致，建议由同一写作模型连贯执行或严格参考 T1。

---

## TODOs

- [x] 1. 建立学术术语库与映射规范
  **What to do**:
  - 根据 `5_conclusion.tex` 中现有的术语，提取诸如“交错划分策略 (interleaved partitioning strategy)”、“界面模态缩减法 (IMR)”、“软硬耦合”等核心词汇。
  - 创建 `.sisyphus/paper3_terminology.md` 以供后续所有任务参考。
  **Recommended Agent Profile**: `writing` (专注学术术语校准)
  **Parallelization**: Sequential (Blocks T2, T3, T4, T5)
  **QA Scenarios**: 
  ```
  Scenario: 术语表生成
    Tool: Bash (cat)
    Steps:
      1. cat .sisyphus/paper3_terminology.md
    Expected Result: 文件存在且包含明确的英中对照表。
    Evidence: .sisyphus/evidence/task-1-terminology.txt
  ```

- [x] 2. 重译 `1_intro.tex`
- [x] 3. 重译 `2_representation.tex`
  **What to do**:
  - 彻底清空原有翻译（若有）。
  - 将原 `3.0-background.tex` 以及 `4.0-method-new.tex` 的上半部分（Phase-complement by Multiple Partitions）翻译至此。
  **Recommended Agent Profile**: `writing`
  **QA Scenarios**: 
  ```
  Scenario: 编译验证
    Tool: Bash (latexmk)
    Steps:
      1. latexmk -xelatex -outdir=out zjuthesis
    Expected Result: 成功编译。
    Evidence: .sisyphus/evidence/task-3-rep.txt
  ```

- [x] 4. 重译 `3_simulation.tex`
  **Recommended Agent Profile**: `writing`
  **QA Scenarios**: 
  ```
  Scenario: 编译与宏验证
    Tool: Bash (grep & latexmk)
    Steps:
      1. grep -v "\\DETtext" body/graduate/paper3/3_simulation.tex
      2. latexmk -xelatex -outdir=out zjuthesis
    Expected Result: 未使用禁用的宏 \DETtext，且编译通过。
    Evidence: .sisyphus/evidence/task-4-sim.txt
  ```

- [x] 5. 重译 `4_results.tex`
  **What to do**:
  - 将原 `5.0-results.tex` 和 `7.0-appendix.tex` 的附录B、C翻译至此。
  - 确保图表引用标签与原论文一致，且 `figures/` 目录挂载正确。
  **Recommended Agent Profile**: `writing`
  **QA Scenarios**: 
  ```
  Scenario: 图表引用验证
    Tool: Bash (grep)
    Steps:
      1. grep "includegraphics" body/graduate/paper3/4_results.tex
    Expected Result: 图片路径均合法。
    Evidence: .sisyphus/evidence/task-5-res.txt
  ```

---

## Final Verification Wave

- [x] F1. **Plan Compliance Audit** — `oracle`
  比对源论文的所有段落是否在目标中完全体现（无遗漏），检查开场白和结尾是否被误删。
- [x] F2. **Code Quality Review** — `unspecified-high`
  检查 LaTeX 源码规范（如引用是否使用 `\cite`、`\cref` 或 `\ref`，公式环境是否匹配）。
- [x] F3. **Real Manual QA** — `unspecified-high`
  执行完整的 `latexmk` 构建，提取生成的 PDF 对应章节的文本进行抽样比对。
- [x] F4. **Scope Fidelity Check** — `deep`
  核对论文中的专用术语（CMS、IMR、多重划分等）是否在全文中被正确、统一地翻译。

---

## Commit Strategy
- Message: `refactor(paper3): complete retranslation of chapter 4 from primal-dual_modes`
- Pre-commit: `latexmk -c && latexmk -xelatex -outdir=out zjuthesis`

---

## Success Criteria
- [ ] 源论文中所有段落、公式、图表都已准确无误地映射并在目标中翻译为学术中文。
- [ ] `5_conclusion.tex` 及 `1_intro.tex` 第一段保持不变。
- [ ] 编译无 Error（少数 Warning 允许，但不应有 Missing `$` inserted 这类中断错误）。