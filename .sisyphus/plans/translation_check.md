# 小论文翻译 100% 完整性审查与补漏计划

## 核心目标
彻底对比英文原稿与中文 Thesis 对应章节，确保**段落、公式、图表、定理证明、附录**的 100% 覆盖。绝不允许出现“原稿有大段论述，中文直接跳过”的现象。

---

## 任务波次：Paper 1 (ConsManifold) 审查

- [x] **T1.1 摘要与引言核对**
  - **对照**：`ConsManifold/EGauthorGuidelines-body.inc` (Abstract, Sec 1) $\leftrightarrow$ `paper1/1_intro.tex`
  - **重点**：清理了与原文无关的脏段落，合并完全。
- [x] **T1.2 运动学表示理论核对**
  - **对照**：`ConsManifold/EGauthorGuidelines-body.inc` (Sec 2) + `invertible.tex` $\leftrightarrow$ `paper1/2_representation.tex`
  - **重点**：可逆性证明与理论体系均已对齐。
- [x] **T1.3 仿真与求解算法核对**
  - **对照**：`ConsManifold/EGauthorGuidelines-body.inc` (Sec 3) + `jacobian-pattern.tex` $\leftrightarrow$ `paper1/3_simulation.tex`
  - **重点**：已补入缺失的预条件器对比图和相关证明文字。
- [x] **T1.4 实验结果与附录核对**
  - **对照**：`ConsManifold/EGauthorGuidelines-body.inc` (Sec 4) + `app_*.tex` $\leftrightarrow$ `paper1/4_results.tex` + 附录
  - **重点**：已全面重建 4_results.tex，所有对比基准（KKT, Penalty, Super-Helices, RedMax）、场景实验与 timing 表格均已恢复。

---

## 任务波次：Paper 2 (agFEM_draft) 审查

- [x] **T2.1 背景与动机核对**
  - **对照**：`agFEM_draft/body/` (0.2-abstract, 1.0-intro, 1.1-related, 2-background) $\leftrightarrow$ `paper2/` (1_intro, 2_related, 3_background)
  - **重点**：Sliver elements 等概念已被覆盖。
- [x] **T2.2 核心方法（层次结构与基函数）核对**
  - **对照**：`agFEM_draft/body/3-method.tex` $\leftrightarrow$ `paper2/4_method.tex`
  - **重点**：核对 Strong Links 公式及 Candidate Selection，已被覆盖。
- [x] **T2.3 实验数据与附录核对**
  - **对照**：`agFEM_draft/body/` (4-results, 4.1-statistics, appendix) $\leftrightarrow$ `paper2/5_results.tex` + 附录
  - **重点**：网格统计表已迁移；原稿附录中仅为占位无实体缺失。

---

## 任务波次：Paper 3 (primal-dual_modes) 审查

- [x] **T3.1 摘要与背景（CMS与Schur补）核对**
  - **对照**：`primal-dual_modes/paper-body/` (abstract, 1.0, 2.0, 3.0) $\leftrightarrow$ `paper3/` (1_intro, 2_related, 3_background)
  - **重点**：原版 3.0 中对 CMS（模态综合法）和 Schur 补的高昂代价的分析推导（包含你之前提到的 cost analysis 图表）已通过补入图表和代价分析完成。
- [x] **T3.2 交错空间划分机制核对**
  - **对照**：`primal-dual_modes/paper-body/4.0-method-new.tex` $\leftrightarrow$ `paper3/4_method.tex`
  - **重点**：交错划分策略完备性证明与IMR公式已被覆盖且未删改。
- [x] **T3.3 算法实现与性能数据核对**
  - **对照**：`primal-dual_modes/paper-body/` (4.1-implementation, 4.1.1, 5.0, 5.1) $\leftrightarrow$ `paper3/` (5_implementation, 5_1_alg, 6_results)
  - **重点**：已完整补齐统计数据表、强弱扩展性分析、各种比较基准叙述与分布式架构平台讨论。
- [x] **T3.4 结尾与原稿附录排查**
  - **对照**：`primal-dual_modes/paper-body/` (6.0, 7.0-appendix) $\leftrightarrow$ `paper3/7_summary.tex`
  - **重点**：排查原版 `7.0-appendix.tex`后，已新建 `8_appendix.tex` 容纳 Schur 补推导与误差积分说明。

---

## 审查与修复规范 (QA Policy)

对于上述每一个 Checkbox，执行以下严格动作：
1. **对比检索**：使用双开阅读或脚本比对，定位英文原稿段落，在 Thesis 对应文件中寻找中文译文。
2. **遗漏判定**：
   - 如果发现原版有一段说明（>3句话）在中文里完全找不到对应逻辑 $\rightarrow$ **判定为遗漏**。
   - 如果发现原版有一个公式/表格/伪代码块在中文里缺失 $\rightarrow$ **判定为遗漏**。
3. **修复动作**：
   - 记录遗漏的“原版行号/内容”。
   - 根据前置确认的“统一叙事风格（严肃、不浮夸）”，将其翻译补写进 Thesis 的对应 `.tex` 文件中。
   - 保证补充内容与上下文的过渡自然。