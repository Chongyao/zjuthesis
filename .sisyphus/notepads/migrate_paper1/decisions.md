# Migrate Paper 1 Decisions

## 2026-03-02

### Decision: Skip redundant bib entries
- All 44 entries from egbibsample.bib already present in body/ref.bib
- Decision: Do not append duplicates
- Rationale: Avoid bibtex compilation warnings for duplicate keys

### Decision: Copy all figs/ contents recursively
- Preserved subdirectory structure (collideTen/, conf_inext_slip/, etc.)
- Ensures figure paths in LaTeX remain valid


### Decision: Namespace conflicting \DET macro
- Paper 1: `\newcommand{\DET}{\text{det}}` (argument-less)
- Paper 3: `\newcommand{\DET}[1]{\operatorname{det}\left(#1\right)}` (takes argument)
- Decision: Renamed Paper 1's version to `\DETtext`
- Rationale: Different signatures, cannot coexist; `\DET` from Paper 3 is more flexible

### Decision: Skip identical macros
- `\DOT` and `\FPP` are identical between Paper 1 and Paper 3
- Decision: Only include in `paper1_macros.tex` if unique
- Rationale: Avoid redefinition warnings

## 2026-03-02: Macro Migration Decisions

### Decision: Rename conflicting \DET macro
- Paper 1's `\DET` defined as `\text{det}` (no arguments)
- Paper 3's `\DET` defined as `\operatorname{det}(#1)` (takes argument)
- Resolution: Renamed Paper 1 version to `\DETtext`
- Rationale: Paper 3's version is more functional (takes matrix argument)

### Decision: Skip identical macros
- `\DOT` and `\FPP` have identical definitions in both papers
- Skipped adding duplicates to avoid "already defined" errors

### Decision: Include TikZ-based operators
- `\LowerTri`, `\UpperTri`, `\Diag`, `\TriDiag` are visual matrix pattern operators
- These require TikZ package which is already included via paper3_macros.tex
- Added to paper1_macros.tex for matrix pattern illustrations


## 2026-03-02: Macro Migration Decisions

### Decision: Namespace \DET collision
- Paper 1's \DET (\text{det}, no args) conflicts with Paper 3's \DET[1] (\operatorname{det}(arg))
- Decision: Rename Paper 1 version to \DETtext
- Rationale: Paper 3's version is more flexible (takes argument), keep it as default \DET

### Decision: Skip identical macros
- \DOT and \FPP definitions identical in both papers
- Decision: Skip including in paper1_macros.tex (already available via paper3_macros.tex)
- Rationale: Avoid duplicate definition warnings

### Decision: Include TikZ operators
- \LowerTri, \UpperTri, \Diag, \TriDiag are TikZ-based visual macros
- Decision: Include all four in paper1_macros.tex
- Rationale: Used extensively in Paper 1's preconditioner.tex for matrix pattern visualization

## 2026-03-02: Macro Migration Decisions

### Decision: Namespace colliding macros
- Collision: `\DET` defined differently in Paper 1 (`\text{det}`) vs Paper 3 (`\operatorname{det}(#1)`)
- Decision: Rename Paper 1's version to `\DETtext`
- Rationale: Paper 3's version is more flexible (takes argument), Paper 1's is simpler
- Alternative considered: Could have used `\renewcommand` but namespacing is safer

### Decision: Skip identical macros
- `\DOT` and `\FPP` have identical definitions in both papers
- Decision: Do not include in `paper1_macros.tex`
- Rationale: Avoid duplicate definition warnings

### Decision: Include TikZ operators
- Added `\LowerTri`, `\UpperTri`, `\Diag`, `\TriDiag` from Paper 1
- Decision: Include complete TikZ definitions
- Rationale: These are visual matrix pattern indicators used in preconditioner.tex
- Dependency: Requires `\usepackage{tikz}` (already in paper3_macros.tex)
