# 2026-09-23：完整课程 Python AST 扫描与分批修复结果

**证据边界：** [CI 首轮完整历史与全量扫描](https://github.com/1998x-stack/manim_math/actions/runs/35828312845) 从可达非合并历史扫描 316 commits，按修复关键词检出 113 条提交、4994 个历史路径；对当次检出的 613 个课程 Python 文件分 7 批完成 AST 检查，产生 8 个候选。每条线索须核对实际行号与上下文，候选告警不等于实测 Manim/LaTeX 错误；历史修复提交也不等于 `main` 上的当前状态。

| 扫描 ID | 源码 | 原始问题、核实与本 PR 处理 |
| --- | --- | --- |
| `1fc0a846885e4edc` | `external/monge_circle.py:737` | 默认 `MathTex` 中含中文 `半径`；改为 `Text` 和 `MathTex` 的 VGroup，保留原公式。已提交，仍待真实渲染。 |
| `6e9b2d4102a1d0c1` | `初中/九年级/第二学期/第二十七章-圆与正多边形/008切线的性质与判定/tangent_properties.py:1030` | 双层 `self.play(self.play(...))`；改为单层 FadeOut，使用 `list(self.mobjects)` 对待清理元素取快照。已提交，仍待真实渲染。 |
| `d538ac574caa2ccf` | `小学/四年级/第一学期/第五章-几何小实践——圆与角/001线段、射线、直线/001_线段、射线、直线.py:3` | 类名含中文顿号 `、` 导致 SyntaxError；原内容也只是画圆的占位动画。更换为有效的 `SegmentRayLineLesson(Scene)`，实际展示线段、射线、直线及端点数量，竖屏配置前置。 |
| `3c341fce7ffd54a5` | `小学/四年级/第一学期/第四章-数的运算——除数是两位数的除法/002笔算除法(试商与调商)/002_笔算除法(试商与调商).py:3` | 类名含括号导致 SyntaxError、占位圆形与教学内容不符；更换为 `TrialQuotientAdjustmentLesson(Scene)`，演示 `1476 ÷ 28 = 52 余 20`、调商以及余数小于除数的核验。 |
| `e4d78ddfd4b80136` | `小学/四年级/第二学期/第三章-统计/001单式折线统计图/001_单式折线统计图.py:18` | 直接将中文交给默认 MathTex，原画面只有无关圆形；更换为 `SingleLineChartLesson(Scene)`，用五个明确数据点展示折线图及相邻变化。 |
| `e235f4d6f2daf6c1` | `高中/高一/第一学期/第三章-函数的基本性质/003函数的运算/function_operations.py:525` | 该 MathTex **显式传入 `tex_template=TexTemplateLibrary.ctex`**。与 H01 默认 TeX 中文故障不构成同一触发条件，暂归类为当前静态规则的例外；是否实际编译仍需对应 TeX/字体环境渲染。 |
| `4fda854c6f51d917` | `高中/高二/第二学期/第十二章-圆锥曲线/002圆的方程/circle_equation.py:386` | 显式传入 `TexTemplateLibrary.ctex`，同上；不能在没有渲染证据时盲改教材文字和公式。 |
| `e56b368f90d4f259` | `高中/高二/第二学期/第十二章-圆锥曲线/004椭圆的几何性质/ellipse_properties.py:663` | 显式传入 `TexTemplateLibrary.ctex`，同上。 |

**已修复源码的数学与渲染状态不同：** 新增无 Manim 依赖的 AST 回归用于拦截非法类名、中文错误 TeX 和嵌套动画；小学除法额外检查数值等式、余数约束，折线图核对五个数据点。静态验证不代表每帧的布局或数学叙述均正确。上述五个实际修复需进一步执行独立的低清 Scene 渲染、LaTeX/字体检查、关键帧视觉核查，确认视频实际产生后再发布。

批次扫描和文件覆盖的当前机器真实状态以本 PR `TODO.json` 以及最新 CI 工件为准；如果源码改动后旧问题不再命中，扫描器会移除候选，历史已修复事实则保留在本页。
