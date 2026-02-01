# 特殊角的三角比值 - 动画分镜脚本

## 元信息
- 目标时长: 60-75秒
- 场景数量: 8个
- 难度等级: 中等
- 目标年级: 九年级

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主三角形
COLOR_30 = "#e74c3c"             # 红色 - 30°特殊角
COLOR_45 = "#2ecc71"             # 绿色 - 45°特殊角
COLOR_60 = "#f39c12"             # 橙色 - 60°特殊角
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_TABLE = WHITE              # 白色 - 表格
```

## 几何预计算清单

### 30°角 - 等边三角形的一半
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 等边三角形边长 | 2.0 * SCALE | self.side_30 |
| 顶点A (左下) | np.array([-1, 0, 0]) * SCALE | self.A_30 |
| 顶点B (右下) | np.array([1, 0, 0]) * SCALE | self.B_30 |
| 顶点C (顶部) | np.array([0, √3, 0]) * SCALE | self.C_30 |
| 中点D (AB中点) | (A_30 + B_30) / 2 | self.D_30 |
| 高CD长度 | √3 * SCALE | self.height_30 |
| 对边 (CD) | √3 | - |
| 斜边 (AC) | 2 | - |
| 邻边 (AD) | 1 | - |

### 45°角 - 等腰直角三角形
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 直角边长度 | √2 * SCALE | self.leg_45 |
| 顶点P (直角) | np.array([0, 0, 0]) | self.P_45 |
| 顶点Q (水平) | np.array([√2, 0, 0]) * SCALE | self.Q_45 |
| 顶点R (竖直) | np.array([0, √2, 0]) * SCALE | self.R_45 |
| 对边 (PR) | √2 | - |
| 斜边 (QR) | 2 | - |
| 邻边 (PQ) | √2 | - |

### 60°角 - 等边三角形的另一半
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 使用30°的数据 | 共用等边三角形 | - |
| 60°角顶点 | A_30 (左下角) | - |
| 对边 (CD) | √3 | - |
| 邻边 (AD) | 1 | - |
| 斜边 (AC) | 2 | - |

### 通用参数
```python
SCALE = 1.2
OFFSET = UP * 1.5
FONT_SIZE_FORMULA = 28
FONT_SIZE_LABEL = 20
```

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，提出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题: "30°、45°、60°的三角比值, 你能记住吗?"
3. 三个角度符号快闪

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时长 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 三个角度符号闪烁 | `FadeIn(angle_30, scale=0.5)` 等 | 0.6s |
| 1.7s | 等待 | `Wait(1.0)` | 1.0s |
| 2.7s | 淡出钩子 | `FadeOut(hook_text, angles)` | 0.5s |

### 清理
- FadeOut: hook_text, angle_symbols
- 保留: author_info

---

## Scene 2: 30°角构造 (8-10秒)
**目的**: 通过等边三角形推导30°角的三角比

### 元素
1. 等边三角形ABC (边长=2)
2. 高线CD (从C到AB)
3. 直角标记
4. 边长标注: AC=2, AD=1, CD=√3
5. 角度标注: ∠CAD=30°

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时长 |
|------|------|---------|---------|
| 0.0s | 标题淡入 | `FadeIn(title_30)` | 0.4s |
| 0.4s | 绘制等边三角形 | `Create(triangle_30)` | 1.0s |
| 1.4s | 标注顶点ABC | `Write(labels_ABC)` | 0.5s |
| 1.9s | 绘制高线CD | `Create(altitude_CD), FadeIn(point_D)` | 0.8s |
| 2.7s | 添加直角符号 | `FadeIn(right_angle)` | 0.3s |
| 3.0s | 标注边长 | `Write(label_AC), Write(label_AD), Write(label_CD)` | 1.0s |
| 4.0s | 高亮30°角 | `Create(angle_30_arc), Write(angle_label)` | 0.8s |
| 4.8s | 说明文字 | `FadeIn(explanation)` | 0.5s |
| 5.3s | 等待理解 | `Wait(2.0)` | 2.0s |

### 几何验证
- [x] AD = AB/2 = 1 (等边三角形高线平分底边)
- [x] CD = √3 (勾股定理: AC² = AD² + CD²)
- [x] ∠CAD = 30° (等边三角形每个角60°，高线平分)
- [x] 直角标记位置正确 (∠ADC = 90°)

### 清理
- 保留三角形用于下一场景

---

## Scene 3: 30°角三角比计算 (6-8秒)
**目的**: 展示sin30°, cos30°, tan30°的计算过程

### 元素
1. 保留的30°直角三角形
2. 三角比公式:
   - sin30° = 对边/斜边 = CD/AC = √3/2
   - cos30° = 邻边/斜边 = AD/AC = 1/2
   - tan30° = 对边/邻边 = CD/AD = √3/1 = √3/3

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时长 |
|------|------|---------|---------|
| 0.0s | sin公式出现 | `Write(sin_formula)` | 0.8s |
| 0.8s | 高亮对边和斜边 | `Indicate(CD), Indicate(AC)` | 0.6s |
| 1.4s | 显示计算结果 | `TransformMatchingTex(sin_formula, sin_result)` | 0.8s |
| 2.2s | cos公式出现 | `Write(cos_formula)` | 0.8s |
| 3.0s | 高亮邻边和斜边 | `Indicate(AD), Indicate(AC)` | 0.6s |
| 3.6s | 显示计算结果 | `TransformMatchingTex(cos_formula, cos_result)` | 0.8s |
| 4.4s | tan公式出现 | `Write(tan_formula)` | 0.8s |
| 5.2s | 显示计算结果 | `TransformMatchingTex(tan_formula, tan_result)` | 0.8s |
| 6.0s | 等待 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: triangle_30, formulas
- 保留: author_info

---

## Scene 4: 45°角构造 (7-9秒)
**目的**: 通过等腰直角三角形推导45°角的三角比

### 元素
1. 等腰直角三角形PQR (直角边=√2)
2. 直角标记 (在P点)
3. 边长标注: PQ=√2, PR=√2, QR=2
4. 角度标注: ∠PQR=45°

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时长 |
|------|------|---------|---------|
| 0.0s | 标题淡入 | `FadeIn(title_45)` | 0.4s |
| 0.4s | 绘制等腰直角三角形 | `Create(triangle_45)` | 1.0s |
| 1.4s | 标注顶点PQR | `Write(labels_PQR)` | 0.5s |
| 1.9s | 添加直角符号 | `FadeIn(right_angle_P)` | 0.3s |
| 2.2s | 标注边长 | `Write(label_PQ), Write(label_PR), Write(label_QR)` | 1.0s |
| 3.2s | 高亮45°角 | `Create(angle_45_arc), Write(angle_label)` | 0.8s |
| 4.0s | 说明文字 | `FadeIn(explanation_45)` | 0.5s |
| 4.5s | 等待理解 | `Wait(2.0)` | 2.0s |

### 几何验证
- [x] PQ = PR = √2 (等腰直角三角形)
- [x] QR = 2 (勾股定理: QR² = PQ² + PR²)
- [x] ∠PQR = ∠PRQ = 45° (等腰直角三角形)
- [x] ∠QPR = 90°

### 清理
- 保留三角形用于下一场景

---

## Scene 5: 45°角三角比计算 (6-8秒)
**目的**: 展示sin45°, cos45°, tan45°的计算过程

### 元素
1. 保留的45°直角三角形
2. 三角比公式:
   - sin45° = PR/QR = √2/2
   - cos45° = PQ/QR = √2/2
   - tan45° = PR/PQ = √2/√2 = 1

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时长 |
|------|------|---------|---------|
| 0.0s | sin公式出现 | `Write(sin_formula_45)` | 0.8s |
| 0.8s | 高亮对边和斜边 | `Indicate(PR), Indicate(QR)` | 0.6s |
| 1.4s | 显示计算结果 | `TransformMatchingTex(...)` | 0.8s |
| 2.2s | cos公式出现 | `Write(cos_formula_45)` | 0.8s |
| 3.0s | 高亮邻边和斜边 | `Indicate(PQ), Indicate(QR)` | 0.6s |
| 3.6s | 显示计算结果 | `TransformMatchingTex(...)` | 0.8s |
| 4.4s | tan公式出现 | `Write(tan_formula_45)` | 0.8s |
| 5.2s | 显示计算结果 (=1) | `TransformMatchingTex(...)` | 0.8s |
| 6.0s | 强调tan45°=1 | `Flash(tan_result), Indicate(tan_result)` | 0.8s |
| 6.8s | 等待 | `Wait(1.0)` | 1.0s |

### 清理
- FadeOut: triangle_45, formulas
- 保留: author_info

---

## Scene 6: 60°角构造 (6-8秒)
**目的**: 展示60°角与30°角的关系

### 元素
1. 重新绘制等边三角形 (复用30°的几何数据)
2. 高线CD
3. 高亮60°角 (∠ACD 或 ∠DCA)
4. 边长标注: AD=1, CD=√3, AC=2

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时长 |
|------|------|---------|---------|
| 0.0s | 标题淡入 | `FadeIn(title_60)` | 0.4s |
| 0.4s | 绘制等边三角形 | `Create(triangle_60)` | 1.0s |
| 1.4s | 绘制高线 | `Create(altitude_CD)` | 0.8s |
| 2.2s | 高亮60°角 | `Create(angle_60_arc), Write(angle_label)` | 0.8s |
| 3.0s | 标注边长 | `Write(labels)` | 1.0s |
| 4.0s | 说明文字 | `FadeIn(explanation_60)` | 0.5s |
| 4.5s | 等待理解 | `Wait(2.0)` | 2.0s |

### 几何验证
- [x] 使用与30°相同的等边三角形
- [x] ∠ACD = 60° (等边三角形内角)
- [x] 对边和邻边互换 (相对于30°)

### 清理
- 保留三角形用于下一场景

---

## Scene 7: 60°角三角比计算 (6-8秒)
**目的**: 展示sin60°, cos60°, tan60°的计算过程

### 元素
1. 保留的60°直角三角形
2. 三角比公式:
   - sin60° = CD/AC = √3/2
   - cos60° = AD/AC = 1/2
   - tan60° = CD/AD = √3/1 = √3

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时长 |
|------|------|---------|---------|
| 0.0s | sin公式出现 | `Write(sin_formula_60)` | 0.8s |
| 0.8s | 高亮对边和斜边 | `Indicate(CD), Indicate(AC)` | 0.6s |
| 1.4s | 显示计算结果 | `TransformMatchingTex(...)` | 0.8s |
| 2.2s | cos公式出现 | `Write(cos_formula_60)` | 0.8s |
| 3.0s | 高亮邻边和斜边 | `Indicate(AD), Indicate(AC)` | 0.6s |
| 3.6s | 显示计算结果 | `TransformMatchingTex(...)` | 0.8s |
| 4.4s | tan公式出现 | `Write(tan_formula_60)` | 0.8s |
| 5.2s | 显示计算结果 | `TransformMatchingTex(...)` | 0.8s |
| 6.0s | 等待 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: triangle_60, formulas
- 保留: author_info

---

## Scene 8: 汇总表格 (8-10秒)
**目的**: 展示所有特殊角的三角比值总结表

### 元素
1. 三角比值汇总表:
   ```
   角度 | sin   | cos   | tan
   30°  | 1/2   | √3/2  | √3/3
   45°  | √2/2  | √2/2  | 1
   60°  | √3/2  | 1/2   | √3
   ```
2. 记忆提示

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时长 |
|------|------|---------|---------|
| 0.0s | 标题淡入 | `FadeIn(title_summary)` | 0.4s |
| 0.4s | 表格框架出现 | `Create(table)` | 1.0s |
| 1.4s | 30°行数据填充 | `Write(row_30)` | 0.8s |
| 2.2s | 45°行数据填充 | `Write(row_45)` | 0.8s |
| 3.0s | 60°行数据填充 | `Write(row_60)` | 0.8s |
| 3.8s | 高亮特殊规律 | `Indicate(special_patterns)` | 1.0s |
| 4.8s | 记忆提示出现 | `FadeIn(memory_tips)` | 0.8s |
| 5.6s | 等待 | `Wait(2.5)` | 2.5s |

### 记忆提示内容
- "sin和cos互换: sin30°=cos60°, sin60°=cos30°"
- "45°的sin和cos相等"
- "tan45°=1, tan30°和tan60°互为倒数的√3倍"

### 清理
- 保留表格用于片尾

---

## Scene 9: 片尾关注 (4-5秒)
**目的**: 引导关注，强化品牌

### 元素
1. 作者信息放大
2. 关注提示: "关注我, 获得更多数学技巧!"
3. 三角形装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时长 |
|------|------|---------|---------|
| 0.0s | 淡出表格 | `FadeOut(table)` | 0.5s |
| 0.5s | 作者信息放大 | `Transform(author_info, author_large)` | 0.6s |
| 1.1s | 关注提示出现 | `FadeIn(follow_text, shift=UP*0.3)` | 0.5s |
| 1.6s | 三角形装饰闪烁 | `FadeIn(triangles), Rotate(triangles)` | 1.5s |
| 3.1s | 等待 | `Wait(1.5)` | 1.5s |

### 清理
- 全部淡出

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 9 | 全程保留 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| triangle_30 | Scene 2 | Scene 3 | 30°三角形 |
| triangle_45 | Scene 4 | Scene 5 | 45°三角形 |
| triangle_60 | Scene 6 | Scene 7 | 60°三角形 |
| summary_table | Scene 8 | Scene 9 | 汇总表格 |

---

## 技术注意事项

### LaTeX公式
- ✅ 使用 `r"..."` 原始字符串
- ✅ 度数符号: `^\circ`
- ✅ 分数: `\frac{a}{b}`
- ✅ 根号: `\sqrt{3}`
- ❌ 避免中文在MathTex中

### 角度标记
```python
# 30°角标记 (使用Angle.from_three_points)
angle_30 = Angle.from_three_points(
    self.B_30,  # AB边上的点
    self.A_30,  # 顶点
    self.C_30,  # AC边上的点
    radius=0.5,
    color=COLOR_30
)
```

### 直角标记
```python
# 使用RightAngle或Elbow
right_angle = RightAngle(
    Line(self.A, self.D),
    Line(self.D, self.C),
    length=0.2,
    quadrant=(1, 1)
)
```

### 边界检查
- x ∈ [-4, 4]
- y ∈ [-7, 7] (主内容区 y ∈ [-3, 5])
- 标题区: y ∈ [5.5, 7]
- 底部说明: y ∈ [-6, -3]

---

## 预期效果

1. **教学目标**: 学生能够理解并记忆30°、45°、60°的三角比值
2. **视觉吸引力**: 颜色鲜明，动画流畅
3. **逻辑清晰**: 从几何构造到数值计算，步骤分明
4. **记忆辅助**: 提供规律总结和记忆技巧

---

## 总时长估算
- Scene 1: 3-4秒
- Scene 2: 8-10秒
- Scene 3: 6-8秒
- Scene 4: 7-9秒
- Scene 5: 6-8秒
- Scene 6: 6-8秒
- Scene 7: 6-8秒
- Scene 8: 8-10秒
- Scene 9: 4-5秒

**总计**: 54-70秒 ✅ (符合TikTok短视频规范)