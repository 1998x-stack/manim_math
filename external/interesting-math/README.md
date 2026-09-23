# 有趣数学 × Manim：五个独立探索专题

这五个专题是跨学段的独立探索，放在现有的 `external/` 中，不猜测教材章节、不重命名旧媒体。按 `.claude/skills/manim-video-production/SKILL.md` 的顺序，为每个主题提供 `description.json`（课程元数据）、`storyboard.md`（数学规格／逐镜分镜／边界条件）、`scene.py`（可定位的 Manim Scene）；共享的 `test_math.py` 对五个 Scene 中的纯数学函数做无 Manim 依赖回归。

| 专题 | 目录 | Scene 类名 | 数学看点 |
| --- | --- | --- | --- |
| 奇数拼平方 | `odd-squares/` | `OddSquaresScene` | 第 n 层增加 2n−1 格，构成 n×n |
| 蒙提霍尔换门 | `monty-hall/` | `MontyHallScene` | 固定初选下三种等可能奖品位置，两种换门获胜 |
| 杨辉三角奇偶分形 | `pascal-fractal/` | `PascalFractalScene` | 按二项式系数模 2 着色，出现有限层级自相似图案 |
| 复数旋转 | `complex-rotation/` | `ComplexRotationScene` | 乘以 cosθ+i sinθ 时保持模并改变辐角 |
| 科赫雪花 | `koch-snowflake/` | `KochSnowflakeScene` | 周长因子 4/3，新增面积因子 4/9，周长发散而面积有界 |

## 校验步骤

```bash
# 仓库根目录；完全不需要安装 Manim 的数学和静态检查：
python -m unittest discover -s external/interesting-math -p 'test_*.py' -v
for scene in external/interesting-math/*/scene.py; do
  python -m py_compile "$scene"
  python .claude/skills/manim-video-production/scripts/audit_scene.py "$scene"
done

# 安装目标版本 Manim Community、LaTeX、中文字体后，每个 Scene 分别低清预览。
# 注意 scene.py 中指定了生产像素；若 CLI 低清选项被源码配置覆盖，
# 请在用于预览的独立副本中暂改 config.pixel_width/height，并探测实际输出尺寸。
manim -pql external/interesting-math/odd-squares/scene.py OddSquaresScene
manim -pql external/interesting-math/monty-hall/scene.py MontyHallScene
manim -pql external/interesting-math/pascal-fractal/scene.py PascalFractalScene
manim -pql external/interesting-math/complex-rotation/scene.py ComplexRotationScene
manim -pql external/interesting-math/koch-snowflake/scene.py KochSnowflakeScene

# 逐镜抽查实际完整对象边界、中文字体、公式、动画生命周期后，再做正式渲染：
manim -qh external/interesting-math/odd-squares/scene.py OddSquaresScene
# 对其他四个 Scene 使用同样的命令模式；ffprobe 应确认最终 1080×1920、时长及轨道。
```

## 证据与未完成的门禁

- 本分支提供源代码、数学规格、分镜、元数据及独立数学测试；专用 CI `.github/workflows/interesting-math-quality.yml` 在 PR 上运行语法、Skill AST 审计和数学单测。CI 通过之前不得写 `verified`。
- 未附 MP4、音乐或可证明已渲染的关键帧。没有安装 Manim／TeX／中文字体的执行环境不能进行真实渲染，不能将数学单测或 CI 静态通过写作 `rendered`。
- 视频正式发布还需对每个实际 Scene 做低清预览、关键帧和 9×16 安全区检查、媒体探测，以及任何授权音轨的独立审核；这里只生成静默的源码，不覆盖旧视频或删除文件。
