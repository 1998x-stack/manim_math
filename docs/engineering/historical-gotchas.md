# Manim 历史 Gotchas 与初中课件逐项治理

> 状态：2026-09-23，文档与静态检测第一轮。**已记载 ≠ 已在所有初中课件重现；静态告警 ≠ 已确认渲染失败；旧 MP4 ≠ 修复后源码的验收证据。**本页保留问题来源、确认范围、复现条件、正确修法和后续逐课验收入口。

## 0. 史料与版本边界

- 原始七条记录：[历史 `docs/Error.md`（迁移前提交）](https://github.com/1998x-stack/manim_math/blob/6dfc3f775babf4abb96f30a5470448384a12e2d7/docs/Error.md) → [当前事实源 `docs/engineering/references/Error.md`](references/Error.md)。`docs/Error.md` 现为兼容跳转；不修改或删除历史原文。
- 原文标题中的 `0.19.2(latest)` 仅描述当时记录的环境，**不是对当前最新 Manim 版本的判断**。本仓库的代码是否兼容，应以锁定的实际运行版本/真实渲染日志判定。
- 后续发现的同类故障记录：[七年级专项 PR #23](https://github.com/1998x-stack/manim_math/pull/23)、[八年级专项 PR #28](https://github.com/1998x-stack/manim_math/pull/28)、[九年级源码审查](grade9-code-audit.md)。PR 中尚未合并的变更不能算作 `main` 上已修复。

## 1. 历史七条：逐项记录、复现和预防

| ID | 来源 | 可复现的触发条件 / 影响 | 最小安全修法 | 静态规则与人工验收 |
| --- | --- | --- | --- | --- |
| H01 中文误入 TeX | 原记录 1 | 使用默认 LaTeX 模板，`MathTex("周角")` 编译失败；自定义 CJK 模板需另判。 | `Text("周角", font=可用中文字体)`，数学单独使用 `MathTex`。 | `CHINESE_IN_TEX`（候选警告）；用实际模板渲染核验。 |
| H02 Unicode 角度 | 原记录 2 | `MathTex("30°")` 交给 LaTeX 可能因字体/编码失败。 | `MathTex(r"30^{\circ}")`。 | `UNICODE_IN_TEX`；检查显示角度与几何角度一致。 |
| H03 Sector/AnnularSector 混用 | 原记录 3 | 向 `Sector` 传 `inner_radius` / `outer_radius`，导致构造参数不匹配。 | `Sector(radius=...)` 或明确需要环形扇区时改用 `AnnularSector(inner_radius=..., outer_radius=...)`。 | `SECTOR_RADIUS_KEYWORD`（确定形态）；仍需验证弧起点、角度、半径。 |
| H04 TeX 分组 | 原记录 4 | 分式/分组不匹配时 LaTeX 编译失败，部分 `\over` 写法难排查。 | 优先 `MathTex(r"\frac{a}{b}")`，检查括号配对、公式转义、分母非零条件。 | 人工检查/真实 LaTeX 渲染；**`{{...}}` 在 Manim 中亦可表示子串隔离，不能无条件识别为错误。** |
| H05 Arrow 缩放 API | 原记录 5 | `arrow.scale(..., scale_tips=...)` 在所用 API 版本不受支持。 | 去掉未经验证的参数；需要箭头端点/箭头尖尺寸固定时显式测试当前 API。 | `LEGACY_SCALE_TIPS`（版本相关警告）；逐帧检查箭头尖大小。 |
| H06 中文与公式混排 | 原记录 6 | 默认 `Tex(r"周角 $=360^\circ$")` 仍包含中文且依赖 LaTeX 的中文环境。 | `VGroup(Text("周角 =", font=可用字体), MathTex(r"360^\circ")).arrange(RIGHT)`。 | `CHINESE_IN_TEX`；检查混排基线、字幕宽度与字体回退。 |
| H07 Rectangle 圆角参数 | 原记录 7 | `Rectangle(corner_radius=...)` 无该构造参数。 | 圆角矩形选 `RoundedRectangle(corner_radius=...)`，普通矩形去掉该参数。 | `RECTANGLE_CORNER_RADIUS`（确定形态）；检查圆角和碰撞区域。 |

原记录中 H01/H06 是同一底层根因的两种场景；仍保留独立 ID，以便把历史条目逐条对应到审计结果。H02 在 `Text` 中显示 `°` 不等于错误：规则仅作用于 `Tex/MathTex` 的可静态分析字符串实参。

## 2. 后续同类故障：来自现有具体代码/PR 的扩充案例

| ID | 已观察到的代码或记录 | 出错机制与修复条件 | 现行处理 |
| --- | --- | --- | --- |
| H08 动态绘图零宽区间 | [九年级二次函数审查](grade9-code-audit.md)：`ValueTracker(CURVE_X[0])` 与 `x_range=[CURVE_X[0], t.get_value()]` 起始端点重合；`x²` 在 `|x|=2.5` 时超出 `y=5` 的轴范围。 | 起点必须非零宽；绘制区间需同时满足 `y` 轴可见范围和实际函数值；不要只裁掉坐标轴却保留离屏曲线。 | `ZERO_WIDTH_PLOT` 只抓**字面量**等端点；变量值相等/函数越界仍需专项数学检查与渲染。九年级记录中此问题尚未修。 |
| H09 `self.play` 对象分支类型 | [九年级二次函数源码](../../初中/九年级/第一学期/第二十六章-二次函数/001二次函数的概念/quadratic_function.py) 存在 `FadeOut(x_lab) if x_lab else []`；当 `else` 分支执行时，列表被当成单个动画实参。 | 构造 `animations = [...]`，存在时追加 `FadeOut(x_lab)`，最后 `self.play(*animations)`。 | `PLAY_EMPTY_ANIMATION` 提示待人工复核；当前源代码尚未改动。 |
| H10 对象生命周期不匹配 | [八年级专项 PR #28](https://github.com/1998x-stack/manim_math/pull/28)：一元二次方程场景对临时创建的透明框执行 `FadeOut`，未清除真正显示的高亮框。 | 保存并 FadeOut 原有对象；Scene 间核对仍然保留的文本/高亮/水印。 | 修复在独立 PR，**不与本分支重复修改同一课件**；需要低清渲染验收。 |
| H11 随机数污染与概率表述 | [八年级专项审查记录（PR #28）](https://github.com/1998x-stack/manim_math/blob/fix/grade8-scene-audit-20260923/docs/reviews/grade8-source-audit.md) 指出 `np.random.seed(42)` 污染全局状态；将频率描述为随次数单调靠近 0.5 并不成立。 | 使用局部 `rng = np.random.default_rng(42)`；说明独立同分布、公平试验等前提，频率可波动。 | `GLOBAL_NUMPY_SEED` 可提示源码位置；数学描述需要人工逐镜检查，当前场景尚未修。 |
| H12 几何标签与实际坐标不一致 | [九年级专项修复 PR #24](https://github.com/1998x-stack/manim_math/pull/24) 已对锐角三角比的直角顶点、相邻边和角标签进行修改。 | 角 A 与对边/邻边/斜边必须从**实际坐标和顶点顺序**验证；避免硬编码与动画对象脱节。 | 该课源码已在 main 修改，仍需实际渲染与关键帧验收；不能用通用 AST 检查代替数学几何验证。 |

## 3. 初中范围与逐文件执行方式

此仓库的初中树还包含**六年级**；故扫描范围是 `初中/{六年级,七年级,八年级,九年级}/**/*.py`，覆盖课程脚本与可能存在的辅助 Python 文件，不扫描二进制视频和长 `prompt.md`。对报告每条结果按 `path:line + code` 对齐实际源码；不能仅凭相似文件名、旧视频存在或历史 PR 的标题宣称本文件已修。

```bash
python tools/audit_junior_gotchas.py --json > junior-gotchas.json
python -m unittest discover -s tools/tests -p 'test_audit_junior_gotchas.py' -v
# 仅当每一条旧问题已经分辨并修复后，才启动警告强制失败：
python tools/audit_junior_gotchas.py --strict
```

当前默认行为：语法错误/已知非法字面调用参数/静态零宽区间为 `error`，其余历史风险为 `warning`；出现 `error` 返回非零状态。`--strict` 还将候选警告纳入失败。全量结果应保存原始 JSON，按文件逐项核对，而不是笼统地自动替换全部中文、双大括号、扇区或箭头写法。

### 每条修复的最小验收记录

| 字段 | 必须记录的证据 |
| --- | --- |
| 发现 | `Hxx`、Git 源码路径、Scene 类名、原行号、原问题及复现条件；必要时关联历史 PR/错误日志。 |
| 修复 | 最小差异、是否更换 Scene 名称/视频/素材、与分镜的一致性、适用的 Manim/LaTeX/字体环境。 |
| 静态 | `py_compile`、专项规则/回归测试、复扫原路径及周边同类调用。 |
| 数学 | 特定知识点的数值/符号/退化边界断言；文字条件与几何顶点/角/边、概率样本空间一致。 |
| 渲染 | `manim -ql <path.py> <SceneName>` 的实际日志、关键帧/字幕遮挡/9:16 离屏检查；最后才考虑重新制作 MP4。 |
| 状态 | `发现 / 待复核 / 已修源码 / 静态通过 / 渲染通过 / 已发布`，不要将阶段性通过折叠为“全部完成”。 |

### 已知待办和并行 PR 避免冲突

- 六年级：复查此前已合并的 [#12](https://github.com/1998x-stack/manim_math/pull/12) 涉及的脚本和其他同类文件，逐课区分既有数学修复与新报告。
- 七年级：先核对 [#23](https://github.com/1998x-stack/manim_math/pull/23) 的四个场景和两个数学检查脚本，避免在 `main` 上再次编辑其未合并的相同路径；再处理其余审计命中项。
- 八年级：先核对 [#28](https://github.com/1998x-stack/manim_math/pull/28) 已修的一元二次方程场景；概率频率/RNG 的内容缺陷、二次根式画面边界依原审查逐项处理。
- 九年级：依 [40 课验收矩阵](grade9-code-audit.md) 复核二次函数动态范围、垂径定理退化输入、方差数据绑定及其余课程。除已明确定位的问题外，其余课件标记“待审查”，不谎称无缺陷。

**本分支首批交付是历史汇编、风险定位器及其回归测试，不声称完成初中所有 Scene 的源码修复或视频验收。**后续对每一条发现直接在对应课程源码修复并添加数学/渲染证据，不因扫描器告警数量下降而替代实际检查。
