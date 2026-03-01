import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# 导入 colormap, Normalize 和 Line2D
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from matplotlib.lines import Line2D

print("--- 开始生成最终版图表 (统一样式) ---")

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "figures",
    ),
)
from plot_style_config import get_style, apply_style

SCHEME = os.environ.get('PLOT_COLOR_SCHEME', 'teal_coral')
STYLE = get_style(SCHEME)
apply_style(STYLE, scale="double_column")

LABEL_FONTSIZE = STYLE.scaled_fontsize("label", "double_column")
LEGEND_FONTSIZE = STYLE.scaled_fontsize("legend", "double_column")
TICK_FONTSIZE = STYLE.scaled_fontsize("tick", "double_column")

FIG_SIZE = (12, 7)
DPI = 300
LINE_WIDTH = 4
MARKER_SIZE = 12

# --- 2. 加载数据 ---
csv_file = "results_diff_partition.csv"
try:
    df = pd.read_csv(csv_file)
    print(f"成功加载 '{csv_file}'")
except FileNotFoundError:
    print(f"错误: 文件 '{csv_file}' 未找到。")
    exit()
except Exception as e:
    print(f"读取 '{csv_file}' 时出错: {e}")
    exit()

# --- 3. 数据预处理和映射 ---
required_cols = ["accuracy", "nep", "time", "algorithm", "group"]
if not all(col in df.columns for col in required_cols):
    print(f"错误: CSV 文件必须包含以下列: {', '.join(required_cols)}")
    exit()

try:
    df["group_value"] = df["group"].astype(str).str.split("_").str[0].astype(int)
    print("成功从 'group' 列提取了数值。")
except Exception as e:
    print(f"错误: 无法从 'group' 列提取数值 (例如 '4_5' -> 4)。 错误: {e}")
    exit()

# b. 'algorithm' -> 标记
unique_algorithms = sorted(df["algorithm"].unique())
markers = ["s", "X", "o", "D", "^", "v"]
algorithm_marker_map = {
    alg: markers[i % len(markers)] for i, alg in enumerate(unique_algorithms)
}

# d. 'group_value' -> 颜色 (使用 Colormap)
cmap = STYLE.get_sequential_cmap()
norm = Normalize(vmin=df["group_value"].min(), vmax=df["group_value"].max())
sm = ScalarMappable(cmap=cmap, norm=norm)

# --- 4. 创建绘图 (1行2列), 共享 Y 轴 ---
print("正在创建图表...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIG_SIZE, sharey=True)

# --- 设置所有子图外边框为纯黑实线 ---
for ax in [ax1, ax2]:
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_edgecolor(STYLE.ui_colors["spine"])
        spine.set_linewidth(1.5)

# 绘制数据
grouped = df.groupby(["algorithm", "group"])
for (alg, grp), subset in grouped:
    marker = algorithm_marker_map[alg]
    group_val = subset["group_value"].iloc[0]
    color = cmap(norm(group_val))
    subset_ax1 = subset.sort_values(by="nep")
    ax1.plot(
        subset_ax1["nep"],
        subset_ax1["accuracy"],
        color=color,
        linestyle="solid",
        marker=marker,
        linewidth=LINE_WIDTH,
        markersize=MARKER_SIZE,
    )
    subset_ax2 = subset.sort_values(by="time")
    ax2.plot(
        subset_ax2["time"],
        subset_ax2["accuracy"],
        color=color,
        linestyle="solid",
        marker=marker,
        linewidth=LINE_WIDTH,
        markersize=MARKER_SIZE,
    )

# --- 5. 样式化: 标题和标签 ---
ax1.set_xlabel(r"$q_{\mathcal{I}}$", fontsize=LABEL_FONTSIZE, wrap=True)
ax1.set_ylabel(r"$\epsilon_{ev}$", fontsize=LABEL_FONTSIZE)
ax1.set_yscale("log")
ax1.tick_params(axis="both", which="major", labelsize=TICK_FONTSIZE)
ax1.grid(False)

ax2.set_xlabel("Time (s)", fontsize=LABEL_FONTSIZE)
ax2.set_yscale("log")
ax2.tick_params(axis="both", which="major", labelsize=TICK_FONTSIZE)
ax2.grid(False)

# --- 6. 添加 Algorithm 图例 (内部) ---
TARGET_NAME = "Schur and Eigen-free IMR"
legend_order = sorted(
    algorithm_marker_map.keys(), key=lambda n: (0 if n == TARGET_NAME else 1, n)
)
alg_handles = []
for alg_name in legend_order:
    marker = algorithm_marker_map[alg_name]
    line = Line2D(
        [0],
        [0],
        color=STYLE.ui_colors["spine"],
        linestyle="None",
        marker=marker,
        label=alg_name,
        markersize=MARKER_SIZE,
    )
    alg_handles.append(line)

fig_legend = fig.legend(
    handles=alg_handles,
    ncol=len(algorithm_marker_map),
    fontsize=LEGEND_FONTSIZE,
    loc="upper center",
    bbox_to_anchor=(0.5, 0.97),
    frameon=False,
    borderpad=0.0,
    labelspacing=0.0,
    handlelength=0,
    handletextpad=0.4,
)

# --- 7. 手动调整布局并添加 Colorbar ---
fig.subplots_adjust(left=0.1, right=0.88, bottom=0.1, top=0.90, wspace=0.02)

cbar_ax = fig.add_axes((0.90, 0.1, 0.03, 0.8))
for spine in cbar_ax.spines.values():
    spine.set_edgecolor(STYLE.ui_colors["spine"])
    spine.set_linewidth(1.5)

ticks = sorted(df["group_value"].unique())
cbar = fig.colorbar(sm, cax=cbar_ax, ticks=ticks)
cbar.set_label(r"Number of substructures of $\mathcal{P}^p$", size=LABEL_FONTSIZE)
cbar.ax.tick_params(labelsize=TICK_FONTSIZE)

# --- 8. 保存绘图 ---
output_file_png = "accuracy_plots_final_v4.png"
output_file_pdf = "accuracy_plots_final_v4.pdf"
try:
    plt.savefig(output_file_png, dpi=DPI, bbox_inches="tight")
    plt.savefig(output_file_pdf, dpi=DPI, bbox_inches="tight")
    print(f"\n成功保存图表到: {output_file_png} 与 {output_file_pdf}")
except Exception as e:
    print(f"保存图表时出错: {e}")

print("--- 绘图完成 ---")
