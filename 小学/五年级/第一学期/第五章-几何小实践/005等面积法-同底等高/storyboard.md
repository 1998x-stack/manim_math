# 分镜｜同底等高与等积变形

- 受众：小学四至五年级；视频目标：通过顶点沿平行线移动证明同底等高三角形面积相等。
- 源材料：本目录 `prompt.md`；数学输入由 `area_model.py` 校验。
- 画幅：逻辑 9×16、深色背景；默认正式输出 1080×1920/30fps，预览 270×480/15fps。
- 时长：动画约 18–25 秒，适合配合讲解调整停顿；不是已经测量的媒体时长。

## Scene 01｜提出问题（约 2 秒）
- learning_fact：固定三角形底边、顶点能在图上移动。
- screen：顶部标题「同底等高，面积不变」、副标题「顶点移动，面积会变吗？」。
- objects_and_state：title、intro 创建；没有数学结论显示。
- check：标题完整包围盒在 `x∈[-4,4],y∈[-7,7]`。

## Scene 02｜确定共同底与高度（约 4 秒）
- learning_fact：AB=6 cm；两条水平平行线相距 3 cm；C 位于上方直线。
- screen：蓝色 △ABC、底边 AB、辅助平行线、高线、`AB=6 cm`、`h=3 cm`。
- objects_and_state：base、guide、original、labels、vertices、height 创建并保持。
- data：A=(-3,-1.7)、B=(3,-1.7)、C=(-2.3,1.3)。
- check：底边差 6、纵坐标差 3、辅助线与 AB 平行；标签 A/B/C 对应实际点。

## Scene 03｜计算原始面积（约 3 秒）
- learning_fact：面积由底与对应高决定，`S=6×3÷2=9 cm²`。
- screen：金色面积公式；旧三角形留在原位。
- objects_and_state：question 创建；original 保持。
- check：`triangle_area(6,3)` 与 `lesson_area(-2.3)` 相等。

## Scene 04｜移动顶点并比较（约 6 秒）
- learning_fact：新顶点沿与 AB 平行的直线从 C 移动到 D，底和高不变。
- screen：蓝色原三角形与动态绿色新三角形同时保留；移动结束显示 D 标签。
- objects_and_state：apex_x 从 -2.3 变到 2.3；moving/moving_dot 由同一 tracker 更新；original 仍在 Scene；D 标签在动画结束后创建。
- check：抽查 x=-2.3、0、2.3 关键帧，确认动图形顶点始终位于 y=1.3；移动标签 D 只能在点到达终点后出现；不出现残影。

## Scene 05｜公式总结（约 4 秒）
- learning_fact：`S_ABC=S_ABD=9 cm²`，条件是同底且高相等。
- screen：底部绿色等面积公式与文字「共同的底边 + 相等的高 = 相等的面积」。
- objects_and_state：conclusion、reason 创建；原图与移动后的图保留用于比较。
- check：公式与图形的点 A/B/C/D 严格匹配，底部文字在安全区且不被平台 UI 遮挡。

## 验收清单（本文件创建时状态；不得当作已渲染证明）

| check | status | evidence / command |
| --- | --- | --- |
| math | specified | `python -m unittest discover -s . -p 'test_area_model.py'` |
| syntax | not_run | `python -m py_compile lesson.py area_model.py test_area_model.py` |
| ast | not_run | `.claude/skills/manim-video-production/scripts/audit_scene.py` |
| manim_render | not_run | `MANIM_PREVIEW=1 manim lesson.py EqualAreaMovingApex` |
| frame_review | not_run | 比对顶点动画开始、中间、结束及公式显隐 |
| ffprobe | not_run | 正式渲染后检查 1080×1920、30 fps 与实际时长 |
| audio_review | not_run | 本课不包含外部音轨 |
