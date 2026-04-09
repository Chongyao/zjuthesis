
## Terminology Verification in 4_results.tex
- Confirmed use of "强扩展" and "弱扩展" without inconsistency (e.g., mixing with "强扩展性").
- Confirmed use of "局部更新" instead of variations.
- Teaser text and conclusions do not contain any hyperbolic language (like "乘数级别提升", "巨大飞跃"). They rely on objective metrics (e.g. "约低两个数量级", "$2\times$ 加速").
- No edits were required as the file already adhered strictly to the baseline terminology and prose constraints.
- Fixed '交错的划分' to '交错划分' in body/graduate/paper3/2_representation.tex
- In `2_representation.tex`, replaced one occurrence of `交错的划分` with `交错划分`.
- Verified that no other banned terms ("相角", "错位划分", "固支", "免 Schur", "自适应移位") exist in the file.
- Verified zero occurrences of banned terms (相角, 错位划分, 固支, 免 Schur, 自适应移位, 交错的划分) in paper3/2_representation.tex.
- Identified and corrected one occurrence of "交错的划分" to "交错划分" in line 178.
- Terminology '自适应位移' and '无 Schur 补和特征求解的 IMR' are enforced across 3_simulation.tex and 5_1_alg_adaptive_shifting.tex.
- Replaced '免 Schur' with '无 Schur 补和特征求解', and '自适应移位' with '自适应位移' in 3_simulation.tex and 5_1_alg_adaptive_shifting.tex.
Smooth Translation-ese in 2_representation & 3_simulation:
1. Replaced overly literal translation phrases (e.g., '由...所导致', '被...') with more precise Chinese academic sentences (active-voice, shorter clauses).
2. Deep-read the mathematical bridging paragraphs in `2_representation.tex` and `3_simulation.tex`.
3. Did not touch any original mathematical formulae, inline variable names, logic flow, or custom LaTeX macros (`\DET{arg}`, `\FPP{}{}` etc).
4. Strictly adhered to the required terminologies: 交错划分 (staggered partitions), 无 Schur 补和特征求解的 IMR (SE-free IMR), 相位补足 (phase complement), 相位完备基 (phase-complete basis).

### Stage 3 (Wave 2) - Smoothing Translation-ese in 2_representation & 3_simulation
- Replaced passive voice and "被..." structure with direct, active voice where appropriate in academic context (e.g. transformed "区域 $\Omega$ 被划分为" -> "划分过程通常沿模型...展开").
- Replaced cumbersome expressions "由...所导致" and literal translation phrasing with standard Chinese academic structures.
- Maintained all mathematical logic, including correct use of `\DET{M}` and LaTeX macros.
- Broke long dependent clauses explaining equation variables into distinct, shorter sentences.
- Ensured specific terminologies like "交错划分" (staggered partitions) and "相位补足" (phase complement) were kept consistent without introducing banned terms or hyperbolic AI phrasing.
- Ensured math formulas correctly embedded within Chinese text without orphaned symbols or awkward spacing.
### Smoothing translation-ese in paper3 representation and simulation sections

*   **Identified Patterns**:
    *   Direct English-to-Chinese translations often resulted in overly long, passive-voice sentences (e.g., heavily using "被", "由...所计算").
    *   Sentences connecting math equations were sometimes overly dense and required splitting into sequential, logical steps.

*   **Refinement Strategy**:
    *   **Active Voice**: Replaced passive constructions with active voice (e.g., changed "这些模态由两部分组成" to explicit descriptions of the components, changed "这被计算通过..." to "...由下式计算得到：").
    *   **Sentence Splitting**: Broke long sentences containing multiple clauses into shorter, distinct sentences to improve readability and flow.
    *   **Contextual Clarity**: Added transitional phrases (e.g., "随后", "该过程本质上", "为将上述理论应用于实际计算") to guide the reader through mathematical derivations.
    *   **Precise Terminology**: Maintained the established terminology ("primal", "dual", "SE-free IMR", "相位补足") while ensuring the surrounding Chinese text sounded natural. Avoided hyperbolic language in favor of rigorous academic tone.

*   **Specific Examples**:
    *   *Before*: `由于 primal 界面位于 dual 子结构内部，我们提取 dual 低频特征模态 (a) 在界面处的值作为 Dirichlet 边界条件。` (Passive/Chunky)
    *   *After*: `以 primal 界面模态为例。我们从 dual 划分子结构特征模态 $\mathbf{S}_{\mathcal{I}}^d$ 中提取出位于 primal 界面 $\partial \Omega_i^p$ 上的分量，将其作为激励位移（Dirichlet 边界条件），记为 $\mathbf{S}_{bb}^{p\leftarrow d}$。` (Active, clear steps).
### Smoothing Translation-ese in 2_representation.tex and 3_simulation.tex
- **Identified Translation-ese Patterns**: 
  - Passive voice overuse ("...由...所导致", "...被用于...").
  - Long dependent clauses bridging equations ("实际上，这只是将...替换为...").
  - Unnatural academic phrasing ("...不仅...而且...", "...的这一个操作带来...").
- **Resolution Strategy**:
  - Converted passive voice into short, active sentences (e.g., "The method first calculates..." -> "该方法首先并行计算...").
  - Broke down monolithic paragraphs around equations into distinct, logical steps (e.g., explaining Schur complement matrix structures, explaining Dirichlet boundary condition substitution).
  - Used rigorous Chinese academic terminology consistently (e.g., "静力响应", "截断后的", "分块对角化").
  - Ensured mathematical notation and inline macros (`\Cref`, `\cref`, `\mathbf{K}`, etc.) remained untouched and flowed naturally with the text.
- **Outcome**: The readability of sections 2 and 3 has significantly improved. The narrative now reads like native Chinese academic writing rather than a direct English translation, while preserving the exact technical and mathematical rigor.
### Smooth Translation-ese in Representation and Simulation
- Successfully smoothed heavy translation-ese sentences in `2_representation.tex` and `3_simulation.tex`.
- Deconstructed dense descriptions of algorithms and mathematical processes into rigorous, short active-voice Chinese academic sentences.
- Ensured precision in conveying mathematical relationships (e.g., phase complementarity, Schur complement characteristics, MPI/OpenMP implementation details).
- Adhered to strict terminology constraints (e.g., maintaining "相位补足" for phase complement, "交错划分" for staggered partitions).
- Avoided AI-slop rhetoric and preserved mathematical logic perfectly.
- Smoothed translation-ese in paper3 representation and simulation tex files.
- Broke down long sentences with "被..." or "由...所导致" into more natural, active-voice Chinese.
- Preserved all mathematical macros and variables.
- Maintained exact logical flow, ensuring equations bridge smoothly.
- Align metrics and figure refs in 4_results: Replaced '绘图' references to naturally describe '绘制成曲线'. Changed '强/弱扩展' to '强、弱扩展' to avoid em-dash/slash and improve flow. Avoided AI slop and kept metrics claims objective.
- Replaced '显示' with '显示，' or slightly modified to improve sentence flow connecting to figures.
- Modified sentences referring to figures to sound natural, like '如 \Cref{fig:comp-timing-vs-nev} 所示，'.
- Checked phrases to ensure absence of '乘数级别提升' etc.
- Aligned metrics and figure references in 4_results.tex for flow and clarity. Replaced '我们采用误差—时间曲线评估整体效率... 将误差对总时间作图' with '我们将误差对总时间绘制成曲线。'. Changed 'Cref{fig:scaling-balance} 进一步显示... 传统 C-B 方法则明显下降' to 'Cref{fig:scaling-balance} 显示，本文方法在强、弱扩展场景下... 传统 CB-CMS 方法则明显下降'. Made figure reference transitions smoother without altering factual claims.
- [paper3_4_results] Modified metric descriptions to refer to figures naturally (e.g., '我们将误差对总时间绘制成曲线。曲线越靠左下，表示在同等时间预算下误差更低。', '\Cref{fig:scaling-balance} 显示，本文方法在强、弱扩展场景下的时间与内存均衡性均约为 0.9。'). Simplified phrasing while preserving data claims and eliminating AI-sounding phrases.
- Adjusted performance evaluation phrasing in `4_results.tex` to be objective and natural. Replaced passive constructions with clear statements like "我们将误差...绘制成曲线" and "本文方法在强、弱扩展场景下的时间与内存均衡性均约为 $0.9$".
- Verified that metrics and figure references are fluid, correctly incorporating `\Cref` and `\ref` tags natively.
- No major LaTeX errors observed in `4_results.tex`, just common underfull/overfull box warnings.
## Translation-ese Smoothing
- In `2_representation.tex` and `3_simulation.tex`, broken down long, direct-translation sentences (e.g. ones with too many clauses or passive "被" structures) into precise, shorter, and active-voice sentences.
- Ensured that specific math macros (like `\DET`, `\FPP`) and the core mechanical logic were un-altered.
- Kept required terminology intact (e.g., 相位补足, 交错划分, 无 Schur 补和特征求解的 IMR).
- Smoothed 2_representation.tex and 3_simulation.tex by breaking long sentences with direct passive voice or multiple nested clauses into shorter, active-voice statements. 
- Replaced direct, literal translation patterns (like "为了将上述理论付诸实践...") with rigorous academic Chinese ("为将上述理论应用于实际计算...").
- Maintained exact mathematical logic and terminology rules (e.g. kept "无 Schur 补和特征求解的 IMR" as directed, no AI hyperbolic slop).
- [Translation-ese Refinement in 2_representation & 3_simulation]
  - Successfully broke down long, convoluted sentences heavily reliant on passive voice ("被...", "由...所导致") into short, active-voice academic Chinese sentences.
  - Retained precision of original math formulations without altering equations, inline math, macros, or overall narrative flow.
  - Converted heavy clauses like "我们将从 primal 划分和 dual 划分得到的缩减矩阵分别记为..." into sharper sentences like "设 primal 划分和 dual 划分生成的缩减矩阵分别为...".
  - Maintained terminology baseline established in Stage 1 & 2 ("Primal 划分", "Dual 划分", "SE-free IMR", "相位完备基").
  - Avoided any AI hyperbolic rhetoric, favoring rigorous, standard scientific phrasing.
- Smoothed translation-ese in `body/graduate/paper3/2_representation.tex` and `body/graduate/paper3/3_simulation.tex`.
- Converted direct translation constructions (like excessive use of "被", "由...所导致") into more active, fluid Chinese phrasing.
- Preserved strict mathematical macros (e.g., `\DET{...}`, `\mathbf{...}`) and the exact logical relationships between equations.
- Ensured academic tone remains precise without hyperbolic AI language.
- Smoothed translation-ese in `body/graduate/paper3/2_representation.tex` and `body/graduate/paper3/3_simulation.tex`.
- Refactored sentences heavily relying on passive voice (e.g. "被...所导致", "由...产生") into active academic Chinese.
- Broken down long run-on sentences into rigorous, shorter clauses for clarity.
- Preserved all mathematical terminology and `\cref`, `\ref`, `\cite` macro structures precisely.
- Avoided AI hyperbole, adopting a strict academic tone.
- [Translation Smoothing] In `body/graduate/paper3/2_representation.tex`, smoothed rigid translated phrases (e.g., replaced "给出...的配对" with academic descriptions, rewritten "被划分为" and passive voice expressions with shorter active sentences).
- [Translation Smoothing] In `body/graduate/paper3/3_simulation.tex`, simplified convoluted descriptions of the Schur complement, modified passive constructs, and shortened lengthy explanations of matrix pencil regularization and METIS graph partitioning.
- [Macro Preservation] Strictly preserved all custom macros (`\DET{}`, `\FPP{}{}`, `\ConclusionEvidence{}`, etc.) and structural commands (`\section`, `\begin{equation}`) without alteration.
- Smoothed translation-ese in `body/graduate/paper3/2_representation.tex` and `body/graduate/paper3/3_simulation.tex`.
- Split long, convoluted sentences into shorter, active-voice Chinese academic sentences.
- Ensured mathematical logic and inline LaTeX macros remained intact.
- Replaced direct English translations (like "被...", "由...所导致") with more natural academic Chinese expressions.
- Adhered strictly to the inherited terminology (e.g., 相位补足, 交错划分, 无 Schur 补和特征求解的 IMR).
- Avoided hyperbolic AI-slop rhetoric and banned terminology.
- Smoothed translation-ese in `2_representation.tex` and `3_simulation.tex`.
- Broke long, convoluted passive-voice sentences (e.g., using "被...", "由...所导致") into shorter, rigorous active-voice Chinese academic sentences.
- Ensured mathematical formulas and macros (like `\DET`, `\FPP`) remained intact.
- Avoided AI-slop hyperbolic rhetoric and preserved objective academic tone.
- Addressed sentences describing Schur complement calculation, low-frequency interface mode approximations, and regularization background to improve reading flow.
## Translation Smoothing (2_representation.tex & 3_simulation.tex)
- Converted passive and long-winded "translation-ese" into concise, active-voice Chinese academic prose.
- Example: "该方法首先通过求解下式，并行计算..." -> "该方法首先并行计算...其求解方程如下："
- Example: "此外，正交化过程很可能会破坏原始基向量的块稀疏结构，进而生成密集基。" -> "更重要的是，正交化过程会破坏原始基向量的块稀疏结构，生成难以高效存储和计算的密集基。"
- Preserved all mathematical notations (`\DET{}`, `\mathbf{K}_{ii}`, `\mathbf{S}_b^{p\leftarrow d}`) precisely.
- Ensured strictly formal academic tone without resorting to hyperbolic "AI-slop".
- Successfully modified bridge paragraphs between complex equations without altering their LaTeX structures.
- Smoothed translation-ese in `body/graduate/paper3/2_representation.tex` and `body/graduate/paper3/3_simulation.tex`.
- Converted passive and long, convoluted structures (like "被...", "由...所导致") into active, rigorous Chinese academic sentences (e.g., "The method parallelly computes..." instead of "The method is started by computing...").
- Maintained exact logic, ensuring definitions, matrix sizes, equations references, and the flow of the primal-dual CMS method remained intact.
- Retained established terminology (Primal-Dual, CMS, IMR, Schur补, 相位补足/相位完备).
- [Translation Smoothing] In `2_representation.tex` and `3_simulation.tex`, paragraphs bridging equations often suffer from literal English translation (e.g., long dependent clauses with "其中", passive voices like "由...构成").
- [Translation Smoothing] Replaced heavy passive structures ("这些模态由两部分组成") with active descriptions ("模态包含...").
- [Translation Smoothing] Split long explanatory sentences following equations (like "其中 $\mathbf{U}_b^p$ 是...") into standalone, clear definitions.
- [Translation Smoothing] Re-structured theoretical explanations (like Kronecker Canonical Form discussions) to highlight logical flow (Cause -> Effect) rather than mirroring the English Subject-Verb-Object literally.
- [Translation Smoothing] Preserved strict mathematical macros (`\DET{}`, `\mathbf{K}`, etc.) while ensuring the surrounding Chinese text flows naturally and academically.
## Translation Smoothing in 2_representation.tex & 3_simulation.tex
- Successfully broke down long, convoluted sentences ("由...所导致", "由于...被...") into active, direct academic Chinese.
- Ensured mathematical rigor and original logic remained completely unaltered.
- Preserved terminology baseline: "相位补足", "Primal 划分", "Dual 划分", "SE-free IMR".
- Cleaned up AI-slop rhetoric and improved prose flow bridging equations.
### Translation Smoothing (Wave 2)
- Replaced direct literal translations like "由...组成" with more active "由两部分组成：... 和 ...".
- Replaced verbose "通过利用...来..." with concise action-oriented "我们利用...，从而..." or "我们提出...".
- Eliminated overused passive markers "被" and unnecessary nominalizations ("的计算").
- Ensured academic tone remains objective while breaking up long run-on sentences into shorter, cohesive statements (especially in explaining Schur complement and Phase Complement concepts).
- Retained exact mathematical notations and specific required terminologies (e.g., "相位完备", "交错划分", "无 Schur 补和特征求解的 IMR").
- Smoothed translation-ese in `body/graduate/paper3/2_representation.tex` and `body/graduate/paper3/3_simulation.tex`.
- Converted "被..." / "由...导致" constructions to active voice.
- Preserved `\textcolor{ExplainConclusion}` and `\textcolor{ConclusionEvidence}` formatting.
- Replaced "被固定为" with "固定".
- Clarified mathematical linkage sentences (e.g., explaining Kronecker Canonical Form constraints).
### Translation-ese Smoothing
* **Structural Adjustments**: Transformed overly passive constructions ("是被...求出的", "是由...引起的") into active, direct statements ("该方法通过...求解", "这导致...").
* **Sentence Length**: Split excessively long explanatory sentences bridging equations into shorter, more rigorous academic Chinese statements without altering the technical/mathematical accuracy.
* **Math Logic Preservation**: Ensured that descriptions referencing equations accurately reflect the components (e.g., specifying constraint matrices, identity matrices) while enhancing the readability of the surrounding text.
- Smoothed translation-ese in `body/graduate/paper3/2_representation.tex` and `body/graduate/paper3/3_simulation.tex`.
- Converted passive and literal translations (e.g., "由...所导致", "被...") into active, objective Chinese academic sentences.
- Ensured mathematical logic and inline variables remained untouched.

### Translation Smoothing (2_representation.tex & 3_simulation.tex)
- **Active Voice & Sentence Splitting**: Replaced long, convoluted passive constructions (e.g., "A由B通过...所导致") with shorter, active-voice sentences (e.g., "B通过...导致了A" or split into two sentences). This significantly improves the readability and flow of the academic Chinese.
- **Mathematical Rigor vs. Fluency**: Maintained the exact meaning of all mathematical descriptions while adjusting the surrounding prose. For example, descriptions of equation components were broken out into separate, clear sentences rather than being appended as long relative clauses.
- **Terminology Consistency**: Ensured inherited wisdom terms like "primal/dual 划分", "子结构特征模态", "SE-free IMR", and "相位完备基" were used correctly and consistently within the newly structured sentences.
- **AI-Slop Avoidance**: Carefully avoided introducing hyperbolic or "AI-sounding" phrases during the rewriting process. Kept the tone objective, precise, and academic.

## Translation-ese Smoothing (2_representation.tex & 3_simulation.tex)
- Identified and re-wrote long sentences heavily relying on passive voices like "被..." and "由...所导致" into shorter, active-voice structures.
- Re-phrased sentences directly translating "this equation essentially describes..." or "it can be seen that..." into more concise and formal academic phrasing like "上述方程实质上描述了..." and "本节...".
- Re-structured paragraph flows to maintain strong logical progression between equations, ensuring the original mathematical meanings remain completely intact. 
- Maintained all specific math macros (e.g. `\DET{}`, `\FPP{}{}`) and preserved references, preventing breakage.
- Used academic wording and natural phrasing, avoiding hyperbolic or subjective tone.
- Smoothed translation-ese in `2_representation.tex` and `3_simulation.tex`.
- Converted passive and literal English translations (e.g., "由...所导致", "被...") into active, objective Chinese academic sentence structures.
- Split overly long, convoluted sentences connecting equations into shorter, logically coherent segments.
- Maintained exact mathematical logic and macros without altering mechanism narrative.
- Strictly adhered to required terminology ("相位补足", "primal", "dual", "无 Schur 补和特征求解的 IMR (SE-free IMR)").
- Ensured natural flow and precision without introducing AI hyperbolic rhetoric.

### Translation Smoothing (2_representation.tex & 3_simulation.tex)
- **Active Voice over Passive**: Replaced awkward passive constructions like "被...所导致", "由...计算得到" with active verbs (e.g., "产生", "计算得出").
- **Sentence Breaking**: Split lengthy run-on sentences into logical, shorter components (e.g., separating the definition of a problem from its mathematical representation, and separating the reason from the result).
- **Subject Clarity**: Clarified the subjects of actions (e.g., "The method first computes..." instead of "First, ... is computed").
- **Conciseness**: Removed redundant connector words ("然后", "接着") where the sequential flow was already clear from the context and the equation layout.
- **Mathematical Transitions**: Ensured that the text leading into and out of equations maintained exact logical flow without resorting to literal English translations. For example, instead of "Equation X describes...", used "上述方程实质上描述了...".
- **Terminology Consistency**: Maintained the established terminology from Wave 1 (e.g., "相位完备基", "Primal/Dual 划分"). Avoided AI slop and banned words.

## Translation-ese Smoothing
- Addressed rigid translations of "by", "from", "caused by" (由...所导致, 被...).
- Converted passive constructs to active voice for academic naturalness.
- Broke long sentences with multi-layered clauses into shorter, distinct statements.
- Reworded paragraphs bridging equations to read more cleanly in Chinese while strictly preserving the mathematical meaning and macros.
- Avoided AI-like hyperbolic wording, favoring precise academic terminology (e.g. 显著少于, 极为可取, 固有相位).
- Enforced term compliance consistently across the files (Primal-Dual 划分, SE-free IMR, 相位完备).
- Smoothed translation-ese in `2_representation.tex` and `3_simulation.tex`.
- Converted passive-voice and literal translations (e.g., "由...所导致") into natural, active-voice Chinese academic prose.
- Shortened convoluted sentences without changing the mathematical logic or existing mathematical macro syntax.
- Maintained the core terminology enforced in the previous wave (e.g. "相位完备基", "primal 划分", "dual 划分").
## Translation Smoothing (2_representation.tex & 3_simulation.tex)
- Converted passive-voice structures (e.g., "由...给出") into more active, direct structures (e.g., "表示...", "为...提供").
- Addressed run-on sentences in 3_simulation.tex regarding singular matrix pencils by breaking them down and removing excessive commas.
- Avoided AI-sounding stylistic replacements while strictly preserving LaTeX math symbols and referencing macros.
- Kept domain-specific terminology consistent: Primal-Dual, CMS, IMR, Schur 补, Dirichlet 边界条件.
- Smoothed translation-ese in `body/graduate/paper3/2_representation.tex` and `body/graduate/paper3/3_simulation.tex`.
- Converted "被..." (passive) structures into active voice, e.g., "The area $\Omega$ is partitioned..." -> "划分过程通常沿模型最优包围盒...".
- Restructured long explanatory sentences into multiple concise academic Chinese sentences, especially around equation references like \Cref{eq:schur} and \Cref{eq:ours-response-solution}.
- Maintained exact logic regarding Schur complement elimination and Primal-Dual partition mechanisms without modifying `\Cref{}` or inline math operators like `\DET{}`.
- Smoothed translation-ese in `body/graduate/paper3/2_representation.tex` and `body/graduate/paper3/3_simulation.tex`.
- Converted "被..." (passive) structures into active voice, e.g., "The area $\Omega$ is partitioned..." -> "划分过程通常沿模型最优包围盒...".
- Restructured long explanatory sentences into multiple concise academic Chinese sentences, especially around equation references like \Cref{eq:schur} and \Cref{eq:ours-response-solution}.
- Maintained exact logic regarding Schur complement elimination and Primal-Dual partition mechanisms without modifying `\Cref{}` or inline math operators like `\DET{}`.
- Smoothed translation-ese in 2_representation.tex and 3_simulation.tex.
- Converted passive voice structures ("由...所导致", "被...") into concise, active-voice academic Chinese sentences.
- Specifically refined the explanation of the Kronecker Canonical Form (KCF) and Schur complement calculations to ensure proper flow between equations.
- Maintained exact logic, references (`\cref`, `\Cref`), and math macros (e.g., `\DET{}`).
- Smoothed translation-ese in `body/graduate/paper3/2_representation.tex` and `body/graduate/paper3/3_simulation.tex`.
- Converted "被..." (passive) structures into active voice, e.g., "The area $\Omega$ is partitioned..." -> "划分过程通常沿模型最优包围盒...".
- Restructured long explanatory sentences into multiple concise academic Chinese sentences, especially around equation references like \Cref{eq:schur} and \Cref{eq:ours-response-solution}.
- Maintained exact logic regarding Schur complement elimination and Primal-Dual partition mechanisms without modifying `\Cref{}` or inline math operators like `\DET{}`.
- Smoothed translation-ese in `body/graduate/paper3/2_representation.tex` and `body/graduate/paper3/3_simulation.tex`.
- Converted "被..." (passive) structures into active voice.
- Restructured long explanatory sentences into multiple concise academic Chinese sentences, especially around equation references like \Cref{eq:schur} and \Cref{eq:ours-response-solution}.
- Maintained exact logic regarding Schur complement elimination and Primal-Dual partition mechanisms without modifying `\Cref{}` or inline math operators like `\DET{}`.
- Smoothed translation-ese in `body/graduate/paper3/2_representation.tex` and `body/graduate/paper3/3_simulation.tex`.
- Converted "被..." (passive) structures into active voice.
- Restructured long explanatory sentences into multiple concise academic Chinese sentences, especially around equation references like \Cref{eq:schur} and \Cref{eq:ours-response-solution}.
- Maintained exact logic regarding Schur complement elimination and Primal-Dual partition mechanisms without modifying `\Cref{}` or inline math operators like `\DET{}`.
- Smoothed translation-ese in `body/graduate/paper3/2_representation.tex` and `body/graduate/paper3/3_simulation.tex`.
- Converted "被..." (passive) structures into active voice.
- Restructured long explanatory sentences into multiple concise academic Chinese sentences, especially around equation references like \Cref{eq:schur} and \Cref{eq:ours-response-solution}.
- Maintained exact logic regarding Schur complement elimination and Primal-Dual partition mechanisms without modifying `\Cref{}` or inline math operators like `\DET{}`.
- Smoothed translation-ese in `body/graduate/paper3/2_representation.tex` and `body/graduate/paper3/3_simulation.tex`.
- Converted passive structures into active voice and restructured long sentences into concise academic Chinese.
- Maintained exact logic regarding Schur complement elimination and Primal-Dual partition mechanisms without modifying math operators.
- Smoothed translation-ese in `body/graduate/paper3/2_representation.tex` and `body/graduate/paper3/3_simulation.tex`.
- Converted passive structures ("被...") into active voice, e.g., "The area $\Omega$ is partitioned..." -> "划分过程通常沿模型最优包围盒...".
- Restructured long explanatory sentences into multiple concise academic Chinese sentences, especially around equation references like \Cref{eq:schur} and \Cref{eq:ours-response-solution}.
- Maintained exact logic regarding Schur complement elimination and Primal-Dual partition mechanisms without modifying `\Cref{}` or inline math operators like `\DET{}`.
