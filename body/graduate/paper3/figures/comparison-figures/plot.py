#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from matplotlib.lines import Line2D

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figures.plot_style_config import get_style, apply_style

SCHEME = os.environ.get('PLOT_COLOR_SCHEME', 'teal_coral')
STYLE = get_style(SCHEME)
apply_style(STYLE, scale="double_column")

LABEL_FONTSIZE = STYLE.scaled_fontsize("label", "double_column")
LEGEND_FONTSIZE = STYLE.scaled_fontsize("legend", "double_column")
TICK_FONTSIZE = STYLE.scaled_fontsize("tick", "double_column")

FIG_SIZE = (14, 7)
DPI = 300
LINE_WIDTH = 4.0
MARKER_SIZE = 10
BORDER_WIDTH = 2.0

ALG_TO_STYLE_KEY = {
    "PD": "ours",
    "PD-NC": "ours_nc",
    "CB-CMS": "cms",
    "CMS-INTRD": "imr",
    "AMLS": "amls",
}
ALG_DISPLAY_NAMES = {
    "PD": "Ours",
    "PD-NC": "PD-NC",
    "CB-CMS": "CB-CMS",
    "CMS-INTRD": "CMS-IMR",
    "AMLS": "AMLS",
}


def main():
    csv_file = (
        sys.argv[1]
        if len(sys.argv) > 1
        else next(
            (f for f in os.listdir(".") if "summary_clean.csv" in f),
            "board_summary_clean.csv",
        )
    )

    if not os.path.exists(csv_file):
        print(f"Error: File not found: {csv_file}")
        return

    df = pd.read_csv(csv_file)
    col_map = {
        "Method": "algorithm",
        "Num_Modes": "nep",
        "Error_2norm": "error",
        "Time_Total": "time",
    }
    df.rename(
        columns={k: v for k, v in col_map.items() if k in df.columns}, inplace=True
    )

    for col in ["nep", "error", "time"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df.dropna(inplace=True)

    unique_algorithms = sorted(df["algorithm"].unique())

    alg_style_map = {}
    for alg in unique_algorithms:
        style_key = ALG_TO_STYLE_KEY.get(alg, "ours")
        alg_style_map[alg] = {
            "marker": "o",
            "color": STYLE.method_colors.get(style_key, STYLE.ours),
        }

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIG_SIZE, sharey=True)

    for ax in [ax1, ax2]:
        for spine in ax.spines.values():
            spine.set_edgecolor(STYLE.ui_colors["spine"])
            spine.set_linewidth(BORDER_WIDTH)
        ax.grid(False)

    for alg, subset in df.groupby("algorithm"):
        style = alg_style_map[alg]
        display_name = ALG_DISPLAY_NAMES.get(alg, alg)

        subset_sorted_by_nep = subset.sort_values(by="nep")
        ax1.plot(
            subset_sorted_by_nep["nep"],
            subset_sorted_by_nep["error"],
            color=style["color"],
            marker=style["marker"],
            linestyle="solid",
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE,
            label=display_name,
        )

        ax2.plot(
            subset_sorted_by_nep["time"],
            subset_sorted_by_nep["error"],
            color=style["color"],
            marker=style["marker"],
            linestyle="solid",
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE,
        )

    ax1.set_xlabel(r"Number of Eigenpairs ($N_{ep}$)", fontsize=LABEL_FONTSIZE)
    ax1.set_ylabel(r"Relative Error ($\epsilon_{ev}$)", fontsize=LABEL_FONTSIZE)
    ax1.set_yscale("log")
    ax1.tick_params(
        axis="both", which="major", labelsize=TICK_FONTSIZE, width=2, length=6
    )

    ax2.set_xlabel("Total Time (s)", fontsize=LABEL_FONTSIZE)
    ax2.set_yscale("log")
    ax2.tick_params(
        axis="both", which="major", labelsize=TICK_FONTSIZE, width=2, length=6
    )

    plt.subplots_adjust(left=0.08, right=0.92, bottom=0.15, top=0.88, wspace=0.02)

    legend_handles = [
        Line2D(
            [0],
            [0],
            color=alg_style_map[alg]["color"],
            marker="o",
            linestyle="None",
            markersize=MARKER_SIZE,
            label=ALG_DISPLAY_NAMES.get(alg, alg),
        )
        for alg in unique_algorithms
    ]
    fig.legend(
        handles=legend_handles,
        ncol=len(unique_algorithms),
        fontsize=LEGEND_FONTSIZE,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.98),
        frameon=False,
        handletextpad=0.2,
        columnspacing=1.5,
    )

    csv_dir = os.path.dirname(csv_file) or "."
    base_name = os.path.splitext(os.path.basename(csv_file))[0].replace(
        "_summary_clean", ""
    )
    output_path = os.path.join(csv_dir, f"{base_name}_comparison")
    plt.savefig(f"{output_path}.png", dpi=DPI, bbox_inches="tight")
    plt.savefig(f"{output_path}.pdf", dpi=DPI, bbox_inches="tight")
    print(f"Saved: {output_path}.png")


if __name__ == "__main__":
    main()
