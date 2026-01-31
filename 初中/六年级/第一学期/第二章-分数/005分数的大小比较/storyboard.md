# 分数大小比较 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 六年级
- 知识点: 分数大小比较（同分母、同分子、异分母异分子）

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要分数
COLOR_SECONDARY = "#e74c3c"    # 红色 - 对比分数
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_CORRECT = "#2ecc71"      # 绿色 - 正确答案
COLOR_BACKGROUND = "#1a1a2e"   # 深蓝背景
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 数轴中心 | y = 0 | self.numberline_center |
| 分数1位置 | 根据数值计算 | self.frac1_pos |
| 分数2位置 | 根据数值计算 | self.frac2_pos |
| 圆形分割 | 360°/分母 | self.sector_angle |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 吸引注意力，提出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (中心大字)
3. 两个分数对比

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 问题文字弹出 | `Write(hook_question)` |
| 1.0s | 显示两个分数 | `FadeIn(frac1), FadeIn(frac2)` |
| 2.0s | 分数闪烁强调 | `Flash(frac1), Flash(frac2)` |
| 3.5s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_question
- 保留: author_info, 准备进入场景2

---

## Scene 2: 同分母比较 (10秒)
**目的**: 展示同分母分数比分子的方法

### 元素
1. 标题: "方法一: 同分母比分子"
2. 两个分数: 3/7 和 5/7
3. 圆形可视化 (分成7份)
4. 结论文字

### 几何计算
```python
# 圆形半径
self.circle_radius = 1.2
# 扇形角度 (360°/7)
self.sector_angle = 360 / 7
# 圆形位置
self.circle1_pos = LEFT * 2 + UP * 1
self.circle2_pos = RIGHT * 2 + UP * 1
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 显示分数 3/7 和 5/7 | `Write(frac1), Write(frac2)` |
| 1.5s | 绘制两个圆形 | `Create(circle1), Create(circle2)` |
| 2.5s | 分割圆形(7份) | `Create(sectors)` |
| 3.5s | 填充3份(左圆) | `FadeIn(filled_sectors1)` |
| 4.5s | 填充5份(右圆) | `FadeIn(filled_sectors2)` |
| 5.5s | 高亮分子 | `Indicate(numerator1), Indicate(numerator2)` |
| 6.5s | 显示结论 | `FadeIn(conclusion)` |
| 8.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title, circles, fractions, conclusion
- 保留: author_info

---

## Scene 3: 同分子比较 (10秒)
**目的**: 展示同分子分数比分母的方法

### 元素
1. 标题: "方法二: 同分子比分母"
2. 两个分数: 2/5 和 2/7
3. 条形图可视化
4. 结论文字

### 几何计算
```python
# 条形宽度
self.bar_width = 0.5
# 条形最大高度
self.bar_max_height = 3.0
# 条形1高度 (2/5 的可视化)
self.bar1_height = self.bar_max_height * (2/5)
# 条形2高度 (2/7 的可视化)
self.bar2_height = self.bar_max_height * (2/7)
# 条形位置
self.bar1_pos = LEFT * 2
self.bar2_pos = RIGHT * 2
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 显示分数 2/5 和 2/7 | `Write(frac1), Write(frac2)` |
| 1.5s | 绘制两个矩形底座 | `Create(base1), Create(base2)` |
| 2.5s | 分割左矩形(5份) | `Create(divisions1)` |
| 3.0s | 分割右矩形(7份) | `Create(divisions2)` |
| 3.5s | 填充2份(左) | `GrowFromEdge(filled1, DOWN)` |
| 4.0s | 填充2份(右) | `GrowFromEdge(filled2, DOWN)` |
| 5.0s | 高亮分母 | `Indicate(denominator1), Indicate(denominator2)` |
| 6.0s | 显示结论 | `FadeIn(conclusion)` |
| 8.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title, bars, fractions, conclusion
- 保留: author_info

---

## Scene 4: 通分法 - 引入 (8秒)
**目的**: 引出异分母异分子的比较方法

### 元素
1. 标题: "方法三: 通分后比较"
2. 两个分数: 2/3 和 3/4
3. 问号动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 显示分数 2/3 和 3/4 | `Write(frac1), Write(frac2)` |
| 1.5s | 显示问号 | `FadeIn(question_mark, scale=0.5)` |
| 2.0s | 问号闪烁 | `Flash(question_mark)` |
| 2.5s | 提示文字 | `FadeIn(hint_text)` |
| 5.0s | 等待 | `Wait(2.5)` |

### 清理
- FadeOut: question_mark, hint_text
- 保留: title, frac1, frac2

---

## Scene 5: 通分过程 (12秒)
**目的**: 演示通分的详细步骤

### 元素
1. 原始分数: 2/3 和 3/4
2. 最小公倍数: LCM(3,4) = 12
3. 通分后分数: 8/12 和 9/12
4. 箭头动画

### 几何计算
```python
# 分数位置
self.original_left = LEFT * 3 + UP * 2
self.original_right = RIGHT * 3 + UP * 2
self.lcm_pos = ORIGIN
self.converted_left = LEFT * 3 + DOWN * 2
self.converted_right = RIGHT * 3 + DOWN * 2
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 移动原分数到上方 | `frac1.animate.move_to(...)` |
| 1.0s | 显示"找最小公倍数" | `FadeIn(lcm_text)` |
| 2.0s | 显示LCM = 12 | `Write(lcm_result)` |
| 3.0s | 箭头指向下方 | `GrowArrow(arrow1), GrowArrow(arrow2)` |
| 4.0s | 显示转换过程 | `Write(conversion1), Write(conversion2)` |
| 5.5s | 显示结果 8/12, 9/12 | `FadeIn(result1), FadeIn(result2)` |
| 7.0s | 高亮分子比较 | `Indicate(num1), Indicate(num2)` |
| 8.0s | 显示结论 | `FadeIn(conclusion)` |
| 10.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: 所有转换过程元素
- 保留: author_info

---

## Scene 6: 数轴可视化 (10秒)
**目的**: 用数轴直观展示分数大小

### 元素
1. 数轴 (0到1)
2. 分数点标注
3. 比较箭头

### 几何计算
```python
# 数轴参数
self.numberline_start = LEFT * 4
self.numberline_end = RIGHT * 4
self.numberline_y = 0
# 分数在数轴上的位置
self.pos_2_3 = self.numberline_start + (2/3) * (self.numberline_end - self.numberline_start)
self.pos_3_4 = self.numberline_start + (3/4) * (self.numberline_end - self.numberline_start)
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 绘制数轴 | `Create(numberline)` |
| 1.0s | 标注0和1 | `FadeIn(label_0), FadeIn(label_1)` |
| 2.0s | 标记2/3位置 | `FadeIn(dot1), Write(label1)` |
| 3.0s | 标记3/4位置 | `FadeIn(dot2), Write(label2)` |
| 4.0s | 绘制比较箭头 | `GrowArrow(comparison_arrow)` |
| 5.0s | 显示结论 | `FadeIn(conclusion)` |
| 7.5s | 等待 | `Wait(2.5)` |

### 清理
- FadeOut: numberline, dots, labels, conclusion
- 保留: author_info

---

## Scene 7: 总结与片尾 (10秒)
**目的**: 总结三种方法，引导关注

### 元素
1. 三种方法卡片
2. 关注提示
3. 作者信息放大

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题"三种比较方法" | `Write(summary_title)` |
| 1.0s | 卡片1滑入 | `card1.animate.shift(...)` |
| 1.5s | 卡片2滑入 | `card2.animate.shift(...)` |
| 2.0s | 卡片3滑入 | `card3.animate.shift(...)` |
| 3.5s | 所有卡片闪烁 | `Flash(cards)` |
| 4.5s | 关注提示淡入 | `FadeIn(follow_text, scale=1.1)` |
| 6.0s | 作者信息放大 | `author_info.animate.scale(1.5)` |
| 8.0s | 等待 | `Wait(2.0)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| hook_question | Scene 1 | Scene 1 | 开场钩子 |
| method1_title | Scene 2 | Scene 2 | 方法标题 |
| circles | Scene 2 | Scene 2 | 圆形可视化 |
| method2_title | Scene 3 | Scene 3 | 方法标题 |
| bars | Scene 3 | Scene 3 | 条形可视化 |
| method3_title | Scene 4 | Scene 5 | 方法标题 |
| conversion_elements | Scene 5 | Scene 5 | 通分过程 |
| numberline | Scene 6 | Scene 6 | 数轴 |
| summary_cards | Scene 7 | Scene 7 | 总结卡片 |

---

## 关键参数配置

### 字体大小
```python
FONT_SIZES = {
    "title": 36,
    "subtitle": 28,
    "body": 22,
    "fraction": 32,
    "label": 20,
    "small": 18,
}
```

### 时间控制
```python
TIMINGS = {
    "fast_transition": 0.3,
    "normal_transition": 0.5,
    "slow_transition": 0.8,
    "understanding_pause": 1.5,
    "scene_pause": 2.0,
}
```

### 坐标边界
```python
SAFE_BOUNDS = {
    "x_min": -4.0,
    "x_max": 4.0,
    "y_min": -7.0,
    "y_max": 7.0,
    "y_top_safe": 7.0,    # 作者信息区
    "y_content_top": 5.5,  # 内容区顶部
    "y_content_bottom": -3.0,  # 内容区底部
    "y_bottom_safe": -6.0,  # 底部文字区
}
```

---

## 验证清单

### 前置检查
- [ ] 所有分数值已验证正确
- [ ] 几何计算公式已确认
- [ ] 颜色配置统一
- [ ] 字体大小符合规范

### 渲染后检查
- [ ] 无元素溢出边界
- [ ] 无文字重叠
- [ ] 动画流畅自然
- [ ] 难点有充足停留时间
- [ ] 总时长在目标范围内 (60-75秒)