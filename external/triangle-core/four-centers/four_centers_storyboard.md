# 动画分镜｜三角形四心与欧拉线

- 归档：`external/triangle-core/four-centers/`，独立几何拓展，避免冒充某一上海学期的必修进度。
- 场景：`four_centers_visual.py::FourCentersVisual`；学生已会中线、角平分线、垂直平分线与高；9:16 竖屏。

## 数学规格
- 给定非共线点 A、B、C。重心 `G=(A+B+C)/3`；外心 O 为两条垂直平分线交点，满足 `OA=OB=OC`；垂心 H 为三条高所在直线交点；内心 I 为三条内角平分线交点，三边距离相等。
- 计算式：`H=A+B+C−2O=3G−2O`，故 O、G、H 共线，非等边情形 `OG:GH=1:2`，G 在 O、H 之间。等边三角形三点重合时比例 `0:0` 未定义，不能把该比例直接宣称适用于所有非退化三角形。
- 以 `AB` 固定，C 从 `(-0.7,2.0)` 运动到 `(1.4,0.3)`，整个动画不共线。钝角状态外心/垂心可以在三角形外，不能强行将它们限制在内部。
- 完整推理提示：由向量 `H−A=(B−O)+(C−O)`，与 BC 垂直（因为 `(B−O)·(C−B)+(C−O)·(C−B)=|C−O|²−|B−O|²=0`），其余两条高同理，推出 H 的表达式。数值图形只是佐证，不是证明替代。

## 镜头
| 镜头 | learning_fact | 屏幕状态与对象 | 验收 |
|---|---|---|---|
| 01 | 四心不同定义与外接圆 | `picture=always_redraw(figure)`，O/G/H/I 彩色点及标签，圈与外心 O 同源构造 | O 到三个顶点等距；I 到三条边等距；对应图例颜色一致 |
| 02 | 形状改变时四心位置可能改变 | `cx`、`cy` 同步动画，图形依据 `triangle_centers()` 实时更新 | 三点始终不共线；各心无奇异计算；钝角情形不把外心、垂心画错 |
| 03 | 欧拉线与 1:2 | 高亮 `Line(O,H)`，展示 `H=3G−2O` 和 `OG:GH=1:2` | 非等边条件显式；G 位于 O/H 之间，比例数值回归 |

## 分层验收
- `python -m unittest discover -s external/triangle-core -p test_triangle_core_math.py -v`：直接提取 `triangle_centers()`，检验高的垂直、外心等距、内心等距、欧拉线和共线退化报错。
- `python -m py_compile four_centers_visual.py`、Skill AST 审计；渲染 `manim -pql four_centers_visual.py FourCentersVisual`，检查初/末帧与动态中间帧的真实文字包围盒。
- 新 MP4、截图复核、`ffprobe` 与音轨审查：`not_run`；绝不将已有 `external/euler_line.py` 的历史视频当作本片成品。
