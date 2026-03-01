#!/bin/bash

# ==========================================
# CMS-INTRD 方法数据整理脚本
# ==========================================

SEARCH_DIR="${1:-.}"

# 1. 推断模型名称
MODEL_NAME=$(basename "$(cd "$SEARCH_DIR" && pwd)")
METHOD_NAME="CMS-INTRD"
OUTPUT_FILE="${MODEL_NAME}_${METHOD_NAME}.csv"

# 2. 写入 CSV 表头
# Fact:分解 | Stat:静态模态 | Ifc:接口处理 | RedCon:构造缩减 | RedSol:缩减求解
echo "Modes,Err_Mean,Err_2norm,T_Fact,T_Stat,T_Ifc,T_RedCon,T_RedSol,T_Total" > "$OUTPUT_FILE"

echo "正在处理目录: $SEARCH_DIR"
echo "输出文件目标: $OUTPUT_FILE"

# 3. 遍历与提取
find "$SEARCH_DIR" -maxdepth 1 -type d \( -name "NEP_*_CMS-INTRD" -o -name "NEP_*_CMSINTRD*" \) | sort -V | while read folder; do
    
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
        err_mean=$(grep "error of eigen values (Mean)" "$log_file" | tail -n1 | grep -oE ": [0-9]+\.[0-9]+e[-+][0-9]+" | awk '{print $2}')
        err_2norm=$(grep "error of eigen values (2-norm)" "$log_file" | tail -n1 | grep -oE ": [0-9]+\.[0-9]+e[-+][0-9]+" | awk '{print $2}')
        
        [ -z "$err_mean" ] && err_mean="NaN"
        [ -z "$err_2norm" ] && err_2norm="NaN"

        # === B. 提取耗时 (核心分块) ===
        
        # 1. T_Fact: factorization of stiffness
        t_fact=$(grep "factorization of stiffness" "$log_file" | tail -n1 | grep -oE "cost [0-9]+\.[0-9]+" | awk '{print $2}')

        # 2. T_Stat: solving for static modes
        t_stat=$(grep "solving for static modes" "$log_file" | tail -n1 | grep -oE "cost [0-9]+\.[0-9]+" | awk '{print $2}')

        # 3. T_Ifc: 接口相关操作总和 (将几个小的步骤加起来)
        #   - extracting coupling matrices
        #   - extract Kbb Mbb
        #   - reduction cost
        #   - interface eigenvalue solve
        #   - final assembly
        t_ifc_1=$(grep "extracting coupling matrices" "$log_file" | tail -n1 | grep -oE "cost [0-9]+\.[0-9]+" | awk '{print $2}')
        t_ifc_2=$(grep "extract Kbb Mbb" "$log_file" | tail -n1 | grep -oE "cost [0-9]+\.[0-9]+" | awk '{print $2}')
        t_ifc_3=$(grep "reduction cost" "$log_file" | tail -n1 | grep -oE "cost [0-9]+\.[0-9]+" | awk '{print $2}')
        t_ifc_4=$(grep "interface eigenvalue solve" "$log_file" | tail -n1 | grep -oE "cost [0-9]+\.[0-9]+" | awk '{print $2}')
        t_ifc_5=$(grep "final assembly" "$log_file" | tail -n1 | grep -oE "cost [0-9]+\.[0-9]+" | awk '{print $2}')

        # 计算 T_Ifc 总和
        t_ifc=$(awk "BEGIN {print ${t_ifc_1:-0} + ${t_ifc_2:-0} + ${t_ifc_3:-0} + ${t_ifc_4:-0} + ${t_ifc_5:-0}}")

        # 4. T_RedCon: construct reduced K, M
        t_red_c=$(grep "construct reduced K, M cost" "$log_file" | tail -n1 | grep -oE "cost [0-9]+\.[0-9]+" | awk '{print $2}')

        # 5. T_RedSol: solve reduced eigen
        t_red_s=$(grep "solve reduced eigen cost" "$log_file" | tail -n1 | grep -oE "cost [0-9]+\.[0-9]+" | awk '{print $2}')

        # === C. 计算总耗时 ===
        t_fact=${t_fact:-0}
        t_stat=${t_stat:-0}
        t_red_c=${t_red_c:-0}
        t_red_s=${t_red_s:-0}
        
        # 注意: T_Ifc 已经是计算过的变量，不需要再默认0 (awk output is always valid number or 0)
        
        t_total=$(awk "BEGIN {print $t_fact + $t_stat + $t_ifc + $t_red_c + $t_red_s}")

        # === D. 写入 CSV ===
        echo "$num_modes,$err_mean,$err_2norm,$t_fact,$t_stat,$t_ifc,$t_red_c,$t_red_s,$t_total" >> "$OUTPUT_FILE"
    fi
done

echo "完成！已保存为: $OUTPUT_FILE"