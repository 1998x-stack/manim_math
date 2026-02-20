# 等差数列教学动画 - 分镜脚本

## 元信息
- **目标时长**: 75-90 秒
- **场景数量**: 8 个
- **难度等级**: 高二第一学期
- **知识点**: 等差数列的定义、通项公式、前n项和、等差中项、性质

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要数列项
COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调/公差
COLOR_HIGHLIGHT = "#f39c12"    # 橙色 - 重点内容
COLOR_AUXILIARY = "#95a5a6"    # 灰色 - 辅助线
COLOR_FORMULA = "#2ecc71"      # 绿色 - 公式
COLOR_BACKGROUND = "#1a1a2e"   # 深蓝背景
```

## 核心元素预计算

### 等差数列参数
```python
# 示例数列: 2, 5, 8, 11, 14, 17, 20, ...
self.a1 = 2          # 首项
self.d = 3           # 公差
self.n_terms = 7     # 展示项数

# 计算各项
self.terms = [self.a1 + (n-1) * self.d for n in range(1, self.n_terms + 1)]
# 结果: [2, 5, 8, 11, 14, 17, 20]
```

### NumberLine配置
```python
self.number_line_range = [0, 22, 1]  # [min, max, step]
self.number_line_length = 7          # 逻辑长度
self.number_line_center = ORIGIN + DOWN * 1
```

### Axes配置（场景6）
```python
self.axes_config = {
    "x_range": [0, 8, 1],
    "y_range": [0, 22, 5],
    "x_length": 6,
    "y_length": 7,
    "axis_config": {"include_numbers": True}
}
self.axes_center = UP * 0.5
```

### 几何验证清单
| 验证项 | 公式 | 说明 |
|--------|------|------|
| 公差一致性 | `terms[i+1] - terms[i] == d` | 所有相邻项差相等 |
| 通项公式 | `terms[n-1] == a1 + (n-1)*d` | 验证通项公式 |
| 前n项和 | `sum(terms) == n*(a1+an)/2` | 验证求和公式 |
| 等差中项 | `2*terms[i] == terms[i-1]+terms[i+1]` | 中间项是两边的平均 |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 快速吸引注意力，引出等差数列概念

### 元素
1. 作者标识（顶部）
2. 钩子问题（大字）："2, 5, 8, 11, 14, ...下一个是？"
3. 数轴快闪动画

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 顶部灰色小字 |
| 0.3s | 钩子问题书写 | `Write(hook_question)` | "2, 5, 8, 11, 14, ...?" 大号字体 |
| 1.0s | 数轴创建 | `Create(number_line)` | 0-22的数轴 |
| 1.5s | 点依次跳出 | `LaggedStart(*[GrowFromCenter(dot) for dot in dots])` | 7个点按数列值位置 |
| 2.8s | 问号闪烁 | `Flash(question_mark)` | 强调悬念 |
| 3.3s | 等待 | `self.wait(0.5)` | 给观众思考时间 |

### 几何计算
```python
# 数轴上各点的位置
dot_positions = [
    number_line.number_to_point(term) 
    for term in self.terms
]
```

### 清理
- FadeOut: hook_question, question_mark
- 保留: author_info, number_line, dots

---

## Scene 2: 等差数列定义 (10-12秒)
**目的**: 清晰定义等差数列，强调公差概念

### 元素
1. 定义文字（中文）
2. 数学表达式：aₙ₊₁ - aₙ = d
3. 公差标注（Brace）
4. 动画演示相邻项的差

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题出现 | `Write(title)` | "等差数列 Arithmetic Sequence" |
| 0.6s | 定义文字 | `FadeIn(definition_text)` | "从第二项起，每项与前一项的差等于同一常数" |
| 1.5s | 公式出现 | `Write(formula_definition)` | aₙ₊₁ - aₙ = d (常数) |
| 2.3s | 高亮第一对 | `Indicate(dot[0], dot[1])` | 闪烁第1和第2个点 |
| 2.8s | Brace标注d | `GrowFromCenter(brace_1)` | 括号连接两点，标注"d=3" |
| 3.5s | 高亮第二对 | `Indicate(dot[1], dot[2])` | 第2和第3个点 |
| 4.0s | Brace标注d | `GrowFromCenter(brace_2)` | 同样标注"d=3" |
| 4.7s | 强调公差一致 | `Flash(d_labels, color=COLOR_SECONDARY)` | 所有d标签同时闪烁 |
| 5.5s | 公差值动画 | `Transform(d_labels to single_d)` | 所有d标签聚合成一个"公差 d = 3" |
| 7.0s | 说明文字 | `FadeIn(explanation)` | "公差可正、可负、可为零" |
| 8.5s | 等待 | `self.wait(1.5)` | 让学生理解 |

### 几何计算
```python
# Brace位置计算
for i in range(len(dots) - 1):
    brace = Brace(
        Line(dot_positions[i], dot_positions[i+1]),
        direction=UP,
        buff=0.1
    )
    label = MathTex(f"d={self.d}").next_to(brace, UP, buff=0.05)
```

### 清理
- FadeOut: title, definition_text, formula_definition, braces, explanation
- 保留: number_line, dots, single_d (缩小移到右上角)

---

## Scene 3: 通项公式推导 (15-18秒)
**目的**: 直观推导通项公式 aₙ = a₁ + (n-1)d

### 元素
1. 逐步展示各项
2. 规律识别动画
3. 通项公式推导过程
4. 最终公式高亮

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题 | `Write(title)` | "通项公式 General Term" |
| 0.6s | 显示a₁ | `Write(term_1)` | a₁ = 2 |
| 1.2s | 显示a₂ | `Write(term_2)` | a₂ = a₁ + d = 2 + 3 = 5 |
| 2.0s | 箭头连接 | `GrowArrow(arrow_1)` | a₁ → a₂ 标注"+d" |
| 2.6s | 显示a₃ | `Write(term_3)` | a₃ = a₁ + 2d = 2 + 2×3 = 8 |
| 3.3s | 箭头连接 | `GrowArrow(arrow_2)` | a₂ → a₃ 标注"+d" |
| 4.0s | 显示a₄ | `Write(term_4)` | a₄ = a₁ + 3d = 2 + 3×3 = 11 |
| 4.7s | 省略号 | `FadeIn(ellipsis)` | ... |
| 5.3s | 规律框选 | `ShowCreationThenDestruction(rect)` | 红框圈出"d的系数=n-1"规律 |
| 6.5s | 通项公式出现 | `Write(formula_general)` | aₙ = a₁ + (n-1)d |
| 7.5s | 公式放大高亮 | `formula_general.animate.scale(1.3).set_color(COLOR_FORMULA)` | 强调核心公式 |
| 8.5s | 验证示例 | `FadeIn(verification)` | 例：a₇ = 2+(7-1)×3 = 20 ✓ |
| 10.0s | 第七个点闪烁 | `Flash(dots[6])` | 对应a₇ |
| 11.5s | 等待 | `self.wait(2.0)` | 关键公式，多停留 |

### 几何计算
```python
# 公式排列（纵向）
formulas = VGroup(
    MathTex(r"a_1 = 2"),
    MathTex(r"a_2 = a_1 + d = 5"),
    MathTex(r"a_3 = a_1 + 2d = 8"),
    MathTex(r"a_4 = a_1 + 3d = 11"),
    Tex(r"\vdots"),
    MathTex(r"a_n = a_1 + (n-1)d", color=COLOR_FORMULA)
).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
formulas.move_to(UP * 2)
```

### 清理
- FadeOut: title, term_1~4, arrows, ellipsis, verification
- 保留: formula_general (移到顶部作为参考), number_line, dots

---

## Scene 4: 前n项和公式 (18-20秒)
**目的**: 推导和展示前n项和的两个公式

### 元素
1. 求和符号 Σ
2. 倒序相加法动画
3. 两个求和公式
4. 公式等价性说明

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题 | `Write(title)` | "前n项和 Sum of First n Terms" |
| 0.6s | 求和式 | `Write(sum_notation)` | Sₙ = a₁ + a₂ + ... + aₙ |
| 1.5s | 正序展开 | `FadeIn(forward_seq)` | Sₙ = a₁ + (a₁+d) + ... + aₙ |
| 2.5s | 倒序展开 | `FadeIn(reverse_seq)` | Sₙ = aₙ + (aₙ-d) + ... + a₁ |
| 3.5s | 对齐动画 | `reverse_seq.animate.next_to(forward_seq, DOWN)` | 两式上下对齐 |
| 4.5s | 逐项相加 | `Create(addition_lines)` | 画竖线连接对应项 |
| 5.5s | 结果展示 | `Write(sum_result)` | 2Sₙ = (a₁+aₙ) + (a₁+aₙ) + ... = n(a₁+aₙ) |
| 7.0s | 公式1推出 | `Write(formula_sum_1)` | Sₙ = n(a₁+aₙ)/2 |
| 8.0s | 公式1高亮 | `formula_sum_1.animate.set_color(COLOR_FORMULA)` | 第一个求和公式 |
| 9.0s | 替换aₙ | `TransformMatchingTex(formula_sum_1, formula_sum_2)` | 将aₙ替换为a₁+(n-1)d |
| 10.5s | 公式2推出 | `Write(formula_sum_2_final)` | Sₙ = na₁ + n(n-1)d/2 |
| 11.5s | 两公式并列 | `VGroup(formula_sum_1, formula_sum_2_final).arrange(DOWN)` | 展示两个等价公式 |
| 12.5s | 验证示例 | `FadeIn(example)` | 例：S₇ = 7×(2+20)/2 = 77 |
| 14.0s | 数轴上标注总和 | `Create(sum_brace)` | 大括号标注所有点，显示"S₇=77" |
| 16.0s | 等待 | `self.wait(2.0)` | 重要公式停留 |

### 几何计算
```python
# 验证计算
n = 7
a1 = 2
an = 20
d = 3

# 公式1
sum_1 = n * (a1 + an) / 2  # = 77

# 公式2
sum_2 = n * a1 + n * (n - 1) * d / 2  # = 77

# 断言
assert abs(sum_1 - sum_2) < 1e-10
```

### 清理
- FadeOut: title, all intermediate steps, example
- 保留: formula_sum_1, formula_sum_2_final (缩小移到参考区), number_line, dots

---

## Scene 5: 等差中项 (8-10秒)
**目的**: 解释等差中项概念及其几何意义

### 元素
1. 三个数 a, A, b
2. 等差中项定义：A = (a+b)/2
3. 数轴上的视觉演示
4. 中点关系

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题 | `Write(title)` | "等差中项 Arithmetic Mean" |
| 0.6s | 定义 | `FadeIn(definition)` | "若a, A, b成等差数列，则A为a和b的等差中项" |
| 1.5s | 新数轴 | `Create(simple_line)` | 简化数轴，只标3个点 |
| 2.0s | 三点出现 | `FadeIn(point_a, point_A, point_b)` | a=5, A=8, b=11 |
| 2.8s | 标签 | `Write(labels)` | 标注"a", "A", "b" |
| 3.5s | 距离标注 | `GrowFromCenter(brace_left, brace_right)` | 左右两段标注"d" |
| 4.5s | 等式出现 | `Write(equation_1)` | A - a = b - A |
| 5.5s | 移项 | `TransformMatchingTex(equation_1, equation_2)` | 2A = a + b |
| 6.5s | 中项公式 | `Write(formula_mean)` | A = (a+b)/2 |
| 7.5s | 公式高亮 | `formula_mean.animate.scale(1.2).set_color(COLOR_FORMULA)` | 强调 |
| 8.0s | 几何意义 | `FadeIn(geometry_note)` | "A是a和b的中点（算术平均）" |
| 9.0s | 等待 | `self.wait(1.0)` | 理解时间 |

### 几何计算
```python
# 三点位置（等差）
a_val = 5
A_val = 8
b_val = 11

# 验证等差中项
assert A_val == (a_val + b_val) / 2  # 8 == 8 ✓

# 数轴位置
point_a = simple_line.number_to_point(a_val)
point_A = simple_line.number_to_point(A_val)
point_b = simple_line.number_to_point(b_val)

# 验证中点
midpoint = (point_a + point_b) / 2
assert np.allclose(point_A, midpoint)  # 几何验证
```

### 清理
- FadeOut: title, definition, simple_line, all elements
- 保留: formula_mean (移到参考区)

---

## Scene 6: 图形规律 (10-12秒)
**目的**: 用坐标系展示等差数列的线性特征

### 元素
1. 坐标系 Axes (n为横轴，aₙ为纵轴)
2. 数列各项的点
3. 连接的直线
4. 斜率标注

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题 | `Write(title)` | "图形特征 Graphical Pattern" |
| 0.6s | 坐标系创建 | `Create(axes)` | n-aₙ 坐标系 |
| 1.5s | 轴标签 | `Write(x_label, y_label)` | "n" 和 "aₙ" |
| 2.3s | 点依次出现 | `LaggedStart(*[GrowFromCenter(dot) for dot in points])` | (1,2), (2,5), ..., (7,20) |
| 3.5s | 连线 | `Create(connecting_line)` | 连接所有点的直线 |
| 4.5s | 函数标注 | `Write(function_label)` | aₙ = a₁ + (n-1)d |
| 5.5s | 线性强调 | `Indicate(connecting_line)` | 闪烁直线 |
| 6.5s | 斜率说明 | `FadeIn(slope_explanation)` | "斜率 = 公差 d = 3" |
| 7.5s | 斜率标注 | `Create(slope_triangle)` | 画直角三角形标注Δy/Δx=d |
| 8.5s | 截距说明 | `FadeIn(intercept_note)` | "n=0时的纵截距 = a₁-d" |
| 9.5s | 等待 | `self.wait(1.5)` | 理解线性关系 |

### 几何计算
```python
# 坐标点
points_coords = [(n, self.a1 + (n-1)*self.d) for n in range(1, 8)]
# [(1,2), (2,5), (3,8), (4,11), (5,14), (6,17), (7,20)]

# 在坐标系中的位置
point_positions = [axes.c2p(n, an) for n, an in points_coords]

# 拟合直线（验证线性）
from numpy.polynomial import Polynomial
ns = [p[0] for p in points_coords]
ans = [p[1] for p in points_coords]
poly = Polynomial.fit(ns, ans, 1)  # 一次多项式
# 系数应为: [a₁-d, d] = [-1, 3]
assert abs(poly.coef[1] - self.d) < 1e-10  # 斜率=d

# 直线函数图
line_graph = axes.plot(
    lambda n: self.a1 + (n-1)*self.d,
    x_range=[0.5, 7.5],
    color=COLOR_PRIMARY
)
```

### 清理
- FadeOut: title, axes, all elements
- 保留: 无

---

## Scene 7: 性质与应用 (8-10秒)
**目的**: 展示等差数列的关键性质和简单应用

### 元素
1. 性质：m+n=p+q ⇒ aₘ+aₙ=aₚ+aₓ
2. 简单应用例子
3. 快速解题示例

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题 | `Write(title)` | "重要性质 Key Properties" |
| 0.6s | 性质1 | `Write(property_1)` | m+n = p+q ⇒ aₘ+aₙ = aₚ+aₓ |
| 1.5s | 示例 | `FadeIn(example_indices)` | 例：3+5 = 2+6，验证a₃+a₅ = a₂+a₆ |
| 2.5s | 计算验证 | `Write(calculation)` | 8+14 = 22, 5+17 = 22 ✓ |
| 3.5s | 应用题 | `FadeIn(problem)` | "某等差数列，a₃=7, a₇=15, 求a₅" |
| 4.5s | 解法提示 | `Write(hint)` | "利用等差中项：a₅ = (a₃+a₇)/2" |
| 5.5s | 计算过程 | `Write(solution)` | a₅ = (7+15)/2 = 11 |
| 6.5s | 答案强调 | `Circumscribe(solution, color=COLOR_HIGHLIGHT)` | 圈出答案 |
| 7.5s | 等待 | `self.wait(1.5)` | 理解应用 |

### 几何计算
```python
# 验证性质
m, n, p, q = 3, 5, 2, 6
assert m + n == p + q  # 3+5 = 2+6 = 8

a_m = self.terms[m-1]  # a₃ = 8
a_n = self.terms[n-1]  # a₅ = 14
a_p = self.terms[p-1]  # a₂ = 5
a_q = self.terms[q-1]  # a₆ = 17

assert a_m + a_n == a_p + a_q  # 8+14 = 5+17 = 22 ✓

# 应用题验证
a3 = 7
a7 = 15
a5 = (a3 + a7) / 2  # = 11
# 反推验证
d = (a7 - a3) / (7 - 3)  # = 2
assert a5 == a3 + (5-3) * d  # 11 = 7+2×2 ✓
```

### 清理
- FadeOut: 所有元素
- 保留: 无

---

## Scene 8: 总结与关注 (5-6秒)
**目的**: 总结关键公式，引导关注

### 元素
1. 关键公式汇总
2. 作者信息放大
3. 关注提示动画

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题 | `Write(title)` | "等差数列要点" |
| 0.5s | 公式框1 | `FadeIn(formula_box_1)` | 通项公式：aₙ = a₁+(n-1)d |
| 1.0s | 公式框2 | `FadeIn(formula_box_2)` | 求和公式：Sₙ = n(a₁+aₙ)/2 |
| 1.5s | 公式框3 | `FadeIn(formula_box_3)` | 等差中项：A = (a+b)/2 |
| 2.0s | 作者信息放大 | `author_info.animate.scale(2).move_to(ORIGIN)` | 从顶部移到中央 |
| 2.8s | 关注提示 | `Write(follow_text)` | "关注我，掌握更多数学技巧！" |
| 3.5s | 点赞动画 | `Create(thumb_icon)` | 大拇指图标 |
| 4.2s | 图标闪烁 | `Flash(thumb_icon, color=COLOR_HIGHLIGHT)` | 强调 |
| 5.0s | 等待 | `self.wait(1.0)` | 结束停留 |

### 几何计算
无特殊几何计算

### 清理
全部保留至结束

---

## 元素生命周期追踪表

| 元素ID | 创建场景 | 销毁场景 | 持续场景 | 备注 |
|--------|---------|---------|---------|------|
| `author_info` | Scene 1 | Scene 8 | 全程 | 顶部作者信息 |
| `number_line` | Scene 1 | Scene 5结束 | 1-5 | 主数轴 |
| `dots` | Scene 1 | Scene 5结束 | 1-5 | 数列各项的点 |
| `hook_question` | Scene 1 | Scene 1 | 1 | 开场问题 |
| `formula_general` | Scene 3 | Scene 8 | 3-8 | 通项公式（缩小后保留） |
| `formula_sum_1` | Scene 4 | Scene 8 | 4-8 | 求和公式1（缩小后保留） |
| `formula_sum_2` | Scene 4 | Scene 8 | 4-8 | 求和公式2（缩小后保留） |
| `formula_mean` | Scene 5 | Scene 8 | 5-8 | 等差中项公式（缩小后保留） |
| `axes` | Scene 6 | Scene 6 | 6 | 坐标系 |
| `connecting_line` | Scene 6 | Scene 6 | 6 | 线性关系直线 |

---

## 动画节奏控制

### 各场景时长分配
| 场景 | 时长 | 节奏 | 说明 |
|------|------|------|------|
| Scene 1 | 3-4s | 快 | 吸引注意 |
| Scene 2 | 10-12s | 中 | 定义清晰 |
| Scene 3 | 15-18s | 慢 | 核心推导，重点停留 |
| Scene 4 | 18-20s | 慢 | 公式推导，重点停留 |
| Scene 5 | 8-10s | 中 | 补充概念 |
| Scene 6 | 10-12s | 中 | 视觉理解 |
| Scene 7 | 8-10s | 中 | 应用示例 |
| Scene 8 | 5-6s | 快 | 总结收尾 |

### 停顿策略
- **关键公式后**: 2-3秒（Scene 3, 4）
- **定义/性质后**: 1-1.5秒（Scene 2, 5, 7）
- **过渡动画**: 0.3-0.5秒
- **总计**: 约80秒（符合TikTok最佳长度）

---

## 渲染命令

```bash
# 快速预览（开发阶段）
manim -pql arithmetic_sequence.py ArithmeticSequenceLesson

# 高质量渲染（最终输出）
manim -qh arithmetic_sequence.py ArithmeticSequenceLesson

# 4K渲染（如需要）
manim -qk arithmetic_sequence.py ArithmeticSequenceLesson
```

---

## 质量检查清单

### 内容完整性
- [ ] 所有关键概念都有定义
- [ ] 通项公式推导清晰
- [ ] 求和公式有视觉证明
- [ ] 等差中项有几何解释
- [ ] 图形特征直观展示

### 技术规范
- [ ] 所有坐标通过NumPy精确计算
- [ ] 中文使用`Text()`，数学使用`MathTex()`
- [ ] 度数使用`^\circ`
- [ ] 所有几何关系已验证
- [ ] 元素位置在安全边界内

### 动画质量
- [ ] 节奏符合难度（慢快结合）
- [ ] 关键公式有足够停留
- [ ] 无元素重叠或溢出
- [ ] 颜色对比清晰
- [ ] 字体大小适中

### 教学效果
- [ ] 开场有吸引力
- [ ] 逻辑递进清晰
- [ ] 视觉辅助充分
- [ ] 总结完整
- [ ] 有互动提示（关注）

---

## 备注

1. **数列参数可调**: 如需演示不同数列，修改`self.a1`和`self.d`即可
2. **公式对齐**: 所有公式左对齐，便于阅读
3. **颜色一致性**: 同类元素使用相同颜色（如所有"d"用红色）
4. **音效建议**: 
   - Scene 1: 悬念音效
   - Scene 3, 4: 推导完成时"叮"声
   - Scene 8: 关注提示音
5. **字幕备选**: 如需字幕，放在底部安全区（y=-6到-7）