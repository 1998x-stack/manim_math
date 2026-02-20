# 弧长与扇形面积 - 动画分镜脚本

## 元信息
- 目标时长: 60-70 秒
- 场景数量: 9 个
- 难度等级: 中等（九年级）
- 竖屏格式: 1080×1920 (9:16)

## 颜色配置
```python
COLOR_PRIMARY = "#e74c3c"        # 红色 - 扇形/弧
COLOR_SECONDARY = "#3498db"      # 蓝色 - 辅助线
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 重点标注
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助元素
COLOR_CIRCLE = WHITE             # 白色 - 圆
COLOR_FORMULA = "#2ecc71"        # 绿色 - 公式
```

## 几何预计算清单

### 主要参数
| 元素 | 值/计算公式 | 存储变量 |
|------|------------|---------|
| 圆心 | (0, 1.5, 0) | `self.center` |
| 半径 | 2.0 | `self.radius` |
| 圆心角（度） | 60° | `self.angle_deg` |
| 圆心角（弧度） | π/3 | `self.angle_rad` |

### 派生点
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 弧起点 | center + radius*(cos(0), sin(0), 0) | `self.arc_start` |
| 弧终点 | center + radius*(cos(π/3), sin(π/3), 0) | `self.arc_end` |
| 弧中点 | center + radius*(cos(π/6), sin(π/6), 0) | `self.arc_mid` |

### 计算值
| 元素 | 公式 | 值 | 存储变量 |
|------|-----|-----|---------|
| 弧长 | l = (60×π×2)/180 | 2.094 | `self.arc_length` |
| 扇形面积(公式1) | S = (60×π×4)/360 | 2.094 | `self.sector_area_1` |
| 扇形面积(公式2) | S = (2.094×2)/2 | 2.094 | `self.sector_area_2` |

---

## Scene 1: 开场钩子 (0-4s)

**目的**: 用披萨切片引入话题，抓住注意力

### 元素
1. 作者标识（顶部）
2. 钩子问题（大字）
3. 披萨图形（圆形扇形）

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 披萨图创建 | `Create(pizza_sector)` | 1.0s |
| 2.1s | 问题文字淡入 | `FadeIn(question)` | 0.5s |
| 2.6s | 等待 | `Wait()` | 1.0s |

### 具体内容
- 钩子文字: "切一块披萨"
- 问题: "边缘有多长？面积是多少？"
- 披萨扇形: 60°, 红色填充

### 清理
- FadeOut: hook_text, question, pizza_sector
- 保留: author_info

---

## Scene 2: 圆心角介绍 (4-10s)

**目的**: 建立圆心角的概念

### 元素
1. 完整的圆
2. 两条半径
3. 圆心角标记
4. 角度标签

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` | 0.4s |
| 0.4s | 圆创建 | `Create(circle)` | 1.0s |
| 1.4s | 圆心点闪现 | `Flash(center_dot)` | 0.3s |
| 1.7s | 两条半径生长 | `GrowFromCenter(radius_1, radius_2)` | 0.8s |
| 2.5s | 角弧创建 | `Create(angle_arc)` | 0.6s |
| 3.1s | 角度标签书写 | `Write(angle_label)` | 0.5s |
| 3.6s | 说明文字 | `FadeIn(definition)` | 0.5s |
| 4.1s | 等待理解 | `Wait()` | 1.5s |

### 几何精确性
```python
# 圆心
self.center = np.array([0, 1.5, 0])

# 半径1（水平向右）
self.radius_1_end = self.center + self.radius * RIGHT

# 半径2（60度方向）
angle_rad = np.radians(60)
self.radius_2_end = self.center + self.radius * np.array([
    np.cos(angle_rad), 
    np.sin(angle_rad), 
    0
])

# 角弧 - 使用 Angle.from_three_points
# 注意：验证角度方向，确保 other_angle 参数正确
```

### 清理
- FadeOut: title, definition
- 保留: circle, radius_1, radius_2, angle_arc, angle_label, center_dot

---

## Scene 3: 弧长公式推导 (10-20s)

**目的**: 从周长公式推导弧长公式

### 元素
1. 圆周长公式
2. 比例关系
3. 弧长公式

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题显示 | `FadeIn(title)` | 0.4s |
| 0.4s | 圆周长公式 | `Write(formula_circumference)` | 1.0s |
| 1.4s | 等待 | `Wait()` | 0.8s |
| 2.2s | 比例说明 | `FadeIn(proportion_text)` | 0.6s |
| 2.8s | 比例公式 | `Write(proportion_formula)` | 1.2s |
| 4.0s | 等待 | `Wait()` | 1.0s |
| 5.0s | 推导箭头 | `GrowArrow(arrow)` | 0.5s |
| 5.5s | 弧长公式 | `Write(arc_length_formula)` | 1.2s |
| 6.7s | 公式高亮 | `Indicate(arc_length_formula)` | 0.8s |
| 7.5s | 等待理解 | `Wait()` | 2.0s |

### 公式内容
```python
# 1. 圆周长
formula_1 = MathTex(r"C = 2\pi r")

# 2. 比例关系
proportion = MathTex(
    r"\frac{l}{C}", r"=", r"\frac{n^\circ}{360^\circ}"
)

# 3. 弧长公式
formula_2 = MathTex(
    r"l", r"=", r"\frac{n\pi r}{180}"
)
```

### 视觉辅助
- 在圆上高亮显示完整周长（蓝色虚线）
- 高亮显示弧长部分（红色实线）
- 用 Brace 标注角度和周长的对应关系

### 清理
- FadeOut: formula_circumference, proportion_text, proportion_formula, arrow
- 保留: arc_length_formula（移到顶部变小）
- 清理: circle保留，其他圆相关元素淡出

---

## Scene 4: 弧长示例计算 (20-28s)

**目的**: 用具体数值演示弧长计算

### 元素
1. 新的扇形图（带标注）
2. 已知条件
3. 计算过程
4. 结果

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 扇形绘制 | `Create(sector)` | 1.0s |
| 1.4s | 标注半径 | `Write(radius_label)` | 0.5s |
| 1.9s | 标注角度 | `Write(angle_label)` | 0.5s |
| 2.4s | 公式带入 | `Write(substitution)` | 1.0s |
| 3.4s | 计算过程 | `TransformMatchingTex(step1, step2)` | 0.8s |
| 4.2s | 结果高亮 | `Indicate(result)` | 0.6s |
| 4.8s | 弧长标注 | `Create(arc_brace), Write(arc_length)` | 0.8s |
| 5.6s | 等待 | `Wait()` | 1.5s |

### 计算展示
```python
# 已知
r = 2, n = 60°

# 代入公式
l = (60 × π × 2) / 180

# 计算
l = 120π / 180 = 2π/3

# 数值结果
l ≈ 2.09 (单位)
```

### 清理
- FadeOut: title, substitution, calculation
- 保留: sector, labels（变小移到一边）

---

## Scene 5: 扇形定义 (28-34s)

**目的**: 明确扇形的组成

### 元素
1. 扇形图形
2. 组成部分标注
3. 定义文字

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 扇形出现 | `FadeIn(sector)` | 0.6s |
| 1.0s | 半径1高亮 | `sector[0].animate.set_color(YELLOW)` | 0.5s |
| 1.5s | 标注"半径" | `Write(label_r1)` | 0.3s |
| 1.8s | 半径1恢复 | `sector[0].animate.set_color(PRIMARY)` | 0.3s |
| 2.1s | 半径2高亮 | `sector[1].animate.set_color(YELLOW)` | 0.5s |
| 2.6s | 标注"半径" | `Write(label_r2)` | 0.3s |
| 2.9s | 半径2恢复 | `sector[1].animate.set_color(PRIMARY)` | 0.3s |
| 3.2s | 弧高亮 | `sector[2].animate.set_color(YELLOW)` | 0.5s |
| 3.7s | 标注"弧" | `Write(label_arc)` | 0.3s |
| 4.0s | 定义文字 | `FadeIn(definition)` | 0.6s |
| 4.6s | 等待 | `Wait()` | 1.0s |

### 定义文字
"扇形 = 两条半径 + 一段弧"

### 清理
- FadeOut: title, definition, labels
- 保留: sector

---

## Scene 6: 扇形面积公式1推导 (34-44s)

**目的**: 从圆面积推导扇形面积公式

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 圆面积公式 | `Write(formula_circle)` | 1.0s |
| 1.4s | 等待 | `Wait()` | 0.8s |
| 2.2s | 比例关系 | `FadeIn(proportion_text)` | 0.6s |
| 2.8s | 比例公式 | `Write(proportion_formula)` | 1.2s |
| 4.0s | 等待 | `Wait()` | 1.0s |
| 5.0s | 推导箭头 | `GrowArrow(arrow)` | 0.5s |
| 5.5s | 扇形面积公式 | `Write(sector_area_formula)` | 1.2s |
| 6.7s | 公式高亮 | `Indicate(sector_area_formula)` | 0.8s |
| 7.5s | 等待 | `Wait()` | 2.0s |

### 公式内容
```python
# 圆面积
S_circle = MathTex(r"S_{\text{circle}} = \pi r^2")

# 比例
proportion = MathTex(
    r"\frac{S_{\text{sector}}}{S_{\text{circle}}}", 
    r"=", 
    r"\frac{n^\circ}{360^\circ}"
)

# 扇形面积
S_sector = MathTex(
    r"S", r"=", r"\frac{n\pi r^2}{360}"
)
```

### 清理
- FadeOut: 所有推导过程
- 保留: sector_area_formula（移到顶部）

---

## Scene 7: 扇形面积公式2 (44-52s)

**目的**: 展示弧长关系式

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 说明文字 | `FadeIn(explanation)` | 0.6s |
| 1.0s | 公式1显示 | `Write(formula_1)` | 0.8s |
| 1.8s | 替换提示 | `FadeIn(hint)` | 0.5s |
| 2.3s | 弧长公式 | `Write(arc_formula)` | 0.8s |
| 3.1s | 代入过程 | `TransformMatchingTex()` | 1.0s |
| 4.1s | 公式2显示 | `Write(formula_2)` | 1.0s |
| 5.1s | 公式高亮 | `Indicate(formula_2)` | 0.8s |
| 5.9s | 等待 | `Wait()` | 1.5s |

### 公式推导
```python
# 公式1
S = nπr² / 360

# 因为 l = nπr / 180
# 所以 nπr = 180l

# 代入
S = (180l × r) / 360 = lr / 2

# 公式2
S = (1/2) × l × r
```

### 视觉提示
- 用颜色区分 l 和 r
- 在扇形图上标注这两个量

### 清理
- FadeOut: 所有公式（除了最终公式）
- 保留两个公式框并排显示

---

## Scene 8: 综合示例 (52-62s)

**目的**: 完整计算一个例子

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 题目显示 | `FadeIn(problem)` | 0.8s |
| 1.2s | 扇形绘制 | `Create(sector)` | 1.0s |
| 2.2s | 求弧长 | `Write(step1)` | 0.8s |
| 3.0s | 弧长结果 | `Write(result1)` | 0.6s |
| 3.6s | 求面积 | `Write(step2)` | 0.8s |
| 4.4s | 面积结果 | `Write(result2)` | 0.6s |
| 5.0s | 验证公式2 | `Write(verification)` | 1.0s |
| 6.0s | 结果一致 | `Indicate(checkmark)` | 0.6s |
| 6.6s | 等待 | `Wait()` | 2.0s |

### 题目
已知：r = 3，n = 120°
求：弧长 l 和扇形面积 S

### 计算展示
```python
# 弧长
l = (120 × π × 3) / 180 = 2π

# 面积（公式1）
S = (120 × π × 9) / 360 = 3π

# 验证（公式2）
S = (2π × 3) / 2 = 3π ✓
```

### 清理
- FadeOut: 所有元素

---

## Scene 9: 结尾关注 (62-68s)

**目的**: 引导关注

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 总结卡片 | `FadeIn(summary_card)` | 0.8s |
| 0.8s | 公式闪烁 | `Flash(formulas)` | 0.6s |
| 1.4s | 作者信息放大 | `author.animate.scale(2)` | 0.6s |
| 2.0s | 关注提示 | `Write(follow_text)` | 0.8s |
| 2.8s | 圆形装饰 | `Create(circles)` | 0.8s |
| 3.6s | 等待 | `Wait()` | 1.5s |

### 总结卡片内容
- 弧长公式: l = nπr/180
- 面积公式1: S = nπr²/360
- 面积公式2: S = lr/2

### 清理
- FadeOut: 全部

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 9 | 全程保留在顶部 |
| circle | Scene 2 | Scene 3 | 基础圆 |
| sector | Scene 4, 5, 6, 8 | 各自场景结束 | 多次创建 |
| arc_length_formula | Scene 3 | Scene 4 | 移到顶部保留 |
| sector_area_formula | Scene 6 | Scene 8 | 移到顶部保留 |

---

## 关键注意事项

### 几何验证检查点
1. ✅ 圆心角度数 < 180°
2. ✅ 弧长计算精确
3. ✅ 扇形顶点在圆心
4. ✅ 半径长度一致
5. ✅ 角弧方向正确（other_angle参数）

### LaTeX 安全性
- ❌ 禁止：MathTex(r"\text{扇形}")
- ✅ 正确：Text("扇形", font="Noto Sans CJK SC")
- ✅ 度数符号：r"60^\circ"

### 边界安全
- 主内容区：y ∈ [-3, +5]
- 标题区：y ∈ [+5.5, +7]
- 底部文字：y ∈ [-6, -3]

---

## 动画时长预算

| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1 | 4s | 4s |
| Scene 2 | 6s | 10s |
| Scene 3 | 10s | 20s |
| Scene 4 | 8s | 28s |
| Scene 5 | 6s | 34s |
| Scene 6 | 10s | 44s |
| Scene 7 | 8s | 52s |
| Scene 8 | 10s | 62s |
| Scene 9 | 6s | 68s |

**总时长**: 约68秒 ✓（符合TikTok短视频标准）