# 点的对称变换 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 6 个
- 难度等级: 基础（七年级）
- 目标：理解点关于坐标轴和原点的对称规律

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 原点
COLOR_SYMMETRY_X = "#e74c3c"   # 红色 - 关于x轴对称
COLOR_SYMMETRY_Y = "#2ecc71"   # 绿色 - 关于y轴对称
COLOR_SYMMETRY_O = "#f39c12"   # 橙色 - 关于原点对称
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_AXES = WHITE             # 白色 - 坐标轴
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 原点P | (2, 3) | self.point_P | 第一象限原始点 |
| 关于x轴对称P' | (2, -3) | self.point_Px | x不变，y取反 |
| 关于y轴对称P'' | (-2, 3) | self.point_Py | y不变，x取反 |
| 关于原点对称P''' | (-2, -3) | self.point_Po | x和y都取反 |
| P到x轴垂线 | - | self.perp_to_x | 用于展示对称 |
| P到y轴垂线 | - | self.perp_to_y | 用于展示对称 |
| 原点连线 | - | self.line_origin | 连接P和P''' |

**重要验证**：
- 验证P和P'关于x轴距离相等
- 验证P和P''关于y轴距离相等
- 验证P和P'''关于原点距离相等且共线

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出对称的概念

### 元素
1. 作者标识（顶部）
2. 钩子问题（大字）
3. 一个点和它的三个"影子"闪烁

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` "点的对称有什么规律?" |
| 1.0s | 原点P闪烁 | `Flash(dot_P, color=BLUE)` |
| 1.5s | 三个对称点同时闪烁 | `Flash(dots_group)` |
| 2.5s | 等待 | `Wait(0.8)` |

### 清理
- FadeOut: hook_text, mystery_dots
- 保留: author_info

---

## Scene 2: 建立坐标系和原点P (5-6秒)
**目的**: 介绍坐标系和原始点

### 元素
1. 坐标系
2. 点P(2, 3)在第一象限
3. 坐标标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 坐标轴生长 | `Create(axes)` |
| 1.0s | 点P出现 | `FadeIn(dot_P, scale=0.5), Flash(dot_P)` |
| 1.5s | 坐标标注 | `Write(label_P "P(2, 3)")` |
| 2.5s | 说明文字 | `FadeIn(explain)` "从这个点开始探索对称" |
| 4.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: explain
- 保留: axes, dot_P, label_P

---

## Scene 3: 关于x轴对称 (12-15秒)
**目的**: 理解关于x轴对称的规律

### 元素
1. 标题 "关于x轴对称"
2. x轴高亮
3. P到x轴的垂线
4. 对称点P'(2, -3)
5. 公式 (x, y) → (x, -y)
6. 距离标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` "关于x轴对称" |
| 0.5s | x轴高亮 | `x_axis.animate.set_color(YELLOW)` |
| 1.2s | P到x轴垂线 | `Create(perpendicular)` 虚线 |
| 1.9s | 在x轴下方标记等距点 | `Flash(foot)` 垂足闪烁 |
| 2.6s | 对称点P'出现 | `FadeIn(dot_Px), Flash(dot_Px)` |
| 3.3s | 坐标标注 | `Write(label_Px "P'(2, -3)")` |
| 4.0s | 连线PP' | `Create(line_PP')` 穿过x轴 |
| 4.7s | 距离标注 | `FadeIn(distance_marks)` 两侧距离相等 |
| 5.7s | 规律公式 | `Write(formula)` "(x,y)→(x,-y)" |
| 7.0s | 重点提示 | `FadeIn(highlight)` "横坐标不变，纵坐标取反" |
| 9.0s | 等待 | `Wait(2.0)` 让学生理解 |

### 清理
- FadeOut: title, perpendicular, line_PP', distance_marks, formula, highlight
- x轴恢复颜色
- 保留: dot_P, label_P, dot_Px, label_Px (变淡)

---

## Scene 4: 关于y轴对称 (12-15秒)
**目的**: 理解关于y轴对称的规律

### 元素
1. 标题 "关于y轴对称"
2. y轴高亮
3. P到y轴的垂线
4. 对称点P''(-2, 3)
5. 公式 (x, y) → (-x, y)
6. 距离标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` "关于y轴对称" |
| 0.5s | y轴高亮 | `y_axis.animate.set_color(YELLOW)` |
| 1.2s | P到y轴垂线 | `Create(perpendicular)` 虚线 |
| 1.9s | 在y轴左侧标记等距点 | `Flash(foot)` 垂足闪烁 |
| 2.6s | 对称点P''出现 | `FadeIn(dot_Py), Flash(dot_Py)` |
| 3.3s | 坐标标注 | `Write(label_Py "P''(-2, 3)")` |
| 4.0s | 连线PP'' | `Create(line_PP'')` 穿过y轴 |
| 4.7s | 距离标注 | `FadeIn(distance_marks)` 两侧距离相等 |
| 5.7s | 规律公式 | `Write(formula)` "(x,y)→(-x,y)" |
| 7.0s | 重点提示 | `FadeIn(highlight)` "纵坐标不变，横坐标取反" |
| 9.0s | 等待 | `Wait(2.0)` 让学生理解 |

### 清理
- FadeOut: title, perpendicular, line_PP'', distance_marks, formula, highlight
- y轴恢复颜色
- 保留: dot_P, label_P, dot_Py, label_Py (变淡)

---

## Scene 5: 关于原点对称 (12-15秒)
**目的**: 理解关于原点对称的规律

### 元素
1. 标题 "关于原点对称"
2. 原点O高亮
3. 连接P和对称点P'''的直线（穿过原点）
4. 对称点P'''(-2, -3)
5. 公式 (x, y) → (-x, -y)
6. 距离标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` "关于原点对称" |
| 0.5s | 原点O高亮 | `Indicate(origin_dot, scale_factor=2)` |
| 1.2s | 从P画线穿过原点 | `Create(line_through_O)` 虚线延伸 |
| 2.2s | 在对侧标记等距点 | `Flash(symmetric_point)` |
| 2.9s | 对称点P'''出现 | `FadeIn(dot_Po), Flash(dot_Po)` |
| 3.6s | 坐标标注 | `Write(label_Po "P'''(-2, -3)")` |
| 4.3s | 完整连线 | `line_through_O.animate.set_color(RED)` |
| 5.0s | 距离标注 | `FadeIn(distance_marks)` 两侧距离相等 |
| 6.0s | 规律公式 | `Write(formula)` "(x,y)→(-x,-y)" |
| 7.3s | 重点提示 | `FadeIn(highlight)` "横纵坐标都取反" |
| 9.3s | 三点共线说明 | `FadeIn(explain)` "三点共线且原点平分" |
| 11.3s | 等待 | `Wait(2.0)` 让学生理解 |

### 清理
- FadeOut: title, line_through_O, distance_marks, formula, highlight, explain
- 保留: dot_P, dot_Po (其他点变淡)

---

## Scene 6: 总结与关注 (8-10秒)
**目的**: 总结规律，引导关注

### 元素
1. 四个点同时显示（P和三个对称点）
2. 三条对称规律总结
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 所有点恢复显示 | `dots_group.animate.set_opacity(1)` |
| 0.5s | 坐标系缩小淡化 | `axes.animate.scale(0.6).fade(0.7)` |
| 1.2s | 总结标题 | `Write(summary_title)` "对称规律总结" |
| 1.7s | 规律1 | `FadeIn(rule1, shift=RIGHT)` "关于x轴: (x,y)→(x,-y)" |
| 2.4s | 规律2 | `FadeIn(rule2, shift=RIGHT)` "关于y轴: (x,y)→(-x,y)" |
| 3.1s | 规律3 | `FadeIn(rule3, shift=RIGHT)` "关于原点: (x,y)→(-x,-y)" |
| 4.0s | 装饰框 | `Create(box)` 框住三条规律 |
| 5.0s | 作者放大 | `author_info.animate.scale(1.5).move_to(UP)` |
| 5.7s | 关注文字 | `Write(follow_text)` "关注我, 学更多数学!" |
| 6.7s | 装饰动画 | `Rotate(decorations)` |
| 8.7s | 淡出 | `FadeOut(all)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 始终保留 |
| axes | Scene 2 | Scene 6 | 主坐标系 |
| dot_P | Scene 2 | Scene 6 | 原始点 |
| dot_Px | Scene 3 | Scene 6 | 关于x轴对称 |
| dot_Py | Scene 4 | Scene 6 | 关于y轴对称 |
| dot_Po | Scene 5 | Scene 6 | 关于原点对称 |
| perpendiculars | Scene 3-4 | 各场景内 | 临时辅助线 |
| connecting_lines | Scene 3-5 | 各场景内 | 连接线 |

---

## 技术要点

### 1. 对称点精确计算
```python
# 关于x轴对称
def reflect_over_x_axis(point):
    x, y, z = point
    return np.array([x, -y, z])

# 关于y轴对称
def reflect_over_y_axis(point):
    x, y, z = point
    return np.array([-x, y, z])

# 关于原点对称
def reflect_over_origin(point):
    x, y, z = point
    return np.array([-x, -y, z])
```

### 2. 距离验证
```python
# 验证关于x轴对称：到x轴距离相等
dist_P_to_x = abs(point_P[1])
dist_Px_to_x = abs(point_Px[1])
assert abs(dist_P_to_x - dist_Px_to_x) < epsilon

# 验证关于y轴对称：到y轴距离相等
dist_P_to_y = abs(point_P[0])
dist_Py_to_y = abs(point_Py[0])
assert abs(dist_P_to_y - dist_Py_to_y) < epsilon

# 验证关于原点对称：到原点距离相等
dist_P_to_O = np.linalg.norm(point_P)
dist_Po_to_O = np.linalg.norm(point_Po)
assert abs(dist_P_to_O - dist_Po_to_O) < epsilon
```

### 3. 共线验证（原点对称）
```python
# 验证P、O、P'''三点共线
# 使用叉积：如果共线，叉积为0
vec_OP = point_P - origin
vec_OPo = point_Po - origin
cross_product = np.cross(vec_OP[:2], vec_OPo[:2])
assert abs(cross_product) < epsilon
```

### 4. 对称轴高亮动画
```python
# x轴高亮（用于Scene 3）
x_axis_highlight = axes.x_axis.copy().set_color(YELLOW).set_stroke(width=4)
self.play(FadeIn(x_axis_highlight), run_time=0.5)

# y轴高亮（用于Scene 4）
y_axis_highlight = axes.y_axis.copy().set_color(YELLOW).set_stroke(width=4)
self.play(FadeIn(y_axis_highlight), run_time=0.5)
```

---

## 动画节奏控制

### 关键停顿时机
1. **Scene 3 末尾**: 2.0s - 理解关于x轴对称规律
2. **Scene 4 末尾**: 2.0s - 理解关于y轴对称规律
3. **Scene 5 末尾**: 2.0s - 理解关于原点对称规律（最难）

### 速度建议
- 坐标系建立: 快速 (已经学过)
- 第一个对称: 慢速 (详细讲解)
- 后续对称: 中速 (类比理解)
- 原点对称: 慢速 (最复杂，需要理解共线)
- 总结: 慢速 (强化记忆)

---

## 预期问题与解决方案

### 问题1: 对称点可能超出边界
**解决**: 选择合适的原始点坐标，确保所有对称点都在可见范围内
- 原点P选择(2, 3)，所有对称点都在 [-4, 4] × [-4, 4] 范围内

### 问题2: 标签可能重叠
**解决**: 使用智能定位，不同象限的点标签放在不同方向

### 问题3: 原点对称的共线性不明显
**解决**: 
- 使用虚线连接三点
- 标注距离相等
- 说明"三点共线且原点平分"

### 问题4: 学生可能混淆三种对称
**解决**:
- 使用不同颜色区分
- 每种对称都有明确的公式
- 最后总结时对比展示

---

## 验证清单

### 几何精确性
- [ ] P'关于x轴与P对称（y坐标相反，x相同）
- [ ] P''关于y轴与P对称（x坐标相反，y相同）
- [ ] P'''关于原点与P对称（x和y都相反）
- [ ] P和P'到x轴距离相等
- [ ] P和P''到y轴距离相等
- [ ] P和P'''到原点距离相等
- [ ] P、O、P'''三点共线

### 视觉清晰度
- [ ] 所有点在安全区域内
- [ ] 标签不重叠
- [ ] 颜色区分明显
- [ ] 公式清晰可读

### 教学有效性
- [ ] 每种对称都有详细讲解
- [ ] 规律总结清晰
- [ ] 难点（原点对称）有足够时间

---

## 总预估时长
- Scene 1: 3-4s
- Scene 2: 5-6s
- Scene 3: 12-15s
- Scene 4: 12-15s
- Scene 5: 12-15s
- Scene 6: 8-10s
- **总计**: 约 52-65 秒 ✓ (在60-75秒目标范围内)

---

## 下一步
1. ✅ 分镜脚本完成
2. ⏳ 编写 Python 代码
3. ⏳ 创建 verify_geometry.py
4. ⏳ 渲染测试