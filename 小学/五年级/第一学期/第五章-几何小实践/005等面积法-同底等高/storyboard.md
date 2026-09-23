# 分镜｜等面积法：动点、动态高线与长方形对角线

- 受众：小学四至五年级奥数，先修：长方形面积、三角形的底与高。
- 源：本目录 `prompt.md`、`area_model.py`；完整几何对象取自实际 `lesson.py`。正式视频 9:16、1080×1920/30fps；`MANIM_PREVIEW=1` 为 270×480/15fps。
- 核心断言：固定 AB=6 cm，C/P 始终位于与 AB 平行、距离 3 cm 的直线上，则每个三角形面积恒为 9 cm²。垂线段必须与对应的底边垂直，单纯的斜边不能当作高。
- 镜头时间是预计动画长度，不是实测视频时长。首屏的安全区目标为 x∈[-4,4]、y∈[-7,7]，最终须按实际字体及渲染包围盒复查。

## Scene 01｜建立平行线与底边
- learning_fact：AB 是唯一固定底边；另一条平行线承载可动顶点。
- diagram：水平基线 x∈[-3.5,3.5]、y=-1.7；平行虚线 y=1.3；蓝色 △ABC 顶点 A=(-3,-1.7)、B=(3,-1.7)、C=(-2.3,1.3)。
- motion：先展示两线与 `ℓ∥AB`，再逐点填充蓝色 △ABC，给底边标 `AB=6 cm`。
- check：实际坐标差 AB=6，上下线距 3；字母跟随正确的点，而不是浮在三角形的另一边。

## Scene 02｜作垂线，展示公式
- learning_fact：C 到 AB 的垂足 H=(-2.3,-1.7)，CH=3 cm；直角符号要位于垂足处。
- diagram：金色虚线 CH、垂足 H、直角记号；面积式 `S_ABC=6×3/2=9 cm²`。
- motion：先作垂线和直角，后写面积式。
- check：向量 AB·CH=0；垂足来自 `altitude_foot()`，数值面积来自 `lesson_area()`。

## Scene 03｜同底等高的动态证据
- learning_fact：固定 AB，P 沿 y=1.3 移动，垂足及直角记号与动点同步，垂直距离始终为 3；绿色的 △ABP 不是另一块独立面积加到蓝色三角形上。
- diagram：蓝色 △ABC 原图保持，绿色 △ABP 覆盖它；P 从 -2.3 移至 0 再至 2.3。金色动态高线、动态直角、动态垂足同步，底部公式 `S_ABP=9 cm²`。
- object_lifecycle：原始高线离场；`apex_x` 是移动图形、高线、垂足、直角及 P 字母的唯一数据源；动画结束时动态对象整体离场。
- check：抽查 x=-2.3、0、2.3 和中间点；垂足 x 与 P 相同、y=-1.7；观察动态物体是否与文字重叠、离场后有无残影。

## Scene 04｜用长方形对角线看懂“÷2”
- learning_fact：长方形的对角线将 6×3 的图形分成两块面积相等的三角形，这是公式解释示例，不把长方形等同于此前任意形状的动点三角形。
- diagram：清空第一幅几何图；绘制顶点 (-3,-1.5),(3,-1.5),(3,1.5),(-3,1.5) 的 6×3 长方形；描金色左下到右上对角线，一半绿色、一半蓝色。
- motion：先描边标尺寸，再依次显现两半，最后显示 `S_rect=6×3=18 cm²` 和 `S_△=18÷2=9 cm²`。
- check：两个直角三角形共对角线但各自取一条 6 cm 的水平边作底，对应高为 3 cm；每块面积 9，总和 18。

## 质量验收（状态不得与媒体验收混淆）

| 检查 | 状态 | 运行方法或证据 |
| --- | --- | --- |
| mathematics | 待本分支 CI | `python -m unittest discover -s . -p 'test_area_model.py'`：101 个运动取样、垂足、斜底投影、对角线两半、退化情况 |
| syntax | 待本分支 CI | `python -m py_compile lesson.py area_model.py test_area_model.py` |
| ast | not_run | `python .claude/skills/manim-video-production/scripts/audit_scene.py <本课绝对路径>/lesson.py` |
| manim_render | not_run | `MANIM_PREVIEW=1 manim lesson.py EqualAreaMovingApex` |
| frame_review | not_run | 移动初/中/末、旧标签清除、高线直角、矩形两半与完整包围盒 |
| ffprobe | not_run | 正式渲染后检查分辨率、帧率、时长 |
| audio_review | not_run | 本课不添加音乐或讲解音轨 |
