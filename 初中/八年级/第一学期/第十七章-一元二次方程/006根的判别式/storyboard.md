# 根的判别式 - 动画分镜脚本

## 元信息
- **目标时长**: 60-75秒
- **场景数量**: 7个
- **难度等级**: 中等
- **年级**: 八年级
- **知识点**: 一元二次方程的根的判别式

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主方程
COLOR_DELTA_POSITIVE = "#2ecc71" # 绿色 - Δ>0
COLOR_DELTA_ZERO = "#f39c12"     # 橙色 - Δ=0
COLOR_DELTA_NEGATIVE = "#e74c3c" # 红色 - Δ<0
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
COLOR_BACKGROUND = "#1a1a2e"
```

## 核心元素定义
由于这是代数主题（非几何），无需复杂的几何预计算。主要元素：
- 抛物线图像（使用 Axes + plot）
- 数轴（使用 NumberLine）
- 公式（使用 MathTex）
- 交点标记（使用 Dot）

---

## Scene 1: 开场钩子 (0-4秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题："如何判断方程有几个根？"
3. 三个不同的抛物线快闪

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` |
| 1.1s | 三个抛物线依次闪现 | `FadeIn(parabola_1), FadeIn(parabola_2), FadeIn(parabola_3)` |
| 2.8s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_text, parabolas
- 保留: author_info

---

## Scene 2: 方程介绍 (4-10秒)
**目的**: 展示一元二次方程标准形式，引入判别式

### 元素
1. 标题："一元二次方程"
2. 标准形式：ax²+bx+c=0 (a≠0)
3. 判别式定义：Δ=b²-4ac

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 4.0s | 标题写入 | `Write(title)` |
| 4.6s | 标准形式展示 | `Write(standard_form)` |
| 5.6s | 框选系数a,b,c | `Indicate(a), Indicate(b), Indicate(c)` |
| 6.8s | 判别式公式出现 | `FadeIn(delta_formula, shift=UP)` |
| 7.8s | 高亮判别式 | `Flash(delta_formula)` |
| 8.5s | 说明文字 | `FadeIn(explanation)` |

### 清理
- FadeOut: title, explanation
- 保留: standard_form, delta_formula (移到顶部作为参考)

---

## Scene 3: 情况一 - Δ>0 (10-22秒)
**目的**: 展示Δ>0时有两个不相等的实数根

### 元素
1. 副标题："情况1: Δ > 0"
2. 具体例子：x²-5x+6=0
3. 坐标系 + 抛物线（与x轴两个交点）
4. 数轴上的两个根

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 10.0s | 副标题 | `Write(subtitle_1)` |
| 10.5s | 例子方程 | `Write(example_1)` |
| 11.2s | 计算判别式 | `TransformMatchingTex(step by step)` |
| 12.5s | 结果：Δ=1>0 | `Indicate(delta_value)` |
| 13.5s | 创建坐标系 | `Create(axes)` |
| 14.5s | 绘制抛物线 | `Create(parabola, run_time=1.5)` |
| 16.0s | 标记交点 | `FadeIn(dot_1), FadeIn(dot_2)` |
| 16.8s | 闪烁交点 | `Flash(dot_1), Flash(dot_2)` |
| 17.5s | 数轴出现 | `Create(number_line)` |
| 18.2s | 根的位置 | `FadeIn(root_dot_1), FadeIn(root_dot_2)` |
| 19.0s | 标注x₁, x₂ | `Write(root_label_1), Write(root_label_2)` |
| 19.8s | 结论文字 | `FadeIn(conclusion_1)` |

### 清理
- FadeOut: 所有当前场景元素
- 保留: 顶部参考公式

---

## Scene 4: 情况二 - Δ=0 (22-34秒)
**目的**: 展示Δ=0时有两个相等的实数根（重根）

### 元素
1. 副标题："情况2: Δ = 0"
2. 具体例子：x²-4x+4=0
3. 坐标系 + 抛物线（与x轴相切，一个交点）
4. 数轴上的重根

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 22.0s | 副标题 | `Write(subtitle_2)` |
| 22.5s | 例子方程 | `Write(example_2)` |
| 23.2s | 计算判别式 | `TransformMatchingTex(step by step)` |
| 24.5s | 结果：Δ=0 | `Indicate(delta_value, color=COLOR_DELTA_ZERO)` |
| 25.5s | 创建坐标系 | `Create(axes)` |
| 26.5s | 绘制抛物线 | `Create(parabola, run_time=1.5)` |
| 28.0s | 标记切点 | `FadeIn(tangent_dot)` |
| 28.5s | 闪烁切点（强调） | `Flash(tangent_dot)` |
| 29.2s | 数轴出现 | `Create(number_line)` |
| 29.9s | 重根位置 | `FadeIn(root_dot)` |
| 30.5s | 标注x₁=x₂ | `Write(root_label)` |
| 31.2s | 结论文字 | `FadeIn(conclusion_2)` |

### 清理
- FadeOut: 所有当前场景元素
- 保留: 顶部参考公式

---

## Scene 5: 情况三 - Δ<0 (34-46秒)
**目的**: 展示Δ<0时没有实数根

### 元素
1. 副标题："情况3: Δ < 0"
2. 具体例子：x²+2x+5=0
3. 坐标系 + 抛物线（不与x轴相交）
4. 数轴（无交点标记）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 34.0s | 副标题 | `Write(subtitle_3)` |
| 34.5s | 例子方程 | `Write(example_3)` |
| 35.2s | 计算判别式 | `TransformMatchingTex(step by step)` |
| 36.5s | 结果：Δ=-16<0 | `Indicate(delta_value, color=COLOR_DELTA_NEGATIVE)` |
| 37.5s | 创建坐标系 | `Create(axes)` |
| 38.5s | 绘制抛物线 | `Create(parabola, run_time=1.5)` |
| 40.0s | x轴闪烁 | `Indicate(x_axis)` |
| 40.8s | 叉号标记（无交点）| `Write(cross_mark)` |
| 41.5s | 数轴出现 | `Create(number_line)` |
| 42.2s | 问号标记 | `FadeIn(question_mark)` |
| 43.0s | 结论文字 | `FadeIn(conclusion_3)` |

### 清理
- FadeOut: 所有当前场景元素
- 保留: 顶部参考公式

---

## Scene 6: 三种情况总结 (46-58秒)
**目的**: 汇总三种情况，强化记忆

### 元素
1. 标题："判别式总结"
2. 三行对比表格：
   - Δ>0 ⟺ 两个不等实根
   - Δ=0 ⟺ 两个相等实根
   - Δ<0 ⟺ 无实根
3. 三个小抛物线图示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 46.0s | 标题 | `Write(summary_title)` |
| 46.8s | 第一行 | `FadeIn(row_1), FadeIn(mini_graph_1)` |
| 48.2s | 第二行 | `FadeIn(row_2), FadeIn(mini_graph_2)` |
| 49.6s | 第三行 | `FadeIn(row_3), FadeIn(mini_graph_3)` |
| 51.0s | 框选整体 | `Create(surrounding_box)` |
| 52.0s | 重点提示 | `FadeIn(key_point, scale=1.1)` |
| 54.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: 所有元素

---

## Scene 7: 片尾关注 (58-65秒)
**目的**: 品牌展示，引导关注

### 元素
1. 作者信息放大
2. 抖音ID
3. 关注提示："关注我，获得更多数学技巧!"
4. 装饰元素（小星星/数学符号）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 58.0s | 作者名放大 | `Transform(author_info, author_large)` |
| 58.8s | 抖音ID | `FadeIn(author_id, shift=UP*0.3)` |
| 59.5s | 关注提示 | `FadeIn(follow_text, scale=1.1)` |
| 60.5s | 装饰符号旋转 | `Rotate(decorations, angle=PI)` |
| 62.0s | 等待 | `Wait(2.0)` |
| 64.0s | 全部淡出 | `FadeOut(VGroup(*))` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留，最后放大 |
| delta_formula | Scene 2 | Scene 6 | 作为参考保留 |
| axes (各场景) | Scene 3/4/5 | Scene 3/4/5 | 每个场景独立 |
| parabolas | Scene 3/4/5 | Scene 3/4/5 | 每个场景独立 |
| summary_table | Scene 6 | Scene 6 | 总结表格 |

---

## 技术要点

### 1. 抛物线绘制
```python
axes = Axes(
    x_range=[-2, 6, 1],
    y_range=[-2, 8, 2],
    axis_config={"include_numbers": True}
).scale(0.6).move_to(UP*1.5)

parabola = axes.plot(lambda x: x**2 - 5*x + 6, color=COLOR_PRIMARY)
```

### 2. 交点计算
```python
# 求根公式
import numpy as np
discriminant = b**2 - 4*a*c
if discriminant >= 0:
    x1 = (-b + np.sqrt(discriminant)) / (2*a)
    x2 = (-b - np.sqrt(discriminant)) / (2*a)
    point1 = axes.c2p(x1, 0)  # 坐标转换
    point2 = axes.c2p(x2, 0)
```

### 3. 数轴创建
```python
number_line = NumberLine(
    x_range=[0, 5, 1],
    length=6,
    include_numbers=True
).move_to(DOWN*3)
```

### 4. 公式高亮
```python
delta_formula = MathTex(
    r"\Delta", "=", "b^2", "-", "4ac"
)
delta_formula.set_color_by_tex("b^2", BLUE)
delta_formula.set_color_by_tex("4ac", RED)
```

---

## 验证清单

### 数学正确性
- [ ] 判别式计算准确
- [ ] 根的求解正确
- [ ] 抛物线与根的位置对应

### 视觉效果
- [ ] 三种情况颜色区分明显
- [ ] 交点/切点位置精确
- [ ] 文字不溢出边界

### 节奏控制
- [ ] 每个情况时长均衡（~12秒）
- [ ] 关键步骤有足够停留
- [ ] 总时长60-75秒

---

## 边界参考 (TikTok竖屏)
```
┌─────────────────────────────┐  y = +8
│  顶部：作者信息 + 参考公式    │  y = +7
├─────────────────────────────┤  y = +5.5
│                             │
│  主内容区域：                │  y ∈ [-3, +5]
│  - 坐标系（y ∈ [0, +4]）     │
│  - 公式展示（y ∈ [+4, +5.5]）│
│                             │
├─────────────────────────────┤  y = -3
│  底部：数轴、结论文字         │  y ∈ [-6, -3]
├─────────────────────────────┤  y = -6
│  底部安全区                  │  y = -8
└─────────────────────────────┘

横向: x ∈ [-4, +4] (安全区域)
```