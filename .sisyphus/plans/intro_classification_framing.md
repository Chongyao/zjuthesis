# Intro Classification Framing Refinement

## TL;DR
> **Quick Summary**: Shift the rhetorical framing of the introduction from a "chapter method escalation" narrative to a "mechanism-based classification" (Physical -> Discretization -> Algorithmic) narrative. Update colloquial terms to academic standards.
> 
> **Deliverables**:
> - `body/graduate/intro/1_background.tex` (2 modifications)
> - `body/graduate/intro/2_related_and_problems.tex` (4 modifications + terminology upgrade)
> - `body/graduate/intro/3_contributions_and_organization.tex` (5 modifications)
> 
> **Estimated Effort**: Quick
> **Parallel Execution**: YES - 3 files can be modified in parallel.

---

## Context
### Original Request
The user requested to weaken the sequential/progressive relationship between the three thesis chapters and strengthen their classification into three mechanism layers: Constitutive (Physical), Discretization, and Algorithmic. The user also requested to replace the colloquial term "刚度污染" (stiffness pollution) with the more academic term "数值刚化效应" (numerical stiffening effect).

### Interview Summary
**Key Decisions**:
- **Classification Strategy**: The problem sources progress in abstract layers (intrinsic physics -> representation -> algorithm), but the chapters themselves are parallel cases of "representation space reconstruction".
- **Terminology**: "人工刚度污染" will be upgraded to "数值刚化效应".

---

## Work Objectives
### Core Objective
Apply 11 specific rhetorical shifts to establish the three-layer mechanism classification in the thesis introduction.

### Concrete Deliverables
- Modified `1_background.tex`
- Modified `2_related_and_problems.tex`
- Modified `3_contributions_and_organization.tex`

### Definition of Done
- [x] 11 target sentences successfully rewritten.
- [x] "刚度污染" replaced with "数值刚化效应".
- [x] `latexmk` compiles successfully.

---

## Verification Strategy
> **ZERO HUMAN INTERVENTION** - ALL verification is agent-executed.
### QA Policy
- **Compilation**: Use `interactive_bash` or `bash` to run `latexmk -outdir=out zjuthesis` and verify 0 fatal errors.
- **Diff Check**: Read the diff to ensure EXACTLY 11 areas were touched and no structural LaTeX commands were broken.

---

## Execution Strategy

Wave 1 (Parallel text replacement):
├── Task 1: Rewrite 1_background.tex [quick]
├── Task 2: Rewrite 2_related_and_problems.tex [quick]
└── Task 3: Rewrite 3_contributions_and_organization.tex [quick]

Wave FINAL:
└── Task F1: Compile & Plan Compliance Audit [oracle]

---

## TODOs

- [x] 1. Rewrite 1_background.tex
  **What to do**:
  - Replace line 21's "最终拓展至..." with: `第三类则更进一步，源于降阶算法在构造近似空间时引入的虚假边界刚性约束（以固定界面模态综合法为代表），这会严重干扰系统对全局低频响应的表达。`
  - Replace line 25's "通过对这一系列问题的探讨与整合..." with: `针对这三类处于不同物理与数值层次的软硬耦合机制，本论文旨在...`
  
  **QA Scenarios**:
  ```
  Scenario: File compiles and text updated
    Tool: Bash
    Steps:
      1. grep "处于不同物理与数值层次" body/graduate/intro/1_background.tex
    Expected Result: Match found.
    Evidence: .sisyphus/evidence/task-1-background.txt
  ```

- [x] 2. Rewrite 2_related_and_problems.tex
  **What to do**:
  - Replace line 106 "下面我们将依次剖析..." with: `下面我们将从物理本构、空间离散到算法构造这三个层次，分别剖析物理仿真中三类最具代表性的软硬耦合病态系统...`
  - Replace lines 139-141 "学术界开始了第二类路线...切入点。" with: `不可伸长细杆由于其硬约束表现为显式的极短距离，是物理本构导致软硬耦合的最直观体现。通过坐标与表示空间的重构来内化这些物理硬约束，构成了本文应对第一层次病态刚度的核心案例。`
  - Prepend to line 163 "当局部网格严重扁平...": `即使底层物理参数（如本构材料张量）并不极端，不合适的离散化仍会人为制造局部的高刚度方向。在有限元方法中，局部刚度的二次型不仅取决于材料参数，更受到基函数梯度与几何映射（雅可比矩阵）的直接控制。`
  - Replace line 169 "面对这种由畸变网格单元引起的人工刚度污染，最直观的第一类解决路径是..." with: `面对这种由畸变网格单元引发的数值刚化效应，最直观的思路是从几何源头入手...`
  
  **QA Scenarios**:
  ```
  Scenario: File compiles and text updated
    Tool: Bash
    Steps:
      1. grep "数值刚化效应" body/graduate/intro/2_related_and_problems.tex
    Expected Result: Match found.
    Evidence: .sisyphus/evidence/task-2-problems.txt
  ```

- [x] 3. Rewrite 3_contributions_and_organization.tex
  **What to do**:
  - Replace line 123 "发展出了一系列层层深入的重构策略..." with: `发展出了一套从物理内生到离散诱导、再到算法附加的系统性重构框架及相应的模拟算法。`
  - Delete the last two sentences of line 124: `然而，这种基于一维链式...极大的局限。`
  - Replace line 126 "为了处理网格导致的软硬耦合，第三章将研究对象转向了..." with: `即使物理模型本身并不极端，离散表示仍可能引入数值病态。第三章针对\textbf{网格导致的软硬耦合}，探讨了包含恶劣畸变单元的有限元模拟。`
  - Replace line 128's "第四章致力于在更宏观的层面打破大尺度系统算法导致的软硬耦合..." with: `第四章关注即使在物理模型与离散网格都合理时，\textbf{算法构造导致的附加软硬耦合}。直接切入大规模广义特征值问题中的模态综合法（CMS）。` AND replace "在此基础上...进一步提出" with `由于传统的界面模态构造高度依赖 Schur 补运算，会导致巨大的通信与内存开销，本章针对这一瓶颈提出了一种无 Schur 补...`
  - Replace line 130 "第五章总结了本文围绕‘消除局部高频基函数’所发展的一系列表示空间重构思路..." with: `第五章总结了本文针对不同层次软硬耦合问题所提出的表示空间重构思路、方法和核心结论。`
  
  **QA Scenarios**:
  ```
  Scenario: File compiles and text updated
    Tool: Bash
    Steps:
      1. grep "物理内生到离散诱导" body/graduate/intro/3_contributions_and_organization.tex
    Expected Result: Match found.
    Evidence: .sisyphus/evidence/task-3-contributions.txt
  ```

---

## Final Verification Wave
- [x] F1. **Plan Compliance Audit** — `oracle`
  Run `latexmk -outdir=out zjuthesis`. Verify 0 fatal errors. Verify no "刚度污染" remains in the intro.
