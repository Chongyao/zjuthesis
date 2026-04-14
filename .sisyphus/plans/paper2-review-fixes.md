# Paper2 Review Fixes Work Plan

## TL;DR

> **Quick Summary**: Repair paper2 according to the AGENTS.md writing rules by fixing reader-order logic first, then tightening wording, terminology, headers/captions, and chapter closure.
>
> **Deliverables**:
> - Revised `body/graduate/paper2/1_intro.tex`
> - Revised `body/graduate/paper2/3_background.tex`
> - Revised `body/graduate/paper2/4_method.tex`
> - Revised `body/graduate/paper2/5_results.tex`
> - Revised `body/graduate/paper2/6_summary.tex`
> - Successful `latexmk` build for the thesis
>
> **Estimated Effort**: Medium
> **Parallel Execution**: YES - 3 implementation waves
> **Critical Path**: T2 → T3 → T5 → T8 → F1-F4

---

## Context

### Original Request
根据前面总结出的 11 条审阅意见，为 paper2 制定一份正式的修订计划。

### Interview Summary
**Key Discussions**:
- 修订必须遵循仓库 `AGENTS.md`：先修结构与段落顺序，再修文字与术语。
- in-scope 文件限定为 `body/graduate/paper2/1_intro.tex`、`3_background.tex`、`4_method.tex`、`5_results.tex`、`6_summary.tex`。
- 用户此前已经明确要求术语统一为“强连接”。
- 当前计划目标是整理 work plan，而不是直接实施修订。

**Research Findings**:
- `1_intro.tex`：贡献列表后缺少总结与章节导航段。
- `3_background.tex`：结尾段同时承担问题来源、危害、方法方向与节尾收束，角色混杂。
- `4_method.tex`：候选选择出现过晚；强连接处理分支有重复引入；开头与强连接部分存在长句、口语化和 reader-order 问题。
- `5_results.tex`：表头英文化；“强链接/强连接”混用；实验块缺少“本节验证什么”的显式说明；benchmark、困难情形、应用之间的桥接不足。
- `6_summary.tex`：总体稳定，但需要先完成 paper2 自身闭环，再承担跨章预告。

### Metis Review
**Identified Gaps** (addressed):
- 需要显式锁定 scope，避免从 paper2 扩散到全文术语统一。
- 需要把 11 条意见与具体任务建立一一对应关系，避免“泛化式润色”。
- 需要把 `3_background.tex` → `4_method.tex` 作为一个联合过渡任务处理，而不是拆散。
- 需要把 `4_method.tex` 的主线稳定作为 `5_results.tex` 结果叙事修订的前置条件。
- 需要把“编译成功”之外的结构性验收标准写清楚，例如术语检查、桥段检查、实验块验证目标检查。

---

## Work Objectives

### Core Objective
基于已识别的 11 条问题，系统修复 paper2 的结构逻辑、章节衔接、术语统一和图表表述，使其符合 `AGENTS.md` 所要求的 reader-order logic 与论文写作规范。

### Concrete Deliverables
- `1_intro.tex` 在贡献列表后新增明确的收束/导航段。
- `3_background.tex` 结尾段拆分或重构，使“问题诊断”与“方法过渡”分工清晰。
- `4_method.tex` 的主线顺序、强连接叙事和措辞得到修复。
- `5_results.tex` 中各实验块明确对应方法设计选择，且术语、表头、caption 风格统一。
- `6_summary.tex` 明确先完成 paper2 的本章闭环，再进行下一章预告。
- Thesis 通过 `latexmk` 成功编译。

### Definition of Done
- [ ] 11 条审阅意见全部在任务矩阵中有对应处理项。
- [ ] `latexmk` 编译成功，生成 `out/zjuthesis.pdf`。
- [ ] 5 个 in-scope 文件中，“强链接”残留为 0 次，“强连接”为唯一术语。
- [ ] `1_intro.tex`、`3_background.tex`、`4_method.tex`、`5_results.tex`、`6_summary.tex` 均通过结构性人工审读标准对应的 agent-executed 检查。

### Must Have
- 所有修订以“结构先于措辞”为原则。
- 不改变 paper2 的技术结论、数值结果、图像资产与核心论证结论。
- 每一项修改都能追溯到至少一条已识别问题。
- 最终验证必须包含编译、术语一致性检查、结构桥段检查。

### Must NOT Have (Guardrails)
- 不扩展到 paper1、paper3 或 thesis 全文统一润色。
- 不新增实验、不改实验结果、不调整图像资产本身。
- 不修改 `.cls`、宏包、参考文献数据库或模板基础设施。
- 不把多个独立问题模糊合并成“大范围文字润色”。
- 不使用“看起来更顺了”作为唯一验收标准。

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** - ALL verification is agent-executed. No exceptions.
> 验收不能依赖“用户自己读一下”。所有关键标准都必须能通过读取文件、grep 或编译命令验证。

### Test Decision
- **Infrastructure exists**: YES
- **Automated tests**: None（文稿修订任务）
- **Framework**: `latexmk` + read/grep-based verification
- **If TDD**: 不适用；但采用“spec first”的文稿验证方式：先锁定目标结构与术语，再修改正文。

### QA Policy
每个任务都必须带有 agent-executed QA 场景：
- **结构检查**：`Read` 目标段落，验证段落角色与顺序。
- **术语检查**：`grep` 检查统一术语与英文残留。
- **编译检查**：`latexmk` 验证整篇 thesis 可编译。
- **结果叙事检查**：`Read` 每个实验块开头与结尾，检查是否明确说明验证目标与过渡。

Evidence saved to `.sisyphus/evidence/`.

---

## Execution Strategy

### Parallel Execution Waves

> Maximize throughput by grouping independent tasks into parallel waves.
> The narrative spine (`3_background` → `4_method` → `5_results`) remains dependency-sensitive.

```
Wave 1 (Start Immediately - edge sections + planning anchors):
├── T1: Intro navigation bridge [quick]
├── T2: Background closing split + method handoff setup [deep]
├── T4: Summary local closure strengthening [quick]
└── T7: Terminology/header/caption policy lock for paper2 [quick]

Wave 2 (After T2 - method spine stabilization):
├── T3: Method mainline reordering and candidate-selection framing [deep]
├── T6: Method wording tightening and repeated strong-link branching cleanup [quick]
└── T8: Cross-file transition harmonization across intro/background/method [deep]

Wave 3 (After T3, T6, T7, T8 - evidence framing and normalization):
├── T5: Results block framing by design choice [deep]
├── T9: Results bridge paragraphs between benchmark, difficult cases, and applications [quick]
└── T10: Results table/header/caption normalization [quick]

Wave FINAL (After ALL tasks — 4 parallel reviews):
├── F1: Plan compliance audit (oracle)
├── F2: Text quality and terminology review (unspecified-high)
├── F3: Build and PDF QA execution (unspecified-high)
└── F4: Scope fidelity check (deep)
```

### Dependency Matrix
- **T1**: Blocked By: None | Blocks: T8
- **T2**: Blocked By: None | Blocks: T3, T8
- **T3**: Blocked By: T2 | Blocks: T5, T6, T8
- **T4**: Blocked By: None | Blocks: F1-F4
- **T5**: Blocked By: T3, T7, T8 | Blocks: T9, T10, F1-F4
- **T6**: Blocked By: T3 | Blocks: T8, F1-F4
- **T7**: Blocked By: None | Blocks: T5, T10, F1-F4
- **T8**: Blocked By: T1, T2, T3, T6 | Blocks: T5, F1-F4
- **T9**: Blocked By: T5 | Blocks: F1-F4
- **T10**: Blocked By: T5, T7 | Blocks: F1-F4

### Agent Dispatch Summary
- **Wave 1**: T1 → `quick`, T2 → `deep`, T4 → `quick`, T7 → `quick`
- **Wave 2**: T3 → `deep`, T6 → `quick`, T8 → `deep`
- **Wave 3**: T5 → `deep`, T9 → `quick`, T10 → `quick`
- **FINAL**: F1 → `oracle`, F2 → `unspecified-high`, F3 → `unspecified-high`, F4 → `deep`

---

## TODOs
- [x] T1. Add intro navigation bridge in `body/graduate/paper2/1_intro.tex` so the introduction no longer ends directly on the contribution bullets.
- [x] T2. Restructure the `3_background.tex` ending and `4_method.tex` opening handoff so diagnosis leads cleanly into local treatment setup.
- [x] T3. Reorder `4_method.tex` mainline so candidate-selection and treatment logic follow reader order and repeated branching setup is removed.
- [x] T4. Strengthen local closure in `body/graduate/paper2/6_summary.tex` before cross-chapter positioning and next-chapter preview.
- [x] T5. Revise `body/graduate/paper2/5_results.tex` so each major experiment block explicitly states which method design choice it validates.
- [x] T6. Tighten `body/graduate/paper2/4_method.tex` prose by splitting overloaded sentences, removing oral phrasing, and preserving canonical method framing.
- [x] T7. Lock and minimally apply the local terminology/style policy, including canonical `强连接` usage.
- [x] T8. Harmonize cross-file transitions across `1_intro.tex`, `3_background.tex`, and `4_method.tex` after method mainline stabilization.
- [x] T9. Add explicit bridge paragraphs between benchmark, difficult cases, and application sections in `5_results.tex`.
- [x] T10. Normalize `5_results.tex` table headers, captions, and related terminology into thesis-consistent Chinese academic style.

---

## Final Verification Wave

> 4 review agents run in PARALLEL after all implementation tasks. All must approve before the work is considered complete.

- [ ] F1. **Plan Compliance Audit** — `oracle`
  Read the plan and all five in-scope files. Verify that each of the 11 review findings has a concrete resolution in the final text.
  Output: `Findings [11/11 resolved or justified] | VERDICT: APPROVE/REJECT`

- [ ] F2. **Text Quality and Terminology Review** — `unspecified-high`
  Check for terminology drift (`强链接` vs `强连接`), direct English overuse, remaining oral expressions, and caption/header style inconsistencies.
  Output: `Terminology [PASS/FAIL] | Style [PASS/FAIL] | VERDICT`

- [ ] F3. **Build and PDF QA** — `unspecified-high`
  Run `latexmk` from repo root, confirm successful build, and inspect generated PDF sections around revised paragraphs and figures to ensure ordering and references are intact.
  Output: `Build [PASS/FAIL] | PDF spot checks [N/N] | VERDICT`

- [ ] F4. **Scope Fidelity Check** — `deep`
  Verify the diff only touches paper2 review-fix scope: structure, wording, terminology, table headers, captions, and necessary local references. Reject any scope creep beyond the agreed files unless explicitly justified.
  Output: `Scope [CLEAN/ISSUES] | Unaccounted changes [0/N] | VERDICT`

---

## Commit Strategy

- **Commit 1**: `refactor(paper2-intro): add post-contribution navigation bridge`
- **Commit 2**: `refactor(paper2-background-method): fix pathology-to-treatment handoff`
- **Commit 3**: `refactor(paper2-method): reorder mainline and remove repeated branching`
- **Commit 4**: `fix(paper2-method): tighten wording and formalize terminology`
- **Commit 5**: `refactor(paper2-results): align experiment framing with method design`
- **Commit 6**: `fix(paper2-results): normalize headers captions and terminology`
- **Commit 7**: `refactor(paper2-summary): strengthen local closure`
- **Commit 8**: `test(paper2): verify build and review checklist closure`

---

## Success Criteria

### Verification Commands
```bash
latexmk
# Expected: build succeeds and out/zjuthesis.pdf is generated

grep -R "强链接" body/graduate/paper2/{1_intro,3_background,4_method,5_results,6_summary}.tex
# Expected: no matches
```

### Final Checklist
- [ ] All 11 review findings mapped to concrete fixes
- [ ] Intro no longer ends directly on contribution bullets
- [ ] Background ends with a clean handoff into method
- [ ] Method no longer introduces candidate/treatment logic in reader-confusing order
- [ ] Results blocks explicitly state what they validate
- [ ] Results transitions between benchmark / difficult cases / applications are present
- [ ] Table headers and captions are stylistically consistent with the thesis
- [ ] Summary closes paper2 itself before previewing the next chapter
- [ ] `latexmk` succeeds
