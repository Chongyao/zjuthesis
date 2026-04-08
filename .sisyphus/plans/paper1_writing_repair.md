# Paper 1 Writing & Terminology Repair Plan

## TL;DR

> **Quick Summary**: Fix medium/low severity writing issues (M1, M2, M5, L1, L2, L4, L5) in Paper 1 and the Introduction chapter to improve academic tone, cross-chapter consistency, and narrative pacing.
> 
> **Deliverables**:
> - `body/graduate/intro/3_contributions_and_organization.tex` (tone down rhetoric)
> - `body/graduate/paper1/main.tex` & `1_intro.tex` (terminology mapping)
> - `body/graduate/paper1/3_simulation.tex` (add logical transitions)
> - `body/graduate/paper1/4_results.tex` (decouple facts from evaluation)
> - `body/graduate/paper1/5_conclusion.tex` (split long sentences)
> 
> **Estimated Effort**: Short
> **Parallel Execution**: YES - 2 waves
> **Critical Path**: Task 1, 2, 3 -> Task 4, 5 -> F1-F4

---

## Context

### Original Request
The user requested a concrete repair plan for a subset of writing and consistency issues (M1, M2, M5, L1, L2, L4, L5) identified in a previous review, focusing specifically on the introduction and paper 1. High-severity structural issues are excluded from this scope.

### Interview Summary
**Key Discussions**:
- **Terminology Mapping (M1, M2, L5)**: Paper 1 needs to explicitly anchor itself to the overarching "表示空间重构" (representation space reconstruction) and "软硬耦合" (stiff-soft coupling) concepts defined in the intro.
- **Narrative Pacing (M5, L2)**: Transitions between abstract mathematical concepts and specific algorithmic choices (e.g., SQP) need smoothing. Long, dense sentences in conclusions need to be split.
- **Academic Tone (L1, L4)**: Overly strong rhetoric (e.g., "极其优雅地", "彻底打破") must be toned down. Technical facts and subjective evaluations should be separated into distinct sentences.

---

## Work Objectives

### Core Objective
Elevate Paper 1 from a "standalone paper" to a cohesive, rigorous, and logically integrated "doctoral thesis chapter" by aligning terminology, smoothing transitions, and strictly regulating academic tone.

### Concrete Deliverables
- Edited `.tex` files in `intro/` and `paper1/` directories containing the textual refinements.

### Definition of Done
- [ ] All targeted overly strong rhetoric is neutralized.
- [ ] Terminology mapping sentences are injected at chapter boundaries (main.tex, 1_intro.tex).
- [ ] Long compound sentences in the conclusion are split.
- [ ] Project successfully compiles via `latexmk` with no new errors.

### Must Have
- Strict preservation of all mathematical macros (e.g., `\LowerTri`, `\FPPmathbf`).
- Strict preservation of all TikZ figure environments.
- LaTeX compilation must remain perfectly functional.

### Must NOT Have (Guardrails)
- DO NOT change any scientific claims or experimental results; only alter the rhetorical packaging.
- DO NOT touch high-severity structural issues (e.g., moving sections around).
- DO NOT inject overly complex new paragraphs; stick to bridging sentences and term replacement.

---

## Verification Strategy

### Test Decision
- **Infrastructure exists**: YES (LaTeX `latexmk` build system)
- **Automated tests**: NO (Manual visual & structural check)
- **Framework**: `bash`
- **QA Policy**: 
  Every task MUST include agent-executed QA scenarios using `grep` to verify textual changes (both addition of new text and removal of targeted old text) and `latexmk` to ensure compilation integrity.

---

## Execution Strategy

### Parallel Execution Waves

```text
Wave 1 (Start Immediately - Terminology & Tone):
├── Task 1: Intro Rhetoric Tone-down [writing]
├── Task 2: Paper 1 Terminology Mapping [writing]
└── Task 3: Paper 1 Conclusion Splitting [writing]

Wave 2 (After Wave 1 - Transitions & Decoupling):
├── Task 4: Simulation Transition Smoothing [writing] (depends: 2)
└── Task 5: Results Evaluation Decoupling [writing] (depends: 1)

Wave FINAL (After ALL tasks — 4 parallel reviews, then user okay):
├── Task F1: Plan compliance audit (oracle)
├── Task F2: Code quality review (unspecified-high)
├── Task F3: Real manual QA (unspecified-high)
└── Task F4: Scope fidelity check (deep)
```

### Agent Dispatch Summary
- **Wave 1**: T1-T3 -> `writing`
- **Wave 2**: T4-T5 -> `writing`
- **FINAL**: F1 -> `oracle`, F2-F3 -> `unspecified-high`, F4 -> `deep`

---

## TODOs

- [x] 1. Intro Rhetoric Tone-down
  **What to do**:
  - Edit `body/graduate/intro/3_contributions_and_organization.tex`.
  - Locate the sentence containing "极其优雅地将拉伸硬约束内建于运动学表述中，自然消除了硬约束".
  - Split and tone down: "这种重构方法精确匹配了 Kirchhoff 杆的弯扭模态，将拉伸硬约束直接内建于运动学表述中。这一设计避免了在底层的代数求解器中处理该类硬约束，从而改善了条件数。"

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Requires precise textual editing and tone adjustment in LaTeX.
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocked By**: None

  **References**:
  - `body/graduate/intro/3_contributions_and_organization.tex` - Section 1.4 summary of Chapter 2.

  **Acceptance Criteria**:
  - [ ] "极其优雅地" is removed from the file.
  - [ ] Sentence is split into two logical parts (fact + evaluation).

  **QA Scenarios**:
  ```yaml
  Scenario: Verify Intro Tone-down
    Tool: bash
    Preconditions: None
    Steps:
      1. grep "极其优雅地" body/graduate/intro/3_contributions_and_organization.tex
    Expected Result: Command fails (exit code 1), indicating the phrase was successfully removed.
    Evidence: .sisyphus/evidence/task-1-grep-intro.txt
  ```

- [x] 2. Paper 1 Terminology Mapping
  **What to do**:
  - Edit `body/graduate/paper1/main.tex`: Update the chapter introduction paragraph to explicitly state that this chapter is the first concrete instance of the "表示空间重构" (representation space reconstruction) methodology addressing "本构导致的软硬耦合" (constitutive stiff-soft coupling).
  - Edit `body/graduate/paper1/1_intro.tex`: In section 1.2, change "本章的基本思想是..." to "针对此类由材料本构导致的极端刚度失配问题，本章的基本思想是...".

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Requires inserting bridging terminology safely.
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocked By**: None

  **References**:
  - `body/graduate/paper1/main.tex` - Chapter intro text.
  - `body/graduate/paper1/1_intro.tex` - Section 1.2 first paragraph.

  **Acceptance Criteria**:
  - [ ] "表示空间重构" appears in `paper1/main.tex`.
  - [ ] "材料本构导致的极端刚度失配问题" appears in `paper1/1_intro.tex`.

  **QA Scenarios**:
  ```yaml
  Scenario: Verify Terminology Injection
    Tool: bash
    Preconditions: None
    Steps:
      1. grep "表示空间重构" body/graduate/paper1/main.tex
    Expected Result: Command succeeds (exit code 0), showing the injected mapping sentence.
    Evidence: .sisyphus/evidence/task-2-grep-main.txt
  ```

- [x] 3. Paper 1 Conclusion Splitting

  **What to do**:
  - Edit `body/graduate/paper1/5_conclusion.tex`.
  - Locate the long compound sentence: "在此基础上，结合利用该表示特有非零模式设计的线性复杂度算子与一致对称正定的混合预条件子，本文在 SQP 隐式积分框架下实现了对不可伸长约束的一致满足，并在大时间步长及显著碰撞场景中获得了良好的加速表现。"
  - Split into 3 sentences: 1. Design of operators and preconditioner. 2. Application in SQP framework. 3. Experimental performance.
  - In the second paragraph, ensure the transition to the next chapter is explicitly tied to "本构导致的软硬耦合".

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Text segmentation and readability improvement.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocked By**: None

  **References**:
  - `body/graduate/paper1/5_conclusion.tex` - Paragraph 1 and 2.

  **Acceptance Criteria**:
  - [ ] The identified long sentence is broken into at least two separate sentences separated by periods.

  **QA Scenarios**:
  ```yaml
  Scenario: Verify Conclusion Splitting
    Tool: bash
    Preconditions: None
    Steps:
      1. grep "结合利用该表示特有非零模式" body/graduate/paper1/5_conclusion.tex
    Expected Result: Command fails, indicating the original overly long sentence was broken up/rewritten.
    Evidence: .sisyphus/evidence/task-3-grep-conclusion.txt
  ```

- [x] 4. Simulation Transition Smoothing
  - Edit `body/graduate/paper1/3_simulation.tex`.
  - Between the end of 3.1 (Coordinate Transformation) and the beginning of 3.2 (SQP Framework), add a logical transition explaining *why* SQP is used.
  - Example insertion: "通过上述向轴角链式空间的广义坐标变换，细杆的内在极硬约束已被内化消除。此时，系统的隐式时间积分被转化为一个维数更低、且仅受碰撞等外部边界条件限制的优化问题。为了高效处理这些剩余的不等式约束并保持大时间步长下的稳定性，我们在新表示下引入了基于主动集的序列二次规划（SQP）求解框架。"

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Adding narrative glue between mathematical sections.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocked By**: Task 2

  **References**:
  - `body/graduate/paper1/3_simulation.tex` - Around line 70-80, before Section 3.2.

  **Acceptance Criteria**:
  - [ ] Transition sentences explaining the shift from coordinate reconstruction to inequality constraint handling (SQP) are present.

  **QA Scenarios**:
  ```yaml
  Scenario: Verify Simulation Transition
    Tool: bash
    Preconditions: None
    Steps:
      1. grep "剩余的不等式约束" body/graduate/paper1/3_simulation.tex
    Expected Result: Command succeeds (exit code 0).
    Evidence: .sisyphus/evidence/task-4-grep-sim.txt
  ```

- [x] 5. Results Evaluation Decoupling

  **What to do**:
  - Edit `body/graduate/paper1/4_results.tex`.
  - Locate section 4.1.2 (与直接 KKT 方法的比较).
  - Change "相比之下，本文紧凑表示天然满足式 X，无需为这些内在约束额外付出计算" to a more decoupled, objective statement: "相比之下，本文的紧凑表示在参数化层面满足式 X。在相同的实验设置下，这避免了对内在约束进行额外计算迭代所需的开销。"
  - Scan for and remove any instance of "魔咒" (replace with "计算瓶颈" or similar).

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Tone adjustment in results evaluation.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocked By**: Task 1

  **References**:
  - `body/graduate/paper1/4_results.tex` - Section 4.1.2.

  **Acceptance Criteria**:
  - [ ] Strong rhetoric decoupling is applied to the KKT comparison.
  - [ ] Project still compiles.

  **QA Scenarios**:
  ```yaml
  Scenario: Verify Compilation After All Edits
    Tool: bash
    Preconditions: All tasks complete
    Steps:
      1. latexmk -c && latexmk
    Expected Result: Compilation succeeds without fatal errors.
    Evidence: .sisyphus/evidence/task-5-latexmk.txt
  ```

---

## Final Verification Wave

- [x] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. Verify that all 5 target files were modified. Verify that no mathematical formulas or TikZ environments were damaged. Check evidence files exist in `.sisyphus/evidence/`.
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT: APPROVE/REJECT`

- [x] F2. **Code Quality Review** — `unspecified-high`
  Run `latexmk` to ensure the thesis still compiles perfectly. Review Git diff to ensure no unintended files were touched.
  Output: `Build [PASS/FAIL] | Files [N clean/N issues] | VERDICT`

- [x] F3. **Real Manual QA** — `unspecified-high`
  Execute EVERY QA scenario from EVERY task — verify that `grep` commands yield the expected success/fail status indicating the text was actually changed. Save to `.sisyphus/evidence/final-qa/`.
  Output: `Scenarios [N/N pass] | VERDICT`

- [x] F4. **Scope Fidelity Check** — `deep`
  Verify that ONLY rhetorical packaging and transitions were altered, and that the scientific claims remain exactly the same.
  Output: `Tasks [N/N compliant] | Contamination [CLEAN/N issues] | VERDICT`

---

## Commit Strategy

- **1**: `refactor(paper1): improve academic tone and cross-chapter terminology mapping` - `body/graduate/intro/*.tex`, `body/graduate/paper1/*.tex`, `latexmk`

---

## Success Criteria

### Verification Commands
```bash
latexmk  # Expected: output successful compilation without fatal errors
grep -r "极其优雅地" body/graduate/ # Expected: no results
```

### Final Checklist
- [x] All "Must Have" present (latexmk passes)
- [x] All "Must NOT Have" absent (no math/tikz broken)
- [x] All QA scenarios pass
