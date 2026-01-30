# 组合图形面积计算 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 六年级 (中等)
- 核心概念: 割补法计算组合图形面积

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要图形
COLOR_SECONDARY = "#e74c3c"      # 红色 - 辅助图形
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮/闪烁
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_SECTOR = "#2ecc71"         # 绿色 - 扇形
COLOR_TRIANGLE = "#f39c12"       # 橙色 - 三角形
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 正方形边长 | 固定值 2.5 | self.side_length |
| 正方形顶点 | 基于中心点和边长 | self.A, self.B, self.C, self.D |
| 圆心 | 正方形中心 | self.center |
| 半圆圆心 | 正方形顶边中点 | self.semicircle_center |
| 四分之一圆圆心 | 正方形右下角 | self.quarter_circle_center |
| 缩放系数 | 0.85 | self.SCALE |
| 垂直偏移 | UP * 1.0 | self.OFFSET |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力，提出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题文字
3. 组合图形缩略图

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_text)` |
| 1.5s | 组合图形淡入 | `FadeIn(composite_figure)` |
| 2.5s | 图形闪烁提示 | `Flash(composite_figure)` |
| 3.5s | 等待 | `Wait(1.0)` |

### 钩子文字
"这个图形的面积怎么算？"

### 清理
- FadeOut: hook_text
- 保留: composite_figure, author_info
- 移动: composite_figure 向上移动到主内容区

---

## Scene 2: 图形分解介绍 (5-12秒)
**目的**: 介绍割补法概念

### 元素
1. 标题: "割补法"
2. 说明文字
3. 组合图形
4. 分解提示箭头

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 5.0s | 标题淡入 | `Write(title)` |
| 5.8s | 说明文字淡入 | `FadeIn(explanation)` |
| 6.5s | 图形放大 | `composite_figure.animate.scale(1.2)` |
| 7.5s | 分解箭头出现 | `Create(arrows)` |
| 9.0s | 等待理解 | `Wait(1.5)` |

### 文字内容
- 标题: "割补法"
- 说明: "把复杂图形分成简单图形"

### 清理
- FadeOut: title, explanation, arrows
- 保留: composite_figure

---

## Scene 3: 分解步骤1 - 正方形 (12-20秒)
**目的**: 识别正方形部分

### 元素
1. 步骤标题: "第一步：找出正方形"
2. 正方形高亮
3. 边长标注
4. 面积公式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 12.0s | 步骤标题出现 | `Write(step_title)` |
| 13.0s | 正方形高亮 | `square.animate.set_color(COLOR_HIGHLIGHT)` |
| 14.0s | 边长标注出现 | `FadeIn(side_labels)` |
| 15.0s | 面积公式书写 | `Write(formula)` |
| 16.5s | 计算结果显示 | `Write(result)` |
| 18.0s | 等待 | `Wait(1.5)` |

### 公式
- S₁ = a² = 2.5² = 6.25

### 清理
- FadeOut: step_title
- 保留: square (恢复原色), side_labels, formula, result
- 移动: formula 和 result 到左侧记录区

---

## Scene 4: 分解步骤2 - 半圆 (20-28秒)
**目的**: 识别半圆部分

### 元素
1. 步骤标题: "第二步：找出半圆"
2. 半圆高亮
3. 半径标注
4. 面积公式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 20.0s | 步骤标题出现 | `Write(step_title)` |
| 21.0s | 半圆高亮 | `semicircle.animate.set_color(COLOR_HIGHLIGHT)` |
| 22.0s | 半径标注 | `Create(radius_line), Write(radius_label)` |
| 23.0s | 面积公式书写 | `Write(formula)` |
| 24.5s | 计算结果显示 | `Write(result)` |
| 26.0s | 等待 | `Wait(1.5)` |

### 公式
- S₂ = πr²/2 = π(1.25)²/2 ≈ 2.45

### 清理
- FadeOut: step_title, radius_line, radius_label
- 保留: semicircle (恢复原色)
- 移动: formula 和 result 到左侧记录区

---

## Scene 5: 分解步骤3 - 四分之一圆 (28-36秒)
**目的**: 识别四分之一圆（需要减去）

### 元素
1. 步骤标题: "第三步：注意多余部分"
2. 四分之一圆高亮
3. 半径标注
4. 面积公式（带负号）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 28.0s | 步骤标题出现 | `Write(step_title)` |
| 29.0s | 四分之一圆闪烁 | `Flash(quarter_circle)` |
| 29.5s | 四分之一圆高亮红色 | `quarter_circle.animate.set_color(RED)` |
| 30.5s | 提示文字 | `Write(warning)` "这部分要减掉!" |
| 31.5s | 面积公式书写 | `Write(formula)` |
| 33.0s | 计算结果显示 | `Write(result)` |
| 34.5s | 等待 | `Wait(1.5)` |

### 公式
- S₃ = πr²/4 = π(1.25)²/4 ≈ 1.23

### 清理
- FadeOut: step_title, warning
- 保留: quarter_circle (保持红色)
- 移动: formula 和 result 到左侧记录区

---

## Scene 6: 总结计算 (36-50秒)
**目的**: 综合所有部分，计算总面积

### 元素
1. 标题: "组合计算"
2. 总公式
3. 分步计算
4. 最终答案（特效）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 36.0s | 标题出现 | `Write(title)` |
| 37.0s | 三个公式聚拢 | `Transform(formulas, summary_group)` |
| 38.5s | 总公式书写 | `Write(total_formula)` |
| 40.0s | 计算过程显示 | `Write(calculation)` |
| 42.0s | 等号出现 | `Write(equals)` |
| 43.0s | 最终答案放大显示 | `Write(final_answer).scale(1.5)` |
| 44.0s | 答案闪烁 | `Flash(final_answer)` |
| 45.0s | 图形全部高亮展示 | 各部分依次闪烁 |
| 47.5s | 等待 | `Wait(2.0)` |

### 公式
- S = S₁ + S₂ - S₃
- S = 6.25 + 2.45 - 1.23
- S = 7.47 (平方单位)

### 清理
- 保留所有元素用于总结场景

---

## Scene 7: 结尾总结 (50-65秒)
**目的**: 强化记忆点，引导关注

### 元素
1. 关键提示框
2. 作者信息放大
3. 关注提示
4. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 50.0s | 前一场景淡出 | `FadeOut(all_previous)` |
| 51.0s | 关键点提示框淡入 | `FadeIn(key_points_box)` |
| 52.0s | 要点依次显示 | `Write(point_1), Write(point_2), Write(point_3)` |
| 56.0s | 作者信息放大 | `Transform(author_info, author_large)` |
| 57.5s | 关注提示 | `Write(follow_text)` |
| 59.0s | 装饰元素 | `FadeIn(decorations)` |
| 62.0s | 等待 | `Wait(2.0)` |

### 文字内容
关键点:
1. "识别基本图形"
2. "加上凸出部分"
3. "减去重叠部分"

关注提示: "关注我，学更多数学技巧!"

### 清理
- 全部淡出结束

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 贯穿全程 |
| composite_figure | Scene 1 | Scene 6 | 主图形 |
| square | Scene 3 | Scene 6 | 正方形部分 |
| semicircle | Scene 4 | Scene 6 | 半圆部分 |
| quarter_circle | Scene 5 | Scene 6 | 四分之一圆 |
| formula_1 | Scene 3 | Scene 6 | 正方形公式 |
| formula_2 | Scene 4 | Scene 6 | 半圆公式 |
| formula_3 | Scene 5 | Scene 6 | 四分之一圆公式 |
| key_points | Scene 7 | Scene 7 | 总结要点 |

---

## 几何计算验证

### 正方形
- 边长: a = 2.5
- 顶点: 
  - A = center + UP*1.25 + LEFT*1.25
  - B = center + UP*1.25 + RIGHT*1.25
  - C = center + DOWN*1.25 + RIGHT*1.25
  - D = center + DOWN*1.25 + LEFT*1.25
- 面积: S₁ = 2.5² = 6.25

### 半圆
- 圆心: 正方形上边中点
- 半径: r = 1.25 (边长的一半)
- 面积: S₂ = πr²/2 = π × 1.5625 / 2 ≈ 2.454

### 四分之一圆
- 圆心: 正方形右下角 C 点
- 半径: r = 1.25
- 面积: S₃ = πr²/4 = π × 1.5625 / 4 ≈ 1.227

### 总面积
- S = S₁ + S₂ - S₃
- S = 6.25 + 2.454 - 1.227
- S ≈ 7.477 平方单位

---

## 技术注意事项

### 字体处理
- 中文: `Text("...", font="Noto Sans CJK SC")`
- 数学公式: `MathTex(r"...")`
- 不要在 MathTex 中放中文！

### 虚线处理
- 使用 `DashedLine(start, end, dash_length=0.1)`
- 不使用 `set_style(stroke_dasharray=...)`

### 坐标边界
- 主内容区: y ∈ [-3, +5]
- 文字区: y ∈ [-6, -3]
- 标题区: y ∈ [+5.5, +7.5]
- 横向: x ∈ [-4, +4]

### 动画节奏
- 简单图形创建: 0.8-1.0s
- 文字书写: 0.5-0.8s
- 关键步骤停留: 1.5-2.0s
- 场景切换: 0.4-0.6s