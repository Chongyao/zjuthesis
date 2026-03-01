#!/usr/bin/env python
"""
Generate a color palette swatch for the current color scheme.
Colors are ordered from left to right by importance/frequency of use.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plot_style_config import get_style, COLOR_SCHEMES

def generate_color_palette(scheme_name='teal_coral', output_dir=None):
    """Generate a color palette swatch image."""

    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))

    style = get_style(scheme_name)
    colors = style.colors

    # Define colors in order of importance (most important first)
    palette = [
        (colors['primary'], 'Primary\n(Ours)'),
        (colors['secondary'], 'Secondary\n(CMS)'),
        (colors['tertiary'], 'Tertiary\n(AMLS)'),
        (colors['quaternary'], 'Quaternary'),
        (colors['primary_light'], 'Primary\nLight'),
        (colors['quinary'], 'Quinary'),
        (colors['senary'], 'Senary'),
    ]

    # Add sequential colors
    sequential = colors.get('sequential', [])
    for i, c in enumerate(sequential):
        palette.append((c, f'Seq {i+1}'))

    n_colors = len(palette)

    # Create figure
    fig_width = min(n_colors * 1.2, 16)
    fig, ax = plt.subplots(figsize=(fig_width, 2.5))

    # Draw color blocks
    block_width = 1.0
    block_height = 1.0
    spacing = 0.1

    for i, (color, label) in enumerate(palette):
        x = i * (block_width + spacing)
        rect = mpatches.FancyBboxPatch(
            (x, 0), block_width, block_height,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            facecolor=color,
            edgecolor='#333333',
            linewidth=1.5
        )
        ax.add_patch(rect)

        # Add color hex code
        ax.text(x + block_width/2, -0.15, color.upper(),
                ha='center', va='top', fontsize=8, fontfamily='monospace')

        # Add label
        ax.text(x + block_width/2, block_height + 0.08, label,
                ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Set axis limits and remove axes
    total_width = n_colors * (block_width + spacing) - spacing
    ax.set_xlim(-0.2, total_width + 0.2)
    ax.set_ylim(-0.4, block_height + 0.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Add title
    ax.set_title(f'Color Palette: {scheme_name}', fontsize=14, fontweight='bold', pad=20)

    # Save
    output_path = os.path.join(output_dir, f'color_palette_{scheme_name}.pdf')
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    output_path_png = os.path.join(output_dir, f'color_palette_{scheme_name}.png')
    plt.savefig(output_path_png, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    print(f"Saved: {output_path}")
    print(f"Saved: {output_path_png}")

    return output_path


def generate_breakdown_palette(scheme_name='teal_coral', output_dir=None):
    """Generate a breakdown color palette for pie charts and stacked bars."""

    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))

    style = get_style(scheme_name)
    breakdown = style.breakdown_colors

    if not breakdown:
        print(f"No breakdown colors defined for scheme: {scheme_name}")
        return None

    # Filter unique colors and their primary labels
    seen_colors = {}
    for label, color in breakdown.items():
        if color not in seen_colors:
            seen_colors[color] = label

    # Sort by label length (shorter = more important/common)
    palette = [(color, label) for color, label in seen_colors.items()]

    n_colors = len(palette)

    # Create figure
    fig_width = min(n_colors * 1.5, 18)
    fig, ax = plt.subplots(figsize=(fig_width, 3))

    # Draw color blocks
    block_width = 1.0
    block_height = 1.0
    spacing = 0.15

    for i, (color, label) in enumerate(palette):
        x = i * (block_width + spacing)
        rect = mpatches.FancyBboxPatch(
            (x, 0), block_width, block_height,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            facecolor=color,
            edgecolor='#333333',
            linewidth=1.5
        )
        ax.add_patch(rect)

        # Add color hex code
        ax.text(x + block_width/2, -0.15, color.upper(),
                ha='center', va='top', fontsize=7, fontfamily='monospace')

        # Add short label (wrap long labels)
        short_label = label.replace(' (Ours)', '').replace(' (CMS)', '')
        if len(short_label) > 15:
            words = short_label.split()
            mid = len(words) // 2
            short_label = '\n'.join([' '.join(words[:mid]), ' '.join(words[mid:])])
        ax.text(x + block_width/2, block_height + 0.08, short_label,
                ha='center', va='bottom', fontsize=7, fontweight='bold')

    # Set axis limits and remove axes
    total_width = n_colors * (block_width + spacing) - spacing
    ax.set_xlim(-0.2, total_width + 0.2)
    ax.set_ylim(-0.4, block_height + 0.7)
    ax.set_aspect('equal')
    ax.axis('off')

    # Add title
    ax.set_title(f'Breakdown Colors: {scheme_name}', fontsize=14, fontweight='bold', pad=20)

    # Save
    output_path = os.path.join(output_dir, f'color_palette_{scheme_name}_breakdown.pdf')
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    output_path_png = os.path.join(output_dir, f'color_palette_{scheme_name}_breakdown.png')
    plt.savefig(output_path_png, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    print(f"Saved: {output_path}")
    print(f"Saved: {output_path_png}")

    return output_path


if __name__ == '__main__':
    scheme = os.environ.get('PLOT_COLOR_SCHEME', 'teal_coral')

    if len(sys.argv) > 1:
        scheme = sys.argv[1]

    generate_color_palette(scheme)
    generate_breakdown_palette(scheme)
