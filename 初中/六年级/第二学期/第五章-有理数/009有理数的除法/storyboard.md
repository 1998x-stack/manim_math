# 有理数的除法 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 初级（六年级）
- 目标受众: 小学六年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主题色
COLOR_POSITIVE = "#2ecc71"     # 绿色 - 正数
COLOR_NEGATIVE = "#e74c3c"     # 红色 - 负数
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
COLOR_RECIPROCAL = "#9b59b6"   # 紫色 - 倒数
COLOR_BACKGROUND = "#1a1a2e"   # 深蓝黑 - 背景
```

## 核心概念可视化策略
这是代数内容，重点展示：
- 除法到乘法的转换（Transform 动画）
- 倒数的概念（翻转、对称）
- 符号规则（颜色编码）
- 特殊情况（0的除法）

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 无几何元素 | N/A | N/A |

本动画为代数内容，无需几何计算，但需要精确的公式变换动画。

---

## Scene 1: 开场钩子 (4秒)
**目的**: 抓住注意力，引出除法问题

### 元素
1. 作者标识（顶部小字）
2. 钩子问题："(-6) ÷ (-2) = ？"
3. 困惑动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_question)` |
| 1.5s | 大问号闪烁 | `Flash(question_mark)` |
| 2.5s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: hook_question, question_mark
- 保留: author_info

---

## Scene 2: 核心法则 - 除法转乘法 (8秒)
**目的**: 展示除法的本质：除以b = 乘以b的倒数

### 元素
1. 标题："除法的秘密"
2. 核心公式：a ÷ b = a × (1/b)
3. 转换动画：除号→乘号，b→1/b

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title)` |
| 1.0s | 除法公式淡入 | `FadeIn(division)` |
| 2.0s | 箭头指示转换 | `GrowArrow(arrow)` |
| 2.5s | 变换为乘法 | `TransformMatchingTex(div, mult)` |
| 4.0s | 高亮关键部分 | `Indicate(reciprocal)` |
| 6.0s | 等待 | `Wait(2.0)` |

### 清理
- 缩小移至侧边
- 保留: 核心公式（侧边参考）

---

## Scene 3: 倒数概念 (10秒)
**目的**: 详细讲解什么是倒数

### 元素
1. 标题："倒数"
2. 定义：两个数的乘积为1
3. 示例：
   - 2的倒数是1/2（因为 2 × 1/2 = 1）
   - -3的倒数是-1/3
   - 1/4的倒数是4

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title)` |
| 1.0s | 定义淡入 | `FadeIn(definition)` |
| 2.0s | 示例1创建 | `Write(example1)` |
| 3.0s | 验证乘积=1 | `FadeIn(verification1)` |
| 4.5s | 示例2创建 | `Write(example2)` |
| 5.5s | 验证 | `FadeIn(verification2)` |
| 7.0s | 示例3创建 | `Write(example3)` |
| 8.0s | 验证 | `FadeIn(verification3)` |
| 9.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: examples
- 保留: title, definition（缩小）

---

## Scene 4: 符号法则 - 同号得正 (8秒)
**目的**: 演示同号除法结果为正

### 元素
1. 公式：(-6) ÷ (-2)
2. 转换：(-6) × (-1/2)
3. 符号判断：负×负=正
4. 结果：+3

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 原问题淡入 | `FadeIn(problem)` |
| 1.0s | 转换箭头 | `GrowArrow(arrow)` |
| 1.5s | 转为乘法 | `TransformMatchingTex(div, mult)` |
| 2.5s | 标注符号 | `FadeIn(sign_labels)` |
| 3.5s | 符号规则提示 | `Write(rule_hint)` |
| 4.5s | 计算结果 | `Write(result)` |
| 5.5s | 高亮答案 | `Flash(result)` |
| 7.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 5: 符号法则 - 异号得负 (8秒)
**目的**: 演示异号除法结果为负

### 元素
1. 公式：(+8) ÷ (-4)
2. 转换：(+8) × (-1/4)
3. 符号判断：正×负=负
4. 结果：-2

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 原问题淡入 | `FadeIn(problem)` |
| 1.0s | 转换箭头 | `GrowArrow(arrow)` |
| 1.5s | 转为乘法 | `TransformMatchingTex(div, mult)` |
| 2.5s | 标注符号 | `FadeIn(sign_labels)` |
| 3.5s | 符号规则提示 | `Write(rule_hint)` |
| 4.5s | 计算结果 | `Write(result)` |
| 5.5s | 高亮答案 | `Flash(result)` |
| 7.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 6: 特殊情况 - 0的除法 (10秒)
**目的**: 强调0的除法规则

### 元素
1. 规则1：0 ÷ a = 0（a ≠ 0）
2. 示例：0 ÷ 5 = 0
3. 规则2：a ÷ 0 = 无意义（禁止标志）
4. 警告：除数不能为0

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title)` |
| 1.0s | 规则1淡入 | `FadeIn(rule1)` |
| 2.0s | 示例1 | `Write(example1)` |
| 3.0s | 验证 | `FadeIn(check_mark)` |
| 4.0s | 规则2淡入 | `FadeIn(rule2)` |
| 5.0s | 禁止标志 | `Create(prohibition_sign)` |
| 6.0s | 警告闪烁 | `Flash(warning)` |
| 7.0s | 重点提示 | `Write(key_point)` |
| 9.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 7: 总结与片尾 (12秒)
**目的**: 总结规律，引导关注

### 元素
1. 核心规律卡片：
   - 除法 = 乘倒数
   - 同号 → 正
   - 异号 → 负
   - 0 ÷ a = 0（a ≠ 0）
   - a ÷ 0 = 禁止
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 规律卡片滑入 | `cards.animate.shift(RIGHT*0)` |
| 4.0s | 卡片高亮 | `Flash(cards)` |
| 5.0s | 作者信息放大 | `Transform(author_small, author_big)` |
| 6.0s | 关注提示 | `Write(follow_text)` |
| 7.0s | 装饰动画 | `Rotate(decorations)` |
| 11.0s | 全部淡出 | `FadeOut(everything)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 顶部常驻 |
| hook_question | Scene 1 | Scene 1 | 钩子问题 |
| core_formula | Scene 2 | Scene 6 | 核心转换 |
| reciprocal_def | Scene 3 | Scene 3 | 倒数定义 |
| sign_examples | Scene 4-5 | Scene 5 | 符号示例 |
| zero_rules | Scene 6 | Scene 6 | 0的规则 |
| summary_cards | Scene 7 | Scene 7 | 总结卡片 |

---

## 动画节奏要点
1. **Scene 1**: 快速吸引（4秒）
2. **Scene 2**: 核心转换（8秒）- 重点
3. **Scene 3**: 倒数概念（10秒）- 基础
4. **Scene 4-5**: 符号规则（每个8秒）
5. **Scene 6**: 特殊情况（10秒）- 强调
6. **Scene 7**: 收尾关注（12秒）

## 教学重点
- 除法=乘倒数（核心转换）
- 倒数的定义和求法
- 符号法则（与乘法一致）
- 0的特殊规则（强调除数不能为0）
- 颜色编码：绿色=正，红色=负，紫色=倒数

## 与乘法的联系
- 符号法则完全相同
- 强调"除法是乘法的特殊形式"
- 可以引用前一个视频的内容