# 四种命题及其关系｜与 `four_propositions.py` 同步的教学分镜

## 唯一数学模型

整数论域 `n∈ℤ`；令 `p` 表示「n 为 4 的倍数」，`q` 表示「n 为偶数」。整片的四种形式固定为：原 `p→q`、逆 `q→p`、否 `¬p→¬q`、逆否 `¬q→¬p`。原与逆否为真；`n=2` 同时反驳逆与否。展示 `n=2` 是针对本例，四种形式的一般真值关系由全部四行真值表检验，不用一个例子代替一般证明。

## 布局与对象身份

作者标识 y≈6.82；每镜标题 y≈5.65；四张卡片中心依次为 (-1.95,2.2)、(1.95,2.2)、(-1.95,-1.5)、(1.95,-1.5)，各宽 3.34、高 1.75；临时反例文字 y≈-4.42、公式位于其下方。均须通过实际 Mobject 包围盒和逐帧渲染复核。

| 镜头 / Scene 方法 | learning_fact / 数学内容 | 可见状态与生命周期 | check |
|---|---|---|---|
| 1 `show_opening` | 四种形式由同一个命题产生 | 四种名称预览；仅作者信息常驻 | 无先行断言四式全等价 |
| 2 `show_what_is_proposition` | `n∈ℤ`，固定条件 p、q | 同屏给出 `n∈4ℤ`、`n∈2ℤ`，退场后继续使用同一模型 | 明确整数论域，否则 4 的倍数/偶数含义不清 |
| 3 `show_original` | `p→q`，本例为真 | 创建并保留原命题卡片 | 每个 4 的倍数为偶数 |
| 4 `show_converse` | `q→p`，本例为假 | 保留原卡片，创建逆命题卡片；显示反例 n=2 后清除反例 | `2∈2ℤ` 但 `2∉4ℤ` |
| 5 `show_inverse` | `¬p→¬q`，本例为假 | 创建否命题卡片；仍用 n=2 反驳 | n=2 满足 ¬p、但不满足 ¬q |
| 6 `show_contrapositive` | `¬q→¬p`，本例为真 | 创建第四张卡片，四卡引用不变 | 奇数不能是 4 的倍数 |
| 7 `show_relationship_diagram` | 上排原↔逆、下排否↔逆否为互逆；两列纵向为互否 | 用卡片间连线与文字显示变换；底部两式展示原↔逆否、逆↔否的等价关系；结束时清除四张卡片 | 关系标签不把互逆/互否误称等价 |
| 8 `show_equivalence` | 对任意 p、q：`p→q` 与 `¬q→¬p` 同真值；`q→p` 与 `¬p→¬q` 同真值 | 根据 `proposition_values` 计算四行六列真值表；全部退场 | 4 组 p/q 的组合穷举；包括 p 假 q 真时的非等价情况 |
| 9 `show_outro` | 复述两组等价关系 | 片尾总结及作者标识淡出 | 无遗留对象 |

## 分层验收

1. `python -m py_compile four_propositions.py verify_four_propositions.py`。
2. `python verify_four_propositions.py`：独立提取真实源码的 `implies` 与 `proposition_values` 并运行全部四组真值、整数反例及 Scene 文案/类名静态检查。数学通过不等于视频通过。
3. 运行仓库 `.opencode/skills/manim-video-production/scripts/audit_scene.py`，对 ERROR 修复、对 WARN 逐条解释。
4. 在具备 Manim、TeX、中文字体的环境运行 `manim -ql four_propositions.py FourPropositions`；审查四卡区域、文字宽度、LaTeX、转场、四行真值表、片尾；正式成片另需 ffprobe 和音频验收。当前未完成时写 `not_run`，不覆盖旧 MP4，不合并 Draft PR。
