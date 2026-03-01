#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
combine_jsons.py

此脚本用于预处理，将 'aggregate_all_benchmarks_to_six.sh' 脚本生成的
6 个单独的 JSON 数组文件合并为 1 个单独的 JSON 对象文件。

这个合并后的文件 (all_benchmarks_combined.json) 将作为
'plot_scaling_benchmarks.py' 脚本的统一数据输入。
"""

import json
import sys

# 定义 6 个输入文件和 1 个输出文件
INPUT_FILES = {
    "weak-pd": "weak-pd_benchmarks.json",
    "weak-sp": "weak-sp_benchmarks.json",
    "weak-gt": "weak-gt_benchmarks.json",
    "strong-pd": "strong-pd_benchmarks.json",
    "strong-sp": "strong-sp_benchmarks.json",
    "strong-gt": "strong-gt_benchmarks.json"
}

OUTPUT_FILE = "all_benchmarks_combined.json"

def main():
    """
    主函数：加载 6 个 JSON，合并，然后保存。
    """
    combined_data = {}

    print("开始合并 JSON 文件...")

    for key, file_name in INPUT_FILES.items():
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                #
                data = json.load(f) 
                combined_data[key] = data
                print(f"  [成功] 加载了 {file_name} (作为 '{key}')，包含 {len(data)} 个条目。")
        
        except FileNotFoundError:
            print(f"  [!! 警告 !!] 文件未找到: {file_name}。 '{key}' 键将为空。")
            combined_data[key] = []
        except json.JSONDecodeError:
            print(f"  [!! 错误 !!] 文件 {file_name} 不是有效的 JSON。 '{key}' 键将为空。")
            combined_data[key] = []
        except Exception as e:
            print(f"  [!! 错误 !!] 加载 {file_name} 时发生未知错误: {e}")
            combined_data[key] = []

    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(combined_data, f, indent=2)
        
        print(f"\n合并成功！")
        print(f"所有数据已写入: {OUTPUT_FILE}")

    except Exception as e:
        print(f"\n[!!! 严重错误 !!!] 无法写入最终文件 {OUTPUT_FILE}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
    