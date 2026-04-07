# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common commands

- `make build` or `latexmk` — incremental build of the current thesis to `out/zjuthesis.pdf`
- `make safe` — try incremental build first, then clean + rebuild if it fails
- `make rebuild` — full rebuild from scratch
- `make clean` — remove auxiliary files but keep the PDF
- `make cleanall` — remove all generated files, including `out/`
- `make watch` — continuous rebuild on file changes via `latexmk -pvc`
- `make count` — word count using `script/utils/word_count.sh` (requires a prior successful build)
- `make view` — open `out/zjuthesis.pdf`
- `latexmk -xelatex -outdir=out zjuthesis` — explicit XeLaTeX build
- `latexmk -pdflua -outdir=out` — LuaLaTeX build variant from the upstream template docs

### CI / regression-style builds

- `bash script/ci/github-action/build_grad.sh` — build the graduate template matrix into `dist/` and `out-ci/`
- `bash script/ci/github-action/build_undergrad.sh` — build the undergraduate template matrix into `dist/` and `out-ci/`
- `bash script/ci/github-action/build_single.sh graduate general thesis final false doctor chinese` — build one specific configuration

`script/ci/github-action/build_zjuthesis.sh` rewrites option lines inside `zjuthesis.tex` with `sed` before compiling. Treat these scripts like test harnesses: they mutate the working copy and are not the normal way to build your in-progress thesis.

## High-level architecture

- `zjuthesis.tex` is the main entry point. It holds the documentclass options that control almost everything: `Degree`, `MajorFormat`, `Type`, `Period`, `BlindReview`, `Language`, and `GradLevel`. The root file then dispatches into either the undergraduate or graduate assembly flow.
- `zjuthesis.cls` is the core class. It declares the key-value options, loads `ctexrep`, imports global packages and paper-specific macro files, then wires in the path layer (`config/path.tex`), command layer (`config/commands.tex`), and formatting layer (`config/format/format.tex`).
- `config/commands.tex` is the main indirection layer. `\inputpage` and `\inputbody` resolve files by degree / grad level / major format with this priority (most specific wins):
  - Graduate: `page/graduate/{GradLevel}/{MajorFormat}/file` → `page/graduate/{GradLevel}/file` → `page/graduate/file`
  - Undergraduate: `page/undergraduate/{period}/major/{MajorFormat}/file` → `page/undergraduate/{period}/file`
  - If a change seems to have no effect, check whether a more specific file is shadowing the one you edited.
- `config/path.tex` centralizes shared resource lookup: the global `\graphicspath` and the bibliography source (`body/ref.bib`).
- `config/format/general/*` contains the common layout, numbering, geometry, language, heading, caption, and reference behavior. `config/format/major/*` contains major-specific overrides; per `docs/develop.md`, major-specific package additions should live in that major’s own `packages.tex`, not in `config/packages.tex`.

## Thesis content structure in this branch

This repository is not just the upstream template; it currently contains a dissertation assembled on top of it.

- `body/graduate/content.tex` defines the chapter order: `intro`, `paper1`, `paper2`, `paper3`, then `conclusion`.
- Each chapter directory has a `main.tex` that fans out into section files (e.g., `body/graduate/intro/main.tex`, `body/graduate/paper1/main.tex`).
- `body/graduate/post.tex` assembles the back matter (`post/ref`, `post/appendix`, and `post/cv` when not in blind review mode).
- `page/graduate/**` contains cover pages, TOC, abstract, and other front matter. Which file is chosen depends on the same degree / grad level / major format resolution logic used by `\inputpage`.
- Figures are split between the shared `figure/` directory and paper-local figure directories included via `config/path.tex`.

## Important repository-specific notes

- Use `latexmk`, not bare `xelatex`, for normal work. The template expects a multi-pass build so references and related outputs resolve correctly.
- `README.md` is the authoritative user-facing usage guide; `docs/usage.md`, `docs/FAQ.md`, and `docs/develop.md` are the detailed upstream references when you need template behavior rather than dissertation content.
- The GitHub Actions workflows build many template variants in Docker and generate PDF diff artifacts; if you need to understand “what counts as a regression test” in this repo, start with `.github/workflows/build_test.yml`, `.github/workflows/pr_test.yml`, and the scripts under `script/ci/github-action/`.
- If you are touching the EE undergraduate format, read `config/format/major/ee/README.md` first. It includes extra submission checklist items and a platform-specific font workaround.
- `body/graduate/paper2/main.tex` is explicitly marked as an in-progress refactor placeholder, so expect that chapter to be less stable than the surrounding structure.
