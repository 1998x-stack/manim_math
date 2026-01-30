# 因式分解——分组分解法 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 6 个
- 难度等级: 中等
- 目标年级: 七年级

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要公因式
COLOR_SECONDARY = "#e74c3c"    # 红色 - 第二组
COLOR_HIGHLIGHT = "#f39c12"    # 橙色 - 高亮强调
COLOR_SUCCESS = "#2ecc71"      # 绿色 - 最终答案
COLOR_AUXILIARY = "#95a5a6"    # 灰色 - 辅助线/说明
COLOR_BRACKET = "#9b59b6"      # 紫色 - 括号强调
```

## 核心公式
1. `ax + ay + bx + by = a(x+y) + b(x+y) = (a+b)(x+y)`
2. `x² - y² + x - y = (x+y)(x-y) + (x-y) = (x-y)(x+y+1)`

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力，提出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字)
3. 示例公式淡入

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` - "这个式子能分解吗?" |
| 1.0s | 公式显示 | `Write(formula)` - `ax + ay + bx + by` |
| 2.5s | 等待理解 | `Wait(1.5)` |
| 4.0s | 提示出现 | `FadeIn(hint)` - "试试分组!" |

### 清理
- FadeOut: hook_text, hint
- 保留: formula, author_info

---

## Scene 2: 方法介绍 (5-12秒)
**目的**: 解释分组分解法的核心思想

### 元素
1. 方法名称标题
2. 定义文字
3. 步骤示意

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 5.0s | 标题淡入 | `FadeIn(title)` - "分组分解法" |
| 5.5s | 定义显示 | `Write(definition)` |
| 7.0s | 核心思想 | `FadeIn(key_idea)` - "分组→提公因式→再提" |
| 9.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, definition, key_idea
- 保留: formula, author_info

---

## Scene 3: 例题1详解 - ax+ay+bx+by (12-35秒)
**目的**: 逐步演示第一个例子

### 元素
1. 原式: `ax + ay + bx + by`
2. 分组标记
3. 提取公因式过程
4. 最终答案

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 12.0s | 公式移到顶部 | `formula.animate.move_to(UP*4)` |
| 13.0s | 步骤1标题 | `FadeIn(step1_title)` - "第一步: 分组" |
| 13.5s | 用括号标记分组 | `Create(bracket1)` - (ax+ay) |
| 14.5s | 用括号标记分组 | `Create(bracket2)` - (bx+by) |
| 15.5s | 颜色高亮 | 第一组蓝色，第二组红色 |
| 17.0s | 步骤2标题 | `Transform(step_title)` - "第二步: 各组提公因式" |
| 18.0s | 第一组提取a | `Write(group1_result)` - `a(x+y)` |
| 19.5s | 第二组提取b | `Write(group2_result)` - `b(x+y)` |
| 21.0s | 观察提示 | `FadeIn(observation)` - "发现相同因式!" |
| 22.0s | 高亮(x+y) | 两个(x+y)闪烁黄色 |
| 24.0s | 步骤3标题 | `Transform(step_title)` - "第三步: 再次提公因式" |
| 25.0s | 最终变换 | `Transform` - `(a+b)(x+y)` |
| 27.0s | 答案高亮 | 绿色边框闪烁 |
| 28.5s | 验证提示 | `FadeIn(verify_text)` - "✓ 完成!" |
| 30.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: 所有步骤标记、括号、中间结果
- 保留: 最终答案框架

---

## Scene 4: 例题2详解 - x²-y²+x-y (35-55秒)
**目的**: 展示混合使用公式法的情况

### 元素
1. 原式: `x² - y² + x - y`
2. 分组标记
3. 公式法应用
4. 最终答案

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 35.0s | 清空屏幕 | `FadeOut(previous_content)` |
| 36.0s | 新题目出现 | `Write(formula2)` - `x² - y² + x - y` |
| 37.5s | 提示 | `FadeIn(hint2)` - "这次有点不同..." |
| 39.0s | 分组标记 | `Create(brackets)` - (x²-y²) + (x-y) |
| 40.5s | 步骤1 | `FadeIn(step_text)` - "第一组用平方差公式" |
| 42.0s | 公式变换 | `Transform` - (x+y)(x-y) |
| 44.0s | 第二组保持 | 显示 + (x-y) |
| 45.5s | 观察 | `FadeIn(observation2)` - "又发现(x-y)!" |
| 47.0s | 高亮公因式 | 两个(x-y)闪烁 |
| 48.5s | 最终提取 | `Transform` - `(x-y)(x+y+1)` |
| 50.5s | 答案显示 | 绿色边框 |
| 52.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有中间步骤
- 保留: 答案

---

## Scene 5: 方法总结 (55-65秒)
**目的**: 总结分组分解法的关键步骤

### 元素
1. 三步流程图
2. 关键要点

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 55.0s | 标题 | `FadeIn(summary_title)` - "分组分解三步曲" |
| 56.0s | 步骤1卡片 | `FadeIn(card1, shift=RIGHT)` - "适当分组" |
| 57.5s | 步骤2卡片 | `FadeIn(card2, shift=RIGHT)` - "各组分解" |
| 59.0s | 步骤3卡片 | `FadeIn(card3, shift=RIGHT)` - "再次提取" |
| 60.5s | 关键提示 | `FadeIn(key_tip)` - "分组后要出现公因式!" |
| 62.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有卡片

---

## Scene 6: 片尾关注 (65-75秒)
**目的**: 品牌展示，引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 65.0s | 作者名放大 | `Transform(author_info)` |
| 66.0s | ID显示 | `FadeIn(author_id)` - "@emptyandcalm" |
| 67.0s | 关注文字 | `FadeIn(follow_text)` - "关注我，获得更多数学技巧!" |
| 68.5s | 装饰动画 | 括号图标旋转 |
| 71.0s | 等待 | `Wait(2.0)` |
| 73.0s | 全部淡出 | `FadeOut(all)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 顶部常驻 |
| formula1 | Scene 1 | Scene 3 | 第一个例题 |
| formula2 | Scene 4 | Scene 4 | 第二个例题 |
| step_indicators | Scene 3, 4 | Scene 3, 4 | 步骤标记 |
| brackets | Scene 3, 4 | Scene 3, 4 | 分组括号 |
| summary_cards | Scene 5 | Scene 5 | 总结卡片 |

---

## 特殊注意事项

### 1. 颜色使用策略
- 第一组始终用蓝色 (#3498db)
- 第二组始终用红色 (#e74c3c)
- 公因式高亮用黄色/橙色 (#f39c12)
- 最终答案用绿色边框 (#2ecc71)

### 2. 动画节奏
- 分组阶段: 慢速，给学生思考时间 (1.5-2s停顿)
- 提取公因式: 中速，逐步展示 (1s每步)
- 最终变换: 稍快，强化记忆 (0.8s)

### 3. 文字说明
- 所有中文用 Text() + "Noto Sans CJK SC"
- 所有数学公式用 MathTex()
- 步骤标题 font_size=28
- 正文说明 font_size=22

### 4. 位置管理
- 主公式区: y ∈ [0, 4]
- 步骤说明区: y ∈ [-2, 0]
- 底部提示区: y ∈ [-5, -3]

### 5. 几何元素
本题目不涉及几何图形，主要是代数表达式的变换动画。