# 有理数的乘方 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 初级（六年级）
- 知识点：有理数的乘方基本概念

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要公式
COLOR_SECONDARY = "#e74c3c"      # 红色 - 强调/警告
COLOR_HIGHLIGHT = "#f39c12"      # 橙色 - 高亮
COLOR_POSITIVE = "#2ecc71"       # 绿色 - 正数
COLOR_NEGATIVE = "#e74c3c"       # 红色 - 负数
COLOR_AUXILIARY = "#95a5a6"      # 灰色 - 辅助线
COLOR_BACKGROUND = "#1a1a2e"     # 深蓝黑背景
```

## 几何/元素预计算清单

| 元素 | 计算/定义 | 存储变量 | 用途 |
|------|---------|---------|------|
| 无复杂几何 | - | - | 本动画主要是公式展示 |
| 方块位置 | 均匀排列 | self.box_positions | 展示乘法过程 |
| 箭头位置 | 连接方块 | self.arrow_positions | 连接重复因数 |

## 动画节奏参数
```python
ANIMATION_SPEED = {
    "quick": 0.3,      # 快速过渡
    "normal": 0.6,     # 正常速度
    "slow": 1.0,       # 慢速（重点）
    "pause": 1.5,      # 停顿（理解）
}
```

---

## Scene 1: 开场钩子 (4秒)
**目的**: 吸引注意力，提出问题

### 视觉元素
1. 作者标识（顶部）
2. 钩子问题："2×2×2×2 有更简单的写法吗？"
3. 闪烁的问号

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时长 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子问题书写 | `Write(hook_question)` | 1.0s |
| 1.3s | 显示乘法算式 | `Write(multiplication)` | 0.8s |
| 2.1s | 问号闪烁 | `Flash(question_mark)` | 0.5s |
| 2.6s | 等待思考 | `Wait(1.0)` | 1.0s |
| 3.6s | 答案提示 | `FadeIn(hint_text)` | 0.4s |

### 文本内容
```python
hook_question = "这样写太麻烦了！"
multiplication = "2 × 2 × 2 × 2"
hint_text = "用乘方可以简化！"
```

### 清理
- FadeOut: hook_question, multiplication, hint_text, question_mark
- 保留: author_info

---

## Scene 2: 乘方定义 (8秒)
**目的**: 引入乘方的定义和记号

### 视觉元素
1. 标题："什么是乘方？"
2. 定义文字
3. 一般形式：a^n
4. 术语标注（底数、指数、幂）

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时长 |
|------|------|---------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 0.5s | 定义文字书写 | `Write(definition)` | 1.2s |
| 1.7s | 显示一般形式 | `Write(general_form)` | 0.8s |
| 2.5s | 底数标注 | `Indicate(base_label)` | 0.6s |
| 3.1s | 指数标注 | `Indicate(exponent_label)` | 0.6s |
| 3.7s | 幂标注 | `Indicate(power_label)` | 0.6s |
| 4.3s | 等待理解 | `Wait(1.5)` | 1.5s |

### 文本内容
```python
title = "乘方 Power"
definition = "n个相同因数a相乘"
general_form = "a^n"
base_label = "底数 a"
exponent_label = "指数 n"
power_label = "幂 a^n"
```

### 清理
- FadeOut: title, definition
- 保留: general_form 及其标注（变小移到角落）

---

## Scene 3: 具体例子 - 2^4 (10秒)
**目的**: 用具体例子说明乘方的展开

### 视觉元素
1. 左侧：2^4
2. 中间：等号
3. 右侧：2 × 2 × 2 × 2 的方块展开
4. 箭头连接
5. 计算结果：= 16

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时长 |
|------|------|---------|---------|
| 0.0s | 显示 2^4 | `Write(power_notation)` | 0.6s |
| 0.6s | 等号出现 | `FadeIn(equal_sign)` | 0.3s |
| 0.9s | 第1个方块 | `FadeIn(box1, scale=0.5)` | 0.4s |
| 1.3s | 第2个方块 | `FadeIn(box2, scale=0.5)` | 0.4s |
| 1.7s | 第3个方块 | `FadeIn(box3, scale=0.5)` | 0.4s |
| 2.1s | 第4个方块 | `FadeIn(box4, scale=0.5)` | 0.4s |
| 2.5s | 乘号连接 | `Create(multiplication_signs)` | 0.6s |
| 3.1s | 指数标注 | `Indicate(exponent_4)` | 0.5s |
| 3.6s | 强调4个 | `Circumscribe(boxes)` | 0.8s |
| 4.4s | 计算过程 | `Transform(boxes, result)` | 1.0s |
| 5.4s | 显示结果 | `Write(final_result)` | 0.6s |
| 6.0s | 等待 | `Wait(1.5)` | 1.5s |

### 几何计算
```python
# 方块位置（均匀分布）
box_width = 0.6
spacing = 0.3
total_width = 4 * box_width + 3 * spacing

box_positions = [
    RIGHT * (i * (box_width + spacing) - total_width/2)
    for i in range(4)
]
```

### 清理
- Transform: 整体向上移动变小
- 保留: 简化的 2^4 = 16

---

## Scene 4: 0次幂规则 (7秒)
**目的**: 说明任何非零数的0次幂等于1

### 视觉元素
1. 公式：a^0 = 1 (a ≠ 0)
2. 具体例子：5^0 = 1, (-3)^0 = 1
3. 警告标识：a ≠ 0

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时长 |
|------|------|---------|---------|
| 0.0s | 显示规则 | `Write(zero_power_rule)` | 0.8s |
| 0.8s | 强调条件 | `Indicate(condition)` | 0.6s |
| 1.4s | 例子1 | `Write(example1)` | 0.5s |
| 1.9s | 例子2 | `Write(example2)` | 0.5s |
| 2.4s | 闪光强调 | `Flash(rule)` | 0.4s |
| 2.8s | 等待 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: 所有内容

---

## Scene 5: 负数的乘方 - 核心重点 (15秒)
**目的**: 区分 (-a)^n 与 -a^n，这是最容易出错的地方

### 视觉元素
1. 标题："⚠️ 注意！负号的位置很重要"
2. 左侧：(-2)^2 与 (-2)^3
3. 右侧：-2^2 与 -2^3
4. 对比框
5. 颜色区分：正数绿色，负数红色

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时长 |
|------|------|---------|---------|
| 0.0s | 警告标题 | `Write(warning_title)` | 0.8s |
| 0.8s | 左框架 | `Create(left_box)` | 0.5s |
| 1.3s | 右框架 | `Create(right_box)` | 0.5s |
| 1.8s | (-2)^2 | `Write(formula1)` | 0.6s |
| 2.4s | 展开 | `Write(expansion1)` | 0.8s |
| 3.2s | 结果 +4 | `Write(result1, color=GREEN)` | 0.5s |
| 3.7s | 等待 | `Wait(0.5)` | 0.5s |
| 4.2s | (-2)^3 | `Write(formula2)` | 0.6s |
| 4.8s | 展开 | `Write(expansion2)` | 0.8s |
| 5.6s | 结果 -8 | `Write(result2, color=RED)` | 0.5s |
| 6.1s | 等待 | `Wait(0.5)` | 0.5s |
| 6.6s | -2^2 | `Write(formula3)` | 0.6s |
| 7.2s | 强调负号在外 | `Indicate(minus_sign)` | 0.5s |
| 7.7s | 结果 -4 | `Write(result3, color=RED)` | 0.5s |
| 8.2s | 对比闪烁 | `Flash(comparison)` | 0.6s |
| 8.8s | 等待理解 | `Wait(2.0)` | 2.0s |

### 文本内容
```python
warning_title = "⚠️ 注意！负号的位置"
formula1 = "(-2)² = (-2)×(-2) = +4"  # 负数的偶次幂
formula2 = "(-2)³ = (-2)×(-2)×(-2) = -8"  # 负数的奇次幂
formula3 = "-2² = -(2×2) = -4"  # 负号在外
```

### 清理
- FadeOut: 所有框架和内容

---

## Scene 6: 规律总结 (10秒)
**目的**: 总结负数乘方的规律

### 视觉元素
1. 标题："负数乘方的规律"
2. 规则1：(-a)^偶数 = 正数
3. 规则2：(-a)^奇数 = 负数
4. 图标：✓ 和颜色标识

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时长 |
|------|------|---------|---------|
| 0.0s | 标题 | `Write(title)` | 0.6s |
| 0.6s | 规则1 | `FadeIn(rule1)` | 0.8s |
| 1.4s | 正数标识 | `FadeIn(positive_icon)` | 0.4s |
| 1.8s | 规则2 | `FadeIn(rule2)` | 0.8s |
| 2.6s | 负数标识 | `FadeIn(negative_icon)` | 0.4s |
| 3.0s | 框架强调 | `Create(highlight_box)` | 0.6s |
| 3.6s | 等待记忆 | `Wait(2.0)` | 2.0s |

### 清理
- FadeOut: 所有内容

---

## Scene 7: 结尾总结与关注 (6秒)
**目的**: 总结要点，引导关注

### 视觉元素
1. 总结卡片："今天学了什么？"
2. 要点1：乘方的定义 a^n
3. 要点2：0次幂规则
4. 要点3：负数乘方规律
5. 作者信息放大
6. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时长 |
|------|------|---------|---------|
| 0.0s | 总结卡片 | `FadeIn(summary_card)` | 0.6s |
| 0.6s | 要点依次出现 | `Write(points)` | 1.2s |
| 1.8s | 作者信息放大 | `author.animate.scale(2)` | 0.8s |
| 2.6s | 关注提示 | `FadeIn(follow_text)` | 0.6s |
| 3.2s | 装饰动画 | `Rotate(decorations)` | 1.5s |
| 4.7s | 最后等待 | `Wait(1.0)` | 1.0s |

### 清理
- FadeOut: 全部

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 持久性 | 备注 |
|------|---------|---------|-------|------|
| author_info | Scene 1 | Scene 7 | 全程 | 顶部作者标识 |
| hook_question | Scene 1 | Scene 1 | 临时 | 钩子问题 |
| general_form | Scene 2 | Scene 3 | 短期 | 一般形式，移到角落 |
| power_example | Scene 3 | Scene 4 | 短期 | 2^4示例 |
| zero_rule | Scene 4 | Scene 4 | 临时 | 0次幂规则 |
| negative_comparison | Scene 5 | Scene 5 | 临时 | 负数对比 |
| summary_rules | Scene 6 | Scene 6 | 临时 | 规律总结 |
| summary_card | Scene 7 | Scene 7 | 临时 | 最后总结 |

---

## 关键技术点

### 1. 无复杂几何
本动画主要是公式和文字展示，不涉及三角形、圆等几何图形，因此：
- verify_geometry.py 主要验证布局合理性
- 不需要复杂的角度、距离计算
- 重点是文字排版和动画节奏

### 2. 颜色语义
- 正数结果：绿色 (#2ecc71)
- 负数结果：红色 (#e74c3c)
- 警告提示：橙色 (#f39c12)
- 主要内容：蓝色 (#3498db)

### 3. 节奏控制
- Scene 5（负数乘方）是核心，分配15秒
- 关键停顿：理解后等待1.5-2秒
- 快速过渡：0.3-0.5秒

### 4. 文字大小
```python
FONT_SIZES = {
    "title": 36,          # 场景标题
    "subtitle": 28,       # 副标题
    "formula": 32,        # 数学公式
    "body": 24,           # 正文说明
    "small": 20,          # 小字注释
    "author": 20,         # 作者信息
}
```

---

## 验证要点

### verify_geometry.py 需要检查：
1. ✓ 所有文字元素在边界内 (x∈[-4,4], y∈[-7,7])
2. ✓ 方块位置均匀分布
3. ✓ 箭头方向正确
4. ✓ 颜色对比度足够（文字可读性）
5. ✓ 字体大小符合规范

### 不需要检查的：
- ❌ 角度（无几何图形）
- ❌ 距离精度（非几何动画）
- ❌ 垂直/平行关系

---

## 总时长预估
- Scene 1: 4s
- Scene 2: 8s
- Scene 3: 10s
- Scene 4: 7s
- Scene 5: 15s (重点)
- Scene 6: 10s
- Scene 7: 6s
- **总计**: 60s

符合 TikTok 短视频最佳时长（60-90秒）✓