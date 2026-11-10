# 仓库实际 Gotchas → Skill 规则与正向实现模式

> 本参考系从 manim_math 2026-09-23 的历史事故、课程源代码及专项审计提炼；**具体课件是否已修、PR 是否已合并、旧 MP4 是否更新，必须重新读取当前分支验证**。历史报告中的零静态告警只表示规则覆盖范围内没有新命中，不等同整片质量认证。原案例均为可追溯样本，不能机械套用到所有课程。

## 1. 复用前的证据等级

- `observed_error`：可指出源码语句、触发前提与具体错误（语法/API/数值）；优先编写失败回归，再做最小修改。
- `potential_risk`：AST 无法解析动态值、具体模板与渲染配置不明、计算正确但画面可能越界；仅提示人工/真实渲染检查，**不要当成已复现故障**。
- `verified_pattern`：源代码中有明确的数据校验/生命周期/数学断言；可将设计思想移植，不能只因为它已提交就认定成片优秀。
- `render_verified`：有真实 Scene 渲染日志、关键帧和输出媒体探测记录；旧 MP4/静态 CI 均不能代替。

## 2. 故障矩阵（适用条件 → 最小修法 → 最终验收）

| ID | 触发条件与根因 | 修复原则 | 验证层级 |
|---|---|---|---|
| H01/H06 | 默认 `MathTex` / `Tex` 的字面公式包含中文，LaTeX 环境不支持 CJK | `Text` 负责中文、`MathTex` 负责纯数学；混排用 `VGroup(...).arrange(RIGHT)`；**显式 `TexTemplateLibrary.ctex` 是待渲染验证的例外，不可直接判死错** | 字面 AST；真实 TeX/字体编译 |
| H02 | `MathTex("30°")` 直接含 Unicode 度号 | `MathTex(r"30^{\\circ}")`；`Text("30°")` 不在此规则内 | 字面 AST + 视觉 |
| H03/H07 | `Sector(inner_radius=...)` / `Rectangle(corner_radius=...)` 与当前 API 形态不匹配 | 按实际安装 Manim 版本改 `AnnularSector` / `RoundedRectangle`；不能仅凭类名以外的包装调用判定 | 静态候选 + 实际构造 |
| H04 | 公式括号不匹配/分母条件遗漏 | 优先 `\\frac{a}{b}` 并检查分母不为 0；Manim `{{a}}` 可以是合法子公式隔离，**不全局禁用** | 数学证明 + TeX 编译 |
| H05 | 特定版本 `.scale(..., scale_tips=...)` 不兼容 | 查当前版本签名；必要时重新构造箭头 | 版本确认 + 渲染 |
| H08 | `Axes.plot` 动态起止点在首帧相等；曲线端点 y 超轴范围 | 初始化为非退化短区间，保证绘图时 `x_end > x_start`；分别对每条曲线验算函数像和显示范围 | 纯数学端点/采样 + 首帧/末帧渲染 |
| H09/H10 | `self.play(... if ... else [])` 将列表当作动画实参；对未添加或临时新建的对象淡出 | 只向 `self.play(*animations)` 传动画对象；持有屏上 **同一对象** 引用并跟踪创建/替换/清理 | AST 提示 + 生命周期 + 渲染 |
| H11 | `np.random.seed(...)` 改写全局 RNG，频率被叙述为单调逼近概率 | 局部 `np.random.default_rng(seed)`；标注独立、公平等前提；允许抽样频率波动 | 数学/统计测试 + 画面文案 |
| H12 | 角标签、对边/邻边和几何坐标不一致 | 以实际三点向量计算，分别验角位置、内角/优角和文字结论；不能凭 `other_angle` 的单一布尔值自动修复 | 纯数学 + 关键帧 |
| H13 | 嵌套 `self.play(self.play(...))`；内层返回值不是 Animation | 合并为同一次 `self.play(*animations)` 或拆成顺序 `self.play` | AST 确认 + 渲染 |
| H14 | 无效 Scene 类标识符、占位圆形与教学知识点无关 | 源码先 `py_compile`；以实际 AST 识别 Scene；数学规格与课程画面逐镜一致 | 语法 + 数学审阅 |
| H15 | 计数循环淡出新数字，或表格行末进位规则讲错 | `ReplacementTransform(old, new)`、最后才清理当前数字；表格用程序校验行末与十位变化 | 课程特定回归 + 逐帧 |
| H16 | 视频已有讲解仍直接替换成背景音乐/误删除临时或旧成片 | 先 `ffprobe` 检查音轨与输出时长，使用有权素材，独立目标路径生成并验收后按明确授权替换 | 媒体检查 + 人工听审 |

信息来源：
- `docs/engineering/historical-gotchas.md`（H01–H12）；`docs/engineering/highschool-historical-gotchas-20260923.md`（H13 与高中具体修复）；`docs/engineering/full-audit-findings-20260923.md`（H14/跨学段案例）；`docs/engineering/grade-one-quality-audit.md`（H15）；`docs/engineering/junior-gotchas-round2-20260923.md`（零宽图、全局种子与未修边界）。
- 比较时以实际课程源代码和实际分支为准；审计文档可能早于后续修改。

## 3. 有直接源代码依据的正向模式

### 集合课：数学模型与示意图分离

见 `高中/高一/第一学期/第一章-集合与命题/002集合间的关系/verify_sets.py`：用纯 Python 枚举有限全集全部子集、检查 `A⊆A`、`∅⊆A`、真子集数 `2^n−1`，另用 `圆心距 + 内圆半径 ≤ 外圆半径` 检查 Venn 图确实画出包含。**集合图不是代替集合证明**；`grep_MathTex` 的占位打印也不能当作真实编译成功。纯数学验证函数保持与 Scene 分离，并在异常时退出非零。

### 一年级计数：可见对象与数据一一对应

见 `小学/一年级/上册/第一章-10以内数的认识/001数一数/counting_animation.py`：`count_labels(total)` 拒绝非法输入；`star_vertices()` 的交替顶点按 `π/5` 增量递进，避免错误星形拓扑；`_show_counting` 持有 `current_number`，通过 `ReplacementTransform` 更新而非错误淡出新数字。将相同思想用于其他动态数物对应：**先验证模型，再保持对应画面对象的单一身份**。

### 中学函数：数据域驱动绘图与文字

见 `docs/engineering/junior-gotchas-round2-20260923.md` 的 `quadratic_function.py` 案例：零宽绘图起点必须被处理，曲线每个变换状态的 y 值都需落入设定轴域。只修标准式不代表平移曲线和交点式已修。三角函数另核对 `A sin(ωx+φ)` 的振幅 `|A|`、`ω ≠ 0` 时周期 `2π/|ω|`，包括 `ω<0` 以及相位平移方向。不要在绘图超域时简单藏掉坐标轴。

### 概率与统计：可复现但不污染全局

在独立生成器内抽样，例如 `rng = np.random.default_rng(42)`，在同一镜头使用相同样本数组构造图表与字幕。试验样本量增大不保证**每一步**频率更接近理论概率；不能从一次抽样推导确定性结论。参见 `docs/engineering/junior-gotchas-round2-20260923.md`。

## 4. 将模式变成新课的最小验收记录

1. 记录 `source_path`、真实 `SceneClass`、知识点、当前 Manim/字体/LaTeX 版本、对应 Hxx（不适用写 `N/A`）。
2. 在 `storyboard.md` 为每镜建立 `math_claim → observable_state → data_assertion → render_frame`，而不是用通用几何测试冒充集合、统计或代数检查。
3. 运行 AST 检查与该课**独立**纯数学单元测试；将 warnings 逐条分类为已排除、已修复、待渲染，而非全部自动替换。
4. 对初始、状态切换、退化边界、结论帧做 Manim 低清渲染与截图；检查屏上对象引用、文字重叠、公式编译和数学意义。
5. 最终成片通过媒体探测与人工检查才能标为 `render_verified`，不得将独立 `verify_geometry.py` 的 JSON 检查称为 Mobject 运行时边界验证。
