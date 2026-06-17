#!/usr/bin/env python3

import json
import os
import argparse
import re
import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style_config import get_style, apply_style, apply_spines

SCHEME = os.environ.get("PLOT_COLOR_SCHEME", "teal_coral")
STYLE = get_style(SCHEME)
apply_style(STYLE, scale="double_column")
# 中文显示名称映射 (用于 breakdown 图例和标签)
DISPLAY_NAME_MAP = {
    "Solve Eigenmodes": "求解特征模态",
    "Interface Modes (CMS)": "界面模态 (CMS)",
    "SE-free Modes (Ours)": "SE-free 模态 (本文方法)",
    "Matrix-Reducing (Ours)": "矩阵缩减 (本文方法)",
    "Preprocessing of SE-free Modes (Ours)": "SE-free 模态预处理 (本文方法)",
    "Postprocessing of SE-free Modes (Ours)": "SE-free 模态后处理 (本文方法)",
    "Preprocessing of Matrix-Reducing (Ours)": "矩阵缩减预处理 (本文方法)",
    "Postprocessing of Matrix-Reducing (Ours)": "矩阵缩减后处理 (本文方法)",
    "Solve Reduced Eigenmodes (Ours)": "求解降阶特征模态 (本文方法)",
    "Solve Reduced Eigenmodes (CMS)": "求解降阶特征模态 (CMS)",
    "Assemble Reduced Matrix (CMS)": "组装降阶矩阵 (CMS)",
}


TITLE_FONTSIZE = STYLE.scaled_fontsize("title", "double_column")
LABEL_FONTSIZE = STYLE.scaled_fontsize("label", "double_column")
LEGEND_FONTSIZE = STYLE.scaled_fontsize("legend", "double_column")
TICK_FONTSIZE = STYLE.scaled_fontsize("tick", "double_column")
LINE_WIDTH = STYLE.methods["ours"]["linewidth"]
MARKER_SIZE = STYLE.methods["ours"]["markersize"]

FIG_SIZE = (12, 6)
FIG_SIZE_COMBINED = (14, 8)
DPI = 300

OURS_COLOR = STYLE.ours
CMS_COLOR = STYLE.cms
OURS_SERIAL = STYLE.colors["serial"]
OURS_PARALLEL = STYLE.colors["parallel"]
CMS_SERIAL = STYLE.colors["serial_cms"]
CMS_PARALLEL = STYLE.colors["parallel_cms"]
CMS_ALPHA = STYLE.methods["cms"]["alpha"]

EFF_OURS_COLOR = STYLE.colors.get("efficiency_ours", "#CC3311")
EFF_CMS_COLOR = STYLE.colors.get("efficiency_cms", "#882255")

BASE_PURPLE = OURS_COLOR
BASE_YELLOW = CMS_COLOR

yscale = "linear"
# =========================================================================
# --- 2. 核心数据提取辅助函数 ---
# =========================================================================


def get_gt_reference_point(gt_data):
    """
    从 gt_data 列表中找到用作参考点（Baseline）的数据点。
    策略：找到 'nx' 最小的那个点。
    """
    if not gt_data:
        return None

    best_point = gt_data[0]
    min_nx = float("inf")

    for point in gt_data:
        run_key = point.get("run_key", "")
        # 尝试提取 nx
        match = re.search(r"nx(\d+)", run_key)
        if match:
            nx = int(match.group(1))
            if nx < min_nx:
                min_nx = nx
                best_point = point

    if min_nx != float("inf"):
        print(
            f"  (GT) Selected reference point with nx={min_nx} from {len(gt_data)} candidates."
        )
    else:
        print(f"  (GT) Warning: Could not parse 'nx' from run_keys. Using first point.")

    return best_point


def get_x_axis_and_indices(data_list):
    """
    提取 X 轴数据 (计算节点数) 并返回排序后的标签和索引。
    X 轴 = 该数据点中所有并行任务的 'num_tasks' 的最大值。
    """
    x_values = []
    if not data_list:  # 增加空值检查
        return [], []

    for data_point in data_list:
        max_tasks = 0
        if "steps" in data_point:
            for step in data_point["steps"].values():
                if step.get("type") == "parallel":
                    max_tasks = max(max_tasks, step["stats"].get("num_tasks", 0))
        # [修复] 如果没有并行任务 (例如 'gt' 数据)，尝试从 'serial' 任务获取
        if max_tasks == 0 and "steps" in data_point:
            for step in data_point["steps"].values():
                if step.get("type") == "serial":
                    # 这是一个 'gt' 风格的数据点，X轴应该来自'run_key'或一个固定值
                    # 但对于 'pd' 和 'sp'，它必须来自并行
                    # 如果真的没有并行任务，我们返回 0
                    pass
        x_values.append(max_tasks)

    # 获取排序索引
    sorted_indices = np.argsort(x_values)
    # 获取排序后的 x 轴标签
    sorted_x_labels = [x_values[i] for i in sorted_indices]

    # 返回排序后的X轴标签和用于排序Y值的索引
    return sorted_x_labels, sorted_indices


def get_stacked_bar_data(data_list, sorted_indices, type_filter):
    """
    为堆叠条形图提取 breakdown 数据。
    """
    plot_data = {}
    all_keys = set()

    if not data_list:  # 增加空值检查
        return {}

    # 第一次遍历：收集所有步骤名称
    for data_point in data_list:
        if "steps" in data_point:
            for step_name, step_data in data_point["steps"].items():
                if step_data.get("type") == type_filter:
                    all_keys.add(step_name)

    # 初始化 plot_data
    plot_data = {key: [] for key in all_keys}

    # 第二次遍历：填充Y值
    for data_point in data_list:
        # 确定Y值使用哪个键
        if type_filter == "parallel":
            y_key = "max_wall_time_s"
        else:  # 'serial'
            y_key = "wall_time_s"

        point_values = {}
        if "steps" in data_point:
            for step_name, step_data in data_point["steps"].items():
                if step_data.get("type") == type_filter:
                    point_values[step_name] = step_data["stats"].get(y_key, 0)

        # 附加值 (或0，如果该步骤不存在)
        for key in all_keys:
            plot_data[key].append(point_values.get(key, 0))

    # 第三步：使用传入的索引对所有数据进行排序
    sorted_plot_data = {}
    for key, values in plot_data.items():
        if not values:  # 增加检查
            continue
        sorted_plot_data[key] = [values[i] for i in sorted_indices]

    return sorted_plot_data


def get_line_data(data_list, sorted_indices, json_path):
    """
    为线图提取单个Y值。
    json_path 是一个键列表, e.g., ['summary_parallel', 'avg_load_balance_time']
    """
    y_values = []
    if not data_list:  # 增加空值检查
        return []

    for data_point in data_list:
        try:
            val = data_point
            for key in json_path:
                val = val[key]
            y_values.append(val)
        except KeyError:
            y_values.append(np.nan)  # 如果键不存在，添加 nan

    # 使用传入的索引对Y值进行排序
    sorted_y_values = [y_values[i] for i in sorted_indices]
    return sorted_y_values


# =========================================================================
# --- 3. 核心绘图函数 (*** 已修改 ***) ---
# =========================================================================


def plot_stacked_bar_comparison(
    pd_plot_data,
    sp_plot_data,
    x_labels,
    title,
    ylabel,
    output_path,
    yscale=yscale,
    pd_efficiency=None,  # 新增: pd efficiency 数据
    sp_efficiency=None,  # 新增: sp efficiency 数据
):
    """
    绘制堆叠条形图的核心函数，具有分离的图例和自动颜色。
    支持双纵轴：左侧为时间，右侧为 efficiency。
    """
    print(f"  ... 正在生成: {os.path.basename(output_path)}")
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    width = 0.4

    num_x_points = len(x_labels)
    x_ticks = np.arange(num_x_points)

    # --- 1. 自动颜色映射 (基于所有唯一的键) ---
    sp_labels = sorted(list(sp_plot_data.keys()))
    pd_labels = sorted(list(pd_plot_data.keys()))
    all_unique_labels = sorted(list(set(sp_labels + pd_labels)))

    colors = {}
    if all_unique_labels:
        # 使用 'viridis' colormap
        color_values = STYLE.get_sequential_cmap()(
            np.linspace(0, 1, len(all_unique_labels))
        )
        colors = {label: color for label, color in zip(all_unique_labels, color_values)}
    else:
        print(f"警告: 在 {title} 中未找到数据标签")

    # --- 2. 绘制 "cms" (SP) - 左侧条形图 ---
    bottom = np.zeros(num_x_points)
    sp_bars = []
    for label in sp_labels:
        data = np.array(sp_plot_data.get(label, [0] * num_x_points))
        bar = ax.bar(
            x_ticks - width / 2.0,
            data,
            width,
            bottom=bottom,
            label=DISPLAY_NAME_MAP.get(label, label),
            color=colors.get(label, STYLE.ui_colors["reference_line"]),
        )
        sp_bars.append(bar)
        bottom += data

    # --- 3. 绘制 "ours" (PD) - 右侧条形图 ---
    bottom = np.zeros(num_x_points)
    pd_bars = []
    for label in pd_labels:
        data = np.array(pd_plot_data.get(label, [0] * num_x_points))
        bar = ax.bar(
            x_ticks + width / 2.0,
            data,
            width,
            bottom=bottom,
            label=DISPLAY_NAME_MAP.get(label, label),
            color=colors.get(label, STYLE.ui_colors["reference_line"]),
        )
        pd_bars.append(bar)
        bottom += data

    # --- 4. 绘制 Efficiency 曲线 (双纵轴) ---
    ax2 = None
    efficiency_handles = []
    if pd_efficiency is not None and sp_efficiency is not None:
        ax2 = ax.twinx()  # 创建共享 X 轴的第二个 Y 轴

        # 定义 efficiency 曲线的颜色
        pd_eff_color = STYLE.efficiency_colors["ours"]
        sp_eff_color = STYLE.efficiency_colors["cms"]

        # 绘制 pd efficiency
        ax2.plot(
            x_ticks,
            pd_efficiency,
            color=pd_eff_color,
            marker="o",
            linestyle="-",
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE * 0.8,
            label="本文方法 效率",
            zorder=10,
        )

        # 绘制 sp efficiency
        ax2.plot(
            x_ticks,
            sp_efficiency,
            color=sp_eff_color,
            marker="o",
            linestyle="--",
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE * 0.8,
            label="CB-CMS 效率",
            zorder=10,
        )

        # 设置右侧 Y 轴
        ax2.set_ylabel("效率", fontsize=LABEL_FONTSIZE)
        ax2.set_yscale("log")
        ax2.tick_params(axis="y", which="major", labelsize=TICK_FONTSIZE)

        all_eff_values = [v for v in pd_efficiency + sp_efficiency if v > 0]
        if all_eff_values:
            eff_min, eff_max = min(all_eff_values), max(all_eff_values)
            import math

            log_min = math.floor(math.log10(eff_min * 0.8))
            log_max = math.ceil(math.log10(eff_max * 1.2))
            ylim_min = max(10**log_min, 0.001)
            ylim_max = min(10**log_max, 10.0)
            ax2.set_ylim(ylim_min, ylim_max)
        else:
            ax2.set_ylim(0.01, 2.0)

        # 创建 efficiency 图例句柄
        efficiency_handles = [
            Line2D(
                [0],
                [0],
                color=pd_eff_color,
                lw=LINE_WIDTH,
                marker="o",
                linestyle="-",
                label="本文方法效率",
            ),
            Line2D(
                [0],
                [0],
                color=sp_eff_color,
                lw=LINE_WIDTH,
                marker="o",
                linestyle="-",
                label="CB-CMS效率",
            ),
        ]

    # --- 5. 添加分离的图例 ---
    sp_legend_handles = list(sp_bars)
    sp_legend_title = "CB-CMS"

    if sp_legend_handles:
        sp_legend = ax.legend(
            handles=sp_legend_handles,
            loc="upper left",
            title=sp_legend_title,
            fontsize=LEGEND_FONTSIZE,
        )
        sp_legend.get_title().set_fontsize(LEGEND_FONTSIZE)
        ax.add_artist(sp_legend)

    # pd 图例 + efficiency 图例
    pd_legend_handles = list(pd_bars) + efficiency_handles
    if pd_legend_handles:
        pd_legend = ax.legend(
            handles=pd_legend_handles,
            loc="upper right",
            title="本文方法" if not efficiency_handles else "本文方法 & 效率",
            fontsize=LEGEND_FONTSIZE,
        )
        pd_legend.get_title().set_fontsize(LEGEND_FONTSIZE)

    # --- 6. 格式化图表 (使用全局字体大小) ---
    ax.set_title(title, fontsize=TITLE_FONTSIZE, pad=20)
    ax.set_xlabel("计算节点数", fontsize=LABEL_FONTSIZE)
    ax.set_ylabel(ylabel, fontsize=LABEL_FONTSIZE)
    ax.set_yscale(yscale)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, fontsize=TICK_FONTSIZE)
    ax.tick_params(axis="y", which="major", labelsize=TICK_FONTSIZE)
    ax.grid(False)

    if yscale == "log":
        ylim = ax.get_ylim()
        if ylim[0] > 0 and ylim[1] > 0:  # 防止 log(0) 错误
            ax.set_ylim(ylim[0], ylim[1] * 10)
    else:
        ylim = ax.get_ylim()
        ax.set_ylim(ylim[0], ylim[1] * 1.2)

    fig.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches="tight")
    plt.close(fig)


def plot_line_comparison(
    pd_lines,
    sp_lines,
    gt_lines,  # <-- 新增: 'gt' 线条数据
    x_labels,
    title,
    ylabel,
    output_path,
    yscale=yscale,
):
    """
    绘制线图的核心函数，具有两个分离的图例（按方法和按指标）。
    *** [修复] 修复了 'x_ticks' is not defined 错误 ***
    """
    print(f"  ... 正在生成: {os.path.basename(output_path)}")
    fig, ax = plt.subplots(figsize=FIG_SIZE)

    # --- [修复] ---
    # 定义 x_ticks，使其与 plot_stacked_bar_comparison 保持一致
    num_x_points = len(x_labels)
    x_ticks = np.arange(num_x_points)
    # --- [修复结束] ---

    # --- 1. 定义颜色和样式 ---
    pd_color = STYLE.ours
    sp_color = STYLE.cms
    gt_color = STYLE.method_colors["spectra"]  # <-- 'gt' 颜色

    metric_handles = []
    seen_metric_labels = set()

    # --- 2. 绘制 "ours" (PD) 线条 ---
    for metric_name, (y_vals, marker, linestyle) in pd_lines.items():
        if len(y_vals) != num_x_points:  # 安全检查
            print(
                f"  警告 (PD): {metric_name} Y数据点 ({len(y_vals)}) 与 X轴 ({num_x_points}) 不匹配。跳过。"
            )
            continue
        ax.plot(
            x_ticks,
            y_vals,  # <-- [修复] 使用 x_ticks
            color=pd_color,
            marker=marker,
            linestyle=linestyle,
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE,
            label=f"ours - {metric_name}",
        )

        if metric_name not in seen_metric_labels:
            metric_handles.append(
                Line2D(
                    [0],
                    [0],
                    color=STYLE.ui_colors["spine"],
                    marker=marker,
                    linestyle=linestyle,
                    label=metric_name,
                    markersize=MARKER_SIZE,
                    linewidth=LINE_WIDTH,
                )
            )
            seen_metric_labels.add(metric_name)

    # --- 3. 绘制 "cms" (SP) 线条 ---
    for metric_name, (y_vals, marker, linestyle) in sp_lines.items():
        if len(y_vals) != num_x_points:  # 安全检查
            print(
                f"  警告 (SP): {metric_name} Y数据点 ({len(y_vals)}) 与 X轴 ({num_x_points}) 不匹配。跳过。"
            )
            continue
        ax.plot(
            x_ticks,
            y_vals,  # <-- [修复] 使用 x_ticks
            color=sp_color,
            marker=marker,
            linestyle=linestyle,
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE,
            label=f"cms - {metric_name}",
        )

    # --- 4. [新增] 绘制 "gt" (Global) 线条 ---
    for metric_name, (y_vals, marker, linestyle) in gt_lines.items():
        if len(y_vals) != num_x_points:  # 安全检查
            print(
                f"  警告 (GT): {metric_name} Y数据点 ({len(y_vals)}) 与 X轴 ({num_x_points}) 不匹配。跳过。"
            )
            continue
        ax.plot(
            x_ticks,
            y_vals,  # <-- [修复] 使用 x_ticks
            color=gt_color,
            marker=marker,
            linestyle=linestyle,
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE,
            label=f"gt - {metric_name}",
        )

        if metric_name not in seen_metric_labels:
            metric_handles.append(
                Line2D(
                    [0],
                    [0],
                    color=STYLE.ui_colors["spine"],
                    marker=marker,
                    linestyle=linestyle,
                    label=metric_name,
                    markersize=MARKER_SIZE,
                    linewidth=LINE_WIDTH,
                )
            )
            seen_metric_labels.add(metric_name)

    # --- 5. 添加两个图例 ---
    method_handles = [
        Line2D([0], [0], color=pd_color, lw=LINE_WIDTH, label="本文方法"),
        Line2D([0], [0], color=sp_color, lw=LINE_WIDTH, label="CB-CMS"),
    ]
    if gt_lines:  # <-- 新增: 仅当 gt 数据存在时才添加图例
        method_handles.append(
            Line2D([0], [0], color=gt_color, lw=LINE_WIDTH, label="Spectra")
        )

    method_legend = ax.legend(
        handles=method_handles,
        loc="upper left",
        title="方法",
        fontsize=LEGEND_FONTSIZE,
    )
    method_legend.get_title().set_fontsize(LEGEND_FONTSIZE)
    ax.add_artist(method_legend)

    if metric_handles and len(metric_handles) > 1:
        metric_legend = ax.legend(
            handles=metric_handles,
            loc="upper right",
            title="指标",
            fontsize=LEGEND_FONTSIZE,
        )
        metric_legend.get_title().set_fontsize(LEGEND_FONTSIZE)
        ax.add_artist(metric_legend)

    # --- 6. 格式化图表 (使用全局字体大小) ---
    ax.set_title(title, fontsize=TITLE_FONTSIZE, pad=20)
    ax.set_xlabel("计算节点数", fontsize=LABEL_FONTSIZE)
    ax.set_ylabel(ylabel, fontsize=LABEL_FONTSIZE)
    ax.set_yscale(yscale)

    # 确保 X 轴标签显示正确 (特别是对于数值标签)
    ax.set_xticks(x_ticks)  # <-- [修复] 此处现在可以正常工作
    ax.set_xticklabels(x_labels, fontsize=TICK_FONTSIZE)

    ax.tick_params(axis="y", which="major", labelsize=TICK_FONTSIZE)
    ax.grid(False)

    if yscale == "log":
        ylim = ax.get_ylim()
        if ylim[0] > 0 and ylim[1] > 0:  # 防止 log(0) 错误
            ax.set_ylim(ylim[0], ylim[1] * 10)
    else:
        ylim = ax.get_ylim()
        min_y = 0 if ylim[0] > -0.1 else ylim[0]
        max_y = 1.1 if ylim[1] < 1.0 else ylim[1] * 1.2
        ax.set_ylim(min_y, max_y)

    fig.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches="tight")
    plt.close(fig)


def plot_combined_pie_all(
    pd_para, sp_para, pd_seri, sp_seri, x_labels, title, output_path
):
    """
    绘制 breakdown 的组合饼图 (4行 x N列)，每行图例放在该行下方。
    """
    print(f"  ... 正在生成组合饼图: {os.path.basename(output_path)}")

    max_pies = 3
    x_labels = x_labels[:max_pies]
    num_cols = len(x_labels)
    if num_cols == 0:
        return

    from matplotlib.patches import Patch
    import matplotlib.patheffects as path_effects

    fig = plt.figure(figsize=(num_cols * 5.0, 24))
    gs = fig.add_gridspec(
        8,
        num_cols,
        height_ratios=[5, 1.2, 5, 1.2, 5, 1.2, 5, 1.2],
        hspace=0.02,
        wspace=0.05,
    )

    colors = STYLE.breakdown_colors

    row_configs = [
        (pd_para, "本文方法 并行"),
        (sp_para, "CB-CMS 并行"),
        (pd_seri, "本文方法 串行"),
        (sp_seri, "CB-CMS 串行"),
    ]

    for row_idx, (data, row_title) in enumerate(row_configs):
        pie_row = row_idx * 2
        legend_row = pie_row + 1
        row_labels_used = set()

        for col_idx in range(num_cols):
            ax = fig.add_subplot(gs[pie_row, col_idx])

            if col_idx == 0:
                ax.set_ylabel(
                    row_title, fontsize=16, rotation=90, labelpad=30, weight="bold"
                )

            if row_idx == 0:
                ax.set_title(f"节点: {x_labels[col_idx]}", fontsize=16, weight="bold")

            sizes, labels, pie_colors = [], [], []

            for key in sorted(data.keys()):
                vals = data[key]
                if col_idx < len(vals) and vals[col_idx] > 0:
                    sizes.append(vals[col_idx])
                    labels.append(DISPLAY_NAME_MAP.get(key, key))
                    pie_colors.append(
                        colors.get(key, STYLE.ui_colors["reference_line"])
                    )
                    row_labels_used.add(key)

            if sizes:
                wedges, texts, autotexts = ax.pie(
                    sizes,
                    autopct=lambda pct: "{:.1f}%".format(pct) if pct > 5 else "",
                    colors=pie_colors,
                    startangle=90,
                    textprops={
                        "fontsize": 14,
                        "color": STYLE.ui_colors["marker_edge"],
                        "weight": "bold",
                    },
                )
                for autotext in autotexts:
                    autotext.set_path_effects(
                        [
                            path_effects.withStroke(
                                linewidth=2, foreground=STYLE.ui_colors["spine"]
                            )
                        ]
                    )

        legend_ax = fig.add_subplot(gs[legend_row, :])
        legend_ax.axis("off")

        if row_labels_used:
            sorted_row_labels = sorted(list(row_labels_used))
            print(f"    [DEBUG] {row_title} legend labels: {sorted_row_labels}")
            legend_handles = [
                Patch(color=colors[l], label=DISPLAY_NAME_MAP.get(l, l)) for l in sorted_row_labels
            ]
            legend_ncol = 2
            legend_ax.legend(
                handles=legend_handles,
                loc="center",
                ncol=legend_ncol,
                fontsize=20,
                frameon=False,
            )

    plt.suptitle(title, fontsize=TITLE_FONTSIZE, y=0.98)
    fig.savefig(output_path, dpi=DPI, bbox_inches="tight")
    plt.close(fig)


# =========================================================================
# --- 4. 键替换函数 (无修改) ---
# =========================================================================


def parse_replacement_file(filename):
    """
    解析替换文件 (old_key,new_key)。
    返回一个 (old_prefix, new_prefix) 元组的列表。
    """
    replacements = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):  # 忽略空行和注释
                    continue
                parts = line.split(",")
                if len(parts) == 2:
                    old_key = parts[0].strip()
                    new_key = parts[1].strip()
                    if old_key and new_key:
                        replacements.append((old_key, new_key))
        print(f"成功加载 {len(replacements)} 条替换规则 (来自 {filename})")
        print(replacements)
    except FileNotFoundError:
        print(f"警告: 替换文件未找到: {filename}")
    except Exception as e:
        print(f"加载替换文件时出错: {e}")
    return replacements


def apply_key_replacements(data_dict, replacement_map):
    """
    遍历数据并根据映射替换 'steps' 字典中的键。
    使用前缀匹配 (e.g., 'alfim' -> 'ALFIM' 会匹配 'alfim_compute')。
    """
    print("正在应用步骤名称替换...")
    if not replacement_map:
        return data_dict

    # 按键长度降序排序，以优先匹配更长的键
    # e.g., 匹配 'alfim_compute' 优先于 'alfim'
    sorted_map = sorted(replacement_map, key=lambda x: len(x[0]), reverse=True)

    for scaling_type, data_list in data_dict.items():
        if not isinstance(data_list, list):
            continue

        for data_point in data_list:
            if not isinstance(data_point, dict) or "steps" not in data_point:
                continue

            original_steps = data_point.get("steps", {})
            new_steps = {}

            for old_step_name, step_data in original_steps.items():
                new_step_name = old_step_name
                # 查找第一个匹配的前缀并应用它
                for old_prefix, new_prefix in sorted_map:
                    if new_step_name.startswith(old_prefix):
                        # 仅替换第一次出现 (前缀)
                        new_step_name = new_step_name.replace(old_prefix, new_prefix, 1)
                        break  # 应用第一个（最长的）匹配后即停止

                new_steps[new_step_name] = step_data

            data_point["steps"] = new_steps

    print("替换完成。")
    return data_dict


# =========================================================================
# --- 5. 主调度函数 (*** 已修改 ***) ---
# =========================================================================


def generate_all_plots_for_scaling_type(pd_data, sp_data, gt_data, scaling_prefix):
    """
    为给定的扩展类型 (weak 或 strong) 生成所有 5 张图。
    *** [修复] 增加 X 轴交集逻辑 (intersection) ***
    """
    print(f"\n--- 真正为 '{scaling_prefix}' 生成所有图表 ---")

    output_dir = f"{scaling_prefix}_plots"
    os.makedirs(output_dir, exist_ok=True)
    print(f"图表将保存到: {output_dir}/")

    # --- 1. 提取 X 轴并验证 (pd 和 sp) ---
    try:
        # X 轴由 pd 和 sp 驱动
        pd_x_labels_raw, pd_indices_raw = get_x_axis_and_indices(pd_data)
        sp_x_labels_raw, sp_indices_raw = get_x_axis_and_indices(sp_data)

        # --- [修复] 查找 X 轴的交集 ---
        if pd_x_labels_raw == sp_x_labels_raw:
            # 快乐路径：X 轴完全匹配
            x_labels = pd_x_labels_raw
            pd_data_final = [pd_data[i] for i in pd_indices_raw]
            sp_data_final = [sp_data[i] for i in sp_indices_raw]
            # 新的索引很简单，因为数据已经排序
            pd_indices_final = np.arange(len(pd_data_final))
            sp_indices_final = np.arange(len(sp_data_final))
            print(f"  X 轴匹配: {x_labels}")
        else:
            # 不匹配路径：(例如 Strong Scaling)
            print(f"警告: {scaling_prefix} 的 X 轴标签不匹配。")
            print(f"  PD 节点: {pd_x_labels_raw}")
            print(f"  SP 节点: {sp_x_labels_raw}")

            # 1. 找到交集
            x_labels = sorted(list(set(pd_x_labels_raw) & set(sp_x_labels_raw)))
            if not x_labels:
                print("错误：PD 和 SP 之间没有共同的 X 轴点。跳过。")
                return

            print(f"  将使用交集: {x_labels}")

            # 2. 过滤数据
            pd_data_sorted = [pd_data[i] for i in pd_indices_raw]
            sp_data_sorted = [sp_data[i] for i in sp_indices_raw]

            pd_data_final = [
                d for d, x in zip(pd_data_sorted, pd_x_labels_raw) if x in x_labels
            ]
            sp_data_final = [
                d for d, x in zip(sp_data_sorted, sp_x_labels_raw) if x in x_labels
            ]

            # 3. 新的索引很简单
            pd_indices_final = np.arange(len(pd_data_final))
            sp_indices_final = np.arange(len(sp_data_final))

        if not x_labels:
            print("错误：未找到 X 轴数据。跳过此扩展类型。")
            return

        num_x_points = len(x_labels)

    except Exception as e:
        print(f"提取 X 轴时出错: {e}")
        return

    # --- 2. 提取 'gt' 基准数据 (用于图 3, 4, 5 的 node=1 数据点) ---
    # Strong Scaling 和 Weak Scaling 都使用 gt 的第一个数据点作为 node=1

    is_strong_scaling = scaling_prefix == "strong_scaling"
    gt_node1_time = None
    gt_node1_memory = None
    gt_node1_balance_time = None
    gt_node1_balance_memory = None

    if gt_data and len(gt_data) > 0:
        try:
            gt_point = get_gt_reference_point(gt_data)
            if gt_point:
                gt_node1_time = gt_point["summary_serial"]["total_wall_time_s"]
                gt_node1_memory = gt_point["summary_serial"]["max_peak_memory_gb"]
                # 对于 node=1，没有并行任务，balance 设为 1.0 (完美均衡)
                gt_node1_balance_time = 1.0
                gt_node1_balance_memory = 1.0
                print(
                    f"  (GT) 提取 node=1 数据: Time={gt_node1_time}s, Mem={gt_node1_memory}GB"
                )
        except Exception as e:
            print(f"提取 'gt' 数据时出错: {e}")

    # --- [修复] 所有绘图调用现在使用过滤后的数据和索引 ---

    # --- 绘图 1: 并行时间 Breakdown (Stacked Bar) ---
    try:
        pd_plot_data = get_stacked_bar_data(pd_data_final, pd_indices_final, "parallel")
        sp_plot_data = get_stacked_bar_data(sp_data_final, sp_indices_final, "parallel")
        plot_stacked_bar_comparison(
            pd_plot_data,
            sp_plot_data,
            x_labels,
            title=f"{scaling_prefix.title()} - Parallel Time Breakdown",
            ylabel="时间 (s) (对数刻度)",
            output_path=os.path.join(
                output_dir, f"1_{scaling_prefix}_time_parallel_breakdown.png"
            ),
            yscale=yscale,
        )
    except Exception as e:
        print(f"绘制 'Parallel Time Breakdown' 时失败: {e}")

    # --- 绘图 2: 串行时间 Breakdown (Stacked Bar) ---
    try:
        pd_plot_data = get_stacked_bar_data(pd_data_final, pd_indices_final, "serial")
        sp_plot_data = get_stacked_bar_data(sp_data_final, sp_indices_final, "serial")
        plot_stacked_bar_comparison(
            pd_plot_data,
            sp_plot_data,
            x_labels,
            title=f"{scaling_prefix.title()} - Serial Time Breakdown",
            ylabel="时间 (s) (对数刻度)",
            output_path=os.path.join(
                output_dir, f"2_{scaling_prefix}_time_serial_breakdown.png"
            ),
            yscale=yscale,
        )
    except Exception as e:
        print(f"绘制 'Serial Time Breakdown' 时失败: {e}")

    # Call Combined Pie Chart (Parallel + Serial, All Nodes)
    try:
        pd_para = get_stacked_bar_data(pd_data_final, pd_indices_final, "parallel")
        sp_para = get_stacked_bar_data(sp_data_final, sp_indices_final, "parallel")
        pd_seri = get_stacked_bar_data(pd_data_final, pd_indices_final, "serial")
        sp_seri = get_stacked_bar_data(sp_data_final, sp_indices_final, "serial")

        plot_combined_pie_all(
            pd_para,
            sp_para,
            pd_seri,
            sp_seri,
            x_labels,
            ("强扩展 - 时间代价详细分解 (全部节点)" if scaling_prefix == "strong_scaling" else "弱扩展 - 时间代价详细分解 (全部节点)"),
            os.path.join(output_dir, f"6_{scaling_prefix}_combined_pie_breakdown.png"),
        )
    except Exception as e:
        print(f"绘制 'Combined Pie Breakdown' 时失败: {e}")

    # --- 绘图 3: 总体时间 Breakdown (Stacked Bar) ---
    try:
        pd_serial_y = get_line_data(
            pd_data_final, pd_indices_final, ["summary_serial", "total_wall_time_s"]
        )
        pd_parallel_y = get_line_data(
            pd_data_final,
            pd_indices_final,
            ["summary_parallel", "total_bottleneck_wall_time_s"],
        )
        sp_serial_y = get_line_data(
            sp_data_final, sp_indices_final, ["summary_serial", "total_wall_time_s"]
        )
        sp_parallel_y = get_line_data(
            sp_data_final,
            sp_indices_final,
            ["summary_parallel", "total_bottleneck_wall_time_s"],
        )

        # Strong Scaling 和 Weak Scaling: 在前面添加 node=1 的数据点
        if gt_node1_time is not None:
            # node=1 时，只有 serial time，parallel time 为 0
            pd_serial_y = [gt_node1_time] + pd_serial_y
            pd_parallel_y = [0.0] + pd_parallel_y
            sp_serial_y = [gt_node1_time] + sp_serial_y
            sp_parallel_y = [0.0] + sp_parallel_y
            x_labels_plot3 = [1] + list(x_labels)
        else:
            x_labels_plot3 = x_labels

        pd_plot_data = {"Serial Time": pd_serial_y, "Parallel Time": pd_parallel_y}
        sp_plot_data = {"Serial Time": sp_serial_y, "Parallel Time": sp_parallel_y}

        # 计算 Efficiency
        pd_total_time = [s + p for s, p in zip(pd_serial_y, pd_parallel_y)]
        sp_total_time = [s + p for s, p in zip(sp_serial_y, sp_parallel_y)]

        pd_efficiency = []
        sp_efficiency = []

        if gt_node1_time is not None:
            for i, n in enumerate(x_labels_plot3):
                if is_strong_scaling:
                    # Strong Scaling: Efficiency = T_1 / (N * T_N)
                    pd_eff = (
                        gt_node1_time / (n * pd_total_time[i])
                        if pd_total_time[i] > 0
                        else 0
                    )
                    sp_eff = (
                        gt_node1_time / (n * sp_total_time[i])
                        if sp_total_time[i] > 0
                        else 0
                    )
                else:
                    # Weak Scaling: Efficiency = T_1 / T_N
                    pd_eff = (
                        gt_node1_time / pd_total_time[i] if pd_total_time[i] > 0 else 0
                    )
                    sp_eff = (
                        gt_node1_time / sp_total_time[i] if sp_total_time[i] > 0 else 0
                    )
                pd_efficiency.append(pd_eff)
                sp_efficiency.append(sp_eff)
        else:
            pd_efficiency = None
            sp_efficiency = None

        plot_stacked_bar_comparison(
            pd_plot_data,
            sp_plot_data,
            x_labels_plot3,
            title=f"{scaling_prefix.title()} - Total Time (Serial vs Parallel)",
            ylabel="时间 (s)",
            output_path=os.path.join(
                output_dir, f"3_{scaling_prefix}_time_total_breakdown.png"
            ),
            yscale=yscale,
            pd_efficiency=pd_efficiency,
            sp_efficiency=sp_efficiency,
        )
    except Exception as e:
        print(f"绘制 'Total Time Breakdown' 时失败: {e}")

    # --- 绘图 4: 均衡性对比 (时间 vs 内存) (Line) ---
    try:
        pd_time_y = get_line_data(
            pd_data_final,
            pd_indices_final,
            ["summary_parallel", "avg_load_balance_time"],
        )
        pd_mem_y = get_line_data(
            pd_data_final,
            pd_indices_final,
            ["summary_parallel", "avg_load_balance_memory"],
        )
        sp_time_y = get_line_data(
            sp_data_final,
            sp_indices_final,
            ["summary_parallel", "avg_load_balance_time"],
        )
        sp_mem_y = get_line_data(
            sp_data_final,
            sp_indices_final,
            ["summary_parallel", "avg_load_balance_memory"],
        )

        # Strong Scaling 和 Weak Scaling: 在前面添加 node=1 的数据点 (balance = 1.0)
        if gt_node1_balance_time is not None:
            pd_time_y = [gt_node1_balance_time] + pd_time_y
            pd_mem_y = [gt_node1_balance_memory] + pd_mem_y
            sp_time_y = [gt_node1_balance_time] + sp_time_y
            sp_mem_y = [gt_node1_balance_memory] + sp_mem_y
            x_labels_plot4 = [1] + list(x_labels)
        else:
            x_labels_plot4 = x_labels

        metric_styles = {"Time Balance": ("o", "-"), "Memory Balance": ("s", "--")}
        pd_lines = {
            "Time Balance": (pd_time_y, *metric_styles["Time Balance"]),
            "Memory Balance": (pd_mem_y, *metric_styles["Memory Balance"]),
        }
        sp_lines = {
            "Time Balance": (sp_time_y, *metric_styles["Time Balance"]),
            "Memory Balance": (sp_mem_y, *metric_styles["Memory Balance"]),
        }
        plot_line_comparison(
            pd_lines,
            sp_lines,
            {},
            x_labels_plot4,
            title=f"{scaling_prefix.title()} - Balance Comparison (Time vs Memory)",
            ylabel="均衡比",
            output_path=os.path.join(
                output_dir, f"4_{scaling_prefix}_balance_comparison.png"
            ),
            yscale="linear",
        )
    except Exception as e:
        print(f"绘制 'Balance Comparison' 时失败: {e}")

    # --- 绘图 5: 峰值内存 (串/并) (Line) ---
    try:
        pd_serial_y = get_line_data(
            pd_data_final, pd_indices_final, ["summary_serial", "max_peak_memory_gb"]
        )
        pd_parallel_y = get_line_data(
            pd_data_final, pd_indices_final, ["summary_parallel", "max_peak_memory_gb"]
        )
        sp_serial_y = get_line_data(
            sp_data_final, sp_indices_final, ["summary_serial", "max_peak_memory_gb"]
        )
        sp_parallel_y = get_line_data(
            sp_data_final, sp_indices_final, ["summary_parallel", "max_peak_memory_gb"]
        )

        # Strong Scaling 和 Weak Scaling: 在前面添加 node=1 的数据点
        if gt_node1_memory is not None:
            # node=1 时，只有 serial memory，parallel memory 为 0
            pd_serial_y = [gt_node1_memory] + pd_serial_y
            pd_parallel_y = [0.0] + pd_parallel_y
            sp_serial_y = [gt_node1_memory] + sp_serial_y
            sp_parallel_y = [0.0] + sp_parallel_y
            x_labels_plot5 = [1] + list(x_labels)
        else:
            x_labels_plot5 = x_labels

        metric_styles = {"串行": ("s", "--"), "并行": ("^", ":")}
        pd_lines = {
            "串行": (pd_serial_y, *metric_styles["串行"]),
            "并行": (pd_parallel_y, *metric_styles["并行"]),
        }
        sp_lines = {
            "串行": (sp_serial_y, *metric_styles["串行"]),
            "并行": (sp_parallel_y, *metric_styles["并行"]),
        }

        # 不再使用 gt_lines，因为 gt 已融入 pd/sp 数据
        plot_line_comparison(
            pd_lines,
            sp_lines,
            {},
            x_labels_plot5,
            title=f"{scaling_prefix.title()} - Peak Memory (Serial vs Parallel)",
            ylabel="峰值内存 (GB)",
            output_path=os.path.join(
                output_dir, f"5_{scaling_prefix}_memory_peak_comparison.png"
            ),
            yscale=yscale,
        )
    except Exception as e:
        print(f"绘制 'Peak Memory' 时失败: {e}")


# =========================================================================
# --- 6. 合并图函数 (Strong + Weak) ---
# =========================================================================


def save_both(fig, path):
    fig.savefig(path, dpi=DPI, bbox_inches="tight")
    if path.lower().endswith(".png"):
        fig.savefig(path[:-4] + ".pdf", dpi=DPI, bbox_inches="tight")
    plt.close(fig)


def generate_combined_strong_weak_total(
    pd_strong, sp_strong, pd_weak, sp_weak, gt_strong, gt_weak, output_dir
):
    import math
    from matplotlib.colors import to_rgba
    from matplotlib.patches import Patch

    os.makedirs(output_dir, exist_ok=True)
    print(f"组合图表将保存到: {output_dir}/")

    def filter_by_intersection(pd_data, sp_data):
        pd_x, pd_idx = get_x_axis_and_indices(pd_data)
        sp_x, sp_idx = get_x_axis_and_indices(sp_data)
        if pd_x != sp_x:
            common = sorted(list(set(pd_x) & set(sp_x)))
            if not common:
                return pd_x, pd_idx, sp_idx, pd_data, sp_data
            pd_sorted = [pd_data[i] for i in pd_idx]
            sp_sorted = [sp_data[i] for i in sp_idx]
            pd_filtered = [d for d, x in zip(pd_sorted, pd_x) if x in common]
            sp_filtered = [d for d, x in zip(sp_sorted, sp_x) if x in common]
            return (
                common,
                np.arange(len(pd_filtered)),
                np.arange(len(sp_filtered)),
                pd_filtered,
                sp_filtered,
            )
        return pd_x, pd_idx, sp_idx, pd_data, sp_data

    x_strong, pd_idx_s, sp_idx_s, pd_s_data, sp_s_data = filter_by_intersection(
        pd_strong, sp_strong
    )
    x_weak, pd_idx_w, sp_idx_w, pd_w_data, sp_w_data = filter_by_intersection(
        pd_weak, sp_weak
    )

    if not x_strong or not x_weak:
        print("错误：未找到X轴数据。")
        return

    gt_node1_time_strong = None
    gt_node1_time_weak = None
    if gt_strong and len(gt_strong) > 0:
        try:
            gt_point = get_gt_reference_point(gt_strong)
            if gt_point:
                gt_node1_time_strong = gt_point["summary_serial"]["total_wall_time_s"]
        except Exception as e:
            print(f"提取 GT Strong 数据时出错: {e}")
    if gt_weak and len(gt_weak) > 0:
        try:
            gt_point = get_gt_reference_point(gt_weak)
            if gt_point:
                gt_node1_time_weak = gt_point["summary_serial"]["total_wall_time_s"]
        except Exception as e:
            print(f"提取 GT Weak 数据时出错: {e}")

    def get_total_data(pd_data, sp_data, pd_idx, sp_idx, gt_node1_time):
        pd_serial = get_line_data(
            pd_data, pd_idx, ["summary_serial", "total_wall_time_s"]
        )
        pd_parallel = get_line_data(
            pd_data, pd_idx, ["summary_parallel", "total_bottleneck_wall_time_s"]
        )
        sp_serial = get_line_data(
            sp_data, sp_idx, ["summary_serial", "total_wall_time_s"]
        )
        sp_parallel = get_line_data(
            sp_data, sp_idx, ["summary_parallel", "total_bottleneck_wall_time_s"]
        )
        if gt_node1_time is not None:
            pd_serial = [gt_node1_time] + pd_serial
            pd_parallel = [0.0] + pd_parallel
            sp_serial = [gt_node1_time] + sp_serial
            sp_parallel = [0.0] + sp_parallel
        return {"串行": pd_serial, "并行": pd_parallel}, {
            "串行": sp_serial,
            "并行": sp_parallel,
        }

    pd_data_strong, sp_data_strong = get_total_data(
        pd_s_data, sp_s_data, pd_idx_s, sp_idx_s, gt_node1_time_strong
    )
    pd_data_weak, sp_data_weak = get_total_data(
        pd_w_data, sp_w_data, pd_idx_w, sp_idx_w, gt_node1_time_weak
    )
    x_labels_strong_plot = [1] + list(x_strong) if gt_node1_time_strong else x_strong
    x_labels_weak_plot = [1] + list(x_weak) if gt_node1_time_weak else x_weak

    ours_colors = [OURS_SERIAL, OURS_PARALLEL]
    cms_colors = [to_rgba(CMS_SERIAL, CMS_ALPHA), to_rgba(CMS_PARALLEL, CMS_ALPHA)]

    pd_eff_color = EFF_OURS_COLOR
    sp_eff_color = EFF_CMS_COLOR

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=FIG_SIZE_COMBINED, sharex=False)

    def compute_efficiency(
        pd_plot_data, sp_plot_data, x_labels_plot, gt_node1_time, is_strong_scaling
    ):
        pd_total = [
            s + p for s, p in zip(pd_plot_data["串行"], pd_plot_data["并行"])
        ]
        sp_total = [
            s + p for s, p in zip(sp_plot_data["串行"], sp_plot_data["并行"])
        ]

        pd_efficiency = []
        sp_efficiency = []

        if gt_node1_time is not None:
            for i, n in enumerate(x_labels_plot):
                if is_strong_scaling:
                    # Strong Scaling: Efficiency = T_1 / (N * T_N)
                    pd_eff = gt_node1_time / (n * pd_total[i]) if pd_total[i] > 0 else 0
                    sp_eff = gt_node1_time / (n * sp_total[i]) if sp_total[i] > 0 else 0
                else:
                    # Weak Scaling: Efficiency = T_1 / T_N
                    pd_eff = gt_node1_time / pd_total[i] if pd_total[i] > 0 else 0
                    sp_eff = gt_node1_time / sp_total[i] if sp_total[i] > 0 else 0
                pd_efficiency.append(pd_eff)
                sp_efficiency.append(sp_eff)

        return pd_efficiency, sp_efficiency

    def plot_single(
        ax,
        pd_plot_data,
        sp_plot_data,
        x_labels_plot,
        title,
        gt_node1_time,
        is_strong_scaling,
    ):
        apply_spines(ax)
        width = 0.4
        num_x = len(x_labels_plot)
        x_ticks = np.arange(num_x)
        pd_labels = sorted(pd_plot_data.keys())
        sp_labels = sorted(sp_plot_data.keys())
        pd_colors_map = {
            lab: ours_colors[i % len(ours_colors)] for i, lab in enumerate(pd_labels)
        }
        sp_colors_map = {
            lab: cms_colors[i % len(cms_colors)] for i, lab in enumerate(sp_labels)
        }

        bottom = np.zeros(num_x)
        for lab in sp_labels:
            data = np.array(sp_plot_data.get(lab, [0] * num_x))
            ax.bar(
                x_ticks - width / 2.0,
                data,
                width,
                bottom=bottom,
                color=sp_colors_map[lab],
                edgecolor=None,
                zorder=2,
            )
            bottom += data

        bottom = np.zeros(num_x)
        for lab in pd_labels:
            data = np.array(pd_plot_data.get(lab, [0] * num_x))
            ax.bar(
                x_ticks + width / 2.0,
                data,
                width,
                bottom=bottom,
                color=pd_colors_map[lab],
                edgecolor=None,
                zorder=2,
            )
            bottom += data

        ax.set_yscale("log")
        ax.grid(False)
        ax.text(
            0.98,
            0.90,
            title,
            transform=ax.transAxes,
            fontsize=LEGEND_FONTSIZE,
            ha="right",
            va="top",
        )
        ax.set_xticks(x_ticks)
        ax.set_xticklabels(x_labels_plot, fontsize=TICK_FONTSIZE)
        ax.tick_params(axis="y", labelsize=TICK_FONTSIZE)
        ylim = ax.get_ylim()
        ax.set_ylim(ylim[0], ylim[1] * 10)

        # --- 添加 Efficiency 曲线 (双纵轴) ---
        pd_efficiency, sp_efficiency = compute_efficiency(
            pd_plot_data, sp_plot_data, x_labels_plot, gt_node1_time, is_strong_scaling
        )

        if pd_efficiency and sp_efficiency:
            ax2_eff = ax.twinx()

            # 绘制 ours (pd) efficiency
            ax2_eff.plot(
                x_ticks,
                pd_efficiency,
                color=pd_eff_color,
                marker="o",
                linestyle="-",
                linewidth=LINE_WIDTH,
                markersize=MARKER_SIZE * 0.8,
                label="本文方法效率",
                zorder=10,
            )

            # 绘制 cms (sp) efficiency
            ax2_eff.plot(
                x_ticks,
                sp_efficiency,
                color=sp_eff_color,
                marker="o",
                linestyle="-",
                linewidth=LINE_WIDTH,
                markersize=MARKER_SIZE * 0.8,
                label="CB-CMS效率",
                zorder=10,
            )

            ax2_eff.set_ylabel("效率", fontsize=LABEL_FONTSIZE)
            ax2_eff.set_yscale("log")
            ax2_eff.tick_params(axis="y", which="major", labelsize=TICK_FONTSIZE)

            # 设置 efficiency Y 轴范围
            all_eff_values = [v for v in pd_efficiency + sp_efficiency if v > 0]
            if all_eff_values:
                eff_min, eff_max = min(all_eff_values), max(all_eff_values)
                log_min = math.floor(math.log10(eff_min * 0.8))
                log_max = math.ceil(math.log10(eff_max * 1.2))
                ylim_min = max(10**log_min, 0.001)
                ylim_max = min(10**log_max, 10.0)
                ax2_eff.set_ylim(ylim_min, ylim_max)
            else:
                ax2_eff.set_ylim(0.01, 2.0)

            return ax2_eff
        return None

    ax1_eff = plot_single(
        ax1,
        pd_data_strong,
        sp_data_strong,
        x_labels_strong_plot,
        "强扩展",
        gt_node1_time_strong,
        is_strong_scaling=True,
    )
    ax2_eff = plot_single(
        ax2,
        pd_data_weak,
        sp_data_weak,
        x_labels_weak_plot,
        "弱扩展",
        gt_node1_time_weak,
        is_strong_scaling=False,
    )

    ax1.set_ylabel("时间 (s)", fontsize=LABEL_FONTSIZE)
    ax2.set_ylabel("时间 (s)", fontsize=LABEL_FONTSIZE)
    ax2.set_xlabel("计算节点数", fontsize=LABEL_FONTSIZE)

    legend_handles = [
        Patch(color=ours_colors[0], label="本文方法 串行"),
        Patch(color=cms_colors[0], label="CB-CMS 串行"),
        Patch(color=ours_colors[1], label="本文方法 并行"),
        Patch(color=cms_colors[1], label="CB-CMS 并行"),
        Line2D(
            [0],
            [0],
            color=pd_eff_color,
            marker="o",
            linestyle="-",
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE * 0.8,
            label="本文方法效率",
        ),
        Line2D(
            [0],
            [0],
            color=sp_eff_color,
            marker="o",
            linestyle="-",
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE * 0.8,
            label="CB-CMS效率",
        ),
    ]
    fig.legend(
        handles=legend_handles,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.02),
        ncol=3,
        frameon=False,
        fontsize=LEGEND_FONTSIZE,
    )
    fig.subplots_adjust(top=0.86, hspace=0.15)
    save_both(fig, os.path.join(output_dir, "combined_strong_weak_total_breakdown.png"))


def generate_combined_strong_weak_balance_line(
    pd_strong, sp_strong, pd_weak, sp_weak, gt_strong, gt_weak, output_dir
):
    from matplotlib.colors import to_rgba

    os.makedirs(output_dir, exist_ok=True)

    def filter_by_intersection(pd_data, sp_data):
        pd_x, pd_idx = get_x_axis_and_indices(pd_data)
        sp_x, sp_idx = get_x_axis_and_indices(sp_data)
        if pd_x != sp_x:
            common = sorted(list(set(pd_x) & set(sp_x)))
            if not common:
                return pd_x, pd_idx, sp_idx, pd_data, sp_data
            pd_sorted = [pd_data[i] for i in pd_idx]
            sp_sorted = [sp_data[i] for i in sp_idx]
            pd_filtered = [d for d, x in zip(pd_sorted, pd_x) if x in common]
            sp_filtered = [d for d, x in zip(sp_sorted, sp_x) if x in common]
            return (
                common,
                np.arange(len(pd_filtered)),
                np.arange(len(sp_filtered)),
                pd_filtered,
                sp_filtered,
            )
        return pd_x, pd_idx, sp_idx, pd_data, sp_data

    x_strong, pd_idx_s, sp_idx_s, pd_s_data, sp_s_data = filter_by_intersection(
        pd_strong, sp_strong
    )
    x_weak, pd_idx_w, sp_idx_w, pd_w_data, sp_w_data = filter_by_intersection(
        pd_weak, sp_weak
    )

    if not x_strong or not x_weak:
        print("警告：缺少 Strong 或 Weak 的 X 轴数据，跳过 Balance 合并线图")
        return

    gt_node1_balance = None
    if gt_strong and len(gt_strong) > 0:
        gt_node1_balance = 1.0

    fig, (ax_top, ax_bottom) = plt.subplots(
        2, 1, figsize=FIG_SIZE_COMBINED, sharex=False
    )
    pd_color_map = {"Time Balance": OURS_SERIAL, "Memory Balance": OURS_PARALLEL}
    sp_color_map = {
        "Time Balance": to_rgba(CMS_SERIAL, CMS_ALPHA),
        "Memory Balance": to_rgba(CMS_PARALLEL, CMS_ALPHA),
    }

    def draw_subplot(
        ax,
        pd_list,
        sp_list,
        pd_idx,
        sp_idx,
        x_labels,
        title,
        remove_xlabel=False,
        show_legend=True,
    ):
        apply_spines(ax)
        pd_time = get_line_data(
            pd_list, pd_idx, ["summary_parallel", "avg_load_balance_time"]
        )
        pd_mem = get_line_data(
            pd_list, pd_idx, ["summary_parallel", "avg_load_balance_memory"]
        )
        sp_time = get_line_data(
            sp_list, sp_idx, ["summary_parallel", "avg_load_balance_time"]
        )
        sp_mem = get_line_data(
            sp_list, sp_idx, ["summary_parallel", "avg_load_balance_memory"]
        )

        x_plot = [1] + list(x_labels) if gt_node1_balance else x_labels
        if gt_node1_balance:
            pd_time = [gt_node1_balance] + pd_time
            pd_mem = [gt_node1_balance] + pd_mem
            sp_time = [gt_node1_balance] + sp_time
            sp_mem = [gt_node1_balance] + sp_mem

        (cms_time,) = ax.plot(
            x_plot,
            sp_time,
            marker="o",
            linestyle="-",
            color=sp_color_map["Time Balance"],
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE,
            label="CB-CMS 时间",
        )
        (cms_mem,) = ax.plot(
            x_plot,
            sp_mem,
            marker="o",
            linestyle="-",
            color=sp_color_map["Memory Balance"],
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE,
            label="CB-CMS 内存",
        )
        (ours_time,) = ax.plot(
            x_plot,
            pd_time,
            marker="o",
            linestyle="-",
            color=pd_color_map["Time Balance"],
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE,
            label="本文方法 时间",
        )
        (ours_mem,) = ax.plot(
            x_plot,
            pd_mem,
            marker="o",
            linestyle="-",
            color=pd_color_map["Memory Balance"],
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE,
            label="本文方法 内存",
        )

        ax.text(
            0.98,
            0.95,
            title,
            transform=ax.transAxes,
            fontsize=LEGEND_FONTSIZE,
            ha="right",
            va="top",
        )
        ax.set_ylabel("均衡比", fontsize=LABEL_FONTSIZE)
        ax.set_xticks(x_plot)
        ax.set_xticklabels(x_plot, fontsize=TICK_FONTSIZE)
        ax.tick_params(axis="y", labelsize=TICK_FONTSIZE)
        ax.grid(False)
        all_vals = [v for v in pd_time + pd_mem + sp_time + sp_mem if not np.isnan(v)]
        if all_vals:
            ax.set_ylim(0.4, max(all_vals) * 1.2)
        if not remove_xlabel:
            ax.set_xlabel("计算节点数", fontsize=LABEL_FONTSIZE)
        if show_legend:
            ax.legend(
                handles=[ours_time, ours_mem, cms_time, cms_mem],
                labels=["本文方法 时间", "本文方法 内存", "CB-CMS 时间", "CB-CMS 内存"],
                loc="upper center",
                bbox_to_anchor=(0.5, 1.2),
                ncol=4,
                frameon=False,
                fontsize=LEGEND_FONTSIZE,
            )

    draw_subplot(
        ax_top,
        pd_s_data,
        sp_s_data,
        pd_idx_s,
        sp_idx_s,
        x_strong,
        "强扩展",
        remove_xlabel=True,
        show_legend=True,
    )
    draw_subplot(
        ax_bottom,
        pd_w_data,
        sp_w_data,
        pd_idx_w,
        sp_idx_w,
        x_weak,
        "弱扩展",
        remove_xlabel=False,
        show_legend=False,
    )
    fig.subplots_adjust(top=0.88, hspace=0.20)
    save_both(fig, os.path.join(output_dir, "combined_strong_weak_balance_line.png"))
    print("完成: combined_strong_weak_balance_line.{png,pdf}")


def generate_combined_strong_weak_peak_memory_line(
    pd_strong, sp_strong, pd_weak, sp_weak, gt_strong, gt_weak, output_dir
):
    from matplotlib.colors import to_rgba

    os.makedirs(output_dir, exist_ok=True)

    def filter_by_intersection(pd_data, sp_data):
        pd_x, pd_idx = get_x_axis_and_indices(pd_data)
        sp_x, sp_idx = get_x_axis_and_indices(sp_data)
        if pd_x != sp_x:
            common = sorted(list(set(pd_x) & set(sp_x)))
            if not common:
                return pd_x, pd_idx, sp_idx, pd_data, sp_data
            pd_sorted = [pd_data[i] for i in pd_idx]
            sp_sorted = [sp_data[i] for i in sp_idx]
            pd_filtered = [d for d, x in zip(pd_sorted, pd_x) if x in common]
            sp_filtered = [d for d, x in zip(sp_sorted, sp_x) if x in common]
            return (
                common,
                np.arange(len(pd_filtered)),
                np.arange(len(sp_filtered)),
                pd_filtered,
                sp_filtered,
            )
        return pd_x, pd_idx, sp_idx, pd_data, sp_data

    x_strong, pd_idx_s, sp_idx_s, pd_s_data, sp_s_data = filter_by_intersection(
        pd_strong, sp_strong
    )
    x_weak, pd_idx_w, sp_idx_w, pd_w_data, sp_w_data = filter_by_intersection(
        pd_weak, sp_weak
    )

    if not x_strong or not x_weak:
        print("警告：缺少 Strong 或 Weak 的 X 轴数据，跳过 Peak Memory 合并线图")
        return

    gt_node1_memory = None
    if gt_strong and len(gt_strong) > 0:
        try:
            gt_point = get_gt_reference_point(gt_strong)
            if gt_point:
                gt_node1_memory = gt_point["summary_serial"]["max_peak_memory_gb"]
        except:
            pass

    fig, (ax_top, ax_bottom) = plt.subplots(
        2, 1, figsize=FIG_SIZE_COMBINED, sharex=False
    )
    pd_color_map = {"串行": OURS_SERIAL, "并行": OURS_PARALLEL}
    sp_color_map = {
        "串行": to_rgba(CMS_SERIAL, CMS_ALPHA),
        "并行": to_rgba(CMS_PARALLEL, CMS_ALPHA),
    }

    def draw_subplot(
        ax,
        pd_list,
        sp_list,
        pd_idx,
        sp_idx,
        x_labels,
        title,
        remove_xlabel=False,
        show_legend=True,
    ):
        apply_spines(ax)
        pd_serial = get_line_data(
            pd_list, pd_idx, ["summary_serial", "max_peak_memory_gb"]
        )
        pd_parallel = get_line_data(
            pd_list, pd_idx, ["summary_parallel", "max_peak_memory_gb"]
        )
        sp_serial = get_line_data(
            sp_list, sp_idx, ["summary_serial", "max_peak_memory_gb"]
        )
        sp_parallel = get_line_data(
            sp_list, sp_idx, ["summary_parallel", "max_peak_memory_gb"]
        )

        x_plot_serial = [1] + list(x_labels) if gt_node1_memory else list(x_labels)
        x_plot_parallel = list(x_labels)
        if gt_node1_memory:
            pd_serial = [gt_node1_memory] + pd_serial
            sp_serial = [gt_node1_memory] + sp_serial

        (cms_serial,) = ax.plot(
            x_plot_serial,
            sp_serial,
            marker="o",
            linestyle="-",
            color=sp_color_map["串行"],
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE,
            label="CB-CMS 串行",
        )
        (cms_parallel,) = ax.plot(
            x_plot_parallel,
            sp_parallel,
            marker="o",
            linestyle="-",
            color=sp_color_map["并行"],
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE,
            label="CB-CMS 并行",
        )
        (ours_serial,) = ax.plot(
            x_plot_serial,
            pd_serial,
            marker="o",
            linestyle="-",
            color=pd_color_map["串行"],
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE,
            label="本文方法 串行",
        )
        (ours_parallel,) = ax.plot(
            x_plot_parallel,
            pd_parallel,
            marker="o",
            linestyle="-",
            color=pd_color_map["并行"],
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE,
            label="本文方法 并行",
        )

        ax.text(
            0.98,
            0.90,
            title,
            transform=ax.transAxes,
            fontsize=LEGEND_FONTSIZE,
            ha="right",
            va="top",
        )
        ax.set_ylabel("峰值内存 (GB)", fontsize=LABEL_FONTSIZE)
        ax.set_xticks(x_plot_serial)
        ax.set_xticklabels(x_plot_serial, fontsize=TICK_FONTSIZE)
        ax.tick_params(axis="y", labelsize=TICK_FONTSIZE)
        ax.grid(False)
        ax.set_yscale("log")
        ylim = ax.get_ylim()
        ax.set_ylim(ylim[0], ylim[1] * 10)
        if not remove_xlabel:
            ax.set_xlabel("计算节点数", fontsize=LABEL_FONTSIZE)
        if show_legend:
            ax.legend(
                handles=[ours_serial, ours_parallel, cms_serial, cms_parallel],
                labels=[
                    "本文方法 串行",
                    "本文方法 并行",
                    "CB-CMS 串行",
                    "CB-CMS 并行",
                ],
                loc="upper center",
                bbox_to_anchor=(0.5, 1.18),
                ncol=4,
                frameon=False,
                fontsize=16,
            )

    draw_subplot(
        ax_top,
        pd_s_data,
        sp_s_data,
        pd_idx_s,
        sp_idx_s,
        x_strong,
        "强扩展",
        remove_xlabel=True,
        show_legend=True,
    )
    draw_subplot(
        ax_bottom,
        pd_w_data,
        sp_w_data,
        pd_idx_w,
        sp_idx_w,
        x_weak,
        "弱扩展",
        remove_xlabel=False,
        show_legend=False,
    )
    fig.subplots_adjust(top=0.85, hspace=0.15)
    save_both(
        fig, os.path.join(output_dir, "combined_strong_weak_peak_memory_line.png")
    )
    print("完成: combined_strong_weak_peak_memory_line.{png,pdf}")


# =========================================================================
# --- 7. 主执行函数 ---
# =========================================================================


def main():
    """
    加载所有6个JSON文件，可选地替换键，并为 weak 和 strong scaling 生成图表。
    """
    # --- 1. 设置 ArgParse ---
    parser = argparse.ArgumentParser(description="Generate scaling benchmark plots.")
    parser.add_argument(
        "-r",
        "--replacements",
        dest="replacement_file",
        default=None,
        help="Path to a CSV file (old_prefix,new_prefix) for replacing step keys.",
    )
    args = parser.parse_args()

    replacement_map = []
    replacement_file = args.replacement_file
    if replacement_file is None and os.path.exists("replacement.txt"):
        replacement_file = "replacement.txt"
        print(f"自动检测到 replacement.txt，将使用该文件")

    if replacement_file:
        replacement_map = parse_replacement_file(replacement_file)
    else:
        replacement_map = [
            ("solve_eig", "sub_eig"),
            ("alfim", "ALFIM"),
            ("mp_cms", "galerkin_projection"),
            ("traditional_cms_assemble", "assemble"),
            ("solve_reduced_sparse_reg", "solve_reduced_eig"),
        ]
        print(f"使用默认替换规则 ({len(replacement_map)} 条)")

    # --- 3. 加载 JSON 数据 (*** 修改: 增加 gt ***) ---
    json_files = {
        "weak_pd": "weak-pd_benchmarks.json",
        "weak_sp": "weak-sp_benchmarks.json",
        "weak_gt": "weak-gt_benchmarks.json",  # <-- 新增
        "strong_pd": "strong-pd_benchmarks.json",
        "strong_sp": "strong-sp_benchmarks.json",
        "strong_gt": "strong-gt_benchmarks.json",  # <-- 新增
    }

    data = {}

    for key, filename in json_files.items():
        if not os.path.exists(filename):
            # 'gt' 文件是可选的
            if "gt" in key:
                print(f"提示: 未找到基准文件: {filename} (可选)")
            else:
                print(f"错误: 未找到所需文件: {filename}")
                # data[key] = None # 确保键存在
        else:
            try:
                with open(filename, "r") as f:
                    data[key] = json.load(f)
                print(f"成功加载: {filename}")
            except Exception as e:
                print(f"加载 {filename} 时出错: {e}")
                # data[key] = None

    # --- 4. 应用替换 (新步骤) ---
    # 在加载数据后、绘图前执行
    if replacement_map:
        data = apply_key_replacements(data, replacement_map)

    if "weak_pd" in data and "weak_sp" in data:
        generate_all_plots_for_scaling_type(
            data["weak_pd"], data["weak_sp"], data.get("weak_gt"), "weak_scaling"
        )
    else:
        print("\n跳过 Weak Scaling，因为缺少 'weak_pd' 或 'weak_sp' 数据。")

    if "strong_pd" in data and "strong_sp" in data:
        generate_all_plots_for_scaling_type(
            data["strong_pd"],
            data["strong_sp"],
            data.get("strong_gt"),
            "strong_scaling",
        )
    else:
        print("\n跳过 Strong Scaling，因为缺少 'strong_pd' 或 'strong_sp' 数据。")

    if all(k in data for k in ("strong_pd", "strong_sp", "weak_pd", "weak_sp")):
        generate_combined_strong_weak_total(
            data["strong_pd"],
            data["strong_sp"],
            data["weak_pd"],
            data["weak_sp"],
            data.get("strong_gt"),
            data.get("weak_gt"),
            "combined_plots",
        )
        generate_combined_strong_weak_balance_line(
            data["strong_pd"],
            data["strong_sp"],
            data["weak_pd"],
            data["weak_sp"],
            data.get("strong_gt"),
            data.get("weak_gt"),
            "combined_plots",
        )
        generate_combined_strong_weak_peak_memory_line(
            data["strong_pd"],
            data["strong_sp"],
            data["weak_pd"],
            data["weak_sp"],
            data.get("strong_gt"),
            data.get("weak_gt"),
            "combined_plots",
        )
    else:
        print("\n跳过组合图，因为缺少 Strong 或 Weak 数据。")

    print("\n--- 所有绘图任务完成 (共 13 张图: 10 单独 + 3 合并) ---")


if __name__ == "__main__":
    main()
