# 动画分镜｜三条线段何时构成三角形

- 来源：本目录 `description.json`；新建 `triangle_inequality_visual.py::TriangleInequalityVisual`，保留既有 `main.py`、`prompt.md` 和视频。
- 七年级；先修：圆与线段长度；9:16 竖屏。

## 数学规格
- 固定 `AB=3.2`、`BC=2.2`，参数为 `AC=t`。非退化三角形存在当且仅当 `|AB−BC|<AC<AB+BC`，即 `1.0<t<5.4`。
- 作图原理：以 A 为圆心、t 为半径和以 B 为圆心、2.2 为半径的两圆在严格不等式成立时有两个交点，取 AB 上方的一个为 C。`x=(t²−2.2²+3.2²)/(2·3.2)`，`y=sqrt(t²−x²)`；这里 x 是从 A 沿 AB 量出的坐标。
- 边界：t=1.0 或 t=5.4 时两圆相切、三点共线，不构成非退化三角形；t=0.8 和 t=5.6 时无交点。长度必须严格正。

## 分镜
| 镜头 | learning_fact | 屏幕状态、动作与约束 | 验收 |
|---|---|---|---|
| 01 | 判断闭合而不是凭目测拼接 | `picture=always_redraw(geometry)` 从 t=0.8 开始，仅保留 AB；t 的数值通过 `DecimalNumber` 同源更新 | 不显示不存在的 C 或假三角形 |
| 02 | 理解严格双边界 | t 动画至 2.2，真实绘制三条边及两条半径均为 2.2 的圆；原图对象引用始终为 `picture` | AC、BC 数值与几何长度一致；两圆确实相交 |
| 03 | 过长、退化与取等号 | 移除圆；t 至 5.6 后再至 1.0，显示相应说明 | 失败时没有 C；等号时不把共线图形渲染成三角形 |

## 验收
- `python -m unittest discover -s external/triangle-core -p test_triangle_core_math.py -v`：直接提取 `upper_vertex()` 的 AST，验证正常、近边界、负长度、等号及不可能输入。
- `python -m py_compile triangle_inequality_visual.py`，再用 Skill 的 `scripts/audit_scene.py` 检查。
- 低清渲染 `manim -pql triangle_inequality_visual.py TriangleInequalityVisual`，重点检查动态切换、圆的边界与文字遮挡。正式 MP4、关键帧和音轨检查：`not_run`；已有旧 MP4 不是本次新作品。
