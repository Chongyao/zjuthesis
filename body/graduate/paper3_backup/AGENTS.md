# Paper 3: Primal-Dual Modes (模态综合法)

**Paper:** 基于多重划分的模态综合法求解大规模特征值问题

## STRUCTURE
```
paper3/
├── main.tex               # Chapter entry
├── 1_intro.tex            # Introduction (no separate abstract)
├── 2_related.tex          # Related work
├── 3_background.tex       # Background theory
├── 4_method.tex           # Core method
├── 5_implementation.tex   # Implementation details
├── 5_1_alg_adaptive_shifting.tex  # Adaptive shifting algorithm
├── 6_results.tex          # Results & experiments
├── 7_summary.tex          # 本章小结 (conclusion)
├── figures/               # 110+ figure files
│   ├── teaser/            # Teaser figures
│   ├── comparison-figures/ # Benchmark comparisons
│   ├── scaling_aggregation_new/ # Scaling plots
│   └── ...
```

## KEY MACROS (config/paper3_macros.tex)
| Macro | Definition | Usage |
|-------|------------|-------|
| `\DOT{a}` | `\left\langle{a}\right\rangle` | Inner product |
| `\FPP{f}{x}` | `\frac{\partial f}{\partial x}` | Partial derivative |
| `\DET{M}` | `\operatorname{det}\left(M\right)` | Determinant (operator form) |
| Colors: `IsConclusion`, `ExplainConclusion`, `ConclusionEvidence` | RGB 0,0,0 | Figure coloring |

## TERMINOLOGY (per migration plan)
| English | Chinese |
|---------|---------|
| Component Modes Synthesis (CMS) | 模态综合法 (CMS) |
| Interface Mode Reduction (IMR) | 界面模态缩减法 (IMR) |

## WHERE TO LOOK
| Task | Location |
|------|----------|
| Add figures | `figures/` subdirectories |
| Modify math notation | `config/paper3_macros.tex` |
| Update conclusion | `7_summary.tex` (renamed from conclusion) |
| Algorithm details | `5_1_alg_adaptive_shifting.tex` |

## ANTI-PATTERNS
- **NEVER** use `\DETtext` here — use `\DET{arg}` operator form
- **NEVER** rename `7_summary.tex` — must be `\section{本章小结}` per plan

## NOTES
- Migration plan: `.sisyphus/plans/migrate_paper3.md`
- Original source: `/home/zcy/workspace/records/primal-dual_modes`
- Abstract merged into intro (no standalone abstract)
- Conclusion renamed to "本章小结"