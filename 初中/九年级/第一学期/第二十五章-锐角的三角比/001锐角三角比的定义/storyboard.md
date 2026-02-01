# 锐角三角比的定义 - 动画分镜脚本

## 元信息
- 目标时长: 80-95 秒
- 场景数量: 8 个
- 难度等级: 九年级
- 主题: 正弦、余弦、正切的定义及性质

## 颜色配置
```python
COLOR_TRIANGLE = WHITE           # 三角形主色
COLOR_OPPOSITE = "#e74c3c"       # 红色 - 对边
COLOR_ADJACENT = "#3498db"       # 蓝色 - 邻边
COLOR_HYPOTENUSE = "#2ecc71"     # 绿色 - 斜边
COLOR_ANGLE = "#f39c12"          # 橙色 - 锐角
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
COLOR_FORMULA = "#9b59b6"        # 紫色 - 公式
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 直角顶点C | np.array([0, 0, 0]) | self.C |
| 顶点A | C + 斜边长度 * cos(角度) * RIGHT + sin(角度) * UP | self.A |
| 顶点B | C + 邻边长度 * RIGHT | self.B |
| 对边长度 | \|A - B\| | self.opposite |
| 邻边长度 | \|B - C\| | self.adjacent |
| 斜边长度 | \|A - C\| | self.hypotenuse |
| sinA值 | 对边 / 斜边 | self.sin_A |
| cosA值 | 邻边 / 斜边 | self.cos_A |
| tanA值 | 对边 / 邻边 | self.tan_A |

---

## Scene 1: 开场钩子 (4-5秒)
**目的**: 引起兴趣，提出问题

### 元素
1. 作者标识 (y=7)
2. 钩子问题大字 (y=5.5)
3. 直角三角形轮廓 (y=1)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info)` |
| 0.3s | 钩子问题书写 | `Write(hook_question, run_time=1.2)` |
| 1.5s | 直角三角形创建 | `Create(triangle, run_time=1.0)` |
| 2.5s | 角A闪烁强调 | `Flash(angle_A)` |
| 3.0s | 提示文字 | `FadeIn(hint_text)` |
| 4.0s | 等待 | `Wait(0.8)` |

### 坐标计算
```python
# 直角三角形 (C为直角)
angle_A_value = 35 * DEGREES  # 锐角A约35度
self.C = np.array([0, 0, 0])
self.B = self.C + 3.0 * RIGHT  # 邻边长度3
# 对边长度 = 邻边 * tan(35°) ≈ 2.1
self.A = self.C + 3.0 * RIGHT + 2.1 * UP
# 位置偏移
offset = UP * 1.0
```

### 清理
- FadeOut: hook_question, hint_text
- 保留: triangle, author_info

---

## Scene 2: 认识三条边 (10-12秒)
**目的**: 介绍对边、邻边、斜边的概念

### 元素
1. 标题: "认识直角三角形的三条边" (y=5.5)
2. 直角标记 (C点)
3. 角A标记
4. 三条边的标注和高亮

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title)` |
| 0.8s | 直角符号创建 | `Create(right_angle_mark)` |
| 1.3s | 角A标记 | `Create(angle_A_arc)` |
| 2.0s | 高亮斜边 | `line_CA.animate.set_color(COLOR_HYPOTENUSE)` |
| 2.5s | 标注"斜边" | `Write(hyp_label)` |
| 3.5s | 说明文字 | `FadeIn(hyp_explain)` |
| 4.5s | 高亮对边 | `line_AB.animate.set_color(COLOR_OPPOSITE)` |
| 5.0s | 标注"对边" | `Write(opp_label)` |
| 5.5s | Brace标记对边 | `Create(opp_brace)` |
| 6.5s | 高亮邻边 | `line_BC.animate.set_color(COLOR_ADJACENT)` |
| 7.0s | 标注"邻边" | `Write(adj_label)` |
| 7.5s | Brace标记邻边 | `Create(adj_brace)` |
| 8.5s | 等待理解 | `Wait(1.5)` |

### 坐标计算
```python
# 直角标记 (使用RightAngle或手动Polygon)
right_angle_size = 0.3
# 角A的弧 (使用Angle.from_three_points)
angle_arc_radius = 0.5
# Brace位置
opp_brace = Brace(Line(self.A, self.B), direction=RIGHT)
adj_brace = Brace(Line(self.B, self.C), direction=DOWN)
```

### 清理
- FadeOut: title, hyp_explain, braces
- 保留: triangle (with colored edges), angle mark, right angle mark, labels

---

## Scene 3: 正弦 sinA 的定义 (10-12秒)
**目的**: 引入正弦的定义

### 元素
1. 标题: "正弦 sine" (y=5.5)
2. 定义文字 (y=4.5)
3. 公式推导区 (y=1到-2)
4. 数值计算演示 (y=-3)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title)` |
| 0.8s | 定义文字 | `FadeIn(definition)` |
| 1.5s | 公式框架 | `Write(formula_framework)` |
| 2.0s | "sin A =" | `Write(sin_symbol)` |
| 2.5s | 对边高亮闪烁 | `Flash(opposite_side)` |
| 3.0s | 分子: "对边" | `Write(numerator_text)` |
| 3.5s | 分数线 | `Create(fraction_line)` |
| 4.0s | 斜边高亮闪烁 | `Flash(hypotenuse_side)` |
| 4.5s | 分母: "斜边" | `Write(denominator_text)` |
| 5.5s | 箭头指向数值 | `GrowArrow(arrow)` |
| 6.0s | 具体数值公式 | `Write(numerical_formula)` |
| 6.8s | 计算过程 | `TransformMatchingTex` |
| 7.5s | 结果闪烁 | `Flash(result)` |
| 8.5s | 等待 | `Wait(1.5)` |

### 坐标计算
```python
# 公式位置
formula_center = UP * 0.5
# 数值计算区
calc_area = DOWN * 2.5
# 具体数值 (根据三角形)
# sin(35°) ≈ 2.1/3.6 ≈ 0.583
```

### 清理
- FadeOut: title, definition, calculation details
- 保留: main formula (sin A = 对边/斜边)，移到角落作为参考

---

## Scene 4: 余弦 cosA 的定义 (10-12秒)
**目的**: 引入余弦的定义

### 元素
1. 标题: "余弦 cosine" (y=5.5)
2. 定义文字 (y=4.5)
3. 公式推导区 (y=1到-2)
4. 数值计算演示 (y=-3)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title)` |
| 0.8s | 定义文字 | `FadeIn(definition)` |
| 1.5s | "cos A =" | `Write(cos_symbol)` |
| 2.0s | 邻边高亮闪烁 | `Flash(adjacent_side)` |
| 2.5s | 分子: "邻边" | `Write(numerator_text)` |
| 3.0s | 分数线 | `Create(fraction_line)` |
| 3.5s | 斜边高亮闪烁 | `Flash(hypotenuse_side)` |
| 4.0s | 分母: "斜边" | `Write(denominator_text)` |
| 5.0s | 具体数值公式 | `Write(numerical_formula)` |
| 5.8s | 计算过程 | `TransformMatchingTex` |
| 6.5s | 结果闪烁 | `Flash(result)` |
| 7.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, definition, calculation details
- 保留: main formula (cos A = 邻边/斜边)

---

## Scene 5: 正切 tanA 的定义 (10-12秒)
**目的**: 引入正切的定义

### 元素
1. 标题: "正切 tangent" (y=5.5)
2. 定义文字 (y=4.5)
3. 公式推导区 (y=1到-2)
4. 关系式: tan A = sin A / cos A (y=-4)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title)` |
| 0.8s | 定义文字 | `FadeIn(definition)` |
| 1.5s | "tan A =" | `Write(tan_symbol)` |
| 2.0s | 对边高亮 | `Flash(opposite_side)` |
| 2.5s | 分子: "对边" | `Write(numerator_text)` |
| 3.0s | 分数线 | `Create(fraction_line)` |
| 3.5s | 邻边高亮 | `Flash(adjacent_side)` |
| 4.0s | 分母: "邻边" | `Write(denominator_text)` |
| 5.0s | 数值计算 | `Write(numerical_calc)` |
| 6.0s | 关系式标题 | `FadeIn(relation_title)` |
| 6.5s | 推导关系 | `Write(tan_sin_cos_relation)` |
| 7.5s | 验证闪烁 | `Flash(relation)` |
| 8.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, definition, relation
- 保留: three formulas (sin, cos, tan) 缩小并排列

---

## Scene 6: 三角比的不变性 (12-15秒)
**目的**: 证明三角比只与角度有关，与三角形大小无关

### 元素
1. 标题: "三角比只与角度有关!" (y=6)
2. 原三角形 (缩小)
3. 相似三角形 (放大版)
4. 对比表格

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title)` |
| 1.0s | 原三角形移到左侧并缩小 | `triangle.animate.scale(0.6).shift(LEFT*2)` |
| 2.0s | 复制三角形 | `triangle_copy = triangle.copy()` |
| 2.5s | 放大到右侧 | `triangle_copy.animate.scale(2).shift(RIGHT*2)` |
| 3.5s | 标注"角A相同" | `FadeIn(same_angle_text)` |
| 4.5s | 表格标题 | `Write(table_header)` |
| 5.0s | 小三角形数据 | `Write(small_data)` |
| 6.0s | 大三角形数据 | `Write(large_data)` |
| 7.0s | sin值对比 | `Write(sin_comparison)` |
| 7.5s | 相等符号闪烁 | `Flash(equals_sign)` |
| 8.0s | cos值对比 | `Write(cos_comparison)` |
| 8.5s | tan值对比 | `Write(tan_comparison)` |
| 9.5s | 结论高亮 | `FadeIn(conclusion, scale=1.2)` |
| 11.0s | 等待 | `Wait(1.5)` |

### 坐标计算
```python
# 原三角形缩放因子
scale_small = 0.5
pos_small = LEFT * 2.5 + UP * 1.5

# 大三角形缩放因子
scale_large = 1.5
pos_large = RIGHT * 2.0 + UP * 1.5

# 验证：角度相同，比值相同
# sin(35°) = 0.583 (两个三角形都是)
```

### 清理
- FadeOut: title, triangles, table, conclusion
- 回到单个标准三角形

---

## Scene 7: 公式总结 (8-10秒)
**目的**: 汇总三个公式，加深记忆

### 元素
1. 标题: "三角比公式总结" (y=6.5)
2. 三个公式卡片
3. 记忆口诀

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title)` |
| 1.0s | 卡片1: sin A | `card_1.animate.shift(RIGHT*0)` |
| 1.5s | 卡片2: cos A | `card_2.animate.shift(RIGHT*0)` |
| 2.0s | 卡片3: tan A | `card_3.animate.shift(RIGHT*0)` |
| 3.0s | 口诀淡入 | `FadeIn(mnemonic)` |
| 4.0s | 三角形示意图 | `FadeIn(triangle_diagram)` |
| 5.0s | 边的标注闪烁 | `Flash(all_sides)` |
| 6.5s | 等待 | `Wait(1.5)` |

### 坐标计算
```python
# 卡片排列
cards = VGroup().arrange(DOWN, buff=0.8).move_to(UP * 1.5)
# 口诀位置
mnemonic_pos = DOWN * 3
# 示意图
diagram_pos = UP * 1.5 + RIGHT * 3
```

### 清理
- 准备进入片尾

---

## Scene 8: 片尾关注 (8-10秒)
**目的**: 品牌曝光，引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息放大 | `Transform(author_info, large_author)` |
| 1.0s | ID淡入 | `FadeIn(author_id)` |
| 2.0s | 关注文字 | `FadeIn(follow_text, shift=UP*0.3)` |
| 3.0s | 装饰三角形 | `FadeIn(decorative_triangles)` |
| 4.0s | 旋转动画 | `Rotate(triangles, angle=PI)` |
| 5.5s | 公式图标 | `FadeIn(formula_icons)` |
| 6.5s | 等待 | `Wait(1.0)` |
| 7.5s | 全部淡出 | `FadeOut(all_elements)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 贯穿全程 |
| main_triangle | Scene 1 | Scene 7 | 主三角形 |
| right_angle_mark | Scene 2 | Scene 6 | 直角标记 |
| angle_A_arc | Scene 2 | Scene 6 | 角A标记 |
| edge_labels | Scene 2 | Scene 6 | 边的标注 |
| sin_formula | Scene 3 | Scene 7 | 正弦公式 |
| cos_formula | Scene 4 | Scene 7 | 余弦公式 |
| tan_formula | Scene 5 | Scene 7 | 正切公式 |

---

## 技术注意事项

### 几何精度要求
```python
# 必须使用精确计算
def setup_geometry(self):
    # 基准参数
    self.angle_A = 35 * DEGREES  # 锐角A
    self.adjacent = 3.0          # 邻边CB
    
    # 精确计算对边
    self.opposite = self.adjacent * np.tan(self.angle_A)
    
    # 精确计算斜边
    self.hypotenuse = self.adjacent / np.cos(self.angle_A)
    
    # 验证勾股定理
    check = np.sqrt(self.opposite**2 + self.adjacent**2)
    assert abs(check - self.hypotenuse) < 1e-6, "勾股定理验证失败"
```

### 角度标记规范
```python
# 使用Angle.from_three_points确保正确方向
angle_A = Angle.from_three_points(
    self.B,  # 第一条射线上的点
    self.A,  # 顶点
    self.C,  # 第二条射线上的点
    radius=0.5,
    color=COLOR_ANGLE
)

# 直角标记
right_angle = RightAngle(
    Line(self.C, self.B),  # 第一条边
    Line(self.C, self.A),  # 第二条边
    length=0.3,
    color=YELLOW
)
```

### 边界检查
```python
# 确保三角形在安全区域内
MAX_X = 4.0
MAX_Y = 7.0
# 三角形顶点
self.C = ORIGIN
self.B = self.C + min(self.adjacent, MAX_X - 0.5) * RIGHT
# 确保A点不超出边界
```

### 数值显示规范
```python
# 保留3位小数
sin_value = DecimalNumber(
    np.sin(self.angle_A),
    num_decimal_places=3,
    font_size=28
)

# 分数显示
fraction = MathTex(
    r"\frac{" + f"{self.opposite:.1f}" + r"}{" + f"{self.hypotenuse:.1f}" + r"}",
    font_size=32
)
```

---

## 验证清单

### 几何验证
- [ ] 直角是否精确90度
- [ ] 勾股定理是否成立
- [ ] 角A + 角B = 90度
- [ ] 边长比值计算正确

### 动画验证
- [ ] 角度标记方向正确
- [ ] 边的颜色编码一致
- [ ] 公式与图形对应
- [ ] 时长控制在90秒内

### 视觉验证
- [ ] 所有元素在边界内
- [ ] 标签无重叠
- [ ] 字体大小适配
- [ ] 颜色对比度足够