# Learnings - blind-review-direct-fixes

## Task 1: Build Surface & Exclusions (2026-05-09)

### Active Build Surface
- 5 chapters active: intro, paper1–paper3, conclusion
- `BlindReview = true` is the active build mode (zjuthesis.tex:36)
- Latexmk is the only supported build command (avoids ref resolution issues)
- Each paper has its own `main.tex` that inputs sub-section files via `\inputbody{}`

### Key Exclusions Discovered
- **paper2/2_related.tex is COMMENTED OUT** in `paper2/main.tex:6`. It exists on disk but does not participate in the build. This is important — any changes there would have zero effect on the output PDF.
- **paper1_backup/** is a full backup directory with its own `main.tex` containing additional commented-out inputs (jacobian_pattern, preconditioner). Must ignore entirely.
- **paper1/4_results_tikz_preview.tex** is a standalone preview file with its own `\documentclass`. It is NOT referenced from any active `\inputbody` chain.

### Build Architecture Pattern
- `zjuthesis.tex` → `\inputgraduate{}` → `\inputbody{content}` → `content.tex` → chapters
- `\inputbody{x}` resolves to `body/graduate/x.tex`
- `\inputpage{x}` resolves to `page/graduate/x.tex`
- Page-level inputs (cover, previous, toc, post) are included OUTSIDE the chapter loop

### Verification Technique
- Grep for `^%\\inputbody` to find commented-out sections
- Grep for `\\documentclass` to find standalone preview files in the body tree
- Always cross-reference active `\inputbody` directives against physical file existence

---

## Task 3: Heading/Caption/Reference-Placement Hotspots (2026-05-09)

### Empty Short-Caption Hotspots
- **2 hotspots confirmed** in active intro files (none in paper2)
- `intro/1_background.tex:40`: `\caption[]{数值模拟过程与网格离散示意图}` — source-fixable
- `intro/3_contributions_and_organization.tex:121`: `\caption[]{论文组织结构示意图}` — source-fixable
- Both are pure source-level fixes; no float-reflow risk from caption text change alone
- Nearby `\Cref` flow: `1_background.tex` has forward reference (line 6 `\Cref` before figure at line 42), but uses idiomatic "如\Cref{...}所示" pattern — acceptable

### Title Punctuation Hotspots
- **4 active-title hotspots** with `：` colon across 2 files
- `paper2/main.tex:3`: chapter-level title with colon — **highest priority** (appears in TOC + page header; needs post-fix layout verification)
- `intro/2_related_and_problems.tex` lines 5, 67, 81: three subsection-level titles with colon — source-fixable, low layout risk
- All colons are in source text, NOT injected by heading config (`config/format/general/heading.tex`)
- **1 low-priority observation**: `paper3/4_results.tex:48` `\paragraph` with colon — not classified as hotspot (inline `\paragraph` titles accept natural colon usage)

### Key Insight: Config vs Source
- `heading.tex` controls numbering format, skips, and font sizes only
- No colon-insertion logic exists — all `：` characters originate in source text
- This means **source-local fixes are the correct approach**; no config-level changes warranted

### Reference Flow Pattern
- All 7 `\Cref` usages in intro files have natural figure-adjacent flow
- Forward references (2 cases) use standard Chinese academic idiom "如\Cref{...}所示"
- No broken or confusing `\Cref` reference-placement issues identified

### Evidence Files Produced
- `.sisyphus/evidence/task-3-empty-caption-hotspots.md` — 2 hotspots + `\Cref` flow matrix
- `.sisyphus/evidence/task-3-title-hotspots.md` — 4 hotspots + 1 observation + exclusions

---

## Task 2: First-Person Inventory (2026-05-09)

### Active Surface Coverage
- 20 active .tex files searched across 5 chapters (intro, paper1-3, conclusion)
- Paper 1 is CLEAN (0 hits) — prior migration successfully rewrote first-person to '本文'/passive
- Conclusion is CLEAN (0 hits) — already uses '本文' consistently
- Intro, Paper 2, Paper 3 account for all 73 occurrences

### Distribution Pattern
| Chapter | Hits | Rewrite Burden |
|---------|------|----------------|
| Intro | 5 | Low |
| Paper 1 | 0 | None (gold standard) |
| Paper 2 | 29 | High |
| Paper 3 | 39 | High |
| Conclusion | 0 | None |

### Classification Heuristics Established
- **A (Authorial narration)**: "我们提出...", "我们使用...", "我们的方法..." → must rewrite to '本文'/passive
- **T (Technical/math reasoning)**: "不失一般性，我们假设..." → borderline, weaker violation
- **C (Caption)**: `\caption[...]{...我们...}` → lowest priority, depends on style guide
- ~85% of hits are class A (authorial), requiring '本文' substitution or passive reconstruction

### Rewrite Priority Matrix
- HIGH priority (~55 hits): narrator-voice actions (我们提出/实现/开发/采用/使用/设计/展示/模拟)
- MEDIUM priority (~8 hits): transitional phrases (下面我们将..., 我们首先考虑...)
- LOW priority (~10 hits): figure captions + mathematical derivations

### Key Insight: Paper 1 as Migration Template
- Paper 1 active prose has zero first-person — all original was rewritten during its migration
- Paper 2 and Paper 3 still carry original Chinese-draft first-person voice
- The backup directories preserve pre-migration state with ~200+ hits as reference

### Evidence Files Produced
- .sisyphus/evidence/task-2-first-person-inventory.md — complete 73-hit inventory
- .sisyphus/evidence/task-2-scope-check.md — active graph verification, exclusion list

## Task 5: Figure-Format Fixability Triage (2026-05-09)

### Figure Number Verification
- Figure numbering is strictly LaTeX auto-counter per chapter. Verified by counting all `\begin{figure}...\end{figure}` environments in chapter include order.
- Chapter-to-figure mapping:
  - Ch1 (intro): 图1.1–1.9 (1_background → 2_related → 3_contributions)
  - Ch2 (paper1): 图2.1–2.16 (3_simulation → preconditioner_content → 4_results)
  - Ch3 (paper2): 图3.1+
  - Ch4 (paper3): 图4.1–4.21 (2_foundation → 2_representation → 3_simulation → 4_results)

### Fixability Patterns
- **Pure TikZ (TEX)**: intro 图1.1, 图1.9; paper2 algorithmic figures; paper1 hybrid TikZ overlays. Font sizes, colors, positioning all controllable.
- **Hybrid TikZ+Image (TEX for text layer only)**: paper1 图2.5 and 图2.11. TikZ `\node` text overlays on external render.png. Overlay text is fixable; background image is not.
- **Pure external PDF/PNG (EXT)**: All paper1 result figures (Ch2) and paper3 result figures (Ch4). Generated by C++ sim output (paper1, scripts absent) or Python/matplotlib (paper3, scripts present).
- **Float placement (FLT)**: 图1.9 placement, table-figure proximity, general float ordering.

### Key Discovery: PDF+LaTeX Overlay
- `body/graduate/paper3/figures/matrix_structure.pdf_tex` (图4.8) uses Inkscape's PDF+LaTeX export mechanism. Similar to psfrag but not technically psfrag. The LaTeX portion is source-fixable.
- No actual `\psfrag` commands found anywhere in the codebase.

### Preconditioner Content Inclusion
- `preconditioner_content.tex` is `\inputbody`'d at line 299 of `paper1/3_simulation.tex`. Its 3 figures become 图2.2, 图2.3, 图2.4 — between fig:single-chain (图2.1) and 4_results section (图2.5+).
- This was initially missed when scanning only 4_results.tex. The background agent's chapter-level figure count caught this.

### Standalone Preview Exclusion
- `paper1/4_results_tikz_preview.tex` exists as a standalone development preview. NOT included in thesis build. Per plan guardrails, excluded from edits.


## Task 6: Third-person normalization rewrites (2026-05-09)

- Rewrote active-body authorial narration from  to objective forms ( / impersonal declaratives) across intro, paper2, and paper3 active files.
- Preserved equations, symbols, claims, and experimental numbers; edits were local sentence-level voice changes only.
- For technical derivation phrases, used natural impersonal rewrites (e.g., ).
- Explicitly handled previously truncated long-line contexts in  around the former ~125 and ~139-line hits by converting remaining authorial phrasing to objective narration.
- Residual  after rewrite is caption-only in scoped paper2/paper3 files; no remaining authorial body narration hits in target files.


## Task 6: Third-person normalization rewrites (2026-05-09)

- Rewrote active-body authorial narration from first-person to objective forms (本文 / impersonal declaratives) across intro, paper2, and paper3 active files.
- Preserved equations, symbols, claims, and experimental numbers; edits were local sentence-level voice changes only.
- For technical derivation phrases, used natural impersonal rewrites (e.g., 不失一般性，可假设...).
- Explicitly handled previously truncated long-line contexts in paper3/3_simulation.tex around the former ~125 and ~139-line hits by converting authorial phrasing to objective narration.
- Residual 我们 after rewrite is caption-only in scoped paper2/paper3 files; no remaining authorial body narration hits in target files.

## Task 7: Heading Punctuation Normalization (2026-05-09)

### Changes Applied
- **T1** (`paper2/main.tex:3`): Replaced `：` → `——` in chapter title `有限元方法中病态网格单元的处理——局部基空间重构与隔离`. Em-dash chosen over whitespace to preserve the problem-domain/solution-approach semantic separator.
- **T2** (`intro/2_related_and_problems.tex:5`): Replaced `：` → `——` in `\subsection{物理量的离散表达——基函数}`.
- **T3** (`intro/2_related_and_problems.tex:67`): Replaced `：` → `——` in `\subsection{缓解病态性的代数路线——预处理技术}`.
- **T4** (`intro/2_related_and_problems.tex:81`): Replaced `：` → `——` in `\subsection{缓解病态性的表征路线——基函数变换与能量景观重塑}`.

### Key Decisions
- **Em-dash (`——`) chosen over whitespace**: In all four titles, the colon separates a broader category from a specific focus (e.g. "problem domain：solution approach"). A whitespace replacement would obscure the semantic structure. Two-em-dash preserves the conceptual separation while satisfying punctuation normalization.
- **T5 (`paper3/4_results.tex:48`) intentionally skipped**: `\paragraph` headings are run-in per ctexrep default. Per Task 3 evidence, colons in inline paragraph titles function as natural body-text punctuation and are not classified as hotspots. No config changes made (`heading.tex` confirmed not to inject colons).

### Verification
- Residual grep `\\(chapter|section|subsection|subsubsection)\{[^}]*：[^}]*\}` across `body/graduate/` returns **zero active-file hits**.
- Two remaining `：` hits exist only in `paper2_backup/` and `paper3_backup/` — excluded per evidence.
- No config files modified; all changes source-local.

## Task 8: Intro Short Caption Repair (2026-05-09)

### Changes Applied
- **H1** (`intro/1_background.tex:40`): `\caption[]{数值模拟过程与网格离散示意图}` → `\caption[数值模拟过程与网格离散]{数值模拟过程与网格离散示意图}`. Short caption drops "示意图" suffix — the "Figure" prefix from the ToC/side-caption context makes "示意图" redundant.
- **H2** (`intro/3_contributions_and_organization.tex:121`): `\caption[]{论文组织结构示意图}` → `\caption[论文组织结构]{论文组织结构示意图}`. Short caption drops "示意图" suffix, same reasoning.

### Key Decisions
- Short-caption text derived from long caption by removing "示意图" (schematic/diagram suffix). This preserves the core noun phrase while avoiding redundant "figure diagram" in LoF/toc context.
- Figure labels, `\Cref` flow, and paragraph semantics unchanged. Pure caption-text-only edits.

### Verification
- Residual grep `\\caption\\[\\]\\{` across `body/graduate/intro/` returns zero matches.
- Both forward (`1_background.tex:6`) and backward (`3_contributions_and_organization.tex:125`) `\Cref` references remain coherent with caption text.

## Task 10: Bounded bibliography normalization (2026-05-10)

- Safe bib-only fixes in this repo fall into three low-risk buckets: cosmetic entry-type/field-name normalization, removal of Zotero/Mendeley export artifacts (`urldate`, local `file` paths), and metadata additions that are directly supported by existing venue/ISSN evidence already present in the entry.
- Bounded bib edits are easy to corrupt when replacing overlapping ranges; re-reading after each edit batch is essential because duplicate field insertions can happen silently if a later replacement targets stale line IDs.
- `latexmk` is a practical verification step for bibliography-only work: it confirms that the edited `.bib` remains parseable and that no new bib errors were introduced, while unrelated project-wide font/overfull warnings should be treated separately.


## Task 12: Exclusion-evidence closure (2026-05-10)

- Completed the missing Task 12 closure artifact by creating `.sisyphus/evidence/blind-review-direct-fixes-exclusions.md` from the Task 5 exclusion inputs and current repo state, explicitly separating deferred EXT issues from already-addressed repo-local TEX/FLT fixes. The key pattern is that paper3 external plots are often regenerable in principle because scripts and, in several cases, supporting data are checked in, whereas paper1 external plot assets remain largely opaque because only rendered PDFs/PNGs are present in this repo; this distinction should be stated clearly in final evidence rather than flattening all exclusions into a single generic reason.

## Task 13: Blind-review latexmk fallout check (2026-05-10)
- Full latexmk blind-review build succeeded after a one-line fallout repair in body/graduate/intro/1_background.tex (restored the missing comma between TikZ style definitions).
- Final log inspection found no undefined references or citations introduced by the direct-fix tasks; the remaining U+2010 missing-character warning comes from body/graduate/post/ref.tex and is outside this task scope.


## Task 15: Reviewer-facing closure matrix (2026-05-10)

- The safest final-review pattern is to map each direct-fix reviewer item to one of four states—fixed, partial, deferred, excluded—and require every non-fixed claim to cite the exact evidence artifact that justifies the limitation; this prevents accidental overclaim, especially for EXT figure issues and bounded bibliography repairs.

## Task 16: Final evidence consolidation (2026-05-10)
- Consolidating reviewer-facing evidence works best when summary tables are split into completed / partial / deferred / excluded buckets and each row carries direct artifact links; this preserves transparency and prevents drift between matrix claims and exclusion notes.

## Task 17: Reviewer-style final read (2026-05-10)
- Final reviewer-facing verdicts for bounded cleanup work should default to `APPROVE_WITH_LIMITATIONS` whenever the evidence shows real source-level closure but also explicit EXT exclusions or bounded bibliography deferrals; this keeps the pass honest without discarding completed in-repo fixes.

## Task F4: Scope fidelity audit (2026-05-10)
- The most reliable scope-cleanliness signal is the intersection of three artifacts: raw changed-file list (`git diff --name-only`), Task 14 scope-drift evidence, and Task 15/16 honesty matrices. When all three agree, scope verdicts can cite concrete path-level proof instead of relying on a subjective summary.
- `blind-review-comments.md` is outside thesis source but still scope-consistent here because it is the reviewer-scope ledger used by the plan and evidence package; it does not violate the forbidden-path policy.
- For this plan, EXT exclusions should be treated as positive evidence of boundedness, not as incomplete hiding: if external plot issues remain explicitly listed in the exclusion artifact and are not mislabeled fixed in Task 15/16, the exclusion policy is being respected.

## Task F4: Scope fidelity re-evaluation (2026-05-10)
- When the orchestrator clarifies an allowlist, F4 should apply the plan guardrails literally: path-level scope cleanliness depends on forbidden-path avoidance, not on whether a touched allowed artifact is thesis prose versus supporting reviewer ledger.
- A failed explore delegate with no findings should not block a bounded audit when the needed repository evidence is already present locally and can answer the clarified rule directly.
