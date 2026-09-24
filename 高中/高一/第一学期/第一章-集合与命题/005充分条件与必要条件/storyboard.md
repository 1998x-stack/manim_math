# 充分条件与必要条件｜对应 `sufficient_necessary_conditions.py` 的五镜分镜

## 数学定义与画面约束

前两课例始终在实数论域 `x∈ℝ` 中使用 `p: x>2` 与 `q: x>0`，所以 `p⇒q`，即 p 是 q 的充分条件，q 是 p 的必要条件；反向 `q⇒p` 为假，反例 `x=1`。对应的解集 `P=(2,+∞)` 严格包含于 `Q=(0,+∞)`。

**充要镜必须明示换了一组条件**：`r: |x|<1`、`s: -1<x<1`，二者解集 R 与 S 相同，因此 `r⇔s`。不能把原本真包含的 P/Q 两圆直接移动为相等后继续沿用原来的 p/q 文案。

竖屏逻辑范围 9×16，建议安全区 x∈[-4,4]、y∈[-7,7]；作者标识 y≈6.8、标题 y≈5.65、集合图中心 y≈1.35、定义与示例安排在 y≈-1.9 到 -5.05，不再使用旧片尾 y=-7.5 的溢出位置。理论坐标检测不能代替实际 Mobject 包围盒检测。

| 镜头 / Scene 方法 | learning_fact / 数学条件 | 可见状态、生命周期与检查 |
|---|---|---|
| 1 `show_opening` | `p⇒q` 表示 p 成立必能推出 q | 简要展示箭头与标题；作者标识常驻，临时对象退场；不能把箭头读成 q⇒p |
| 2 `show_sufficient_condition` | 在 ℝ 上 `x>2 ⇒ x>0`；P 真包含于 Q | Q 圆半径 1.92、中心 (0,1.35)；P 圆半径 1.12、中心 (-0.5,1.35)；圆心距 + 小半径 < 大半径。显示 p/q 的数学式与 P⊊Q；结尾保留同一个 `inclusion` 图组 |
| 3 `show_necessary_condition` | q 对 p 必要，不意味着 q 对 p 充分 | 直接沿用镜头 2 的集合对象；屏上仍为 p⇒q 与 q⇐p，显示 x=1 时 q 真 p 假，结束后完整移除 `inclusion` |
| 4 `show_equivalent_condition` | 新定义 r、s，`|x|<1 ⇔ -1<x<1` | 先说明条件已更换；R/S 同心同半径，用实线与虚线轮廓表示同一解集；本镜所有对象按原始引用清理 |
| 5 `show_summary` | p 对 q 充分、q 对 p 必要；r 与 s 互为充要 | 同屏呈现三行方向关系，强调只有双向蕴含才是充要；作者和卡片全部退出，文字位于竖屏安全区 |

## 分层回归

1. `python -m py_compile sufficient_necessary_conditions.py verify_conditions_scene.py`；`python verify_conditions_scene.py`。测试从真实 Scene 提取圆心、半径及数学门槛，包含 x=0、1、2、±1 等边界，不导入 Manim。
2. 运行 `.opencode/skills/manim-video-production/scripts/audit_scene.py`，将 ERROR 修复、WARN 逐项确认。
3. 只有安装 Manim、TeX、中文字体后才能 `manim -ql sufficient_necessary_conditions.py SufficientNecessaryConditions`；检查首帧、同心圆实虚线、公式、符号、文字宽度和所有关键帧。正式成片另使用 ffprobe 和音轨检查。未执行的层级写 `not_run`，不得覆盖原 MP4 或将旧视频视为本次通过。
