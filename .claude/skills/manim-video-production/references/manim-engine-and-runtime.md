# ManimGX 引擎与运行时验收

> 本仓库生产运行时是 ManimGX。API、CLI、字体、排版和动画语义以当前 pinned ManimGX、`manimgx --help` 与实际 inspect/render 为最终依据；不要把历史 ManimCE 行为无条件带入。

## 1. 核心机制与迁移风险

- **Scene 生命周期**：`Scene.add/remove` 管理当前对象，`Scene.play` 编排时间线。对象可能通过父组存在于 Scene；有 Python 引用不代表正在画面上。
- **Transform / ReplacementTransform**：继续根据实际 `Scene.mobjects` 管理对象身份；替换动画后更新业务引用，避免后续对旧对象操作。
- **精确时间语义**：ManimGX 每帧按该帧的精确场景时间求值。带 `dt` 的 updater 使用独立时钟，使模拟在不同 FPS 下保持一致；迁移 CE 场景时必须重验依赖累计 `dt` 的函数。
- **`.animate`**：调用在该 animation 开始时应用；在 `Succession` 中后一段从前一段结束状态开始。同一对象同时开始的动画会合成变化。不要只凭 CE 成片猜最终状态。
- **旋转**：ManimGX 将对象作为刚体围绕一个 point 旋转；依赖历史局部点重算的 Scene 要重点抽样。
- **Axes**：使用 `axes.c2p/coords_to_point` 把数学坐标映射到画布。轴发生移动/缩放后应重新映射；动态 plot 仍需检查定义域、间断点与零宽范围。
- **文字**：`Text` 由 Typst 设置。ManimGX 自带跨平台字体和 Noto CJK；新代码优先 generic `sans-serif`。显式系统字体（如 PingFang SC）只在确认目标机器存在时使用。
- **公式**：`MathTex`/`Tex` 将 LaTeX-like 输入经 mitex 转为 Typst。常见分数、根式、求和、积分、矩阵、cases、Greek、`\\mathbb`、`\\text` 可用；LaTeX package 与 `\\def` 不兼容。复杂宏改成 ManimGX 支持的 MathTex，或直接用 `Typst/MathTypst`。
- **画幅**：`config.frame_width` 是由 `frame_height * pixel_width/pixel_height` 推导的只读值。历史 1080×1920、9×16 逻辑画幅应设置 `pixel_width=1080`、`pixel_height=1920`、`frame_height=16`，得到 `frame_width=9`。

## 2. 类型检查是迁移门禁

ManimGX API 是 typed 的。安装 `ty` 后：

```bash
ty check lesson.py
```

它用于发现：不存在的 ManimGX 名称、拼错 keyword、参数类型不匹配、错误 `.animate` 链。运行时对未知 keyword 可能较宽松，因此**类型检查不能省**。动态自定义方法若无法直接 `.animate`，使用 ManimGX 支持的 callable 形式，并写真实 Scene 测试。

## 3. 数学模型与画面双向契约

1. 用纯函数计算 `claim` 对应数据；先覆盖正常、边界、退化、反例。
2. Scene 从同一份数据创建 Mobject 与文字，不分别硬编码。
3. 关键对象登记 `object_id`、当前对象引用、预期中心/边界与采样时刻。
4. 对 updater/ValueTracker 场景检查初态、中间态、极值/退化附近和末态。
5. `manimgx inspect` 是布局采样，不是逐帧数学证明；最终仍需视频和人工关键帧检查。

## 4. Runtime checkpoint

课程目录可复制 `scripts/runtime_probe.py`，或把 Skill scripts 加到 `PYTHONPATH`：

```python
import manimgx as m
from runtime_probe import assert_checkpoint


class Demo(m.Scene):
    def construct(self) -> None:
        p = m.Dot([0, 0, 0])
        self.add(p)
        assert_checkpoint(self, "initial", {"point": p}, expected_centers={"point": (0, 0)})
        self.play(p.animate.shift(m.RIGHT))
        assert_checkpoint(self, "shifted", {"point": p}, expected_centers={"point": (1, 0)})
        q = m.Dot([1, 1, 0])
        self.play(m.ReplacementTransform(p, q))
        p = q
        assert_checkpoint(self, "replaced", {"point": p}, expected_centers={"point": (1, 1)})
```

`assert_checkpoint` 检查实际 Scene 家族、bbox 和中心；默认项目安全区 `[-4,-7,4,7]` 是 9×16 课件的保守规范，不是 ManimGX 通用默认。设置 `MANIM_PROBE_REPORT=/absolute/path/checkpoints.jsonl` 可输出证据。

## 5. Inspect 优先

```bash
manimgx inspect lesson.py Demo -t 0,end
manimgx inspect lesson.py Demo -t 0,1.5,8,end
```

Inspect 写 storyboard、打印 timeline，并在 2D 场景检查：对象被 frame 裁切、文字互相覆盖、线/填充覆盖文字、字号过小。它按采样帧检查，复杂运动必须增加 `-t` 中间时刻。

## 6. Render 与媒体

ManimGX CLI：

```bash
manimgx render lesson.py Demo -r 270x480 --fps 15 -o /tmp/preview.mp4
manimgx render lesson.py Demo -r 1080x1920 --fps 30 -o /tmp/final.mp4
```

注意：
- `-r` 使用 `WIDTHxHEIGHT`，不是 CE 的 `W,H`。
- 不使用 `-ql/-qh`、`--disable_caching`、`--media_dir`。
- `-o` 可以直接给独立 MP4 路径；storyboard 与字幕会跟随输出路径。
- ManimGX 自己完成视频编码；`ffprobe` 只用于独立验收，不是渲染依赖。

## 7. 生产检查

在 Skill 目录：

```bash
python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/production_check.py /absolute/path/lesson.py Demo --math-test /absolute/path/test_math.py
python scripts/production_check.py /absolute/path/lesson.py Demo --math-test /absolute/path/test_math.py --render --preview
```

`production_check.py` 依次执行语法、AST、可选数学测试、ManimGX inspect、preview/final render、checkpoint 与 ffprobe。输出放在新的 run 目录，不覆盖旧媒体。`frame_review` 和 `audio_review` 仍需人工完成。
