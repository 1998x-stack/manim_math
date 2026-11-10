# Manim 引擎与运行时验收（Manim Community）

> 适用于当前仓库目标版本；任何 API、渲染参数及字体/TeX 行为，均以目标环境 `python -m manim --version`、`python -m manim render --help` 和实际渲染为最终依据。此文档没有将某一版本行为无条件推广到其他版本或 ManimGL。

## 1. 核心机制决定测试策略

- **Scene 生命周期**：`Scene.add/remove` 控制场景所持有的对象，`Scene.play` 执行动画；对象可能作为一个 `VGroup` 的子对象显示。不要仅用 `mob in scene.mobjects` 判断可见身份，需遍历 `scene.mobjects` 的 `submobjects`；有引用不等于当前在画面上。
- **Transform 和 ReplacementTransform 不同**：普通 `Transform(source,target)` 通常改变 source 自身而不将 target 自动加入 Scene；`ReplacementTransform` 会在结束后使用目标替换源。前者继续追踪 source，后者更新为 target 引用。动画结束后以实际 `Scene.mobjects` 为准。
- **ValueTracker 与 updater**：`tracker.animate.set_value(v)` 让数值随动画变化；updater/`always_redraw` 可能每帧重算图形。所有中点、垂足、切点、标签应在每一状态由同一数学函数派生；`always_redraw` 内不得以退化零宽绘图范围调用 `Axes.plot`。不要把每帧重建的对象引用当作永久不变的屏上对象。
- **Axes 坐标与屏幕坐标不同**：使用 `axes.c2p(x,y)` 将数学坐标映射到画布，移动/缩放轴后要重新映射；不能将数学坐标 `(x,y)` 直接当作最终 Mobject `get_center()` 的期望值。`Axes.plot` 采样不保证间断点、渐近线处的函数图像严格正确。
- **文字和公式**：普通中文用 `Text`，数学表达用 `MathTex`；`MathTex` 的 `{{...}}` 是合法的子公式分组语法，不能用通用括号检查误判；ctex 例外需实测当前 TeX 引擎与字体。
- **分辨率优先级**：官方 Community v0.21.0 CLI 将 `-r` 说明为 `W,H`。例如目标 1080×1920 时，优先尝试 `-r 1080,1920`，实际安装版本应运行 `python -m manim render --help` 再确认。源码内 `config.pixel_width/height` 可能覆盖 CLI；必须 `ffprobe` 读取 MP4 的实际尺寸。预览为 `-r 270,480`，正式为 `-r 1080,1920`，均应按目标版本核验；不要同时混用质量预设覆盖这些数值。

官方依据：
- https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html
- https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html
- https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html
- https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html
- https://docs.manim.community/en/stable/reference/manim.animation.updaters.mobject_update_utils.html
- https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html
- https://docs.manim.community/en/stable/guides/configuration.html

## 2. 数学模型与画面的双向契约

1. 将 `claim`、`assumptions`、`domain`、`counterexample`、`math_test` 写入分镜；采用**纯数学函数**计算派生点和标签数值。选用解析证明或完整讨论支持课程结论；有限采样只能证明被测数据。
2. 几何图的模型坐标经过 `axes.c2p`（若使用坐标轴）或同一明确定义的仿射映射变为画布坐标。画面对象使用这套结果创建，禁止分别硬编码两个不同版本。
3. 对关键时刻，按 `object_id` 登记**当前正在显示的同一个对象**、预期中心和可见包围盒。对每一个显示结论重复做数据断言。独立 `verify_geometry.py` 只检查提供的 JSON，不会自动读取 Manim 对象。
4. 动画阶段至少核验初始、变化过程中的有意义状态、边界/退化附近状态、结论、离场状态。显式检查点只检查调用时刻；不能把它写成完整逐帧覆盖。复杂轨迹需要渲染并抽样视频帧，逐帧安全关键动作可另写 updater 断言并实测开销。

## 3. 在课程 Scene 中接入实际 Mobject 检查

将本 Skill 的 `scripts/runtime_probe.py` 复制进本次课程目录（或者明确将 Skill `scripts/` 添加至 `PYTHONPATH`）。以下示例没有引用仓库根目录、网络或其他 Skill：

```python
from manim import *
from runtime_probe import assert_checkpoint

class Demo(Scene):
    def construct(self):
        p = Dot([0, 0, 0])
        self.add(p)
        assert_checkpoint(self, "initial", {"point": p}, expected_centers={"point": (0, 0)})
        self.play(p.animate.shift(RIGHT))
        assert_checkpoint(self, "shifted", {"point": p}, expected_centers={"point": (1, 0)})
        next_p = Dot([1, 1, 0])
        self.play(ReplacementTransform(p, next_p))
        p = next_p  # 替换动画之后引用必须更新
        assert_checkpoint(self, "replaced", {"point": p}, expected_centers={"point": (1, 1)})
```

- `assert_checkpoint` 基于 `scene.mobjects` 的对象身份及其子对象检查是否仍属于当前 Scene，使用 `get_left/right/top/bottom` 验证完整几何边界，并用 `get_center` 比较画布坐标。默认安全区 `[-4,-7,4,7]`，是本项目 9×16 的保守建议，并非 Manim 的通用默认值。
- 若设置 `MANIM_PROBE_REPORT=/absolute/path/checkpoints.jsonl`，脚本会逐行追加 JSON 检查记录；调用方需确保父目录存在。检查失败会抛 `AssertionError`，未捕获则中止该次渲染。
- 这里只检查**注册对象**；需要逐个注册主图、标题、每个重要标签/公式。一个 `VGroup` 整体在安全区内，不保证其中元素相互不遮挡。`ValueTracker` 等非显示数据对象不要注册为文字或图形。
- 点的数学坐标应先按实际场景变换映射到画布坐标，才可作为 `expected_centers`。一个显示对象的中心（如三角形）不等于对应的数学顶点，应注册对应的 `Dot`/标签或另外设计顶点断言。

## 4. 生产检查与诚实交付

在 Skill 目录运行：

```bash
python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/production_check.py /absolute/path/lesson.py Demo --math-test /absolute/path/test_math.py
python scripts/production_check.py /absolute/path/lesson.py Demo --math-test /absolute/path/test_math.py --render --preview
```

`production_check.py` 默认只跑语法、AST 和指定的数学测试；`--render` **显式开启**预览/正式渲染以及 `ffprobe` 检查，并在独立新目录写入报告、日志和输出视频。预览与正式渲染将调用当前 Python 环境里的 Manim，绝不自动安装包、删除缓存、覆盖旧 MP4 或添加背景音乐。没有实际安装 Manim、LaTeX、ffprobe 时，报告为 `blocked`/`not_run`，不得称作视频已验收。

该脚本只确认视频流尺寸与正时长；需继续人工检查首帧、中间关键帧、错位/遮挡、公式含义、所有结论和音轨。即使全部检查点 `pass`，也不等于证明成立或整片无视觉问题。只有数学测试、渲染检查、关键帧人工审查和素材许可分别有证据时，才相应标记通过。
