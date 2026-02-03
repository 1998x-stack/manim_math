# 棱柱 (Prism) - 动画分镜脚本

## 元信息
- 目标时长: 60-75秒
- 场景数量: 7个
- 难度等级: 高三
- 主题: 棱柱的定义、分类、性质和计算公式

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主棱柱
COLOR_SECONDARY = "#e74c3c"    # 红色 - 高亮边
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 强调元素
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线
COLOR_BASE = "#2ecc71"         # 绿色 - 底面
COLOR_LATERAL = "#9b59b6"      # 紫色 - 侧面
```

## 3D 几何预计算清单

### 三棱柱 (Triangular Prism)
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 底面顶点A,B,C | 正三角形 | self.A_bottom, self.B_bottom, self.C_bottom |
| 顶面顶点A',B',C' | 底面平移向上 | self.A_top, self.B_top, self.C_top |
| 侧棱长度 | h = 3.0 | self.height |
| 底面边长 | a = 2.0 | self.base_side |
| 底面积 | S = (√3/4)a² | self.base_area |
| 侧面积 | S_lateral = 3ah | self.lateral_area |
| 体积 | V = S·h | self.volume |

### 直棱柱与斜棱柱对比
| 元素 | 计算方式 |
|------|---------|
| 直棱柱侧棱 | 垂直于底面，方向向量 [0,0,1] |
| 斜棱柱侧棱 | 倾斜方向向量 [0.5,0,1] |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 引入棱柱概念，吸引注意力

### 元素
1. 作者信息（顶部）
2. 钩子问题："什么是棱柱？"
3. 3D三棱柱旋转展示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.0s | 3D棱柱创建 | `Create(prism)` |
| 2.0s | 棱柱旋转展示 | `Rotate(prism, axis=UP)` |
| 3.5s | 等待 | `Wait(0.5)` |

### 几何计算
```python
# 底面正三角形 (边长2.0)
base_side = 2.0
A_bottom = np.array([-1, 0, 0])
B_bottom = np.array([1, 0, 0])
C_bottom = np.array([0, np.sqrt(3), 0])

# 顶面 (向上平移h=3)
height = 3.0
A_top = A_bottom + np.array([0, 0, height])
B_top = B_bottom + np.array([0, 0, height])
C_top = C_bottom + np.array([0, 0, height])
```

### 清理
- FadeOut: hook_text
- 保留: prism, author_info

---

## Scene 2: 棱柱定义 (8秒)
**目的**: 解释棱柱的三要素（两底面、侧面、侧棱）

### 元素
1. 标题："棱柱的定义"
2. 底面高亮（绿色）
3. 侧面高亮（紫色）
4. 侧棱高亮（红色）
5. 文字说明

### 动画序列
| 时间 | 动作 | 描述 |
|------|------|------|
| 0.0s | 标题淡入 | "棱柱的定义" |
| 0.5s | 底面闪烁 | 两个平行全等多边形 |
| 2.0s | 文字说明1 | "两底面：平行且全等" |
| 3.5s | 侧面闪烁 | 平行四边形侧面 |
| 5.0s | 文字说明2 | "侧面：平行四边形" |
| 6.5s | 侧棱闪烁 | 平行且相等的棱 |
| 7.5s | 文字说明3 | "侧棱：平行且相等" |

### 几何验证
```python
# 验证底面平行
assert verify_parallel(normal_bottom, normal_top)

# 验证侧棱平行且相等
edge1 = A_top - A_bottom
edge2 = B_top - B_bottom
edge3 = C_top - C_bottom
assert verify_parallel(edge1, edge2)
assert np.allclose(edge1, edge2)
```

### 清理
- FadeOut: 标题, 所有文字说明
- 保留: prism

---

## Scene 3: 棱柱分类 - 按底面 (10秒)
**目的**: 展示三棱柱、四棱柱、五棱柱的区别

### 元素
1. 标题："按底面形状分类"
2. 三棱柱（已有）
3. 四棱柱（正方形底）
4. 五棱柱（正五边形底）
5. 标签 n=3, n=4, n=5

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 标题淡入 |
| 0.5s | 三棱柱移至左侧 |
| 1.5s | 四棱柱创建于中间 |
| 2.5s | 五棱柱创建于右侧 |
| 3.5s | 标签淡入 "三棱柱" "四棱柱" "五棱柱" |
| 5.0s | 公式淡入 "n棱柱：底面为n边形" |
| 7.5s | 等待 |

### 几何计算
```python
# 四棱柱底面（正方形）
square_vertices = [
    np.array([-0.8, -0.8, 0]),
    np.array([0.8, -0.8, 0]),
    np.array([0.8, 0.8, 0]),
    np.array([-0.8, 0.8, 0])
]

# 五棱柱底面（正五边形）
n = 5
pentagon_vertices = [
    np.array([np.cos(2*PI*i/n), np.sin(2*PI*i/n), 0])
    for i in range(n)
]
```

### 清理
- FadeOut: 标题, 四棱柱, 五棱柱, 标签, 公式
- 保留: 三棱柱（移回中心）

---

## Scene 4: 棱柱分类 - 直棱柱vs斜棱柱 (10秒)
**目的**: 对比直棱柱和斜棱柱的区别

### 元素
1. 标题："直棱柱 vs 斜棱柱"
2. 直棱柱（左侧）
3. 斜棱柱（右侧）
4. 垂直符号（直棱柱）
5. 倾斜角度标注（斜棱柱）

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 标题淡入 |
| 0.5s | 直棱柱移至左侧 |
| 1.5s | 斜棱柱创建于右侧 |
| 2.5s | 直棱柱添加垂直符号 |
| 3.5s | 文字："侧棱⊥底面" |
| 5.0s | 斜棱柱添加角度标注 |
| 6.0s | 文字："侧棱与底面成角" |
| 8.5s | 等待 |

### 几何计算
```python
# 直棱柱：侧棱垂直向上
lateral_edge_straight = np.array([0, 0, height])

# 斜棱柱：侧棱倾斜
tilt_angle = PI / 6  # 30度倾斜
lateral_edge_oblique = np.array([
    height * np.tan(tilt_angle),
    0,
    height
])

# 验证垂直
assert verify_perpendicular(
    lateral_edge_straight, 
    np.array([1, 0, 0])  # 底面内任意向量
)
```

### 清理
- FadeOut: 标题, 斜棱柱, 所有标注
- 保留: 直棱柱（移回中心，变回三棱柱）

---

## Scene 5: 正棱柱 (8秒)
**目的**: 介绍正棱柱的定义和特征

### 元素
1. 标题："正棱柱"
2. 正三棱柱（等边三角形底）
3. 底面中心标注
4. 外接圆展示
5. 定义文字

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 标题淡入 "正棱柱" |
| 0.5s | 底面高亮 |
| 1.5s | 底面外接圆创建 |
| 2.5s | 文字："底面是正多边形" |
| 4.0s | 侧棱高亮 |
| 5.0s | 文字："侧棱垂直于底面" |
| 6.5s | 完整定义："正n棱柱 = 直棱柱 + 正n边形底" |
| 8.0s | 等待 |

### 几何验证
```python
# 验证底面是等边三角形
AB = np.linalg.norm(B_bottom - A_bottom)
BC = np.linalg.norm(C_bottom - B_bottom)
CA = np.linalg.norm(A_bottom - C_bottom)
assert np.allclose([AB, BC, CA], [AB, AB, AB])

# 验证侧棱垂直底面
normal = np.cross(B_bottom - A_bottom, C_bottom - A_bottom)
lateral = A_top - A_bottom
assert verify_perpendicular(normal, lateral)
```

### 清理
- FadeOut: 标题, 外接圆, 所有文字
- 保留: 正三棱柱

---

## Scene 6: 体积和表面积公式 (12秒)
**目的**: 推导和展示体积、表面积计算公式

### 元素
1. 标题："体积和表面积"
2. 底面积标注 S₀
3. 高度标注 h
4. 体积公式 V = S₀ · h
5. 侧面积展示（侧面展开）
6. 表面积公式 S = 2S₀ + S侧

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 标题淡入 |
| 0.5s | 底面高亮，标注S₀ |
| 1.5s | 高度标注h（虚线） |
| 2.5s | 体积公式淡入：V = S₀ · h |
| 4.0s | 数值代入示例 |
| 5.5s | 侧面展开动画 |
| 7.0s | 侧面积公式：S侧 = 周长 · h |
| 9.0s | 表面积公式：S = 2S₀ + S侧 |
| 11.0s | 等待 |

### 几何计算
```python
# 底面积（等边三角形）
base_side = 2.0
base_area = (np.sqrt(3) / 4) * base_side**2

# 高度
height = 3.0

# 体积
volume = base_area * height

# 周长
perimeter = 3 * base_side

# 侧面积
lateral_area = perimeter * height

# 表面积
surface_area = 2 * base_area + lateral_area

# 验证计算
print(f"底面积: {base_area:.3f}")
print(f"体积: {volume:.3f}")
print(f"侧面积: {lateral_area:.3f}")
print(f"表面积: {surface_area:.3f}")
```

### 清理
- FadeOut: 标题, 所有公式, 标注
- 保留: 棱柱

---

## Scene 7: 总结与片尾 (10秒)
**目的**: 总结要点，引导关注

### 元素
1. 棱柱缩小至左上角
2. 要点卡片（右侧）
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 棱柱缩小移至左上 |
| 1.0s | 要点卡片1："两底面平行全等" |
| 2.0s | 要点卡片2："侧棱平行相等" |
| 3.0s | 要点卡片3："V = S底 · h" |
| 4.0s | 要点卡片4："S = 2S底 + S侧" |
| 6.0s | 作者信息放大 |
| 7.0s | 关注提示："关注获取更多立体几何技巧!" |
| 9.0s | 装饰动画（旋转图标） |

### 清理
- 无（片尾场景）

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 顶部作者信息 |
| main_prism | Scene 1 | Scene 7 | 主三棱柱 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| definition_texts | Scene 2 | Scene 2 | 定义说明 |
| quad_prism | Scene 3 | Scene 3 | 四棱柱 |
| penta_prism | Scene 3 | Scene 3 | 五棱柱 |
| oblique_prism | Scene 4 | Scene 4 | 斜棱柱 |
| formulas | Scene 6 | Scene 6 | 公式组 |
| summary_cards | Scene 7 | - | 总结卡片 |

---

## 3D相机设置
```python
# 初始相机角度
phi = 70 * DEGREES      # 俯视角
theta = -45 * DEGREES   # 水平旋转角

# Scene 1: 旋转展示
self.move_camera(phi=60*DEGREES, theta=-30*DEGREES, run_time=2)

# Scene 2-6: 稳定视角
phi = 70 * DEGREES
theta = -45 * DEGREES

# Scene 7: 正面视角
self.move_camera(phi=0*DEGREES, theta=0*DEGREES, run_time=1.5)
```

---

## 验证检查清单
- [ ] 所有顶点通过精确计算
- [ ] 底面平行性验证
- [ ] 侧棱平行性验证
- [ ] 侧棱长度一致性验证
- [ ] 体积公式数值验证
- [ ] 表面积公式数值验证
- [ ] 3D坐标系正确性
- [ ] 相机角度适宜性

---

## 时间控制
- **总时长**: 60-75秒
- **关键停顿**: Scene 2 (+2s), Scene 6 (+2s)
- **过渡时间**: 每个场景间0.5秒

---

## 特殊注意事项
1. **3D渲染**: 使用ThreeDScene而非Scene
2. **相机控制**: 适时调整phi和theta角度
3. **透视效果**: 注意前后元素的遮挡关系
4. **标注位置**: 3D空间中的2D文字要固定在相机平面
5. **颜色对比**: 确保3D物体在深色背景下清晰可见
