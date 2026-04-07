# Plan: paper2-structural-alignment

## TL;DR

> **Quick Summary**: Reorganize Chapter 3 (Paper 2) to strictly mirror the top-level section structure of Chapter 2 (Paper 1), enhancing cross-chapter alignment and reflecting the Introduction's three-problem framework.
> 
> **Deliverables**: 
> - Re-structured `paper2` LaTeX files with 5 top-level sections matching Paper 1 exactly.
> - Preserved substantive content (no deletion/rewriting of physics, math, or results).
> 
> **Estimated Effort**: Short
> **Parallel Execution**: NO - sequential file refactoring
> **Critical Path**: Define mapping -> Update `main.tex` and files -> Fix references

---

## Context

### Original Request
Reorganize Paper 2 (Chapter 3) to use the exact same section structure as Paper 1 (Chapter 2) so that it aligns better with the Introduction. Keep the content unchanged.

### Interview Summary
**Key Discussions**:
- [Target]: Reorganize Paper 2 to match Paper 1 top-level sections.
- [Alignment]: Title-level alignment (exact mirroring of Paper 1 section titles).
- [Constraint]: Substantive content remains unchanged.

### Metis Review
**Identified Gaps** (addressed):
- [Gap 1]: Semantic mismatch between Paper 1's title "基函数变换" and Paper 2's method. -> Addressed: Paper 2's method *is* technically a basis function optimization/transformation (h-refinement + Dirac-wavelet basis), so this title actually fits perfectly.
- [Gap 2]: Related Work consolidation. -> Addressed: Paper 1 integrates Related Work into Section 1. We will merge Paper 2's standalone related work into Section 1.
- [Gap 3]: Broken cross-references ("上一节" etc.). -> Addressed: Explicit QA scenario added to check text flow.

---

## Work Objectives

### Core Objective
Restructure the LaTeX files in `body/graduate/paper2/` so that the compiled Chapter 3 has exactly five `\section` headings matching Chapter 2, while preserving all existing text, equations, and figures.

### Concrete Deliverables
- Re-sectioned files in `body/graduate/paper2/`

### Definition of Done
- [ ] Chapter 3 compiles successfully with `latexmk`.
- [ ] Chapter 3 has exactly 5 `\section` commands with the target titles.
- [ ] Zero substantive paragraphs, equations, or figures from the original paper2 are missing.

### Must Have
- Target Top-Level Structure:
  1. 研究背景
  2. 软硬耦合分析
  3. 基函数变换
  4. 实验结果与分析
  5. 本章小结

### Must NOT Have (Guardrails)
- Do not delete substantive content (equations, results, claims).
- Do not rewrite paragraphs except for minimal transition/connector phrases if strictly necessary.
- Do not change figure/table captions or data.

---

## Verification Strategy

### Test Decision
- **Infrastructure exists**: NO
- **Automated tests**: None
- **Agent-Executed QA**: ALWAYS. We will use `grep` and `bash (latexmk)` to verify the structure and compilation.

### QA Policy
Every task MUST include agent-executed QA scenarios using `bash` or `grep`.

---

## Execution Strategy

### Section Mapping Strategy

| Original Paper 2 Structure | Target Paper 1 Structure | Action/Mapping |
| :--- | :--- | :--- |
| **1. 引言** | **1. 研究背景** | Rename to `1. 研究背景`. |
| 1.1 相关工作与传统方法的局限 | 1.1 相关工作与传统方法的局限 | Keep as subsection. |
| **2. 相关工作** | | Move content into `1.1 相关工作与传统方法的局限`. |
| 1.2 本章方法与贡献 | 1.2 本章方法与贡献 | Keep as subsection. |
| **3. 研究背景** (Mathematical origin) | **2. 软硬耦合分析** | Rename section. This fits perfectly, as it analyzes the ill-conditioning source. |
| 3.1 主要贡献 | | Consolidate with `1.2 本章方法与贡献` or keep as a paragraph in Intro. |
| **4. 构建数值适应的层次结构** | **3. 基函数变换** | Rename section. The method is literally optimizing basis functions to adapt to numerics. |
| 4.1 - 4.4 Subsections | 3.1 - 3.4 Subsections | Keep subsections as they are. |
| **5. 结果与讨论** | **4. 实验结果与分析** | Rename section. |
| 5.1 - 5.4 Subsections | 4.1 - 4.4 Subsections | Keep subsections as they are. |
| **6. 本章小结** | **5. 本章小结** | Keep section name. |

### Parallel Execution Waves

Wave 1 (Sequential Refactoring):
├── Task 1: Rename and reorganize Section 1 & 2 files
├── Task 2: Rename and reorganize Section 3, 4, 5 files
└── Task 3: Update `main.tex` and verify compilation

Critical Path: Task 1 → Task 2 → Task 3 → Final Verification

---

## TODOs

- [x] 1. Reorganize Section 1 (研究背景) and Section 2 (软硬耦合分析)

  **What to do**:
  - Edit `paper2/1_intro.tex`: Change `\section{引言}` to `\section{研究背景}`.
  - Read `paper2/2_related.tex`. Move its entire content into `paper2/1_intro.tex` under the existing subsection `\subsection{相关工作与传统方法的局限}`.
  - Read `paper2/3_background.tex`. Change `\section{研究背景}` to `\section{软硬耦合分析}`.
  - In `paper2/3_background.tex`, there is a `\subsection{主要贡献}`. Move this content into `paper2/1_intro.tex` under `\subsection{本章方法与贡献}` to avoid duplication, or append it there logically.
  
  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Text manipulation and moving blocks.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: NO (Sequential)

  **References**:
  - `body/graduate/paper2/1_intro.tex`
  - `body/graduate/paper2/2_related.tex`
  - `body/graduate/paper2/3_background.tex`

  **Acceptance Criteria**:
  - [ ] `1_intro.tex` contains `\section{研究背景}` and merged related work.
  - [ ] `3_background.tex` contains `\section{软硬耦合分析}`.

  **QA Scenarios**:
  ```
  Scenario: Check section titles
    Tool: Bash (grep)
    Steps:
      1. grep -E "\\section\{" body/graduate/paper2/1_intro.tex body/graduate/paper2/3_background.tex
    Expected Result: Shows \section{研究背景} and \section{软硬耦合分析}
    Evidence: .sisyphus/evidence/task-1-grep.txt
  ```

- [x] 2. Reorganize Section 3 (基函数变换), Section 4 (实验结果与分析), Section 5 (本章小结)

  **What to do**:
  - Edit `paper2/4_method.tex`: Change `\section{构建数值适应的层次结构}` to `\section{基函数变换}`.
  - Edit `paper2/5_results.tex`: Change `\section{结果与讨论}` to `\section{实验结果与分析}`.
  - Check `paper2/6_summary.tex`: It should already be `\section{本章小结}`. Keep it.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Simple text replacement.

  **Parallelization**:
  - **Can Run In Parallel**: NO (Sequential)

  **References**:
  - `body/graduate/paper2/4_method.tex`
  - `body/graduate/paper2/5_results.tex`

  **Acceptance Criteria**:
  - [ ] Titles updated in files.

  **QA Scenarios**:
  ```
  Scenario: Check section titles
    Tool: Bash (grep)
    Steps:
      1. grep -E "\\section\{" body/graduate/paper2/4_method.tex body/graduate/paper2/5_results.tex body/graduate/paper2/6_summary.tex
    Expected Result: Shows exactly the 3 target section titles.
    Evidence: .sisyphus/evidence/task-2-grep.txt
  ```

- [x] 3. Update `main.tex` and Verify Compilation

  **What to do**:
  - Edit `body/graduate/paper2/main.tex`: Update the `\inputbody` list to reflect the new structure. You may need to rename files to keep it logical (e.g., `3_background.tex` -> `2_analysis.tex`), but simply updating the `\inputbody` order and commenting out `2_related.tex` (since its content was moved) is sufficient.
  - Let's use the existing files but change the inclusion in `main.tex`:
    ```latex
    \inputbody{paper2/1_intro}
    %\inputbody{paper2/2_related} % merged into intro
    \inputbody{paper2/3_background} % now section 2
    \inputbody{paper2/4_method} % now section 3
    \inputbody{paper2/5_results} % now section 4
    \inputbody{paper2/6_summary} % now section 5
    ```
  - Run `latexmk` to ensure the document compiles without errors.
  
  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: Needs to run build and check for LaTeX errors.

  **Parallelization**:
  - **Can Run In Parallel**: NO (Sequential)

  **References**:
  - `body/graduate/paper2/main.tex`

  **Acceptance Criteria**:
  - [ ] `main.tex` reflects the 5-file inclusion.
  - [ ] Compilation succeeds.

  **QA Scenarios**:
  ```
  Scenario: Compile thesis
    Tool: Bash (latexmk)
    Steps:
      1. latexmk -c
      2. latexmk
    Expected Result: Compilation succeeds without fatal errors.
    Evidence: .sisyphus/evidence/task-3-build.txt
  ```

---

## Final Verification Wave

- [x] F1. **Plan Compliance Audit** — `oracle`
  Read `paper2` files. Verify exactly 5 `\section` commands exist matching Paper 1. Check evidence files.
  Output: `VERDICT: APPROVE/REJECT`

- [x] F2. **Code Quality Review** — `unspecified-high`
  Run `latexmk`. Verify no broken cross-references (warnings about undefined references).
  Output: `Build [PASS/FAIL] | VERDICT`

- [x] F3. **Real Manual QA** — `unspecified-high`
  Read through the merged `1_intro.tex`. Check if the transition between original intro and merged related work / contributions flows logically without duplicated paragraphs.
  Output: `Flow [PASS/FAIL] | VERDICT`

- [x] F4. **Scope Fidelity Check** — `deep`
  Compare `git diff` of `paper2` directory. Verify no substantive equations, figures, or claims were deleted.
  Output: `Contamination [CLEAN/N issues] | VERDICT`
