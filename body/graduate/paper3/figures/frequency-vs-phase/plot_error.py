import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib import cm
import os
import sys

print("--- 脚本开始 ---")

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style_config import get_style, apply_style

SCHEME = os.environ.get('PLOT_COLOR_SCHEME', 'teal_coral')
STYLE = get_style(SCHEME)
apply_style(STYLE, scale='double_column')

# 定义字体大小
TITLE_FONTSIZE = STYLE.scaled_fontsize('title', 'double_column')
LABEL_FONTSIZE = STYLE.scaled_fontsize('label', 'double_column')
LEGEND_FONTSIZE = STYLE.scaled_fontsize('legend', 'double_column')
TICK_FONTSIZE = STYLE.scaled_fontsize('tick', 'double_column')
DPI = 300
LINE_WIDTH = 2
MARKER_SIZE = 12

# --- 2. 加载您的新数据 ---
FILE_FIXED = "phase-fixed-error.txt"
FILE_COMPLETE = "phase-complete-error.txt"

try:
    errors_grid_freq = np.loadtxt(FILE_FIXED, delimiter=',')
    errors_grid_phase = np.loadtxt(FILE_COMPLETE, delimiter=',')
    print(f"成功从 '{FILE_FIXED}' 和 '{FILE_COMPLETE}' 加载数据。")
except Exception as e:
    print(f"错误: 无法加载数据文件。请确保文件存在且格式正确。 {e}")
    exit()

# --- 3. 定义坐标轴和网格 ---

# 根据您的说明：
# X 轴来自行 
n_rows = errors_grid_freq.shape[0]
m_values = np.arange(1, n_rows + 1) * 21  # X-axis ticks: [21, 42, ..., 378]

# Y 轴来自列 
n_cols = errors_grid_freq.shape[1]
n_global_values = np.arange(1, n_cols + 1)  # Y-axis ticks: [1, 2, ..., 96]

print(f"数据维度: {n_rows} 行 (X轴) x {n_cols} 列 (Y轴)")
print(f"X 轴 (Substructure Eig): {m_values.shape[0]} 个点, 从 {m_values[0]} 到 {m_values[-1]}")
print(f"Y 轴 (Global Order): {n_global_values.shape[0]} 个点, 从 {n_global_values[0]} 到 {n_global_values[-1]}")

# !!! 关键: 我们需要转置数据以匹配 X/Y 轴的期望
errors_grid_freq_T = errors_grid_freq.T
errors_grid_phase_T = errors_grid_phase.T

# 计算比率网格（已转置）
ratio_grid_T = errors_grid_freq_T / np.maximum(errors_grid_phase_T, 1e-16)
# --- 4. 绘图 (使用 lap_cms.py 的布局) ---

fig, axes = plt.subplots(1, 3, figsize=(16, 6), sharey=True)
# 与 lap_cms.py 一致

# 定义共享的颜色尺度
z_min = np.min(errors_grid_phase_T[errors_grid_phase_T > 0])
z_max = np.max(errors_grid_freq_T)
norm = LogNorm(vmin=max(z_min, 1e-16), vmax=z_max)

# 定义绘图范围 (extent)
# [x_min, x_max, y_min, y_max]
plot_extent = [
    m_values[0] - 10.5,   # X min (21 - 10.5 = 10.5)
    m_values[-1] + 10.5,  # X max (378 + 10.5 = 388.5)
    n_global_values[0] - 0.5,   # Y min (1 - 0.5 = 0.5)
    n_global_values[-1] + 0.5   # Y max (96 + 0.5 = 96.5)
]

# --- 图 1: Phase-fixed Heatmap ---
im1 = axes[0].imshow(
    errors_grid_freq_T,
    cmap=STYLE.get_sequential_cmap(),
    norm=norm,
    origin="lower",
    extent=plot_extent,
    aspect="auto",
)
axes[0].set_title("")
axes[0].set_xlabel("")
axes[0].set_ylabel("Global Eigen Order", fontsize=LABEL_FONTSIZE)

axes[0].set_xticks(m_values[::2])
axes[0].set_yticks(n_global_values[9::10])
axes[0].tick_params(labelsize=TICK_FONTSIZE)
axes[0].grid(False)

# --- 图 2: Phase-complete Heatmap ---
im2 = axes[1].imshow(
    errors_grid_phase_T,
    cmap=STYLE.get_sequential_cmap(),
    norm=norm,
    origin="lower",
    extent=plot_extent,
    aspect="auto",
)
axes[1].set_title("")
axes[1].set_xlabel("")
axes[1].set_xticks(m_values[::2])
axes[1].tick_params(labelsize=TICK_FONTSIZE)
axes[1].grid(False)

# --- 图 3: Ratio Heatmap ---
ratio_norm = LogNorm(vmin=1, vmax=np.max(ratio_grid_T[np.isfinite(ratio_grid_T)]))
im3 = axes[2].imshow(
    ratio_grid_T,
    cmap=STYLE.get_secondary_cmap(),
    norm=ratio_norm,
    origin="lower",
    extent=plot_extent,
    aspect="auto",
)
axes[2].grid(False)
axes[2].set_title("Improvement Factor\n(Ratio: fixed/complete)", fontsize=TITLE_FONTSIZE)
axes[2].set_xlabel("")
axes[2].set_xticks(m_values[::2])
axes[2].tick_params(labelsize=TICK_FONTSIZE)


# --- 5. 添加 Colorbars 和调整布局 (来自 lap_cms.py) ---

# 为误差图添加共享 colorbar (左侧紧凑, 标签在左)
cbar_ax = fig.add_axes([0.055, 0.12, 0.018, 0.72])
cbar = fig.colorbar(im1, cax=cbar_ax, orientation="vertical")
cbar.set_label("Average L2 Norm Error", size=LABEL_FONTSIZE, labelpad=2)
cbar.ax.yaxis.set_label_position('left')
cbar.ax.yaxis.tick_left()
cbar.ax.yaxis.set_ticks_position('left')
cbar.ax.tick_params(labelsize=TICK_FONTSIZE)

# 为比率图添加独立 colorbar (右侧紧凑)
cbar_ax_ratio = fig.add_axes([0.935, 0.12, 0.018, 0.72])
cbar_ratio = fig.colorbar(im3, cax=cbar_ax_ratio, orientation="vertical")
cbar_ratio.set_label("Improvement Factor", size=LABEL_FONTSIZE, labelpad=4)
cbar_ratio.ax.tick_params(labelsize=TICK_FONTSIZE)

# 使用 axes.text 手动放置单行标题居中（垂直居中于双行高度）
single_line_y = 1.12  # 位于两行标题的中间偏上
axes[0].text(0.5, single_line_y, 'Error using $[\\mathbf{S}^p_{\\mathcal{I}}, \\mathbf{S}^p_b]$',
             ha='center', va='center', transform=axes[0].transAxes, fontsize=TITLE_FONTSIZE)
axes[1].text(0.5, single_line_y, 'Error using $[\\mathbf{S}^p_{\\mathcal{I}}, \\mathbf{S}^p_b, \\mathbf{S}^d_{\\mathcal{I}}]$',
             ha='center', va='center', transform=axes[1].transAxes, fontsize=TITLE_FONTSIZE)

# 调整布局矩形以扩大中间绘图区并为共享 xlabel 留空间
plt.tight_layout(rect=[0.09, 0.07, 0.93, 0.96])
fig.text(0.5, 0.05, 'Total number of Substructure Eigenmodes', ha='center', va='center', fontsize=LABEL_FONTSIZE)

# --- 6. 保存 ---
OUTPUT_FILE = "fixed-vs-complete-eig-error.png"
try:
    plt.savefig(OUTPUT_FILE, dpi=DPI, bbox_inches='tight')
    pdf_path = OUTPUT_FILE[:-4] + '.pdf' if OUTPUT_FILE.lower().endswith('.png') else OUTPUT_FILE + '.pdf'
    plt.savefig(pdf_path, dpi=DPI, bbox_inches='tight')
    print(f"\n成功保存图表到: {OUTPUT_FILE} 与 {pdf_path}")
except Exception as e:
    print(f"保存图表时出错: {e}")

print("--- 绘图完成 ---")
