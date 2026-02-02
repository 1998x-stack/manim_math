# 相似三角形判定定理 - 动画分镜脚本

## 元信息
- 目标时长: 75-90 秒
- 场景数量: 7 个
- 难度等级: 中等
- 目标年级: 九年级

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主三角形
COLOR_SECONDARY = "#e74c3c"    # 红色 - 相似三角形
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮强调
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线/标注
COLOR_SUCCESS = GREEN          # 绿色 - 成功标记
COLOR_BACKGROUND = "#1a1a2e"   # 深蓝背景
```

## 几何预计算清单

### 三角形1 (ABC) - 主三角形
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点A | np.array([-2.5, 0, 0]) * SCALE + OFFSET | self.A1 |
| 顶点B | np.array([2.5, 0, 0]) * SCALE + OFFSET | self.B1 |
| 顶点C | np.array([0, 2.8, 0]) * SCALE + OFFSET | self.C1 |
| 边长AB | np.linalg.norm(B1 - A1) | self.AB1 |
| 边长BC | np.linalg.norm(C1 - B1) | self.BC1 |
| 边长CA | np.linalg.norm(A1 - C1) | self.CA1 |
| 角A | GeometryCalculator.angle_at_vertex(C1, A1, B1) | self.angle_A1 |
| 角B | GeometryCalculator.angle_at_vertex(A1, B1, C1) | self.angle_B1 |
| 角C | GeometryCalculator.angle_at_vertex(B1, C1, A1) | self.angle_C1 |

### 三角形2 (DEF) - 相似三角形（缩放版本）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 相似比 | 0.6 | self.SIMILAR_RATIO |
| 顶点D | A1 * SIMILAR_RATIO + offset | self.D |
| 顶点E | B1 * SIMILAR_RATIO + offset | self.E |
| 顶点F | C1 * SIMILAR_RATIO + offset | self.F |
| 边长DE | AB1 * SIMILAR_RATIO | self.DE |
| 边长EF | BC1 * SIMILAR_RATIO | self.EF |
| 边长FD | CA1 * SIMILAR_RATIO | self.FD |

### AA判定专用三角形
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点G | 独立定义（保持∠G = ∠A, ∠H = ∠B） | self.G |
| 顶点H | 根据角度关系计算 | self.H |
| 顶点I | 根据角度关系计算 | self.I |

### SAS判定专用三角形
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点J | 保持两边比例和夹角相等 | self.J |
| 顶点K | 根据比例关系计算 | self.K |
| 顶点L | 根据比例关系计算 | self.L |

---

## Scene 1: 开场引入 (0-5秒)
**目的**: 吸引注意力 + 引出相似三角形概念

### 元素
1. 作者标识 (顶部，常驻)
2. 钩子问题（大字）
3. 两个三角形（一大一小，相似）

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 创建 author_info |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 创建 hook_text |
| 1.0s | 大三角形创建 | `Create(triangle_ABC)` | 创建 triangle_ABC |
| 1.8s | 小三角形创建并移到右侧 | `Create(triangle_DEF).shift(RIGHT*3)` | 创建 triangle_DEF |
| 2.5s | 相似符号闪烁 | `Flash(similar_symbol)` | 创建 similar_symbol |
| 3.5s | 提示文字淡入 | `FadeIn(hint_text)` | 创建 hint_text |
| 4.5s | 等待 | `Wait(1.0)` | - |

### 钩子文字内容
```
"如何判断两个三角形相似?"
font_size=42, color=GOLD
```

### 提示文字内容
```
"三大判定定理帮你搞定!"
font_size=28, color=YELLOW
```

### 清理
- FadeOut: hook_text, hint_text, similar_symbol
- 保留: triangle_ABC, triangle_DEF (移回center), author_info

---

## Scene 2: AA判定 - 两角对应相等 (5-20秒)
**目的**: 展示并证明AA相似判定定理

### 元素
1. 标题: "判定1: AA (两角对应相等)"
2. 两个三角形
3. 角度标记（相等的角）
4. 公式展示
5. 验证标记 (✓)

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 5.0s | 标题写入 | `Write(title_aa)` | 创建 title_aa |
| 5.8s | 移除之前三角形，创建新三角形ABC | `FadeOut(old), Create(triangle_ABC)` | 重建 triangle_ABC |
| 6.8s | 创建三角形GHI（右侧） | `Create(triangle_GHI).shift(RIGHT*3.5)` | 创建 triangle_GHI |
| 7.5s | 标记角A和角G（相等） | `Create(angle_A), Create(angle_G)` | 创建 angle_A, angle_G |
| 8.3s | 添加角度数值标签 | `FadeIn(label_angle_A, label_angle_G)` | 创建标签 |
| 9.0s | 角A和角G同时高亮闪烁 | `Flash(angle_A), Flash(angle_G)` | - |
| 10.0s | 标记角B和角H（相等） | `Create(angle_B), Create(angle_H)` | 创建 angle_B, angle_H |
| 10.8s | 添加角度数值标签 | `FadeIn(label_angle_B, label_angle_H)` | 创建标签 |
| 11.5s | 角B和角H同时高亮闪烁 | `Flash(angle_B), Flash(angle_H)` | - |
| 12.5s | 显示公式 | `Write(formula_aa)` | 创建 formula_aa |
| 14.0s | 结论文字 | `FadeIn(conclusion_aa)` | 创建 conclusion_aa |
| 15.0s | 成功标记 | `FadeIn(checkmark, scale=0.5), Flash(checkmark)` | 创建 checkmark |
| 16.5s | 等待理解 | `Wait(1.5)` | - |

### 公式内容
```latex
MathTex(r"\angle A = \angle G, \, \angle B = \angle H")
MathTex(r"\Downarrow")
MathTex(r"\triangle ABC \sim \triangle GHI")
```

### 结论文字
```
"两角对应相等 ⟹ 三角形相似"
font_size=24, color=COLOR_SUCCESS
```

### 几何计算要点
```python
# 确保角度相等
self.angle_A1 = GeometryCalculator.angle_at_vertex(self.C1, self.A1, self.B1)
self.angle_B1 = GeometryCalculator.angle_at_vertex(self.A1, self.B1, self.C1)

# 构造GHI时，保持∠G = ∠A, ∠H = ∠B
# 方法：使用旋转和缩放
self.angle_G = self.angle_A1  # 目标角度
self.angle_H = self.angle_B1  # 目标角度
```

### 清理
- FadeOut: title_aa, triangle_ABC, triangle_GHI, 所有角度标记, formula_aa, conclusion_aa, checkmark
- 保留: author_info

---

## Scene 3: SAS判定 - 两边成比例且夹角相等 (20-38秒)
**目的**: 展示并证明SAS相似判定定理

### 元素
1. 标题: "判定2: SAS (两边成比例且夹角相等)"
2. 两个三角形
3. 边长标记（比例相等）
4. 角度标记（夹角相等）
5. 公式展示
6. 验证标记 (✓)

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 20.0s | 标题写入 | `Write(title_sas)` | 创建 title_sas |
| 21.0s | 创建三角形ABC | `Create(triangle_ABC)` | 创建 triangle_ABC |
| 22.0s | 创建三角形JKL（右侧） | `Create(triangle_JKL).shift(RIGHT*3.5)` | 创建 triangle_JKL |
| 23.0s | 标记边AB和边JK | `Create(line_AB), Create(line_JK)` | 高亮边 |
| 24.0s | 添加边长标签 | `FadeIn(label_AB, label_JK)` | 创建标签 AB=5, JK=3 |
| 25.0s | 标记边AC和边JL | `Create(line_AC), Create(line_JL)` | 高亮边 |
| 26.0s | 添加边长标签 | `FadeIn(label_AC, label_JL)` | 创建标签 AC=6, JL=3.6 |
| 27.0s | 显示比例关系 | `Write(ratio_formula)` | 创建 ratio_formula |
| 28.5s | 比例等号高亮 | `Flash(equal_sign)` | - |
| 29.5s | 标记夹角A和夹角J | `Create(angle_A), Create(angle_J)` | 创建角度标记 |
| 30.5s | 添加角度标签 | `FadeIn(label_angle_A, label_angle_J)` | 创建标签 |
| 31.5s | 角度闪烁强调 | `Flash(angle_A), Flash(angle_J)` | - |
| 32.5s | 显示完整公式 | `Write(formula_sas)` | 创建 formula_sas |
| 34.0s | 结论文字 | `FadeIn(conclusion_sas)` | 创建 conclusion_sas |
| 35.0s | 成功标记 | `FadeIn(checkmark, scale=0.5), Flash(checkmark)` | 创建 checkmark |
| 36.5s | 等待理解 | `Wait(2.0)` | - |

### 公式内容
```latex
# 比例公式
MathTex(r"\frac{AB}{JK} = \frac{5}{3} = \frac{5}{3}")
MathTex(r"\frac{AC}{JL} = \frac{6}{3.6} = \frac{5}{3}")

# 完整SAS公式
MathTex(r"\frac{AB}{JK} = \frac{AC}{JL}, \, \angle A = \angle J")
MathTex(r"\Downarrow")
MathTex(r"\triangle ABC \sim \triangle JKL")
```

### 结论文字
```
"两边成比例 + 夹角相等 ⟹ 三角形相似"
font_size=22, color=COLOR_SUCCESS
```

### 几何计算要点
```python
# 三角形ABC
self.A1 = np.array([-2.5, 0, 0]) * SCALE + OFFSET
self.B1 = np.array([2.5, 0, 0]) * SCALE + OFFSET
self.C1 = np.array([0, 2.8, 0]) * SCALE + OFFSET

self.AB1 = np.linalg.norm(self.B1 - self.A1)  # = 5
self.AC1 = np.linalg.norm(self.C1 - self.A1)  # = 6
self.angle_A1 = GeometryCalculator.angle_at_vertex(self.C1, self.A1, self.B1)

# 三角形JKL - 保持比例 3/5 和角度相等
ratio = 3.0 / 5.0
self.J = np.array([1.5, -0.5, 0]) * SCALE + OFFSET

# JK边: 长度 = AB1 * ratio, 方向与AB1相同
vec_AB = (self.B1 - self.A1) / self.AB1  # 单位向量
self.K = self.J + vec_AB * (self.AB1 * ratio)  # JK = 3

# JL边: 长度 = AC1 * ratio, 保持角度 = angle_A1
vec_AC = (self.C1 - self.A1) / self.AC1  # 单位向量
self.L = self.J + vec_AC * (self.AC1 * ratio)  # JL = 3.6

# 验证
self.JK = np.linalg.norm(self.K - self.J)
self.JL = np.linalg.norm(self.L - self.J)
assert abs(self.JK / self.AB1 - ratio) < 1e-6
assert abs(self.JL / self.AC1 - ratio) < 1e-6
self.angle_J = GeometryCalculator.angle_at_vertex(self.L, self.J, self.K)
assert abs(self.angle_J - self.angle_A1) < 1e-6
```

### 清理
- FadeOut: title_sas, 所有三角形, 标记, 公式, conclusion_sas, checkmark
- 保留: author_info

---

## Scene 4: SSS判定 - 三边成比例 (38-56秒)
**目的**: 展示并证明SSS相似判定定理

### 元素
1. 标题: "判定3: SSS (三边成比例)"
2. 两个三角形
3. 三条边的长度标记
4. 比例关系展示
5. 公式展示
6. 验证标记 (✓)

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 38.0s | 标题写入 | `Write(title_sss)` | 创建 title_sss |
| 39.0s | 创建三角形ABC | `Create(triangle_ABC)` | 创建 triangle_ABC |
| 40.0s | 创建三角形MNP（右侧，缩小版） | `Create(triangle_MNP).shift(RIGHT*3.5)` | 创建 triangle_MNP |
| 41.0s | 标记边AB和边MN | `Create(line_AB), Create(line_MN)` | 高亮边 |
| 42.0s | 添加边长标签 | `FadeIn(label_AB, label_MN)` | AB=5, MN=2 |
| 43.0s | 标记边BC和边NP | `Create(line_BC), Create(line_NP)` | 高亮边 |
| 44.0s | 添加边长标签 | `FadeIn(label_BC, label_NP)` | BC=6, NP=2.4 |
| 45.0s | 标记边CA和边PM | `Create(line_CA), Create(line_PM)` | 高亮边 |
| 46.0s | 添加边长标签 | `FadeIn(label_CA, label_PM)` | CA=7, PM=2.8 |
| 47.0s | 显示三个比例 | `Write(ratio_formula_1)` | 创建 ratio_formula_1 |
| 48.0s | 继续显示比例 | `Write(ratio_formula_2)` | 创建 ratio_formula_2 |
| 49.0s | 继续显示比例 | `Write(ratio_formula_3)` | 创建 ratio_formula_3 |
| 50.0s | 三个比例等号同时高亮 | `Flash(...)` | - |
| 51.0s | 显示完整公式 | `Write(formula_sss)` | 创建 formula_sss |
| 52.5s | 结论文字 | `FadeIn(conclusion_sss)` | 创建 conclusion_sss |
| 53.5s | 成功标记 | `FadeIn(checkmark, scale=0.5), Flash(checkmark)` | 创建 checkmark |
| 55.0s | 等待理解 | `Wait(2.0)` | - |

### 公式内容
```latex
# 三个比例
MathTex(r"\frac{AB}{MN} = \frac{5}{2} = 2.5")
MathTex(r"\frac{BC}{NP} = \frac{6}{2.4} = 2.5")
MathTex(r"\frac{CA}{PM} = \frac{7}{2.8} = 2.5")

# 完整SSS公式
MathTex(r"\frac{AB}{MN} = \frac{BC}{NP} = \frac{CA}{PM}")
MathTex(r"\Downarrow")
MathTex(r"\triangle ABC \sim \triangle MNP")
```

### 结论文字
```
"三边对应成比例 ⟹ 三角形相似"
font_size=24, color=COLOR_SUCCESS
```

### 几何计算要点
```python
# 三角形ABC（保持之前定义）
self.AB1 = 5.0
self.BC1 = 6.0
self.CA1 = 7.0

# 三角形MNP - 严格按比例缩放
ratio = 2.0 / 5.0  # = 0.4
self.MN = self.AB1 * ratio  # = 2.0
self.NP = self.BC1 * ratio  # = 2.4
self.PM = self.CA1 * ratio  # = 2.8

# 坐标计算 - 保持形状完全相似
# 方法：先定义ABC，然后整体缩放
center = (self.A1 + self.B1 + self.C1) / 3
self.M = (self.A1 - center) * ratio + target_center
self.N = (self.B1 - center) * ratio + target_center
self.P = (self.C1 - center) * ratio + target_center

# 验证
assert abs(np.linalg.norm(self.N - self.M) - self.MN) < 1e-6
assert abs(np.linalg.norm(self.P - self.N) - self.NP) < 1e-6
assert abs(np.linalg.norm(self.M - self.P) - self.PM) < 1e-6
```

### 清理
- FadeOut: title_sss, 所有三角形, 标记, 公式, conclusion_sss, checkmark
- 保留: author_info

---

## Scene 5: 直角三角形HL判定 (56-69秒)
**目的**: 特别介绍直角三角形的HL相似判定

### 元素
1. 标题: "特殊: 直角三角形 HL判定"
2. 两个直角三角形
3. 直角标记
4. 斜边和一直角边标记
5. 公式展示

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 56.0s | 标题写入 | `Write(title_hl)` | 创建 title_hl |
| 57.0s | 创建直角三角形ABC（∠C=90°） | `Create(triangle_ABC)` | 创建 triangle_ABC |
| 58.0s | 标记直角C | `Create(right_angle_C)` | 创建直角符号 |
| 59.0s | 创建直角三角形QRS（∠S=90°） | `Create(triangle_QRS).shift(RIGHT*3.5)` | 创建 triangle_QRS |
| 60.0s | 标记直角S | `Create(right_angle_S)` | 创建直角符号 |
| 61.0s | 高亮斜边AB和QR | `Create(line_AB), Create(line_QR)` | 高亮斜边 |
| 62.0s | 添加斜边标签 | `FadeIn(label_AB, label_QR)` | AB=5, QR=4 |
| 63.0s | 高亮直角边BC和RS | `Create(line_BC), Create(line_RS)` | 高亮边 |
| 64.0s | 添加边长标签 | `FadeIn(label_BC, label_RS)` | BC=3, RS=2.4 |
| 65.0s | 显示比例关系 | `Write(ratio_formula)` | 创建比例公式 |
| 66.0s | 显示完整HL公式 | `Write(formula_hl)` | 创建 formula_hl |
| 67.0s | 结论文字 | `FadeIn(conclusion_hl)` | 创建 conclusion_hl |
| 68.0s | 成功标记 | `FadeIn(checkmark, scale=0.5), Flash(checkmark)` | 创建 checkmark |

### 公式内容
```latex
# 比例
MathTex(r"\frac{AB}{QR} = \frac{5}{4} = 1.25")
MathTex(r"\frac{BC}{RS} = \frac{3}{2.4} = 1.25")

# 完整HL公式
MathTex(r"\frac{AB}{QR} = \frac{BC}{RS}, \, \angle C = \angle S = 90^\circ")
MathTex(r"\Downarrow")
MathTex(r"\triangle ABC \sim \triangle QRS")
```

### 几何计算要点
```python
# 直角三角形ABC: ∠C = 90°
self.A_rt = np.array([-2, 0, 0]) * SCALE + OFFSET
self.C_rt = np.array([2, 0, 0]) * SCALE + OFFSET
self.B_rt = np.array([2, 2.4, 0]) * SCALE + OFFSET  # BC垂直于AC

# 验证直角
vec_CA = self.A_rt - self.C_rt
vec_CB = self.B_rt - self.C_rt
assert abs(np.dot(vec_CA[:2], vec_CB[:2])) < 1e-8  # 垂直

# 计算边长
self.AB_rt = np.linalg.norm(self.B_rt - self.A_rt)  # 斜边 = 5
self.BC_rt = np.linalg.norm(self.C_rt - self.B_rt)  # 直角边 = 3
self.CA_rt = np.linalg.norm(self.A_rt - self.C_rt)  # 直角边 = 4

# 直角三角形QRS: 保持比例 4/5
ratio = 4.0 / 5.0
self.Q = ...  # 类似构造
self.R = ...
self.S = ...
self.QR = self.AB_rt * ratio  # 斜边 = 4
self.RS = self.BC_rt * ratio  # 直角边 = 2.4
```

### 清理
- FadeOut: title_hl, 所有三角形, 标记, 公式, conclusion_hl, checkmark
- 保留: author_info

---

## Scene 6: 总结对比 (69-77秒)
**目的**: 快速回顾四种判定方法

### 元素
1. 四张判定卡片（AA, SAS, SSS, HL）
2. 记忆口诀

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 69.0s | 标题写入 | `Write(title_summary)` | 创建 title_summary |
| 70.0s | AA卡片滑入 | `card_AA.animate.shift(LEFT*10, 0)` | 创建 card_AA |
| 70.5s | SAS卡片滑入 | `card_SAS.animate.shift(LEFT*10, 0)` | 创建 card_SAS |
| 71.0s | SSS卡片滑入 | `card_SSS.animate.shift(LEFT*10, 0)` | 创建 card_SSS |
| 71.5s | HL卡片滑入 | `card_HL.animate.shift(LEFT*10, 0)` | 创建 card_HL |
| 72.5s | 口诀淡入 | `FadeIn(mnemonic)` | 创建 mnemonic |
| 74.0s | 所有卡片同时高亮 | `Flash(...)` | - |
| 75.5s | 等待 | `Wait(1.5)` | - |

### 卡片内容
```python
# AA卡片
"AA: 两角对应相等"
color=COLOR_HIGHLIGHT

# SAS卡片
"SAS: 两边成比例且夹角相等"
color=COLOR_HIGHLIGHT

# SSS卡片
"SSS: 三边对应成比例"
color=COLOR_HIGHLIGHT

# HL卡片
"HL: 直角三角形斜边和直角边成比例"
color=COLOR_HIGHLIGHT
```

### 口诀
```
"两角、两边夹角、三边、直角HL"
font_size=32, color=GOLD
```

### 清理
- FadeOut: 所有卡片, title_summary, mnemonic
- 保留: author_info

---

## Scene 7: 片尾关注 (77-85秒)
**目的**: 引导关注，增强记忆

### 元素
1. 作者名称放大
2. ID显示
3. 关注提示
4. 相似三角形图标装饰

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 77.0s | 作者名称放大 | `Transform(author_info, author_large)` | 变换 author_info |
| 77.8s | ID淡入 | `FadeIn(author_id)` | 创建 author_id |
| 78.5s | 关注提示淡入 | `FadeIn(follow_text, scale=1.1)` | 创建 follow_text |
| 79.5s | 相似三角形图标环绕 | `FadeIn(triangles), Rotate(triangles)` | 创建装饰 |
| 81.0s | 四个判定图标快闪 | `FadeIn(icons)` | 创建 icons |
| 83.0s | 全部淡出 | `FadeOut(...)` | 清理所有 |

### 文字内容
```
作者: "上海初高中数学直通车"
ID: "@emptyandcalm"
提示: "关注我，掌握更多相似三角形技巧!"
```

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 常驻顶部 |
| triangle_ABC | Scene 1-6 | 各场景结束 | 主三角形，多次重建 |
| triangle_DEF | Scene 1 | Scene 1 | 开场演示用 |
| triangle_GHI | Scene 2 | Scene 2 | AA判定用 |
| triangle_JKL | Scene 3 | Scene 3 | SAS判定用 |
| triangle_MNP | Scene 4 | Scene 4 | SSS判定用 |
| triangle_QRS | Scene 5 | Scene 5 | HL判定用 |
| checkmark | Scene 2-5 | 各场景结束 | 每个判定后出现 |

---

## 关键验证点

### 角度验证
```python
def verify_angle_equality(angle1, angle2, eps=1e-6):
    assert abs(angle1 - angle2) < eps, f"角度不等: {np.degrees(angle1):.2f}° ≠ {np.degrees(angle2):.2f}°"
```

### 比例验证
```python
def verify_ratio(length1, length2, expected_ratio, eps=1e-6):
    actual_ratio = length1 / length2
    assert abs(actual_ratio - expected_ratio) < eps, f"比例错误: {actual_ratio:.4f} ≠ {expected_ratio:.4f}"
```

### 直角验证
```python
def verify_right_angle(vertex, point1, point2, eps=1e-8):
    vec1 = point1 - vertex
    vec2 = point2 - vertex
    dot = np.dot(vec1[:2], vec2[:2])
    assert abs(dot) < eps, f"不是直角: 点积 = {dot:.8f}"
```

---

## 动画节奏建议

- **AA判定**: 15秒（简单，两个角）
- **SAS判定**: 18秒（中等，两边+一角）
- **SSS判定**: 18秒（稍复杂，三条边）
- **HL判定**: 13秒（特殊情况，快速过）
- **总结**: 8秒（快速回顾）
- **片尾**: 8秒

总计: **80秒** （符合TikTok最佳时长）