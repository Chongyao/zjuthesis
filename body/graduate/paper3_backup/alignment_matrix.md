# Primal-Dual Modes: Section Alignment Matrix

| Original Paper (primal-dual_modes) | Thesis Chapter (zjuthesis_paper3) | Changes / Notes |
| :--- | :--- | :--- |
| **Abstract** | _(Migrated to thesis global abstract)_ | Translated to Chinese. |
| **1.0 Introduction** | **1_intro.tex: \section{引言}** | Translated. |
| **2.0 Related Work** | **1_intro.tex: \subsection{相关工作}** | Demoted to subsection within Introduction. |
| 2.1 Component Modes Synthesis | 1_intro.tex: \subsubsection{模态综合法} | Demoted to subsubsection. |
| 2.2 Interface Mode Reduction | 1_intro.tex: \subsubsection{界面模态缩减法} | Demoted to subsubsection. |
| 2.3 Partitions and the domain decomposition method | 1_intro.tex: \subsubsection{划分与区域分解法} | Demoted to subsubsection. |
| 2.4 Singular matrix pencil | 3_simulation.tex: \subsubsection{奇异矩阵束与正则化背景} | Moved to Implementation section as background. |
| _(New Section)_ | 1_intro.tex: \subsection{本章方法与贡献} | Summary of contributions added. |
| **3.0 Background: CMS** | **2_representation.tex: \section{背景知识：模态综合法与多重划分}** | Translated, title adjusted. |
| 3.1 Partition | 2_representation.tex: \subsection{划分与子结构} | Translated. |
| 3.2 Craig-Bampton (CB) method | 2_representation.tex: \subsection{Craig-Bampton (CB) 方法} | Translated. |
| 3.2.1 Substructure eigenmodes | _(Merged into 3.2)_ | Merged into CB method subsection. |
| 3.2.2 Interface modes | _(Merged into 3.2)_ | Merged into CB method subsection. |
| 3.2.3 Reducing | _(Merged into 3.2)_ | Merged into CB method subsection. |
| 3.3 Analysis of computational cost | 2_representation.tex: \subsection{计算代价分析} | Translated. |
| **4.0 Phase-complement by Multiple Partitions** | **2_representation.tex: \subsection{多重划分的相位补足}** | Demoted to subsection under Background. |
| 4.1 Analysis of the 1D Laplacian problem | 2_representation.tex: \subsubsection{一维拉普拉斯问题的分析} | Demoted to subsubsection. |
| 4.2 Multiple partitions for CMS | 2_representation.tex: \subsubsection{CMS 的多重划分} | Demoted to subsubsection. |
| **4.0 Schur- and eigen-free IMR** | **3_simulation.tex: \section{无 Schur 补的界面模态缩减}** | Note: Original paper has two "4.0" sections. Translated. |
| **7.1 Schur Complement (Appendix)** | **3_simulation.tex: \subsection{Schur 补的数学结构}** | **Migrated from Appendix** to main text. |
| 4.1 Approximation of Low-frequency interface modes | 3_simulation.tex: \subsection{低频界面模态的近似} | Translated. |
| **4.1 Implementation** | **3_simulation.tex: \subsection{实现细节}** | Demoted to subsection. |
| 4.1.2 Regularization | 3_simulation.tex: \subsubsection{正则化} | Demoted to subsubsection. |
| 4.1.3 Fast Reduced Matrix Assembly | 3_simulation.tex: \subsubsection{快速缩减矩阵组装} | Demoted to subsubsection. |
| 4.1.4 Hybrid MPI/OpenMP Framework | 3_simulation.tex: \subsubsection{混合 MPI/OpenMP 框架} | Demoted to subsubsection. |
| 4.1.5 Partition by METIS | 3_simulation.tex: \subsubsection{基于 METIS 的划分} | Demoted to subsubsection. |
| **5.0 Results** | **4_results.tex: \section{实验结果}** | Translated. |
| 5.1 Evaluation of accuracy and performance | 4_results.tex: \subsection{精度与性能评估} | Translated. |
| 5.2 Scalability | 4_results.tex: \subsection{可扩展性} | Translated. |
| 5.2.1 Emulation of MPI environment and performance metrics | 4_results.tex: \subsubsection{MPI 环境模拟与性能指标} | Translated. |
| 5.2.2 Experimental settings | 4_results.tex: \subsubsection{实验设置} | Translated. |
| 5.2.3 Results | 4_results.tex: \subsubsection{结果} | Translated. |
| 5.3 Comparison | 4_results.tex: \subsection{方法对比} | Translated. |
| 5.3.1 Error-Time Analysis | 4_results.tex: \subsubsection{误差--时间分析} | Translated. |
| 5.3.2 Timing vs. Number of Accurate Modes | 4_results.tex: \subsubsection{时间 vs. 准确模态数量} | Translated. |
| 5.4 Extensibility | 4_results.tex: \subsection{可扩展能力} | Translated. |
| 5.4.1 Reusability | 4_results.tex: \subsubsection{可重用性} | Translated. |
| 5.4.2 Performance on Large-Scale Model | 4_results.tex: \subsubsection{超大规模模型性能} | Translated. |
| **7.3 Experimental Details for Integrated Error Analysis (Appendix)** | **4_results.tex: \subsection{积分误差分析的实验细节}** | **Migrated from Appendix** to main text. |
| 7.3.1 Objective | 4_results.tex: \subsubsection{实验目标} | Demoted to subsubsection. |
| 7.3.2 Methodology | 4_results.tex: \subsubsection{实验方法} | Demoted to subsubsection. |
| 7.3.3 Parameters | 4_results.tex: \subsubsection{参数设置} | Demoted to subsubsection. |
| **7.4 Breakdown of Scaling Benchmark (Appendix)** | **4_results.tex: \subsection{可扩展性基准的代价分解}** | **Migrated from Appendix** to main text. |
| **6.0 Conclusion** | **5_conclusion.tex: \section{本章小结}** | Translated. |
| **7.0 Appendix** | _(Absorbed into main text)_ | All relevant appendices migrated to appropriate sections. |
