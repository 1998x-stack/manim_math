# 有余数的除法 - 动画分镜脚本

## 元信息
- 目标时长: 60 秒
- 场景数量: 5 个
- 难度等级: 简单

## 颜色配置
```python
COLOR_PRIMARY = "#1a1a2e"  # 背景色
COLOR_HIGHLIGHT = YELLOW    # 高亮色
COLOR_SUCCESS = GREEN       # 成功/正确颜色
COLOR_WARNING = ORANGE      # 警告/错误颜色
COLOR_AUXILIARY = GRAY_B    # 辅助色
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 物体位置 | 均匀分布网格 | self.objects |
| 分组位置 | 水平排列 | self.groups |
| 余数位置 | 单独显示 | self.remainder |

---

## Scene 1: 开场 (3-4秒)
**目的**: 钩子 + 引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字)
3. 主图形

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.1s | 图形创建 | `Create(objects)` |
| 2.1s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text
- 保留: objects, author_info

---

## Scene 2: 平均分演示 (10秒)
**目的**: 展示平均分概念和余数产生

### 元素
1. 13个圆形物体（代表苹果）
2. 4个矩形分组框
3. 分配过程动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 显示13个圆 | `Create(objects)` |
| 1.0s | 创建4个分组框 | `Create(groups)` |
| 2.0s | 将3个圆放入每个框 | `Transform` 循环 |
| 4.0s | 显示剩余1个圆 | `FadeIn(remainder)` |
| 5.0s | 高亮显示余数 | `Flash(remainder)` |

### 清理
- 保留: objects, groups, remainder

---

## Scene 3: 数学算式 (12秒)
**目的**: 建立数学表达与视觉的联系

### 元素
1. 算式：13 ÷ 4 = 3 … 1
2. 各部分标签：被除数、除数、商、余数
3. 关系说明：余数 < 除数

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 写入完整算式 | `Write(formula)` |
| 1.0s | 高亮被除数13 | `formula[0].animate.set_color(YELLOW)` |
| 2.0s | 高亮除数4 | `formula[2].animate.set_color(GREEN)` |
| 3.0s | 高亮商3 | `formula[4].animate.set_color(BLUE)` |
| 4.0s | 高亮余数1 | `formula[6].animate.set_color(RED)` |
| 5.0s | 显示关系：1 < 4 | `Write(relation)` |
| 6.0s | 用Brace连接余数和除数 | `Create(brace)` |

### 清理
- 保留: formula, relation, brace

---

## Scene 4: 概念解释 (15秒)
**目的**: 清晰定义概念

### 元素
1. 文字定义："平均分时，有剩余且不够再分一份，剩下的数叫做'余数'"
2. 图形辅助：箭头指向余数圆
3. 错误示例：尝试将余数再分（显示×）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 书写定义文字 | `Write(definition)` |
| 2.0s | 箭头指向余数 | `Create(arrow)` |
| 4.0s | 错误尝试动画 | `Transform(remainder, cross)` |
| 6.0s | 显示×符号 | `Write(cross)` |
| 8.0s | 正确总结 | `Write(summary)` |

### 清理
- 保留: definition, summary

---

## Scene 5: 总结与练习 (15秒)
**目的**: 巩固概念并提供练习

### 元素
1. 总结要点卡片
2. 练习题：17 ÷ 5 = ? … ?
3. 作者信息

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 显示总结卡片 | `FadeIn(cards)` |
| 2.0s | 显示练习题 | `Write(exercise)` |
| 4.0s | 提示思考时间 | `Wait(3.0)` |
| 7.0s | 显示答案 | `Write(answer)` |
| 9.0s | 作者信息淡入 | `FadeIn(author_info)` |
| 10.0s | 关注提示 | `Write(follow_text)` |

### 清理
- 完整场景

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| objects | Scene 1 | Scene 2 | 13个圆形物体 |
| groups | Scene 2 | Scene 2 | 4个分组框 |
| remainder | Scene 2 | Scene 4 | 余数物体 |
| formula | Scene 3 | Scene 5 | 数学算式 |
| definition | Scene 4 | Scene 5 | 概念定义 |
| summary | Scene 4 | Scene 5 | 总结要点 |
| exercise | Scene 5 | Scene 5 | 练习题 |
| answer | Scene 5 | Scene 5 | 答案 |
| author_info | Scene 1 | Scene 5 | 作者信息 |
| follow_text | Scene 5 | Scene 5 | 关注提示 |