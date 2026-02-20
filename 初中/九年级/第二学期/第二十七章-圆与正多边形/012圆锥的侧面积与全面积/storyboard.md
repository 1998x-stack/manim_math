# 圆锥的侧面积与全面积 - 动画分镜脚本

## 元信息
- 目标时长: 70-80 秒
- 场景数量: 10 个
- 难度等级: 中等（九年级）
- 竖屏格式: 1080×1920 (9:16)

## 颜色配置
```python
COLOR_CONE = "#e74c3c"           # 红色 - 圆锥主体
COLOR_BASE = "#3498db"           # 蓝色 - 底面
COLOR_SECTOR = "#f39c12"         # 橙色 - 展开扇形
COLOR_SLANT = "#9b59b6"          # 紫色 - 母线
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 重点标注
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助元素
COLOR_FORMULA = "#2ecc71"        # 绿色 - 公式
```

## 几何预计算清单

### 主要参数（2D投影视图）
| 元素 | 值/计算公式 | 存储变量 |
|------|------------|---------|
| 圆锥顶点 | (0, 2, 0) | `self.apex` |
| 底面圆心 | (0, -1, 0) | `self.base_center` |
| 底面半径 | 1.5 | `self.radius` |
| 高度 | 3.0 | `self.height` |
| 母线长 | sqrt(h² + r²) | `self.slant_height` |

### 派生点（侧视图）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 底面左端点 | base_center + (-radius, 0, 0) | `self.base_left` |
| 底面右端点 | base_center + (radius, 0, 0) | `self.base_right` |
| 母线长度 | sqrt(3² + 1.5²) ≈ 3.35 | `self.slant_height` |

### 展开扇形参数
| 元素 | 公式 | 值 | 存储变量 |
|------|-----|-----|---------|
| 扇形半径 | 母线长 l | 3.35 | `self.sector_radius` |
| 扇形弧长 | 2πr | 9.42 | `self.sector_arc_length` |
| 扇形圆心角（弧度） | 2πr/l | 2.81 | `self.sector_angle` |
| 扇形圆心角（度） | 360r/l | 161° | `self.sector_angle_deg` |

### 计算值
| 元素 | 公式 | 值 | 存储变量 |
|------|-----|-----|---------|
| 底面积 | πr² | 7.07 | `self.base_area` |
| 侧面积 | πrl | 15.71 | `self.lateral_area` |
| 全面积 | πr(l+r) | 22.78 | `self.total_area` |

---

## Scene 1: 开场钩子 (0-4s)

**目的**: 用生活中的圆锥（冰淇淋甜筒）引入话题

### 元素
1. 作者标识（顶部）
2. 钩子问题（大字）
3. 冰淇淋甜筒图像

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 冰淇淋图创建 | `FadeIn(cone_icon)` | 0.8s |
| 1.9s | 问题文字 | `FadeIn(question)` | 0.5s |
| 2.4s | 等待 | `Wait()` | 1.2s |

### 具体内容
- 钩子文字: "冰淇淋甜筒"
- 问题: "表面积怎么算？"
- 图像: 简化的圆锥形状，填充渐变色

### 清理
- FadeOut: hook_text, question, cone_icon
- 保留: author_info

---

## Scene 2: 圆锥结构介绍 (4-11s)

**目的**: 认识圆锥的各部分

### 元素
1. 圆锥侧视图
2. 顶点标注
3. 底面标注
4. 母线标注
5. 高标注

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题显示 | `FadeIn(title)` | 0.4s |
| 0.4s | 圆锥轮廓绘制 | `Create(cone_outline)` | 1.2s |
| 1.6s | 顶点闪烁 | `Flash(apex_dot)` | 0.3s |
| 1.9s | 顶点标注 | `Write(apex_label)` | 0.3s |
| 2.2s | 底面圆创建 | `Create(base_circle)` | 0.8s |
| 3.0s | 底面标注 | `Write(base_label)` | 0.3s |
| 3.3s | 母线高亮 | `Create(slant_line)` | 0.6s |
| 3.9s | 母线标注 | `Write(slant_label)` | 0.4s |
| 4.3s | 高线创建 | `Create(height_line)` | 0.6s |
| 4.9s | 高标注 | `Write(height_label)` | 0.3s |
| 5.2s | 等待理解 | `Wait()` | 1.5s |

### 几何精确性
```python
# 圆锥侧视图（2D投影）
self.apex = np.array([0, 2, 0])           # 顶点
self.base_center = np.array([0, -1, 0])   # 底面圆心
self.radius = 1.5                          # 底面半径
self.height = 3.0                          # 高

# 母线长度（勾股定理）
self.slant_height = np.sqrt(self.height**2 + self.radius**2)

# 底面端点
self.base_left = self.base_center + self.radius * LEFT
self.base_right = self.base_center + self.radius * RIGHT
```

### 清理
- FadeOut: title, labels（部分）
- 保留: cone_outline, base_circle（淡化）

---

## Scene 3: 母线关键性 (11-16s)

**目的**: 强调母线的重要性

### 元素
1. 母线动画
2. 勾股定理展示
3. 母线长度计算

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 母线高亮 | `slant.animate.set_color(YELLOW)` | 0.5s |
| 0.9s | 直角三角形 | `Create(triangle)` | 0.8s |
| 1.7s | 勾股定理公式 | `Write(pythagorean)` | 1.0s |
| 2.7s | 代入计算 | `Write(calculation)` | 0.8s |
| 3.5s | 结果高亮 | `Indicate(result)` | 0.6s |
| 4.1s | 等待 | `Wait()` | 0.5s |

### 计算展示
```python
# 勾股定理
l² = h² + r²

# 代入
l² = 3² + 1.5² = 9 + 2.25 = 11.25

# 结果
l = √11.25 ≈ 3.35
```

### 清理
- FadeOut: title, triangle, formulas
- 保留: cone_outline（变淡）

---

## Scene 4: 展开动画（关键场景）(16-23s)

**目的**: 展示圆锥展开成扇形的神奇过程

### 元素
1. 圆锥侧视图
2. 展开动画
3. 扇形
4. 箭头指示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 提示文字 | `FadeIn(hint)` | 0.5s |
| 0.9s | 母线旋转提示 | `Indicate(slant_line)` | 0.6s |
| 1.5s | 展开动画 | `Transform(cone, sector)` | 2.0s |
| 3.5s | 扇形标注 | `Write(sector_label)` | 0.5s |
| 4.0s | 关键说明 | `FadeIn(explanation)` | 0.8s |
| 4.8s | 等待理解 | `Wait()` | 1.5s |

### 展开动画技术要点
```python
# 圆锥侧面 → 扇形
# 关键对应关系:
# 1. 母线 l → 扇形半径
# 2. 底面周长 2πr → 扇形弧长

# 扇形圆心角计算
sector_angle = (2 * PI * self.radius) / self.slant_height
```

### 关键说明文字
- "母线 → 扇形半径"
- "底面周长 → 扇形弧长"

### 清理
- FadeOut: title, hint, explanation
- 保留: sector

---

## Scene 5: 扇形参数分析 (23-30s)

**目的**: 分析扇形的参数

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 半径标注 | `Create(radius_line), Write(radius_label)` | 0.8s |
| 1.2s | 弧长标注 | `Create(arc_brace), Write(arc_label)` | 0.8s |
| 2.0s | 对应关系1 | `Write(relation_1)` | 0.8s |
| 2.8s | 对应关系2 | `Write(relation_2)` | 0.8s |
| 3.6s | 等待 | `Wait()` | 1.5s |

### 对应关系
```python
# 扇形半径 = 母线 l
r_sector = l

# 扇形弧长 = 底面周长 2πr
arc_length = 2πr
```

### 清理
- FadeOut: labels, relations
- 保留: sector（缩小移到一侧）

---

## Scene 6: 侧面积公式推导 (30-40s)

**目的**: 从扇形面积推导侧面积

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 扇形面积公式 | `Write(sector_formula)` | 1.0s |
| 1.4s | 代入说明 | `FadeIn(substitution_hint)` | 0.6s |
| 2.0s | 代入过程 | `Write(substitution)` | 1.2s |
| 3.2s | 推导箭头 | `GrowArrow(arrow)` | 0.5s |
| 3.7s | 侧面积公式 | `Write(lateral_formula)` | 1.2s |
| 4.9s | 公式高亮 | `Indicate(lateral_formula)` | 0.8s |
| 5.7s | 等待 | `Wait()` | 2.0s |

### 推导过程
```python
# 扇形面积公式
S = (1/2) × 弧长 × 半径

# 代入圆锥参数
# 弧长 = 2πr (底面周长)
# 半径 = l (母线)

S侧 = (1/2) × 2πr × l

# 化简
S侧 = πrl
```

### 公式边框
- 用 SurroundingRectangle 强调最终公式
- 颜色: COLOR_FORMULA

### 清理
- FadeOut: 推导过程
- 保留: 最终公式（移到顶部变小）

---

## Scene 7: 底面积 (40-45s)

**目的**: 补充底面积公式

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 底面圆显示 | `Create(base_circle)` | 0.8s |
| 1.2s | 半径标注 | `Create(radius_line), Write(radius_label)` | 0.6s |
| 1.8s | 底面积公式 | `Write(base_area_formula)` | 0.8s |
| 2.6s | 公式框 | `Create(formula_box)` | 0.4s |
| 3.0s | 等待 | `Wait()` | 1.0s |

### 公式
```python
S底 = πr²
```

### 清理
- FadeOut: base_circle, labels
- 保留: base_area_formula（移到顶部）

---

## Scene 8: 全面积公式 (45-52s)

**目的**: 组合得到全面积

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 圆锥完整图 | `FadeIn(cone_complete)` | 0.6s |
| 1.0s | 侧面+底面 | `FadeIn(explanation)` | 0.5s |
| 1.5s | 组合公式 | `Write(combination)` | 1.2s |
| 2.7s | 推导箭头 | `GrowArrow(arrow)` | 0.5s |
| 3.2s | 全面积公式 | `Write(total_formula)` | 1.0s |
| 4.2s | 公式高亮 | `Indicate(total_formula)` | 0.8s |
| 5.0s | 等待 | `Wait()` | 1.5s |

### 推导
```python
S全 = S侧 + S底

S全 = πrl + πr²

S全 = πr(l + r)
```

### 清理
- FadeOut: 推导过程
- 保留: 最终公式

---

## Scene 9: 综合示例 (52-65s)

**目的**: 完整计算一个例子

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 题目显示 | `FadeIn(problem)` | 0.8s |
| 1.2s | 圆锥图示 | `Create(cone_diagram)` | 1.0s |
| 2.2s | 标注参数 | `Write(parameters)` | 0.6s |
| 2.8s | 步骤1标题 | `Write(step1_title)` | 0.3s |
| 3.1s | 求母线 | `Write(step1_calc)` | 1.0s |
| 4.1s | 母线结果 | `Write(result1)` | 0.5s |
| 4.6s | 步骤2标题 | `Write(step2_title)` | 0.3s |
| 4.9s | 求侧面积 | `Write(step2_calc)` | 1.0s |
| 5.9s | 侧面积结果 | `Write(result2)` | 0.5s |
| 6.4s | 步骤3标题 | `Write(step3_title)` | 0.3s |
| 6.7s | 求全面积 | `Write(step3_calc)` | 1.0s |
| 7.7s | 全面积结果 | `Write(result3)` | 0.5s |
| 8.2s | 等待 | `Wait()` | 2.0s |

### 题目
```
已知：圆锥底面半径 r = 3，高 h = 4
求：侧面积和全面积
```

### 计算展示
```python
# ① 求母线
l² = h² + r² = 16 + 9 = 25
l = 5

# ② 求侧面积
S侧 = πrl = π × 3 × 5 = 15π ≈ 47.1

# ③ 求全面积
S全 = πr(l + r) = π × 3 × (5 + 3) = 24π ≈ 75.4
```

### 清理
- FadeOut: 所有元素

---

## Scene 10: 结尾关注 (65-75s)

**目的**: 引导关注

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 总结卡片 | `FadeIn(summary_card)` | 0.8s |
| 0.8s | 三个公式显示 | `Write(formulas)` | 1.2s |
| 2.0s | 公式闪烁 | `Flash(formulas)` | 0.6s |
| 2.6s | 作者信息放大 | `author.animate.scale(2)` | 0.6s |
| 3.2s | 关注提示 | `Write(follow_text)` | 0.8s |
| 4.0s | 圆锥装饰 | `Create(cone_icons)` | 0.8s |
| 4.8s | 旋转动画 | `Rotate(cone_icons)` | 1.5s |
| 6.3s | 等待 | `Wait()` | 1.5s |

### 总结卡片
```python
公式总结:
1. 母线: l = √(h² + r²)
2. 侧面积: S侧 = πrl
3. 全面积: S全 = πr(l + r)
```

### 清理
- FadeOut: 全部

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 10 | 全程保留在顶部 |
| cone_outline | Scene 2 | Scene 4 | 圆锥轮廓 |
| sector | Scene 4 | Scene 6 | 展开扇形 |
| lateral_formula | Scene 6 | Scene 10 | 移到顶部保留 |
| base_area_formula | Scene 7 | Scene 8 | 临时公式 |
| total_formula | Scene 8 | Scene 10 | 最终公式 |

---

## 关键注意事项

### 几何验证检查点
1. ✅ 母线长度计算精确（勾股定理）
2. ✅ 扇形圆心角 < 360°
3. ✅ 扇形弧长 = 底面周长
4. ✅ 所有比例关系正确
5. ⚠️ 展开动画：需要特殊处理，使用 Transform

### 3D 显示注意
- 圆锥主要使用2D侧视图，更清晰
- 如需3D，使用简化的 Cone 或手绘轮廓
- 避免过于复杂的3D旋转

### LaTeX 安全性
- ❌ 禁止：MathTex(r"\text{母线}")
- ✅ 正确：Text("母线", font="Noto Sans CJK SC")
- ✅ 平方符号：r"r^2"

### 边界安全
- 主内容区：y ∈ [-3, +5]
- 标题区：y ∈ [+5.5, +7]
- 底部文字：y ∈ [-6, -3]

---

## 动画时长预算

| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1 | 4s | 4s |
| Scene 2 | 7s | 11s |
| Scene 3 | 5s | 16s |
| Scene 4 | 7s | 23s |
| Scene 5 | 7s | 30s |
| Scene 6 | 10s | 40s |
| Scene 7 | 5s | 45s |
| Scene 8 | 7s | 52s |
| Scene 9 | 13s | 65s |
| Scene 10 | 10s | 75s |

**总时长**: 约75秒 ✓（符合短视频标准）

---

## 特殊技术要点

### 圆锥展开动画
这是本动画的核心亮点，需要特别设计：

```python
# 方法1：使用 Transform
cone_shape = self.create_cone_side_view()
sector_shape = self.create_sector()

self.play(
    Transform(cone_shape, sector_shape),
    run_time=2.0,
    rate_func=smooth
)

# 方法2：分步展开
# 1. 母线旋转扫过
# 2. 底面周长展开成弧
# 3. 侧面展平成扇形
```

### 扇形圆心角计算
```python
# 关键：扇形弧长 = 底面周长
# l × θ = 2πr
# θ = 2πr / l

sector_angle_rad = (2 * PI * self.radius) / self.slant_height

# 注意：此角度通常 < π，不需要 other_angle=True
```

### 参数一致性验证
```python
def verify_sector_parameters(self):
    """验证扇形参数与圆锥参数的一致性"""
    # 扇形弧长应等于底面周长
    base_circumference = 2 * PI * self.radius
    sector_arc_length = self.sector_radius * self.sector_angle_rad
    
    assert abs(base_circumference - sector_arc_length) < 1e-6, \
        "扇形弧长与底面周长不匹配！"
```