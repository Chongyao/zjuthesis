import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

print("--- 开始生成 mu_and_sigma 图表 (统一样式) ---")

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style_config import get_style, apply_style

SCHEME = os.environ.get('PLOT_COLOR_SCHEME', 'teal_coral')
STYLE = get_style(SCHEME)
apply_style(STYLE, scale='double_column')

LABEL_FONTSIZE = STYLE.scaled_fontsize('label', 'double_column')
LEGEND_FONTSIZE = STYLE.scaled_fontsize('legend', 'double_column')
TICK_FONTSIZE = STYLE.scaled_fontsize('tick', 'double_column')
scale = 1.2
LABEL_FONTSIZE *= scale
LEGEND_FONTSIZE *= scale
TICK_FONTSIZE *= scale

MARKER_SIZE = 12
LINE_WIDTH = 4.0
FIG_SIZE = (5, 5)
DPI = 150
OUTPUT_FILE = 'mu_and_sigma_plot.png'

# --- 2. 加载数据 (水平线) ---
h_line_file = 'S1plusS1ShiftOrthErr1.6169e-07.txt'
h_line_value = None
try:
    with open(h_line_file, 'r') as f:
        h_line_value = float(f.readline().strip())
    print(f"成功读取水平线数值: {h_line_value}")
except FileNotFoundError:
    print(f"错误: 文件 '{h_line_file}' 未找到。")
except Exception as e:
    print(f"读取 '{h_line_file}' 时出错: {e}")

# --- 3. 加载数据 (曲线) ---
csv_file = '测试数据mu_and_sigma_clean.csv'
df = None
try:
    df = pd.read_csv(csv_file)
    print(f"成功加载 '{csv_file}'")
except FileNotFoundError:
    print(f"错误: 文件 '{csv_file}' 未找到。")
except Exception as e:
    print(f"读取 '{csv_file}' 时出错: {e}")


# --- 4. 创建绘图 (仅当数据都加载成功) ---
if df is not None and h_line_value is not None:
    if 'Magnitude' not in df.columns or 'Exact_Err' not in df.columns:
        print(f"错误: CSV 文件必须包含 'Magnitude' 和 'Exact_Err' 列。")
    else:
        df = df.sort_values(by='Magnitude')

        print("正在创建图表...")
        plt.figure(figsize=FIG_SIZE)
        ax = plt.gca()
        
        # 使用统一配色 (blue_orange scheme)
        # Primary blue for regularization, secondary orange for orthogonalization
        colors = [
            STYLE.method_colors['ours'],  # Blue #0173B2 for regularization
            STYLE.method_colors['cms'],   # Orange #DE8F05 for orthogonalization
        ]

        # 绘制曲线 (来自 CSV)
        ax.plot(
            df['Magnitude'], df['Exact_Err'],
            marker='o', linestyle='-', label='正则化',
            markersize=MARKER_SIZE, linewidth=LINE_WIDTH, color=colors[0]
        )

        # 绘制水平线 (来自 TXT)
        legend_label = f'正交化\n({h_line_value:.2e})'
        ax.axhline(
            y=h_line_value, color=colors[1], linestyle='--',
            linewidth=LINE_WIDTH, label=legend_label
        )

        # Y 轴对数
        ax.set_yscale('log')

        # 标签（无标题）
        ax.set_xlabel(r'$\mu/\lambda_{\min}$', fontsize=LABEL_FONTSIZE)
        ax.set_ylabel(r"$\epsilon_{ev}$", fontsize=LABEL_FONTSIZE)

        # 图例
        ax.legend(fontsize=LEGEND_FONTSIZE, frameon=False, loc=[0, 0.6])

        # 刻度
        ax.tick_params(axis='both', which='major', labelsize=TICK_FONTSIZE)

        # 黑色外框统一风格
        for spine in ax.spines.values():
            spine.set_edgecolor(STYLE.ui_colors['spine'])
            spine.set_linewidth(1.5)

        ax.grid(False)

        # 保存
        try:
            plt.tight_layout()
            plt.savefig(OUTPUT_FILE, dpi=DPI, bbox_inches='tight')
            if OUTPUT_FILE.lower().endswith('.png'):
                plt.savefig(OUTPUT_FILE[:-4] + '.pdf', dpi=DPI, bbox_inches='tight')
            print(f"\n成功保存图表到: {OUTPUT_FILE}")
        except Exception as e:
            print(f"保存图表时出错: {e}")

        print("--- 绘图完成 ---")
else:
    print("由于缺少一个或多个数据文件，跳过绘图。")

print("--- 脚本执行完毕 ---")
