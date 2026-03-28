# ZJUTHESIS KNOWLEDGE BASE

**Generated:** 2026-03-28
**Commit:** efbd378
**Branch:** zcy

## OVERVIEW
Zhejiang University PhD thesis LaTeX template. Contains 3 research papers + intro + conclusion. Uses ctexrep class with XeLaTeX.

## STRUCTURE
```
zjuthesis/
├── zjuthesis.tex          # Main entry, documentclass options
├── zjuthesis.cls          # Class definition, key-value options
├── config/                # Packages, macros, formatting
│   ├── paper1_macros.tex  # Custom math operators (Cosserat)
│   ├── paper3_macros.tex  # Custom macros (Primal-Dual)
├── body/graduate/         # PhD thesis content
│   ├── content.tex        # Chapter input order
│   ├── intro/             # Introduction chapter
│   ├── paper1/            # Paper 1: Cosserat Rod Simulation
│   ├── paper2/            # Paper 2
│   ├── paper3/            # Paper 3: Primal-Dual Modes
│   └── conclusion.tex     # Summary & outlook
├── figure/                # Shared figures
├── page/graduate/         # Cover, TOC, abstract pages
└── out/                   # Build output (gitignored)
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Add new chapter | `body/graduate/content.tex` | Add `\inputbody{new/main}` |
| Configure thesis info | `zjuthesis.tex` | Documentclass options: Degree, GradLevel, Title, etc. |
| Custom math macros | `config/paper*_macros.tex` | Add to existing or create new |
| Fix formatting | `config/format/general/` | fonts.tex, layout.tex, geometry.tex |
| Add figures | `body/graduate/paper*/figures/` | Use `\inputbody{paper*/main}` path |
| References | `body/ref.bib` | Biblatex with gb7714-2015 style |

## CONVENTIONS
- `\inputbody{path}` — includes from `body/graduate/path.tex`
- `\inputpage{file}` — includes from `page/graduate/file.tex`
- Compile with `latexmk` only — ensures references resolve
- Output to `out/` directory
- Each paper has own `figures/` subdirectory with `\graphicspath`

## ANTI-PATTERNS (THIS PROJECT)
- **NEVER** use `xelatex` alone — references won't compile; use `latexmk`
- **NEVER** delete `.latexmkrc` on Overleaf without replacing build config
- **NEVER** skip paper migration translation rules in `.sisyphus/plans/`
- **NEVER** use `\DET` macro directly — conflict exists; use `\DETtext` (paper1) or `\DET{arg}` (paper3)
- **NEVER** modify `zjuthesis.cls` core options without updating `config/commands.tex` paths
- **NEVER** use `algorithm2e` package — use `algorithm` + `algorithmic` syntax (`\IF{}...\ENDIF`, `\COMMENT{}`, `\RETURN`)
- **NEVER** skip any mathematical derivation when translating papers (per .sisyphus/plans)
- **NEVER** use one-sentence summaries for paper content (migrate_paper*.md explicit rule)
- **NEVER** use empty `[]` as figure placement — use `[tbp]` or `[H]`
- **NEVER** place major-specific packages in `config/packages.tex` — use major's local `packages.tex`

## UNIQUE STYLES
- TikZ-based matrix operators: `\LowerTri`, `\UpperTri`, `\Diag`, `\TriDiag` (paper1)
- Custom partial derivative: `\FPP{f}{x}` (paper3), `\FPPmathbf{J}{q}` (paper1)
- Macro collision handled via renamed `\DETtext` vs `\DET`

## COMMANDS
```bash
# Build thesis (recommended)
latexmk

# Alternative: explicit xelatex + biber
latexmk -xelatex -outdir=out zjuthesis

# Clean build artifacts
latexmk -c

# Word count (after one build)
script/utils/word_count.sh
```

## NOTES
- TeXLive 2019+ required for Chinese font handling (no copy乱码)
- Each paper dir has AGENTS.md with paper-specific details
- `.sisyphus/plans/` contains migration plans for paper1 and paper3