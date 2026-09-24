# 003 同角三角比的关系与诱导公式｜修复后分镜

对应实际 `trig_induction.py`、入口 `TrigInduction`、十段 `scene_01_opening` 至 `scene_10_outro`。9:16 竖屏，圆的绘制半径须按 `Axes.c2p(1,0)-Axes.c2p(0,0)` 的长度求得，保证单位圆坐标与图中位置一致。原 MP4 未由新源码重新渲染。

## 数学规格与易错前提

`sin²α+cos²α=1` 对所有实角成立；`tanα=sinα/cosα`、`1+tan²α=1/cos²α` 要求 `cosα≠0`。`sin(π−α)=sinα`、`cos(π−α)=−cosα`；`sin(π/2−α)=cosα`、`cos(π/2−α)=sinα`；`sin(−α)=−sinα`、`cos(−α)=cosα`。带正切的诱导公式还要检查变换后的分母：`tan(π/2−α)=cosα/sinα` 要求 `sinα≠0`。图中示范的 α=π/6 满足所有展示公式的分母要求，数值例证不替代一般证明。

## 十镜追溯：命题 → 数据 → 屏上状态 → 验收

| 实际方法 | learning_fact / 前提 | observable_state 与对象生命周期 | check |
|---|---|---|---|
| `scene_01_opening` | 同角关系可联系诱导公式 | 开场问题与三种角变换依次出现，清空本镜对象 | 文字、公式字体与入口名称复查 |
| `scene_02_unit_circle` | 单位圆 P=(cosα,sinα) | `Axes.c2p` 求圆的物理半径，绘制半径、坐标点与两投影线，结束清理 | `verify_induction.py::test_real_scene_contains_domain_and_true_unit_scaling` |
| `scene_03_pythagorean_identity` | x²+y²=1 由勾股定理得出 | α=π/3 的直角三角形、垂足与直角标识；两条公式依序展示 | `test_pythagorean_identity_all_quadrants`；关键帧检验直角和单位长度 |
| `scene_04_tan_identity` | tan=sin/cos，cos≠0 | α=π/6 的点和投影，带分母条件的两个正切恒等式 | `test_tangent_relation_when_defined`、`test_undefined_tangent_on_vertical_axis` |
| `scene_05_induction_intro` | 反射导致坐标变号或互换 | y 轴、x 轴与 y=x 关系说明先后出现，清空临时对象 | 人工确认镜像轴与坐标变化对应 |
| `scene_06_induction_pi_minus` | π−α 导致 (x,y)→(−x,y) | α=π/6 与 5π/6 的两点、y 轴辅助线及 sin/cos/tan 公式 | `test_pi_minus_induction`、`test_reflection_coordinates` |
| `scene_07_induction_halfpi_minus` | π/2−α 导致 (x,y)→(y,x) | α=π/6 与 π/3 的两点、y=x 辅助线及含 `sinα≠0` 的正切式 | `test_halfpi_minus_induction`、`test_reflection_coordinates` |
| `scene_08_induction_negative` | −α 导致 (x,y)→(x,−y) | α=π/6 与 −π/6 的两点、x 轴辅助线和公式 | `test_negative_angle_induction`、`test_reflection_coordinates` |
| `scene_09_summary` | 归纳有域条件的同角及诱导关系 | 八条核心公式分行显示，整组按同一引用移除 | 重点检查全部文字包围盒及 LaTeX 编译 |
| `scene_10_outro` | 记忆坐标对称而不只靠口诀 | 三种坐标变换与域条件逐项呈现，作者标识与字幕同镜清除 | 结尾关键帧与 ffprobe 检查 |

## 分层状态

`syntax`、`math`、`unit_tests`、`ast`：本 PR 的 CI 结果为依据。`manim_render`、`frame_review`、`ffprobe`、`audio_review`：未执行。AST `DYNAMIC_TEX` 仍需用真实字体/TeX 在目标环境编译验证，静态通过不等于成片通过。