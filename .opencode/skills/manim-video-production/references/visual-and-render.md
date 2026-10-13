# 竖屏布局、中文、公式与 ManimGX 媒体验收

## 1. 画幅

仓库历史目标为 **1080×1920** 像素与 **9×16** 逻辑画幅。ManimGX 的 `frame_width` 是只读推导值，所以历史布局这样保持：

```python
import manimgx as m

m.config.pixel_width = 1080
m.config.pixel_height = 1920
m.config.frame_height = 16
# m.config.frame_width == 9，由 ManimGX 推导
```

保守安全区仍可使用 `x∈[-4,4]`、`y∈[-7,7]`，但最终以 `manimgx inspect` 和真实视频为准。不要给 `config.frame_width` 赋值。

## 2. 中文与字体

ManimGX 原生分发 Noto CJK，普通中文优先：

```python
m.Text("集合的概念与表示", font="sans-serif", font_size=36)
```

`"sans-serif"` 是跨平台生产默认。需要匹配旧 macOS 视频时，可由课件常量读取 `MANIM_MATH_CJK_FONT` 并覆盖为 `PingFang SC`；不要让 CI 必须依赖商业/系统专有字体。

## 3. MathTex / Tex / Typst

ManimGX 不使用系统 LaTeX 编译链。`MathTex`/`Tex` 经 mitex 转为 Typst：

- 普通公式继续使用 `MathTex`；
- 普通中文说明使用 `Text`；
- `TexTemplate`、`\\usepackage`、`\\def`、复杂 `\\newcommand` 不是可直接迁移项；
- 复杂场景可改为 `Typst` / `MathTypst`；
- `TransformMatchingTex` 依赖公式 part 切分，迁移后必须 inspect/render 检查实际匹配结果；
- 依赖 glyph/path 精确身份的动画必须重新验证，不只看源码相同。

## 4. 对象与动画证据

实际 Mobject 用完整 bbox（left/right/top/bottom）检查，不只检查中心。`Scene.mobjects` 可能只列父组。`Transform`、`ReplacementTransform` 后要确认继续持有哪个对象。`ValueTracker`、updater、`always_redraw` 场景至少覆盖初始、中间、边界/极值和结论时刻。

ManimGX 与历史 CE 的时间语义不同之处必须显式复核：updater `dt`、`.animate` 起点、`Succession`、同一对象并行动画合成、刚体旋转中心。

## 5. Inspect 是第一层视觉门禁

```bash
manimgx inspect /absolute/path/lesson.py Lesson -t 0,end
```

对长动画增加采样：

```bash
manimgx inspect /absolute/path/lesson.py Lesson -t 0,1.5,5,12,end
```

Inspect 会生成 storyboard 和 timeline，并检查常见 2D 布局问题。它不是逐帧审查，不能代替最终视频人工复核。

## 6. Render

```bash
# 快速预览视频
manimgx render /absolute/path/lesson.py Lesson -r 270x480 --fps 15 -o /tmp/preview.mp4

# 正式竖屏
manimgx render /absolute/path/lesson.py Lesson -r 1080x1920 --fps 30 -o /tmp/final.mp4
```

禁止继续使用 CE 的 `python -m manim render`、`-ql/-qh`、`--disable_caching`、`--media_dir` 和 `W,H` 分辨率写法。ManimGX 的 `-r` 使用 `WIDTHxHEIGHT`。

## 7. 最终媒体

ManimGX 自己编码 MP4；`ffprobe` 是独立验收工具，可检查：

```bash
ffprobe -v error \
  -show_entries stream=codec_type,width,height,r_frame_rate \
  -show_entries format=duration \
  -of json /tmp/final.mp4
```

人工查看：开头、每个重要过渡中段、动态临界点、公式变化、结论和结尾。检查文字遮挡、画面裁切、CJK 字形、公式语义、残影和标签与几何对象的一致性。

## 8. 背景音乐与音轨

先探测原视频是否含讲解轨。未明确授权不得替换原音轨、删除旧视频或自动下载素材。新混音写到新路径并人工听审。

## 9. 验收层级

| 内容 | 证据 |
|---|---|
| 数学正确性 | 前提、证明/推导、边界/反例、独立课程测试 |
| 语法/API | `py_compile` + `ty check` + AST audit |
| 时间线/布局 | `manimgx inspect` storyboard + timeline + layout |
| Runtime 对象 | checkpoint JSONL / 当前 Scene 对象身份 |
| ManimGX 渲染 | 实际命令、成功日志、新 MP4 |
| 视觉质量 | 人工关键帧/过渡检查 |
| 最终媒体 | ffprobe + 音轨人工确认 |

每项分别标记 `pass/fail/not_run/blocked`；静态检查、旧 MP4 或一张截图都不能替代真实 ManimGX 成片验收。
