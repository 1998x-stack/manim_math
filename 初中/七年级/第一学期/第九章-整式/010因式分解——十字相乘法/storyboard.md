# 因式分解——十字相乘法 动画分镜脚本

<!-- /root/code/sss/media/videos/cross_multiplication/1920p60/CrossMultiplicationMethod.mp4 -->
## 元信息
- 目标时长: 80-95 秒
- 场景数量: 8 个
- 难度等级: 七年级 (中等偏上)
- 知识点: 十字相乘法因式分解

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要元素
COLOR_SECONDARY = "#e74c3c"      # 红色 - 交叉线/强调
COLOR_HIGHLIGHT = YELLOW          # 黄色 - 高亮
COLOR_SUCCESS = "#2ecc71"         # 绿色 - 成功/正确
COLOR_AUXILIARY = GRAY_B          # 灰色 - 辅助说明
COLOR_CROSS_LINE = "#e67e22"      # 橙色 - 十字交叉线
COLOR_BOX_BG = "#2c3e50"          # 深蓝灰 - 背景框
```

## 十字相乘法关键视觉元素
| 元素 | 说明 | 视觉表现 |
|------|------|---------|
| 十字框架 | 2×2网格 | 垂直线+水平线形成十字 |
| 交叉箭头 | 对角线相乘 | 从左上到右下，左下到右上 |
| 数字分解 | 分解系数和常数项 | 动态变换显示 |
| 相加验证 | 交叉积之和 | 水平箭头汇聚 |

## 动画时长分配
| 场景 | 时长 | 累计时长 |
|------|------|---------|
| Scene 1: 开场钩子 | 5s | 5s |
| Scene 2: 方法介绍 | 8s | 13s |
| Scene 3: 简单例题1 (x²+5x+6) | 15s | 28s |
| Scene 4: 验证过程 | 8s | 36s |
| Scene 5: 例题2 (x²-5x+6) | 12s | 48s |
| Scene 6: 复杂例题 (2x²+7x+3) | 20s | 68s |
| Scene 7: 技巧总结 | 12s | 80s |
| Scene 8: 片尾关注 | 8s | 88s |

---

## Scene 1: 开场钩子 (0-5s)
**目的**: 用一个看似复杂的题目吸引注意力

### 元素
1. 作者标识 (顶部, y=7)
2. 钩子问题 "如何快速分解?" (y=5.5)
3. 题目: 2x²+7x+3 (y=4)
4. 神秘的十字符号闪烁 (y=2)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_question)` |
| 1.0s | 题目表达式出现 | `Write(problem_expr)` |
| 2.0s | 问号闪烁 | `Flash(question_mark)` |
| 2.5s | 十字符号神秘出现 | `FadeIn(cross_symbol, scale=2)` |
| 3.5s | 提示 "用十字相乘法!" | `FadeIn(hint_text)` |

### 清理
- FadeOut: hook_question, problem_expr, question_mark, hint_text
- 保留: author_info, cross_symbol (缩小移至角落)

---

## Scene 2: 方法介绍 (5-13s)
**目的**: 介绍十字相乘法的基本原理和结构

### 元素
1. 标题 "十字相乘法" (y=6)
2. 通用公式 x²+(p+q)x+pq = (x+p)(x+q) (y=4.5)
3. 十字图示 (y=2)
4. 步骤说明 (y=-2到y=-4)

### 十字图示结构
```
     x    p
  ×  ─────┼─────
     x    q
     
对角相乘: x×q, x×p
相加: xq + xp = (p+q)x ✓
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 5.0s | 标题写入 | `Write(title)` |
| 5.8s | 通用公式出现 | `Write(general_formula)` |
| 7.0s | 十字框架绘制 | `Create(cross_frame)` |
| 7.8s | 填入x, x, p, q | `FadeIn(entries)` |
| 8.5s | 对角箭头动画 | `Create(diagonal_arrows)` |
| 9.5s | 步骤1: "找p,q使p×q=常数项" | `FadeIn(step_1)` |
| 10.3s | 步骤2: "p+q=一次项系数" | `FadeIn(step_2)` |
| 11.2s | 步骤3: "结果(x+p)(x+q)" | `FadeIn(step_3)` |

### 清理
- FadeOut: general_formula, cross_frame entries, steps
- 保留: title (缩小至顶部)

---

## Scene 3: 简单例题1 - x²+5x+6 (13-28s)
**目的**: 通过最简单的例子详细展示十字相乘法的每一步

### 元素
1. 例题标题 "例题1" (y=5.5)
2. 原式 x²+5x+6 (y=4)
3. 十字图框架 (y=1)
4. 分解过程动画
5. 结果 (x+2)(x+3) (y=-3)

### 十字图详细步骤
```
步骤1: 确定第一列 (x²的系数=1)
     x    ?
  ×  ─────┼─────
     x    ?

步骤2: 找两个数p,q使p×q=6
可能: (1,6), (2,3), (3,2), (6,1)

步骤3: 验证p+q=5
2+3=5 ✓

步骤4: 填入
     x    2
  ×  ─────┼─────
     x    3
     
步骤5: 交叉相乘
x×3=3x
x×2=2x
3x+2x=5x ✓
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 13.0s | 例题标题+原式 | `FadeIn(example_1_title), Write(original)` |
| 14.0s | 分析: "分解6=2×3" | `FadeIn(analysis_1)` |
| 15.0s | 数字6变换为2×3 | `Transform(six, two_times_three)` |
| 16.0s | 十字框架出现 | `Create(cross_grid)` |
| 16.8s | 填入左列: x, x | `FadeIn(left_x_entries)` |
| 17.5s | 尝试2和3 | `FadeIn(numbers_2_3)` |
| 18.5s | 绘制交叉箭头 | `Create(cross_arrows)` |
| 19.5s | 显示交叉积 | `FadeIn(cross_products)` |
| 20.5s | 计算: 3x+2x | `Write(sum_calculation)` |
| 21.5s | 验证: =5x ✓ | `FadeIn(verification_check)` |
| 22.5s | 结果出现 | `Write(result)` |
| 23.5s | 结果框高亮 | `SurroundingRectangle(result, GREEN)` |
| 24.5s | 对号 | `FadeIn(checkmark)` |

### 清理
- FadeOut: 所有中间步骤
- 保留: result (移至顶部小字)

---

## Scene 4: 验证过程 (28-36s)
**目的**: 展示如何验证答案的正确性

### 元素
1. 验证标题 "验证" (y=4.5)
2. 展开过程 (y=2)
3. 化简步骤 (y=0到y=-2)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 28.0s | 验证标题 | `Write(verify_title)` |
| 28.5s | 写出 (x+2)(x+3) | `Write(factored_form)` |
| 29.5s | FOIL展开动画 | `展示乘法分配` |
| 30.5s | = x²+3x+2x+6 | `Write(expanded)` |
| 31.5s | 合并同类项 | `Transform(middle_terms)` |
| 32.5s | = x²+5x+6 ✓ | `Write(final_check)` |
| 33.5s | 与原式对比 | `Arrow连接` |
| 34.5s | 完全匹配! | `Flash效果` |

### 清理
- FadeOut: 所有验证元素

---

## Scene 5: 例题2 - x²-5x+6 (36-48s)
**目的**: 展示负号情况的处理

### 元素
1. 例题标题 "例题2" (y=5.5)
2. 原式 x²-5x+6 (y=4)
3. 十字图 (y=1)
4. 特别提示: 注意符号! (y=-4)

### 关键点
```
分解6: 可选(1,6), (2,3), (-1,-6), (-2,-3)
需要: p+q=-5
选择: -2+(-3)=-5 ✓

     x    -2
  ×  ─────┼─────
     x    -3
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 36.0s | 例题2标题+原式 | `FadeIn, Write` |
| 37.0s | 强调负号 | `Indicate(minus_sign, RED)` |
| 38.0s | 分析: "两数积=6, 和=-5" | `FadeIn(analysis)` |
| 39.0s | 十字框架 | `Create(cross_grid)` |
| 40.0s | 尝试-2和-3 | `FadeIn(negative_numbers)` |
| 41.0s | 交叉相乘 | `Create(arrows)` |
| 42.0s | -3x+(-2x)=-5x ✓ | `Write(verification)` |
| 43.0s | 结果 (x-2)(x-3) | `Write(result)` |
| 44.5s | 符号提示框 | `FadeIn(tip_box)` |
| 45.5s | "负负得正!" | `Write(tip_text)` |

### 清理
- FadeOut: 所有元素
- 保留: result (顶部)

---

## Scene 6: 复杂例题 - 2x²+7x+3 (48-68s)
**目的**: 展示首项系数不为1的情况（挑战题）

### 元素
1. 挑战题标题 ⭐ (y=5.5)
2. 原式 2x²+7x+3 (y=4)
3. 扩展十字图 (y=1)
4. 双重分解过程

### 复杂十字图
```
步骤1: 分解2x² → 2x, x 或 x, 2x
步骤2: 分解3 → 1, 3 或 3, 1

尝试布局:
     2x    1
  ×  ─────┼─────
     x     3
     
交叉: 2x×3=6x, x×1=x
和: 6x+x=7x ✓

结果: (2x+1)(x+3)
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 48.0s | 挑战题标题 | `Write(challenge_title, GOLD)` |
| 48.8s | 原式出现 | `Write(original)` |
| 49.8s | 分析: "需要分解2和3" | `FadeIn(analysis)` |
| 50.8s | 显示2x²=2x·x | `Transform(two_x_squared)` |
| 51.8s | 显示3=1·3 | `Transform(three)` |
| 52.8s | 十字框架 | `Create(cross_grid)` |
| 53.5s | 尝试1: 2x,x,1,3 | `FadeIn(attempt_1)` |
| 54.5s | 交叉相乘 | `Create(arrows)` |
| 55.5s | 计算: 6x+x=7x ✓ | `Write(check)` |
| 56.5s | 成功高亮 | `Flash(GREEN)` |
| 57.5s | 结果 (2x+1)(x+3) | `Write(result)` |
| 59.0s | 另一种尝试(失败) | `灰色显示错误尝试` |
| 60.5s | 对比说明 | `Arrow指向正确方案` |
| 62.0s | 技巧提示 | `FadeIn(tip_box)` |
| 63.0s | "先试简单组合" | `Write(tip)` |

### 清理
- FadeOut: 所有中间步骤
- 保留: result

---

## Scene 7: 技巧总结 (68-80s)
**目的**: 总结十字相乘法的关键技巧和注意事项

### 元素
1. 总结标题 "技巧总结" (y=6)
2. 技巧卡片 (y=3到y=-3)
3. 流程图 (y=-4)

### 技巧卡片内容
```
技巧1: 先找因数对
      - 列出所有可能的p,q组合
      
技巧2: 验证和
      - p+q必须等于一次项系数
      
技巧3: 注意符号
      - 正正得正，负负得正
      - 正负得负
      
技巧4: 首项系数≠1时
      - 同时分解首项和常数项
      - 交叉相乘验证
      
技巧5: 多试几次
      - 不怕失败，找到正确组合
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 68.0s | 总结标题 | `Write(summary_title, GOLD)` |
| 69.0s | 技巧1卡片滑入 | `card_1.animate.shift(RIGHT*10)` |
| 70.0s | 技巧2卡片滑入 | `card_2.animate.shift(RIGHT*10)` |
| 71.0s | 技巧3卡片滑入 | `card_3.animate.shift(RIGHT*10)` |
| 72.0s | 技巧4卡片滑入 | `card_4.animate.shift(RIGHT*10)` |
| 73.0s | 技巧5卡片滑入 | `card_5.animate.shift(RIGHT*10)` |
| 74.0s | 所有卡片闪烁 | `Flash效果` |
| 75.5s | 流程图出现 | `Create(flowchart)` |
| 77.0s | 记忆口诀 | `FadeIn(mnemonic)` |
| 78.0s | "十字交叉乘，相加要相等" | `Write(slogan)` |

### 清理
- FadeOut: 所有元素，准备片尾

---

## Scene 8: 片尾关注 (80-88s)
**目的**: 引导关注，强化品牌

### 元素
1. 作者信息放大 (y=2)
2. 关注提示 (y=0)
3. 十字符号装饰动画 (环绕)
4. 小图标闪烁

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 80.0s | 作者信息居中放大 | `Transform(author_info)` |
| 81.0s | ID显示 | `FadeIn(author_id)` |
| 82.0s | 关注提示 | `Write(follow_text)` |
| 83.0s | 十字符号环绕 | `创建并旋转` |
| 84.5s | 例题缩略图 | `FadeIn(thumbnails)` |
| 86.0s | 全部闪烁 | `Flash效果` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 全程显示 |
| cross_symbol | Scene 1 | Scene 8 | 角标装饰 |
| example_1_result | Scene 3 | Scene 7 | 顶部小字 |
| example_2_result | Scene 5 | Scene 7 | 顶部小字 |
| challenge_result | Scene 6 | Scene 7 | 顶部小字 |
| cross_grid | 各例题 | 各例题 | 临时使用 |
| verification_steps | Scene 4 | Scene 4 | 临时验证 |

---

## 关键坐标参考
```
顶部安全区: y = 7 (作者信息)
标题区域: y = 5.5 到 6
主内容区: y = -3 到 5
十字图区域: y = -1 到 3
步骤说明: y = -3 到 -5
底部安全区: y < -6.5
```

## 字体大小规范
- 标题: 38
- 副标题: 30
- 公式: 32-36
- 例题: 28-32
- 步骤说明: 22-26
- 提示/技巧: 20-24
- 作者信息: 20

## 十字图尺寸规范
```python
CROSS_GRID_SIZE = 2.5  # 整体大小
CELL_WIDTH = 1.2
CELL_HEIGHT = 0.8
LINE_THICKNESS = 3
ARROW_THICKNESS = 4
NUMBER_FONT_SIZE = 32
```