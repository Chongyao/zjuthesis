# Paper3 Refine Stage 2: Intro & Conclusion

## TL;DR

> **Quick Summary**: 对 `body/graduate/paper3/1_intro.tex` 和 `5_conclusion.tex` 进行逐段翻译层精修，消除过度修辞，恢复严谨朴实的学术英文对照风格，修复被压缩的物理机制解释，统一专业术语。
>
> **Deliverables**:
> - 修改后的 `1_intro.tex`
> - 修改后的 `5_conclusion.tex`
> - 相关段落改写后的本地编译检查
>
> **Estimated Effort**: High
> **Parallel Execution**: NO (sequential modifications on thesis files)
> **Critical Path**: `1_intro.tex` 改写 $\rightarrow$ `5_conclusion.tex` 改写 $\rightarrow$ 编译与人工检视

---

## Context

### Preceding Stage (Stage 1)
- 已经完成 `paper3` 与 `primal-dual_modes` 原文的对应映射。
- 确认了 `1_intro.tex` 是 abstract、introduction 和 related work 的混合体，带有明显的情绪化扩写。
- 确立了术语基线（如“自适应位移”、“界面模态缩减”、“相位补足”等）。
- 确立了风格反模式（如禁用“浩瀚天堑”、“逆转乾坤”、“填鸭式”等宏大词汇）。

### Work Objectives
- **Target 1**: 彻底清洗 `1_intro.tex` 中的非学术修辞，将原本被抽象口号掩盖的“Fourier 相位限制”与“静力平衡代替特征求解”的机制解释还原。
- **Target 2**: 收缩 `5_conclusion.tex` 的篇幅和调性，将其压回原本 conclusion 的事实边界内，只保留必要的章节承接。

## Execution Tasks

- [x] **Task 1: Rewrite intro P1-P3 (Background & Bottleneck)**
  - 改写 `1_intro.tex` 前 3 段。
  - 清除“最致命瓶颈”、“绝不打折扣的标准金律”等词汇。
  - 保留 Krylov, SLEPc, MUMPS 的事实描述。

- [x] **Task 2: Rewrite intro P4-P7 (Related Work)**
  - 对照原文清理 related work 段落。
  - 维持现有逻辑框架，仅统一专业术语，压实句子结构。

- [x] **Task 3: Rewrite intro P8-P12 (Mechanism & Proposed Method)**
  - **核心难点**：重构传统 CMS 相位缺失的机理描述。
  - 增加：Fourier 模式局部窗口边界截断导致相位受限。
  - 改写：多重划分如何通过错位提供不同相位的同频基函数（补足相位）。
  - 还原：SE-free IMR 并不是单纯的“踢出整体链路”，而是“用另一划分的低频模态边界取值作为静力平衡激励”。
- [x] **Task 4: Rewrite intro P13 (Contributions)**
  - 将三个主要贡献点的描述降温。
  - 把“跃升级的精度赋能”、“彻底颠覆陈规”改写为“提出...提升了...保留了...”。

- [x] **Task 5: Refine 5_conclusion.tex**
  - 参照原文 conclusion 收敛总结。
  - 保留合理展望，剔除宣传性定语。

- [x] **Task 6: Final Compilation Check**
  - 使用 `latexmk` 编译检查论文是否正常生成，引用是否无断链。

---

## Terminology Enforcement
- Component Mode Synthesis (CMS) $\rightarrow$ 模态综合法
- Interface Mode Reduction (IMR) $\rightarrow$ 界面模态缩减法
- phase-complete basis $\rightarrow$ 相位完备基
- Schur complement $\rightarrow$ Schur 补
- adaptive shifting $\rightarrow$ 自适应位移
- spatially staggered partitions $\rightarrow$ 交错划分
