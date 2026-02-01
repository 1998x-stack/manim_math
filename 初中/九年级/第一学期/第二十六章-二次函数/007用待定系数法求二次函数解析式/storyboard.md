# 二次函数待定系数法 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等
- 目标受众: 九年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要曲线
COLOR_SECONDARY = "#e74c3c"      # 红色 - 重点标注
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮提示
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_GENERAL_FORM = "#2ecc71"   # 绿色 - 一般式
COLOR_VERTEX_FORM = "#9b59b6"    # 紫色 - 顶点式
COLOR_INTERCEPT_FORM = "#f39c12" # 橙色 - 交点式
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 坐标系 | Axes(x_range=[-5,5,1], y_range=[-3,8,1]) | self.axes |
| 示例抛物线1 | y = x² - 2x - 3 | self.parabola_1 |
| 顶点 | (1, -4) | self.vertex |
| x轴交点 | (-1, 0), (3, 0) | self.x_intercept_1, self.x_intercept_2 |
| 三个已知点 | (0, -3), (1, -4), (2, -3) | self.point_A, self.point_B, self.point_C |

---

## Scene 1: 开场钩子 (4-5秒)
**目的**: 吸引注意力，引出核心问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题文字 (大字)
3. 三个抛物线快闪

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_text)` 文字："三种方法，一个目标！" |
| 1.2s | 三个抛物线快闪 | `LaggedStart(*[Create(p) for p in parabolas], lag_ratio=0.3)` |
| 2.5s | 副标题淡入 | `FadeIn(subtitle)` 文字："如何求二次函数解析式？" |
| 3.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text, parabolas, subtitle
- 保留: author_info

---

## Scene 2: 建立坐标系 (3-4秒)
**目的**: 建立视觉基础

### 元素
1. 坐标系 (中心偏上)
2. 标题：二次函数的三种形式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 坐标系创建 | `Create(axes)` |
| 0.8s | 标题淡入 | `FadeIn(title)` 位置：UP*5.5 |
| 1.3s | 等待 | `Wait(0.5)` |

### 清理
- 保留: axes, author_info
- FadeOut: title

---

## Scene 3: 一般式 y=ax²+bx+c (12-15秒)
**目的**: 演示已知三点求解析式

### 元素
1. 标题："方法一：一般式"
2. 公式显示：y = ax² + bx + c
3. 三个已知点：(0, -3), (1, -4), (2, -3)
4. 三元一次方程组
5. 解得结果

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title)` "方法一：一般式" 位置：UP*5 |
| 0.5s | 公式出现 | `Write(formula)` y=ax²+bx+c 位置：UP*4 |
| 1.2s | 三个点依次标注 | `LaggedStart` 创建点和标签 |
| 2.5s | 说明文字 | `FadeIn(explain)` "已知三点，代入一般式" |
| 3.5s | 方程组展开 | `Write(equations)` 三个方程式 位置：DOWN*2 |
| 5.0s | 高亮第一个方程 | `Indicate(eq1)` |
| 5.5s | 高亮第二个方程 | `Indicate(eq2)` |
| 6.0s | 高亮第三个方程 | `Indicate(eq3)` |
| 6.5s | 求解动画 | `Transform` 方程组变为解 |
| 8.0s | 结果高亮 | `Flash` a=1, b=-2, c=-3 |
| 9.0s | 最终解析式 | `Write(result)` y=x²-2x-3 位置：DOWN*4 |
| 10.5s | 绘制抛物线 | `Create(parabola)` 穿过三点 |
| 12.0s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: title, formula, points, equations, result, explain
- 保留: axes, parabola (变淡，作为参考)

---

## Scene 4: 顶点式 y=a(x-h)²+k (12-15秒)
**目的**: 演示已知顶点和一点求解析式

### 元素
1. 标题："方法二：顶点式"
2. 公式显示：y = a(x-h)² + k
3. 顶点标注：(1, -4)
4. 另一点：(0, -3)
5. 代入求解过程

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清除前一场景元素 | `FadeOut` 一般式相关 |
| 0.5s | 标题淡入 | `Write(title)` "方法二：顶点式" 位置：UP*5 |
| 1.0s | 公式出现 | `Write(formula)` y=a(x-h)²+k 位置：UP*4 |
| 1.8s | 标注顶点 | `FadeIn(vertex_dot, vertex_label)` (1,-4) |
| 2.5s | 高亮顶点 | `Flash(vertex_dot)` |
| 3.0s | 说明文字 | `FadeIn(explain)` "已知顶点(h,k)和另一点" |
| 4.0s | 标注另一点 | `FadeIn(point_dot)` (0,-3) |
| 5.0s | 代入顶点坐标 | `Write(step1)` y=a(x-1)²-4 位置：DOWN*1.5 |
| 6.5s | 代入另一点 | `Write(step2)` -3=a(0-1)²-4 位置：DOWN*2.5 |
| 8.0s | 求解a | `Transform` -3=a-4 → a=1 |
| 9.0s | 结果高亮 | `Flash` a=1 |
| 9.5s | 最终解析式 | `Write(result)` y=(x-1)²-4 位置：DOWN*4 |
| 11.0s | 展开验证 | `TransformMatchingTex` y=x²-2x-3 |
| 12.0s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: title, formula, vertex elements, point, steps, result
- 保留: axes, parabola (变淡)

---

## Scene 5: 交点式 y=a(x-x₁)(x-x₂) (12-15秒)
**目的**: 演示已知x轴交点和一点求解析式

### 元素
1. 标题："方法三：交点式"
2. 公式显示：y = a(x-x₁)(x-x₂)
3. 两个x轴交点：(-1, 0), (3, 0)
4. 另一点：(0, -3)
5. 代入求解过程

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清除前一场景元素 | `FadeOut` 顶点式相关 |
| 0.5s | 标题淡入 | `Write(title)` "方法三：交点式" 位置：UP*5 |
| 1.0s | 公式出现 | `Write(formula)` y=a(x-x₁)(x-x₂) 位置：UP*4 |
| 1.8s | 标注两个交点 | `FadeIn(intercepts)` (-1,0) 和 (3,0) |
| 2.8s | 高亮交点 | `LaggedStart(*[Flash(dot) for dot in intercept_dots])` |
| 3.5s | 说明文字 | `FadeIn(explain)` "已知x轴交点和另一点" |
| 4.5s | 标注另一点 | `FadeIn(point_dot)` (0,-3) |
| 5.5s | 代入交点坐标 | `Write(step1)` y=a(x+1)(x-3) 位置：DOWN*1.5 |
| 7.0s | 代入另一点 | `Write(step2)` -3=a(0+1)(0-3) 位置：DOWN*2.5 |
| 8.5s | 求解a | `Transform` -3=a(-3) → a=1 |
| 9.5s | 结果高亮 | `Flash` a=1 |
| 10.0s | 最终解析式 | `Write(result)` y=(x+1)(x-3) 位置：DOWN*4 |
| 11.5s | 展开验证 | `TransformMatchingTex` y=x²-2x-3 |
| 12.5s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: title, formula, intercept elements, point, steps, result
- 保留: axes, parabola (变淡)

---

## Scene 6: 三种方法对比 (8-10秒)
**目的**: 总结三种方法的适用场景

### 元素
1. 三个并列卡片
2. 每个卡片包含：方法名、公式、适用条件

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清除抛物线 | `FadeOut(parabola)` |
| 0.5s | 标题出现 | `Write(title)` "三种方法对比" 位置：UP*6 |
| 1.0s | 第一张卡片滑入 | `card1.animate.shift(RIGHT*0)` 一般式 |
| 1.5s | 第二张卡片滑入 | `card2.animate.shift(RIGHT*0)` 顶点式 |
| 2.0s | 第三张卡片滑入 | `card3.animate.shift(RIGHT*0)` 交点式 |
| 3.0s | 高亮适用条件 | `Indicate` 每张卡片的条件部分 |
| 4.5s | 重点提示 | `FadeIn(hint)` "选对方法，事半功倍！" |
| 6.5s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: 所有卡片, title, hint
- 保留: axes, author_info

---

## Scene 7: 片尾关注 (5-6秒)
**目的**: 引导关注，强化品牌

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰元素（小抛物线图标）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清除坐标系 | `FadeOut(axes)` |
| 0.5s | 作者名放大 | `Transform(author_info, large_author)` |
| 1.0s | ID淡入 | `FadeIn(author_id)` @emptyandcalm |
| 1.5s | 关注提示 | `FadeIn(follow_text, scale=1.1)` "关注我，掌握更多解题技巧！" |
| 2.5s | 装饰抛物线 | `LaggedStart` 六个小抛物线环绕 |
| 3.5s | 旋转动画 | `Rotate(decorations, angle=PI)` |
| 5.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 全部元素

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| axes | Scene 2 | Scene 7 | 主坐标系 |
| parabola | Scene 3 | Scene 6 | 参考曲线 |
| general_form_elements | Scene 3 | Scene 3 | 一般式相关 |
| vertex_form_elements | Scene 4 | Scene 4 | 顶点式相关 |
| intercept_form_elements | Scene 5 | Scene 5 | 交点式相关 |
| comparison_cards | Scene 6 | Scene 6 | 对比卡片 |

---

## 关键技术要点

### 1. 坐标系配置
```python
self.axes = Axes(
    x_range=[-5, 5, 1],
    y_range=[-3, 8, 1],
    x_length=8,
    y_length=10,
    axis_config={"include_numbers": True, "font_size": 20}
).scale(0.6).move_to(UP * 0.5)
```

### 2. 抛物线精确绘制
```python
# 使用 lambda 函数确保精确
parabola = self.axes.plot(
    lambda x: x**2 - 2*x - 3,
    x_range=[-2, 4],
    color=COLOR_PRIMARY
)
```

### 3. 点的精确定位
```python
# 使用 axes.c2p (coords_to_point) 转换
point_A = self.axes.c2p(0, -3)  # 坐标 (0, -3)
dot_A = Dot(point_A, color=RED)
```

### 4. 公式对齐
```python
# 使用 VGroup 和 arrange
equations = VGroup(
    MathTex(r"-3 = a(0)^2 + b(0) + c"),
    MathTex(r"-4 = a(1)^2 + b(1) + c"),
    MathTex(r"-3 = a(2)^2 + b(2) + c")
).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
```

### 5. 卡片创建模板
```python
def create_method_card(self, title, formula, condition, color, position):
    # 背景框
    bg = RoundedRectangle(
        width=7, height=1.5, corner_radius=0.2,
        fill_color=color, fill_opacity=0.2,
        stroke_color=color, stroke_width=2
    )
    
    # 标题
    title_text = Text(title, font="Noto Sans CJK SC", font_size=24, color=WHITE)
    
    # 公式
    formula_tex = MathTex(formula, font_size=28, color=color)
    
    # 条件
    condition_text = Text(condition, font="Noto Sans CJK SC", font_size=18, color=GRAY_A)
    
    # 组合
    content = VGroup(title_text, formula_tex, condition_text).arrange(DOWN, buff=0.15)
    card = VGroup(bg, content)
    card.move_to(position)
    
    return card
```

---

## 验证检查点

### 运行前检查
- [ ] 所有坐标点使用 `axes.c2p()` 转换
- [ ] 中文文本使用 `Text(font="Noto Sans CJK SC")`
- [ ] 数学公式使用 `MathTex(r"...")`
- [ ] 度数符号使用 `^\circ`
- [ ] 元素位置在边界范围内 (x∈[-4,4], y∈[-7,7])

### 数学验证
- [ ] 抛物线 y=x²-2x-3 通过点 (0,-3), (1,-4), (2,-3)
- [ ] 顶点坐标 (1, -4) 正确
- [ ] x轴交点 (-1, 0), (3, 0) 正确
- [ ] 三种形式展开后一致

### 动画节奏
- [ ] 开场钩子足够吸引人（4-5秒）
- [ ] 每种方法讲解充分（12-15秒）
- [ ] 关键步骤有停留时间（1-2秒）
- [ ] 总时长控制在60-75秒

---

## 预期效果

1. **开场**: 快节奏，吸引眼球
2. **主体**: 清晰展示三种方法，步骤分明
3. **对比**: 帮助学生理解适用场景
4. **结尾**: 强化品牌，引导关注

学生观看后应能：
- 识别三种解析式形式
- 根据已知条件选择合适方法
- 理解待定系数法的基本思路