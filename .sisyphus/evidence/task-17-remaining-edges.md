# Task 17 Remaining Direct-Fix-Scope Edges

Date: 2026-05-10  
Plan: `blind-review-direct-fixes`

Only unresolved items that still belong to the original direct-fix subset are listed here. Each row is classified as **excluded**, **deferred**, or **future-work** to prevent overclaim.

## Remaining edges

### 1. Figure/table text sizing and plot-internal formatting (`一.1`, `五.1`)
- **Classification:** excluded
- **Why unresolved:** the dominant remaining issues are **EXT** items embedded inside externally generated PDF/PNG assets, including axis/tick fonts, labels, units, legend placement, missing colorbars, and similar plot-internal formatting.
- **Evidence:** `blind-review-direct-fixes-exclusions.md`, `task-5-figure-triage.md`, `task-15-reviewer-matrix.md`
- **Bound:** not fixable by TeX-only edits in this pass.

### 2. Thesis-wide whitespace cleanup (`一.5`)
- **Classification:** future-work
- **Why unresolved:** evidence supports local float/reference-neighborhood tightening, but not a complete thesis-wide closure for all reviewer-observed whitespace / leave-blank locations.
- **Evidence:** `task-15-reviewer-matrix.md`, `task-15-honesty-check.md`
- **Bound:** do not describe as fully fixed beyond the documented local FLT adjustments.

### 3. Basis-function symbol font consistency (`二.1`)
- **Classification:** deferred
- **Why unresolved:** this was triaged as source-fixable in principle, but the current evidence package does not contain a dedicated closure artifact proving complete normalization.
- **Evidence:** `task-5-figure-triage.md`, `task-16-final-summary.md`, `task-15-honesty-check.md`
- **Bound:** unresolved due to missing closure evidence, not because the item is outside repo control.

### 4. Bibliography completeness and standardization (`二.6`, `五.6`)
- **Classification:** deferred
- **Why unresolved:** the bibliography pass was intentionally bounded; entries needing externally verified pages, venue metadata, type confirmation, or missing core fields remain open by design.
- **Evidence:** `task-4-bib-scope.md`, `task-4-bib-guardrails.md`, `task-15-reviewer-matrix.md`
- **Bound:** explicitly includes bounded bib deferrals such as missing page ranges and not-yet-verifiable venue details.

### 5. Figure/table proximity beyond the documented intro fix (`四.1`)
- **Classification:** future-work
- **Why unresolved:** the evidence proves at least one real repo-local proximity fix, but does not prove that every non-nearby figure/table case across the thesis was resolved.
- **Evidence:** `task-15-reviewer-matrix.md`, `blind-review-direct-fixes-exclusions.md`
- **Bound:** only the documented intro organization figure neighborhood should be claimed fixed.

## Explicit non-edges

The following should **not** be listed as remaining direct-fix edges in reviewer-facing summaries:
- **三.2** high-priority third-person narration cleanup — evidenced as completed in active prose.
- **三.3** targeted active heading-colon cleanup — evidenced as completed in active scope.
- **二.2** intro figure-reference-order fix — evidenced as completed in the narrow documented sense.

## Closure rule

Any future claim stronger than this file must first remove the **EXT exclusions** through asset regeneration and clear the **bounded bibliography deferrals** through verified metadata updates.
