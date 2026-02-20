# 含绝对值不等式 - 动画分镜脚本

## 元信息
- 目标时长: 45-60 秒
- 场景数量: 7 个
- 难度等级: 中等
- 目标观众: 高一学生

## 颜色配置
```python
COLOR_ABSOLUTE_VALUE = BLUE
COLOR_NUMBER_LINE = WHITE
COLOR_POINTS = YELLOW
COLOR_SOLUTION_REGION = GREEN
COLOR_AUXILIARY = GRAY_B
BACKGROUND_COLOR = "#1a1a2e"
COLOR_HIGHLIGHT = YELLOW
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 数轴原点 | n2p(0) | self.origin_pos |
| a点位置 | n2p(a) | self.pos_a |
| -a点位置 | n2p(-a) | self.neg_a |
| b点位置 | n2p(b) | self.pos_b |
| -b点位置 | n2p(-b) | self.neg_b |
| 中心a位置 | n2p(center_a) | self.center_a_pos |
| a-b位置 | n2p(center_a-b) | self.center_a_minus_b |
| a+b位置 | n2p(center_a+b) | self.center_a_plus_b |

---

## Scene 1: 开场 (3-4秒)
**目的**: 钩子 + 引出绝对值不等式的概念

### 元素
1. 作者标识 (顶部小字)
2. 主标题 (含绝对值不等式)
3. 钩子问题 ("你知道|x|<3的解是什么吗？")

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 标题书写 | `Write(title)` |
| 1.1s | 钩子问题出现 | `Write(hook_question)` |
| 2.1s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_question
- 保留: title, author_info

---

## Scene 2: 绝对值几何意义 (6-8秒)
**目的**: 复习绝对值的几何意义

### 元素
1. 数轴
2. 原点标记
3. 正负示例点
4. 距离可视化

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 绘制数轴 | `Create(number_line)` |
| 0.5s | 标记原点 | `Dot(origin_pos), Write(origin_label)` |
| 1.0s | 创建示例点x=2 | `Dot(x_pos), Write(x_label)` |
| 2.0s | 绘制距离线段 | `Line(origin_pos, x_pos)` |
| 3.0s | 显示距离值 | `Brace(distance_line), Write(distance_text)` |
| 4.0s | 添加反向点x=-2 | `Dot(x_neg_pos), Line(origin_pos, x_neg_pos)` |
| 5.0s | 解释几何意义 | `Write(geometric_meaning)` |

### 清理
- 保留: number_line, origin_dot

---

## Scene 3: |x| < a 型不等式 (8-10秒)
**目的**: 演示|x| < a的几何解释和解法

### 元素
1. 数轴
2. -a和a点标记
3. 区间(-a, a)高亮
4. 等价形式公式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 保持数轴显示 | `Keep(number_line)` |
| 0.5s | 标记-a和a点 | `Dot(neg_a_pos), Dot(pos_a_pos), Write(labels)` |
| 1.5s | 高亮区间(-a,a) | `Line(neg_a_pos, pos_a_pos, stroke_width=8, color=green)` |
| 2.5s | 显示等价形式 | `Write(equivalence: |x|<a ⟺ -a<x<a)` |
| 3.5s | 几何解释动画 | `Animating solution region on number line` |

### 清理
- 保留: number_line, solution_interval

---

## Scene 4: |x| > a 型不等式 (8-10秒)
**目的**: 演示|x| > a的几何解释和解法

### 元素
1. 数轴
2. -a和a点标记
3. 区间(-∞, -a)∪(a, +∞)高亮
4. 等价形式公式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 保持数轴显示 | `Keep(number_line)` |
| 0.5s | 保留-a和a点标记 | `Keep(neg_a_dot, pos_a_dot)` |
| 1.0s | 高亮左半部分 | `DashedLine(left_end, neg_a_pos, stroke_width=8)` |
| 2.0s | 高亮右半部分 | `DashedLine(pos_a_pos, right_end, stroke_width=8)` |
| 3.0s | 显示等价形式 | `Write(equivalence: |x|>a ⟺ x<-a 或 x>a)` |
| 4.0s | 几何解释动画 | `Animating solution regions` |

### 清理
- 保留: number_line, neg_a_dot, pos_a_dot

---

## Scene 5: |x-a| < b 型不等式 (8-10秒)
**目的**: 演示平移型绝对值不等式

### 元素
1. 数轴
2. 中心点a和边界点a-b, a+b
3. 区间(a-b, a+b)高亮
4. 等价转换公式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 显示数轴 | `ShowCreation(number_line)` |
| 0.5s | 标记中心点a | `Dot(center_a_pos), Write(center_label)` |
| 1.0s | 标记边界点 | `Dot(a_minus_b_pos), Dot(a_plus_b_pos), Write(boundary_labels)` |
| 2.0s | 高亮区间 | `Line(a_minus_b_pos, a_plus_b_pos, stroke_width=8)` |
| 3.0s | 显示等价转换 | `Write(equivalence: |x-a|<b ⟺ a-b<x<a+b)` |
| 4.0s | 几何解释 | `Animating distance from center point` |

### 清理
- 保留: number_line, center_a_dot

---

## Scene 6: 三角不等式 (6-8秒)
**目的**: 介绍重要的三角不等式

### 元素
1. 三角不等式公式
2. 举例验证
3. 拓展公式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 主公式出现 | `Write(main_inequality: |a+b|≤|a|+|b|)` |
| 1.0s | 拓展公式 | `Write(extended_inequality: ||a|-|b||≤|a±b|≤|a|+|b|)` |
| 2.0s | 举例验证 | `Write(example: a=3, b=-2)` |
| 3.0s | 数值计算 | `Write(calculation: |3+(-2)|=1≤|3|+|-2|=5)` |

### 清理
- 保留: main_inequality

---

## Scene 7: 总结 (4-5秒)
**目的**: 重点回顾 + 关注提示

### 元素
1. 三种主要形式总结
2. 作者信息
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 总结文字出现 | `Write(summary_text)` |
| 1.0s | 作者信息出现 | `FadeIn(author_info)` |
| 2.0s | 关注提示出现 | `Write(follow_hint)` |
| 3.0s | 等待结束 | `Wait(1.0)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| number_line | Scene 2 | End | 主数轴 |
| origin_dot | Scene 2 | End | 原点标记 |
| pos_a/neg_a_dots | Scene 3 | End | a和-a点 |
| title | Scene 1 | Scene 2 | 标题 |
| hook_question | Scene 1 | Scene 1 | 钩子问题 |
| solution_interval | Scene 3 | Scene 4 | 解集区间 |
| main_inequality | Scene 6 | End | 三角不等式 |

---

## 数学公式
- |x| < a ⟺ -a < x < a (a > 0)
- |x| > a ⟺ x < -a 或 x > a (a > 0)
- |x - a| < b ⟺ a - b < x < a + b
- |a + b| ≤ |a| + |b| (三角不等式)
- ||a| - |b|| ≤ |a ± b| ≤ |a| + |b|

## 相关知识点
- 绝对值的几何意义
- 数轴上的距离
- 分类讨论思想
- 三角不等式
