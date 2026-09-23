# 006 点与圆的位置关系｜分层修复记录

- 源文件：`point_circle_position.py`；Scene：`PointCirclePosition`，保留七段课程流程。
- 直接观察到的缺陷：原知识卡片向左移 10 单位后运行 `RIGHT*0`，不能进入画面；动态演示每帧构造 `MathTex` 与 `Text`；位置判定与动态状态使用不同容差，边界文案不一致；原数值错误只输出 WARNING。
- 修订：抽出标准库纯数学模型 `point_circle_math.py`，半径正、距离非负且有限；用严格 `d<r`、`d=r`、`d>r`，三类案例在渲染前校验。动态轨迹限于圆心右侧，以同一 ValueTracker 驱动 Dot/DecimalNumber；移动状态文字只在准确端点出现。总结卡片逐张 `FadeIn`。
- 数学：精确边界及两侧小量、圆心点、非法半径与距离由 `test_point_circle_math.py` 独立测试。
- syntax: **not_run**（需要在具备源码的 Python 环境中运行 `python -m py_compile point_circle_position.py point_circle_math.py test_point_circle_math.py`）。
- math/unit_tests: **not_run**（运行 `python -m unittest -v test_point_circle_math`）。
- ast: **not_run**（运行 `.opencode/skills/manim-video-production/scripts/audit_scene.py`，逐条解释 WARN）。
- manim_render/frame_review: **not_run**（运行 `manim -ql point_circle_position.py PointCirclePosition`，逐镜检查 LaTeX、字体、状态更新、9:16 完整边界）。
- ffprobe/audio_review: **not_run**（新视频真实渲染后再验收）。原 MP4、音轨、Prompt 未改。
