# 仓库历史 Gotchas → ManimGX 迁移规则

> 本参考保留历史事故的数学/动画经验，但**运行时结论全部按 ManimGX 重新验证**。旧 ManimCE 错误、PR 或 MP4 只能作为迁移线索，不能证明 ManimGX 当前分支正确。

## 证据等级

- `observed_error`：当前 ManimGX 分支可指出源码、触发条件与错误。
- `migration_risk`：来自 CE 历史或静态分析，尚未在 ManimGX 复现；需要 typecheck/inspect/render。
- `verified_pattern`：数学模型、对象生命周期或数据约束已由当前源码/测试确认。
- `inspect_verified`：ManimGX inspect 对指定采样时刻通过。
- `render_verified`：真实 ManimGX render + 媒体探测 + 关键帧人工检查通过。

## 故障矩阵

| ID | 风险 | ManimGX 处理 | 验收 |
|---|---|---|---|
| GX01 | 残留 `from manim import ...` / CE module path | 使用 `manimgx` 顶层公开 API；不仿造 CE 内部模块树 | audit + ty |
| GX02 | `config.frame_width = ...` | 删除赋值；用 pixel ratio + `frame_height` 推导 | runtime assertion |
| GX03 | CE `-ql/-qh`、`--media_dir`、`--disable_caching`、`-r W,H` | 改 `manimgx inspect/render`、`-r WIDTHxHEIGHT`、`-o` | CLI + render |
| GX04 | `TexTemplate`、`\\usepackage`、`\\def`、复杂宏 | 改写为支持的 MathTex，或 Typst/MathTypst | construction + inspect |
| GX05 | 指定 `PingFang SC` 等系统字体导致 Linux 不可复现 | 新代码 `font="sans-serif"`；必要时 env 覆盖旧字体 | inspect/render on CI |
| GX06 | CE updater 累积 `dt` 假设 | 按 ManimGX 精确时间/独立 updater clock 重验 | 多 FPS/采样测试 |
| GX07 | `.animate` / `Succession` 起点假设 | 逐段检查开始/结束状态 | inspect 中间时刻 |
| GX08 | 同一对象并行动画在 CE 下依赖覆盖顺序 | ManimGX 会组合同时开始的变化；重构为明确目标状态 | state assertions |
| GX09 | 历史旋转依赖局部点重算 | ManimGX 刚体绕 point 旋转；明确 `about_point` | geometry + render |
| GX10 | `MovingCameraScene` / `ApplyMethod` / `ScaleInPlace` / `FadeToColor` 等旧别名 | 新代码用 `Scene` 与 `.animate` 主 API | ty + inspect |
| H08 | 动态 `Axes.plot` 首帧零宽或函数奇点 | 初始化合法区间并对动态域做数学断言 | math test + inspect |
| H09/H13 | 列表被当 animation、嵌套 `self.play` | 构建 animation list 后展开，或拆成顺序 play | AST + runtime |
| H10/H15 | 淡出临时新对象、ReplacementTransform 后仍持旧引用 | 始终持有当前屏上对象；替换后更新变量 | checkpoint |
| H11 | 全局随机种子污染、把频率说成单调趋近 | 局部 RNG；文案与统计事实一致 | math test |
| H12 | 角标签/边名与真实几何不一致 | 从同一组点计算位置与结论 | geometry + frame review |
| H16 | 直接覆盖讲解音轨/旧视频 | 新路径输出，先探测音轨，素材需授权 | ffprobe + listen |

## 公式与中文的新规则

历史 CE 中“中文放 MathTex 会导致 LaTeX CJK 编译失败”的具体根因不再成立，因为 ManimGX 不使用系统 LaTeX；但设计上仍建议：

- 中文教学说明 → `Text`；
- 纯数学表达 → `MathTex`；
- 混排需要明确分组，避免依赖未知 LaTeX package；
- `MathTex(r"30^{\\circ}")` 比依赖 Unicode 数学解析更稳定；
- 任何 `TexTemplateLibrary.ctex`、package 或宏方案视为 CE 遗留，改成 ManimGX/Typst 方案。

## 可复用的正向模式

### 数学模型与 Scene 分离

圆方程、集合关系、函数定义域、概率抽样、三角形几何等先写纯 Python 函数与边界测试。Scene 只消费其结果。这样从 ManimCE 迁到 ManimGX 时，数学内核无需跟渲染器一起重写。

### 同一数据驱动画面与字幕

计数、高亮数量、概率曲线、函数值、几何标签都从同一份 validated data 创建，禁止图形与文字分别硬编码。

### 动态对象单一身份

对同一屏幕含义保留一个“当前对象”引用。`ReplacementTransform(old, new)` 后立即更新变量；清理时淡出当前对象而不是重新构造一个看起来相同的对象。

### Inspect 驱动的视觉验证

静态 AST 之后，先 `manimgx inspect` 采样初态/中间态/结论；再真实 render。布局问题和数学问题分开记录，不用一个自动化 pass 代替另一类证据。

## 新课最小迁移记录

1. `source_path`、SceneClass、知识点、ManimGX 版本、画幅、字体策略。
2. `math_claim → validated_data → screen_object → checkpoint/time`。
3. `py_compile`、AST、`ty check`、课程数学测试结果。
4. `manimgx inspect` 的 sampled times、storyboard、layout 结果。
5. `manimgx render` 命令、MP4 路径、ffprobe 数据、人工关键帧结果。
6. 对每个 GX/Hxx 标记 `N/A / risk / fixed / verified`，不得把历史结论直接标为已通过。
