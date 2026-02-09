# 集合间的关系 - 动画分镜脚本

## 元信息
- 目标时长: 70-85 秒
- 场景数量: 8 个
- 难度等级: 中等
- 目标观众: 高一学生

## 颜色配置
```python
COLOR_SET_A = "#3498db"        # 蓝色 - 集合A
COLOR_SET_B = "#e74c3c"        # 红色 - 集合B
COLOR_SUBSET = "#2ecc71"       # 绿色 - 子集
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
COLOR_EMPTY = "#95a5a6"        # 灰色 - 空集
```

## 视觉元素预计算清单
| 元素 | 计算方式 | 存储变量 |
|------|---------|---------|
| 集合A圆心 | 固定位置 | self.circle_A_center = LEFT * 1.2 + UP * 2 |
| 集合B圆心 | 固定位置 | self.circle_B_center = RIGHT * 1.2 + UP * 2 |
| 圆半径 | 统一 | self.CIRCLE_RADIUS = 1.5 |
| 元素点位置 | 圆内均匀分布 | self.element_positions_A, self.element_positions_B |
| 公式位置 | 底部安全区 | self.formula_pos = DOWN * 2.5 |

## 核心约束
- 所有圆心和半径在 `setup_geometry()` 中统一定义
- Venn 图位置精确计算，确保不重叠或完全包含时的正确性
- 文字大小遵循规范（标题36，正文22，公式28）
- 元素不溢出边界 (x∈[-4,4], y∈[-7,7])
- 中文使用 `Text()` + "Noto Sans CJK SC"
- 数学符号使用 `MathTex()`

---

## Scene 1: 开场钩子 (0-4秒)
**目的**: 引出集合间关系的问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题
3. 两个集合的预览

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字 | `Write(hook)` - "集合A和B，谁包含谁?" |
| 1.5s | 两个圆淡入 | `FadeIn(circle_A), FadeIn(circle_B)` |
| 2.5s | 问号出现 | `Write(question_mark)` |
| 3.5s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook, question_mark
- 保留: author_info, circles (会变换)

---

## Scene 2: 子集定义 (4-14秒)
**目的**: 介绍子集的概念 A⊆B

### 元素
1. 标题 "子集 Subset"
2. 定义文字
3. Venn 图（A在B内部）
4. 公式 A⊆B

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 4.0s | 标题淡入 | `FadeIn(title)` |
| 4.5s | 清空旧圆，创建新布局 | `FadeOut(old)` |
| 5.0s | 绘制大圆B | `Create(circle_B)` - 半径2.0 |
| 6.0s | 绘制小圆A（在B内） | `Create(circle_A)` - 半径1.2 |
| 7.0s | 添加元素点 | `FadeIn(dots_A), FadeIn(dots_B)` |
| 8.0s | 高亮A的元素 | `Indicate(dots_A)` |
| 8.8s | 箭头指向 | `GrowArrow(arrow)` "都在B中" |
| 9.5s | 公式出现 | `Write(formula)` A⊆B |
| 10.5s | 朗读 | `FadeIn(reading)` "A是B的子集" |
| 12.0s | 定义文字 | `FadeIn(definition)` |
| 13.5s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: title, definition, arrow, formula
- 保留: circles, dots

---

## Scene 3: 真子集 (14-24秒)
**目的**: 介绍真子集的概念 A⊊B

### 元素
1. 标题 "真子集 Proper Subset"
2. 强调 A≠B
3. 公式 A⊊B

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 14.0s | 标题淡入 | `FadeIn(title)` |
| 14.5s | 高亮B中不在A的元素 | `Indicate(extra_dots_B, color=RED)` |
| 15.5s | 不等号 | `Write(inequality)` A≠B |
| 16.5s | 真子集符号 | `Write(formula)` A⊊B |
| 17.5s | 说明文字 | `FadeIn(explanation)` "A⊆B且A≠B" |
| 19.0s | 对比动画 | 子集符号→真子集符号变换 |
| 21.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, formula, explanation
- 保留: circles, dots

---

## Scene 4: 集合相等 (24-32秒)
**目的**: 说明集合相等的条件

### 元素
1. 标题 "集合相等"
2. 两个完全重合的圆
3. 公式 A=B ⟺ A⊆B且B⊆A

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 24.0s | 标题淡入 | `FadeIn(title)` |
| 24.5s | 圆A移动重合 | `circle_A.animate.move_to(circle_B)` |
| 26.0s | 两圆变同色 | `set_color(PURPLE)` |
| 27.0s | 双向包含箭头 | `GrowArrow(arrows)` ⊆ 和 ⊆ |
| 28.5s | 等号公式 | `Write(formula)` A=B |
| 29.5s | 条件说明 | `FadeIn(condition)` |
| 31.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: title, arrows, formula, condition
- 重置: circles到原位

---

## Scene 5: 空集性质 (32-42秒)
**目的**: 说明空集是任何集合的子集

### 元素
1. 标题 "空集 Empty Set"
2. 空集符号 ∅
3. 公式 ∅⊆A

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 32.0s | 标题淡入 | `FadeIn(title)` |
| 32.5s | 清空圆A | `FadeOut(dots_A)` |
| 33.5s | 空集符号 | `Write(empty_symbol)` ∅ |
| 34.5s | 移入圆B | `empty_symbol.animate.move_to(circle_B)` |
| 36.0s | 公式1 | `Write(formula_1)` ∅⊆A |
| 37.5s | 说明 | `FadeIn(text)` "空集是任何集合的子集" |
| 39.0s | 公式2 | `Write(formula_2)` ∅⊊A (非空) |
| 40.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: title, formulas, text, empty_symbol
- 恢复: dots_A

---

## Scene 6: 子集个数公式 (42-54秒)
**目的**: 介绍子集个数公式 2^n

### 元素
1. 标题 "子集个数"
2. 集合 A={1,2,3}
3. 列举所有子集
4. 公式 2^n

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 42.0s | 标题淡入 | `FadeIn(title)` |
| 42.5s | 展示集合A | `Write(set_A)` A={1,2,3} |
| 43.5s | n=3 | `Write(n_value)` |
| 44.5s | 子集逐个出现 | 8个子集框依次淡入 |
| 44.8s | ∅ | 第1个 |
| 45.2s | {1} | 第2个 |
| 45.6s | {2} | 第3个 |
| 46.0s | {3} | 第4个 |
| 46.4s | {1,2} | 第5个 |
| 46.8s | {1,3} | 第6个 |
| 47.2s | {2,3} | 第7个 |
| 47.6s | {1,2,3} | 第8个 |
| 48.5s | 计数动画 | 高亮8个子集 |
| 49.5s | 公式 | `Write(formula)` 2^3 = 8 |
| 51.0s | 一般公式 | `TransformMatchingTex` 2^n |
| 52.5s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, subsets, formulas
- 保留: circles

---

## Scene 7: 真子集个数 (54-64秒)
**目的**: 介绍真子集个数公式 2^n - 1

### 元素
1. 标题 "真子集个数"
2. 排除自身
3. 公式 2^n - 1

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 54.0s | 标题淡入 | `FadeIn(title)` |
| 54.5s | 重新展示8个子集 | 快速淡入 |
| 55.5s | 划掉{1,2,3} | `Cross` 标记 |
| 56.5s | 说明 | `FadeIn(text)` "排除自身" |
| 57.5s | 剩余7个高亮 | `Indicate` |
| 58.5s | 公式 | `Write(formula)` 2^3 - 1 = 7 |
| 60.0s | 一般公式 | `TransformMatchingTex` 2^n - 1 |
| 61.5s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, subsets, formulas
- 清空场景

---

## Scene 8: 片尾总结 (64-85秒)
**目的**: 总结要点 + 引导关注

### 元素
1. 知识要点卡片
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 64.0s | 清空场景 | `FadeOut(*)` |
| 65.0s | 标题 | `FadeIn(title)` "集合关系要点" |
| 66.0s | 卡片1 | "子集: A⊆B" |
| 67.0s | 卡片2 | "真子集: A⊊B (A≠B)" |
| 68.0s | 卡片3 | "空集: ∅⊆任何集合" |
| 69.0s | 卡片4 | "子集: 2^n, 真子集: 2^n-1" |
| 71.0s | 作者信息放大 | `author_info.animate.scale(2)` |
| 73.0s | 关注文字 | "关注我，学更多数学技巧!" |
| 75.0s | 集合符号装饰 | ⊆⊊符号旋转动画 |
| 78.0s | 等待 | `Wait(3.0)` |
| 81.0s | 全部淡出 | `FadeOut(*)` |

### 清理
- 全部清空

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 一直保留，最后放大 |
| circle_A | Scene 2 | Scene 7 | 会变换位置和大小 |
| circle_B | Scene 2 | Scene 7 | 主要参考圆 |
| dots_A | Scene 2 | Scene 7 | 集合A的元素 |
| dots_B | Scene 2 | Scene 7 | 集合B的元素 |
| formulas | 各场景 | 各场景结束 | 临时公式 |
| subset_boxes | Scene 6 | Scene 6 | 子集列举框 |
| summary_cards | Scene 8 | Scene 8 | 总结卡片 |

---

## 关键坐标定义
```python
# 主要区域
TITLE_Y = 5.5          # 标题位置
MAIN_Y = 2.0           # 主内容区（Venn图）
FORMULA_Y = -2.5       # 公式区
EXPLANATION_Y = -4.5   # 说明文字区
AUTHOR_Y = 7.0         # 作者信息

# Venn 图参数（场景2-5）
CIRCLE_A_CENTER_SUBSET = LEFT * 0.5 + UP * MAIN_Y  # A在B内时
CIRCLE_B_CENTER_SUBSET = ORIGIN + UP * MAIN_Y
CIRCLE_A_RADIUS_SUBSET = 1.2
CIRCLE_B_RADIUS_SUBSET = 2.0

# 独立圆参数（场景1）
CIRCLE_A_CENTER_INIT = LEFT * 1.5 + UP * MAIN_Y
CIRCLE_B_CENTER_INIT = RIGHT * 1.5 + UP * MAIN_Y
CIRCLE_RADIUS_INIT = 1.3
```

---

## 动画节奏控制
- 快速动画: 0.3-0.5s (简单淡入淡出)
- 正常动画: 0.8-1.2s (绘制、变换)
- 理解停顿: 1.5-2.0s (关键概念后)
- 场景切换: 0.4-0.6s
- 子集列举: 0.4s/个 (快速展示)

---

## 验证清单
- [ ] 所有圆心和半径在 setup_geometry() 中定义
- [ ] Venn 图包含关系精确（A真包含于B）
- [ ] 公式使用 MathTex，避免中文
- [ ] 子集列举动画流畅
- [ ] 总时长 70-85 秒
- [ ] 开场有钩子，结尾有总结+关注