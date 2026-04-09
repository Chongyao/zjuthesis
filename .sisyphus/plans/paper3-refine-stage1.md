# Paper3 Refine Stage 1

## TL;DR

> **Quick Summary**: 建立 paper3 当前 thesis 版与英文原文的精确段落级对应关系，并锁定翻译层精修的术语与风格基线，为后续逐段精修提供无歧义依据。
>
> **Deliverables**:
> - paper3 文件/章节/段落级对应矩阵
> - 术语对照表与风格约束表
> - Stage 1 风险清单（漏译/误译/过度改写/附录前移承载）
> - 可直接用于 Stage 2 执行的逐文件核对清单
>
> **Estimated Effort**: Medium
> **Parallel Execution**: YES - 3 waves
> **Critical Path**: 映射核查 → 术语与风格基准 → 风险确认 → Stage 2 输入物

---

## Context

### Original Request
用户要求先解决 paper3 的风格问题，目标语言风格为“严谨、朴实”。需要先找到当前 thesis 版 paper3 与英文原文 `/home/zcy/workspace/records/primal-dual_modes` 的对应关系，然后制定一个翻译层面的精修计划，要求非常精确、完整，不漏掉任何内容。随后用户进一步要求：
1. 将当前分析完整保留为 Markdown；
2. 开始建立 `paper3-refine-stage1` 计划。

### Interview Summary
**Key Discussions**:
- 当前不直接修改正文，而是先完成高质量规划。
- 精修必须是“翻译层面”而不是自由改写。
- 计划组织粒度选定为：**逐节逐段对照**。
- 由于任务复杂，需要分阶段推进；当前先建立 Stage 1 计划。

**Research Findings**:
- thesis 版 `paper3` 与英文原文不是简单直译，而是重组后的章节化改编。
- `1_intro.tex` 融合了 abstract、introduction、related work，并加入 thesis 特有承接前两章的内容。
- `3_simulation.tex` 融合了 method 后半、implementation、related work 中 singular matrix pencil，以及 appendix 中 Schur Complement。
- `4_results.tex` 融合了 results 主体、statistics、teaser 与 appendix 的实验细节。
- 风格偏差最大的文件是 `1_intro.tex` 与 `5_conclusion.tex`。

### Metis Review
**Identified Gaps** (addressed in this plan):
- 需要先做段落级对应矩阵，不能直接进入精修。
- 需要单独锁定 appendix 前移内容的承载关系，避免漏译。
- 需要明确 `5_conclusion.tex` 中 thesis 特有扩写的边界，避免后续误保留。
- 需要先建立术语与风格基准，防止 Stage 2 逐段校订时术语漂移。

---

## Work Objectives

### Core Objective
完成 paper3 精修前的全部“基础设施”准备工作：建立 thesis 版与英文原文的精确对照体系、术语体系、风格约束与高风险问题清单，使 Stage 2 可以在不丢内容的前提下进行逐段翻译层精修。

### Concrete Deliverables
- `.sisyphus/drafts/paper3-style-polish.md` 作为完整分析记录
- `.sisyphus/plans/paper3-refine-stage1.md` 作为 Stage 1 执行计划
- Stage 1 结束时应产出：
  - 文件级/章节级/段落级映射表
  - appendix 前移内容承载表
  - 术语对照表
  - 风格约束表
  - 高风险段落清单

### Definition of Done
- [x] 当前 thesis 版每个主文件都能追溯到原文来源文件
- [x] `1_intro.tex`、`3_simulation.tex`、`4_results.tex` 的混编结构被拆解清楚
- [x] `5_conclusion.tex` 的原文边界与 thesis 扩写边界明确
- [x] appendix 中必须保留的内容已确认在 thesis 中的承载位置
- [x] 已形成 Stage 2 可直接执行的逐文件核对输入

### Must Have
- 段落级对应，不只停留在文件名对应
- 明确记录合并/拆分/重排/改名关系
- 明确记录 thesis 特有新增与可能弱化/省略内容
- 术语表必须能直接约束后续翻译层精修

### Must NOT Have (Guardrails)
- 不允许直接开始正文修改
- 不允许把“风格优化”演变为“自由改写”
- 不允许跳过 appendix / teaser / statistics 等边缘来源文件
- 不允许只做模糊总结而不给出可执行映射

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** - ALL verification is agent-executed. No exceptions.
> Acceptance criteria requiring “user manually checks the mapping” are FORBIDDEN.

### Test Decision
- **Infrastructure exists**: NO
- **Automated tests**: None
- **Framework**: none

### QA Policy
Stage 1 是 Markdown 规划/分析工作，不依赖单元测试。验证通过读取计划文件、草稿文件以及映射内容完整性来完成。
Evidence saved to `.sisyphus/evidence/`.

- **Library/Module**: Use Read + Grep to verify plan sections, file references, and mapping coverage
- **CLI**: Use Bash only for non-mutating directory/status confirmation if needed

---

## Execution Strategy

### Parallel Execution Waves

Wave 1 (Start Immediately - source mapping foundation):
├── Task 1: Confirm original paper source inventory [quick]
├── Task 2: Confirm thesis paper3 source inventory [quick]
├── Task 3: Build file-level mapping table [quick]
└── Task 4: Identify mixed-source files and appendix-forward content [quick]

Wave 2 (After Wave 1 - semantic alignment):
├── Task 5: Build section/subsection alignment matrix [unspecified-high]
├── Task 6: Build terminology baseline table [quick]
├── Task 7: Build style baseline and anti-pattern table [writing]
└── Task 8: Mark thesis-specific additions vs. original-bound content [unspecified-high]

Wave 3 (After Wave 2 - execution handoff prep):
├── Task 9: Build paragraph-level risk checklist for intro [unspecified-high]
├── Task 10: Build paragraph-level risk checklist for simulation/results [unspecified-high]
├── Task 11: Build paragraph-level risk checklist for conclusion [unspecified-high]
└── Task 12: Prepare Stage 2 input package summary [quick]

Wave FINAL (After ALL tasks — 4 parallel reviews, then user okay):
├── Task F1: Plan compliance audit (oracle)
├── Task F2: Content completeness review (unspecified-high)
├── Task F3: Mapping QA execution (unspecified-high)
└── Task F4: Scope fidelity check (deep)
-> Present results -> Get explicit user okay

Critical Path: 1 → 3 → 5 → 8 → 9/10/11 → 12 → F1-F4
Parallel Speedup: ~60% faster than sequential
Max Concurrent: 4

### Dependency Matrix
- **1**: - - 3, 5
- **2**: - - 3, 5
- **3**: 1, 2 - 4, 5, 8
- **4**: 3 - 8, 10
- **5**: 1, 2, 3 - 9, 10, 11, 12
- **6**: 1, 2, 3 - 12
- **7**: 1, 2, 3 - 12
- **8**: 3, 4, 5 - 9, 10, 11, 12
- **9**: 5, 8 - 12
- **10**: 4, 5, 8 - 12
- **11**: 5, 8 - 12
- **12**: 5, 6, 7, 8, 9, 10, 11 - F1-F4

### Agent Dispatch Summary
- **Wave 1**: 4 tasks - T1-T4 → `quick`
- **Wave 2**: 4 tasks - T5 → `unspecified-high`, T6 → `quick`, T7 → `writing`, T8 → `unspecified-high`
- **Wave 3**: 4 tasks - T9-T11 → `unspecified-high`, T12 → `quick`
- **FINAL**: 4 tasks - F1 → `oracle`, F2-F3 → `unspecified-high`, F4 → `deep`

---

## TODOs

- [x] 1. Confirm original paper source inventory

  **What to do**:
  - Read and verify the original paper control files and source directories under `/home/zcy/workspace/records/primal-dual_modes/paper-body/`.
  - Confirm the existence and roles of `abstract`, `introduction`, `related_work`, `background`, `method`, `implementation`, `results`, `conclusion`, `appendix`, `teaser`, and statistics-related files.
  - Record any non-obvious source files that carry textual meaning later reused in thesis.

  **Must NOT do**:
  - Do not edit original paper files.
  - Do not assume file roles from names alone without reading the control structure.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: inventory verification is bounded, read-only, and source-focused.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: not needed; this is source discovery, not prose drafting.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2, 3, 4)
  - **Blocks**: 3, 5
  - **Blocked By**: None (can start immediately)

  **References**:
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/document.tex` - Original paper body assembly order; authoritative source for chapter/section inclusion order.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-tog.tex` - Top-level LaTeX entry confirming how the paper body is embedded in the publication wrapper.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/` - Directory containing all main text source files that need inventory confirmation.

  **Acceptance Criteria**:
  - [x] All primary original-paper text source files are listed with roles.
  - [x] Any appendix or auxiliary text sources with semantic content are identified.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Verify original source inventory completeness
    Tool: Read
    Preconditions: Original project path exists
    Steps:
      1. Read `paper-body/document.tex` and note every `\input` target in order.
      2. Read `paper-tog.tex` and confirm body entry path is correct.
      3. Compare listed inputs against the `paper-body/` directory contents.
    Expected Result: A complete source inventory with no missing body file category.
    Failure Indicators: A body file category appears in directory contents but not in inventory; control file order remains unclear.
    Evidence: .sisyphus/evidence/task-1-original-source-inventory.md
  
  Scenario: Detect semantic auxiliary files
    Tool: Read
    Preconditions: Inventory from previous scenario is available
    Steps:
      1. Check whether `teaser.tex`, statistics files, or appendix-linked files contain textual content reused in thesis.
      2. Record whether each such file must be tracked for Stage 1 mapping.
    Expected Result: Auxiliary semantic sources are explicitly marked include/exclude.
    Failure Indicators: Teaser/statistics/appendix-linked text carriers remain unclassified.
    Evidence: .sisyphus/evidence/task-1-aux-source-classification.md
  ```

  **Evidence to Capture**:
  - [ ] Inventory note file
  - [ ] Auxiliary-source classification note

  **Commit**: NO

- [x] 2. Confirm thesis paper3 source inventory

  **What to do**:
  - Read and verify the thesis paper3 chapter entry and all current chapter files under `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/`.
  - Confirm which files are narrative text carriers versus figures/algorithm-only support files.
  - Mark likely mixed-source files for deeper Stage 1 mapping.

  **Must NOT do**:
  - Do not edit thesis files.
  - Do not treat AGENTS guidance as a substitute for reading actual text files.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: bounded inventory and role classification task.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: not needed during inventory pass.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 3, 4)
  - **Blocks**: 3, 5
  - **Blocked By**: None (can start immediately)

  **References**:
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/main.tex` - Thesis chapter assembly order; confirms active chapter file list.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/AGENTS.md` - Local migration notes, including abstract merge and conclusion rename.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/` - Current thesis chapter source directory.

  **Acceptance Criteria**:
  - [x] All thesis text-bearing files are listed with roles.
  - [x] Mixed-source candidate files are flagged.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Verify thesis chapter inventory completeness
    Tool: Read
    Preconditions: Thesis project path exists
    Steps:
      1. Read `body/graduate/paper3/main.tex` and note every included file in order.
      2. Compare included files with current `paper3/` directory text files.
      3. Mark which files contain primary prose versus algorithm/auxiliary support only.
    Expected Result: A complete thesis chapter inventory with role labels.
    Failure Indicators: Included text file missing from inventory or misclassified as support-only.
    Evidence: .sisyphus/evidence/task-2-thesis-source-inventory.md
  
  Scenario: Confirm migration notes affect structure
    Tool: Read
    Preconditions: Inventory from previous scenario is available
    Steps:
      1. Read `AGENTS.md`.
      2. Verify structural notes such as `abstract merged into intro` and `conclusion renamed` are reflected in the actual file list.
    Expected Result: Migration notes and real files are aligned.
    Failure Indicators: Guidance notes contradict current chapter structure.
    Evidence: .sisyphus/evidence/task-2-structure-notes-check.md
  ```

  **Evidence to Capture**:
  - [ ] Thesis inventory note file
  - [ ] Migration-note consistency check

  **Commit**: NO

- [x] 3. Build file-level mapping table

  **What to do**:
  - Produce a file-to-file mapping between original paper sources and thesis paper3 sources.
  - Explicitly mark one-to-one, one-to-many, many-to-one, and thesis-only structural cases.
  - Assign confidence per mapping row.

  **Must NOT do**:
  - Do not collapse mixed mappings into vague summaries.
  - Do not omit low-confidence rows; mark them explicitly instead.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: mapping synthesis is concise once both inventories are confirmed.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: final polish unnecessary at this stage; correctness matters more than elegance.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 4)
  - **Blocks**: 4, 5, 8
  - **Blocked By**: 1, 2

  **References**:
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/document.tex` - Original assembly order for mapping source roles.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/main.tex` - Thesis assembly order for mapping destination roles.
  - `.sisyphus/drafts/paper3-style-polish.md` - Existing confirmed mapping findings to preserve and refine.

  **Acceptance Criteria**:
  - [x] Every thesis text file has at least one source mapping row.
  - [x] Every original main text file is accounted for in destination mapping.
  - [x] Confidence annotations are present.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Verify bidirectional mapping coverage
    Tool: Read
    Preconditions: Original and thesis inventories are complete
    Steps:
      1. Build a table listing thesis files as destination rows.
      2. Build a reverse check listing original files as source rows.
      3. Confirm no source or destination file is left unmapped.
    Expected Result: Complete bidirectional coverage.
    Failure Indicators: Any thesis file or original source file lacks a mapping row.
    Evidence: .sisyphus/evidence/task-3-file-mapping-table.md
  
  Scenario: Verify mapping confidence labeling
    Tool: Read
    Preconditions: Mapping table exists
    Steps:
      1. Inspect each row for explicit confidence markers.
      2. Check that mixed-source files are not mislabeled as simple 1:1 mappings.
    Expected Result: Mapping table includes confidence and structure type per row.
    Failure Indicators: Missing confidence labels or oversimplified mixed mappings.
    Evidence: .sisyphus/evidence/task-3-file-mapping-audit.md
  ```

  **Evidence to Capture**:
  - [ ] File mapping table
  - [ ] Mapping audit note

  **Commit**: NO

- [x] 4. Identify mixed-source files and appendix-forward content

  **What to do**:
  - Identify which thesis files merge multiple original sources.
  - Explicitly track appendix-forward migrations such as Schur Complement and experiment-detail sections.
  - Mark which of these migrations create high risk of漏译、误归类或论证顺序错位.

  **Must NOT do**:
  - Do not treat appendix content as optional merely because it was auxiliary in the paper format.
  - Do not ignore teaser/statistics text carriers.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: focused structural classification task.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: not needed for classification deliverable.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3)
  - **Blocks**: 8, 10
  - **Blocked By**: 3

  **References**:
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/7.0-appendix.tex` - Source of appendix-forward content that may now live in thesis正文.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/teaser.tex` - Source of teaser text/function later absorbed into thesis results.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/5.1-statistics.tex` - Independent source later merged into thesis results.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/3_simulation.tex` - Destination file for method/implementation/appendix recomposition.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/4_results.tex` - Destination file for results/statistics/teaser/appendix recomposition.

  **Acceptance Criteria**:
  - [x] Mixed-source thesis files are explicitly listed.
  - [x] Appendix-forward content items are individually named and assigned destinations.
  - [x] High-risk migration points are flagged for Stage 2.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Verify appendix-forward content tracking
    Tool: Read
    Preconditions: Original appendix and thesis destination files are identified
    Steps:
      1. Read appendix section names and note semantically meaningful blocks.
      2. Locate the corresponding thesis sections carrying those blocks.
      3. Record source-to-destination migration rows.
    Expected Result: Every required appendix-forward block has an explicit thesis destination.
    Failure Indicators: Appendix block has no mapped destination or only vague destination notes.
    Evidence: .sisyphus/evidence/task-4-appendix-forward-map.md
  
  Scenario: Verify mixed-source risk classification
    Tool: Read
    Preconditions: File mapping table exists
    Steps:
      1. Review thesis files with 2+ source files.
      2. Mark why each is risky: merge, split, reorder, thesis-only addition, or narrative-function shift.
    Expected Result: Mixed-source risk matrix is explicit and actionable.
    Failure Indicators: Mixed-source files listed without risk reasons.
    Evidence: .sisyphus/evidence/task-4-mixed-source-risk-matrix.md
  ```

  **Evidence to Capture**:
  - [ ] Appendix-forward mapping table
  - [ ] Mixed-source risk matrix

  **Commit**: NO

- [x] 5. Build section/subsection alignment matrix

  **What to do**:
  - Construct a section/subsection alignment matrix between original paper structure and thesis chapter structure.
  - Record when original sections become thesis subsections, when multiple original sections merge into one thesis section, and when appendix sections move into body text.
  - Preserve labels and semantic anchors where possible to support later paragraph-level traceability.

  **Must NOT do**:
  - Do not stop at file-level mapping.
  - Do not lose original rhetorical roles such as introduction, related work, background, method, implementation, results, conclusion, and appendix.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: requires careful structural reasoning across mixed-source files and reordered section hierarchies.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: output needs correctness and traceability more than stylistic prose polish.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 6, 7, 8)
  - **Blocks**: 9, 10, 11, 12
  - **Blocked By**: 1, 2, 3

  **References**:
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/1.0-introduction.tex` - Original introduction structure and contribution placement.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/2.0-related_work.tex` - Original related-work section hierarchy.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/3.0-background.tex` - Original background section hierarchy.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/4.0-method-new.tex` - Original method section hierarchy, especially phase-complement and SE-free IMR split.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/4.1-implementation.tex` - Original implementation structure later merged into thesis.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/5.0-results.tex` - Original results section structure.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/6.0-conclusion.tex` - Original conclusion role and scope.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/7.0-appendix.tex` - Original appendix sections later partially moved forward.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/1_intro.tex` - Thesis destination for merged abstract/introduction/related-work content.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/2_representation.tex` - Thesis destination for background + method-first-half structure.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/3_simulation.tex` - Thesis destination for method-second-half + implementation + appendix-forward content.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/4_results.tex` - Thesis destination for results + teaser + appendix-forward content.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/5_conclusion.tex` - Thesis destination for conclusion + thesis-specific chapter summary expansion.

  **Acceptance Criteria**:
  - [x] Every original section/subsection has a thesis-side destination.
  - [x] Section hierarchy shifts are explicitly recorded.
  - [x] Appendix-forward sections are represented in the matrix.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Verify section-level bidirectional alignment
    Tool: Read
    Preconditions: File-level mapping exists
    Steps:
      1. List all original section/subsection headers in order.
      2. List all thesis section/subsection headers in order.
      3. Map each original header to one or more thesis destinations and mark structure changes.
    Expected Result: A complete section/subsection alignment matrix.
    Failure Indicators: Any original header lacks a thesis destination or any thesis header lacks identified source provenance.
    Evidence: .sisyphus/evidence/task-5-section-alignment-matrix.md
  
  Scenario: Verify rhetorical-role preservation
    Tool: Read
    Preconditions: Alignment matrix exists
    Steps:
      1. Review whether each mapped block retains its rhetorical role (e.g. related work remains literature review, not mistaken as method).
      2. Flag all role shifts for Stage 2 attention.
    Expected Result: Role shifts are explicitly listed and justified.
    Failure Indicators: Structural mapping exists but rhetorical-role changes are unmarked.
    Evidence: .sisyphus/evidence/task-5-role-shift-audit.md
  ```

  **Evidence to Capture**:
  - [ ] Section/subsection alignment matrix
  - [ ] Role-shift audit

  **Commit**: NO

- [x] 6. Build terminology baseline table

  **What to do**:
  - Build a bilingual terminology baseline table for paper3, covering core method names, structural mechanics vocabulary, eigensolver vocabulary, and recurring chapter-specific terms.
  - Lock preferred thesis-side Chinese forms and forbidden variant forms where ambiguity exists.
  - Include notes on first-use explanation strategy where English abbreviations remain necessary.

  **Must NOT do**:
  - Do not allow multiple uncontrolled Chinese renderings for the same core term.
  - Do not introduce terminology that conflicts with existing thesis intro terminology.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: bounded terminology normalization task once source corpus is known.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: terminology locking is a precision task, not prose generation.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 5, 7, 8)
  - **Blocks**: 12
  - **Blocked By**: 1, 2, 3

  **References**:
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/AGENTS.md` - Existing migration terminology guidance for CMS and IMR.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/intro/2_related_and_problems.tex` - Thesis-wide terminology already used to frame paper3 within the full dissertation.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/1.0-introduction.tex` - Original core terminology in contribution framing.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/3.0-background.tex` - Original background terminology around CMS, interface modes, and reduction.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/4.0-method-new.tex` - Original method terminology for phase complement and SE-free IMR.

  **Acceptance Criteria**:
  - [x] Core terms have single preferred Chinese renderings.
  - [x] Abbreviations and first-use rules are defined.
  - [x] Conflict terms and banned variants are listed.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Verify terminology coverage
    Tool: Read
    Preconditions: Core source files are available
    Steps:
      1. Extract recurring technical terms from intro, background, method, implementation, and results.
      2. Confirm each recurring term appears in the baseline table.
    Expected Result: No high-frequency technical term lacks a locked rendering.
    Failure Indicators: A repeated source term is missing from the baseline table.
    Evidence: .sisyphus/evidence/task-6-terminology-baseline.md
  
  Scenario: Verify thesis-wide consistency
    Tool: Read
    Preconditions: Terminology baseline exists
    Steps:
      1. Compare locked terms with terminology already used in thesis intro and paper3 AGENTS guidance.
      2. Flag conflicts or duplicate Chinese renderings.
    Expected Result: Terminology is consistent with thesis-wide usage.
    Failure Indicators: Same concept has multiple preferred renderings or conflicts with prior thesis terminology.
    Evidence: .sisyphus/evidence/task-6-terminology-consistency-check.md
  ```

  **Evidence to Capture**:
  - [ ] Terminology baseline table
  - [ ] Consistency check note

  **Commit**: NO

- [x] 7. Build style baseline and anti-pattern table

  **What to do**:
  - Derive a style baseline from the English original and from the user requirement `严谨、朴实`.
  - Create an anti-pattern table capturing the current failure modes in thesis text: over-literary diction, inflated rhetoric, overlong sentences, vague macro claims, and thesis-unsafe emotional phrasing.
  - Translate the baseline into explicit rewrite constraints for Stage 2.

  **Must NOT do**:
  - Do not define style in vague adjectives only; each rule must be operationalizable.
  - Do not over-correct into dry literalism that loses mechanism clarity.

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: this task converts observed style differences into explicit editorial rules and examples.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `brand-guidelines`: irrelevant; this is academic prose normalization, not visual or marketing style.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 5, 6, 8)
  - **Blocks**: 12
  - **Blocked By**: 1, 2, 3

  **References**:
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/1.0-introduction.tex` - Source style for problem framing and contribution statements.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/5.0-results.tex` - Source style for evidence-led result narration.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/6.0-conclusion.tex` - Source style for restrained conclusion writing.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/1_intro.tex` - High-risk style deviation sample.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/5_conclusion.tex` - High-risk style deviation sample.

  **Acceptance Criteria**:
  - [x] Style baseline contains explicit positive rules.
  - [x] Anti-pattern table contains concrete negative examples or categories.
  - [x] Stage 2 rewrite constraints are directly usable.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Verify style rules are operational
    Tool: Read
    Preconditions: Style baseline draft exists
    Steps:
      1. Check each style rule for an actionable test (e.g. sentence-length reduction, banned rhetoric class, mechanism-before-claim rule).
      2. Remove or rewrite any rule that is too vague to enforce.
    Expected Result: Every style rule can guide concrete line editing.
    Failure Indicators: Rules rely only on subjective adjectives without actionable checks.
    Evidence: .sisyphus/evidence/task-7-style-baseline.md
  
  Scenario: Verify anti-pattern coverage against risky files
    Tool: Read
    Preconditions: Anti-pattern table exists
    Steps:
      1. Compare anti-pattern categories against `1_intro.tex` and `5_conclusion.tex`.
      2. Confirm major deviation types are captured.
    Expected Result: Main observed style failures are all represented.
    Failure Indicators: Known style issues in risky files are missing from anti-pattern categories.
    Evidence: .sisyphus/evidence/task-7-antipattern-coverage.md
  ```

  **Evidence to Capture**:
  - [ ] Style baseline table
  - [ ] Anti-pattern coverage note

  **Commit**: NO

- [ ] 8. Mark thesis-specific additions vs. original-bound content

  **What to do**:
  - Identify which thesis passages are required chapter-context additions versus which ones drift beyond original-bound meaning.
  - Mark passages that must be preserved as dissertation-context bridges.
  - Mark passages that must be tightened or reconsidered in Stage 2 because they over-expand beyond original informational scope.

  **Must NOT do**:
  - Do not assume all thesis-only additions are bad; some are necessary for chapter integration.
  - Do not allow thesis-specific additions to mask missing original content.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: requires interpretive judgment about acceptable dissertation-context additions versus unsafe over-expansion.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: this is classification and boundary-setting, not final prose drafting.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 5, 6, 7)
  - **Blocks**: 9, 10, 11, 12
  - **Blocked By**: 3, 4, 5

  **References**:
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/1_intro.tex` - Contains thesis-specific transition material not present in the original paper.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/5_conclusion.tex` - Contains chapter-summary expansion beyond the original conclusion.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/intro/3_contributions_and_organization.tex` - Thesis-level framing that may justify certain chapter-context additions.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/abstract.tex` - Helps distinguish thesis bridge text from original abstract-derived content.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/6.0-conclusion.tex` - Helps distinguish valid conclusion content from thesis over-expansion.

  **Acceptance Criteria**:
  - [ ] Thesis-only additions are explicitly labeled preserve/rewrite/review.
  - [ ] Original-bound content is distinguished from chapter-context bridges.
  - [ ] Over-expansion risk is documented for Stage 2.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Verify thesis-specific addition classification
    Tool: Read
    Preconditions: Section alignment and style baseline exist
    Steps:
      1. Review passages with no direct original source anchor.
      2. Classify each as dissertation-context bridge, neutral reorganization, or over-expansion risk.
    Expected Result: All thesis-only passages are explicitly categorized.
    Failure Indicators: Thesis-only passages remain unlabeled or are treated uniformly.
    Evidence: .sisyphus/evidence/task-8-thesis-addition-classification.md
  
  Scenario: Verify no original content is hidden behind additions
    Tool: Read
    Preconditions: Classification table exists
    Steps:
      1. Compare thesis additions against adjacent original-derived content blocks.
      2. Confirm original arguments are still present and not displaced by expansion.
    Expected Result: Additions do not obscure missing original content.
    Failure Indicators: A thesis-only expansion occupies space where original content is absent or weakened.
    Evidence: .sisyphus/evidence/task-8-original-boundary-check.md
  ```

  **Evidence to Capture**:
  - [ ] Thesis-addition classification table
  - [ ] Original-boundary check note

  **Commit**: NO

- [x] 9. Build paragraph-level risk checklist for intro

  **What to do**:
  - For `1_intro.tex`, create a paragraph-by-paragraph checklist showing source provenance, role, style risk, completeness risk, and likely Stage 2 action.
  - Separate abstract-derived content, introduction-derived content, related-work-derived content, and thesis-only transition content.
  - Mark paragraphs with over-expansion, compressed mechanism explanation, or likely missing original qualifiers.

  **Must NOT do**:
  - Do not treat `1_intro.tex` as a single block; paragraph-level resolution is required.
  - Do not blur introduction and related-work functions.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: this is the highest-risk mixed-source file and requires granular interpretive mapping.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: no final line editing yet; checklist accuracy comes first.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 10, 11, 12)
  - **Blocks**: 12
  - **Blocked By**: 5, 8

  **References**:
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/1_intro.tex` - Destination file to be risk-indexed paragraph by paragraph.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/abstract.tex` - Original abstract source.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/1.0-introduction.tex` - Original introduction source.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/2.0-related_work.tex` - Original related-work source.

  **Acceptance Criteria**:
  - [x] Every paragraph in `1_intro.tex` has source provenance or a thesis-only classification.
  - [x] Each paragraph has role and risk labels.
  - [x] Stage 2 actions are suggested per paragraph or paragraph group.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Verify intro paragraph provenance coverage
    Tool: Read
    Preconditions: Paragraph checklist draft exists
    Steps:
      1. Enumerate every paragraph in `1_intro.tex`.
      2. Confirm each paragraph has a provenance tag and risk tag.
    Expected Result: No intro paragraph is unclassified.
    Failure Indicators: Any paragraph lacks source or risk labeling.
    Evidence: .sisyphus/evidence/task-9-intro-risk-checklist.md
  
  Scenario: Verify intro function separation
    Tool: Read
    Preconditions: Checklist exists
    Steps:
      1. Review paragraph roles and confirm abstract/introduction/related-work/thesis-bridge functions are not conflated.
      2. Flag ambiguous role assignments.
    Expected Result: Functional zones in intro are clearly separated.
    Failure Indicators: Related work paragraphs are mislabeled as method framing or thesis bridges remain unmarked.
    Evidence: .sisyphus/evidence/task-9-intro-function-audit.md
  ```

  **Evidence to Capture**:
  - [ ] Intro paragraph-level risk checklist
  - [ ] Intro function audit

  **Commit**: NO

- [ ] 10. Build paragraph-level risk checklist for simulation/results

  **What to do**:
  - Create paragraph-level risk checklists for `3_simulation.tex` and `4_results.tex`.
  - Track mixed-source blocks, especially implementation insertion, appendix-forward sections, teaser/statistics absorption, and result-methodology explanations.
  - Mark where original mechanism explanations may have been compressed or reordered in ways that increase Stage 2 correction risk.

  **Must NOT do**:
  - Do not treat method and results risk as identical; preserve their distinct failure modes.
  - Do not ignore appendix-forward blocks just because they appear late in thesis results.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: these are structurally mixed files with medium-to-high risk of role drift or compressed explanations.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: checklist creation is diagnostic, not rewrite execution.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 9, 11, 12)
  - **Blocks**: 12
  - **Blocked By**: 4, 5, 8

  **References**:
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/3_simulation.tex` - Mixed-source method/implementation/appendix-forward destination.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/4_results.tex` - Mixed-source results/statistics/teaser/appendix-forward destination.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/4.0-method-new.tex` - Original method source.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/4.1-implementation.tex` - Original implementation source.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/5.0-results.tex` - Original results source.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/5.1-statistics.tex` - Statistics source.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/7.0-appendix.tex` - Appendix-forward experimental and Schur-complement source.

  **Acceptance Criteria**:
  - [ ] Every paragraph in `3_simulation.tex` and `4_results.tex` is provenance-tagged or thesis-classified.
  - [ ] Mixed-source sections and appendix-forward sections receive explicit risk labels.
  - [ ] Results methodology and evidence explanation risks are separated from method-logic risks.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Verify simulation/results paragraph coverage
    Tool: Read
    Preconditions: Checklists exist
    Steps:
      1. Enumerate paragraphs in `3_simulation.tex` and `4_results.tex`.
      2. Confirm each paragraph has provenance and risk labeling.
    Expected Result: No paragraph in either file is left unclassified.
    Failure Indicators: Missing provenance or missing risk tags in either file.
    Evidence: .sisyphus/evidence/task-10-sim-results-risk-checklist.md
  
  Scenario: Verify appendix-forward risk capture
    Tool: Read
    Preconditions: Checklists exist
    Steps:
      1. Review all blocks sourced from appendix or teaser/statistics side files.
      2. Confirm each such block is explicitly marked as a moved-source risk point.
    Expected Result: All moved-source blocks are clearly identified.
    Failure Indicators: Appendix-forward or teaser/statistics-derived blocks are present without moved-source risk labels.
    Evidence: .sisyphus/evidence/task-10-moved-source-audit.md
  ```

  **Evidence to Capture**:
  - [ ] Simulation/results paragraph-level risk checklist
  - [ ] Moved-source audit

  **Commit**: NO

- [ ] 11. Build paragraph-level risk checklist for conclusion

  **What to do**:
  - For `5_conclusion.tex`, create a paragraph-level checklist comparing each thesis paragraph against the original conclusion and identifying thesis-only expansions.
  - Mark which paragraphs preserve original conclusion functions, which serve legitimate chapter-summary purposes, and which likely exceed original informational scope.
  - Prepare explicit Stage 2 actions: preserve, compress, re-anchor to original, or review for removal.

  **Must NOT do**:
  - Do not assume all chapter-summary expansion is acceptable.
  - Do not force an exact paragraph count match if thesis conclusion legitimately integrates chapter-context bridging.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: conclusion is a high-risk file with strong style drift and thesis-level expansion beyond the original paper conclusion.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: the task is diagnostic boundary-setting before any rewrite begins.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 9, 10, 12)
  - **Blocks**: 12
  - **Blocked By**: 5, 8

  **References**:
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/5_conclusion.tex` - Thesis destination requiring high-risk boundary analysis.
  - `/home/zcy/workspace/records/primal-dual_modes/paper-body/6.0-conclusion.tex` - Original conclusion source anchor.
  - `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/intro/3_contributions_and_organization.tex` - Thesis-level context that may justify certain chapter-summary echoes.

  **Acceptance Criteria**:
  - [ ] Every conclusion paragraph is classified by provenance and purpose.
  - [ ] Thesis-only expansion zones are identified.
  - [ ] Stage 2 action labels are assigned per paragraph or paragraph group.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Verify conclusion paragraph provenance coverage
    Tool: Read
    Preconditions: Conclusion checklist draft exists
    Steps:
      1. Enumerate every paragraph in `5_conclusion.tex`.
      2. Confirm each paragraph has provenance/purpose labels.
    Expected Result: No conclusion paragraph is left unclassified.
    Failure Indicators: Missing provenance or purpose labels for any paragraph.
    Evidence: .sisyphus/evidence/task-11-conclusion-risk-checklist.md
  
  Scenario: Verify expansion-boundary labeling
    Tool: Read
    Preconditions: Checklist exists
    Steps:
      1. Compare thesis conclusion paragraphs against original conclusion functions.
      2. Confirm chapter-summary expansions are explicitly distinguished from over-expansion risk.
    Expected Result: Safe chapter-summary bridges and unsafe over-expansion are separated.
    Failure Indicators: Thesis-only additions are unlabeled or all treated identically.
    Evidence: .sisyphus/evidence/task-11-expansion-boundary-audit.md
  ```

  **Evidence to Capture**:
  - [ ] Conclusion paragraph-level risk checklist
  - [ ] Expansion-boundary audit

  **Commit**: NO

- [ ] 12. Prepare Stage 2 input package summary

  **What to do**:
  - Consolidate all Stage 1 artifacts into a single Stage 2 handoff summary.
  - Organize by destination file, with required inputs: provenance map, terminology baseline, style rules, paragraph risks, appendix-forward notes, and preserve/rewrite/remove guidance.
  - Ensure Stage 2 can begin line editing without redoing discovery work.

  **Must NOT do**:
  - Do not leave Stage 2 dependencies scattered across ad hoc notes only.
  - Do not omit evidence file references and source anchors.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: this is a synthesis/handoff task once upstream analyses exist.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: packaging clarity matters, but this is still a structured technical handoff task.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 9, 10, 11)
  - **Blocks**: F1-F4
  - **Blocked By**: 5, 6, 7, 8, 9, 10, 11

  **References**:
  - `.sisyphus/drafts/paper3-style-polish.md` - Full analysis record to preserve.
  - `.sisyphus/plans/paper3-refine-stage1.md` - Stage 1 plan and task structure.
  - `.sisyphus/evidence/` - Evidence directory containing all Stage 1 verification artifacts.

  **Acceptance Criteria**:
  - [ ] Stage 2 receives one consolidated input package summary.
  - [ ] Each thesis destination file has a dedicated handoff subsection.
  - [ ] All dependencies reference concrete evidence paths.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Verify Stage 2 handoff completeness
    Tool: Read
    Preconditions: Upstream Stage 1 artifacts exist
    Steps:
      1. Compile all Stage 1 outputs into a file-structured summary.
      2. Check each thesis file has provenance, style, terminology, and risk inputs.
    Expected Result: Stage 2 can begin without repeating discovery work.
    Failure Indicators: Any thesis file lacks one or more required input categories.
    Evidence: .sisyphus/evidence/task-12-stage2-handoff-summary.md
  
  Scenario: Verify evidence traceability
    Tool: Read
    Preconditions: Handoff summary exists
    Steps:
      1. Inspect each handoff subsection for evidence links/paths.
      2. Confirm claims in the handoff can be traced to Stage 1 artifacts.
    Expected Result: Handoff summary is fully traceable to supporting evidence.
    Failure Indicators: Handoff claims lack evidence references or source anchors.
    Evidence: .sisyphus/evidence/task-12-handoff-traceability-check.md
  ```

  **Evidence to Capture**:
  - [ ] Stage 2 handoff summary
  - [ ] Handoff traceability check

  **Commit**: NO

---

## Final Verification Wave

- [ ] F1. **Plan Compliance Audit** — `oracle`
  Verify that all Stage 1 deliverables are represented in tasks, especially: file mapping, section mapping, appendix-forward mapping, terminology baseline, style baseline, and Stage 2 handoff artifacts.

- [ ] F2. **Content Completeness Review** — `unspecified-high`
  Check that no source category is omitted: abstract, introduction, related work, background, method, implementation, results, conclusion, appendix, teaser, statistics.

- [ ] F3. **Mapping QA Execution** — `unspecified-high`
  Read the draft and plan outputs, verify file references exist, and ensure mixed-source thesis files have explicit source decomposition.

- [ ] F4. **Scope Fidelity Check** — `deep`
  Confirm the plan remains strictly Stage 1 only: planning and mapping, not direct body text editing.

---

## Commit Strategy

- No commit in Stage 1 unless user explicitly requests one.

---

## Success Criteria

### Verification Commands
```bash
# No build required for Stage 1; verification is read-based.
```

### Final Checklist
- [x] All mixed-source files identified
- [x] All original source sections accounted for
- [x] Appendix-forward content explicitly tracked
- [x] High-risk style deviation files prioritized
- [x] Stage 2 handoff inputs fully specified
