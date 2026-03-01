#!/bin/bash

# ==========================================
# AMLS 有效特征值提取脚本
# 目标 Log 行: "Number of valid eigenvalues ... : 8"
# 输出列: algorithm, nev, time
# ==========================================

SEARCH_DIR="${1:-.}"
OUTPUT_FILE="amls_valid_nev.csv"

# 1. 写入 CSV 表头
echo "algorithm,nev,time" > "$OUTPUT_FILE"

echo "正在扫描目录: $SEARCH_DIR"

# 2. 遍历 NEP_*_AMLS 文件夹
# sort -V 保证按数字顺序处理 (NEP_100, NEP_120...)
find "$SEARCH_DIR" -maxdepth 1 -type d -name "NEP_*_AMLS" | sort -V | while read folder; do
    
    log_file="$folder/run.log"

    if [ -f "$log_file" ]; then
        
        # === A. 提取有效特征值数量 (nev) ===
        # 目标行样例: Number of valid eigenvalues (cumulative 2-norm error < 1.000000e-04): 8
        # 逻辑: 找到包含关键词的行 -> 提取冒号后的整数
        nev=$(grep "Number of valid eigenvalues" "$log_file" | tail -n1 | awk -F': ' '{print $2}' | tr -d '\r')
        
        # === B. 提取总耗时 (time) ===
        # 目标行样例: AMLS Elapsed time: 38.045422(s)
        # 逻辑: 找到关键词 -> 提取数字
        time_val=$(grep "AMLS Elapsed time" "$log_file" | tail -n1 | grep -oE "[0-9]+\.[0-9]+")
        
        # === C. 写入 CSV ===
        # 只有当两个数据都提取成功时才写入
        if [ -n "$nev" ] && [ -n "$time_val" ]; then
            echo "AMLS,$nev,$time_val" >> "$OUTPUT_FILE"
        else
            # 可选：打印警告以便调试
            # echo "Warning: Data missing in $folder"
            :
        fi
    fi
done

echo "完成！已生成文件: $OUTPUT_FILE"
# 打印前几行预览
head -n 5 "$OUTPUT_FILE"