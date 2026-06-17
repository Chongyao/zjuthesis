"""
Unified thesis figure configuration — single source of truth for all matplotlib figures.

Usage:
    from thesis_figure_config import setup_figure_fonts, LABEL_SIZE, TICK_SIZE

    setup_figure_fonts()
    ax.set_xlabel("...", fontsize=LABEL_SIZE)
    ax.tick_params(labelsize=TICK_SIZE)

Font size rationale:
    Thesis body text: 12pt (ctexrep, 12pt option).
    Figures are embedded at width=0.8-1.0\\linewidth (~310-390 pt).
    matplotlib figures are typically 12-14 inches wide at 300 dpi.
    Scale factor = embed_width / (fig_width_inches × 72) ≈ 0.3-0.45.

    To produce effective 7-9pt labels (smaller than body, readable in print):
        matplotlib_label_size × scale = target_effective
        22.4 × 0.39 = 8.7pt (for 14in fig at 100% linewidth)
        22.4 × 0.31 = 7.0pt (for 14in fig at 80% linewidth)
"""

import matplotlib.pyplot as plt
from matplotlib import font_manager

# ---------------------------------------------------------------------------
# Font sizes (in matplotlib points — will be scaled down ~0.3-0.45× in PDF)
# ---------------------------------------------------------------------------
TITLE_SIZE  = 25.6   # effective ~10pt
LABEL_SIZE  = 22.4   # effective ~7-9pt
LEGEND_SIZE = 19.2   # effective ~6-7pt
TICK_SIZE   = 19.2   # effective ~6-7pt

# ---------------------------------------------------------------------------
# Figure dimensions
# ---------------------------------------------------------------------------
DPI = 300
LINE_WIDTH  = 3.0
MARKER_SIZE = 10

# ---------------------------------------------------------------------------
# CJK font fallback chain
# ---------------------------------------------------------------------------
CJK_FONT_CANDIDATES = [
    "Noto Sans CJK SC",
    "Source Han Sans CN",
    "WenQuanYi Micro Hei",
    "Microsoft YaHei",
    "SimHei",
]


def _pick_cjk_font() -> str:
    """Return the first available CJK font, or the first candidate as fallback."""
    available = {f.name for f in font_manager.fontManager.ttflist}
    for name in CJK_FONT_CANDIDATES:
        if name in available:
            return name
    return CJK_FONT_CANDIDATES[0]


def setup_figure_fonts() -> str:
    """Configure matplotlib for CJK-capable, print-ready figure output.

    Returns the name of the selected CJK font.
    """
    chosen = _pick_cjk_font()

    plt.rcParams["font.family"]       = [chosen, "Times New Roman", "DejaVu Sans"]
    plt.rcParams["font.sans-serif"]   = CJK_FONT_CANDIDATES + ["DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False
    plt.rcParams["mathtext.fontset"]  = "stix"

    # Sizes (consistent across all labels, legends, ticks)
    plt.rcParams["axes.titlesize"]    = TITLE_SIZE
    plt.rcParams["axes.labelsize"]    = LABEL_SIZE
    plt.rcParams["legend.fontsize"]   = LEGEND_SIZE
    plt.rcParams["xtick.labelsize"]   = TICK_SIZE
    plt.rcParams["ytick.labelsize"]   = TICK_SIZE

    # PDF embedding
    plt.rcParams["pdf.fonttype"]      = 42
    plt.rcParams["ps.fonttype"]       = 42

    # Line / marker defaults
    plt.rcParams["lines.linewidth"]   = LINE_WIDTH
    plt.rcParams["lines.markersize"]  = MARKER_SIZE

    # Figure defaults
    plt.rcParams["figure.dpi"]        = 150
    plt.rcParams["savefig.dpi"]       = DPI
    plt.rcParams["savefig.bbox"]      = "tight"
    plt.rcParams["savefig.pad_inches"] = 0.05

    print(f"[thesis_figure_config] CJK font: {chosen}")
    return chosen
