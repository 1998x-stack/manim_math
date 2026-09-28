# 001 集合的概念与表示｜可核验分镜

> 对应入口 `sets_concept.py::SetsConceptAnimation`。本版分镜以当前修改后的源码为准；旧 MP4 不代表本版已经渲染。中文由 `Text` 绘制，纯公式由 `MathTex` 绘制。逻辑画布 9×16，目标 1080×1920；画面实际包围盒及字体需通过真实渲染检查。

## 数学规格与屏上对象

- 全程同一集合：`DISPLAYED_ELEMENTS=(1,2,3,4,5)`，`A={1,2,3,4,5}`。元素 `3∈A`、`6∉A`。
- 互异性：`{1,2,2,3,4,5}=A`；无序性：`{5,3,1,4,2}=A`。
- 描述法：`A={x∈ℤ | 1≤x≤5}`；**整数域和闭区间两个条件不可遗漏**。
- 主圆圆心 `(0,1)`、半径 `1.8`；五个标签中心相对圆心半径 `1.08`，红点半径 `0.26`。圆形只是集合示意，不作为集合性质的证明。
- 标题中心 `y=5.25`；公式中心 `y=-2.1`；解释文字中心 `y=-4.3`；作者标识中心 `y=6.85`。公式和文字均按实际宽度压到不大于 `7.4`，但最终 Mobject 包围盒仍需在渲染中核对。

| 镜头/方法 | learning_fact 与可见状态 | 对象生命周期与动态变化 | check / 建议验收关键帧 |
|---|---|---|---|
| 1 `scene_1_opening` | 引出 `1、2、3、4、5` 与 `A={1,2,3,4,5}` | 标题、提问及公式出现后清理；顶部作者标识保留 | 开场公式完整、无挤压、无 Emoji 字体依赖 |
| 2 `scene_2_definition` | 集合为确定对象组成的整体；圆内五个红点及数字 `1…5` | 建立 `self.set_circle`、`self.set_label`、`self.element_dots`、`self.element_labels`；仅清除本镜标题与说明 | 圆内显示**恰好**五个不同元素，数字与红点一一对应；标签不越圆界 |
| 3 `scene_3_properties` | `3∈A, 6∉A`；重复元素不增加成员；元素重新排序集合不变 | 三个小节分别展示标题、公式、解释并逐节清除；集合圆不改动 | 比较每一个等式左右的集合成员；三小节结束后下方无旧公式残影 |
| 4 `scene_4_membership` | 圈内 `3∈A`；圈外 `6∉A` | 高亮原有第 3 个标签；使用 `ReplacementTransform` 将当前公式/解释更新；圈外 `6` 临时出现后清除 | 6 的位置在圆外；退出镜头后只保留原有五个元素 |
| 5 `scene_5_roster_notation` | 列举法公式 `A={1,2,3,4,5}` | 公式一次构建，依次强调**屏幕上原有**的五个标签，不复制临时公式标签；结束清理 | 圆内五元素与公式逐项一致，无括号挤压、漂浮副本 |
| 6 `scene_6_set_builder_notation` | `A={x∈ℤ | 1≤x≤5}` | 公式/说明结束后，移除实际在场的圆、标签、点及元素标签 | 数学域为整数，端点 1、5 均包含；清场没有旧对象残留 |
| 7 `scene_7_outro` | 三特性、元素隶属、两种表示的简洁总结 | 四行总结依次出现后退出；作者标识在整片末尾移除 | 长公式不裁切，四行互不重叠，结尾画面不残留 |

## 分层验收记录

- `math`: `python verify_sets_concept.py` 验证五个元素、隶属关系、互异性、无序性以及两种表示一致。
- `syntax`: `python -m py_compile sets_concept.py verify_sets_concept.py`。
- `ast`: `python .opencode/skills/manim-video-production/scripts/audit_scene.py <课件路径>/sets_concept.py --json`（从仓库根目录执行）。
- `manim_render`: 在装有 Manim、LaTeX 与中文字体的环境中运行 `manim -ql sets_concept.py SetsConceptAnimation`；人工核对以上七镜的初始、转场、结论与清场帧。
- `frame_review` / `ffprobe` / `audio_review`: **未取得真实渲染与媒体探测证据前，保持 not_run**；不得据此覆盖已有视频或音轨。
