#!/bin/bash

# ==========================================
# 自动化全流程脚本 (V4 - 采集/清洗/绘图)
# 功能：
# 1. 遍历模型 -> 调用采集脚本 (collect_*.sh)
# 2. 生成汇总表并清洗 NaN
# 3. [新增] 自动调用 Python 脚本生成对比图
# ==========================================

# --- 配置路径 ---
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DATA_ROOT="../comparison-data"
# 指定 Python 绘图脚本的路径 (假设它在当前脚本同级目录下)
PLOT_SCRIPT="${SCRIPT_DIR}/plot.py"

# --- 检查依赖 ---
if [ ! -d "$DATA_ROOT" ]; then
    echo "错误: 找不到数据目录 $DATA_ROOT"
    exit 1
fi

if ! command -v python &> /dev/null; then
    echo "错误: 未找到 python 命令，无法进行绘图。"
    echo "请确保已安装 python 并配置好环境变量。"
    exit 1
fi

if [ ! -f "$PLOT_SCRIPT" ]; then
    echo "警告: 未找到绘图脚本 $PLOT_SCRIPT"
    echo "脚本将只执行数据整理，不执行绘图。"
fi

echo "=== 开始批量处理 (V4: 采集 + 清洗 + 绘图) ==="

# 1. 遍历 comparison-data 下的所有子目录
for model_path in "$DATA_ROOT"/*; do
    if [ -d "$model_path" ]; then
        model_name=$(basename "$model_path")
        echo ">>> 正在处理模型: $model_name"

        # 定义输出目录 (例如 comparison-figures/rock_arm)
        output_dir="${SCRIPT_DIR}/${model_name}"
        mkdir -p "$output_dir"

        # --- 步骤 A: 生成各方法的详细 CSV ---
        declare -a scripts=("collect_amls.sh" "collect_cb_cms.sh" "collect_cms_intrd.sh" "collect_pd.sh" "collect_pd_nc.sh")
        
        for script in "${scripts[@]}"; do
            if [ -f "${SCRIPT_DIR}/$script" ]; then
                chmod +x "${SCRIPT_DIR}/$script"
                # 执行脚本
                "${SCRIPT_DIR}/$script" "$model_path" > /dev/null 2>&1
            fi
        done

        # 归档生成的详细 CSV
        mv "${SCRIPT_DIR}/${model_name}_"*.csv "$output_dir/" 2>/dev/null

        # --- 步骤 B: 生成该模型的【原始】汇总表 ---
        raw_summary="${output_dir}/${model_name}_summary.csv"
        echo "Method,Num_Modes,Error_2norm,Time_Total" > "$raw_summary"

        for csv_file in "$output_dir/${model_name}_"*.csv; do
            if [ -f "$csv_file" ]; then
                filename=$(basename "$csv_file")
                method_name=$(echo "$filename" | sed -e "s/^${model_name}_//" -e "s/\.csv$//")
                
                if [[ "$method_name" == *"summary"* ]]; then continue; fi
                if [ "$method_name" == "CMS-INTRD" ]; then time_col=9; else time_col=8; fi

                awk -F, -v meth="$method_name" -v tcol="$time_col" \
                    'NR>1 {print meth "," $1 "," $3 "," $tcol}' "$csv_file" >> "$raw_summary"
            fi
        done
        # echo "    已生成原始汇总: $(basename "$raw_summary")"

        # --- 步骤 C: 生成【清洗】汇总表 (去除 NaN) ---
        clean_summary="${output_dir}/${model_name}_summary_clean.csv"
        awk -F, 'NR==1 || ($3 != "NaN" && $4 != "NaN")' "$raw_summary" > "$clean_summary"
        echo "    已生成数据: $(basename "$clean_summary")"

        # --- 步骤 D: [新增] 自动绘图 ---
        if [ -f "$PLOT_SCRIPT" ]; then
            echo "    正在生成图表..."
            
            # 关键技巧：进入 output_dir 运行 python
            # 这样生成的 .png/.pdf 就会直接保存在模型文件夹内，而不是脚本所在目录
            pushd "$output_dir" > /dev/null
            
            # 调用上级目录的 plot_cms.py，并传入刚才生成的 clean csv 文件名
            # Python 脚本会自动读取这个文件并生成对应的 _plot.png
            python "$PLOT_SCRIPT" "$(basename "$clean_summary")"
            
            # 返回脚本目录
            popd > /dev/null
            
            echo "    图表已保存至: $output_dir"
        fi
    fi
done

echo "=== 全部完成 ==="