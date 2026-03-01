# Bug Fix: collect_pd.sh 无法处理 cat 模型数据

## 问题描述

`collect_pd.sh` 脚本在处理 `comparison-data/cat` 目录时无法提取任何数据。

## 根本原因

存在两个问题：

### 1. 文件夹命名不一致

| 模型 | PD 文件夹命名格式 | 示例 |
|------|------------------|------|
| rock_arm | `NEP_*_PD` | `NEP_100_PD` |
| breaker | `NEP_*_PD` | `NEP_100_PD` |
| cat | `NEP_*_PD_4` | `NEP_100_PD_4` |

原脚本使用 `-name "NEP_*_PD"` 匹配，无法匹配 `cat` 的 `NEP_*_PD_4` 格式。

### 2. 日志文件名不一致

| 模型 | 日志文件名 |
|------|-----------|
| rock_arm, breaker | `run.log` |
| cat (PD_4) | `result.log` |

原脚本硬编码 `log_file="$folder/run.log"`，无法找到 `cat` 的日志文件。

## 修复方案

1. 修改 find 命令以匹配两种命名格式：
   ```bash
   find "$SEARCH_DIR" -maxdepth 1 -type d \( -name "NEP_*_PD" -o -name "NEP_*_PD_*" \)
   ```

2. 添加日志文件名检测逻辑：
   ```bash
   if [ -f "$folder/run.log" ]; then
       log_file="$folder/run.log"
   elif [ -f "$folder/result.log" ]; then
       log_file="$folder/result.log"
   else
       continue
   fi
   ```
