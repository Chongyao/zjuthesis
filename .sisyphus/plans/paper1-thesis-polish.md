# Paper 1 Thesis Polish

## TL;DR

> **Quick Summary**: Polish Chapter 2 (paper1) and its corresponding intro sections to ensure dissertation-level maturity. We will unify terminology, temper exaggerated language, enhance bridging between sections, and refine heading titles.
> 
> **Deliverables**: 
> - Unify terminology ("轴角链式坐标" and "零内在几何硬约束") across intro and chapter 2.
> - Expand problem diagnosis with penalty method condition number issues at the end of `2_representation.tex`.
> - Add smooth transitions in `3_simulation.tex`.
> - Integrate a short chapter guide into `1_intro.tex` (without making it a standalone paragraph).
> - Rename appendix-like titles to be descriptive and thesis-native.
> - Tone down overly absolute claims ("完美", "彻底", "卓越") restricted ONLY to paper1.
> 
> **Estimated Effort**: Medium
> **Parallel Execution**: YES

---

## Context

### Original Request
The user requested to polish Chapter 2 (paper 1) to match the maturity of a Ph.D. thesis chapter based on prior review feedback. The user explicitly accepted specific edits and rejected others.

**Approved Changes**:
1. **Terminology**: Use "轴角链式坐标" instead of "关节角广义坐标变换" in the intro to align with Chapter 2. Soften "零约束" to "零内在几何硬约束".
2. **Problem Expansion**: Add a paragraph at the end of `body/graduate/paper1/2_representation.tex` explaining that the common penalty method for inextensible constraints with weight -> infinity leads to ill-conditioned stiffness matrices and severely restricts the time step in implicit Euler integration. Add proper transition to the next section.
3. **Section Bridging**: Add short transition sentences at the boundaries of `body/graduate/paper1/3_simulation.tex`.
4. **Chapter Guide**: Integrate the chapter guide into `body/graduate/paper1/1_intro.tex` without creating a standalone paragraph.
5. **Heading Rename**: Provide low-risk heading renaming for the former appendix sections (`app_*.tex`) to integrate them into the main text logically.
6. **Tone-down**: Soften promotional language ("完美", "彻底", "数量级") strictly within the scope of paper 1.

**Rejected Changes (Out of Scope)**:
- No structural restructuring of the former appendix files.
- No additional experiment-to-contribution mappings.
- No boundary scope expansion.
- No preconditioner independent value dismantling.
- No tone-down in intro, paper2, or paper3.

---

## Work Objectives

### Definition of Done
- [ ] No occurrences of "关节角广义坐标变换" in intro (replaced with "轴角链式坐标").
- [ ] "零约束" downgraded to "零内在几何硬约束" or similar.
- [ ] Penalty method explanation paragraph added to the end of `2_representation.tex`.
- [ ] `1_intro.tex` has an integrated chapter guide.
- [ ] `3_simulation.tex` has bridging sentences.
- [ ] Appendix-like headings renamed logically (based on user decision).
- [ ] Promotional language toned down in paper1.

### Must Have
- Reference labels (`\label{...}`) must remain intact.

### Must NOT Have (Guardrails)
- Do NOT restructure the document.
- Do NOT modify the tone or language style of the general intro, paper2, or paper3.
- Do NOT break existing mathematical macros or formatting.

---

## Verification Strategy

- **Agent-Executed QA**: We will verify the changes by running `latexmk` and reading the modified files.

---

## Execution Strategy

### Parallel Execution Waves

Wave 1 (Start Immediately):
├── Task 1: Unify Terminology and Chapter Guide [quick]
│   - Edit `body/graduate/intro/3_contributions_and_organization.tex`
│   - Edit `body/graduate/paper1/1_intro.tex`
├── Task 2: Expand Problem Diagnosis [quick]
│   - Edit `body/graduate/paper1/2_representation.tex`
├── Task 3: Add Transitions & Tone-down Simulation [quick]
│   - Edit `body/graduate/paper1/3_simulation.tex`
│   - Edit `body/graduate/paper1/preconditioner_content.tex`
├── Task 4: Rename Headings & Tone-down Conclusion [quick]
│   - Edit `body/graduate/paper1/5_conclusion.tex`
│   - Edit `body/graduate/paper1/app_*.tex` (Pending user choice)

---

## TODOs

- [x] 1. Unify Terminology & Integrate Chapter Guide
  **What to do**:
  - In `body/graduate/intro/3_contributions_and_organization.tex`, replace "关节角广义坐标" with "轴角链式坐标" and "零约束" with "零内在几何硬约束".
  - In `body/graduate/paper1/1_intro.tex`, integrate a chapter guide into the existing text smoothly without making a new standalone paragraph. Also, tone down exaggerated terms.
  **Recommended Agent**: `quick`
  **QA Scenarios**: Read the file to ensure the edits are made and no LaTeX syntax is broken.

- [x] 2. Expand Problem Diagnosis in Representation
  **What to do**:
  - In `body/graduate/paper1/2_representation.tex`, add a paragraph at the end explaining the penalty method for inextensible constraints, how weight->infinity causes ill-conditioned stiffness matrices, restricts implicit Euler time step, and transition to the next section.
  **Recommended Agent**: `quick`
  **QA Scenarios**: Read the end of the file.

- [x] 3. Add Transitions & Tone-down Simulation
  **What to do**:
  - In `body/graduate/paper1/3_simulation.tex`, add short bridging sentences at subsection boundaries. Tone down absolute claims.
  - In `body/graduate/paper1/preconditioner_content.tex`, tone down claims like "至少可带来一个数量级的提升".
  **Recommended Agent**: `quick`
  **QA Scenarios**: Read the edits to verify bridging and softer tone.

- [x] 4. Rename Headings & Tone-down Conclusion
  **What to do**:
  - Apply the chosen heading names to `app_energy_terms.tex`, `app_active_set.tex`, `app_invertible_proof.tex`, and `app_extended_redmax.tex` while keeping existing `\label{}`s.
  - In `body/graduate/paper1/5_conclusion.tex`, tone down "彻底内建", "从源头上消除了", "逾百倍的加速表现", etc.
  **Recommended Agent**: `quick`
  **QA Scenarios**: Ensure LaTeX compiles after renaming and the tone is successfully softened.

---

## Final Verification Wave

- [x] F1. **Compile and Check** — `quick`
  Run `latexmk -xelatex -outdir=out zjuthesis` to ensure the document still compiles perfectly.
