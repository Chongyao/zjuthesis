# Learnings

## 2026-04-13 Session: paper2-review-fixes initialization
- Canonical terminology is fixed to `强连接`; implementation must remove residual `强链接` inside the five in-scope paper2 files.
- Structure-first rule from AGENTS.md is binding: repair paragraph order and section handoffs before doing sentence-level polish.
- Chapter identity should remain `由离散化导致的软硬耦合问题` / `由畸变单元引起的离散化软硬耦合问题`, not generic mesh repair or generic preconditioning.
- Canonical method identity should remain `基于算子感知的局部基空间重构与隔离`.
- `3_background.tex` -> `4_method.tex` is a single narrative handoff and should be revised as one atomic transition unit.
- `5_results.tex` framing depends on a stable method narrative in `4_method.tex`; do not finalize results wording before method mainline is stable.
- Avoid rhetorical inflation, oral phrasing, and generic “looks smoother” edits; every change must map back to one of the 11 review findings.
- 2026-04-13: Reworked the `3_background.tex` ending and `4_method.tex` opening as one transition unit: background now closes on the locality of distortion-induced pathology and the need for local treatment, while method now opens by first introducing candidate tetrahedra / patch entry into the workflow before detailed reconstruction and isolation steps.

## 2026-04-13 Summary local-closure tightening
- In `body/graduate/paper2/6_summary.tex`, strengthened the first paragraph's local closure so it now finishes Paper 2's own problem-method-evidence chain before moving into thesis-level positioning.
- Preserved the three-paragraph summary structure, kept the tone evidence-bounded, retained the contrast with Chapter 2 and the bridge to Chapter 4 only after the chapter-local conclusion was completed.


## 2026-04-13 Task T7: local terminology/style policy lock for paper2
- Canonical local term is fixed as `强连接`; any residual `强链接` in the active paper2 files should be normalized to `强连接` before broader prose work.
- Minimal safe fix applied now: `5_results.tex` benchmark paragraph was normalized from `强链接` to `强连接`; no structural rewriting or full results/header/caption rewrite was performed.
- Locked local style policy for later `5_results.tex` work: keep the chapter framed as `由离散化导致的软硬耦合问题` / `由畸变单元引起的离散化软硬耦合问题`, and keep the method identity as `基于算子感知的局部基空间重构与隔离`.
- Remaining `5_results.tex` normalization targets for later tasks (do not rewrite yet):
  - Table 5.1 header is still English-heavy: `Example`, `opt. time (s)`, and `\#TET` / `\#T($\gamma>50$)` should be normalized into thesis-style Chinese labels when the full results pass is performed.
  - Figure/benchmark wording still contains English-heavy labels or untranslated abbreviations that may need coordinated normalization, e.g. `Thingi10k`, `CG`, `DOFs`, and mixed English model names (`Nut`, `BCC`, `SphereShell`), but these should be handled only in a dedicated results-language pass.
  - Results captions and subsection headers should later be checked together for consistent Chinese academic style, especially benchmark/statistics phrasing, without changing the verified experimental meaning.
  - Keep `强连接` as the canonical term during that later pass, including captions and any quoted configuration names.
- 2026-04-13: For `1_intro.tex`, a safe structural repair is to add a restrained bridge paragraph immediately after the contribution list so the section closes on reader guidance rather than ending directly on bullets; the bridge should summarize the list as the chapter's problem-solving mainline and preview background, method, results, and summary without adding new claims.
- 2026-04-13: For `4_method.tex`, a minimal safe reader-order repair is to establish the workflow once near the opening as “candidate entry -> implicit-to-explicit strong-connection exposure -> local basis optimization/isolation”, move `候选选择` before the branch-treatment discussion, and let the later `显式强连接的隔离` subsection execute only the stricter branch instead of re-announcing both choices.

## 2026-04-13 Task T6: sentence-level cleanup for `4_method.tex`
- Kept the method identity fixed as `基于算子感知的局部基空间重构与隔离`; edits were limited to sentence splitting, de-oralization, and translationese cleanup.
- Safe local pattern: when a method paragraph carries both setup and consequence in one long sentence, split at the claim boundary rather than reordering the paragraph, so canonical framing and technical meaning remain unchanged.

- 2026-04-13: Final T6 cleanup in `4_method.tex` removed residual raw `patch` carryover after first mention, replaced informal `降掉` with formal `移除`, and split the opening workflow paragraph without altering the accepted reader-order mainline.

## 2026-04-13 Task T8: cross-file transition harmonization
- Coordinated the intro bridge, background closing, and method opening as one chapter-spine pass: intro now previews the narrowed problem and workflow order, background now hands off with `候选四面体单元及其局部邻域`, and method opening keeps the same candidate-entry -> strong-connection exposure -> local reconstruction/isolation chain without re-inflating rhetoric.

## 2026-04-13 Task T5: results-block validation framing
- In `body/graduate/paper2/5_results.tex`, a safe framing pattern is to open each major results block with one restrained sentence that names the specific method choice being validated—candidate selection + strong-connection treatment, hierarchy step count `q`, implicit-to-explicit strong-connection exposure, local basis reconstruction/isolation stability, or application/precomputation value—before restating the unchanged evidence.

## 2026-04-13 Task T9: cross-block bridge prose in `5_results.tex`
- In `body/graduate/paper2/5_results.tex`, the safest progression repair was to add one restrained bridge after the average-case benchmark/step-count evidence and one before applications, explicitly naming the chapter movement from overall statistical benefit, to concentrated difficult cases, to application-level value without changing experiment order or claims.

## 2026-04-13 Task T10: final results-language normalization in `5_results.tex`
- Normalized Table 5.1 toward Chinese-first thesis style while preserving dataset/model names and symbols: `Example` -> `示例`, `\#TET` -> `四面体数`, `\#T($\gamma>50$)` -> `满足 $\gamma>50$ 的四面体数`, and `opt. time (s)` -> `优化时间（s）`.
- Kept canonical term `强连接` unchanged and aligned application/result captions with the accepted method identity `基于算子感知的局部基空间重构与隔离`, avoiding broader structural rewrites or experiment-order changes.
- Safe caption rule confirmed for later similar passes: translate surrounding presentation into formal Chinese academic style, but retain dataset names, model names, and necessary abbreviations such as CG when full forced translation would reduce precision.

## 2026-04-13 Task T10 follow-up: minimal local style-tail cleanup in `5_results.tex`
- In `body/graduate/paper2/5_results.tex`, the safest final local cleanup was to replace `自由度（Degrees of Freedom, DOFs）` with `更少自由度` and to normalize `最大"行和"` to `最大行和`, keeping dataset names, structure, ordering, and accepted T5/T9 framing unchanged.

## 2026-04-13 Merge-conflict resolution principle
- Resolved paper2 merge conflicts by keeping the accepted local reader-order structure and results framing from `paper2-review-fixes`, while only absorbing upstream wording refinements when they improved citation or sentence flow without changing section order, terminology (`强连接`), or experimental meaning.
