# 2026-09-23 初中 Gotchas 逐文件命中与修复台账

> 本台账记录 `tools/audit_junior_gotchas.py` 第一次完整 CI 结果及第一次课件修复后的复扫。`warning` 是待人工复核的源码风险，不一定导致运行失败；无命中不等于课件已逐行审阅或渲染通过。历史分类与防范方式见 [historical-gotchas.md](historical-gotchas.md)。

## 一、真实覆盖与复扫证据

- [初次 CI](https://github.com/1998x-stack/manim_math/actions/runs/35824201411)：四年级 Python 文件总计 **211**（六年级 62、七年级 54、八年级 52、九年级 43），静态确定型错误 **0**、待复核提示 **14**；10 项工具回归测试通过。原始结果可下载为该运行的 `junior-historical-gotchas` JSON artifact。
- [第一次源码修复](https://github.com/1998x-stack/manim_math/commit/901f43c1c335e6e45dbd76593aeaa9ef6f4c6e57)：六年级有理数大小比较原位修复，保留公开 Scene 入口。
- [复扫 CI](https://github.com/1998x-stack/manim_math/actions/runs/35824292828)：扫描覆盖仍为 211，静态确定型错误 **0**、待复核提示 **13**；工具测试 10/10 通过。这证明**本扫描器**不再报告该课的中文 MathTex 风险；并非真实渲染通过。

## 二、首轮 14 条逐文件结果

根路径均为 `初中/`；条目以实际 CI JSON 为准，行号指**首轮扫描时的源文件**，修复后可能移动。

| # | 年级 / 文件（去掉 `初中/` 前缀） | 原行 | 分类 | 处理状态及验收 |
| --- | --- | ---: | --- | --- |
| 01 | `六年级/第二学期/第五章-有理数/005有理数的大小比较/005_有理数的大小比较.py` | 18 | H01 `CHINESE_IN_TEX` | **源码已修**：用 NumberLine 真正比较 -2、0、1；中文改 `Text`，数学比较用 `MathTex`；复扫不再报告，仍待低清渲染与关键帧审核。 |
| 02 | `六年级/第一学期/第四章-圆和扇形/005弧长公式/arc_length_formula.py` | 310 | H02 `UNICODE_IN_TEX` | 待核对真实字符串与 LaTeX 模板，局部替换角度符号后重跑渲染。 |
| 03 | 同上 `arc_length_formula.py` | 359 | H02 `UNICODE_IN_TEX` | 同上；逐公式核对角度单位。 |
| 04 | 同上 `arc_length_formula.py` | 392 | H02 `UNICODE_IN_TEX` | 同上；检查弧长表达式变量单位。 |
| 05 | 同上 `arc_length_formula.py` | 456 | H02 `UNICODE_IN_TEX` | 同上；检查最终公式与可见范围。 |
| 06 | 同上 `arc_length_formula.py` | 457 | H02 `UNICODE_IN_TEX` | 同上；不要仅改一个调用就标记整课完成。 |
| 07 | `八年级/第一学期/第十九章-几何证明/008勾股定理的逆定理/pythagorean_inverse.py` | 164 | H02 `UNICODE_IN_TEX` | 源码实见 `MathTex(r"\angle C = 90°", ...)`；待转换为 LaTeX `90^{\circ}` 并检查角 C 与三边标签/逆定理条件。 |
| 08 | 同上 `pythagorean_inverse.py` | 181 | H02 `UNICODE_IN_TEX` | 同上；正向和逆向两个镜头必须**分别**替换、验证。 |
| 09 | `八年级/第二学期/第二十三章-概率初步/004频率与概率的关系/probability_frequency.py` | 184 | H11 `GLOBAL_NUMPY_SEED` | 待复核全部随机调用后以局部 Generator 代替；同时校正“频率单调靠近概率”的教学风险；不覆盖正在进行的八年级其他 PR。 |
| 10 | `九年级/第一学期/第二十六章-二次函数/001二次函数的概念/quadratic_function.py` | 177 | H09 `PLAY_EMPTY_ANIMATION` | 源码实见 `FadeOut(x_lab) if x_lab else []`；改为条件追加动画并拆除 `x²` 动态零宽起点/超出纵轴的问题，逐段低清渲染。 |
| 11 | `九年级/第一学期/第二十六章-二次函数/004二次函数y=a(x-h)²+k的图像与性质/quadratic_function_vertex.py` | 725 | H01 `CHINESE_IN_TEX` | 待核查字面中文的上下文/实际模板；分离中文 Text 和 LaTeX MathTex。 |
| 12 | 同上 `quadratic_function_vertex.py` | 737 | H01 `CHINESE_IN_TEX` | 同上；一个文件的两处命中均需复核。 |
| 13 | `九年级/第一学期/第二十六章-二次函数/004二次函数y=a(x-h)²+k的图像与性质/quadratic_vertex_form.py` | 630 | H01 `CHINESE_IN_TEX` | 待复核原调用及可能的自定义 TeX 模板。 |
| 14 | `九年级/第二学期/第二十八章-统计初步/007用样本估计总体/sample_estimation.py` | 54 | H11 `GLOBAL_NUMPY_SEED` | 待查看下游取样方式，使用局部生成器隔离随机状态并检查样本/总体估计公式。 |

按**提示条目数**统计：六年级 6→5、七年级 0→0、八年级 3→3、九年级 5→5。按**文件数**统计不能把同一课的五个角度符号当作五份课件。零告警的七年级依然需要数学正确性、屏幕布局及未命中模板的逐课复查。

## 三、扫描器不能自动证明、但已在先前审查中定位的风险

- [九年级二次函数审查](grade9-code-audit.md)：以变量表示 `x_range` 时，初始端点在运行时重合，不会命中字面 `ZERO_WIDTH_PLOT` 规则；标准抛物线纵轴溢出、交点式的实根前提也需实质修改。
- [九年级垂径定理/方差审查](grade9-code-audit.md)：退化输入、图形与注释不一致、硬编码数据仍需逐镜复核。
- [八年级专项审查（#28）](https://github.com/1998x-stack/manim_math/pull/28)：透明高亮框生命周期修复位于另一个未合并分支，不得计入本 PR 的修复；概率课的前提与动态文案尚待治理。
- [七年级专项审查（#23）](https://github.com/1998x-stack/manim_math/pull/23)：四个课件的修复仍处于独立 PR，勿因本轮扫描零提示而重复改动或断言逐课合格。

## 四、验收分级

每个实际修复按「发现并复核源码 → 最小源码修复 → AST/回归测试 → 数学不变量 → Manim+LaTeX 低清渲染/关键帧 → 发布新视频」分级记录。当前台账仅第 01 项达到源码修复与本扫描器复扫阶段；其余 13 条及其他未命中问题没有被标记为已修。旧 `*.mp4` 未重制，不能视为新版源码结果。
