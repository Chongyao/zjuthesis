# 博士论文绪论（第一章）局部与段落级修改计划

## TL;DR

> **Quick Summary**: 本计划旨在依据《绪论审稿意见记录》中的分级评定，执行“A.低难度”与“B.中难度”的修改任务。在不改变第一章整体论述架构（如“背景-物理管线-病态性-三个问题”）的前提下，彻底清除格式硬伤、统一行文称谓、修复未完成引用，并对部分行文冗余、评价过强或论断过大的段落进行结构性压缩与措辞收敛。
> 
> **Deliverables**: 
> - 格式与命名规范化后的绪论源文件集合（处理图表、引用与文件命名问题）
> - 语言风格凝练、修辞降温后的正文（处理冗余修饰、长句与宣传式表达）
> 
> **Estimated Effort**: Medium
> **Parallel Execution**: YES - 2 waves (Wave 1: 格式与命名规范化; Wave 2: 文本与措辞精简)
> **Critical Path**: Task 1 (文件重命名与配置剥离) → Task 2 (引用与称谓修复) → Task 3-5 (各小节文本压缩与措辞收敛)

---

## Context

### Original Request
用户要求按照根目录下 `intro_review.md` 中构建的分级 Todo List，完成“低难度”与“中难度”的修改任务。高难度（涉及整体逻辑重组）暂不处理。

### Metis Review
**Identified Gaps** (addressed):
- **命名规范明确**: 明确 `3.1_structure.tex` 应重命名为 `3_structure.tex` 或是将其内容直接合并，由于其仅包含 TikZ 代码，最合理的做法是将其 TikZ 配置部分移出，正文部分并入 `3_contributions_and_organization.tex` 或保留统一命名。本计划决定将绘图代码合并入 `3_contributions...` 中，并清理冗余文件。
- **保护 LaTeX 结构**: 在进行“中难度”的文本压缩与重写时，必须严格保护原有的公式环境 (`\begin{equation}...`)、引用 (`\cite{...}`) 及专业术语。
- **“本书”称谓统一**: 全文将严格统一替换为“本文”。
- **验证手段**: 必须确保修改后 `latexmk` 能够无误编译，且 PDF 中无 `??` 引用缺失。
- **任务分离原则**: 采纳 Metis 建议，将修改严格分为“机械性替换（Wave 1）”和“语境感知的文本压缩（Wave 2）”两个波次，防止在改写长句时意外破坏 LaTeX 结构。

---

## Work Objectives

### Core Objective
完成绪论部分低、中难度的审稿意见修改，提升绪论的格式规范性与文本凝练度，使其语言风格贴近合格的博士论文标准。

### Concrete Deliverables
- 修正后的 `1_background.tex`（压缩 AGI 背景与连锁反应段落）
- 修正后的 `2_related_and_problems.tex`（修复 6 处占位图、统一 `\ref` 引用、拆分过长句子、调低评价性措辞）
- 修正后的 `3_contributions_and_organization.tex`（吸收原 `3.1_structure.tex` 的有益部分并清理后者、精简总论性表述）
- 清理掉的不规范文件 `3.1_structure.tex`。

### Definition of Done
- [ ] 根目录下执行 `latexmk` 编译成功，无 Error。
- [ ] `grep -r "本书" body/graduate/intro` 无结果。
- [ ] `grep -r "如图" body/graduate/intro | grep "xxx"` 无结果。
- [ ] `grep -r "TODO: 替换为实际图片" body/graduate/intro` 无结果。

### Must Have
- 必须使用 `\ref{}` 替代所有的 `图 xxx`。
- 必须将所有的占位图片替换为 `example-image-a` 到 `f`（或解除注释并确保占位图能够通过编译，如果用户环境中没有实际图片，则使用 `graphicx` 的占位符或现有的占位图）。
- 必须保留所有的物理推导与核心数学逻辑。

### Must NOT Have (Guardrails)
- 绝对禁止改变原有的段落层级（如将 `\section` 改为 `\subsection`）。这属于高难度逻辑调整，本计划不涉及。
- 绝对禁止破坏现有的 `\cite{...}` 引用标记。
- 绝对禁止在压缩文本时改变作者试图表达的核心学术观点（表征路线优于纯代数路线）。

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed. No exceptions.

### Test Decision
- **Infrastructure exists**: YES (LaTeX `latexmk` build system)
- **Automated tests**: None (Documentation update)
- **QA Policy**: 
  - 使用 Bash 运行 `latexmk` 确保文档可编译。
  - 使用 `grep` 验证特定的中文字符和占位符已被完全清除。

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Start Immediately — 机械性替换与格式规范，防破损基础):
├── Task 1: 文件结构重整与 TikZ 配置迁移 [quick]
├── Task 2: 占位图修复与交叉引用规范化 [quick]
└── Task 3: 全局术语与称谓统一 ("本书" -> "本文") [quick]

Wave 2 (After Wave 1 — 文本压缩与措辞收敛，中难度):
├── Task 4: 1_background.tex 文本精简与降温 [writing]
├── Task 5: 2_related_and_problems.tex 句型重构与评价客观化 [writing]
└── Task 6: 3_contributions_and_organization.tex 冗余清理与限制词补充 [writing]

Wave FINAL (After ALL tasks — 验证与编译):
└── Task F1: 编译测试与关键词残留核查 (oracle)
```

---

## TODOs

  - [x] 1. **文件结构重整与 TikZ 配置迁移**
- [x] 2. **占位图修复与交叉引用规范化**

  **What to do**:
  - 在 `2_related_and_problems.tex` 中，查找所有的 `% \includegraphics[...]{example-image-x} % TODO: 替换为实际图片`。
  - 取消对 `\includegraphics` 的注释，并删除 `% TODO...` 尾缀。
  - 查找所有的 `如图 xxx 所示` 或 `图 xxx`，根据上下文和后续图的 `\label`，将其替换为正确的 `如图~\ref{fig:...} 所示`。
  - 确保图 1 (细杆离散) 对应 `fig:intro_rod_representation`，图 2 (软硬刚度失配) 对应 `fig:intro_stiff_soft_rod`，依此类推。

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: 明确的占位符替换。

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] 运行 `grep "xxx" body/graduate/intro/2_related_and_problems.tex` 无结果。
  - [ ] 运行 `grep "TODO: 替换为实际图片" body/graduate/intro/2_related_and_problems.tex` 无结果。

  **QA Scenarios**:
  ```
  Scenario: Verify placeholders are removed
    Tool: Bash
    Preconditions: None
    Steps:
      1. grep -n "xxx" body/graduate/intro/2_related_and_problems.tex
      2. grep -n "TODO" body/graduate/intro/2_related_and_problems.tex
    Expected Result: Empty output for both commands.
    Evidence: .sisyphus/evidence/task-2-placeholder-check.txt
  ```

- [x] 3. **全局术语与称谓统一**

  **What to do**:
  - 扫描整个 `intro` 目录，将所有的“本书”替换为“本文”。（重点在 `2_related_and_problems.tex` 第78行和第93行附近）。
  - 将所有强烈的修辞副词如“疯狂堆叠”替换为中性词“过度堆叠/大量堆叠”；“彻底打破”改为“打破”。

  **Recommended Agent Profile**:
  - **Category**: `quick`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] 运行 `grep "本书" body/graduate/intro/*.tex` 无结果。

  **QA Scenarios**:
  ```
  Scenario: Verify "本书" is completely replaced
    Tool: Bash
    Preconditions: None
    Steps:
      1. grep "本书" body/graduate/intro/2_related_and_problems.tex
    Expected Result: Empty output.
    Evidence: .sisyphus/evidence/task-3-terminology-check.txt
  ```

- [ ] 4. **1_background.tex 文本精简与降温**

  **What to do**:
  - **精简背景铺陈**：将第一、二段中关于 CAE 和 CG 并行发展的历史描述压缩，提取核心论点（两者都需要数值精确与稳定性），去除冗余的文艺性描写（如“飞速发展的黄金阶段”、“殊途同归”）。
  - **降温 AGI 论断**：将第三段中“攻克物理仿真中的数值瓶颈，已从单纯的视觉追求演变为构建通用人工智能（AGI）底座的核心技术诉求”弱化为“高保真仿真环境在具身智能等前沿应用中日益重要，这对仿真算法的鲁棒性与计算效率提出了更严苛的要求”。
  - **压缩连锁反应段落**：整合第四、五段对病态性的描述，去除类似“毁灭性连锁反应”等极端词汇。

  **Must NOT do**:
  - 不要删除方程 `\begin{equation}...`。
  - 不要改变段落探讨的核心主题。

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: 需要进行学术中文的重写与润色。

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocked By**: Task 3

  **QA Scenarios**:
  ```
  Scenario: Verify tone has been softened
    Tool: Bash
    Preconditions: Task 4 complete
    Steps:
      1. grep "通用人工智能" body/graduate/intro/1_background.tex
      2. grep "毁灭性" body/graduate/intro/1_background.tex
    Expected Result: Both commands return empty or modified contexts.
    Evidence: .sisyphus/evidence/task-4-tone-check.txt
  ```

- [ ] 5. **2_related_and_problems.tex 句型重构与评价客观化**

  **What to do**:
  - **拆分长句**：梳理各 Subsection 中包含 3 个以上分句的超长复杂句，尤其是分析刚度来源的段落，将其拆分为“一句表达一个核心判断”的短句组合。
  - **客观化已有方法评价**：将针对传统代数路线的评价词进行软化。
    - 将“纯代数路线本质上是一种‘黑盒’修补...对其底层的物理成因毫无感知”修改为“纯代数路线主要从矩阵结构出发，较难直接感知底层的物理成因”。
    - 将“灾难性的衰减”修改为“显著衰减/急剧下降”。
    - 将“必然选择”修改为“一种极具潜力的有效途径”。
  - **缩减冗余推导说明**：在保留数学公式的前提下，删减对公式中每个平凡项（如 $\mathbf{b}$ 为体积力）的过度详细口语化解释，保持学术精炼。
  - **增加量化结果限定**：如果段落末尾提及性能提升，添加“在本文测试场景下”或“在具体实验设置中”等限定语（若有）。

  **Recommended Agent Profile**:
  - **Category**: `writing`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocked By**: Task 2, Task 3

  **QA Scenarios**:
  ```
  Scenario: Verify extreme evaluative words are removed
    Tool: Bash
    Preconditions: Task 5 complete
    Steps:
      1. grep "毫无感知" body/graduate/intro/2_related_and_problems.tex
      2. grep "黑盒修补" body/graduate/intro/2_related_and_problems.tex
      3. grep "灾难性" body/graduate/intro/2_related_and_problems.tex
    Expected Result: Empty output.
    Evidence: .sisyphus/evidence/task-5-eval-check.txt
  ```

- [ ] 6. **3_contributions_and_organization.tex 冗余清理与限制词补充**

  **What to do**:
  - **清理总论重复**：删除前两段中关于“挖掘软硬成分”与“距离约束”、“畸变单元”等与前文（第 1、2 节）高度重复的原理解释。直接切入“本文基于上述对软硬耦合的分析，主要研究工作包含以下三个方面：”。
  - **合并 TikZ 代码**：确保 Task 1 转移过来的 TikZ 代码在该文件末尾正常闭合，并且颜色定义等放在合适位置（最好放到文件头部）。

  **Recommended Agent Profile**:
  - **Category**: `writing`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocked By**: Task 1

  **QA Scenarios**:
  ```
  Scenario: Verify redundancy removal
    Tool: Bash
    Preconditions: Task 6 complete
    Steps:
      1. cat body/graduate/intro/3_contributions_and_organization.tex | head -n 15
    Expected Result: Shows direct transition to contributions, omitting the lengthy recap of hard/soft definitions.
    Evidence: .sisyphus/evidence/task-6-redundancy-check.txt
  ```

---

## Final Verification Wave

- [ ] F1. **编译测试与关键词残留核查** — `oracle`
  运行 `latexmk -c && latexmk`。确保编译成功且退出码为 0。
  运行 `grep` 验证 "本书", "图 xxx", "TODO: 替换为实际图片", "灾难性" 等关键字在整个 `body/graduate/intro/` 目录中已绝迹。
  Output: `Build [PASS/FAIL] | Keywords [CLEAN/FAIL] | VERDICT: APPROVE/REJECT`

---

## Commit Strategy

- **1**: `refactor(intro): fix placeholders, rename files, and compress text` — `body/graduate/intro/*.tex`

---

## Success Criteria

### Verification Commands
```bash
latexmk  # Expected: output ends with no fatal errors, pdf generated
grep -r "本书" body/graduate/intro/  # Expected: empty
```

### Final Checklist
- [ ] 所有低难度格式问题修复完成。
- [ ] 所有中难度文本精简完成。
- [ ] LaTeX 文档可编译。