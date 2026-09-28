# 002 二次根式的性质｜逐镜可验分镜

- 源码：`radical_properties.py`；真实入口：`QuadraticRadicalProperties`。
- 受众：八年级上；画幅：9:16（逻辑 9×16）；中文 `Text`，数学公式 `MathTex`。
- 实数范围内，命题 P1：`(√a)²=a` 的前提 `a≥0`；命题 P2：`√(a²)=|a|` 的前提 `a∈ℝ`。P2 当 `a=0` 时两种分类表达均给出 0。
- 纯数学验证：`python -m unittest test_radical_properties_math.py -v`；编译：`python -m py_compile radical_properties.py`。静态检查不代替 Manim 视频渲染。

| 镜头 / 方法 | learning_fact 与实际屏上状态 | check / 关键帧 |
|---|---|---|
| 1 `scene_1_hook` | `√((-3)²)=√9=3`，追问结果为何不是 -3 | 核实括号包住 -3；正结果清晰且水印在画面内 |
| 2 `scene_2_review` | `√a` 在实数范围内要求 `a≥0`；并列显示两条性质及**不同的适用域** | 两条公式各自条件完整、公式不叠字 |
| 3 `scene_3_prop1` | `(√a)²=a (a≥0)`；`(√9)²=3²=9`、`(√5)²=5` | `a=0`、正数及负值拒绝由 `root_then_square` 测试；提示不能把 `√(-9)` 当实数 |
| 4 `scene_4_prop2_trap` | 猜测 `√(a²)=a`，对比 `a=3` 成立、`a=-3` 时 `3≠-3`，以反例否定全称命题 | 独立的正负例卡片、完整反例公式，确认不再出现歧义的 `≠a=-3` 断句 |
| 5 `scene_5_prop2_full` | 数轴 -3 与 +3 各自到 0 的距离相同；`√(a²)=|a|`；`a≥0` 时为 a，`a<0` 时为 -a | 端点取自 `NumberLine.n2p`，左右各 3 单位；数轴及公式完整、两种情况非重叠 |
| 6 `scene_6_pitfall` | 依次判断 -5、-2 与 `√4` 的四条等式，使用数值模型验证答案真伪 | 对错误式仅标记“错误”，不以 `MathTex` 表示中文；每张卡片与左右边界内 |
| 7 `scene_7_summary` | 回收 P1/P2、突出 P1 的 `a≥0` 与 P2 的 `a∈ℝ`，末尾仅一次移除水印 | 两条适用条件同框且清晰，最后无残留对象 |

## 动画生命周期及视觉验收

`author_info` 在 `construct` 中建立，前六镜与第七镜的 `_clear` 始终保留；最后单独移除。其余对象由每镜独立建立，`_clear` 仅取当前 `self.mobjects` 顶层的同一对象，各对象只有一次 `FadeOut`。负数正反例不再将几段长公式拼成一整行超出卡片。主卡片宽 7.7，按内容包围盒缩放；仍需通过**真实预览渲染**检查小字、字体回退、全部字幕、实际 Mobject 边界和全程状态。

### 分层验收记录

- `math`: 数学回归由 CI 执行，详见工作流；`syntax`: `py_compile`；`ast`: Skill `audit_scene.py`。
- `manim_render` / `frame_review` / `ffprobe` / `audio_review`: 未执行，不能用旧 MP4 作为本次代码生成视频的证据；不覆盖原有 MP4、prompt 或音轨。
