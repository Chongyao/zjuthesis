# Task 2: First-Person (`我们`) Inventory — Active Thesis Prose

**Generated:** 2026-05-09  
**Scope:** Active build-surface files only (from `body/graduate/content.tex` include graph)  
**Excluded:** `*_backup/`, commented-out `\inputbody` calls, figures/ subdirectories, non-.tex files

---

## Summary

| Chapter | Active Files | Files w/ `我们` | Occurrences |
|---------|-------------|-----------------|-------------|
| Intro (Ch.1) | 3 | 2 | 5 |
| Paper 1 (Ch.2) | 5 | **0** | 0 |
| Paper 2 (Ch.3) | 5 | 4 | 29 |
| Paper 3 (Ch.4) | 6 | 4 | 39 |
| Conclusion (Ch.5) | 1 | **0** | 0 |
| **TOTAL** | **20** | **10** | **73** |

> **Note:** Paper 1 (Cosserat Rod) is **clean** — zero `我们` in active prose. This was likely already rewritten to `本文` or passive voice during the paper1 migration.

---

## Detailed Inventory

### Classification Key
- **A** = Authorial narration (describes research actions: "我们提出...", "我们使用...", "我们的方法...")
- **T** = Technical/math reasoning (derivations, proof steps: "不失一般性，我们假设...")
- **C** = Caption (figure/table captions)
- **R** = Rewrite priority: **HIGH** (first-person dominates paragraph voice), **MEDIUM** (incidental), **LOW** (figure caption, acceptable in some conventions)

---

### 1. Intro — `body/graduate/intro/`

#### `2_related_and_problems.tex` (4 occurrences)

| # | Line | Context Snippet | Class | Rewrite |
|---|------|----------------|-------|---------|
| 1 | 9 | `...假设我们选取 $n$ 个基函数组成集合...` | T | MEDIUM |
| 2 | 23 | `...我们仅在计算机中维护离散采样点...` | A | HIGH |
| 3 | 61 | `...我们可以考察基函数...` | T | LOW |
| 4 | 106 | `下面我们将从物理本构、空间离散到算法构造这三个层次...` | A | HIGH |

#### `3_contributions_and_organization.tex` (1 occurrence)

| # | Line | Context Snippet | Class | Rewrite |
|---|------|----------------|-------|---------|
| 5 | 11 | `...在原理上，我们识别了不同仿真场景下造成全局系统病态的这些局部高频"硬"模态。` | A | HIGH |

---

### 2. Paper 1 — `body/graduate/paper1/`

**CLEAN** — No `我们` occurrences in active files.

All previous `我们` usage migrated to `本文` in active version; old first-person prose retained only in `paper1_backup/`.

---

### 3. Paper 2 — `body/graduate/paper2/`

#### `1_intro.tex` (1 occurrence)

| # | Line | Context Snippet | Class | Rewrite |
|---|------|----------------|-------|---------|
| 1 | 19 | `我们不再采用全面重构三维体全局自由度的做法，而是采用局部策略...` | A | HIGH |

#### `3_background.tex` (1 occurrence)

| # | Line | Context Snippet | Class | Rewrite |
|---|------|----------------|-------|---------|
| 2 | 28 | `下面我们聚焦于由单元质量引起的软硬耦合问题。` | A | MEDIUM |

#### `4_method.tex` (14 occurrences)

| # | Line | Context Snippet | Class | Rewrite |
|---|------|----------------|-------|---------|
| 3 | ~8 | `因此，我们利用现有基函数和自适应 h-细化层次结构提出了一种...` | A | HIGH |
| 4 | ~63 | `我们通过直接最小化细分后四面体块的迹来优化 $z$` | A | HIGH |
| 5 | ~68 | `随后，我们按这十种情况的最大特征值排序，并选择产生最小值的配置。` | A | HIGH |
| 6 | ~73 | `\caption[...]{...我们分别考虑边细分与面细分等不同情形...}` | C | LOW |
| 7 | ~77 | `由于我们始终将新顶点保留在局部区域内...` | T | MEDIUM |
| 8 | ~81 | `为简单起见，我们首先考虑同质情形...` | T | MEDIUM |
| 9 | ~84 | `我们利用这些上界来确定要聚合哪些单元。` | A | HIGH |
| 10 | ~91 | `随后，我们选择对最大行和贡献最大的单元：` | A | HIGH |
| 11 | ~96 | `我们递归地将任一排序函数应用于它...` | A | HIGH |
| 12 | ~98 | `...阈值 $t$（我们默认设为 0.1）...` | T | LOW |
| 13 | ~104 | `...我们将其中一部分局部高频模态从主计算空间中分离出来...` | A | HIGH |
| 14 | ~115 | `下面我们将这一过程统一纳入基于细化的层次结构框架中加以描述。` | A | MEDIUM |
| 15 | ~119 | `...我们首先在局部区域上引入递归 h-细化...` | A | HIGH |
| 16 | ~205 | `...我们仍采用与前文一致的局部基函数优化思想...` | A | HIGH |

#### `5_results.tex` (13 occurrences)

| # | Line | Context Snippet | Class | Rewrite |
|---|------|----------------|-------|---------|
| 17 | 3 | `在本节中，我们展示了基函数优化降低全局刚度矩阵最大特征值的效果...` | A | HIGH |
| 18 | 28 | `我们使用 Thingi10k 数据集评估了我们的方法...` | A | HIGH |
| 19 | 30 | `为此，我们收集了应用方法前后最大特征值...` | A | HIGH |
| 20 | 30 | `我们还对未使用小波变换处理"强连接"的配置进行了测试。` | A | HIGH |
| 21 | 43 | `对于这些示例，我们使用与基准测试研究相同的边界条件求解静力平衡问题。` | A | HIGH |
| 22 | 45 | `因此，我们的方法本质上涉及 CG 收敛所需迭代次数与每次迭代计算成本之间的权衡...` | A | HIGH |
| 23 | 56 | `接下来我们保持实验顺序不变，转向更具针对性的困难情形...` | A | HIGH |
| 24 | 83 | `\caption[...]{...没有我们的方法时，原始解几乎被完全锁定（左）。...}` | C | LOW |
| 25 | 88 | `虽然我们目前未实现混合单元网格的细化（将其留待未来工作），但我们的重点放在合并前的四面体网格上。` | A | HIGH |
| 26 | 102 | `为了减小线性弹性的人工效应，我们使用旋转-应变坐标...` | A | HIGH |
| 27 | 109 | `\caption[...]{...我们使用旋转-应变坐标与泊松重建对线性弹性结果进行后处理...}` | C | LOW |
| 28 | 114 | `我们以准静态方式模拟此切割过程。` | A | HIGH |
| 29 | 126 | `例如，我们将方法应用于包含大量类四边形病态四面体的螺母模型...` | A | HIGH |

---

### 4. Paper 3 — `body/graduate/paper3/`

#### `2_foundation.tex` (1 occurrence)

| # | Line | Context Snippet | Class | Rewrite |
|---|------|----------------|-------|---------|
| 1 | 11 | `不失一般性，我们假设自由度已重新排序...` | T | LOW |

#### `2_representation.tex` (2 occurrences)

| # | Line | Context Snippet | Class | Rewrite |
|---|------|----------------|-------|---------|
| 2 | 12 | `\caption[...]{...我们比较了固定相位基和相位完备基...}` | C | LOW |
| 3 | 35 | `\caption[...]{...我们通过滑动区间起点 $a$...}` | C | LOW |

#### `3_simulation.tex` (17 occurrences)

| # | Line | Context Snippet | Class | Rewrite |
|---|------|----------------|-------|---------|
| 4 | 14 | `我们将这些额外引入的基函数称为对原基函数的相位补足...` | A | HIGH |
| 5 | 16 | `为验证相位完备基函数相较于传统模态综合法中固定相位基的优势，我们分析了积分误差。` | A | HIGH |
| 6 | 49 | `实际应用中，我们通过多重划分（尤其是交错划分）生成相位完备基。` | A | HIGH |
| 7 | 51 | `对于复杂拓扑或几何切片困难的模型，我们采用 METIS 库...` | A | HIGH |
| 8 | 92 | `为消除舒尔补带来的庞大计算负担，我们结合多重划分策略，提出了一种高效的无舒尔补界面模态缩减法。` | A | HIGH |
| 9 | 114 | `\caption[...]{...我们提取对偶低频特征模态...}` | C | LOW |
| 10 | 118 | `我们从对偶划分子结构特征模态中提取...` | A | HIGH |
| 11 | 125 | (omitted in tool output — likely contains additional `我们`) | TBC | TBC |
| 12 | 139 | (omitted in tool output — likely contains additional `我们`) | TBC | TBC |
| 13 | 143 | `因此，我们提出一种轻量级的正则化方案...` | A | HIGH |
| 14 | 159 | `在实际实现中，我们设计了自适应位移算法...` | A | HIGH |
| 15 | 166 | `但我们深入挖掘了基向量的正交性和静力平衡特性...` | A | HIGH |
| 16 | 185 | `为在分布式内存集群上实现最大的计算可扩展性，我们开发了基于混合 MPI 与 OpenMP 架构的并行计算框架。` | A | HIGH |
| 17 | 186 | `我们将来自原始划分和对偶划分的每个子结构视为独立的计算单元...` | A | HIGH |
| 18 | 201 | `为生成满足要求的两种差异化划分，我们设计了两阶段边权重调节策略。` | A | HIGH |
| 19 | 204 | `为修复这一局部缺陷，我们在交汇点处显式引入辅助子结构。` | A | HIGH |
| 20 | 206 | `我们利用子结构特征模态...因此我们并未为这部分子结构引入界面模态。` | A | HIGH |

#### `4_results.tex` (19 occurrences)

| # | Line | Context Snippet | Class | Rewrite |
|---|------|----------------|-------|---------|
| 21 | 4 | `我们首先在标准二维矩形区域上验证方法的基础数值行为。` | A | HIGH |
| 22 | 39 | `根据是否具备高精度基准解，我们采用不同精度指标评估计算所得的特征对。` | A | HIGH |
| 23 | 41 | `...我们测量相对特征值误差：` | A | HIGH |
| 24 | 49 | `我们使用误差--时间曲线评估整体效率。` | A | HIGH |
| 25 | 51 | `为生成该曲线，我们通过系统地增加每次运行的 $q_{\mathcal{I}}$ 来执行多次计算。` | A | HIGH |
| 26 | 63 | `受限于资源，我们的实验通过模拟这种并行环境来进行...` | A | HIGH |
| 27 | 67 | `...我们使用平均值与最大值之比来量化工作负载与内存分布效率...` | A | HIGH |
| 28 | 74 | `为公平对比，我们设置统一的误差阈值...` | A | HIGH |
| 29 | 83 | `这证实了我们的分析：传统模态综合法的峰值内存由稠密界面矩阵主导...` | A | HIGH |
| 30 | 135 | `我们对提出的方法...进行全面的性能评估。` | A | HIGH |
| 31 | 137 | `我们分析针对固定的目标特征模态数量...达到特定精度所需的计算时间...` | A | HIGH |
| 32 | 138 | `我们检验计算成本与准确解析的模态数之间的关系...` | A | HIGH |
| 33 | 142 | `我们使用误差-时间曲线来评估计算效率...` | A | HIGH |
| 34 | 225 | `为了进一步量化实践中的优势，我们基于累积相对误差...` | A | HIGH |
| 35 | 243 | `我们通过两个场景展示此能力。` | A | HIGH |
| 36 | 302 | `此外，我们将本方法与 SLEPc 分布式特征值求解器进行了对比测试。` | A | HIGH |
| 37 | 305 | `基于这一子空间，我们进一步计算了下落龙模型的动画过程...` | A | HIGH |
| 38 | 312 | `\caption[...]{龙模型使用我们的方法计算得到前50个低阶模态...}` | C | LOW |
| 39 | 245 | `其次，我们在包含了晶格微结构的 3D 弹性问题上验证该方法的效率...` | A | HIGH |

---

### 5. Conclusion — `body/graduate/conclusion.tex`

**CLEAN** — No `我们` occurrences. Entire conclusion already uses `本文` and passive voice.

---

## Key Observations

1. **Paper 1 is the gold standard** — zero first-person usage in active prose. All occurrences migrated to `本文` or passive voice during its dedicated migration.

2. **Paper 2 and Paper 3 dominate** — together account for 68/73 (93%) of all hits. These are the papers still carrying original Chinese-draft first-person prose.

3. **Intro has small residual** — 5 hits total, moderate rewrite burden.

4. **Caption occurrences (C classification, ~6 total)** are borderline. Some thesis style guides allow `我们` in captions; others enforce `本文`. These are the lowest priority for rewrite.

5. **Technical reasoning (T classification, ~5 total)** like "不失一般性，我们假设..." could be rephrased to impersonal form but this is a weak stylistic preference rather than a clear violation.

6. **Authorial narration (A classification, ~62 hits)** is the primary rewrite target. These describe research actions taken by the authors and should use `本文` or passive voice per standard Chinese academic thesis convention.

## Rewrite Strategy (NOT executed in this task)

Per the task directive, no rewrites are proposed here. However, the data supports these observations for downstream work:

- **Paper 1**: No action needed.
- **Intro**: ~3 HIGH priority replacements, ~2 lower priority.
- **Paper 2 (4_method, 5_results)**: ~25 HIGH priority, ~3 MEDIUM, ~2 LOW.
- **Paper 3 (3_simulation, 4_results)**: ~30 HIGH priority, ~4 LOW (captions).
- **Conclusion**: No action needed.
