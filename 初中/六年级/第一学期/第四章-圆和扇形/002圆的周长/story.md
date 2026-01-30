# 圆的周长 - 动画分镜脚本

## 元信息
- 目标时长: 70-85 秒
- 场景数量: 8 个
- 难度等级: 初级 (六年级)
- 格式: TikTok 竖屏 (1080×1920)

## 颜色配置
```python
COLOR_CIRCLE = "#3498db"         # 蓝色 - 圆
COLOR_CIRCUMFERENCE = "#e74c3c"  # 红色 - 周长
COLOR_DIAMETER = "#f39c12"       # 橙色 - 直径
COLOR_RADIUS = "#2ecc71"         # 绿色 - 半径
COLOR_PI = "#9b59b6"             # 紫色 - π
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆心O | 固定点 | self.O |
| 半径r | 固定长度 | self.radius |
| 直径d | 2r | self.diameter |
| 周长C | 2πr | self.circumference |
| 展开线长度 | 2πr | self.unrolled_length |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出周长概念

### 元素
1. 作者标识 (顶部)
2. 钩子问题："圆一周有多长？"
3. 圆形出现并旋转

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info)` | 0.3s |
| 0.3s | 钩子问题书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 圆形创建 | `Create(circle)` | 1.0s |
| 2.1s | 圆周高亮闪烁 | `Flash` + 颜色变化 | 0.8s |
| 2.9s | 等待 | `Wait(0.8)` | 0.8s |

### 清理
- FadeOut: hook_text
- 保留: circle, author_info

---

## Scene 2: 周长定义 (8-10秒)
**目的**: 介绍周长的概念

### 元素
1. 标题："什么是周长？"
2. 定义文字
3. 动点沿圆运动演示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 0.5s | 定义文字出现 | `Write(definition)` | 1.5s |
| 2.0s | 小点沿圆运动 | `MoveAlongPath` | 2.5s |
| 4.5s | 圆周加粗高亮 | `circle.set_stroke(width=6)` | 0.6s |
| 5.1s | 公式初步介绍 | `Write(formula_hint)` | 1.0s |
| 6.1s | 等待理解 | `Wait(2.0)` | 2.0s |

### 清理
- FadeOut: title, definition, formula_hint, moving_dot
- 保留: circle

---

## Scene 3: 神奇的π (10-12秒)
**目的**: 介绍π的概念

### 元素
1. 标题："神奇的常数 π"
2. 圆周与直径的比值演示
3. π的近似值

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题出现 | `FadeIn(title)` | 0.5s |
| 0.5s | 直径线段出现 | `Create(diameter)` | 0.6s |
| 1.1s | 标注直径d | `FadeIn(label_d)` | 0.4s |
| 1.5s | 比值公式 | `Write(ratio_formula)` | 1.0s |
| 2.5s | π符号闪亮登场 | `Flash(pi_symbol)` | 0.8s |
| 3.3s | π的值 | `Write(pi_value)` | 1.0s |
| 4.3s | 说明文字 | `Write(explanation)` | 1.5s |
| 5.8s | 等待 | `Wait(2.0)` | 2.0s |

### 清理
- FadeOut: title, explanation, diameter, label_d
- 保留: circle, pi_symbol (缩小移到角落)

---

## Scene 4: 圆周长公式 C=πd (8-10秒)
**目的**: 推导并展示第一个公式

### 元素
1. 标题："周长公式"
2. 公式 C = πd
3. 公式推导动画

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题出现 | `FadeIn(title)` | 0.4s |
| 0.4s | 直径重新出现 | `Create(diameter)` | 0.6s |
| 1.0s | 公式 C = πd 书写 | `Write(formula_1)` | 1.0s |
| 2.0s | 公式分解说明 | 标注各部分 | 1.5s |
| 3.5s | 数值示例 | 显示具体计算 | 1.5s |
| 5.0s | 等待 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: title, diameter, 数值示例
- 保留: circle, formula_1

---

## Scene 5: 第二个公式 C=2πr (7-8秒)
**目的**: 展示第二个公式及其与第一个的关系

### 元素
1. 标题："另一种表达"
2. 公式 C = 2πr
3. 公式变换演示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题出现 | `FadeIn(title)` | 0.4s |
| 0.4s | 半径线段出现 | `Create(radius)` | 0.6s |
| 1.0s | 标注 d=2r | `Write(relation)` | 0.8s |
| 1.8s | 公式变换 | `TransformMatchingTex` | 1.0s |
| 2.8s | 公式 C=2πr | `Write(formula_2)` | 1.0s |
| 3.8s | 说明文字 | `Write(explanation)` | 1.0s |
| 4.8s | 等待 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: title, explanation, radius
- 保留: circle, formula_2

---

## Scene 6: 视觉验证 - "展开"圆 (12-15秒)
**目的**: 通过视觉演示验证公式

### 元素
1. 标题："验证：展开圆周"
2. 圆周"展开"成直线
3. 直线与直径对比

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题出现 | `FadeIn(title)` | 0.5s |
| 0.5s | 圆周高亮 | `set_color(HIGHLIGHT)` | 0.4s |
| 0.9s | 标记起点 | `FadeIn(start_dot)` | 0.3s |
| 1.2s | 圆开始"展开" | 动画变换 | 3.0s |
| 4.2s | 展开的线段出现 | `Create(unrolled_line)` | 1.0s |
| 5.2s | 直径线段对比 | `Create(diameter_copies)` | 1.5s |
| 6.7s | 标注π倍关系 | 箭头+文字 | 1.5s |
| 8.2s | 强调公式 | `formula.animate.scale(1.2)` | 0.6s |
| 8.8s | 等待 | `Wait(2.0)` | 2.0s |

### 清理
- FadeOut: title, unrolled_line, diameter_copies, 标注
- 保留: circle

---

## Scene 7: 实际应用示例 (10-12秒)
**目的**: 展示周长计算的实际应用

### 元素
1. 标题："实际应用"
2. 示例问题
3. 逐步计算过程

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题出现 | `FadeIn(title)` | 0.4s |
| 0.4s | 问题文字 | `Write(problem)` | 1.2s |
| 1.6s | 圆的参数 | 显示半径r=3 | 0.8s |
| 2.4s | 步骤1：写公式 | `Write(step1)` | 0.8s |
| 3.2s | 步骤2：代入数值 | `Write(step2)` | 1.0s |
| 4.2s | 步骤3：计算结果 | `Write(step3)` | 1.0s |
| 5.2s | 答案高亮 | `answer.set_color(HIGHLIGHT)` | 0.6s |
| 5.8s | 等待 | `Wait(2.0)` | 2.0s |

### 清理
- FadeOut: title, problem, steps
- 保留: circle

---

## Scene 8: 总结回顾 (8-10秒)
**目的**: 快速回顾核心知识点

### 元素
1. 标题："周长知识要点"
2. 知识卡片
3. 公式汇总

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题出现 | `FadeIn(title)` | 0.5s |
| 0.5s | 圆缩小到上方 | `circle.animate.scale(0.6).shift(UP*3)` | 0.8s |
| 1.3s | 知识卡片1 | 周长定义 | 0.6s |
| 1.9s | 知识卡片2 | π的意义 | 0.6s |
| 2.5s | 知识卡片3 | 公式 C=πd | 0.6s |
| 3.1s | 知识卡片4 | 公式 C=2πr | 0.6s |
| 3.7s | 重点提示 | `FadeIn(highlight_text)` | 0.6s |
| 4.3s | 等待 | `Wait(2.5)` | 2.5s |

### 清理
- FadeOut: 所有元素
- 准备结尾

---

## Scene 9: 片尾关注 (4-5秒)
**目的**: 引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者名放大 | `Transform(author_info)` | 0.8s |
| 0.8s | ID出现 | `FadeIn(author_id)` | 0.4s |
| 1.2s | 关注文字 | `FadeIn(follow_text)` | 0.6s |
| 1.8s | 圆形装饰旋转 | `Rotate(circles)` | 1.5s |
| 3.3s | 全部淡出 | `FadeOut(all)` | 1.0s |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 9 | 贯穿全片 |
| main_circle | Scene 1 | Scene 8 | 主圆形 |
| center_dot | Scene 2 | Scene 8 | 圆心点 |
| moving_dot | Scene 2 | Scene 2 | 运动的点 |
| pi_symbol | Scene 3 | Scene 8 | π符号 |
| diameter | Scene 3, 4, 6 | 各场景内 | 直径线段 |
| radius | Scene 5 | Scene 5 | 半径线段 |
| formula_1 | Scene 4 | Scene 5 | C=πd |
| formula_2 | Scene 5 | Scene 8 | C=2πr |
| unrolled_line | Scene 6 | Scene 6 | 展开的线段 |
| example_calc | Scene 7 | Scene 7 | 计算示例 |
| summary_cards | Scene 8 | Scene 8 | 总结卡片 |

---

## 技术要点

### 1. 圆周"展开"动画 (Scene 6 核心)
```python
# 使用 TracedPath 记录圆周轨迹
traced_path = TracedPath(dot.get_center, stroke_color=COLOR_CIRCUMFERENCE)

# 或使用参数方程逐渐"展开"
t = ValueTracker(0)
unrolling_line = always_redraw(lambda: 
    Line(start_point, start_point + RIGHT * self.radius * t.get_value())
)
```

### 2. π的精确表示
```python
# 使用 MathTex 显示π符号
pi_symbol = MathTex(r"\pi", font_size=48, color=COLOR_PI)

# π的近似值
pi_value = MathTex(r"\pi \approx 3.14159...", font_size=32)
```

### 3. 公式变换动画
```python
# 从 C=πd 变换到 C=2πr
formula_1 = MathTex(r"C = \pi {{ d }}")
formula_2 = MathTex(r"C = \pi \cdot {{ 2r }}")
formula_3 = MathTex(r"C = 2\pi r")

self.play(TransformMatchingTex(formula_1, formula_2))
self.play(TransformMatchingTex(formula_2, formula_3))
```

### 4. 数值计算示例
```python
# 使用 DecimalNumber 显示计算过程
radius_value = DecimalNumber(3, num_decimal_places=0)
result = DecimalNumber(2 * PI * 3, num_decimal_places=2)

# 动画更新数值
self.play(result.animate.set_value(18.85))
```

---

## 预期效果
- 清晰展示周长的概念和意义
- 直观演示π的来源
- 视觉化验证公式的正确性
- 提供实际计算示例
- 符合六年级学生认知水平
- TikTok 竖屏格式，节奏紧凑

## 难点处理
1. **π的理解**: 通过比值演示，避免抽象定义
2. **展开动画**: 使用渐进式动画，不要太快
3. **公式推导**: 分步骤，每步都有视觉对应
4. **数值计算**: 保留π的符号形式，同时给出近似值