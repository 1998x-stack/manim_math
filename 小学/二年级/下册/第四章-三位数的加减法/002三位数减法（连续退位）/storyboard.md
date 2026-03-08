# 三位数减法（连续退位）- 动画分镜脚本

## 元信息
- 目标时长: 60 秒
- 场景数量: 6 个
- 难度等级: 中等

## 颜色配置
```python
COLOR_PRIMARY = "#1a1a2e"  # 背景色
COLOR_HIGHLIGHT = "#f1c40f"  # 高亮色
COLOR_AUXILIARY = "#95a5a6"  # 辅助色
COLOR_NEGATIVE = "#e74c3c"  # 错误/退位提示色
COLOR_POSITIVE = "#2ecc71"  # 正确色
```

---

## Scene 1: 开场钩子 (5秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字)
3. 题目展示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.5s | 题目展示 | `Write(problem)` |
| 3.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: hook_text
- 保留: problem, author_info

---

## Scene 2: 竖式对齐 (8秒)
**目的**: 展示相同数位对齐

### 元素
1. 竖式数字
2. 数位对齐线

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 写出被减数500 | `Write(minuend)` |
| 1.0s | 写出减号和减数123 | `Write(subtrahend)` |
| 2.5s | 画出横线 | `Create(hr)` |
| 4.0s | 高亮数位对齐 | `Indicate(digits, color=COLOR_HIGHLIGHT)` |
| 6.0s | 等待 | `Wait(2.0)` |

### 清理
- 无
- 保留: 竖式所有元素

---

## Scene 3: 个位不够减，向十位借 (12秒)
**目的**: 展示个位0减3不够，向十位借

### 元素
1. 个位数字高亮
2. 借位箭头
3. 十位是0的提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 高亮个位0和3 | `Indicate(ones_digits, color=COLOR_HIGHLIGHT)` |
| 1.5s | 显示“0不够减3” | `Write(ones_problem)` |
| 3.0s | 画借位箭头到十位 | `GrowArrow(arrow_to_tens)` |
| 4.5s | 高亮十位0 | `Indicate(tens_zero, color=COLOR_NEGATIVE)` |
| 6.0s | 显示“十位是0，借不到！” | `Write(tens_problem)` |
| 8.0s | 等待 | `Wait(4.0)` |

### 清理
- FadeOut: ones_problem, tens_problem
- 保留: arrow_to_tens, 竖式

---

## Scene 4: 十位向百位借 (15秒)
**目的**: 展示十位向百位借，百位5变4，十位0变10

### 元素
1. 借位箭头到百位
2. 百位5变4
3. 十位0变10
4. 十位再借给个位1，变9

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 画借位箭头到百位 | `GrowArrow(arrow_to_hundreds)` |
| 1.5s | 百位5变4（划掉5，写4） | `CrossOut(five), Write(four)` |
| 3.5s | 十位0变10（写10） | `Write(ten_on_tens)` |
| 5.5s | 显示“十位有10了，借给个位1” | `Write(tens_lend)` |
| 7.5s | 十位10变9（划掉10，写9） | `CrossOut(ten_on_tens), Write(nine_on_tens)` |
| 9.5s | 个位0变10（写10） | `Write(ten_on_ones)` |
| 11.5s | 等待 | `Wait(3.5)` |

### 清理
- FadeOut: tens_lend
- 保留: 所有借位标记、竖式

---

## Scene 5: 计算结果 (12秒)
**目的**: 逐位计算，得出答案377

### 元素
1. 个位计算：10-3=7
2. 十位计算：9-2=7
3. 百位计算：4-1=3
4. 最终答案377

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 个位计算：10-3=7 | `Write(ones_result)` |
| 2.0s | 十位计算：9-2=7 | `Write(tens_result)` |
| 4.0s | 百位计算：4-1=3 | `Write(hundreds_result)` |
| 6.0s | 组合答案377 | `Write(final_answer)` |
| 8.0s | 高亮最终答案 | `Indicate(final_answer, color=COLOR_POSITIVE)` |
| 10.0s | 等待 | `Wait(2.0)` |

### 清理
- 无
- 保留: 完整竖式和答案

---

## Scene 6: 总结与片尾 (8秒)
**目的**: 总结步骤，引导关注

### 元素
1. 步骤总结文字
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 竖式淡出，总结文字淡入 | `FadeOut(vertical_form), FadeIn(summary)` |
| 2.0s | 作者信息放大 | `Transform(author_info, author_large)` |
| 4.0s | 关注提示淡入 | `FadeIn(follow_text)` |
| 6.0s | 等待 | `Wait(2.0)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 作者信息 |
| problem | Scene 1 | Scene 2 | 题目展示 |
| vertical_form | Scene 2 | Scene 6 | 完整竖式 |
| arrow_to_tens | Scene 3 | Scene 6 | 个位到十位的借位箭头 |
| arrow_to_hundreds | Scene 4 | Scene 6 | 十位到百位的借位箭头 |
| final_answer | Scene 5 | Scene 6 | 最终答案377 |
| summary | Scene 6 | Scene 6 | 步骤总结 |
