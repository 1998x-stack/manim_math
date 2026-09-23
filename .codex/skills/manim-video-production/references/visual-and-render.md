# 竖屏设计、代码规范与渲染验收

## 9:16 场景规范

```python
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
CJK_FONT = "Noto Sans CJK SC"  # 先确认实际可用；缺字时换已安装字体
SAFE_LEFT, SAFE_RIGHT = -4.0, 4.0
SAFE_BOTTOM, SAFE_TOP = -7.0, 7.0

class Lesson(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("集合的概念与表示", font=CJK_FONT, font_size=36)
        formula = MathTex(r"A=\{1,2,3\}", font_size=28)
        title.move_to([0, 6, 0])
        formula.move_to([0, 0, 0])
        self.play(FadeIn(title), Write(formula))
        self.wait(1.5)
```

像素宽高是 1080×1920；逻辑范围 x∈[-4.5,4.5]、y∈[-8,8]。保守安全区 x∈[-4,4]、y∈[-7,7]；推荐顶部标题 y∈[5.5,7]、主内容 y∈[-3,5]、底部说明 y∈[-6,-3]，按作品实际平台的 UI 遮挡重新评估。不能沿用横屏 `MAX_X=7`、`MAX_Y=4`。

`MathTex` 只输入可编译的数学 LaTeX；不要将中文字符或直接的度数符号 `°` 混入其字符串。中文用 `Text(...,font=CJK_FONT)` 与 `MathTex(r"90^\circ")` 分开排版；若明确采用已配置的 ctex 模板，可用 `Tex` 处理中文，但必须通过实际编译测试。常用公式例如 `MathTex(r"x\in A")`、`MathTex(r"x\notin A")`、`MathTex(r"A=\{x\in\mathbb{N}\mid x<4\}")`；Python 原始字符串有助于避免反斜杠转义，但不保证 LaTeX 必然可编译。

## 布局/生命周期的真实验证

在实际 Manim Scene 中对**最终缩放与移动后**的完整 Mobject 做包围盒检查，不能只检查中心；示例：

```python
def verify_mobject_bounds(mob, margin_x=0.5, margin_y=1.0):
    from manim import config
    left = -config.frame_width / 2 + margin_x
    right = config.frame_width / 2 - margin_x
    bottom = -config.frame_height / 2 + margin_y
    top = config.frame_height / 2 - margin_y
    if not (left <= mob.get_left()[0] <= mob.get_right()[0] <= right
            and bottom <= mob.get_bottom()[1] <= mob.get_top()[1] <= top):
        raise ValueError(f"out-of-bounds: {mob!r}")
```

对标题、文字标签、主图、结论栏的实际位置检查，并在 `Transform` / `animate.shift` / 相机移动的开始、中间和结束关键帧抽查；静态 AST 和独立 JSON 验证器均无法发现所有动态遮挡。追踪每个对象的创建、更新、清理，避免 `Transform` 后错误引用被替换对象或重复 `add` 造成画面残影。

几何题的基准顶点允许按画面要求设定；**所有被数学约束定义的派生点**必须由公式求得。缩放/移动后须同步更新点集和标签，或绑定 `always_redraw`；切忌对三角形图形做变换后仍引用原始外心坐标。若三点共线或长度为零，几何求解应报告失败，不能返回貌似有效的结果。

## 推荐执行命令（在 Skill 目录运行）

```bash
python scripts/audit_scene.py /absolute/path/to/lesson.py
# 仅当课程存在可核实的几何关系和 JSON 规格时：
python scripts/verify_geometry.py /absolute/path/to/geometry_spec.json
python -m py_compile /absolute/path/to/lesson.py
# Manim 的 -r 参数顺序为高度,宽度；预览/正式均保持 9:16：
manim -r 480,270 --fps 15 /absolute/path/to/lesson.py Lesson
manim -r 1920,1080 --fps 30 /absolute/path/to/lesson.py Lesson
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate -show_entries format=duration -of json /path/to/output.mp4
```

先通过 `manim --help` 确认安装版本支持上述选项，并检查命令行配置的优先级。渲染路径以 Manim 运行结果为准，不能猜测输出目录；最终分辨率以 `ffprobe` 实际报告为准。若 Python 文件中的 `config.pixel_*` 覆盖了预览分辨率，需为预览使用明确的独立配置，并复查预览输出。`-ql`/`-qh` 等质量预设可能重置像素参数，不要未验证就与竖屏分辨率混用。

## 背景音乐（可选且不覆盖原文件）

只有用户明确要求且对音乐拥有相应使用权时才合成。先确认原视频有无需要保留的音轨，再按需求选 `amix` 或新建纯音乐轨；原视频已有讲解声时，不可直接用 `-map 1:a:0` 替换讲解。示例仅适用于**无原音轨的视频**：

```bash
ffmpeg -i input.mp4 -stream_loop -1 -i licensed_music.mp3 -filter_complex "[1:a]volume=0.12[a]" -map 0:v:0 -map "[a]" -t VIDEO_DURATION -c:v copy -c:a aac -movflags +faststart output-with-music.mp4
```

`VIDEO_DURATION` 必须换成经过探测的实际时长；先检查输出再决定是否替换目标，默认不删除任何中间文件。若视频包含讲解，应单独设计 `amix`、归一化和响度检查，保证听懂数学讲解。

## 交付门槛

| 项目 | 可核实证据 | 未满足时状态 |
|---|---|---|
| 数学 | 命题与条件、反例/退化分析、数值或符号校验 | fail / not_run |
| 静态代码 | `audit_scene.py` 无 ERROR、已解释 WARN | fail / not_run |
| Python | `py_compile` 通过 | fail / not_run |
| Manim | 实际调用成功、无 LaTeX/字体/运行时异常 | fail / blocked / not_run |
| 动态画面 | 检查主要镜头和动画过渡，无越界、错角弧、遮挡 | fail / not_run |
| 最终媒体 | ffprobe 等实际检测得到 1080×1920、有效音轨和时长 | fail / not_run |

不要写“CI 通过”除非确实取得对应工作流运行结果；仅写入文件或添加脚本不代表执行过测试。任何非通过项都必须在交付清单中如实注明。
