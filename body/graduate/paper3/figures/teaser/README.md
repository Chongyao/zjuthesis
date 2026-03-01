# Mode Shape Visualization

一体化脚本：从渲染到拼接一次完成，不保留中间结果。

## 使用方法

### 渲染预设配色

```bash
# Fast 配色
python3 render_and_stitch.py --preset "Fast"

# Cool to Warm 配色
python3 render_and_stitch.py --preset "Cool to Warm"
```

### 渲染自定义配色

```bash
# 自定义配色（JSON格式：[[value, r, g, b], ...]）
# value: 0-1 (0=最小位移, 1=最大位移)
# r, g, b: 0-1 (RGB颜色值)
python3 render_and_stitch.py --custom-colormap '[[0,0.2,0.4,0.8],[0.5,1,1,1],[1,0.8,0.4,0.2]]'
```

## 输出

所有最终拼接图保存在 `final_stitched/` 目录：
- `{slug}_primal_interior_modes_stitched.png`
- `{slug}_dual_interior_modes_stitched.png`
- `{slug}_primal_interface_modes_stitched.png`
- `{slug}_dual_interface_modes_stitched.png`

其中 `{slug}` 是配色方案的简称（如 `fast`、`coolwarm`、`custom`）。

## 目录结构

```
.
├── render_and_stitch.py    # 一体化脚本（唯一需要运行的脚本）
├── render_single.py        # 单个模态渲染脚本（被 render_and_stitch.py 调用）
├── selected_modes.json     # 选定的36个模态配置
└── final_stitched/         # 最终输出的拼接图
```

## 模态选择配置

要修改渲染哪些模态，编辑 `selected_modes.json` 文件：

```json
{
  "categories": {
    "primal_interior_modes": {
      "vtk_pattern": "interior_modes_primal_sub{}.vtk",
      "modes": [
        {"submesh": 0, "mode": 1},
        {"submesh": 1, "mode": 11},
        ...
      ]
    },
    ...
  }
}
```

每个 category 包含：
- `vtk_pattern`: VTK 文件命名模板（`{}` 会被替换为 submesh 索引）
- `modes`: 模态列表，每项包含 `submesh` 和 `mode` 索引

## 配置参数

如需修改渲染参数，编辑 `render_and_stitch.py` 中的配置部分：

```python
WARP_RATIO = 0.07          # 变形比例
VIEW_SIZE = [2146, 1358]   # 输出图像尺寸
CAMERA_VIEW_UP = [0, 1, 0] # 相机朝向
MAX_WORKERS = 8            # 并行渲染数量
GAP = 20                   # 拼接图之间的间隙
```

## 数据源

数据源在 `selected_modes.json` 中配置：

```json
{
  "data_source": "/path/to/vtk/files",
  ...
}
```

当前数据源：
`/home/zcy/workspace/projects/arborecence/pipline/cms_local_update/falcon_shell_balanced_small/results`

每个 submesh 包含 20 个模态（mode_0 到 mode_19）。
