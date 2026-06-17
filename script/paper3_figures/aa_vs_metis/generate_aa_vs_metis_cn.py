#!/usr/bin/env python3
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import LogFormatterMathtext

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(THIS_DIR)))
TARGET_DIR = os.path.join(
    REPO_ROOT, "body", "graduate", "paper3", "figures",
    "comparison-figures", "aa_vs_metis",
)

sys.path.insert(0, os.path.join(REPO_ROOT, "body", "graduate", "paper3", "figures"))
from plot_style_config import get_style, apply_style

sys.path.insert(0, os.path.join(REPO_ROOT, "script"))
from thesis_figure_config import setup_figure_fonts, LABEL_SIZE as LABEL_FONTSIZE
from thesis_figure_config import LEGEND_SIZE as LEGEND_FONTSIZE, TICK_SIZE as TICK_FONTSIZE

SCHEME = os.environ.get("PLOT_COLOR_SCHEME", "teal_coral")
STYLE = get_style(SCHEME)
apply_style(STYLE, scale="double_column")
setup_figure_fonts()

FIG_SIZE = (14, 7)
LINE_WIDTH = 4.0
MARKER_SIZE = 10
BORDER_WIDTH = 2.0

PARTITION_COLORS = {
    "AA": STYLE.method_colors.get("ours", STYLE.ours),
    "METIS": STYLE.method_colors.get("cms", STYLE.cms),
}


def main():
    csv_file = os.path.join(THIS_DIR, "cat_aa_vs_metis.csv")
    df = pd.read_csv(csv_file)

    for col in ["Num_Modes", "Error_2norm", "Time_Total"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df.dropna(inplace=True)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIG_SIZE, sharey=True)

    for ax in [ax1, ax2]:
        for spine in ax.spines.values():
            spine.set_edgecolor(STYLE.ui_colors["spine"])
            spine.set_linewidth(BORDER_WIDTH)
        ax.grid(False)

    for ptype, subset in df.groupby("PartitionType"):
        ptype = str(ptype)
        color = PARTITION_COLORS[ptype]
        subset = subset.sort_values(by="Num_Modes")
        ax1.plot(
            subset["Num_Modes"], subset["Error_2norm"],
            color=color, marker="o", linestyle="solid",
            linewidth=LINE_WIDTH, markersize=MARKER_SIZE, label=ptype,
        )
        ax2.plot(
            subset["Time_Total"], subset["Error_2norm"],
            color=color, marker="o", linestyle="solid",
            linewidth=LINE_WIDTH, markersize=MARKER_SIZE,
        )

    ax1.set_xlabel(r"特征对数量 ($N_{ep}$)", fontsize=LABEL_FONTSIZE)
    ax1.set_ylabel(r"相对误差 ($\epsilon_{ev}$)", fontsize=LABEL_FONTSIZE)
    ax1.set_yscale("log")
    ax1.yaxis.set_major_formatter(LogFormatterMathtext())
    ax1.tick_params(axis="both", which="major", labelsize=TICK_FONTSIZE, width=2, length=6)

    ax2.set_xlabel("总计算时间 (秒)", fontsize=LABEL_FONTSIZE)
    ax2.set_yscale("log")
    ax2.yaxis.set_major_formatter(LogFormatterMathtext())
    ax2.tick_params(axis="both", which="major", labelsize=TICK_FONTSIZE, width=2, length=6)

    legend_handles = [
        Line2D([0], [0], color=PARTITION_COLORS[k], marker="o", linestyle="None",
               markersize=MARKER_SIZE, label={"AA": "轴对齐划分", "METIS": "METIS 划分"}[k])
        for k in ["AA", "METIS"]
    ]
    fig.legend(
        handles=legend_handles, ncol=2,
        fontsize=LEGEND_FONTSIZE, loc="upper center",
        bbox_to_anchor=(0.5, 0.98), frameon=False,
        handletextpad=0.2, columnspacing=1.5,
    )

    plt.subplots_adjust(left=0.08, right=0.92, bottom=0.15, top=0.88, wspace=0.02)

    os.makedirs(TARGET_DIR, exist_ok=True)
    out_base = os.path.join(TARGET_DIR, "cat_aa_vs_metis_comparison")
    plt.savefig(f"{out_base}.png", dpi=300, bbox_inches="tight")
    plt.savefig(f"{out_base}.pdf", dpi=300, bbox_inches="tight")
    print(f"Saved: {out_base}.png")
    print(f"Saved: {out_base}.pdf")


if __name__ == "__main__":
    main()
