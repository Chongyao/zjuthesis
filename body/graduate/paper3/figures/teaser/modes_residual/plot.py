#!/usr/bin/env python3
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from plot_style_config import get_style, apply_style

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "final_errors_right.txt")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "modes_residual.pdf")

SCHEME = os.environ.get("PLOT_COLOR_SCHEME", "teal_coral")
STYLE = get_style(SCHEME)
apply_style(STYLE, scale="double_column")

import matplotlib.ticker as ticker


def main():
    # Read pipe-separated text file, skipping header and separator line
    # Data has 3 columns: Index, Lambda, RelErr (despite header showing 4)
    df = pd.read_csv(
        DATA_FILE,
        sep=r"\s*\|\s*",
        skiprows=2,
        header=None,
        names=["Index", "Lambda", "RelErr"],
        engine="python",
    )

    df_filtered = df[df["Index"] >= 6].copy()

    fig, ax = plt.subplots(figsize=(7, 3))

    primary_color = STYLE.method_colors["cms"]

    ax.scatter(
        df_filtered["Index"],
        df_filtered["RelErr"],
        s=4,
        color=primary_color,
        alpha=0.5,
        edgecolor="none",
        rasterized=True,
    )

    ax.text(
        0.5,
        0.04,
        "Mode Index",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=STYLE.scaled_fontsize("label", "double_column") * 0.9,
        weight="bold",
        color="white",
    )

    ax.set_ylabel(
        r"$\|\mathbf{K}\mathbf{x} - \lambda \mathbf{M}\mathbf{x}\| / |\lambda| \|\mathbf{x}\|$",
        fontsize=STYLE.scaled_fontsize("label", "double_column") * 0.9,
        color="white",
    )

    ax.set_yscale("log")

    ax.yaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=10))
    ax.yaxis.set_minor_locator(
        ticker.LogLocator(base=10.0, subs=tuple(range(2, 10)), numticks=10)
    )

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color("white")
        spine.set_linewidth(0.8)

    ax.tick_params(
        axis="both",
        which="both",
        direction="in",
        top=True,
        right=True,
        colors="white",
        labelsize=STYLE.scaled_fontsize("tick", "double_column") * 0.85,
    )

    ax.set_xlim(left=6, right=df_filtered["Index"].max() * 1.02)

    y_min = df_filtered["RelErr"].min()
    y_max = df_filtered["RelErr"].max()
    ax.set_ylim(y_min * 0.3, y_max * 3.0)

    ax.grid(False)

    plt.tight_layout(pad=0.2)

    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight", transparent=True)
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
