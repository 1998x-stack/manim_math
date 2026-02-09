# 有理数的大小比较 - 动画分镜脚本

## 元信息
- 目标时长: 60-75秒
- 场景数量: 7个
- 难度等级: 初级
- 目标受众: 六年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
COLOR_SECONDARY = "#e74c3c"    # 红色 - 对比元素
COLOR_POSITIVE = "#2ecc71"     # 绿色 - 正数
COLOR_NEGATIVE = "#e74c3c"     # 红色 - 负数
COLOR_ZERO = "#95a5a6"         # 灰色 - 零
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 辅助线条
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 数轴中心 | ORIGIN | self.number_line_center |
| 数轴长度 | 8 | self.number_line_length |
| 点位置 | n2p(value) | 使用NumberLine的n2p方法 |

---

## Scene 1: 开场 (4-5秒)
**目的**: 钩子 + 引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题: "哪个数更大？"
3. 示例数字: 3, -5, 0

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.0s | 三个数字依次出现 | `FadeIn(number, scale=0.5)` |
| 2.5s | 疑问符号闪烁 | `Flash(question_mark)` |
| 3.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text, numbers, question_mark
- 保留: author_info

---

## Scene 2: 规则1 - 正数>0>负数 (8-10秒)
**目的**: 展示基本规则

### 元素
1. 标题: "规则1: 正数 > 0 > 负数"
2. 数轴 (横向, -5到5)
3. 零点标记
4. 正数区域和负数区域

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 数轴绘制 | `Create(number_line)` |
| 1.5s | 零点标记 | `FadeIn(zero_dot)` |
| 2.0s | 左侧阴影(负数区) | `FadeIn(negative_region)` |
| 2.5s | 右侧阴影(正数区) | `FadeIn(positive_region)` |
| 3.0s | 箭头指示方向 | `GrowArrow(direction_arrow)` |
| 4.5s | 示例: 3 > 0 > -5 | `Write(example)` |
| 6.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title, negative_region, positive_region, example
- 保留: number_line (用于后续场景)

---

## Scene 3: 规则2 - 两个正数比较 (10-12秒)
**目的**: 正数比较绝对值

### 元素
1. 标题: "规则2: 正数比大小 = 比绝对值"
2. 两个正数: 3 和 5
3. 绝对值表示: |3| = 3, |5| = 5
4. 比较结果

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 数字3出现在数轴上 | `FadeIn(dot_3)` |
| 1.0s | 数字5出现在数轴上 | `FadeIn(dot_5)` |
| 1.5s | 绝对值表达式出现 | `Write(abs_expr)` |
| 2.5s | 比较: 5 > 3 | `Write(comparison)` |
| 3.5s | 高亮5在3右侧 | `Indicate(dot_5)` |
| 4.5s | 结论: 5 > 3 | `Write(conclusion)` |
| 6.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title, dots, abs_expr, comparison, conclusion
- 保留: number_line

---

## Scene 4: 规则3 - 两个负数比较 (12-15秒)
**目的**: 负数比较绝对值（反向）

### 元素
1. 标题: "规则3: 负数比大小 = 绝对值反向"
2. 两个负数: -2 和 -4
3. 绝对值表示: |-2| = 2, |-4| = 4
4. 关键提示: "绝对值大的反而小!"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 数字-2出现 | `FadeIn(dot_neg2)` |
| 1.0s | 数字-4出现 | `FadeIn(dot_neg4)` |
| 1.5s | 绝对值表达式 | `Write(abs_expr)` |
| 2.5s | 绝对值比较: 4 > 2 | `Write(abs_comparison)` |
| 3.5s | 关键提示闪烁 | `Flash(hint, color=YELLOW)` |
| 4.5s | 结论: -2 > -4 | `Write(conclusion)` |
| 5.5s | 用箭头指示-2在-4右侧 | `GrowArrow(arrow)` |
| 7.0s | 等待理解 | `Wait(2.5)` |

### 清理
- FadeOut: title, dots, abs_expr, hint, conclusion, arrow
- 保留: number_line

---

## Scene 5: 规则4 - 数轴法则 (8-10秒)
**目的**: 数轴右边的数大于左边

### 元素
1. 标题: "规则4: 数轴上，右边 > 左边"
2. 完整数轴
3. 多个示例点
4. 方向箭头

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 多个点依次出现 | `LaggedStart(*[FadeIn(dot) for dot in dots])` |
| 2.0s | 右侧箭头强调 | `GrowArrow(right_arrow)` |
| 3.0s | 从左到右扫描 | `MoveAlongPath(scanner, line)` |
| 4.5s | 示例比较 | `Write(examples)` |
| 6.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, dots, arrow, scanner, examples
- 保留: number_line (用于总结)

---

## Scene 6: 综合示例 (10-12秒)
**目的**: 综合应用所有规则

### 元素
1. 标题: "综合练习"
2. 题目: 比较 -3, 5, 0, -1, 2 的大小
3. 数轴排序
4. 结果

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 题目出现 | `Write(question)` |
| 1.5s | 数字随机散布 | `AnimationGroup(*[FadeIn(n, shift=random) for n in numbers])` |
| 3.0s | 数字移动到数轴位置 | `LaggedStart(*[n.animate.move_to(pos) for n, pos in zip(numbers, positions)])` |
| 5.0s | 从小到大排序 | `Write(sorted_result)` |
| 6.5s | 答案: -3 < -1 < 0 < 2 < 5 | `Write(answer)` |
| 8.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: 所有元素

---

## Scene 7: 片尾 (4-5秒)
**目的**: 作者信息 + 关注提示

### 元素
1. 作者名称放大
2. 关注提示
3. 四条规则快速回顾

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息放大 | `Transform(author, author_large)` |
| 0.8s | 关注提示 | `FadeIn(follow_text, shift=UP*0.3)` |
| 1.5s | 四条规则卡片 | `LaggedStart(*[FadeIn(card, shift=LEFT) for card in cards])` |
| 3.0s | 等待 | `Wait(1.5)` |
| 4.5s | 全部淡出 | `FadeOut(VGroup(*all_objects))` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 持续存在，位置固定在顶部 |
| number_line | Scene 2 | Scene 6 | 主数轴，多场景共用 |
| title_text | 每个场景 | 每个场景 | 场景标题，每场景更新 |
| dots | Scene 2-5 | 各场景结束 | 数轴上的点 |
| examples | Scene 3-5 | 各场景结束 | 示例文字 |

---

## 关键技术要点

### 1. 数轴精确定位
```python
number_line = NumberLine(
    x_range=[-5, 5, 1],
    length=8,
    include_numbers=True,
    numbers_to_include=range(-5, 6),
    font_size=20
).move_to(UP * 1)

# 将数值转换为坐标
point_3 = number_line.n2p(3)
```

### 2. 颜色规则
- 正数点: GREEN
- 负数点: RED
- 零点: GRAY
- 高亮: YELLOW

### 3. 动画节奏
- 简单动画: 0.5-0.8s
- 复杂变换: 1.0-1.5s
- 理解停顿: 1.5-2.5s

### 4. 字体规范
- 标题: 32px
- 正文: 24px
- 数字: 28px
- 作者信息: 20px
