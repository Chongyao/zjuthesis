import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
import sys

# --- START: 应用统一样式 ---
print("--- 开始生成 Integration Diagram (应用统一样式) ---")

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style_config import get_style, apply_style

SCHEME = os.environ.get('PLOT_COLOR_SCHEME', 'teal_coral')
STYLE = get_style(SCHEME)
apply_style(STYLE, scale="double_column")

TITLE_FONTSIZE = STYLE.scaled_fontsize("title", "double_column")
LABEL_FONTSIZE = STYLE.scaled_fontsize("label", "double_column")
LEGEND_FONTSIZE = STYLE.scaled_fontsize("legend", "double_column")
TICK_FONTSIZE = STYLE.scaled_fontsize("tick", "double_column")

DPI = 300
LINE_WIDTH = 2
OUTPUT_FILE = "integration.png"
# --- END: 样式应用 ---

# --- 1. Parameters ---
L = 10.0  # Global domain length
l = 2.0  # Length of the sliding window
n_global_to_show = 5

# --- 2. Setup Plot ---
fig, ax = plt.subplots(1, 1, figsize=(12, 6))

x_global = np.linspace(0, L, 500)

cmap = STYLE.get_sequential_cmap()

# --- 3. Draw the Single Global Function ---
global_func_vals = np.sin(n_global_to_show * np.pi * x_global / L)
ax.plot(
    x_global,
    global_func_vals,
    color=cmap(0.2),
    linewidth=LINE_WIDTH,
    label=f"全局模态 (n={n_global_to_show})",
)
ax.axhline(0, color=STYLE.ui_colors["reference_line"], linestyle="--", linewidth=0.8)

# --- 4. Draw Two "Boat" Rectangles ---
window_starts = [L * 0.2, L * 0.45]

ax.set_ylim([-1.2, 1.2])
boat_y_min_norm = (0 - ax.get_ylim()[0]) / (ax.get_ylim()[1] - ax.get_ylim()[0])
boat_height_norm = 0.05

boat_colors = cmap(np.linspace(0.5, 0.9, 2))

for j, a_start in enumerate(window_starts):
    a_end = a_start + l
    current_boat_color = boat_colors[j]

    ax.axvspan(
        a_start,
        a_end,
        ymin=boat_y_min_norm,
        ymax=boat_y_min_norm + boat_height_norm,
        color=current_boat_color,
        alpha=0.6,
        hatch="///",
        edgecolor=STYLE.method_colors["imr"],
        linewidth=0.5,
        zorder=2,
    )

    ax.vlines(
        a_start,
        ymin=ax.get_ylim()[0],
        ymax=ax.get_ylim()[1],
        color=STYLE.method_colors["imr"],
        linestyle="-",
        linewidth=1,
        alpha=0.7,
        zorder=1,
    )
    ax.vlines(
        a_end,
        ymin=ax.get_ylim()[0],
        ymax=ax.get_ylim()[1],
        color=STYLE.method_colors["imr"],
        linestyle="-",
        linewidth=1,
        alpha=0.7,
        zorder=1,
    )
    ax.vlines(
        a_start,
        ymin=boat_y_min_norm + boat_height_norm,
        ymax=boat_y_min_norm + boat_height_norm + 0.05,
        color=STYLE.method_colors["imr"],
        linestyle="-",
        linewidth=1,
        alpha=0.7,
        transform=ax.transAxes,
        zorder=1,
    )
    ax.vlines(
        a_end,
        ymin=boat_y_min_norm + boat_height_norm,
        ymax=boat_y_min_norm + boat_height_norm + 0.05,
        color=STYLE.method_colors["imr"],
        linestyle="-",
        linewidth=1,
        alpha=0.7,
        transform=ax.transAxes,
        zorder=1,
    )

# Add a shorter arrow
arrow_start_pos = window_starts[0]
arrow_end_pos = arrow_start_pos + l
arrow_y_pos_length = 0.4

ax.annotate(
    "",
    xy=(arrow_end_pos, arrow_y_pos_length),
    xytext=(arrow_start_pos, arrow_y_pos_length),
    arrowprops=dict(arrowstyle="<->", color="black", linewidth=1, shrinkA=0, shrinkB=0),
)
ax.text(
    arrow_start_pos + l / 2,
    arrow_y_pos_length + 0.05,
    f"子域长度 $l$",
    color="black",
    fontsize=LEGEND_FONTSIZE,
    ha="center",
    va="bottom",
    bbox=dict(
        facecolor=STYLE.ui_colors["annotation_bg"], alpha=0.7, edgecolor="none", pad=1
    ),
)


# Move "Window slides" and the green long arrow
slide_arrow_y_pos = -0.35
slide_text_y_pos = slide_arrow_y_pos - 0.1

arrow_start_x = 2.0
arrow_end_x = L - 2.0

ax.annotate(
    "",
    xy=(arrow_end_x, slide_arrow_y_pos),
    xytext=(arrow_start_x, slide_arrow_y_pos),
    arrowprops=dict(
        arrowstyle="->",
        color="black",
        linewidth=2,
        mutation_scale=20,
    ),
)
ax.text(
    (arrow_start_x + arrow_end_x) / 2,
    slide_text_y_pos,
    r"窗口滑动: $a \in [0, L-l]$",
    color="black",
    fontsize=LEGEND_FONTSIZE,
    ha="center",
    va="top",
    bbox=dict(
        facecolor=STYLE.ui_colors["annotation_bg"], alpha=0.7, edgecolor="none", pad=1
    ),
)


# --- 5. Final Touches ---
ax.set_title(
    f"集成误差滑动子结构示意图 (全局模态 $n={n_global_to_show}$)",
    fontsize=LABEL_FONTSIZE,
)
ax.set_xlabel("全局域坐标 $x$", fontsize=LABEL_FONTSIZE)
ax.set_ylabel("振幅", fontsize=LABEL_FONTSIZE)
ax.tick_params(axis="both", which="major", labelsize=TICK_FONTSIZE)

ax.grid(False)
ax.set_xlim([-0.5, L + 0.5])
ax.legend(
    loc="upper right",
    fontsize=LEGEND_FONTSIZE,
    facecolor=STYLE.ui_colors["legend_bg"],
    framealpha=0.8,
)

plt.tight_layout()

try:
    plt.savefig(OUTPUT_FILE, dpi=DPI)
    pdf_path = OUTPUT_FILE[:-4] + ".pdf"
    plt.savefig(pdf_path, dpi=DPI)
    print(f"\n成功保存图表到: {OUTPUT_FILE} 与 {pdf_path}")
except Exception as e:
    print(f"保存图表时出错: {e}")

print("--- 绘图完成 ---")
