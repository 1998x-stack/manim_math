# 分式不等式 - 动画分镜脚本

## 元信息
- 目标时长: 60 秒
- 场景数量: 6 个
- 难度等级: 中等

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"  # 蓝色 - 主要元素
COLOR_SECONDARY = "#2ecc71"  # 绿色 - 次要元素
COLOR_HIGHLIGHT = YELLOW  # 黄色 - 高亮元素
COLOR_AUXILIARY = GRAY_B  # 灰色 - 辅助线
COLOR_NEGATIVE = RED  # 红色 - 负值区域
COLOR_POSITIVE = GREEN  # 绿色 - 正值区域
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 数轴 | 从-5到5 | self.number_line |
| 关键点 | 分子分母零点 | self.critical_points |
| 区间 | 关键点划分的区间 | self.intervals |

---

## Scene 1: 开场 (3-4秒)
**目的**: 钩子 + 引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字)
3. 主图形

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.1s | 分式不等式展示 | `Write(inequality)` |
| 2.1s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text
- 保留: inequality, author_info

---

## Scene 2: 概念引入 (5-6秒)
**目的**: 介绍分式不等式的定义和特点

### 元素
1. 一般形式 f(x)/g(x) > 0
2. 强调不能交叉相乘
3. 等价转化 f(x)*g(x) > 0

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 展示一般形式 | `Write(general_form)` |
| 1.0s | 高亮强调不能交叉相乘 | `Indicate(cross_multiply_warning)` |
| 2.0s | 展示等价转化过程 | `TransformMatchingTex(...)` |
| 3.0s | 强调条件g(x)≠0 | `Write(condition)` |

### 清理
- 保留: general_form, condition

---

## Scene 3: 解题步骤演示 (8-10秒)
**目的**: 展示解题步骤

### 元素
1. 移项通分
2. 使不等式一边为0
3. 转化为乘积形式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 展示原始不等式 | `Write(original_inequality)` |
| 1.0s | 移项 | `TransformMatchingTex(original, moved)` |
| 2.0s | 通分 | `TransformMatchingTex(moved, simplified)` |
| 3.0s | 转化为乘积形式 | `TransformMatchingTex(simplified, product_form)` |

### 清理
- 保留: product_form

---

## Scene 4: 数轴标根法 (12-15秒)
**目的**: 演示数轴标根法的核心思想

### 元素
1. 数轴绘制
2. 标出关键点(分子分母零点)
3. 奇穿偶不穿法则
4. 标注正负区间

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 绘制数轴 | `Create(number_line)` |
| 1.0s | 标出关键点 | `FadeIn(critical_points)` |
| 2.0s | 从右上方开始标正负 | `Create(signs)` |
| 3.0s | 演示"奇穿偶不穿" | `DrawBorderThenFill(piercing_lines)` |

### 清理
- 保留: number_line, critical_points, signs

---

## Scene 5: 实例演示 (15-18秒)
**目的**: 通过具体例子演示整个解题过程

### 元素
1. 具体分式不等式
2. 分子分母因式分解
3. 标出关键点
4. 标注正负区间
5. 确定解集

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 展示具体例子 | `Write(example_inequality)` |
| 1.0s | 因式分解 | `TransformMatchingTex(example, factored)` |
| 2.0s | 找到关键点 | `Create(key_points)` |
| 3.0s | 数轴标根 | `Create(root_diagram)` |
| 4.0s | 确定解集 | `Highlight(solution)` |

### 清理
- 保留: example_inequality, solution

---

## Scene 6: 总结与提醒 (5-7秒)
**目的**: 总结方法，强调注意事项

### 元素
1. 解题步骤回顾
2. 分母不为0的提醒
3. 关注信息

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 总结解题步骤 | `Create(steps_summary)` |
| 1.0s | 强调分母不为0 | `Indicate(denominator_warning)` |
| 2.0s | 展示关注信息 | `Write(follow_message)` |

### 清理
- 保留: follow_message

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| inequality | Scene 1 | Scene 6 | 原始不等式 |
| number_line | Scene 4 | Scene 6 | 数轴 |
| critical_points | Scene 4 | Scene 6 | 关键点 |
| solution | Scene 5 | Scene 6 | 最终解 |
| ... | ... | ... | ... |
