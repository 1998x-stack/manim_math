# 有趣数学 × Manim：五个以几何构造为主的探索专题

这五集是跨学段独立探索，暂置于既有 `external/interesting-math/`，不猜测教材章节、不迁移旧媒体。每个专题都有 `description.json`、`storyboard.md`、`scene.py`，全部使用 9×16 竖屏约束。各个关键几何对象由同一份数学数据驱动；几何证明的前提、逐镜对象和画面核对项目见 [GEOMETRY.md](GEOMETRY.md)。制作及验证依据 `.claude/skills/manim-video-production/SKILL.md`。

| 专题 | 目录 / Scene | 几何讲解主线 |
| --- | --- | --- |
| 奇数拼平方 | `odd-squares/` · `OddSquaresScene` | 新增 L 形格子，正方形外边框和两条边长同步增长，比较相邻面积 |
| 蒙提霍尔换门 | `monty-hall/` · `MontyHallScene` | 三组实体门牌和改选箭头 → 奖品位置三枝概率树 → 两胜一负的图块 |
| 杨辉三角奇偶分形 | `pascal-fractal/` · `PascalFractalScene` | 数字圆牌和双亲连线 → 三角形奇偶格阵 → 三个等比例缩小的图案轮廓 |
| 复数旋转 | `complex-rotation/` · `ComplexRotationScene` | 固定向量/旋转向量/真实半径的轨迹圆/累积角弧/有向坐标投影 |
| 科赫雪花 | `koch-snowflake/` · `KochSnowflakeScene` | 单边三等分及等边凸起 → 每代新增面积染色 → 周长与面积的极限 |

## 数学、语法与 AST 检查

```bash
# 仓库根目录；不依赖 Manim 的验证，包含图形构造数学不变量：
python -m unittest discover -s external/interesting-math -p 'test_*.py' -v
for scene in external/interesting-math/*/scene.py; do
  python -m py_compile "$scene"
  python .claude/skills/manim-video-production/scripts/audit_scene.py "$scene"
done
```

新增 `test_geometry.py` 验证 L 形格阵不重叠、杨辉图案左右两个递归复制块、复数端点投影与旋转模长、科赫新增三角形等边与真实增加面积。原 `test_math.py` 仍检查各专题的基本公式。这些检查不能代替 Scene 实际渲染和视觉检查。

## 独立预览及正式渲染

```bash
manim -pql external/interesting-math/odd-squares/scene.py OddSquaresScene
manim -pql external/interesting-math/monty-hall/scene.py MontyHallScene
manim -pql external/interesting-math/pascal-fractal/scene.py PascalFractalScene
manim -pql external/interesting-math/complex-rotation/scene.py ComplexRotationScene
manim -pql external/interesting-math/koch-snowflake/scene.py KochSnowflakeScene

# 每集预览成功、完整对象边界和关键帧审查后，再在目标环境正式渲染：
manim -qh external/interesting-math/odd-squares/scene.py OddSquaresScene
# 其余场景按各自 Scene 类名执行相同模式；使用 ffprobe 核对实际视频。
```

`scene.py` 中设置了生产像素宽高，`-pql` 不保证输出一定是低清：应先查看本机 Manim 版本的配置优先级并用 `ffprobe` 确认，必要时使用独立预览配置，避免改动已提交的生产规格。运行前确认中文字体 `Noto Sans CJK SC`、Manim Community 和 LaTeX 可用。

## 交付状态

场景源码、逐镜文档、独立数学测试与路径限定的 GitHub Actions 静态工作流已加入 PR。只有实际得到成功工作流结果，才能称相应静态测试通过；即使静态测试通过，`manim_render`、`frame_review`、`ffprobe` 仍分别需要实际执行记录。当前未附 MP4、授权音乐或完整渲染帧，不覆盖已有视频/音轨，也不删除历史中间文件。