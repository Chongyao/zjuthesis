# Task 13 Fallout Scope Check

## Trigger
A full blind-review `latexmk` run initially failed before PDF completion. The fatal error occurred in `body/graduate/intro/1_background.tex` inside the TikZ figure under the introduction background section.

## Root Cause
The failure was a direct-fix fallout issue in an already touched file:
- `body/graduate/intro/1_background.tex`
- Missing comma between two TikZ style definitions:
  - `basisBox/.style={...}`
  - `flowArrow/.style={...}`

Without that comma, the subsequent `\node[basisBox]` line triggered `! Missing \endcsname inserted.`

## Remediation Scope
The remediation was kept strictly local to direct-fix consequences.

### Actual edit made
- Restored one trailing comma in `body/graduate/intro/1_background.tex`.

### Explicit non-actions
- No scientific content was changed.
- No bibliography entries were changed.
- No excluded files or external assets were touched.
- No unrelated cleanup was performed.

## Post-fix Verification
- `latexmk` completed successfully in blind-review mode and produced `out/zjuthesis.pdf`.
- Inspection of `out/zjuthesis.log` found no undefined references or undefined citations introduced by the direct-fix tasks.
- Workspace-level LaTeX diagnostics did not reveal build-blocking errors in thesis sources after the repair.

## Remaining Warning Outside Scope
A non-blocking `U+2010` missing-character warning is still reported from `body/graduate/post/ref.tex` processing. It did not break the build and was not caused by the direct-fix fallout repaired here, so it was left unchanged under the task scope guardrail.
