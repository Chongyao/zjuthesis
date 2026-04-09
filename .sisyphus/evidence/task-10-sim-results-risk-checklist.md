# Task 10: Simulation / Results Risk Checklist

## `3_simulation.tex` Risk Map
| Section | Source Provenance | Risk | Action for Stage 2 / 3 |
| :--- | :--- | :--- | :--- |
| Intro | `4.0-method-new.tex` (Latter half) | Low | Ensure terminology consistency (SE-free IMR vs 无 Schur 补). |
| `\subsection{Schur 补的数学结构}` | `7.0-appendix.tex` (7.1 Schur Complement) | **High (Moved-source)** | Verify no formulas were lost during migration. Ensure smooth transition from main text. |
| `\subsection{低频界面模态的近似}` | `4.1 Approximation of Low-frequency interface modes` | Medium | Check if physical explanation of static equilibrium mapping is retained clearly. |
| `\subsection{实现细节}` | `4.1-implementation.tex` | Low | Verify algorithm names and variable matching. |
| `\subsubsection{奇异矩阵束与正则化背景}` | `2.0-related_work.tex` (2.4 Singular matrix pencil) | **Medium (Moved-source)** | Ensure related work context makes sense inside the implementation section. |

## `4_results.tex` Risk Map
| Section | Source Provenance | Risk | Action for Stage 2 / 3 |
| :--- | :--- | :--- | :--- |
| Intro & General | `5.0-results.tex` | Low | Check translation accuracy. |
| Statistics Tables | `5.1-statistics.tex` | Low | Verify all numbers match original table. |
| `\subsection{可扩展能力}` | `5.4 Extensibility` & `teaser.tex` | **Medium (Moved-source)** | Ensure teaser claims are supported by the text. |
| `\subsection{积分误差分析的实验细节}` | `7.0-appendix.tex` (7.3) | **High (Moved-source)** | Ensure all experimental parameter details are preserved. |
| `\subsection{可扩展性基准的代价分解}` | `7.0-appendix.tex` (7.4) | **High (Moved-source)** | Ensure breakdown aligns with the results body text. |