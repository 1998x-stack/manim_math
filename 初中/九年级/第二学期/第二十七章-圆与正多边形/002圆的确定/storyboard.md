# 圆的确定 - 动画分镜脚本

## 元信息
- 目标时长: 70-85 秒
- 场景数量: 8 个
- 难度等级: 中级（九年级）
- 核心概念: 三点确定圆、外接圆、外心、垂直平分线

## 颜色配置
```python
COLOR_TRIANGLE = "#3498db"      # 蓝色 - 三角形
COLOR_CIRCLE = "#e74c3c"        # 红色 - 外接圆
COLOR_CIRCUMCENTER = "#f39c12"  # 橙色 - 外心
COLOR_PERP_BISECTOR = "#2ecc71" # 绿色 - 垂直平分线
COLOR_RADIUS = "#9b59b6"        # 紫色 - 半径
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
```

## 几何预计算清单

| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 三角形顶点A | 预设坐标 | self.A = np.array([-2.5, 0, 0]) * SCALE + OFFSET |
| 三角形顶点B | 预设坐标 | self.B = np.array([2.5, -1, 0]) * SCALE + OFFSET |
| 三角形顶点C | 预设坐标 | self.C = np.array([0, 2.5, 0]) * SCALE + OFFSET |
| AB中点 | (A+B)/2 | self.M_AB = (self.A + self.B) / 2 |
| BC中点 | (B+C)/2 | self.M_BC = (self.B + self.C) / 2 |
| CA中点 | (C+A)/2 | self.M_CA = (self.C + self.A) / 2 |
| 外心O | 垂直平分线交点 | self.O = self.calculate_circumcenter() |
| 外接圆半径 | \|OA\| | self.radius = np.linalg.norm(self.O - self.A) |
| AB垂直平分线方向 | 垂直于AB | perp_AB = rotate(AB, 90°) |
| BC垂直平分线方向 | 垂直于BC | perp_BC = rotate(BC, 90°) |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 引发思考 - 三个点能确定一个圆吗？

### 元素
1. 作者标识（顶部）
2. 钩子问题："三个点，能画出一个圆吗？"
3. 三个随机放置的点

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` |
| 1.1s | 三个点依次出现 | `FadeIn(dot_A), FadeIn(dot_B), FadeIn(dot_C)` |
| 2.1s | 问号闪烁 | `Indicate(question_mark)` |
| 3.1s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_text
- 保留: dots, author_info

---

## Scene 2: 共线检查 (5-6秒)
**目的**: 说明三点共线无法确定圆

### 元素
1. 小标题："条件：三点不共线"
2. 共线的三个点（反例）
3. 叉号标记
4. 说明文字："共线的点无法确定圆"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题写入 | `Write(subtitle)` |
| 0.5s | 创建共线三点 | `FadeIn(collinear_dots)` |
| 1.0s | 连接成线 | `Create(line)` |
| 1.5s | 叉号出现 | `FadeIn(cross_mark, scale=0.5)` |
| 2.0s | 说明文字 | `FadeIn(explanation)` |
| 3.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有共线元素
- 保留: subtitle 短暂后 FadeOut

---

## Scene 3: 非共线三点 (4-5秒)
**目的**: 展示正确情况 - 不共线的三点

### 元素
1. 说明："不共线的三点 ✓"
2. 三个不共线的点（A, B, C）
3. 对勾标记
4. 连接成三角形

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 说明文字淡入 | `FadeIn(explanation)` |
| 0.5s | 三点重新定位到非共线位置 | `dots.animate.move_to(...)` |
| 1.5s | 对勾出现 | `FadeIn(check_mark, scale=0.5)` |
| 2.0s | 连接成三角形 | `Create(triangle)` |
| 3.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: explanation, check_mark
- 保留: triangle, dots

---

## Scene 4: 垂直平分线AB (8-10秒)
**目的**: 构造第一条垂直平分线

### 元素
1. 小标题："寻找外心 - 垂直平分线"
2. AB边高亮
3. AB中点M
4. AB的垂直平分线
5. 说明："垂直平分线上的点到A、B距离相等"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题写入 | `Write(subtitle)` |
| 0.6s | AB边高亮 | `Indicate(line_AB, color=HIGHLIGHT)` |
| 1.2s | 中点M出现 | `FadeIn(dot_M, scale=0.5)` |
| 1.8s | 垂直平分线生长 | `GrowFromCenter(perp_bisector_AB)` |
| 2.8s | 垂直符号 | `FadeIn(right_angle_mark)` |
| 3.5s | 说明文字淡入 | `FadeIn(explanation)` |
| 5.0s | 等待理解 | `Wait(2.0)` |

### 几何验证
```python
# 验证垂直关系
vec_AB = self.B - self.A
vec_perp = perp_direction
dot_product = np.dot(vec_AB[:2], vec_perp[:2])
assert abs(dot_product) < 1e-6  # 垂直
```

### 清理
- FadeOut: explanation, right_angle_mark
- 保留: perp_bisector_AB, dot_M, subtitle

---

## Scene 5: 垂直平分线BC (6-8秒)
**目的**: 构造第二条垂直平分线

### 元素
1. BC边高亮
2. BC中点N
3. BC的垂直平分线
4. 说明："两条垂直平分线相交"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | BC边高亮 | `Indicate(line_BC, color=HIGHLIGHT)` |
| 0.6s | 中点N出现 | `FadeIn(dot_N, scale=0.5)` |
| 1.2s | 垂直平分线生长 | `GrowFromCenter(perp_bisector_BC)` |
| 2.2s | 垂直符号 | `FadeIn(right_angle_mark_2)` |
| 3.0s | 说明文字 | `FadeIn(explanation)` |
| 4.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: explanation, right_angle_marks
- 保留: perp_bisector_AB, perp_bisector_BC, subtitle

---

## Scene 6: 外心出现 (7-9秒)
**目的**: 标记外心并说明其性质

### 元素
1. 外心点O（两垂直平分线交点）
2. 外心标注"O"
3. 标签"外心"
4. 公式："OA = OB = OC"
5. 三条半径虚线

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 交点闪光 | `Flash(intersection_point)` |
| 0.5s | 外心点出现 | `FadeIn(dot_O, scale=0.5)` |
| 1.0s | 标注"O" | `FadeIn(label_O)` |
| 1.5s | 标签"外心" | `FadeIn(label_circumcenter)` |
| 2.5s | 三条半径依次出现 | `Create(radius_OA), Create(radius_OB), Create(radius_OC)` |
| 4.5s | 公式淡入 | `FadeIn(formula)` |
| 5.5s | 半径同时高亮（验证等长） | `Indicate(radii_group)` |
| 6.5s | 等待 | `Wait(1.5)` |

### 几何验证
```python
# 验证外心到三顶点距离相等
dist_OA = np.linalg.norm(self.O - self.A)
dist_OB = np.linalg.norm(self.O - self.B)
dist_OC = np.linalg.norm(self.O - self.C)
assert abs(dist_OA - dist_OB) < 1e-6
assert abs(dist_OB - dist_OC) < 1e-6
```

### 清理
- FadeOut: subtitle, perp_bisectors, dot_M, dot_N
- 保留: dot_O, label_O, radii

---

## Scene 7: 外接圆绘制 (8-10秒)
**目的**: 绘制外接圆，完成"三点确定圆"的演示

### 元素
1. 外接圆（以O为圆心，OA为半径）
2. 说明："这就是三角形的外接圆"
3. 强调：圆经过三个顶点
4. 公式："不共线的三点确定一个圆"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 外接圆描绘 | `Create(circumcircle, run_time=2.0)` |
| 2.0s | 说明文字 | `FadeIn(explanation)` |
| 3.0s | 三个顶点依次闪烁 | `Indicate(dot_A), Indicate(dot_B), Indicate(dot_C)` |
| 4.5s | 公式淡入 | `FadeIn(main_formula)` |
| 5.5s | 圆旋转一周（强调完整性） | `Rotate(circumcircle, TAU, run_time=1.5)` |
| 7.0s | 等待 | `Wait(1.5)` |

### 几何验证
```python
# 验证圆确实经过三个顶点
for point in [self.A, self.B, self.C]:
    dist = np.linalg.norm(point - self.O)
    assert abs(dist - self.radius) < 1e-6
```

### 清理
- FadeOut: explanation, radii (虚线半径)
- 保留: circumcircle, triangle, dot_O, label_O, main_formula

---

## Scene 8: 总结与片尾 (10-12秒)
**目的**: 知识总结，强化记忆

### 元素
1. 图形缩小移到上方
2. 知识卡片（3个要点）
3. 总结文字："掌握外接圆，解锁几何新技能！"
4. 作者关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 整体缩小并上移 | `VGroup(...).animate.scale(0.6).move_to(UP*4)` |
| 1.0s | 知识卡片1："不共线三点确定圆" | `FadeIn(card_1, shift=RIGHT)` |
| 2.0s | 知识卡片2："外心：垂直平分线交点" | `FadeIn(card_2, shift=RIGHT)` |
| 3.0s | 知识卡片3："外心性质：OA=OB=OC" | `FadeIn(card_3, shift=RIGHT)` |
| 4.5s | 总结文字 | `FadeIn(summary_text, shift=UP*0.3)` |
| 5.5s | 作者信息放大 | `author_info.animate.scale(1.5).move_to(UP*1)` |
| 6.5s | 关注提示 | `FadeIn(follow_text, scale=1.1)` |
| 7.5s | 装饰动画 | `Rotate(decorations, PI)` |
| 9.0s | 等待 | `Wait(1.5)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 顶部作者信息 |
| dot_A, dot_B, dot_C | Scene 1 | Scene 8 | 三角形顶点 |
| triangle | Scene 3 | Scene 8 | 主三角形 |
| perp_bisector_AB | Scene 4 | Scene 6 | AB垂直平分线 |
| perp_bisector_BC | Scene 5 | Scene 6 | BC垂直平分线 |
| dot_O | Scene 6 | Scene 8 | 外心 |
| circumcircle | Scene 7 | Scene 8 | 外接圆 |
| radii (虚线) | Scene 6 | Scene 7 | 半径 |
| knowledge_cards | Scene 8 | Scene 8 | 知识卡片 |

---

## 关键技术点

### 1. 外心的精确计算
```python
def calculate_circumcenter(A, B, C):
    """使用解析公式计算外心"""
    ax, ay = A[0], A[1]
    bx, by = B[0], B[1]
    cx, cy = C[0], C[1]
    
    D = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    
    ux = ((ax**2 + ay**2) * (by - cy) + 
          (bx**2 + by**2) * (cy - ay) + 
          (cx**2 + cy**2) * (ay - by)) / D
    
    uy = ((ax**2 + ay**2) * (cx - bx) + 
          (bx**2 + by**2) * (ax - cx) + 
          (cx**2 + cy**2) * (bx - ax)) / D
    
    return np.array([ux, uy, 0])
```

### 2. 垂直平分线的精确绘制
```python
def perpendicular_bisector(P1, P2, length=3.0):
    """计算线段的垂直平分线"""
    midpoint = (P1 + P2) / 2
    segment = P2 - P1
    # 垂直方向（旋转90度）
    perpendicular = np.array([-segment[1], segment[0], 0])
    perpendicular = perpendicular / np.linalg.norm(perpendicular)
    
    start = midpoint - perpendicular * length / 2
    end = midpoint + perpendicular * length / 2
    
    return start, end
```

### 3. 验证点不共线
```python
def are_collinear(A, B, C):
    """验证三点是否共线"""
    # 使用三角形面积法
    area = 0.5 * abs(
        A[0] * (B[1] - C[1]) + 
        B[0] * (C[1] - A[1]) + 
        C[0] * (A[1] - B[1])
    )
    return area < 1e-6
```

### 4. 直角标记
```python
def create_right_angle_mark(corner, point1, point2, size=0.2):
    """创建直角标记"""
    vec1 = (point1 - corner) / np.linalg.norm(point1 - corner) * size
    vec2 = (point2 - corner) / np.linalg.norm(point2 - corner) * size
    
    return Polygon(
        corner,
        corner + vec1,
        corner + vec1 + vec2,
        corner + vec2,
        color=YELLOW,
        stroke_width=1.5
    )
```

---

## 预期时长分配

| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1: 开场钩子 | 3-4s | 4s |
| Scene 2: 共线检查 | 5-6s | 10s |
| Scene 3: 非共线三点 | 4-5s | 15s |
| Scene 4: 垂直平分线AB | 8-10s | 25s |
| Scene 5: 垂直平分线BC | 6-8s | 33s |
| Scene 6: 外心出现 | 7-9s | 42s |
| Scene 7: 外接圆绘制 | 8-10s | 52s |
| Scene 8: 总结 | 10-12s | 64s |
| **总计** | **70-85s** | |

---

## 风格统一要点

1. **几何精确性**：所有坐标通过公式计算，外心、中点、垂足等
2. **动画节奏**：重要概念（外心、外接圆）停留2-3秒
3. **视觉引导**：高亮 → 闪烁 → 标注，层次分明
4. **配色一致**：每类元素专属颜色
5. **边界检查**：主内容在 y ∈ [-3, 5]，文字在 y ∈ [-6, -3]

---

## 验证清单

### 几何验证
- [ ] 三点不共线
- [ ] 外心到三顶点距离相等
- [ ] 垂直平分线确实垂直
- [ ] 外接圆半径 = 外心到任意顶点距离
- [ ] 所有元素在边界内

### LaTeX检查
- [ ] 无中文字符在 MathTex 中
- [ ] 使用 `^\circ` 而非 `°`
- [ ] 原始字符串 `r"..."`

### 动画流畅性
- [ ] 场景过渡自然
- [ ] 无元素突然消失/出现
- [ ] 颜色对比度足够
- [ ] 字体大小适中