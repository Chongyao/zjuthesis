#!/bin/bash

# ==========================================
# AMLS 方法数据整理脚本 (输出到 CSV)
# ==========================================

SEARCH_DIR="${1:-.}"

# 1. 推断模型名称
MODEL_NAME=$(basename "$(cd "$SEARCH_DIR" && pwd)")
METHOD_NAME="AMLS"
OUTPUT_FILE="${MODEL_NAME}_${METHOD_NAME}.csv"

# 2. 写入 CSV 表头
# Setup: Metis分块 | Sub: 子结构变换 | RedSol: 缩减求解 | Recov: 恢复向量
echo "Modes,Err_Mean,Err_2norm,T_Setup,T_Sub,T_RedSol,T_Recov,T_Total" > "$OUTPUT_FILE"

echo "正在处理目录: $SEARCH_DIR"
echo "输出文件目标: $OUTPUT_FILE"

# 3. 遍历与提取
find "$SEARCH_DIR" -maxdepth 1 -type d -name "NEP_*_AMLS" | sort -V | while read folder; do
    
    # 解析模态数
    folder_name=$(basename "$folder")
    num_modes=$(echo "$folder_name" | cut -d'_' -f2)
    log_file="$folder/run.log"

    if [ -f "$log_file" ]; then
        
        # === A. 提取误差 ===
        # 尝试查找 Mean 误差 (如果有的话)
        err_mean=$(grep "Error of eigen values (Mean)" "$log_file" | tail -n1 | grep -oE ":[ ]*[0-9]+\.[0-9]+e[-+][0-9]+" | tr -d ': ')
        
        # 查找 2-norm 误差 (Log样例: Error of eigen values (2-norm):0.372728)
        # 注意：这里冒号后面可能紧跟数字，也可能有空格，正则处理 ":[ ]*数字"
        err_2norm=$(grep "Error of eigen values (2-norm)" "$log_file" | tail -n1 | grep -oE ":[ ]*[0-9]+\.[0-9]+" | tr -d ': ')
        
        [ -z "$err_mean" ] && err_mean="NaN"
        [ -z "$err_2norm" ] && err_2norm="NaN"

        # === B. 提取耗时 (精确匹配关键词) ===
        
        # 1. T_Setup: metisNodeNDP time
        t_setup=$(grep "metisNodeNDP" "$log_file" | tail -n1 | grep -oE "time: [0-9]+\.[0-9]+" | awk '{print $2}')
        
        # 2. T_Sub: subsystem transformation time
        t_sub=$(grep "subsystem transformation time" "$log_file" | tail -n1 | grep -oE "time: [0-9]+\.[0-9]+" | awk '{print $2}')

        # 3. T_RedSol: reduced eigen solve time
        t_red_sol=$(grep "reduced eigen solve time" "$log_file" | tail -n1 | grep -oE "time: [0-9]+\.[0-9]+" | awk '{print $2}')

        # 4. T_Recov: recover eigenvector time
        t_recov=$(grep "recover eigenvector time" "$log_file" | tail -n1 | grep -oE "time: [0-9]+\.[0-9]+" | awk '{print $2}')

        # === C. 计算总和 ===
        t_setup=${t_setup:-0}
        t_sub=${t_sub:-0}
        t_red_sol=${t_red_sol:-0}
        t_recov=${t_recov:-0}
        
        # 累加所有分块时间
        t_total=$(awk "BEGIN {print $t_setup + $t_sub + $t_red_sol + $t_recov}")

        # === D. 写入 CSV ===
        echo "$num_modes,$err_mean,$err_2norm,$t_setup,$t_sub,$t_red_sol,$t_recov,$t_total" >> "$OUTPUT_FILE"
    fi
done

echo "完成！已保存为: $OUTPUT_FILE"