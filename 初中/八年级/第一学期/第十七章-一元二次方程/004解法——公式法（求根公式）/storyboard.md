# 求根公式（公式法）- 动画分镜脚本

## 元信息
- 目标时长: 65-80 秒
- 场景数量: 7 个
- 难度等级: 初中进阶
- 知识点: 一元二次方程的求根公式（公式法）

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主公式
COLOR_SECONDARY = "#e74c3c"      # 红色 - 判别式
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助
COLOR_SUCCESS = "#2ecc71"        # 绿色 - 正确答案
COLOR_WARNING = "#f39c12"        # 橙色 - 警告/条件
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
2. 钩子问题: "2x² + 5x - 3 = 0"
3. 问号动画："怎么解？"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入顶部 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子方程书写 | `Write(hook_equation, run_time=1.0)` |
| 1.3s | 问号出现 | `FadeIn(question_mark, scale=0.5)` |
| 2.0s | 问号闪烁 | `Flash(question_mark)` |
| 2.5s | 等待 | `self.wait(0.5)` |

### 清理
- FadeOut: hook_equation, question_mark
- 保留: author_info

---

## Scene 2: 介绍求根公式 (5-15秒)
**目的**: 展示万能求根公式

### 元素
1. 方法标题: "求根公式（公式法）"
2. 标准形式: ax² + bx + c = 0
3. 求根公式框（核心）
4. 条件说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title, run_time=1.0)` |
| 1.0s | 标准形式出现 | `Write(standard_form)` |
| 2.0s | 公式框创建 | `Create(formula_box)` |
| 2.5s | 求根公式书写 | `Write(formula, run_time=1.5)` |
| 4.5s | 条件框出现 | `FadeIn(condition_box)` |
| 5.5s | 强调 a≠0 | `Indicate(condition_a)` |
| 6.5s | 公式闪烁强调 | `Flash(formula)` |
| 8.0s | 等待理解 | `self.wait(1.5)` |

### 清理
- FadeOut: title
- 保留: author_info, formula（缩小移到角落）

---

## Scene 3: 判别式详解 (15-25秒)
**目的**: 讲解 Δ = b²-4ac 的作用

### 元素
1. 判别式定义: Δ = b²-4ac
2. 三种情况框
3. 图示：Δ>0, Δ=0, Δ<0

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | "判别式"标题 | `Write(discriminant_title)` |
| 0.8s | Δ定义出现 | `Write(delta_definition)` |
| 1.5s | 高亮根号内部分 | `Indicate(sqrt_part)` |
| 2.5s | 情况1框：Δ>0 | `FadeIn(case1_box, shift=RIGHT)` |
| 3.5s | "两个不等实根" | `Write(case1_text)` |
| 4.5s | 情况2框：Δ=0 | `FadeIn(case2_box, shift=RIGHT)` |
| 5.5s | "两个相等实根" | `Write(case2_text)` |
| 6.5s | 情况3框：Δ<0 | `FadeIn(case3_box, shift=RIGHT)` |
| 7.5s | "无实数根" | `Write(case3_text)` |
| 8.5s | 整体闪烁 | `Flash(all_cases)` |
| 9.0s | 等待 | `self.wait(0.5)` |

### 清理
- FadeOut: 所有判别式元素
- 保留: author_info

---

## Scene 4: 公式拆解（步骤展示）(25-35秒)
**目的**: 展示使用公式的步骤

### 元素
1. 步骤卡片组
2. 步骤1: 确定 a, b, c
3. 步骤2: 计算判别式
4. 步骤3: 代入公式
5. 步骤4: 计算结果

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | "使用步骤"标题 | `Write(steps_title)` |
| 1.0s | 步骤1卡片滑入 | `FadeIn(step1, shift=RIGHT)` |
| 2.0s | 步骤2卡片滑入 | `FadeIn(step2, shift=RIGHT)` |
| 3.0s | 步骤3卡片滑入 | `FadeIn(step3, shift=RIGHT)` |
| 4.0s | 步骤4卡片滑入 | `FadeIn(step4, shift=RIGHT)` |
| 5.5s | 整体闪烁 | `Flash(all_steps)` |
| 7.0s | 等待 | `self.wait(1.5)` |

### 清理
- FadeOut: 所有步骤卡片
- 保留: author_info

---

## Scene 5: 实例演示1 - 简单系数 (35-48秒)
**目的**: 演示 x² + 5x + 6 = 0 的求解

### 元素
1. 例题标签
2. 原方程
3. 识别系数: a=1, b=5, c=6
4. 计算判别式: Δ=25-24=1
5. 代入公式
6. 最终答案: x₁=-2, x₂=-3

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 例题1标签 | `Write(example1_label)` |
| 0.5s | 写出方程 | `Write(equation)` |
| 1.5s | 识别系数 | `Write(coefficients)` |
| 2.5s | a=1 高亮 | `Indicate(a_value)` |
| 3.0s | b=5 高亮 | `Indicate(b_value)` |
| 3.5s | c=6 高亮 | `Indicate(c_value)` |
| 4.5s | 计算Δ标签 | `Write(delta_label)` |
| 5.0s | Δ计算过程 | `Write(delta_calc)` |
| 6.0s | Δ=1 出现 | `Write(delta_result)` |
| 7.0s | 代入公式 | `Write(substitution)` |
| 8.5s | 简化 | `Transform(substitution, simplified)` |
| 9.5s | 分离答案 | `Write(answers)` |
| 11.0s | 答案框高亮 | `SurroundingRectangle(answers, GREEN)` |
| 12.0s | 等待 | `self.wait(0.5)` |

### 清理
- FadeOut: 所有例题1元素
- 保留: author_info

---

## Scene 6: 实例演示2 - 一般系数 (48-60秒)
**目的**: 演示 2x² + 5x - 3 = 0 的求解

### 元素
1. 例题2标签
2. 原方程
3. 识别系数: a=2, b=5, c=-3
4. 计算判别式: Δ=25+24=49
5. 代入公式
6. 最终答案: x₁=½, x₂=-3

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 例题2标签 | `Write(example2_label)` |
| 0.5s | 写出方程 | `Write(equation2)` |
| 1.5s | 识别系数 | `Write(coefficients2)` |
| 2.5s | 系数高亮 | `Indicate(all_coefficients)` |
| 3.5s | 计算Δ | `Write(delta_calc2)` |
| 4.5s | Δ=49 | `Write(delta_result2)` |
| 5.5s | 代入公式 | `Write(substitution2)` |
| 7.0s | 简化 | `Transform(substitution2, simplified2)` |
| 8.0s | 计算√49=7 | `Write(sqrt_step)` |
| 9.0s | 分离答案 | `Write(answers2)` |
| 10.5s | 答案框高亮 | `SurroundingRectangle(answers2, GREEN)` |
| 11.5s | 等待 | `self.wait(0.5)` |

### 清理
- FadeOut: 所有例题2元素
- 保留: author_info

---

## Scene 7: 总结与关注 (60-80秒)
**目的**: 总结公式法要点，引导关注

### 元素
1. 总结标题
2. 核心公式回顾
3. 使用要点（3条）
4. 作者信息放大
5. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 总结标题 | `Write(summary_title)` |
| 1.0s | 公式回顾 | `Write(formula_recap)` |
| 2.5s | 要点1滑入 | `FadeIn(point1, shift=RIGHT)` |
| 3.5s | 要点2滑入 | `FadeIn(point2, shift=RIGHT)` |
| 4.5s | 要点3滑入 | `FadeIn(point3, shift=RIGHT)` |
| 6.0s | 整体闪烁 | `Flash(all_points)` |
| 7.0s | 作者信息放大 | `Transform(author_info, author_large)` |
| 8.5s | 关注文字 | `FadeIn(follow_text, scale=1.1)` |
| 10.0s | 装饰旋转 | `Rotate(decorations)` |
| 13.0s | 全部淡出 | `FadeOut(all_elements)` |

### 清理
- FadeOut: 全部

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保持顶部 |
| hook_equation | Scene 1 | Scene 1 | 钩子方程 |
| formula | Scene 2 | Scene 2 | 求根公式 |
| discriminant | Scene 3 | Scene 3 | 判别式讲解 |
| steps | Scene 4 | Scene 4 | 步骤展示 |
| example1 | Scene 5 | Scene 5 | 例题1 |
| example2 | Scene 6 | Scene 6 | 例题2 |
| summary | Scene 7 | Scene 7 | 总结要点 |

---

## 特殊注意事项

### LaTeX 使用规范
- ✅ 使用 `r"..."` 原始字符串
- ✅ 中文用 `Text()` 而非 `MathTex()`
- ✅ 分数用 `\frac{a}{b}`
- ✅ 根号用 `\sqrt{}`
- ✅ ± 符号用 `\pm`
- ✅ 判别式用 `\Delta` (大写Delta)
- ✅ 不等号用 `\neq`, `\geq`
- ✅ 下标用 `_{1}`, `_{2}`

### 边界约束
- y ∈ [-7, 7]：主内容区域 [-5, 5]
- x ∈ [-4, 4]：安全宽度
- 顶部 y=7：作者信息固定
- 底部 y∈[-6, -5]：说明文字区域

### 字体大小
- 标题: 36-40
- 公式: 28-32（核心公式可以32-36）
- 说明: 20-24
- 作者: 20
- 系数标注: 20-22

### 动画节奏
- 公式书写: 0.8-1.2s
- 变换动画: 1.0-1.5s
- 理解停顿: 1.0-2.0s
- 快速提示: 0.3-0.5s
- 核心公式: 额外停顿 2.0s

### 公式复杂度处理
- 求根公式较长，需要合适的字号
- 分子分母用 `\frac{}{}` 清晰展示
- 判别式单独高亮
- 代入数值时分步展示，避免信息过载

### 颜色使用策略
- 蓝色: 主要公式和方程
- 红色: 判别式（重要概念）
- 黄色: 关键步骤高亮
- 绿色: 最终答案
- 橙色: 条件和警告（a≠0等）