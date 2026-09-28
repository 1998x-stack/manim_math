# 004 圆心角、弧、弦、弦心距的关系：修复验收记录

- 原始 Scene：`CircleRelationships`；保留八段教学顺序、9:16 配置及已有 MP4，未修改 `prompt.md`。
- 已核实问题：原源码将 `|OM|`、`|ON|` 变量命名为 `sagitta`（弓高），其实际几何意义是弦心距；等价命题的呈现没有清楚限定劣弧和较小圆心角。原脚本中的角度、弧长、弦长、距离分散硬编码，存在修改几何却遗漏更新字幕的风险。
- 修复：统一 `circle_metrics(R, theta)`、弦端点、中点与 Arc 的起止角；以 60° 的两组劣弧说明 `弧长=Rθ`、`弦长=2Rsin(θ/2)`、`弦心距=Rcos(θ/2)`，仅对 `R>0, 0<θ<π` 的本课非退化示例作上述同圆等价展示；新增真实几何距离/垂直性断言。
- syntax: `python -m py_compile circle_relationships.py test_circle_relationships.py`，本地通过。
- unit_tests: `python -m unittest -v test_circle_relationships`，本地四项通过；包括数学恒等式、多组半径与角度、非法输入、Scene 结构。
- ast: 定向检查无嵌套 play、零位移动画；**未运行**仓库 Skill 的完整 `audit_scene.py`。
- manim_render/frame_review/ffprobe/audio_review: **not_run**。当前执行环境没有 Manim、LaTeX/中文字体与完整视频渲染环境，不得将旧 MP4 视为本次新源码的渲染证据。

待验收：在具备依赖的环境执行 `manim -ql circle_relationships.py CircleRelationships`，核对全部八段、初末帧、文本/坐标完整包围盒及字幕与弦弧对应；再对新渲染媒体执行 `ffprobe`。未经这些检查不覆盖已有视频。
