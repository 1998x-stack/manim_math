# 初中 Gotchas 第二轮修复与验收（2026-09-23）

## 范围与基线

基于 [`junior-gotchas-findings-20260923.md`](junior-gotchas-findings-20260923.md) 的首次 14 条、六年级首课修复后 13 条历史提示。重新检查 `main` 时，八年级勾股定理逆定理（LaTeX 度数）和频率与概率（局部 RNG、频率波动与等可能条件）已经由其他分支原位修复，因此本次**没有覆盖**那两份新源码。

本轮只改六年级与九年级的五份原有 Scene；不改入口名、目录、MP4、Gallery 索引及公开 URL。唯一的一次修复脚本 `tools/repair_junior_gotchas_round2.py` 使用有期望次数的源码预映像验证、整体 AST 语法验证后写文件，禁止盲目全仓库字符串替换。

## 已实际修复

| 课件 | 源码更改 | 验收范围 |
| --- | --- | --- |
| 六年级·弧长公式 `arc_length_formula.py` | 原有 `MathTex(r"n°")` 三处、`MathTex(r"360°")` 两处改成 `^{\\circ}`；保留 `ArcLengthFormula` 类。 | 五处均在 AST 契约测试中检查；未跑真实 LaTeX。 |
| 九年级·二次函数概念 `quadratic_function.py` | 移除未 add 到 Scene 的 `x_lab` 的非法 `FadeOut(x_lab) if x_lab else []`；标准 `x²` 曲线端点从 ±2.5 缩到 ±2，保证 y=4 不超出纵轴 y_max=5；ValueTracker 初始端点与左界差 0.02，避免 `Axes.plot` 零宽区间。 | 静态、语法和数值边界断言；其他平移/交点曲线可能有独立越界，须逐镜检验。 |
| 九年级·二次函数顶点式 `quadratic_function_vertex.py` | 最小值/最大值使用 `Text` 中文与 `MathTex("= k")` 并排，移除默认 MathTex 模板不兼容的中文。 | AST 契约检查中文片段与真实 MathTex 分离；待低清渲染。 |
| 九年级·另一顶点式 `quadratic_vertex_form.py` | 用 `Text("当")`、`Text("时，")` 与独立 `MathTex` 重建最值公式。 | 源码保留 `y_{\\min}=k` 数学含义；待检验文字排版。 |
| 九年级·样本估计 `sample_estimation.py` | `np.random.seed` 与 `random.seed` 改为 Scene 本地 `default_rng(42)`；总体生成与三次无放回抽样共用局部 Generator；改正“样本容量越大估计越准确”的确定性暗示，区分非随机抽样与随机抽样可能的抽样误差。 | AST 契约检查局部 RNG、`replace=False`、文案；尚未做场景统计蒙特卡罗和关键帧验收。 |

## 可追溯验证

[第二轮 GitHub Actions 运行](https://github.com/1998x-stack/manim_math/actions/runs/35825686338) 在源码写入后执行全部初中源码 `compileall`、5 项 `test_junior_round2_contract.py`、现有四年级 `audit_junior_gotchas.py`，再由受限工作流提交上述五份 Scene 到独立修复分支。该 CI 产出的 JSON 为 **211 份 Python 源码，0 条静态 error、0 条 warning**。这只证明检测器覆盖的语法/API/字面风险，不是全部数学证明、Manim 实机运行、LaTeX 编译、镜头审查或旧视频更新。最初一次 CI 因测试猜测 Scene 类名而未提交任何源码，改为检查真实的 `ArcLengthFormula` 入口后第二次 CI 通过。

## 尚需继续的实际源码问题

- `quadratic_function.py` 的另外两条平移曲线仍使用 `[-1.9,2.8]` 和 `[-2.0,2.8]`，在左端点时函数值可能超过现有纵轴上限 5；交点式示例 `x=-2.2` 的 y=5.04 同样略超限。需统一各曲线坐标域与图像轴边界后逐镜渲染，不能因为标准曲线已修而认为全片可发布。
- 同一课三种二次函数形式对比尚未在总结处明确：交点式 `a(x-x_1)(x-x_2)` 在实数课堂语境下要求存在实零点。应补充如 `y=x²+1` 的反例，不改写原有一般式/顶点式定义。
- 六年级弧长、九年级顶点公式的中文字体、位置、实际 LaTeX 构建和对象生命周期待 Manim 0.19.x + 可用中文字体环境中的低清渲染与关键帧核查。
- 其他未被 AST 命中的数学风险，参考 [`grade9-code-audit.md`](grade9-code-audit.md)：垂径定理退化输入与标注、方差数据硬编码等，仍未由本批修改解决。

## 后续验收命令（含人工审核步骤）

```bash
python -m compileall -q '初中'
python -m unittest discover -s tools/tests -p 'test_junior_round2_contract.py' -v
python tools/audit_junior_gotchas.py --json
# 在装好 manim/LaTeX/中文字体的环境逐个执行：
manim -ql '初中/六年级/第一学期/第四章-圆和扇形/005弧长公式/arc_length_formula.py' ArcLengthFormula
manim -ql '初中/九年级/第一学期/第二十六章-二次函数/001二次函数的概念/quadratic_function.py' QuadraticFunctionIntro
```

渲染后需复核画幅外对象、曲线端点、每个分镜的数学内容和旧视频差异；**旧 MP4 未替换**。
