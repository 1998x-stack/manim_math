# 向量的加法与减法 - 动画分镜脚本

## 元信息
- 目标时长: 70-85 秒
- 场景数量: 8 个
- 难度等级: 中等
- 知识点: 向量加法（三角形法则、平行四边形法则）、向量减法

## 颜色配置
```python
COLOR_VECTOR_A = "#e74c3c"        # 红色 - 向量a
COLOR_VECTOR_B = "#3498db"        # 蓝色 - 向量b
COLOR_VECTOR_SUM = "#2ecc71"      # 绿色 - 和向量
COLOR_VECTOR_DIFF = "#f39c12"     # 橙色 - 差向量
COLOR_VECTOR_NEG = "#9b59b6"      # 紫色 - 相反向量
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
COLOR_POLYGON = WHITE
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 向量a起点 | O = (0, 0, 0) | self.O | 原点 |
| 向量a终点 | A = O + vec_a | self.A | 向量a的方向 |
| 向量b起点(三角形) | A | self.A | 首尾相接 |
| 向量b终点(三角形) | C = A + vec_b | self.C | 三角形法则 |
| 向量b起点(平行四边形) | O | self.O | 同起点 |
| 向量b终点(平行四边形) | B = O + vec_b | self.B | 平行四边形 |
| 平行四边形第四顶点 | D = A + vec_b | self.D | 对角线交点 |
| 相反向量终点 | -B = O - vec_b | self.neg_B | 方向相反 |

## 向量参数设定
```python
# 向量a: 从原点到右上方
vec_a = np.array([2.5, 1.5, 0])

# 向量b: 从原点到右方偏上
vec_b = np.array([1.8, 0.8, 0])

# 验证计算
# 三角形法则: O + vec_a + vec_b = C
C = O + vec_a + vec_b

# 平行四边形法则: O + vec_a + vec_b = D
D = O + vec_a + vec_b  # 应该等于C

# 向量减法: a - b = a + (-b)
vec_neg_b = -vec_b
diff = O + vec_a + vec_neg_b
```

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力 + 引出向量概念

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字)
3. 几个箭头快闪

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 箭头动画展示 | `GrowArrow(arrows)` | 0.8s |
| 1.9s | 问号闪烁 | `Flash(question)` | 0.3s |
| 2.2s | 等待 | `Wait(1.0)` | 1.0s |
| 3.2s | 清理钩子 | `FadeOut(hook_text, arrows)` | 0.4s |

### 钩子文案
- 主标题: "箭头能加减吗?"
- 副标题: "向量运算，其实很简单！"

### 清理
- FadeOut: hook_text, demo_arrows, question
- 保留: author_info

---

## Scene 2: 向量基础 (5-12秒)
**目的**: 介绍向量的概念和表示

### 元素
1. 坐标原点
2. 第一个向量
3. 向量标记（箭头、标签）

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 标题出现 | `FadeIn(title)` | 0.5s |
| 0.5s | 原点标记 | `FadeIn(origin_dot, label)` | 0.4s |
| 0.9s | 绘制向量a | `GrowArrow(vector_a)` | 1.0s |
| 1.9s | 向量标签 | `Write(vector_a_label)` | 0.5s |
| 2.4s | 说明文字 | `FadeIn(explanation)` | 0.6s |
| 3.0s | 等待理解 | `Wait(1.5)` | 1.5s |

### 说明文字
- "向量：既有大小又有方向"
- "用箭头表示，记作 →a"
- 位置: 底部 (y=-5)

### 清理
- FadeOut: title, explanation
- 保留: origin_dot, vector_a, vector_a_label

---

## Scene 3: 三角形法则 (12-28秒)
**目的**: 演示首尾相接的向量加法

### 元素
1. 向量a (已有)
2. 向量b (从a的终点开始)
3. 和向量 (从起点到b的终点)
4. 三角形轮廓

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 标题出现 | `FadeIn(title_triangle)` | 0.5s |
| 0.5s | 公式显示 | `Write(formula)` | 1.0s |
| 1.5s | 向量b出现(起点在A) | `GrowArrow(vector_b_triangle)` | 1.2s |
| 2.7s | 标注"首尾相接" | `FadeIn(annotation)` | 0.6s |
| 3.3s | 绘制和向量 | `GrowArrow(sum_vector)` | 1.5s |
| 4.8s | 高亮三角形路径 | `Create(triangle_path)` | 1.0s |
| 5.8s | 公式解释 | `FadeIn(explanation)` | 0.8s |
| 6.6s | 等待理解 | `Wait(2.5)` | 2.5s |

### 公式展示
```
→AB + →BC = →AC
（首）   （尾）  （首到尾）
```

### 说明文字
- "首尾相接：第二个向量起点接在第一个终点"
- "结果向量：从第一个起点到第二个终点"
- 位置: 底部 (y=-5.5)

### 动画高亮
- 用虚线三角形框出 O→A→C 的路径
- 高亮颜色: YELLOW

### 清理
- FadeOut: title, formula, annotation, triangle_path, explanation
- 保留: origin_dot
- 移除: vector_b_triangle (后续用平行四边形法)

---

## Scene 4: 平行四边形法则 (28-44秒)
**目的**: 演示同起点的向量加法

### 元素
1. 向量a (从原点)
2. 向量b (从原点，不同方向)
3. 平行四边形
4. 对角线（和向量）

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 清理并重置 | `FadeOut(old), vector_a回到原点` | 0.6s |
| 0.6s | 标题出现 | `FadeIn(title_parallelogram)` | 0.5s |
| 1.1s | 公式显示 | `Write(formula)` | 1.0s |
| 2.1s | 向量b出现(同起点) | `GrowArrow(vector_b_para)` | 1.2s |
| 3.3s | 标注"同起点" | `FadeIn(annotation)` | 0.6s |
| 3.9s | 构造平行四边形 | `Create(parallelogram)` | 1.5s |
| 5.4s | 绘制对角线(和向量) | `GrowArrow(sum_vector_diag)` | 1.5s |
| 6.9s | 高亮对角线 | `Indicate(sum_vector)` | 0.8s |
| 7.7s | 说明文字 | `FadeIn(explanation)` | 0.8s |
| 8.5s | 等待理解 | `Wait(2.5)` | 2.5s |

### 公式展示
```
→OA + →OB = →OC
（同起点）    （对角线）
```

### 平行四边形构造
- 顶点: O, A, D, B (按逆时针)
- D = A + vec_b = O + vec_a + vec_b
- 验证: OA // BD, OB // AD

### 说明文字
- "同起点：两向量从同一点出发"
- "和向量：以两向量为邻边的平行四边形对角线"
- 位置: 底部 (y=-5.5)

### 清理
- FadeOut: title, formula, annotation, parallelogram, explanation
- 保留: origin_dot, vector_a, vector_b, sum_vector

---

## Scene 5: 两种法则等价性 (44-52秒)
**目的**: 展示两种方法得到相同结果

### 元素
1. 三角形法则图示（左侧）
2. 平行四边形法则图示（右侧）
3. 等号连接

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 场景分屏 | `VGroup左右移动` | 0.8s |
| 0.8s | 左侧三角形法则 | `Create(triangle_method)` | 1.2s |
| 2.0s | 右侧平行四边形法则 | `Create(parallelogram_method)` | 1.2s |
| 3.2s | 等号出现 | `FadeIn(equals_sign)` | 0.5s |
| 3.7s | 结果向量高亮 | `Indicate(both_results)` | 0.8s |
| 4.5s | 说明文字 | `FadeIn(explanation)` | 0.6s |
| 5.1s | 等待 | `Wait(1.5)` | 1.5s |

### 说明文字
- "两种方法，结果相同！"
- "可根据题目选择合适方法"

### 清理
- FadeOut: 分屏内容, equals_sign, explanation
- 返回: 主场景

---

## Scene 6: 向量减法 - 相反向量 (52-64秒)
**目的**: 引入相反向量概念

### 元素
1. 向量b
2. 相反向量 -b
3. 对比展示

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 标题出现 | `FadeIn(title_subtraction)` | 0.5s |
| 0.5s | 向量b显示 | `GrowArrow(vector_b)` | 0.8s |
| 1.3s | 公式显示 | `Write(formula_neg)` | 0.8s |
| 2.1s | 相反向量出现 | `GrowArrow(vector_neg_b)` | 1.0s |
| 3.1s | 对比标注 | `Create(comparison_arrows)` | 0.8s |
| 3.9s | 说明文字 | `FadeIn(explanation)` | 0.8s |
| 4.7s | 长度相等演示 | `Indicate(both_vectors)` | 0.8s |
| 5.5s | 方向相反演示 | `Rotate动画` | 1.0s |
| 6.5s | 等待理解 | `Wait(1.5)` | 1.5s |

### 公式展示
```
-→b: 与→b长度相等，方向相反
```

### 说明文字
- "相反向量：长度相等，方向相反"
- "箭头掉头，大小不变"

### 清理
- FadeOut: title, comparison, explanation
- 保留: vector_b, vector_neg_b

---

## Scene 7: 向量减法运算 (64-76秒)
**目的**: 演示 a - b = a + (-b)

### 元素
1. 向量a
2. 向量b
3. 相反向量 -b
4. 差向量

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 标题出现 | `FadeIn(title)` | 0.5s |
| 0.5s | 公式显示 | `Write(formula_subtraction)` | 1.0s |
| 1.5s | 向量a和b显示 | `GrowArrow(a, b)` | 1.0s |
| 2.5s | b变换为-b | `Transform(b to -b)` | 1.2s |
| 3.7s | 三角形法则应用 | `Create(-b接在a后)` | 1.5s |
| 5.2s | 绘制差向量 | `GrowArrow(diff_vector)` | 1.5s |
| 6.7s | 公式完整显示 | `Write(complete_formula)` | 0.8s |
| 7.5s | 说明文字 | `FadeIn(explanation)` | 0.6s |
| 8.1s | 等待理解 | `Wait(2.0)` | 2.0s |

### 公式展示
```
→a - →b = →a + (-→b)
减法 = 加上相反向量
```

### 说明文字
- "减法转化为加法"
- "加上相反向量即可"

### 清理
- FadeOut: title, formula, explanation
- 保留: diff_vector 用于总结

---

## Scene 8: 总结 + 片尾 (76-85秒)
**目的**: 知识点总结 + 引导关注

### 元素
1. 三个要点卡片
2. 公式汇总
3. 作者信息

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 标题出现 | `FadeIn(title_summary)` | 0.5s |
| 0.5s | 卡片1滑入 | `card1.shift(LEFT)` | 0.5s |
| 1.0s | 卡片2滑入 | `card2.shift(LEFT)` | 0.5s |
| 1.5s | 卡片3滑入 | `card3.shift(LEFT)` | 0.5s |
| 2.0s | 公式汇总 | `Write(formulas)` | 1.2s |
| 3.2s | 全部高亮 | `Flash(all_cards)` | 0.6s |
| 3.8s | 清理准备片尾 | `FadeOut(cards)` | 0.5s |
| 4.3s | 作者信息放大 | `author.scale(2)` | 0.6s |
| 4.9s | 关注提示 | `FadeIn(follow_text)` | 0.5s |
| 5.4s | 向量符号装饰 | `Create(vector_icons)` | 0.8s |
| 6.2s | 全部淡出 | `FadeOut(all)` | 1.0s |

### 三张卡片内容

**卡片1: 三角形法则**
- 图标: 三角形示意
- 内容: 首尾相接，首到尾
- 公式: →AB + →BC = →AC
- 颜色: COLOR_VECTOR_SUM

**卡片2: 平行四边形法则**
- 图标: 平行四边形示意
- 内容: 同起点，对角线
- 公式: →OA + →OB = →OC
- 颜色: COLOR_VECTOR_SUM

**卡片3: 向量减法**
- 图标: 箭头对比
- 内容: 加相反向量
- 公式: →a - →b = →a + (-→b)
- 颜色: COLOR_VECTOR_DIFF

### 关注文案
- "关注我，获得更多数学技巧!"
- 向量箭头装饰环绕

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 持续存在 |
| origin_dot | Scene 2 | Scene 7 | 坐标原点 |
| vector_a | Scene 2 | Scene 7 | 向量a主元素 |
| vector_b_triangle | Scene 3 | Scene 3 | 三角形法则临时 |
| vector_b_para | Scene 4 | Scene 7 | 平行四边形法则 |
| parallelogram | Scene 4 | Scene 4 | 平行四边形 |
| sum_vector | Scene 3/4 | Scene 7 | 和向量 |
| vector_neg_b | Scene 6 | Scene 7 | 相反向量 |
| diff_vector | Scene 7 | Scene 7 | 差向量 |
| summary_cards | Scene 8 | Scene 8 | 总结卡片 |

---

## 字体大小规范（严格遵守）
- 标题 (Scene Title): 36
- 公式 (Formula): 28
- 向量标签 (Vector Label): 24
- 说明文字 (Explanation): 22
- 标注 (Annotation): 20
- 作者信息 (Author): 20
- 小字注释: 18

---

## 颜色使用规范
- 背景: #1a1a2e (深蓝紫)
- 向量a: #e74c3c (红)
- 向量b: #3498db (蓝)
- 和向量: #2ecc71 (绿)
- 差向量: #f39c12 (橙)
- 相反向量: #9b59b6 (紫)
- 高亮: YELLOW
- 辅助: GRAY_B

---

## 关键帧时间轴
```
0s   ━━━━━━━━━━━ Scene 1: 开场钩子
5s   ━━━━━━━━━━━ Scene 2: 向量基础
12s  ━━━━━━━━━━━ Scene 3: 三角形法则
28s  ━━━━━━━━━━━ Scene 4: 平行四边形法则
44s  ━━━━━━━━━━━ Scene 5: 两种法则等价性
52s  ━━━━━━━━━━━ Scene 6: 相反向量
64s  ━━━━━━━━━━━ Scene 7: 向量减法
76s  ━━━━━━━━━━━ Scene 8: 总结 + 片尾
85s  END
```

---

## 预期难点与解决方案

### 难点1: 向量箭头的精确绘制
**问题**: Arrow 对象需要精确的起点和终点
**解决**: 
```python
vector_a_arrow = Arrow(
    start=self.O,
    end=self.A,
    buff=0,
    stroke_width=6,
    max_tip_length_to_length_ratio=0.15,
    color=COLOR_VECTOR_A
)
```

### 难点2: 平行四边形的精确构造
**问题**: 确保对边平行且相等
**解决**: 
```python
# O, A, D, B 四个顶点
# 验证: vec(OA) = vec(BD), vec(OB) = vec(AD)
D = self.O + vec_a + vec_b
assert np.allclose(self.A - self.O, D - self.B)
```

### 难点3: 向量标签位置
**问题**: 箭头标签可能重叠或超出边界
**解决**: 使用智能定位
```python
label_pos = (start + end) / 2 + perpendicular_offset
```

---

## 验证检查清单
- [ ] 所有向量起点、终点通过精确计算
- [ ] 平行四边形对边确实平行（叉积为0）
- [ ] 向量长度计算正确
- [ ] 相反向量方向正确（点积为负）
- [ ] 三角形法则和平行四边形法则结果一致
- [ ] 所有元素在边界范围内
- [ ] 中文使用 Text()，数学公式使用 MathTex()
- [ ] 字体大小符合规范
- [ ] 颜色使用一致
- [ ] 动画节奏流畅
- [ ] 总时长 70-85 秒

---

## 特殊注意事项

### 向量箭头绘制
- 使用 `Arrow` 而不是 `Vector`（Vector在某些版本可能不稳定）
- 设置 `buff=0` 确保箭头从起点开始
- 调整 `max_tip_length_to_length_ratio` 确保箭头尖端比例合适

### 向量标签
- 使用 MathTex 显示向量符号: `r"\vec{a}"` 或 `r"\overrightarrow{AB}"`
- 标签位置使用中点 + 垂直偏移

### 平行关系验证
- 使用叉积验证平行: `np.cross(v1, v2) ≈ 0`
- 使用点积验证垂直: `np.dot(v1, v2) ≈ 0`