import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# --- 1. Parameters ---
# Define the subdomain for visualization
a = 2.0
b = 7.0
D = b - a  # Length of the subdomain

# Number of internal modes to visualize for each basis
M = 4

# --- START: 应用统一样式 ---
print("--- 开始生成 Basis Function 图表 (应用统一样式) ---")

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style_config import get_style, apply_style
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))), "script"))
from thesis_figure_config import setup_figure_fonts
setup_figure_fonts()

SCHEME = os.environ.get('PLOT_COLOR_SCHEME', 'teal_coral')
STYLE = get_style(SCHEME)
apply_style(STYLE, scale='double_column')

# 定义字体大小
TITLE_FONTSIZE = STYLE.scaled_fontsize('title', 'double_column')
LABEL_FONTSIZE = STYLE.scaled_fontsize('label', 'double_column')
LEGEND_FONTSIZE = STYLE.scaled_fontsize('legend', 'double_column')
TICK_FONTSIZE = STYLE.scaled_fontsize('tick', 'double_column')

FIG_SIZE = (16, 6)
DPI = 300
LINE_WIDTH = 2
OUTPUT_FILE = 'basis.png'
# --- END: 样式应用 ---


# --- 2. Plotting Setup ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIG_SIZE, sharey=True)
x_vals = np.linspace(a, b, 400)
x_local = x_vals - a  # Local coordinate [0, D] for basis functions

# --- 3. Plotting the Frequency-Adapted Basis (Left Panel) ---
ax1.text(0.98, 0.95, "固定相位基函数", transform=ax1.transAxes,
         ha='right', va='top', fontsize=LABEL_FONTSIZE)

# 为 M 条线从 viridis 调色板生成 M 个颜色
colors_ax1 = STYLE.get_sequential_cmap()(np.linspace(0.3, 1, M))
print(f"为左侧图(ax1)的 {M} 条线生成 Blues 颜色。")

for n in range(1, M + 1):
    y_vals = np.sin(n * np.pi * x_local / D)
    ax1.plot(x_vals, y_vals, label=f"n={n} (sin)", linewidth=LINE_WIDTH, color=colors_ax1[n-1])

ax1.set_xlabel(r"全局坐标 $x$", fontsize=LABEL_FONTSIZE)
ax1.set_ylabel("基函数值", fontsize=LABEL_FONTSIZE)
ax1.grid(False)
ax1.legend(fontsize=LEGEND_FONTSIZE)
ax1.axhline(0, color=STYLE.ui_colors['spine'], linewidth=0.5)
ax1.tick_params(axis='both', which='major', labelsize=TICK_FONTSIZE)

# --- 4. Plotting the Phase-Adapted Basis (Right Panel) ---
ax2.text(0.98, 0.95, "完整相位基函数", transform=ax2.transAxes,
         ha='right', va='top', fontsize=LABEL_FONTSIZE)
num_pairs = M // 2
colors_ax2 = colors_ax1

for n in range(1, num_pairs + 1):
    # Plot the sine component (the "hammer")
    y_sin = np.sin(n * np.pi * x_local / D)
    ax2.plot(x_vals, y_sin, linestyle="-", color=colors_ax2[n - 1], label=f"n={n} (sin)", linewidth=LINE_WIDTH)

    # Plot the cosine component (the "screwdriver")
    y_cos = np.cos(n * np.pi * x_local / D)
    ax2.plot(x_vals, y_cos, linestyle="--", color=colors_ax2[n - 1], label=f"n={n} (cos)", linewidth=LINE_WIDTH)

# If M is odd, add the last remaining sine term
if M % 2 != 0:
    n = num_pairs + 1
    y_sin = np.sin(n * np.pi * x_local / D)
    ax2.plot(x_vals, y_sin, linestyle="-", color=colors_ax2[n - 1], label=f"n={n} (sin)", linewidth=LINE_WIDTH)

ax2.set_xlabel(r"全局坐标 $x$", fontsize=LABEL_FONTSIZE)
ax2.grid(False)
ax2.legend(fontsize=LEGEND_FONTSIZE)
ax2.axhline(0, color=STYLE.ui_colors['spine'], linewidth=0.5)
ax2.tick_params(axis='both', which='major', labelsize=TICK_FONTSIZE)

# --- 5. Final Touches ---
plt.tight_layout()

try:
    plt.savefig(OUTPUT_FILE, dpi=DPI)
    pdf_path = OUTPUT_FILE[:-4] + '.pdf' if OUTPUT_FILE.lower().endswith('.png') else OUTPUT_FILE + '.pdf'
    plt.savefig(pdf_path, dpi=DPI)
    print(f"\n成功保存图表到: {OUTPUT_FILE} 与 {pdf_path}")
except Exception as e:
    print(f"保存图表时出错: {e}")

print("--- 绘图完成 ---")
