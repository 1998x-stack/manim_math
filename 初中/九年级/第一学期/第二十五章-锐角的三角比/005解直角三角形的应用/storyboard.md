# 解直角三角形的应用 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等
- 目标受众: 九年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要几何元素
COLOR_SECONDARY = "#e74c3c"      # 红色 - 强调元素
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_BUILDING = "#95a5a6"       # 建筑物颜色
COLOR_GROUND = "#2c3e50"         # 地面颜色
COLOR_SKY = "#ecf0f1"            # 天空颜色
COLOR_SLOPE = "#16a085"          # 斜坡颜色
```

## 几何预计算清单

### 场景1-2: 仰角问题（测量建筑物）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 观察点 | 原点 | self.observer |
| 建筑物底部 | 水平距离30m处 | self.building_base |
| 建筑物顶部 | 底部+高度h | self.building_top |
| 仰角 | 45° | self.elevation_angle |
| 视线 | observer到building_top | self.sight_line |
| 水平线 | observer水平延伸 | self.horizon_line |
| 高度 | 距离 × tan(45°) | self.height |

### 场景3-4: 俯角问题（山顶观察）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 山顶观察点 | 高度100m | self.peak |
| 目标点 | 地面水平距离处 | self.target |
| 俯角 | 30° | self.depression_angle |
| 视线 | peak到target | self.sight_line_down |
| 水平参考线 | peak水平延伸 | self.horizon_ref |
| 水平距离 | 高度 / tan(30°) | self.distance |

### 场景5-6: 坡度问题（道路设计）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 起点 | 原点 | self.slope_start |
| 终点 | 水平+垂直 | self.slope_end |
| 坡角 | arctan(i) | self.slope_angle |
| 坡度 | i = 1:5 = 0.2 | self.slope_i |
| 垂直高度 | 10m | self.vertical_rise |
| 水平距离 | 高度/坡度 = 50m | self.horizontal_run |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识（顶部小字）
2. 钩子问题文字
3. 建筑物剪影
4. 问号动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write("如何测量高楼的高度?")` |
| 1.0s | 建筑物剪影创建 | `Create(building_silhouette)` |
| 1.8s | 问号闪烁 | `Flash(question_mark)` |
| 2.5s | 等待 | `Wait(0.8)` |

### 清理
- FadeOut: 钩子文字、问号
- 保留: 作者信息、建筑物轮廓

---

## Scene 2: 仰角问题 - 测量建筑物高度 (12-15秒)
**目的**: 展示仰角的定义和应用

### 元素
1. 标题："仰角 - Elevation Angle"
2. 直角三角形（观察者-建筑底部-建筑顶部）
3. 水平参考线（虚线）
4. 仰角标记（角弧+标签）
5. 已知数据标注
6. 计算过程

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 绘制地面和建筑物 | `Create(ground, building)` |
| 1.2s | 标记观察者位置 | `FadeIn(observer_dot)` |
| 1.8s | 绘制水平参考线 | `Create(horizon_line)` |
| 2.3s | 绘制视线 | `Create(sight_line)` |
| 3.0s | 标记仰角 | `Create(angle_arc)` + `Write("α=45°")` |
| 3.8s | 标注距离 | `Write("距离=30m")` |
| 4.5s | 高亮直角三角形 | `triangle.animate.set_color(YELLOW)` |
| 5.2s | 显示公式 | `Write("tan α = h/30")` |
| 6.0s | 计算过程 | `TransformMatchingTex("h = 30×tan 45°")` |
| 6.8s | 结果 | `Write("h = 30m")` |
| 7.5s | 等待理解 | `Wait(1.5)` |

### 几何精确计算
```python
# 观察者位置
self.observer = np.array([-3.0, -2.0, 0])

# 建筑物底部（水平距离30m，缩放后为3单位）
self.building_base = self.observer + np.array([3.0, 0, 0])

# 仰角45°，计算建筑物高度
self.elevation_angle = 45 * DEGREES
self.horizontal_dist = 3.0  # 缩放后的单位
self.building_height = self.horizontal_dist * np.tan(self.elevation_angle)

# 建筑物顶部
self.building_top = self.building_base + np.array([0, self.building_height, 0])

# 验证：仰角应该等于45°
calculated_angle = np.arctan(self.building_height / self.horizontal_dist)
assert abs(calculated_angle - self.elevation_angle) < 1e-6
```

### 清理
- FadeOut: 标题、公式、标注
- Transform: 建筑物和三角形缩小移到左上角
- 保留: 作者信息

---

## Scene 3: 俯角问题 - 山顶观察 (12-15秒)
**目的**: 展示俯角的定义和应用

### 元素
1. 标题："俯角 - Depression Angle"
2. 山的轮廓
3. 山顶观察点
4. 地面目标点
5. 水平参考线（虚线）
6. 俯角标记（角弧+标签）
7. 直角三角形
8. 计算过程

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 绘制山的轮廓 | `Create(mountain)` |
| 1.2s | 标记山顶观察点 | `FadeIn(peak_dot)` |
| 1.8s | 绘制水平参考线 | `Create(horizon_ref)` |
| 2.3s | 标记地面目标 | `FadeIn(target_dot)` |
| 2.8s | 绘制视线 | `Create(sight_line_down)` |
| 3.5s | 标记俯角 | `Create(angle_arc)` + `Write("β=30°")` |
| 4.2s | 标注高度 | `Write("高度=100m")` |
| 4.9s | 高亮直角三角形 | `triangle.animate.set_color(YELLOW)` |
| 5.6s | 显示公式 | `Write("tan β = 100/d")` |
| 6.4s | 计算过程 | `TransformMatchingTex("d = 100/tan 30°")` |
| 7.2s | 结果 | `Write("d ≈ 173m")` |
| 8.0s | 等待理解 | `Wait(1.5)` |

### 几何精确计算
```python
# 山顶位置
self.peak = np.array([0, 2.5, 0])

# 山的高度（缩放单位）
self.mountain_height = 2.5

# 俯角30°
self.depression_angle = 30 * DEGREES

# 计算水平距离
self.horizontal_distance = self.mountain_height / np.tan(self.depression_angle)

# 目标点位置
self.target = self.peak + np.array([self.horizontal_distance, -self.mountain_height, 0])

# 水平参考线
self.horizon_ref_end = self.peak + np.array([4.0, 0, 0])

# 验证：俯角应该等于30°
vec_horizon = np.array([1, 0, 0])
vec_sight = self.target - self.peak
vec_sight_normalized = vec_sight / np.linalg.norm(vec_sight)
calculated_angle = np.arccos(np.dot(vec_horizon, vec_sight_normalized))
assert abs(calculated_angle - self.depression_angle) < 1e-6
```

### 清理
- FadeOut: 标题、山、公式、标注
- 保留: 作者信息

---

## Scene 4: 仰角vs俯角对比 (6-8秒)
**目的**: 对比仰角和俯角的区别

### 元素
1. 左右分屏
2. 左侧：仰角示意图（简化）
3. 右侧：俯角示意图（简化）
4. 对比文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 分割线出现 | `Create(divider)` |
| 0.4s | 左侧仰角图淡入 | `FadeIn(elevation_diagram)` |
| 0.8s | 右侧俯角图淡入 | `FadeIn(depression_diagram)` |
| 1.4s | 标注"仰角" | `Write("仰角: 向上看")` |
| 2.0s | 标注"俯角" | `Write("俯角: 向下看")` |
| 2.6s | 高亮水平线 | `horizon_lines.animate.set_color(YELLOW)` |
| 3.2s | 文字提示 | `Write("都以水平线为基准")` |
| 4.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有元素
- 保留: 作者信息

---

## Scene 5: 坡度问题 - 道路设计 (12-15秒)
**目的**: 展示坡度和坡角的关系

### 元素
1. 标题："坡度与坡角"
2. 道路斜坡（带纹理）
3. 直角三角形
4. 坡角标记
5. 坡度公式
6. 垂直高度和水平距离标注
7. 计算过程

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 绘制地面 | `Create(ground)` |
| 1.0s | 绘制斜坡 | `Create(slope)` |
| 1.8s | 标记起点和终点 | `FadeIn(start_dot, end_dot)` |
| 2.4s | 绘制辅助线形成直角三角形 | `Create(vertical_line, horizontal_line)` |
| 3.2s | 标记直角 | `Create(right_angle_mark)` |
| 3.8s | 标记坡角 | `Create(angle_arc)` + `Write("α")` |
| 4.5s | 标注尺寸 | `Write("h=10m", "d=50m")` |
| 5.3s | 显示坡度定义 | `Write("i = h/d")` |
| 6.1s | 计算坡度 | `TransformMatchingTex("i = 10/50 = 1/5")` |
| 6.9s | 关系公式 | `Write("i = tan α")` |
| 7.7s | 计算坡角 | `Write("α = arctan(1/5) ≈ 11.3°")` |
| 8.5s | 等待理解 | `Wait(1.5)` |

### 几何精确计算
```python
# 坡度参数
self.slope_ratio = 1/5  # i = 1:5
self.vertical_rise = 1.0  # 缩放单位
self.horizontal_run = self.vertical_rise / self.slope_ratio  # 5.0单位

# 起点和终点
self.slope_start = np.array([-2.5, -1.5, 0])
self.slope_end = self.slope_start + np.array([self.horizontal_run, self.vertical_rise, 0])

# 坡角计算
self.slope_angle = np.arctan(self.slope_ratio)

# 验证：tan(坡角) 应该等于坡度
calculated_slope = np.tan(self.slope_angle)
assert abs(calculated_slope - self.slope_ratio) < 1e-6

# 直角三角形的三个顶点
self.triangle_bottom_left = self.slope_start
self.triangle_bottom_right = np.array([self.slope_end[0], self.slope_start[1], 0])
self.triangle_top_right = self.slope_end

# 验证直角
vec1 = self.triangle_bottom_right - self.triangle_bottom_left
vec2 = self.triangle_top_right - self.triangle_bottom_right
dot_product = np.dot(vec1[:2], vec2[:2])
assert abs(dot_product) < 1e-6  # 应该垂直
```

### 清理
- FadeOut: 标题、斜坡、公式、标注
- 保留: 作者信息

---

## Scene 6: 实际应用示例 (8-10秒)
**目的**: 展示更多实际应用场景

### 元素
1. 三个应用场景图标/简图
   - 测量树高
   - 桥梁设计
   - 航海导航
2. 文字说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题"更多应用" | `Write(title)` |
| 0.6s | 场景1淡入 | `FadeIn(tree_scene)` + `Write("测量树高")` |
| 1.4s | 场景2淡入 | `FadeIn(bridge_scene)` + `Write("桥梁坡度")` |
| 2.2s | 场景3淡入 | `FadeIn(ship_scene)` + `Write("航海定位")` |
| 3.0s | 关键提示 | `Write("关键：构造直角三角形")` |
| 4.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有应用场景
- 保留: 作者信息

---

## Scene 7: 总结与片尾 (8-10秒)
**目的**: 总结要点，引导关注

### 元素
1. 三个核心概念卡片
2. 关注提示
3. 作者信息放大

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题"三个关键概念" | `Write(title)` |
| 0.6s | 卡片1: 仰角/俯角 | `FadeIn(card1, shift=UP)` |
| 1.2s | 卡片2: 坡度=tan α | `FadeIn(card2, shift=UP)` |
| 1.8s | 卡片3: 构造直角三角形 | `FadeIn(card3, shift=UP)` |
| 2.6s | 作者信息放大 | `author.animate.scale(1.5).move_to(UP)` |
| 3.4s | 关注提示 | `Write("关注我，学更多解题技巧!")` |
| 4.2s | 装饰动画 | `Flash(decorations)` |
| 5.0s | 等待 | `Wait(2.0)` |

### 清理
- 所有元素淡出

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| hook_text | Scene 1 | Scene 1 | 钩子文字 |
| building | Scene 2 | Scene 2 | 建筑物 |
| elevation_triangle | Scene 2 | Scene 2 | 仰角三角形 |
| mountain | Scene 3 | Scene 3 | 山的轮廓 |
| depression_triangle | Scene 3 | Scene 3 | 俯角三角形 |
| comparison_diagrams | Scene 4 | Scene 4 | 对比图 |
| slope | Scene 5 | Scene 5 | 斜坡 |
| slope_triangle | Scene 5 | Scene 5 | 坡度三角形 |
| application_scenes | Scene 6 | Scene 6 | 应用场景 |
| summary_cards | Scene 7 | Scene 7 | 总结卡片 |

---

## 关键技术要点

### 1. 角度计算精确性
- 所有角度使用 `DEGREES` 或弧度制
- 仰角/俯角的 `other_angle` 参数设置
- 使用 `Angle.from_three_points` 确保方向正确

### 2. 边界安全
- 建筑物高度不超过 y=5
- 山的轮廓控制在 y∈[-3, 5]
- 所有文字标注避免重叠

### 3. 动画节奏
- 几何构造: 0.8-1.2s
- 公式书写: 0.6-0.8s
- 理解停顿: 1.5-2.0s（关键步骤）
- 场景切换: 0.4-0.6s

### 4. 视觉层次
- 主要元素: stroke_width=3
- 辅助线: stroke_width=2, dashed
- 标注文字: font_size=20-24
- 公式: font_size=26-28

---

## 验证检查项

- [ ] 所有角度使用精确计算
- [ ] 直角三角形的直角标记正确
- [ ] 仰角和俯角的方向正确（不要混淆）
- [ ] 坡度公式 i = h/d = tan α 准确
- [ ] 所有标注清晰可读
- [ ] 没有元素溢出边界
- [ ] 动画总时长在目标范围内
- [ ] 中文使用 Text()，数学公式使用 MathTex()