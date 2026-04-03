# Draft: 博士论文小论文迁移与整合计划

## 1. 统一的叙事框架设计 (Unified Narrative Framework)

根据绪论（引言）中的核心逻辑图（病态系统 $\rightarrow$ 存在软硬耦合的基函数 $\rightarrow$ 解耦 $\rightarrow$ 基函数变换），三篇小论文（第2、3、4章）必须统一收束于**“通过基函数变换与空间重构来解除软硬耦合，从而解决病态刚度”**这一宏观叙事之下。

为了保证章节之间的逻辑连贯性，每一篇小论文在转换为论文主干章节时，均需遵循以下标准化叙事结构：

1. **研究背景与问题聚焦 (Motivation \& Problem Definition)**
   - **宏观映射**：明确本章针对绪论中提到的哪一种“软硬耦合”极端场景（如：一维显式距离约束、三维隐式退化形函数、宏观抽象的频域截断）。
   - **具体痛点**：该场景下传统的处理方法如何遭遇计算瓶颈。
2. **软硬耦合的数值根源分析 (Root Cause Analysis)**
   - 从代数或几何空间的角度，精准剖析“硬约束”是如何混入基函数，进而引发全局刚度矩阵病态的。
3. **空间重构与基函数解耦 (Space Reconstruction \& Decoupling) —— [本章核心创新]**
   - 详细阐述如何通过表示重构（如：基于关节角的链式坐标变换、算子感知的局域基函数优化、多重空间交错划分策略）将高频硬模态隔离，保留并增强低频软模态。
4. **高效数值求解框架 (Numerical Framework \& Algorithm)**
   - 基于重构后的新解空间，配套的高效离散与代数求解算法（如：定制预条件器、无Schur补的降阶计算）。
5. **实验评估与分析 (Evaluation \& Discussion)**
   - 证明基函数解耦后在物理保真度、代数稳定性和求解效率上的突破。
6. **本章小结 (Conclusion)**
   - 呼应绪论，总结本章重构策略的适用范围与优越性，并自然过渡到下一章更深层次或更宏观的病态问题。

---

## 2. 翻译与内容完整度校验任务设计 (Translation Completeness Tasks)

目标：绝对的 100% 翻译无遗漏。分为三个子论文，每个子论文执行严格的章节对齐与公式定理追溯。

### 论文 1: ConsManifold (对应 thesis paper1)
- **对照源**：`/home/zcy/workspace/records/ConsManifold`
- **任务目标**：
  - [ ] 校验 `1_intro.tex` 是否完全覆盖原版 Introduction 和 Related Work，无一遗漏。
  - [ ] 校验 `2_representation.tex` 中的紧凑表示推导，特别是附录中关于能量项和 Active Set 的公式是否全部正确迁移。
  - [ ] 校验 `3_simulation.tex` 中 SQP 框架和 $O(n)$ 复杂度矩阵向量乘法，特别是 `jacobian-pattern` 部分的数学细节。
  - [ ] 校验实验章节 `4_results.tex` 数据表格与图表的完整度。

### 论文 2: agFEM_draft (对应 thesis paper2)
- **对照源**：`/home/zcy/workspace/records/agFEM_draft`
- **任务目标**：
  - [ ] 校验原稿 `3-method.tex` 中关于数值适应层次结构（Numerical Coarsening/Refinement）的翻译。
  - [ ] 仔细审查“强连接（Strong Links）”与“劣形单元（Badly-shaped elements）”核心理论体系在 `4_method.tex` 中的完整度。
  - [ ] 检查原版附录中的补充数学推导（如有）是否已被整合或平移。
  - [ ] 确保原稿的 Benchmarks 及所有的统计算法（`4.1-statistics.tex`）在 `5_results.tex` 中得到 100% 还原。

### 论文 3: primal-dual_modes (对应 thesis paper3)
- **对照源**：`/home/zcy/workspace/records/primal-dual_modes`
- **任务目标**：
  - [ ] 校验交错空间划分策略（Interleaved Space Partitioning）机制的公式体系完整性。
  - [ ] 校验无 Schur 补及无局部特征分解的界面模态缩减（IMR）核心推导。
  - [ ] 核对所有精度对比和分布式架构通信开销的图表（实验部分）。

---

## 3. 备份任务 (Backup Protocol)

执行翻译校验与结构修改之前，必须对所有原稿和当前的 thesis 章节进行快照备份：
- [ ] 备份原稿：`ConsManifold`, `agFEM_draft`, `primal-dual_modes` 至安全路径。
- [ ] 备份当前 Thesis 对应的 `paper1`, `paper2`, `paper3` 目录。
