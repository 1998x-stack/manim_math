# 比例的意义与性质 - 动画分镜脚本

## 元信息
- 目标时长: 65-75 秒
- 场景数量: 7 个
- 难度等级: 中等
- 目标观众: 六年级学生
- 主题: 比例的定义和基本性质（内项积等于外项积）

## 颜色配置
```python
COLOR_OUTER = "#e74c3c"         # 红色 - 外项
COLOR_INNER = "#3498db"         # 蓝色 - 内项
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮重点
COLOR_PROPERTY = "#2ecc71"      # 绿色 - 性质/定理
COLOR_CROSS = "#9b59b6"         # 紫色 - 交叉线
COLOR_EQUALS = GOLD             # 金色 - 相等关系
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助元素
COLOR_BACKGROUND = "#1a1a2e"    # 深蓝背景
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 比例式中心 | UP * 2 | self.proportion_center |
| 外项a位置 | LEFT * 3 + UP * 2 | self.pos_a |
| 内项b位置 | LEFT * 1 + UP * 2 | self.pos_b |
| 内项c位置 | RIGHT * 1 + UP * 2 | self.pos_c |
| 外项d位置 | RIGHT * 3 + UP * 2 | self.pos_d |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 吸引注意力，引出比例概念

### 元素
1. 作者标识 (顶部)
2. 钩子问题
3. 两个比展示: 2:3 和 4:6

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子问题书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 第一个比2:3 | `FadeIn(ratio_1)` | 0.5s |
| 1.6s | 第二个比4:6 | `FadeIn(ratio_2)` | 0.5s |
| 2.1s | 等号闪烁 | `Flash(equals_sign)` | 0.4s |
| 2.5s | 问题文字 | `FadeIn(question)` | 0.5s |
| 3.0s | 等待 | `Wait(1.0)` | 1.0s |

### 文案
- 钩子: "两个比相等意味着什么?"
- 展示: "2 : 3 = 4 : 6"
- 问题: "这个式子有什么神奇的性质?"

### 清理
- FadeOut: hook_text, question
- 保留: 比例式, author_info

---

## Scene 2: 比例的定义 (8秒)
**目的**: 明确比例的定义

### 元素
1. 标题: "比例的意义"
2. 定义文字
3. 一般形式: a:b=c:d
4. 具体例子: 2:3=4:6

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题书写 | `Write(title)` | 0.6s |
| 0.6s | 定义淡入 | `FadeIn(definition)` | 0.5s |
| 1.1s | 一般形式 | `Write(general_form)` | 0.8s |
| 1.9s | 箭头 | `GrowArrow(arrow)` | 0.4s |
| 2.3s | 具体例子 | `Write(example)` | 0.8s |
| 3.1s | 高亮"两个比相等" | `Indicate(equality_concept)` | 0.6s |
| 3.7s | 说明文字 | `FadeIn(explanation)` | 0.5s |
| 4.2s | 等待 | `Wait(3.0)` | 3.0s |

### 公式
```python
general_form = MathTex(r"a:b = c:d")
example = MathTex(r"2:3 = 4:6")
```

### 清理
- FadeOut: 所有元素
- 准备下一场景

---

## Scene 3: 比例各部分名称 (10秒)
**目的**: 介绍外项和内项的概念

### 元素
1. 标题: "比例的各部分"
2. 比例式: a:b=c:d
3. 外项标注 (a, d)
4. 内项标注 (b, c)
5. 颜色区分

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `Write(title)` | 0.6s |
| 0.6s | 比例式 | `Write(proportion)` | 0.8s |
| 1.4s | 高亮a | `a.animate.set_color(COLOR_OUTER).scale(1.2)` | 0.5s |
| 1.9s | 高亮d | `d.animate.set_color(COLOR_OUTER).scale(1.2)` | 0.5s |
| 2.4s | "外项"标签 | `FadeIn(outer_label)` | 0.5s |
| 2.9s | 外项弧线 | `Create(outer_arc)` | 0.6s |
| 3.5s | 高亮b | `b.animate.set_color(COLOR_INNER).scale(1.2)` | 0.5s |
| 4.0s | 高亮c | `c.animate.set_color(COLOR_INNER).scale(1.2)` | 0.5s |
| 4.5s | "内项"标签 | `FadeIn(inner_label)` | 0.5s |
| 5.0s | 内项弧线 | `Create(inner_arc)` | 0.6s |
| 5.6s | 说明文字 | `FadeIn(explanation)` | 0.5s |
| 6.1s | 等待 | `Wait(3.0)` | 3.0s |

### 视觉设计
- 外项 (a, d): 红色，两端
- 内项 (b, c): 蓝色，中间
- 用弧线连接外项和内项

### 清理
- 保留比例式，淡出标签和弧线

---

## Scene 4: 基本性质演示 - 交叉相乘 (12秒)
**目的**: 演示内项积等于外项积

### 元素
1. 标题: "比例的基本性质"
2. 比例式: a:b=c:d
3. 交叉线动画
4. 乘法表达式

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `Write(title)` | 0.6s |
| 0.6s | 性质说明 | `FadeIn(property_text)` | 0.5s |
| 1.1s | 比例式 | `Write(proportion)` | 0.8s |
| 1.9s | 交叉线1 (a→d) | `Create(cross_line_1)` | 0.8s |
| 2.7s | 交叉线2 (b→c) | `Create(cross_line_2)` | 0.8s |
| 3.5s | 形成X形 | `Indicate(cross_lines)` | 0.5s |
| 4.0s | 外项积公式 | `Write(outer_product: a×d)` | 0.8s |
| 4.8s | 等号 | `Write(equals)` | 0.4s |
| 5.2s | 内项积公式 | `Write(inner_product: b×c)` | 0.8s |
| 6.0s | 完整公式高亮 | `Indicate(full_formula)` | 0.6s |
| 6.6s | 结论文字 | `FadeIn(conclusion)` | 0.5s |
| 7.1s | 等待 | `Wait(4.0)` | 4.0s |

### 公式
```python
proportion = MathTex(r"a:b = c:d")
outer_product = MathTex(r"a \times d")
inner_product = MathTex(r"b \times c")
property_formula = MathTex(r"a \times d = b \times c")
```

### 视觉效果
- 交叉线用紫色
- 动画展示 a×d 和 b×c
- 强调"内项积 = 外项积"

### 清理
- FadeOut: 交叉线
- 保留公式

---

## Scene 5: 具体例子验证 (12秒)
**目的**: 用数字验证基本性质

### 元素
1. 例子: 2:3=4:6
2. 计算外项积: 2×6
3. 计算内项积: 3×4
4. 验证相等: 12=12

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `Write(verification_title)` | 0.5s |
| 0.5s | 例子比例 | `Write(example_proportion)` | 0.8s |
| 1.3s | 标注外项 | `Indicate(outer_terms)` | 0.5s |
| 1.8s | 外项积计算 | `Write(calc_outer: 2×6=12)` | 1.0s |
| 2.8s | 标注内项 | `Indicate(inner_terms)` | 0.5s |
| 3.3s | 内项积计算 | `Write(calc_inner: 3×4=12)` | 1.0s |
| 4.3s | 两个12闪烁 | `Flash(both_12s)` | 0.6s |
| 4.9s | 等号强调 | `Write(big_equals)` | 0.5s |
| 5.4s | 完整验证式 | `Write(verification: 12=12)` | 0.8s |
| 6.2s | 成功标记 | `FadeIn(checkmark)` | 0.5s |
| 6.7s | 结论 | `FadeIn(conclusion_text)` | 0.5s |
| 7.2s | 等待 | `Wait(4.0)` | 4.0s |

### 计算展示
```python
example = MathTex(r"2:3 = 4:6")
outer_calc = MathTex(r"2 \times 6 = 12")
inner_calc = MathTex(r"3 \times 4 = 12")
verification = MathTex(r"12 = 12")
```

### 清理
- FadeOut: 所有计算元素

---

## Scene 6: 应用 - 判断能否组成比例 (10秒)
**目的**: 展示如何用性质判断四个数能否组成比例

### 元素
1. 问题: "3, 4, 6, 8 能否组成比例?"
2. 尝试: 3:4=6:8
3. 验证计算
4. 结论

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 问题引入 | `Write(problem)` | 0.8s |
| 0.8s | 四个数展示 | `FadeIn(numbers: 3,4,6,8)` | 0.6s |
| 1.4s | 尝试组合 | `Write(attempt: 3:4=6:8)` | 0.8s |
| 2.2s | 外项积 | `Write(3×8=24)` | 0.8s |
| 3.0s | 内项积 | `Write(4×6=24)` | 0.8s |
| 3.8s | 验证相等 | `Write(24=24)` | 0.5s |
| 4.3s | 成功提示 | `FadeIn(success_icon)` | 0.5s |
| 4.8s | 结论 | `FadeIn(conclusion)` | 0.6s |
| 5.4s | 方法说明 | `FadeIn(method_text)` | 0.6s |
| 6.0s | 等待 | `Wait(3.5)` | 3.5s |

### 文案
- 问题: "3, 4, 6, 8 能组成比例吗?"
- 结论: "能! 因为 3×8 = 4×6"
- 方法: "内项积 = 外项积 → 能组成比例"

### 清理
- FadeOut: 所有元素

---

## Scene 7: 总结与片尾 (9秒)
**目的**: 巩固知识点，引导关注

### 元素
1. 知识点总结卡片
2. 核心公式回顾
3. 作者信息
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 总结标题 | `Write(summary_title)` | 0.6s |
| 0.6s | 要点1滑入 | `card_1.animate.shift(RIGHT*10)` | 0.5s |
| 1.1s | 要点2滑入 | `card_2.animate.shift(RIGHT*10)` | 0.5s |
| 1.6s | 要点3滑入 | `card_3.animate.shift(RIGHT*10)` | 0.5s |
| 2.1s | 核心公式 | `Write(key_formula)` | 0.8s |
| 2.9s | 等待 | `Wait(0.8)` | 0.8s |
| 3.7s | 淡出总结 | `FadeOut(summary_group)` | 0.5s |
| 4.2s | 作者放大 | `author.animate.scale(2)` | 0.6s |
| 4.8s | 关注文字 | `FadeIn(follow_text)` | 0.5s |
| 5.3s | 装饰 | `LaggedStart(icons)` | 0.8s |
| 6.1s | 等待 | `Wait(2.0)` | 2.0s |

### 总结要点
1. "比例: 两个比相等的式子"
2. "比例基本性质: 内项积 = 外项积"
3. "应用: 判断四个数能否组成比例"

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 持续存在 |
| proportion_basic | Scene 1 | Scene 2 | 初始比例 |
| outer_inner_labels | Scene 3 | Scene 3 | 外项内项标注 |
| cross_lines | Scene 4 | Scene 4 | 交叉线 |
| property_formula | Scene 4 | Scene 5 | 基本性质公式 |
| verification | Scene 5 | Scene 5 | 验证计算 |
| application | Scene 6 | Scene 6 | 应用示例 |
| summary_cards | Scene 7 | Scene 7 | 总结卡片 |

---

## 时长分配检查
- Scene 1: 4秒
- Scene 2: 8秒
- Scene 3: 10秒
- Scene 4: 12秒
- Scene 5: 12秒
- Scene 6: 10秒
- Scene 7: 9秒
- **总计: 65秒** (符合45-90秒范围)

---

## 难点停留策略
1. **外项内项概念** (Scene 3): 停留3秒，清晰展示位置
2. **交叉相乘** (Scene 4): 停留4秒，强调X形交叉
3. **数值验证** (Scene 5): 停留4秒，逐步计算
4. **应用方法** (Scene 6): 停留3.5秒，理解判断方法

---

## 视觉设计notes
1. **数字大小**: 比例式字号48，公式字号32，说明字号22
2. **颜色一致性**: 
   - 外项始终为红色
   - 内项始终为蓝色
   - 交叉线为紫色
   - 相等关系为金色
3. **动画速度**: 
   - 交叉线创建: 0.8秒
   - 数值计算: 1.0秒
   - 验证相等: 0.5秒
4. **布局**: 保持在安全区域 y∈[-6, 7], x∈[-4, 4]
5. **交叉线设计**: 使用 Line + Arrow 或纯 Line，颜色突出