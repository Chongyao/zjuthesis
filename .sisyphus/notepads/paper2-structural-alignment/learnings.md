# Learnings and Decisions

- **Task 1 Completion Notes**:
  - Reorganized `body/graduate/paper2/1_intro.tex` to title `\section{研究背景}` and merged `2_related.tex` related work content fully within its subsection `\subsection{相关工作与传统方法的局限}`.
  - Reorganized `body/graduate/paper2/3_background.tex` to title `\section{软硬耦合分析}` and merged its previous `\subsection{主要贡献}` points directly into `1_intro.tex`'s `\subsection{本章方法与贡献}` to remove redundancy.
  - Left `2_related.tex` as a commented-out placeholder (for transition to Task 3) rather than deleting it.

- Task 2 (Reorganize Section Titles): Changed `\section{构建数值适应的层次结构}` to `\section{基函数变换}` in 4_method.tex and `\section{结果与讨论}` to `\section{实验结果与分析}` in 5_results.tex. Verified `\section{本章小结}` in 6_summary.tex. No unexpected structural risks.
- Task 3 (main.tex alignment): Commented out `\inputbody{paper2/2_related}` in `body/graduate/paper2/main.tex` so paper2 now follows the intended 5-section structure after related-work content was merged into `1_intro.tex`.

- **Task Fix Completion**: Reverted the contribution bullet list in `1_intro.tex` to strictly match the exact four bullet points originally present in `3_background.tex`. Removed the newly-synthesized claims regarding "Dirac-wavelet 隔离技术在解决严重网格..." and "共轭梯度法评测..." that were inadvertently introduced during structural merging. Ensured absolute scope fidelity by avoiding any editorial expansion.
