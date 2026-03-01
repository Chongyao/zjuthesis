# Modes Residual Plot

绘制模态残差图（对数坐标）。

## 数据

- **输入**: `residuals_nep50.csv`
- **格式**: CSV，包含 `index`, `eigenvalue`, `residual` 三列
- **模态范围**: 从 index=6 开始绘制

## 使用方法

```bash
# 使用默认配色（blue_orange）
python3 plot.py

# 使用其他配色
PLOT_COLOR_SCHEME=purple_yellow python3 plot.py
```

## 输出

- `modes_residual.pdf` - 矢量图
- `modes_residual.png` - 位图（300 DPI）

## 图表特性

- **横轴**: Mode Index (从 6 开始)
- **纵轴**: Residual (对数坐标)
- **配色**: 使用 `plot_style_config.py` 统一配色
- **样式**: 
  - 主色：primary color (ours)
  - 标记：圆圈 (o)
  - 线宽：1.5
  - 标记大小：3
  - 无网格线
  - 隐藏顶部和右侧边框
