# Decisions

## 2026-04-13 Planning lock
- In-scope files are restricted to: `1_intro.tex`, `3_background.tex`, `4_method.tex`, `5_results.tex`, `6_summary.tex`.
- No new experiments, no changed numerical claims, no figure asset changes, no thesis-wide cleanup.
- Verification must include: file reads of revised bridge paragraphs, grep for `强链接`, and full-thesis `latexmk` build.
- Final implementation should preserve the existing technical argument while improving reader-order logic and section closure.
