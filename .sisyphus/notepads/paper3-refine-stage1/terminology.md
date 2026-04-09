# Paper 3 Bilingual Terminology Baseline

This table compares key English terms from the original paper (`/home/zcy/workspace/records/primal-dual_modes/paper-body/`) with their preferred Chinese translations used in the Zhejiang University PhD thesis (`/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3/`).

| Category | English Source Term | Chinese Thesis Translation | Notes / Context |
| :--- | :--- | :--- | :--- |
| **Core Methods** | Component Mode Synthesis (CMS) | 模态综合法 (CMS) | Standard translation, per `AGENTS.md`. |
| **Core Methods** | Craig-Bampton (CB) method | Craig-Bampton (CB) 方法 | Kept in English with Chinese suffix. |
| **Core Methods** | Interface Mode Reduction (IMR) | 界面模态缩减法 (IMR) | Standard translation, per `AGENTS.md`. |
| **Core Methods** | Multiple Partitions | 多重划分 | Used consistently throughout. |
| **Core Methods** | Phase-complement | 相位补足 / 相位完备 | E.g., "phase-complete basis" -> "相位完备基". |
| **Core Methods** | Schur complement | Schur 补 | "Schur" kept in English. |
| **Core Methods** | Schur- and Eigen-free IMR (SE-free IMR) | 无 Schur 补和特征求解的 IMR (SE-free IMR) | Often abbreviated as SE-free IMR in text. |
| **Core Methods** | Primal partition | Primal 划分 | "Primal" kept in English (often capitalized). |
| **Core Methods** | Dual partition | Dual 划分 | "Dual" kept in English (often capitalized). |
| **Core Methods** | Complementary partition | 互补划分 | Auxiliary partition to fix phase issues. |
| **Structural Mechanics** | Domain | 区域 / 计算域 | |
| **Structural Mechanics** | Substructure | 子结构 | |
| **Structural Mechanics** | Interface | 界面 | |
| **Structural Mechanics** | Degrees of Freedom (DoFs) | 自由度 (DoFs) | |
| **Structural Mechanics** | Substructure eigenmodes | 子结构特征模态 | Sometimes "局部特征模态". |
| **Structural Mechanics** | Interface modes | 界面模态 | |
| **Structural Mechanics** | Stiffness matrix | 刚度矩阵 | |
| **Structural Mechanics** | Mass matrix | 质量矩阵 | |
| **Structural Mechanics** | Reduced matrix / system | 缩减矩阵 / 缩减系统 | |
| **Structural Mechanics** | Static equilibrium | 静力平衡 | |
| **Structural Mechanics** | Local updates | 局部更新 | |
| **Eigensolvers & HPC** | Generalized eigenproblem | 广义特征值问题 | |
| **Eigensolvers & HPC** | Eigenvalue / Eigenvector | 特征值 / 特征向量 | |
| **Eigensolvers & HPC** | Eigensolver | 特征值求解器 | |
| **Eigensolvers & HPC** | Singular matrix pencil | 奇异矩阵束 | |
| **Eigensolvers & HPC** | Regularization | 正则化 | |
| **Eigensolvers & HPC** | High-Performance Computing (HPC) | HPC / 高性能计算 | |
| **Eigensolvers & HPC** | Strong scaling / Weak scaling | 强扩展 / 弱扩展 | |
| **Eigensolvers & HPC** | Load balance | 负载均衡 | |
| **Eigensolvers & HPC** | Emulation of parallel environment | 并行环境模拟 | |
| **Eigensolvers & HPC** | Hybrid MPI/OpenMP | 混合 MPI/OpenMP | |

## Key Conventions Observed
1.  **Mixed-case Technical Terms:** `Primal`, `Dual`, `Schur`, `Dirichlet`, `Galerkin`, and acronyms (`CMS`, `IMR`, `MPI`, `OpenMP`) are frequently retained in English within the Chinese text to preserve technical precision and avoid clunky literal translations.
2.  **Explicit Rules:** As defined in `AGENTS.md`, `\DET{M}` is used over `\DETtext`, and the conclusion chapter is explicitly named `7_summary.tex` ("本章小结").
3.  **Phrasing:** Sentences are structured to sound natural in academic Chinese (e.g., using "本文方法" instead of direct "our method" translations in many cases).
