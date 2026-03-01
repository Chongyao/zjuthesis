#!/usr/bin/env python3

"""
Generates a comprehensive set of performance plots from the benchmark_results.csv file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import os
import sys

# --- Unified Style Config ---
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style_config import get_style, apply_style

SCHEME = os.environ.get('PLOT_COLOR_SCHEME', 'teal_coral')
STYLE = get_style(SCHEME)
apply_style(STYLE, scale='double_column')

LABEL_FONTSIZE = STYLE.scaled_fontsize('label', 'double_column')
LEGEND_FONTSIZE = STYLE.scaled_fontsize('legend', 'double_column')
TICK_FONTSIZE = STYLE.scaled_fontsize('tick', 'double_column')

# --- Configuration ---
CSV_FILE = "benchmark_results.csv"
PLT_STYLE = 'seaborn-v0_8-darkgrid'

def load_and_process_data(csv_file):
    """Loads the CSV and calculates derived features."""
    print(f"Loading data from {csv_file}...")
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
        print("Please ensure the CSV file is in the same directory as this script.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None

    print("Data loaded. Calculating features...")
    
    # Calculate Degrees of Freedom (DoFs)
    df['DoFs'] = (df['size'] * df['size']) / 3
    
    # Calculate Factorization Cost Percentage
    df['factorization_percentage'] = (df['factorization_cost_s'] / df['sub_eig_cost_s'])
    
    print("Feature calculation complete.")
    return df

def get_plot_styling(df):
    """Creates a consistent color map for 'size' using unified sequential colors."""
    sizes = sorted(df['size'].unique())
    # Use sequential colors from unified style
    seq_colors = STYLE.colors['sequential']
    # Interpolate to match number of sizes
    n = len(sizes)
    if n <= len(seq_colors):
        plot_colors = seq_colors[:n]
    else:
        # Generate more colors by interpolation
        cmap = STYLE.get_sequential_cmap()
        plot_colors = [cmap(i / n) for i in range(n)]
    size_to_color = dict(zip(sizes, plot_colors))
    return sizes, size_to_color

def plot_total_cost(df, sizes, size_to_color):
    """Plot 1: Total Cost vs. Eigenvalues (Grouped by Size)"""
    print("Generating Plot 1: Total Cost vs. Eigenvalues...")
    output_file = 'total_cost_vs_neig_blk.png'
    
    plt.figure(figsize=(10, 6))
    for size in sizes:
        df_size = df[df['size'] == size]
        plt.plot(
            df_size['neig_blk'], 
            df_size['sub_eig_cost_s'], 
            marker='o', 
            linestyle='-', 
            label=f'size={size}',
            color=size_to_color[size],
            markersize=5
        )
    
    plt.title('Total Cost vs. Number of Eigenvalues', fontsize=16)
    plt.xlabel('Number of Eigenvalues (neig_blk)', fontsize=12)
    plt.ylabel('Total Cost (s)', fontsize=12)
    plt.legend(title='Size', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(False)
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()
    print(f"Saved: {output_file}")

def plot_factorization_cost(df):
    """Plot 2: Factorization Cost vs. Problem Size (Linear and Log-Log)"""
    print("Generating Plot 2: Factorization Cost vs. DoFs...")
    output_file_linear = 'factorization_cost_vs_dofs.png'
    output_file_log = 'factorization_cost_vs_dofs_log.png'

    # Aggregate data: Average factorization cost per size/DoFs
    df_agg = df.groupby(['DoFs', 'size'])['factorization_cost_s'].mean().reset_index()

    # Plot 2a: Linear Scale
    plt.figure(figsize=(10, 6))
    plt.plot(
        df_agg['DoFs'], 
        df_agg['factorization_cost_s'], 
        marker='o', 
        linestyle='-'
    )
    plt.title('Average Factorization Cost vs. Problem Size', fontsize=16)
    plt.xlabel('Degrees of Freedom (size*size/3)', fontsize=12)
    plt.ylabel('Average Factorization Cost (s)', fontsize=12)
    plt.grid(False)
    plt.tight_layout()
    plt.savefig(output_file_linear, dpi=150)
    plt.close()
    print(f"Saved: {output_file_linear}")

    # Plot 2b: Log-Log Scale
    plt.figure(figsize=(10, 6))
    plt.plot(
        df_agg['DoFs'], 
        df_agg['factorization_cost_s'], 
        marker='o', 
        linestyle='-'
    )
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Average Factorization Cost vs. Problem Size (Log-Log Scale)', fontsize=16)
    plt.xlabel('Degrees of Freedom (Log Scale)', fontsize=12)
    plt.ylabel('Average Factorization Cost (s, Log Scale)', fontsize=12)
    plt.grid(False)
    plt.tight_layout()
    plt.savefig(output_file_log, dpi=150)
    plt.close()
    print(f"Saved: {output_file_log}")

def plot_nsolve_count(df, sizes, size_to_color):
    """Plot 3: Solver Work vs. Eigenvalues (Grouped by Size)"""
    print("Generating Plot 3: Solver Work vs. Eigenvalues...")
    output_file = 'nsolve_vs_neig_blk.png'
    
    plt.figure(figsize=(10, 6))
    for size in sizes:
        df_size = df[df['size'] == size]
        plt.plot(
            df_size['neig_blk'], 
            df_size['nsolve_count'], 
            marker='o', 
            linestyle='-', 
            label=f'size={size}',
            color=size_to_color[size],
            markersize=5
        )
    
    plt.title('Solver Work vs. Number of Eigenvalues', fontsize=16)
    plt.xlabel('Number of Eigenvalues (neig_blk)', fontsize=12)
    plt.ylabel('Number of Solves (nsolve_count)', fontsize=12)
    plt.legend(title='Size', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(False)
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()
    print(f"Saved: {output_file}")

def plot_heatmap(df):
    """Plot 4: Heatmap of Factorization Cost Percentage"""
    print("Generating Plot 4: Factorization Cost Percentage Heatmap...")
    output_file = 'factorization_percentage_heatmap.png'
    
    try:
        # Pivot by 'DoFs'
        df_pivot = df.pivot(index='DoFs', columns='neig_blk', values='factorization_percentage')
    except Exception as e:
        print(f"Warning: Could not pivot data (may have duplicates). Using pivot_table... {e}")
        # Fallback pivot_table also by 'DoFs'
        df_pivot = pd.pivot_table(df, index='DoFs', columns='neig_blk', values='factorization_percentage', aggfunc='mean')
    
    # Ensure the pivot index is sorted for a correct Y-axis
    df_pivot.sort_index(ascending=True, inplace=True)

    plt.figure(figsize=(11, 6))
    ax = plt.gca()

    # Use LogNorm for the log-scale color mapping
    c = ax.pcolormesh(
        df_pivot.values,
        norm=colors.LogNorm(vmin=df_pivot.min().min(), vmax=df_pivot.max().max()),
        cmap=STYLE.get_sequential_cmap()
    )
    
    # Add a color bar
    plt.colorbar(c, ax=ax, label=' Percentage')

    # Set Title and Axis Labels
    plt.title('Factorization Cost as Percentage of $t_{fac}/t_{sub-eig}$', fontsize=16)
    plt.xlabel('Number of Eigenvalues (neig_blk)', fontsize=12)
    # Update Y-axis label
    plt.ylabel('Degrees of Freedom (DoFs)', fontsize=12)

    # Set X-axis ticks (show every 4th label to keep it clean)
    xtick_labels = df_pivot.columns
    xtick_locs = np.arange(len(xtick_labels)) + 0.5
    visible_xtick_indices = np.arange(0, len(xtick_labels), 4)
    ax.set_xticks(xtick_locs[visible_xtick_indices])
    ax.set_xticklabels(xtick_labels[visible_xtick_indices])

    # Set Y-axis ticks
    ytick_labels = df_pivot.index
    ytick_locs = np.arange(len(ytick_labels)) + 0.5
    ax.set_yticks(ytick_locs)
    
    # CHANGE: Format labels using scientific notation (e.g., "3.33e+04")
    # f'{label:.2e}' means format as exponential notation with 2 decimal places.
    ax.set_yticklabels([f'{label:.2e}' for label in ytick_labels])

    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()
    print(f"Saved: {output_file}")

def main():
    """Main execution function."""
    
    # Set plot style
    try:
        plt.style.use(PLT_STYLE)
    except:
        print(f"Warning: Plot style '{PLT_STYLE}' not found. Using default.")

    # Load and process data
    df = load_and_process_data(CSV_FILE)
    
    if df is not None:
        # Get common styling
        sizes, size_to_color = get_plot_styling(df)
        
        # Generate all plots
        plot_total_cost(df, sizes, size_to_color)
        plot_factorization_cost(df)
        plot_nsolve_count(df, sizes, size_to_color)
        plot_heatmap(df)
        
        print("\nAll plots generated successfully.")

if __name__ == "__main__":
    main()
