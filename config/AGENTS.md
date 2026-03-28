# Configuration Hub

**Purpose:** LaTeX packages, macros, and formatting rules

## STRUCTURE
```
config/
├── packages.tex           # Core packages (biblatex, ctex, tikz, etc.)
├── commands.tex           # \inputbody, \inputpage, signature macros
├── path.tex               # \graphicspath, bibliography path
├── version.tex            # Template version number
├── paper1_macros.tex      # Paper 1 math operators
├── paper3_macros.tex      # Paper 3 macros + colors
└── format/
    ├── format.tex         # Format loader
    ├── general/           # Default formatting (11 files)
    │   ├── fonts.tex      # Chinese fonts (仿宋, 宋体, 黑体)
    │   ├── layout.tex     # Page layout, fancyhdr
    │   ├── geometry.tex   # Paper size, margins
    │   └── ...
    └── major/             # Major-specific overrides
        ├── cs/            # Computer science
        ├── ee/            # Electrical engineering
        ├── opteng/        # Optical engineering
        └── ...
```

## WHERE TO LOOK
| Task | Location |
|------|----------|
| Add new package | `packages.tex` |
| Add custom macro | `paper*_macros.tex` or create new |
| Change fonts | `format/general/fonts.tex` or `format/major/*/fonts.tex` |
| Adjust margins | `format/general/geometry.tex` |
| Modify header/footer | `format/general/layout.tex` → `\fancypagestyle` |
| Change citation style | `packages.tex` → `biblatex` options |

## ANTI-PATTERNS
- **NEVER** duplicate macros between paper1 and paper3 — check both files first
- **NEVER** modify `ctexrep` class options in `zjuthesis.cls` without testing Chinese fonts
- **NEVER** skip `fontset=noto` — required for Chinese rendering

## NOTES
- `format/major/` directories override `format/general/` based on `MajorFormat` option
- Paper-specific macros loaded AFTER packages.tex in zjuthesis.cls
- `\DET` macro collision resolved via `\DETtext` (paper1) and `\DET{arg}` (paper3)