# 分数与小数的互化 - 动画分镜脚本

## 元信息
- 目标时长: 75-90 秒
- 场景数量: 7 个
- 难度等级: 六年级
- 主题: 分数与小数互化、有限小数判定

## 颜色配置
```python
COLOR_FRACTION = "#3498db"      # 蓝色 - 分数
COLOR_DECIMAL = "#e74c3c"       # 红色 - 小数
COLOR_DIVISION = "#2ecc71"      # 绿色 - 除法过程
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线
COLOR_PRIME = "#9b59b6"         # 紫色 - 素因数
COLOR_ARROW = "#f39c12"         # 橙色 - 箭头
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 数轴原点 | np.array([0, 0, 0]) | self.ORIGIN_POS |
| 数轴长度 | 6.0 | self.NUMBERLINE_LENGTH |
| 分数位置 | UP * 2.5 | self.FRACTION_POS |
| 小数位置 | UP * 2.5 | self.DECIMAL_POS |
| 除法演示区 | UP * 1.0 | self.DIVISION_AREA |
| 公式区域 | DOWN * 2.0 | self.FORMULA_AREA |

---

## Scene 1: 开场钩子 (4-5秒)
**目的**: 抓住注意力，引出主题

### 元素
1. 作者标识 (顶部小字) - y=7
2. 钩子问题大字 - y=5
3. 分数和小数的对比符号 - y=2

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=1.2)` |
| 1.5s | 分数 3/4 淡入左侧 | `FadeIn(fraction, shift=RIGHT*0.5)` |
| 2.0s | 问号闪烁 | `Flash(question_mark)` |
| 2.5s | 小数 0.75 淡入右侧 | `FadeIn(decimal, shift=LEFT*0.5)` |
| 3.5s | 等待理解 | `Wait(1.0)` |

### 坐标计算
```python
author_info.move_to(UP * 7)
hook_text.move_to(UP * 5)
fraction.move_to(LEFT * 2.5 + UP * 2.5)
question_mark.move_to(UP * 2.5)
decimal.move_to(RIGHT * 2.5 + UP * 2.5)
```

### 清理
- FadeOut: hook_text, question_mark
- 保留: author_info, fraction, decimal (作为transition)

---

## Scene 2: 分数化小数 - 基本原理 (10-12秒)
**目的**: 展示分数转小数的核心规则

### 元素
1. 标题: "分数 → 小数" - y=5.5
2. 核心规则文字 - y=4.5
3. 示例: 3/4 = 3÷4 - y=2
4. 长除法演示区域 - y=0到-2

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title)` |
| 0.8s | 规则文字显示 | `FadeIn(rule_text)` |
| 1.5s | 分数移动到中心 | `fraction.animate.move_to(UP*2)` |
| 2.0s | 箭头指向除法 | `GrowArrow(arrow)` |
| 2.5s | 除法式子书写 | `Write(division_expr)` |
| 3.0s | 长除法框架创建 | `Create(division_box)` |
| 3.5s | 除法步骤1: 3÷4 | `TransformMatchingTex` |
| 4.5s | 除法步骤2: 30÷4=7余2 | `TransformMatchingTex` |
| 5.5s | 除法步骤3: 20÷4=5 | `TransformMatchingTex` |
| 6.5s | 结果0.75闪烁 | `Flash(result)` |
| 7.5s | 等待 | `Wait(1.5)` |

### 坐标计算
```python
title.move_to(UP * 5.5)
rule_text.move_to(UP * 4.5)
division_box_top = UP * 1.5
division_steps = [UP * 1.0, UP * 0.5, ORIGIN, DOWN * 0.5]
```

### 清理
- FadeOut: title, rule_text, division_box, division_steps
- Transform: result → 保留为小数示例

---

## Scene 3: 小数化分数 - 位数定分母 (10-12秒)
**目的**: 展示小数转分数的方法

### 元素
1. 标题: "小数 → 分数" - y=5.5
2. 核心规则: "小数位数决定分母" - y=4.5
3. 示例: 0.125 - y=2
4. 分步演示区 - y=0

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title)` |
| 0.8s | 示例0.125显示 | `Write(decimal_example)` |
| 1.5s | 标注小数位数 | `FadeIn(digit_marks)` |
| 2.0s | 说明文字: "3位小数" | `FadeIn(explanation)` |
| 2.8s | 箭头指向分数 | `GrowArrow(arrow)` |
| 3.3s | 分母1000出现 | `Write(denominator)` |
| 4.0s | 分子125出现 | `Write(numerator)` |
| 4.5s | 分数线创建 | `Create(fraction_line)` |
| 5.0s | 完整分数 125/1000 | `VGroup组合` |
| 5.8s | 约分提示 | `FadeIn(simplify_hint)` |
| 6.5s | 约分过程: ÷125 | `Transform动画` |
| 7.5s | 最简分数 1/8 闪烁 | `Flash(final_fraction)` |
| 8.5s | 等待 | `Wait(1.0)` |

### 坐标计算
```python
title.move_to(UP * 5.5)
decimal_example.move_to(UP * 2)
digit_marks = VGroup(*[Dot().move_to(decimal_example.get_center() + RIGHT*(0.3*i) + DOWN*0.3) for i in range(3)])
fraction_center = ORIGIN
```

### 清理
- FadeOut: title, digit_marks, explanation, simplify_hint, intermediate steps
- 保留: final_fraction (1/8)

---

## Scene 4: 数轴可视化对比 (8-10秒)
**目的**: 直观展示分数和小数在数轴上的等价性

### 元素
1. 标题: "在数轴上是同一个点!" - y=5
2. 数轴 (0到1) - y=0
3. 分数标记点 - y=0
4. 小数标记点 - y=0

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 数轴创建 | `Create(numberline)` |
| 1.2s | 0和1标记 | `FadeIn(labels)` |
| 2.0s | 3/4从上方降落 | `fraction.animate.move_to(position)` |
| 2.8s | 标记点A闪烁 | `Flash(dot_A)` |
| 3.5s | 0.75从下方升起 | `decimal.animate.move_to(position)` |
| 4.3s | 重合闪烁效果 | `Flash(overlap_indicator)` |
| 5.0s | 连线到同一点 | `Create(connecting_lines)` |
| 6.0s | 等号强调 | `Write(equal_sign)` |
| 7.0s | 等待 | `Wait(1.0)` |

### 坐标计算
```python
numberline_center = ORIGIN
numberline = NumberLine(x_range=[0, 1, 0.25], length=6, include_numbers=True)
fraction_start = UP * 3
decimal_start = DOWN * 3
target_position = numberline.n2p(0.75)  # 3/4 = 0.75的位置
```

### 清理
- FadeOut: title, numberline, connecting_lines, equal_sign
- 移除数轴场景所有元素

---

## Scene 5: 有限小数判定法则 (12-15秒)
**目的**: 教授判断最简分数能否化为有限小数的方法

### 元素
1. 大标题: "如何判断能否化为有限小数?" - y=6
2. 法则文字 - y=4.5
3. 素因数分解示例 - y=2到-2
4. 判定表格 - y=-3到-5

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 问题标题书写 | `Write(question_title)` |
| 1.0s | 法则卡片滑入 | `card.animate.shift(RIGHT*0)` |
| 2.0s | 示例1: 3/4 | `FadeIn(example_1)` |
| 2.5s | 分母4分解: 2² | `Write(factorization_1)` |
| 3.5s | 只含2 → 有限小数 | `FadeIn(conclusion_1, color=GREEN)` |
| 4.5s | 示例2: 1/8 | `FadeIn(example_2)` |
| 5.0s | 分母8分解: 2³ | `Write(factorization_2)` |
| 6.0s | 只含2 → 有限小数 | `FadeIn(conclusion_2, color=GREEN)` |
| 7.0s | 示例3: 1/6 | `FadeIn(example_3)` |
| 7.5s | 分母6分解: 2×3 | `Write(factorization_3)` |
| 8.5s | 含3 → 无限小数 | `FadeIn(conclusion_3, color=RED)` |
| 9.5s | 关键公式高亮 | `Flash(formula_box)` |
| 10.5s | 等待 | `Wait(1.5)` |

### 坐标计算
```python
question_title.move_to(UP * 6)
rule_card.move_to(UP * 4.5)
examples_group = VGroup().arrange(DOWN, buff=0.8).move_to(UP * 0.5)
formula_box.move_to(DOWN * 4)
```

### 清理
- FadeOut: question_title, examples, factorizations
- 保留: rule_card (缩小并移到角落作为reminder)

---

## Scene 6: 互动练习题 (10-12秒)
**目的**: 巩固学习，让学生思考

### 元素
1. 练习标题 - y=6
2. 题目: 判断 2/5 能否化为有限小数 - y=4
3. 思考时间倒计时 - y=2
4. 分步解答 - y=0到-3

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 练习标题淡入 | `FadeIn(practice_title)` |
| 0.5s | 题目显示 | `Write(problem)` |
| 1.5s | 倒计时3秒 | `DecimalNumber倒计时` |
| 4.5s | 倒计时结束 | `FadeOut(countdown)` |
| 5.0s | 解答步骤1: 分母5 | `FadeIn(step_1)` |
| 6.0s | 解答步骤2: 5=5¹ | `Write(step_2)` |
| 7.0s | 解答步骤3: 只含5 | `FadeIn(step_3, color=GREEN)` |
| 8.0s | 结论: 能! | `Flash(conclusion)` |
| 8.5s | 验证: 2÷5=0.4 | `Write(verification)` |
| 9.5s | 等待 | `Wait(1.0)` |

### 坐标计算
```python
practice_title.move_to(UP * 6)
problem.move_to(UP * 4)
countdown.move_to(UP * 2)
solution_steps = VGroup().arrange(DOWN, buff=0.5).move_to(ORIGIN)
```

### 清理
- FadeOut: 全部练习元素

---

## Scene 7: 总结 + 片尾 (8-10秒)
**目的**: 总结知识点，引导关注

### 元素
1. 总结标题 - y=6
2. 知识点卡片×3 - y=3, 1, -1
3. 作者信息放大 - y=0
4. 关注提示 - y=-3
5. 装饰动画元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 总结标题书写 | `Write(summary_title)` |
| 1.0s | 卡片1滑入: 分数→小数 | `card_1.animate.shift(RIGHT*0)` |
| 1.5s | 卡片2滑入: 小数→分数 | `card_2.animate.shift(RIGHT*0)` |
| 2.0s | 卡片3滑入: 有限小数判定 | `card_3.animate.shift(RIGHT*0)` |
| 3.0s | 作者信息放大 | `Transform(author_info, large_author)` |
| 4.0s | 关注提示淡入 | `FadeIn(follow_text, shift=UP*0.3)` |
| 5.0s | 装饰圆圈旋转 | `Rotate(circles, angle=PI)` |
| 6.5s | 全部保持 | `Wait(1.5)` |

### 坐标计算
```python
summary_title.move_to(UP * 6)
cards = VGroup().arrange(DOWN, buff=1.2).move_to(UP * 1.5)
author_large.move_to(DOWN * 1.5)
follow_text.move_to(DOWN * 3.5)
```

### 清理
- 淡出所有元素 (在最后1秒)

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 贯穿全程，最后放大 |
| fraction_example | Scene 1 | Scene 4 | 3/4示例 |
| decimal_example | Scene 1 | Scene 4 | 0.75示例 |
| division_box | Scene 2 | Scene 2 | 临时除法演示 |
| numberline | Scene 4 | Scene 4 | 临时数轴 |
| rule_card | Scene 5 | Scene 6 | 法则卡片 |
| practice_elements | Scene 6 | Scene 6 | 练习题专用 |
| summary_cards | Scene 7 | Scene 7 | 总结卡片 |

---

## 技术注意事项

### 字体使用
- 中文: `Text(..., font="Noto Sans CJK SC")`
- 数学公式: `MathTex(r"...")`
- 避免在MathTex中使用中文

### 动画时长控制
- 简单元素创建: 0.5-0.8s
- 复杂公式书写: 1.0-1.5s
- 重要概念停留: 1.5-2.5s
- 场景过渡: 0.4-0.6s

### 颜色使用原则
- 分数: 蓝色系 (冷色调)
- 小数: 红色系 (暖色调)
- 正确/成功: 绿色
- 错误/警告: 红色
- 高亮重点: 黄色

### 坐标边界检查
- 横向安全区: x ∈ [-4, 4]
- 纵向安全区: y ∈ [-7, 7]
- 顶部留白: y < 7.5 (作者信息区)
- 底部留白: y > -7.5

### 数学符号规范
- 分数线: `Line()`而非`-`
- 除号: `MathTex(r"\div")` 
- 等号: `MathTex(r"=")` 
- 度数: `MathTex(r"^\circ")` 而非 `°`
- 乘号: `MathTex(r"\times")` 

### 验证清单
- [ ] 所有中文使用Text而非MathTex
- [ ] 所有坐标在安全范围内
- [ ] 元素生命周期明确
- [ ] 动画时长合理
- [ ] 颜色符合主题
- [ ] 字体大小适配竖屏