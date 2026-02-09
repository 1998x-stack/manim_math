# 函数的概念 - 动画分镜脚本

## 元信息
- **目标时长:** 70-80秒
- **场景数量:** 8个
- **难度等级:** 高一
- **关键概念:** 函数定义、定义域、值域、对应法则、函数相等

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 主要概念（蓝色）
COLOR_SECONDARY = "#e74c3c"      # 次要元素（红色）
COLOR_HIGHLIGHT = YELLOW         # 高亮强调
COLOR_AUXILIARY = GRAY_B         # 辅助线
COLOR_DOMAIN = "#2ecc71"         # 定义域（绿色）
COLOR_RANGE = "#f39c12"          # 值域（橙色）
BACKGROUND = "#1a1a2e"           # 深色背景
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 | 验证 |
|------|---------|---------|------|
| 集合A圆心 | [-2.5, 2, 0] | self.set_A_center | 位置在边界内 |
| 集合B圆心 | [2.5, 2, 0] | self.set_B_center | 位置在边界内 |
| 箭头起点 | set_A内元素位置 | self.arrow_starts | 在椭圆内 |
| 箭头终点 | set_B内元素位置 | self.arrow_ends | 在椭圆内 |
| 坐标系原点 | [0, 0, 0] | - | 中心位置 |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 引起兴趣，抛出问题

### 元素
1. 作者标识（顶部）
2. 钩子问题："什么是函数？"
3. 神秘的数学符号 f(x)

### 动画序列
| 时间 | 动作 | 代码参考 | 清理 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 保留 |
| 0.3s | 钩子问题书写 | `Write(hook_question, run_time=0.8)` | 3.5s移除 |
| 1.1s | f(x)符号出现 | `FadeIn(fx_symbol, scale=1.2)` | 3.5s移除 |
| 2.0s | 符号闪烁 | `Flash(fx_symbol, color=YELLOW)` | - |
| 3.0s | 等待 | `Wait(1.0)` | - |

### 布局
```
┌─────────────────────────┐ y=+7
│  上海初高中数学直通车     │
├─────────────────────────┤ y=+6
│                         │
│  什么是函数？            │ y=+5
│                         │
│      f(x) = ?           │ y=+2
│                         │
└─────────────────────────┘
```

### 清理
- FadeOut: hook_question, fx_symbol
- 保留: author_info

---

## Scene 2: 函数的定义 - 对应关系 (10-12秒)
**目的**: 展示函数是集合间的对应关系

### 元素
1. 标题："函数 = 对应关系"
2. 集合A（椭圆，包含x₁, x₂, x₃）
3. 集合B（椭圆，包含y₁, y₂, y₃）
4. 箭头表示对应关系
5. 定义文字

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 3.5s | 标题出现 | `Write(title, run_time=0.6)` | 中文用Text() |
| 4.1s | 集合A创建 | `Create(ellipse_A, run_time=0.8)` | 椭圆 |
| 4.4s | A中元素出现 | `FadeIn(dots_A, lag_ratio=0.2)` | x₁, x₂, x₃ |
| 5.2s | 集合B创建 | `Create(ellipse_B, run_time=0.8)` | 椭圆 |
| 5.5s | B中元素出现 | `FadeIn(dots_B, lag_ratio=0.2)` | y₁, y₂, y₃ |
| 6.5s | 箭头依次出现 | `Create(arrows, lag_ratio=0.3)` | 一一对应 |
| 8.0s | 定义文字 | `Write(definition, run_time=1.5)` | 底部说明 |
| 10.0s | 关键公式 | `Write(formula_fx, run_time=0.8)` | y = f(x) |
| 11.5s | 理解停顿 | `Wait(2.0)` | **关键停顿** |

### 几何计算
```python
# 集合A椭圆
self.set_A_center = np.array([-2.5, 2, 0])
self.ellipse_A = Ellipse(width=1.8, height=3.0, color=COLOR_PRIMARY)
self.ellipse_A.move_to(self.set_A_center)

# 集合A中的点位置（均匀分布）
self.points_A = [
    self.set_A_center + np.array([0, 0.8, 0]),   # x₁
    self.set_A_center + np.array([0, 0, 0]),     # x₂
    self.set_A_center + np.array([0, -0.8, 0])   # x₃
]

# 集合B同理
self.set_B_center = np.array([2.5, 2, 0])
self.points_B = [
    self.set_B_center + np.array([0, 0.8, 0]),   # y₁
    self.set_B_center + np.array([0, 0, 0]),     # y₂
    self.set_B_center + np.array([0, -0.8, 0])   # y₃
]

# 验证点在椭圆内
# (x-cx)²/a² + (y-cy)²/b² <= 1
```

### 清理
- FadeOut: title, definition
- 保留: ellipse_A, ellipse_B, dots, arrows（淡化透明度）

---

## Scene 3: 定义域和值域 (8-10秒)
**目的**: 解释定义域和值域的概念

### 元素
1. 标题："定义域 & 值域"
2. 定义域高亮（集合A）
3. 值域高亮（集合B中被映射到的部分）
4. 公式和说明

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 13.5s | 标题出现 | `Write(title, run_time=0.6)` | |
| 14.1s | 集合A高亮 | `ellipse_A.animate.set_color(COLOR_DOMAIN)` | 定义域 |
| 14.6s | "定义域"标签 | `Write(domain_label)` | 集合A旁 |
| 15.2s | 定义域说明 | `Write(domain_explain)` | 底部文字 |
| 16.5s | 集合B高亮 | `ellipse_B.animate.set_color(COLOR_RANGE)` | 值域 |
| 17.0s | "值域"标签 | `Write(range_label)` | 集合B旁 |
| 17.6s | 值域说明 | `Write(range_explain)` | 底部文字 |
| 19.0s | 公式出现 | `Write(domain_formula)` | x ∈ A |
| 20.0s | 理解停顿 | `Wait(2.5)` | **关键停顿** |

### 特殊效果
```python
# 定义域高亮动画
self.play(
    ellipse_A.animate.set_color(COLOR_DOMAIN).set_stroke(width=5),
    *[dot.animate.set_color(COLOR_DOMAIN) for dot in dots_A],
    run_time=0.8
)

# 值域高亮动画
self.play(
    ellipse_B.animate.set_color(COLOR_RANGE).set_stroke(width=5),
    *[dot.animate.set_color(COLOR_RANGE) for dot in dots_B],
    run_time=0.8
)
```

### 清理
- FadeOut: title, domain_explain, range_explain
- 保留: ellipse_A, ellipse_B（恢复原色）

---

## Scene 4: 函数相等的条件 (6-8秒)
**目的**: 说明两个函数相等需要定义域和对应法则都相同

### 元素
1. 标题："函数相等的条件"
2. 两组对应关系对比
3. 条件列表

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 22.5s | 清理上一场景 | `FadeOut(previous_objects)` | |
| 23.0s | 标题出现 | `Write(title)` | |
| 23.8s | 条件1出现 | `Write(condition_1)` | "定义域相同" |
| 24.8s | 条件2出现 | `Write(condition_2)` | "对应法则相同" |
| 25.8s | 反例说明 | `Write(counter_example)` | f(x₁)=f(x₂) ≠ x₁=x₂ |
| 27.5s | 理解停顿 | `Wait(2.0)` | |

### 布局
```
┌─────────────────────────┐
│  函数相等的条件           │ y=+5
├─────────────────────────┤
│  ① 定义域相同            │ y=+3
│  ② 对应法则相同          │ y=+2
├─────────────────────────┤
│  注意: f(x₁) = f(x₂)     │ y=-2
│        不要求 x₁ = x₂    │ y=-3
└─────────────────────────┘
```

### 清理
- FadeOut: 全部内容
- 准备进入函数图像场景

---

## Scene 5: 函数图像示例 (12-15秒)
**目的**: 通过y=x²展示函数的图像表示

### 元素
1. 坐标系（Axes）
2. 函数曲线 y=x²
3. 定义域和值域的标注
4. 公式 y = x²

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 29.5s | 标题出现 | `Write(title)` | "函数的图像" |
| 30.2s | 坐标系创建 | `Create(axes, run_time=1.2)` | |
| 31.4s | 函数公式 | `Write(formula)` | y = x² |
| 32.4s | 函数曲线绘制 | `Create(graph, run_time=2.0)` | 平滑绘制 |
| 34.4s | 定义域标注 | `Create(domain_line)` | x轴区间 |
| 35.2s | 定义域文字 | `Write(domain_text)` | "定义域: ℝ" |
| 36.0s | 值域标注 | `Create(range_line)` | y轴区间 |
| 36.8s | 值域文字 | `Write(range_text)` | "值域: [0, +∞)" |
| 38.0s | 追踪点动画 | `dot.animate.move_along(graph)` | 动态演示 |
| 40.5s | 理解停顿 | `Wait(2.5)` | **关键停顿** |

### 几何计算
```python
# 坐标系设置
self.axes = Axes(
    x_range=[-3, 3, 1],
    y_range=[0, 5, 1],
    x_length=6,
    y_length=4,
    axis_config={"include_numbers": True, "font_size": 20}
).scale(0.7).shift(UP * 0.5)

# 函数曲线
self.graph = self.axes.plot(
    lambda x: x**2,
    x_range=[-2.5, 2.5],
    color=COLOR_PRIMARY
)

# 定义域标注（x轴双向箭头）
self.domain_arrow = DoubleArrow(
    start=self.axes.c2p(-2.5, 0),
    end=self.axes.c2p(2.5, 0),
    color=COLOR_DOMAIN,
    buff=0
)

# 值域标注（y轴单向箭头）
self.range_arrow = Arrow(
    start=self.axes.c2p(0, 0),
    end=self.axes.c2p(0, 4.5),
    color=COLOR_RANGE,
    buff=0
)
```

### 动态演示
```python
# 追踪点沿曲线移动
t = ValueTracker(-2)
dot = always_redraw(
    lambda: Dot(
        self.axes.c2p(t.get_value(), t.get_value()**2),
        color=YELLOW,
        radius=0.08
    )
)

self.add(dot)
self.play(t.animate.set_value(2), run_time=3)
```

### 清理
- 保留: axes, graph（淡化）
- FadeOut: 其他标注

---

## Scene 6: 定义域的求法 (10-12秒)
**目的**: 展示如何求函数的定义域

### 元素
1. 标题："如何求定义域？"
2. 三种情况列表
3. 示例函数

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 43.0s | 清理上一场景 | `FadeOut(previous)` | |
| 43.5s | 标题出现 | `Write(title)` | |
| 44.2s | 规则1 | `Write(rule_1)` | "分母 ≠ 0" |
| 45.2s | 示例1 | `Write(example_1)` | f(x) = 1/x |
| 46.2s | 规则2 | `Write(rule_2)` | "偶次根号下 ≥ 0" |
| 47.2s | 示例2 | `Write(example_2)` | f(x) = √x |
| 48.2s | 规则3 | `Write(rule_3)` | "对数真数 > 0" |
| 49.2s | 示例3 | `Write(example_3)` | f(x) = ln(x) |
| 50.5s | 理解停顿 | `Wait(2.5)` | **关键停顿** |

### 布局
```
┌─────────────────────────┐
│  如何求定义域？          │ y=+5.5
├─────────────────────────┤
│  ① 分母 ≠ 0              │ y=+3.5
│     例: f(x) = 1/x       │
│     定义域: x ≠ 0        │
├─────────────────────────┤
│  ② 偶次根号下 ≥ 0        │ y=+1
│     例: f(x) = √x        │
│     定义域: x ≥ 0        │
├─────────────────────────┤
│  ③ 对数真数 > 0          │ y=-1.5
│     例: f(x) = ln(x)     │
│     定义域: x > 0        │
└─────────────────────────┘
```

### 清理
- FadeOut: 全部内容

---

## Scene 7: 总结 (5-6秒)
**目的**: 回顾关键概念

### 元素
1. 总结标题
2. 关键点卡片
3. 核心公式

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 53.0s | 标题出现 | `Write(summary_title)` | "函数三要素" |
| 53.8s | 卡片1滑入 | `card_1.animate.shift(RIGHT*0)` | "定义域" |
| 54.4s | 卡片2滑入 | `card_2.animate.shift(RIGHT*0)` | "值域" |
| 55.0s | 卡片3滑入 | `card_3.animate.shift(RIGHT*0)` | "对应法则" |
| 55.8s | 核心公式 | `Write(core_formula)` | y = f(x), x∈A |
| 57.0s | 理解停顿 | `Wait(2.0)` | |

### 卡片设计
```python
def create_summary_card(title, content, color, position):
    icon = Circle(radius=0.2, fill_color=color, fill_opacity=1)
    title_text = Text(title, font="Noto Sans CJK SC", font_size=24)
    content_text = Text(content, font="Noto Sans CJK SC", font_size=18)
    
    card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.3)
    card.move_to(position)
    card.shift(LEFT * 10)  # 初始位置在左侧外
    return card
```

### 清理
- FadeOut: 全部内容

---

## Scene 8: 片尾 (3-4秒)
**目的**: 引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 59.0s | 作者名放大 | `Transform(author_info, large_author)` | |
| 59.8s | ID显示 | `FadeIn(author_id)` | @emptyandcalm |
| 60.4s | 关注文字 | `FadeIn(cta_text, scale=1.1)` | "关注我..." |
| 61.2s | 装饰元素 | `FadeIn(decorations)` | 小图标 |
| 62.2s | 旋转动画 | `Rotate(decorations, PI)` | |
| 64.0s | 等待 | `Wait(1.0)` | |
| 65.0s | 全部淡出 | `FadeOut(all)` | |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 贯穿全程 |
| hook_question | Scene 1 | Scene 1 | 仅开场 |
| fx_symbol | Scene 1 | Scene 1 | 仅开场 |
| ellipse_A | Scene 2 | Scene 4 | 对应关系演示 |
| ellipse_B | Scene 2 | Scene 4 | 对应关系演示 |
| arrows | Scene 2 | Scene 4 | 映射箭头 |
| axes | Scene 5 | Scene 6 | 坐标系 |
| graph | Scene 5 | Scene 6 | 函数曲线 |

---

## 时间预算
| 类别 | 时间 | 百分比 |
|------|------|--------|
| 开场 | 3-4s | 5% |
| 对应关系 | 10-12s | 16% |
| 定义域值域 | 8-10s | 13% |
| 函数相等 | 6-8s | 10% |
| 函数图像 | 12-15s | 20% |
| 定义域求法 | 10-12s | 16% |
| 总结 | 5-6s | 8% |
| 片尾 | 3-4s | 5% |
| **总计** | **70-80s** | **100%** |

---

## 实现前检查清单
- [ ] 所有几何计算已规划
- [ ] 验证条件已指定
- [ ] 场景转换已计划
- [ ] 元素生命周期已追踪
- [ ] 时间在指导范围内
- [ ] 中文使用Text()，公式使用MathTex()
- [ ] 颜色定义一致
- [ ] 清理策略明确

---

## 特殊注意事项
- 集合用椭圆表示，确保点在椭圆内部
- 箭头方向准确，从A指向B
- 函数曲线平滑，使用足够的采样点
- 定义域和值域的标注清晰
- 所有数学公式使用MathTex()
- 中文说明使用Text()
- 关键概念停顿2-3秒
- 坐标系比例适中，数字清晰可读

---

## 调试策略
- 使用 `manim -pql` 快速预览
- 验证椭圆和点的位置关系
- 检查箭头端点是否精确
- 测试函数曲线的平滑度
- 确认所有元素在边界内
- 检查文字是否重叠