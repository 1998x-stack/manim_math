# 002 任意角的三角比｜九镜修复后分镜

对应 `any_angle_trigonometry.py` 的真实 `AnyAngleTrigonometry` Scene，共九个场景，目标 9:16 竖屏。图形半径必须来自 `axes.c2p(1,0)-axes.c2p(0,0)` 的显示单位长度，不能把世界坐标半径为 2 的圆与坐标半径 1 的定义混用。旧 MP4 是旧源码成片，尚未对新代码重新渲染。

## 数学规格

单位圆以坐标原点为圆心、数学半径为 1，点 `P=(cos α,sin α)`；`sin α=y`、`cos α=x`、`tan α=y/x` 仅当 `x=cos α≠0` 时有定义。四象限符号规则不直接覆盖坐标轴上的角；`90°`、`270°` 的正切不存在。点 `30°/150°/210°/330°` 分别位于四象限，横纵坐标均由相同的正余弦数据计算。

## 可追溯分镜

| 实际方法 | learning_fact / 条件 | observable_state / 同一引用的对象 | check |
|---|---|---|---|
| `show_opening` | 从锐角推广到任意角 | 30°、150°、210°、330° 依次展示，清除开场对象 | 角度与四象限归属核对 |
| `show_unit_circle_definition` | `P=(cosα,sinα)` 与 `tanα=y/x(x≠0)` | 由 `Axes.c2p` 计算实际单位半径，画圆、点、投影线与三条公式后全部清理 | `verify_any_angle_trig.py::test_unit_circle_points`、`test_actual_scene_uses_axes_unit_size` |
| `show_quadrant_1` | 30° 时 x>0、y>0，三比均正 | 显示正余弦坐标点与两条投影，三个符号一行呈现 | `test_four_quadrant_signs`、`test_exact_sample_coordinate_magnitudes` |
| `show_quadrant_2` | 150° 时 x<0、y>0，只有 sin 正 | 几何点由 150° 计算，公式使用同一 `QUADRANTS` 数据 | `test_four_quadrant_signs` |
| `show_quadrant_3` | 210° 时 x<0、y<0，tan 正 | 几何点与坐标标签来自同一角度 | `test_four_quadrant_signs` |
| `show_quadrant_4` | 330° 时 x>0、y<0，cos 正 | 几何点与坐标标签来自同一角度 | `test_four_quadrant_signs` |
| `show_sign_rule_mnemonic` | 符号取决于 x、y；坐标轴上另判 | 四象限符号行与 `cosα=0` 的注意事项出现，逐一清理 | `test_tangent_undefined_on_vertical_axis` |
| `show_rotation_demo` | 终边连续转动时 P 的横纵坐标同步变化 | `ValueTracker(0→TAU)` 驱动同一组 `always_redraw` 半径、点和投影；结束清理引用 | `test_angle_turns_preserve_unit_circle_coordinates`；渲染首/中/末帧及垂直轴过渡 |
| `show_outro` | 复述单位圆定义、符号与分母条件 | 四项核心结论依次出现，结尾清理作者和标题 | 渲染结尾文字及公式边界 |

## 验收状态

`syntax`、`math`、`unit_tests`、`ast`：以本 PR 专项 CI 为依据；`manim_render`、`frame_review`、`ffprobe`、`audio_review`：未运行。AST 的动态 TeX 警告仅指需复查，不能代替目标环境编译。