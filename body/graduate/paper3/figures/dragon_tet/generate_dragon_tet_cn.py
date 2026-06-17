#!/usr/bin/env python3
"""
Dragon_tet scaling analysis: effect of partition count (np) on accuracy and performance.
Generates two figures:
  1. dragon_tet_performance.png/pdf  (1x2: Error vs NEP, Error vs Total Time)
  2. dragon_tet_breakdown.png/pdf    (stacked bar: time breakdown by component)
"""

import os
import re
import sys
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogFormatterMathtext

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(THIS_DIR)))))
TARGET_DIR = THIS_DIR

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style_config import get_style, apply_style

sys.path.insert(0, os.path.join(REPO_ROOT, "script"))
from thesis_figure_config import setup_figure_fonts, LABEL_SIZE as LABEL_FONTSIZE
from thesis_figure_config import LEGEND_SIZE as LEGEND_FONTSIZE, TICK_SIZE as TICK_FONTSIZE

SCHEME = os.environ.get("PLOT_COLOR_SCHEME", "teal_coral")
STYLE = get_style(SCHEME)
apply_style(STYLE, scale="double_column")
setup_figure_fonts()

LINE_WIDTH = 3.0
MARKER_SIZE = 10

LOG_DIR = os.path.join(THIS_DIR, "logs")
SUMMARY_CSV = os.path.join(THIS_DIR, "dragon_tet_summary.csv")


# ---------------------------------------------------------------------------
# 1. Extract data from run.log files
# ---------------------------------------------------------------------------

def extract_log_data(log_dir):
    records = []
    pattern = os.path.join(log_dir, "NEP_*_PD_np*")
    for folder in sorted(glob.glob(pattern)):
        basename = os.path.basename(folder)
        m = re.match(r"NEP_(\d+)_PD_np(\d+)", basename)
        if not m:
            continue
        nep = int(m.group(1))
        np_val = int(m.group(2))

        log_file = os.path.join(folder, "run.log")
        if not os.path.exists(log_file):
            continue

        with open(log_file, "r") as f:
            content = f.read()

        def grep_float(pattern_str):
            m = re.search(pattern_str, content)
            return float(m.group(1)) if m else np.nan

        t_sub_matches = re.findall(r"\[TOC\] CMS::solve time:\s+([0-9]+\.[0-9]+)", content)
        t_sub = sum(float(v) for v in t_sub_matches) if t_sub_matches else np.nan

        err_2norm = grep_float(r"error of eigen values \(2-norm\):\s+([0-9]+\.[0-9]+e[-+]?[0-9]+)")
        err_mean  = grep_float(r"error of eigen values \(Mean\):\s+([0-9]+\.[0-9]+e[-+]?[0-9]+)")
        t_ifc     = grep_float(r"set interface modes cost\s+([0-9]+\.[0-9]+)")
        t_red_c   = grep_float(r"construct reduced K, M cost\s+([0-9]+\.[0-9]+)")
        t_red_s   = grep_float(r"solve reduced eigen cost\s+([0-9]+\.[0-9]+)")
        t_gt      = grep_float(r"Spectra get ground truth cost\s+([0-9]+\.[0-9]+)")

        t_total = t_sub + t_ifc + t_red_c + t_red_s

        records.append({
            "NEP": nep, "np": np_val,
            "error_2norm": err_2norm, "error_mean": err_mean,
            "t_sub": t_sub, "t_ifc": t_ifc,
            "t_red_c": t_red_c, "t_red_s": t_red_s,
            "t_total": t_total, "t_gt": t_gt,
        })

    df = pd.DataFrame(records)
    df.sort_values(by=["NEP", "np"], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


def save_csv(df, filename="dragon_tet_summary.csv"):
    df.to_csv(filename, index=False)
    print(f"Saved summary CSV: {filename}")


# ---------------------------------------------------------------------------
# 2. Plot 1: Error and Total Time vs NEP (1x2)
# ---------------------------------------------------------------------------

def plot_performance(df):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    for ax in [ax1, ax2]:
        for spine in ax.spines.values():
            spine.set_edgecolor(STYLE.ui_colors["spine"])
            spine.set_linewidth(1.5)
        ax.grid(False)

    np_vals = sorted(df["np"].unique())
    colors = STYLE.get_sequential_colors(len(np_vals))
    np_to_color = {np_val: colors[i] for i, np_val in enumerate(np_vals)}

    # --- Left: Error vs NEP ---
    for np_val in np_vals:
        sub = df[df["np"] == np_val].sort_values("NEP")
        ax1.plot(
            sub["NEP"], sub["error_2norm"],
            color=np_to_color[np_val], marker="o", linestyle="solid",
            linewidth=LINE_WIDTH, markersize=MARKER_SIZE, label=f"np={np_val}",
        )

    ax1.set_xlabel(r"特征对数量 ($N_{ep}$)", fontsize=LABEL_FONTSIZE)
    ax1.set_ylabel(r"相对误差 ($\epsilon_{ev}$)", fontsize=LABEL_FONTSIZE)
    ax1.set_yscale("log")
    ax1.yaxis.set_major_formatter(LogFormatterMathtext())
    ax1.tick_params(axis="both", which="major", labelsize=TICK_FONTSIZE, width=2, length=6)

    # --- Right: Error vs Total Time ---
    for np_val in np_vals:
        sub = df[df["np"] == np_val].sort_values("t_total")
        ax2.plot(
            sub["t_total"], sub["error_2norm"],
            color=np_to_color[np_val], marker="o", linestyle="solid",
            linewidth=LINE_WIDTH, markersize=MARKER_SIZE, label=f"np={np_val}",
        )

    ax2.set_xlabel("总计算时间 (秒)", fontsize=LABEL_FONTSIZE)
    ax2.set_yscale("log")
    ax2.yaxis.set_major_formatter(LogFormatterMathtext())
    ax2.tick_params(axis="both", which="major", labelsize=TICK_FONTSIZE, width=2, length=6)

    # Shared legend on top
    handles, labels = ax2.get_legend_handles_labels()
    fig.legend(
        handles=handles, labels=labels, ncol=len(handles),
        fontsize=LEGEND_FONTSIZE, loc="upper center",
        bbox_to_anchor=(0.5, 0.98), frameon=False,
        handletextpad=0.3, columnspacing=1.5,
    )

    plt.subplots_adjust(left=0.08, right=0.92, bottom=0.12, top=0.88, wspace=0.18)

    os.makedirs(TARGET_DIR, exist_ok=True)
    for ext in ["png", "pdf"]:
        path = os.path.join(TARGET_DIR, f"dragon_tet_performance.{ext}")
        plt.savefig(path, dpi=300, bbox_inches="tight")
        print(f"Saved: {path}")
    plt.close()


# ---------------------------------------------------------------------------
# 3. Plot 2: Time Breakdown Stacked Bar
# ---------------------------------------------------------------------------

def plot_breakdown(df):
    fig, ax = plt.subplots(figsize=(12, 6))

    for spine in ax.spines.values():
        spine.set_edgecolor(STYLE.ui_colors["spine"])
        spine.set_linewidth(1.5)
    ax.grid(False)

    nep_vals = sorted(df["NEP"].unique())
    np_vals = sorted(df["np"].unique())
    n_np = len(np_vals)
    bar_width = 0.25
    group_spacing = 0.6

    COMPONENT_MAP = {
        "子结构\n特征模态": STYLE.breakdown_colors.get("Substructure Eigenmodes", STYLE.ours),
        "界面\n模态": STYLE.breakdown_colors.get("Interface Modes", STYLE.method_colors.get("ours_nc", STYLE.cms)),
        "矩阵\n降维": STYLE.breakdown_colors.get("Matrix Reducing", STYLE.cms),
        "缩减\n求解": STYLE.breakdown_colors.get("Reduced Solve", STYLE.amls),
    }
    components = list(COMPONENT_MAP.keys())
    col_keys = ["t_sub", "t_ifc", "t_red_c", "t_red_s"]

    x_positions = []
    x_labels = []
    for i, nep in enumerate(nep_vals):
        base = i * (n_np * bar_width + group_spacing)
        for j, np_val in enumerate(np_vals):
            x_positions.append(base + j * bar_width)
        x_labels.append(base + (n_np - 1) * bar_width / 2)

    bottoms = np.zeros(len(x_positions))

    for comp_name, col_key in zip(components, col_keys):
        values = []
        for nep in nep_vals:
            for np_val in np_vals:
                row = df[(df["NEP"] == nep) & (df["np"] == np_val)]
                val = row[col_key].values[0] if not row.empty else 0.0
                values.append(val)
        ax.bar(
            x_positions, values, width=bar_width,
            label=comp_name, bottom=bottoms,
            color=COMPONENT_MAP[comp_name],
        )
        bottoms += np.array(values)

    ax.set_xlabel(r"特征对数量 ($N_{ep}$)", fontsize=LABEL_FONTSIZE)
    ax.set_ylabel("时间 (秒)", fontsize=LABEL_FONTSIZE)
    ax.set_xticks(x_labels)
    ax.set_xticklabels([str(n) for n in nep_vals], fontsize=TICK_FONTSIZE)
    ax.tick_params(axis="y", labelsize=TICK_FONTSIZE)

    ax.legend(loc="upper left", fontsize=LEGEND_FONTSIZE, frameon=False)

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15)

    os.makedirs(TARGET_DIR, exist_ok=True)
    for ext in ["png", "pdf"]:
        path = os.path.join(TARGET_DIR, f"dragon_tet_breakdown.{ext}")
        plt.savefig(path, dpi=300, bbox_inches="tight")
        print(f"Saved: {path}")
    plt.close()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print(f"Scanning logs in: {LOG_DIR}")
    df = extract_log_data(LOG_DIR)
    if df.empty:
        print(f"No data extracted from logs. Loading summary CSV: {SUMMARY_CSV}")
        df = pd.read_csv(SUMMARY_CSV)
    if df.empty:
        raise RuntimeError("No dragon_tet data available from logs or summary CSV.")

    print("\nExtracted data:")
    print(df.to_string(index=False))
    save_csv(df, os.path.join(THIS_DIR, "dragon_tet_summary_generated.csv"))

    print("\nGenerating performance plot...")
    plot_performance(df)

    print("\nGenerating breakdown plot...")
    plot_breakdown(df)

    print("\nAll done.")


if __name__ == "__main__":
    main()
