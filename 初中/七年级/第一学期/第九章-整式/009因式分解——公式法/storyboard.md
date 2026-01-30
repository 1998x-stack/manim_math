# 因式分解——公式法 动画分镜脚本

<!-- /root/code/sss/media/videos/factorization_formulas/1920p60/FactorizationFormulas.mp4 -->
## 元信息
- 目标时长: 75-90 秒
- 场景数量: 7 个
- 难度等级: 七年级 (中等)
- 知识点: 公式法因式分解 (平方差公式、完全平方公式)

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主公式
COLOR_SECONDARY = "#e74c3c"      # 红色 - 强调项
COLOR_HIGHLIGHT = YELLOW          # 黄色 - 高亮
COLOR_SUCCESS = "#2ecc71"         # 绿色 - 成功/正确
COLOR_AUXILIARY = GRAY_B          # 灰色 - 辅助线/说明
COLOR_FORMULA_BG = "#2c3e50"      # 深蓝灰 - 公式背景
```

## 几何/公式预计算清单
| 元素 | 说明 | 存储变量 |
|------|------|---------|
| 平方差公式 | a²-b² = (a+b)(a-b) | formula_diff_of_squares |
| 完全平方公式1 | a²+2ab+b² = (a+b)² | formula_perfect_square_1 |
| 完全平方公式2 | a²-2ab+b² = (a-b)² | formula_perfect_square_2 |
| 例题1 | x²-9 | example_1 |
| 例题2 | x²+6x+9 | example_2 |
| 例题3 | 4x²-9y² | example_3 |

## 动画时长分配
| 场景 | 时长 | 累计时长 |
|------|------|---------|
| Scene 1: 开场钩子 | 5s | 5s |
| Scene 2: 平方差公式讲解 | 13s | 18s |
| Scene 3: 平方差公式例题 | 12s | 30s |
| Scene 4: 完全平方公式讲解 | 15s | 45s |
| Scene 5: 完全平方公式例题 | 15s | 60s |
| Scene 6: 综合例题 | 12s | 72s |
| Scene 7: 总结与关注 | 8s | 80s |

---

## Scene 1: 开场钩子 (0-5s)
**目的**: 吸引注意力，引出因式分解的神奇之处

### 元素
1. 作者标识 (顶部小字, y=7)
2. 钩子问题 "如何快速分解 x²-100?" (大字, y=5.5)
3. 三个公式卡片渐入 (y=2到y=-2)

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 持续显示 |
| 0.3s | 钩子问题书写 | `Write(hook_question, run_time=1.0)` | 大字吸引注意 |
| 1.5s | 问号闪烁 | `Flash(question_mark, color=YELLOW)` | 制造悬念 |
| 2.0s | 三个公式卡片依次滑入 | `card.animate.shift(RIGHT*10)` | 从左侧进入 |
| 4.5s | 提示文字 "掌握这三个公式就够了!" | `FadeIn(hint_text)` | y=-4 |

### 清理
- FadeOut: hook_question, question_mark, hint_text
- 保留: author_info, formula_cards (移动到顶部)

---

## Scene 2: 平方差公式讲解 (5-18s)
**目的**: 详细讲解平方差公式的结构和识别方法

### 元素
1. 标题 "平方差公式" (y=6)
2. 公式: a² - b² = (a+b)(a-b) (y=4, 分步展示)
3. 几何正方形动画 (视觉化理解)
4. 识别要点文字 (y=-4到y=-6)

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 5.0s | 标题写入 | `Write(title, run_time=0.8)` | "平方差公式" |
| 5.8s | 左侧公式出现 | `Write(formula_left, run_time=1.0)` | a² - b² |
| 6.8s | 高亮a²和b² | `Indicate(term_a), Indicate(term_b)` | 黄色闪烁 |
| 7.5s | 等号出现 | `FadeIn(equal_sign)` | - |
| 7.8s | 右侧因式出现 | `Write(formula_right, run_time=1.2)` | (a+b)(a-b) |
| 9.0s | 几何图形动画 | `Create(square_large), Create(square_small)` | 大正方形减小正方形 |
| 10.5s | 图形变换 | `Transform(area_diff, factored_rectangles)` | 面积差→长方形 |
| 12.0s | 识别要点1 | `FadeIn(point_1)` | "①两项相减" |
| 12.8s | 识别要点2 | `FadeIn(point_2)` | "②都是平方项" |
| 13.5s | 识别要点3 | `FadeIn(point_3)` | "③结构: □²-△²" |
| 15.0s | 公式整体高亮 | `Circumscribe(formula_group, color=YELLOW)` | 强调记忆 |

### 清理
- FadeOut: geometric_shapes, identification_points
- 保留: title, formula (移至顶部缩小)

---

## Scene 3: 平方差公式例题 (18-30s)
**目的**: 通过具体例题巩固平方差公式应用

### 元素
1. 例题标题 "例题1" (y=5.5)
2. 原式: x² - 9 (y=3.5)
3. 分步分解过程
4. 答案: (x+3)(x-3) (y=1)
5. 验证步骤 (可选)

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 18.0s | 例题标题出现 | `FadeIn(example_title)` | "例题1" |
| 18.3s | 原式书写 | `Write(original_expr, run_time=1.0)` | x² - 9 |
| 19.5s | 分析步骤1 | `FadeIn(step_1)` | "识别: x²和9=3²" |
| 20.5s | 高亮x² | `x_squared.animate.set_color(RED)` | - |
| 21.0s | 高亮9→3² | `Transform(nine, three_squared)` | 9变成3² |
| 22.0s | 分析步骤2 | `FadeIn(step_2)` | "应用公式: a²-b²=(a+b)(a-b)" |
| 23.0s | 对应关系 | `Arrow连接 x²→a², 3²→b²` | 虚线箭头 |
| 24.5s | 结果出现 | `TransformMatchingTex(original, result)` | (x+3)(x-3) |
| 25.5s | 答案框高亮 | `SurroundingRectangle(result, color=GREEN)` | 绿色边框 |
| 26.5s | 验证动画 | `(x+3)(x-3) → x²-3x+3x-9 → x²-9` | 展开验证 |
| 28.5s | 对号出现 | `FadeIn(checkmark, scale=2)` | ✓ |

### 清理
- FadeOut: example_title, all_steps, verification
- 保留: result (移至顶部小字)

---

## Scene 4: 完全平方公式讲解 (30-45s)
**目的**: 讲解两个完全平方公式的结构和区别

### 元素
1. 标题 "完全平方公式" (y=6)
2. 公式1: a² + 2ab + b² = (a+b)² (y=3.5)
3. 公式2: a² - 2ab + b² = (a-b)² (y=2)
4. 识别要点对比表 (y=-1到y=-5)

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 30.0s | 标题写入 | `Write(title, run_time=0.8)` | "完全平方公式" |
| 30.8s | 公式1左侧 | `Write(formula_1_left, run_time=1.2)` | a²+2ab+b² |
| 32.0s | 高亮三项 | `VGroup(a², 2ab, b²).set_color_by_gradient(RED, YELLOW, BLUE)` | 彩色渐变 |
| 33.0s | 公式1右侧 | `Write(formula_1_right, run_time=0.8)` | (a+b)² |
| 34.0s | 公式2左侧 | `Write(formula_2_left, run_time=1.2)` | a²-2ab+b² |
| 35.2s | 对比箭头 | `DoubleArrow(formula_1, formula_2)` | 指出区别 |
| 36.0s | 公式2右侧 | `Write(formula_2_right, run_time=0.8)` | (a-b)² |
| 37.0s | 识别要点标题 | `FadeIn(key_points_title)` | "识别关键" |
| 37.5s | 要点1 | `FadeIn(point_1)` | "①三项式" |
| 38.2s | 要点2 | `FadeIn(point_2)` | "②首末是平方项" |
| 39.0s | 要点3 | `FadeIn(point_3)` | "③中间项=±2ab" |
| 40.0s | 要点4 | `FadeIn(point_4)` | "④+号→(a+b)², -号→(a-b)²" |
| 41.5s | 对比表格 | `Create(comparison_table)` | 列出+/-对应关系 |
| 43.5s | 强调中间符号 | `Indicate(plus_sign), Indicate(minus_sign)` | 闪烁强调 |

### 清理
- FadeOut: comparison_table, key_points
- 保留: title, both_formulas (移至顶部缩小)

---

## Scene 5: 完全平方公式例题 (45-60s)
**目的**: 通过例题展示完全平方公式应用

### 元素
1. 例题标题 "例题2" (y=5.5)
2. 原式: x² + 6x + 9 (y=3.5)
3. 分步识别过程
4. 答案: (x+3)² (y=1)

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 45.0s | 例题标题 | `FadeIn(example_title)` | "例题2" |
| 45.3s | 原式书写 | `Write(original_expr, run_time=1.0)` | x²+6x+9 |
| 46.5s | 步骤1: 检查首项 | `Circumscribe(x_squared, color=RED)` | "首项: x²=x²" |
| 47.5s | 步骤2: 检查末项 | `Circumscribe(nine, color=BLUE)` | "末项: 9=3²" |
| 48.5s | 步骤3: 检查中间项 | `Circumscribe(six_x, color=YELLOW)` | "中间: 6x=2·x·3✓" |
| 50.0s | 公式对应 | `Arrow连接到公式a²+2ab+b²` | 虚线连接 |
| 51.0s | 标注对应关系 | `a=x, b=3` | 小字注释 |
| 52.5s | 结果变换 | `TransformMatchingTex(original, result)` | (x+3)² |
| 53.5s | 答案高亮 | `SurroundingRectangle(result, color=GREEN)` | 绿色边框 |
| 54.5s | 验证展开 | `(x+3)² → x²+2·x·3+3² → x²+6x+9` | 反向验证 |
| 57.0s | 对号确认 | `FadeIn(checkmark, scale=2)` | ✓ |
| 58.0s | 技巧提示 | `FadeIn(tip)` | "技巧: 中间项是关键!" |

### 清理
- FadeOut: example_title, all_steps, tip
- 保留: result (移至顶部)

---

## Scene 6: 综合例题 (60-72s)
**目的**: 展示稍复杂的例题，综合应用两个公式

### 元素
1. 例题标题 "例题3: 挑战题" (y=5.5)
2. 原式: 4x² - 9y² (y=3.5)
3. 分步分解
4. 答案: (2x+3y)(2x-3y) (y=1)

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 60.0s | 挑战题标题 | `Write(challenge_title, color=GOLD)` | "挑战题" 金色 |
| 60.5s | 原式书写 | `Write(original_expr, run_time=1.0)` | 4x²-9y² |
| 61.7s | 识别平方差 | `FadeIn(hint)` | "平方差结构!" |
| 62.5s | 分解4x² | `Transform(four_x_squared, two_x_squared)` | 4x²=(2x)² |
| 63.5s | 分解9y² | `Transform(nine_y_squared, three_y_squared)` | 9y²=(3y)² |
| 64.5s | 重写表达式 | `TransformMatchingTex()` | (2x)²-(3y)² |
| 65.5s | 应用公式 | `Arrow指向平方差公式` | 对应a=2x, b=3y |
| 67.0s | 结果出现 | `Write(result, run_time=1.2)` | (2x+3y)(2x-3y) |
| 68.5s | 答案框 | `SurroundingRectangle(result, color=GOLD)` | 金色强调 |
| 69.5s | 庆祝动画 | `Flash连续闪烁 + 星星特效` | 完成挑战 |

### 清理
- FadeOut: challenge_title, all_steps
- 保留: result

---

## Scene 7: 总结与关注 (72-80s)
**目的**: 总结三个公式，引导关注

### 元素
1. 总结标题 "三大公式助你快速分解!" (y=5)
2. 三个公式卡片整齐排列 (y=2到y=-2)
3. 口诀/记忆技巧 (y=-4)
4. 作者信息放大 (y=0)
5. 关注提示 (y=-6)

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 72.0s | 总结标题 | `Write(summary_title, color=GOLD)` | 金色标题 |
| 72.8s | 三个公式卡片集中 | `VGroup(cards).arrange(DOWN).move_to(UP*1)` | 整齐排列 |
| 73.8s | 公式卡片依次闪烁 | `Flash(card_1), Flash(card_2), Flash(card_3)` | 强调重点 |
| 75.0s | 记忆口诀 | `FadeIn(mnemonic, shift=UP*0.3)` | "两平方相减→平方差" |
| 76.0s | 口诀2 | `FadeIn(mnemonic_2)` | "三项式中间2ab→完全平方" |
| 77.0s | 作者信息放大 | `author_info.animate.scale(1.5).move_to(CENTER)` | 居中放大 |
| 78.0s | 关注提示 | `Write(follow_text)` | "关注我,掌握更多技巧!" |
| 78.8s | 装饰动画 | `公式图标环绕旋转` | 视觉效果 |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保持顶部显示 |
| formula_diff_of_squares | Scene 2 | Scene 7 | 平方差公式 |
| formula_perfect_square_1 | Scene 4 | Scene 7 | 完全平方公式(+) |
| formula_perfect_square_2 | Scene 4 | Scene 7 | 完全平方公式(-) |
| geometric_shapes | Scene 2 | Scene 2 | 几何可视化 |
| example_1 | Scene 3 | Scene 3 | 例题1 |
| example_2 | Scene 5 | Scene 5 | 例题2 |
| example_3 | Scene 6 | Scene 6 | 例题3 |
| summary_cards | Scene 7 | Scene 7 | 总结卡片 |

---

## 关键坐标参考
```
顶部安全区: y = 7 (作者信息)
标题区域: y = 5.5 到 6
主内容区: y = -3 到 5
公式展示: y = 2 到 4
步骤说明: y = -1 到 -3
提示文字: y = -4 到 -6
底部安全区: y < -6.5
```

## 字体大小规范
- 标题: 36-42
- 公式: 32-36
- 例题: 28-32
- 步骤说明: 22-26
- 提示/注释: 18-22
- 作者信息: 20