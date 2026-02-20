# 直接开平方法 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 初中基础
- 知识点: 一元二次方程的直接开平方法

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主公式
COLOR_SECONDARY = "#e74c3c"      # 红色 - 关键步骤
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_SUCCESS = "#2ecc71"        # 绿色 - 正确答案
COLOR_BACKGROUND = "#1a1a2e"     # 深蓝背景
```

## 几何预计算清单
本动画主要涉及公式和符号，无复杂几何图形。
主要元素为 MathTex 和 Text。

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题: "x² = 9，x等于多少？"
3. 思考气泡动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入顶部 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_question, run_time=0.8)` |
| 1.1s | 思考气泡出现 | `FadeIn(thinking_bubble, scale=0.5)` |
| 2.0s | 问号闪烁 | `Flash(question_mark)` |
| 2.5s | 等待 | `self.wait(0.5)` |

### 清理
- FadeOut: hook_question, thinking_bubble
- 保留: author_info

---

## Scene 2: 引入方法名称 (5-10秒)
**目的**: 介绍"直接开平方法"

### 元素
1. 方法标题: "直接开平方法"
2. 副标题: "Direct Square Root Method"
3. 简短说明文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title, run_time=1.0)` |
| 1.0s | 副标题淡入 | `FadeIn(subtitle)` |
| 1.5s | 说明文字出现 | `FadeIn(description, shift=UP*0.3)` |
| 3.0s | 等待理解 | `self.wait(1.0)` |

### 清理
- FadeOut: title, subtitle, description
- 保留: author_info

---

## Scene 3: 基本公式推导 (10-25秒)
**目的**: 讲解最基础形式 x² = n

### 元素
1. 起始公式: x² = 9
2. 推导步骤: 
   - 两边开平方
   - x = ±√9
   - x = ±3
3. 强调符号 ±

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 写出 x² = 9 | `Write(eq1)` |
| 1.0s | 箭头指示"开平方" | `GrowArrow(arrow1)` |
| 1.5s | 提示文字"两边开平方" | `FadeIn(hint1)` |
| 2.5s | 变换到 x = ±√9 | `TransformMatchingTex(eq1, eq2)` |
| 3.5s | 高亮 ± 符号 | `Indicate(plus_minus_sign)` |
| 4.5s | 解释框: "正负两个解" | `FadeIn(explanation_box)` |
| 6.0s | 变换到 x = ±3 | `TransformMatchingTex(eq2, eq3)` |
| 7.0s | 答案框高亮 | `SurroundingRectangle(eq3, color=GREEN)` |
| 8.5s | 等待 | `self.wait(1.5)` |

### 清理
- FadeOut: 所有公式、箭头、提示
- 保留: author_info

---

## Scene 4: 通用公式展示 (25-35秒)
**目的**: 展示通用形式 (x+m)² = n

### 元素
1. 通用公式框
2. 公式: (x+m)² = n ⟹ x = -m ± √n
3. 条件说明: n ≥ 0

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 公式框创建 | `Create(formula_box)` |
| 0.8s | 通用公式书写 | `Write(general_formula)` |
| 2.0s | 双箭头展开 | `GrowArrow(double_arrow)` |
| 3.0s | 解的形式出现 | `Write(solution_form)` |
| 4.5s | 条件框出现 | `FadeIn(condition_box)` |
| 5.5s | 条件说明 n≥0 | `Write(condition_text)` |
| 7.0s | 整体框闪烁强调 | `Flash(VGroup(formula_box, general_formula))` |
| 8.0s | 等待 | `self.wait(1.5)` |

### 清理
- FadeOut: formula_box, condition_box
- 保留: author_info

---

## Scene 5: 实例演示1 - 简单配方 (35-48秒)
**目的**: 演示 (x+2)² = 16 的求解

### 元素
1. 例题: (x+2)² = 16
2. 求解步骤展示
3. 最终答案: x₁ = 2, x₂ = -6

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 例题标签 | `Write(example_label)` |
| 0.5s | 写出问题 | `Write(problem)` |
| 1.5s | 步骤1: 开平方 | `TransformMatchingTex(step1, step2)` |
| 2.5s | 出现 x+2 = ±4 | `Write(step2)` |
| 3.5s | 步骤2: 移项 | `TransformMatchingTex(step2, step3)` |
| 4.5s | 出现 x = -2 ± 4 | `Write(step3)` |
| 5.5s | 分离两解 | `TransformMatchingTex(step3, step4)` |
| 7.0s | x₁=2, x₂=-6 出现 | `Write(solutions)` |
| 8.5s | 答案框高亮 | `SurroundingRectangle(solutions, color=GREEN)` |
| 10.0s | 等待 | `self.wait(1.5)` |

### 清理
- FadeOut: 所有步骤元素
- 保留: author_info

---

## Scene 6: 实例演示2 - 需要配方 (48-60秒)
**目的**: 演示 x² + 6x + 9 = 25 → (x+3)² = 25

### 元素
1. 原始方程: x² + 6x + 9 = 25
2. 识别完全平方: (x+3)²
3. 求解过程
4. 最终答案: x₁ = 2, x₂ = -8

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 例题2标签 | `Write(example2_label)` |
| 0.5s | 写出原方程 | `Write(original_eq)` |
| 1.5s | 高亮左侧 x²+6x+9 | `Indicate(left_side)` |
| 2.5s | 提示"完全平方式" | `FadeIn(hint_perfect_square)` |
| 3.5s | 变换为 (x+3)² | `TransformMatchingTex(original, transformed)` |
| 4.5s | 开平方 x+3 = ±5 | `Write(sqrt_step)` |
| 5.5s | 移项 x = -3 ± 5 | `Write(solve_step)` |
| 6.5s | 分离答案 | `Write(final_answers)` |
| 8.0s | 答案高亮 | `SurroundingRectangle(final_answers, GREEN)` |
| 9.5s | 等待 | `self.wait(1.0)` |

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 7: 总结与关注 (60-75秒)
**目的**: 总结方法要点，引导关注

### 元素
1. 关键要点总结（3条）
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 总结标题出现 | `Write(summary_title)` |
| 1.0s | 要点1滑入 | `FadeIn(point1, shift=RIGHT)` |
| 2.0s | 要点2滑入 | `FadeIn(point2, shift=RIGHT)` |
| 3.0s | 要点3滑入 | `FadeIn(point3, shift=RIGHT)` |
| 5.0s | 要点闪烁 | `Flash(all_points)` |
| 6.0s | 作者信息放大 | `Transform(author_info, author_large)` |
| 7.5s | 关注文字出现 | `FadeIn(follow_text, scale=1.1)` |
| 9.0s | 装饰元素旋转 | `Rotate(decorations)` |
| 12.0s | 全部淡出 | `FadeOut(all_elements)` |

### 清理
- FadeOut: 全部

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保持顶部 |
| hook_question | Scene 1 | Scene 1 | 钩子问题 |
| title | Scene 2 | Scene 2 | 方法名称 |
| eq1, eq2, eq3 | Scene 3 | Scene 3 | 基础推导 |
| general_formula | Scene 4 | Scene 4 | 通用公式 |
| example1 | Scene 5 | Scene 5 | 例题1 |
| example2 | Scene 6 | Scene 6 | 例题2 |
| summary | Scene 7 | Scene 7 | 总结要点 |

---

## 特殊注意事项

### LaTeX 使用规范
- ✅ 使用 `r"..."` 原始字符串
- ✅ 中文用 `Text()` 而非 `MathTex()`
- ✅ 度数符号用 `^\circ` 而非 `°`
- ✅ ± 符号用 `\pm` 
- ✅ 根号用 `\sqrt{}`
- ✅ 下标用 `_{1}`, `_{2}`

### 边界约束
- y ∈ [-7, 7]：主内容区域 [-5, 5]
- x ∈ [-4, 4]：安全宽度
- 顶部 y=7：作者信息固定
- 底部 y∈[-6, -5]：说明文字区域

### 字体大小
- 标题: 36-40
- 公式: 28-32
- 说明: 20-24
- 作者: 20

### 动画节奏
- 公式书写: 0.8-1.2s
- 变换动画: 1.0-1.5s
- 理解停顿: 1.0-2.0s
- 快速提示: 0.3-0.5s