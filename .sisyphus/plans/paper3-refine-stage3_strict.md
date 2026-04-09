# Paper3 Refine Stage 3: Core Chapters Strict Terminology & Translation-ese Smoothing

## TL;DR

> **Quick Summary**: 针对 `paper3` 的核心技术与实验章节（`2_representation.tex`, `3_simulation.tex`, `4_results.tex`, `5_1_alg_adaptive_shifting.tex`）进行全盘扫描，强制统一在 Stage 1/2 锁定的核心术语表达，消除翻译腔与长难句，确保 thesis 全文专业术语的绝对唯一性。
>
> **Deliverables**:
> - 术语严格一致且无明显翻译腔的核心技术章节。
> - 修正后的伪代码及其对应的正文解释。
> - 最终本地编译检查及 PDF 完整性确认。
>
> **Estimated Effort**: Medium
> **Parallel Execution**: YES - 2 waves (Independent terminology sweeps can run in parallel, followed by specific translation-ese fixes)
> **Critical Path**: 全局术语统一 $\rightarrow$ 局部平滑长难句 $\rightarrow$ 最终编译与交叉引用验证

---

## Context

### Preceding Stage (Stage 2 Strict)
- 已经完成了 `1_intro.tex` (引言) 和 `5_conclusion.tex` (本章小结) 的深度重写与逻辑归位，消除了“浩瀚天堑”、“逆转乾坤”等过度文学化、情绪化的 AI-slop 修辞。
- 重构了“加窗傅里叶模态与相位互补”和“静力平衡映射”的机理论述，恢复了学术朴实风格。
- **现存遗留问题**：在核心理论、实现及结果章节（第 2、3、4、5.1 节）中，仍可能存在同一专业词汇的多种变体（如“相角互补” vs “相位互补”，“免 Schur 补” vs “无 Schur 补和特征求解”等），且长公式后的解释性中文存在从英文生硬直译的翻译腔。

### Work Objectives
- **Target 1 (Terminology Enforcement)**: 实施零容忍的术语替换，确保所有核心词汇全篇唯一，并与 `1_intro.tex` 保持绝对一致。
- **Target 2 (Translation-ese Smoothing)**: 对核心章节的公式推导前后的解释性语句（`2_representation`、`3_simulation`）和实验结果分析（`4_results`）进行轻度平滑处理，使中文表达更加自然、流畅。

---

## Terminology Enforcement (Strict Baseline)

| 概念 | 统一中文术语 (必须使用) | 禁用的变体 |
|------|-------------------------|------------|
| Phase complement / complementary | **相位补足** (动/名词) / **相位互补** (形) | 相角互补、相位补充 |
| Staggered partitions | **交错划分** | 交错的划分、错位划分、错位多重网格划分 |
| Schur- and eigen-free IMR | **无 Schur 补和特征求解的 IMR** (或 SE-free IMR) | 免 Schur 补、解绑局部特征运算的 IMR |
| Adaptive shifting | **自适应位移** | 自适应移位 |
| Phase-complete basis | **相位完备基** | 完备相位基函数 |
| Fixed-interface / boundary | **固定界面** / **固定边界** | 固支边界 |

---

## Execution Strategy

### Parallel Execution Waves

Wave 1 (Global Terminology Enforcement):
├── Task 1: Enforce Terminology in 2_representation.tex [writing]
├── Task 2: Enforce Terminology in 3_simulation.tex & 5_1_alg [writing]
└── Task 3: Enforce Terminology in 4_results.tex [writing]

Wave 2 (Translation-ese Smoothing & Metric Alignment):
├── Task 4: Smooth Translation-ese in 2_representation & 3_simulation [writing]
└── Task 5: Align Metrics and Figure Refs in 4_results [writing]

Wave FINAL (Verification):
├── Task F1: Full LaTeX Compilation Check [quick]
├── Task F2: Terminology Sweeping Audit across Chapter 4 [oracle]
└── Task F3: Cross-Reference & Macro Fidelity Check [unspecified-high]

Critical Path: Wave 1 $\rightarrow$ Wave 2 $\rightarrow$ Wave FINAL

---

## TODOs

- [x] 1. Enforce Terminology in 2_representation.tex

  **What to do**:
  - Read `2_representation.tex`.
  - Replace any occurrence of banned terms (e.g., "相角", "错位划分") with the required terminology baseline.
  - Pay special attention to the `Analysis of the 1D Laplacian problem` and `Multiple partitions for CMS` subsections.

  **Must NOT do**:
  - Do not modify mathematical formulas or their inline LaTeX variables (e.g., $\mathbf{K}, \mathbf{M}, S^p, S^d$).

  **Recommended Agent Profile**:
  - **Category**: `writing`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] Zero terminology drift in `2_representation.tex`.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Terminology grep verification for 2_representation
    Tool: Grep
    Preconditions: 2_representation.tex modified.
    Steps:
      1. Grep for "相角", "错位", "固支".
    Expected Result: 0 matches found.
    Evidence: .sisyphus/evidence/stage3-task1-audit.txt
  ```

- [x] 2. Enforce Terminology in 3_simulation.tex & 5_1_alg

  **What to do**:
  - Read `3_simulation.tex` and `5_1_alg_adaptive_shifting.tex`.
  - Enforce "无 Schur 补和特征求解的 IMR" or "SE-free IMR".
  - Ensure "adaptive shifting" is strictly translated as "自适应位移", not "自适应移位".
  - Verify that the text in `5_1_alg` matches the algorithmic terminology in `3_simulation.tex`.

  **Must NOT do**:
  - Do not break `\begin{algorithm}` or algorithm macro structures.

  **Recommended Agent Profile**:
  - **Category**: `writing`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] "自适应位移" and "无 Schur 补和特征求解" are used uniformly.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Terminology grep verification for 3_simulation
    Tool: Grep
    Preconditions: 3_simulation.tex modified.
    Steps:
      1. Grep for "移位", "免 Schur".
    Expected Result: 0 matches found.
    Evidence: .sisyphus/evidence/stage3-task2-audit.txt
  ```

- [x] 3. Enforce Terminology in 4_results.tex

  **What to do**:
  - Check `4_results.tex` for instances of "强扩展" (strong scaling), "弱扩展" (weak scaling), "局部更新" (local updating).
  - Ensure any teaser text or statistical text absorbed from original `5.1-statistics` does not contain hyperbolic language.

  **Must NOT do**:
  - Do not change the numerical values or error percentages reported.

  **Recommended Agent Profile**:
  - **Category**: `writing`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] Terminology matches the established baseline.

- [x] 4. Smooth Translation-ese in 2_representation & 3_simulation

  **What to do**:
  - Deep-read paragraphs bridging equations.
  - Identify long, convoluted sentences that clearly stem from direct English translation (e.g., heavy use of "被...", "由...所导致").
  - Break them into shorter, active-voice Chinese academic sentences without losing physical or mathematical meaning.

  **Must NOT do**:
  - Do not alter the logical flow or change the narrative of the original paper's mechanism.

  **Recommended Agent Profile**:
  - **Category**: `writing`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocked By**: 1, 2

  **Acceptance Criteria**:
  - [ ] Sentence structures feel native to rigorous Chinese academic writing while preserving exact mathematical logic.

- [x] 5. Align Metrics and Figure Refs in 4_results

  **What to do**:
  - Verify that metric descriptions (like "Error-Time curve", "condition number", "memory footprint") are described fluidly.
  - Ensure sentences connecting to figures (e.g., "As shown in Fig. 6...") are natural (e.g., "如图 6 所示...").

  **Must NOT do**:
  - Do not modify `\ref{...}` labels.

  **Recommended Agent Profile**:
  - **Category**: `writing`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocked By**: 3

  **Acceptance Criteria**:
  - [ ] Natural flow in result reporting with intact data claims.

---

## Final Verification Wave

- [x] F1. **Full LaTeX Compilation Check** — `quick`
  Run `latexmk` to ensure no syntax errors or broken references were introduced during the terminology sweeping and sentence smoothing.

- [x] F2. **Terminology Sweeping Audit across Chapter 4** — `oracle`
  Grep the entire `body/graduate/paper3/` directory for any remaining banned variants (相角, 错位多重, 移位).

- [x] F3. **Cross-Reference & Macro Fidelity Check** — `unspecified-high`
  Ensure math macros (`\DET`, `\FPP`) and citation commands (`\cite`, `\ref`) were not accidentally deleted or malformed.

---

## Success Criteria

### Final Checklist
- [x] Terminology is strictly unified across all 6 sections.
- [x] Convoluted translation-ese is broken into rigorous, short Chinese sentences.
- [x] Final verification wave passes with 0 terminology violations and 0 compilation errors.