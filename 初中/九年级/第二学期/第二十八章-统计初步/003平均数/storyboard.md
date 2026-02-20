# 平均数教学动画 - 分镜脚本

## 元信息
- 目标时长: 70-85 秒
- 场景数量: 7 个
- 难度等级: 初中
- 知识点: 算术平均数、加权平均数、极端值影响

## 颜色配置
```python
COLOR_ARITHMETIC_MEAN = "#3498db"   # 蓝色 - 算术平均数
COLOR_WEIGHTED_MEAN = "#e74c3c"     # 红色 - 加权平均数
COLOR_DATA_POINT = "#2ecc71"        # 绿色 - 数据点
COLOR_EXTREME = "#f39c12"           # 橙色 - 极端值
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
COLOR_BACKGROUND = "#1a1a2e"
```

## 数据定义清单
| 元素 | 数据源 | 存储变量 |
|------|--------|---------|
| 算术平均数示例 | [6, 7, 8, 9, 10] | self.simple_data |
| 加权平均数示例 | 平时80, 期中85, 期末90 | self.weighted_scores |
| 权重 | 30%, 30%, 40% | self.weights |
| 极端值对比 | [6,7,8,9,10] vs [6,7,8,9,50] | self.normal_data, self.extreme_data |

## 公式验证清单
| 公式 | 用途 | 验证方法 |
|------|------|---------|
| x̄ = (x₁+x₂+...+xₙ)/n | 算术平均数 | 验证计算结果 |
| x̄ = Σ(xᵢfᵢ)/Σfᵢ | 加权平均数 | 验证加权计算 |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 引出生活中的平均数问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 "班级平均分是多少？"
3. 5个学生成绩卡片

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子问题书写 | `Write(question)` | 0.8s |
| 1.1s | 成绩卡片依次出现 | `FadeIn(cards, lag_ratio=0.2)` | 1.0s |
| 2.1s | 数字高亮 | `Indicate(scores)` | 0.5s |
| 2.6s | 等待 | `Wait(0.8)` | 0.8s |

### 数据
```python
scores = [75, 82, 88, 79, 91]  # 5个学生成绩
```

### 清理
- FadeOut: question, cards (保留数字转换到下一场景)
- 保留: author_info

---

## Scene 2: 算术平均数概念 (5-15秒)
**目的**: 展示算术平均数的定义和可视化

### 元素
1. 标题 "算术平均数"
2. 数轴 (0-100分)
3. 5个数据点 (在数轴上)
4. 平均值位置标记
5. 公式

### 数据计算
```python
data = [6, 7, 8, 9, 10]  # 简化数据便于展示
mean = sum(data) / len(data) = 8.0
positions = [6, 7, 8, 9, 10]  # 数轴上的位置
```

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 5.0s | 标题写入 | `Write(title)` | 0.8s |
| 5.8s | 数轴绘制 | `Create(number_line)` | 1.0s |
| 6.8s | 数据点依次出现 | `FadeIn(dots, lag_ratio=0.2)` | 1.0s |
| 7.8s | 标注数值 | `FadeIn(labels)` | 0.5s |
| 8.3s | 平衡点概念 | 支点动画 | 1.0s |
| 9.3s | 平均值标记 | `Create(mean_line)` | 0.8s |
| 10.1s | 公式展示 | `Write(formula)` | 1.0s |
| 11.1s | 等待 | `Wait(1.2)` | 1.2s |

### 清理
- FadeOut: number_line, dots, mean_line, formula
- 保留: title (移到顶部), author_info

---

## Scene 3: 算术平均数计算 (15-28秒)
**目的**: 动画展示计算过程

### 元素
1. 数据列表 [6, 7, 8, 9, 10]
2. 求和过程动画
3. 除以个数
4. 结果

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 15.0s | 数据排列 | `Arrange(numbers)` | 0.8s |
| 15.8s | 公式出现 | `Write(formula_template)` | 1.0s |
| 16.8s | 数字移入分子 | `Transform(nums, numerator)` | 1.2s |
| 18.0s | 加号连接 | `Create(plus_signs)` | 0.8s |
| 18.8s | 求和结果 | `Transform(sum_expr, result)` | 1.0s |
| 19.8s | 分母n=5 | `Write(denominator)` | 0.6s |
| 20.4s | 除法计算 | `Write(division)` | 0.8s |
| 21.2s | 最终结果 | `Write(final_result)` | 0.8s |
| 22.0s | 高亮答案 | `Indicate(answer)` | 0.5s |
| 22.5s | 等待 | `Wait(1.5)` | 1.5s |

### 计算验证
```python
data = [6, 7, 8, 9, 10]
sum_value = 40
n = 5
mean = 40 / 5 = 8.0
```

### 清理
- FadeOut: 所有计算元素
- 保留: author_info

---

## Scene 4: 加权平均数 (28-45秒)
**目的**: 引入权重概念，展示加权平均数

### 元素
1. 标题 "加权平均数"
2. 场景：考试成绩
3. 三次成绩：平时80、期中85、期末90
4. 权重：30%、30%、40%
5. 计算过程
6. 公式

### 数据计算
```python
scores = [80, 85, 90]
weights = [0.3, 0.3, 0.4]
weighted_mean = (80*0.3 + 85*0.3 + 90*0.4) / (0.3 + 0.3 + 0.4)
              = (24 + 25.5 + 36) / 1.0
              = 85.5
```

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 28.0s | 标题写入 | `Write(title)` | 0.8s |
| 28.8s | 场景说明 | `FadeIn(context)` | 0.6s |
| 29.4s | 成绩卡片出现 | `FadeIn(score_cards, lag_ratio=0.2)` | 1.2s |
| 30.6s | 权重标注 | `Write(weight_labels)` | 1.0s |
| 31.6s | 公式展示 | `Write(formula)` | 1.2s |
| 32.8s | 计算每项 | `Write(calculations, lag_ratio=0.3)` | 1.5s |
| 34.3s | 求和 | `Write(sum_result)` | 0.8s |
| 35.1s | 最终结果 | `Write(final_answer)` | 0.8s |
| 35.9s | 对比说明 | `FadeIn(comparison)` | 0.6s |
| 36.5s | 等待 | `Wait(2.0)` | 2.0s |

### 对比
```
算术平均数: (80+85+90)/3 = 85.0
加权平均数: 80×30% + 85×30% + 90×40% = 85.5
```

### 清理
- FadeOut: 所有加权相关元素
- 保留: author_info

---

## Scene 5: 极端值影响 (45-60秒)
**目的**: 展示平均数易受极端值影响的特性

### 元素
1. 标题 "平均数的特点"
2. 对比组：正常数据 vs 含极端值数据
3. 数轴可视化
4. 计算对比

### 数据
```python
normal_data = [6, 7, 8, 9, 10]
normal_mean = 8.0

extreme_data = [6, 7, 8, 9, 50]  # 最后一个是极端值
extreme_mean = 16.0

差异 = 16.0 - 8.0 = 8.0
```

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 45.0s | 标题写入 | `Write(title)` | 0.8s |
| 45.8s | 正常数据展示 | `Create(normal_group)` | 1.0s |
| 46.8s | 正常平均值 | `Write(normal_mean)` | 0.8s |
| 47.6s | 引入极端值 | `Transform(10→50)` | 1.0s |
| 48.6s | 极端值标注 | `Indicate(extreme_value)` | 0.5s |
| 49.1s | 重新计算 | `Write(new_calculation)` | 1.2s |
| 50.3s | 新平均值 | `Write(extreme_mean)` | 0.8s |
| 51.1s | 对比箭头 | `Create(comparison_arrow)` | 0.6s |
| 51.7s | 说明文字 | `FadeIn(explanation)` | 0.8s |
| 52.5s | 警告提示 | `Write(warning)` | 0.8s |
| 53.3s | 等待 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: 所有对比元素
- 保留: author_info

---

## Scene 6: 总结对比 (60-72秒)
**目的**: 总结三个要点

### 元素
1. 标题 "平均数知识总结"
2. 三个要点卡片
3. 公式卡片

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 60.0s | 标题写入 | `Write(title)` | 0.8s |
| 60.8s | 要点1 | `FadeIn(point1)` | 0.8s |
| 61.6s | 要点2 | `FadeIn(point2)` | 0.8s |
| 62.4s | 要点3 | `FadeIn(point3)` | 0.8s |
| 63.2s | 公式对比 | `FadeIn(formulas)` | 1.0s |
| 64.2s | 关键提示 | `Write(key_point)` | 0.8s |
| 65.0s | 等待 | `Wait(2.0)` | 2.0s |

### 三个要点
1. 算术平均数：所有数相加除以个数
2. 加权平均数：考虑不同权重
3. 注意极端值：会影响平均数的代表性

### 清理
- FadeOut: 所有总结元素
- 保留: author_info

---

## Scene 7: 片尾 (72-85秒)
**目的**: 品牌强化，引导关注

### 元素
1. 作者信息放大
2. "关注我，学更多数学技巧!"
3. 数学符号装饰

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 72.0s | 作者信息放大 | `author.animate.scale(1.5)` | 0.8s |
| 72.8s | 关注文字 | `Write(follow_text)` | 0.8s |
| 73.6s | 符号装饰旋转 | `Rotate(symbols)` | 1.5s |
| 75.1s | 等待 | `Wait(2.0)` | 2.0s |
| 77.1s | 全部淡出 | `FadeOut(VGroup(*all))` | 1.0s |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| simple_mean | Scene 2 | Scene 2 | 算术平均数可视化 |
| calculation | Scene 3 | Scene 3 | 计算过程 |
| weighted_mean | Scene 4 | Scene 4 | 加权平均数 |
| extreme_comparison | Scene 5 | Scene 5 | 极端值影响 |
| summary | Scene 6 | Scene 6 | 总结 |

---

## 数据验证检查项
- [ ] 算术平均数计算正确: (6+7+8+9+10)/5 = 8.0
- [ ] 加权平均数计算正确: 80×0.3 + 85×0.3 + 90×0.4 = 85.5
- [ ] 极端值对比正确: 正常8.0 vs 极端16.0
- [ ] 所有文字在安全区域内 (x∈[-4,4], y∈[-7,7])
- [ ] 公式 LaTeX 语法正确
- [ ] 颜色对比度足够

---

## 特殊注意事项
1. **中文文字**: 使用 `Text(..., font="Noto Sans CJK SC")` 而非 `MathTex`
2. **公式格式**: 
   - 上标下标: x₁ 使用 `x_1`, x̄ 使用 `\bar{x}`
   - 求和符号: Σ 使用 `\sum`
3. **数轴对齐**: 确保所有点在正确的数值位置
4. **颜色一致性**: 同类元素使用相同颜色
5. **动画节奏**: 计算步骤留足理解时间 (1.5-2秒)

---

## 公式 LaTeX 表达式
```latex
# 算术平均数
\bar{x} = \frac{x_1 + x_2 + \cdots + x_n}{n}

# 通用形式
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i

# 加权平均数
\bar{x} = \frac{x_1f_1 + x_2f_2 + \cdots + x_kf_k}{f_1 + f_2 + \cdots + f_k}

# 通用形式
\bar{x} = \frac{\sum_{i=1}^{k}x_if_i}{\sum_{i=1}^{k}f_i}
```

---

## 视觉设计要点
1. **数轴设计**: 使用 NumberLine，清晰标注刻度
2. **数据点**: 使用 Dot 标记，配合数值标签
3. **平衡感**: 用支点/杠杆比喻帮助理解
4. **对比呈现**: 并排展示正常vs极端数据
5. **计算流程**: 分步展示，不要一次性全部出现