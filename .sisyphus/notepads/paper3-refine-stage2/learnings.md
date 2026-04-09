## 1_intro.tex Rewrite P1-P3 (Stage 2)

- **What was changed**: 
    - Rewrote the opening paragraph (P1) to maintain its role as a thesis chapter transition while stripping away overly emotional or dramatic phrases (like "逆转乾坤", "浩瀚天堑", "最致命瓶颈"). Replaced them with more restrained, academic phrasing ("消除不良数值刚度的策略", "计算瓶颈发生了系统性的转移").
    - Rewrote P2 to faithfully mirror the original English text (`1.0-introduction.tex`), focusing on the strengths and weaknesses of global solvers (SLEPc, MUMPS), highlighting scalability issues due to ill-conditioning and the lack of flexibility for design iterations.
    - Rewrote P3 to align with the original text discussing Component Mode Synthesis (CMS). Kept the terminology consistent with the baseline (模态综合法, Schur 补, etc.) and accurately reflected the trade-off CMS makes (sacrificing convergence/accuracy for workflow efficiency and reusability) and the core observation of the paper (spatially staggered partitions/空间错位划分 provide phase-complementary bases).
- **Why**: To ensure the text adheres to the "严谨、朴实" (rigorous, plain) academic style required for the thesis while remaining completely faithful to the technical claims and logic of the original English paper. Removed the "AI-slop" and literary embellishments present in the previous draft.

## 1_intro.tex Rewrite P4-P7 (Stage 2)

- **What was changed**:
    - **P4-P5 (CMS and IMR review)**: Rewrote the related work sections on Component Mode Synthesis (CMS) and Interface Mode Reduction (IMR) to ensure formal, objective language. Replaced dramatic or colloquial phrasings ("浩如烟海", "灾难", "疯狂补充") with more rigorous academic terminology ("网格规模庞大时尤为明显", "计算效率显著下降").
    - **P6-P7 (Partitions and Singular matrix pencil)**: Kept the structure faithful to the original English draft. Translated "Singular matrix pencil" to "奇异矩阵束" and "deflate" to "提取" (deflate is often translated this way in numerical linear algebra, or as 降阶/消除, here "提取（deflate）" or "消除" is acceptable, but the overall tone is now strict and objective). Removed any promotional language.
    - **P8 (Contributions)**: Restructured the final bullet points. Replaced exaggerated terms like "狂飙突破 3 个甚至更大量的精度进阶数量级提升跨度优势" and "无解工业实战应用红利优势" with precise statements ("相比传统 CMS 系列方法实现了三个数量级以上的精度提升", "重点展示了本方法在工业应用中的两项优势"). Ensure terms like "错位多重网格划分融合策略", "无 Schur 补", and "超高效 IMR 结构" are used directly without excessive adjectives.
- **Why**: To maintain the "严谨、朴实" (rigorous, plain) academic style required for the thesis while remaining completely faithful to the technical claims and logic of the original English paper. Replaced all remaining AI-slop and literary embellishments with standard scientific writing conventions.
- Mechanism translation: P8-P12 rewritten to explicitly describe (1) high-frequency orthogonal penalty of CMS, (2) phase deficiency of fixed-interface bases, (3) phase-complement mechanism of staggered partitions, and (4) formulation of Schur-/eigen-free IMR via local static equilibrium equations with boundary constraints from the other partition. Kept tone plain and rigorous.
- **P8-P12 Rewrite**: Maintained objective academic tone. Clarified that higher frequency modes from fixed-interface CMS are inefficient because they are nearly orthogonal to target global modes. Explained that fixed-interface modes can be seen as windowed Fourier modes with restricted phases, and that a second staggered partition naturally provides phase-complementary bases. Described the Schur-/eigen-free IMR approach which replaces dense interface eigenproblems with static equilibrium problems whose boundary conditions come from the other partition's eigenmodes. Kept standard terminology (模态综合法, Schur 补, 界面模态缩减法, 交错划分).
- **Paper 3 mechanism transition**: Maintained stability of technical terminology (模态综合法, Schur 补, 交错划分) and accurately described the phase complementary effect across staggered partitions avoiding exaggerated non-academic phrasing. Schur-free IMR is defined as replacing computationally heavy Schur complement eigendecompositions with static equilibrium problems leveraging constraints mapped from a staggered partition.


- Rewrite mechanism chain carefully, emphasizing the phase mismatch problem and the staggered partition's phase complementary nature.
- Describe Schur-free interface modes as static equilibrium problems solved with locally extracted boundary conditions instead of dense eigensolves.
- Adhere strictly to the requested professional academic tone.

## P8-P12 Translation Strategy
- Retained rigorous, sober tone ("为了提高精度，通常需要提高截断频率以包含更多的子结构特征模态" instead of exaggerated phrasing)
- Accurately conveyed the technical details of slow convergence: higher modes being nearly orthogonal.
- Accurately framed the fixed-interface modes as windowed Fourier modes with zero phase at the boundary, and how the staggered partition acts as a phase-complement.
- Accurately communicated the Schur- and eigen-free IMR concept: solving local static equilibrium problems constrained by eigenmodes from the alternative partition, avoiding dense eigensolves entirely.
- Kept terminology consistent: 模态综合法, 界面模态缩减法, Schur 补, 交错划分, 相位互补.
- P8-P12 rewritten to faithfully convey the phase-complement idea, the Schur-free idea and to use stable terminology (模态综合法, 界面模态缩减法, Schur 补, 相位互补, 交错划分).
- Translated mechanism transition (P8-P12) in 1_intro.tex to rigorous academic Chinese without exaggerated terms. Phase deficiency correctly framed as boundary restrictions, and Schur-free IMR described as using mapped boundary conditions.
- Mechanism translation for CMS convergence and phase deficiency: 
  - Ensure the analogy of "windowed Fourier modes with fixed phase constraints" is translated naturally.
  - Using "加窗傅里叶模态" and "相位约束" correctly conveys the mathematical intuition without being hyperbolic.
  - Highlighted that simply increasing high-frequency modes is inefficient due to near-orthogonality with target modes.
- Staggered partition terminology: 
  - Adopted "交错划分" to describe the spatially staggered dual partition.
  - "自然形成了一种空间上的相位互补关系" perfectly captures the essence of "phase-complement" basis functions.
- Schur-/eigen-free IMR structure translation: 
  - Conveyed the heavy cost of interface modes explicitly as the "Schur complement assembly and dense eigenvalue problems".
  - Explained that the new method uses "静力平衡问题" (static equilibrium problems) with boundary conditions mapped from existing eigenmodes, rather than "无脑" or "掐断" phrases.
- Rewrite of P8-P12 completed. Replaced exaggerated phrasing with rigorous academic terms ("相位互补", "无特征值运算").
- Preserved existing macros (\DET{}, \cite{}).
- Used static equilibrium concepts to explain SE-free interface modes.

### Intro P8-P12 Rewrite
- **Mechanism clarity:** Kept the logical chain from the English paper: traditional CMS lacks phase complementarity -> fixed-interface modes are windowed Fourier modes -> multiple staggered partitions supply different phases.
- **IMR framing:** Emphasized the "Schur-free" and "eigen-free" nature of the proposed interface mode reduction, tying it to solving local static equilibrium problems.
- **Tone:** Kept it rigorous ("空间错位划分", "相位互补", "静力平衡问题"), avoiding hyperbolic slogans.

### Task 3 (P8-P12 Rewrite)
- **Problem**: Translating the mechanism of slow convergence in CMS, phase deficiency, staggered partitions, and Schur-free IMR.
- **Solution**:
  - Replaced P8 with a rigorous explanation: "为了提高精度... 但随着子结构特征模态数量的增加... 这些额外的基函数与目标模态几乎正交..."
  - Replaced P9-P11 with the "固定界面模态受限于人工截断边界，可以视为相位约束的加窗傅里叶模态" and "第二套交错划分提供空间上的相位互补".
  - Replaced P12 with the explanation of Schur complement computation cost and how IMR with local static equilibrium equations using mapped boundary conditions resolves it.
  - Used formatting consistently (`\textcolor{ExplainConclusion}`, `\textcolor{IsConclusion}`).
- **Key Terms Maintained**: 模态综合法 (CMS), 界面模态缩减法 (IMR), Schur 补, 相位互补, 交错划分.
- **Verification**: `latexmk` passed.
## P8-P12 Rewrite Learnings
- **Mechanism explanation**: Replaced vague descriptions with concrete academic language. Explained that traditional CMS basis functions are fixed-phase (Dirichlet), making them orthogonal to global modes and causing slow convergence. 
- **Phase complement**: Clarified that a second staggered partition provides basis functions in the same frequency band but with different phases, naturally complementing the missing phase information.
- **Schur-free IMR**: Explained that traditional IMR requires expensive Schur complement assembly and dense eigenproblems. The proposed method replaces this by solving local static equilibrium problems with boundary conditions mapped from the other partition's eigenmodes, avoiding interface assembly entirely.
- **Tone**: Maintained "严谨、朴实" style, avoiding exaggerated terms while preserving technical accuracy.
- For paragraphs explaining mathematical concepts in plain Chinese, strictly maintain terms like 相位缺失 (phase deficiency) and 相位互补 (phase-complement) without exaggeration.
- For P8-P12 in 1_intro.tex, maintained academic Chinese tone: 严谨、朴实.
- Explained CMS convergence issues, phase deficiency (fixed-interface modes as windowed Fourier modes with restricted phases), and how staggered partitions provide phase-complementary bases.
- Explained Schur-free IMR: replacing expensive interface eigenvalue problems and Schur complement computations with local static equilibrium problems mapped from another partition's eigenmodes.

### Task 3 (P8-P12 Rewrite)
- **Problem:** The original CMS explanation was too vague, failing to explain *why* high-frequency modes cause slow convergence (nearly orthogonal to global modes).
- **Mechanism Restored:** Explicitly connected fixed-interface boundary constraints to windowed Fourier modes with fixed phases. Explained that adding more high-frequency modes cannot efficiently compensate for missing phase information.
- **Phase Complement:** Clarified that the staggered partition provides basis functions in similar frequency bands but with different phases, naturally complementing the missing phase information.
- **Schur-Free IMR:** Explained that traditional IMR relies on expensive Schur complement assembly and dense eigenproblems. The proposed method uses static equilibrium equations on local substructures with boundary conditions mapped from the other partition, entirely avoiding Schur complement computation and dense eigen-solves.
- **Tone:** Maintained plain academic language (严谨、朴实), avoiding exaggerated buzzwords. Preserved original citations and LaTeX structures.
- **P8-P12 Rewrite**: Successfully rewrote the mechanism transition. Simplified the explanation of why traditional CMS converges slowly (high-frequency modes are orthogonal) and explained the phase-complement idea from staggered partitions clearly using plain academic Chinese ("相位互补", "交错划分").
- **Schur-free IMR**: Replaced the expensive Schur complement and dense eigenvalue problems with local static equilibrium equations using mapped boundary conditions. Maintained rigorous tone ("无特征值运算", "静力平衡问题") avoiding AI slogans.
- Rewrite P8-P12 in 1_intro.tex (Phase-complement and Schur-free IMR explanation): Used plain academic Chinese ('错位划分', '相位互补'). Successfully removed exaggerated terms while preserving technical accuracy.

## P8-P12 Rewrite
- **Mechanism Explanation:** Kept the explanation of CMS phase deficiency precise by comparing it to "windowed Fourier modes with phase restricted by artificial boundaries" (加窗傅里叶模态，受限于人工截断边界), emphasizing the "spatial phase complementary" (空间上的相位互补) nature of the staggered partition.
- **IMR Transition:** Clarified that Schur complement and dense eigenproblems are the true bottlenecks. Framed the proposed method as converting the interface eigensolve into a set of "static equilibrium problems" (静力平衡问题) where boundaries are inferred from the other partition, effectively bypassing the expensive assembly and solving steps.
- In 1_intro.tex, carefully preserved the plain and rigorous academic tone when rewriting the mechanism section, avoiding exaggerated terms while fully translating the theoretical meaning of staggered partitions (空间错位划分) and Schur-free/eigen-free local IMR.

### Task 3: P8-P12 Rewrite
- Fixed CMS convergence issue description by strictly matching the mechanism from the original English text (high-frequency modes being nearly orthogonal).
- Maintained the "fixed-interface normal modes as windowed Fourier modes with fixed phase" mechanism.
- Staggered partition (交错划分) phrasing stabilized and explained as providing phase-complementarity without jargon.
- Retained Schur-free IMR mechanism: avoiding expensive interface eigensolves by solving local equilibrium equations with boundary conditions from the other partition's eigenmodes.
- Used plain, rigorous tone avoiding exaggerated words like "颠覆".
- Resolved line ending/format issues during edits by carefully matching line ranges and using `cat`/`edit`.

### Task 3 (P8-P12 Rewrite)
- Replaced "收敛速度往往不尽如人意" with a precise explanation of the mechanism (higher frequency modes being nearly orthogonal).
- Introduced the concept of phase deficiency ("加窗傅里叶模态", "相位约束") and explained why staggered partitions help ("相位互补关系").
- Explained why interface modes are expensive ("Schur 补", "稠密的特征值问题", "平方级增长").
- Clarified the SE-free IMR mechanism: avoiding Schur complement/eigensolves by using local static equilibrium problems with boundary conditions mapped from the other partition.
- Kept the tone academic and rigorous, avoiding exaggerated marketing terms.
- Intro mechanism translation: Rewrote CMS convergence issues, phase complement, and Schur-free IMR using plain academic Chinese without exaggerated terminology.
- Mechanism of slow convergence for CMS explained: Substructure eigenmodes have fixed phases at boundaries, so approximating global modes requires high-frequency modes that are nearly orthogonal to the target, making them inefficient.
- Staggered partitions: A second partition provides basis functions in similar frequency bands but with different phases, achieving phase complement and enriching the subspace.
- SE-free IMR mechanism: Replaces costly dense Schur complement assembly and local eigenvalue problems with local static equilibrium problems. Boundary conditions are inferred from existing eigenmodes of the other partition.
- Preserved original terminology: 模态综合法 (CMS), 界面模态缩减法 (IMR), Schur 补, 固定界面模态, 相位互补, 交错划分.
- In `1_intro.tex`, the mechanism explanation for why traditional CMS converges slowly and how multiple staggered partitions resolve phase deficiency has been rewritten to be more rigorous and thesis-appropriate.
- Explained the Schur-free/eigen-free IMR concept as translating interface mode computation into local structural static equilibrium problems using mapped boundary conditions, bypassing costly Schur complement assemblies.
- Avoided using exaggerated terms like "铁锁" or "惊艳", favoring standard terminology like "相位约束" and "空间错位划分".
- Verified that `latexmk` builds the document successfully with no errors after updates.

### Stage 2 - Intro P8-P12 Rewrite

*   **Mechanism Explanation:** Traditional CMS converges slowly because substructure modes with fixed interfaces act like windowed Fourier modes with restricted phases. Additional higher-frequency modes are nearly orthogonal to the target low-frequency global modes, making them inefficient.
*   **Staggered Partitions:** Introducing a second, spatially staggered partition provides basis functions in the same frequency band but with different phases (phase complement), effectively enriching the subspace for low-frequency global modes.
*   **Schur-free IMR:** Interface modes traditionally require expensive Schur complement assembly and dense eigenproblems. The new method leverages the staggered partitions: an interface in one partition often falls inside a substructure of the other. Thus, the interface modes are computed via local static equilibrium problems, with boundary conditions mapped from the other partition's eigenmodes, completely bypassing Schur complements and local eigensolves.
*   **Tone:** The rewrite uses plain, rigorous academic Chinese ("交错划分" for staggered partition, "相位互补" for phase complement, "静力平衡问题" for static equilibrium problems), avoiding exaggerated phrases like "颠覆" or "死循环病灶".

### Task 3: P8-P12 Intro Mechanism Translation
- **Method Framing**: 
  - Framed phase deficiency as the limitation of fixed-interface boundaries constraining windowed Fourier modes. 
  - Framed the staggered partition (交错划分) as naturally supplying the missing phase information in the same frequency band.
  - Framed the Schur-/eigen-free IMR as replacing dense interface eigenvalue problems with local substructure static equilibrium problems mapped from the staggered partition.
- **Tone**: Used rigorous, plain academic Chinese. Avoided marketing buzzwords or aggressive terms.
- **Integration**: Preserved `\textcolor` elements indicating the logical flow of Conclusion->Evidence. Maintained correct formatting of LaTeX blocks.
- Use `\textcolor{IsConclusion}{}` or similar only when rewriting directly relates to existing marked blocks. Kept plain academic style without exaggerated words for the method transition.
- Explained phase deficiency as windowed Fourier modes lacking phase degree of freedom, complemented by staggered partitions.
- Explained Schur-free interface modes via static equilibrium mappings instead of "choking the bottleneck" slogans.
- Mechanism translation: Converted the math-heavy description of phase deficiency into intuitive plain Chinese (加窗傅里叶模态, 相位约束), matching the original English intent without losing rigor.
- Used "交错划分" to consistently describe "staggered partition", maintaining the established terminology.
- Preserved thesis-specific colors (`\textcolor{ExplainConclusion}`, `\textcolor{IsConclusion}`) during the rewrite.
- Emphasized that Schur complement and interface eigenvalue decomposition are avoided by solving a local static equilibrium problem, fulfilling the Schur-free/eigen-free IMR concept.
- Mechanism translation: Explain mechanism accurately and without hype phrases.
  - Slower convergence in CMS corresponds to phase deficiency. Local fixed-interface modes can be seen as windowed Fourier modes subject to artificial phase constraints from boundaries. Expanding the frequency bandwidth fails to correct the phase shift effectively.
  - Phase compensation is achieved via a staggered partition, providing overlapping boundary regions that recover phase information missing from the primal partition.
  - Schur-free interface reduction bypasses expensive Schur complement eigen-solves. The dense matrix Schur-complement calculation scales quadratically with interface nodes, creating bottlenecks. Instead of assembling Schur components, interface modes are represented directly through localized static equilibrium mappings whose Dirichlet boundary conditions are inherently informed by the overlapping subset of eigenmodes generated from the dual partition.
- Mechanism translation: Converted "high-frequency modes are orthogonal" and "phase deficiency" concepts into precise academic Chinese. Used "加窗傅里叶模态" and "空间错位划分" to accurately describe the phase-complement idea.
- Schur-/eigen-free translation: Avoided exaggerated marketing terms ("铁锁", "踢出整体链路"). Instead, rigorously explained the replacement of Schur complement and dense eigensolves with local static equilibrium problems mapped from adjacent partitions.

## P8-P12 Rewrite Learnings
- Mechanism of slow convergence for CMS was reframed as 'additional modes have higher frequencies and are almost orthogonal to target global modes'.
- Phase deficiency was framed as 'fixed-interface modes are windowed Fourier modes with phase constrained by artificial boundaries'.
- Spatially staggered partitions supply complementary phase information without computing very high frequency modes.
- IMR bottleneck was explained as the $\mathcal{O}(n^3)$ cost of dense Schur complement matrix assembly and interface eigensolving.
- The SE-free method replaces interface eigensolves with static equilibrium problems with boundary conditions mapped from another partition.

- In mechanism explanations, explicitly referencing physical interpretations (e.g., phase-constraint from artificial boundaries) helps ground abstract linear algebra arguments.
- For performance discussion, tying complexity ($\mathcal{O}(n^3)$ or quadratic memory growth) to specific system structures (like dense interface DOFs) makes the motivation robust.

## Intro Mechanism Translation (P8-P12)
- Replaced exaggerated phrasing ("铁锁", "死循环病灶", "颠覆") with rigorous academic terminology ("人工截断边界", "受限于其人工截断边界", "无特征值运算的超高效 IMR 构造策略").
- Explained phase-complement mechanism clearly: fixed-interface modes are like windowed Fourier modes with fixed phase due to truncation boundaries. Adding a second staggered partition provides basis functions in similar frequency bands but with different phases, naturally complementing the phase information.
- Explained Schur-free IMR mechanism clearly: instead of computing dense Schur complements and expensive interface eigensolves, interface modes are solved via local static equilibrium problems on substructures, using boundary conditions mapped from existing eigenmodes of the staggered partition.
- Use `\textcolor{IsConclusion}{}` or `\textcolor{ExplainConclusion}{}` to annotate structural points for reviewer reference when necessary.
- Avoid abstract slogans like "颠覆" or "死循环病灶", prefer technically accurate descriptions like "子结构局部的固定界面模态本质上受限于其人工截断边界，可以视为在子域内施加了相位约束的加窗傅里叶模态".
- Mechanism chain refactoring in `1_intro.tex`: Replaced vague statements with the correct mechanism chain (slow convergence due to high-frequency and near-orthogonal nature of extra modes, phase constraint analogy to windowed Fourier modes, staggered partition as phase-complement).
- Re-established exact technical terms: `交错划分` (staggered partition), `固定界面模态` (fixed-interface modes), `相位互补` (phase-complement).
- Restructured Schur-free IMR mechanism explanation: Avoided hyperbolic language, framing it explicitly as converting a dense eigenproblem on the interface (whose storage/assembly limits scalability) into local static equilibrium problems mapped from existing eigenmodes of the alternate partition.
- Use `\textcolor{ExplainConclusion}` / `\textcolor{IsConclusion}` to mark key causal explanations and conclusions exactly as dictated in the `config/paper3_macros.tex`.
- In rewriting CMS bottleneck mechanics:
  - "Staggered partition" -> "交错划分" avoids exaggerated wording and accurately reflects the geometric offset.
  - Phrasing should logically bridge from phase deficiency in "fixed-interface normal modes" to the efficiency of using shifted modes that act as a "phase-complement" (相位互补).
  - Schur-free interface modes are best described as converting an expensive interface eigenproblem into "局部子结构上的静力平衡问题" (local static equilibrium problems).
- Mechanism explanations (like phase complement and Schur-free interface modes) must be rigorous and plain without using exaggerated phrases.
- When describing algorithms/mechanism in LaTeX, be careful to use correct macros (e.g. `\textcolor{IsConclusion}{...}`).

## Intro Mechanism Rewrite (P8-P12)
- Replaced vague mechanism descriptions with plain, rigorous explanations grounded in the English original.
- Clarified that traditional CMS converges slowly because extra basis functions have higher frequencies and are nearly orthogonal to target global modes.
- Added the explanation of fixed-interface modes as "phase-constrained windowed Fourier modes" and how a second staggered partition naturally provides phase-complementary bases.
- Explained the Schur-complement bottleneck (O(N^2) scaling, dense eigenproblems) and introduced the Schur/eigen-free IMR concept which maps boundary conditions from the other partition into local static equilibrium problems.
- Maintained consistent, stable terminology (模态综合法, 界面模态缩减法, Schur 补, 相位互补, 交错划分) and preserved the `\textcolor` and `\textbf` latex commands as required.
- Mechanism translation for CMS slow convergence, phase deficiency, staggered partitions, and SE-free IMR successfully refined in 1_intro.tex using plain academic Chinese, avoiding exaggerated phrasing while maintaining technical accuracy.
- Mechanism translation: P8-P12 rewritten to clearly explain slow CMS convergence (orthogonal high-freq modes), phase-constraint of fixed-interface bases, phase-complement via staggered partitions, and Schur-/eigen-free IMR via local static equilibrium.
- For P8-P12 rewrite, the explanation of mechanism needs to be rigorous, plain academic Chinese.
- Avoided using exaggerated terms like "铁锁", "掐断", etc.
- Used "交错划分" for "staggered partition" and "无 Schur 补" for "Schur-free" to stay consistent.
- Mechanism translation for CMS, staggered partitions, phase complement, and Schur-/eigen-free IMR was successfully added with rigorous academic tone.
Paragraphs successfully rewritten to explain the mechanism accurately in academic Chinese.
- The rewritten mechanism text in paper 3 introduction was mistakenly placed inside the Related Work section. The correct position for the transition mechanism text is after the final related work subsection (Singular Matrix Pencil) and before the Contributions list.
Moved mechanism paragraphs after Related Work section to maintain logical flow and contiguous subsection structure.
- Mechanism sections should logically flow after the related work discussion to maintain the paper's structural coherence. Always ensure `\subsection{本章方法与贡献}` (which introduces the mechanism/contributions) appears at the very end of the introduction section, after all related works have been discussed.
- Moved mechanism introduction (P8-P12) down to appear after Related Work section to maintain logical flow and avoid interrupting the Related Work subsections.
- Use rigorous and factual translations in Chinese LaTeX. Replaced excessive emotional/exaggerated phrases with standard academic ones (e.g. "免 Schur 补且无特征值运算" instead of "直接丢弃摒弃并免除搭建复杂且昂贵的天文运算级稠密 Schur 补耦合连接体").
- Adhere to the provided terminology matching the original English (模态综合法 (CMS), 界面模态缩减法 (IMR), Schur 补, 交错划分, 相位互补).
- Use `\section{本章小结}` for conclusion instead of abstract or english translation
- Restrict to objective academic chinese tone instead of marketing languages

- When translating a conclusion, strip away overly dramatic phrasing and stick to the original factual claims to match rigorous academic Chinese style.
- Writing conclusions in rigorous Chinese requires striking a balance between factual summary and highlighting the value of the method, avoiding dramatic rhetoric while maintaining academic weight.
- Proper use of terminology (e.g., 界面模态缩减法 instead of "免除搭建复杂且昂贵的天文运算级稠密 Schur 补耦合连接体") greatly improves the credibility of the thesis.
