# 竖屏布局、文字与真实媒体验收

## 画幅和独立验证

默认目标是像素 **1080×1920**、逻辑宽高 **9×16**，在此配置下画布为 `x∈[-4.5,4.5]`、`y∈[-8,8]`；推荐的保守安全区是 `x∈[-4,4]`、`y∈[-7,7]`。顶部标题可在 `y∈[5.5,7]`，主图在 `y∈[-3,5]`，下方解说在 `y∈[-6,-3]`，具体仍应按平台遮挡及对象真实尺寸重新调整。不能简单复用横屏尺寸常量。

```python
from manim import *

config.frame_width = 9
config.frame_height = 16
BG = "#1a1a2e"
CJK_FONT = "Noto Sans CJK SC"  # 必须核查实际系统字体

class Lesson(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("集合的概念与表示", font=CJK_FONT, font_size=36).move_to([0, 6, 0])
        formula = MathTex(r"A=\{1,2,3\}", font_size=28)
        self.play(FadeIn(title), Write(formula))
        self.wait(1.5)
```

在需要从命令行控制预览/正式输出时，不要在课件中强行写死 `config.pixel_width/height`。Manim Community v0.21.0 的 CLI 官方说明 `-r` 参数顺序是 **宽度,高度 (`W,H`)**；实际环境可能是其他版本，必须先执行 `python -m manim render --help`，然后用 `ffprobe` 确认输出，不凭文件名或历史文档猜测。若课件动态重写 config，可能覆盖 CLI 指定的尺寸；应在实际渲染后纠正该冲突。

## 数学图形、对象生命周期和视觉证据

`MathTex` 负责可编译的数学 LaTeX；默认模板下不要直接传中文或 Unicode 度数符号 `°`，用 `Text("中文")` 与 `MathTex(r"90^\circ")` 分离混排。明确使用并实测中文 TeX 模板的合法用法可保留。原始字符串不保证所有 TeX 均能编译； `MathTex` 中 `{{...}}` 是合法的子公式分组语法。

实际 `Mobject` 的完整 bbox 使用 `get_left/get_right/get_top/get_bottom` 检查，不能只检查中心；`Scene.mobjects` 可能包含父组而非单独列出其子对象。`Transform` 通常原对象被改变，`ReplacementTransform` 则将原对象替换为目标对象，更新后续引用并检查 Scene 的实际对象身份。`ValueTracker`/`always_redraw` 等动态动画需在初始化、中间、极值附近、结论等**多个状态**重验派生点和标签；一个时刻的检查不代表整段动画。具体 API 及 `scripts/runtime_probe.py` 的真实对象检查用法见 [Manim 引擎与运行时](manim-engine-and-runtime.md)。

一张截图不能发现动画残影、角弧方向错误、文字与图形重叠、字幕时序失配、真实字体缺字等问题。对标题、公式、主图、标签分别注册对象；除了程序检查之外，应人工复查第一帧、运动中段、边界/退化帧和结尾帧。

## 推荐执行命令（Skill 目录）

```bash
python -m unittest discover -s scripts -p 'test_*.py' -v
python -m py_compile /absolute/path/lesson.py
python scripts/audit_scene.py /absolute/path/lesson.py --json
# 仅在几何课有真实、可核验的 JSON 规格时：
python scripts/verify_geometry.py /absolute/path/geometry_spec.json
python -m manim --version
python -m manim render --help
# 官方 Community v0.21.0 的 -r 顺序为 W,H，以下均是竖屏：
python -m manim render -r 270,480 --fps 15 /absolute/path/lesson.py Lesson
python -m manim render -r 1080,1920 --fps 30 /absolute/path/lesson.py Lesson
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate -show_entries format=duration -of json /actual/output.mp4
```

统一自动化入口：`python scripts/production_check.py /absolute/path/lesson.py Lesson --math-test /absolute/path/test_math.py --render --preview`。它生成独立目录与报告，不覆盖旧视频、不自动配置音轨，也不代替人工逐镜审查。

## 背景音乐（仅在明确需要并持有使用权时）

先 `ffprobe` 查原视频是否有讲解轨；**不得**直接使用新音乐替换讲解。对有讲解轨的素材，另行设计混音、音量控制与听审。无原音轨时，也应输出到新路径，音乐应以实际视频时长为准，并检查成片后再决定是否依用户授权覆盖/清理。严禁假设旧音轨不重要，严禁默认删除中间文件。

## 验收等级

| 内容 | 所需证据 |
|---|---|
| 数学正确性 | 课内结论的成立条件、推导、反例及专项测试 |
| 静态代码 | `py_compile`、AST 检查结果；逐条处理 WARN |
| 实际对象 | 显式 Scene checkpoint JSONL，明确时间点和对象 ID |
| Manim 渲染 | 对应目标版本、真实命令、成功日志与新媒体路径 |
| 视觉质量 | 人工核对有代表性的真实视频帧和过渡 |
| 最终媒体 | `ffprobe` 实测分辨率/帧率/时长/存在的音轨，人工确认可听懂 |

每项如实记录 `pass/fail/not_run/blocked`。静态 CI、已有旧 MP4、一个对象中心坐标正确或单帧截图漂亮，均不能替代完整的视频与数学验收。
