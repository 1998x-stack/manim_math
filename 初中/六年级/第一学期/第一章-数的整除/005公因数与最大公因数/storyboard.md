# 最大公因数 (Greatest Common Divisor) - 动画分镜脚本

<!-- /root/code/sss/media/videos/gcd_teaching/1920p60/GCDTeaching.mp4 -->

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 6 个
- 难度等级: 中等
- 目标观众: 六年级学生
- 主题: 公因数与最大公因数的概念及短除法求解

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要数字
COLOR_SECONDARY = "#e74c3c"    # 红色 - 次要数字
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮重点
COLOR_COMMON = "#2ecc71"       # 绿色 - 公因数
COLOR_GCD = GOLD               # 金色 - 最大公因数
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_BACKGROUND = "#1a1a2e"   # 深蓝背景
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 数字12的位置 | UP * 3 + LEFT * 2 | self.pos_12 |
| 数字18的位置 | UP * 3 + RIGHT * 2 | self.pos_18 |
| 因数表格中心 | UP * 1 | self.table_center |
| Venn图左圆心 | LEFT * 1.5 | self.venn_left |
| Venn图右圆心 | RIGHT * 1.5 | self.venn_right |
| 短除法表格顶部 | UP * 4 | self.division_top |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 吸引注意力，提出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字动画)
3. 两个数字闪烁: 12 和 18

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字打字效果 | `Write(hook_text)` | 1.0s |
| 1.3s | 数字12淡入并放大 | `FadeIn(num_12, scale=0.5)` | 0.4s |
| 1.7s | 数字18淡入并放大 | `FadeIn(num_18, scale=0.5)` | 0.4s |
| 2.1s | 两数字闪烁高亮 | `Flash(num_12), Flash(num_18)` | 0.5s |
| 2.6s | 问题文字淡入 | `FadeIn(question)` | 0.5s |
| 3.1s | 等待思考 | `Wait(0.9)` | 0.9s |

### 文案
- 钩子: "12和18有什么共同点?"
- 问题: "它们的最大公因数是多少?"

### 清理
- FadeOut: hook_text, question
- 保留: num_12, num_18, author_info

---

## Scene 2: 因数概念回顾 (8秒)
**目的**: 复习因数概念，为公因数做铺垫

### 元素
1. 标题: "什么是因数?"
2. 12的因数列表动画
3. 18的因数列表动画
4. 箭头指向

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题书写 | `Write(title)` | 0.6s |
| 0.6s | 定义文字淡入 | `FadeIn(definition)` | 0.5s |
| 1.1s | 12向左移动 | `num_12.animate.move_to(pos_left)` | 0.6s |
| 1.1s | 18向右移动 | `num_18.animate.move_to(pos_right)` | 0.6s |
| 1.7s | 12的因数逐个出现 | `LaggedStart(*factors_12_anims)` | 1.5s |
| 3.2s | 18的因数逐个出现 | `LaggedStart(*factors_18_anims)` | 1.5s |
| 4.7s | 说明文字 | `FadeIn(explanation)` | 0.5s |
| 5.2s | 等待 | `Wait(2.0)` | 2.0s |

### 数据
- 12的因数: 1, 2, 3, 4, 6, 12
- 18的因数: 1, 2, 3, 6, 9, 18

### 清理
- FadeOut: title, definition, explanation
- 保留: num_12, num_18, factors_12, factors_18

---

## Scene 3: 公因数展示 - Venn图 (10秒)
**目的**: 可视化公因数概念

### 元素
1. 标题: "公因数"
2. Venn图两个圆
3. 因数移动到对应区域
4. 公共区域高亮

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题淡入 | `Write(title)` | 0.6s |
| 0.6s | 绘制左圆(12) | `Create(circle_12)` | 0.8s |
| 1.4s | 绘制右圆(18) | `Create(circle_18)` | 0.8s |
| 2.2s | 左圆标签 | `FadeIn(label_12)` | 0.3s |
| 2.5s | 右圆标签 | `FadeIn(label_18)` | 0.3s |
| 2.8s | 12的独有因数移入 | `factors_12_unique.animate.move_to()` | 1.0s |
| 3.8s | 18的独有因数移入 | `factors_18_unique.animate.move_to()` | 1.0s |
| 4.8s | 公因数移入交集 | `common_factors.animate.move_to()` | 1.2s |
| 6.0s | 交集区域高亮 | `intersection.animate.set_fill(opacity=0.3)` | 0.5s |
| 6.5s | 公因数文字说明 | `FadeIn(explanation)` | 0.5s |
| 7.0s | 圈出公因数 | `Create(highlight_box)` | 0.6s |
| 7.6s | 等待 | `Wait(1.5)` | 1.5s |

### Venn图几何
```python
# 左圆 (12的因数)
self.venn_left = LEFT * 1.5 + UP * 0.5
radius = 1.8

# 右圆 (18的因数)
self.venn_right = RIGHT * 1.5 + UP * 0.5
radius = 1.8

# 交集区域 (公因数: 1, 2, 3, 6)
intersection_center = (self.venn_left + self.venn_right) / 2
```

### 清理
- FadeOut: Venn图, 所有因数
- 保留: title (变换为下一场景标题)

---

## Scene 4: 最大公因数概念 (8秒)
**目的**: 引出最大公因数的定义

### 元素
1. 标题: "最大公因数 (GCD)"
2. 公因数列表: 1, 2, 3, 6
3. 最大值高亮动画
4. 公式展示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题变换 | `TransformMatchingTex(old_title, new_title)` | 0.6s |
| 0.6s | 公因数水平排列 | `Arrange(common_list, RIGHT)` | 0.8s |
| 1.4s | 逐个淡入公因数 | `LaggedStart(*[FadeIn(n) for n in [1,2,3,6]])` | 1.2s |
| 2.6s | "最大"文字强调 | `FadeIn(max_text, scale=1.2)` | 0.5s |
| 3.1s | 6放大并变色 | `num_6.animate.scale(1.5).set_color(GOLD)` | 0.8s |
| 3.9s | 其他数字变暗 | `others.animate.set_opacity(0.3)` | 0.4s |
| 4.3s | 公式书写 | `Write(gcd_formula)` | 1.0s |
| 5.3s | 箭头指向6 | `GrowArrow(arrow)` | 0.5s |
| 5.8s | 结论文字 | `FadeIn(conclusion)` | 0.5s |
| 6.3s | 等待 | `Wait(1.2)` | 1.2s |

### 公式
```python
gcd_formula = MathTex(r"\gcd(12, 18) = 6")
# 或
gcd_formula = MathTex(r"\text{gcd}(12, 18) = 6")
```

### 清理
- FadeOut: 所有当前元素
- 保留: author_info

---

## Scene 5: 短除法演示 (18秒)
**目的**: 教授短除法求最大公因数

### 元素
1. 标题: "短除法求最大公因数"
2. 短除法竖式结构
3. 步骤说明文字
4. 箭头和高亮

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题书写 | `Write(title)` | 0.8s |
| 0.8s | 说明文字 | `FadeIn(instruction)` | 0.5s |
| 1.3s | 绘制初始结构 | `Create(division_frame)` | 0.6s |
| 1.9s | 写入12和18 | `Write(num_12), Write(num_18)` | 0.6s |
| 2.5s | 步骤1说明 | `FadeIn(step1_text)` | 0.5s |
| 3.0s | 除数2出现 | `FadeIn(divisor_2, shift=LEFT*0.3)` | 0.5s |
| 3.5s | 横线绘制 | `Create(h_line_1)` | 0.4s |
| 3.9s | 计算12÷2 | `Write(result_6_left)` | 0.6s |
| 4.5s | 计算18÷2 | `Write(result_9_right)` | 0.6s |
| 5.1s | 步骤2说明 | `FadeIn(step2_text), FadeOut(step1_text)` | 0.5s |
| 5.6s | 除数3出现 | `FadeIn(divisor_3, shift=LEFT*0.3)` | 0.5s |
| 6.1s | 横线绘制 | `Create(h_line_2)` | 0.4s |
| 6.5s | 计算6÷3 | `Write(result_2_left)` | 0.6s |
| 7.1s | 计算9÷3 | `Write(result_3_right)` | 0.6s |
| 7.7s | 互质说明 | `FadeIn(coprime_text)` | 0.5s |
| 8.2s | 圈出公因数 | `Create(highlight_2), Create(highlight_3)` | 0.8s |
| 9.0s | 乘法公式 | `Write(multiply_formula)` | 1.0s |
| 10.0s | 计算过程 | `Write(calculation)` | 1.2s |
| 11.2s | 答案高亮 | `answer.animate.scale(1.3).set_color(GOLD)` | 0.6s |
| 11.8s | 庆祝动画 | `Flash(answer, color=GOLD)` | 0.5s |
| 12.3s | 等待 | `Wait(4.0)` | 4.0s |

### 短除法结构
```python
# 竖式布局
#     2 | 12  18
#     3 |  6   9
#       |  2   3

# 位置计算
division_top = UP * 4
row_spacing = 1.2
col_spacing = 1.5

# 第一行
divisor_2_pos = division_top + LEFT * 3
num_12_pos = division_top + LEFT * 0.5
num_18_pos = division_top + RIGHT * 1.5

# 第二行
divisor_3_pos = divisor_2_pos + DOWN * row_spacing
result_6_pos = num_12_pos + DOWN * row_spacing
result_9_pos = num_18_pos + DOWN * row_spacing

# 第三行 (最终结果)
final_2_pos = result_6_pos + DOWN * row_spacing
final_3_pos = result_9_pos + DOWN * row_spacing
```

### 清理
- FadeOut: 短除法表格
- 保留: 最终答案 (缩小到角落)

---

## Scene 6: 总结与片尾 (7秒)
**目的**: 巩固知识点，引导关注

### 元素
1. 知识点总结卡片
2. 示例回顾
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 总结标题 | `Write(summary_title)` | 0.6s |
| 0.6s | 要点1滑入 | `summary_card_1.animate.shift(RIGHT*10)` | 0.5s |
| 1.1s | 要点2滑入 | `summary_card_2.animate.shift(RIGHT*10)` | 0.5s |
| 1.6s | 要点3滑入 | `summary_card_3.animate.shift(RIGHT*10)` | 0.5s |
| 2.1s | 示例回顾 | `FadeIn(example_recap)` | 0.6s |
| 2.7s | 等待 | `Wait(0.8)` | 0.8s |
| 3.5s | 淡出总结 | `FadeOut(summary_group)` | 0.5s |
| 4.0s | 作者信息放大 | `author_info.animate.scale(2).move_to(UP)` | 0.6s |
| 4.6s | 关注文字 | `FadeIn(follow_text, scale=1.1)` | 0.5s |
| 5.1s | 装饰元素 | `LaggedStart(*[FadeIn(icon) for icon in icons])` | 0.8s |
| 5.9s | 等待 | `Wait(0.6)` | 0.6s |

### 总结要点
1. "公因数: 两个数共有的因数"
2. "最大公因数: 公因数中最大的一个"
3. "短除法: 用公因数连续除，最后相乘"

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 持续存在 |
| num_12 | Scene 1 | Scene 4 | 主数字 |
| num_18 | Scene 1 | Scene 4 | 主数字 |
| factors_12 | Scene 2 | Scene 3 | 12的因数列表 |
| factors_18 | Scene 2 | Scene 3 | 18的因数列表 |
| venn_diagram | Scene 3 | Scene 3 | Venn图 |
| common_factors | Scene 3 | Scene 4 | 公因数 |
| gcd_result | Scene 4 | Scene 5 | 最大公因数结果 |
| division_table | Scene 5 | Scene 5 | 短除法表格 |
| summary_cards | Scene 6 | Scene 6 | 总结卡片 |

---

## 时长分配检查
- Scene 1: 4秒
- Scene 2: 8秒
- Scene 3: 10秒
- Scene 4: 8秒
- Scene 5: 18秒
- Scene 6: 7秒
- **总计: 55秒** (符合45-90秒范围，留有调整空间)

---

## 难点停留策略
1. **公因数概念** (Scene 3): 停留1.5秒，让学生理解交集
2. **短除法第一步** (Scene 5): 详细演示，每步0.6秒
3. **公因数相乘** (Scene 5): 停留1.2秒，理解为何要相乘
4. **最终答案** (Scene 5): 停留4秒，包含庆祝动画

---

## 视觉设计notes
1. **数字大小**: 主数字字号48，因数字号28，说明字号22
2. **颜色一致性**: 
   - 12相关 → 蓝色系
   - 18相关 → 红色系
   - 公因数 → 绿色
   - 最大公因数 → 金色
3. **动画速度**: 
   - 创建动画: 0.6-0.8秒
   - 变换动画: 0.4-0.6秒
   - 文字书写: 0.6-1.0秒
4. **布局**: 所有元素保持在 y∈[-6, 7], x∈[-4, 4] 安全区