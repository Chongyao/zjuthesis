# 编译警告修复计划

## 问题分析

当前编译警告：
1. **重复定义标签** (18 个): `app:active_set`, `eq: collision constraint`, `model_redMax`, `app:invertible`, `alg: active_set`
2. **未定义引用** (4 个): `fig:compare_preconditioner`, `fig:pre`, `fig:compute`
3. **字体警告**: 无害，可忽略

## 根本原因

### main.tex 中重复引用附录文件

```
第 10 行：\inputbody{paper1/app_active_set}
第 11 行：\inputbody{paper1/app_extended_redmax}
第 12 行：\inputbody{paper1/app_active_set}      ← 重复
第 13 行：\inputbody{paper1/app_extended_redmax} ← 重复
第 14 行：\inputbody{paper1/app_invertible_proof}
第 15 行：\inputbody{paper1/app_active_set}      ← 重复
第 16 行：\inputbody{paper1/app_extended_redmax} ← 重复
```

### 3_simulation.tex 中重复引用

```
第 247 行：\inputbody{paper1/app_invertible_proof}
```

而 main.tex 第 14 行也已经引用了该文件。

## 修复方案

### 任务 1: 清理 main.tex 中的重复引用

**目标文件**: `body/graduate/paper1/main.tex`

**修改内容**: 删除第 12-16 行的重复引用，只保留：
```latex
\inputbody{paper1/app_energy_terms}
\inputbody{paper1/app_active_set}
\inputbody{paper1/app_extended_redmax}
\inputbody{paper1/app_invertible_proof}
```

### 任务 2: 清理 3_simulation.tex 中的重复引用

**目标文件**: `body/graduate/paper1/3_simulation.tex`

**修改内容**: 删除第 247 行的 `\inputbody{paper1/app_invertible_proof}`，因为已在 main.tex 中引用。

### 任务 3: 修复缺失的图片引用

**问题**: `fig:compare_preconditioner`, `fig:pre`, `fig:compute` 未定义

**原因**: preconditioner_content.tex 中引用了这些图片，但图片环境被注释或缺失。

**解决方案**: 在 preconditioner_content.tex 中添加图片环境的占位符或注释说明。

### 任务 4: 验证编译

```bash
rm -rf out/
make
```

预期结果：无重复标签警告，无未定义引用警告。

## 执行步骤

1. 修复 main.tex - 删除重复引用
2. 修复 3_simulation.tex - 删除重复引用
3. 修复 preconditioner_content.tex - 添加图片占位符
4. 清理并重新编译
5. 验证警告已消除
6. 提交更改

## 成功标准

- ✅ 无"multiply defined"警告
- ✅ 无"undefined reference"警告
- ✅ PDF 正常生成
- ✅ 所有标签唯一定义
