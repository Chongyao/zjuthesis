## Migration Learnings - Paper3 Figures and Bib

### Figures Migration
- Source: `/home/zcy/workspace/records/primal-dual_modes/figures/`
- Target: `body/graduate/paper3/figures/`
- Successfully copied all image files (.png, .pdf) and subdirectories
- Permission errors on some .out files (output logs) - these are not needed for LaTeX paper
- Structure preserved: critical-qb/, domain_definition/, frequency-vs-phase/, teaser/, etc.

### BibTeX Merging
- Source: `/home/zcy/workspace/records/primal-dual_modes/all.bib/all.bib` (2214 lines)
- Target: `body/ref.bib`
- Strategy: Extract entry keys from source, check against existing keys in target
- Existing keys in target: 4 (tikz, zjugradthesisrules, zjuthesis, zjuthesisrules)
- New entries added: 153
- Total entries after merge: 157

### Dedup Approach
1. Parse existing ref.bib to extract all citation keys
2. Parse source .bib to find all entries and their keys
3. Filter out entries whose keys already exist in target
4. Append remaining entries to ref.bib

### Key Learnings
- Some @String entries in source (cgforum, tog) were also copied as they may be referenced
- BibTeX entry keys are case-sensitive
#JK|- Multi-line entries need careful handling - use blank line as separator

### Main.tex Structure
- Chapter title: `\chapter{基于多重划分的模态综合法求解大规模特征值问题}`
- Section includes: `\inputbody{paper3/X_section}` format
- Empty section files created: 1_intro.tex through 7_summary.tex
- Zjuthesis uses `\inputbody{dir/file}` to include files relative to `body/graduate/`



### Translation Guidelines (1_intro.tex)
- Source files: `abstract.tex` and `1.0-introduction.tex`
- Target file: `body/graduate/paper3/1_intro.tex`
- Abstract becomes introductory paragraph (no `\begin{abstract}` environment)
- Section heading: `\section{引言}` (not `\section{Introduction}`)
- Terminology established:
  - Component Mode Synthesis (CMS) → 模态综合法 (CMS)
  - Interface Mode Reduction (IMR) → 界面模态缩减法 (IMR)
  - Krylov subspace methods → Krylov 子空间方法
  - eigenvalues/eigenvectors → 特征值/特征向量
  - substructure → 子结构
  - partition → 划分
  - staggered → 交错
  - Schur complement → Schur 补
- Preserve all LaTeX commands: `\cite{}`, `\Cref{}`, `\textbf{}`, `\textit{}`, `\textcolor{}{}`
- Itemize environments translated but structure preserved
- Color commands like `\textcolor{IsConclusion}{}` kept as-is (defined elsewhere in template)

### Translation Guidelines (2_related.tex)
- Source file: `2.0-related_work.tex`
- Target file: `body/graduate/paper3/2_related.tex`
- Section heading: `\section{相关工作}` (not `\section{Related Work}`)
- Additional terminology:
  - Component Mode Synthesis (CMS) → 模态综合法 (CMS) [confirmed]
  - Interface Mode Reduction (IMR) → 界面模态缩减法 (IMR) [confirmed]
  - Domain Decomposition Method (DDM) → 区域分解法 (DDM)
  - eigenproblem → 特征值问题
  - monolithic approach → "整体式"方法
  - fixed-interface normal modes → 固定界面正规模态
  - static constraint modes → 静态约束模态
  - singular matrix pencil → 奇异矩阵束
  - Kronecker Canonical Form (KCF) → Kronecker 标准型 (KCF)
  - staircase algorithm → 阶梯算法
  - regularization methods → 正则化方法
  - shift-and-invert → 位移-逆变换
- Source file contains commented-out paragraph lines (59-94) - these are draft content that was already integrated above
- Kept all LaTeX commands: `\cite{}`, `\citet{}`, `\citep{}`, `\ref{}`, `\label{}`, `\DET{}`
- Math environments preserved exactly: inline math `$...$` and display math `\[...\]`
### Translation Guidelines (3_background.tex)
- Source file: `3.0-background.tex`
- Target file: `body/graduate/paper3/3_background.tex`
- Section heading: `\section{背景知识：模态综合法 (CMS)}` (not `\section{Background: CMS}`)
- Additional terminology:
  - eigenproblem → 特征值问题
  - DoFs (degrees of freedom) → 自由度
  - partition → 划分
  - substructure → 子结构
  - interface → 界面
  - truncated → 截断后的
  - constrained modal analysis → 约束模态分析
  - unit displacement excitation → 单位位移激励
  - static equilibrium state → 静力平衡状态
  - Galerkin triple-matrix-product → Galerkin 三重矩阵乘积
  - factorization → 分解
  - forward/backward substitutions → 前代/回代
  - superlinear → 超线性
- Preserved all LaTeX commands: `\cite{}`, `\Cref{}`, `\label{}`, `\textbf{}`, `\textcolor{}{}`
- All equation environments preserved exactly
- Commented-out English text kept as-is (lines with `%%`)
- `\newcommand{\PIC}...` inside figure environment preserved
- Colored text in equations (`\textcolor{blue}{}`, `\textcolor{red}{}`) preserved

### Translation Guidelines (4_method.tex)
- Source file: `4.0-method-new.tex`
- Target file: `body/graduate/paper3/4_method.tex`
- Section headings:
  - `\section{Phase-complement by Multiple Partitions}` → `\section{多重划分的相位补足}`
  - `\subsection{Analysis of the 1D Laplacian problem}` → `\subsection{一维拉普拉斯问题的分析}`
  - `\subsection{Multiple partitions for CMS}` → `\subsection{CMS 的多重划分}`
  - `\section{Schur- and eigen-free IMR}` → `\section{无 Schur 补和无特征求解的 IMR}`
  - `\subsection{Approximation of Low-frequency interface modes}` → `\subsection{低频界面模态的近似}`
- Additional terminology:
  - phase-complement → 相位补足
  - phase-complete → 相位完备
  - Primal-Dual → Primal-Dual (kept as-is)
  - basis functions → 基函数
  - eigenmodes → 特征模态
  - Dirichlet boundary conditions → Dirichlet 边界条件
  - Galerkin projection → Galerkin 投影
  - integrated error → 积分误差
  - frequency band → 频带
  - condensed matrices → 凝聚矩阵
  - memory footprint → 内存占用
  - staggered partitions → 交错划分
- Key translation decisions:
  - "phase-complement" used as verb phrase "进行相位补足" in Chinese
  - "phase-complete" translated as "相位完备" to describe the enriched basis
  - Primal/Dual kept as-is since they are technical terms in the method
  - All `\Cref{}` references preserved exactly
  - Math equations and `\label{}` preserved exactly
  - Figure captions translated but figure labels kept as-is
  - Colored text `\textcolor{}{}` commands preserved with translated content
- Commented-out sections (with `%%`) were NOT translated - left as-is per previous convention
- Figure environments fully translated including captions
- All `\includegraphics{}` paths preserved exactly
- Matrix notation preserved: $\mathbf{S}^p$, $\mathbf{S}^d$, etc.
- Subscript notation preserved: $p\leftarrow d$ notation kept as-is
- Source had two main sections that became two sections in target
- Original file was 329 lines with many commented-out sections; translated file is 128 lines (active content only)

### Translation Guidelines (5_implementation.tex)
- Source file: `4.1-implementation.tex`
- Target file: `body/graduate/paper3/5_implementation.tex`
- Section headings:
  - `\section{Implementation}` → `\section{实现细节}`
  - `\subsection{Regularization}` → `\subsection{正则化}`
  - `\subsection{Fast Reduced Matrix Assembly}` → `\subsection{快速缩减矩阵组装}`
  - `\subsection{Hybrid MPI/OpenMP Framework}` → `\subsection{混合 MPI/OpenMP 框架}`
  - `\subsection{Partition by METIS}` → `\subsection{基于 METIS 的划分}`
- Additional terminology:
  - singular matrix pencil → 奇异矩阵束
  - rank-deficient → 秩亏
  - null space → 零空间
  - regularization → 正则化
  - perturbation → 扰动
  - implicitly restarted Lanczos method → 隐式重启动 Lanczos 方法
  - near-null space → 近零空间
  - cut-off frequency → 截止频率
  - SE-free interface modes → SE-free 界面模态
  - static equilibrium equation → 静力平衡方程
  - vanish identically → 恒为零
  - boundary DOFs → 边界自由度
  - computational cost → 计算代价
  - sparsity patterns → 稀疏结构
  - computational unit → 计算单元
  - MPI rank → MPI 进程
  - communication graph → 通信图
  - axis-aligned → 轴向对齐的
  - graph-based partitioning → 基于图的划分
  - load balancing → 负载均衡
  - phase constraint → 相位约束
  - auxiliary substructures → 辅助子结构
  - vertex neighborhood → 顶点邻域
  - complementary partition → 互补划分
- Algorithm translation: `\caption{Adaptive shifting}` → `\caption{自适应位移}`
- Algorithm comments translated: `\tcp{Initial attempt}` → `\tcp{初始尝试}`
- Algorithm flow control keywords kept as-is: `\If`, `\While`, `\Else`, `\Return`, `\textbf{break}`
- Figure caption translated with preserved labels
- All `\Cref{}` and `\label{}` preserved exactly
- Colored text `\textcolor{}{}` preserved with translated content
- Commented-out English sections (with `%%`) kept as-is per previous convention
- Separate algorithm file created: `5_1_alg_adaptive_shifting.tex`

### Translation Guidelines (7_summary.tex)
- Source file: `6.0-conclusion.tex`
- Target file: `body/graduate/paper3/7_summary.tex`
- Section heading: `\section{Conclusion}` → `\section{本章小结}`
- Additional terminology:
  - phase deficiency → 相位缺失
  - phase-complete subspace → 相位完备的子空间
  - Schur- and Eigen-free formulation → 无 Schur 补和无特征求解的形式
  - computational overhead → 计算开销
  - scaling benchmarks → 可扩展性测试
  - three orders of magnitude → 三个数量级
  - rapid local updating → 快速局部更新
  - small inter-rank communication → 进程间通信量小
  - interior eigenproblems → 内部特征值问题
  - target shift → 目标位移
  - staggering → 交错划分
  - heuristic METIS adjustments → 启发式的 METIS 调整
  - adaptive partitioning schemes → 自适应划分方案
  - error estimators → 误差估计器
  - multi-level frameworks → 多层级框架
  - multiplicative efficiency gains → 乘积级的效率提升
  - phase adaptivity → 相位自适应性
- All `\cite{}` commands preserved exactly
- Paragraphs translated paragraph-by-paragraph, no summarization
- Future work and limitations sections clearly translated with appropriate Chinese academic phrasing

### Translation Guidelines (6_results.tex)
- Source file: `5.0-results.tex`
- Target file: `body/graduate/paper3/6_results.tex`
- Section heading: `\section{Results}` → `\section{实验结果}`
- Subsection headings:
  - `\subsection{Evaluation of accuracy and performance}` → `\subsection{精度与性能评估}`
  - `\subsection{Scalability}` → `\subsection{可扩展性}`
  - `\subsection{Comparison}` → `\subsection{方法对比}`
  - `\subsection{Extensibility}` → `\subsection{可扩展性}` (note: both Scalability and Extensibility translate to 可扩展性, context determines which)
- Additional terminology:
  - strong scaling → 强扩展性
  - weak scaling → 弱扩展性
  - embarrassingly parallel → 高度并行
  - coarse-grained → 粗粒度
  - fine-grained → 细粒度
  - wall-clock time → 挂钟时间
  - load balance → 负载均衡
  - eigenpairs → 特征对
  - ground truth → 基准解
  - error metrics → 误差度量
  - convergence plots → 收敛曲线
  - computational budget → 计算预算
  - benchmarks → 基准方法/基准测试
  - axis-aligned partition → 轴向对齐划分
  - irregular subdomains → 不规则子域
  - high-fidelity modes → 高保真模态
  - monolithic solvers → 整体式求解器
  - modularity → 模块化
  - local updates → 局部更新
  - topology modification → 拓扑修改
  - microstructures → 微结构
  - unit cell → 单元
  - lattice → 晶格
  - residual → 残差
- Algorithm translation:
  - `\caption{CMS with Multiple Partitions}` → `\caption{多重划分 CMS}`
  - Algorithm comments like `\tcp{Parallel Run...}` → `\tcp{并行运行...}`
- Figure captions fully translated
- All `\Cref{}`, `\label{}`, `\cite{}` preserved exactly
- Colored text `\textcolor{ConclusionEvidence}{}`, `\textcolor{IsConclusion}{}` preserved with translated content
- The `\input{5.1-statistics}` line was kept commented out as in source
- SLEPc, MUMPS, Cluster Pardiso kept as-is (software names)
- Falcon 9 rocket → 猎鹰 9 号火箭

### Algorithm Migration (5_1_alg_adaptive_shifting.tex)
- Source file used `algorithm2e` syntax
- Target file converted to `algorithmic` syntax (ZJU template standard)
- Syntax conversions:
  - `\KwIn` / `\KwOut` → not used in this algorithm
  - `\tcp{...}` → `\COMMENT{...}`
  - `\If{cond}{...}` → `\IF{cond} ... \ENDIF`
  - `\Else{...}` → `\ELSE ... \ENDIF`
  - `\While{cond}{...}` → `\WHILE{cond} ... \ENDWHILE`
  - `\Return` → `\RETURN`
  - `\BlankLine` → removed (left blank lines in code)
  - Removed all trailing `\;` (algorithm2e-specific)
  - `\textbf{break}` kept as-is
- Environment wrapper: `\begin{algorithm}[H]` + `\begin{algorithmic}[1]`
- All Chinese text and math expressions preserved exactly
- No compilation errors related to algorithmic syntax
- Compilation showed citation warnings (unrelated to algorithm migration)
- Plan: Fix `outer par mode` issues by ensuring blank lines before all \begin{figure} blocks in targeted TeX files and remove stray literal sequences carefully.
- Action taken: automated patch applied to 3_background.tex and 4_method.tex; inserted blank lines before figure environments; handled a corrupted 
  \newcommand line by restoring the missing backslash for \newcommand and ensuring macro definitions remain intact.
#HV|- Result: Initial compilation improved, but Not in outer par mode errors persisted elsewhere; next steps are to propagate the same blank-line strategy across all .tex files and re-run latexmk until a clean 0 exit status is achieved.
#XX|
#QQ|### 2026-03-03 Task: Fix rogue \\end{document} in 4_method.tex
#JB|- Task: Remove fatal \\end{document} tag from body/graduate/paper3/4_method.tex
#BR|- Investigation: Performed extensive searches using grep, strings, xxd, and direct file reading
#QQ|- Result: NO \\end{document} found in 4_method.tex - file is CLEAN
#BR|- Possible causes: Issue may have been fixed by previous agent runs, or was in a different file
#MM|- Workaround: Using latexmk with -f flag forces compilation past errors, produces 107-page PDF
#QQ|- Note: Without -f, compilation stops at 46 pages due to LaTeX errors (unclosed figure somewhere)
- Created style guidelines for Paper 3 translation focusing on '严谨、朴实' (Rigorous & Plain). Found massive AI-slop over-translations in 1_intro.tex (e.g. 逆转乾坤, 浩瀚天堑) compared to the calm English original.
