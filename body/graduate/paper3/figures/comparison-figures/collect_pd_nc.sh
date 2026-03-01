#!/bin/bash

# ==========================================
# PD 方法数据整理脚本 (输出到 CSV)
# ==========================================

# 1. 确定搜索路径
# 如果没有参数，默认为当前目录
SEARCH_DIR="${1:-.}"

# 2. 推断模型名称 (用于命名 CSV)
# 进入目标目录获取绝对路径的文件夹名
# 例如: ./rock_arm -> rock_arm
# 例如: . (而在 rock_arm 目录下) -> rock_arm
MODEL_NAME=$(basename "$(cd "$SEARCH_DIR" && pwd)")
METHOD_NAME="PD-NC"
OUTPUT_FILE="${MODEL_NAME}_${METHOD_NAME}.csv"

# 3. 写入 CSV 表头
echo "Modes,Err_Mean,Err_2norm,T_Sub,T_Ifc,T_RedCon,T_RedSol,T_Total" > "$OUTPUT_FILE"

echo "正在处理目录: $SEARCH_DIR"
echo "输出文件目标: $OUTPUT_FILE"

# 4. 遍历与提取
# 使用 sort -V 确保数字排序 (NEP_50 在 NEP_100 前)
find "$SEARCH_DIR" -maxdepth 1 -type d -name "NEP_*_PD_NC_*" | sort -V | while read folder; do
    
    # 解析模态数
    folder_name=$(basename "$folder")
    num_modes=$(echo "$folder_name" | cut -d'_' -f2)

    # 支持 run.log 和 result.log 两种日志文件名
    if [ -f "$folder/run.log" ]; then
        log_file="$folder/run.log"
    elif [ -f "$folder/result.log" ]; then
        log_file="$folder/result.log"
    else
        continue
    fi

    if [ -f "$log_file" ]; then
        
        # === A. 提取误差 ===
        # 逻辑：匹配 ": 数字" 避免抓到时间戳
        err_mean=$(grep "error of eigen values (Mean)" "$log_file" | tail -n1 | grep -oE ": [0-9]+\.[0-9]+e[-+][0-9]+" | awk '{print $2}')
        err_2norm=$(grep "error of eigen values (2-norm)" "$log_file" | tail -n1 | grep -oE ": [0-9]+\.[0-9]+e[-+][0-9]+" | awk '{print $2}')
        
        # 如果为空，CSV中通常留空或填NaN
        [ -z "$err_mean" ] && err_mean="NaN"
        [ -z "$err_2norm" ] && err_2norm="NaN"

        # === B. 提取并统计耗时 ===
        
        # 1. T_Sub (求和): 匹配 "time: 数字"
        t_sub=$(grep "CMS::solve time" "$log_file" | grep -oE "time: [0-9]+\.[0-9]+" | awk '{sum+=$2} END {print sum}')
        
        # 2. T_Ifc: 匹配 "cost 数字"
        t_ifc=$(grep "set interface modes cost" "$log_file" | tail -n1 | grep -oE "cost [0-9]+\.[0-9]+" | awk '{print $2}')

        # 3. T_RdCon: 匹配 "cost 数字"
        t_red_c=$(grep "construct reduced K, M cost" "$log_file" | tail -n1 | grep -oE "cost [0-9]+\.[0-9]+" | awk '{print $2}')

        # 4. T_RdSol: 匹配 "cost 数字"
        t_red_s=$(grep "solve reduced eigen cost" "$log_file" | tail -n1 | grep -oE "cost [0-9]+\.[0-9]+" | awk '{print $2}')

        # === C. 计算总和 ===
        t_sub=${t_sub:-0}
        t_ifc=${t_ifc:-0}
        t_red_c=${t_red_c:-0}
        t_red_s=${t_red_s:-0}
        
        # awk 计算总和
        t_total=$(awk "BEGIN {print $t_sub + $t_ifc + $t_red_c + $t_red_s}")

        # === D. 写入 CSV 行 ===
        echo "$num_modes,$err_mean,$err_2norm,$t_sub,$t_ifc,$t_red_c,$t_red_s,$t_total" >> "$OUTPUT_FILE"
    fi
done

echo "完成！已保存为: $OUTPUT_FILE"