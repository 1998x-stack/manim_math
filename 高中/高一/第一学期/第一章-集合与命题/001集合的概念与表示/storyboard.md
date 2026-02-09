# 集合的概念与表示 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 入门
- 目标观众: 高一学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主集合
COLOR_SECONDARY = "#e74c3c"    # 红色 - 元素/强调
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
COLOR_SUCCESS = "#2ecc71"      # 绿色 - 正确
COLOR_ERROR = "#e67e22"        # 橙色 - 错误
```

## 视觉元素预计算清单
| 元素 | 计算方式 | 存储变量 |
|------|---------|---------|
| 主集合圆 | 固定位置 | self.set_circle_center = UP * 2 |
| 元素点位置 | 圆内均匀分布 | self.element_positions (list) |
| 文字框位置 | 底部安全区 | self.text_box_pos = DOWN * 5 |
| 公式位置 | 中部 | self.formula_pos = ORIGIN |

## 核心约束
- 所有元素位置在 `setup_visual_elements()` 中统一计算
- 文字大小遵循规范（标题36，正文22，标签20）
- 元素不溢出边界 (x∈[-4,4], y∈[-7,7])
- 中文使用 `Text()` + "Noto Sans CJK SC"
- 公式使用 `MathTex()`

---

## Scene 1: 开场钩子 (0-4秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题（大字）
3. 数字和物品混乱动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_question)` - "1, 2, 3, 🍎, 🐱... 如何整理?" |
| 1.5s | 数字和图标随机飞入 | `LaggedStart(*[FadeIn(obj, shift=random) for obj in objects])` |
| 3.0s | 混乱元素聚拢 | `objects.animate.arrange_in_grid()` |
| 3.8s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_question, random_objects
- 保留: author_info

---

## Scene 2: 集合的定义 (4-12秒)
**目的**: 介绍集合的基本概念

### 元素
1. 标题 "什么是集合?"
2. 定义文字
3. 圆形集合可视化
4. 元素点（1, 2, 3, 4, 5）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 4.0s | 标题淡入 | `FadeIn(title, shift=DOWN)` |
| 4.5s | 圆形绘制 | `Create(set_circle)` |
| 5.5s | 标签 "集合A" | `Write(set_label)` |
| 6.0s | 定义文字出现 | `FadeIn(definition)` - "由确定对象组成的整体" |
| 7.0s | 元素点依次出现 | `Succession(*[FadeIn(dot) for dot in dots])` |
| 8.5s | 元素标签 | `Write(element_labels)` - 1,2,3,4,5 |
| 10.0s | 强调 "整体" | `Indicate(set_circle)` |
| 11.0s | 等待理解 | `Wait(1.0)` |

### 清理
- FadeOut: title, definition
- 保留: set_circle, dots, element_labels, set_label

---

## Scene 3: 三大特性 (12-28秒)
**目的**: 讲解确定性、互异性、无序性

### 3.1 确定性 (12-17秒)
| 时间 | 动作 | 说明 |
|------|------|------|
| 12.0s | 标题 "确定性" | 淡入 |
| 12.5s | 问号 "?" 靠近集合 | 表示不确定的对象 |
| 13.5s | 问号被弹开 | `问号.animate.shift(DOWN*3).fade(1)` |
| 14.0s | √ 符号靠近 | 表示确定的对象 |
| 14.8s | √ 进入集合 | `FadeIn(new_dot)` |
| 15.5s | 说明文字 | "要么属于，要么不属于" |

### 3.2 互异性 (17-22秒)
| 时间 | 动作 | 说明 |
|------|------|------|
| 17.0s | 标题 "互异性" | 淡入 |
| 17.5s | 复制一个 "3" | 尝试加入集合 |
| 18.5s | 红色警告 ✗ | `Flash(duplicate, color=RED)` |
| 19.0s | 重复元素消失 | 表示不能重复 |
| 19.8s | 说明文字 | "元素互不相同" |

### 3.3 无序性 (22-28秒)
| 时间 | 动作 | 说明 |
|------|------|------|
| 22.0s | 标题 "无序性" | 淡入 |
| 22.5s | 元素重新排列动画 | `dots.animate.arrange()` 多次 |
| 25.0s | 等号 "=" 出现 | 表示仍是同一集合 |
| 26.0s | 说明文字 | "顺序不影响集合" |

### 清理
- FadeOut: 所有特性标题和说明
- 保留: set_circle, dots (恢复原始位置)

---

## Scene 4: 元素与集合关系 (28-38秒)
**目的**: 讲解 ∈ 和 ∉ 符号

### 元素
1. 公式 `3 ∈ A`
2. 公式 `6 ∉ A`
3. 动画演示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 28.0s | 标题 "元素与集合" | 淡入 |
| 28.5s | 高亮元素 3 | `Indicate(dot_3, color=YELLOW)` |
| 29.5s | 公式 `3 ∈ A` 出现 | `Write(formula_1)` |
| 31.0s | 朗读符号 | 文字 "3 属于 A" |
| 32.5s | 数字 6 出现在圆外 | `FadeIn(six_dot, shift=LEFT)` |
| 33.5s | 公式 `6 ∉ A` 出现 | `Write(formula_2)` |
| 35.0s | 朗读符号 | 文字 "6 不属于 A" |
| 36.5s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: formulas, six_dot, title
- 保留: set_circle, dots

---

## Scene 5: 表示方法 - 列举法 (38-48秒)
**目的**: 介绍列举法

### 元素
1. 标题 "列举法"
2. 公式 `A = {1, 2, 3, 4, 5}`
3. 元素与公式对应动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 38.0s | 标题 "表示方法 1: 列举法" | 淡入 |
| 39.0s | 公式框架 `A = { }` | `Write(formula_shell)` |
| 40.0s | 元素依次加入公式 | 点亮圆内元素，同时添加到公式 |
| 40.5s | "1" 加入 | `Transform(dot_1_label.copy(), formula_1)` |
| 41.0s | "2" 加入 | 同上 |
| 41.5s | "3" 加入 | 同上 |
| 42.0s | "4" 加入 | 同上 |
| 42.5s | "5" 加入 | 同上 |
| 43.5s | 最终公式 `A = {1,2,3,4,5}` | 完整显示 |
| 44.5s | 说明文字 | "一一列举元素" |
| 46.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: formula, title
- 保留: set_circle, dots

---

## Scene 6: 表示方法 - 描述法 (48-58秒)
**目的**: 介绍描述法

### 元素
1. 标题 "描述法"
2. 公式 `A = {x | x ∈ ℕ, 1 ≤ x ≤ 5}`
3. 条件高亮动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 48.0s | 标题 "表示方法 2: 描述法" | 淡入 |
| 49.0s | 公式 `A = {x │ ... }` 框架 | `Write(formula_framework)` |
| 50.0s | 条件 `x ∈ ℕ` 出现 | `Write(condition_1)` |
| 51.5s | 条件 `1 ≤ x ≤ 5` 出现 | `Write(condition_2)` |
| 53.0s | 完整公式 | 全部组合 |
| 54.0s | 说明文字 | "用共同特征描述" |
| 55.0s | 高亮 "x" | `Indicate(x_symbols)` |
| 56.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: formula, title
- 保留: set_circle (透明化准备下一场景)

---

## Scene 7: 片尾总结 (58-75秒)
**目的**: 总结要点 + 引导关注

### 元素
1. 三大特性总结
2. 两种表示法
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 58.0s | 清空场景 | `FadeOut(set_circle, dots)` |
| 59.0s | 标题 "集合要点" | 大字淡入 |
| 60.0s | 卡片1: 三大特性 | 从左侧滑入 |
| 61.0s | 卡片2: ∈ 和 ∉ | 从左侧滑入 |
| 62.0s | 卡片3: 两种表示法 | 从左侧滑入 |
| 64.0s | 作者信息放大 | `author_info.animate.scale(2).move_to(UP)` |
| 66.0s | 关注文字 | "关注我，学更多数学技巧!" |
| 68.0s | 小图标装饰 | 集合符号旋转动画 |
| 70.0s | 等待 | `Wait(3.0)` |
| 73.0s | 全部淡出 | `FadeOut(*)` |

### 清理
- 全部清空

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 一直保留，最后放大 |
| set_circle | Scene 2 | Scene 7 | 主集合圆 |
| dots (元素点) | Scene 2 | Scene 7 | 1-5 的点 |
| element_labels | Scene 2 | Scene 7 | 元素标签 |
| hook_question | Scene 1 | Scene 1 | 开场钩子 |
| random_objects | Scene 1 | Scene 1 | 临时混乱元素 |
| property_titles | Scene 3 | Scene 3 | 三大特性标题 |
| formulas | Scene 4-6 | 各自场景结束 | 临时公式 |
| summary_cards | Scene 7 | Scene 7 | 总结卡片 |

---

## 关键坐标定义
```python
# 主要区域
TITLE_Y = 6.5          # 标题位置
MAIN_Y = 2.0           # 主内容区（集合圆）
FORMULA_Y = -2.0       # 公式区
EXPLANATION_Y = -4.5   # 说明文字区
AUTHOR_Y = 7.0         # 作者信息

# 集合圆参数
SET_CIRCLE_RADIUS = 1.8
SET_CIRCLE_CENTER = UP * MAIN_Y

# 元素点分布（圆内均匀）
ELEMENT_ANGLES = [0, 72, 144, 216, 288]  # 五个点均匀分布
ELEMENT_RADIUS = 1.2  # 距圆心距离
```

---

## 动画节奏控制
- 快速动画: 0.3-0.5s (简单淡入淡出)
- 正常动画: 0.8-1.2s (绘制、变换)
- 理解停顿: 1.5-2.0s (关键概念后)
- 场景切换: 0.4-0.6s

---

## 验证清单
- [ ] 所有文字在边界内
- [ ] 元素点位置精确计算（圆内均匀分布）
- [ ] 公式使用 MathTex，中文使用 Text
- [ ] 动画节奏流畅，无突兀跳跃
- [ ] 总时长 60-75 秒
- [ ] 开场有钩子，结尾有总结+关注