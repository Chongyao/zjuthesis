import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    file_path = 'output.csv'
    if not os.path.exists(file_path):
        print(f"文件 {file_path} 不存在。")
        return

    try:
        # 读取CSV文件
        df = pd.read_csv(file_path)

        # 检查必要的列是否存在
        if 'conv' not in df.columns or 'time' not in df.columns:
            print("CSV文件中缺少 'conv' 或 'time' 列。")
            return

        plt.figure(figsize=(10, 6))

        # 如果有 'algorithm' 列，按算法分类着色
        if 'algorithm' in df.columns:
            algorithms = df['algorithm'].unique()
            for algo in algorithms:
                subset = df[df['algorithm'] == algo]
                plt.scatter(subset['conv'], subset['time'], label=algo, alpha=0.7)
            plt.legend(title='Algorithm')
        else:
            plt.scatter(df['conv'], df['time'], alpha=0.7)

        plt.title('Time vs nconv')
        plt.xlabel('nconv')
        plt.ylabel('time')
        plt.grid(True)
        
        # 保存图片
        output_img = 'plot_result.png'
        plt.savefig(output_img)
        print(f"图表已生成并保存为 {output_img}")
        
        # 显示图片 (如果在支持GUI的环境中)
        plt.show()

    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()
