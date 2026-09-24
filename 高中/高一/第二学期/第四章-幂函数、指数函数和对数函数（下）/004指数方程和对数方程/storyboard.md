# 004 指数方程与对数方程｜修复后分镜和核验

Scene 入口：`ExponentialLogarithmicEquations`；七段教学函数，与 `exponential_logarithmic.py` 对应。数学坐标均由 `Axes.c2p` 映射到 9:16 画面，图像安全区最终以真实渲染包围盒为准。保留旧 MP4 与 Prompt，不将旧片作为新代码的验收。

## 数学规格

`2^x=8 ⇔ x=3`，指数函数底数为 2（大于 0 且不等于 1），故从 `2^x=2^3` 得 `x=3`。`log₂x=3` 要求 `x>0`，对应解 `x=8`。更复杂的对数方程必须先确定每个真数为正，换底数时需核实底数合法，再检验候选解。

新增验根示例：`log₂(x−1)+log₂(x−3)=3` 的原始定义域为 `x>3`。化为 `(x−1)(x−3)=8` 后，代数候选值为 `5,-1`；`-1` 不满足原定义域，`5` 代回得 `log₂4+log₂2=3`。

## 分镜

| Scene | learning_fact / 条件 | observable_state / 生命周期 | check |
|---|---|---|---|
| opening | 指数方程 `2^x=8` 与对数方程 `log₂t=3` 的未知数位置不同 | 两道题依次显示各自的解 3 与 8 | `verify_equations.py::test_exponential_solution` 与 `test_logarithm_solution` |
| exponential_definition | 同底数等式可比较指数，前提 a>0、a≠1 | `2^x=8→2^x=2³→x=3`，依序演示 | 检查底数条件与画面指数式 |
| exponential_graph_solution | 指数曲线与 `y=8` 的交点为 `(3,8)` | 坐标轴 x∈[-1,4]、y∈[0,9]；指数曲线只画到 `x=log₂9`，用垂线投影读取 x=3；同一身份清理 | `test_exp_curve_within_axes`，检查交点及渲染曲线端点 |
| same_base_method | 底数合法才可由 `a^u=a^v` 得 u=v | 纯公式推导，不依赖 `MathTex` 子字符下标猜底数 | 检查构造 API 和 TeX 数学语义 |
| logarithm_definition | `log₂x=3` 的真数须为正 | `x>0`、`x=8`、代回 `log₂8=3` | `test_logarithm_solution` |
| logarithm_graph_solution | 对数曲线与 `y=3` 的交点为 `(8,3)` | 坐标轴 x∈[0,10]、y∈[-1,4]；曲线仅显示 x∈[0.5,10]，绝不在 x≤0 时伪造函数值 | `test_log_curve_within_axes`；关键帧检查图与文字同步 |
| verification_outro | 变形后的代数候选解需验根 | 先展示 x>3，再解二次方程；排除 -1，代回验 5 | `test_log_equation_domain_and_extraneous_root`；结尾清理作者信息 |

## 证据等级

`syntax`、`math`、`unit_tests`、`ast`：本 PR 的 CI；`manim_render`、`frame_review`、`ffprobe`、`audio_review`：`not_run`。禁止以静态坐标检查替代实际对象宽高和音轨核验。
