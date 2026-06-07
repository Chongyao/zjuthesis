# Paper3 新增实验与中文图表迁移计划

## 目标

将原始论文 `/home/zcy/workspace/records/primal-dual_modes` 中后续新增、但尚未完整迁移到博士论文第四章 `paper3` 的实验内容补入当前博士论文，并将新增图表中的英文标注替换为中文。

目标文件主要为：

```text
/home/zcy/workspace/records/zjuthesis/body/graduate/paper3/4_results.tex
```

目标图片目录主要为：

```text
/home/zcy/workspace/records/zjuthesis/body/graduate/paper3/figures/
```

整体写作要求：

- 严谨、客观、不夸大；
- 结论限定在具体实验条件下；
- 重点解释机制，而不是单纯强调性能优势；
- 不保留原论文中的 `\modified{...}` 或 `\textcolor{modified}{...}` 修改痕迹；
- 使用当前第四章已有的中文学位论文风格。

---

## 一、需要迁移的新增内容

### 1. 补充误差指标：平衡残差误差 `\epsilon_{\text{eq}}`

#### 来源

```text
/home/zcy/workspace/records/primal-dual_modes/paper-body/5.0-results.tex
```

原文位于 `Error Metrics` 部分，新增指标为：

```latex
\epsilon_{\text{eq}} =
\frac{\left\| \mathbf{K} \mathbf{x} - \lambda \mathbf{M} \mathbf{x} \right\|}{ |\lambda| \left\| \mathbf{x} \right\|}.
```

#### 目标位置

插入当前第四章 `4_results.tex` 的：

```latex
\paragraph{误差度量}
```

中，位于 `\epsilon_{\text{ev}}` 公式及解释之后，`\paragraph{性能评估：误差--时间曲线}` 之前。

#### 需要同步修改

当前第四章中已有表述：

```latex
将结果误差（$\epsilon_{\text{ev}}$）绘制为对应总计算时间（$t_{\text{cms}}$）的函数。
```

加入 `\epsilon_{\text{eq}}` 后应改为：

```latex
将结果误差（$\epsilon_{\text{ev}}$ 或 $\epsilon_{\text{eq}}$）绘制为对应总计算时间（$t_{\text{cms}}$）的函数。
```

#### 写作风格

应写成评价指标补充，不应写成新指标“更优”。推荐表达方向：

> 当问题规模较大、难以获得高精度参考谱时，本文采用平衡残差误差作为补充指标，用于衡量计算所得特征对满足原始广义特征值方程的程度。

---

### 2. 补充统计表中的 Dragon 模型

#### 来源

```text
/home/zcy/workspace/records/primal-dual_modes/paper-body/5.1-statistics.tex
```

原始新增行：

```latex
Dragon(\Cref{fig:animation},\Cref{fig:dragon-tet-tradeoff}) & 244K & 1.2M & 300
```

#### 目标位置

当前第四章 `tab:statistics` 的计算服务器部分。

当前结构为：

```latex
\multirow{4}*{\makecell{计算服务器...}}
& Frame ...
& Breaker ...
& Cat ...
& Wing ...
```

需要改为：

```latex
\multirow{5}*{\makecell{计算服务器...}}
```

并在 `Wing` 后加入：

```latex
& Dragon（\Cref{fig:animation,fig:dragon-tet-tradeoff}） & 244K & 1.2M & 300 \\
```

同时建议更新 Cat 行，加入新增图引用：

```latex
& Cat（\Cref{fig:laplacian-metis-error-time}、\Cref{fig:laplacian-aa-vs-metis}） & 765K & 1.5M & 500 \\
```

#### 命名建议

正文中已有“龙模型”，但统计表中其它模型多保留英文名，例如 `Frame`、`Breaker`、`Cat`、`Wing`。因此表格中建议保留 `Dragon`；正文中首次出现时可写为“Dragon 四面体模型”。

---

### 3. 新增实验：轴对齐划分与 METIS 划分对比

#### 来源

```text
/home/zcy/workspace/records/primal-dual_modes/paper-body/5.0-results.tex
```

原始小节：

```latex
\subsubsection{\modified{Axis-aligned vs. METIS partitions.}}
```

对应图：

```latex
\label{fig:laplacian-aa-vs-metis}
```

#### 目标位置

当前第四章 `4_results.tex` 中：

```latex
\paragraph{时间与准确模态数量关系}
...
\begin{figure}[tbp]
  ...
  \label{fig:comp-timing-vs-nev}
\end{figure}

% 新增此处

\subsection{应用验证}
```

建议新增：

```latex
\paragraph{轴对齐划分与 METIS 划分的对比}
```

#### 原始图文件

源图文件包括：

```text
comparison-figures/aa_vs_metis/aa-primal-partition.png
comparison-figures/aa_vs_metis/aa-dual-partition.png
comparison-figures/aa_vs_metis/cat_aa_vs_metis_comparison.pdf
```

探索结果显示这些文件可能位于：

```text
/home/zcy/workspace/records/primal-dual_modes/_tog454_stage_used/comparison-figures/aa_vs_metis/
```

需要在实施时确认实际存在位置。

#### 目标图目录

应复制或链接到：

```text
/home/zcy/workspace/records/zjuthesis/body/graduate/paper3/figures/comparison-figures/aa_vs_metis/
```

#### LaTeX 中的图片路径

保持：

```latex
comparison-figures/aa_vs_metis/aa-primal-partition.png
comparison-figures/aa_vs_metis/aa-dual-partition.png
comparison-figures/aa_vs_metis/cat_aa_vs_metis_comparison.pdf
```

因为当前 paper3 的 `\graphicspath` 已指向：

```text
body/graduate/paper3/figures/
```

#### 写作定位

该实验不应写成：

> 轴对齐划分优于 METIS 划分。

应写成：

> 在 Cat 拉普拉斯算例中，轴对齐划分在当前实验设置下取得了更低误差和更短总运行时间。该结果说明，划分策略会影响原始—对偶子结构的错位关系和互补子结构构造成本。

#### 机制解释重点

需要说明：

- 轴对齐划分更容易形成规则错位的相邻子结构；
- METIS 虽然能优化界面规模，但可能引入更多原始/对偶划分界面交叉；
- 界面交叉区域需要额外互补子结构来恢复局部相位完备性；
- 这些额外结构会增加基函数构造与降维装配成本；
- 因此划分策略会影响端到端效率。

---

### 4. 新增实验：子结构数量对求解质量与效率的影响

#### 来源

```text
/home/zcy/workspace/records/primal-dual_modes/paper-body/5.0-results.tex
```

原始小节：

```latex
\subsubsection{\modified{Effect of number of substructures.}}
```

对应图：

```latex
\label{fig:dragon-tet-tradeoff}
```

#### 目标位置

紧接在“轴对齐划分与 METIS 划分的对比”之后，`\subsection{应用验证}` 之前。

建议新增：

```latex
\paragraph{子结构数量对求解质量与效率的影响}
```

#### 原始图文件

源图文件：

```text
/home/zcy/workspace/records/primal-dual_modes/figures/dragon_tet/
```

包括：

```text
np4-primal-partition.png
np8-primal-partition.png
np16-primal-partition.png
np4-dual-partition.png
np8-dual-partition.png
np16-dual-partition.png
dragon_tet_performance.pdf
dragon_tet_breakdown.pdf
```

#### 目标图目录

应复制或链接到：

```text
/home/zcy/workspace/records/zjuthesis/body/graduate/paper3/figures/dragon_tet/
```

#### LaTeX 中的图片路径

原论文路径带有 `figures/` 前缀：

```latex
figures/dragon_tet/...
```

迁移到博士论文时必须去掉 `figures/` 前缀，写成：

```latex
dragon_tet/np4-primal-partition.png
dragon_tet/np8-primal-partition.png
dragon_tet/np16-primal-partition.png
dragon_tet/np4-dual-partition.png
dragon_tet/np8-dual-partition.png
dragon_tet/np16-dual-partition.png
dragon_tet/dragon_tet_performance.pdf
dragon_tet/dragon_tet_breakdown.pdf
```

#### 写作定位

该实验应作为参数敏感性或适用边界分析，不应写成负面结果，也不应写成性能宣传。

不要写：

> 子结构数量越多效果越差。

应写：

> 在 Dragon 四面体模型上，增加子结构数量并不必然带来端到端效率提升。

#### 机制解释重点

需要说明：

- 增加子结构数量会降低局部子结构特征值问题规模；
- 但会增加全局基函数数量、矩阵降维代价和缩减系统求解代价；
- 在该实验中，后者逐渐抵消前者节省；
- 因此子结构数量需要在局部求解规模、相位补足效果、矩阵装配规模和缩减求解成本之间权衡。

---

## 二、图表中文化计划

新增要求是：

> 新生成的图片中的英文要换成中文。可以把数据 soft link 过来，脚本也拷贝过来，然后修改脚本重新生成图片。

因此，不应只复制现成 PDF/PNG，而应尽量找到对应生成脚本和数据，重新生成中文版图。

### 1. 需要中文化的图表

#### A. 轴对齐 vs. METIS 图

目标图：

```text
cat_aa_vs_metis_comparison.pdf
```

可能包含英文内容：

- legend；
- axis label；
- method name；
- title；
- annotation。

建议翻译：

| 英文 | 中文建议 |
|---|---|
| Axis-aligned | 轴对齐划分 |
| METIS | METIS 划分 |
| Error | 误差 |
| Time | 时间 |
| Total Time | 总计算时间 |
| Number of modes | 模态数量 |
| Ours | 本文方法 |
| Traditional CMS | 传统模态综合法 |
| IMR | 界面模态缩减法 |
| AMLS | 自动多层子结构法 |

如果 partition PNG 本身没有英文标注，可以直接复用；若图内有英文标题，也需要重新生成或替换标注。

#### B. Dragon tet 子结构数量图

目标图：

```text
dragon_tet_performance.pdf
dragon_tet_breakdown.pdf
```

可能包含英文内容：

- error-time 曲线坐标轴；
- runtime breakdown 的 legend；
- stage names；
- `n_p=4,8,16` 标注；
- title；
- method labels。

建议翻译：

| 英文 | 中文建议 |
|---|---|
| Error | 误差 |
| Time | 时间 |
| Runtime | 运行时间 |
| Breakdown | 代价分解 |
| Eigensolve | 子结构特征求解 |
| Matrix Reduction | 矩阵降维 |
| Reduced Solve | 缩减系统求解 |
| Preprocess | 预处理 |
| Postprocess | 后处理 |
| Total | 总时间 |
| Number of Substructures | 子结构数量 |
| Primal Partition | 原始划分 |
| Dual Partition | 对偶划分 |

---

## 三、数据与脚本迁移计划

### 1. 数据迁移原则

为避免重复拷贝大型数据，建议采用 soft link：

- 原始数据目录用软链接；
- 生成脚本复制到 thesis 项目内；
- 修改复制后的脚本；
- 不修改原始论文仓库中的脚本；
- 生成后的中文图片保存在 thesis 的 `paper3/figures` 目录下。

### 2. 目标生成目录

建议在 thesis 项目中建立：

```text
/home/zcy/workspace/records/zjuthesis/script/paper3_figures/
```

推荐结构：

```text
script/paper3_figures/
├── aa_vs_metis/
│   ├── data -> /home/zcy/workspace/records/primal-dual_modes/.../aa_vs_metis/data
│   ├── generate_aa_vs_metis_cn.py
│   └── README_or_notes.txt
├── dragon_tet/
│   ├── data -> /home/zcy/workspace/records/primal-dual_modes/.../dragon_tet/data
│   ├── generate_dragon_tet_cn.py
│   └── README_or_notes.txt
```

如果原始脚本不是 Python，也按原脚本语言复制，例如 `.sh`、`.m`、`.ipynb`、`.py`。

### 3. 脚本查找计划

#### 对 `aa_vs_metis`

搜索关键词：

```text
aa_vs_metis
cat_aa_vs_metis_comparison
aa-primal-partition
aa-dual-partition
```

重点查找：

```text
/home/zcy/workspace/records/primal-dual_modes/
```

可能位置：

```text
comparison-figures/aa_vs_metis/
_tog454_stage_used/comparison-figures/aa_vs_metis/
source_data/
comparison-data/
figures/
```

#### 对 `dragon_tet`

搜索关键词：

```text
dragon_tet
dragon_tet_performance
dragon_tet_breakdown
np4-primal-partition
np8-primal-partition
np16-primal-partition
```

重点查找：

```text
/home/zcy/workspace/records/primal-dual_modes/figures/dragon_tet/
/home/zcy/workspace/records/primal-dual_modes/source_data/
/home/zcy/workspace/records/primal-dual_modes/comparison-data/
```

### 4. 脚本修改原则

修改脚本时遵循：

1. 不改原始仓库脚本；
2. 复制脚本到 thesis 仓库；
3. 软链接数据；
4. 修改输出路径为 thesis 图片目录；
5. 修改图中英文为中文；
6. 保持数据、曲线、数值不变；
7. 不改变实验结论；
8. 重新生成 PDF/PNG；
9. 用 `latexmk` 验证图表可编译。

### 5. 中文字体与 Matplotlib 设置

如果生成脚本使用 Python/Matplotlib，需要处理中文字体。建议优先使用系统中可用中文字体，例如：

```python
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = [
    "Noto Sans CJK SC",
    "Source Han Sans SC",
    "SimHei",
    "WenQuanYi Zen Hei",
]
plt.rcParams["axes.unicode_minus"] = False
```

如果生成 PDF，并希望 LaTeX 编译中字体稳定，可以考虑：

- 直接生成 PDF；
- 或生成 SVG/PDF 后检查中文是否嵌入；
- 若中文字体显示异常，改用 PNG 输出；
- 最终以 thesis 编译成功和图中文字可读为准。

---

## 四、LaTeX 图表格式计划

### 1. 轴对齐 vs. METIS 图

推荐结构：

```latex
\begin{figure}[tbp]
  \centering
  \begin{subfigure}{\linewidth}
    \centering
    \includegraphics[width=0.38\linewidth]{comparison-figures/aa_vs_metis/aa-primal-partition.png}\hfill
    \includegraphics[width=0.38\linewidth]{comparison-figures/aa_vs_metis/aa-dual-partition.png}
    \subcaption{轴对齐划分下的原始划分与对偶划分。}
  \end{subfigure}

  \begin{subfigure}{\linewidth}
    \centering
    \includegraphics[width=\linewidth]{comparison-figures/aa_vs_metis/cat_aa_vs_metis_comparison.pdf}
  \end{subfigure}

  \caption[轴对齐划分与 METIS 划分的对比]{轴对齐划分与 METIS 划分的对比。上方展示 Cat 模型上的轴对齐原始划分与对偶划分；下方比较了本文方法在轴对齐划分与 METIS 划分下的误差--时间表现。}
  \label{fig:laplacian-aa-vs-metis}
\end{figure}
```

注意：

- 不使用 `\textbf{}`；
- 不使用 `\modified{}`；
- 使用 `[tbp]`；
- caption 简洁客观。

### 2. Dragon 子结构数量图

推荐结构：

```latex
\begin{figure}[tbp]
  \centering
  \begin{tabular}{@{}c c c@{}}
    \includegraphics[width=0.31\linewidth]{dragon_tet/np4-primal-partition.png} &
    \includegraphics[width=0.31\linewidth]{dragon_tet/np8-primal-partition.png} &
    \includegraphics[width=0.31\linewidth]{dragon_tet/np16-primal-partition.png} \\
    \includegraphics[width=0.31\linewidth]{dragon_tet/np4-dual-partition.png} &
    \includegraphics[width=0.31\linewidth]{dragon_tet/np8-dual-partition.png} &
    \includegraphics[width=0.31\linewidth]{dragon_tet/np16-dual-partition.png} \\
  \end{tabular}

  \includegraphics[width=\linewidth]{dragon_tet/dragon_tet_performance.pdf}
  \includegraphics[width=\linewidth]{dragon_tet/dragon_tet_breakdown.pdf}

  \caption[子结构数量对 Dragon 模型求解性能的影响]{子结构数量对 Dragon 四面体模型求解性能的影响。上方展示 $n_p=4,8,16$ 时的原始划分与对偶划分；下方给出对应的误差--时间曲线和时间代价分解。}
  \label{fig:dragon-tet-tradeoff}
\end{figure}
```

---

## 五、正文写作计划

### 1. 轴对齐 vs. METIS 段落结构

建议写成两段。

#### 第一段：说明实验目的和观察结果

内容包括：

- 已经在前面分别测试了轴对齐和 METIS；
- 此处进一步直接比较二者；
- 在 Cat 算例中，轴对齐划分表现出更低误差和较短时间；
- 结论限定在当前实验设置下。

#### 第二段：解释机制和边界

内容包括：

- 轴对齐划分更容易产生规则错位；
- METIS 可能引入更多界面交叉；
- 交叉需要互补子结构；
- 额外互补子结构增加构造和降维成本；
- 因此划分策略需要结合几何和计算代价选择。

### 2. 子结构数量段落结构

建议写成两段。

#### 第一段：说明实验设计

内容包括：

- 在 Dragon 四面体模型上改变 $n_p$；
- 比较 $n_p=4,8,16$；
- 观察误差--时间曲线和代价分解；
- 说明这是对子结构数量影响的补充分析。

#### 第二段：说明观察与机制

内容包括：

- 子结构数量增加会降低局部特征问题规模；
- 但矩阵降维和缩减求解成本会上升；
- 在该实验中整体近似质量并未改善；
- 因此不能只按局部子问题规模最小化选择子结构数量；
- 需要综合考虑相位补足、装配规模和缩减求解成本。

---

## 六、整体写作风格要求

### 1. 推荐使用的表达

- “如 \Cref{...} 所示”；
- “可以看到”；
- “在该实验设置下”；
- “结果显示”；
- “实验表明”；
- “这一现象说明”；
- “其原因在于”；
- “需要注意的是”；
- “并不意味着”；
- “需要在……之间进行权衡”。

### 2. 避免使用的表达

避免：

- “显著优于”；
- “全面优于”；
- “完全证明”；
- “绝对优势”；
- “大幅领先”；
- “彻底解决”；
- “最优划分”；
- “子结构越多越差”；
- “METIS 不如轴对齐”。

### 3. 推荐语气

应该是：

> 在该模型和当前设置下观察到某种趋势，并给出机制解释。

而不是：

> 本文方法或某个划分策略普遍优于其它方法。

---

## 七、实施步骤计划

### Step 1：确认新增图和生成脚本位置

目标是找到：

- `aa_vs_metis` 图的生成脚本和数据；
- `dragon_tet` 图的生成脚本和数据。

搜索关键词：

```text
aa_vs_metis
cat_aa_vs_metis_comparison
dragon_tet
dragon_tet_performance
dragon_tet_breakdown
```

输出应列出：

- 数据路径；
- 脚本路径；
- 当前生成输出路径；
- 脚本语言；
- 依赖库。

### Step 2：建立 thesis 内的图生成工作区

建议建立：

```text
/home/zcy/workspace/records/zjuthesis/script/paper3_figures/
```

结构：

```text
script/paper3_figures/
├── aa_vs_metis/
└── dragon_tet/
```

### Step 3：迁移数据与脚本

数据用 soft link：

```text
script/paper3_figures/aa_vs_metis/data -> 原始数据目录
script/paper3_figures/dragon_tet/data -> 原始数据目录
```

脚本复制原始生成脚本，并命名为：

```text
generate_aa_vs_metis_cn.*
generate_dragon_tet_cn.*
```

不修改原始论文仓库脚本。

### Step 4：修改脚本为中文图表

修改内容：

1. 坐标轴；
2. 图例；
3. 标题；
4. 阶段名；
5. 方法名；
6. 输出路径；
7. 字体设置；
8. PDF/PNG 输出格式。

输出到：

```text
body/graduate/paper3/figures/comparison-figures/aa_vs_metis/
body/graduate/paper3/figures/dragon_tet/
```

### Step 5：生成中文图表

生成：

```text
comparison-figures/aa_vs_metis/cat_aa_vs_metis_comparison.pdf
dragon_tet/dragon_tet_performance.pdf
dragon_tet/dragon_tet_breakdown.pdf
```

如果 partition 图片本身无英文，可直接复用或软链接；如果有英文，也要重新生成或替换标注。

### Step 6：修改 `4_results.tex`

修改点：

1. `tab:statistics`：
   - Cat 行增加 `fig:laplacian-aa-vs-metis`；
   - `multirow{4}` 改为 `multirow{5}`；
   - 新增 Dragon 行。
2. `误差度量`：
   - 新增 `\epsilon_{\text{eq}}`。
3. `性能评估：误差--时间曲线`：
   - `\epsilon_{\text{ev}}` 改为 `\epsilon_{\text{ev}} 或 \epsilon_{\text{eq}}`。
4. `方法对比分析`：
   - `fig:comp-timing-vs-nev` 后新增：
     - `\paragraph{轴对齐划分与 METIS 划分的对比}`；
     - `fig:laplacian-aa-vs-metis`；
     - `\paragraph{子结构数量对求解质量与效率的影响}`；
     - `fig:dragon-tet-tradeoff`。
5. `应用验证` 开头段落视情况增加过渡，例如：
   - “在上述方法对比与参数影响分析之后，本节进一步展示……”。

### Step 7：编译验证

使用项目要求的命令：

```bash
latexmk
```

不要使用单独 `xelatex`。

验证：

- 图片路径是否正确；
- 中文图中文字是否显示；
- `\Cref{fig:laplacian-aa-vs-metis}` 是否解析；
- `\Cref{fig:dragon-tet-tradeoff}` 是否解析；
- `\Cref{eq:error-eq}` 是否解析；
- 表格是否溢出；
- 图片是否过大；
- caption 是否进入目录正常；
- 是否出现字体缺失或 PDF 中文乱码。

### Step 8：人工检查 PDF

重点检查：

1. 新增图是否中文化完整；
2. 图中文字是否过小；
3. 图例是否遮挡曲线；
4. 坐标轴是否清楚；
5. Dragon 图是否过高导致浮动位置异常；
6. 新增段落是否与前后文衔接自然；
7. 新增结论是否过强；
8. 是否符合“严谨、客观、不夸大”。

---

## 八、风险与注意事项

### 1. 图脚本可能找不到

若找不到原始生成脚本，有两种方案。

优先方案：

> 从原始数据重新写一个最小生成脚本，严格复现原图数据和曲线。

备选方案：

> 使用现有 PDF/PNG，但这不满足“英文换中文”的要求，只有在数据或脚本缺失时作为临时方案。

### 2. 中文字体可能导致 PDF 编译问题

如果 Matplotlib 输出 PDF 中文不稳定：

- 尝试嵌入 Noto Sans CJK；
- 或改用 PNG；
- 或使用 LaTeX/TikZ/PGF 生成；
- 最终以 thesis 编译成功和文字清晰为准。

### 3. 图名和 label 不要改变

应保留：

```latex
fig:laplacian-aa-vs-metis
fig:dragon-tet-tradeoff
eq:error-eq
```

这样与原始论文和统计表引用保持一致。

### 4. 不要保留原论文 revision 标记

迁移时删除：

```latex
\modified{...}
\textcolor{modified}{...}
```

博士论文中不需要显示论文修改痕迹。

### 5. 不要照搬原文强表述

原始论文中的：

- `outperforms`；
- `orders of magnitude`；
- `superior`；
- `significantly`；
- `drastically`。

需要降调处理。

---

## 九、最终交付物

### 1. 新增或更新图片

```text
body/graduate/paper3/figures/comparison-figures/aa_vs_metis/
body/graduate/paper3/figures/dragon_tet/
```

包括中文化后的：

```text
cat_aa_vs_metis_comparison.pdf
dragon_tet_performance.pdf
dragon_tet_breakdown.pdf
```

以及必要的 partition 图片。

### 2. 新增图生成脚本

```text
script/paper3_figures/aa_vs_metis/
script/paper3_figures/dragon_tet/
```

包括：

- 复制并修改后的脚本；
- 数据 soft link；
- 输出路径配置；
- 中文字体配置。

### 3. 修改后的 LaTeX

```text
body/graduate/paper3/4_results.tex
```

新增：

- `\epsilon_{\text{eq}}`；
- Dragon 表格行；
- 轴对齐 vs. METIS 小节和图；
- 子结构数量影响小节和图。

### 4. 编译验证结果

使用：

```bash
latexmk
```

验证通过，或记录剩余问题。

---

## 十、建议执行顺序

推荐按以下顺序实施：

1. 先找脚本和数据；
2. 先生成中文图；
3. 再修改 `4_results.tex`；
4. 最后统一编译检查。

这样可以避免 LaTeX 先引用不存在图片的风险，也便于先解决中文字体和图表重生成问题。
