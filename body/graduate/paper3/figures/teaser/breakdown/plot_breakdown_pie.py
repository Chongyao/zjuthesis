#!/usr/bin/env python3
import os
import sys
import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from plot_style_config import get_style, apply_style, COLOR_SCHEMES

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "time_breakdown_pie.pdf")

SCHEME = os.environ.get("PLOT_COLOR_SCHEME", "teal_coral")
STYLE = get_style(SCHEME)
apply_style(STYLE, scale="double_column")


scale = 1.3


def load_data(filename):
    path = os.path.join(SCRIPT_DIR, filename)
    with open(path, "r") as f:
        return json.load(f)


def main():
    data = load_data("breakdown_NEP100_NEV3000.json")
    stages = {s["name"]: s for s in data["stages"]}

    items = []

    t_interior = stages["Interior Eigenmodes"]["total_time"]
    items.append(
        {
            "label": "Interior Eigenmodes",
            "time": t_interior,
            "color": COLOR_SCHEMES[SCHEME]["primary"],
            "components": stages["Interior Eigenmodes"]["components"],
        }
    )

    t_interface = stages["Interface Modes"]["total_time"]
    items.append(
        {
            "label": "Interface Modes",
            "time": t_interface,
            "color": COLOR_SCHEMES[SCHEME]["secondary"],
            "components": stages["Interface Modes"]["components"],
        }
    )

    t_proj = stages["Matrix Reducing"]["total_time"]
    items.append(
        {
            "label": "Matrix Reducing",
            "time": t_proj,
            "color": COLOR_SCHEMES[SCHEME]["tertiary"],
            "components": stages["Matrix Reducing"]["components"],
        }
    )

    t_reduce = (
        stages["Solve Reduced eigen probelm"]["total_time"]
        + stages["Assemble Reduce Operator"]["total_time"]
    )
    items.append(
        {
            "label": "Reduced Solve",
            "time": t_reduce,
            "color": COLOR_SCHEMES[SCHEME]["quaternary"],
            "components": [
                {"name": "Computation", "time": t_reduce, "type": "computation"}
            ],
        }
    )

    total_time = sum(item["time"] for item in items)

    # 二级组件的阴影样式（按类型）
    component_hatches = {
        "computation": "",  # 无阴影
        "idle": "//",  # 斜线阴影
        "communication": "xx",  # 交叉阴影
    }

    # 创建图形
    fig, ax = plt.subplots(figsize=(17, 17))

    # 格式化时间
    def format_time(seconds):
        """格式化时间为分钟或秒"""
        if seconds >= 60:
            return f"{seconds / 60:.1f} min"
        else:
            return f"{seconds:.1f} s"

    # 准备外环数据（一级阶段）
    outer_sizes = [item["time"] for item in items]
    outer_colors = [item["color"] for item in items]
    outer_labels = [
        f"{item['label']}\n{item['time'] / total_time * 100:.1f}% ({format_time(item['time'])})" for item in items
    ]

    # 准备内环数据（二级组件）
    inner_sizes = []
    inner_colors = []
    inner_hatches = []
    for item in items:
        for comp in item["components"]:
            inner_sizes.append(comp["time"])
            # 内环使用较浅的颜色
            inner_colors.append(item["color"])
            inner_hatches.append(
                component_hatches.get(comp.get("type", "computation"), "")
            )

    # 绘制外环（一级阶段）
    outer_wedges, outer_texts = ax.pie(
        outer_sizes,
        radius=1.0,
        colors=outer_colors,
        wedgeprops=dict(width=0.3, edgecolor="white", linewidth=2),
        startangle=45,
        counterclock=False,
    )

    # 添加外环标签 - 放置在饼图两侧
    for i, (wedge, label) in enumerate(zip(outer_wedges, outer_labels)):
        angle = (wedge.theta2 + wedge.theta1) / 2

        # 将标签放置在饼图两侧，x 坐标固定在左右两边
        if np.cos(np.radians(angle)) > 0:
            x = 1.25  # 右侧，连线更短
            ha = "left"
        else:
            x = -1.25  # 左侧，连线更短
            ha = "right"
        y = 1.1 * np.sin(np.radians(angle))

        ax.annotate(
            label,
            xy=(1.0 * np.cos(np.radians(angle)), 1.0 * np.sin(np.radians(angle))),
            xytext=(x, y),
            ha=ha,
            va="center",
            fontsize=STYLE.scaled_fontsize("legend") * scale * 1.6,  # 字体继续放大
            fontweight="bold",
            color="white",  # Text color white
            arrowprops=dict(arrowstyle="-", color="white", lw=1.2),  # Arrow color white
        )

    # 绘制内环（二级组件）
    inner_wedges, _ = ax.pie(
        inner_sizes,
        radius=0.7,
        colors=inner_colors,
        wedgeprops=dict(width=0.25, edgecolor="white", linewidth=1),
        startangle=45,
        counterclock=False,
    )

    # 为内环添加阴影
    for wedge, hatch in zip(inner_wedges, inner_hatches):
        if hatch:
            wedge.set_hatch(hatch)
            wedge.set_edgecolor("white")
            wedge.set_linewidth(2)  # 白色阴影加粗

    # 图例 - 只保留阴影类型
    legend_patches = [
        mpatches.Patch(facecolor="gray", edgecolor="white", label="Computation"),
        mpatches.Patch(facecolor="gray", edgecolor="white", hatch="//", label="Idle"),
        mpatches.Patch(facecolor="gray", edgecolor="white", hatch="xx", label="Comm.(<0.1%)"),
    ]

    ax.legend(
        handles=legend_patches,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.05),  # 抬高 legend
        ncol=3,
        frameon=False,
        handlelength=1.2,
        handletextpad=0.4,
        markerscale=2,
        columnspacing=0.8,
        labelcolor="white",  # Legend text color
        prop={"weight": "bold", "size": STYLE.scaled_fontsize("legend") * scale * 1.8},  # 字体加粗+放大
    )

    # 在中心添加总时间
    ax.text(
        0,
        0,
        f"Total\n{format_time(total_time)}",
        ha="center",
        va="center",
        fontsize=STYLE.scaled_fontsize("title") * scale,
        fontweight="bold",
        color="white",  # Center text color white
    )

    ax.set_aspect("equal")
    plt.tight_layout()

    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight")
    print(f"✓ Saved: {OUTPUT_FILE}")

    plt.savefig(
        OUTPUT_FILE.replace(".pdf", ".png"),
        dpi=300,
        bbox_inches="tight",
        transparent=True,
    )
    print(f"✓ Saved: {OUTPUT_FILE.replace('.pdf', '.png')}")


if __name__ == "__main__":
    main()
