# 百分比应用 - 动画分镜脚本

## 元信息
- 目标时长: 70-80 秒
- 场景数量: 5 个
- 难度等级: 小学/初中基础
- 目标观众: 六年级学生

## 颜色配置
```python
COLOR_DISCOUNT = "#e74c3c"      # 红色 - 折扣
COLOR_INTEREST = "#3498db"      # 蓝色 - 利率
COLOR_CONCENTRATION = "#2ecc71" # 绿色 - 浓度
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
COLOR_FORMULA = "#f39c12"       # 橙色 - 公式
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
COLOR_BACKGROUND = "#1a1a2e"    # 深蓝背景
```

## 核心概念
- 百分比在生活中的实际应用
- 折扣：打几折 = 原价 × 折扣率
- 利率：利息 = 本金 × 利率 × 时间
- 浓度：浓度 = 溶质 / 溶液 × 100%
- 使用实际生活场景帮助理解

## 视觉元素设计
- 折扣场景：使用价格标签、打折图标
- 利率场景：使用钱袋、银行图标、时间轴
- 浓度场景：使用烧杯、溶液动画

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力，引出百分比应用主题

### 元素
1. 作者标识 (顶部)
2. 钩子问题: "百分比在生活中有哪些应用？"
3. 四个应用图标：折扣、利率、浓度、税率

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=1.0)` |
| 1.3s | 四个图标弹出 | `FadeIn(icons, scale=0.5, lag_ratio=0.2)` |
| 2.5s | 等待 | `Wait(0.8)` |

### 清理
- FadeOut: hook_text, icons
- 保留: author_info

---

## Scene 2: 应用概览 (5-10秒)
**目的**: 展示三个主要应用场景

### 元素
1. 标题: "生活中的百分比"
2. 三个应用卡片
   - 折扣：购物打折
   - 利率：银行存款
   - 浓度：溶液配置

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题写入 | `Write(title)` |
| 0.8s | 卡片1滑入 | `card1.animate.shift(LEFT*0)` |
| 1.2s | 卡片2滑入 | `card2.animate.shift(LEFT*0)` |
| 1.6s | 卡片3滑入 | `card3.animate.shift(LEFT*0)` |
| 2.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, cards

---

## Scene 3: 折扣应用 (10-28秒)
**目的**: 演示折扣计算：折扣价 = 原价 × 折扣率

### 核心例子
"一件外套原价500元，打8折，实际多少钱？"

### 元素
1. 问题文字
2. 价格标签（原价500元）
3. 折扣标签（8折）
4. 折扣可视化（矩形条形图）
5. 公式：500 × 80%
6. 答案：400元

### 几何计算
```python
# 原价矩形
self.price_rect = Rectangle(width=6, height=0.8, color=COLOR_DISCOUNT)
self.price_rect.move_to(UP * 2.5)

# 折扣部分 (80% = 0.8)
self.discount_rect = Rectangle(width=6*0.8, height=0.8, 
                                color=COLOR_FORMULA, fill_opacity=0.5)
self.discount_rect.align_to(self.price_rect, LEFT)
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.8s | 问题显示 | `FadeIn(question)` |
| 1.5s | 原价标签 | `FadeIn(price_tag)` |
| 2.5s | 原价矩形 | `Create(price_rect)` |
| 3.5s | 折扣标签 | `FadeIn(discount_tag)` |
| 4.5s | 折扣部分高亮 | `Create(discount_rect)` |
| 5.5s | 公式展示 | `Write(formula)` |
| 6.5s | 计算过程 | `Write(calculation)` |
| 7.5s | 答案闪现 | `FadeIn(answer), Flash(answer)` |
| 9.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: 所有元素

---

## Scene 4: 利率应用 (28-50秒)
**目的**: 演示利率计算：利息 = 本金 × 利率 × 时间

### 核心例子
"存入10000元，年利率3%，存3年，利息多少？"

### 元素
1. 问题文字
2. 钱袋图标（本金10000）
3. 时间轴（3年）
4. 利率标签（3%）
5. 公式：10000 × 3% × 3
6. 答案：900元

### 视觉设计
```python
# 本金可视化
self.principal_bag = Circle(radius=0.8, fill_color=COLOR_INTEREST, 
                            fill_opacity=0.3)

# 时间轴
self.timeline = Line(LEFT*3, RIGHT*3, color=COLOR_AUXILIARY)
self.year_marks = [Dot(pos) for pos in [LEFT*3, ORIGIN, RIGHT*3]]

# 利息累积动画
self.interest_bars = [Rectangle(...) for year in range(3)]
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.8s | 问题显示 | `FadeIn(question)` |
| 1.5s | 本金显示 | `FadeIn(principal_bag), FadeIn(label)` |
| 2.5s | 时间轴创建 | `Create(timeline), FadeIn(marks)` |
| 3.5s | 利率标签 | `FadeIn(rate_label)` |
| 4.5s | 第1年利息 | `GrowFromEdge(bar1, LEFT)` |
| 5.5s | 第2年利息 | `GrowFromEdge(bar2, LEFT)` |
| 6.5s | 第3年利息 | `GrowFromEdge(bar3, LEFT)` |
| 7.5s | 公式展示 | `Write(formula)` |
| 9.0s | 计算步骤 | `TransformMatchingTex(step1, step2)` |
| 10.0s | 答案闪现 | `FadeIn(answer), Flash(answer)` |
| 11.5s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: 所有元素

---

## Scene 5: 浓度应用 (50-68秒)
**目的**: 演示浓度计算：浓度 = 溶质 / 溶液 × 100%

### 核心例子
"20克盐溶解在100克水中，浓度是多少？"

### 元素
1. 问题文字
2. 烧杯图标
3. 盐（20克）
4. 水（100克）
5. 溶液（120克）
6. 公式：20 / 120 × 100%
7. 答案：≈16.7%

### 视觉设计
```python
# 烧杯
self.beaker = Polygon(
    [(-1, -2, 0), (-1, 1, 0), (-0.8, 1.2, 0),
     (0.8, 1.2, 0), (1, 1, 0), (1, -2, 0)],
    color=COLOR_CONCENTRATION
)

# 盐（小方块）
self.salt_cubes = VGroup(*[Square(0.2) for _ in range(5)])

# 水（蓝色矩形）
self.water = Rectangle(width=1.6, height=2, 
                       fill_color=BLUE, fill_opacity=0.3)

# 溶液（混合颜色）
self.solution = Rectangle(width=1.6, height=2.4,
                          fill_color=BLUE_E, fill_opacity=0.4)
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.8s | 问题显示 | `FadeIn(question)` |
| 1.5s | 烧杯创建 | `Create(beaker)` |
| 2.5s | 水倒入 | `FadeIn(water, shift=DOWN)` |
| 3.5s | 盐标签 | `FadeIn(salt_label)` |
| 4.0s | 盐倒入 | `FadeIn(salt_cubes, shift=DOWN, lag_ratio=0.2)` |
| 5.0s | 溶解动画 | `Transform(water+salt, solution)` |
| 6.0s | 溶液标签 | `FadeIn(solution_label)` |
| 7.0s | 公式展示 | `Write(formula)` |
| 8.5s | 计算步骤 | `Write(calculation)` |
| 9.5s | 答案闪现 | `FadeIn(answer), Flash(answer)` |
| 11.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: 所有元素

---

## Scene 6: 总结与关注 (68-78秒)
**目的**: 总结三个应用，引导关注

### 元素
1. 总结标题: "百分比，生活好帮手"
2. 三个应用卡片回顾
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 总结标题 | `Write(summary_title)` |
| 1.0s | 应用卡片 | `FadeIn(cards, lag_ratio=0.2)` |
| 2.5s | 作者信息放大 | `author_info.animate.scale(1.5)` |
| 3.5s | 关注提示 | `FadeIn(follow_text)` |
| 4.5s | 装饰动画 | `Rotate(decorations)` |
| 7.0s | 全部淡出 | `FadeOut(VGroup(*all))` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 全程保留 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| overview_cards | Scene 2 | Scene 2 | 应用概览 |
| price_rect | Scene 3 | Scene 3 | 折扣矩形 |
| timeline | Scene 4 | Scene 4 | 时间轴 |
| beaker | Scene 5 | Scene 5 | 烧杯 |
| summary_cards | Scene 6 | Scene 6 | 总结卡片 |

---

## 动画节奏控制
- 每个应用场景: 15-20秒
- 理解停顿: 2秒（每个答案后）
- 场景切换: 0.5秒
- 总时长: 约75秒

## 字体大小规范
- 标题: 36-40
- 问题文字: 28-32
- 公式: 32-36
- 标签: 22-24
- 作者信息: 20

## 关键设计原则
1. 使用实际生活场景增强理解
2. 视觉化展示计算过程
3. 颜色编码不同应用类型
4. 动画展示关键概念
5. 每个例子都有明确的实际意义