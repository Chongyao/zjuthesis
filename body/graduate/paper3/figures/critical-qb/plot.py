# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style_config import get_style, apply_style

SCHEME = os.environ.get('PLOT_COLOR_SCHEME', 'teal_coral')
STYLE = get_style(SCHEME)
apply_style(STYLE, scale='double_column')

OURS_COLOR = STYLE.ours
CMS_COLOR = STYLE.cms
OURS_MARKER = 'o'
CMS_MARKER = 'o'
LINE_WIDTH = STYLE.methods['ours']['linewidth']
MARKER_SIZE = STYLE.methods['ours']['markersize']
TITLE_FONTSIZE = STYLE.scaled_fontsize('title', 'double_column')
LABEL_FONTSIZE = STYLE.scaled_fontsize('label', 'double_column')
LEGEND_FONTSIZE = STYLE.scaled_fontsize('legend', 'double_column')
TICK_FONTSIZE = STYLE.scaled_fontsize('tick', 'double_column')

def load_data(path, is_pd=False):
    """Loads data from a text file. For PD data, converts npart to num_nodes."""
    try:
        data = np.loadtxt(path)
        x = data[:, 0]
        y = data[:, 1]
        if is_pd:
            x = x * 2 + 1
        return x, y
    except FileNotFoundError:
        print(f"Warning: Data file not found at '{path}'")
        return None, None
    except IndexError:
        print(f"Warning: Data file at '{path}' has incorrect format.")
        return None, None

def generate_plot(data1_path, data2_path, output_filename_base, title, legend_options=None, show_xlabel=True):
    """
    Generates and saves a plot for the given data.
    """
    x1, y1 = load_data(data1_path)
    x2, y2 = load_data(data2_path)

    # Skip plotting if data is missing
    if x1 is None or x2 is None:
        print(f"Skipping plot for '{title}' due to missing data.")
        return

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x1, y1, marker=OURS_MARKER, linestyle='-', color=OURS_COLOR, label='本文方法', markersize=MARKER_SIZE, linewidth=LINE_WIDTH)
    ax.plot(x2, y2, marker=CMS_MARKER, linestyle='-', color=CMS_COLOR, label='CB-CMS', markersize=MARKER_SIZE, linewidth=LINE_WIDTH)

    if show_xlabel:
        ax.set_xlabel('计算节点数', fontsize=LABEL_FONTSIZE)
    ax.set_ylabel(r'$q_b$', fontsize=LABEL_FONTSIZE)

    ax.text(0.98, 0.95, title,
            transform=ax.transAxes,
            fontsize=TITLE_FONTSIZE,
            verticalalignment='top',
            horizontalalignment='right')
    
    ax.tick_params(axis='x', labelsize=TICK_FONTSIZE)
    ax.tick_params(axis='y', labelsize=TICK_FONTSIZE)
    
    # Use scientific notation for y-axis
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    ax.yaxis.offsetText.set_fontsize(16)

    # --- Conditional Legend Handling ---
    if legend_options and legend_options.get('visible', True):
        # For legend outside, we use fig.legend
        fig.legend(
            loc=legend_options.get('loc', 'best'),
            bbox_to_anchor=legend_options.get('bbox_to_anchor', None),
            fontsize=legend_options.get('fontsize', 22),
            ncol=legend_options.get('ncol', 1),
            frameon=legend_options.get('frameon', False),
            edgecolor=legend_options.get('edgecolor', STYLE.ui_colors['marker_edge']),
            fancybox=False # Use sharp corners for the frame
        )

    ax.grid(False)
    
    # Adjust layout if legend is outside
    if legend_options and legend_options.get('loc') == 'upper center':
         fig.tight_layout(rect=[0, 0, 1, 0.9]) # Make space for outside legend
    else:
         fig.tight_layout()


    output_png = f'{output_filename_base}.png'
    output_pdf = f'{output_filename_base}.pdf'

    plt.savefig(output_png, dpi=300, bbox_inches='tight')
    plt.savefig(output_pdf, dpi=300, bbox_inches='tight')
    plt.close()  # Close the figure to free up memory
    
    print(f"Successfully generated: {output_png} and {output_pdf}")

def main():
    """
    Main function to generate both weak and strong scaling plots.
    """
    plot_combined_scaling()

def plot_combined_scaling():
    """Generates a single figure with Weak (top) and Strong (bottom) scaling plots stacked vertically."""
    print("--- Generating Combined Weak & Strong Scaling Figure ---")
    
    TARGET_NODES = [9, 17, 25, 33, 41, 49, 57]
    
    def filter_data(x, y, target_nodes):
        if x is None or y is None:
            return None, None
        mask = np.isin(x, target_nodes)
        return x[mask], y[mask]
    
    w_x1_raw, w_y1_raw = load_data('weak-pd_unit200x200/time_record.txt', is_pd=True)
    w_x2_raw, w_y2_raw = load_data('weak-sp_unit200x200/time_record.txt', is_pd=False)
    s_x1_raw, s_y1_raw = load_data('strong-pd_s1000/time_record.txt', is_pd=True)
    s_x2_raw, s_y2_raw = load_data('strong-sp_s1000/time_record.txt', is_pd=False)

    if any(v is None for v in [w_x1_raw, w_x2_raw, s_x1_raw, s_x2_raw]):
        print("Data missing; aborting combined figure.")
        return
    
    w_x1, w_y1 = filter_data(w_x1_raw, w_y1_raw, TARGET_NODES)
    w_x2, w_y2 = filter_data(w_x2_raw, w_y2_raw, TARGET_NODES)
    s_x1, s_y1 = filter_data(s_x1_raw, s_y1_raw, TARGET_NODES)
    s_x2, s_y2 = filter_data(s_x2_raw, s_y2_raw, TARGET_NODES)
    
    print(f"  Weak PD nodes: {w_x1.tolist() if w_x1 is not None and len(w_x1) > 0 else 'empty'}")
    print(f"  Weak SP nodes: {w_x2.tolist() if w_x2 is not None and len(w_x2) > 0 else 'empty'}")
    print(f"  Strong PD nodes: {s_x1.tolist() if s_x1 is not None and len(s_x1) > 0 else 'empty'}")
    print(f"  Strong SP nodes: {s_x2.tolist() if s_x2 is not None and len(s_x2) > 0 else 'empty'}")

    fig, (ax_top, ax_bottom) = plt.subplots(2, 1, figsize=(14, 8), sharex=False)

    ax_top.plot(w_x1, w_y1, marker=OURS_MARKER, linestyle='-', color=OURS_COLOR, label='本文方法', markersize=MARKER_SIZE, linewidth=LINE_WIDTH)
    ax_top.plot(w_x2, w_y2, marker=CMS_MARKER, linestyle='-', color=CMS_COLOR, label='CB-CMS', markersize=MARKER_SIZE, linewidth=LINE_WIDTH)
    ax_top.set_ylabel(r'$q_{\mathcal{I}^\star}$', fontsize=LABEL_FONTSIZE)
    ax_top.text(0.98, 0.95, '弱扩展', transform=ax_top.transAxes,
                fontsize=TITLE_FONTSIZE, va='top', ha='right')
    ax_top.tick_params(axis='x', labelsize=TICK_FONTSIZE)
    ax_top.tick_params(axis='y', labelsize=TICK_FONTSIZE)
    ax_top.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    ax_top.yaxis.offsetText.set_fontsize(TICK_FONTSIZE)
    ax_top.grid(False)

    ax_bottom.plot(s_x1, s_y1, marker=OURS_MARKER, linestyle='-', color=OURS_COLOR, label='本文方法', markersize=MARKER_SIZE, linewidth=LINE_WIDTH)
    ax_bottom.plot(s_x2, s_y2, marker=CMS_MARKER, linestyle='-', color=CMS_COLOR, label='CB-CMS', markersize=MARKER_SIZE, linewidth=LINE_WIDTH)
    ax_bottom.set_ylabel(r'$q_{\mathcal{I}^\star}$', fontsize=LABEL_FONTSIZE)
    ax_bottom.text(0.98, 0.95, '强扩展', transform=ax_bottom.transAxes,
                   fontsize=TITLE_FONTSIZE, va='top', ha='right')
    ax_bottom.tick_params(axis='x', labelsize=TICK_FONTSIZE)
    ax_bottom.tick_params(axis='y', labelsize=TICK_FONTSIZE)
    ax_bottom.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    ax_bottom.yaxis.offsetText.set_fontsize(TICK_FONTSIZE)
    ax_bottom.grid(False)

    fig.supxlabel('计算节点数', fontsize=LABEL_FONTSIZE, y=0.03)

    # Outside legend (use handles from bottom plot)
    handles, labels = ax_bottom.get_legend_handles_labels()
    legend = fig.legend(handles, labels,
                        loc='upper center', bbox_to_anchor=(0.5, 1.00),
                        ncol=2, fontsize=LEGEND_FONTSIZE, frameon=True)
    frame = legend.get_frame()
    frame.set_edgecolor('none')
    frame.set_facecolor('none')
    frame.set_linewidth(0.0)

    plt.tight_layout(h_pad = 0.0, rect=[0, 0, 1, 0.97])
    out_png = 'combined_scaling.png'
    out_pdf = 'combined_scaling.pdf'
    plt.savefig(out_png, dpi=300, bbox_inches='tight')
    plt.savefig(out_pdf, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved combined figure: {out_png}, {out_pdf}")

if __name__ == "__main__":
    main()