# 因数与倍数 - Manim动画分镜脚本

<!-- /root/code/sss/media/videos/factors_multiples/1920p60/FactorsAndMultiples.mp4 -->

## 元信息
- 目标时长: 70-80秒
- 场景数量: 6个
- 难度等级: 六年级（小学）
- 知识点: 因数与倍数的概念、性质

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"       # 蓝色 - 主要概念
COLOR_FACTOR = "#e74c3c"        # 红色 - 因数
COLOR_MULTIPLE = "#2ecc71"      # 绿色 - 倍数
COLOR_HIGHLIGHT = "#f39c12"     # 橙色 - 高亮
COLOR_SPECIAL = "#9b59b6"       # 紫色 - 特殊情况
COLOR_AUXILIARY = "#95a5a6"     # 灰色 - 辅助
COLOR_BACKGROUND = "#1a1a2e"    # 深蓝灰 - 背景
```

## 视觉元素预计算
本动画主要涉及表格、数轴、文字和公式，不涉及复杂几何图形。
主要元素：Table、NumberLine、Dot、MathTex、Text、VGroup、SurroundingRectangle、Arrow

---

## Scene 1: 开场引入 (4-5秒)
**目的**: 用生活化问题吸引注意力

### 元素
1. 作者标识 (顶部)
2. 钩子问题："12个糖果，怎么平均分？"
3. 引导到因数概念

### 动画序列
| 时间 | 动作 | 代码参考 | y坐标 |
|------|------|---------|-------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info)` | y=7 |
| 0.3s | 钩子问题书写 | `Write(hook_text)` | y=5.5 |
| 1.2s | 糖果图标出现 | `FadeIn(candy_icons)` | y=3 |
| 2.5s | 分组示意 | `Transform(candies)` | y=1 |
| 3.5s | 引导文字 | `FadeIn(hint)` | y=-1 |
| 4.5s | 等待理解 | `Wait(0.5)` | - |

### 钩子问题
"12个糖果，可以平均分给几个人？"

### 清理
- FadeOut: hook_text, candy_icons, hint
- 保留: author_info

---

## Scene 2: 因数与倍数定义 (8-10秒)
**目的**: 清晰讲解核心概念

### 元素
1. 标题："因数与倍数"
2. 定义公式：a = b × q
3. 关系图示
4. 举例：12 = 3 × 4

### 动画序列
| 时间 | 动作 | 代码参考 | y坐标 |
|------|------|---------|-------|
| 0.0s | 标题淡入 | `FadeIn(title)` | y=5.5 |
| 0.8s | 公式出现 | `Write(formula)` | y=3.5 |
| 2.0s | 高亮"b是a的因数" | `Indicate(factor_part)` | - |
| 3.0s | 高亮"a是b的倍数" | `Indicate(multiple_part)` | - |
| 4.0s | 具体例子 | `FadeIn(example)` | y=0.5 |
| 5.0s | 标注关系 | `Create(arrows)` | - |
| 7.0s | 说明文字 | `FadeIn(explanation)` | y=-3 |
| 8.5s | 等待 | `Wait(1.0)` | - |

### 核心公式
```
若 a = b × q (q为正整数)
则：b 是 a 的因数
    a 是 b 的倍数
```

### 举例
```
12 = 3 × 4
  ↓   ↓   ↓
倍数 因数 因数
```

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 3: 找因数 - 有限性 (12-15秒)
**目的**: 演示如何找一个数的所有因数，强调有限性

### 元素
1. 标题："找12的所有因数"
2. 系统检查：1到12每个数
3. 表格展示结果
4. 强调"因数是有限的"

### 动画序列
| 时间 | 动作 | 代码参考 | y坐标 |
|------|------|---------|-------|
| 0.0s | 标题书写 | `Write(title)` | y=5.5 |
| 0.8s | 数轴出现 | `Create(number_line)` | y=3.5 |
| 1.5s | 逐个检查1-12 | `循环动画` | - |
| 6.0s | 因数高亮 | `Indicate(factors)` | - |
| 7.0s | 创建表格 | `Create(table)` | y=0 |
| 8.5s | 填充因数 | `FadeIn(entries)` | - |
| 10.0s | 强调有限性 | `SurroundingRectangle` | - |
| 11.5s | 说明文字 | `FadeIn(explanation)` | y=-4 |
| 13.0s | 等待 | `Wait(1.5)` | - |

### 检查过程
```
12 ÷ 1 = 12 ✓ → 1是因数
12 ÷ 2 = 6  ✓ → 2是因数
12 ÷ 3 = 4  ✓ → 3是因数
12 ÷ 4 = 3  ✓ → 4是因数
12 ÷ 5 = ? ✗ → 5不是因数
...
```

### 表格内容
| 数 | 12的因数 |
|----|---------|
| 结果 | 1, 2, 3, 4, 6, 12 |
| 共 | 6个（有限） |

### 清理
- FadeOut: number_line, 中间步骤
- 保留: table (淡化), author_info

---

## Scene 4: 找倍数 - 无限性 (12-15秒)
**目的**: 演示倍数的无限性，与因数形成对比

### 元素
1. 标题："找3的倍数"
2. 数轴动画：不断延伸
3. 倍数标记
4. 省略号强调无限

### 动画序列
| 时间 | 动作 | 代码参考 | y坐标 |
|------|------|---------|-------|
| 0.0s | 标题书写 | `Write(title)` | y=5.5 |
| 0.8s | 公式提示 | `FadeIn(formula_hint)` | y=4 |
| 1.5s | 数轴出现 | `Create(number_line)` | y=2 |
| 2.5s | 3标记 | `FadeIn(dot_3)` | - |
| 3.5s | 6标记 | `FadeIn(dot_6)` | - |
| 4.5s | 9标记 | `FadeIn(dot_9)` | - |
| 5.5s | 12标记 | `FadeIn(dot_12)` | - |
| 6.5s | 箭头延伸 | `GrowArrow(arrow)` | - |
| 7.5s | 省略号 | `FadeIn(ellipsis)` | y=0 |
| 9.0s | 强调无限 | `Flash(infinity_text)` | y=-2 |
| 10.5s | 说明文字 | `FadeIn(explanation)` | y=-4 |
| 12.5s | 等待 | `Wait(1.5)` | - |

### 数轴展示
```
0 -- 3 -- 6 -- 9 -- 12 -- 15 -- 18 -- ...
     ●    ●    ●     ●     ●     ●
```

### 公式提示
```
3 × 1 = 3
3 × 2 = 6
3 × 3 = 9
3 × 4 = 12
...
```

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 5: 特殊规律 (10-12秒)
**目的**: 强调1和0的特殊性

### 元素
1. 标题："特殊规律"
2. 规律1：1是所有正整数的因数
3. 规律2：0是所有非零整数的倍数
4. 视觉化展示

### 动画序列
| 时间 | 动作 | 代码参考 | y坐标 |
|------|------|---------|-------|
| 0.0s | 标题书写 | `Write(title)` | y=5.5 |
| 0.8s | 规律1框 | `Create(rule1_box)` | y=3 |
| 1.5s | 示例1展开 | `FadeIn(examples1)` | y=1.5 |
| 3.5s | 高亮1 | `Indicate(ones)` | - |
| 5.0s | 规律2框 | `Create(rule2_box)` | y=-1 |
| 6.0s | 示例2展开 | `FadeIn(examples2)` | y=-2.5 |
| 8.0s | 高亮0 | `Indicate(zeros)` | - |
| 9.5s | 等待理解 | `Wait(1.5)` | - |

### 规律1展示
```
1 × 5 = 5   → 1是5的因数
1 × 12 = 12 → 1是12的因数
1 × 99 = 99 → 1是99的因数
...
1是所有正整数的因数
```

### 规律2展示
```
3 × 0 = 0
7 × 0 = 0
15 × 0 = 0
...
0是所有非零整数的倍数
```

### 清理
- FadeOut: 所有规律框
- 保留: author_info

---

## Scene 6: 总结与巩固 (10-12秒)
**目的**: 总结要点，强化记忆

### 元素
1. 总结卡片
2. 对比表格
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | y坐标 |
|------|------|---------|-------|
| 0.0s | 标题淡入 | `FadeIn(title)` | y=5.5 |
| 0.8s | 对比表格 | `Create(comparison_table)` | y=2.5 |
| 2.5s | 要点1 | `FadeIn(point1, shift=LEFT)` | y=0 |
| 3.5s | 要点2 | `FadeIn(point2, shift=LEFT)` | y=-1.5 |
| 4.5s | 要点3 | `FadeIn(point3, shift=LEFT)` | y=-3 |
| 6.0s | 关注提示 | `Write(follow_text)` | y=-5 |
| 8.0s | 装饰闪烁 | `Flash(stars)` | - |
| 10.0s | 全部淡出 | `FadeOut(all)` | - |

### 对比表格
|  | 因数 | 倍数 |
|--|------|------|
| 数量 | 有限 | 无限 |
| 最小 | 1 | 本身 |
| 关系 | 相互依存 | 相互依存 |

### 总结要点
1. **定义**: a = b × q，b是a的因数，a是b的倍数
2. **数量**: 因数有限，倍数无限
3. **特殊**: 1是所有正整数的因数，0是所有非零整数的倍数

### 关注文字
"关注我，学更多数学技巧！"

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 始终在顶部 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| definition | Scene 2 | Scene 2 | 定义公式 |
| factor_table | Scene 3 | Scene 3 | 因数表格 |
| multiple_line | Scene 4 | Scene 4 | 倍数数轴 |
| rule_boxes | Scene 5 | Scene 5 | 特殊规律 |
| summary_table | Scene 6 | Scene 6 | 总结表格 |

---

## 时间轴总览
```
0-5s:    Scene 1 - 开场引入
5-15s:   Scene 2 - 因数与倍数定义
15-30s:  Scene 3 - 找因数（有限性）
30-45s:  Scene 4 - 找倍数（无限性）
45-57s:  Scene 5 - 特殊规律
57-69s:  Scene 6 - 总结与巩固
总时长: 约69秒
```

---

## 字体大小规范
```python
FONT_SIZES = {
    "title": 36,          # 场景标题
    "subtitle": 28,       # 副标题
    "formula": 32,        # 主要公式
    "body": 22,           # 说明文字
    "label": 20,          # 标签
    "small": 18,          # 小字
    "author": 20,         # 作者信息
}
```

---

## 关键技术点
1. **Table**: 用于展示因数和倍数的对比
2. **NumberLine**: 展示倍数的分布和无限性
3. **循环动画**: 检查因数时的逐个验证
4. **Indicate/Flash**: 高亮重要概念
5. **SurroundingRectangle**: 框选强调
6. **GrowArrow**: 表示无限延伸

---

## 注意事项
1. 六年级学生，语言要简单易懂
2. 用颜色区分因数（红）和倍数（绿）
3. 动画节奏要适中，给学生思考时间
4. 数字不要太大，避免计算困难
5. 多用视觉化元素，少用纯文字
6. 强调"相互依存"的关系，避免孤立理解
7. 特别注意1和0的特殊性说明要清晰