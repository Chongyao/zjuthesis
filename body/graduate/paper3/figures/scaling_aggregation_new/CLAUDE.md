# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a subdirectory of the **arborescence** project - a C++/Python scientific computing framework for finite element analysis with focus on Component Mode Synthesis (CMS) and eigenvalue problems. This specific directory (`scaling_aggregation_new`) contains Python scripts for performance benchmarking analysis and visualization.

## Directory Purpose

`scaling_aggregation_new/` contains performance analysis tools for MPI-based simulation benchmarks:
- `combine_jsons.py` - Aggregates benchmark JSON files from different scaling types (weak-pd, weak-sp, weak-gt, strong-pd, strong-sp, strong-gt)
- `plot_new_benchmarks.py` - Generates performance visualization plots using matplotlib/numpy
- `*_benchmarks.json` - Raw benchmark data files
- `*_scaling_plots/` - Generated PNG visualizations

## Running Python Scripts

```bash
# Combine benchmark JSON files
python combine_jsons.py

# Generate plots (optional: with key replacement file)
python plot_new_benchmarks.py [--replacement-file <file>]
```

## Parent Project Build Commands

The parent project (`/home/zcy/workspace/projects/arborecence`) uses CMake with presets:

```bash
# Configure and build (from project root)
make release          # Release build with GCC
make debug            # Debug build with GCC

# Or use CMake presets directly
cmake --preset=release && cmake --build --preset=release
cmake --preset=debug && cmake --build --preset=debug
cmake --preset=release-clang  # Clang release build

# Binaries output to: build-<preset>/bin/
```

## Parent Project Architecture

The main arborescence project structure:
- `src/` - Core libraries organized by functionality:
  - `fem/` - Finite element method implementation
  - `eigen_solver/` - Eigenvalue solvers (Spectra-based)
  - `simulator/` - FEM system assembly and simulation
  - `coarsened_basis/` - Basis coarsening for multigrid/CMS
  - `geometry/` - Mesh geometry operations
  - `graph_partition/` - METIS-based mesh partitioning
  - `io/` - VTK and matrix I/O
  - `tools/` - Utility functions
- `apps/` - Standalone executables (CMS solvers, mesh tools)
- `test/` - Test executables
- `pipline/` - Workflow scripts and benchmarking (this directory's parent)

## Key Dependencies

- Eigen3 (with BLAS), SuiteSparse (CHOLMOD), Spectra (eigensolvers)
- MPI for distributed computing
- METIS for graph partitioning
- Boost (program_options, json)
- matplotlib/numpy for Python plotting

## CMS (Component Mode Synthesis) Pipeline

The main computational pipeline involves:
1. Mesh partitioning (`cms_get_partition`)
2. Substructure eigensolve (`cms_local_update`, `cms_solve_substructure`)
3. Interface mode generation
4. Reduced system assembly and solve (`cms_reduce_solve`)

Performance methods compared: `pd` (primal-dual), `sp` (subspace), `gt` (global/traditional)
