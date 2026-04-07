# Learnings and Decisions

## 2026-04-07 Chapter 3 rhetoric audit

- Active Chapter 3 files are `paper2/main.tex`, `1_intro.tex`, `3_background.tex`, `4_method.tex`, `5_results.tex`, and `6_summary.tex`; `2_related.tex` is currently commented out in `main.tex` and was not treated as active text.
- The chapter-level framing in the introduction is "网格导致/离散导致的软硬耦合" and more specifically "discretization-induced soft-hard coupling" handled via local operator-aware basis-space reconstruction, optimization, and isolation. Chapter 3 drifts when it rebrands the problem as generic "病态单元处理", "数值预处理", or broad mesh-quality repair, rather than emphasizing discretization-induced soft-hard coupling.
- The strongest style risk is rhetorical inflation: many passages use combative, dramatic, or promotional metaphors (e.g. "病毒般污染", "精准点杀", "沙上建塔", "外科手术式", "至高命题") that exceed restrained doctoral-thesis tone.
- Terminology drift appears in both the problem name and the method name. Problem labels alternate among "病态系统", "劣质单元", "局域数值奇异性", "强链接", "数值锁定", and mesh-quality language without consistently tying them back to discretization-induced soft-hard coupling. Method labels alternate among "基函数优化", "局部基函数优化与隔离框架", "数值预处理框架", "基函数降维剥离机制", and wavelet/polyhedral language, which weakens chapter identity.
- The weakest closure is `6_summary.tex`, which shifts from summarizing verified chapter findings to sweeping thesis-level claims and grand transition rhetoric. It needs restrained closure tied to what Chapter 3 actually established.
