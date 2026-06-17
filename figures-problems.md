# 盲审意见中的图表问题摘录

## 一、审稿人 1 — 图中文字字号

> 图和表的文字需要稍作调整，如图1.1、图4.9等，图中文字字号不应大于正文字体。

| 涉及图表 | 当前状态 |
|---|---|
| 图 1.1（绪论图） | 待重生成 |
| 图 4.9（Paper3 elastic comparison） | ✅ 已修复 |
| 其他外部生成图片中的字号问题 | ✅ 已统一 — thesis_figure_config.py + plot_style_config.py |

---

## 二、审稿人 2 — 图 1-2 超前引用

> 图 1-2 在引用该图的文字前，建议修改。

| 涉及图表 | 当前状态 |
|---|---|
| 图 1-2（`fig:locking_issue`） | ✅ 已完成 |

---

## 三、审稿人 4 — 表格引图不在附近

> 有些表格引用的图不在表格附近，需要在上下文寻找。

| 涉及图表 | 当前状态 |
|---|---|
| Paper2 统计表远距离引用图号 | ✅ 已完成 |
| 图 1-2 超前引用 | ✅ 已完成 |
| Paper3 模型统计表 `\Cref{}` 章节索引 | 保持现状 |

---

## 四、审稿人 5-1 — 图表格式大面积不规范

### 4.1 外部生成图片问题

| 问题类型 | 被点名的图 | 状态 |
|---|---|---|
| 坐标轴标签缺失 | 图 2.2、2.4、4.5、4.7 | 🔶 Paper2 待处理 |
| 量纲与数值混写 | 同上 | ✅ 中文化后统一标注 |
| 对数坐标未标注 | 图 2.2、2.4 | ✅ LogFormatterMathtext |
| 图例遮挡数据曲线 | 部分图 | 🔶 需逐张检查 |
| 坐标轴标签字体过小 | 多张核心图表 | ✅ 统一 22.4pt/19.2pt |

### 4.2 源码级问题

| 问题类型 | 状态 |
|---|---|
| 算法流程排版缩进 | ✅ 已完成 |
| 变量引用不统一 | ✅ 已完成 |

---

## 五、Paper3 图表与脚本对照（清理后）

所有脚本在 `body/graduate/paper3/figures/` 下。

| 输出 PDF | 生成脚本 | figsize | 语言 |
|---|---|---|---|
| `comparison-figures/cat/cat_comparison.pdf` | `comparison-figures/plot.py` | (14,7) | 中文 ✅ |
| `comparison-figures/board/board_comparison.pdf` | `comparison-figures/plot.py` | (14,7) | 中文 ✅ |
| `comparison-figures/breaker/breaker_comparison.pdf` | `comparison-figures/plot.py` | (14,7) | 中文 ✅ |
| `comparison-figures/aa_vs_metis/cat_aa_vs_metis_comparison.pdf` | `comparison-figures/aa_vs_metis/generate_aa_vs_metis_cn.py` | (14,7) | 中文 ✅ |
| `dragon_tet/dragon_tet_performance.pdf` | `dragon_tet/generate_dragon_tet_cn.py` | (14,6) | 中文 ✅ |
| `dragon_tet/dragon_tet_breakdown.pdf` | `dragon_tet/generate_dragon_tet_cn.py` | (12,6) | 中文 ✅ |
| `critical-qb/combined_scaling.pdf` | `critical-qb/plot.py` | (12,6)/(14,8) | 中文 ✅ |
| `frequency-vs-phase/basis.pdf` | `frequency-vs-phase/plot_basis.py` | (16,6) | 中文 ✅ |
| `frequency-vs-phase/frequency-vs-phase.pdf` | `frequency-vs-phase/lap_cms.py` | (20,6) | 中文 ✅ |
| `frequency-vs-phase/integration.pdf` | `frequency-vs-phase/plot_integration.py` | (12,6) | 中文 ✅ |
| `frequency-vs-phase/fixed-vs-complete-eig-error.pdf` | `frequency-vs-phase/plot_error.py` | (16,6) | 中文 ✅ |
| `mu_and_sigma/mu_and_sigma_plot.pdf` | `mu_and_sigma/plot.py` | (12,6) | 中文 ✅ |
| `local_update/PCB_np4_neig100/benchmark_comparison.pdf` | `local_update/plot_benchmark.py` | (14,6) | 中文 ✅ |
| `local_update/micro_long/benchmark_neig100_comparison.pdf` | `local_update/plot_benchmark.py` | (14,6) | 中文 ✅ |
| `time-nev/nev_vs_time_plot_sparse.pdf` | `time-nev/plot.py` | (12,6) | 中文 ✅ |
| `substructure_analysis/schur_vs_eig_timing_curves.pdf` | `substructure_analysis/plot_comp.py` | (12,6) | 中文 ✅ |
| `scaling_aggregation_new/combined_plots/combined_*.pdf` | `scaling_aggregation_new/plot_new_benchmarks.py` | (12,6)/(14,8) | 中文 ✅ |

**ParaView 渲染**（无文本标签）：所有 partition/eig/comp PNG、pd-partition-demo、interface-modes-example、domain_definition、animation、teaser 子图。

**共享配置**：
- `plot_style_config.py` — 配色方案
- `script/thesis_figure_config.py` — CJK 字体 + 字号

---

## 六、分优先级的修复路线

### ✅ 第一优先级：Paper3 — 完成

全图中文化、figsize 统一、log scale 修复、冗余脚本清理、字体配置统一。

### ✅ 第二优先级：Paper2 — 不修改

大部分图为 ParaView 渲染截图 / PPT 拼图，可程序化调整的 matplotlib 脚本仅 2 个且输出非主图。无集中式字体配置。

### ✅ 第三优先级：Paper1 — 不修改

全部 PDF 为 Excel 导出或 ParaView 渲染，无 Python 脚本。数据分析在 `ConsManifold/sheet/*.xlsx` 中，字体调整需手动操作 Excel。
