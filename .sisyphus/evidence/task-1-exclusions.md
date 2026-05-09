# Task 1 — Forbidden Edit Paths (Exclusions)

**Date:** 2026-05-09
**Source:** Direct inspection of source files and grep confirmation.

## Excluded from Active Build

### 1. `paper2/2_related.tex` — COMMENTED OUT

- **Evidence:** `body/graduate/paper2/main.tex:6` — `%\inputbody{paper2/2_related}`
- **Grep confirmation:** Only one match in the entire `body/graduate/` tree for `^%\\inputbody` outside backup.
- **Verdict:** This file exists on disk but is **NOT** included in the active PDF build. It must NOT be edited as part of the blind-review direct-fix scope. If the orchestrator later decides to activate it, that decision belongs to a separate task.

### 2. `body/graduate/paper1_backup/` — BACKUP DIRECTORY

- **Evidence:** `body/graduate/paper1_backup/main.tex` (lines 5-6) contains additional commented-out inputs:
  - `%\inputbody{paper1/jacobian_pattern}`
  - `%\inputbody{paper1/preconditioner}`
- **Grep confirmation:** These commented-out inputs exist only in the backup tree, not in any active file.
- **Verdict:** The entire `paper1_backup/` directory is a backup copy of the pre-migration paper1 source. It is **NOT** reachable from the active `\inputbody` chain in `content.tex`. It must NOT be edited.

### 3. `body/graduate/paper1/4_results_tikz_preview.tex` — STANDALONE PREVIEW

- **Evidence:** `body/graduate/paper1/4_results_tikz_preview.tex:1` — `\documentclass[UTF8,fontset=none]{ctexart}`
- **Grep confirmation:** This is the **only** file under `body/graduate/` with a standalone `\documentclass`.
- **Context:** The file is a self-contained LaTeX document designed to preview TikZ figures independently. It is **NOT** referenced by any `\inputbody` directive in the active build chain. It uses its own preamble, geometry, and font settings.
- **Verdict:** Standalone preview-only tool. Must NOT be edited as part of thesis content work.

### 4. Any file NOT transitively reachable from `\inputbody{content}` chain

This includes (but is not limited to):
- Files in `body/graduate/paper*/` not listed as active sub-inputs above
- Backup directories (`paper1_backup/`, and any future backups)
- Standalone preview/tool files with their own `\documentclass`
- Build artifacts in `out/` (gitignored)

## Forbidden Operations

| Operation | Reason |
|-----------|--------|
| Editing `paper2/2_related.tex` | Commented out in active build |
| Editing any file in `paper1_backup/` | Backup directory, not active |
| Editing `4_results_tikz_preview.tex` | Standalone preview, not part of thesis |
| Modifying `zjuthesis.cls` | Core class file — plan-mandated exclusion |
| Modifying `config/format/` | Formatting config — plan-mandated exclusion (unless specifically authorized) |
| Adding new `\inputbody` directives in `content.tex` | Changes build surface — requires separate approval |
