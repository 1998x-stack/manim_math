# 有理数的乘法 - 动画分镜脚本

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
COLOR_BACKGROUND = "#1a1a2e"   # 深蓝黑 - 背景
```

## 核心概念可视化策略
由于这是代数而非几何题目，不需要复杂的几何计算。主要使用：
- 数轴可视化（NumberLine）
- 符号规则表格（Rectangle + MathTex）
- 动画示例（颜色编码：正数用绿色，负数用红色）

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 数轴中心 | ORIGIN | self.number_line_center |
| 表格位置 | UP * 2 | self.table_position |
| 示例区域 | DOWN * 2 | self.example_position |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 抓住注意力，提出核心问题

### 元素
1. 作者标识（顶部小字）
2. 钩子问题："负数×负数 = ？"
3. 困惑表情/问号动画

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

## Scene 2: 法则总览 (6秒)
**目的**: 展示四条基本法则

### 元素
1. 标题："有理数乘法法则"
2. 四条法则：
   - (+) × (+) = +
   - (-) × (-) = +
   - (+) × (-) = -
   - (-) × (+) = -

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title)` |
| 1.0s | 法则1逐条淡入 | `FadeIn(rule1, shift=RIGHT*0.3)` |
| 1.5s | 法则2淡入 | `FadeIn(rule2, shift=RIGHT*0.3)` |
| 2.0s | 法则3淡入 | `FadeIn(rule3, shift=RIGHT*0.3)` |
| 2.5s | 法则4淡入 | `FadeIn(rule4, shift=RIGHT*0.3)` |
| 3.5s | 高亮关键点 | `Indicate(key_rules)` |
| 5.0s | 等待 | `Wait(1.0)` |

### 清理
- Transform: 法则移至侧边缩小版
- 保留: title (缩小), rules (侧边)

---

## Scene 3: 同号得正 - 正×正 (8秒)
**目的**: 用数轴和实例演示 (+3) × (+2) = +6

### 元素
1. 公式：(+3) × (+2)
2. 数轴（0到10）
3. 跳跃动画：3个单位跳2次

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 公式书写 | `Write(formula)` |
| 1.0s | 数轴创建 | `Create(number_line)` |
| 2.0s | 起点标记 | `FadeIn(start_dot)` |
| 2.5s | 第一次跳跃 +3 | `MoveAlongPath(dot, arc1)` |
| 3.5s | 第二次跳跃 +3 | `MoveAlongPath(dot, arc2)` |
| 4.5s | 终点标记 6 | `Flash(end_dot)` |
| 5.0s | 结果高亮 | `Indicate(result)` |
| 6.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: number_line, dots, arcs
- 保留: formula (移至顶部)

---

## Scene 4: 同号得正 - 负×负 (10秒)
**目的**: 用对称性演示 (-3) × (-2) = +6

### 元素
1. 公式：(-3) × (-2)
2. 双向数轴（-10到10）
3. 反向跳跃动画
4. 对称性说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 公式书写 | `Write(formula)` |
| 1.0s | 双向数轴创建 | `Create(number_line)` |
| 2.0s | 起点标记 0 | `FadeIn(start_dot)` |
| 2.5s | 反向理解提示 | `FadeIn(hint_text)` |
| 3.5s | 第一次反向跳 -3 | `MoveAlongPath(dot, arc1)` |
| 4.5s | 第二次反向跳 -3 | `MoveAlongPath(dot, arc2)` |
| 5.5s | 终点标记 +6 | `Flash(end_dot)` |
| 6.0s | 关键提示 | `FadeIn(key_insight)` |
| 8.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: number_line, dots, hint
- 保留: formula (移至顶部)

---

## Scene 5: 异号得负 - 正×负 (8秒)
**目的**: 演示 (+3) × (-2) = -6

### 元素
1. 公式：(+3) × (-2)
2. 数轴
3. 负向跳跃

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 公式书写 | `Write(formula)` |
| 1.0s | 数轴创建 | `Create(number_line)` |
| 2.0s | 起点标记 | `FadeIn(start_dot)` |
| 2.5s | 负向跳跃 -2 | `MoveAlongPath(dot, arc1)` |
| 3.5s | 负向跳跃 -2 | `MoveAlongPath(dot, arc2)` |
| 4.5s | 负向跳跃 -2 | `MoveAlongPath(dot, arc3)` |
| 5.5s | 终点 -6 高亮 | `Flash(end_dot)` |
| 7.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: number_line, dots
- 保留: formula

---

## Scene 6: 多个数相乘规律 (10秒)
**目的**: 展示负因数个数规律

### 元素
1. 标题："负因数个数决定符号"
2. 示例：
   - 2个负数：(-2) × (-3) = +6
   - 3个负数：(-2) × (-3) × (-1) = -6
   - 4个负数：(-1) × (-1) × (-1) × (-1) = +1

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title)` |
| 1.0s | 示例1创建 | `FadeIn(example1)` |
| 2.0s | 负数计数动画 | `Indicate(negative_count)` |
| 2.5s | 结果高亮（正） | `example1.result.set_color(GREEN)` |
| 3.5s | 示例2创建 | `FadeIn(example2)` |
| 4.5s | 负数计数 | `Indicate(negative_count)` |
| 5.0s | 结果高亮（负） | `example2.result.set_color(RED)` |
| 6.0s | 示例3创建 | `FadeIn(example3)` |
| 7.0s | 结果高亮（正） | `example3.result.set_color(GREEN)` |
| 8.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: examples
- 保留: title

---

## Scene 7: 总结与片尾 (10秒)
**目的**: 总结规律，引导关注

### 元素
1. 核心规律卡片：
   - 同号 → 正
   - 异号 → 负
   - 偶数个负因数 → 正
   - 奇数个负因数 → 负
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 规律卡片滑入 | `cards.animate.shift(RIGHT*0)` |
| 3.0s | 卡片高亮 | `Flash(cards)` |
| 4.0s | 作者信息放大 | `Transform(author_small, author_big)` |
| 5.0s | 关注提示 | `Write(follow_text)` |
| 6.0s | 装饰动画 | `Rotate(decorations)` |
| 9.0s | 全部淡出 | `FadeOut(everything)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 顶部常驻 |
| hook_question | Scene 1 | Scene 1 | 钩子问题 |
| rule_table | Scene 2 | Scene 6 | 法则总览 |
| number_line_1 | Scene 3 | Scene 3 | 正×正数轴 |
| number_line_2 | Scene 4 | Scene 4 | 负×负数轴 |
| number_line_3 | Scene 5 | Scene 5 | 正×负数轴 |
| examples | Scene 6 | Scene 6 | 多数相乘 |
| summary_cards | Scene 7 | Scene 7 | 总结卡片 |

---

## 动画节奏要点
1. **Scene 1**: 快速吸引（4秒）
2. **Scene 2**: 建立框架（6秒）
3. **Scene 3-5**: 详细演示（每个8-10秒）
4. **Scene 6**: 规律总结（10秒）
5. **Scene 7**: 收尾关注（10秒）

## 教学重点
- 用颜色区分正负（绿色=正，红色=负）
- 数轴可视化帮助理解
- 多次重复核心规律
- 动画节奏：关键步骤慢，过渡快