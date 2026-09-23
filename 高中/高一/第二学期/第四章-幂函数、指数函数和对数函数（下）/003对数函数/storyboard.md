# 003 对数函数｜修复后分镜与验收

对应实际场景 `LogarithmFunction`，画幅 9:16、逻辑 9×16。目标时长仅为剪辑建议；当前 PR 的原视频没有重新渲染。严格区分真实数学定义域 `x>0` 与用于屏幕展示的有限区间 `[1/8,6]`。

## 数学规格

`y=log_a x` 要求 `a>0, a≠1, x>0`；定义域 `(0,+∞)`，值域 `R`，所有合法底数图像经过 `(1,0)`，`x=0` 是垂直渐近线。`a>1` 严格递增，`0<a<1` 严格递减；并非任意两个不同底数都会有相反的单调性。`log_(1/2) x = -log_2 x`，二者在所用相同坐标系关于 x 轴对称。

## 七镜追溯

| 实际函数 | learning_fact | observable_state | check |
|---|---|---|---|
| `show_opening` | 指数的逆运算与对数函数相联系 | `2^x` 转到 `log₂x`；清除全部临时对象 | 核对原函数与反函数不混用自变量 |
| `show_definition` | 底数条件、真数域、值域及共同定点 | `a>0,a≠1,x>0`、`D=(0,+∞)`、`R=R`、`log_a1=0` 依次出现 | `verify_logarithm_graph.py::test_domains`、`test_fixed_point` |
| `show_axes` | 在统一坐标轴上表示共同定点和渐近线 | `x∈[0,6]`、`y∈[-3,3]`，坐标 `axes.c2p(1,0)`，`x=0` 只作渐近线 | 首镜/坐标边界截图；`test_vertical_asymptote_not_a_domain_point` |
| `show_case_a_greater_than_1` | 底数 2 的函数递增 | 只画 x∈`[1/8,6]`，显示 `(1,0),(2,1),(4,2)`；保留原图进入比较镜 | `test_monotonicity_on_domain`、`test_sample_points`、`test_both_plot_ranges_fit_axes` |
| `show_case_a_less_than_1` | 底数 1/2 的函数递减 | 同区间叠画第二条曲线，显示 `(1,0),(2,-1),(4,-2)` 与 `log_(1/2)x=-log₂x` | `test_reciprocal_base_symmetry`；截图确认各点匹配实际绘图 |
| `show_summary` | 所有合法底数的共性及两类单调性 | 先按同一引用移除全部图像，再逐条展示定义域、值域、渐近线等，不与旧画面叠加 | 关键帧检查文字基线与边界 |
| `show_outro` | 两类底数分别对应增减，二者都过 `(1,0)` | 将数学公式和中文 `Text` 分离，最后清除全部画面对象 | 真实 TeX/中文字体与结尾画面检查 |

## 证据等级

`syntax`、`math`、`unit_tests`、`ast`：对应本 PR CI；`manim_render`、`frame_review`、`ffprobe`、`audio_review`：`not_run`。静态 JSON 边界不代替实际 Mobject 包围盒，旧 MP4 不证明新版源文件的成片质量。
