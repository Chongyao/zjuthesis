# paper1-layout-and-appendix-refinement issues

## 2026-04-07 Chapter 2 relocation risk analysis for Tasks 4-9

- Scope checked with file/line support:
  - `body/graduate/paper1/main.tex:5-15`
  - `body/graduate/paper1/3_simulation.tex:1-285`
  - `body/graduate/paper1/preconditioner_content.tex:1-170`
  - `body/graduate/paper1/4_results.tex:1-270`
  - `body/graduate/paper1/app_energy_terms.tex:1-44`
  - `body/graduate/paper1/app_active_set.tex:1-38`
  - `body/graduate/paper1/app_extended_redmax.tex:1-116`
  - `body/graduate/paper1/app_invertible_proof.tex:1-55`

- TOC / hierarchy risk summary:
  - `main.tex:11-15` currently inputs `5_conclusion` before all four appendix-like files. This explains the inherited symptom: TOC reaches `2.5 本章小结` and then continues with trailing appendix-like entries, because appendix headings are still part of the same chapter after the conclusion.
  - `app_energy_terms.tex:1`, `app_active_set.tex:1`, and `app_extended_redmax.tex:1` are all `\subsection{...}`. If moved earlier into Chapter 2/Chapter section flow, they will appear as third-level entries under the most recent active `\section`. If they stay after `5_conclusion`, they become children of `2.5 本章小结`, which is structurally wrong.
  - `app_invertible_proof.tex:1` is `\section{预条件器正定性证明}` rather than `\subsection`. If left in place, it becomes a same-level section after `2.5 本章小结`; if moved inside Section 2.3 material without demotion, it would create a new top-level section and break chapter numbering/flow.

- Recommended target heading levels after relocation:
  - `app_energy_terms.tex:1` -> keep at `\subsection`; target position immediately after `3_simulation.tex:62-79` discussion of energy terms / active-set reformulation.
  - `app_active_set.tex:1` -> keep at `\subsection`; target position immediately after `3_simulation.tex:79-80` where pseudo-code is referenced.
  - `preconditioner_content.tex:1` already sits at `\subsection` under `3_simulation.tex:165`; no heading change needed, but relocation of related proof material must preserve that parent section.
  - `app_invertible_proof.tex:1` -> demote from `\section` to `\subsection`; target position immediately after `preconditioner_content.tex` as a sibling under `3_simulation.tex:165`'s `\section{...算子评估}` unless a new dedicated parent section is introduced.
  - `app_extended_redmax.tex:1` -> keep at `\subsection`; target position in `4_results.tex` before or inside the RedMax comparison block (`4_results.tex:153-156`) so the appendix-like derivation is no longer trailing after the chapter conclusion.

- Exact heading-depth conflicts to watch:
  - Conflict A: `app_invertible_proof.tex:1` uses `\section`, but the surrounding preconditioner material is only a `\subsection` chain (`3_simulation.tex:165`, `preconditioner_content.tex:1`). Without demotion, TOC will create an extra section peer after Section 2.3 / 2.4 rather than a nested proof block.
  - Conflict B: `app_energy_terms.tex:1`, `app_active_set.tex:1`, `app_extended_redmax.tex:1` are safe only if inserted while a parent `\section` is active. If pasted after a `\subsubsection` in `4_results.tex`, they would still attach to the enclosing `\subsection`, producing unexpected TOC siblings unless spacing/order is deliberate.
  - Conflict C: `4_results.tex` already uses `\subsubsection` heavily (`31`, `106`, `137`, `153`). Inserting relocated `\subsection` blocks inside the middle of that sequence will reset hierarchy upward and visually interrupt the comparison narrative. For RedMax material, place the relocated block before the `\subsubsection{与 RedMax 的比较}` sequence begins, or demote it if it must live inside that comparison stream.

- Likely TOC outcomes by option:
  - If no heading edits are made and only file order changes:
    - Moving `app_energy_terms` / `app_active_set` into `3_simulation` will likely produce clean subsection entries under Section 2.3.
    - Moving `app_invertible_proof` into `3_simulation` without demotion will create a new section-level TOC entry after the simulation section, which is probably too strong.
    - Moving `app_extended_redmax` ahead of results without demotion/change will create a subsection-level TOC item near the RedMax discussion; acceptable only if the chapter intends an explicit methods supplement before results prose.
  - If the goal is to eliminate appendix-like feel from TOC, the minimal safe path is: keep the three `\subsection` appendix files as-is, demote `app_invertible_proof` to `\subsection`, and relocate each next to its first citation site.

- Minimal wording adjustments required near citation sites after relocation:
  - `3_simulation.tex:62` currently says `这些项的具体公式见附录~\ref{app:energies}`. After relocation inside the main flow, change `附录` to wording like `下文` / `本节后续部分` / `本节中的“能量项详细推导”小节`.
  - `3_simulation.tex:79` currently says `伪代码见附录~\ref{app:active_set}`. After relocation, change `附录` to `后文` / `下文` / `见“碰撞的有效集法”小节`.
  - `4_results.tex:154` currently says `为公平比较，我们在附录~\ref{model_redMax} 中将其扩展到 Kirchhoff 杆`. If relocated into nearby main-text results context, change `附录` to `前文` / `下文` / `见“Kirchhoff 杆仿真的扩展 RedMax”小节` depending on final placement.
  - No nearby prose currently cites `app:invertible`; the risk is TOC/heading depth, not wording. References inside the proof file itself (`app_invertible_proof.tex:5,18`) are equation refs and do not need appendix wording cleanup.

- Reference integrity notes:
  - Labels likely remain valid after relocation: `app:energies`, `app:active_set`, `model_redMax`, `app:invertible` are local anchors and do not depend on file order.
  - `app_extended_redmax.tex:23` references `eq:V_q`, so placing RedMax derivation before `app_energy_terms.tex` is still technically okay because LaTeX resolves globally, but concept flow becomes weaker; better to keep the energy derivation earlier than the RedMax derivation.

- Minimal relocation checklist for implementation phase:
  1. Reorder `main.tex:10-15` so appendix-like blocks no longer follow `5_conclusion`.
  2. Keep `app_energy_terms` and `app_active_set` as `\subsection` under `3_simulation`.
  3. Demote `app_invertible_proof` from `\section` to `\subsection` before inserting near preconditioner material.
  4. Place `app_extended_redmax` adjacent to `4_results.tex:153-156` and update `附录` wording there.
  5. Verify TOC no longer shows entries after `2.5 本章小结`.

## 2026-04-07 Task 5 hierarchy caveat
- `app_energy_terms.tex` needed demotion from `\subsection` to `\subsubsection` after being inlined under the existing simulation section; keeping it at `\subsection` would have introduced an unnecessary same-level block and visually interrupted the surrounding Section 2.3 narrative.

- No additional reference-risk found during Task 7: moving `app_invertible_proof` inline after the SPD statement preserved both `\ref{eq:preconditioner_structure}` usage inside the proof and the `\label{app:invertible}` anchor, so no wording or label repair was needed at this step.
- [Item 6]: `app_active_set` is still labeled with `\label{app:active_set}` which might conflict with referencing style depending on task 9 requirements.
- ## 2026-04-07 Task 8 hierarchy caveat
- `app_extended_redmax.tex` could not remain a `\subsection` after inline relocation into the RedMax comparison stream of `4_results.tex`, because that would interrupt the ongoing `\subsubsection` comparison sequence before `更多结果`. Demoting it to `\paragraph` keeps the `\label{model_redMax}` anchor available while avoiding a new peer subsection in the chapter hierarchy; note that `\paragraph` references may resolve to the parent counter rather than a dedicated numbered subsection.
- [Task 6 fix] Cross-reference diagnostics in the touched TeX fragments still report existing undefined references without compilation; these are not introduced by the appendix-anchor move.
- ## 2026-04-07 Task 9 remaining caveat
- `latexmk` now succeeds and `out/zjuthesis.toc` is clean for Chapter 2, but the full thesis build still reports unrelated pre-existing warnings (e.g. Biber legacy month fields, one missing U+2010 glyph in Times New Roman, and general over/underfull boxes outside this task scope).
- ## 2026-04-07 Final verification note
- No blocking acceptance issue found. The only unresolved cosmetic concern is that `out/zjuthesis.toc` still shows `Kirchhoff 杆仿真的扩展 RedMax` as a standalone `paragraph` entry under `2.4.1.4`; this is acceptable for closure but is the one remaining TOC style irregularity if a future polish-only pass is ever requested.
- ## 2026-04-07 TOC polish caveat
- `latexmk` succeeds and `out/zjuthesis.toc` no longer contains a standalone `paragraph` entry for `Kirchhoff 杆仿真的扩展 RedMax`; remaining build warnings are the same unrelated pre-existing full-thesis warnings already noted earlier, and texlab still flags the local label as unused inside `app_extended_redmax.tex` because the cross-reference is consumed from `4_results.tex` at document scope.