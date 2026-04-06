## 2026-04-06 investigation notes
- Requested plan filename in task context did not exist: `.sisyphus/plans/migrate_paper1.md` returned file-not-found.
- Matching actual structure plan found via grep: `.sisyphus/plans/migrate_paper1_structure.md`.
- There are two preconditioner-related files: `preconditioner.tex` and `preconditioner_content.tex`. The active include from `3_simulation.tex` is `preconditioner_content.tex`; `preconditioner.tex` appears to be an older or alternate standalone version and is not included by `paper1/main.tex`.
