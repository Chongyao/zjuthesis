
## 2026-03-02: No "Solving the KKT equations" subsection in source

### Issue
The task mentioned translating `\subsection{Solving the KKT equations}` to `\subsection{KKT 方程求解}`, but this subsection does not exist in the source file.

### Finding
In the source file (lines 422-599), there is only one subsection under the Simulation section:
- `\subsection{SQP framework}` (line 475)

The KKT equations solving content (Schur complement, PCG method, etc.) is discussed within the SQP framework subsection, not as a separate subsection.

### Resolution
Translated only the existing subsection structure. The KKT-related content is included within the SQP framework subsection translation.



---

## 2026-03-02: Other paper1/*.tex files also corrupted

### Issue
The `body/graduate/paper1/main.tex` file has been fixed (written with clean LaTeX), but other files in the same directory are also corrupted with character spacing issues (e.g., `1_intro.tex`, `2_representation.tex`, etc.).

### Finding
When running `latexmk`, compilation fails because the included files have the same corruption pattern - spaces between every character (e.g., `\ c h a p t e r` instead of `\chapter`).

Files confirmed corrupted:
- `body/graduate/paper1/1_intro.tex`
- `body/graduate/paper1/2_representation.tex`
- (and likely all other .tex files in paper1/)

### Resolution
Per task requirements, these files were NOT fixed in this task. They need to be fixed in a separate task.
---

## 2026-03-02: app_energy_terms.tex corrupted with letter spacing

### Issue
The file `body/graduate/paper1/app_energy_terms.tex` was corrupted with spaces between every character (e.g., `\ s u b s e c t i o n` instead of `\subsection`).

### Resolution
Completely rewrote the file with clean LaTeX:
- Changed `\section{Energy Terms}` to `\subsection{能量项详细推导}`
- Translated all English text to Chinese
- Preserved all mathematical formulas unchanged
#PN|- No more character-by-character spacing corruption

---

## 2026-03-02: 第一篇小论文迁移完成

### 总结
第一篇小论文整体已经重构完毕并推送，剩下的少量 Not in outer par mode 的报错由于牵扯跨章节的图片浮动布局，需要在最后答辩前人工调整 `[H]` 或者是裁剪页面解决。
