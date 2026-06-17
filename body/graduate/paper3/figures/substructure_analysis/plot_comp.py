#!/usr/bin/env python3

"""
A comprehensive script to analyze and compare the performance of 'sub-eig' and
'sub-schur' methods using three data sources.

This script reads data from:
- benchmark_results.csv (sub-eig, large neig_blk range)
- benchmark_results_small.csv (sub-eig, small neig_blk range to improve interpolation)
- benchmark_results_schur_fixed_params.csv (sub-schur)

It produces two plots suitable for academic papers.
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize
from scipy.interpolate import interp1d
from matplotlib.patches import ConnectionPatch, Rectangle
import numpy as np
import sys
import os

# --- Unified Style Configuration ---
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style_config import get_style, apply_style

SCHEME = os.environ.get('PLOT_COLOR_SCHEME', 'teal_coral')
STYLE = get_style(SCHEME)
apply_style(STYLE, scale="double_column")

# Font sizes from unified config
TITLE_FONTSIZE = STYLE.scaled_fontsize("title", "double_column")
LABEL_FONTSIZE = STYLE.scaled_fontsize("label", "double_column")
LEGEND_FONTSIZE = STYLE.scaled_fontsize("legend", "double_column")
TICK_FONTSIZE = STYLE.scaled_fontsize("tick", "double_column")

# --- Configuration ---
EIG_CSV_LARGE = "benchmark_results.csv"
EIG_CSV_SMALL = "benchmark_results_small.csv"
SCHUR_CSV = "benchmark_results_schur_fixed_params.csv"
# Switched to a style with a white background
PLT_STYLE = "seaborn-v0_8-whitegrid"
SIZE_LIMIT = 1200  # Analyze up to size 1200


def load_and_prepare_data():
    """
    Loads data from all three CSV files, merges the 'sub-eig' data,
    and filters it for the analysis.
    """
    print("Loading benchmark data from three files...")
    try:
        df_eig_large = pd.read_csv(EIG_CSV_LARGE)
        df_eig_small = pd.read_csv(EIG_CSV_SMALL)
        df_schur = pd.read_csv(SCHUR_CSV)
    except FileNotFoundError as e:
        print(f"Error loading data: {e}")
        return None, None

    print("Data loaded. Merging 'sub-eig' datasets to improve accuracy...")
    df_eig_combined = pd.concat([df_eig_large, df_eig_small], ignore_index=True)
    df_eig_combined.drop_duplicates(
        subset=["size", "neig_blk"], keep="first", inplace=True
    )
    df_eig_combined.sort_values(by=["size", "neig_blk"], inplace=True)
    print(f"Total unique 'sub-eig' data points: {len(df_eig_combined)}")

    df_schur_filtered = df_schur[df_schur["size"] <= SIZE_LIMIT].copy()
    common_sizes = df_schur_filtered["size"].unique()
    df_eig_filtered = df_eig_combined[df_eig_combined["size"].isin(common_sizes)].copy()

    return df_eig_filtered, df_schur_filtered


def create_monotonic_interpolators(df_eig):
    """
    Creates robust interpolation models (cost -> neig_blk) by enforcing
    monotonicity on the cost data to handle measurement noise.
    """
    interpolators = {}
    for size, group in df_eig.groupby("size"):
        group_sorted = group.sort_values(by="neig_blk")
        monotonic_cost = group_sorted["sub_eig_cost_s"].cummax()
        f = interp1d(
            monotonic_cost,
            group_sorted["neig_blk"],
            bounds_error=False,
            fill_value="extrapolate",
        )
        interpolators[size] = f
    return interpolators


def plot_equivalence_bar_chart(df_eig, df_schur):
    """
    Plot 1: Generates the bar chart comparing equivalent performance.
    """
    print("\n--- Generating Plot 1: Equivalence Bar Chart ---")
    output_file_png = "eig_vs_schur_equivalence.png"
    output_file_pdf = "eig_vs_schur_equivalence.pdf"

    interpolators = create_monotonic_interpolators(df_eig)

    results = []
    for _, row in df_schur.iterrows():
        size = row["size"]
        if size in interpolators:
            equivalent_neig_blk = interpolators[size](row["sub_schur_total_cost"])
            results.append(
                {"DoFs": (size * size) / 3, "equivalent_neig_blk": equivalent_neig_blk}
            )
    df_comparison = pd.DataFrame(results)

    # --- Plotting ---
    plt.figure(figsize=(14, 8))
    y_values = pd.to_numeric(
        df_comparison["equivalent_neig_blk"], errors="coerce"
    ).fillna(0)
    max_val = y_values.max()
    normalized_colors = y_values / max_val if max_val > 0 else np.zeros(len(y_values))
    color_data = np.asarray(normalized_colors, dtype=float)

    x_labels = [f"{int(dof)}" for dof in df_comparison["DoFs"]]
    bars = plt.bar(
        x_labels,
        y_values,
        width=0.8,
        color=STYLE.get_sequential_cmap()(color_data),
        label="Equivalent eigenvalues solved by eig",
    )

    plt.axhline(
        y=3,
        color=STYLE.method_colors["imr"],
        linestyle="--",
        linewidth=2,
        label="schur Performance (3 Eigenvalues)",
    )

    for bar in bars:
        yval = bar.get_height()
        if yval > 0:
            plt.text(
                bar.get_x() + bar.get_width() / 2.0,
                yval + 0.1,
                f"{yval:.1f}",
                ha="center",
                va="bottom",
                fontsize=12,
            )

    plt.title("Performance Comparison: eig vs. schur", fontsize=TITLE_FONTSIZE)
    plt.xlabel("Degrees of Freedom (DoFs)", fontsize=LABEL_FONTSIZE)
    plt.ylabel(
        "Equivalent Number of Eigenvalues Solved", fontsize=LABEL_FONTSIZE, labelpad=28
    )
    plt.xticks(rotation=45, fontsize=TICK_FONTSIZE)
    plt.yticks(fontsize=TICK_FONTSIZE)
    from matplotlib.font_manager import FontProperties

    legend_font = FontProperties(size=LEGEND_FONTSIZE)
    plt.legend(prop=legend_font)
    plt.grid(False)  # Unified style: no grid
    plt.ylim(bottom=0)
    plt.tight_layout()
    plt.savefig(output_file_png, dpi=150)
    plt.savefig(output_file_pdf, dpi=150)
    plt.close()
    print(f"Saved: {output_file_png} and {output_file_pdf}")


def plot_timing_curves(df_eig, df_schur, legend_cfg=None):
    from matplotlib.gridspec import GridSpec

    fig = plt.figure(figsize=(12, 6))
    gs = GridSpec(1, 3, width_ratios=[2, 1, 0.08], wspace=0.15)
    ax = fig.add_subplot(gs[0, 0])
    ax_zoom = fig.add_subplot(gs[0, 1], sharey=None)
    # 设置主图和放大图四条边框为纯黑色线
    for spine in ["left", "right", "top", "bottom"]:
        ax.spines[spine].set_color(STYLE.ui_colors["spine"])  # 主图保持黑色
        ax.spines[spine].set_linewidth(1.5)
        ax_zoom.spines[spine].set_color(
            STYLE.ui_colors["highlight"]
        )  # 放大图改为浅蓝色
        ax_zoom.spines[spine].set_linewidth(1.5)
    from matplotlib.ticker import ScalarFormatter

    """
    Plot 2: Generates the timing curves with schur performance translated
    onto the same axes and connected with a line.
    """
    print("\\n--- Generating Plot 2: Timing Curves with Schur Overlay ---")
    plot_color = STYLE.method_colors["cms"]

    output_file_png = "schur_vs_eig_timing_curves.png"
    output_file_pdf = "schur_vs_eig_timing_curves.pdf"

    cost_to_neig_interpolators = create_monotonic_interpolators(df_eig)

    schur_equiv_points = []
    for _, row in df_schur.iterrows():
        size = row["size"]
        if size in cost_to_neig_interpolators:
            schur_cost = row["sub_schur_total_cost"]
            equiv_neig = cost_to_neig_interpolators[size](schur_cost)
            schur_equiv_points.append(
                {"size": size, "equiv_neig": equiv_neig, "cost": schur_cost}
            )

    df_schur_equiv = pd.DataFrame(schur_equiv_points)

    sizes = sorted(df_eig["size"].unique())

    # Create lists for line segments and their corresponding colors (size values)
    segments = []

    # only get neig_blk from <= 100
    segments_short = []
    colors_for_segments = []
    colors_for_segments_short = []
    for size in sizes:
        # Sort by neig_blk to ensure lines are drawn correctly
        df_size_eig = df_eig[df_eig["size"] == size].sort_values(by="neig_blk")

        # --- Main Plot Segments ---
        if len(df_size_eig) > 1:
            points = np.array(
                [df_size_eig["neig_blk"], df_size_eig["sub_eig_cost_s"]]
            ).T.reshape(-1, 1, 2)
            # print(points) # Removed verbose print
            size_segments = np.concatenate([points[:-1], points[1:]], axis=1)
            segments.extend(size_segments)
            colors_for_segments.extend([size] * len(size_segments))

            # --- Inset Plot Segments (neig_blk <= 100) ---
            df_size_eig_short = df_size_eig[df_size_eig["neig_blk"] <= 100]
            if len(df_size_eig_short) > 1:
                points_short = np.array(
                    [df_size_eig_short["neig_blk"], df_size_eig_short["sub_eig_cost_s"]]
                ).T.reshape(-1, 1, 2)
                size_segments_short = np.concatenate(
                    [points_short[:-1], points_short[1:]], axis=1
                )
                segments_short.extend(size_segments_short)
                colors_for_segments_short.extend(
                    [size] * len(size_segments_short)
                )  # Populate the new list

    # 主图
    norm = Normalize(vmin=min(sizes), vmax=max(sizes))
    lc = LineCollection(segments, cmap=STYLE.get_sequential_cmap(), norm=norm)
    lc.set_array(np.array(colors_for_segments))
    lc.set_linewidth(4.5)
    line = ax.add_collection(lc)
    # 色标放最右
    cax = fig.add_subplot(gs[0, 2])
    cbar = fig.colorbar(line, cax=cax)
    cbar.set_label("问题规模", size=LABEL_FONTSIZE)
    cbar.ax.tick_params(labelsize=TICK_FONTSIZE)
    for l in cbar.ax.yaxis.get_ticklabels():
        l.set_family("Times New Roman")

    # 主图：画全部数据
    if not df_schur_equiv.empty:
        df_schur_equiv.sort_values(by="size", inplace=True)
        ax.plot(
            df_schur_equiv["equiv_neig"],
            df_schur_equiv["cost"],
            color=plot_color,
            marker="o",
            linestyle="--",
            linewidth=3.5,
            markersize=9,
            markeredgecolor=STYLE.ui_colors["marker_edge"],
            label=r"$t_{sub-schur}$",
        )
    # 红色实线框参数
    box_x_min, box_x_max = 0, 100
    box_y_min, box_y_max = 0, 30
    LIGHT_BLUE = STYLE.ui_colors["highlight"]
    rect_main = Rectangle(
        (box_x_min, box_y_min),
        box_x_max - box_x_min,
        box_y_max - box_y_min,
        facecolor="none",
        edgecolor=LIGHT_BLUE,
        linewidth=2,
        linestyle="-",
        zorder=10,
    )
    ax.add_patch(rect_main)
    # 主图设置
    # ax.set_xlabel('Number of Eigenmodes', fontsize=22, family='Times New Roman')
    # ax.set_ylabel('Time (s)', fontsize=22, family='Times New Roman')
    ax.tick_params(axis="x", labelsize=TICK_FONTSIZE)
    ax.tick_params(axis="y", labelsize=TICK_FONTSIZE)
    # 中文字体已由 plot_style_config 全局设置
    # 不在这里创建单独 legend，稍后统一合并
    ax.grid(False)  # Unified style: no grid
    ax.set_xlim(df_eig["neig_blk"].min(), df_eig["neig_blk"].max())
    ax.set_ylim(
        df_eig["sub_eig_cost_s"].min() * 0.8, df_eig["sub_eig_cost_s"].max() * 1.2
    )
    # 去掉主图标题
    ax.set_title("")
    # 设置主图y轴为科学计数法，x轴为普通数字
    ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=False))
    ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))
    # 设置科学计数法的10^n字体为Times New Roman
    ax.yaxis.offsetText.set_fontname("Times New Roman")
    ax.yaxis.offsetText.set_fontsize(TICK_FONTSIZE)

    # 右侧放大图
    # 只画 neig_blk <= 100 区域
    if segments_short:
        lc_short = LineCollection(
            segments_short, cmap=STYLE.get_sequential_cmap(), norm=norm
        )
        lc_short.set_array(np.array(colors_for_segments_short))
        lc_short.set_linewidth(4.5)
        ax_zoom.add_collection(lc_short)
    # schur 曲线
    if not df_schur_equiv.empty:
        df_schur_equiv_short = df_schur_equiv[df_schur_equiv["equiv_neig"] <= 100]
        ax_zoom.plot(
            df_schur_equiv_short["equiv_neig"],
            df_schur_equiv_short["cost"],
            color=plot_color,
            marker="o",
            linestyle="--",
            linewidth=3.5,
            markersize=9,
            markeredgecolor=STYLE.ui_colors["marker_edge"],
            label=r"$t_{sub-schur}$",
        )
    # 设置放大图坐标轴范围
    df_eig_short_all = df_eig[df_eig["neig_blk"] <= 100]
    if not df_eig_short_all.empty:
        max_y_inset = df_eig_short_all["sub_eig_cost_s"].max()
        min_y_inset = df_eig_short_all["sub_eig_cost_s"].min()
        if not df_schur_equiv.empty:
            df_schur_equiv_short = df_schur_equiv[df_schur_equiv["equiv_neig"] <= 100]
            if not df_schur_equiv_short.empty:
                max_y_inset = max(max_y_inset, df_schur_equiv_short["cost"].max())
                min_y_inset = min(min_y_inset, df_schur_equiv_short["cost"].min())
        ax_zoom.set_xlim(10, 100)
        ax_zoom.set_ylim(min_y_inset * 0.9, max_y_inset * 1.1)
    # 放大图不再绘制浅蓝色内部矩形，只保留浅蓝色外边框
    # 使用 ConnectionPatch 连接：主图浅蓝色矩形右上角 (数据坐标) -> 次图左侧中点 (Axes 归一化坐标)
    from matplotlib.patches import ConnectionPatch

    conn = ConnectionPatch(
        xyA=(box_x_max, box_y_max),
        coordsA=ax.transData,
        xyB=(0.0, 0.5),
        coordsB=ax_zoom.transAxes,
        color=LIGHT_BLUE,
        linewidth=2.2,
        linestyle="-",
    )
    fig.add_artist(conn)
    # 放大图设置
    # ax_zoom.set_xlabel('Number of Eigenmodes', fontsize=22, family='Times New Roman')
    # 不显示y轴标签
    ax_zoom.set_ylabel("")
    ax_zoom.tick_params(axis="x", labelsize=TICK_FONTSIZE)
    ax_zoom.tick_params(axis="y", labelsize=TICK_FONTSIZE)
    for label in ax_zoom.get_xticklabels() + ax_zoom.get_yticklabels():
        label.set_family("Times New Roman")
    ax_zoom.grid(False)  # Unified style: no grid
    # 去掉放大图标题
    ax_zoom.set_title("")
    ax_zoom.yaxis.set_tick_params(labelleft=True)
    # 设置放大图y轴为科学计数法，x轴为普通数字
    ax_zoom.xaxis.set_major_formatter(ScalarFormatter(useMathText=False))
    ax_zoom.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax_zoom.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))
    ax_zoom.yaxis.offsetText.set_fontname("Times New Roman")
    ax_zoom.yaxis.offsetText.set_fontsize(TICK_FONTSIZE)
    # 不在这里创建单独 legend，稍后统一合并

    # 统一x/y轴标签居中
    # fig.supxlabel('Number of Eigenmodes', fontsize=24, family='Times New Roman')

    # 调整子图间距和supxlabel位置
    # 增加左侧边距 (left 从 0.08 -> 0.12) 给共享 y 轴标签留更大空间，避免与 y 轴刻度或科学计数法偏移文本重叠
    plt.subplots_adjust(left=0.06, right=0.92, bottom=0.12, top=0.95, wspace=0.04)
    shared_ylabel = fig.supylabel(
        r"$t_\text{sub-eig} \ (s)$", fontsize=LABEL_FONTSIZE
    )
    # 适度左移共享 y 轴标签（默认在 x≈0.0 处），通过设置一个略微负的 x 使其离轴更远
    try:
        shared_ylabel.set_x(-0.01)
    except Exception:
        pass  # 兼容旧版本 matplotlib 若不支持 set_x
    fig.supxlabel(
        "特征模态数",
        fontsize=LABEL_FONTSIZE,
        y=0.00,
    )

    # ---------------- 统一图例设置 ----------------
    if legend_cfg is None:
        legend_cfg = {
            "pos": (0.72, -0.04),  # 左下角 (x,y) figure 坐标归一化到 [0,1]
            "width": 0.002,  # 传入宽度 (0-1 figure 相对单位)
            "height": 0.0001,  # 传入高度 (0-1 figure 相对单位)
            "fontsize": 22,
            "frame": False,
            "edgecolor": STYLE.ui_colors["spine"],
            "facecolor": STYLE.ui_colors["legend_bg"],
            "ncol": 1,  # 默认单列
            "title": None,  # 可选标题
        }

    handles_ax, labels_ax = ax.get_legend_handles_labels()
    handles_zoom, labels_zoom = ax_zoom.get_legend_handles_labels()
    combined = []
    seen = set()
    for h, l in list(zip(handles_ax, labels_ax)) + list(zip(handles_zoom, labels_zoom)):
        if l not in seen:
            combined.append((h, l))
            seen.add(l)
    handles = [h for h, _ in combined]
    labels = [l for _, l in combined]
    from matplotlib.font_manager import FontProperties

    shared_font = FontProperties(
        size=legend_cfg.get("fontsize", 32)
    )
    # 支持宽高：通过 bbox_transform + bbox_to_anchor 指定 legend 的下左角，并使用 bbox_to_anchor 的 (x,y,width,height)
    pos = legend_cfg.get("pos", (0.5, 0.5))
    width = legend_cfg.get("width", None)
    height = legend_cfg.get("height", None)
    if width is not None and height is not None:
        bbox_to_anchor = (pos[0], pos[1], width, height)
    else:
        bbox_to_anchor = pos  # 兼容旧用法
    legend = fig.legend(
        handles,
        labels,
        bbox_to_anchor=bbox_to_anchor,
        bbox_transform=fig.transFigure,
        prop=shared_font,
        frameon=legend_cfg.get("frame", True),
        ncol=legend_cfg.get("ncol", 1),
        title=legend_cfg.get("title", None),
        loc="lower left",
    )
    if legend_cfg.get("title"):
        legend.get_title().set_fontfamily("Times New Roman")
        legend.get_title().set_fontsize(legend_cfg.get("fontsize", 32))
    if legend_cfg.get("frame", True):
        frame = legend.get_frame()
        frame.set_edgecolor(legend_cfg.get("edgecolor", STYLE.ui_colors["spine"]))
        frame.set_facecolor(legend_cfg.get("facecolor", STYLE.ui_colors["legend_bg"]))
        frame.set_linewidth(1.5)

    plt.savefig(output_file_png, dpi=150)
    plt.savefig(output_file_pdf, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_file_png} and {output_file_pdf}")


def main():
    """Main execution function to run all analyses."""
    # try:
    #     #plt.style.use(PLT_STYLE)
    # except:
    #     print(f"Warning: Plot style '{PLT_STYLE}' not found. Using default.")

    df_eig, df_schur = load_and_prepare_data()

    if (
        df_eig is not None
        and df_schur is not None
        and not df_eig.empty
        and not df_schur.empty
    ):
        plot_equivalence_bar_chart(df_eig, df_schur)
        plot_timing_curves(df_eig, df_schur)
        print("\nAll plots generated successfully.")
    else:
        print("\nCould not generate plots. Please check input files and data ranges.")


if __name__ == "__main__":
    main()
