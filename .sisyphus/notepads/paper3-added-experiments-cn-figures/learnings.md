
## Explore findings — 2026-06-07

### 4_results.tex 插入锚点确认

1. **epsilon_eq**:
   - 插入位置：第 47 行之后（`\epsilon_{\text{ev}}` 解释结束），第 48 行（`\paragraph{性能评估：误差--时间曲线}`）之前
   - 同时需要在第 51 行将 `\epsilon_{\text{ev}}` 扩展为 `\epsilon_{\text{ev}} 或 \epsilon_{\text{eq}}`
   - 新增 label：`eq:error-eq`

2. **tab:statistics 表格更新**:
   - 第 15 行：`\multirow{5}` 已是 5（桌面工作站 5 行），无需修改
   - 第 22 行：`\multirow{4}` 需改为 `\multirow{5}`（计算服务器从 4 行变 5 行）
   - 第 25 行：Cat 行引用更新，加入 `\Cref{fig:laplacian-aa-vs-metis}`
   - 在第 26 行（Wing）之后新增 Dragon 行

3. **aa_vs_metis 段落**:
   - 插入位置：第 236 行之后（`fig:comp-timing-vs-nev` 的 `\end{figure}` 之后），第 237 行（`\subsection{应用验证}`）之前
   - 新增 `\paragraph{轴对齐划分与 METIS 划分的对比}`
   - 新增 `\label{fig:laplacian-aa-vs-metis}`

4. **dragon_tet 段落**:
   - 插入位置：aa_vs_metis 小节之后，`\subsection{应用验证}` 之前
   - 新增 `\paragraph{子结构数量对求解质量与效率的影响}`
   - 新增 `\label{fig:dragon-tet-tradeoff}`

### 图文件路径约定
- `\graphicspath` 已指向 `body/graduate/paper3/figures/`，includegraphics 使用相对路径
- 不需要 `figures/` 前缀
- 现有惯例：
  - `comparison-figures/{model}/{file}` 用于对比图
  - `scaling_aggregation_new/` 用于扩展性图
  - `time-nev/` 用于时间-模态数图
  - 直接使用子目录名如 `dragon_tet/`、`teaser/`、`animation/` 等

### 目标图目录状态
- `body/graduate/paper3/figures/comparison-figures/aa_vs_metis/` — **不存在，需创建**
- `body/graduate/paper3/figures/dragon_tet/` — **不存在，需创建**
- `script/paper3_figures/` — **不存在，需创建**

### 源文件确认存在
- `aa_vs_metis` 源：
  - `/home/zcy/workspace/records/primal-dual_modes/comparison-figures/aa_vs_metis/plot.py`
  - `/home/zcy/workspace/records/primal-dual_modes/comparison-figures/aa_vs_metis/build_data.py`
  - `/home/zcy/workspace/records/primal-dual_modes/comparison-figures/aa_vs_metis/render_partitions.py`
  - `/home/zcy/workspace/records/primal-dual_modes/comparison-figures/aa_vs_metis/cat_aa_vs_metis.csv`（数据文件）
  - 已有渲染好的 `aa-primal-partition.png`, `aa-dual-partition.png`, `cat_aa_vs_metis_comparison.pdf`（英文）
  - `_tog454_stage_used/comparison-figures/aa_vs_metis/` 也有副本

- `dragon_tet` 源：
  - `/home/zcy/workspace/records/primal-dual_modes/figures/dragon_tet/plot.py`（从 log 文件提取数据 + 绘图）
  - `/home/zcy/workspace/records/primal-dual_modes/figures/dragon_tet/render_partitions.py`（分区图渲染）
  - 数据：`/home/zcy/workspace/records/primal-dual_modes/source_data/dragon_tet/logs/`（NEP_*_PD_np* 目录 + run.log）
  - 分区数据：`/home/zcy/workspace/records/primal-dual_modes/source_data/dragon_tet/partitions/`（np4/np8/np16 子目录 + VTK 文件）
  - 已有渲染好的 PNG/PDF

### LaTeX 包/宏约束
- `subcaption` — 已加载（在 paper3_macros.tex），支持 `\begin{subfigure}`
- `adjustbox`[export] — 已加载，支持 `valign=m`
- `tikz` — 已加载，用于 micro-local-update 图
- `amsmath`, `cleveref`, `xcolor` — 已加载
- `makecell`, `multirow` — 已加载，用于表格排版
- `algorithm` + `algorithmic`（非 algorithm2e）
- 使用 `\Cref`（cleveref），label 必须可解析

### aa_vs_metis plot.py 分析
- 从 `cat_aa_vs_metis.csv` 读取数据
- 生成 1×2 子图：NEP vs Error（左）+ Total Time vs Error（右）
- 英文坐标轴标签：`Number of Eigenpairs (N_ep)`, `Relative Error (ε_ev)`, `Total Time (s)`
- 图例用 `AA` vs `METIS`
- 依赖 `plot_style_config.py` 从 PROJECT_ROOT/figures 目录
- 使用 teal_coral 配色方案

### dragon_tet plot.py 分析
- 从 `source_data/dragon_tet/logs/` 提取 log 数据（extract_log_data）
- 生成两张图：dragon_tet_performance + dragon_tet_breakdown
- Performance: 1×2, Error vs NEP (左) + Error vs Total Time (右)
- Breakdown: 堆叠柱状图，4 个组件：Substructure Eigenmodes / Interface Modes / Matrix Reducing / Reduced Solve
- 英文标签：`np=4/8/16`, `Number of Eigenpairs (N_ep)`, `Relative Error (ε_ev)`, `Total Time (s)`, `Time (s)`
- 分区 PNG 已存在：np4/np8/np16 的 primal-partition 和 dual-partition（无英文标注，可直接复用）
- 依赖 `plot_style_config.py` 从源仓库的 figures 目录（需要 soft link 到 thesis 版本）

### 潜在构建风险
1. **paper2_backup 中的断链链**：不影响 latexmk 编译（不在 content.tex 中），但影响 glob/grep 工具输出
2. **中文字体在 matplotlib 中问题**：
   - 当前 `plot_style_config.py` 使用 `font.family: ["Source Han Sans CN", "Times New Roman"]`
   - 需要用 `Noto Sans CJK SC` 或其他系统可用的中文字体
   - 如果用 PDF 输出，需确认字体嵌入
3. **dragon_tet 脚本数据依赖**：脚本从 `source_data/dragon_tet/logs/` 提取数据（相对路径 3 层 up），如果 soft link 数据，脚本中的路径计算需调整
4. **图文件不存在则 latexmk 失败**：必须先在目标目录生成图文件，再修改 4_results.tex
5. **subcaption 和 figure 嵌套**：`fig:metis-pd-partition` 和 `fig:metis-c-partition` 是 subfigure 内的 label，新图的 subfigure 是否有子 label 由计划决定
6. **\Cref 引用必须可解析**：`fig:laplacian-aa-vs-metis` 和 `fig:dragon-tet-tradeoff` 必须被 `\label{...}` 定义后才能被 `\Cref{...}` 引用

### 执行顺序建议
1. 先创建 `script/paper3_figures/aa_vs_metis/` 和 `script/paper3_figures/dragon_tet/`
2. soft link 数据，复制生成脚本
3. 修改脚本生成中文版图（先确认中文字体可用）
4. 输出到 thesis 的 `body/graduate/paper3/figures/` 下的目标子目录
5. 再修改 `4_results.tex`
6. `latexmk` 编译验证


---

## 深入探索发现 — 2026-06-07 (第二轮)

### 完整文件清单 (所有路径已证实存在)

#### aa_vs_metis 完整路径
**生成脚本 (可复用):**
- `/home/zcy/workspace/records/primal-dual_modes/comparison-figures/aa_vs_metis/plot.py` (96行)
- `/home/zcy/workspace/records/primal-dual_modes/comparison-figures/aa_vs_metis/build_data.py` (101行，数据抽取，非必需)
- `/home/zcy/workspace/records/primal-dual_modes/comparison-figures/aa_vs_metis/render_partitions.py` (62行，ParaView，非必需)

**数据文件:**
- `cat_aa_vs_metis.csv` (29行): PartitionType, Method, Num_Modes, Error_2norm, Time_Total
- `cat_AA_PD.csv`: 中间产物 (AA数据抽取结果)
- `/home/zcy/workspace/records/primal-dual_modes/comparison-figures/cat/cat_PD.csv` (19行): METIS基准数据

**外部数据源 (build_data.py 用):**
- `/home/zcy/workspace/models/cat/log/NEP_*_PD_np*/run.log` — 存在，AA实验原始日志

**依赖:**
- `plot_style_config.py` — 从 `figures/` 导入 (PROJECT_ROOT 自动计算)
- matplotlib, pandas, numpy

**中文化要点 (plot.py):**
| 行号 | 原文 | 中文 |
|------|------|------|
| 62 | Number of Eigenpairs (N_ep) | 特征对数量 |
| 63 | Relative Error (ε_ev) | 相对误差 |
| 67 | Total Time (s) | 总计算时间 (秒) |
| 71-74 | AA / METIS (legend) | 轴对齐划分 / METIS 划分 |

#### dragon_tet 完整路径
**生成脚本 (可复用):**
- `/home/zcy/workspace/records/primal-dual_modes/figures/dragon_tet/plot.py` (297行) — 一体化脚本: 抽取日志数据 + 生成两张图 + 保存CSV
- `/home/zcy/workspace/records/primal-dual_modes/figures/dragon_tet/render_partitions.py` (96行，ParaView，非必需)

**数据文件:**
- `dragon_tet_summary.csv` (16行): NEP, np, error_2norm, error_mean, t_sub, t_ifc, t_red_c, t_red_s, t_total, t_gt
- `source_data/dragon_tet/logs/NEP_{40,80,120,160,200}_PD_np{4,8,16}/run.log` — 15个目录

**分区数据 (ParaView):**
- `source_data/dragon_tet/partitions/np{4,8,16}/Partition_Summary.vtk` — 存在

**依赖:**
- `plot_style_config.py` — 3层目录up (从 figures/dragon_tet → figures/)
- matplotlib, pandas, numpy

**中文化要点 (plot.py):**
| 行号/位置 | 原文 | 中文 |
|------|------|------|
| 133 | Number of Eigenpairs (N_ep) | 特征对数量 |
| 134 | Relative Error (ε_ev) | 相对误差 |
| 152 | Total Time (s) | 总计算时间 (秒) |
| 199-204 | Substructure Eigenmodes / Interface Modes / Matrix Reducing / Reduced Solve | 子结构特征模态 / 界面模态 / 矩阵降维 / 缩减求解 |
| 235 | Number of Eigenpairs (N_ep) | 特征对数量 |
| 236 | Time (s) | 时间 (秒) |
| 130 | np=4,8,16 (legend) | 保持数学符号 |

### plot_style_config.py 字体配置
- 路径: `/home/zcy/workspace/records/primal-dual_modes/figures/plot_style_config.py`
- 字体: `font.family: "Times New Roman"`, `mathtext: "stix"`
- 中文需要额外字体配置: `plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", ...]`
- 建议在复制后的中文脚本中覆盖此设置

### 分区图片状态
- **aa_vs_metis 分区图** (aa-primal-partition.png, aa-dual-partition.png): 无英文标注，可直接复用
- **dragon_tet 分区图** (np{4,8,16}-{primal,dual}-partition.png): 无英文标注，可直接复用
- 分区图是3D网格彩色渲染，不含文字标签

### 目标目录状态 (确认)
- `body/graduate/paper3/figures/comparison-figures/` — 已存在 (有 breaker, cat, board, lady 子目录)
- `body/graduate/paper3/figures/comparison-figures/aa_vs_metis/` — 需要创建
- `body/graduate/paper3/figures/dragon_tet/` — 需要创建
- `script/paper3_figures/` — 需要创建

### 原论文 LaTeX 引用路径
原论文使用 `figures/dragon_tet/...` 前缀 (因原论文 \graphicspath 不同)
博士论文中须去掉 `figures/` 前缀 → `dragon_tet/...` 相对路径

---

## Figure generation completed — 2026-06-07

### Created thesis-local workspaces
- `script/paper3_figures/aa_vs_metis/`
  - copied source script to `generate_aa_vs_metis_cn.py`
  - linked `cat_aa_vs_metis.csv` to source CSV
  - linked `plot_style_config.py` to source style config
- `script/paper3_figures/dragon_tet/`
  - copied source script to `generate_dragon_tet_cn.py`
  - linked `logs` to source raw log directory
  - linked `dragon_tet_summary.csv` to source summary CSV as fallback only
  - linked `plot_style_config.py` to source style config
  - generated local `dragon_tet_summary_generated.csv` from logs, avoiding writes through source-data symlink

### Generated Chinese plot outputs
- `body/graduate/paper3/figures/comparison-figures/aa_vs_metis/cat_aa_vs_metis_comparison.pdf`
- `body/graduate/paper3/figures/comparison-figures/aa_vs_metis/cat_aa_vs_metis_comparison.png`
- `body/graduate/paper3/figures/dragon_tet/dragon_tet_performance.pdf`
- `body/graduate/paper3/figures/dragon_tet/dragon_tet_performance.png`
- `body/graduate/paper3/figures/dragon_tet/dragon_tet_breakdown.pdf`
- `body/graduate/paper3/figures/dragon_tet/dragon_tet_breakdown.png`

### Reused/copied partition images
- `body/graduate/paper3/figures/comparison-figures/aa_vs_metis/aa-primal-partition.png`
- `body/graduate/paper3/figures/comparison-figures/aa_vs_metis/aa-dual-partition.png`
- `body/graduate/paper3/figures/dragon_tet/np{4,8,16}-{primal,dual}-partition.png`

### Font and verification notes
- Matplotlib selected `Source Han Sans CN` automatically from installed CJK fonts; `fc-match` also showed `Noto Sans CJK SC` available.
- Scripts configure `pdf.fonttype=42`, `ps.fonttype=42`, and `axes.unicode_minus=False`.
- `pdffonts` confirmed `SourceHanSansCN-Regular` is embedded/subset in all three generated PDFs.
- Verification run: both generation scripts succeeded; `python -m py_compile` succeeded; LSP diagnostics were clean for both generated scripts.

#AA|### 4_results.tex 迁移完成
#BB|- 已将 `\epsilon_{\text{eq}}` 作为补充误差指标加入 `\paragraph{误差度量}`，并把误差--时间曲线的说明扩展为 `\epsilon_{\text{ev}}` 与 `\epsilon_{\text{eq}}`。
#CC|- `tab:statistics` 已补入 `Dragon` 行，`Cat` 行补上 `fig:laplacian-aa-vs-metis` 引用。
#DD|- 新增的 Cat 对比与 Dragon 子结构数分析均使用 thesis-local 路径，未加 `figures/` 前缀。
