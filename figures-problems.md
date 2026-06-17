# 盲审意见中的图表问题摘录

## 一、审稿人 1 — 图中文字字号

> 图和表的文字需要稍作调整，如图1.1、图4.9等，图中文字字号不应大于正文字体。

| 涉及图表 | 当前状态 |
|---|---|
| 图 1.1（绪论图） | 待重生成 |
| 图 4.9（Paper3 elastic comparison） | 待重生成 |
| 其他外部生成图片中的字号问题 | 待重生成 |

---

## 二、审稿人 2 — 图 1-2 超前引用

> 图 1-2 在引用该图的文字前，建议修改。

| 涉及图表 | 当前状态 |
|---|---|
| 图 1-2（`fig:locking_issue`） | 已完成 |

---

## 三、审稿人 4 — 表格引图不在附近

> 有些表格引用的图不在表格附近，需要在上下文寻找。

| 涉及图表 | 当前状态 |
|---|---|
| Paper2 统计表远距离引用图号 | 已完成（用自解释示例名替代） |
| 图 1-2 超前引用 | 已完成 |
| Paper3 模型统计表 `\Cref{}` 章节索引 | 保持现状（属标准论文模式） |

---

## 四、审稿人 5-1 — 图表格式大面积不规范（最严重）

> 多张核心图表（图2.2、2.4、4.5、4.7等）存在坐标轴标签缺失、量纲与数值混写、对数坐标未标注等严重格式问题。图例与曲线标识混乱，部分图例遮挡数据曲线，部分子图缺少图例或colorbar。坐标轴标签字体过小，无法辨识。算法流程排版缩进混乱，变量引用不统一。

### 4.1 外部生成图片问题（待重生成）

| 问题类型 | 被点名的图 | 具体表现 |
|---|---|---|
| 坐标轴标签缺失 | 图 2.2、2.4、4.5、4.7 | x/y 轴无标签或有标签但含义不明 |
| 量纲与数值混写 | 图 2.2、2.4、4.5、4.7 | 数值与单位之间缺少明确分隔 |
| 对数坐标未标注 | 图 2.2、2.4 等 | log scale 的轴未注明是对数坐标 |
| 图例遮挡数据曲线 | 部分图 | 图例放置位置不当 |
| 子图缺少图例/colorbar | 部分子图 | 多子图时某个子图缺图例 |
| 坐标轴标签字体过小 | 多张核心图表 | 打印后无法辨识 |

### 4.2 源码级问题（已完成）

| 问题类型 | 涉及内容 | 状态 |
|---|---|---|
| 算法流程排版缩进混乱 | `algorithm` / `algorithmic` 环境 | 已完成 |
| 变量引用不统一 | 算法伪代码中的变量名 | 已完成 |

---

## 五、图表问题的总体完成度

| 类别 | 状态 |
|---|---|
| 源码可直接修复的（表内文字、算法缩进、引用位置、图注口语化） | **已完成** |
| 外部生成图片的重生成（坐标轴、图例、字号、量纲、对数标注） | **待处理** |

---

## 六、被点名但不在可修改范围内的图

以下图属于 ParaView 渲染或矢量示意图，不含可编程修改的文本标签，无法通过改脚本修复，需单独处理：

| 图号 | 类型 | 说明 |
|---|---|---|
| 图 1-1 | ParaView/示意图 | 绪论导图 |
| 图 2-2 中的渲染部分 | ParaView | 3D 网格渲染，文本在 LaTeX 侧用 `\put` 或 subcaption 叠加 |
| 图 4-5 中的分区图 | ParaView | 分区颜色展示，无文本标签 |

---

## 七、可修改图表的生成脚本对照表

### Paper3（Primal-Dual Modes）— 基础设施最完善

所有脚本源路径前缀：`/home/zcy/workspace/records/primal-dual_modes/`

**已中文化（3 个图）**

| 论文图号 | 输出文件 | 生成脚本（thesis 仓库） | 备注 |
|---|---|---|---|
| 图 4.18 | `comparison-figures/aa_vs_metis/cat_aa_vs_metis_comparison.pdf` | `script/paper3_figures/aa_vs_metis/generate_aa_vs_metis_cn.py` | 轴对齐 vs METIS |
| 图 4.19 | `dragon_tet/dragon_tet_performance.pdf` | `script/paper3_figures/dragon_tet/generate_dragon_tet_cn.py` | Dragon 误差-时间 |
| 图 4.19 | `dragon_tet/dragon_tet_breakdown.pdf` | `script/paper3_figures/dragon_tet/generate_dragon_tet_cn.py` | Dragon 代价分解 |

**待中文化（~26 个图，均可用脚本修改）**

| 输出文件 | 论文引用位置 | 原始生成脚本（在 primal-dual_modes 中） |
|---|---|---|
| `comparison-figures/cat/cat_comparison.pdf` | 图 4.14 | `figures/comparison-figures/plot.py`（共享，一拖四） |
| `comparison-figures/board/board_comparison.pdf` | 图 4.16 | 同上 |
| `comparison-figures/breaker/breaker_comparison.pdf` | 图 4.13 | 同上 |
| `comparison-figures/rock_arm/rock_arm_comparison.pdf` | 未在 tex 中 | 同上 |
| `comparison-figures/lady/accuracy_plots_final_v4.pdf` | 未在 tex 中 | `figures/comparison-figures/lady/plot_comparison.py` |
| `frequency-v s-phase/basis.pdf` | 图 4.2 | `figures/frequency-vs-phase/plot_basis.py` |
| `frequency-vs-phase/frequency-vs-phase.pdf` | 图 4.2 下部 | `figures/frequency-vs-phase/lap_cms.py` |
| `frequency-vs-phase/integration.pdf` | 图 4.3 | `figures/frequency-vs-phase/plot_integration.py` |
| `frequency-vs-phase/fixed-vs-complete-eig-error.pdf` | 图 4.5 | `figures/frequency-vs-phase/plot_error.py` |
| `substructure_analysis/schur_cost_breakdown.pdf` | 图 4.7 | `figures/substructure_analysis/plot_schur.py`（一拖二） |
| `substructure_analysis/schur_scaling_analysis.pdf` | 图 4.7 附 | 同上 |
| `substructure_analysis/schur_vs_eig_timing_curves.pdf` | 图 4.7 | `figures/substructure_analysis/plot_comp.py` |
| `substructure_analysis/eig_vs_schur_equivalence.pdf` | 图 4.8 | `figures/substructure_analysis/plot.py` |
| `time-nev/nev_vs_time_plot_sparse.pdf` | 图 4.17 | `figures/time-nev/plot.py`（一拖二） |
| `time-nev/nev_vs_time_plot_all.pdf` | 图 4.17 附 | 同上 |
| `scaling_aggregation_new/combined_plots/combined_strong_weak_total_breakdown.pdf` | 图 4.10 | `figures/scaling_aggregation_new/plot_new_benchmarks.py`（一拖三，1898行） |
| `scaling_aggregation_new/combined_plots/combined_strong_weak_peak_memory_line.pdf` | 图 4.10 | 同上 |
| `scaling_aggregation_new/combined_plots/combined_strong_weak_balance_line.pdf` | 图 4.11 | 同上 |
| `mu_and_sigma/mu_and_sigma_plot.pdf` | 图 4.12 | `figures/mu_and_sigma/plot.py` |
| `critical-qb/combined_scaling.pdf` | 图 4.9 | `figures/critical-qb/plot.py` |
| `local_update/micro_long/benchmark_neig100_comparison.pdf` | 图 4.22 | `figures/local_update/micro_long/plot_benchmark.py`（一拖二） |
| `local_update/micro_long/benchmark_neig100_cms_breakdown.pdf` | 图 4.22 附 | 同上 |
| `local_update/PCB_np4_neig100/benchmark_comparison.pdf` | 图 4.21 | `figures/local_update/PCB_np4_neig100/plot_benchmark.py` |
| `teaser/modes_residual/modes_residual.pdf` | 图 4.23 | `figures/teaser/modes_residual/plot.py` |
| `teaser/breakdown/time_breakdown_pie.pdf` | 图 4.23 附 | `figures/teaser/breakdown/plot_breakdown_pie.py` |

实际需改的独立脚本数：**~17 个**（不含已中文化的 2 个）。

最大杠杆脚本：
- `comparison-figures/plot.py` → 改 1 个脚本，覆盖 4 个对比图
- `scaling_aggregation_new/plot_new_benchmarks.py` → 改 1 个脚本，覆盖 3 个扩展图

---

### Paper2（ConsManifold）— 生成脚本在外部项目仓库

所有脚本在 `/home/zcy/workspace/projects/` 下，不在论文仓库内。

| 论文图号 | 输出文件（推测） | 生成脚本 | 备注 |
|---|---|---|---|
| 图 2.2（CG benchmark） | `plot_figures/cg_benchmark/*_ratio_hist.png`（~27文件） | `projects/arborecence/pipline/localAG-smk/scripts/cg_benchmark.py` | 最大杠杆 |
| 图 2.4（频谱 vs 迭代） | `plot_figures/spectrum/*.png`（~14文件） | `projects/arborecence/pipline/localAG-smk/scripts/plot_spectrum_wrt_iters.py` | |
| 不同步数 CG 图 | `plot_figures/different_steps/*.png`（~28文件） | `projects/arborecence/pipline/localAG-smk/scripts/statistic_cut.py` | |
| 质量条件数 | `plot_figures/numeric-eigmax.png` 等 | `projects/bad_ele_lap/plot_condition_numbers.py` | 已有中文字体 |
| 强化链接进展 | `plot_figures/refinement_progress*.png` | `projects/strong_link_refine/scripts/plot_results.py` | |
| 动力学能量 | `plot_figures/dynamics/p1-p5.png` 等 | `projects/arborecence/pipline/beams/plot.py` | |
| Cholesky 频谱 | `plot_figures/*spectrum*.png` | `projects/arborecence/pipline/chol/plot_specturm.py` | |

实际需改的独立脚本数：**~7 个**。

---

### Paper1（Cosserat / agFEM）— 无现存脚本，需从数据重建

Paper1 的 ~38 个 Matplotlib PDF 全部由 Excel 生成，无 Python 脚本存活。
原始数据在：`/home/zcy/workspace/records/ConsManifold/sheet/*.xlsx`

| 论文图号 | 输出文件 | 数据源 | 难度 |
|---|---|---|---|
| 图 2.9 等 | `sheet/pdf/violation_inext_1e2.pdf`、`violation_inext_1e9.pdf` | `ConsManifold/sheet/violation.xlsx` | 高 |
| 图 2.12 | `sheet/pdf/violation_align_1e2.pdf`、`violation_align_1e9.pdf` | 同上 | 高 |
| 图 2.14 | `sheet/pdf/kinetic_energy_cmp.pdf` | `ConsManifold/sheet/data.xlsx` | |
| 图 2.15 | `sheet/pdf/offset.pdf` | 同上 | |
| 图 2.16 | `sheet/pdf/penalty_timing_A.pdf`、`penalty_timing_B.pdf` | `ConsManifold/sheet/penalty_timeing.xlsx` | |
| 图 2.18 | `sheet/pdf/KKT_ours_time_cost_cmp.pdf` | 同上 | |
| 图 2.19 | `sheet/pdf/violation_inext_KKT.pdf`、`violation_align_KKT.pdf` | `ConsManifold/sheet/violation.xlsx` | |
| 图 2.20 | `sheet/pdf/RedMax.pdf` | `ConsManifold/sheet/data.xlsx` | |
| 预条件子 | `sheet/pdf/single_chain_preconditioner_A/B/C.pdf`、`pcg_mu_our.pdf`、`pcg_mu_blk.pdf`、`linear_increasing.pdf` | `sheet/compare_precondition_single_chain.xlsx` | |
| 其他 | `catenary.pdf`、`condition_number.pdf` 等 ~15 个 | 各自 xlsx / csv | |

**参考**：`/home/zcy/workspace/records/agFEM_draft` 的 `chinese_figures` 分支有现成案例（7 个 Matplotlib 脚本 + 2 个 SVG）。

---

## 八、分优先级的修复路线

### 第一优先级：Paper3（~25 个图，~17 个脚本）

- 已有 `_cn.py` 模板脚本，流程成熟
- 每个脚本：复制 → 加 `configure_chinese_font()` + `LogFormatterMathtext` → 改英文为中文
- 可同时修复盲审意见中的：坐标轴标签、量纲、对数标注、字号

### 第二优先级：Paper2（~7 个脚本）

- 需决定在项目仓库改还是复制到 thesis 仓库参照 Paper3 模式
- `cg_benchmark.py` 一个脚本覆盖最多图

### 第三优先级：Paper1（~38 个图，需从零写脚本）

- 从 `agFEM_draft/chinese_figures` 分支取参考
- 从 xlsx 提取数据
- 建议只处理当前论文中实际引用的 ~17 个
