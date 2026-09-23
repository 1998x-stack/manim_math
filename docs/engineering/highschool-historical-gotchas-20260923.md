# 高中 Manim 历史 Gotchas：逐文件扫描与源码修复台账（2026-09-23）

> 范围：`高中/{高一,高二,高三}/**/*.py`。源代码静态检查与数学测试不等于真实 Manim/LaTeX/中文字体渲染，也不代表逐镜验证全部数学内容。旧 MP4 未更新。

## 历史依据和实际覆盖

- 历史七项与后续扩展：[historical-gotchas.md](historical-gotchas.md)；共用 `tools/audit_junior_gotchas.py:audit_source`，高中专用 `tools/audit_highschool_gotchas.py` 增加对嵌套 `self.play` 和 `random.seed` 的检查。
- [首次完整审计 CI](https://github.com/1998x-stack/manim_math/actions/runs/35826469193)：高一 **49**、高二 **42**、高三 **40**，合计 **131** 个 Python 文件；原历史规则 **0 error / 24 warnings**（22 处中文 Tex/MathTex、2 处 Unicode 度号）。原始逐条 JSON 为该运行的 `highschool-historical-gotchas` artifact。
- 新增动态调用规则并辨识显式 ctex 后，[复扫 CI](https://github.com/1998x-stack/manim_math/actions/runs/35826681321) 实见 **2 个 NESTED_SELF_PLAY error、21 个待修 warning、3 个显式 ctex 人工复核信息项**。ctex 仅降低“默认模板中文报错”这一类型的误报，不表示不需要字体/LaTeX 实际渲染。
- [受控源码修复和测试 CI](https://github.com/1998x-stack/manim_math/actions/runs/35826852209)：修复三份源文件后，全高中语法编译、6 个专项回归测试、131 份源码复扫通过；**0 error / 0 warning / 3 ctex review**。修复仅在隔离分支提交了三份课程源文件；一次性 `contents: write` 工作流已删除，持久 CI 为只读、严格审计。

## 首次命中的 6 份课件：逐文件结论

| 年级 / 路径（省略 `高中/`） | 原命中 | 本轮状态与具体处理 |
| --- | ---: | --- |
| `高一/第一学期/第三章-函数的基本性质/003函数的运算/function_operations.py` | `CHINESE_IN_TEX` 1 | **显式 `TexTemplateLibrary.ctex`**，不等同默认 TeX 中文错误；保留数学与文字原有排版，仅登记人工复核项，待真实渲染。 |
| `高一/第二学期/第五章-三角比/001任意角与弧度制/001_任意角与弧度制.py` | `UNICODE_IN_TEX` 1 | **源码已修**：动态角度 f-string 使用 `rf` 与 LaTeX `^{\\circ}`，保留 `任意角与弧度制Animation` Scene 入口；Text 里的正常 `°` 不删除。 |
| `高一/第二学期/第五章-三角比/002任意角的三角比/any_angle_trigonometry.py` | `UNICODE_IN_TEX` 1 | **源码已修**：角度标签使用 LaTeX `^{\\circ}`，将直接 `int(angle*180/PI)` 截断替换成 `int(round(np.degrees(angle)))`，避免浮点舍入导致 60° 显示 59°。 |
| `高一/第二学期/第六章-三角函数/003函数y=Asin(ωx+φ)的图像与性质/003_函数y=Asin(ωx+φ)的图像与性质.py` | `CHINESE_IN_TEX` 19；扩展规则 `NESTED_SELF_PLAY` 2 | **源码已修**：中文说明用 `Text`、数学分式/变量用 `MathTex`，19 处均改；两处错误嵌套 `self.play(self.play(...))` 统一改为一次 `self.play(*[FadeOut(...)])`；展示全周期的横轴覆盖 `[-2π,2π]`，当 `ω≠0` 时周期使用 `2π/|ω|`，振幅应取 `|A|`；保留原中文 Scene 名及动画顺序。 |
| `高二/第二学期/第十二章-圆锥曲线/002圆的方程/circle_equation.py` | `CHINESE_IN_TEX` 1 | **显式 ctex 人工复核**；圆心/半径表达式依赖该模板和所选 LaTeX 环境，尚无真实渲染证据。 |
| `高二/第二学期/第十二章-圆锥曲线/004椭圆的几何性质/ellipse_properties.py` | `CHINESE_IN_TEX` 1 | **显式 ctex 人工复核**；通径公式的中文编译与版面需实际渲染确认。 |

**高三 40 份源码**未触发本轮这些规则；不等同已逐镜验证。无规则命中的另 125 份高中课件也只是完成这一类静态扫描，不能标为“全面修好”。

## 可复跑验证

```bash
python -m compileall -q '高中'
python -m unittest discover -s tools/tests -p 'test_highschool_gotchas.py' -v
python tools/audit_highschool_gotchas.py --strict --json > highschool-gotchas.json
```

代码修改清单以本 PR 实际 `Files changed` 为准；`tools/repair_highschool_gotchas.py` 是有预期命中数量保护的**一次性修复脚本**，仅供追溯，不能对已修版本反复执行。工作流只读；不存在复用一次性写权限流程自动改动 `main` 的安排。

## 仍需逐课与逐镜完成的工作

1. 高一：三角函数课的箭头方向/相位平移、不同幅值与负频率、坐标轴标签、`TransformMatchingShapes` 的对象生命周期以及整体 9:16 边界；另两份三角比课角度及弧度位置、公式宽度、LaTeX 渲染。
2. 高二：三处 `ctex` 中对应的两处实际高二中文公式，结合仓库目标环境验证 XeLaTeX、中文字体和字幕间距；核查椭圆参数 `a>b>0`、根号/分母非零、圆的判别式三种情形。
3. 高三：逐 Scene 核对导数/参数/概率统计前提、退化输入、动态坐标上限与对象生命周期，不能以该轮零告警代替人工审阅。
4. 渲染门槛：按课程实际 Scene 入口执行 `manim -ql <文件> <Scene>`；记录 LaTeX/字体日志、关键帧、公式与字幕是否遮挡、画面外溢；再考虑重新生成旧 MP4。**本次未进行真实渲染，也未更换旧视频。**
