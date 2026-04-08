# Plan: paper2-style-calibration

## TL;DR

> **Quick Summary**: Revise Chapter 3 (`paper2`) into a plainer, more rigorous doctoral-thesis register while preserving technical substance and the already-completed section structure.
>
> **Deliverables**:
> - A full-chapter style calibration pass across `body/graduate/paper2/`.
> - A simplified two-bullet contribution list in `1_intro.tex`.
> - A fully rewritten `6_summary.tex` aligned with the Introduction’s framing.
>
> **Estimated Effort**: Medium
> **Parallel Execution**: YES - 3 waves
> **Critical Path**: Style audit -> intro/contribution rewrite -> body-wide tone normalization -> summary rewrite -> compile + review

---

## Context

### Original Request
Create an improvement plan for `paper2` based on reviewer-style critique. The user wants the whole chapter revised into plain, rigorous, restrained language; related-work organization should stay as-is; the contribution list should be simplified to two balanced bullets; and the ending should be fully rewritten so it aligns with the Introduction and frames this chapter as solving the soft-hard coupling problem caused by discretization.

### Interview Summary
**Key Discussions**:
- [Tone]: The user agreed that the current prose is too dense, rhetorical, and extreme for a doctoral thesis.
- [Scope]: The user wants a whole-chapter pass, not just the opening and ending.
- [Related Work]: The user explicitly said not to reorganize or shorten the related-work architecture in this round.
- [Contributions]: The user agreed that the current contribution list is unbalanced and should be simplified to two higher-level contributions.
- [Ending]: The user explicitly asked for the whole ending to be rewritten.
- [Framing]: The user wants the ending aligned with the Introduction’s abstraction level: paper2 addresses soft-hard coupling induced by discretization.

**Research Findings**:
- `body/graduate/paper2/1_intro.tex` contains multiple instances of promotional, metaphor-heavy, or over-assertive language.
- `body/graduate/paper2/6_summary.tex` contains strong rhetorical inflation, over-claimed conclusions, and weak chapter-closing discipline.
- The Introduction frames Chapter 3 as: discretization / local geometric degeneration -> artificial high-frequency stiffness -> local operator-aware basis optimization/isolation.

### Metis Review
**Identified Gaps** (addressed):
- [Gap 1]: Need explicit edit-depth policy. -> Resolved: sentence-level to paragraph-level rewriting is allowed, but no section reordering.
- [Gap 2]: Risk of scope creep into related-work redesign. -> Resolved: related-work structure and subsection organization are frozen in this round.
- [Gap 3]: Need claim-discipline rule. -> Resolved: when in doubt, weaken statements to the strongest claim directly supported by chapter evidence.
- [Gap 4]: Need acceptance criteria beyond opening/ending. -> Resolved: full-chapter tone check includes intro, middle technical sections, results discussion, and summary.
- [Gap 5]: Need terminology policy. -> Resolved: chapter-wide terminology must consistently align with the Introduction’s framing of discretization-induced soft-hard coupling.

---

## Work Objectives

### Core Objective
Revise the prose and argumentative tone of `paper2` so that the chapter reads as a restrained, rigorous PhD thesis chapter rather than a rhetorically amplified journal-style narrative, while preserving all technical substance and the current section structure.

### Concrete Deliverables
- Revised `body/graduate/paper2/1_intro.tex`
- Revised middle chapter files in `body/graduate/paper2/` where tone inflation or overclaiming appears
- Rewritten `body/graduate/paper2/6_summary.tex`
- Updated two-bullet contribution list in `1_intro.tex`

### Definition of Done
- [ ] `paper2` contains no obviously promotional, metaphor-heavy, or over-claimed thesis prose.
- [ ] The contribution list in `1_intro.tex` contains exactly two balanced, higher-level bullets.
- [ ] `6_summary.tex` is fully rewritten in a restrained thesis style.
- [ ] The chapter consistently frames its problem as discretization-induced soft-hard coupling.
- [ ] `latexmk` succeeds after the edits.

### Must Have
- Whole-chapter tone calibration, not just endpoint cleanup
- Two-bullet contribution list
- Ending rewritten to align with Introduction-level abstraction
- Stable terminology for problem and method across the chapter

### Must NOT Have (Guardrails)
- Do not reorganize the related-work subsection structure in this round.
- Do not add new experiments, references, or technical claims.
- Do not alter the already-completed section structure alignment with `paper1`.
- Do not strengthen claims beyond chapter evidence.
- Do not turn the revision into a logic/proof redesign task.

---

## Verification Strategy

### Test Decision
- **Infrastructure exists**: NO
- **Automated tests**: None
- **Agent-Executed QA**: ALWAYS

### QA Policy
Every task must include agent-executed QA based on direct file reading, targeted grep checks for rhetorical phrases / overclaim patterns, and `latexmk` for compilation validation.
Evidence saved to `.sisyphus/evidence/` where useful.

---

## Execution Strategy

### Parallel Execution Waves

Wave 1 (Foundation audit + terminology policy):
├── Task 1: Audit full `paper2` for rhetoric, overclaiming, and terminology drift
├── Task 2: Define canonical phrasing rules for chapter-level problem/method framing
└── Task 3: Map current four contribution bullets into two balanced contribution themes

Wave 2 (Core writing revisions, parallel by file cluster):
├── Task 4: Rewrite opening and method/contribution transition in `1_intro.tex`
├── Task 5: Perform middle-section tone normalization across `paper2` body files
└── Task 6: Rewrite `6_summary.tex` to align with Introduction and thesis register

Wave 3 (Integration + verification):
├── Task 7: Cross-file consistency pass for terminology and claim strength
├── Task 8: Compile thesis with `latexmk` and inspect warnings for regression
└── Task 9: Reviewer-style final read focused on tone, restraint, and chapter closure quality

Critical Path: Task 1 -> Task 2 -> Task 4 -> Task 6 -> Task 7 -> Task 8 -> Task 9

### Dependency Matrix
- **1**: None -> 4, 5, 6
- **2**: 1 -> 4, 5, 6, 7
- **3**: 1 -> 4
- **4**: 2, 3 -> 7
- **5**: 1, 2 -> 7
- **6**: 1, 2 -> 7
- **7**: 4, 5, 6 -> 8, 9
- **8**: 7 -> 9
- **9**: 7, 8 -> Final verification

### Agent Dispatch Summary
- **Wave 1**: T1 → `deep`, T2 → `quick`, T3 → `quick`
- **Wave 2**: T4 → `writing`, T5 → `writing`, T6 → `writing`
- **Wave 3**: T7 → `quick`, T8 → `unspecified-high`, T9 → `oracle`

---

## TODOs

- [ ] 1. Audit chapter-wide rhetoric, overclaiming, and terminology drift

  **What to do**:
  - Read all files under `body/graduate/paper2/`.
  - Mark passages with promotional, metaphor-heavy, triumphalist, or over-strong language.
  - Mark places where the chapter’s problem framing drifts away from “discretization-induced soft-hard coupling”.
  - Mark places where method labels are inconsistent.

  **Must NOT do**:
  - Do not rewrite files yet.
  - Do not change related-work organization.

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Requires chapter-wide qualitative analysis and taxonomy of issues.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocks**: 4, 5, 6
  - **Blocked By**: None

  **References**:
  - `body/graduate/paper2/*.tex` - Full chapter scope to identify style drift and overclaim patterns.
  - `body/graduate/intro/1_background.tex` - Canonical thesis-level framing of the problem.
  - `body/graduate/intro/3_contributions_and_organization.tex` - Canonical thesis-level framing of Chapter 3’s role.

  **Acceptance Criteria**:
  - [ ] A complete issue map exists for all `paper2` files.
  - [ ] Problematic passages are categorized (rhetoric / overclaim / inconsistency / weak closure).

  **QA Scenarios**:
  ```
  Scenario: Confirm full paper2 coverage
    Tool: Bash (grep)
    Preconditions: paper2 files present
    Steps:
      1. grep -n "\\section\|\\subsection" body/graduate/paper2/*.tex
      2. Verify every chapter file was included in the audit notes
    Expected Result: All active paper2 files are covered in the audit
    Evidence: .sisyphus/evidence/paper2-style-audit-coverage.txt

  Scenario: Confirm issue taxonomy exists
    Tool: Read
    Preconditions: audit notes drafted by executor
    Steps:
      1. Read the produced audit notes / scratch output
      2. Verify each issue is classified by type
    Expected Result: No flagged passage remains unclassified
    Evidence: .sisyphus/evidence/paper2-style-audit-taxonomy.txt
  ```

- [ ] 2. Define canonical chapter phrasing policy

  **What to do**:
  - Establish one preferred phrasing for the chapter’s central problem.
  - Establish one preferred phrasing for the chapter’s method identity.
  - Establish claim-strength rules for results and chapter-level significance.

  **Must NOT do**:
  - Do not over-engineer a glossary.
  - Do not change thesis-wide files outside `paper2`.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Short policy-definition task grounded in the Introduction.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocks**: 4, 5, 6, 7
  - **Blocked By**: 1

  **References**:
  - `body/graduate/intro/1_background.tex` - Source of thesis-level framing language.
  - `body/graduate/intro/3_contributions_and_organization.tex` - Source of Chapter 3 role description.

  **Acceptance Criteria**:
  - [ ] Problem phrasing policy defined.
  - [ ] Method phrasing policy defined.
  - [ ] Claim-softening policy defined.

  **QA Scenarios**:
  ```
  Scenario: Check policy completeness
    Tool: Read
    Preconditions: phrasing policy drafted
    Steps:
      1. Read policy notes
      2. Verify it includes problem phrasing, method phrasing, and claim-strength rules
    Expected Result: All three policy elements exist and are concrete
    Evidence: .sisyphus/evidence/paper2-phrasing-policy.txt

  Scenario: Check intro alignment
    Tool: Read
    Preconditions: policy drafted and intro available
    Steps:
      1. Compare policy wording against intro framing passages
      2. Confirm no contradiction in abstraction level
    Expected Result: Policy wording matches Introduction-level framing
    Evidence: .sisyphus/evidence/paper2-phrasing-policy-alignment.txt
  ```

- [ ] 3. Redesign contribution list into two balanced bullets

  **What to do**:
  - Group the current four contribution bullets into two higher-level, balanced contribution statements.
  - Preserve substantive ideas while eliminating weak or mismatched granularity.
  - Ensure both bullets sit at the same abstraction level.

  **Must NOT do**:
  - Do not drop substantive method ideas without re-homing them in ordinary prose.
  - Do not leave one bullet as “method” and the other as “experiments”.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Small but conceptually precise restructuring of contribution statements.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocks**: 4
  - **Blocked By**: 1

  **References**:
  - `body/graduate/paper2/1_intro.tex` - Current four-bullet contribution list.
  - `body/graduate/intro/3_contributions_and_organization.tex` - Thesis-level framing of Chapter 3 contribution.

  **Acceptance Criteria**:
  - [ ] Exactly two contribution bullets remain.
  - [ ] The two bullets are balanced in abstraction level.
  - [ ] All important contribution content from the old list remains represented somewhere.

  **QA Scenarios**:
  ```
  Scenario: Verify bullet count
    Tool: Read
    Preconditions: contribution list rewritten
    Steps:
      1. Read the contribution subsection in 1_intro.tex
      2. Count \item entries
    Expected Result: Exactly 2 \item bullets
    Evidence: .sisyphus/evidence/paper2-contribution-count.txt

  Scenario: Verify semantic coverage
    Tool: Read
    Preconditions: old and new contribution lists available
    Steps:
      1. Compare old 4-bullet content against new 2-bullet statements
      2. Confirm each old idea is preserved or relocated into nearby prose
    Expected Result: No substantive contribution idea is silently lost
    Evidence: .sisyphus/evidence/paper2-contribution-coverage.txt
  ```

- [ ] 4. Rewrite opening and method/contribution transition in `1_intro.tex`

  **What to do**:
  - Rewrite the opening bridge from Chapter 2 to Chapter 3 in plainer, more restrained doctoral-thesis language.
  - Rewrite the problem framing paragraph(s) to remove metaphor-heavy or promotional wording.
  - Rewrite the transition into `\subsection{本章方法与贡献}` so it introduces the method without early self-promotion.
  - Apply the two-bullet contribution redesign.

  **Must NOT do**:
  - Do not reorganize the related-work structure.
  - Do not add new technical claims.

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Requires nuanced thesis-level prose calibration and structural restraint.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: 7
  - **Blocked By**: 2, 3

  **References**:
  - `body/graduate/paper2/1_intro.tex` - Primary rewrite target.
  - `body/graduate/intro/1_background.tex` - Tone and framing benchmark.
  - `body/graduate/intro/3_contributions_and_organization.tex` - Role of Chapter 3 within the thesis.

  **Acceptance Criteria**:
  - [ ] Opening no longer contains obvious promotional or metaphor-heavy language.
  - [ ] Transition into method/contribution is neutral and technically framed.
  - [ ] Contribution list reduced to two balanced bullets.

  **QA Scenarios**:
  ```
  Scenario: Check opening for inflated rhetoric
    Tool: Bash (grep)
    Preconditions: 1_intro.tex rewritten
    Steps:
      1. grep -n "病毒般\|霸道地\|沙上建塔\|开创性\|致命\|极佳" body/graduate/paper2/1_intro.tex
    Expected Result: No matches for the targeted inflated phrases
    Evidence: .sisyphus/evidence/paper2-opening-rhetoric-check.txt

  Scenario: Check contribution structure
    Tool: Read
    Preconditions: 1_intro.tex rewritten
    Steps:
      1. Read the method and contribution subsection
      2. Verify method introduction is descriptive rather than promotional
      3. Verify exactly two balanced bullets remain
    Expected Result: Neutral transition and two-bullet structure confirmed
    Evidence: .sisyphus/evidence/paper2-opening-contribution-review.txt
  ```

- [ ] 5. Normalize prose tone across middle `paper2` body files

  **What to do**:
  - Review the remaining `paper2` files after the intro.
  - Replace exaggerated, literary, triumphalist, or over-strong phrases with plain and precise thesis prose.
  - Tighten sentences whose density comes from stacked modifiers or dramatic contrasts.
  - Leave the related-work architecture intact while still softening evaluative overstatements inside it.

  **Must NOT do**:
  - Do not alter derivations, notation, or section structure.
  - Do not expand this into a technical correctness rewrite unless a sentence’s meaning becomes unsound.

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Multi-file thesis prose normalization task.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: 7
  - **Blocked By**: 1, 2

  **References**:
  - `body/graduate/paper2/*.tex` - Whole chapter body, excluding endpoint-specific priorities already covered by Tasks 4 and 6.
  - `body/graduate/intro/*.tex` - Tone benchmark for abstract level and restraint.

  **Acceptance Criteria**:
  - [ ] No obvious promotional language remains in middle chapter files.
  - [ ] Technical substance and notation remain unchanged.
  - [ ] Sentence-level readability improves without stylistic beautification drift.

  **QA Scenarios**:
  ```
  Scenario: Scan for high-risk rhetorical markers
    Tool: Bash (grep)
    Preconditions: middle files revised
    Steps:
      1. grep -R -n "开创性\|彻底\|极其深刻\|无情\|精准点杀\|独具匠心\|至高命题\|完美" body/graduate/paper2
    Expected Result: No unjustified rhetorical markers remain in paper2 body files
    Evidence: .sisyphus/evidence/paper2-body-rhetoric-scan.txt

  Scenario: Spot-check technical preservation
    Tool: Read
    Preconditions: body files revised
    Steps:
      1. Read one middle technical section and one results section
      2. Verify equations, notation, and method descriptions are preserved
    Expected Result: Tone changed, technical substance preserved
    Evidence: .sisyphus/evidence/paper2-body-preservation-check.txt
  ```

- [ ] 6. Rewrite `6_summary.tex` as a restrained thesis-style chapter closing

  **What to do**:
  - Fully rewrite `body/graduate/paper2/6_summary.tex`.
  - Make the summary answer: what problem was addressed, what mechanism was proposed, what evidence supports it, what role this chapter plays in the thesis, and how it leads to Chapter 4.
  - Align the abstraction level with the Introduction.
  - Explicitly frame the chapter as addressing discretization-induced soft-hard coupling.
  - Remove new interpretive layers not needed for chapter closure.

  **Must NOT do**:
  - Do not retain rhetorical flourish for style.
  - Do not make claims stronger than the chapter’s evidence supports.
  - Do not turn the summary into a second mini-introduction.

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Full summary rewrite with thesis-level framing discipline.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: 7
  - **Blocked By**: 1, 2

  **References**:
  - `body/graduate/paper2/6_summary.tex` - Rewrite target.
  - `body/graduate/intro/1_background.tex` - Problem abstraction benchmark.
  - `body/graduate/intro/3_contributions_and_organization.tex` - Chapter role and transition benchmark.

  **Acceptance Criteria**:
  - [ ] Summary is fully rewritten.
  - [ ] No extreme rhetoric remains.
  - [ ] Conclusion strength is proportionate to chapter evidence.
  - [ ] The final paragraph clearly and soberly transitions to Chapter 4.

  **QA Scenarios**:
  ```
  Scenario: Check summary for banned rhetoric
    Tool: Bash (grep)
    Preconditions: 6_summary.tex rewritten
    Steps:
      1. grep -n "精准点杀\|独具匠心\|无情剥离\|深水区\|至高命题\|完美" body/graduate/paper2/6_summary.tex
    Expected Result: No matches
    Evidence: .sisyphus/evidence/paper2-summary-rhetoric-check.txt

  Scenario: Check summary closure function
    Tool: Read
    Preconditions: 6_summary.tex rewritten
    Steps:
      1. Read the summary end-to-end
      2. Verify it includes problem, mechanism, evidence-bounded conclusion, thesis role, and Chapter 4 bridge
    Expected Result: Summary closes the chapter instead of reopening it
    Evidence: .sisyphus/evidence/paper2-summary-closure-review.txt
  ```

- [ ] 7. Run cross-file consistency pass on terminology and claim strength

  **What to do**:
  - Read revised chapter files together.
  - Normalize remaining terminology drift.
  - Ensure no sentence in intro, middle body, results, or summary exceeds the agreed claim-strength policy.
  - Ensure the chapter consistently uses the Introduction-aligned framing.

  **Must NOT do**:
  - Do not introduce new content in the name of consistency.
  - Do not reopen related-work structural questions.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Integration pass focused on consistency, not major rewriting.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Sequential after Wave 2
  - **Blocks**: 8, 9
  - **Blocked By**: 4, 5, 6

  **References**:
  - Revised `body/graduate/paper2/*.tex`
  - `body/graduate/intro/1_background.tex`
  - `body/graduate/intro/3_contributions_and_organization.tex`

  **Acceptance Criteria**:
  - [ ] Terminology is stable across the chapter.
  - [ ] The chapter’s framing matches the Introduction.
  - [ ] No obvious overclaim remains.

  **QA Scenarios**:
  ```
  Scenario: Check chapter framing consistency
    Tool: Read
    Preconditions: full chapter revised
    Steps:
      1. Read intro framing passages and revised paper2 opening/ending
      2. Confirm same abstraction level and problem framing
    Expected Result: Chapter 3 is consistently framed as discretization-induced soft-hard coupling
    Evidence: .sisyphus/evidence/paper2-framing-consistency.txt

  Scenario: Check claim-strength discipline
    Tool: Bash (grep)
    Preconditions: full chapter revised
    Steps:
      1. grep -R -n "彻底\|完全\|根本上\|完美\|决定性地\|毫无遗漏" body/graduate/paper2
      2. Review any remaining matches manually
    Expected Result: No unjustified high-strength claim language remains
    Evidence: .sisyphus/evidence/paper2-claim-strength-scan.txt
  ```

- [ ] 8. Compile thesis and inspect for regression

  **What to do**:
  - Run `latexmk -c` and `latexmk`.
  - Confirm no fatal compilation errors were introduced.
  - Check whether any citation or reference issue appears newly due to text rewrites.

  **Must NOT do**:
  - Do not treat pre-existing unrelated warnings as blockers unless the rewrite caused them.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: Compilation verification and warning discrimination.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Sequential after Task 7
  - **Blocks**: 9
  - **Blocked By**: 7

  **References**:
  - `zjuthesis.tex`
  - `body/graduate/paper2/*.tex`

  **Acceptance Criteria**:
  - [ ] `latexmk` succeeds.
  - [ ] No new fatal errors are introduced by the rewrite.

  **QA Scenarios**:
  ```
  Scenario: Compile thesis
    Tool: Bash (latexmk)
    Preconditions: revised paper2 files saved
    Steps:
      1. latexmk -c
      2. latexmk
    Expected Result: Compilation succeeds without fatal errors
    Evidence: .sisyphus/evidence/paper2-style-build.txt

  Scenario: Check regression scope
    Tool: Read/Grep on build log
    Preconditions: build completed
    Steps:
      1. Inspect build log for new paper2-specific failures or malformed references
      2. Distinguish them from pre-existing thesis-wide warnings
    Expected Result: No paper2 rewrite regression detected
    Evidence: .sisyphus/evidence/paper2-style-build-review.txt
  ```

- [ ] 9. Perform strict reviewer-style final read

  **What to do**:
  - Read the revised opening, one middle technical section, one results passage, and the rewritten summary.
  - Judge the chapter as a strict PhD reviewer would.
  - Verify the chapter now reads as sober, precise, and proportionate in claims.

  **Must NOT do**:
  - Do not auto-approve without explicit evidence.
  - Do not reduce review to “sounds smoother”.

  **Recommended Agent Profile**:
  - **Category**: `oracle`
    - Reason: Requires high-level judgment on thesis quality and proportionality.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Final sequential task
  - **Blocks**: Final verification
  - **Blocked By**: 7, 8

  **References**:
  - Revised `body/graduate/paper2/1_intro.tex`
  - Revised middle `paper2` files
  - Revised `body/graduate/paper2/6_summary.tex`
  - `body/graduate/intro/*.tex`

  **Acceptance Criteria**:
  - [ ] Reviewer-style read passes without major tone or claim-boundary objections.
  - [ ] Opening and ending are consistent with doctoral-thesis norms.
  - [ ] The chapter’s role in the thesis is clear and restrained.

  **QA Scenarios**:
  ```
  Scenario: Reviewer-style endpoint check
    Tool: Read
    Preconditions: revised intro and summary available
    Steps:
      1. Read the beginning and ending consecutively
      2. Judge whether tone, abstraction level, and claim strength are thesis-appropriate
    Expected Result: No major reviewer-style objection remains
    Evidence: .sisyphus/evidence/paper2-reviewer-endpoint-check.txt

  Scenario: Whole-chapter spot review
    Tool: Read
    Preconditions: all revisions complete and compiled
    Steps:
      1. Read one middle technical section and one results passage
      2. Confirm tone normalization was applied beyond endpoints
    Expected Result: Whole chapter, not just endpoints, meets the same standard
    Evidence: .sisyphus/evidence/paper2-reviewer-spotcheck.txt
  ```

---

## Final Verification Wave

- [x] F1. **Plan Compliance Audit** — `oracle`
  Verify that the executed revisions match this plan exactly: related-work structure untouched, contribution list reduced to two bullets, summary rewritten, and chapter-wide tone calibrated.
  Output: `VERDICT: APPROVE/REJECT`

- [x] F2. **Code/Build Quality Review** — `unspecified-high`
  Run `latexmk`. Confirm no paper2-specific regression was introduced and no malformed LaTeX was created by the rewriting pass.
  Output: `Build [PASS/FAIL] | VERDICT`

- [x] F3. **Real Manual QA** — `unspecified-high`
  Read revised opening, middle section, results section, and summary. Confirm the prose is plain, rigorous, and restrained throughout.
  Output: `Tone [PASS/FAIL] | VERDICT`

- [x] F4. **Scope Fidelity Check** — `deep`
  Compare plan vs actual edits. Confirm the revision stayed within style/calibration scope and did not become a structural or technical redesign.
  Output: `Scope [CLEAN/N issues] | VERDICT`

---

## Commit Strategy

- **1**: `refactor(paper2): calibrate chapter prose and closing section` - all revised `paper2` files, `latexmk`

---

## Success Criteria

### Verification Commands
```bash
latexmk -c && latexmk
# Expected: succeeds without fatal errors

grep -R -n "精准点杀\|独具匠心\|无情剥离\|至高命题\|开创性\|霸道地\|病毒般" body/graduate/paper2
# Expected: no matches in revised chapter prose
```

### Final Checklist
- [ ] Whole chapter prose revised into restrained thesis style
- [ ] Related-work organization unchanged
- [ ] Two balanced contribution bullets in `1_intro.tex`
- [ ] `6_summary.tex` fully rewritten
- [ ] Chapter framed consistently as discretization-induced soft-hard coupling
- [ ] Compilation passes
