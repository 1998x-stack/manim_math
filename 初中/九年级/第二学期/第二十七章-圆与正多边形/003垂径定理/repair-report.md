# 003 垂径定理｜逐课修复与验收记录

- 本课保留 `PerpendicularChordTheorem` Scene 入口和七个教学阶段；未替换旧 MP4、音轨或课程 Prompt。
- 数学故障：旧 A、B 位于 150°、30°，C 位于 90°，另一端点位于 270°。旧代码声称经过 C 的 A→C→B 为优弧，但将两段 -60° 的顺时针弧分别归一成 +300°，合计绘制 600°；经过圆周下端点的弧反被声称为劣弧。此为图形与数学标签直接不一致，而非单纯布局警告。
- 修法：以圆心、正半径与不经过圆心的弦的实际数据为单一来源，明确 C 是劣弧 ACB 上的中点、E 是优弧 AEB 上的中点；以 `alpha=asin(h/r)` 派生有向弧角：`AC=CB=alpha-90°`（顺时针）、`AE=EB=90°+alpha`（逆时针）。对示例 `h=r/2` 分别为 -60° 和 +120°，劣弧合计 120°，优弧合计 240°。
- 几何检查：正半径、`0<h<r`、各端点在圆上、AM=MB、优劣弧区间均由实际 Scene 读取的同一个纯数学函数校验。
- `math`: pass；`syntax`: pass（`python -m py_compile`）；`unit_tests`: pass（`python -m unittest -v test_perpendicular_chord`，3 tests OK）。
- `ast`: not_run（未运行 Skill 的 `audit_scene.py`）；`manim_render`: not_run（无 Manim）；`frame_review`: not_run；`ffprobe`: not_run；`audio_review`: not_run。

具备 Manim、TeX、中文字体和 ffmpeg 的环境中，在课程目录内验证：

```bash
python -m py_compile perpendicular_chord_theorem.py test_perpendicular_chord.py
python -m unittest -v test_perpendicular_chord
python ../../../../../.opencode/skills/manim-video-production/scripts/audit_scene.py perpendicular_chord_theorem.py --json
manim -ql perpendicular_chord_theorem.py PerpendicularChordTheorem
```

人工逐关键帧检查：点 A/B/C/E 和弦中点 M 是否对应正确；优弧只经过 E、劣弧只经过 C；数学公式和弧着色是否一致；字幕、直角标记、总结视图完整包围盒是否位于竖屏安全区。没有完成真实渲染前，不能宣布视频成片修复完成。
