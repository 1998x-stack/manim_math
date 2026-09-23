# 002 圆的确定｜逐课修复记录

- 范围：`circle_determination.py` 与本课专项数学回归；保留 `CircleDetermination` Scene 入口和原八段教学顺序。原 MP4、音轨、`prompt.md`、`description.json` 不变。
- `observed_error`：原 `calculate_circumcenter` 对共线三点返回重心并继续作外接圆；原 `verify_geometry` 只打印警告却报告通过。原知识卡片先移到画外 `LEFT * 10`，再执行 `RIGHT * 0` 的零位移动画，导致总结无法入场。
- `potential_risk`：原垂直平分线采用固定线段长度，未核验交点是否落在实际显示线段上；原直角、文字和圆周包围盒仍需通过真实渲染验证。
- 修复：外心计算使用相对顶点的行列式，拒绝重合、共线和病态近共线三点，校验到三点距离以及 AB/BC 中垂线条件；画面中实际虚线线段长度由外心距离确定。卡片定位于可见画面内并实际使用带位移的入场动画。
- `math`: pass；本课纯数学回归涵盖一般、直角、重合、共线与近共线三点。
- `syntax`: pass；已在本地运行 `python -m py_compile circle_determination.py test_circle_determination.py`。
- `unit_tests`: pass；已在本地运行 `python -m unittest -v test_circle_determination`，4 tests OK。
- `ast`: partial-pass；定向 AST 未发现嵌套 `self.play`、列表实参和中文/度号字面 MathTex；未运行 Skill 原版 `audit_scene.py`。
- `manim_render`: not_run（当前环境无 Manim）；`frame_review`: not_run；`ffprobe`: not_run；`audio_review`: not_run。

在安装 Manim、中文字体、LaTeX 的环境中，进入本课目录逐项检查：

```bash
python -m py_compile circle_determination.py test_circle_determination.py
python -m unittest -v test_circle_determination
python ../../../../../.opencode/skills/manim-video-production/scripts/audit_scene.py circle_determination.py --json
manim -ql circle_determination.py CircleDetermination
```

必须逐关键帧核对共线反例、两条中垂线与外心交点、右角标志、圆是否经过 A/B/C、全部字幕与知识卡片完整包围盒。真实渲染与媒体验收完成前，不能将旧 MP4 或纯数学测试视为已通过成片验收。
