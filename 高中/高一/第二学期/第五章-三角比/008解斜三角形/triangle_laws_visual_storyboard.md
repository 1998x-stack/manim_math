# 动画分镜｜解斜三角形：正弦定理与余弦定理

- 输入位置：高一第二学期第五章 `008解斜三角形`；分别衔接相邻 `006正弦定理` 与 `007余弦定理`。不修改既有 prompt、课件和媒体。
- Scene：`triangle_laws_visual.py::TriangleLawsVisual`。默认 9:16，深色背景；中文 Text / 纯公式 MathTex。

## 数学规格
- 三点不共线，`a=|BC|, b=|CA|, c=|AB|`，A/B/C 是相应顶点内角，`S>0` 是面积，`R>0` 是外接圆半径。
- 正弦定理：`2S=bc sin A=ca sin B=ab sin C`，得 `a/sin A=b/sin B=c/sin C`；弦长与同弧圆周角关系给出共同值 `2R`。分母均不为零（非退化三角形）。圆周角的关系由外接圆图示提示，并非单凭一个实例构成证明。
- 余弦定理：在本片所选图形中垂足 D 落在 AB 线段内部，`AD=b cos A, CD=b sin A`，由勾股定理 `a²=(c−b cos A)²+(b sin A)²=b²+c²−2bc cos A`。一般钝角 A 的情形需要使用有向投影或向量，而不能直接称 D 总在 AB 内。
- 反例/边界：退化三角形 `S=0` 时外接圆与 `sin A` 分式不适用；不能用动图尺寸代替精确数值/证明。

## 分镜
| 镜头 | learning_fact | 运动及可观察状态 | 检查 |
|---|---|---|---|
| 01 | 对边与内角、三边符号对应 | `drawing=always_redraw(labeled_triangle)`，C 连续移动；`length` 的读数与 BC 长同源 | a 始终在 BC 上，b 在 CA 上，c 在 AB 上；三个顶点不共线 |
| 02 | 正弦定理的面积形式与外接圆形式 | 冻结末位置 C，重建 `triangle`、外接圆 `circle`，显示 `2S=...` 与 `a/sin A=...=2R` | 三顶点共圆；a、b、c 和角匹配；R 为真实外接圆半径 |
| 03 | 余弦定理来自垂线与勾股 | 清理前一公式与圆、保留同一 `triangle`；从 C 到 AB 作 CD，依次出现两行计算与结论 | `D=(C_x,A_y)` 在 AB 内；AD=b cos A；各公式排版/边界正确 |

## 验收
- `python -m unittest discover -s external/triangle-core -p test_triangle_core_math.py -v`：急、钝角两类样本验面积、正弦与余弦定理。
- 语法/Skill AST：`python -m py_compile triangle_laws_visual.py` 后运行 `.claude/skills/manim-video-production/scripts/audit_scene.py`。
- 低清：`manim -pql triangle_laws_visual.py TriangleLawsVisual`；确认第一帧、移动中段、外接圆画面、垂足 D 与末帧内容，预览截图人工核对。
- 正式 MP4、关键帧审查、`ffprobe` 和配乐许可审查均尚未进行；旧视频不充当本次验收结果。
