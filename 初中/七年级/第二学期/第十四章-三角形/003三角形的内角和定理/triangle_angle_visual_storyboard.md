# 动画分镜｜三角形内角和与外角

- 源材料：本目录 `description.json` 与既有课程；此文件是新增独立版本，不修改原始 `prompt.md`、场景或 MP4。
- Scene：`triangle_angle_visual.py::TriangleAngleSumVisual`；七年级，已知平行线内错角性质。
- 画幅：9:16，1080×1920，深色背景；时长依实际渲染确认。中文 `Text`，数学 `MathTex`。

## 数学规格
- 条件：欧氏平面中 A、B、C 不共线，A(-2.7,-1.1)、B(2.7,-1.1)、C=(t,2.1+0.18t)，`t∈[-1.3,1.2]`；始终逆时针，内角均在 `(0,180°)`。
- 结论一：`∠A+∠B+∠C=180°`。过 C 作 `l∥AB`，CA、CB 将 l 一侧的平角分成三个角；两端角与 A、B 处内角分别相等。
- 结论二：D 位于 AB 的 B 端延长线上，外角 `∠CBD=∠A+∠C`。理由是它与 `∠ABC` 互补。
- 限制：拖动图形与测量只帮助发现，不构成普遍证明；三点共线时三角形内角与外角教学定义不适用。

## 镜头与校验
| 镜头 | learning_fact 与屏幕证据 | 动作/对象引用 | 验收 |
|---|---|---|---|
| 01 | 识别三个内角与内角和等式；颜色弧线来自同一组顶点 | `drawing=always_redraw(diagram)` 建立；`t` 连续变化；等式 `fact` 常驻 | 每帧角弧对应 A/B/C；顶点不共线；画面不越界 |
| 02 | 内错角证明，不把拖动当证明 | `FadeOut(drawing)` 后用冻结的 C 创建 `fixed`、`fixed_tags` 和平行线 `parallel`；`ReplacementTransform(fact,proof[1])` | 平行线与 AB 水平；公式直接用屏幕已标出的 ∠A、∠C、∠B；平行线端点留在竖屏安全区 |
| 03 | 外角等于两个不相邻内角之和 | 清理镜头 02 对象；沿 AB 方向创建 BD，实际 D 在 B 右方、标签不出界 | `∠CBD=180°−∠B=∠A+∠C` |

## 质量门槛
- 数学回归：`python -m unittest discover -s external/triangle-core -p test_triangle_core_math.py -v`，涵盖正常位置与外角关系。
- 语法与 AST：`python -m py_compile triangle_angle_visual.py`；Skill `scripts/audit_scene.py` 应使用仓库真实路径执行。
- 渲染：`manim triangle_angle_visual.py TriangleAngleSumVisual`；逐帧查 9:16 边距、平行线、角弧、结尾外角；正式成片另查 `ffprobe`。
- 当前状态：新 MP4/音轨未生成；渲染、关键帧、媒体探测均 `not_run`。不得拿本目录旧 MP4 代替本次验收。
