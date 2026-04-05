# Paper 1 (Chapter 2) 结构重组执行计划

**目标**：将第二章从“独立论文结构”改造为“博士论文递进章节”，使其与第一章（绪论）提出的“软硬耦合病态系统与表示空间重构”总路线严密对齐。

**核心要求**：
1. 统一采用标准章节结构：章首摘要混合段 $\rightarrow$ 研究背景 $\rightarrow$ 软硬耦合分析 $\rightarrow$ 基函数变换 $\rightarrow$ 实验结果与分析 $\rightarrow$ 本章小结。
2. 凡是在绪论（`intro/2_related_and_problems.tex`）中已经详细阐述过的概念（如软硬模式、长度约束导致谱分离、传统 KKT/罚函数的宏观局限、DER/Super-Helices的宏观对比），在本章必须**注释保留（不要删除）**。
3. 将核心技术部分的叙事从“提出一种表示方法”转变为“为了隔离病态刚度而进行的基函数/广义坐标变换”。

---

## 阶段 1：章首架构与背景去重 (Target: `main.tex` & `1_intro.tex`)

### 任务 1.1：重构 `main.tex` 入口
- **文件**：`body/graduate/paper1/main.tex`
- **动作**：
  - 在 `\chapter{...}` 之后，直接插入（或 \input）一段没有 `\section` 标题的文本，作为“章首摘要”。
  - 这段摘要的内容应直接采用当前 `1_intro.tex` 中已经被我改写过的那段“第一章指出...”的承上启下文字。

### 任务 1.2：改造与精简 `1_intro.tex`
- **文件**：`body/graduate/paper1/1_intro.tex`
- **动作**：
  - 移除开头的章首摘要内容（因其已移至 `main.tex` 或独立文件）。
  - 将 `\section{引言}` 改为 `\section{研究背景}`。
  - **精准注释（查重）**：
    - 仔细对比 `intro/2_related_and_problems.tex` 中 `\subsection{不可伸长弹性细杆的刚度失配问题}` 的内容。
    - 将 `1_intro.tex` 中关于“拉伸很硬、弯扭很软导致谱分离”的详细原理解释用 `%` 注释掉。
    - 将关于 Penalty、KKT、DER、Super-Helices、RedMax 的**大段宏观综述**注释掉（绪论已讲）。
    - *保留*：仅保留极短的本章局部应用背景（如纱线、毛发需要何种处理），以及“本章方法与贡献”列表。

---

## 阶段 2：拆解表示方法，聚焦“软硬耦合分析” (Target: `2_representation.tex`)

### 任务 2.1：设立问题分析专节
- **文件**：`body/graduate/paper1/2_representation.tex`
- **动作**：
  - 将 `\section{不可伸长 Cosserat 杆的表示方法}` 改为 `\section{软硬耦合分析}`。
  - 明确划分两个 `\subsection`：
    1. `\subsection{传统笛卡尔表示与冗余自由度}`：保留原有对变量 $\mathbf{x} = [\mathbf{p}^T, \mathbf{q}^T]^T$ 和三大约束（式 2.1 - 2.3）的数学描述。
    2. `\subsection{局部硬约束引发的病态性}`：在这里补充/修改几句话，点明这三个约束（特别是长度约束）如何构成离散系统中的“极高频硬模式”，从而导致传统求解域条件数恶化（呼应绪论）。

### 任务 2.2：将“紧凑表示”移出
- **文件**：`body/graduate/paper1/2_representation.tex`
- **动作**：
  - 将原有的 `\subsection{紧凑表示}`（包含轴角转换、链式结构定义、式 2.4 - 2.8 等核心数学变换）从本文件中**剪切移出**。
  - 这部分内容将作为“基函数变换”的核心，放入下一阶段。

---

## 阶段 3：统合技术实现为“基函数变换” (Target: `3_simulation.tex`)

### 任务 3.1：确立变换主轴
- **文件**：`body/graduate/paper1/3_simulation.tex`
- **动作**：
  - 将 `\section{仿真算法}` 改为 `\section{基函数变换}`。
  - 将阶段 2 移出的“紧凑表示”内容粘贴到本节开头，并重命名为 `\subsection{向轴角链式空间的广义坐标变换}` 或类似名称。

### 任务 3.2：重组子节逻辑
- **文件**：`body/graduate/paper1/3_simulation.tex`
- **动作**：调整本节后续内容的逻辑连贯性，使其看起来是“完成变换后的必然结果”：
  1. 引入新小节（或过渡段）：说明在新坐标空间 $\mathbf{s}$ 下，原问题转化为无（显式距离）约束优化域，自然消除了病态性。
  2. 保留原算法框架，可置于 `\subsection{新表示下的 SQP 求解框架}`。
  3. 保留算子评估性能分析，可置于 `\subsection{\texorpdfstring{$\mathcal{O}(n)$}{O(n)} 时间复杂度的算子评估}`。
  4. 确认 `\inputbody{paper1/preconditioner_content}`（即混合预条件器部分）正常挂靠在本 section 末尾。

---

## 阶段 4：后续验证与收尾 (Target: `4_results.tex` & `5_conclusion.tex`)

### 任务 4.1：引用与标号检查
- **文件**：`body/graduate/paper1/4_results.tex`、附录等。
- **动作**：
  - `4_results.tex` 保持 `\section{实验结果与分析}` 不变。
  - 检查全章所有的 `\ref{sec:...}` 或 `\Cref{...}`，确保因 section 重命名或拆分导致的引用没有断裂或指向错误。

### 任务 4.2：结尾结构确认
- **文件**：`body/graduate/paper1/5_conclusion.tex`
- **动作**：
  - 确认保持 `\section{本章小结}`。
  - 此前已完成对该文件“呼应绪论、总结剥离机制、引出第三章”的改写，只需确认编译无误即可。

---

**执行准则：**
- 所有结构调整均需保证 LaTeX 能够正常编译 (`latexmk`)。
- 被注释掉的文本必须使用 `%` 并最好加上 `[Covered in Intro]` 之类的标记以备查。
- 保证最终生成的 PDF 目录（TOC）结构完美符合目标设想。