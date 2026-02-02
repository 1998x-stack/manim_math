# 椭圆中点弦问题 - 动画分镜脚本

## 元信息
- 目标时长: 90-120 秒
- 场景数量: 8 个
- 难度等级: 高中数学
- 核心方法: 点差法

## 颜色配置
```python
COLOR_ELLIPSE = "#3498db"          # 蓝色 - 椭圆
COLOR_CHORD = "#e74c3c"            # 红色 - 弦AB
COLOR_MIDPOINT = "#f39c12"         # 橙色 - 中点M
COLOR_SLOPE_LINE = "#2ecc71"       # 绿色 - 斜率线
COLOR_FORMULA = "#9b59b6"          # 紫色 - 公式
COLOR_HIGHLIGHT = YELLOW           # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B           # 灰色 - 辅助线
```

## 几何预计算清单

### 基础椭圆参数
| 元素 | 值/公式 | 存储变量 |
|------|---------|---------|
| 长半轴 a | 4.0 | self.a |
| 短半轴 b | 2.0 | self.b |
| 椭圆缩放 | 0.7 | self.ELLIPSE_SCALE |
| 椭圆偏移 | UP * 1.0 | self.ELLIPSE_OFFSET |

### 关键点坐标
| 点 | 数学定义 | 计算方法 |
|---|----------|---------|
| 中点M | (x₀, y₀) | self.M = np.array([1.5, 0.8, 0]) * SCALE + OFFSET |
| 点A | (x₁, y₁) 在椭圆上 | 通过参数方程计算，满足椭圆方程和中点条件 |
| 点B | (x₂, y₂) 在椭圆上 | B = 2*M - A (中点公式反推) |
| 椭圆中心O | (0, 0) | self.O = ORIGIN + OFFSET |

### 斜率计算
| 项 | 公式 | 说明 |
|----|------|------|
| 弦斜率 k | k = -b²x₀/(a²y₀) | 点差法核心公式 |
| 验证 | k = (y₂-y₁)/(x₂-x₁) | 两点斜率公式验证 |

### 坐标系设置
```python
# Axes配置
x_range = [-5, 5, 1]
y_range = [-3, 3, 1]
axes_scale = 0.6
axes_offset = UP * 1.0
```

---

## Scene 1: 开场钩子 (0-5秒)

### 目的
吸引注意力，抛出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字动画)
3. 椭圆图形淡入
4. 中点M和弦AB同时出现

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字打字效果 | `Write(hook_text)` | 1.0s |
| 1.3s | 椭圆创建 | `Create(ellipse)` | 1.2s |
| 2.5s | 中点M闪现 | `FadeIn(dot_M, scale=0.5), Flash(dot_M)` | 0.5s |
| 3.0s | 弦AB绘制 | `Create(chord_AB)` | 0.8s |
| 3.8s | 等待理解 | `Wait(1.2)` | 1.2s |

### 钩子文字内容
```
主标题: "椭圆的中点弦"
副标题: "已知中点，如何求弦的方程?"
```

### 关键代码片段
```python
hook_main = Text(
    "椭圆的中点弦",
    font="Noto Sans CJK SC",
    font_size=48,
    color=COLOR_HIGHLIGHT
).move_to(UP * 6)

hook_sub = Text(
    "已知中点M，弦AB的斜率是多少?",
    font="Noto Sans CJK SC",
    font_size=28,
    color=GRAY_A
).move_to(UP * 5.2)
```

### 几何初始化
```python
# 椭圆
ellipse = Ellipse(
    width=2*self.a*self.ELLIPSE_SCALE,
    height=2*self.b*self.ELLIPSE_SCALE,
    color=COLOR_ELLIPSE,
    stroke_width=3
).move_to(self.ELLIPSE_OFFSET)

# 中点M (椭圆内部)
dot_M = Dot(self.M, color=COLOR_MIDPOINT, radius=0.12)
label_M = MathTex("M(x_0, y_0)", font_size=24, color=COLOR_MIDPOINT).next_to(dot_M, UR, buff=0.15)

# 弦AB (需精确计算A, B使其在椭圆上且M为中点)
chord_AB = Line(self.A, self.B, color=COLOR_CHORD, stroke_width=4)
```

### 清理
- FadeOut: hook_main, hook_sub
- 保留: ellipse, chord_AB, dot_M, label_M, author_info

---

## Scene 2: 问题设定 (5-12秒)

### 目的
明确题目条件和目标

### 元素
1. 椭圆方程显示
2. 条件列表动画
3. 目标公式框

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 5.0s | 椭圆方程书写 | `Write(ellipse_eq)` | 0.8s |
| 5.8s | 条件1: 点A在椭圆上 | `FadeIn(cond_1, shift=UP*0.2)` | 0.5s |
| 6.3s | 高亮点A | `Flash(dot_A), dot_A.animate.scale(1.3)` | 0.4s |
| 6.7s | 条件2: 点B在椭圆上 | `FadeIn(cond_2, shift=UP*0.2)` | 0.5s |
| 7.2s | 高亮点B | `Flash(dot_B), dot_B.animate.scale(1.3)` | 0.4s |
| 7.6s | 条件3: M是中点 | `FadeIn(cond_3, shift=UP*0.2)` | 0.5s |
| 8.1s | 中点关系动画 | 显示虚线MA, MB | 0.6s |
| 8.7s | 目标框淡入 | `FadeIn(goal_box, shift=DOWN*0.3)` | 0.6s |
| 9.3s | 等待理解 | `Wait(2.7)` | 2.7s |

### 数学内容
```python
# 椭圆方程
ellipse_eq = MathTex(
    r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1",
    font_size=32,
    color=COLOR_ELLIPSE
).move_to(UP * 5.5)

# 条件列表 (使用Text + MathTex组合)
cond_1 = VGroup(
    Text("条件1: ", font="Noto Sans CJK SC", font_size=24, color=GRAY_A),
    MathTex(r"A(x_1, y_1)", font_size=24, color=COLOR_CHORD),
    Text(" 在椭圆上", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
).arrange(RIGHT, buff=0.1).move_to(UP * 4.5 + LEFT * 2)

cond_2 = VGroup(
    Text("条件2: ", font="Noto Sans CJK SC", font_size=24, color=GRAY_A),
    MathTex(r"B(x_2, y_2)", font_size=24, color=COLOR_CHORD),
    Text(" 在椭圆上", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
).arrange(RIGHT, buff=0.1).move_to(UP * 3.8 + LEFT * 2)

cond_3 = VGroup(
    Text("条件3: ", font="Noto Sans CJK SC", font_size=24, color=GRAY_A),
    MathTex(r"M(x_0, y_0)", font_size=24, color=COLOR_MIDPOINT),
    Text(" 是中点", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
).arrange(RIGHT, buff=0.1).move_to(UP * 3.1 + LEFT * 2)

# 目标框
goal_box = VGroup(
    Text("求: 弦AB的斜率", font="Noto Sans CJK SC", font_size=28, color=COLOR_HIGHLIGHT),
    MathTex(r"k = ?", font_size=32, color=COLOR_SLOPE_LINE)
).arrange(DOWN, buff=0.3).move_to(DOWN * 5)
```

### 点的标注
```python
# 添加点A, B的标注
dot_A = Dot(self.A, color=COLOR_CHORD, radius=0.10)
label_A = MathTex("A", font_size=22, color=COLOR_CHORD).next_to(dot_A, UL, buff=0.1)

dot_B = Dot(self.B, color=COLOR_CHORD, radius=0.10)
label_B = MathTex("B", font_size=22, color=COLOR_CHORD).next_to(dot_B, DR, buff=0.1)
```

### 清理
- FadeOut: ellipse_eq, cond_1, cond_2, cond_3, goal_box
- 保留: ellipse, chord_AB, dot_M, dot_A, dot_B, labels

---

## Scene 3: 点差法介绍 (12-20秒)

### 目的
引入点差法的核心思想

### 元素
1. 标题 "点差法"
2. 核心思想说明
3. 两个方程组显示

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 12.0s | 标题淡入 | `Write(title_method)` | 0.6s |
| 12.6s | 思想说明 | `FadeIn(idea_text, shift=UP*0.2)` | 0.8s |
| 13.4s | 方程1: A在椭圆上 | `Write(eq_A)` | 1.0s |
| 14.4s | 高亮点A | `Indicate(dot_A)` | 0.4s |
| 14.8s | 方程2: B在椭圆上 | `Write(eq_B)` | 1.0s |
| 15.8s | 高亮点B | `Indicate(dot_B)` | 0.4s |
| 16.2s | 减号动画 | `FadeIn(minus_sign)` | 0.3s |
| 16.5s | 两式相减提示 | `FadeIn(subtract_hint, shift=DOWN*0.2)` | 0.5s |
| 17.0s | 等待理解 | `Wait(3.0)` | 3.0s |

### 数学内容
```python
# 标题
title_method = Text(
    "点差法",
    font="Noto Sans CJK SC",
    font_size=40,
    color=COLOR_FORMULA
).move_to(UP * 6.5)

# 核心思想
idea_text = Text(
    "两点都在椭圆上 → 两式相减 → 得到关系",
    font="Noto Sans CJK SC",
    font_size=24,
    color=GRAY_A
).move_to(UP * 5.8)

# 方程组
eq_A = MathTex(
    r"\frac{x_1^2}{a^2} + \frac{y_1^2}{b^2} = 1",
    font_size=30,
    color=COLOR_CHORD
).move_to(UP * 4.5)

eq_B = MathTex(
    r"\frac{x_2^2}{a^2} + \frac{y_2^2}{b^2} = 1",
    font_size=30,
    color=COLOR_CHORD
).move_to(UP * 3.5)

# 减号
minus_sign = MathTex(
    r"-",
    font_size=40,
    color=YELLOW
).move_to(UP * 4.0 + LEFT * 3.5)

# 提示
subtract_hint = Text(
    "两式相减",
    font="Noto Sans CJK SC",
    font_size=26,
    color=COLOR_HIGHLIGHT
).move_to(UP * 2.5)
```

### 清理
- FadeOut: title_method, idea_text, subtract_hint
- 保留: eq_A, eq_B, minus_sign (为下一场景准备)

---

## Scene 4: 代数推导 - 相减 (20-32秒)

### 目的
展示点差法的代数计算过程

### 元素
1. 相减后的式子
2. 因式分解动画
3. 中点代入

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 20.0s | 清除前面方程 | `FadeOut(eq_A, eq_B, minus_sign)` | 0.4s |
| 20.4s | 相减结果书写 | `Write(subtract_result)` | 1.2s |
| 21.6s | 等待理解 | `Wait(1.0)` | 1.0s |
| 22.6s | 因式分解提示 | `FadeIn(factor_hint)` | 0.5s |
| 23.1s | 变换到因式分解 | `TransformMatchingTex(subtract_result, factored)` | 1.5s |
| 24.6s | 等待理解 | `Wait(1.2)` | 1.2s |
| 25.8s | 中点公式提示 | `FadeIn(midpoint_hint)` | 0.6s |
| 26.4s | 显示中点关系 | `Write(midpoint_formulas)` | 1.0s |
| 27.4s | 代入中点 | `TransformMatchingTex(factored, with_midpoint)` | 1.5s |
| 28.9s | 等待理解 | `Wait(3.1)` | 3.1s |

### 数学内容
```python
# 相减结果
subtract_result = MathTex(
    r"\frac{x_1^2 - x_2^2}{a^2} + \frac{y_1^2 - y_2^2}{b^2} = 0",
    font_size=28,
    color=COLOR_FORMULA
).move_to(UP * 4.5)

# 因式分解提示
factor_hint = Text(
    "因式分解",
    font="Noto Sans CJK SC",
    font_size=24,
    color=COLOR_HIGHLIGHT
).move_to(UP * 3.5)

# 因式分解结果
factored = MathTex(
    r"\frac{(x_1 - x_2)(x_1 + x_2)}{a^2} + \frac{(y_1 - y_2)(y_1 + y_2)}{b^2} = 0",
    font_size=26,
    color=COLOR_FORMULA
).move_to(UP * 4.5)

# 中点公式提示
midpoint_hint = Text(
    "利用中点坐标关系",
    font="Noto Sans CJK SC",
    font_size=24,
    color=COLOR_HIGHLIGHT
).move_to(UP * 2.5)

# 中点公式
midpoint_formulas = VGroup(
    MathTex(r"x_1 + x_2 = 2x_0", font_size=24),
    MathTex(r"y_1 + y_2 = 2y_0", font_size=24)
).arrange(RIGHT, buff=0.8).move_to(UP * 1.8)

# 代入中点后
with_midpoint = MathTex(
    r"\frac{2x_0(x_1 - x_2)}{a^2} + \frac{2y_0(y_1 - y_2)}{b^2} = 0",
    font_size=26,
    color=COLOR_FORMULA
).move_to(UP * 4.5)
```

### 清理
- FadeOut: factor_hint, midpoint_hint, midpoint_formulas
- 保留: with_midpoint (为下一场景)

---

## Scene 5: 得到斜率公式 (32-42秒)

### 目的
从代数式推导出斜率公式

### 元素
1. 斜率定义
2. 代数整理
3. 最终公式框

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 32.0s | 斜率定义淡入 | `FadeIn(slope_def)` | 0.6s |
| 32.6s | 等待理解 | `Wait(0.8)` | 0.8s |
| 33.4s | 两边除以(x₁-x₂) | `Write(divide_hint)` | 0.8s |
| 34.2s | 变换到整理式 | `TransformMatchingTex(with_midpoint, rearranged)` | 1.5s |
| 35.7s | 等待理解 | `Wait(1.0)` | 1.0s |
| 36.7s | 最终公式淡入 | `FadeIn(final_formula_box, shift=UP*0.3)` | 1.0s |
| 37.7s | 公式闪烁强调 | `Circumscribe(final_formula_box, color=YELLOW)` | 1.0s |
| 38.7s | 等待强调 | `Wait(3.3)` | 3.3s |

### 数学内容
```python
# 斜率定义
slope_def = MathTex(
    r"k = \frac{y_1 - y_2}{x_1 - x_2}",
    font_size=28,
    color=COLOR_SLOPE_LINE
).move_to(UP * 3.0)

# 提示
divide_hint = Text(
    "两边同时除以 (x₁ - x₂)",
    font="Noto Sans CJK SC",
    font_size=22,
    color=GRAY_A
).move_to(UP * 2.0)

# 整理后的式子
rearranged = MathTex(
    r"\frac{x_0}{a^2} + \frac{y_0}{b^2} \cdot k = 0",
    font_size=28,
    color=COLOR_FORMULA
).move_to(UP * 4.5)

# 最终公式框
final_formula_box = VGroup(
    Text("中点弦斜率公式:", font="Noto Sans CJK SC", font_size=28, color=COLOR_HIGHLIGHT),
    MathTex(
        r"k = -\frac{b^2 x_0}{a^2 y_0}",
        font_size=36,
        color=COLOR_SLOPE_LINE
    )
).arrange(DOWN, buff=0.3).move_to(DOWN * 4.5)

# 添加边框
formula_rect = SurroundingRectangle(
    final_formula_box,
    color=YELLOW,
    buff=0.3,
    stroke_width=3
)
final_formula_with_box = VGroup(final_formula_box, formula_rect)
```

### 清理
- FadeOut: with_midpoint, slope_def, divide_hint, rearranged
- 保留: final_formula_with_box (移到左上角)

---

## Scene 6: 几何验证 (42-54秒)

### 目的
用几何图形验证公式的正确性

### 元素
1. 公式移到左上角
2. 绘制斜率线
3. 数值验证

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 42.0s | 公式移动缩小 | `final_formula_with_box.animate.scale(0.6).to_corner(UL)` | 0.8s |
| 42.8s | 说明文字 | `FadeIn(verify_text)` | 0.5s |
| 43.3s | 计算斜率动画 | 显示计算过程 | 1.5s |
| 44.8s | 得到k值 | `Write(k_value)` | 0.6s |
| 45.4s | 绘制斜率线 | `Create(slope_line)` | 1.2s |
| 46.6s | 斜率线延长 | `slope_line.animate.scale(1.5)` | 0.8s |
| 47.4s | 验证提示 | `FadeIn(check_text)` | 0.5s |
| 47.9s | 两点斜率计算 | 显示 (y₂-y₁)/(x₂-x₁) | 1.2s |
| 49.1s | 结果一致动画 | 两个k值重叠 | 0.8s |
| 49.9s | 成功标记 | `FadeIn(checkmark)` | 0.4s |
| 50.3s | 等待确认 | `Wait(3.7)` | 3.7s |

### 数学内容
```python
# 验证说明
verify_text = Text(
    "几何验证",
    font="Noto Sans CJK SC",
    font_size=32,
    color=COLOR_HIGHLIGHT
).move_to(UP * 5.5)

# 计算过程 (假设 a=4, b=2, M(1.5, 0.8))
calc_steps = VGroup(
    MathTex(r"k = -\frac{2^2 \times 1.5}{4^2 \times 0.8}", font_size=26),
    MathTex(r"k = -\frac{4 \times 1.5}{16 \times 0.8}", font_size=26),
    MathTex(r"k = -\frac{6}{12.8} \approx -0.47", font_size=26)
).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(UP * 4.0 + LEFT * 1.5)

# k值
k_value = MathTex(
    r"k \approx -0.47",
    font_size=30,
    color=COLOR_SLOPE_LINE
).move_to(UP * 2.5)

# 斜率线 (通过M，斜率为k)
slope_line = Line(
    self.M + LEFT * 2,
    self.M + RIGHT * 2,
    color=COLOR_SLOPE_LINE,
    stroke_width=3
).rotate(np.arctan(self.calculated_k), about_point=self.M)

# 验证提示
check_text = Text(
    "用两点坐标验证:",
    font="Noto Sans CJK SC",
    font_size=24,
    color=GRAY_A
).move_to(DOWN * 3.5)

# 两点斜率
two_point_slope = MathTex(
    r"k = \frac{y_2 - y_1}{x_2 - x_1} \approx -0.47",
    font_size=26,
    color=COLOR_SLOPE_LINE
).move_to(DOWN * 4.5)

# 成功标记
checkmark = Text(
    "✓ 验证成功!",
    font="Noto Sans CJK SC",
    font_size=32,
    color=GREEN
).move_to(DOWN * 6)
```

### 清理
- FadeOut: verify_text, calc_steps, k_value, check_text, two_point_slope, checkmark
- 保留: ellipse, chord_AB, slope_line, final_formula_with_box

---

## Scene 7: 特殊情况说明 (54-70秒)

### 目的
说明公式的适用条件和特殊情况

### 元素
1. 三种特殊情况卡片
2. 动画演示

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 54.0s | 清理前面元素 | `FadeOut(slope_line, chord_AB, ellipse)` | 0.5s |
| 54.5s | 标题淡入 | `Write(special_title)` | 0.6s |
| 55.1s | 情况1卡片滑入 | `card_1.animate.shift(RIGHT*10)` | 0.8s |
| 55.9s | 情况1图示 | 绘制 y₀=0 情况 | 1.5s |
| 57.4s | 情况2卡片滑入 | `card_2.animate.shift(RIGHT*10)` | 0.8s |
| 58.2s | 情况2图示 | 绘制 x₀=0 情况 | 1.5s |
| 59.7s | 情况3卡片滑入 | `card_3.animate.shift(RIGHT*10)` | 0.8s |
| 60.5s | 情况3图示 | 绘制中点在椭圆上 | 1.5s |
| 62.0s | 汇总提示 | `FadeIn(summary_text)` | 0.8s |
| 62.8s | 等待理解 | `Wait(7.2)` | 7.2s |

### 数学内容
```python
# 标题
special_title = Text(
    "特殊情况",
    font="Noto Sans CJK SC",
    font_size=40,
    color=COLOR_HIGHLIGHT
).move_to(UP * 6.5)

# 情况1: y₀ = 0
card_1 = VGroup(
    Text("情况1: ", font="Noto Sans CJK SC", font_size=24, color=YELLOW),
    MathTex(r"y_0 = 0", font_size=24),
    Text(" → 弦垂直于x轴", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
).arrange(RIGHT, buff=0.2).move_to(UP * 5.0 + LEFT * 10)

# 情况2: x₀ = 0
card_2 = VGroup(
    Text("情况2: ", font="Noto Sans CJK SC", font_size=24, color=YELLOW),
    MathTex(r"x_0 = 0", font_size=24),
    Text(" → 弦平行于x轴", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
).arrange(RIGHT, buff=0.2).move_to(UP * 3.5 + LEFT * 10)

# 情况3: M在椭圆上
card_3 = VGroup(
    Text("情况3: M在椭圆上 → 切线斜率", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
).move_to(UP * 2.0 + LEFT * 10)

# 汇总
summary_text = Text(
    "公式适用于: M在椭圆内部, y₀≠0",
    font="Noto Sans CJK SC",
    font_size=24,
    color=COLOR_HIGHLIGHT
).move_to(DOWN * 5.5)
```

### 图示
每个情况配一个小椭圆图示，位于右侧

### 清理
- FadeOut: 所有卡片, 图示, summary_text
- 保留: special_title (变换为下一场景标题)

---

## Scene 8: 片尾总结 (70-90秒)

### 目的
总结要点，引导关注

### 元素
1. 核心公式回顾
2. 应用提示
3. 作者信息放大

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 70.0s | 标题变换 | `Transform(special_title, summary_title)` | 0.6s |
| 70.6s | 公式框回到中央 | 大号公式 | 1.0s |
| 71.6s | 三要点卡片 | 依次滑入 | 1.8s |
| 73.4s | 装饰动画 | 椭圆环绕 | 1.0s |
| 74.4s | 应用场景 | `FadeIn(application_text)` | 1.0s |
| 75.4s | 作者信息放大 | `author_info.animate.scale(2).move_to(UP*1.5)` | 0.8s |
| 76.2s | ID显示 | `FadeIn(author_id)` | 0.5s |
| 76.7s | 关注提示 | `FadeIn(follow_text, scale=1.1)` | 0.6s |
| 77.3s | 装饰旋转 | 小椭圆图标旋转 | 2.0s |
| 79.3s | 等待结束 | `Wait(10.7)` | 10.7s |

### 数学内容
```python
# 总结标题
summary_title = Text(
    "核心总结",
    font="Noto Sans CJK SC",
    font_size=40,
    color=GOLD
).move_to(UP * 6.5)

# 大号公式
big_formula = MathTex(
    r"k = -\frac{b^2 x_0}{a^2 y_0}",
    font_size=48,
    color=COLOR_SLOPE_LINE
).move_to(UP * 4.5)

# 三要点
point_1 = Text("✓ 点差法: 两式相减", font="Noto Sans CJK SC", font_size=24, color=GRAY_A).move_to(UP * 2.5)
point_2 = Text("✓ 利用中点坐标关系", font="Noto Sans CJK SC", font_size=24, color=GRAY_A).move_to(UP * 1.5)
point_3 = Text("✓ 适用于椭圆/双曲线/抛物线", font="Noto Sans CJK SC", font_size=24, color=GRAY_A).move_to(UP * 0.5)

# 应用场景
application_text = Text(
    "应用: 求弦方程、弦长、对称问题",
    font="Noto Sans CJK SC",
    font_size=22,
    color=COLOR_HIGHLIGHT
).move_to(DOWN * 1.0)

# 作者信息
author_name = Text(
    "上海初高中数学直通车",
    font="Noto Sans CJK SC",
    font_size=40,
    color=WHITE
).move_to(UP * 1.5)

author_id = Text(
    "@emptyandcalm",
    font="Noto Sans CJK SC",
    font_size=32,
    color=GRAY_B
).move_to(UP * 0.5)

follow_text = Text(
    "关注我, 掌握更多解题技巧!",
    font="Noto Sans CJK SC",
    font_size=30,
    color=COLOR_HIGHLIGHT
).move_to(DOWN * 0.5)

# 装饰椭圆
decorations = VGroup(*[
    Ellipse(width=0.6, height=0.4, color=COLOR_ELLIPSE, fill_opacity=0.5)
    .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
    for i in range(6)
])
```

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 贯穿全程，最后放大 |
| ellipse | Scene 1 | Scene 7 | 主椭圆 |
| chord_AB | Scene 1 | Scene 7 | 弦AB |
| dot_M | Scene 1 | Scene 6 | 中点M |
| dot_A, dot_B | Scene 2 | Scene 6 | 端点A, B |
| final_formula_box | Scene 5 | Scene 8 | 核心公式，移到角落 |
| slope_line | Scene 6 | Scene 7 | 斜率线 |

---

## 几何精确计算方案

### 椭圆参数化
```python
# 给定 a=4, b=2, 中点 M(x₀, y₀) = (1.5, 0.8)
# 斜率 k = -b²x₀/(a²y₀) = -4*1.5/(16*0.8) = -6/12.8 ≈ -0.46875

# 弦方程: y - y₀ = k(x - x₀)
# 联立椭圆: x²/16 + y²/4 = 1

# 解出 A, B 坐标 (需要数值求解)
```

### A, B 点计算
```python
def calculate_chord_endpoints(a, b, x0, y0):
    """
    计算以(x0, y0)为中点的弦的端点坐标
    
    返回: (A_coords, B_coords)
    """
    # 斜率
    k = -b**2 * x0 / (a**2 * y0)
    
    # 弦方程: y = k(x - x0) + y0
    # 代入椭圆: x²/a² + (k(x-x0)+y0)²/b² = 1
    
    # 整理成二次方程: Ax² + Bx + C = 0
    A_coeff = 1/a**2 + k**2/b**2
    B_coeff = 2*k*(y0 - k*x0)/b**2
    C_coeff = (y0 - k*x0)**2/b**2 - 1
    
    # 求解
    discriminant = B_coeff**2 - 4*A_coeff*C_coeff
    x1 = (-B_coeff + np.sqrt(discriminant)) / (2*A_coeff)
    x2 = (-B_coeff - np.sqrt(discriminant)) / (2*A_coeff)
    
    y1 = k * (x1 - x0) + y0
    y2 = k * (x2 - x0) + y0
    
    return np.array([x1, y1, 0]), np.array([x2, y2, 0])
```

---

## 动画节奏控制

### 快节奏部分 (0.3-0.5s)
- 简单淡入淡出
- 场景转换

### 中节奏部分 (0.8-1.2s)
- 公式书写
- 图形创建

### 慢节奏部分 (1.5-3.0s)
- 核心推导步骤
- 关键概念停留

### 总时长分配
| 场景 | 时长 | 占比 |
|------|------|------|
| Scene 1: 开场 | 5s | 6% |
| Scene 2: 问题设定 | 7s | 8% |
| Scene 3: 点差法介绍 | 8s | 9% |
| Scene 4: 代数推导 | 12s | 13% |
| Scene 5: 斜率公式 | 10s | 11% |
| Scene 6: 几何验证 | 12s | 13% |
| Scene 7: 特殊情况 | 16s | 18% |
| Scene 8: 总结 | 20s | 22% |
| **总计** | **90s** | **100%** |

---

## 验证清单

### 几何验证
- [ ] 中点M在椭圆内部
- [ ] 点A, B在椭圆上 (代入方程验证)
- [ ] M是AB中点 (坐标验证)
- [ ] 斜率一致 (公式计算 vs 两点坐标)

### 代码验证
- [ ] 所有坐标通过计算获得
- [ ] 中文使用 Text()
- [ ] LaTeX 使用 r"..." 原始字符串
- [ ] 度数使用 ^\circ
- [ ] 所有元素在边界内
- [ ] 时间总和符合预期

### 视觉验证
- [ ] 字体大小合适
- [ ] 颜色对比度足够
- [ ] 无元素重叠
- [ ] 动画流畅