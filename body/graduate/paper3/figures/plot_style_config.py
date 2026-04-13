"""
Unified plot style configuration for primal-dual paper figures.
Provides consistent colors, fonts, and style conventions across all matplotlib plots.

Usage:
    from plot_style_config import get_style, apply_style

    style = get_style('blue_orange')  # or 'purple_yellow', 'teal_coral'
    apply_style(style)

    # Access colors
    ours_color = style.method_colors['ours']
    cms_color = style.method_colors['cms']
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
import matplotlib.pyplot as plt
import matplotlib as mpl


# =============================================================================
# Color Scheme Definitions
# =============================================================================

COLOR_SCHEMES = {
    "blue_orange": {
        "primary": "#0173B2",
        "primary_light": "#56B4E9",
        "secondary": "#DE8F05",
        "tertiary": "#029E73",
        "quaternary": "#D55E00",
        "quinary": "#CC78BC",
        "senary": "#CA9161",
        "sequential": ["#C6DBEF", "#9ECAE1", "#6BAED6", "#3182BD", "#08519C"],
        "gradient_colors": ["#0173B2", "#029E73", "#F0E442", "#DE8F05"],
        "diverging": ["#D55E00", "#F0E442", "#009E73"],
        # For stacked bars: Serial (darker) vs Parallel (lighter)
        "serial": "#0173B2",
        "parallel": "#56B4E9",
        "serial_cms": "#DE8F05",
        "parallel_cms": "#FDBF6F",
        "efficiency_ours": "#CC3311",
        "efficiency_cms": "#882255",
        # Breakdown colors for pie charts and stacked bars (unified across scripts)
        "breakdown": {
            "Solve Eigenmodes": "#0173B2",  # Blue - main computation
            "Interface Modes (CMS)": "#DE8F05",  # Orange - CMS interface
            "SE-free Modes (Ours)": "#029E73",  # Green - our SE-free
            "Matrix-Reducing (Ours)": "#D55E00",  # Red-orange - our matrix reducing
            "Preprocessing of SE-free Modes (Ours)": "#56B4E9",  # Light blue
            "Postprocessing of SE-free Modes (Ours)": "#CC78BC",  # Pink
            "Preprocessing of Matrix-Reducing (Ours)": "#F0E442",  # Yellow
            "Postprocessing of Matrix-Reducing (Ours)": "#CA9161",  # Brown
            "Solve Reduced Eigenmodes (Ours)": "#9467BD",  # Purple
            "Solve Reduced Eigenmodes (CMS)": "#8C564B",  # Dark brown
            "Assemble Reduced Matrix (CMS)": "#BCBD22",  # Yellow-green
            # Aliases for local_update script
            "Substructure Eigenmodes": "#0173B2",
            "Interface Modes": "#DE8F05",
            "Matrix Reducing": "#D55E00",
            "Reduced Solve": "#9467BD",
            "Global Solve": "#8C564B",
        },
    },
    "purple_yellow": {
        "primary": "#7B2D8E",
        "primary_light": "#B57EDC",
        "secondary": "#F0C000",
        "tertiary": "#2E8B57",
        "quaternary": "#DC143C",
        "quinary": "#4169E1",
        "senary": "#8B4513",
        "sequential": ["#E8D4F0", "#C9A0DC", "#9B59B6", "#7B2D8E", "#4A0072"],
        "gradient_colors": ["#4A0072", "#7B2D8E", "#B57EDC", "#F0C000"],
        "diverging": ["#7B2D8E", "#F8F8F8", "#F0C000"],
        "serial": "#7B2D8E",
        "parallel": "#B57EDC",
        "serial_cms": "#F0C000",
        "parallel_cms": "#FFF3B0",
        "efficiency_ours": "#DC143C",
        "efficiency_cms": "#4169E1",
        "breakdown": {
            "Solve Eigenmodes": "#7B2D8E",
            "Interface Modes (CMS)": "#F0C000",
            "SE-free Modes (Ours)": "#2E8B57",
            "Matrix-Reducing (Ours)": "#DC143C",
            "Preprocessing of SE-free Modes (Ours)": "#B57EDC",
            "Postprocessing of SE-free Modes (Ours)": "#E377C2",
            "Preprocessing of Matrix-Reducing (Ours)": "#FFF3B0",
            "Postprocessing of Matrix-Reducing (Ours)": "#8B4513",
            "Solve Reduced Eigenmodes (Ours)": "#4169E1",
            "Solve Reduced Eigenmodes (CMS)": "#654321",
            "Assemble Reduced Matrix (CMS)": "#9ACD32",
            "Substructure Eigenmodes": "#7B2D8E",
            "Interface Modes": "#F0C000",
            "Matrix Reducing": "#DC143C",
            "Reduced Solve": "#4169E1",
            "Global Solve": "#654321",
        },
    },
    "teal_coral": {
        "primary": "#008080",
        "primary_light": "#4DB6AC",
        "secondary": "#FF6B6B",
        "tertiary": "#4ECDC4",
        "quaternary": "#FFE66D",
        "quinary": "#95E1D3",
        "senary": "#AA96DA",
        "sequential": ["#B2DFDB", "#80CBC4", "#4DB6AC", "#26A69A", "#00897B"],
        "gradient_colors": ["#008080", "#4ECDC4", "#FFE66D", "#FF6B6B"],
        "diverging": ["#FF6B6B", "#F8F8F8", "#008080"],
        "serial": "#008080",
        "parallel": "#4DB6AC",
        "serial_cms": "#FF6B6B",
        "parallel_cms": "#FFAB91",
        "efficiency_ours": "#FFE66D",
        "efficiency_cms": "#AA96DA",
        "breakdown": {
            "Solve Eigenmodes": "#008080",
            "Interface Modes (CMS)": "#FF6B6B",
            "SE-free Modes (Ours)": "#4ECDC4",
            "Matrix-Reducing (Ours)": "#FFE66D",
            "Preprocessing of SE-free Modes (Ours)": "#4DB6AC",
            "Postprocessing of SE-free Modes (Ours)": "#95E1D3",
            "Preprocessing of Matrix-Reducing (Ours)": "#FFAB91",
            "Postprocessing of Matrix-Reducing (Ours)": "#AA96DA",
            "Solve Reduced Eigenmodes (Ours)": "#B39DDB",
            "Solve Reduced Eigenmodes (CMS)": "#8D6E63",
            "Assemble Reduced Matrix (CMS)": "#AED581",
            "Substructure Eigenmodes": "#008080",
            "Interface Modes": "#FF6B6B",
            "Matrix Reducing": "#FFE66D",
            "Reduced Solve": "#B39DDB",
            "Global Solve": "#8D6E63",
        },
    },
    "viridis": {
        "primary": "#440154",
        "primary_light": "#7A0177",
        "secondary": "#FDE725",
        "tertiary": "#21918C",
        "quaternary": "#3B528B",
        "quinary": "#5DC863",
        "senary": "#B8DE29",
        "sequential": ["#440154", "#472D7B", "#3B528B", "#2C728E", "#21918C"],
        "gradient_colors": ["#440154", "#3B528B", "#21918C", "#5DC863", "#FDE725"],
        "diverging": ["#440154", "#21918C", "#FDE725"],
        "serial": "#440154",
        "parallel": "#7A0177",
        "serial_cms": "#FDE725",
        "parallel_cms": "#B8DE29",
        "efficiency_ours": "#5DC863",
        "efficiency_cms": "#3B528B",
        "breakdown": {
            "Solve Eigenmodes": "#440154",
            "Interface Modes (CMS)": "#FDE725",
            "SE-free Modes (Ours)": "#21918C",
            "Matrix-Reducing (Ours)": "#3B528B",
            "Preprocessing of SE-free Modes (Ours)": "#7A0177",
            "Postprocessing of SE-free Modes (Ours)": "#5DC863",
            "Preprocessing of Matrix-Reducing (Ours)": "#B8DE29",
            "Postprocessing of Matrix-Reducing (Ours)": "#2C728E",
            "Solve Reduced Eigenmodes (Ours)": "#472D7B",
            "Solve Reduced Eigenmodes (CMS)": "#1F968B",
            "Assemble Reduced Matrix (CMS)": "#73D055",
            "Substructure Eigenmodes": "#440154",
            "Interface Modes": "#FDE725",
            "Matrix Reducing": "#3B528B",
            "Reduced Solve": "#472D7B",
            "Global Solve": "#1F968B",
        },
    },
    "macaron": {
        "primary": "#7EB5A6",
        "primary_light": "#A8D5BA",
        "secondary": "#E8A87C",
        "tertiary": "#C5A3C8",
        "quaternary": "#F4B9B2",
        "quinary": "#95B8D1",
        "senary": "#DDA0DD",
        "sequential": ["#E8F5E9", "#C8E6C9", "#A5D6A7", "#81C784", "#66BB6A"],
        "gradient_colors": ["#95B8D1", "#7EB5A6", "#C5A3C8", "#E8A87C", "#F4B9B2"],
        "diverging": ["#E8A87C", "#F5F5F5", "#7EB5A6"],
        "serial": "#7EB5A6",
        "parallel": "#A8D5BA",
        "serial_cms": "#E8A87C",
        "parallel_cms": "#FFDAB9",
        "efficiency_ours": "#F4B9B2",
        "efficiency_cms": "#C5A3C8",
        "breakdown": {
            "Solve Eigenmodes": "#7EB5A6",
            "Interface Modes (CMS)": "#E8A87C",
            "SE-free Modes (Ours)": "#C5A3C8",
            "Matrix-Reducing (Ours)": "#F4B9B2",
            "Preprocessing of SE-free Modes (Ours)": "#A8D5BA",
            "Postprocessing of SE-free Modes (Ours)": "#95B8D1",
            "Preprocessing of Matrix-Reducing (Ours)": "#FFDAB9",
            "Postprocessing of Matrix-Reducing (Ours)": "#DDA0DD",
            "Solve Reduced Eigenmodes (Ours)": "#B4A7D6",
            "Solve Reduced Eigenmodes (CMS)": "#D7CCC8",
            "Assemble Reduced Matrix (CMS)": "#C5E1A5",
            "Substructure Eigenmodes": "#7EB5A6",
            "Interface Modes": "#E8A87C",
            "Matrix Reducing": "#F4B9B2",
            "Reduced Solve": "#B4A7D6",
            "Global Solve": "#D7CCC8",
        },
    },
    "warm_earth": {
        "primary": "#8B4513",  # Saddle brown (Ours) - earthy, warm
        "primary_light": "#CD853F",  # Peru (variant)
        "secondary": "#CC5500",  # Burnt orange (CMS)
        "tertiary": "#556B2F",  # Dark olive green
        "quaternary": "#B22222",  # Firebrick red
        "quinary": "#DAA520",  # Goldenrod
        "senary": "#6B4423",  # Dark brown
        "sequential": ["#FFF8DC", "#FAEBD7", "#DEB887", "#D2B48C", "#BC8F8F"],
        "gradient_colors": ["#6B4423", "#8B4513", "#CD853F", "#DAA520", "#CC5500"],
        "diverging": ["#CC5500", "#F5F5DC", "#8B4513"],
        "serial": "#8B4513",
        "parallel": "#CD853F",
        "serial_cms": "#CC5500",
        "parallel_cms": "#FFA07A",
        "efficiency_ours": "#B22222",
        "efficiency_cms": "#556B2F",
        "breakdown": {
            "Solve Eigenmodes": "#8B4513",
            "Interface Modes (CMS)": "#CC5500",
            "SE-free Modes (Ours)": "#556B2F",
            "Matrix-Reducing (Ours)": "#B22222",
            "Preprocessing of SE-free Modes (Ours)": "#CD853F",
            "Postprocessing of SE-free Modes (Ours)": "#DAA520",
            "Preprocessing of Matrix-Reducing (Ours)": "#FFA07A",
            "Postprocessing of Matrix-Reducing (Ours)": "#6B4423",
            "Solve Reduced Eigenmodes (Ours)": "#A0522D",
            "Solve Reduced Eigenmodes (CMS)": "#8B7355",
            "Assemble Reduced Matrix (CMS)": "#9ACD32",
            "Substructure Eigenmodes": "#8B4513",
            "Interface Modes": "#CC5500",
            "Matrix Reducing": "#B22222",
            "Reduced Solve": "#A0522D",
            "Global Solve": "#8B7355",
        },
    },
    "bright_modern": {
        "primary": "#2196F3",  # Bright blue (Ours) - modern, vibrant
        "primary_light": "#64B5F6",  # Light blue (variant)
        "secondary": "#FF9800",  # Bright orange (CMS)
        "tertiary": "#4CAF50",  # Green
        "quaternary": "#E91E63",  # Pink
        "quinary": "#9C27B0",  # Purple
        "senary": "#00BCD4",  # Cyan
        "sequential": ["#BBDEFB", "#90CAF9", "#64B5F6", "#42A5F5", "#2196F3"],
        "gradient_colors": ["#2196F3", "#00BCD4", "#4CAF50", "#FF9800", "#E91E63"],
        "diverging": ["#FF9800", "#FAFAFA", "#2196F3"],
        "serial": "#2196F3",
        "parallel": "#64B5F6",
        "serial_cms": "#FF9800",
        "parallel_cms": "#FFCC80",
        "efficiency_ours": "#E91E63",
        "efficiency_cms": "#9C27B0",
        "breakdown": {
            "Solve Eigenmodes": "#2196F3",
            "Interface Modes (CMS)": "#FF9800",
            "SE-free Modes (Ours)": "#4CAF50",
            "Matrix-Reducing (Ours)": "#E91E63",
            "Preprocessing of SE-free Modes (Ours)": "#64B5F6",
            "Postprocessing of SE-free Modes (Ours)": "#00BCD4",
            "Preprocessing of Matrix-Reducing (Ours)": "#FFCC80",
            "Postprocessing of Matrix-Reducing (Ours)": "#9C27B0",
            "Solve Reduced Eigenmodes (Ours)": "#7E57C2",
            "Solve Reduced Eigenmodes (CMS)": "#795548",
            "Assemble Reduced Matrix (CMS)": "#8BC34A",
            "Substructure Eigenmodes": "#2196F3",
            "Interface Modes": "#FF9800",
            "Matrix Reducing": "#E91E63",
            "Reduced Solve": "#7E57C2",
            "Global Solve": "#795548",
        },
    },
}


# =============================================================================
# Method Style Definitions (consistent across all figures)
# =============================================================================

METHOD_STYLES = {
    "ours": {
        "marker": "o",
        "linestyle": "-",
        "linewidth": 2.5,
        "markersize": 8,
        "alpha": 1.0,
        "label": "Ours",
        "label_short": "Ours",
    },
    "ours_nc": {
        "marker": "o",
        "linestyle": "--",
        "linewidth": 2.5,
        "markersize": 8,
        "alpha": 0.85,
        "label": "PD-NC",
        "label_short": "PD-NC",
    },
    "cms": {
        "marker": "s",
        "linestyle": "--",
        "linewidth": 2.5,
        "markersize": 8,
        "alpha": 0.85,
        "label": "CB-CMS",
        "label_short": "CB-CMS",
    },
    "amls": {
        "marker": "^",
        "linestyle": ":",
        "linewidth": 2.5,
        "markersize": 8,
        "alpha": 1.0,
        "label": "AMLS",
        "label_short": "AMLS",
    },
    "imr": {
        "marker": "d",
        "linestyle": "-.",
        "linewidth": 2.5,
        "markersize": 8,
        "alpha": 1.0,
        "label": "CMS-IMR",
        "label_short": "CMS-IMR",
    },
    "schur_imr": {
        "marker": "v",
        "linestyle": "-",
        "linewidth": 2.5,
        "markersize": 8,
        "alpha": 1.0,
        "label": "Schur and Eigen-free IMR",
        "label_short": "Schur-IMR",
    },
    "spectra": {
        "marker": "x",
        "linestyle": ":",
        "linewidth": 2.5,
        "markersize": 8,
        "alpha": 0.85,
        "label": "Spectra",
        "label_short": "Spectra",
    },
}

# Metric styles (for distinguishing serial/parallel, time/memory, etc.)
METRIC_STYLES = {
    "serial": {"linestyle": "-", "marker_suffix": ""},
    "parallel": {"linestyle": "--", "marker_suffix": ""},
    "time": {"linestyle": "-", "marker_suffix": ""},
    "memory": {"linestyle": "--", "marker_suffix": ""},
    "efficiency": {"linestyle": ":", "marker_suffix": ""},
}


# =============================================================================
# Font Configuration
# =============================================================================

FONT_CONFIG = {
    "family": ["Source Han Sans CN", "Times New Roman"],
    "fallback": "serif",
    "mathtext": "stix",
    "title": 16,
    "label": 14,
    "legend": 12,
    "tick": 12,
    "annotation": 11,
    "scale_single_column": 1.6,
    "scale_double_column": 1.6,
    "scale_half_width": 1.8,
}


# =============================================================================
# Style Class
# =============================================================================


@dataclass
class PlotStyle:
    """Container for all style settings."""

    scheme_name: str
    colors: Dict
    methods: Dict = field(default_factory=lambda: METHOD_STYLES.copy())
    metrics: Dict = field(default_factory=lambda: METRIC_STYLES.copy())
    fonts: Dict = field(default_factory=lambda: FONT_CONFIG.copy())

    @property
    def method_colors(self) -> Dict[str, str]:
        """Get method -> color mapping."""
        return {
            "ours": self.colors["primary"],
            "ours_nc": self.colors.get("primary_light", "#56B4E9"),
            "cms": self.colors["secondary"],
            "amls": self.colors["tertiary"],
            "imr": self.colors["quaternary"],
            "schur_imr": self.colors["quinary"],
            "spectra": self.colors.get("senary", "#CA9161"),
        }

    @property
    def ours(self) -> str:
        return self.colors["primary"]

    @property
    def cms(self) -> str:
        return self.colors["secondary"]

    @property
    def amls(self) -> str:
        return self.colors["tertiary"]

    def get_method_style(self, method: str, metric: str = None) -> Dict:
        """Get complete style dict for a method, optionally modified by metric."""
        style = self.methods.get(method, self.methods["ours"]).copy()
        style["color"] = self.method_colors.get(method, self.colors["primary"])

        if metric and metric in self.metrics:
            style["linestyle"] = self.metrics[metric]["linestyle"]

        return style

    def get_sequential_colors(self, n: int) -> List[str]:
        """Get n colors from sequential palette."""
        seq = self.colors["sequential"]
        if n <= len(seq):
            step = len(seq) // n
            return [seq[i * step] for i in range(n)]
        # Interpolate if need more colors
        import numpy as np
        from matplotlib.colors import LinearSegmentedColormap

        cmap = LinearSegmentedColormap.from_list("seq", seq, N=n)
        return [mpl.colors.rgb2hex(cmap(i / (n - 1))) for i in range(n)]

    def scaled_fontsize(self, base_key: str, scale: str = "single_column") -> float:
        """Get scaled font size."""
        base = self.fonts.get(base_key, 12)
        scale_factor = self.fonts.get(f"scale_{scale}", 1.0)
        return base * scale_factor

    def get_sequential_cmap(self):
        from matplotlib.colors import LinearSegmentedColormap

        gradient = self.colors.get("gradient_colors")
        if gradient:
            return LinearSegmentedColormap.from_list("custom_gradient", gradient, N=256)
        seq = self.colors["sequential"]
        return LinearSegmentedColormap.from_list("seq_cmap", seq)

    def get_secondary_cmap(self):
        """Get secondary colormap for contrast data (e.g., Oranges replacement)."""
        from matplotlib.colors import LinearSegmentedColormap

        base = self.colors["secondary"]
        # Generate gradient from light to the secondary color
        import matplotlib.colors as mcolors

        rgb = mcolors.to_rgb(base)
        light = tuple(min(1.0, c + 0.7 * (1 - c)) for c in rgb)
        light_hex = mcolors.to_hex(light)
        return LinearSegmentedColormap.from_list("sec_cmap", [light_hex, base])

    @property
    def ui_colors(self) -> Dict[str, str]:
        """Get UI element colors (spines, backgrounds, etc.)."""
        return {
            "spine": "#000000",
            "text_secondary": "#555555",
            "marker_edge": "#FFFFFF",
            "legend_bg": "#FFFFFF",
            "reference_line": "#808080",
            "annotation_bg": "#FFFFFF",
            "highlight": self.colors.get("primary_light", "#56B4E9"),
            "accent": self.colors.get("quaternary", "#D55E00"),
        }

    @property
    def efficiency_colors(self) -> Dict[str, str]:
        """Get efficiency curve colors."""
        return {
            "ours": self.colors.get("quaternary", "#CC3311"),
            "cms": self.colors.get("quinary", "#882255"),
        }

    @property
    def breakdown_colors(self) -> Dict[str, str]:
        """Get breakdown colors for pie charts and stacked bars."""
        return self.colors.get("breakdown", {})


def get_style(scheme: str = "blue_orange") -> PlotStyle:
    """Get a PlotStyle instance for the given color scheme."""
    if scheme not in COLOR_SCHEMES:
        raise ValueError(
            f"Unknown scheme: {scheme}. Available: {list(COLOR_SCHEMES.keys())}"
        )
    return PlotStyle(scheme_name=scheme, colors=COLOR_SCHEMES[scheme])


def apply_style(style: PlotStyle, scale: str = "single_column"):
    """Apply style settings to matplotlib rcParams."""
    # Font settings
    try:
        plt.rcParams["font.family"] = style.fonts["family"]
    except:
        plt.rcParams["font.family"] = style.fonts["fallback"]

    plt.rcParams["mathtext.fontset"] = style.fonts["mathtext"]
    plt.rcParams["axes.unicode_minus"] = False

    # Font sizes (scaled)
    plt.rcParams["axes.titlesize"] = style.scaled_fontsize("title", scale)
    plt.rcParams["axes.labelsize"] = style.scaled_fontsize("label", scale)
    plt.rcParams["legend.fontsize"] = style.scaled_fontsize("legend", scale)
    plt.rcParams["xtick.labelsize"] = style.scaled_fontsize("tick", scale)
    plt.rcParams["ytick.labelsize"] = style.scaled_fontsize("tick", scale)

    # Line and marker defaults
    plt.rcParams["lines.linewidth"] = 2.5
    plt.rcParams["lines.markersize"] = 8

    # Grid and spines
    plt.rcParams["axes.grid"] = False
    plt.rcParams["axes.spines.top"] = True
    plt.rcParams["axes.spines.right"] = True
    plt.rcParams["axes.linewidth"] = 1.2

    # Figure defaults
    plt.rcParams["figure.dpi"] = 150
    plt.rcParams["savefig.dpi"] = 300
    plt.rcParams["savefig.bbox"] = "tight"
    plt.rcParams["savefig.pad_inches"] = 0.05


def apply_spines(ax, color="black", linewidth=1.2):
    """Apply consistent spine styling to an axis."""
    for spine in ax.spines.values():
        spine.set_edgecolor(color)
        spine.set_linewidth(linewidth)


# =============================================================================
# Convenience Functions
# =============================================================================


def get_method_color(method: str, scheme: str = "blue_orange") -> str:
    """Quick access to method color."""
    style = get_style(scheme)
    return style.method_colors.get(method, style.colors["primary"])


def get_comparison_colors(methods: List[str], scheme: str = "blue_orange") -> List[str]:
    """Get colors for a list of methods."""
    style = get_style(scheme)
    return [style.method_colors.get(m, style.colors["primary"]) for m in methods]


def plot_method_line(
    ax, x, y, method: str, style: PlotStyle, metric: str = None, **kwargs
):
    """Plot a line with consistent method styling."""
    method_style = style.get_method_style(method, metric)
    # Allow kwargs to override
    method_style.update(kwargs)
    return ax.plot(x, y, **method_style)


# =============================================================================
# Color scheme preview (for testing)
# =============================================================================


def preview_schemes():
    """Generate a preview of all color schemes."""
    import numpy as np

    fig, axes = plt.subplots(
        len(COLOR_SCHEMES), 1, figsize=(12, 3 * len(COLOR_SCHEMES))
    )
    if len(COLOR_SCHEMES) == 1:
        axes = [axes]

    x = np.linspace(0, 10, 50)

    for ax, (name, colors) in zip(axes, COLOR_SCHEMES.items()):
        style = get_style(name)
        apply_style(style)

        for i, (method, method_style) in enumerate(METHOD_STYLES.items()):
            y = np.sin(x + i * 0.5) + i * 0.3
            full_style = style.get_method_style(method)
            ax.plot(
                x,
                y,
                label=method_style["label"],
                **{k: v for k, v in full_style.items() if k != "label"},
            )

        ax.set_title(f"Color Scheme: {name}")
        ax.legend(loc="upper right", ncol=len(METHOD_STYLES))
        ax.set_xlim(0, 10)

    plt.tight_layout()
    plt.savefig("color_scheme_preview.png", dpi=150)
    plt.close()
    print("Saved: color_scheme_preview.png")


# =============================================================================
# ParaView Colormap Integration
# =============================================================================


def hex_to_rgb(hex_color: str) -> tuple:
    """Convert hex color to RGB tuple (0-1 range)."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) / 255.0 for i in (0, 2, 4))


def get_paraview_rgb_points(
    scheme: str = "blue_orange",
    data_min: float = 0.0,
    data_max: float = 1.0,
    colormap_type: str = "eigenvec",
) -> List[float]:
    """
    Generate ParaView RGBPoints from plot_style_config gradient colors.

    Args:
        scheme: Color scheme name (e.g., 'blue_orange', 'viridis')
        data_min: Minimum data value for the colormap
        data_max: Maximum data value for the colormap
        colormap_type: 'eigenvec' for sequential gradient, 'partition' for discrete

    Returns:
        List of floats in ParaView RGBPoints format: [val, r, g, b, val, r, g, b, ...]

    Usage in ParaView:
        from plot_style_config import get_paraview_rgb_points
        lut = GetColorTransferFunction(field_name)
        lut.RGBPoints = get_paraview_rgb_points('blue_orange', data_min, data_max)
    """
    style = get_style(scheme)
    gradient = style.colors.get("gradient_colors", style.colors["sequential"])

    rgb_points = []
    n_colors = len(gradient)

    for i, hex_color in enumerate(gradient):
        # Linearly interpolate data value
        t = i / (n_colors - 1) if n_colors > 1 else 0.5
        val = data_min + t * (data_max - data_min)
        r, g, b = hex_to_rgb(hex_color)
        rgb_points.extend([val, r, g, b])

    return rgb_points


def get_paraview_partition_colors(
    scheme: str = "blue_orange", n_partitions: int = 8
) -> List[float]:
    """
    Generate ParaView RGBPoints for discrete partition coloring.

    Args:
        scheme: Color scheme name
        n_partitions: Number of partitions to color

    Returns:
        List of floats in ParaView RGBPoints format
    """
    style = get_style(scheme)

    # Use method colors for first few partitions, then cycle gradient
    base_colors = [
        style.method_colors["ours"],
        style.method_colors["cms"],
        style.method_colors["amls"],
        style.method_colors["imr"],
        style.method_colors["schur_imr"],
        style.method_colors["spectra"],
    ]

    # Extend with gradient colors if needed
    gradient = style.colors.get("gradient_colors", style.colors["sequential"])
    all_colors = base_colors + gradient

    rgb_points = []
    for i in range(n_partitions):
        color_idx = i % len(all_colors)
        r, g, b = hex_to_rgb(all_colors[color_idx])
        rgb_points.extend([float(i), r, g, b])

    return rgb_points


def apply_paraview_colormap(
    lut, scheme: str = "blue_orange", data_min: float = 0.0, data_max: float = 1.0
):
    """
    Apply custom colormap to a ParaView LookupTable.

    Args:
        lut: ParaView ColorTransferFunction (from GetColorTransferFunction)
        scheme: Color scheme name
        data_min: Minimum data value
        data_max: Maximum data value

    Usage in ParaView script:
        from plot_style_config import apply_paraview_colormap
        lut = GetColorTransferFunction(field_name)
        apply_paraview_colormap(lut, 'blue_orange', 0, max_val)
    """
    rgb_points = get_paraview_rgb_points(scheme, data_min, data_max)
    lut.RGBPoints = rgb_points
    lut.ColorSpace = "Lab"  # Better perceptual interpolation


if __name__ == "__main__":
    preview_schemes()
