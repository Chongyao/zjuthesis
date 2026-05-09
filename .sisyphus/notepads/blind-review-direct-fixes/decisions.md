# Decisions - blind-review-direct-fixes

## Task 4: Bibliography Scope Audit (2026-05-09)

### Entry Numbering Convention
- DECIDED: Reviewer's literature numbers include the 4 template @www entries at the top of ref.bib.
- Verified by matching "文献15无页码" → Jabbari2022AdaptiveRefinement which has no `pages` field.

### Scope Bounding
- DECIDED: Only 5 reviewer-flagged entries + directly adjacent entries (±3 positions) showing the same defect patterns are in scope.
- DECIDED: ~17 entries are directly fixable (format normalization + publisher additions + artifact cleanup).
- DECIDED: ~10 entries are deferred — need external page/venue lookup that cannot be done from local evidence.

### Deferred Entries
- DECIDED: Missing pages for Jabbari2022AdaptiveRefinement, huang2025stiffgipc, Kressner2024AnalysisOfeigenvalue deferred — need external DOI lookup.
- DECIDED: gantmakher2000theory (book) deferred — pagination depends on in-text citation context.
- DECIDED: 2007ComponentMS, karl2024ShiftInvertArnoldi, hetmaniuk2014error deferred — require complete reconstruction or removal.

### Fixable Patterns
- DECIDED: @ARTICLE → @article normalization is cosmetic and safe — 4 entries affected (servin2008rigid, spillmann2008cosseratnet, kim2012physics, RH2005EliminateSlivers).
- DECIDED: Export artifacts (urldate, file fields with local paths) should be removed — 8 entries affected.
- DECIDED: Missing publisher/journal fields can be added where ISSN provides unambiguous identification (e.g., HuangRS2011 missing journal, ISSN 1077-2626 → IEEE TVCG).

### Out of Scope
- DECIDED: Full 2360-line bibliography rewrite is OUT OF SCOPE — only flagged + adjacent entries.
- DECIDED: Journal-name italicization and book-name formatting are biblatex style issues, not bib data issues — out of scope for bib audit.
- DECIDED: Citation infrastructure (config/format/general/reference.tex) is NOT modified.
- DECIDED: Entry key rename (Dasgupta2003 → Martin2008Polyhedral) noted but left for Task 10 to coordinate with .tex reference updates.

## Task 10: Bounded bibliography normalization applied (2026-05-10)

- DECIDED: Applied only evidence-backed local repairs in `body/ref.bib`: entry-type case normalization, clearly supportable publisher/journal additions, and export-artifact cleanup.
- DECIDED: Kept deferred entries unchanged when a fix would require external verification or citation-context review (`Jabbari2022AdaptiveRefinement`, `huang2025stiffgipc`, `gantmakher2000theory`, `Kressner2024AnalysisOfeigenvalue`, `hetmaniuk2014error`, conference records with empty pages, and `ni_numerical_2023` page semantics).
- DECIDED: Treated `chen2021multiscale` publisher addition as bounded and supportable because the entry already cites ICCV explicitly as an IEEE/CVF proceedings venue.
- DECIDED: Accepted existing non-biblatex warnings from the project-wide build as pre-existing/out-of-scope because the bibliography edit introduced no new TeX diagnostics and `latexmk` completed successfully.

- DECIDED: Verification found two accidental duplicate-field insertions during editing (`giammatteo2024extension`, `hetmaniuk2010special`) and one duplicate journal line in `HuangRS2011`; these were cleaned before final verification.
