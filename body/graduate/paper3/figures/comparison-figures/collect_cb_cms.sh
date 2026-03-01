#!/bin/bash

# ==========================================
# CB-CMS 方法数据整理脚本
# ==========================================

SEARCH_DIR="${1:-.}"

# 1. 推断模型名称
MODEL_NAME=$(basename "$(cd "$SEARCH_DIR" && pwd)")
METHOD_NAME="CB-CMS"
OUTPUT_FILE="${MODEL_NAME}_${METHOD_NAME}.csv"

# 2. 写入 CSV 表头
# Pre: 预处理 | Sub: 子结构求解 | Schur: 接口缩减(含K,M,T) | RedSol: 缩减求解
echo "Modes,Err_Mean,Err_2norm,T_Pre,T_Sub,T_Schur,T_RedSol,T_Total" > "$OUTPUT_FILE"

echo "正在处理目录: $SEARCH_DIR"
echo "输出文件目标: $OUTPUT_FILE"

# 3. 遍历与提取
find "$SEARCH_DIR" -maxdepth 1 -type d -name "NEP_*_CB-CMS" | sort -V | while read folder; do
    
    # 解析模态数
    folder_name=$(basename "$folder")
    num_modes=$(echo "$folder_name" | cut -d'_' -f2)
    log_file="$folder/run.log"

    if [ -f "$log_file" ]; then
        
        # === A. 提取误差 ===
        # 你的 Log 中 Error 放在最后，Mean 和 2-norm 都有
        # 格式: Error of eigen values (Mean): 2.003956e-02
        err_mean=$(grep "Error of eigen values (Mean)" "$log_file" | tail -n1 | grep -oE ": [0-9]+\.[0-9]+e[-+][0-9]+" | awk '{print $2}')
        err_2norm=$(grep "Error of eigen values (2-norm)" "$log_file" | tail -n1 | grep -oE ": [0-9]+\.[0-9]+e[-+][0-9]+" | awk '{print $2}')
        
        [ -z "$err_mean" ] && err_mean="NaN"
        [ -z "$err_2norm" ] && err_2norm="NaN"

        # === B. 提取并统计耗时 ===
        # 使用 grep -oE "time: [0-9...]" 避开颜色代码干扰
        
        # 1. T_Pre: preprocess time
        t_pre=$(grep "CMS::preprocess time" "$log_file" | tail -n1 | grep -oE "time: [0-9]+\.[0-9]+" | awk '{print $2}')
        
        # 2. T_Sub: solveSSystem time (子结构特征值求解)
        t_sub=$(grep "CMS::solveSSystem time" "$log_file" | tail -n1 | grep -oE "time: [0-9]+\.[0-9]+" | awk '{print $2}')

        # 3. T_Schur (接口缩减三部曲)
        # 3.1 求解 T 矩阵
        t_eq_t=$(grep "solveEquationDenseRHS for T time" "$log_file" | tail -n1 | grep -oE "time: [0-9]+\.[0-9]+" | awk '{print $2}')
        # 3.2 计算 K 的 Schur 补
        t_k_schur=$(grep "CMS::computeKSchurComplement time" "$log_file" | tail -n1 | grep -oE "time: [0-9]+\.[0-9]+" | awk '{print $2}')
        # 3.3 计算 M 的 Schur 补
        t_m_schur=$(grep "CMS::computeNormalMibAndMschur time" "$log_file" | tail -n1 | grep -oE "time: [0-9]+\.[0-9]+" | awk '{print $2}')
        
        # 处理可能的空值
        t_eq_t=${t_eq_t:-0}
        t_k_schur=${t_k_schur:-0}
        t_m_schur=${t_m_schur:-0}
        
        # 计算 Schur 总和
        t_schur=$(awk "BEGIN {print $t_eq_t + $t_k_schur + $t_m_schur}")

        # 4. T_RedSol: solveReduceMatrix time (缩减问题求解)
        t_red_s=$(grep "CMS::solveReduceMatrix time" "$log_file" | tail -n1 | grep -oE "time: [0-9]+\.[0-9]+" | awk '{print $2}')

        # === C. 计算总耗时 ===
        t_pre=${t_pre:-0}
        t_sub=${t_sub:-0}
        t_schur=${t_schur:-0}
        t_red_s=${t_red_s:-0}

        t_total=$(awk "BEGIN {print $t_pre + $t_sub + $t_schur + $t_red_s}")

        # === D. 写入 CSV ===
        echo "$num_modes,$err_mean,$err_2norm,$t_pre,$t_sub,$t_schur,$t_red_s,$t_total" >> "$OUTPUT_FILE"
    fi
done

echo "完成！已保存为: $OUTPUT_FILE"