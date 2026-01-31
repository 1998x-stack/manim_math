# 因式分解——分组分解法 动画分镜脚本

<!-- /root/code/sss/media/videos/factorization_grouping/1920p60/FactorizationGrouping.mp4 -->

## 元信息
- **目标时长**: 60-75秒
- **场景数量**: 7个
- **难度等级**: 中等
- **年级**: 七年级
- **知识点**: 分组分解法

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要公式
COLOR_SECONDARY = "#e74c3c"      # 红色 - 分组标识
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮强调
COLOR_SUCCESS = "#2ecc71"        # 绿色 - 成功/最终结果
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助元素
COLOR_GROUP_A = "#9b59b6"        # 紫色 - 第一组
COLOR_GROUP_B = "#f39c12"        # 橙色 - 第二组
```

## 核心教学流程
1. **开场钩子** - 引出问题困境
2. **概念介绍** - 什么是分组分解法
3. **例题1** - ax + ay + bx + by 的分组
4. **例题2** - x² - y² + x - y 的分组
5. **关键技巧** - 分组策略总结
6. **练习提示** - 鼓励练习
7. **片尾关注** - 作者信息

## 数学元素清单
| 元素 | 类型 | 说明 |
|------|------|------|
| 例题1原式 | MathTex | ax + ay + bx + by |
| 例题1分组 | MathTex | (ax+ay) + (bx+by) |
| 例题1提取1 | MathTex | a(x+y) + b(x+y) |
| 例题1最终 | MathTex | (a+b)(x+y) |
| 例题2原式 | MathTex | x² - y² + x - y |
| 例题2分组 | MathTex | (x²-y²) + (x-y) |
| 例题2提取1 | MathTex | (x+y)(x-y) + (x-y) |
| 例题2最终 | MathTex | (x-y)(x+y+1) |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识（顶部）
2. 钩子问题（大字）
3. 困难公式展示

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | y=7 |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | y=5.5 |
| 1.1s | 困难公式淡入 | `FadeIn(problem_eq)` | y=3 |
| 1.6s | 公式闪烁强调 | `Flash(problem_eq, color=YELLOW)` | y=3 |
| 2.6s | 提示文字 | `FadeIn(hint_text)` | y=1 |
| 3.6s | 等待 | `Wait(0.4)` | - |

### 具体内容
```python
# 钩子文字
hook_text = "这个式子怎么分解?"
# 困难公式
problem_eq = "ax + ay + bx + by = ?"
# 提示文字
hint_text = "用分组分解法!"
```

### 清理
- FadeOut: hook_text, hint_text
- 保留: author_info, problem_eq

### 坐标说明
- 作者信息: UP * 7
- 钩子文字: UP * 5.5
- 困难公式: UP * 3
- 提示文字: UP * 1

---

## Scene 2: 概念介绍 (8秒)
**目的**: 解释分组分解法的定义和策略

### 元素
1. 标题："分组分解法"
2. 定义文字
3. 策略要点（3条）

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 0.0s | 标题书写 | `Write(title)` | y=5 |
| 0.8s | 定义文字淡入 | `FadeIn(definition, shift=UP*0.3)` | y=3.5 |
| 1.8s | 策略1淡入 | `FadeIn(strategy_1)` | y=2 |
| 2.4s | 策略2淡入 | `FadeIn(strategy_2)` | y=1 |
| 3.0s | 策略3淡入 | `FadeIn(strategy_3)` | y=0 |
| 4.0s | 整体高亮 | 三条策略同时闪烁 | - |
| 5.5s | 等待理解 | `Wait(1.5)` | - |
| 7.0s | 清理 | `FadeOut(VGroup(...))` | - |

### 具体内容
```python
title = "分组分解法"
definition = "将多项式的项分组，使每组都能分解"

strategy_1 = "① 适当分组"
strategy_2 = "② 各组提取公因式"
strategy_3 = "③ 继续分解共同因式"
```

### 清理
- FadeOut: title, definition, strategy_1, strategy_2, strategy_3
- 保留: author_info

---

## Scene 3: 例题1 - 分组过程 (15秒)
**目的**: 详细展示 ax + ay + bx + by 的分组分解

### 元素
1. 例题标题
2. 原式
3. 分组示意（括号+颜色）
4. 分步骤公式

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 0.0s | 例题标题 | `Write(example_title)` | y=5.5 |
| 0.6s | 原式书写 | `Write(eq_step0)` | y=3.5 |
| 1.6s | 等待 | `Wait(0.5)` | - |
| 2.1s | 第一组高亮 | ax+ay 变紫色 | - |
| 2.6s | 第二组高亮 | bx+by 变橙色 | - |
| 3.1s | 添加括号 | `Create(brackets)` | - |
| 4.1s | 说明文字 | "分成两组" | y=2 |
| 5.1s | 变换到分组式 | `TransformMatchingTex(eq_step0, eq_step1)` | y=3.5 |
| 6.1s | 提示文字 | "提取公因式" | y=2 |
| 7.1s | 第一组提取 | a(x+y) 高亮 | - |
| 8.1s | 第二组提取 | b(x+y) 高亮 | - |
| 9.1s | 变换到提取式 | `TransformMatchingTex(eq_step1, eq_step2)` | y=3.5 |
| 10.1s | 标识公因式 | (x+y) 用方框 | - |
| 11.1s | 提示文字 | "继续提取(x+y)" | y=2 |
| 12.1s | 最终答案 | `TransformMatchingTex(eq_step2, eq_final)` | y=3.5 |
| 13.1s | 成功特效 | `Flash(eq_final, color=GREEN)` | - |
| 14.1s | 等待 | `Wait(1.0)` | - |

### 具体内容
```python
example_title = "例题1"
eq_step0 = MathTex(r"ax", r"+", r"ay", r"+", r"bx", r"+", r"by")
eq_step1 = MathTex(r"(", r"ax", r"+", r"ay", r")", r"+", r"(", r"bx", r"+", r"by", r")")
eq_step2 = MathTex(r"a", r"(", r"x", r"+", r"y", r")", r"+", r"b", r"(", r"x", r"+", r"y", r")")
eq_final = MathTex(r"(", r"a", r"+", r"b", r")", r"(", r"x", r"+", r"y", r")")
```

### 颜色标记策略
- 第一组 (ax+ay): COLOR_GROUP_A (紫色)
- 第二组 (bx+by): COLOR_GROUP_B (橙色)
- 公因式 (x+y): COLOR_HIGHLIGHT (黄色)

### 清理
- FadeOut: example_title, 所有说明文字, 方框
- 保留: eq_final (移到顶部作为参考)

---

## Scene 4: 例题2 - 公式法+提取 (15秒)
**目的**: 展示 x² - y² + x - y 的分组分解

### 元素
1. 例题标题
2. 原式
3. 分组示意
4. 公式法应用
5. 最终结果

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 0.0s | 例题标题 | `Write(example_title_2)` | y=5.5 |
| 0.6s | 原式书写 | `Write(eq2_step0)` | y=3.5 |
| 1.6s | 等待 | `Wait(0.5)` | - |
| 2.1s | 第一组高亮 | x²-y² 变紫色 | - |
| 2.6s | 第二组高亮 | x-y 变橙色 | - |
| 3.1s | 添加括号 | `Create(brackets)` | - |
| 4.1s | 变换到分组式 | `TransformMatchingTex(eq2_step0, eq2_step1)` | y=3.5 |
| 5.1s | 提示文字 | "平方差公式" | y=2 |
| 6.1s | 公式展示 | a²-b²=(a+b)(a-b) | y=1 |
| 7.1s | 应用公式 | x²-y² → (x+y)(x-y) | - |
| 8.1s | 变换 | `TransformMatchingTex(eq2_step1, eq2_step2)` | y=3.5 |
| 9.1s | 标识公因式 | (x-y) 用方框 | - |
| 10.1s | 提示文字 | "提取(x-y)" | y=2 |
| 11.1s | 最终答案 | `TransformMatchingTex(eq2_step2, eq2_final)` | y=3.5 |
| 12.1s | 成功特效 | `Flash(eq2_final, color=GREEN)` | - |
| 13.1s | 等待 | `Wait(1.0)` | - |

### 具体内容
```python
example_title_2 = "例题2"
eq2_step0 = MathTex(r"x^2", r"-", r"y^2", r"+", r"x", r"-", r"y")
eq2_step1 = MathTex(r"(", r"x^2", r"-", r"y^2", r")", r"+", r"(", r"x", r"-", r"y", r")")
eq2_step2 = MathTex(r"(", r"x", r"+", r"y", r")", r"(", r"x", r"-", r"y", r")", r"+", r"(", r"x", r"-", r"y", r")")
eq2_final = MathTex(r"(", r"x", r"-", r"y", r")", r"(", r"x", r"+", r"y", r"+", r"1", r")")
```

### 清理
- FadeOut: example_title_2, 所有说明文字, 公式展示, 方框
- 保留: eq2_final (移到顶部)

---

## Scene 5: 对比总结 (10秒)
**目的**: 并排展示两个例题，强调共同模式

### 元素
1. 两个例题并排
2. 箭头指示
3. 总结文字

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 0.0s | 标题 | `Write(summary_title)` | y=5.5 |
| 0.6s | 例题1移动 | eq_final → LEFT | x=-2.5, y=3 |
| 1.1s | 例题2移动 | eq2_final → RIGHT | x=2.5, y=3 |
| 1.6s | 箭头1 | 指向例题1 | - |
| 2.1s | 说明1 | "两组都有公因式" | y=1.5 |
| 2.6s | 箭头2 | 指向例题2 | - |
| 3.1s | 说明2 | "先公式法，再提取" | y=0.5 |
| 4.1s | 关键点 | "分组方式很关键!" | y=-1 |
| 5.1s | 高亮闪烁 | 两个例题同时闪烁 | - |
| 7.1s | 等待 | `Wait(1.0)` | - |

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 6: 技巧提示 (8秒)
**目的**: 给出分组分解法的实用技巧

### 元素
1. 技巧标题
2. 技巧卡片（3个）

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 0.0s | 标题 | `Write(tips_title)` | y=5.5 |
| 0.8s | 技巧1滑入 | `card_1.animate.shift(RIGHT*10)` | y=3 |
| 1.8s | 技巧2滑入 | `card_2.animate.shift(RIGHT*10)` | y=1.5 |
| 2.8s | 技巧3滑入 | `card_3.animate.shift(RIGHT*10)` | y=0 |
| 3.8s | 整体高亮 | 三个卡片闪烁 | - |
| 5.8s | 等待 | `Wait(1.0)` | - |

### 具体内容
```python
tips_title = "分组技巧"

tip_1 = "看是否有公因式可提"
tip_2 = "看能否用公式分解"
tip_3 = "尝试不同分组方式"
```

### 卡片设计
- 图标: Circle (小圆点)
- 标题: 技巧序号
- 内容: 技巧说明

### 清理
- FadeOut: 所有卡片和标题
- 保留: author_info

---

## Scene 7: 片尾关注 (7秒)
**目的**: 鼓励关注，提供后续学习提示

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰图标

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 0.0s | 作者名放大 | `Transform(author_info, large_name)` | y=2 |
| 0.8s | ID显示 | `FadeIn(author_id)` | y=1 |
| 1.3s | 关注文字 | `FadeIn(follow_text, scale=1.1)` | y=-0.5 |
| 2.3s | 装饰图标 | 4个数学符号旋转 | 围绕文字 |
| 3.3s | 旋转动画 | `Rotate(icons, PI)` | - |
| 5.3s | 等待 | `Wait(1.0)` | - |
| 6.3s | 全部淡出 | `FadeOut(everything)` | - |

### 具体内容
```python
large_name = "上海初高中数学直通车"
author_id = "@emptyandcalm"
follow_text = "关注我，掌握更多因式分解技巧!"

# 装饰图标：括号、加号、等号、乘号
icons = ["()", "+", "=", "×"]
```

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保留在顶部 |
| problem_eq | Scene 1 | Scene 2 | 开场问题 |
| eq_final (例题1) | Scene 3 | Scene 5 | 移到顶部保留 |
| eq2_final (例题2) | Scene 4 | Scene 5 | 移到顶部保留 |
| 所有临时说明文字 | 各场景 | 当前场景 | 及时清理 |
| 所有高亮框/箭头 | 各场景 | 当前场景 | 及时清理 |

---

## 时间节奏控制
- Scene 1: 4秒（快速抓住注意力）
- Scene 2: 8秒（概念解释，适度停留）
- Scene 3: 15秒（详细示范，关键场景）
- Scene 4: 15秒（第二个例题，同样重要）
- Scene 5: 10秒（对比总结，加深理解）
- Scene 6: 8秒（技巧提示，实用内容）
- Scene 7: 7秒（片尾关注）

**总时长**: 约67秒 ✓

---

## 关键注意事项

### 1. LaTeX 公式分离
- 中文用 `Text("...", font="Noto Sans CJK SC")`
- 数学符号用 `MathTex(r"...")`
- 避免混用导致编译错误

### 2. 颜色高亮策略
- 第一组: 紫色 (#9b59b6)
- 第二组: 橙色 (#f39c12)
- 公因式: 黄色 (YELLOW)
- 最终答案: 绿色 (#2ecc71)

### 3. 位置边界
- x 范围: [-4, 4]
- y 范围: [-7, 7]
- 顶部安全区: y = 7 (作者信息)
- 底部安全区: y = -7

### 4. 动画节奏
- 简单变换: 0.6-0.8秒
- 公式变换: 1.0秒
- 理解停顿: 0.5-1.0秒
- 关键步骤: 1.5-2.0秒

### 5. 元素清理
- 每个场景结束前必须清理临时元素
- 只保留需要跨场景的核心元素
- 使用 `VGroup` 批量管理临时元素

---

## 验证检查项
- [x] 总时长在60-75秒范围内
- [x] 所有公式都正确分离中文和LaTeX
- [x] 位置坐标在安全边界内
- [x] 颜色配置清晰一致
- [x] 元素生命周期明确
- [x] 动画节奏合理
- [x] 难点有足够停留时间
- [x] 开头有钩子，结尾有关注引导