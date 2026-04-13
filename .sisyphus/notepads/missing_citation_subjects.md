# 论文中缺少主语的 Citation 扫描报告

当前学位论文使用了 `gb7714-2015` 参考文献格式，在该格式下 `\cite{...}` 默认会渲染为上标形式（例如 `^{[1]}`）。
如果在行文中直接把 `\cite` 当作名词主语/宾语使用（例如“在 \cite 中指出”、“根据 \cite”），编译出来的 PDF 会出现主语缺失的问题（变成“在 $^{[1]}$ 中指出”、“根据 $^{[1]}$”），会显著破坏中文学术表达。

## 1. Undefined reference / citation 检查结果

已检查完整编译日志 `out/zjuthesis.log`。当前**没有真实的**：
- `Undefined citation`
- `Undefined reference`

也就是说，当前全文引用系统本身是可解析的；此前单文件 `lsp_diagnostics` 中出现的大量 `Undefined reference`，主要是单文件 LaTeX 诊断的交叉引用误报，而不是完整编译下的实际错误。

## 2. 已确认需要补主语的 Citation 位置（非 backup 文件）

以下位置已经确认为“在当前上标引用格式下，最好补充明确主语/名词”的用法。第二轮处理中，遵循了新的更强规则：**若能用具体方法名（中文）或作者名，就不再使用泛化的“文献”**。

### Paper 1 (Cosserat Rod)

| 文件路径 | 行号 | 问题类型 | 当前处理结果 |
|---|---:|---|---|
| `paper1/2_representation.tex` | 3 | `文献~\cite 中` 前后空格与衔接不自然 | 已改为更紧凑的 `文献~\cite{...}中的...`；此处缺少稳定方法名，保留 generic 写法 |
| `paper1/2_representation.tex` | 33 | `文献~\cite 中` 前后空格与衔接不自然 | 已改为更紧凑的 `文献~\cite{...}中的...`；此处缺少稳定方法名，保留 generic 写法 |
| `paper1/3_simulation.tex` | 84 | `遵循文献~\cite 的方法` 缺少方法名词承接 | 第二轮已升级为 `遵循 Pan 等人~\cite{...}的方法` |
| `paper1/3_simulation.tex` | 115 | `如~\cite 那样` 主语缺失 | 第二轮已升级为 `如 Pan 等人~\cite{...}那样` |
| `paper1/4_results.tex` | 108 | `文献~\cite 亦包含...` 需要具体主语 | 第二轮已升级为 `Deul 等人~\cite{...}的方法亦包含...` |
| `paper1/4_results.tex` | 139 | `并由~\cite 提供...` 主语缺失 | 第二轮已升级为 `并由 Thomas 算法~\cite{...}提供...` |
| `paper1/app_active_set.tex` | 3 | `根据~\cite` 主语缺失 | 第二轮已升级为 `根据 Bridson 等人~\cite{...}的方法` |
| `paper1/app_energy_terms.tex` | 3 | `见~\cite` 略显裸露 | 第二轮已升级为 `见离散弹性杆模型~\cite{...}` |

### Paper 2 (Distorted Mesh)

| 文件路径 | 行号 | 问题类型 | 当前处理结果 |
|---|---:|---|---|
| `paper2/4_method.tex` | 21 | `与 \cite 中...` 主语缺失 | 第二轮已升级为 `与 Chen 等人~\cite{...}中...` |
| `paper2/4_method.tex` | 23 | `在 \cite 中，他们...` 主语缺失 | 第二轮已升级为 `Chen 等人~\cite{...}通过...` |
| `paper2/4_method.tex` | 36 | `可在~\cite 中找到` 主语缺失 | 保留 generic：`可在文献~\cite{...}中找到`；混合引用缺少单一稳定方法名 |
| `paper2/4_method.tex` | 53 | `遵循~\cite` 主语缺失 | 第二轮已升级为 `遵循 Chen 等人~\cite{...}的方法` |
| `paper2/5_results.tex` | 92 | `我们使用 \cite 提出的...` 主语缺失 | 第二轮已升级为 `我们使用旋转-应变坐标~\cite{...}` |
| `paper2/5_results.tex` | 92 | `该策略也在 \cite 中采用` 主语缺失 | 第二轮已升级为 `该策略也在数值粗化方法~\cite{...}中采用` |

### Paper 3 (Primal-Dual Modes)

| 文件路径 | 行号 | 问题类型 | 当前处理结果 |
|---|---:|---|---|
| `paper3/4_results.tex` | 63 | `这与 ...~\cite 类似` 表述略松散 | 第二轮已升级为 `这与 SMPI 等模拟框架~\cite{...}中的做法类似` |

## 3. 扫描后判定为“无需修改”的误报

以下位置曾被自动脚本标记，但人工复核后认为**不需要改**：

| 文件路径 | 行号 | 原因 |
|---|---:|---|
| `paper1/3_simulation.tex` | 62 | `更多细节可参阅文献~\cite{...}` 已有明确名词，且多篇文献并列时不适合强行指定单一方法名 |
| `paper2/3_background.tex` | 9 | `文献~\cite{...}指出` 已有主语，不需要修改 |
| `paper3/2_foundation.tex` | 125 | `在某些文献~\cite{...}中` 已有主语与介词结构，不需要修改 |

## 4. 备注

- `intro` 中大多数 `\cite` 都位于句末或图题出处位置，当前不存在明显“主语缺失”问题。
- `paper3/1_intro.tex` 中的 `SLEPc~\cite`、`MUMPS~\cite`、`LOBPCG~\cite` 等都属于“方法/软件名词 + 引用”的标准写法，不需要补主语。
- `paper2/5_results.tex` 中的 `Thingi10k~\cite 数据集` 与 `Tetgen~\cite` 也属于可接受的名词修饰结构。
- 第二轮处理的原则是：**能用具体方法名 / 作者名时不用 generic 的“文献”**；只有在混合引用、上下文缺少稳定单一方法名时，才保留 `文献~\cite` 这一中性写法。