#!/usr/bin/env python3
"""
从 log 目录中提取数据并生成 CSV 文件，格式仿照 results.csv
"""

import os
import re
import csv

LOG_DIR = "/home/zcy/workspace/records/primal-dual_modes/comparison-figures/lady/log"
OUTPUT_FILE = "/home/zcy/workspace/records/primal-dual_modes/comparison-figures/lady/log_results.csv"

def parse_log_file(log_path):
    """解析单个 log 文件，提取关键数据"""
    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 移除 ANSI 颜色代码
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    content = ansi_escape.sub('', content)

    result = {}

    # 提取 CMS::solve time (有两次，需要求和)
    cms_solve_times = re.findall(r'\[TOC\] CMS::solve time: ([\d.]+) s', content)
    if cms_solve_times:
        result['solve_time'] = sum(float(t) for t in cms_solve_times)

    # 提取 construct reduced K, M cost
    construct_match = re.search(r'TOC: construct reduced K, M cost ([\d.]+) seconds', content)
    if construct_match:
        result['construct_time'] = float(construct_match.group(1))

    # 提取 solve reduced eigen cost
    reduce_match = re.search(r'TOC: solve reduced eigen cost ([\d.]+) seconds', content)
    if reduce_match:
        result['reduce_time'] = float(reduce_match.group(1))

    # 提取 set interface modes cost
    interface_match = re.search(r'TOC: set interface modes cost ([\d.]+) seconds', content)
    if interface_match:
        result['interface_time'] = float(interface_match.group(1))

    # 提取 error of eigen values (Mean)
    accuracy_match = re.search(r'error of eigen values \(Mean\): ([\d.eE+-]+)', content)
    if accuracy_match:
        result['accuracy'] = float(accuracy_match.group(1))

    # 计算总时间
    if 'solve_time' in result and 'construct_time' in result and 'reduce_time' in result and 'interface_time' in result:
        result['time'] = result['solve_time'] + result['construct_time'] + result['reduce_time'] + result['interface_time']

    return result

def parse_dir_name(dir_name):
    """从目录名解析 nep 和 group 信息
    目录名格式: NEP_X_PD_Y (如 NEP_100_PD_4)
    """
    match = re.match(r'NEP_(\d+)_PD_(\d+)', dir_name)
    if match:
        nep = int(match.group(1))
        pd = int(match.group(2))
        # 根据 results.csv 的格式，group 对应关系: 4->4_5, 6->6_7, 8->8_9
        group_map = {4: '4_5', 6: '6_7', 8: '8_9'}
        group = group_map.get(pd, f'{pd}_{pd+1}')
        return nep, group
    return None, None

def main():
    results = []

    # 遍历 log 目录下的所有子目录
    for dir_name in sorted(os.listdir(LOG_DIR)):
        dir_path = os.path.join(LOG_DIR, dir_name)
        if not os.path.isdir(dir_path):
            continue

        log_file = os.path.join(dir_path, 'run.log')
        if not os.path.exists(log_file):
            continue

        nep, group = parse_dir_name(dir_name)
        if nep is None:
            continue

        log_data = parse_log_file(log_file)
        if not log_data:
            continue

        row = {
            'model_name': 'a_lady',
            'algorithm': 'Primal-Dual IMR',
            'nep': nep,
            'group': group,
            'time': log_data.get('time', ''),
            'accuracy': log_data.get('accuracy', ''),
            'reduce_time': log_data.get('reduce_time', ''),
            'solve_time': log_data.get('solve_time', ''),
            'construct_time': log_data.get('construct_time', ''),
            'interface_time': log_data.get('interface_time', '')
        }
        results.append(row)

    # 按 nep 和 group 排序
    results.sort(key=lambda x: (x['nep'], x['group']))

    # 写入 CSV 文件
    fieldnames = ['model_name', 'algorithm', 'nep', 'group', 'time', 'accuracy',
                  'reduce_time', 'solve_time', 'construct_time', 'interface_time']

    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"数据已提取并保存到: {OUTPUT_FILE}")
    print(f"共处理 {len(results)} 条记录")

if __name__ == '__main__':
    main()
