# 002 直接开平方法｜七镜数学与可视化验收

- 课程源码：`direct_square_root.py`；真正 Scene：`DirectSquareRootMethod`；9×16 逻辑画幅，输出目标 1080×1920，沿用作者水印。
- 前提是实数范围。`(x+m)²=n` 在 `n>0` 时有两个互异实数解 `x=-m±√n`；`n=0` 时只有一个互异实数解 `x=-m`（若计重数则重根）；`n<0` 时没有实数解。不能把 `n≥0` 直接总结成总有两个互异解。
- 原课程实例 `x²=9`、`(x+2)²=16`、`x²+6x+9=25` 均使用相同的纯数学解算器 `solve_shifted_square` 和 `equation_residual` 验算；MathTex 保留纯数学文字，中文交给 Text。

| 方法 / 镜头 | learning_fact → 屏上状态 | check 与关键帧 |
|---|---|---|
| 1 `show_opening` | `x²=9` 的两个根为 -3、3，分别平方都为 9 | 题目、正负根在屏上清楚显示，不能将两根误写成一个 |
| 2 `show_method_introduction` | 展示 `(x+m)²=n` 与 `n≥0` 的开平方写法 | 说明此式 n=0 时 ± 给出同一个根，不能误数成两个 |
| 3 `show_basic_derivation` | `x²=9→x=±√9=±3`；数轴上 -3 与 +3 各有实际 Dot 和对应 MathTex | `NumberLine.n2p(-3/3)` 与标签点对应，平方验算各等于 9，画面不卡片重叠 |
| 4 `show_general_formula` | 分别以卡片与文字展示 `n>0`、`n=0`、`n<0` 三种情况 | 正例 2 根、零 1 根、负例 0 根，由独立测试覆盖 |
| 5 `show_example_1` | `(x+2)²=16→x+2=±4→x=-2±4=2,-6` | 两根逐一代回原方程，残差 0 |
| 6 `show_example_2` | `x²+6x+9=25=(x+3)²`，`x+3=±5`，`x=2,-8` | `x²+6x+9` 的平方展开和两根代入均正确；四张卡片独立不遮挡 |
| 7 `show_summary` | 精确总结 `n>0` 两个互异解、`n=0` 一个互异解、`n<0` 无实数解 | 中文 Text 与 MathTex 分离；最后各对象只淡出一次，作者水印末尾单独清理 |

## 生命周期与分层测试

所有分镜独立创建卡片，`_clear()` 只淡出当前 `self.mobjects` 中除 `author_info` 外的实际顶层对象；无原脚本对离屏新对象直接 `.animate.shift` 或复制公式变换后错误清理的风险。卡片的内容做宽高适配，但真实文字宽高、数轴标签、最末帧仍应经过实际 Manim 预览与包围盒审查。

依次运行 `python -m py_compile direct_square_root.py`、`python -m unittest test_direct_square_root_math.py -v`、Skill 的 `scripts/audit_scene.py`；独立测试覆盖 n 的正负零及原有实例和公式内 CJK。`manim_render`、`frame_review`、`ffprobe`、`audio_review` 尚未执行时应明确记录 `not_run`，不覆盖旧 MP4、prompt、音轨。
