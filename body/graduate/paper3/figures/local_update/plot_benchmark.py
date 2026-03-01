#!/usr/bin/env python3
"""
Unified benchmark visualization for CMS Local Update vs other methods.
Supports both PCB and micro_long models via command line or auto-detection.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style_config import get_style, apply_style

SCHEME = os.environ.get('PLOT_COLOR_SCHEME', 'teal_coral')
STYLE = get_style(SCHEME)
apply_style(STYLE, scale="double_column")

LABEL_FONTSIZE = STYLE.scaled_fontsize("label", "double_column")
LEGEND_FONTSIZE = STYLE.scaled_fontsize("legend", "double_column")
TICK_FONTSIZE = STYLE.scaled_fontsize("tick", "double_column")
TITLE_FONTSIZE = STYLE.scaled_fontsize("title", "double_column")

COLORS = {
    "Substructure Eigenmodes": STYLE.breakdown_colors.get(
        "Substructure Eigenmodes", STYLE.ours
    ),
    "Interface Modes": STYLE.breakdown_colors.get(
        "Interface Modes", STYLE.method_colors["ours_nc"]
    ),
    "Matrix Reducing": STYLE.breakdown_colors.get("Matrix Reducing", STYLE.cms),
    "Reduced Solve": STYLE.breakdown_colors.get("Reduced Solve", STYLE.amls),
    "Global Solve": STYLE.breakdown_colors.get(
        "Global Solve", STYLE.method_colors["imr"]
    ),
}

COMPONENTS = [
    "Substructure Eigenmodes",
    "Interface Modes",
    "Matrix Reducing",
    "Reduced Solve",
    "Global Solve",
]

# Map CSV method names to canonical display names
METHOD_DISPLAY_NAMES = {
    "Origin CMS Full": "Origin mesh\nOurs full comp.",
    "Updated CMS Full": "Modified mesh\nOurs full comp.",
    "CMS Local Update": "Modified mesh\nOurs local update",
    "Global Spectra": "Modified mesh\nSpectra",
}


def get_display_name(method):
    """Get canonical display name for a method."""
    return METHOD_DISPLAY_NAMES.get(method, method)


def detect_model():
    """Auto-detect model type based on available CSV files."""
    if os.path.exists("benchmark_core.csv"):
        return "pcb", "benchmark_core.csv", "benchmark_comparison"
    elif os.path.exists("benchmark_neig100_core.csv"):
        return "micro", "benchmark_neig100_core.csv", "benchmark_neig100_comparison"
    else:
        raise FileNotFoundError(
            "No benchmark CSV found. Expected benchmark_core.csv or benchmark_neig100_core.csv"
        )


def plot_benchmark(model_type, csv_file, output_prefix):
    df = pd.read_csv(csv_file)
    print(df)

    fig, ax = plt.subplots(figsize=(10, 6))

    methods = df["Method"].tolist()
    x = np.arange(len(methods))
    width = 0.6

    bottom = np.zeros(len(methods))
    for col in COMPONENTS:
        values = df[col].values
        if values.sum() > 0:
            ax.bar(x, values, width, label=col, bottom=bottom, color=COLORS[col])
            bottom += values

    ax.set_xlabel("Method", fontsize=LABEL_FONTSIZE)
    ax.set_ylabel("Core Computation Time (seconds)", fontsize=LABEL_FONTSIZE)

    # No title for cleaner figure

    ax.set_xticks(x)
    ax.set_xticklabels([get_display_name(m) for m in methods], fontsize=TICK_FONTSIZE)
    ax.tick_params(axis="y", labelsize=TICK_FONTSIZE)
    ax.grid(False)

    local_update_time = df[df["Method"] == "CMS Local Update"]["Total Core"].values[0]
    speedups = df["Total Core"].values / local_update_time

    ax.axhline(
        y=local_update_time,
        color=STYLE.method_colors["imr"],
        linestyle="--",
        linewidth=1.5,
        label=f"Ours Local Update baseline ({local_update_time:.1f}s)",
    )

    max_total = df["Total Core"].max()
    label_offset1 = max_total * 0.03
    label_offset2 = max_total * 0.10

    for i, (total, speedup) in enumerate(zip(df["Total Core"], speedups)):
        ax.annotate(
            f"{total:.1f}s",
            xy=(i, total + label_offset1),
            ha="center",
            fontsize=12,
            fontweight="bold",
        )
        if speedup == 1.0:
            speedup_text = "(baseline)"
        elif speedup > 1.0:
            speedup_text = f"({speedup:.2f}x slower)"
        else:
            speedup_text = f"({1 / speedup:.2f}x faster)"
        ax.annotate(
            speedup_text,
            xy=(i, total + label_offset2),
            ha="center",
            fontsize=10,
            color=STYLE.ui_colors["text_secondary"],
        )

    ax.set_ylim(0, max_total * 1.25)
    ax.legend(loc="upper right", fontsize=LEGEND_FONTSIZE)

    plt.tight_layout()
    plt.savefig(f"{output_prefix}.png", dpi=150, bbox_inches="tight")
    plt.savefig(f"{output_prefix}.pdf", bbox_inches="tight")
    print(f"Saved: {output_prefix}.png/pdf")
    plt.close()

    if model_type == "micro":
        plot_cms_breakdown(df, "benchmark_neig100_cms_breakdown")

    print_summary(df, model_type, local_update_time)


def plot_cms_breakdown(df, output_prefix):
    fig, ax = plt.subplots(figsize=(10, 6))

    cms_methods = ["Origin CMS Full", "Updated CMS Full", "CMS Local Update"]
    cms_df = df[df["Method"].isin(cms_methods)]

    x = np.arange(len(cms_methods))
    width = 0.2

    components = [
        "Substructure Eigenmodes",
        "Interface Modes",
        "Matrix Reducing",
        "Reduced Solve",
    ]
    for i, comp in enumerate(components):
        values = cms_df[comp].values
        ax.bar(x + i * width, values, width, label=comp, color=list(COLORS.values())[i])

    ax.set_xlabel("Method", fontsize=LABEL_FONTSIZE)
    ax.set_ylabel("Time (seconds)", fontsize=LABEL_FONTSIZE)
    ax.set_xticks(x + 1.5 * width)
    ax.set_xticklabels(
        [get_display_name(m) for m in cms_methods], fontsize=TICK_FONTSIZE
    )
    ax.tick_params(axis="y", labelsize=TICK_FONTSIZE)
    ax.legend(fontsize=LEGEND_FONTSIZE)
    ax.grid(False)

    plt.tight_layout()
    plt.savefig(f"{output_prefix}.png", dpi=150, bbox_inches="tight")
    plt.savefig(f"{output_prefix}.pdf", bbox_inches="tight")
    print(f"Saved: {output_prefix}.png/pdf")
    plt.close()


def print_summary(df, model_type, local_update_time):
    print("\n" + "=" * 60)
    if model_type == "pcb":
        print("BENCHMARK SUMMARY - PCB Model (Laplacian, neig=100, np=4)")
    else:
        print("BENCHMARK SUMMARY - micro_long Model (neig=100, np=10)")
    print("=" * 60)

    print(f"\nCore Computation Times:")
    for _, row in df.iterrows():
        print(f"  {row['Method']:20s}: {row['Total Core']:6.1f}s")

    print(f"\nSpeedup Analysis (CMS Local Update as baseline):")
    for _, row in df.iterrows():
        speedup = row["Total Core"] / local_update_time
        if row["Method"] == "CMS Local Update":
            print(f"  {row['Method']:20s}: baseline")
        elif speedup > 1.0:
            print(f"  {row['Method']:20s}: {speedup:.2f}x slower")
        else:
            print(f"  {row['Method']:20s}: {1 / speedup:.2f}x faster")

    global_time = df[df["Method"] == "Global Spectra"]["Total Core"].values[0]
    print(
        f"\nCMS Local Update vs Global Spectra: {global_time / local_update_time:.2f}x faster"
    )


if __name__ == "__main__":
    model_type, csv_file, output_prefix = detect_model()
    print(f"Detected model: {model_type}, CSV: {csv_file}")
    plot_benchmark(model_type, csv_file, output_prefix)
