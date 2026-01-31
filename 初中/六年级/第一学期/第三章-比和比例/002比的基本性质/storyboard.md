# 比的基本性质 - 动画分镜脚本

<!-- /root/code/sss/media/videos/ratio_properties/1920p60/RatioProperties.mp4 -->

## 元信息
- 目标时长: 60-70 秒
- 场景数量: 6 个
- 难度等级: 中等
- 目标观众: 六年级学生
- 主题: 比的基本性质及其应用

## 颜色配置
```python
COLOR_RATIO_A = "#3498db"       # 蓝色 - 比的前项
COLOR_RATIO_B = "#e74c3c"       # 红色 - 比的后项
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮重点
COLOR_PROPERTY = "#2ecc71"      # 绿色 - 性质/规律
COLOR_MULTIPLY = "#9b59b6"      # 紫色 - 乘法操作
COLOR_DIVIDE = "#f39c12"        # 橙色 - 除法操作
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助元素
COLOR_BACKGROUND = "#1a1a2e"    # 深蓝背景
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 比例条左端 | LEFT * 3 | self.bar_left |
| 比例条右端 | RIGHT * 3 | self.bar_right |
| 前项位置 | UP * 2 + LEFT * 2 | self.pos_a |
| 后项位置 | UP * 2 + RIGHT * 2 | self.pos_b |
| 公式中心 | ORIGIN | self.formula_center |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 吸引注意力，引出比的概念

### 元素
1. 作者标识 (顶部)
2. 钩子问题
3. 两个数字展示比: 4:6

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子问题书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 数字4淡入 | `FadeIn(num_4, scale=0.5)` | 0.4s |
| 1.5s | 冒号淡入 | `FadeIn(colon)` | 0.2s |
| 1.7s | 数字6淡入 | `FadeIn(num_6, scale=0.5)` | 0.4s |
| 2.1s | 整体闪烁 | `Flash(ratio_group)` | 0.4s |
| 2.5s | 问题文字 | `FadeIn(question)` | 0.5s |
| 3.0s | 等待 | `Wait(1.0)` | 1.0s |

### 文案
- 钩子: "比是什么?"
- 展示: "4 : 6"
- 问题: "这个比能化简吗?"

### 清理
- FadeOut: hook_text, question
- 保留: ratio (4:6), author_info

---

## Scene 2: 比的基本性质 - 乘法 (10秒)
**目的**: 演示比的前项和后项同时乘以同一个数，比值不变

### 元素
1. 标题: "比的基本性质"
2. 原比例: 4:6
3. 乘法操作演示
4. 新比例: 8:12

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题书写 | `Write(title)` | 0.6s |
| 0.6s | 性质说明 | `FadeIn(property_text)` | 0.5s |
| 1.1s | 原比例移到左侧 | `ratio.animate.move_to(LEFT*2 + UP*2)` | 0.6s |
| 1.7s | 显示×2操作 | `FadeIn(multiply_by_2)` | 0.5s |
| 2.2s | 箭头出现 | `GrowArrow(arrow)` | 0.4s |
| 2.6s | 4×2动画 | `Transform(4, 8) with highlight` | 0.8s |
| 3.4s | 6×2动画 | `Transform(6, 12) with highlight` | 0.8s |
| 4.2s | 新比例出现 | `FadeIn(new_ratio: 8:12)` | 0.6s |
| 4.8s | 等号强调 | `Write(equals_sign)` | 0.4s |
| 5.2s | 公式显示 | `Write(formula: 4:6 = 8:12)` | 1.0s |
| 6.2s | 说明文字 | `FadeIn(explanation)` | 0.5s |
| 6.7s | 等待理解 | `Wait(2.5)` | 2.5s |

### 公式
```python
formula = MathTex(r"4:6 = 8:12")
property_formula = MathTex(r"a:b = (a \times k):(b \times k)")
```

### 清理
- FadeOut: 演示元素
- 保留: 概念理解

---

## Scene 3: 比的基本性质 - 除法 (10秒)
**目的**: 演示比的前项和后项同时除以同一个数，比值不变

### 元素
1. 原比例: 12:18
2. 除法操作演示
3. 化简后: 2:3

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 新例子引入 | `FadeIn(new_example_text)` | 0.5s |
| 0.5s | 12:18出现 | `Write(ratio_12_18)` | 0.6s |
| 1.1s | ÷6操作提示 | `FadeIn(divide_by_6)` | 0.5s |
| 1.6s | 找公因数说明 | `FadeIn(gcd_hint)` | 0.5s |
| 2.1s | 箭头 | `GrowArrow(arrow)` | 0.4s |
| 2.5s | 12÷6动画 | `Transform(12, 2) with color change` | 0.8s |
| 3.3s | 18÷6动画 | `Transform(18, 3) with color change` | 0.8s |
| 4.1s | 结果2:3 | `FadeIn(simplified_ratio)` | 0.6s |
| 4.7s | 等号 | `Write(equals)` | 0.4s |
| 5.1s | 完整公式 | `Write(formula: 12:18 = 2:3)` | 1.0s |
| 6.1s | "最简整数比" | `FadeIn(simplest_form_text)` | 0.6s |
| 6.7s | 等待 | `Wait(2.5)` | 2.5s |

### 数据
- GCD(12, 18) = 6
- 12 ÷ 6 = 2
- 18 ÷ 6 = 3

### 清理
- FadeOut: 所有元素
- 准备下一场景

---

## Scene 4: 视觉化演示 - 比例条 (12秒)
**目的**: 用视觉化方式展示比值不变的概念

### 元素
1. 比例条 (4:6)
2. 分段标记
3. 变换到 (2:3)
4. 比值相等验证

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `Write(visualization_title)` | 0.5s |
| 0.5s | 比例条出现 | `Create(ratio_bar)` | 0.8s |
| 1.3s | 分成4+6段 | `Create(segments, lag_ratio=0.1)` | 1.2s |
| 2.5s | 标注4和6 | `FadeIn(label_4, label_6)` | 0.5s |
| 3.0s | 计算比值 | `Write(ratio_value: 4/6 = 0.667)` | 0.8s |
| 3.8s | 等待 | `Wait(0.8)` | 0.8s |
| 4.6s | 重新分组动画 | `Transform(10段 → 5段)` | 1.2s |
| 5.8s | 标注2和3 | `FadeIn(label_2, label_3)` | 0.5s |
| 6.3s | 计算比值 | `Write(ratio_value: 2/3 = 0.667)` | 0.8s |
| 7.1s | 高亮相等 | `Indicate(both_ratios)` | 0.6s |
| 7.7s | 结论 | `FadeIn(conclusion)` | 0.5s |
| 8.2s | 等待 | `Wait(3.0)` | 3.0s |

### 比例条设计
```python
# 总长度
total_length = 6
bar_height = 0.4

# 4:6 的情况 (10段，每段0.6)
segments_10 = [Rectangle(width=0.6, height=bar_height) for _ in range(10)]
# 前4段蓝色，后6段红色

# 2:3 的情况 (5段，每段1.2)
segments_5 = [Rectangle(width=1.2, height=bar_height) for _ in range(5)]
# 前2段蓝色，后3段红色
```

### 清理
- FadeOut: 所有元素

---

## Scene 5: 与分数性质的联系 (8秒)
**目的**: 建立比与分数的联系

### 元素
1. 比的形式: 4:6
2. 分数形式: 4/6
3. 对比展示
4. 性质类比

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `Write(connection_title)` | 0.6s |
| 0.6s | 比4:6 | `Write(ratio_form)` | 0.5s |
| 1.1s | 转换符号 | `FadeIn(conversion_arrow)` | 0.3s |
| 1.4s | 分数4/6 | `Write(fraction_form)` | 0.5s |
| 1.9s | 并排对比 | `Arrange(ratio, fraction, RIGHT)` | 0.6s |
| 2.5s | 性质1 | `FadeIn(property_1)` | 0.8s |
| 3.3s | 性质2 | `FadeIn(property_2)` | 0.8s |
| 4.1s | 高亮相似性 | `Indicate(similarities)` | 0.6s |
| 4.7s | 结论 | `FadeIn(conclusion_text)` | 0.5s |
| 5.2s | 等待 | `Wait(2.0)` | 2.0s |

### 对比内容
- 比: a:b → (a×k):(b×k)
- 分数: a/b → (a×k)/(b×k)
- 结论: "比的性质类似于分数的基本性质"

### 清理
- FadeOut: 所有元素

---

## Scene 6: 总结与片尾 (8秒)
**目的**: 巩固知识点，引导关注

### 元素
1. 知识点总结卡片
2. 示例回顾
3. 作者信息
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 总结标题 | `Write(summary_title)` | 0.6s |
| 0.6s | 要点1滑入 | `card_1.animate.shift(RIGHT*10)` | 0.5s |
| 1.1s | 要点2滑入 | `card_2.animate.shift(RIGHT*10)` | 0.5s |
| 1.6s | 要点3滑入 | `card_3.animate.shift(RIGHT*10)` | 0.5s |
| 2.1s | 示例回顾 | `FadeIn(example_recap)` | 0.6s |
| 2.7s | 等待 | `Wait(0.8)` | 0.8s |
| 3.5s | 淡出总结 | `FadeOut(summary_group)` | 0.5s |
| 4.0s | 作者放大 | `author.animate.scale(2).move_to(UP)` | 0.6s |
| 4.6s | 关注文字 | `FadeIn(follow_text)` | 0.5s |
| 5.1s | 装饰 | `LaggedStart(icons)` | 0.8s |
| 5.9s | 等待 | `Wait(1.3)` | 1.3s |

### 总结要点
1. "比的前项和后项同乘一个数，比值不变"
2. "比的前项和后项同除一个数，比值不变"
3. "利用这个性质可以化简比"

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 持续存在 |
| ratio_4_6 | Scene 1 | Scene 2 | 初始比例 |
| ratio_8_12 | Scene 2 | Scene 2 | 乘法结果 |
| ratio_12_18 | Scene 3 | Scene 3 | 除法示例 |
| ratio_2_3 | Scene 3 | Scene 4 | 化简结果 |
| ratio_bar | Scene 4 | Scene 4 | 视觉化条形图 |
| comparison | Scene 5 | Scene 5 | 比与分数对比 |
| summary_cards | Scene 6 | Scene 6 | 总结卡片 |

---

## 时长分配检查
- Scene 1: 4秒
- Scene 2: 10秒
- Scene 3: 10秒
- Scene 4: 12秒
- Scene 5: 8秒
- Scene 6: 8秒
- **总计: 52秒** (符合45-90秒范围)

---

## 难点停留策略
1. **比的性质理解** (Scene 2): 停留2.5秒，展示乘法过程
2. **除法化简** (Scene 3): 停留2.5秒，强调找公因数
3. **视觉化理解** (Scene 4): 停留3秒，看比例条变化
4. **性质类比** (Scene 5): 停留2秒，理解与分数的联系

---

## 视觉设计notes
1. **数字大小**: 比的数字字号48，公式字号28，说明字号22
2. **颜色一致性**: 
   - 前项始终为蓝色
   - 后项始终为红色
   - 操作符号为紫色/橙色
   - 结果/性质为绿色
3. **动画速度**: 
   - 变换: 0.8秒
   - 淡入淡出: 0.4-0.6秒
   - 理解停顿: 2-3秒
4. **布局**: 保持在安全区域内 y∈[-6, 7], x∈[-4, 4]