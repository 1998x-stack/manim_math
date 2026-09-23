# 八年级源码审查与修复记录（阶段一）

目标：`初中/八年级/` 两学期八章，兼容原知识点路径、Scene 类名、竖屏配置及既有画廊；**不重新编码或冒称修改历史 MP4**。分清已实修、已静态扫描、尚待真实渲染的验收层次。

## 已实施的源码修复

| 知识点 / 文件 | 已从原源码定位的缺陷 | 修复及回归保障 |
| --- | --- | --- |
| 第一学期·第十七章·001一元二次方程的概念/`001_一元二次方程的概念.py` | 原场景新建透明 `SurroundingRectangle` 用于 `FadeOut`，没有移除此前显示的高亮框；各分镜对象残留。 | 保存/正确替换高亮对象；`_clear` 对实际的顶层对象清场且保留水印；明确 `a≠0`、化简后才能判断次数，并加入 `x²-x²+x=0` 降次反例。`tests/test_grade8_quadratic_contract.py` 防止基本回退。 |
| 第一学期·第十九章·008勾股定理的逆定理/`pythagorean_inverse.py` | 旧图在 A 点画直角但正文及逆定理结论写为 `∠C=90°`，部分 MathTex 直接使用 Unicode 度数符号，几何角、对边与公式互相不符。 | 统一 `C` 为直角点、`a=BC`、`b=CA`、`c=AB`，相应 3-4-5 图示采用 C 为直角；MathTex 统一 `90^\circ`。新增无 Manim 的三边判定函数及 `tests/test_grade8_pythagorean_math.py`，覆盖典型勾股数组、非直角/退化/非有限边等。 |
| 第二学期·第二十三章·004频率与概率的关系/`probability_frequency.py` | 原 `np.random.seed(42)` 修改进程级 RNG；以固定常数展示的频率与模拟曲线来源不一致；`P=m/n` 未明确等可能前提；“次数越多越精确”等绝对表述易误导。 | 使用局部 `np.random.default_rng(seed)`，统一从同一条公平硬币模拟路径产生表格、图像和频率示例；频率可能波动，不保证误差单调减小；限定等可能计数公式及独立重复试验的条件。将无法确认来源的历史实验表替换为注明性质的模拟数据。新增 `tests/test_grade8_probability_math.py`，验证频率公式、不污染全局 RNG、确定性复现和参数边界。 |

三节课保留公开 Scene 名称、9:16 画幅和作者水印。重写的分镜须与对应 `storyboard.md` 人工核对；**旧视频不是新源代码的渲染产物**。尤其应实测二次根式、公式较长的横向布局和概率折线图的画框边界。

## 范围和实际证据

`tools/audit_grade8.py` 提供不导入 Manim 的递归 AST 检查、学期/章节/Scene 类清单、语法错误、部分高亮框生命周期错误、中文放进 LaTeX 和修改全局 RNG 的静态预警。首次 `grade8-audit.json` 在 GitHub Actions 中覆盖 **52 个 Python 文件、8 个章节**，发现 `probability_frequency.py` 原第 184 行的一处进程级随机种子风险；该风险已在上述场景重写中处理。静态规则没有发现问题**不等于**每节课数学正确、对象不裁切、字体可用或音视频通过。

GitHub Actions `grade8-source-audit.yml` 为每个相关 PR 提供 Python 语法编译、六项 AST 规则测试、三项一元二次方程契约测试、三项勾股逆定理测试、四项依赖 NumPy 的概率模拟测试以及 JSON 审计 artifact；对三节已修场景单独启用 `--strict`。GitHub Actions 的具体成功/失败状态应以对应 commit 的运行结果为准，不能把 workflow 的存在写成已通过。全学年遗留缺陷的误报/漏报需持续通过真实渲染、数学校核验证。

## 已确认、尚未处理的风险

- 第一学期·第十六章·002二次根式的性质/`radical_properties.py`：`scene_4_prop2_trap` 中 `case_a_result` 紧接原有较长公式右侧的 `next_to(..., RIGHT)`，存在超出 9 单位画幅的排版风险。需低清渲染该分镜，若越界则改为上下布局/缩放并断言对象边界。
- 第一学期·第十八章·003反比例函数/`inverse_proportion.py`：文字“k 固定，x 越大，y 越小”未限制 `k>0` 和同一单调区间。对于 `k<0` 或从 x<0 跳到 x>0 的比较，该说法不成立。应结合双曲线两个分支单独叙述单调性、限定 `k≠0` 与 `x≠0`。
- 全部几何类场景：角标/长度标签是否与生成的顶点坐标一致，动态变形是否破坏不变量；需逐镜比较。

## 八章数学验收重点

| 章节 | 高风险边界 |
| --- | --- |
| 第一学期·16 二次根式 | 开平方的定义域、`√(a²)=|a|`、分母非零及负数输入。 |
| 第一学期·17 一元二次方程 | 整理后次数与 `a≠0`，判别式正/零/负，根代入验算。 |
| 第一学期·18 正/反比例函数 | 参数符号、各区间单调性、`x≠0` 与坐标变换。 |
| 第一学期·19 几何证明 | 角—边对应、退化三角形、几何前提、反例和准确的坐标标注。 |
| 第二学期·20 一次函数 | 斜率的零/正/负情形、截距和图像一致性。 |
| 第二学期·21 代数方程 | 原方程定义域、分母限制、平方后增根验算。 |
| 第二学期·22 四边形 | 图形充分/必要判定条件、边角对角线几何不变量。 |
| 第二学期·23 概率初步 | 等可能计数前提、无重复遗漏的列举、随机频率与概率的关系。 |

## 复现检查与发布门禁

```bash
python -m compileall -q '初中/八年级'
python tools/audit_grade8.py --json > grade8-audit.json
python -m unittest discover -s tests -p 'test_audit_grade8.py' -v
python -m unittest discover -s tests -p 'test_grade8_quadratic_contract.py' -v
python -m unittest discover -s tests -p 'test_grade8_pythagorean_math.py' -v
# NumPy 1.26.4 环境：
python -m unittest discover -s tests -p 'test_grade8_probability_math.py' -v

# 有 Manim、LaTeX、中文字体、FFmpeg 的环境中，依次低质量渲染三个真实 Scene：
manim -ql '初中/八年级/第一学期/第十七章-一元二次方程/001一元二次方程的概念/001_一元二次方程的概念.py' '一元二次方程的概念Animation'
manim -ql '初中/八年级/第一学期/第十九章-几何证明/008勾股定理的逆定理/pythagorean_inverse.py' PythagoreanInverse
manim -ql '初中/八年级/第二学期/第二十三章-概率初步/004频率与概率的关系/probability_frequency.py' ProbabilityFrequency
```

**发布前必须实际执行** Manim 低清渲染、抽帧检查 9:16 边框与水印，数学专家核对定义域/角边/统计前提，然后生产渲染并用 `ffprobe` 审核视频；本 PR 暂不修改成片及画廊。未完成这些检查前保持 Draft，不将 52 个文件的语法通过宣传为 52 节数学动画全部修复。
