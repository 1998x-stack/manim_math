# 中位数与众数教学动画 - 分镜脚本

## 元信息
- 目标时长: 55-60 秒
- 场景数量: 7 个
- 难度等级: 初中
- 知识点: 中位数、众数

## 颜色配置
```python
COLOR_MEDIAN = "#e74c3c"          # 红色 - 中位数
COLOR_MODE = "#3498db"            # 蓝色 - 众数
COLOR_DATA = "#2ecc71"            # 绿色 - 数据点
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
COLOR_BACKGROUND = "#1a1a2e"
```

## 数据定义清单
| 元素 | 数据源 | 存储变量 |
|------|--------|---------|
| 奇数数据集 | [3, 7, 5, 9, 2] | self.odd_data |
| 奇数排序后 | [2, 3, 5, 7, 9] | self.odd_sorted |
| 偶数数据集 | [4, 8, 2, 6, 5, 9] | self.even_data |
| 偶数排序后 | [2, 4, 5, 6, 8, 9] | self.even_sorted |
| 众数数据集 | [3, 5, 7, 5, 9, 5, 2] | self.mode_data |
| 极端值数据 | [5, 6, 7, 8, 100] | self.extreme_data |

## 公式验证清单
| 公式 | 用途 | 验证方法 |
|------|------|---------|
| 中位数(奇) = 第(n+1)/2个数 | n=5时，取第3个 | 验证索引=2 |
| 中位数(偶) = (第n/2 + 第n/2+1)/2 | n=6时，取第3、4个平均 | 验证索引=2,3 |
| 众数 = 出现次数最多的数 | 统计频数 | 验证max(频数) |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 "一组数据的中心在哪?"
3. 混乱的数据点

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 数据点随机出现 | `FadeIn(dots, lag_ratio=0.1)` | 1.0s |
| 2.1s | 数据点混乱移动 | `dots.animate.shift(random)` | 0.8s |
| 2.9s | 等待 | `Wait(0.5)` | 0.5s |

### 清理
- FadeOut: hook_text, dots
- 保留: author_info

---

## Scene 2: 中位数概念 - 奇数情况 (5-15秒)
**目的**: 展示奇数个数据的中位数求法

### 元素
1. 标题 "中位数 Median (奇数)"
2. 原始数据 [3, 7, 5, 9, 2]
3. 排序动画
4. 数轴展示
5. 中间位置标记
6. 公式 "中位数 = 第(n+1)/2个数"

### 数据计算
```python
odd_data = [3, 7, 5, 9, 2]
odd_sorted = [2, 3, 5, 7, 9]
n = 5
median_index = (n + 1) // 2 - 1  # Python索引从0开始，所以是2
median_value = odd_sorted[median_index]  # 5
```

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 5.0s | 标题写入 | `Write(title)` | 0.8s |
| 5.8s | 原始数据展示 | `FadeIn(data_boxes)` | 0.8s |
| 6.6s | 排序提示 | `Write(sort_text)` | 0.4s |
| 7.0s | 排序动画 | `data_boxes.animate.arrange()` | 1.2s |
| 8.2s | 标记中间位置 | `Create(middle_arrow)` | 0.5s |
| 8.7s | 高亮中位数 | `box[2].animate.set_color(RED)` | 0.4s |
| 9.1s | 公式展示 | `Write(formula)` | 1.0s |
| 10.1s | 计算示例 | `Write(calculation)` | 0.8s |
| 10.9s | 等待 | `Wait(1.0)` | 1.0s |

### 清理
- FadeOut: title, data_boxes, formula, calculation, sort_text, middle_arrow
- 保留: author_info

---

## Scene 3: 中位数概念 - 偶数情况 (15-25秒)
**目的**: 展示偶数个数据的中位数求法

### 元素
1. 标题 "中位数 Median (偶数)"
2. 原始数据 [4, 8, 2, 6, 5, 9]
3. 排序后 [2, 4, 5, 6, 8, 9]
4. 中间两个数标记
5. 平均值计算
6. 公式

### 数据计算
```python
even_data = [4, 8, 2, 6, 5, 9]
even_sorted = [2, 4, 5, 6, 8, 9]
n = 6
index1 = n // 2 - 1  # 2 (第3个)
index2 = n // 2      # 3 (第4个)
median = (even_sorted[index1] + even_sorted[index2]) / 2  # (5 + 6) / 2 = 5.5
```

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 15.0s | 标题写入 | `Write(title)` | 0.8s |
| 15.8s | 数据展示（已排序） | `FadeIn(data_boxes)` | 0.8s |
| 16.6s | 标记中间两个 | `Create(braces)` | 0.6s |
| 17.2s | 高亮两个数 | `boxes[2:4].animate.set_color(RED)` | 0.4s |
| 17.6s | 显示加法 | `Write(addition)` | 0.6s |
| 18.2s | 显示除法 | `Write(division)` | 0.6s |
| 18.8s | 显示结果 | `Write(result)` | 0.5s |
| 19.3s | 公式展示 | `Write(formula)` | 1.0s |
| 20.3s | 等待 | `Wait(1.0)` | 1.0s |

### 清理
- FadeOut: title, data_boxes, braces, addition, division, result, formula
- 保留: author_info

---

## Scene 4: 中位数性质 - 不受极端值影响 (25-33秒)
**目的**: 展示中位数的鲁棒性

### 元素
1. 标题 "中位数的特点"
2. 正常数据 [5, 6, 7, 8, 9]
3. 极端值数据 [5, 6, 7, 8, 100]
4. 对比展示

### 数据计算
```python
normal_data = [5, 6, 7, 8, 9]
normal_median = 7

extreme_data = [5, 6, 7, 8, 100]
extreme_median = 7  # 仍然是7！

normal_mean = (5 + 6 + 7 + 8 + 9) / 5 = 7.0
extreme_mean = (5 + 6 + 7 + 8 + 100) / 5 = 25.2  # 差异很大
```

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 25.0s | 标题写入 | `Write(title)` | 0.8s |
| 25.8s | 正常数据 | `FadeIn(normal_boxes)` | 0.6s |
| 26.4s | 标记中位数 | `normal_boxes[2].animate.set_color(RED)` | 0.4s |
| 26.8s | 显示中位数=7 | `Write(median_1)` | 0.4s |
| 27.2s | 极端数据 | `Transform(normal_boxes, extreme_boxes)` | 0.8s |
| 28.0s | 100闪烁提示 | `Flash(boxes[4])` | 0.3s |
| 28.3s | 中位数仍是7 | `Write(median_2)` | 0.5s |
| 28.8s | 对比平均数 | `Write(comparison)` | 1.0s |
| 29.8s | 总结文字 | `Write(summary)` | 0.8s |
| 30.6s | 等待 | `Wait(1.0)` | 1.0s |

### 清理
- FadeOut: title, boxes, median_1, median_2, comparison, summary
- 保留: author_info

---

## Scene 5: 众数概念 (33-43秒)
**目的**: 展示众数的定义和计算

### 元素
1. 标题 "众数 Mode"
2. 数据 [3, 5, 7, 5, 9, 5, 2]
3. 频数统计表
4. 高亮出现次数最多的数

### 数据计算
```python
mode_data = [3, 5, 7, 5, 9, 5, 2]
from collections import Counter
freq = Counter(mode_data)
# {3: 1, 5: 3, 7: 1, 9: 1, 2: 1}
mode = 5  # 出现3次
```

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 33.0s | 标题写入 | `Write(title)` | 0.8s |
| 33.8s | 数据展示 | `FadeIn(data_boxes)` | 0.8s |
| 34.6s | 频数统计动画 | `Create(freq_table)` | 1.2s |
| 35.8s | 逐个统计 | `counter_animation()` | 1.5s |
| 37.3s | 高亮5 | `freq_table[5].animate.set_color(BLUE)` | 0.4s |
| 37.7s | 标记众数 | `Write(mode_label)` | 0.5s |
| 38.2s | 定义文字 | `Write(definition)` | 1.0s |
| 39.2s | 等待 | `Wait(1.2)` | 1.2s |

### 清理
- FadeOut: title, data_boxes, freq_table, mode_label, definition
- 保留: author_info

---

## Scene 6: 中位数与众数对比 (43-51秒)
**目的**: 总结两个概念的异同和应用

### 元素
1. 标题 "中位数 vs 众数"
2. 对比表格
3. 应用场景

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 43.0s | 标题写入 | `Write(title)` | 0.8s |
| 43.8s | 中位数卡片 | `FadeIn(median_card)` | 0.6s |
| 44.4s | 众数卡片 | `FadeIn(mode_card)` | 0.6s |
| 45.0s | 特点对比 | `Write(features)` | 1.5s |
| 46.5s | 应用场景 | `Write(applications)` | 1.2s |
| 47.7s | 等待 | `Wait(1.0)` | 1.0s |

### 清理
- FadeOut: title, median_card, mode_card, features, applications
- 保留: author_info

---

## Scene 7: 片尾 (51-55秒)
**目的**: 品牌强化，引导关注

### 元素
1. 作者信息放大
2. "关注我，学更多数学技巧!"
3. 数据装饰

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 51.0s | 作者信息放大 | `author.animate.scale(1.5)` | 0.8s |
| 51.8s | 关注文字 | `Write(follow_text)` | 0.8s |
| 52.6s | 数字装饰 | `FadeIn(numbers)` | 0.6s |
| 53.2s | 等待 | `Wait(1.0)` | 1.0s |
| 54.2s | 全部淡出 | `FadeOut(VGroup(*all))` | 0.8s |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| odd_data_boxes | Scene 2 | Scene 2 | 奇数数据 |
| even_data_boxes | Scene 3 | Scene 3 | 偶数数据 |
| extreme_boxes | Scene 4 | Scene 4 | 极端值数据 |
| mode_freq_table | Scene 5 | Scene 5 | 频数表 |
| comparison_cards | Scene 6 | Scene 6 | 对比卡片 |

---

## 数据验证检查项
- [ ] 奇数中位数索引计算正确：(5+1)//2 - 1 = 2
- [ ] 偶数中位数索引计算正确：6//2 - 1 = 2, 6//2 = 3
- [ ] 众数频数统计正确：5出现3次
- [ ] 所有数据框在安全区域内
- [ ] 公式中使用 MathTex 的 \text{} 包裹中文
- [ ] 所有文字在边界内 (x∈[-4,4], y∈[-7,7])

---

## 特殊注意事项
1. **数据排序动画**: 使用 `AnimationGroup` 配合 `lag_ratio` 实现流畅排序
2. **中位数标记**: 使用 `Arrow` 或 `Brace` 清晰指示
3. **频数统计**: 使用表格或柱状图直观展示
4. **颜色区分**: 中位数用红色，众数用蓝色
5. **公式安全**: 
   - 中文必须在 `\text{}` 内
   - 分数使用 `\frac{}{}`
   - 数学符号正确转义
6. **动画节奏**: 计算步骤留足理解时间 (1-1.5秒)