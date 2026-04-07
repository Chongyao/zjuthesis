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
