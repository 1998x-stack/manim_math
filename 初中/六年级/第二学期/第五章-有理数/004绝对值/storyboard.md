# 绝对值 (Absolute Value) - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 初级 (六年级)
- 核心概念: 绝对值的定义、几何意义、非负性

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要元素
COLOR_SECONDARY = "#e74c3c"      # 红色 - 强调
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
COLOR_POSITIVE = "#2ecc71"       # 绿色 - 正数
COLOR_NEGATIVE = "#e67e22"       # 橙色 - 负数
COLOR_ZERO = "#95a5a6"           # 灰色 - 零
COLOR_DISTANCE = "#9b59b6"       # 紫色 - 距离
COLOR_AUXILIARY = GRAY_B         # 辅助线
```

## 几何预计算清单

### 数轴配置
| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 数轴范围 | x_range=[-5, 5, 1] | self.x_range | -5到5，步长1 |
| 数轴中心 | UP * 2 | self.numberline_center | 垂直偏移2单位 |
| 单位长度 | 0.8 | self.unit_length | 每个整数间距 |
| 原点位置 | numberline.n2p(0) | self.origin_point | 数轴上的0点 |

### 关键点位置（动态计算）
| 点 | 数值 | 计算方式 | 变量名 |
|----|------|---------|--------|
| A | 3 | numberline.n2p(3) | self.point_A |
| B | -3 | numberline.n2p(-3) | self.point_B |
| C | -4 | numberline.n2p(-4) | self.point_C |
| D | 1.5 | numberline.n2p(1.5) | self.point_D |

### 距离测量
| 距离 | 计算 | 存储 |
|------|------|------|
| |3| | np.linalg.norm(point_A - origin) | self.dist_3 |
| |-3| | np.linalg.norm(point_B - origin) | self.dist_neg3 |
| |-4| | np.linalg.norm(point_C - origin) | self.dist_neg4 |

---

## Scene 1: 开场钩子 (0-4秒)
**目的**: 吸引注意力，提出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字闪现)
3. 数轴预览

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子问题书写 | `Write(hook_question)` | 0.8s |
| 1.1s | 问题："3和-3，谁离原点更远？" | - | - |
| 2.1s | 数轴淡入 | `Create(numberline)` | 1.0s |
| 3.1s | 等待思考 | `self.wait(0.9)` | 0.9s |

### 清理
- FadeOut: hook_question
- 保留: numberline, author_info

---

## Scene 2: 引入绝对值概念 (4-10秒)
**目的**: 定义绝对值的几何意义

### 元素
1. 数轴（已存在）
2. 原点标记（红色大点）
3. 点A(3)、点B(-3)
4. 距离标注（双向箭头）

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 4.0s | 标记原点 | `FadeIn(origin_dot)` | 0.4s |
| 4.4s | 原点标签"0" | `Write(origin_label)` | 0.3s |
| 4.7s | 点A淡入 | `FadeIn(dot_A)` | 0.4s |
| 5.1s | 点B淡入 | `FadeIn(dot_B)` | 0.4s |
| 5.5s | A的距离箭头 | `Create(arrow_A)` | 0.6s |
| 6.1s | B的距离箭头 | `Create(arrow_B)` | 0.6s |
| 6.7s | 显示文字"距离相等！" | `FadeIn(equal_text)` | 0.5s |
| 7.2s | 定义文字滑入 | `FadeIn(definition)` | 0.8s |
| 8.0s | "绝对值：到原点的距离" | - | - |
| 9.0s | 等待理解 | `self.wait(1.0)` | 1.0s |

### 关键几何计算
```python
# 距离箭头（双向）
arrow_A = DoubleArrow(
    start=self.origin_point,
    end=self.point_A,
    color=COLOR_DISTANCE,
    buff=0
)

# 距离标注（Brace）
brace_A = Brace(
    Line(self.origin_point, self.point_A),
    direction=UP,
    buff=0.1
)
brace_label_A = MathTex("|3| = 3").next_to(brace_A, UP, buff=0.1)
```

### 清理
- FadeOut: equal_text
- 保留: numberline, dots, arrows, definition

---

## Scene 3: 绝对值符号与计算 (10-18秒)
**目的**: 介绍绝对值符号，展示计算规则

### 元素
1. 绝对值符号 |a|
2. 三个示例计算
3. 动态变换动画

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 10.0s | 清理前一场景多余元素 | `FadeOut(...)` | 0.4s |
| 10.4s | 标题"绝对值符号" | `Write(title)` | 0.6s |
| 11.0s | 公式|3|出现 | `Write(formula_1)` | 0.5s |
| 11.5s | 箭头变换 | `Transform(...)` | 0.6s |
| 12.1s | 结果 = 3 | `Write(result_1)` | 0.4s |
| 12.5s | 等待 | `self.wait(0.4)` | 0.4s |
| 12.9s | 公式|-3|出现 | `Write(formula_2)` | 0.5s |
| 13.4s | 箭头变换 | `Transform(...)` | 0.6s |
| 14.0s | 结果 = 3 | `Write(result_2)` | 0.4s |
| 14.4s | 等待 | `self.wait(0.4)` | 0.4s |
| 14.8s | 公式|0|出现 | `Write(formula_3)` | 0.5s |
| 15.3s | 结果 = 0 | `Write(result_3)` | 0.4s |
| 15.7s | 重点：绝对值≥0 | `FadeIn(highlight)` | 0.6s |
| 16.3s | 高亮非负性 | `Indicate(...)` | 0.7s |
| 17.0s | 等待理解 | `self.wait(1.0)` | 1.0s |

### 公式布局（垂直排列）
```python
formulas = VGroup(
    MathTex(r"|3| = 3").move_to(UP * 1),
    MathTex(r"|-3| = 3").move_to(ORIGIN),
    MathTex(r"|0| = 0").move_to(DOWN * 1)
).move_to(LEFT * 2)

# 颜色标记
formulas[0].set_color_by_tex("3", COLOR_POSITIVE)
formulas[1].set_color_by_tex("-3", COLOR_NEGATIVE)
formulas[2].set_color_by_tex("0", COLOR_ZERO)
```

### 清理
- FadeOut: title, formulas, highlight
- 保留: numberline

---

## Scene 4: 数学规则展示 (18-28秒)
**目的**: 分段函数定义，加深理解

### 元素
1. 分段函数公式
2. 数轴分区（正/负/零）
3. 颜色区分

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 18.0s | 标题"数学定义" | `Write(title)` | 0.6s |
| 18.6s | 分段函数出现 | `Write(piecewise_formula)` | 1.2s |
| 19.8s | 数轴正半轴高亮 | `Create(positive_region)` | 0.6s |
| 20.4s | 标注"a≥0时，|a|=a" | `FadeIn(label_pos)` | 0.6s |
| 21.0s | 示例：|5|=5 | `FadeIn(example_pos)` | 0.5s |
| 21.5s | 等待 | `self.wait(0.8)` | 0.8s |
| 22.3s | 数轴负半轴高亮 | `Create(negative_region)` | 0.6s |
| 22.9s | 标注"a<0时，|a|=-a" | `FadeIn(label_neg)` | 0.6s |
| 23.5s | 示例：|-5|=-(-5)=5 | `FadeIn(example_neg)` | 0.7s |
| 24.2s | 等待 | `self.wait(1.0)` | 1.0s |
| 25.2s | 零点高亮 | `Flash(origin_dot)` | 0.5s |
| 25.7s | 标注"|0|=0" | `FadeIn(label_zero)` | 0.4s |
| 26.1s | 等待理解 | `self.wait(1.9)` | 1.9s |

### 分段函数公式
```python
piecewise_formula = MathTex(
    r"|a| = \begin{cases} a, & a \geq 0 \\ -a, & a < 0 \end{cases}"
).scale(0.8).move_to(UP * 5)

# 颜色标记
piecewise_formula.set_color_by_tex("a \\geq 0", COLOR_POSITIVE)
piecewise_formula.set_color_by_tex("a < 0", COLOR_NEGATIVE)
```

### 数轴区域高亮
```python
# 正半轴区域（半透明矩形）
positive_region = Rectangle(
    width=4.0,  # 覆盖[0, 5]
    height=0.3,
    fill_color=COLOR_POSITIVE,
    fill_opacity=0.3,
    stroke_width=0
).move_to(numberline.n2p(2.5) + UP * 0.15)

# 负半轴区域
negative_region = Rectangle(
    width=4.0,  # 覆盖[-5, 0]
    height=0.3,
    fill_color=COLOR_NEGATIVE,
    fill_opacity=0.3,
    stroke_width=0
).move_to(numberline.n2p(-2.5) + UP * 0.15)
```

### 清理
- FadeOut: title, piecewise_formula, regions, labels, examples
- 保留: numberline

---

## Scene 5: 对称性展示 (28-36秒)
**目的**: 展示|-a|=|a|的对称性质

### 元素
1. 成对的点（a和-a）
2. 对称箭头
3. 动画：点的镜像移动

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 28.0s | 标题"对称性" | `Write(title)` | 0.6s |
| 28.6s | 公式|-a|=|a| | `Write(symmetry_formula)` | 0.7s |
| 29.3s | 点3淡入 | `FadeIn(dot_3)` | 0.4s |
| 29.7s | 点-3镜像出现 | `FadeIn(dot_neg3)` | 0.4s |
| 30.1s | 对称虚线 | `Create(symmetry_line)` | 0.5s |
| 30.6s | 距离箭头（同时） | `Create(arrow_3, arrow_neg3)` | 0.8s |
| 31.4s | 标注"距离相等" | `FadeIn(equal_dist)` | 0.5s |
| 31.9s | 等待 | `self.wait(0.6)` | 0.6s |
| 32.5s | 更换示例：4和-4 | `Transform(...)` | 1.0s |
| 33.5s | 等待 | `self.wait(0.5)` | 0.5s |
| 34.0s | 再换：2.5和-2.5 | `Transform(...)` | 1.0s |
| 35.0s | 等待理解 | `self.wait(1.0)` | 1.0s |

### 对称线（原点处垂直虚线）
```python
symmetry_line = DashedLine(
    start=self.origin_point + DOWN * 0.8,
    end=self.origin_point + UP * 0.8,
    color=COLOR_HIGHLIGHT,
    dash_length=0.1
)
```

### 动画：点的镜像变换
```python
# 使用always_redraw保持箭头更新
def create_symmetric_arrows(value):
    point_pos = numberline.n2p(value)
    point_neg = numberline.n2p(-value)
    
    arrow_pos = DoubleArrow(origin, point_pos, buff=0)
    arrow_neg = DoubleArrow(origin, point_neg, buff=0)
    
    return VGroup(arrow_pos, arrow_neg)
```

### 清理
- FadeOut: title, symmetry_formula, dots, arrows, symmetry_line
- 保留: numberline

---

## Scene 6: 实际应用示例 (36-48秒)
**目的**: 用温度、债务等实际例子加深理解

### 元素
1. 温度计图形（垂直）
2. 债务/存款示例
3. 数轴上的动态标注

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 36.0s | 标题"生活中的绝对值" | `Write(title)` | 0.7s |
| 36.7s | 示例1文字 | `FadeIn(example_1_text)` | 0.6s |
| 37.3s | "温度：-5°C" | - | - |
| 37.9s | 温度计出现 | `Create(thermometer)` | 0.8s |
| 38.7s | 标记-5°C | `FadeIn(temp_mark)` | 0.4s |
| 39.1s | 解释"距离0°是5度" | `FadeIn(explanation_1)` | 0.6s |
| 39.7s | 公式|-5|=5 | `Write(formula_temp)` | 0.5s |
| 40.2s | 等待 | `self.wait(1.0)` | 1.0s |
| 41.2s | 淡出温度示例 | `FadeOut(...)` | 0.5s |
| 41.7s | 示例2文字 | `FadeIn(example_2_text)` | 0.6s |
| 42.3s | "欠款300元" | - | - |
| 42.9s | 数轴标记-300 | `FadeIn(debt_mark)` | 0.5s |
| 43.4s | 解释"欠款数额是300" | `FadeIn(explanation_2)` | 0.6s |
| 44.0s | 公式|-300|=300 | `Write(formula_debt)` | 0.5s |
| 44.5s | 等待理解 | `self.wait(3.5)` | 3.5s |

### 温度计设计
```python
# 垂直温度计（简化）
thermometer_body = Rectangle(
    width=0.4,
    height=3.0,
    fill_color=GRAY,
    fill_opacity=0.3
).move_to(RIGHT * 3)

thermometer_tube = Rectangle(
    width=0.15,
    height=2.8,
    fill_color=BLUE_E,
    fill_opacity=0.7
).move_to(thermometer_body.get_center())

# 刻度线
scale_marks = VGroup(*[
    Line(LEFT * 0.2, RIGHT * 0.2)
    .move_to(thermometer_body.get_top() + DOWN * i * 0.5)
    for i in range(7)
])
```

### 清理
- FadeOut: title, examples, thermometer, formulas, explanations
- 保留: numberline

---

## Scene 7: 总结 + 片尾 (48-60秒)
**目的**: 回顾要点，引导关注

### 元素
1. 三条核心要点卡片
2. 公式汇总
3. 作者信息放大

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 48.0s | 标题"绝对值三要点" | `Write(title)` | 0.7s |
| 48.7s | 卡片1滑入 | `card_1.animate.shift(RIGHT)` | 0.5s |
| 49.2s | "定义：到原点的距离" | - | - |
| 49.7s | 卡片2滑入 | `card_2.animate.shift(RIGHT)` | 0.5s |
| 50.2s | "性质：|a|≥0（非负）" | - | - |
| 50.7s | 卡片3滑入 | `card_3.animate.shift(RIGHT)` | 0.5s |
| 51.2s | "对称：|-a|=|a|" | - | - |
| 51.7s | 等待 | `self.wait(1.0)` | 1.0s |
| 52.7s | 公式汇总出现 | `FadeIn(formula_summary)` | 0.8s |
| 53.5s | 等待阅读 | `self.wait(2.0)` | 2.0s |
| 55.5s | 淡出所有内容 | `FadeOut(...)` | 0.8s |
| 56.3s | 作者信息放大 | `Transform(author_info, ...)` | 0.7s |
| 57.0s | 关注提示 | `FadeIn(follow_text)` | 0.6s |
| 57.6s | "关注我，学更多数学技巧！" | - | - |
| 58.2s | 装饰动画（数字旋转） | `Rotate(decorations)` | 1.2s |
| 59.4s | 等待结束 | `self.wait(0.6)` | 0.6s |

### 要点卡片设计
```python
def create_summary_card(title, content, color, position):
    # 左侧色块
    color_bar = Rectangle(
        width=0.2,
        height=0.8,
        fill_color=color,
        fill_opacity=1,
        stroke_width=0
    )
    
    # 标题
    title_text = Text(title, font="Noto Sans CJK SC", font_size=24, color=WHITE)
    
    # 内容
    content_text = Text(content, font="Noto Sans CJK SC", font_size=18, color=GRAY_A)
    
    # 组合
    card = VGroup(color_bar, title_text, content_text).arrange(RIGHT, buff=0.3)
    card.move_to(position)
    card.shift(LEFT * 10)  # 初始在左侧外
    
    return card
```

### 公式汇总
```python
formula_summary = VGroup(
    MathTex(r"|a| = \text{到原点的距离}"),
    MathTex(r"|a| \geq 0"),
    MathTex(r"|a| = \begin{cases} a, & a \geq 0 \\ -a, & a < 0 \end{cases}"),
    MathTex(r"|-a| = |a|")
).arrange(DOWN, buff=0.4, aligned_edge=LEFT).scale(0.7).move_to(DOWN * 2)
```

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留，最后放大 |
| numberline | Scene 1 | Scene 7 | 主数轴，全程可见 |
| hook_question | Scene 1 | Scene 1 | 开场钩子 |
| origin_dot | Scene 2 | Scene 6 | 原点标记 |
| dot_A, dot_B | Scene 2 | Scene 3 | 示例点 |
| arrows | Scene 2 | Scene 3 | 距离箭头 |
| definition | Scene 2 | Scene 3 | 定义文字 |
| formulas (各种) | Scene 3-6 | 各场景内 | 临时公式 |
| piecewise_formula | Scene 4 | Scene 4 | 分段函数 |
| regions | Scene 4 | Scene 4 | 数轴区域高亮 |
| symmetry_elements | Scene 5 | Scene 5 | 对称性元素 |
| application_elements | Scene 6 | Scene 6 | 应用示例 |
| summary_cards | Scene 7 | Scene 7 | 总结卡片 |

---

## 技术约束检查清单

### 几何计算约束
- [x] 所有点位置通过 `numberline.n2p()` 精确计算
- [x] 距离使用 `np.linalg.norm()` 计算
- [x] 箭头端点基于数轴坐标，无臆想值
- [x] 对称点通过原点镜像计算：`-value`

### LaTeX约束
- [x] 中文使用 `Text()` 而非 `MathTex()`
- [x] 数学公式使用 `MathTex()` 和原始字符串 `r"..."`
- [x] 分段函数使用 `\begin{cases}...\end{cases}`
- [x] 绝对值符号使用 `|...|`，无特殊转义

### 边界约束
- [x] 数轴中心在 UP * 2，安全范围内
- [x] 所有文字元素在 y ∈ [-6, 7] 范围
- [x] 示例元素左右对称，避免溢出

### 动画节奏
- [x] 开场钩子 < 4秒
- [x] 每个概念停留 1-2秒理解时间
- [x] 关键公式出现后等待 0.8-1.0秒
- [x] 片尾关注提示 > 2秒

---

## 验证要点

### Scene 2-3 验证
- [ ] `np.linalg.norm(point_A - origin_point)` 应等于 3.0
- [ ] `np.linalg.norm(point_B - origin_point)` 应等于 3.0
- [ ] 箭头方向正确（从原点指向各点）

### Scene 4 验证
- [ ] 正半轴区域宽度覆盖 [0, 5]
- [ ] 负半轴区域宽度覆盖 [-5, 0]
- [ ] 区域中心精确对齐数轴

### Scene 5 验证
- [ ] 对称点坐标：`numberline.n2p(value)` 和 `numberline.n2p(-value)` 关于原点对称
- [ ] 距离相等：`dist_pos == dist_neg`

---

## 预期输出效果

### 视觉风格
- 简洁明快，色彩对比强烈
- 数轴清晰，标注规范
- 动画流畅，无卡顿

### 教学效果
- 几何意义清晰（距离）
- 代数规则明确（分段函数）
- 应用场景贴近生活

### 时长控制
- 总时长：60-75秒
- 快节奏但不仓促
- 关键点有充足停留