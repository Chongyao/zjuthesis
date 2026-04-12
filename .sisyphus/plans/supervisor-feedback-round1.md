# Plan: supervisor-feedback-round1

## TL;DR

> **Quick Summary**: Execute this supervisor-feedback round as a tightly scoped thesis-revision pass that prioritizes structure-before-wording, stabilizes thesis-level terminology, fixes paragraph ordering in the Introduction and chapter endings, and then performs targeted formatting cleanup.
>
> **Deliverables**:
> - Revised `body/graduate/intro/1_background.tex` for items 1, 2, 3, 4, 5, 6, and 7.
> - Revised `body/graduate/intro/3_contributions_and_organization.tex` for items 9 and 10.
> - Revised `body/graduate/paper1/5_conclusion.tex` for item 11.
> - Revised `body/graduate/paper3/1_intro.tex` plus targeted paper3 formatting/algorithm/equation cleanup for items 13, 14, and 15.
> - Explicit branch-scope exclusion for item 12 (`paper2/5_results.tex`) because the user already fixed it on another branch.
>
> **Estimated Effort**: Large
> **Parallel Execution**: YES - 5 waves
> **Critical Path**: Scope/policy lock -> intro background structural revision -> intro organization revision -> paper1 conclusion reorder -> paper3 cleanup -> compile + final consistency review

---

## Context

### Original Request
Write this round of supervisor feedback as a detailed executable work plan.

### Interview Summary
**Key Discussions**:
- The supervisor feedback was converted into a structured tracker at `.sisyphus/notepads/supervisor_feedback_round1.md`.
- The user clarified the real nature of several comments:
  - Item 4 is primarily about Chinese sentence flow around “如图1.1所示”, not just concept density.
  - Item 5 should standardize on “频谱过宽”.
  - Item 6 should move the paragraph about harms/impacts before the paragraph that classifies the sources of pathology.
  - Item 7 is about method scope / applicability and should immediately follow the three bullets as a summary.
  - Item 9 keeps the bullet list but must move the longer summary paragraph upward and restore the missing Chapter 3 / paper2 preview.
  - Item 10 is mainly a terminology error: “非线性兼容性” is wrong.
  - Item 11 should swap the final two paragraphs in `paper1/5_conclusion.tex`, not compress them.
  - Item 12 is skipped in this branch because it is already fixed elsewhere.
- The user explicitly asked to persist the “structure before wording” lesson into `AGENTS.md` and `CLAUDE.md`, and that is already done.

**Research Findings**:
- The supervisor-comment tracker with source mapping exists at `.sisyphus/notepads/supervisor_feedback_round1.md`.
- The highest-confidence file mappings are:
  - `body/graduate/intro/1_background.tex` for items 1–7
  - `body/graduate/intro/3_contributions_and_organization.tex` for items 9–10
  - `body/graduate/paper1/5_conclusion.tex` for item 11
  - `body/graduate/paper3/1_intro.tex` for item 13
  - `body/graduate/paper3/2_foundation.tex`, `3_simulation.tex`, `4_results.tex`, `5_1_alg_adaptive_shifting.tex` for items 14–15
- Existing plans show the preferred level of detail and wave structure:
  - `.sisyphus/plans/paper2-style-calibration.md`
  - `.sisyphus/plans/intro_refinement.md`
- `AGENTS.md` and `CLAUDE.md` now encode the rule that many thesis problems are ordering problems, not wording problems.

### Metis Review
**Identified Gaps** (addressed):
- Need explicit branch exclusion for item 12. -> Resolved: item 12 is listed as out-of-scope for this branch and excluded from all implementation tasks.
- Need terminology policy before cross-file cleanup. -> Resolved: Wave 1 includes a terminology/policy lock task.
- Need structural tasks separated from sentence-polish tasks. -> Resolved: intro and chapter tasks are grouped by structural concern first, with wording cleanup subordinated to that structural fix.
- Need non-compile acceptance criteria. -> Resolved: each task includes ordering, terminology, or pattern-based QA in addition to compile validation.
- Need scope-creep guardrails. -> Resolved: the plan forbids opportunistic whole-thesis polishing beyond supervisor-linked issues and directly required consistency propagation.
- Need page-number caution. -> Resolved: page markers are treated as navigational hints only, not immutable anchors.

---

## Work Objectives

### Core Objective
Convert this supervisor-feedback round into a controlled, reviewable thesis-revision pass that fixes the flagged structural, rhetorical, terminology, and formatting issues without reopening unrelated thesis content.

### Concrete Deliverables
- Updated `body/graduate/intro/1_background.tex`
- Updated `body/graduate/intro/3_contributions_and_organization.tex`
- Updated `body/graduate/paper1/5_conclusion.tex`
- Updated `body/graduate/paper3/1_intro.tex`
- If required by flagged issues, updated targeted paper3 technical files:
  - `body/graduate/paper3/2_foundation.tex`
  - `body/graduate/paper3/3_simulation.tex`
  - `body/graduate/paper3/4_results.tex`
  - `body/graduate/paper3/5_1_alg_adaptive_shifting.tex`
- No changes to `body/graduate/paper2/5_results.tex` for item 12 in this branch

### Definition of Done
- [ ] Item 12 is explicitly skipped in this branch and untouched by implementation tasks.
- [ ] Items 1–7 are resolved in `intro/1_background.tex` with corrected structure and terminology.
- [ ] Items 9–10 are resolved in `intro/3_contributions_and_organization.tex` with restored chapter-preview symmetry.
- [ ] Item 11 is resolved in `paper1/5_conclusion.tex` by swapping the final two paragraphs rather than compressing content.
- [ ] Item 13 restores/stabilizes thesis-level keywords in `paper3/1_intro.tex`.
- [ ] Items 14–15 are resolved in the identified paper3 formatting/equation/pseudocode hotspots.
- [ ] `latexmk` succeeds after all edits.
- [ ] Final review confirms no banned terminology/order regressions in touched files.

### Must Have
- Structure-before-wording execution order
- Explicit terminology policy for this round
- Explicit skipped-scope note for item 12
- Separation between structural revisions and formatting cleanup
- Final compile plus log review
- Final cross-file consistency check for thesis-level keywords

### Must NOT Have (Guardrails)
- Do not reopen item 12 in this branch.
- Do not convert this round into a whole-thesis opportunistic rewrite.
- Do not change unrelated math content, derivations, experiments, or references.
- Do not use page numbers as the sole anchor after edits shift layout.
- Do not globally replace technically precise local wording unless it conflicts with the approved policy for this round.
- Do not mix structural chapter revisions with template/class-level formatting changes.
- Do not treat compile success alone as proof that the supervisor comments are resolved.

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — verification must be agent-executed through file inspection, grep/pattern checks, and `latexmk` compilation.

### Test Decision
- **Infrastructure exists**: NO traditional automated test suite for prose
- **Automated tests**: None
- **Framework**: none
- **Agent-Executed QA**: ALWAYS

### QA Policy
Every task must include direct, agent-executable verification based on one or more of:
- file reading to confirm paragraph order or local wording
- grep/pattern checks for required and banned terms
- compile validation with `latexmk`
- log review for undefined references/citations and critical warnings in touched areas

Evidence should be captured to `.sisyphus/evidence/` where useful.

---

## Execution Strategy

### Parallel Execution Waves

> Structural and terminology policy work happens first. Formatting cleanup happens after structural text settles.

Wave 1 (Policy lock + baseline mapping):
├── Task 1: Lock branch scope, skipped items, and approved terminology policy [quick]
├── Task 2: Baseline audit for intro background items 1–7 [deep]
├── Task 3: Baseline audit for intro organization items 9–10 [quick]
├── Task 4: Baseline audit for paper1 conclusion item 11 [quick]
└── Task 5: Baseline audit for paper3 keyword / formatting / pseudocode items 13–15 [deep]

Wave 2 (Core intro background revision):
├── Task 6: Rewrite intro opening rhetoric and central-method framing in `1_background.tex` [writing]
├── Task 7: Fix sentence flow, figure cue placement, and “频谱过宽” terminology in `1_background.tex` [writing]
└── Task 8: Reorder pathology harm/source paragraphs and move applicability summary after bullets in `1_background.tex` [writing]

Wave 3 (Intro organization + paper1 closure):
├── Task 9: Repair bullet-following summary flow and restore missing Chapter 3 preview in `3_contributions_and_organization.tex` [writing]
├── Task 10: Fix terminology error and chapter-ending wording in `3_contributions_and_organization.tex` [quick]
└── Task 11: Swap final two paragraphs in `paper1/5_conclusion.tex` while preserving content [quick]

Wave 4 (Paper3 coherence + technical cleanup):
├── Task 12: Stabilize thesis-level keywords in `paper3/1_intro.tex` [writing]
├── Task 13: Clean equation-punctuation / whitespace issues in paper3 technical sections [unspecified-high]
└── Task 14: Fix pseudocode layout issues in paper3 algorithm files [unspecified-high]

Wave 5 (Integration + verification):
├── Task 15: Cross-file consistency sweep for approved terminology and ordering outcomes [quick]
├── Task 16: Compile thesis with `latexmk` and inspect warnings/log fallout [unspecified-high]
└── Task 17: Reviewer-style final read against supervisor tracker [oracle]

Wave FINAL (After ALL tasks — 4 parallel reviews):
├── Task F1: Plan compliance audit (oracle)
├── Task F2: Code/content quality review (unspecified-high)
├── Task F3: Real QA execution of all planned checks (unspecified-high)
└── Task F4: Scope fidelity check (deep)

Critical Path: Task 1 -> Task 2 -> Task 6 -> Task 8 -> Task 9 -> Task 12 -> Task 15 -> Task 16 -> Task 17 -> F1-F4
Parallel Speedup: ~60–70% faster than purely sequential revision
Max Concurrent: 5

### Dependency Matrix
- **1**: None -> 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
- **2**: None -> 6, 7, 8
- **3**: None -> 9, 10
- **4**: None -> 11
- **5**: None -> 12, 13, 14
- **6**: 1, 2 -> 15
- **7**: 1, 2 -> 15
- **8**: 1, 2 -> 15
- **9**: 1, 3 -> 15
- **10**: 1, 3 -> 15
- **11**: 1, 4 -> 15
- **12**: 1, 5 -> 15
- **13**: 1, 5 -> 15, 16
- **14**: 1, 5 -> 15, 16
- **15**: 6, 7, 8, 9, 10, 11, 12, 13, 14 -> 16, 17
- **16**: 13, 14, 15 -> 17
- **17**: 15, 16 -> F1-F4

### Agent Dispatch Summary
- **Wave 1**: T1 → `quick`, T2 → `deep`, T3 → `quick`, T4 → `quick`, T5 → `deep`
- **Wave 2**: T6–T8 → `writing`
- **Wave 3**: T9 → `writing`, T10 → `quick`, T11 → `quick`
- **Wave 4**: T12 → `writing`, T13–T14 → `unspecified-high`
- **Wave 5**: T15 → `quick`, T16 → `unspecified-high`, T17 → `oracle`
- **FINAL**: F1 → `oracle`, F2 → `unspecified-high`, F3 → `unspecified-high`, F4 → `deep`

---

## TODOs

- [x] 1. Lock branch scope, skipped items, and approved terminology policy
- [x] 2. Baseline audit for intro background items 1–7
- [x] 3. Baseline audit for intro organization items 9–10
- [x] 4. Baseline audit for paper1 conclusion item 11
- [x] 5. Baseline audit for paper3 keyword / formatting / pseudocode items 13–15
- [x] 6. Rewrite intro opening rhetoric and central-method framing in `1_background.tex`
- [x] 7. Fix sentence flow, figure cue placement, and “频谱过宽” terminology in `1_background.tex`
- [x] 8. Reorder pathology harm/source paragraphs and move applicability summary after bullets in `1_background.tex`
- [x] 9. Repair bullet-following summary flow and restore missing Chapter 3 preview in `3_contributions_and_organization.tex`
- [x] 10. Fix terminology error and chapter-ending wording in `3_contributions_and_organization.tex`
- [x] 11. Swap final two paragraphs in `paper1/5_conclusion.tex` while preserving content
- [x] 12. Stabilize thesis-level keywords in `paper3/1_intro.tex`
- [x] 13. Clean equation-punctuation / whitespace issues in paper3 technical sections
- [x] 14. Fix pseudocode layout issues in paper3 algorithm files
- [x] 15. Cross-file consistency sweep for approved terminology and ordering outcomes
- [x] 16. Compile thesis with `latexmk` and inspect warnings/log fallout
- [x] 17. Reviewer-style final read against supervisor tracker

> Implementation + verification = one task. Every task must remain tightly scoped to the supervisor-comment round.

---

## Final Verification Wave

> 4 review agents run in parallel after all implementation tasks complete. All must approve before the work is considered complete.

- [x] F1. **Plan Compliance Audit** — `oracle`
  - Read `.sisyphus/notepads/supervisor_feedback_round1.md` and compare each in-scope item against the changed files.
  - Verify item 12 remains explicitly excluded in this branch.
  - Confirm each planned file was touched only for the supervisor-linked issue set.
  - Output: `In-scope items [N/N] | Excluded items respected [Y/N] | VERDICT`

- [x] F2. **Code/Content Quality Review** — `unspecified-high`
  - Run `latexmk`.
  - Inspect touched files for accidental terminology drift, unsupported strengthening, empty placeholders, or broken references.
  - Output: `Build [PASS/FAIL] | References [PASS/FAIL] | Drift [PASS/FAIL] | VERDICT`

- [x] F3. **Real QA Execution** — `unspecified-high`
  - Execute all grep/read/compile checks defined in the tasks.
  - Capture evidence under `.sisyphus/evidence/final-qa/`.
  - Output: `Checks [N/N pass] | Evidence [present/missing] | VERDICT`

- [x] F4. **Scope Fidelity Check** — `deep`
  - Compare actual diff against the plan.
  - Flag any opportunistic cleanup outside the approved scope.
  - Output: `Scope [clean/issues] | Exclusion item 12 [respected/violated] | VERDICT`
  - Compare actual diff against the plan.
  - Flag any opportunistic cleanup outside the approved scope.
  - Output: `Scope [clean/issues] | Exclusion item 12 [respected/violated] | VERDICT`
  - Compare actual diff against the plan.
  - Flag any opportunistic cleanup outside the approved scope.
  - Output: `Scope [clean/issues] | Exclusion item 12 [respected/violated] | VERDICT`

---

## Commit Strategy

- **Commit 1**: `docs(intro): revise background framing and ordering per supervisor feedback`
  - Files: `body/graduate/intro/1_background.tex`
  - Pre-commit: targeted grep checks for required/banned terms in `1_background.tex`

- **Commit 2**: `docs(intro): restore chapter preview symmetry and summary flow`
  - Files: `body/graduate/intro/3_contributions_and_organization.tex`
  - Pre-commit: read/grep checks for bullet-following summary and chapter-preview coverage

- **Commit 3**: `docs(paper1): reorder chapter closing paragraphs`
  - Files: `body/graduate/paper1/5_conclusion.tex`
  - Pre-commit: read check confirming final two paragraphs are swapped and content preserved

- **Commit 4**: `docs(paper3): align keywords and fix technical presentation`
  - Files: `body/graduate/paper3/1_intro.tex`, `2_foundation.tex`, `3_simulation.tex`, `4_results.tex`, `5_1_alg_adaptive_shifting.tex`
  - Pre-commit: grep/read checks for approved terminology, equation punctuation consistency, and algorithm formatting

- **Commit 5**: `docs(thesis): finalize supervisor-feedback round verification fixes`
  - Files: only fallout fixes required by compile or consistency review
  - Pre-commit: `latexmk`

Commit guardrails:
- Keep one conceptual revision unit per commit.
- Do not mix structure changes with unrelated formatting/template changes.
- Make the commit message explain the supervisor-feedback purpose.
- Do not hide new scope inside the verification commit.

---

## Success Criteria

### Verification Commands
```bash
latexmk
# Expected: successful build with no new fatal errors
```

```bash
grep -R "频谱分离" body/graduate/intro body/graduate/paper1 body/graduate/paper3 body/graduate/conclusion.tex
# Expected: no remaining uses in places covered by the approved terminology policy for this round
```

```bash
grep -R "非线性兼容性" body/graduate/intro/3_contributions_and_organization.tex body/graduate/paper3
# Expected: no matches in touched scope
```

### Final Checklist
- [x] All in-scope supervisor items are addressed.
- [x] Item 12 is explicitly skipped and untouched in this branch.
- [x] Intro background now follows reader-order logic.
- [x] Bullet lists are followed by the right summary paragraph where required.
- [x] Paper1 conclusion ends with the stronger closing paragraph after swapping order.
- [x] Paper3 terminology and presentation issues are cleaned within approved scope.
- [x] `latexmk` passes.
