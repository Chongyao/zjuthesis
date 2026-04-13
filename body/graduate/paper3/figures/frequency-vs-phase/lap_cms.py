import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib import cm
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style_config import get_style, apply_style

SCHEME = os.environ.get('PLOT_COLOR_SCHEME', 'teal_coral')
STYLE = get_style(SCHEME)
apply_style(STYLE, scale='double_column')

# 定义字体大小
TITLE_FONTSIZE = STYLE.scaled_fontsize('title', 'double_column')
LABEL_FONTSIZE = STYLE.scaled_fontsize('label', 'double_column')
LEGEND_FONTSIZE = STYLE.scaled_fontsize('legend', 'double_column')
TICK_FONTSIZE = STYLE.scaled_fontsize('tick', 'double_column')
DPI = 150
LINE_WIDTH = 2
MARKER_SIZE = 12

# --- 1. Parameter Definitions ---
L = 10.0
max_n_global = 8  # Y-axis of heatmap
max_M = 12  # X-axis of heatmap

# Substructure window parameters
l = 2  # Length of the sliding window

# File paths for caching
CACHE_DIR = "error_cache"
FREQ_CACHE_FILE = os.path.join(
    CACHE_DIR, f"freq_L{L}_l{l}_n{max_n_global}_m{max_M}.npy"
)
PHASE_CACHE_FILE = os.path.join(
    CACHE_DIR, f"phase_L{L}_l{l}_n{max_n_global}_m{max_M}.npy"
)

# --- 2. Function Definitions ---


def target_function(x, L, n):
    return np.sin(n * np.pi * x / L)


def get_frequency_basis(a, b, M):
    basis = []
    for m in range(1, M + 1):
        basis.append(lambda x, m=m: np.sin(m * np.pi * (x - a) / (b - a)))
    basis.append(lambda x: (b - x) / (b - a))
    basis.append(lambda x: (x - a) / (b - a))
    return basis


def get_phase_adapted_basis(a, b, M):
    basis = []
    num_pairs = M // 2
    for m in range(1, num_pairs + 1):
        basis.append(lambda x, m=m: np.sin(m * np.pi * (x - a) / (b - a)))
        basis.append(lambda x, m=m: np.cos(m * np.pi * (x - a) / (b - a)))
    if M % 2 != 0:
        m = num_pairs + 1
        basis.append(lambda x, m=m: np.sin(m * np.pi * (x - a) / (b - a)))
    basis.append(lambda x: (b - x) / (b - a))
    basis.append(lambda x: (x - a) / (b - a))
    return basis


def _compute_error_for_interval(target_func, basis_funcs, a, b):
    num_basis = len(basis_funcs)
    G = np.zeros((num_basis, num_basis))
    F = np.zeros(num_basis)
    for i in range(num_basis):
        integrand_F = lambda x: target_func(x) * basis_funcs[i](x)
        F[i] = integrate.quad(integrand_F, a, b)[0]
        for j in range(i, num_basis):
            integrand_G = lambda x: basis_funcs[i](x) * basis_funcs[j](x)
            G[i, j] = integrate.quad(integrand_G, a, b)[0]
            G[j, i] = G[i, j]
    try:
        coeffs = np.linalg.solve(G, F)
    except np.linalg.LinAlgError:
        return (
            np.inf
        )  # Return infinite error if matrix is singular (bad basis or interval)

    def approximated_func(x):
        return sum(coeffs[i] * basis_funcs[i](x) for i in range(num_basis))

    error_integrand = lambda x: (target_func(x) - approximated_func(x)) ** 2
    return np.sqrt(integrate.quad(error_integrand, a, b)[0])


def calculate_integrated_error(n_global, M, basis_generator, L, l):
    target_func_instance = lambda x: target_function(x, L, n_global)

    def error_at_position_a(a):
        b = a + l
        basis = basis_generator(a, b, M)
        return _compute_error_for_interval(target_func_instance, basis, a, b)

    # Integrate this error function over all possible window positions
    total_integrated_error, _ = integrate.quad(error_at_position_a, 0, L - l, limit=200)

    # Return the average error
    return total_integrated_error / (L - l)


# --- 3. Generate Integrated Error Grids with Caching ---
m_values = np.arange(1, max_M + 1)
n_global_values = np.arange(1, max_n_global + 1)

# Create cache directory if it doesn't exist
os.makedirs(CACHE_DIR, exist_ok=True)

# Check if cached data exists
if os.path.exists(FREQ_CACHE_FILE) and os.path.exists(PHASE_CACHE_FILE):
    print("--- Loading cached error grids ---")
    errors_grid_freq = np.load(FREQ_CACHE_FILE)
    errors_grid_phase = np.load(PHASE_CACHE_FILE)
    # Basic check to ensure loaded data matches current parameters
    if not (
        errors_grid_freq.shape == (len(m_values), len(n_global_values))
        and errors_grid_phase.shape == (len(m_values), len(n_global_values))
    ):
        print("Cached data shape mismatch. Recalculating...")
        recalculate = True
    else:
        recalculate = False
else:
    recalculate = True

if recalculate:
    errors_grid_freq = np.zeros((len(m_values), len(n_global_values)))
    errors_grid_phase = np.zeros((len(m_values), len(n_global_values)))
    print("--- Calculating Integrated Error Grids (this may take a moment) ---")
    for j, n_global in enumerate(n_global_values):
        for i, m_current in enumerate(m_values):
            # Method A: Frequency-Adapted
            errors_grid_freq[i, j] = calculate_integrated_error(
                n_global, m_current, get_frequency_basis, L, l
            )

            # Method B: Phase-Adapted
            errors_grid_phase[i, j] = calculate_integrated_error(
                n_global, m_current, get_phase_adapted_basis, L, l
            )

        print(f"Completed calculations for global mode n = {n_global}")

    # Save computed grids to cache
    np.save(FREQ_CACHE_FILE, errors_grid_freq)
    np.save(PHASE_CACHE_FILE, errors_grid_phase)
    print("--- Error grids saved to cache ---")

# --- 4. Plotting Side-by-Side Heatmaps with Ratio ---

fig, axes = plt.subplots(1, 3, figsize=(20, 6), sharey=True)

# Define shared color scale
z_min = np.min(errors_grid_phase[errors_grid_phase > 0])  # Smallest non-zero error
z_max = np.max(errors_grid_freq)
norm = LogNorm(vmin=max(z_min, 1e-16), vmax=z_max)

# Calculate ratio grid, handle division by zero/very small numbers
ratio_grid = errors_grid_freq / np.maximum(errors_grid_phase, 1e-16)

# --- Plot 1: Frequency-Adapted Heatmap ---
im1 = axes[0].imshow(
    errors_grid_freq.T,
    cmap=STYLE.get_sequential_cmap(),
    norm=norm,
    origin="lower",
    extent=[
        min(m_values) - 0.5,
        max(m_values) + 0.5,
        min(n_global_values) - 0.5,
        max(n_global_values) + 0.5,
    ],
    aspect="auto",
)
axes[0].set_title("使用固定相位基\n的误差", fontsize=TITLE_FONTSIZE)
axes[0].set_xlabel("")  # 使用共享 X 轴标签
axes[0].set_ylabel("全局模态阶数", fontsize=LABEL_FONTSIZE)
axes[0].set_xticks(m_values[::2])
axes[0].set_yticks(n_global_values)
axes[0].tick_params(labelsize=TICK_FONTSIZE)
axes[0].grid(False)

# --- Plot 2: Phase-Adapted Heatmap ---
im2 = axes[1].imshow(
    errors_grid_phase.T,
    cmap=STYLE.get_sequential_cmap(),
    norm=norm,
    origin="lower",
    extent=[
        min(m_values) - 0.5,
        max(m_values) + 0.5,
        min(n_global_values) - 0.5,
        max(n_global_values) + 0.5,
    ],
    aspect="auto",
)
axes[1].set_title("使用完整相位基\n的误差", fontsize=TITLE_FONTSIZE)
axes[1].set_xlabel("")  # 使用共享 X 轴标签
axes[1].set_xticks(m_values[::2])
axes[1].set_yticks(n_global_values)
axes[1].grid(False)
axes[1].tick_params(labelsize=TICK_FONTSIZE)

# --- Plot 3: Ratio Heatmap ---
ratio_norm = LogNorm(vmin=1, vmax=ratio_grid.max())
im3 = axes[2].imshow(
    ratio_grid.T,
    cmap=STYLE.get_secondary_cmap(),
    norm=ratio_norm,
    origin="lower",
    extent=[
        min(m_values) - 0.5,
        max(m_values) + 0.5,
        min(n_global_values) - 0.5,
        max(n_global_values) + 0.5,
    ],
    aspect="auto",
)
axes[2].grid(False)
axes[2].set_title("改进因子 \n (比值: 固定/完整)", fontsize=TITLE_FONTSIZE)
axes[2].set_xlabel("")  # 使用共享 X 轴标签
axes[2].set_xticks(m_values[::2])
axes[2].set_yticks(n_global_values)
axes[2].tick_params(labelsize=TICK_FONTSIZE)

# --- Colorbars ---

# Add a single colorbar for the error plots, with label on the left
cbar_ax = fig.add_axes([0.055, 0.12, 0.018, 0.72])
cbar = fig.colorbar(im1, cax=cbar_ax, orientation="vertical")
cbar.set_label("平均 L2 范数误差", size=LABEL_FONTSIZE, labelpad=2)
# Move label & ticks to left side
cbar.ax.yaxis.set_label_position('left')
cbar.ax.yaxis.tick_left()
cbar.ax.yaxis.set_ticks_position('left')
cbar.ax.tick_params(labelsize=TICK_FONTSIZE)


# Add a separate colorbar for the ratio plot
cbar_ax_ratio = fig.add_axes([0.935, 0.12, 0.018, 0.72])
cbar = fig.colorbar(im3, cax=cbar_ax_ratio, orientation="vertical")
cbar.set_label("改进因子", size=LABEL_FONTSIZE, labelpad=4)
cbar.ax.tick_params(labelsize=TICK_FONTSIZE)

# Adjust rect to make space for the repositioned colorbar
plt.tight_layout(rect=[0.09, 0.07, 0.93, 0.96])
fig.text(0.5, 0.05, '内部模态数量', ha='center', va='center', fontsize=LABEL_FONTSIZE)

OUTPUT_FILE = "frequency-vs-phase.png"
try:
    plt.savefig(OUTPUT_FILE, dpi=DPI)
    pdf_path = OUTPUT_FILE[:-4] + '.pdf' if OUTPUT_FILE.lower().endswith('.png') else OUTPUT_FILE + '.pdf'
    plt.savefig(pdf_path, dpi=DPI, bbox_inches='tight')
    print(f"\n成功保存图表到: {OUTPUT_FILE} 与 {pdf_path}")
except Exception as e:
    print(f"保存图表时出错: {e}")

print("--- 绘图完成 ---")
