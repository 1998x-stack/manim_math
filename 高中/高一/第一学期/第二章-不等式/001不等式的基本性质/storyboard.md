# 不等式的基本性质｜与 `inequality_properties_full.py` 同步的分镜

## 统一模型

场景使用 9×16 竖屏；标题 y≈5.65、一般公式 y≈4.6、操作前数轴 y≈2.65、操作后数轴 y≈-1.65，底部实例和说明至 y≈-4.45。数轴范围 [-6,6]，各次计算中的数字均应落在真实范围内。数学公式由 `MathTex` 展示，中文由 `Text` 展示。数轴位置与数学命题在本课中是具体例子，不将它们当作普遍证明。

| 镜头 / 实际方法 | 数学前提与 learning_fact | 实际屏幕数据和变化 | 独立 check |
|---|---|---|---|
| 1 `show_opening` | 引出负数乘法的变号问题 | `3>1` 同乘 -2 后 `-6<-2`；开场元素全部清除，作者信息常驻 | 数值和负号关系一致 |
| 2 `show_property_1` | `a>b ⇔ b<a` | 上数轴 3、1；下数轴 1、3；显示 `3>1`、`1<3` | 两侧交换且不等号方向改变 |
| 3 `show_property_2` | `a>b`、`b>c` 才可推 `a>c` | 4>2>-1，结论 4>-1，前后数轴数据以 4 为固定左侧值 | 4>2、2>-1 同时成立 |
| 4 `show_property_3` | `a>b ⇒ a+c>b+c` 对任意实数 c 成立 | 3>1，同加 -2 得 1>-1；上下数轴真实数字都更新 | 两端减去相同的 2，差保持不变 |
| 5 `show_property_4` | `a>b` 且 `c>0` ⇒ `ac>bc` | 2>1，两侧同乘 2 得 4>2 | 两端同乘且 c 严格大于 0 |
| 6 `show_property_5` | `a>b` 且 `c<0` ⇒ `ac<bc` | 2>1，两侧同乘 -2 得 -4<-2；不使用原脚本边界 -6 作为负数乘法唯一示例 | 保留乘法的负号，屏幕不等号真正变向 |
| 7 `show_property_6` | `a>b>0` 足以推出 `a²>b²`，不能对任意负数直接套用 | 使用同尺寸单位小正方形分别拼成 3×3 和 2×2；屏幕面积 9 与 4 严格对应 9:4。反例 -3<-2 但 9>4 | 9 与 4 是实际可见方格数量；检查 b=0、负数边界 |
| 8 `show_summary` | 六性质所需条件不能省略 | 六条公式占独立卡片，特别提示 c=0 时 ac=bc，无法沿用严格不等号 | 逐条从同一数学模型输出，不使用 `<=>` 之类的非标准 TeX 缩写 |
| 9 `show_outro` | 先看条件，再确定方向 | 作者标识和总结文字最终退出 | 屏上对象无残留 |

## 具体验收步骤

1. `python -m py_compile inequality_properties_full.py verify_inequality_properties.py`，然后 `python verify_inequality_properties.py`；回归脚本从真实 Scene 模型抽取五组数轴数值、符号和方格边长，对六性质做含 c=0、c<0、平方负数反例的纯 Python 验证。
2. `python .opencode/skills/manim-video-production/scripts/audit_scene.py <课程路径/inequality_properties_full.py> --json`；ERROR 必须修复，WARN 逐条人工判断。
3. 有 Manim、TeX、中文字体时运行 `manim -ql inequality_properties_full.py InequalityPropertiesFull`，逐镜核对数轴数字、网格 9/4、公式宽度、负数不等号方向、真实对象包围盒和首尾帧。正式视频还须 `ffprobe` 和声音检查。没有真实渲染时不得声称视频验收通过，亦不得覆盖已有 MP4。
