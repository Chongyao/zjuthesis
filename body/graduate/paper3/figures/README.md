# Plot Color Schemes

## Quick Start

Switch color scheme by setting the `PLOT_COLOR_SCHEME` environment variable:

```bash
# Single plot
PLOT_COLOR_SCHEME=viridis python figures/Schur-INTRD-ALFIM/plot.py

# All plots + compile PDF
PLOT_COLOR_SCHEME=purple_yellow ./generate_all_schemes.sh purple_yellow
```

## Available Schemes

| Scheme | Primary | Secondary | Style |
|--------|---------|-----------|-------|
| `blue_orange` | Blue | Orange | Professional, default |
| `viridis` | Purple | Yellow | Scientific, colorblind-safe |
| `purple_yellow` | Purple | Gold | Elegant |
| `teal_coral` | Teal | Coral | Fresh, modern |
| `macaron` | Sage | Peach | Soft, pastel |
| `warm_earth` | Brown | Burnt Orange | Earthy, warm |
| `bright_modern` | Blue | Orange | Vibrant, bold |

## Generate All Scheme PDFs

```bash
./generate_all_schemes.sh
```

Output: `paper-tog-{scheme}.pdf` for each scheme.

## Usage in Python Scripts

```python
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style_config import get_style, apply_style

SCHEME = os.environ.get('PLOT_COLOR_SCHEME', 'blue_orange')
STYLE = get_style(SCHEME)
apply_style(STYLE, scale='double_column')

# Use colors
ours_color = STYLE.method_colors['ours']
cms_color = STYLE.method_colors['cms']

# Use colormap for colorbars
cmap = STYLE.get_sequential_cmap()
```

## Configuration

Edit `figures/plot_style_config.py` to customize:
- `COLOR_SCHEMES`: Color definitions
- `gradient_colors`: Custom colormap colors (4-5 colors from scheme palette)
- `breakdown`: Pie chart / stacked bar colors
