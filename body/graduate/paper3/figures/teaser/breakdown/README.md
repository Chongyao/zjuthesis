# Time Breakdown Visualization

这个目录包含了用于分析和展示时间开销分布的数据和脚本。

## 数据文件

- `breakdown_NEP100_NEV500.json`: 原始运行日志 (NEV=500)，包含详细的时间拆解。
- `breakdown_NEP100_NEV3000.json`: 估算数据 (NEV=3000)，基于前者修改了 Reduce 阶段的时间。

## 绘图脚本

**`plot_breakdown_pie.py`**
   - 生成 `time_breakdown_pie.pdf/png`
   - 类型: 双环饼图 (Nested Pie Chart)
   - 外环: 展示四大阶段 (Interior Eigenmodes, Interface Modes, Matrix Reducing, Reduced Solve) 在总时间中的占比
   - 内环: 展示各阶段内部的组件分解，通过阴影区分计算/空闲/通信类型

## 使用方法

```bash
# 生成图表
python3 plot_breakdown_pie.py
```

## 输出

- `time_breakdown_pie.pdf/png`: 时间占比饼图

