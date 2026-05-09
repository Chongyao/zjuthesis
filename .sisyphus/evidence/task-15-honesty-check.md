# Task 15 Honesty Check

Date: 2026-05-10  
Plan: `blind-review-direct-fixes`

## Purpose

This note records the explicit limitations of the Task 15 reviewer-facing verification so the evidence package does not overstate what the direct-fix pass actually completed.

## No overclaim

### 1. Items that must **not** be described as fully fixed

- **一.1** — figure/table text sizing is only partially addressed; the dominant plot-internal typography issues are still external-asset work. Evidence: [`blind-review-direct-fixes-exclusions.md`](blind-review-direct-fixes-exclusions.md).
- **一.5** — local float-neighborhood improvement exists, but no artifact proves a comprehensive whitespace cleanup across all reviewer-observed locations. Evidence: [`blind-review-direct-fixes-exclusions.md`](blind-review-direct-fixes-exclusions.md).
- **二.1** — source-fixable in principle, but the task-1..14 evidence set does not contain a dedicated closure artifact proving the symbol-font consistency work is complete. Evidence: [`task-5-figure-triage.md`](task-5-figure-triage.md).
- **二.6 / 五.6** — bibliography normalization is bounded and partially deferred; missing pages / venue metadata needing external verification remain open by design. Evidence: [`task-4-bib-scope.md`](task-4-bib-scope.md).
- **四.1** — at least one local figure-reference proximity fix is documented, but the evidence base does not justify a blanket “all proximity issues fixed” statement. Evidence: [`blind-review-direct-fixes-exclusions.md`](blind-review-direct-fixes-exclusions.md), [`task-5-figure-triage.md`](task-5-figure-triage.md).
- **五.1** — many sub-issues are EXT and excluded, especially axis labels, units, legends, colorbars, and tiny plot fonts inside rendered paper1/paper3 assets. Evidence: [`task-5-exclusion-inputs.md`](task-5-exclusion-inputs.md), [`blind-review-direct-fixes-exclusions.md`](blind-review-direct-fixes-exclusions.md).

### 2. Items that can be claimed as fixed, but with caveats stated

- **三.2** can be claimed fixed for the **high-priority authorial narration target**, because Task 14 shows only low-priority residual caption/technical uses of `我们` in active files. Evidence: [`task-14-residual-matrix.md`](task-14-residual-matrix.md).
- **三.3** can be claimed fixed for the **targeted active heading-colon issue**, because residual full-width-colon title hits are backup-only. Evidence: [`task-14-residual-matrix.md`](task-14-residual-matrix.md).
- **二.2** can be claimed fixed only in the narrower sense documented by the evidence package: the intro organization figure neighborhood / reference order issue was handled in-source. Evidence: [`task-3-empty-caption-hotspots.md`](task-3-empty-caption-hotspots.md), [`blind-review-direct-fixes-exclusions.md`](blind-review-direct-fixes-exclusions.md).

## Caveats by evidence quality

| Area | Evidence quality | Caveat |
|---|---|---|
| First-person cleanup | Strong | Residual low-priority `我们` uses remain in captions/technical phrasing; do not describe as zero occurrences everywhere. |
| Title punctuation cleanup | Strong | Verified only for targeted heading commands in active scope, not for all punctuation usage in running text or backup trees. |
| Bibliography cleanup | Medium | The bounded pass clearly happened, but deferred entries are part of the intended outcome; “fully standardized bibliography” would be false. |
| Figure-format cleanup | Medium-to-weak for closure | The strongest evidence is actually exclusion evidence; that supports honesty, not a claim of full repair. |
| Float / whitespace cleanup | Weak-to-medium | There is evidence of local fixes, but not a complete thesis-wide before/after matrix. |

## Verification basis used here

- Direct-fix subset definition: [`../../blind-review-comments.md`](../../blind-review-comments.md)
- Scope guardrails: [`task-1-build-surface.md`](task-1-build-surface.md), [`task-1-exclusions.md`](task-1-exclusions.md), [`task-14-scope-drift.md`](task-14-scope-drift.md)
- Completion / residual evidence: [`task-13-fallout-scope.md`](task-13-fallout-scope.md), [`task-14-residual-matrix.md`](task-14-residual-matrix.md)
- Reviewer-item-specific evidence: [`task-2-first-person-inventory.md`](task-2-first-person-inventory.md), [`task-3-title-hotspots.md`](task-3-title-hotspots.md), [`task-3-empty-caption-hotspots.md`](task-3-empty-caption-hotspots.md), [`task-4-bib-scope.md`](task-4-bib-scope.md), [`task-5-figure-triage.md`](task-5-figure-triage.md), [`task-5-exclusion-inputs.md`](task-5-exclusion-inputs.md), [`blind-review-direct-fixes-exclusions.md`](blind-review-direct-fixes-exclusions.md)

## Bottom line

The direct-fix pass has credible evidence for several real in-repo improvements, but the honest reviewer-facing position is **mixed closure**: some items are fixed, some are partial, some are explicitly excluded as EXT, and some bibliography / notation issues remain deferred because the evidence package itself says they do.
