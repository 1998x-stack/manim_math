# 005 圆周角定理：分层验收记录

- 入口：`InscribedAngleTheorem`；保留原八段课程顺序、9:16 配置；未修改 Prompt、原 MP4 或音轨。
- 可确认的旧脚本问题：四张知识卡片先移至画外，后续 `shift(RIGHT*0)` 不使其入场；结论卡片声称圆周角顶点可在圆上「任意移动」，遗漏位于同一段圆弧上的前提；原数值验证仅打印 WARNING 仍宣称通过。
- 修复：将点 A/B/P/Q 的真实坐标绑定圆心角、圆周角和字幕；对 P=240°、Q=290° 同弧圆周角均为 60°、O=120°，反面弧顶点 90° 则对应 120°；直径两端 0°/180° 对圆上其他非端点均对应 90°。用可见卡片逐项 FadeIn，清理动画始终引用屏上同一对象。
- `syntax`: 本地 `python -m py_compile inscribed_angle_theorem.py test_inscribed.py` **pass**。
- `unit_tests`: 本地 `python -m unittest -v test_inscribed` **5 tests OK**；涵盖同弧、异侧反例、直径、不合法点以及 Scene 结构。
- `ast`: 定向未发现零位移动画；原 Skill 的完整 `audit_scene.py` **not_run**。
- `manim_render` / `frame_review` / `ffprobe` / `audio_review`: **not_run**；当前执行环境无 Manim 和全套视频依赖，不得称旧 MP4 是新源码的渲染产物。

待验收：`manim -ql inscribed_angle_theorem.py InscribedAngleTheorem`，逐段检查 LaTeX 与中文字体、圆周角/圆心角图示及总结卡片边界；正式渲染后以 ffprobe/音轨检查完成成片验收。未经确认不覆盖旧媒体。
