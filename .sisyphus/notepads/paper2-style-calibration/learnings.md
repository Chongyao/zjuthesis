# Learnings and Decisions

## 2026-04-07 Chapter 3 rhetoric audit

- Active Chapter 3 files are `paper2/main.tex`, `1_intro.tex`, `3_background.tex`, `4_method.tex`, `5_results.tex`, and `6_summary.tex`; `2_related.tex` is currently commented out in `main.tex` and was not treated as active text.
- The chapter-level framing in the introduction is "网格导致/离散导致的软硬耦合" and more specifically "discretization-induced soft-hard coupling" handled via local operator-aware basis-space reconstruction, optimization, and isolation. Chapter 3 drifts when it rebrands the problem as generic "病态单元处理", "数值预处理", or broad mesh-quality repair, rather than emphasizing discretization-induced soft-hard coupling.
- The strongest style risk is rhetorical inflation: many passages use combative, dramatic, or promotional metaphors (e.g. "病毒般污染", "精准点杀", "沙上建塔", "外科手术式", "至高命题") that exceed restrained doctoral-thesis tone.
- Terminology drift appears in both the problem name and the method name. Problem labels alternate among "病态系统", "劣质单元", "局域数值奇异性", "强链接", "数值锁定", and mesh-quality language without consistently tying them back to discretization-induced soft-hard coupling. Method labels alternate among "基函数优化", "局部基函数优化与隔离框架", "数值预处理框架", "基函数降维剥离机制", and wavelet/polyhedral language, which weakens chapter identity.
- The weakest closure is `6_summary.tex`, which shifts from summarizing verified chapter findings to sweeping thesis-level claims and grand transition rhetoric. It needs restrained closure tied to what Chapter 3 actually established.
- For the Chapter 3 contribution list, the four existing bullets naturally collapse into two same-level themes: (1) a local operator-aware basis reconstruction pipeline for distorted-element patches, combining patch-localized basis construction with a practical ordering/selection rule for aggregation targets; and (2) an explicit isolation-and-validation theme covering Dirac-wavelet treatment of strongly connected/rigid modes plus the benchmark/application evidence. This preserves all existing substance while avoiding the imbalance of "three method bullets + one experiments bullet".
- The thesis-introduction framing for Chapter 3 should remain centered on locally reconstructing the discretization space to separate artificial high-frequency stiffness induced by distorted meshes from the main solution space, rather than reframing the chapter as generic remeshing, algebraic preconditioning, or broad mesh repair.

## 2026-04-07 Canonical phrasing policy for Chapter 3

- Canonical chapter problem phrasing: use `由离散化导致的软硬耦合问题` as the default chapter-level label; when specificity is needed, expand to `由畸变单元引起的离散化软硬耦合问题` or `由畸变网格单元引起的局部高频人造刚度与全局低频响应之间的软硬耦合`.
- Canonical chapter method phrasing: use `基于算子感知的局部基空间重构与隔离` as the default method identity; when naming the concrete workflow, expand to `通过局部聚合、多面体基函数优化与 Dirac-wavelet 隔离来重构离散解空间`.
- Canonical claim boundary: present the chapter as mitigating discretization-induced ill-conditioning and reducing the numerical interference of local artificial high-frequency stiffness on global low-frequency response; do not claim complete elimination of all pathological effects, general mesh repair, or universal superiority over remeshing/algebraic preconditioning.
- Tone rule: keep the abstraction level aligned with the Introduction—problem first, then representation-space reconstruction, then observed numerical improvement; avoid promotional labels such as `开创性`, `彻底`, `根治`, `优雅地`, or imagery-driven metaphors.
- Transition rule (Chapter 3): Neutralized the method transition from combative labels ("病毒般污染", "彻底削弱", "致命") to objective technical descriptions ("数值干扰", "削弱...影响", "包含强连接构型的单元"). The contribution list is now successfully compressed into exactly two high-level bullets (one for the adaptive basis-reconstruction/aggregation pipeline and one for the Dirac-wavelet explicit isolation mechanism), fully replacing the prior unbalanced 4-bullet list.
- Summary section (6_summary.tex): Successfully rewritten to follow a strict thesis-style closing structure. The new text explicitly restates the problem as discretization-induced soft-hard coupling ("由畸变单元引起的局部高频人造刚度与全局低频响应之间的软硬耦合问题"), summarizes the method precisely ("通过对退化单元区域实施局部多面体聚合...引入 Dirac-wavelet 转换策略"), bounds the outcome claims to solving efficiency (~20% improvement in PCG) and stability in cutting without overclaiming, and situates the local reconstruction method firmly between Chapter 2's global kinematic approach and Chapter 4's upcoming macro-scale subspace challenge. All rhetorical/inflated terms (e.g. "精准点杀", "独具匠心", "无情剥离", "至高命题", "完美的最佳平衡点") and speculative future-work fluff were completely removed.

## 2026-04-07 Chapter 3 summary rewrite (6_summary.tex)
- Restructured the chapter summary to explicitly follow the thesis-level framing: restating the problem as discretization-induced soft-hard coupling (由畸变单元引起的局部高频人造刚度与全局低频响应之间的软硬耦合问题).
- Replaced combative and inflated rhetoric ("精准点杀", "无情剥离", "外科手术式", "至高命题", "独具匠心") with restrained technical descriptions (e.g., "局部多面体聚合", "削弱了局部人造刚度对主求解空间的数值干扰").
- Positioned the chapter carefully within the overall thesis narrative: contrasting its local representation-space adjustment for complex unstructured meshes against Chapter 2's global kinematic chain reconstruction.
- Transitioned smoothly to Chapter 4 by identifying the limitation of Chapter 3's local approach when scaling to massive systems, framing Chapter 4 as addressing macroscopic low-frequency subspace construction (算法导致的软硬耦合) rather than using overly dramatic language.
- Omitted the speculative and overly verbose "future work" paragraph, concluding the chapter with a strong, functional bridge to the next chapter.
- Summary rewriting rule (Chapter 3): The `6_summary.tex` was fully rewritten into a three-paragraph structure. Paragraph 1 restates the chapter problem and the adaptive basis-reconstruction/Dirac-wavelet isolation mechanism in thesis-aligned terms, stating evidence-bounded efficiency improvements (~20%). Paragraph 2 situates Chapter 3 within the thesis arc, contrasting its localized approach to addressing implicit discretization-induced numerical ill-conditioning against Chapter 2's global kinematic approach for explicit material stiffness. Paragraph 3 bridges to Chapter 4 by shifting focus from these localized high-frequency issues to the macro-scale problem of missing global low-frequency responses in large-scale domain decomposition. All promotional rhetoric (e.g., "精准点杀", "无情剥离") and speculative future work were removed to enforce a sober, rigorous academic tone.

- Rewrite rule (`6_summary.tex`): Replaced the combative and grandiloquent tone ("精准点杀", "沙上建塔", "外科手术式", "至高命题") with objective, measured academic language. The chapter summary now restates the problem as "由畸变单元引起的局部高频人造刚度与全局低频响应之间的软硬耦合问题", summarizes the mechanism as "基于算子感知的局部多面体聚合与 Dirac-wavelet 隔离", cites concrete outcome data (e.g., ~$20\%$ efficiency gain in PCG), positions the chapter against Chapter 2's global kinematic approach, and bridges transition to Chapter 4 without ungrounded rhetorical inflation. It explicitly excises speculative and unnecessary "future work" to close cleanly.

- For Paper 2 tone normalization, edits were made to abstract generic "病态单元处理" or promotional phrasing back to the canonical framing of "由畸变单元引起的离散化软硬耦合问题" and "基于算子感知的局部基空间重构与隔离".
- Replaced terms like "最优方法" or "最优" with empirical descriptions. Removed rhetorical inflations such as "显著改进带来了显著的好处", opting for simpler objective wording.
- Changed main.tex chapter title to better reflect the specific method: "有限元方法中病态网格单元的处理：局部基空间重构与隔离" (removed numerical-aware refinement/aggregation buzzwords that didn't align with the thesis canonical framing).

## 2026-04-07 Tone normalization for middle paper2 body files

- Modified `3_background.tex`: Softened promotional claims such as "这种劣质单元往往是局部的且不可避免的" to "换言之，这些劣质单元往往是局部的。因此，本研究的目标是针对由畸变单元引起的离散化软硬耦合问题，开发一种轻量且高效的方法，专门处理这一局部的病态问题。" Added proper framing of the soft-hard coupling problem.
- Modified `4_method.tex`: Softened words like "显著" (changed "产生极高的基函数梯度" -> "导致离散化带来的软硬耦合"). Replaced overly strong phrasing "显著挑战" with "优化挑战", "最大行和贡献最显著的单元" with "最大行和贡献最大的单元", etc. Rewrote the intro paragraph to properly state "基于算子感知的局部基空间重构与隔离方法".
- Modified `5_results.tex`: Softened results language. Removed "最优方法", replaced "最显著的性能提升" with "更好的性能". Reworded "这一显著改进带来了显著的好处：共轭梯度方法所需的计算时间减少了" to "这一改进减少了计算成本：共轭梯度方法所需的计算时间减少了".
- Modified `main.tex`: Corrected the chapter title to properly state "局部基空间重构与隔离" and removed the leading placeholder TODO comment.

## 2026-04-07 Paper2 Middle Body Tone Calibration
- Applied the canonical phrasing to Chapter 3 middle body sections.
- Softened extreme terms like "非常大" replacing "任意大", and removed unverified claims of "最显著", "最优", etc.
- Unified terminology to consistently frame the issue as "由畸变单元引起的离散化软硬耦合问题".

## 2026-04-07 Tone Normalization in paper2 middle chapters
- Replaced general "病态单元处理" with the specific "由畸变单元引起的离散化软硬耦合问题" in `3_background.tex` to maintain chapter identity.
- Reframed the method name as "基于算子感知的局部基空间重构与隔离" or "算子适应基函数优化" to adhere to the canonical method phrasing.
- Softened superlative, promotional language (e.g., removing "最" or "显著") in `4_method.tex` and `5_results.tex`. Focus remains strictly on the verifiable impact of reducing ill-conditioning from mesh distortion.
- Edited `main.tex` to update the chapter title from "处理" to "局部基空间重构与隔离".

## 2026-04-07 Middle body prose normalization

- Successfully normalized rhetoric across `3_background.tex`, `4_method.tex`, and `5_results.tex`.
- In `3_background.tex`: Replaced generic "处理这一局部的特殊问题" with specific canonical phrasing "针对由畸变单元引起的离散化软硬耦合问题，专门处理这一局部的病态问题".
- In `4_method.tex`: Replaced emotional phrasing like "变得任意大" with "变得非常大", "显著贡献" with "较大", "带来了显著挑战" with "带来了优化挑战", "最显著" with "最大", "显著降低" with "明显降低" (reverted one instance back to "显著降低" due to hash mismatch, but overall softened the tone).
- In `5_results.tex`: Replaced "产生最显著的性能提升" with "产生更好的性能", "最优方法" with "该方法", "优越的性能" with "较好的性能", and removed redundant phrases like "显著改进带来了显著的好处".
- In `main.tex`: Applied canonical chapter title "有限元方法中病态网格单元的处理：局部基空间重构与隔离" instead of generic placeholders.

## 2026-04-07 Middle Chapters Tone Normalization

- Replaced "坏形状单元" and "病态单元" with "畸变单元" in `3_background.tex` to maintain the canonical phrasing "由畸变单元引起的离散化软硬耦合问题".
- Softened extreme descriptors like "非常大" replacing "任意大", "优化挑战" replacing "显著挑战", and "最大的降低" instead of "最大程度降低" in `4_method.tex`.
- Replaced hyperbolic/promotional phrasing in `5_results.tex` like "最显著的性能提升" to "更好的性能", "优越的性能" to "较好的性能", and removed redundant phrases like "这一显著改进带来了显著的好处", replaced with "这一改进减少了计算成本".
- Updated `main.tex` title from "数值感知细化与聚合" to "局部基空间重构与隔离", removing the placeholder TODO comment.

## 2026-04-07 Paper 2 middle files tone calibration
- Normalized prose tone in `3_background.tex`, `4_method.tex`, `5_results.tex`, and `main.tex` according to the audit rules.
- Replaced exaggerated promotional rhetoric (e.g. `显著`, `非常大`, `根治`, `最显著`) with more balanced technical wording in Method and Results chapters.
- Clarified the central problem framing as `由畸变单元引起的离散化软硬耦合问题` instead of generic `病态系统` or generic remeshing problems.
- Clarified the core method as `基于算子感知的局部基空间重构与隔离` and its pipeline elements.
- Adjusted `main.tex` Chapter 3 title and removed the placeholder comment.

## 2026-04-07 Task 5: Middle Body Tone Normalization
- Audited `paper2` files: `3_background.tex`, `4_method.tex`, `5_results.tex`, and `main.tex`.
- In `3_background.tex`: Replaced generic ill-conditioned language with standard "由畸变单元引起的离散化软硬耦合问题". Softened "坏形状单元通常不会遍布整个区域" by clarifying the goal to tackle local ill-conditioning.
- In `4_method.tex`: Adjusted subjective claims ("可能变得任意大" -> "可能变得非常大", "显著挑战" -> "优化挑战") and re-aligned the method introduction to "基于算子感知的局部基空间重构与隔离方法". Clarified the nature of "强链接" causing discretization-induced soft-hard coupling.
- In `5_results.tex`: Softened hyperbolic conclusions (e.g., "最显著的性能提升" -> "更好的性能", "优越的性能" -> "较好的性能", "显著改进带来了显著的好处" -> "改进减少了计算成本"). Ensured method framing matches canonical naming ("基于算子感知的局部基空间重构与隔离技术").
- In `main.tex`: Modified the chapter title placeholder from generic "处理：数值感知细化与聚合" to "处理：局部基空间重构与隔离" to align with standard wording. Removed the placeholder TODO comment.
