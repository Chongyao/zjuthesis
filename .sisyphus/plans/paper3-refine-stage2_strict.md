# Paper3 Refine Stage 2: Intro & Conclusion Strict Alignment

## TL;DR

> **Quick Summary**: 针对已初步去修辞化的 `1_intro.tex` 和 `5_conclusion.tex` 进行极严苛的双向校对（对比英文原文），找出遗漏的机制解释、术语漂移以及残存的翻译腔，生成不可逾越的执行任务链，确保文本 100% 达到“严谨、朴实、准确”标准。
>
> **Deliverables**:
> - 彻底校对并修正后的 `1_intro.tex`
> - 彻底校对并修正后的 `5_conclusion.tex`
> - 每个修改段落的 Agent-Executed QA 证据
>
> **Estimated Effort**: High
> **Parallel Execution**: YES - 2 waves (Intro tasks parallel, then Conclusion)
> **Critical Path**: `1_intro` 段落级查漏补缺 $\rightarrow$ `5_conclusion` 边界收缩 $\rightarrow$ 全局编译与一致性验证

---

## Context

### Original Request
用户指出先前未严格遵守 Plan Mode 纪律，过早地、粗粒度地切入了正文修改。要求废弃旧的 Stage 2 流程，一边严格双向校对（当前修改后的中文 vs 英文原文），一边重新生成详尽、标准的 Prometheus 计划文件，交由 Atlas 严格执行。

### Research Findings (Ongoing Calibration)
目前 `1_intro.tex` 已被剥离了大量极端修辞（如“浩瀚天堑”），但双向校对暴露出以下潜在风险点：
1. **P1-P3 (Background)**: 需进一步核对 Krylov、SLEPc、MUMPS 的上下文是否完全还原原文对 condition number 和 flexibility 的论述，移除残留的“极高”、“严峻”等修饰。
2. **P4-P7 (Related Work)**: 需确保文中对相关算法的评价客观中立，统一定义术语。
3. **P8-P12 (Mechanism)**: **(已完成)** 机制段落已被成功转移至 `\subsection{本章方法与贡献}` 下，Fourier 相位与静力平衡解释已到位。
4. **P13 (Contributions)**: 现有的三点贡献陈述仍然残留夸大词汇（如“错位多重网格划分融合策略”、“超高效”），需降温至事实描述。
5. **5_conclusion.tex**: 存在术语错误（如“相角互补”应为“相位互补”），且展望部分（如“乘数级别提升”）依然超出了学术结论的合理边界。

---

## Work Objectives

### Core Objective
完成 `1_intro.tex` 和 `5_conclusion.tex` 的“最后一公里”精修，确保不存在任何缺乏原文支撑的扩写，不存在任何遗漏的数理机制。

### Concrete Deliverables
- 修订后的 `body/graduate/paper3/1_intro.tex`
- 修订后的 `body/graduate/paper3/5_conclusion.tex`
- 对应的 `.sisyphus/evidence/` 验证记录

### Definition of Done
- [ ] `1_intro.tex` 中每一段的因果逻辑链均能与英文原文严格映射。
- [ ] `5_conclusion.tex` 中不存在超出原文 `6.0-conclusion.tex` 数据支撑的定性结论。
- [ ] 强制统一所有术语（CMS, SE-free IMR, 相位补足，交错划分）。

### Must NOT Have (Guardrails)
- 不允许任何“我认为这样写更好”的自由发挥，一切修改需有英文原文锚点。
- 不允许脱离上下文单改一句，必须考虑段落连贯性。

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** - ALL verification is agent-executed. No exceptions.

### QA Policy
所有改动必须通过以下自动化/代理验证：
- **LaTeX Compilation**: `latexmk` 必须全程通过，确保 `\textcolor` 等格式宏无损坏。
- **Agent Peer Review**: 修改后由 `unspecified-high` 代理对照原文检查是否引入了“过度修辞”或“语义丢失”。

---

## Execution Strategy

### Parallel Execution Waves

Wave 1 (Intro Refinement - High Precision):
├── Task 1: Calibrate Intro P1-P3 (Motivation & Context) [writing]
├── Task 2: Calibrate Intro P4-P7 (Related Work Terminology) [writing]
└── Task 3: Calibrate Intro P8-P12 (Phase & IMR Mechanism) [writing]

Wave 2 (Contributions & Conclusion):
├── Task 4: Calibrate Intro P13 (Contributions List) [writing]
└── Task 5: Calibrate 5_conclusion.tex (Boundary Retraction) [writing]

Wave FINAL (Verification):
├── Task F1: Full LaTeX Compilation Check [quick]
├── Task F2: Terminology Sweeping Audit [oracle]
└── Task F3: Tone & Style Fidelity Check [unspecified-high]

Critical Path: Wave 1 $\rightarrow$ Wave 2 $\rightarrow$ Wave FINAL

---

## TODOs

- [x] 1. Calibrate Intro P1-P3 (Motivation & Context)

  **What to do**:
  - Read current `1_intro.tex` P1-P3 and original `1.0-introduction.tex`.
  - Verify if the explanation of ill-conditioning (条件数病态) and lack of flexibility for design iterations (设计迭代的灵活性) perfectly matches the original text.
  - Fix any remaining awkward phrasing or slight over-translations.

  **Must NOT do**:
  - Do not remove the thesis-specific bridge in P1 (connecting to chapters 1 & 2), but ensure its tone is perfectly flat.

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Requires high-precision translation alignment and subtle tone tuning.
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] P1-P3 strictly mirrors the logical flow of the original English introduction.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Semantic equivalence check for P1-P3
    Tool: Read + Oracle evaluation
    Preconditions: 1_intro.tex is modified.
    Steps:
      1. Extract P1-P3 from 1_intro.tex.
      2. Compare with first 3 paragraphs of 1.0-introduction.tex.
      3. Assert that no original technical limitations (e.g., global matrix decomposition cost) are omitted.
    Expected Result: 100% semantic match, no hyperbolic tone.
    Evidence: .sisyphus/evidence/stage2-task1-audit.txt
  ```

- [x] 2. Calibrate Intro P4-P7 (Related Work Terminology)

  **What to do**:
  - Check the translated subsections for CMS, IMR, Partitions, and Singular Matrix Pencil.
  - Ensure terms like "fixed-interface normal modes" and "static constraint modes" are strictly translated as "固定界面正规模态" and "静态约束模态".
  - Ensure the description of AMLS, ACMS, FETI-DP is objective and matches the source citations precisely.

  **Must NOT do**:
  - Do not alter the citation commands (`\cite{...}`).

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] Zero terminology drift in the Related Work section.

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Citation and Terminology verification
    Tool: Grep
    Preconditions: None
    Steps:
      1. Grep for "固定界面", "约束模态", "Schur 补" in the related work block.
      2. Check that no colloquial alternatives (like "固支边界" or "舒尔补") exist.
    Expected Result: Strict terminology adherence.
    Evidence: .sisyphus/evidence/stage2-task2-audit.txt
  ```

- [x] 3. Calibrate Intro P8-P12 (Phase & IMR Mechanism)

  **Status**: COMPLETED. The mechanism transition (Fourier windowing, phase complement, static equilibrium mapping) has been successfully rewritten in rigorous Chinese and moved to the correct structural position under `\subsection{本章方法与贡献}`.
- [x] 4. Calibrate Intro P13 (Contributions List)

  **What to do**:
  - Align the three bullet points exactly with the original English contributions list.
  - Bullet 1: Phase-complement via spatially staggered partitions.
  - Bullet 2: Schur- and eigen-free IMR.
  - Bullet 3: Experimental verification (strong/weak scaling, local update, large-scale MPI).

  **Must NOT do**:
  - Do not use words like "极大", "极其", "惊人". Keep quantities factual ("三个数量级" is fine if backed by data).

  **Recommended Agent Profile**:
  - **Category**: `writing`

  **Parallelization**:
  - **Can Run In Parallel**: NO (Safer to run sequentially after P1-P12 to ensure cohesive flow)
  - **Parallel Group**: Wave 2
  - **Blocked By**: 1, 2, 3

  **Acceptance Criteria**:
  - [ ] Contributions are factual, verifiable, and tone-neutral.

- [x] 5. Calibrate 5_conclusion.tex (Boundary Retraction)

  **What to do**:
  - Read `5_conclusion.tex` and original `6.0-conclusion.tex`.
  - Strip any speculative future work that wasn't in the original paper (unless strictly necessary for dissertation coherence, in which case it must be toned down).
  - Ensure the summary of the method perfectly matches the newly locked terminology from Task 3 & 4.

  **Must NOT do**:
  - Do not introduce new concepts not discussed in the chapter.

  **Recommended Agent Profile**:
  - **Category**: `writing`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] Conclusion relies strictly on demonstrated evidence and original paper claims.

---

## Final Verification Wave

- [x] F1. **Full LaTeX Compilation Check** — `quick`
  Run `latexmk` to ensure no syntax errors or broken references were introduced during the rewriting process.

- [x] F2. **Terminology Sweeping Audit** — `oracle`
  Scan both refined files for banned variants (e.g., ensuring "相角互补" does not exist, only "相位互补").

- [x] F3. **Tone & Style Fidelity Check** — `unspecified-high`
  Read the final versions against the anti-pattern dictionary. Verify zero instances of hyperbolic language.

---

## Success Criteria

### Final Checklist
- [x] All 5 rewriting tasks completed with 1:1 original mapping evidence.
- [x] Final verification wave passes with 0 terminology violations.
- [x] Thesis builds cleanly.