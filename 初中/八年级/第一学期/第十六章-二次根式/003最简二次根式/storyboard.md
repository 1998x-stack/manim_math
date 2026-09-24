# 003 最简二次根式｜逐镜可验分镜

- 实际源文件：`simplest_radical.py`；Scene：`SimplestRadical`；原九段教学顺序不变；画幅逻辑 9×16、目标竖屏。
- 核心规则：二次根式化到最简形式后，被开方数不含分母，亦不含能够开得尽的因数或因式。正整数 `n` 可写成 `n = outside² × inside`，其中 `inside` 无大于 1 的平方因数。
- 特别注明：`√(a²b)=|a|√b` 对所有实数 a 与 `b≥0` 成立；**仅当 a≥0** 时可去掉绝对值写 `a√b`。商的开方公式 `√(a/b)=√a/√b` 需 `a≥0,b>0`，不能省略分母非零且正的条件。

| 镜头 / 实际方法 | learning_fact → 可见状态 | check / 验收帧 |
|---|---|---|
| 1 `scene_opening` | 并列 `√12` 与 `2√3`，说明值相等，后者根号内已无法再开尽 | `√12=2√3`，同时显示不出现错误不等号 |
| 2 `scene_two_conditions` | 定义的两个条件与 `√(3/4)=√3/2`、`√12=2√3` 对应 | 根号内无分母、无可开尽平方因数；上下卡片和标题不互相遮挡 |
| 3 `scene_method` | `12=4×3=2²×3`，开方提出 2、根号内剩下 3 | 每次变化显示同一个整数 12 的等值形式 |
| 4 `scene_example1` | 对 `√12` 逐步分解并给出 `2√3` | `simplify_integer_radicand(12)==(2,3)`，测试 0、完全平方数、非平方数和平方因数混合 |
| 5 `scene_example2` | 先给出 `√(a²b)=|a|√b (b≥0)`，再分 `a≥0` 与 `a<0` 两类 | `a=-2,b=3` 时结果必须为 `2√3`；独立数学测试验证负数和零 |
| 6 `scene_example3` | 商的开方，明确 `a≥0,b>0`；`√(3/4)=√3/2` | 负 a、b=0、b<0 的错误输入由回归拒绝；标注分母已无根号 |
| 7 `scene_judge` | 依次判断 `√3`、`√8`、`√(2/3)`、`3√5`、`√(a²)` | 第五项必须解释为 `|a|`，不可无条件写 `a`；每张判断卡片宽度合规 |
| 8 `scene_summary` | 汇总整数、字母平方和商的三种化简；提醒保留绝对值和适用条件 | 显示 `b≥0`、最后镜头没有无条件的 `√(a²)=a` |
| 9 `scene_outro` | 重现 `√12=2√3` 和符号条件的核心提醒，移除水印 | 最后背景无残留文本或临时对象 |

## 质量门槛与生命周期

由 `construct` 创建 `author`，每镜 `_clear()` 只淡出当前场景中的顶层对象并保留同一水印引用，第九镜末单独移除。表达式和判断说明作为同一张卡片的实际 VGroup 内容布局，代码缩放超宽内容；这只能降低越界风险，**仍须进行真实 Manim 预览和关键帧包围盒核查**。

专项验证：`python -m py_compile simplest_radical.py`、`python -m unittest test_simplest_radical_math.py -v`、`python .opencode/skills/manim-video-production/scripts/audit_scene.py <实际文件> --json`。CI 验证不等于实渲染，旧 MP4/音轨不自动替换。请分开记录 `math/syntax/ast/manim_render/frame_review/ffprobe/audio_review` 的状态。
