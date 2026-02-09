# 集合的运算 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 8 个
- 难度等级: 高一
- 知识点: 交集、并集、补集

## 颜色配置
```python
COLOR_SET_A = "#e74c3c"        # 红色 - 集合A
COLOR_SET_B = "#3498db"        # 蓝色 - 集合B
COLOR_UNIVERSAL = "#95a5a6"    # 灰色 - 全集
COLOR_INTERSECTION = "#9b59b6" # 紫色 - 交集
COLOR_UNION = "#2ecc71"        # 绿色 - 并集
COLOR_COMPLEMENT = "#f39c12"   # 橙色 - 补集
COLOR_HIGHLIGHT = YELLOW
BACKGROUND_COLOR = "#1a1a2e"
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆A中心 | 固定位置 LEFT*1.2 + UP*2 | self.center_A |
| 圆B中心 | 固定位置 RIGHT*1.2 + UP*2 | self.center_B |
| 圆半径 | 固定值 1.2 | self.radius |
| 全集矩形 | 包含两圆 | self.universal_rect |

---

## Scene 1: 开场介绍 (3-4秒)
**目的**: 钩子 + 引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字)
3. 两个圆形集合预览

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.0s | 两个圆形集合创建 | `Create(circle_A), Create(circle_B)` |
| 2.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text
- 保留: circles, author_info

---

## Scene 2: 交集演示 (8-10秒)
**目的**: 演示交集的定义和计算

### 元素
1. 标题: "交集 A ∩ B"
2. 定义文字
3. 两个圆形集合
4. 交集区域高亮

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 定义公式书写 | `Write(formula)` |
| 1.5s | 圆A填充动画 | `circle_A.animate.set_fill(opacity=0.3)` |
| 2.0s | 圆B填充动画 | `circle_B.animate.set_fill(opacity=0.3)` |
| 2.5s | 交集区域高亮 | `FadeIn(intersection_region)` |
| 3.5s | 示例元素展示 | `FadeIn(example_elements)` |
| 5.5s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title, formula, intersection_region, example_elements
- 保留: circles

---

## Scene 3: 并集演示 (8-10秒)
**目的**: 演示并集的定义和计算

### 元素
1. 标题: "并集 A ∪ B"
2. 定义文字
3. 两个圆形集合
4. 并集区域高亮

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 定义公式书写 | `Write(formula)` |
| 1.5s | 并集区域高亮 | `FadeIn(union_region)` |
| 2.5s | 示例元素展示 | `FadeIn(example_elements)` |
| 5.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title, formula, union_region, example_elements
- 保留: circles

---

## Scene 4: 补集演示 (8-10秒)
**目的**: 演示补集的定义和计算

### 元素
1. 全集矩形U
2. 标题: "补集 ∁ᵤA"
3. 定义文字
4. 补集区域高亮

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 全集矩形创建 | `Create(universal_set)` |
| 0.8s | 标题淡入 | `FadeIn(title)` |
| 1.3s | 定义公式书写 | `Write(formula)` |
| 2.3s | 补集区域高亮 | `FadeIn(complement_region)` |
| 4.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title, formula, complement_region
- 保留: universal_set, circles

---

## Scene 5: 运算性质1 (6-8秒)
**目的**: 展示基本性质

### 元素
1. 标题: "基本性质"
2. 公式列表

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 性质1展示 | `Write(property_1)` |
| 1.5s | 性质2展示 | `Write(property_2)` |
| 3.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: all properties
- 保留: universal_set, circles

---

## Scene 6: 运算性质2 (6-8秒)
**目的**: 展示补集性质

### 元素
1. 标题: "补集性质"
2. 公式列表

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 性质1展示 | `Write(property_1)` |
| 1.0s | 性质2展示 | `Write(property_2)` |
| 2.5s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: all properties
- 保留: none

---

## Scene 7: 综合示例 (8-10秒)
**目的**: 综合应用示例

### 元素
1. 具体数字集合
2. 计算过程

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 示例题目展示 | `Write(example)` |
| 1.5s | 集合创建 | `Create(sets)` |
| 3.0s | 结果展示 | `Write(result)` |
| 5.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: all
- 保留: none

---

## Scene 8: 片尾关注 (3-4秒)
**目的**: 引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息放大 | `Transform(author)` |
| 0.8s | 关注提示淡入 | `FadeIn(follow_text)` |
| 2.0s | 装饰动画 | `Rotate(decorations)` |

### 清理
- FadeOut: all

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 作者信息 |
| circle_A | Scene 1 | Scene 7 | 集合A |
| circle_B | Scene 1 | Scene 7 | 集合B |
| universal_set | Scene 4 | Scene 7 | 全集 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |

---

## 动画节奏说明
- 开场快节奏吸引注意 (3-4秒)
- 核心概念详细讲解 (每个8-10秒)
- 性质快速展示 (每个6-8秒)
- 片尾引导关注 (3-4秒)
- 总时长: 60-75秒