# Whole Model Mode Shape Rendering

简洁的 ParaView 渲染脚本，使用 JSON 配置文件设置所有参数。

## 使用方法

```bash
# 使用 pvbatch 运行
pvbatch --mesa render.py
```

## 配置文件：config.json

所有参数都在 `config.json` 中配置：

### 主要配置项

```json
{
  "data_source": "/path/to/eigenvectors.vtk",
  "output_dir": ".",
  "resolution": [2146, 1358],
  "camera": { ... },
  "modes": [ ... ],
  "colormap": { ... }
}
```

### 相机参数

```json
"camera": {
  "ViewSize": [2146, 1358],
  "OrientationAxesVisibility": 0,
  "CenterOfRotation": [x, y, z],
  "UseToneMapping": 1,          // 启用色调映射
  "Exposure": 2.0,              // 曝光度
  "UseAmbientOcclusion": 1,     // 启用环境光遮蔽
  "CameraPosition": [x, y, z],
  "CameraFocalPoint": [x, y, z],
  "CameraViewUp": [x, y, z],
  "CameraFocalDisk": 1.0,
  "CameraParallelScale": 0.96
}
```

**关键渲染设置**（借鉴自 comparison-figures/board/plot_model.py）：
- `UseToneMapping`: 1 (启用)
- `Exposure`: 2.0
- `UseAmbientOcclusion`: 1 (启用)

### 模态配置

```json
"modes": [
  {
    "field_name": "eigenmode_11",    // VTK中的字段名
    "warp_scale": 0.08,              // 变形缩放系数
    "output_name": "eigenmode_11.png"
  }
]
```

### 配色方案

```json
"colormap": {
  "preset": "Fast",          // ParaView预设配色名称
  "compute_normals": true    // 计算法线（更平滑的渲染）
}
```

## 输出

所有图像保存到 `output_dir` 指定的目录（默认为当前目录）。

## 目录结构

```
whole_mode/
├── render.py          # 渲染脚本
├── config.json        # 配置文件
├── README.md          # 使用说明
└── *.png             # 输出图像
```

## 特性

✅ 所有参数都在 JSON 中配置  
✅ 简洁的脚本（~160行）  
✅ 支持批量渲染多个模态  
✅ 高质量渲染设置（tone mapping + ambient occlusion）  
✅ 自动计算位移范围并设置配色  
✅ 清晰的控制台输出

## 与其他脚本的区别

| 脚本 | 用途 | 特点 |
|------|------|------|
| `../render_and_stitch.py` | 渲染子网格模态并拼接 | 多submesh，手选模态，拼接输出 |
| `render.py` | 渲染完整模型的模态 | 单一完整模型，批量渲染 |

## 修改相机参数

最简单的方法是使用 ParaView GUI：

1. 打开 ParaView，加载 VTK 文件
2. 调整相机到满意的视角
3. 使用 `File > Save State` 导出 Python 脚本
4. 从导出的脚本中复制相机参数到 `config.json`
