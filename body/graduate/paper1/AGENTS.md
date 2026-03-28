# Paper 1: Cosserat Rod Simulation

**Paper:** 基于紧凑表示的不可伸长 Cosserat 杆高效稳定仿真

## STRUCTURE
```
paper1/
├── main.tex               # Chapter entry, includes all sections
├── 1_intro.tex            # Abstract + Introduction
├── 2_representation.tex   # Compact representation theory
├── 3_simulation.tex       # Simulation framework
├── 4_results.tex          # Comparisons & benchmarks
├── 5_conclusion.tex       # Conclusions
├── app_*.tex              # Appendices: energy, active set, redmax
├── figures/               # 73+ figure files
│   ├── sheet/             # Sheet figures
│   ├── knot/              # Knot figures
│   ├── single_chain/      # Single chain demos
│   └── ...
```

## KEY MACROS (config/paper1_macros.tex)
| Macro | Definition | Usage |
|-------|------------|-------|
| `\DOT` | `\left\langle{#1}\right\rangle` | Inner product notation |
| `\FPPmathbf{A}{B}` | `\frac{\partial \mathbf{A}}{\partial \mathbf{B}}` | Matrix partial |
| `\TR` | `\text{tr}` | Trace operator |
| `\DETtext` | `\text{det}` | Determinant (text form, NOT `\DET`) |
| `\LowerTri`, `\UpperTri` | TikZ matrix pattern | Triangular indicator |
| `\TriDiag` | TikZ tridiagonal pattern | Matrix type indicator |
| `\Lim{n}` | Custom limit display | Compact limit notation |

## WHERE TO LOOK
| Task | Location |
|------|----------|
| Add figures | `figures/` subdirectories |
| Modify math notation | `config/paper1_macros.tex` |
| Update abstract | `1_intro.tex` first paragraphs |
| Appendix proofs | `app_energy_terms.tex`, `app_active_set.tex` |

## ANTI-PATTERNS
- **NEVER** use `\DET` here — use `\DETtext` to avoid collision with paper3
- **NEVER** modify `\LowerTri` TikZ definition — other macros depend on baseline alignment

## NOTES
- Migration plan: `.sisyphus/plans/migrate_paper1.md`
- Original source: `/home/zcy/workspace/records/ConsManifold`
- Appendices embedded inline in relevant sections via `\inputbody`