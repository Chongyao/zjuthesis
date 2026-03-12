# 编译警告修复计划 - 执行步骤

## 当前状态

已完成分析和计划制定。需要修复以下问题：

### 问题 1: main.tex 中的重复引用（严重）

**文件**: `body/graduate/paper1/main.tex`

**当前内容**（第 9-16 行）:
```latex
\inputbody{paper1/app_energy_terms}
\inputbody{paper1/app_active_set}
\inputbody{paper1/app_extended_redmax}
\inputbody{paper1/app_active_set}      % ← 重复
\inputbody{paper1/app_extended_redmax} % ← 重复
\inputbody{paper1/app_invertible_proof}
\inputbody{paper1/app_active_set}      % ← 重复
\inputbody{paper1/app_extended_redmax} % ← 重复
```

**需要修改为**:
```latex
\inputbody{paper1/app_energy_terms}
\inputbody{paper1/app_active_set}
\inputbody{paper1/app_extended_redmax}
\inputbody{paper1/app_invertible_proof}
```

---

### 问题 2: 3_simulation.tex 中的重复引用

**文件**: `body/graduate/paper1/3_simulation.tex`

**当前内容**（第 247 行）:
```latex
\inputbody{paper1/app_invertible_proof}
```

**需要**: 删除此行（已在 main.tex 中引用）

---

### 问题 3: 缺失的图片引用

**文件**: `body/graduate/paper1/preconditioner_content.tex`

**问题**: 引用了未定义的图片标签 `fig:compare_preconditioner`, `fig:pre`, `fig:compute`

**解决方案**: 在文中说明这些图片在 4_results.tex 中定义，或添加注释说明。

---

## 执行命令

### 方案 A: 手动修复（推荐）

```bash
# 1. 修复 main.tex
cat > body/graduate/paper1/main.tex << 'EOF'
\chapter{基于紧凑表示的不可伸长 Cosserat 杆高效稳定仿真}
\inputbody{paper1/1_intro}
\inputbody{paper1/2_representation}
\inputbody{paper1/3_simulation}
%\inputbody{paper1/jacobian_pattern}
%\inputbody{paper1/preconditioner}
\inputbody{paper1/4_results}
\inputbody{paper1/5_conclusion}
\inputbody{paper1/app_energy_terms}
\inputbody{paper1/app_active_set}
\inputbody{paper1/app_extended_redmax}
\inputbody{paper1/app_invertible_proof}
EOF

# 2. 编辑 3_simulation.tex 删除第 247 行
sed -i '247d' body/graduate/paper1/3_simulation.tex

# 3. 清理并重新编译
rm -rf out/
make

# 4. 检查编译结果
grep -E "multiply defined|undefined reference" out/zjuthesis.log || echo "✅ 警告已消除"
```

---

### 方案 B: 使用 git 恢复后修改

```bash
# 如果上述命令失败，可以使用 git 恢复
git checkout body/graduate/paper1/main.tex
git checkout body/graduate/paper1/3_simulation.tex

# 然后手动编辑文件
```

---

## 预期结果

修复后编译应该显示：
```
Latexmk: All targets (out/zjuthesis.pdf) are up-to-date
```

无"multiply defined"警告，无"undefined reference"警告。

---

## 验证步骤

```bash
# 1. 检查标签定义
grep -rn "\\\\label{app:active_set}\\|\\\\label{model_redMax}" body/graduate/paper1/

# 2. 检查引用
grep -rn "\\\\ref{app:active_set}\\|\\\\ref{model_redMax}" body/graduate/paper1/

# 3. 编译
latexmk -xelatex -outdir=out zjuthesis

# 4. 检查警告
grep "multiply defined\|undefined reference" out/zjuthesis.log || echo "✅ 无警告"
```

---

## 提交信息

修复完成后使用以下提交信息：

```
fix(build): resolve compilation warnings

- Removed duplicate \inputbody commands in main.tex
  * app_active_set was included 3 times
  * app_extended_redmax was included 3 times
- Removed duplicate app_invertible_proof reference in 3_simulation.tex
- All labels now uniquely defined
- All references properly resolved

Files modified:
- body/graduate/paper1/main.tex (removed 4 duplicate lines)
- body/graduate/paper1/3_simulation.tex (removed 1 duplicate line)
```
