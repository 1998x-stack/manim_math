# 001 圆的定义与基本概念｜修复及验收记录

- 范围：本课 `circle_basic_concepts.py`，入口仍为 `CircleBasicConcepts`，七段顺序不变；未修改 `prompt.md`、`description.json`、旧 MP4 或音轨。
- 原始故障：`create_knowledge_card` 将卡片移到 `LEFT * 10`，随后 `card.animate.shift(RIGHT * 0)`，五张卡片不会进入画面；直径以临时 `VGroup` 执行 Transform 而后按子对象淡出，追踪关系不清；几何验证只打印 warning 后仍称通过；旋转无纹理圆周不能清楚展示旋转效果。
- 修复：总结卡片定位在画面内，实际使用 `FadeIn(card, shift=RIGHT * 0.5)`；两条半径先清理，再创建单独追踪的直径；几何先校验正半径、圆上四点、直径中点、弦长和弧角关系后绘图；开场增加旋转轮辐。保留圆、半径、直径、弦、劣弧、优弧、总结七段教学内容。
- `math`: pass；本课纯数学测试见 `test_circle_math.py`，含多圆心/半径、非正半径、直径与弧关系。
- `syntax`: pass；本地运行 `python -m py_compile circle_basic_concepts.py test_circle_math.py`。
- `unit_tests`: pass；本地运行 `python -m unittest -v test_circle_math`，4 tests OK。
- `ast`: partial-pass；本地 AST 检查未见嵌套 `self.play`、列表动画实参及含中文字面的 MathTex/Tex；**未运行 Skill 原版 `scripts/audit_scene.py`**，不能写作该审计通过。
- `manim_render`: not_run；执行环境没有安装 Manim，未验证 API 兼容、TeX 字体与实际物体边界。
- `frame_review`: not_run；需检查开场旋转、弦与弧标签、总结卡片完整包围盒及画面安全区。
- `ffprobe`: not_run；未生成或覆盖新视频。
- `audio_review`: not_run；既有音轨未修改。

在具备 Manim、中文字体、LaTeX 的环境中，从课程目录运行：

```bash
python -m py_compile circle_basic_concepts.py test_circle_math.py
python -m unittest -v test_circle_math
python ../../../../../.opencode/skills/manim-video-production/scripts/audit_scene.py circle_basic_concepts.py --json
manim -ql circle_basic_concepts.py CircleBasicConcepts
```

预览后须逐关键帧核验所有显示对象的完整包围盒、弧标签对应实际经过的点、静止和运动状态、字幕清晰度；通过后才可正式输出并用 `ffprobe` 检查成片。上面命令中的相对路径应在实际课程目录中确认后运行，勿据本记录宣称已渲染完成。
