"""draw_nev_time.py
绘制 PD / CMS / IMR (CMS+) / AMLS 的时间随 nev 变化曲线。
统一样式、字体、线宽与 marker 设置，使用统一配色方案。
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
import os
import sys

# Import unified style config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style_config import get_style, apply_style

SCHEME = os.environ.get('PLOT_COLOR_SCHEME', 'teal_coral')
STYLE = get_style(SCHEME)
apply_style(STYLE, scale="double_column")

# Get colors from unified config
OURS_COLOR = STYLE.ours
CMS_COLOR = STYLE.cms
AMLS_COLOR = STYLE.method_colors["amls"]
IMR_COLOR = STYLE.method_colors["imr"]

SCALE = 1
FIG_SIZE = (11 * SCALE, 6 * SCALE)
DPI = 300
LABEL_FONTSIZE = STYLE.scaled_fontsize("label", "double_column")
LEGEND_FONTSIZE = STYLE.scaled_fontsize("legend", "double_column")
TICK_FONTSIZE = STYLE.scaled_fontsize("tick", "double_column")
LINE_WIDTH = 3.0
MARKER_SIZE = 12

# ================= 2. 加载与预处理数据 =================
csv_file = "nev-time-new.csv"
if not os.path.exists(csv_file):
    print(f"错误: 找不到文件 {csv_file}")
    exit()

# 假定列顺序: algorithm, nev, time
df = pd.read_csv(csv_file, usecols=[0, 1, 2])
df.columns = ["algorithm", "nev", "time"]  # 强制重命名列以防万一

# 清洗数据
df = df.dropna(subset=["algorithm", "nev", "time"])
df["nev"] = pd.to_numeric(df["nev"], errors="coerce")
df["time"] = pd.to_numeric(df["time"], errors="coerce")
df = df.dropna(subset=["nev", "time"])

# 提取各算法数据
pd_df = df[df["algorithm"] == "PD"].sort_values("nev")
cms_df = df[df["algorithm"] == "CMS"].sort_values("nev")
cms_plus_df = df[df["algorithm"] == "CMSINTRD"].sort_values("nev")  # CMS+
amls_df_all = df[df["algorithm"] == "AMLS"].sort_values("nev")
amls_df_dedup = (
    df[df["algorithm"] == "AMLS"]
    .loc[df[df["algorithm"] == "AMLS"].groupby("nev")["time"].idxmin()]
    .sort_values("nev")
)


def plot_scatter_with_fit(ax, x, y, color, label, marker="o", degree=2, sample_step=1):
    if len(x) == 0:
        return
    x_plot = x[::sample_step]
    y_plot = y[::sample_step]
    ax.scatter(
        x_plot,
        y_plot,
        marker=marker,
        s=MARKER_SIZE**2,
        color=color,
        alpha=0.6,
        label=label,
    )
    if len(x) >= degree + 1:
        z = np.polyfit(x, y, degree)
        p = np.poly1d(z)
        x_smooth = np.linspace(x.min(), x.max(), 200)
        ax.plot(
            x_smooth,
            p(x_smooth),
            linestyle="-",
            linewidth=LINE_WIDTH,
            color=color,
            alpha=0.9,
        )


def create_plot(amls_df, sample_step, suffix):
    fig, ax = plt.subplots(figsize=FIG_SIZE, dpi=DPI)

    plot_scatter_with_fit(
        ax, cms_df["nev"].values, cms_df["time"].values, CMS_COLOR, "CB-CMS", marker="o"
    )
    plot_scatter_with_fit(
        ax,
        amls_df["nev"].values,
        amls_df["time"].values,
        AMLS_COLOR,
        "AMLS",
        marker="o",
        sample_step=sample_step,
    )
    plot_scatter_with_fit(
        ax,
        cms_plus_df["nev"].values,
        cms_plus_df["time"].values,
        IMR_COLOR,
        "CMS-IMR",
        marker="o",
    )
    plot_scatter_with_fit(
        ax, pd_df["nev"].values, pd_df["time"].values, OURS_COLOR, "本文方法", marker="o"
    )

    ax.set_xlabel(r"特征值数量 ($n_{ev}$)", fontsize=LABEL_FONTSIZE)
    ax.set_ylabel("时间 (s)", fontsize=LABEL_FONTSIZE)
    ax.tick_params(axis="both", which="major", labelsize=TICK_FONTSIZE)
    ax.grid(False)
    ax.legend(fontsize=LEGEND_FONTSIZE, frameon=False, loc="best")
    for spine in ax.spines.values():
        spine.set_edgecolor(STYLE.ui_colors["spine"])
        spine.set_linewidth(1.5)

    if os.path.isfile(MODEL_IMG):
        try:
            try:
                from PIL import Image

                pil_img = Image.open(MODEL_IMG)
                pil_img = pil_img.rotate(15, expand=True, resample=Image.BICUBIC)
                img = np.array(pil_img)
            except Exception:
                img = plt.imread(MODEL_IMG)
            oi = OffsetImage(img, zoom=0.22)
            ab = AnnotationBbox(
                oi, (0.4, 0.6), xycoords="axes fraction", frameon=False, pad=0.0
            )
            ax.add_artist(ab)
        except Exception:
            pass

    fig.tight_layout()
    fig.savefig(f"nev_vs_time_plot_{suffix}.png", dpi=DPI, bbox_inches="tight")
    fig.savefig(f"nev_vs_time_plot_{suffix}.pdf", dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    return f"nev_vs_time_plot_{suffix}.png", f"nev_vs_time_plot_{suffix}.pdf"


MODEL_IMG = "model.png"

png1, pdf1 = create_plot(amls_df_dedup, sample_step=5, suffix="sparse")
png2, pdf2 = create_plot(amls_df_all, sample_step=1, suffix="all")

print(f"绘图完成！已保存: {png1}, {pdf1}, {png2}, {pdf2}")
