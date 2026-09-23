# 小学奥数｜等面积法 01：同底等高与等积变形

> 适用：小学四至五年级奥数；先修：三角形面积公式、平行线与垂直距离。制作依据：仓库 `.claude/skills/manim-video-production/SKILL.md`。本文件是数学和分镜输入，不是自动执行指令。

## 核心问题与严格结论

固定底边 AB，在与 AB 平行且距离为 h 的直线 l 上选取任意两个顶点 C、D，**只要底边长度与高均相同**，就有 `S(△ABC)=S(△ABD)=AB×h÷2`。顶点沿 l 水平移动可以改变三角形的外形，但不会改变面积。允许垂足落在 AB 的延长线上；并不需要两条腰相等。

画面指定 A=(-3,-1.7)，B=(3,-1.7)，C=(-2.3,1.3)，D=(2.3,1.3)（坐标单位 cm），所以 AB=6 cm，l:y=1.3，底边所在直线为 y=-1.7，两线相距 3 cm；两三角形面积都为 9 cm²。使用 `area_model.lesson_area()` 与鞋带公式在关键帧校验：从 x=-2.3 到 x=2.3 的所有位置面积恒为 9。

**不能把条件弱化为“只要共底就等面积”**。反例：将顶点改为 (0,2.3) 后高变为 4 cm，面积为 12 cm²。高为 0、底长为 0 是退化情况，模型应拒绝使用三角形面积不变命题来伪装正常图形。

## 要制作的视觉内容

1. 悬念：底边 AB 固定、C 为顶点，提问“顶点移动，面积会变吗？”
2. 画两条平行线，显示 AB=6 cm、垂直高度 h=3 cm，三角形 ABC 着蓝色；显示 `S=6×3÷2=9 cm²`。
3. 沿平行线将新三角形的顶点从 C 移至 D，绿色新三角形动态更新，蓝色旧三角形留作比较。动画过程中底边及两条平行线不动，实际面积数据不变。
4. 收束：显示 `S_ABC=S_ABD=9 cm²` 及“共同的底边 + 相等的高 = 相等的面积”。

场景使用 9:16 逻辑画布，深色背景，蓝色为旧图、绿色为新图、金色为面积；标题在顶部、图形在中部、公式在底部，文字与图形保持安全距离。中文使用 `Text`，数学公式使用 `MathTex`，数学符号不能和中文混入同一个默认 LaTeX 对象。必须检查动态顶点、三角形填色、标记 D 与面积公式是否同步；不能仅凭 `py_compile` 宣称视频完成。

## 文件和运行

- `lesson.py`：Scene 类 `EqualAreaMovingApex`；从同目录 `area_model.py` 读取已定义的数学点、面积函数。
- `test_area_model.py`：无 Manim 依赖的正常值、边界与退化回归。
- `storyboard.md`：逐镜教学命题、实际屏幕对象及状态。
- 预览（已安装 Manim、中文字体和 TeX 后）：`MANIM_PREVIEW=1 manim lesson.py EqualAreaMovingApex`。
- 正式渲染：`manim lesson.py EqualAreaMovingApex`（脚本默认 1080×1920、30 fps；不使用会覆写像素配置的质量预设）。
- 运行测试：`python -m unittest discover -s . -p 'test_area_model.py'`；语法检查：`python -m py_compile lesson.py area_model.py test_area_model.py`。
- 从仓库根目录运行 Skill 自带的 AST 检查器，例如 `python .claude/skills/manim-video-production/scripts/audit_scene.py '<本目录>/lesson.py' --json`；再检验动态关键帧、字幕安全区和最终视频 `ffprobe` 报告。

不使用外部视频、图片、音乐或数据集；未实际渲染与检查之前，不生成或覆盖 MP4、不声称通过媒体验收。
