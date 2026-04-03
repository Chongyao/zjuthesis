# 博士论文小论文迁移与整合验证计划

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
- **对照源**：`/home/zcy/workspace/records/ConsManifold` -> 对应 `/home/zcy/workspace/records/zjuthesis/body/graduate/paper1`
- **校验清单**：
  - [x] 校验 `1_intro.tex` 是否完全覆盖原版 Introduction 和 Related Work，无一遗漏。
  - [x] 校验 `2_representation.tex` 中的紧凑表示推导。
  - [x] 校验 `3_simulation.tex` 中 SQP 框架和 $O(n)$ 复杂度矩阵向量乘法，以及原版独立的 `jacobian-pattern.tex` 内容。
  - [x] 校验 `4_results.tex` 数据表格与图表的完整度。
  - [x] 校验 `5_conclusion.tex` 的翻译与过渡。
  - [x] 校验附录部分（`app_*.tex`）是否完整继承了原始论文中关于能量项和 Active Set 的公式证明，以及 `invertible.tex` 的内容是否遗漏。

### 论文 2: agFEM_draft (对应 thesis paper2)
- **对照源**：`/home/zcy/workspace/records/agFEM_draft` -> 对应 `/home/zcy/workspace/records/zjuthesis/body/graduate/paper2`
- **校验清单**：
  - [x] 校验 `1_intro.tex` (原 1.0-introduction.tex)。
  - [x] 校验 `2_related.tex` (原 1.1-relatedWork.tex)。
  - [x] 校验 `3_background.tex` (原 2-background.tex)。
  - [x] 校验原稿 `3-method.tex` 在目标 `4_method.tex` 中的展开，特别是“强连接（Strong Links）”和“候选集选择”的对应关系。
  - [x] 校验原版 `4-results.tex` 和 `4.1-statistics.tex` 在 `5_results.tex` 中得到 100% 还原，包括图表和统计数据。
  - [x] 校验 `6_summary.tex`。
  - [x] 重点排查原版 `appendix.tex` 内容是否遗失：原文件仅含注释占位，无实体遗漏。

### 论文 3: primal-dual_modes (对应 thesis paper3)
- **对照源**：`/home/zcy/workspace/records/primal-dual_modes` -> 对应 `/home/zcy/workspace/records/zjuthesis/body/graduate/paper3`
- **校验清单**：
  - [x] 校验 `1_intro.tex` (原 abstract, teaser, 1.0-introduction)。
  - [x] 校验 `2_related.tex` (原 2.0-related_work.tex)。
  - [x] 校验 `3_background.tex` (原 3.0-background.tex)。
  - [x] 校验交错空间划分策略机制公式体系在 `4_method.tex` (原 4.0-method-new.tex) 中的完整性。
  - [x] 校验实现细节 `5_implementation.tex` 与子算法 `5_1_alg_adaptive_shifting.tex` (原 4.1 目录及文件)。
  - [x] 校验结果 `6_results.tex` 对原版 `5.0-results.tex` 和 `5.1-statistics.tex` 的整合。
  - [x] 校验总结 `7_summary.tex` (原 6.0-conclusion.tex)。
  - [x] 重点排查原版 `7.0-appendix.tex` 内容是否遗漏，已整合新建 `8_appendix.tex` 解决。

---

## 3. 备份任务 (Backup Protocol)
- [x] 已备份 Thesis 原稿 `paper1`, `paper2`, `paper3` 至 sibling 备份目录 (`paper1_backup/`, `paper2_backup/`, `paper3_backup/`)
- [ ] *[可选]* 若需备份 `/home/zcy/workspace/records/` 目录下的外部原稿项目（视文件规模而定，当前作为只读参考，已受 Git 控制）。