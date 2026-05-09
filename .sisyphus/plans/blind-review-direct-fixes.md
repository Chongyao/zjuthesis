# Plan: blind-review-direct-fixes

## TL;DR

> **Quick Summary**: Execute a bounded blind-review cleanup pass that fixes only low-risk, directly actionable thesis issues: third-person narrative normalization, heading punctuation/numbering cleanup, empty short-caption repair, bounded float/whitespace cleanup, bibliography normalization, and repo-local figure/table formatting fixes.
>
> **Deliverables**:
> - Updated active thesis prose files under `body/graduate/` for first-person cleanup and heading/title normalization.
> - Updated intro figure/caption files for empty short-caption repair and local figure-reference flow cleanup.
> - Updated `body/ref.bib` for flagged bibliography-format issues plus directly adjacent malformed entries discovered during the bounded pass.
> - Updated active chapter files for bounded float/whitespace cleanup and any repo-local LaTeX-controlled figure formatting issues.
> - Evidence note documenting any reviewer-flagged figure-format issues that are external-source-only and therefore excluded from this direct-fix pass.
>
> **Estimated Effort**: Medium-Large
> **Parallel Execution**: YES - 4 waves
> **Critical Path**: preflight scope lock -> active-file audits -> direct text/caption/bib fixes -> float/layout cleanup -> blind-review compile -> final verification

---

## Context

### Original Request
Create and complete the work plan for the subset of blind-review comments that are comparatively easy to fix and do not require follow-up confirmation.

### Interview Summary
**Key Discussions**:
- The raw five-reviewer comments were recorded in `blind-review-comments.md`.
- A dedicated section in that file already isolates “可直接修复的问题（无需二次确认）”.
- The plan must cover only low-risk, norms-based fixes and must explicitly avoid theory expansion, new experiments, structural scientific reframing, and contribution rewriting.
- The user then asked to start building the execution plan for this direct-fix subset.

**Research Findings**:
- Active thesis content is wired through `body/graduate/content.tex` into `intro/main`, `paper1/main`, `paper2/main`, `paper3/main`, and `conclusion.tex`.
- The build target is already blind review mode (`BlindReview = true`) in `zjuthesis.tex`.
- Empty short-caption brackets were confirmed in `body/graduate/intro/1_background.tex` and `body/graduate/intro/3_contributions_and_organization.tex`.
- Heading-title colon hotspots were confirmed in active files `body/graduate/intro/2_related_and_problems.tex` and `body/graduate/paper2/main.tex`.
- Caption sizing is controlled globally by `config/format/general/caption.tex`, but this plan treats class/config edits as out of scope unless a preflight task proves they are the only safe path.
- Heading numbering/presentation is controlled by `config/format/general/heading.tex`, but source-title normalization should be attempted before any config-level edit.
- Reviewer-flagged figure-format issues may split into two classes: repo-local LaTeX/TikZ controlled content versus external raster/PDF assets that require regeneration from source scripts.

### Metis Review
**Identified Gaps** (addressed):
- Need explicit exclusion of backup trees and standalone preview files. -> Resolved in guardrails and preflight tasks.
- Need bounded bibliography scope instead of a full-database rewrite. -> Resolved: only flagged and directly adjacent malformed entries are in scope.
- Need non-compile verification. -> Resolved: grep/pattern checks, diff-scope checks, and PDF spot verification are part of the plan.
- Need triage for reviewer-flagged image typography issues that cannot be fixed inside LaTeX. -> Resolved: a dedicated classification task and evidence note are included.
- Need to avoid silent scope creep into template/config work. -> Resolved: config/class edits are forbidden unless preflight proves there is no file-local fix.

---

## Work Objectives

### Core Objective
Execute a controlled blind-review cleanup pass that resolves directly actionable formatting, prose-normalization, bibliography, and layout issues in the active thesis source without reopening scientific-content decisions.

### Concrete Deliverables
- Updated active prose files for third-person narration cleanup.
- Updated active heading/title files for punctuation/numbering normalization.
- Updated intro figure caption definitions for short-caption correctness.
- Updated active chapter files for bounded figure/table placement and whitespace cleanup.
- Updated `body/ref.bib` for directly fixable reviewer-flagged bibliography issues.
- Added `.sisyphus/evidence/blind-review-direct-fixes-exclusions.md` documenting excluded external-source-only figure issues, if any remain after triage.

### Definition of Done
- [ ] No in-scope active thesis prose file retains unresolved authorial “我们” usages.
- [ ] No in-scope active heading targeted by this plan retains reviewer-flagged colon/numbering style.
- [ ] No in-scope intro figure targeted by this plan retains empty `\caption[]{...}` syntax.
- [ ] `body/ref.bib` fixes all reviewer-flagged directly fixable metadata issues in the bounded pass.
- [ ] `latexmk` succeeds in blind-review mode with no undefined references/citations.
- [ ] Final scope review shows no edits to backup trees, standalone preview files, or unrelated theory/experiment content.

### Must Have
- Blind-review compile target preserved.
- Backup directories excluded from edits.
- Standalone preview files excluded unless explicitly proven to be part of the build.
- Bounded bibliography cleanup only.
- Evidence note for excluded external-source-only figure issues.
- Final grep/read verification in addition to compile success.

### Must NOT Have (Guardrails)
- Do not edit `body/graduate/paper1_backup/`, `body/graduate/paper2_backup/`, or other backup-only paths.
- Do not edit standalone preview files like `body/graduate/paper1/4_results_tikz_preview.tex` unless preflight proves they are build inputs.
- Do not modify `zjuthesis.cls`, `config/`, or thesis-wide format config unless a preflight task proves a file-local fix is impossible and the change remains strictly necessary for an in-scope direct-fix item.
- Do not add new scientific claims, experiments, comparisons, or theoretical arguments.
- Do not mechanically replace first-person wording in a way that produces ungrammatical Chinese.
- Do not perform a full 2360-line bibliography rewrite.
- Do not touch commented-out chapter inputs unless the plan explicitly proves they are active in the build.

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — verification must be executable by agents through source inspection, grep checks, `latexmk`, and PDF spot inspection.

### Test Decision
- **Infrastructure exists**: NO traditional automated unit test suite
- **Automated tests**: None
- **Framework**: none
- **Agent-Executed QA**: ALWAYS

### QA Policy
Every task must use one or more of the following:
- file inspection via `read`/`grep` for exact source verification
- bounded compile checks via `latexmk`
- log inspection for undefined references/citations and float fallout
- PDF spot inspection for visible layout/figure-caption outcomes where source-only checks are insufficient
- diff-scope inspection to ensure edits stay inside approved files

Evidence should be saved under `.sisyphus/evidence/` where useful.

---

## Execution Strategy

### Parallel Execution Waves

> Start with scope/fixability classification, then execute direct fixes in parallel by concern, then compile/integrate, then run final review agents.

Wave 1 (Preflight lock + bounded audits):
├── Task 1: Lock active build surface and exclusions [quick]
├── Task 2: Audit authorial first-person usages in active thesis prose [quick]
├── Task 3: Audit heading/caption/reference-placement hotspots in active files [quick]
├── Task 4: Audit bounded bibliography repair scope in `body/ref.bib` [quick]
└── Task 5: Classify reviewer-flagged figure-format issues into LaTeX-fixable vs external-source-only [quick]

Wave 2 (Direct source fixes — maximum parallelism):
├── Task 6: Normalize third-person narrative in active prose files [writing]
├── Task 7: Normalize heading punctuation/numbering in active chapter/title files [quick]
├── Task 8: Repair intro short captions and nearby figure-reference flow [quick]
├── Task 9: Fix directly editable symbol/font consistency hotspots in active thesis source [quick]
└── Task 10: Apply bounded bibliography normalization in `body/ref.bib` [unspecified-high]

Wave 3 (Layout / figure / compile integration):
├── Task 11: Apply bounded float-neighborhood and whitespace cleanup in active chapter files [unspecified-high]
├── Task 12: Fix repo-local LaTeX-controlled figure/table formatting issues and document exclusions [unspecified-high]
├── Task 13: Compile blind-review thesis and resolve direct-fix fallout [unspecified-high]
└── Task 14: Cross-file residual scan for first-person, empty captions, title punctuation, and scope drift [quick]

Wave 4 (Reviewer-facing verification):
├── Task 15: Verify direct-fix completion against `blind-review-comments.md` [deep]
├── Task 16: Produce final evidence summary for completed vs excluded direct-fix items [writing]
└── Task 17: Reviewer-style final read of the bounded direct-fix pass [oracle]

Wave FINAL (After ALL tasks — 4 parallel reviews):
├── Task F1: Plan compliance audit (oracle)
├── Task F2: Content/format quality review (unspecified-high)
├── Task F3: Real QA execution of all planned checks (unspecified-high)
└── Task F4: Scope fidelity check (deep)

Critical Path: Task 1 -> Task 3 -> Task 8 -> Task 11 -> Task 12 -> Task 13 -> Task 14 -> Task 15 -> Task 17 -> F1-F4
Parallel Speedup: ~65% faster than fully sequential cleanup
Max Concurrent: 5

### Dependency Matrix
- **1**: None -> 6, 7, 8, 9, 10, 11, 12, 14
- **2**: None -> 6, 14, 15
- **3**: None -> 7, 8, 11, 12, 14
- **4**: None -> 10, 15
- **5**: None -> 9, 12, 16
- **6**: 1, 2 -> 13, 14, 15
- **7**: 1, 3 -> 13, 14, 15
- **8**: 1, 3 -> 11, 13, 14, 15
- **9**: 1, 5 -> 13, 14, 15
- **10**: 1, 4 -> 13, 14, 15
- **11**: 1, 3, 8 -> 13, 14, 15
- **12**: 1, 3, 5 -> 13, 14, 15, 16
- **13**: 6, 7, 8, 9, 10, 11, 12 -> 14, 15, 16, 17
- **14**: 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13 -> 15, 17
- **15**: 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14 -> 16, 17
- **16**: 5, 12, 13, 15 -> 17, F1-F4
- **17**: 13, 14, 15, 16 -> F1-F4

### Agent Dispatch Summary
- **Wave 1**: T1–T5 → `quick`
- **Wave 2**: T6 → `writing`, T7–T9 → `quick`, T10 → `unspecified-high`
- **Wave 3**: T11–T13 → `unspecified-high`, T14 → `quick`
- **Wave 4**: T15 → `deep`, T16 → `writing`, T17 → `oracle`
- **FINAL**: F1 → `oracle`, F2 → `unspecified-high`, F3 → `unspecified-high`, F4 → `deep`

---

## TODOs
- [x] 1. Lock active build surface and exclusions

  **What to do**:
  - Confirm the active build surface from `body/graduate/content.tex` and `zjuthesis.tex`, including blind-review mode.
  - Record hard exclusions: backup directories, commented-out content unless proven active, standalone preview files, and template/config paths unless preflight proves absolute necessity.
  - Produce a small exclusion checklist so later tasks cannot drift into `paper1_backup`, `paper2_backup`, or `4_results_tikz_preview.tex`.

  **Must NOT do**:
  - Do not edit any thesis source in this task.
  - Do not promote config-level changes merely because they seem globally convenient.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: this is a bounded repository-surface audit with deterministic outputs.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: no prose creation required.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2, 3, 4, 5)
  - **Blocks**: 6, 7, 8, 9, 10, 11, 12, 14
  - **Blocked By**: None

  **References**:
  - `body/graduate/content.tex` - authoritative list of active chapter entry points for the thesis body.
  - `zjuthesis.tex` - confirms `BlindReview = true`, `TwoSide = false`, and the actual graduate thesis build target.
  - `body/graduate/paper2/main.tex` - shows commented-out `paper2/2_related` input and prevents accidental edits to inactive content.
  - `body/graduate/paper1/4_results_tikz_preview.tex` - standalone preview candidate that must be excluded unless proven to be built.

  **Acceptance Criteria**:
  - [ ] Active build surface documented from source, not guessed.
  - [ ] Explicit exclusion list includes backup trees, standalone preview files, and config/class paths.
  - [ ] No file outside the approved surface is later assigned to direct-fix implementation tasks.

  **QA Scenarios**:
  ```
  Scenario: Confirm active build inputs
    Tool: Read
    Preconditions: Repository available locally
    Steps:
      1. Read `body/graduate/content.tex` and list each `\inputbody{...}` target.
      2. Read `zjuthesis.tex` and confirm `BlindReview = true` and graduate thesis mode.
      3. Read `body/graduate/paper2/main.tex` and confirm `paper2/2_related` is commented out.
    Expected Result: A finite approved build surface and exclusion set is established.
    Failure Indicators: Any implementation task later references a backup/inactive/preview file without explicit proof.
    Evidence: .sisyphus/evidence/task-1-build-surface.md

  Scenario: Reject forbidden edit targets
    Tool: Read
    Preconditions: Exclusion candidates identified
    Steps:
      1. Inspect `body/graduate/paper1/4_results_tikz_preview.tex` and note standalone `\documentclass` usage.
      2. Verify backup directories are not present in `body/graduate/content.tex` inputs.
    Expected Result: Preview and backup paths are marked excluded.
    Evidence: .sisyphus/evidence/task-1-exclusions.md
  ```

  **Commit**: NO

- [x] 2. Audit authorial first-person usages in active thesis prose

  **What to do**:
  - Search active thesis prose for authorial first-person usages such as `我们`, keeping the scan inside the approved build surface.
  - Distinguish real authorial narration from mathematical/expository phrasing that may need nuanced rewriting rather than simple deletion.
  - Produce a precise list of files and passages that require third-person normalization in the direct-fix pass.

  **Must NOT do**:
  - Do not search backup trees or commented-out inactive files as if they were build blockers.
  - Do not decide final rewritten wording here; this task is an audit, not the implementation.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: this is a targeted text-pattern inventory for later rewriting.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `oracle`: unnecessary for a bounded usage inventory.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 3, 4, 5)
  - **Blocks**: 6, 14, 15
  - **Blocked By**: None

  **References**:
  - `blind-review-comments.md` - reviewer item `三.2` and related direct-fix scoping for third-person normalization.
  - `body/graduate/content.tex` - restricts the audit to active files only.
  - `body/graduate/intro/2_related_and_problems.tex` - already surfaced one active-file hit in earlier scanning.
  - `body/graduate/intro/3_contributions_and_organization.tex` - already surfaced one active-file hit in earlier scanning.
  - `body/graduate/paper3/3_simulation.tex` - already surfaced multiple active-file hits that need later rewriting review.

  **Acceptance Criteria**:
  - [ ] Every in-scope authorial `我们` usage is inventoried with file and local context.
  - [ ] No backup-only occurrences are treated as blockers for the direct-fix pass.
  - [ ] The audit output is sufficient to drive Task 6 without reopening discovery.

  **QA Scenarios**:
  ```
  Scenario: Inventory active-file first-person usage
    Tool: Grep
    Preconditions: Approved build surface from Task 1
    Steps:
      1. Run a scoped search for `我们` within active thesis prose files only.
      2. Record file paths and nearby context for each hit.
      3. Exclude backup/inactive paths from the final inventory.
    Expected Result: A clean active-file usage list exists for later rewriting.
    Failure Indicators: Inventory includes backup-only files or misses previously known active hits.
    Evidence: .sisyphus/evidence/task-2-first-person-inventory.md

  Scenario: Confirm no config/page false positives drive scope
    Tool: Grep
    Preconditions: Initial scan suggested config/page areas are clean
    Steps:
      1. Recheck config/page thesis text locations if needed.
      2. Confirm no direct-fix task depends on non-body first-person cleanup.
    Expected Result: Scope remains thesis-body-centric.
    Evidence: .sisyphus/evidence/task-2-scope-check.md
  ```

  **Commit**: NO

- [x] 3. Audit heading/caption/reference-placement hotspots in active files

  **What to do**:
  - Confirm all active-file hotspots for title punctuation, empty short captions, and figure-reference flow that map to direct-fix reviewer comments.
  - Separate source-level issues from class/config presentation behavior, so source normalization is attempted first.
  - Produce a file-specific hotspot map for Tasks 7, 8, and 11.

  **Must NOT do**:
  - Do not broaden this into global stylistic title rewriting.
  - Do not assume every colon in a Chinese title is wrong without mapping it to the specific reviewer complaint and intended normalization policy.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: deterministic hotspot confirmation across a small set of active files.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: this task inventories issues only.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 4, 5)
  - **Blocks**: 7, 8, 11, 12, 14
  - **Blocked By**: None

  **References**:
  - `blind-review-comments.md` - reviewer items `二.2`, `三.3`, `四.1`, and format-extract rows already scoped as direct-fix items.
  - `body/graduate/intro/1_background.tex` - contains `\caption[]{数值模拟过程与网格离散示意图}` and a nearby forward `\Cref` usage.
  - `body/graduate/intro/3_contributions_and_organization.tex` - contains `\caption[]{论文组织结构示意图}` and figure-reference flow near the organization diagram.
  - `body/graduate/intro/2_related_and_problems.tex` - contains active subsection titles with `：` punctuation.
  - `body/graduate/paper2/main.tex` - contains the active chapter title with `：` punctuation.
  - `config/format/general/heading.tex` - reference only; helps verify that numbering is controlled by class settings and that source-level fixes should precede config-level edits.

  **Acceptance Criteria**:
  - [ ] Active-file hotspot map exists for title punctuation, empty short captions, and reference-placement cleanup.
  - [ ] Each hotspot is classified as source-fixable or requiring later layout verification.
  - [ ] No backup-only title/caption issues are used to inflate scope.

  **QA Scenarios**:
  ```
  Scenario: Confirm empty short-caption hotspots
    Tool: Grep
    Preconditions: Active thesis files available
    Steps:
      1. Search for `caption[]` occurrences in active thesis files.
      2. Confirm only the two intro files contain empty short-caption brackets in scope.
    Expected Result: Exactly the known intro hotspots are captured unless a new active-file match appears.
    Failure Indicators: Missed active hotspots or polluted results from inactive files.
    Evidence: .sisyphus/evidence/task-3-empty-caption-hotspots.md

  Scenario: Confirm title punctuation hotspots
    Tool: Grep
    Preconditions: Active thesis files available
    Steps:
      1. Search active titles for full-width colon usage in chapter/section/subsection commands.
      2. Confirm `intro/2_related_and_problems.tex` and `paper2/main.tex` are the active targets.
    Expected Result: A bounded title-normalization target list exists.
    Evidence: .sisyphus/evidence/task-3-title-hotspots.md
  ```

  **Commit**: NO

- [x] 4. Audit bounded bibliography repair scope in `body/ref.bib`

  **What to do**:
  - Identify the reviewer-flagged bibliography problems that are directly fixable from bib metadata: missing pages, wrong venue type, incomplete venue fields, and obvious formatting-field omissions.
  - Bound the repair scope to the explicitly flagged entries plus immediately adjacent malformed entries discovered while inspecting the same patterns.
  - Record any entries that require external publication lookup as deferred rather than silently expanding scope to a full bibliography rewrite.

  **Must NOT do**:
  - Do not normalize the entire 2360-line bibliography without evidence of a generator-wide defect.
  - Do not guess venue type or page range if the source entry cannot be verified from existing local evidence.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: this is a bounded metadata audit with explicit reviewer targets.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `librarian`: not needed unless a specific entry later proves unverifiable locally.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3, 5)
  - **Blocks**: 10, 15
  - **Blocked By**: None

  **References**:
  - `blind-review-comments.md` - reviewer items `二.6` and `五.6` define the bounded bibliography-fix scope.
  - `body/ref.bib` - sole active bibliography source to inspect and repair in this pass.
  - `config/format/general/reference.tex` - reference-only context if citation/render behavior needs confirmation.

  **Acceptance Criteria**:
  - [ ] A finite list of directly fixable flagged bibliography entries is produced.
  - [ ] Clearly unverifiable entries are marked deferred instead of guessed.
  - [ ] Task 10 can proceed without reopening discovery.

  **QA Scenarios**:
  ```
  Scenario: Build bounded bibliography repair list
    Tool: Read
    Preconditions: `body/ref.bib` available locally
    Steps:
      1. Inspect the bib file around reviewer-flagged entries and matching malformed patterns.
      2. Record which entries have missing pages, inconsistent venue fields, or likely wrong entry types.
      3. Mark any entry needing external verification as deferred.
    Expected Result: A bounded repair list exists without escalating to a full bibliography rewrite.
    Failure Indicators: Audit proposes editing large unrelated regions of the bib database.
    Evidence: .sisyphus/evidence/task-4-bib-scope.md

  Scenario: Reject bibliography scope creep
    Tool: Read
    Preconditions: Repair list drafted
    Steps:
      1. Compare planned bibliography edits against reviewer-flagged items.
      2. Confirm only adjacent obvious malformed entries are added.
    Expected Result: Scope remains targeted and reviewable.
    Evidence: .sisyphus/evidence/task-4-bib-guardrails.md
  ```

  **Commit**: NO

- [x] 5. Classify reviewer-flagged figure-format issues into LaTeX-fixable vs external-source-only

  **What to do**:
  - Triage reviewer-flagged figure/table formatting complaints into: source-level TeX/TikZ fixable, float-placement fixable, and external-image-source-only.
  - Use repository evidence to determine whether a problematic visual is generated from active TeX/TikZ or embedded as raster/PDF asset.
  - Prepare an exclusions note for external-source-only issues that cannot be responsibly fixed in this direct-fix pass.

  **Must NOT do**:
  - Do not pretend raster/PDF label problems are fixable from LaTeX if the source generator is absent.
  - Do not classify standalone preview files as active build evidence without confirming inclusion.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: issue triage based on file provenance and build role is a bounded repository analysis.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `artistry`: no non-conventional design work required.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3, 4)
  - **Blocks**: 9, 12, 16
  - **Blocked By**: None

  **References**:
  - `blind-review-comments.md` - reviewer items `一.1`, `二.1`, `五.1`, and their format extracts provide the triage targets.
  - `body/graduate/paper1/4_results_tikz_preview.tex` - example of a standalone preview that must not be assumed active.
  - `config/format/general/caption.tex` - shows what is globally controllable from LaTeX versus what likely lives inside figure assets.
  - `body/graduate/intro/1_background.tex` and `intro/3_contributions_and_organization.tex` - active in-source TikZ figures suitable for direct-fix categorization.

  **Acceptance Criteria**:
  - [ ] Each flagged figure-format issue is classified into a fixability bucket.
  - [ ] External-source-only items are documented for exclusion rather than silently dropped.
  - [ ] Tasks 9 and 12 receive only realistically fixable targets.

  **QA Scenarios**:
  ```
  Scenario: Triage figure-format fixability
    Tool: Read
    Preconditions: Reviewer targets identified
    Steps:
      1. Inspect source files for the flagged figure contexts.
      2. Determine whether the visual is built from active TeX/TikZ or from external image assets.
      3. Record the fixability class for each item.
    Expected Result: A defensible fixability map exists.
    Failure Indicators: A raster-only issue is assigned to a pure TeX-edit task without supporting source evidence.
    Evidence: .sisyphus/evidence/task-5-figure-triage.md

  Scenario: Prepare exclusion note inputs
    Tool: Read
    Preconditions: At least one external-source-only issue exists
    Steps:
      1. Record the file path and reason the issue cannot be fixed in-repo.
      2. Preserve this for Task 16 evidence generation.
    Expected Result: Exclusions are transparent and reviewable.
    Evidence: .sisyphus/evidence/task-5-exclusion-inputs.md
  ```

  **Commit**: NO

- [x] 6. Normalize third-person narrative in active prose files

  **What to do**:
  - Rewrite inventoried authorial first-person passages into objective thesis prose while preserving technical meaning and sentence fluency.
  - Prefer local rewrites such as `本文`, impersonal formulations, or direct declarative sentences over awkward mechanical replacements.
  - Keep the rewrite limited to inventoried active-file passages from Task 2.

  **Must NOT do**:
  - Do not polish unrelated prose opportunistically.
  - Do not change scientific claims, strength of conclusions, or methodological scope while rewriting.

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: this is precise prose normalization under strict meaning-preservation constraints.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `internal-comms`: wrong domain; this is thesis prose, not organizational communication.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 7, 8, 9, 10)
  - **Blocks**: 13, 14, 15
  - **Blocked By**: 1, 2

  **References**:
  - `.sisyphus/evidence/task-2-first-person-inventory.md` - authoritative inventory produced by Task 2.
  - `body/graduate/intro/2_related_and_problems.tex` - contains active prose that already surfaced in the first-person scan.
  - `body/graduate/intro/3_contributions_and_organization.tex` - contains active prose that already surfaced in the first-person scan.
  - `body/graduate/paper3/3_simulation.tex` - contains multiple active prose passages requiring careful normalization.

  **Acceptance Criteria**:
  - [ ] All inventoried in-scope first-person usages are rewritten or explicitly justified as non-authorial.
  - [ ] Rewritten sentences remain grammatical and technically faithful.
  - [ ] Residual grep scan in Task 14 finds no unresolved in-scope `我们` usage.

  **QA Scenarios**:
  ```
  Scenario: Rewrite and verify objective narration
    Tool: Read
    Preconditions: Task 2 inventory complete
    Steps:
      1. Inspect each inventoried passage after editing.
      2. Confirm the sentence no longer uses authorial first-person.
      3. Confirm the sentence still makes technical sense in context.
    Expected Result: Objective narration replaces authorial first person without semantic drift.
    Failure Indicators: Mechanical replacements create ungrammatical or ambiguous prose.
    Evidence: .sisyphus/evidence/task-6-third-person-review.md

  Scenario: Residual first-person scan
    Tool: Grep
    Preconditions: Rewrites applied
    Steps:
      1. Re-run scoped search for `我们` across active thesis prose.
      2. Review any remaining hits and classify them as resolved/non-authorial/out-of-scope.
    Expected Result: No unresolved in-scope authorial hits remain.
    Evidence: .sisyphus/evidence/task-6-residual-scan.md
  ```

  **Commit**: YES
  - Message: `style(graduate): normalize third-person thesis narration`
  - Files: active prose files only
  - Pre-commit: `latexmk`

- [x] 7. Normalize heading punctuation/numbering in active chapter/title files

  **What to do**:
  - Normalize the reviewer-flagged active titles so they no longer depend on the questioned colon presentation style.
  - Keep the change source-local and minimal: adjust title text only where needed, not the global heading system.
  - Re-read nearby structure to ensure the new headings remain scientifically specific and grammatically natural.

  **Must NOT do**:
  - Do not modify `config/format/general/heading.tex` in this task.
  - Do not rewrite entire section headings for style polish beyond the punctuation/numbering concern.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: bounded, source-local heading normalization with low conceptual risk.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: the wording change should stay minimal and mechanical.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 6, 8, 9, 10)
  - **Blocks**: 13, 14, 15
  - **Blocked By**: 1, 3

  **References**:
  - `.sisyphus/evidence/task-3-title-hotspots.md` - bounded hotspot list from Task 3.
  - `body/graduate/intro/2_related_and_problems.tex` - active subsection titles containing full-width colons.
  - `body/graduate/paper2/main.tex` - active chapter title containing full-width colon.
  - `config/format/general/heading.tex` - confirms numbering display is class-controlled, so source text should be normalized first.

  **Acceptance Criteria**:
  - [ ] Every targeted active title is normalized in source.
  - [ ] No config/class heading file is touched.
  - [ ] Post-edit source scan no longer finds unresolved targeted title patterns in active files.

  **QA Scenarios**:
  ```
  Scenario: Normalize targeted title text
    Tool: Read
    Preconditions: Task 3 title hotspot map complete
    Steps:
      1. Inspect each targeted heading after editing.
      2. Confirm the questioned colon style is removed or normalized as planned.
      3. Confirm neighboring labels/section structure remain intact.
    Expected Result: Titles are cleaner without changing chapter structure.
    Failure Indicators: Heading edits create awkward phrasing or require config-level changes.
    Evidence: .sisyphus/evidence/task-7-heading-review.md

  Scenario: Residual title-pattern scan
    Tool: Grep
    Preconditions: Heading edits applied
    Steps:
      1. Re-run scoped search for colon-bearing active chapter/section titles.
      2. Confirm only approved out-of-scope/inactive matches remain, if any.
    Expected Result: Active targeted hotspots are gone.
    Evidence: .sisyphus/evidence/task-7-residual-title-scan.md
  ```

  **Commit**: YES
  - Message: `style(intro): normalize direct-review heading punctuation`
  - Files: targeted intro/paper2 title sources
  - Pre-commit: `latexmk`

- [x] 8. Repair intro short captions and nearby figure-reference flow

  **What to do**:
  - Replace empty `\caption[]{...}` forms in the active intro figures with correct short-caption handling.
  - Review nearby `\Cref` / figure placement flow in the same local regions and apply minimal source-order or sentence-order adjustments if needed.
  - Keep this task tightly confined to the intro figure hotspots already confirmed in Task 3.

  **Must NOT do**:
  - Do not reorder large sections of the introduction for broader rhetorical reasons.
  - Do not change figure labels or reference keys unless absolutely required to preserve compilation.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: this is a small, source-local caption/reference cleanup with deterministic targets.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `visual-engineering`: unnecessary because this is LaTeX source cleanup, not frontend design.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 6, 7, 9, 10)
  - **Blocks**: 11, 13, 14, 15
  - **Blocked By**: 1, 3

  **References**:
  - `.sisyphus/evidence/task-3-empty-caption-hotspots.md` - exact in-scope empty-caption targets.
  - `body/graduate/intro/1_background.tex` - contains the active empty short caption and the nearby `\Cref{fig:numerical_simulation_process}` flow.
  - `body/graduate/intro/3_contributions_and_organization.tex` - contains the active empty short caption for the organization diagram.
  - `config/format/general/caption.tex` - reference-only context for caption formatting behavior.

  **Acceptance Criteria**:
  - [ ] No targeted active intro figure retains empty `\caption[]{...}` syntax.
  - [ ] Local figure-reference flow is not made worse by the fix.
  - [ ] The thesis still compiles with correct figure references.

  **QA Scenarios**:
  ```
  Scenario: Fix empty short captions
    Tool: Grep
    Preconditions: Task 3 hotspots confirmed
    Steps:
      1. Replace empty short-caption brackets in the two intro files.
      2. Re-run the empty-caption search within active thesis files.
    Expected Result: No targeted empty `\caption[]{...}` remains.
    Failure Indicators: Empty bracket syntax persists or new empty-caption forms are introduced.
    Evidence: .sisyphus/evidence/task-8-caption-fix.md

  Scenario: Verify local figure-reference flow
    Tool: Read
    Preconditions: Caption edits applied
    Steps:
      1. Read the paragraph surrounding each edited figure.
      2. Confirm the figure is introduced coherently and the local sentence order remains natural.
    Expected Result: Caption cleanup does not introduce awkward forward/backward reference flow.
    Evidence: .sisyphus/evidence/task-8-reference-flow.md
  ```

  **Commit**: YES
  - Message: `style(intro): repair short captions and figure cues`
  - Files: `intro/1_background.tex`, `intro/3_contributions_and_organization.tex`
  - Pre-commit: `latexmk`

- [x] 9. Fix directly editable symbol/font consistency hotspots in active thesis source

  **What to do**:
  - Address only those reviewer-flagged symbol/font consistency issues that are directly editable inside active TeX/TikZ source.
  - Standardize local notation/font usage where the inconsistency is source-visible in the thesis, not embedded inside external image assets.
  - Carry forward the fixability classification from Task 5 so this task never spills into impossible raster regeneration work.

  **Must NOT do**:
  - Do not attempt to regenerate external figures without tracked source assets.
  - Do not edit standalone preview files unless Task 1 explicitly lifted their exclusion, which is not expected.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: source-local typography/notational cleanup is narrow when fixability is pre-triaged.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `artistry`: no creative redesign required.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 6, 7, 8, 10)
  - **Blocks**: 13, 14, 15
  - **Blocked By**: 1, 5

  **References**:
  - `.sisyphus/evidence/task-5-figure-triage.md` - determines which formatting issues are actually TeX-fixable.
  - `blind-review-comments.md` - reviewer items `一.1`, `二.1`, and `五.1` define the problem family.
  - Active TeX/TikZ files surfaced by Task 5 - concrete implementation targets only after fixability is proven.

  **Acceptance Criteria**:
  - [ ] Every change in this task is tied to a fixability-approved active source file.
  - [ ] No external-source-only issue is silently pseudo-fixed.
  - [ ] Resulting notation/font usage is locally consistent where edited.

  **QA Scenarios**:
  ```
  Scenario: Apply only fixable source-level consistency edits
    Tool: Read
    Preconditions: Task 5 triage complete
    Steps:
      1. Inspect each targeted active source hotspot before and after editing.
      2. Confirm the inconsistency was source-level and is now normalized.
    Expected Result: Only truly editable symbol/font issues are changed.
    Failure Indicators: A change references excluded preview/raster-only evidence.
    Evidence: .sisyphus/evidence/task-9-font-symbol-fixes.md

  Scenario: Verify excluded issues stayed excluded
    Tool: Read
    Preconditions: Any external-source-only issues exist
    Steps:
      1. Compare Task 9 edits with the exclusion list from Task 5.
      2. Confirm no excluded item was accidentally worked around with unrelated edits.
    Expected Result: Fixability boundaries are respected.
    Evidence: .sisyphus/evidence/task-9-exclusion-check.md
  ```

  **Commit**: YES
  - Message: `style(graduate): normalize direct-fix notation hotspots`
  - Files: fixability-approved active source files only
  - Pre-commit: `latexmk`

- [x] 10. Apply bounded bibliography normalization in `body/ref.bib`

  **What to do**:
  - Fix the bounded list of directly repairable bibliography entries identified in Task 4.
  - Normalize missing pages, obvious type mismatches, and incomplete venue metadata only where local evidence is sufficient.
  - Preserve the overall bibliography system and style package behavior; change entry data, not citation infrastructure.

  **Must NOT do**:
  - Do not perform a stylistic mass rewrite of unrelated entries.
  - Do not invent missing metadata without local evidence or explicit external verification.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: bibliography data cleanup is low conceptual risk but requires careful high-volume precision in a large `.bib` file.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: this is structured metadata repair, not prose writing.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 6, 7, 8, 9)
  - **Blocks**: 13, 14, 15
  - **Blocked By**: 1, 4

  **References**:
  - `.sisyphus/evidence/task-4-bib-scope.md` - bounded repair list.
  - `body/ref.bib` - the only bibliography data file to edit in this pass.
  - `blind-review-comments.md` - reviewer items `二.6` and `五.6` define the motivating defects.

  **Acceptance Criteria**:
  - [ ] All bounded repair-list entries are corrected or explicitly deferred.
  - [ ] No broad unrelated bibliography sweep is introduced.
  - [ ] Blind-review build later completes without bibliography-related undefined citation fallout.

  **QA Scenarios**:
  ```
  Scenario: Repair bounded bibliography entries
    Tool: Read
    Preconditions: Task 4 repair list complete
    Steps:
      1. Inspect each targeted bib entry after editing.
      2. Confirm required fields are present and obvious type/venue issues are corrected.
    Expected Result: The bounded bibliography repair list is fully addressed.
    Failure Indicators: Untargeted unrelated sections of `body/ref.bib` are rewritten.
    Evidence: .sisyphus/evidence/task-10-bib-review.md

  Scenario: Verify bibliography scope remained bounded
    Tool: Read
    Preconditions: Bib edits applied
    Steps:
      1. Compare edited entries against the Task 4 repair list.
      2. Confirm added edits are only directly adjacent obvious malformed cases.
    Expected Result: Bounded normalization respected.
    Evidence: .sisyphus/evidence/task-10-bib-scope-check.md
  ```

  **Commit**: YES
  - Message: `style(bib): normalize direct-review reference entries`
  - Files: `body/ref.bib`
  - Pre-commit: `latexmk`

- [x] 11. Apply bounded float-neighborhood and whitespace cleanup in active chapter files

  **What to do**:
  - Adjust only the reviewer-relevant local float/paragraph neighborhoods and obvious whitespace hotspots in active chapter files.
  - Use minimal source changes: placement specifiers, local paragraph/float adjacency adjustments, or small source-order improvements where safe.
  - Keep this bounded to the hotspots mapped in Task 3 and any directly linked follow-up from Task 8.

  **Must NOT do**:
  - Do not launch a whole-thesis pagination redesign.
  - Do not move large blocks of scientific discussion merely to chase visual density.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: float/layout cleanup requires careful local judgment and compile feedback while staying tightly bounded.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `visual-engineering`: this is PDF typesetting cleanup, not UI engineering.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 12, 13, 14)
  - **Blocks**: 13, 14, 15
  - **Blocked By**: 1, 3, 8

  **References**:
  - `.sisyphus/evidence/task-3-empty-caption-hotspots.md` and `.sisyphus/evidence/task-3-title-hotspots.md` - upstream hotspot maps.
  - `body/graduate/intro/1_background.tex` - known local figure-reference flow hotspot.
  - `body/graduate/intro/3_contributions_and_organization.tex` - organization figure neighborhood hotspot.
  - `blind-review-comments.md` - reviewer items `一.5` and `四.1` define whitespace and nearby-figure concerns.

  **Acceptance Criteria**:
  - [ ] Targeted local whitespace/float issues are improved without broader layout drift.
  - [ ] No large unrelated source movement is introduced.
  - [ ] Later compile/PDF verification confirms the local neighborhoods are not worse than before.

  **QA Scenarios**:
  ```
  Scenario: Improve bounded float neighborhoods
    Tool: Read
    Preconditions: Hotspot map complete
    Steps:
      1. Inspect each targeted hotspot after editing.
      2. Confirm the surrounding text/float neighborhood is locally cleaner and still coherent.
    Expected Result: Reviewer-relevant float/whitespace hotspots are improved.
    Failure Indicators: Edits cause broader chapter restructuring or unclear local flow.
    Evidence: .sisyphus/evidence/task-11-float-neighborhood.md

  Scenario: Check for obvious whitespace regressions after compile
    Tool: Bash (latexmk)
    Preconditions: Layout edits applied
    Steps:
      1. Build the thesis in blind-review mode.
      2. Inspect the resulting PDF pages around edited hotspots.
    Expected Result: No edited hotspot page exhibits worse blank-area behavior than before.
    Evidence: .sisyphus/evidence/task-11-layout-check.pdf
  ```

  **Commit**: YES
  - Message: `style(graduate): tighten direct-review float layout`
  - Files: targeted active chapter files only
  - Pre-commit: `latexmk`

- [x] 12. Fix repo-local LaTeX-controlled figure/table formatting issues and document exclusions

  **What to do**:
  - Implement only the figure/table formatting fixes that Task 5 proved are controllable from active repo source.
  - For every reviewer-flagged issue that remains external-source-only, document the exclusion cleanly in an evidence note instead of stretching scope.
  - Keep formatting fixes local to active build files and avoid template-wide changes unless unavoidable and explicitly justified.

  **Must NOT do**:
  - Do not edit backup or preview-only files.
  - Do not claim reviewer figure complaints are fully resolved if some items are excluded due to missing source-generation assets.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: this mixes careful LaTeX/TikZ edits with scope-bound exclusion documentation.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: prose-only tooling is insufficient because source-format fixes and exclusion evidence are both required.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 11, 13, 14)
  - **Blocks**: 13, 14, 15, 16
  - **Blocked By**: 1, 3, 5

  **References**:
  - `.sisyphus/evidence/task-5-figure-triage.md` - authoritative fixability classification.
  - `blind-review-comments.md` - reviewer items `一.1`, `二.1`, `五.1`, and format extracts.
  - Active source files surfaced by Task 5 - only these may be edited in this task.
  - `.sisyphus/evidence/task-5-exclusion-inputs.md` - seeds the exclusion note.

  **Acceptance Criteria**:
  - [ ] All repo-local fixable figure/table formatting issues in scope are addressed.
  - [ ] All excluded external-source-only issues are documented with file path and reason.
  - [ ] No forbidden file paths are edited.

  **QA Scenarios**:
  ```
  Scenario: Apply approved figure/table formatting fixes
    Tool: Read
    Preconditions: Task 5 triage complete
    Steps:
      1. Inspect each fixable active-source target after editing.
      2. Confirm the formatting issue is visibly addressed in source and later compile output.
    Expected Result: Only approved fixable targets are changed.
    Failure Indicators: An excluded raster-only issue is treated as resolved without source evidence.
    Evidence: .sisyphus/evidence/task-12-fixable-figure-fixes.md

  Scenario: Generate exclusion evidence
    Tool: Read
    Preconditions: At least one issue remains external-source-only
    Steps:
      1. Write `.sisyphus/evidence/blind-review-direct-fixes-exclusions.md`.
      2. For each excluded item, record reviewer index, affected asset/file, and reason it cannot be fixed in-repo.
    Expected Result: Exclusions are transparent and auditable.
    Evidence: .sisyphus/evidence/blind-review-direct-fixes-exclusions.md
  ```

  **Commit**: YES
  - Message: `style(figures): fix direct-review source-level formatting`
  - Files: fixability-approved active source files and evidence note
  - Pre-commit: `latexmk`

- [x] 13. Compile blind-review thesis and resolve direct-fix fallout

  **What to do**:
  - Run the full thesis build in blind-review mode using `latexmk`.
  - Resolve direct fallout caused by the bounded fixes: broken refs, broken citations, obvious LaTeX syntax errors, and immediately traceable float fallout.
  - Keep remediation strictly tied to the direct-fix changes already made.

  **Must NOT do**:
  - Do not use the compile step as an excuse for unrelated cleanup.
  - Do not change scientific content while resolving compile fallout.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: compilation and fallout resolution require careful end-to-end verification plus disciplined scope control.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `quick`: compile fallout often requires more than trivial follow-through.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 11, 12, 14 after prerequisites)
  - **Blocks**: 14, 15, 16, 17
  - **Blocked By**: 6, 7, 8, 9, 10, 11, 12

  **References**:
  - `AGENTS.md` at repo root - explicitly recommends `latexmk` as the authoritative build command.
  - `zjuthesis.tex` - confirms blind-review build mode.
  - All files edited in Tasks 6–12 - fallout remediation must stay limited to these direct-fix areas unless an immediately adjacent compile blocker appears.

  **Acceptance Criteria**:
  - [ ] `latexmk` succeeds.
  - [ ] No undefined references/citations remain in the build log.
  - [ ] Any compile-fallout edits remain tightly scoped to direct-fix consequences.

  **QA Scenarios**:
  ```
  Scenario: Full blind-review compile
    Tool: Bash (latexmk)
    Preconditions: Tasks 6–12 complete
    Steps:
      1. Run `latexmk` from the repository root.
      2. Inspect the log for undefined references, citation failures, and fatal errors.
    Expected Result: Build succeeds cleanly in blind-review mode.
    Failure Indicators: Fatal build failure or unresolved references/citations remain.
    Evidence: .sisyphus/evidence/task-13-latexmk.log

  Scenario: Verify fallout stayed local
    Tool: Read
    Preconditions: Any compile-driven follow-up edits applied
    Steps:
      1. Review each fallout fix.
      2. Confirm it traces directly to a prior direct-fix change or immediate compile consequence.
    Expected Result: No opportunistic side cleanup was added.
    Evidence: .sisyphus/evidence/task-13-fallout-scope.md
  ```

  **Commit**: NO

- [x] 14. Cross-file residual scan for first-person, empty captions, title punctuation, and scope drift

  **What to do**:
  - Re-run the critical residual scans across active thesis files after implementation and compile stabilization.
  - Check specifically for unresolved `我们`, empty short-caption syntax, targeted title punctuation patterns, and edits outside approved files.
  - Produce a compact pass/fail matrix to drive final verification tasks.

  **Must NOT do**:
  - Do not discover new broad work categories here; this is a residual check, not a new planning phase.
  - Do not treat inactive/backup hits as failures.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: this is a final bounded verification scan across known patterns.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `oracle`: reserved for higher-level final review, not residual pattern scanning.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 11, 12, 13 where dependencies permit)
  - **Blocks**: 15, 17
  - **Blocked By**: 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13

  **References**:
  - `.sisyphus/evidence/task-2-first-person-inventory.md` - baseline inventory for first-person cleanup.
  - `.sisyphus/evidence/task-3-empty-caption-hotspots.md` and `.sisyphus/evidence/task-3-title-hotspots.md` - baseline hotspot inventories.
  - Git diff for the working branch - used to confirm approved-file boundaries.

  **Acceptance Criteria**:
  - [ ] No unresolved in-scope `我们` remains.
  - [ ] No targeted empty `\caption[]{...}` remains.
  - [ ] No targeted active title punctuation issue remains.
  - [ ] Diff scope stays within approved files and evidence outputs.

  **QA Scenarios**:
  ```
  Scenario: Run residual pattern matrix
    Tool: Grep
    Preconditions: Compile-stable direct-fix pass complete
    Steps:
      1. Re-run scoped searches for `我们`, empty `caption[]`, and active title-colon patterns.
      2. Compare results against the baseline hotspot lists.
    Expected Result: All targeted residual scans pass or have documented exclusions.
    Failure Indicators: A baseline hotspot still appears unresolved.
    Evidence: .sisyphus/evidence/task-14-residual-matrix.md

  Scenario: Confirm scope drift absence
    Tool: Read
    Preconditions: Current diff available
    Steps:
      1. Review changed files in the diff.
      2. Confirm every changed path belongs to the approved direct-fix surface or evidence outputs.
    Expected Result: No scope drift is present.
    Evidence: .sisyphus/evidence/task-14-scope-drift.md
  ```

  **Commit**: NO

- [x] 15. Verify direct-fix completion against `blind-review-comments.md`

  **What to do**:
  - Cross-check each in-scope direct-fix item from `blind-review-comments.md` against the actual changed files and residual-scan results.
  - Confirm that every item is either completed or explicitly excluded with evidence.
  - Reject any claimed completion that is only compile-based and not tied to reviewer-facing outcomes.

  **Must NOT do**:
  - Do not reopen out-of-scope theory/experiment issues.
  - Do not mark an item complete if only part of the reviewer-visible defect was addressed without disclosure.

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: this requires careful comparison between reviewer language, actual edits, and exclusion evidence.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: verification, not drafting, is the main need.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 4 (with Tasks 16, 17 where dependencies permit)
  - **Blocks**: 16, 17
  - **Blocked By**: 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14

  **References**:
  - `blind-review-comments.md` - authoritative reviewer-item tracker and direct-fix subset.
  - `.sisyphus/evidence/task-14-residual-matrix.md` - residual scan verdicts.
  - `.sisyphus/evidence/blind-review-direct-fixes-exclusions.md` - explicit exclusions note if any.
  - Git diff of the implementation pass - confirms concrete file-level outcomes.

  **Acceptance Criteria**:
  - [ ] Every in-scope direct-fix item is mapped to a completed edit or explicit exclusion.
  - [ ] No reviewer item is overclaimed.
  - [ ] The verification result is detailed enough to brief the user without extra archaeology.

  **QA Scenarios**:
  ```
  Scenario: Map reviewer items to concrete outcomes
    Tool: Read
    Preconditions: Tasks 6–14 complete
    Steps:
      1. Read the direct-fix subset in `blind-review-comments.md`.
      2. For each item, map it to the changed source or the exclusion note.
      3. Confirm residual checks support the completion claim.
    Expected Result: A reviewer-item completion matrix exists.
    Failure Indicators: Any in-scope item lacks a concrete outcome mapping.
    Evidence: .sisyphus/evidence/task-15-reviewer-matrix.md

  Scenario: Reject overclaimed resolution
    Tool: Read
    Preconditions: Completion matrix drafted
    Steps:
      1. Inspect any item with partial or excluded resolution.
      2. Confirm the matrix states the limitation honestly.
    Expected Result: Verification is precise and non-misleading.
    Evidence: .sisyphus/evidence/task-15-honesty-check.md
  ```

  **Commit**: NO

- [x] 16. Produce final evidence summary for completed vs excluded direct-fix items

  **What to do**:
  - Write a concise evidence summary that separates completed direct fixes from excluded external-source-only items and any deferred bibliography cases.
  - Keep the summary operational: reviewer index, file path, action taken, and residual status.
  - Save the summary in `.sisyphus/evidence/` so later reporting does not depend on memory.

  **Must NOT do**:
  - Do not write speculative justifications for exclusions.
  - Do not hide partial completion behind generic wording.

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: this is a structured evidence document for user-facing traceability.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `internal-comms`: wrong template domain; a plain technical evidence note is sufficient.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 4 (with Tasks 15, 17 where dependencies permit)
  - **Blocks**: 17
  - **Blocked By**: 5, 12, 13, 15

  **References**:
  - `.sisyphus/evidence/blind-review-direct-fixes-exclusions.md` - explicit exclusion source.
  - `.sisyphus/evidence/task-15-reviewer-matrix.md` - reviewer-item completion matrix.
  - Git diff and residual evidence files from Tasks 6–14 - source material for final summary.

  **Acceptance Criteria**:
  - [ ] Evidence summary cleanly separates completed, excluded, and deferred items.
  - [ ] Every exclusion has a file/path-based reason.
  - [ ] The summary is sufficient for user briefing and future audit.

  **QA Scenarios**:
  ```
  Scenario: Write final evidence summary
    Tool: Read
    Preconditions: Task 15 completion matrix available
    Steps:
      1. Draft the final summary from the completion matrix and exclusion note.
      2. Verify every summary row references a concrete evidence source.
    Expected Result: A compact but audit-ready final evidence summary exists.
    Failure Indicators: Summary rows lack traceable evidence anchors.
    Evidence: .sisyphus/evidence/task-16-final-summary.md

  Scenario: Confirm exclusions are visible
    Tool: Read
    Preconditions: Summary drafted
    Steps:
      1. Inspect the summary for a distinct excluded/deferred section.
      2. Confirm no excluded item is presented as resolved.
    Expected Result: Limitations remain explicit.
    Evidence: .sisyphus/evidence/task-16-exclusion-visibility.md
  ```

  **Commit**: NO

- [x] 17. Reviewer-style final read of the bounded direct-fix pass

  **What to do**:
  - Perform a final holistic read as if checking whether the direct-fix subset now looks cleaner, more规范, and internally consistent to a blind reviewer.
  - Focus on whether the repaired issues are genuinely reduced from the reviewer’s perspective, not only technically patched in source.
  - Flag any remaining sharp edges that still belong to the direct-fix subset.

  **Must NOT do**:
  - Do not reopen out-of-scope scientific debates.
  - Do not invent new work categories beyond the already bounded direct-fix set.

  **Recommended Agent Profile**:
  - **Category**: `oracle`
    - Reason: a reviewer-style synthesis benefits from high-level judgment on whether the bounded pass actually improved the manuscript.
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing`: the need is judgment and synthesis, not editing.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 4 (with Tasks 15 and 16 where dependencies permit)
  - **Blocks**: F1, F2, F3, F4
  - **Blocked By**: 13, 14, 15, 16

  **References**:
  - `blind-review-comments.md` - original reviewer complaints and direct-fix subset.
  - `.sisyphus/evidence/task-15-reviewer-matrix.md` - issue completion mapping.
  - `.sisyphus/evidence/task-16-final-summary.md` - concise completed/excluded/deferred summary.
  - Compiled blind-review PDF from Task 13 - final reviewer-facing artifact.

  **Acceptance Criteria**:
  - [ ] Final read produces a clear verdict on the bounded direct-fix pass.
  - [ ] Any remaining direct-fix sharp edges are explicitly identified.
  - [ ] The verdict is usable as the final gateway before the four-agent verification wave.

  **QA Scenarios**:
  ```
  Scenario: Perform reviewer-style bounded-pass read
    Tool: Read
    Preconditions: Compile-stable manuscript and evidence summary available
    Steps:
      1. Review the changed regions and evidence summary as a blind-reviewer would.
      2. Judge whether direct-fix complaints now look materially reduced.
    Expected Result: A concise high-level verdict exists.
    Failure Indicators: Final read cannot explain whether the bounded pass actually improved reviewer-visible quality.
    Evidence: .sisyphus/evidence/task-17-reviewer-verdict.md

  Scenario: Identify remaining direct-fix sharp edges
    Tool: Read
    Preconditions: Reviewer-style read complete
    Steps:
      1. Note any still-visible issue that belongs to the direct-fix subset.
      2. Confirm it is either excluded, deferred, or genuinely remaining work.
    Expected Result: No hidden residual direct-fix issues remain unclassified.
    Evidence: .sisyphus/evidence/task-17-remaining-edges.md
  ```

  **Commit**: NO

## Final Verification Wave

> 4 review agents run in parallel after all implementation tasks complete. All must approve before the work is considered complete.

- [x] F1. **Plan Compliance Audit** — `oracle`
  - Read this plan and verify every in-scope direct-fix item has a corresponding implementation outcome or documented exclusion.
  - Verify no forbidden directories/files were edited.
  - Output: `In-scope direct fixes [N/N] | Forbidden edits [0/N] | VERDICT`

- [x] F2. **Content/Format Quality Review** — `unspecified-high`
  - Run `latexmk` and inspect touched files for formatting regressions, broken refs/citations, caption issues, and awkward first-person rewrites.
  - Output: `Build [PASS/FAIL] | Refs [PASS/FAIL] | Formatting [PASS/FAIL] | VERDICT`

- [x] F3. **Real QA Execution** — `unspecified-high`
  - Execute all grep/read/compile/PDF checks defined in the tasks and confirm evidence files exist.
  - Output: `Checks [N/N pass] | Evidence [present/missing] | VERDICT`

- [x] F4. **Scope Fidelity Check** — `deep`
  - Compare the actual diff against this plan and flag any work outside the direct-fix subset.
  - Output: `Scope [clean/issues] | Exclusions [respected/violated] | VERDICT`

---

## Commit Strategy

- Group 1: prose/heading direct-fix edits
- Group 2: bibliography normalization
- Group 3: layout/figure/caption direct-fix edits
- Group 4: evidence note / final cleanup if needed

---

## Success Criteria

### Verification Commands
```bash
latexmk
# Expected: successful blind-review build with no undefined references/citations in the log
```

### Final Checklist
- [x] All in-scope direct-fix items are either implemented or explicitly excluded with evidence
- [x] No forbidden backup/config/preview files were edited
- [x] No unresolved reviewer-flagged empty caption, first-person, or targeted title-punctuation issue remains in active files
- [x] Bounded bibliography fixes are complete
- [x] Blind-review build succeeds
