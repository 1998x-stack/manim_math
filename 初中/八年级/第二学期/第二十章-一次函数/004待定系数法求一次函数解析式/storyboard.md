# 待定系数法求一次函数解析式 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 6 个
- 难度等级: 中等（八年级）
- 主题: 待定系数法求一次函数解析式

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主函数线
COLOR_SECONDARY = "#e74c3c"    # 红色 - 重点标注
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助元素
COLOR_POINT_A = "#2ecc71"      # 绿色 - 点A
COLOR_POINT_B = "#9b59b6"      # 紫色 - 点B
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 点A | 给定坐标 (1, 3) | self.point_A |
| 点B | 给定坐标 (3, 7) | self.point_B |
| 坐标系 | x∈[-1,5], y∈[-1,9] | self.axes |
| 函数线 | k=2, b=1 → y=2x+1 | self.line |
| 截距点 | (0, 1) | self.intercept |

## 核心数学内容
**已知**: 直线经过两点 A(1, 3) 和 B(3, 7)
**求**: 一次函数解析式

**解题步骤**:
1. 设 y = kx + b
2. 代入点A: 3 = k(1) + b → k + b = 3
3. 代入点B: 7 = k(3) + b → 3k + b = 7
4. 解方程组: k = 2, b = 1
5. 得到解析式: y = 2x + 1

---

## Scene 1: 开场钩子 (4秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题文字
3. 两个神秘的点闪烁

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 标题书写 | `Write(title)` |
| 1.0s | 问题文字淡入 | `FadeIn(question_text, shift=UP*0.3)` |
| 1.5s | 点A闪烁出现 | `Flash(dot_A) + FadeIn(dot_A)` |
| 2.0s | 点B闪烁出现 | `Flash(dot_B) + FadeIn(dot_B)` |
| 2.5s | 疑问: "能画出这条直线吗?" | `FadeIn(hint)` |
| 3.5s | 等待 | `Wait(0.5)` |

### 文字内容
- 标题: "两点确定一条直线"
- 问题: "知道两个点的坐标"
- 提示: "能求出函数解析式吗?"

### 清理
- FadeOut: title, question_text, hint
- 保留: author_info, dot_A, dot_B (变半透明)

---

## Scene 2: 建立坐标系并标注点 (6秒)
**目的**: 展示具体数据，建立视觉基础

### 元素
1. 坐标系 (x∈[-1,5], y∈[-1,9])
2. 点A(1, 3) 完整标注
3. 点B(3, 7) 完整标注
4. 坐标标签

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 坐标系创建 | `Create(axes)` |
| 1.0s | 点A移动到正确位置 | `dot_A.animate.move_to(axes.c2p(1, 3))` |
| 1.5s | 点A坐标标签出现 | `FadeIn(label_A)` |
| 2.0s | 点B移动到正确位置 | `dot_B.animate.move_to(axes.c2p(3, 7))` |
| 2.5s | 点B坐标标签出现 | `FadeIn(label_B)` |
| 3.0s | 说明文字 | `FadeIn(explain)` |
| 5.0s | 等待理解 | `Wait(1.0)` |

### 文字内容
- 点A标签: "A(1, 3)"
- 点B标签: "B(3, 7)"
- 说明: "已知两点坐标"

### 清理
- FadeOut: explain
- 保留: axes, dot_A, dot_B, label_A, label_B

---

## Scene 3: 引入待定系数法 (8秒)
**目的**: 介绍方法核心思想

### 元素
1. 方法名称标题
2. 核心公式 y = kx + b
3. 说明文字
4. k, b 的标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 方法标题出现 | `Write(method_title)` |
| 1.0s | 公式书写 | `Write(formula_general)` |
| 2.0s | k 高亮 | `formula_general[k_part].animate.set_color(YELLOW)` |
| 2.5s | k 说明 | `FadeIn(k_explain)` |
| 3.5s | k 恢复颜色 | `formula_general[k_part].animate.set_color(WHITE)` |
| 4.0s | b 高亮 | `formula_general[b_part].animate.set_color(YELLOW)` |
| 4.5s | b 说明 | `FadeIn(b_explain)` |
| 5.5s | b 恢复颜色 | `formula_general[b_part].animate.set_color(WHITE)` |
| 6.0s | 核心思想 | `FadeIn(core_idea)` |
| 7.5s | 等待 | `Wait(0.5)` |

### 文字内容
- 方法标题: "待定系数法"
- 公式: y = kx + b
- k说明: "斜率(待定)"
- b说明: "截距(待定)"
- 核心: "代入已知点求出k和b"

### 清理
- FadeOut: method_title, k_explain, b_explain, core_idea
- 保留: formula_general (移到顶部缩小)

---

## Scene 4: 代入点A建立方程 (7秒)
**目的**: 演示第一个方程的建立

### 元素
1. 点A闪烁
2. 代入过程动画
3. 第一个方程

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 提示文字 | `FadeIn(hint_step1)` |
| 0.5s | 点A放大脉冲 | `dot_A.animate.scale(1.5) + Flash(dot_A)` |
| 1.0s | 点A恢复 | `dot_A.animate.scale(1/1.5)` |
| 1.5s | 代入公式出现 | `Write(substitute_A)` |
| 2.5s | 化简箭头 | `FadeIn(arrow_1)` |
| 3.0s | 方程1出现 | `Write(equation_1)` |
| 4.0s | 方程1移动到左侧 | `equation_1.animate.move_to(...)` |
| 5.5s | 等待 | `Wait(1.5)` |

### 文字内容
- 提示: "代入点A(1, 3)"
- 代入: "3 = k(1) + b"
- 方程1: "k + b = 3"

### 清理
- FadeOut: hint_step1, substitute_A, arrow_1
- 保留: equation_1 (在左侧), dot_A高亮状态

---

## Scene 5: 代入点B建立方程 (7秒)
**目的**: 演示第二个方程的建立

### 元素
1. 点B闪烁
2. 代入过程动画
3. 第二个方程
4. 方程组框架

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 提示文字 | `FadeIn(hint_step2)` |
| 0.5s | 点B放大脉冲 | `dot_B.animate.scale(1.5) + Flash(dot_B)` |
| 1.0s | 点B恢复 | `dot_B.animate.scale(1/1.5)` |
| 1.5s | 代入公式出现 | `Write(substitute_B)` |
| 2.5s | 化简箭头 | `FadeIn(arrow_2)` |
| 3.0s | 方程2出现 | `Write(equation_2)` |
| 4.0s | 方程2移动到左侧 | `equation_2.animate.move_to(...)` |
| 4.5s | 大括号出现 | `Create(brace)` |
| 5.0s | "方程组"标注 | `FadeIn(system_label)` |
| 6.5s | 等待 | `Wait(0.5)` |

### 文字内容
- 提示: "代入点B(3, 7)"
- 代入: "7 = k(3) + b"
- 方程2: "3k + b = 7"
- 标注: "二元一次方程组"

### 清理
- FadeOut: hint_step2, substitute_B, arrow_2
- 保留: equation_1, equation_2, brace, system_label

---

## Scene 6: 解方程组并绘制函数 (10秒)
**目的**: 展示求解过程和最终结果

### 元素
1. 方程组求解动画
2. k = 2, b = 1 结果
3. 函数线绘制
4. 最终解析式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 提示"相减消元" | `FadeIn(solve_hint)` |
| 0.5s | 方程相减动画 | `TransformMatchingTex(...)` |
| 1.5s | 得到 2k = 4 | `Write(result_k_calc)` |
| 2.5s | k = 2 出现 | `Write(result_k)` |
| 3.0s | k = 2 高亮 | `result_k.animate.set_color(YELLOW)` |
| 3.5s | 代入求b | `Write(calc_b)` |
| 4.5s | b = 1 出现 | `Write(result_b)` |
| 5.0s | b = 1 高亮 | `result_b.animate.set_color(YELLOW)` |
| 5.5s | 最终公式出现 | `Write(final_formula)` |
| 6.5s | 函数线绘制 | `Create(function_line)` |
| 8.0s | 验证: 线过A和B | `Flash(dot_A) + Flash(dot_B)` |
| 9.5s | 等待 | `Wait(0.5)` |

### 文字内容
- 提示: "方程②-方程①"
- 计算: "2k = 4"
- 结果k: "k = 2"
- 计算b: "2 + b = 3"
- 结果b: "b = 1"
- 最终: "y = 2x + 1"

### 清理
- FadeOut: 方程组, 中间计算步骤
- 保留: final_formula, function_line, axes, 点A和B

---

## Scene 7: 总结和关注 (8秒)
**目的**: 总结要点，引导关注

### 元素
1. 总结卡片
2. 关键步骤列表
3. 作者信息
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清空坐标系 | `FadeOut(axes, dots, labels)` |
| 0.5s | 总结标题 | `Write(summary_title)` |
| 1.0s | 步骤1滑入 | `step1.animate.shift(RIGHT*10)` |
| 1.5s | 步骤2滑入 | `step2.animate.shift(RIGHT*10)` |
| 2.0s | 步骤3滑入 | `step3.animate.shift(RIGHT*10)` |
| 2.5s | 步骤4滑入 | `step4.animate.shift(RIGHT*10)` |
| 3.0s | 最终公式放大 | `final_formula.animate.scale(1.3).move_to(DOWN*2)` |
| 4.0s | 作者信息放大 | `author_info.animate.scale(2).move_to(UP*2)` |
| 5.0s | 关注提示 | `FadeIn(follow_hint)` |
| 6.0s | 装饰动画 | `Rotate(decorations)` |
| 7.5s | 等待 | `Wait(0.5)` |

### 文字内容
- 总结标题: "待定系数法四步骤"
- 步骤1: "① 设 y = kx + b"
- 步骤2: "② 代入两点坐标"
- 步骤3: "③ 建立方程组"
- 步骤4: "④ 求解k和b"
- 关注: "关注我，学更多数学技巧!"

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | - | 始终保留 |
| axes | Scene 2 | Scene 7 | 主坐标系 |
| dot_A | Scene 1 | Scene 7 | 点A |
| dot_B | Scene 1 | Scene 7 | 点B |
| formula_general | Scene 3 | Scene 6 | y=kx+b |
| equation_1 | Scene 4 | Scene 6 | 第一个方程 |
| equation_2 | Scene 5 | Scene 6 | 第二个方程 |
| function_line | Scene 6 | Scene 7 | 最终函数线 |
| final_formula | Scene 6 | - | 最终公式保留 |

---

## 关键技术要点

### 坐标精度
- 所有点通过 `axes.c2p(x, y)` 转换
- 函数线使用 `axes.plot(lambda x: 2*x + 1, x_range=[0, 4])`

### 公式分组
- 使用 `{{ }}` 隔离k和b便于高亮
- 例: `MathTex(r"y = {{ k }}x + {{ b }}")`

### 动画节奏
- 简单动画: 0.5-0.8秒
- 公式书写: 0.8-1.2秒
- 理解停顿: 1.0-2.0秒

### 边界控制
- 主内容区: y ∈ [-3, +5]
- 底部文字区: y ∈ [-6, -3]
- 顶部作者: y = +7

### 颜色一致性
- 点A始终用绿色
- 点B始终用紫色
- 函数线用蓝色
- 高亮用黄色