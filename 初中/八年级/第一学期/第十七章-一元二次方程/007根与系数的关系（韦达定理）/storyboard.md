# 韦达定理（根与系数的关系） - 动画分镜脚本

## 元信息
- **目标时长**: 65-80秒
- **场景数量**: 7个
- **难度等级**: 中等
- **年级**: 八年级
- **知识点**: 一元二次方程的根与系数关系

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主公式
COLOR_ROOT_1 = "#e74c3c"         # 红色 - x₁
COLOR_ROOT_2 = "#2ecc71"         # 绿色 - x₂
COLOR_SUM = "#f39c12"            # 橙色 - 和式
COLOR_PRODUCT = "#9b59b6"        # 紫色 - 积式
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
COLOR_BACKGROUND = "#1a1a2e"
```

## 核心元素定义
由于这是纯代数主题，无需几何预计算。主要元素：
- 公式展示（MathTex）
- 推导步骤（TransformMatchingTex）
- 括号标注（Brace）
- 箭头指示（Arrow）

---

## Scene 1: 开场钩子 (0-4秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题："不解方程，如何求两根之和与积？"
3. 方程快闪：x² - 5x + 6 = 0

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=1.0)` |
| 1.3s | 方程出现 | `Write(equation)` |
| 2.1s | 问号闪烁 | `Flash(question_mark)` |
| 2.8s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_text, equation
- 保留: author_info

---

## Scene 2: 韦达定理介绍 (4-12秒)
**目的**: 展示韦达定理的两个核心公式

### 元素
1. 标题："韦达定理"
2. 标准形式：ax²+bx+c=0 (a≠0)
3. 两根标记：x₁, x₂
4. 核心公式：
   - x₁ + x₂ = -b/a
   - x₁ × x₂ = c/a

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 4.0s | 标题写入 | `Write(title)` |
| 4.8s | 标准形式展示 | `Write(standard_form)` |
| 5.8s | 两根标记 | `FadeIn(root_labels)` |
| 6.6s | 公式1出现（和） | `FadeIn(formula_sum, shift=UP)` |
| 7.6s | 公式2出现（积） | `FadeIn(formula_product, shift=UP)` |
| 8.6s | 高亮框选 | `Create(surrounding_box)` |
| 9.6s | 说明文字 | `FadeIn(explanation)` |

### 清理
- FadeOut: title, explanation
- 保留: standard_form, formula_sum, formula_product (移到顶部作为参考)

---

## Scene 3: 公式推导 (12-22秒)
**目的**: 从求根公式推导韦达定理（可选简化版）

### 元素
1. 副标题："公式推导"
2. 求根公式：x = (-b ± √Δ) / (2a)
3. 两根表示：
   - x₁ = (-b + √Δ) / (2a)
   - x₂ = (-b - √Δ) / (2a)
4. 和的推导：x₁ + x₂ = -b/a
5. 积的推导：x₁ × x₂ = c/a

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 12.0s | 副标题 | `Write(subtitle)` |
| 12.5s | 求根公式 | `Write(quadratic_formula)` |
| 13.5s | 展开x₁, x₂ | `TransformMatchingTex` |
| 14.5s | 计算x₁+x₂ | `TransformMatchingTex(step by step)` |
| 16.5s | 结果闪烁 | `Indicate(sum_result)` |
| 17.5s | 计算x₁×x₂ | `TransformMatchingTex(step by step)` |
| 19.5s | 结果闪烁 | `Indicate(product_result)` |

### 清理
- FadeOut: 所有推导过程
- 保留: 顶部参考公式

---

## Scene 4: 例题1 - 已知方程求和积 (22-32秒)
**目的**: 应用韦达定理直接求两根之和与积

### 元素
1. 副标题："例题1：求两根之和与积"
2. 方程：x² - 7x + 12 = 0
3. 系数标注：a=1, b=-7, c=12
4. 计算过程：
   - x₁ + x₂ = -(-7)/1 = 7
   - x₁ × x₂ = 12/1 = 12

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 22.0s | 副标题 | `Write(subtitle_ex1)` |
| 22.5s | 方程 | `Write(equation_ex1)` |
| 23.3s | 标注系数 | `Indicate(a), Indicate(b), Indicate(c)` |
| 24.5s | 计算和 | `TransformMatchingTex(step by step)` |
| 26.0s | 和的结果 | `Indicate(sum_result, color=COLOR_SUM)` |
| 27.0s | 计算积 | `TransformMatchingTex(step by step)` |
| 28.5s | 积的结果 | `Indicate(product_result, color=COLOR_PRODUCT)` |
| 29.5s | 答案框 | `Create(answer_box)` |

### 清理
- FadeOut: 所有当前场景元素
- 保留: 顶部参考公式

---

## Scene 5: 例题2 - 已知两根求方程 (32-42秒)
**目的**: 反向应用韦达定理构造方程

### 元素
1. 副标题："例题2：已知两根，求方程"
2. 已知：x₁ = 3, x₂ = 4
3. 计算：
   - x₁ + x₂ = 7
   - x₁ × x₂ = 12
4. 构造方程：x² - 7x + 12 = 0

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 32.0s | 副标题 | `Write(subtitle_ex2)` |
| 32.5s | 已知条件 | `Write(given_roots)` |
| 33.3s | 计算和 | `Write(sum_calc)` |
| 34.3s | 计算积 | `Write(product_calc)` |
| 35.3s | 反推公式 | `FadeIn(reverse_formula)` |
| 36.5s | 代入数值 | `TransformMatchingTex` |
| 37.8s | 最终方程 | `Indicate(final_equation)` |
| 38.8s | 验证标记 | `Write(check_mark)` |

### 清理
- FadeOut: 所有当前场景元素
- 保留: 顶部参考公式

---

## Scene 6: 例题3 - 对称式计算 (42-54秒)
**目的**: 利用韦达定理计算复杂对称式

### 元素
1. 副标题："例题3：对称式计算"
2. 方程：x² - 5x + 3 = 0
3. 求：x₁² + x₂²
4. 技巧展示：
   - x₁² + x₂² = (x₁+x₂)² - 2x₁x₂
5. 计算过程：
   - x₁ + x₂ = 5
   - x₁ × x₂ = 3
   - x₁² + x₂² = 5² - 2×3 = 25 - 6 = 19

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 42.0s | 副标题 | `Write(subtitle_ex3)` |
| 42.5s | 方程 | `Write(equation_ex3)` |
| 43.3s | 求解目标 | `Write(target)` |
| 44.3s | 技巧公式 | `FadeIn(identity, shift=UP)` |
| 45.5s | 高亮关键 | `Indicate(identity)` |
| 46.5s | 代入x₁+x₂ | `TransformMatchingTex` |
| 47.8s | 代入x₁x₂ | `TransformMatchingTex` |
| 49.0s | 计算结果 | `TransformMatchingTex` |
| 50.5s | 最终答案 | `Indicate(final_answer, color=YELLOW)` |

### 清理
- FadeOut: 所有当前场景元素
- 保留: 顶部参考公式

---

## Scene 7: 总结与片尾 (54-65秒)
**目的**: 总结韦达定理的应用，引导关注

### 元素
1. 标题："韦达定理总结"
2. 三个应用场景：
   - ✓ 求两根之和与积
   - ✓ 已知两根构造方程
   - ✓ 计算对称式
3. 关键提示："韦达定理 = 不解方程的神器"
4. 作者信息与关注引导

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 54.0s | 标题 | `Write(summary_title)` |
| 54.8s | 应用1 | `FadeIn(app_1, shift=UP)` |
| 56.0s | 应用2 | `FadeIn(app_2, shift=UP)` |
| 57.2s | 应用3 | `FadeIn(app_3, shift=UP)` |
| 58.4s | 关键提示 | `FadeIn(key_point, scale=1.1)` |
| 59.5s | 作者放大 | `Transform(author_info, author_large)` |
| 60.3s | 关注提示 | `FadeIn(follow_text)` |
| 61.5s | 装饰符号旋转 | `Rotate(decorations)` |
| 63.0s | 等待 | `Wait(1.5)` |
| 64.5s | 全部淡出 | `FadeOut(VGroup(*))` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留，最后放大 |
| vieta_formulas | Scene 2 | Scene 7 | 作为参考保留 |
| example_equations | Scene 4/5/6 | Scene 4/5/6 | 每个场景独立 |
| summary_content | Scene 7 | Scene 7 | 总结内容 |

---

## 技术要点

### 1. 公式分组与高亮
```python
formula = MathTex(
    r"x_1", r"+", r"x_2", r"=", r"-", r"\frac{b}{a}"
)
formula[0].set_color(COLOR_ROOT_1)  # x₁
formula[2].set_color(COLOR_ROOT_2)  # x₂
formula[5].set_color(COLOR_SUM)     # 结果
```

### 2. 系数标注
```python
equation = MathTex(r"x^2", r"-", r"7x", r"+", r"12", r"=", r"0")

# 使用 Brace 标注
brace_b = Brace(equation[2], DOWN)
label_b = MathTex(r"b=-7").next_to(brace_b, DOWN)
```

### 3. 推导动画
```python
step1 = MathTex(r"x_1 + x_2 = \frac{-b+\sqrt{\Delta}}{2a} + \frac{-b-\sqrt{\Delta}}{2a}")
step2 = MathTex(r"x_1 + x_2 = \frac{-2b}{2a}")
step3 = MathTex(r"x_1 + x_2 = \frac{-b}{a}")

self.play(Write(step1))
self.play(TransformMatchingTex(step1, step2))
self.play(TransformMatchingTex(step2, step3))
```

### 4. 答案框
```python
answer = MathTex(r"x_1 + x_2 = 7")
answer_box = SurroundingRectangle(answer, color=YELLOW, buff=0.2)
self.play(Create(answer_box))
```

---

## 验证清单

### 数学正确性
- [ ] 韦达定理公式正确
- [ ] 例题计算准确
- [ ] 对称式恒等式正确

### LaTeX 正确性
- [ ] 无中文字符在 MathTex 中
- [ ] 分数使用 \frac{}{}
- [ ] 下标使用 _{}

### 视觉效果
- [ ] 颜色区分清晰（两根、和、积）
- [ ] 公式不溢出边界
- [ ] 推导步骤流畅

### 节奏控制
- [ ] 每个例题时长均衡（~10秒）
- [ ] 关键步骤有足够停留
- [ ] 总时长65-80秒

---

## 边界参考 (TikTok竖屏)
```
┌─────────────────────────────┐  y = +8
│  顶部：作者信息 + 参考公式    │  y = +7 ~ +6.5
├─────────────────────────────┤  y = +5.5
│                             │
│  主内容区域：                │  y ∈ [-4, +5]
│  - 公式展示（y ∈ [+2, +5]）  │
│  - 推导过程（y ∈ [-2, +2]）  │
│  - 例题计算（y ∈ [-3, +3]）  │
│                             │
├─────────────────────────────┤  y = -4
│  底部：结论、答案            │  y ∈ [-6, -4]
├─────────────────────────────┤  y = -6
│  底部安全区                  │  y = -8
└─────────────────────────────┘

横向: x ∈ [-4, +4] (安全区域)
```

---

## 特殊注意事项

### 1. 韦达定理的符号
- 注意 x₁ + x₂ = **-b/a** （负号）
- 注意分母是 **a**（二次项系数）

### 2. 对称式计算
- x₁² + x₂² = (x₁+x₂)² - 2x₁x₂
- x₁³ + x₂³ = (x₁+x₂)³ - 3x₁x₂(x₁+x₂)
- 1/x₁ + 1/x₂ = (x₁+x₂)/(x₁x₂)

### 3. 构造方程技巧
- 由 x₁ + x₂ 和 x₁x₂ 可构造：x² - (x₁+x₂)x + x₁x₂ = 0

---

## 动画节奏指南

| 内容类型 | 建议时长 |
|---------|---------|
| 公式展示 | 0.6-1.0s |
| 推导步骤 | 1.0-1.5s |
| 例题讲解 | 8-10s |
| 关键结果高亮 | 0.5-0.8s |
| 理解停顿 | 1.0-1.5s |