# 因式分解——提公因式法 - 动画分镜脚本

<!-- /root/code/sss/media/videos/common_factor_method/1920p60/CommonFactorMethod.mp4 -->
## 元信息
- 目标时长: 60-75秒
- 场景数量: 7个
- 难度等级: 中等
- 年级: 七年级
- 知识点: 提公因式法

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主公式
COLOR_SECONDARY = "#e74c3c"    # 红色 - 公因式高亮
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线/文字
COLOR_SUCCESS = "#2ecc71"      # 绿色 - 正确结果
COLOR_STEP = "#9b59b6"         # 紫色 - 步骤标记
```

## 几何预计算清单
本动画主要涉及数学公式而非几何图形，无需复杂几何计算。
主要元素：MathTex对象的位置管理

---

## Scene 1: 开场钩子 (0-4秒)
**目的**: 抓住注意力，提出问题

### 元素
1. 作者标识 (顶部小字) - y=7
2. 钩子问题 (大字) - y=5
3. 示例公式 - y=2

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_text, run_time=1.0)` |
| 1.3s | 示例公式创建 | `Write(example_formula, run_time=1.2)` |
| 2.5s | 问号闪烁 | `Flash(question_mark)` |
| 3.5s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_text, question_mark
- 保留: author_info, example_formula

---

## Scene 2: 概念引入 (4-10秒)
**目的**: 介绍什么是公因式

### 元素
1. 标题 "什么是公因式?" - y=5.5
2. 简单例子: 6x + 9x - y=2
3. 拆解展示 - y=0
4. 公因式标记 - y=-2

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 4.0s | 标题淡入 | `FadeIn(title)` |
| 4.5s | 示例公式变换 | `TransformMatchingTex(old, new)` |
| 5.5s | 展开为乘积形式 | `Write(factored_forms)` |
| 6.5s | 高亮公因式 | `Indicate(common_factor, color=RED)` |
| 7.5s | 说明文字出现 | `FadeIn(explanation)` |
| 8.5s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: title, explanation
- 保留: 当前公式（将在下场景变换）

---

## Scene 3: 提取步骤演示 (10-25秒)
**目的**: 详细演示提公因式的三个步骤

### 元素
1. 步骤标题 - y=6
2. 主公式 - y=2
3. 步骤说明 - y=-4
4. 箭头和标记

### 子步骤1: 找公因式 (10-14秒)
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 10.0s | 步骤1标题 | `Write(step1_title)` |
| 10.5s | 公式: 6x²y - 9xy² | `Write(formula)` |
| 11.5s | 系数框选 | `SurroundingRectangle(coeffs)` |
| 12.5s | 字母框选 | `SurroundingRectangle(vars)` |
| 13.5s | 公因式出现 | `Write(common_factor_result)` |

### 子步骤2: 提取公因式 (14-19秒)
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 14.0s | 步骤2标题 | `TransformMatchingTex(step1, step2)` |
| 14.5s | 公因式移出 | `公因式(...)形式` |
| 15.5s | 箭头动画 | `GrowArrow(arrow)` |
| 16.5s | 括号内商式 | `Write(quotient)` |
| 17.5s | 验证说明 | `FadeIn(verify_text)` |
| 18.5s | 等待 | `Wait(1.0)` |

### 子步骤3: 检验结果 (19-25秒)
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 19.0s | 步骤3标题 | `TransformMatchingTex(step2, step3)` |
| 19.5s | 展开验证 | `Write(expansion)` |
| 20.5s | 对比原式 | `Create(comparison_arrows)` |
| 21.5s | 打勾确认 | `DrawBorderThenFill(checkmark)` |
| 22.5s | 成功提示 | `FadeIn(success_text, scale=1.2)` |
| 24.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有步骤元素
- 为下一场景准备

---

## Scene 4: 口诀记忆 (25-32秒)
**目的**: 给出记忆口诀

### 元素
1. 口诀卡片 - 中央
2. 装饰图标

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 25.0s | 口诀卡片飞入 | `FadeIn(card, shift=DOWN, scale=0.8)` |
| 26.0s | 口诀1 | `Write(line1, run_time=0.8)` |
| 26.8s | 口诀2 | `Write(line2, run_time=0.8)` |
| 27.6s | 口诀3 | `Write(line3, run_time=0.8)` |
| 28.4s | 口诀4 | `Write(line4, run_time=0.8)` |
| 29.2s | 图标装饰 | `FadeIn(icons)` |
| 30.2s | 整体强调 | `Indicate(card, scale_factor=1.1)` |
| 31.2s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: card, icons

---

## Scene 5: 练习示例1 (32-42秒)
**目的**: 完整演示一个例题

### 元素
1. 例题标题 - y=6
2. 题目公式 - y=3
3. 解答过程 - y=0 到 y=-3
4. 步骤标记

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 32.0s | 例题标题 | `Write(title)` |
| 32.5s | 题目出现 | `Write(problem)` |
| 33.5s | 找公因式标记 | `SurroundingRectangle + label` |
| 34.5s | 提取动画 | `Transform到因式分解形式` |
| 35.5s | 箭头指示 | `GrowArrow` |
| 36.5s | 最终答案 | `Write(answer)` |
| 37.5s | 答案高亮 | `answer.animate.set_color(SUCCESS)` |
| 38.5s | 对号确认 | `DrawBorderThenFill(check)` |
| 39.5s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: 所有例题元素

---

## Scene 6: 练习示例2 (42-52秒)
**目的**: 第二个例题（稍复杂）

### 元素
1. 例题标题 - y=6
2. 题目公式 - y=3
3. 解答过程 - y=0 到 y=-3

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 42.0s | 例题2标题 | `Write(title)` |
| 42.5s | 题目出现 | `Write(problem)` |
| 43.5s | 分析系数 | `Indicate(coefficients)` |
| 44.5s | 分析字母 | `Indicate(variables)` |
| 45.5s | 公因式确定 | `Write(common_factor)` |
| 46.5s | 提取过程 | `Transform` |
| 47.5s | 最终答案 | `Write(answer)` |
| 48.5s | 答案确认 | `Flash + check` |
| 49.5s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: 所有例题元素

---

## Scene 7: 结尾总结 (52-60秒)
**目的**: 总结要点，引导关注

### 元素
1. 总结卡片 - 中央
2. 关键要点列表
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 52.0s | 总结标题 | `Write(summary_title)` |
| 53.0s | 要点1 | `FadeIn(point1, shift=RIGHT)` |
| 54.0s | 要点2 | `FadeIn(point2, shift=RIGHT)` |
| 55.0s | 要点3 | `FadeIn(point3, shift=RIGHT)` |
| 56.0s | 图标装饰 | `Create(decorations)` |
| 57.0s | 关注文字放大 | `author_info放大居中` |
| 58.0s | 关注提示 | `Write(follow_text)` |
| 59.0s | 闪烁效果 | `Flash(follow_text)` |
| 60.0s | 结束 | `Wait(1.0)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 贯穿始终 |
| example_formula | Scene 1 | Scene 2 | 示例公式 |
| step_elements | Scene 3 | Scene 3 | 步骤演示元素 |
| formula_cards | Scene 4 | Scene 4 | 口诀卡片 |
| practice1 | Scene 5 | Scene 5 | 练习1元素 |
| practice2 | Scene 6 | Scene 6 | 练习2元素 |
| summary | Scene 7 | Scene 7 | 总结元素 |

---

## 关键技术点
1. **中文处理**: 所有中文使用 `Text(font="Noto Sans CJK SC")`
2. **公式处理**: 数学公式使用 `MathTex`
3. **颜色管理**: 公因式用红色高亮
4. **动画节奏**: 关键步骤停留2秒，简单动画0.8秒
5. **边界控制**: 所有元素 y ∈ [-6, 7]

## 预期难点
1. TransformMatchingTex 的正确使用
2. 公因式的视觉高亮
3. 箭头和框选的精确对齐
4. 节奏控制确保清晰度