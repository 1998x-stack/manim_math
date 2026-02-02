# 两条直线的位置关系 - 动画分镜脚本

<!-- /root/code/sss/media/videos/two_lines_relationship/1920p60/TwoLinesRelationship.mp4 -->
## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等
- 知识点: 一次函数直线的平行、重合、相交关系

## 颜色配置
```python
COLOR_LINE1 = "#e74c3c"       # 红色 - 第一条直线
COLOR_LINE2 = "#3498db"       # 蓝色 - 第二条直线
COLOR_PARALLEL = "#2ecc71"    # 绿色 - 平行线
COLOR_INTERSECT = "#f39c12"   # 橙色 - 交点
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
COLOR_FORMULA = WHITE
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 直线1 | y = k₁x + b₁ | line1_func | 基准直线 |
| 直线2(平行) | y = k₁x + b₂ | line2_parallel_func | k相同，b不同 |
| 直线2(重合) | y = k₁x + b₁ | line2_coincide_func | k、b都相同 |
| 直线2(相交) | y = k₂x + b₂ | line2_intersect_func | k不同 |
| 交点 | 联立方程求解 | intersection_point | x=(b₂-b₁)/(k₁-k₂) |

## 数学参数设定
```python
# 基准直线：y = 0.5x + 1
k1 = 0.5
b1 = 1.0

# 平行直线：y = 0.5x - 1
k2_parallel = 0.5
b2_parallel = -1.0

# 相交直线：y = -0.8x + 0.5
k2_intersect = -0.8
b2_intersect = 0.5

# 交点计算
intersection_x = (b2_intersect - b1) / (k1 - k2_intersect)
intersection_y = k1 * intersection_x + b1
```

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力 + 引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字)
3. 两条直线快闪

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 两条直线快速绘制 | `Create(line1, line2)` | 0.6s |
| 1.7s | 问号闪烁 | `Flash(question_mark)` | 0.3s |
| 2.0s | 等待 | `Wait(1.0)` | 1.0s |
| 3.0s | 清理钩子文字 | `FadeOut(hook_text)` | 0.4s |

### 钩子文案
- 主标题: "两条直线有几种关系?"
- 副标题: "3种！一起来看"

### 清理
- FadeOut: hook_text, question_mark
- 保留: author_info, axes

---

## Scene 2: 建立坐标系 (5-10秒)
**目的**: 建立数学语境，展示一次函数

### 元素
1. 坐标轴
2. 第一条直线 y = k₁x + b₁
3. 函数表达式标签

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 创建坐标轴 | `Create(axes)` | 1.0s |
| 1.0s | 绘制第一条直线 | `Create(line1_graph)` | 1.2s |
| 2.2s | 显示公式 | `Write(formula1)` | 0.8s |
| 3.0s | 等待理解 | `Wait(1.0)` | 1.0s |

### 说明文字
- "一次函数：y = k₁x + b₁"
- 位置: 右上角 (x=2, y=4)

### 清理
- 保留: axes, line1_graph, formula1
- 移动: formula1 向上移动到 y=5

---

## Scene 3: 情况1 - 平行 (10-25秒)
**目的**: 演示 k₁ = k₂ 且 b₁ ≠ b₂ 时的平行关系

### 元素
1. 第二条直线 (k相同，b不同)
2. 条件标注
3. 平行符号标记

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 标题出现 | `FadeIn(title_parallel)` | 0.5s |
| 0.5s | 显示条件公式 | `Write(condition)` | 1.0s |
| 1.5s | 绘制第二条直线 | `Create(line2_parallel)` | 1.5s |
| 3.0s | 高亮 k 值相同 | `Indicate(k_values)` | 0.8s |
| 3.8s | 平行符号出现 | `FadeIn(parallel_symbol)` | 0.6s |
| 4.4s | 说明文字 | `FadeIn(explanation)` | 0.8s |
| 5.2s | 等待理解 | `Wait(2.0)` | 2.0s |

### 条件公式
```
k₁ = k₂ = 0.5
b₁ = 1, b₂ = -1
→ 两直线平行 ∥
```

### 平行符号
- 在两直线中间位置绘制 "∥" 符号
- 颜色: COLOR_PARALLEL

### 说明文字
- "斜率相同，截距不同"
- "两直线永不相交"
- 位置: 底部 (y=-5)

### 清理
- FadeOut: title_parallel, condition, parallel_symbol, explanation
- 保留: axes, line1_graph, formula1
- 移除: line2_parallel

---

## Scene 4: 情况2 - 重合 (25-38秒)
**目的**: 演示 k₁ = k₂ 且 b₁ = b₂ 时的重合关系

### 元素
1. 第二条直线 (k、b都相同)
2. 条件标注
3. 重合动画效果

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 标题出现 | `FadeIn(title_coincide)` | 0.5s |
| 0.5s | 显示条件公式 | `Write(condition)` | 1.0s |
| 1.5s | 绘制第二条直线(不同色) | `Create(line2_temp, color=BLUE)` | 1.5s |
| 3.0s | 高亮 k、b 值都相同 | `Indicate(kb_values)` | 0.8s |
| 3.8s | 第二条线变色融合 | `line2.animate.set_color(RED)` | 1.0s |
| 4.8s | 闪烁效果 | `Flash(line1)` | 0.4s |
| 5.2s | 说明文字 | `FadeIn(explanation)` | 0.8s |
| 6.0s | 等待理解 | `Wait(2.0)` | 2.0s |

### 条件公式
```
k₁ = k₂ = 0.5
b₁ = b₂ = 1
→ 两直线重合 ≡
```

### 说明文字
- "斜率、截距都相同"
- "实际上是同一条直线"
- 位置: 底部 (y=-5)

### 清理
- FadeOut: title_coincide, condition, explanation
- 保留: axes, line1_graph, formula1

---

## Scene 5: 情况3 - 相交 (38-55秒)
**目的**: 演示 k₁ ≠ k₂ 时的相交关系，并求交点

### 元素
1. 第二条直线 (k不同)
2. 条件标注
3. 交点标记
4. 交点坐标计算过程

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 标题出现 | `FadeIn(title_intersect)` | 0.5s |
| 0.5s | 显示条件公式 | `Write(condition)` | 1.0s |
| 1.5s | 绘制第二条直线 | `Create(line2_intersect)` | 1.5s |
| 3.0s | 高亮 k 值不同 | `Indicate(k_values)` | 0.8s |
| 3.8s | 交点闪烁 | `Flash(intersection_dot)` | 0.5s |
| 4.3s | 交点标记出现 | `FadeIn(intersection_dot, label)` | 0.6s |
| 4.9s | 求解过程展示 | `Write(solution_steps)` | 2.5s |
| 7.4s | 交点坐标高亮 | `Indicate(coordinates)` | 0.8s |
| 8.2s | 说明文字 | `FadeIn(explanation)` | 0.8s |
| 9.0s | 等待理解 | `Wait(2.5)` | 2.5s |

### 条件公式
```
y = 0.5x + 1
y = -0.8x + 0.5
k₁ ≠ k₂ → 相交
```

### 求解过程 (分步展示)
```
Step 1: 0.5x + 1 = -0.8x + 0.5
Step 2: 1.3x = -0.5
Step 3: x ≈ -0.38
Step 4: y = 0.5×(-0.38) + 1 ≈ 0.81
交点: P(-0.38, 0.81)
```

### 交点标记
- Dot: 大号圆点 (radius=0.15)
- 颜色: COLOR_INTERSECT
- 标签: "P" + 坐标

### 说明文字
- "斜率不同，必有交点"
- "联立方程可求交点坐标"
- 位置: 底部 (y=-5.5)

### 清理
- 保留: axes, line1_graph, line2_intersect, intersection_dot
- FadeOut: title, condition, solution_steps, explanation

---

## Scene 6: 总结归纳 (55-65秒)
**目的**: 三种情况汇总，强化记忆

### 元素
1. 三种情况卡片
2. 判别流程图
3. 记忆口诀

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 标题出现 | `FadeIn(title_summary)` | 0.5s |
| 0.5s | 三张卡片依次滑入 | `card.animate.shift(LEFT)` | 1.5s |
| 2.0s | 判别流程图展开 | `Create(flowchart)` | 2.0s |
| 4.0s | 记忆口诀出现 | `Write(mnemonic)` | 1.5s |
| 5.5s | 全部高亮闪烁 | `Flash(all_cards)` | 0.8s |
| 6.3s | 等待 | `Wait(1.5)` | 1.5s |

### 三张卡片内容
**卡片1: 平行**
- 图标: ∥
- 条件: k₁ = k₂, b₁ ≠ b₂
- 结果: 平行
- 颜色: COLOR_PARALLEL

**卡片2: 重合**
- 图标: ≡
- 条件: k₁ = k₂, b₁ = b₂
- 结果: 重合
- 颜色: COLOR_LINE1

**卡片3: 相交**
- 图标: ×
- 条件: k₁ ≠ k₂
- 结果: 相交
- 颜色: COLOR_INTERSECT

### 判别流程图
```
比较斜率 k
    ├─ k₁ = k₂ → 比较截距 b
    │           ├─ b₁ = b₂ → 重合
    │           └─ b₁ ≠ b₂ → 平行
    └─ k₁ ≠ k₂ → 相交
```

### 记忆口诀
```
斜率相同看截距
截距不同就平行
全都相同是重合
斜率不同必相交
```

### 清理
- FadeOut: all elements except author_info

---

## Scene 7: 片尾关注 (65-75秒)
**目的**: 引导关注，品牌强化

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 作者信息放大 | `author.animate.scale(2)` | 0.8s |
| 0.8s | ID 出现 | `FadeIn(author_id)` | 0.5s |
| 1.3s | 关注提示滑入 | `FadeIn(follow_text, shift=UP)` | 0.6s |
| 1.9s | 装饰线条动画 | `Create(decorations)` | 1.0s |
| 2.9s | 数学符号旋转 | `Rotate(symbols)` | 1.5s |
| 4.4s | 全部淡出 | `FadeOut(all)` | 1.0s |

### 关注文案
- "关注我，获得更多数学技巧!"
- 字体大小: 30
- 颜色: COLOR_HIGHLIGHT

### 装饰元素
- 直线符号: ∥ ≡ × 
- 颜色: 对应主题色
- 排列: 圆形环绕

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 持续存在 |
| axes | Scene 2 | Scene 6 | 坐标系 |
| line1_graph | Scene 2 | Scene 6 | 第一条直线 |
| formula1 | Scene 2 | Scene 5 | 公式标签 |
| line2_parallel | Scene 3 | Scene 3 | 平行线(临时) |
| line2_intersect | Scene 5 | Scene 6 | 相交线 |
| intersection_dot | Scene 5 | Scene 6 | 交点 |
| summary_cards | Scene 6 | Scene 6 | 总结卡片 |

---

## 字体大小规范（严格遵守）
- 标题 (Scene Title): 36
- 公式 (Formula): 28
- 条件 (Condition): 24
- 说明文字 (Explanation): 22
- 标签 (Label): 20
- 作者信息 (Author): 20
- 小字注释: 18

---

## 颜色使用规范
- 背景: #1a1a2e (深蓝紫)
- 第一条直线: #e74c3c (红)
- 第二条直线: #3498db (蓝) / #2ecc71 (绿)
- 高亮: YELLOW
- 辅助: GRAY_B
- 公式: WHITE

---

## 关键帧时间轴
```
0s   ━━━━━━━━━━━ Scene 1: 开场钩子
5s   ━━━━━━━━━━━ Scene 2: 建立坐标系
10s  ━━━━━━━━━━━ Scene 3: 平行
25s  ━━━━━━━━━━━ Scene 4: 重合
38s  ━━━━━━━━━━━ Scene 5: 相交
55s  ━━━━━━━━━━━ Scene 6: 总结
65s  ━━━━━━━━━━━ Scene 7: 片尾
75s  END
```

---

## 预期难点与解决方案

### 难点1: 交点坐标计算精度
**问题**: NumPy 计算可能有浮点误差
**解决**: 
```python
intersection_x = (b2_intersect - b1) / (k1 - k2_intersect)
intersection_y = k1 * intersection_x + b1
intersection_point = np.array([intersection_x, intersection_y, 0])
```

### 难点2: 直线在坐标系中的范围
**问题**: 直线可能超出可视范围
**解决**: 
```python
x_range = [-3, 3, 1]
y_range = [-3, 3, 1]
# 确保所有关键点在范围内
```

### 难点3: 公式位置不重叠
**问题**: 多个公式可能重叠
**解决**: 使用精确的 `.move_to()` 和 `.next_to()`
```python
formula1.move_to(UP * 5 + RIGHT * 2)
formula2.next_to(formula1, DOWN, buff=0.3)
```

---

## 验证检查清单
- [ ] 所有坐标通过精确计算获得
- [ ] 交点坐标验证正确 (代入两个方程)
- [ ] 所有元素在边界范围内
- [ ] 中文使用 Text()，数学公式使用 MathTex()
- [ ] 字体大小符合规范
- [ ] 颜色使用一致
- [ ] 动画节奏流畅
- [ ] 总时长 60-75 秒