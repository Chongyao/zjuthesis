#!/usr/bin/env python3

"""
Generates performance plots for the 'sub-schur' benchmark results.

This script reads 'benchmark_results_schur_fixed_params.csv' and produces two plots:
1. schur_cost_breakdown.png: A stacked area chart showing the contribution
   of each component to the total cost as the problem size increases.
2. schur_scaling_analysis.png: A log-log plot showing the scaling complexity
   of each cost component.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style_config import get_style, apply_style

SCHEME = os.environ.get('PLOT_COLOR_SCHEME', 'teal_coral')
STYLE = get_style(SCHEME)
apply_style(STYLE, scale='double_column')

# --- Configuration ---
CSV_FILE = "benchmark_results_schur_fixed_params.csv"

TITLE_FONTSIZE = STYLE.scaled_fontsize('title', 'double_column')
LABEL_FONTSIZE = STYLE.scaled_fontsize('label', 'double_column')
LEGEND_FONTSIZE = STYLE.scaled_fontsize('legend', 'double_column')
TICK_FONTSIZE = STYLE.scaled_fontsize('tick', 'double_column')

# Get colors from style config for consistent theming
COLORS = STYLE.get_sequential_colors(4)

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
    
    # Sort by DoFs to ensure correct plotting for area/line charts
    df.sort_values(by='DoFs', inplace=True)
    
    print("Feature calculation complete.")
    return df

def plot_stacked_area(df):
    """Plot 1: Stacked area plot for cost breakdown."""
    print("Generating Plot 1: Cost Breakdown (Stacked Area)...")
    output_file = 'schur_cost_breakdown.png'
    
    fig, ax = plt.subplots(figsize=(12, 12))

    # Define labels and the data columns for the stacked plot
    labels = ['Factorization', r'$\mathbf{K}_{ii}^{-1} * \mathbf{K}_{ib}$', 'Matrix Multiplication']
    data_columns = ['factorization_cost', 'Kiiinv_Kib_cost', 'matrix_multiplication_cost']
    
    ax.stackplot(df['size'], df[data_columns].T, labels=labels, colors=COLORS[:3])
    
    ax.set_title(r'Breakdown of $t_{sub-schur}$', fontsize=TITLE_FONTSIZE)
    ax.set_xlabel('size', fontsize=LABEL_FONTSIZE)
    ax.set_ylabel(r'$t_{sub-eig} \ (s)$', fontsize=LABEL_FONTSIZE)
    ax.legend(loc='upper left', fontsize=LEGEND_FONTSIZE)
    ax.tick_params(axis='both', labelsize=TICK_FONTSIZE)
    ax.grid(False)
    # Set x-axis limit to start from 0
    ax.set_xlim(left=0)
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.savefig(output_file.replace('.png', '.pdf'), dpi=150)
    plt.close()
    print(f"Saved: {output_file}")


def plot_scaling_analysis(df):
    """Plot 2: Log-log plot for scaling analysis."""
    print("Generating Plot 2: Scaling Analysis (Log-Log)...")
    output_file = 'schur_scaling_analysis.png'
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    ax.plot(df['DoFs'], df['factorization_cost'], marker='o', linestyle='-', color=COLORS[0], label='Factorization')
    ax.plot(df['DoFs'], df['Kiiinv_Kib_cost'], marker='o', linestyle='-', color=COLORS[1], label=r'$\mathbf{K}_{ii}^{-1} * \mathbf{K}_{ib}$')
    ax.plot(df['DoFs'], df['matrix_multiplication_cost'], marker='o', linestyle='-', color=COLORS[2], label='Matrix Multiplication')
    ax.plot(df['DoFs'], df['sub_schur_total_cost'], marker='o', linestyle='-', color=COLORS[3], label='Total Cost')
    
    # Set scales to log-log
    ax.set_xscale('log')
    ax.set_yscale('log')
    
    ax.set_title('Scaling Analysis of Cost Components (Log-Log Scale)', fontsize=TITLE_FONTSIZE)
    ax.set_xlabel('Degrees of Freedom (DoFs)', fontsize=LABEL_FONTSIZE)
    ax.set_ylabel(r'$t_{sub-schur}$ (s)', fontsize=LABEL_FONTSIZE)
    ax.legend(fontsize=LEGEND_FONTSIZE)
    ax.tick_params(axis='both', labelsize=TICK_FONTSIZE)
    ax.grid(False)
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.savefig(output_file.replace('.png', '.pdf'), dpi=150)
    plt.close()
    print(f"Saved: {output_file}")


def main():
    """Main execution function."""
    df = load_and_process_data(CSV_FILE)

    if df is not None:
        plot_stacked_area(df)
        plot_scaling_analysis(df)
        print("\nAll plots generated successfully.")

if __name__ == "__main__":
    main()
