# 三角形内角和定理 - 动画分镜脚本

<!-- /root/code/sss/media/videos/opposite_numbers/1920p60/OppositeNumbers.mp4 -->

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 初中七年级
- 核心知识点: ∠A + ∠B + ∠C = 180°

## 颜色配置
```python
COLOR_PRIMARY = "#00D9FF"        # 青色 - 主三角形
COLOR_ANGLE_A = "#FF6B6B"        # 红色 - 角A
COLOR_ANGLE_B = "#4ECDC4"        # 绿松石 - 角B  
COLOR_ANGLE_C = "#FFE66D"        # 黄色 - 角C
COLOR_AUXILIARY = "#95A5A6"      # 灰色 - 辅助线
COLOR_HIGHLIGHT = YELLOW         # 高亮
COLOR_TEXT = WHITE               # 文字
```

## 几何预计算清单

### 主三角形（居中，缩放后）
| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 顶点A | np.array([-2.5, 1.2, 0]) * SCALE + OFFSET | self.A | 左上顶点 |
| 顶点B | np.array([2.5, -0.8, 0]) * SCALE + OFFSET | self.B | 右下顶点 |
| 顶点C | np.array([-1.0, -2.0, 0]) * SCALE + OFFSET | self.C | 左下顶点 |
| SCALE | 0.85 | self.SCALE | 缩放系数 |
| OFFSET | UP * 1.5 | self.OFFSET | 垂直偏移 |

### 角度数据（弧度）
| 元素 | 计算公式 | 存储变量 | 验证条件 |
|------|---------|---------|---------|
| 角A | angle_at_vertex(C, A, B) | self.angle_A | 使用arccos |
| 角B | angle_at_vertex(A, B, C) | self.angle_B | 使用arccos |
| 角C | angle_at_vertex(B, C, A) | self.angle_C | 使用arccos |
| 角度和 | angle_A + angle_B + angle_C | - | 必须 = π (180°) |

### 平行线构造（场景3）
| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 过C的平行线方向 | B - A | parallel_direction | 平行于AB |
| 平行线起点 | C - 3 * normalize(B-A) | parallel_start | 延伸3单位 |
| 平行线终点 | C + 3 * normalize(B-A) | parallel_end | 延伸3单位 |
| 角A副本位置 | C处，方向同角A | - | 内错角相等 |
| 角B副本位置 | C处，方向同角B | - | 内错角相等 |

### 验证检查
- [ ] 三角形内角和 = 180° (误差 < 1e-6)
- [ ] 平行线确实平行于AB (叉积 < 1e-8)
- [ ] 所有角度标记在正确侧
- [ ] 所有元素在边界内: x∈[-4,4], y∈[-7,7]

---

## Scene 1: 开场钩子 (0-5秒)

### 目的
快速吸引注意力，提出核心问题

### 元素
1. 作者标识 (顶部, y=7)
2. 钩子问题大字 (y=6)
3. 简单三角形闪现 (中心区域)

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2, run_time=0.3)` | 快速出现 |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` | "三个角加起来等于多少度?" |
| 1.1s | 三角形快速创建 | `Create(triangle, run_time=0.6)` | 简洁有力 |
| 1.7s | 三个角度标记闪烁 | `Flash` x 3 | 吸引注意到角 |
| 2.3s | 问号出现 | `FadeIn(question_mark, scale=1.2)` | "?" 大号黄色 |
| 3.5s | 等待 | `Wait(0.8)` | 留思考时间 |

### 清理
- FadeOut: hook_text, question_mark
- 保留: triangle, author_info

---

## Scene 2: 展示三角形与角度 (5-15秒)

### 目的
介绍三角形ABC及其三个内角

### 元素
1. 三角形ABC (已存在)
2. 顶点标签 A, B, C
3. 三个角的弧线标记（带颜色）
4. 角度数值显示（度数）

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 5.0s | 顶点标签淡入 | `FadeIn(VGroup(label_A, B, C))` | 同时出现 |
| 5.6s | 角A弧线创建 | `Create(angle_arc_A, run_time=0.6)` | 红色 |
| 6.2s | 角A度数显示 | `FadeIn(angle_value_A)` | "∠A" |
| 6.8s | 角B弧线创建 | `Create(angle_arc_B, run_time=0.6)` | 绿松石色 |
| 7.4s | 角B度数显示 | `FadeIn(angle_value_B)` | "∠B" |
| 8.0s | 角C弧线创建 | `Create(angle_arc_C, run_time=0.6)` | 黄色 |
| 8.6s | 角C度数显示 | `FadeIn(angle_value_C)` | "∠C" |
| 9.2s | 标题文字出现 | `Write(title)` | "三角形内角和定理" |
| 10.0s | 等待 | `Wait(1.5)` | 观察三个角 |

### 说明文字
```python
Text("认识这三个内角", font_size=24).move_to(DOWN * 4.5)
```

### 清理
- FadeOut: 说明文字
- 保留: triangle, labels, angle_arcs, angle_values, title

---

## Scene 3: 平行线证明法 (15-35秒)

### 目的
使用平行线和内错角证明内角和 = 180°

### 元素
1. 过C点作AB的平行线
2. 标记内错角
3. 角度平移动画
4. 汇聚成平角

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 15.0s | 说明文字 | `Write(explain_1)` | "过点C作AB的平行线" |
| 15.8s | 平行线创建 | `Create(parallel_line)` | 虚线，灰色 |
| 16.6s | 标记平行符号 | `FadeIn(parallel_marks)` | 双箭头标记 |
| 17.4s | 淡出说明 | `FadeOut(explain_1)` | |
| 18.0s | 说明文字2 | `Write(explain_2)` | "内错角相等" |
| 18.8s | 高亮角A | `angle_arc_A.animate.set_stroke(width=5)` | 加粗 |
| 19.6s | 复制角A到C | `TransformFromCopy(angle_arc_A, angle_A_copy)` | 红色角移到C处左侧 |
| 20.6s | 标记∠1=∠A | `FadeIn(label_angle1)` | |
| 21.4s | 恢复角A | `angle_arc_A.animate.set_stroke(width=3)` | |
| 22.2s | 高亮角B | `angle_arc_B.animate.set_stroke(width=5)` | |
| 23.0s | 复制角B到C | `TransformFromCopy(angle_arc_B, angle_B_copy)` | 绿色角移到C处右侧 |
| 24.0s | 标记∠2=∠B | `FadeIn(label_angle2)` | |
| 24.8s | 恢复角B | `angle_arc_B.animate.set_stroke(width=3)` | |
| 25.6s | 淡出说明2 | `FadeOut(explain_2)` | |

### 说明文字 (底部 y=-5)
```python
explain_1 = Text("过点C作AB的平行线", font_size=22)
explain_2 = Text("内错角相等", font_size=22)
```

### 清理
- 保留: parallel_line, angle_copies
- FadeOut: explain texts, parallel_marks

---

## Scene 4: 角度汇聚成平角 (35-45秒)

### 目的
展示 ∠1 + ∠C + ∠2 = 180°（平角）

### 元素
1. 三个角在C处的弧线
2. 平角标记
3. 公式推导

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 35.0s | 说明文字 | `Write(explain_3)` | "三个角拼成一条直线" |
| 35.8s | 高亮三个角 | 所有角闪烁 | Flash效果 |
| 36.6s | 平角弧线出现 | `Create(straight_angle_arc)` | 完整的半圆弧 |
| 37.6s | 平角标注 | `FadeIn(straight_angle_label)` | "180°" |
| 38.4s | 公式出现(步骤1) | `Write(formula_1)` | "∠1 + ∠C + ∠2 = 180°" |
| 39.4s | 等待 | `Wait(1.0)` | 理解 |
| 40.4s | 公式变换(步骤2) | `TransformMatchingTex(formula_1, formula_2)` | "∠A + ∠C + ∠B = 180°" |
| 41.6s | 最终公式 | `TransformMatchingTex(formula_2, formula_3)` | "∠A + ∠B + ∠C = 180°" |
| 42.8s | 等待 | `Wait(1.5)` | 强化记忆 |

### 公式位置
```python
formulas: y = -4.5
```

### 清理
- FadeOut: straight_angle_arc, formula_1, formula_2, parallel_line, angle_copies
- 保留: formula_3 (移至顶部)

---

## Scene 5: 回到原三角形 (45-52秒)

### 目的
回归原三角形，强调定理的普遍性

### 元素
1. 原三角形（放大）
2. 三个角闪烁
3. 最终公式框

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 45.0s | 公式移到顶部 | `formula_3.animate.move_to(UP*6)` | 腾出空间 |
| 45.8s | 三角形居中放大 | `triangle.animate.scale(1.2).move_to(UP*0.5)` | |
| 46.8s | 三角形填充渐变 | `triangle.animate.set_fill(opacity=0.2)` | 半透明 |
| 47.6s | 角度依次闪烁 | Flash A, B, C | 强调 |
| 48.8s | 说明文字 | `Write(conclusion)` | "任意三角形都成立!" |
| 50.0s | 公式加框 | `Create(formula_box)` | SurroundingRectangle |
| 51.0s | 等待 | `Wait(1.5)` | |

### 说明文字
```python
conclusion = Text("任意三角形都成立!", font_size=28, color=YELLOW).move_to(DOWN*4)
```

### 清理
- FadeOut: conclusion
- 保留: triangle, formula_3, formula_box

---

## Scene 6: 推论展示 (52-62秒)

### 目的
展示直角三角形和外角的推论

### 元素
1. 推论卡片
2. 图例

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 52.0s | 推论标题 | `Write(corollary_title)` | "重要推论" |
| 52.8s | 推论1出现 | `FadeIn(推论1_card, shift=LEFT)` | 从左滑入 |
| 54.0s | 推论2出现 | `FadeIn(推论2_card, shift=LEFT)` | 从左滑入 |
| 55.2s | 小三角形示例 | `Create(right_triangle_example)` | 右侧小图 |
| 56.4s | 标注90° | `FadeIn(right_angle_mark)` | |
| 57.6s | 等待 | `Wait(1.5)` | 阅读时间 |

### 推论卡片内容
```python
推论1: "直角三角形两锐角互余: ∠A + ∠B = 90°"
推论2: "外角 = 不相邻两内角之和"
```

### 位置
```python
cards: x = -3.5, y = 0 and -1.5
right_triangle: x = 2.5, y = 0
```

### 清理
- FadeOut: all corollary elements
- 保留: formula_3, author_info

---

## Scene 7: 片尾关注 (62-75秒)

### 目的
品牌展示，引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 62.0s | 清屏 | `FadeOut(triangle, formula_3, etc)` | |
| 62.8s | 作者名放大 | `Transform(author_info, author_large)` | 居中 |
| 63.6s | ID出现 | `FadeIn(author_id)` | @emptyandcalm |
| 64.4s | 关注文字 | `Write(follow_text)` | "关注我，学更多数学技巧!" |
| 65.4s | 三角形装饰 | `FadeIn(decorative_triangles)` | 6个小三角形围绕 |
| 66.4s | 旋转装饰 | `Rotate(decorative_triangles, PI)` | 慢速旋转 |
| 68.0s | 核心公式回顾 | `FadeIn(formula_reminder)` | "∠A+∠B+∠C=180°" 大号 |
| 69.5s | 等待 | `Wait(2.0)` | |
| 71.5s | 全部淡出 | `FadeOut(everything)` | |

### 文字大小
```python
author_large: font_size=40
author_id: font_size=32  
follow_text: font_size=30
formula_reminder: font_size=36
```

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保持在顶部 |
| triangle | Scene 1 | Scene 7 | 主三角形 |
| vertex_labels | Scene 2 | Scene 7 | A, B, C标签 |
| angle_arcs | Scene 2 | Scene 5 | 三个角的弧线 |
| parallel_line | Scene 3 | Scene 4 | 过C的平行线 |
| angle_copies | Scene 3 | Scene 4 | 复制的角 |
| straight_angle_arc | Scene 4 | Scene 4 | 平角弧线 |
| formulas | Scene 4 | Scene 6 | 公式推导 |
| corollary_cards | Scene 6 | Scene 6 | 推论卡片 |

---

## 技术注意事项

### 角度方向控制
- 所有角度使用 `Angle.from_three_points()` 创建
- 确保 `other_angle` 参数正确设置
- 验证角弧在三角形内部

### 平行线验证
```python
# 验证平行
assert abs(np.cross(AB_vec, parallel_vec)) < 1e-8
```

### 内错角位置
```python
# 角A副本：从C向左延伸
angle_A_copy_center = C + left_direction * offset
# 角B副本：从C向右延伸  
angle_B_copy_center = C + right_direction * offset
```

### 数值显示格式
```python
# 度数显示（取整）
angle_deg = int(np.degrees(angle_rad))
MathTex(f"{angle_deg}^\\circ")
```

---

## 预期效果检查

- [ ] 开场3秒内抓住注意力
- [ ] 证明过程清晰易懂（平行线法）
- [ ] 角度动画流畅自然
- [ ] 公式推导步骤明确
- [ ] 推论简洁实用
- [ ] 结尾有效引导关注
- [ ] 总时长控制在75秒内
- [ ] 无元素溢出或重叠
- [ ] 所有几何关系精确验证

---

*基于 Manim Community v0.19.2*
*配置: TikTok 竖屏 1080×1920*