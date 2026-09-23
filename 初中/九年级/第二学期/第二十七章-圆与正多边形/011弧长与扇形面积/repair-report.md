# 011 弧长与扇形面积｜修复验收记录

- Scene `ArcLengthAndSectorArea`；保留原九段教学阶段与课程目标。原始 MP4、Prompt 和音轨不修改。
- 原代码用 `Brace(Line(弧起点,弧终点))` 给弧长作标注，但该线段是弦，不是弧；新动画使用对应 `Arc` 外侧的弧长标注。原源码另有临时 `Transform(VGroup(...), formula_small)` 后存储目标对象作为下一场景引用的身份风险；新场景每镜保留并清理同一真实对象，且避免依赖与 Manim 版本不匹配的 `SurroundingRectangle(corner_radius=...)`。
- 新增纯数学模型 `arc_sector_math.py`：R>0、0°≤n≤360°、θ=nπ/180，独立验证 l=Rθ、S=R²θ/2=Rl/2，与单位制和面积的含义一致。包含 R=2、n=60° 与 R=3、n=120° 两个实际画面示例，均从同一数据计算。
- 新增 `test_arc_sector_math.py`，覆盖样例、角度单位、0°/360° 数学边界、非法输入及 Scene 方法/弧标签一致性。数学模型允许 0° 与 360°；动画 `Sector` 实际仅使用非退化的 60° 与 120°，不将极端图形当作已渲染验证。

## 分层状态
- syntax/math/unit_tests：**not_run**；从课件目录运行 `python -m py_compile arc_length_sector_area.py arc_sector_math.py test_arc_sector_math.py`、`python -m unittest -v test_arc_sector_math`。
- ast：**not_run**；用 Skill 的 `scripts/audit_scene.py` 检查真正 Scene 源码，逐条解释 WARN。
- manim_render/frame_review：**not_run**；运行 `manim -ql arc_length_sector_area.py ArcLengthAndSectorArea`，检查弧长标签位于对应圆弧、扇形填充、公式与 9:16 画面边界。
- ffprobe/audio_review：**not_run**；没有替换旧成片，只有真实新视频渲染成功才验收音视频流。
