# 相似三角形的判定 - 动画分镜脚本

## 元信息
- 目标时长: 75-85 秒
- 场景数量: 8 个
- 难度等级: 中等
- 目标观众: 九年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主三角形
COLOR_SECONDARY = "#e74c3c"    # 红色 - 次三角形
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮重点
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线
COLOR_SUCCESS = "#2ecc71"       # 绿色 - 判定成功
BACKGROUND_COLOR = "#1a1a2e"    # 深蓝背景
```

## 几何预计算清单

### 场景2 - AA判定示例
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| △ABC顶点A | 基准点 | self.AA_triangle1_A |
| △ABC顶点B | A + 向量 | self.AA_triangle1_B |
| △ABC顶点C | 通过角度计算 | self.AA_triangle1_C |
| △DEF顶点D | 基准点 | self.AA_triangle2_D |
| △DEF顶点E | D + 相似比例向量 | self.AA_triangle2_E |
| △DEF顶点F | 通过角度计算（相同角度） | self.AA_triangle2_F |
| 角A大小 | 60° | self.AA_angle_A |
| 角B大小 | 50° | self.AA_angle_B |

### 场景3 - SAS判定示例
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| △ABC顶点A | 基准点 | self.SAS_triangle1_A |
| △ABC顶点B | A + 长度c | self.SAS_triangle1_B |
| △ABC顶点C | A + 旋转角A后长度b | self.SAS_triangle1_C |
| △DEF顶点D | 基准点 | self.SAS_triangle2_D |
| △DEF顶点E | D + 比例k*c | self.SAS_triangle2_E |
| △DEF顶点F | D + 旋转角A后比例k*b | self.SAS_triangle2_F |
| 边长比例 | AB/DE = AC/DF | self.SAS_ratio |
| 夹角A大小 | 70° | self.SAS_angle_A |

### 场景4 - SSS判定示例
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| △ABC顶点A | 基准点 | self.SSS_triangle1_A |
| △ABC顶点B | A + 长度c | self.SSS_triangle1_B |
| △ABC顶点C | 通过三边长构造 | self.SSS_triangle1_C |
| △DEF顶点D | 基准点 | self.SSS_triangle2_D |
| △DEF顶点E | D + 比例k*c | self.SSS_triangle2_E |
| △DEF顶点F | 通过三边长比例构造 | self.SSS_triangle2_F |
| 三边比例 | AB/DE = BC/EF = CA/FD = k | self.SSS_ratio |

---

## Scene 1: 开场钩子 (0-5秒)

**目的**: 吸引注意力，提出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题: "如何判断两个三角形相似?"
3. 两个三角形图形（一大一小，明显相似）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2, run_time=0.3)` |
| 0.3s | 钩子问题书写 | `Write(hook_question, run_time=0.8)` |
| 1.1s | 第一个三角形创建 | `Create(triangle1, run_time=0.8)` |
| 1.9s | 第二个三角形创建（缩放版本） | `Create(triangle2, run_time=0.8)` |
| 2.7s | 相似符号出现 | `FadeIn(similarity_symbol, scale=1.2, run_time=0.4)` |
| 3.1s | 等待 | `Wait(1.0)` |
| 4.1s | 提示文字 | `FadeIn(hint_text, shift=UP*0.3, run_time=0.5)` |

### 几何计算
```python
# 大三角形 (蓝色)
self.intro_A = np.array([-2.5, 0, 0]) * 0.8 + UP * 2
self.intro_B = np.array([2.5, 0, 0]) * 0.8 + UP * 2
self.intro_C = np.array([0, 3, 0]) * 0.8 + UP * 2

# 小三角形 (红色，相似比1:2)
scale = 0.5
offset = DOWN * 1.5
self.intro_D = (self.intro_A - self.intro_centroid) * scale + offset
self.intro_E = (self.intro_B - self.intro_centroid) * scale + offset
self.intro_F = (self.intro_C - self.intro_centroid) * scale + offset
```

### 清理
- FadeOut: hook_question, triangle1, triangle2, similarity_symbol, hint_text
- 保留: author_info

---

## Scene 2: 判定定理总览 (5-10秒)

**目的**: 展示三种主要判定方法

### 元素
1. 标题: "相似三角形判定定理"
2. 三个判定方法卡片: AA, SAS, SSS

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title, run_time=0.8)` |
| 0.8s | AA卡片滑入 | `card_AA.animate.shift(RIGHT, run_time=0.5)` |
| 1.3s | SAS卡片滑入 | `card_SAS.animate.shift(RIGHT, run_time=0.5)` |
| 1.8s | SSS卡片滑入 | `card_SSS.animate.shift(RIGHT, run_time=0.5)` |
| 2.3s | 等待观看 | `Wait(1.5)` |

### 卡片内容
```
AA: 两角对应相等
SAS: 两边成比例且夹角相等
SSS: 三边对应成比例
```

### 清理
- FadeOut: title, cards
- 过渡到下一场景

---

## Scene 3: AA判定详解 (10-25秒)

**目的**: 详细演示AA判定方法

### 元素
1. 场景标题: "判定方法一: AA (角-角)"
2. △ABC (蓝色)
3. △DEF (红色)
4. 角度标记和数值
5. 判定结论

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 场景标题淡入 | `FadeIn(title, run_time=0.5)` |
| 0.5s | 创建△ABC | `Create(triangle_ABC, run_time=1.0)` |
| 1.5s | 标记顶点A,B,C | `Write(labels, run_time=0.6)` |
| 2.1s | 创建△DEF（较小，位置分离） | `Create(triangle_DEF, run_time=1.0)` |
| 3.1s | 标记顶点D,E,F | `Write(labels_DEF, run_time=0.6)` |
| 3.7s | 标记∠A和角弧 | `Create(angle_A, run_time=0.6)` |
| 4.3s | 显示∠A = 60° | `FadeIn(angle_A_label, run_time=0.4)` |
| 4.7s | 标记∠D和角弧 | `Create(angle_D, run_time=0.6)` |
| 5.3s | 显示∠D = 60° | `FadeIn(angle_D_label, run_time=0.4)` |
| 5.7s | 高亮两角相等 | `Flash + 颜色变化, run_time=0.6)` |
| 6.3s | 标记∠B和角弧 | `Create(angle_B, run_time=0.6)` |
| 6.9s | 显示∠B = 50° | `FadeIn(angle_B_label, run_time=0.4)` |
| 7.3s | 标记∠E和角弧 | `Create(angle_E, run_time=0.6)` |
| 7.9s | 显示∠E = 50° | `FadeIn(angle_E_label, run_time=0.4)` |
| 8.3s | 高亮两角相等 | `Flash + 颜色变化, run_time=0.6)` |
| 8.9s | 显示判定公式 | `Write(formula, run_time=1.0)` |
| 9.9s | 显示结论 | `FadeIn(conclusion, scale=1.1, run_time=0.6)` |
| 10.5s | 打勾确认 | `DrawBorderThenFill(checkmark, run_time=0.5)` |
| 11.0s | 等待理解 | `Wait(1.5)` |

### 几何计算
```python
# △ABC (主三角形)
self.AA_A = np.array([-2.0, 1.5, 0])
self.AA_B = np.array([2.0, -0.5, 0])
# ∠A = 60°, ∠B = 50°, 计算C点
angle_A_rad = 60 * DEGREES
angle_B_rad = 50 * DEGREES
# 使用正弦定理构造C点
c_length = 3.0  # AB长度约为4
b_length = c_length * np.sin(angle_B_rad) / np.sin((180-60-50)*DEGREES)
self.AA_C = self.AA_A + b_length * np.array([np.cos(angle_A_rad), np.sin(angle_A_rad), 0])

# △DEF (相似三角形，比例0.6，位置偏移)
scale_ratio = 0.6
offset = DOWN * 2.5 + RIGHT * 0.5
centroid_ABC = (self.AA_A + self.AA_B + self.AA_C) / 3
self.AA_D = (self.AA_A - centroid_ABC) * scale_ratio + offset
self.AA_E = (self.AA_B - centroid_ABC) * scale_ratio + offset
self.AA_F = (self.AA_C - centroid_ABC) * scale_ratio + offset

# 验证角度
verify_angle(self.AA_C, self.AA_A, self.AA_B, 60 * DEGREES)
verify_angle(self.AA_A, self.AA_B, self.AA_C, 50 * DEGREES)
verify_angle(self.AA_F, self.AA_D, self.AA_E, 60 * DEGREES)
verify_angle(self.AA_D, self.AA_E, self.AA_F, 50 * DEGREES)
```

### 公式内容
```latex
∠A = ∠D, ∠B = ∠E ⟹ △ABC ∽ △DEF
```

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 4: SAS判定详解 (25-42秒)

**目的**: 详细演示SAS判定方法

### 元素
1. 场景标题: "判定方法二: SAS (边-角-边)"
2. △ABC (蓝色)
3. △DEF (红色)
4. 边长标注
5. 夹角标记
6. 比例关系
7. 判定结论

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 场景标题淡入 | `FadeIn(title, run_time=0.5)` |
| 0.5s | 创建△ABC | `Create(triangle_ABC, run_time=1.0)` |
| 1.5s | 标记顶点 | `Write(labels, run_time=0.6)` |
| 2.1s | 高亮边AB | `line_AB.animate.set_color(YELLOW, run_time=0.4)` |
| 2.5s | 标注AB长度 | `FadeIn(label_AB, run_time=0.4)` |
| 2.9s | 高亮边AC | `line_AC.animate.set_color(YELLOW, run_time=0.4)` |
| 3.3s | 标注AC长度 | `FadeIn(label_AC, run_time=0.4)` |
| 3.7s | 标记夹角∠A | `Create(angle_A, run_time=0.6)` |
| 4.3s | 显示∠A = 70° | `FadeIn(angle_A_label, run_time=0.4)` |
| 4.7s | 创建△DEF | `Create(triangle_DEF, run_time=1.0)` |
| 5.7s | 标记顶点DEF | `Write(labels_DEF, run_time=0.6)` |
| 6.3s | 高亮边DE并标注 | `同上 + label_DE, run_time=0.8)` |
| 7.1s | 高亮边DF并标注 | `同上 + label_DF, run_time=0.8)` |
| 7.9s | 显示比例关系 | `Write(ratio_formula, run_time=1.0)` |
| 8.9s | 标记夹角∠D | `Create(angle_D, run_time=0.6)` |
| 9.5s | 显示∠D = 70° | `FadeIn(angle_D_label, run_time=0.4)` |
| 9.9s | 高亮角相等 | `Flash两角, run_time=0.6)` |
| 10.5s | 显示判定公式 | `Write(formula, run_time=1.0)` |
| 11.5s | 显示结论 | `FadeIn(conclusion, scale=1.1, run_time=0.6)` |
| 12.1s | 打勾确认 | `DrawBorderThenFill(checkmark, run_time=0.5)` |
| 12.6s | 等待理解 | `Wait(2.0)` |

### 几何计算
```python
# △ABC
self.SAS_A = np.array([-2.5, 1.0, 0])
angle_A = 70 * DEGREES
length_AB = 3.5  # c
length_AC = 2.8  # b

self.SAS_B = self.SAS_A + length_AB * RIGHT
self.SAS_C = self.SAS_A + length_AC * np.array([np.cos(angle_A), np.sin(angle_A), 0])

# △DEF (相似比例 k = 0.65)
k = 0.65
length_DE = length_AB * k
length_DF = length_AC * k
offset = DOWN * 2.0 + RIGHT * 0.3

self.SAS_D = np.array([-2.5, -1.0, 0]) + offset
self.SAS_E = self.SAS_D + length_DE * RIGHT
self.SAS_F = self.SAS_D + length_DF * np.array([np.cos(angle_A), np.sin(angle_A), 0])

# 验证比例
ratio_1 = length_AB / length_DE
ratio_2 = length_AC / length_DF
assert abs(ratio_1 - ratio_2) < 1e-6, "比例不相等"
```

### 公式内容
```latex
AB/DE = AC/DF = k, ∠A = ∠D ⟹ △ABC ∽ △DEF
```

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 5: SSS判定详解 (42-60秒)

**目的**: 详细演示SSS判定方法

### 元素
1. 场景标题: "判定方法三: SSS (边-边-边)"
2. △ABC (蓝色)
3. △DEF (红色)
4. 三边长度标注
5. 比例关系公式
6. 判定结论

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 场景标题淡入 | `FadeIn(title, run_time=0.5)` |
| 0.5s | 创建△ABC | `Create(triangle_ABC, run_time=1.0)` |
| 1.5s | 标记顶点 | `Write(labels, run_time=0.6)` |
| 2.1s | 高亮AB + 标注长度 | `高亮 + FadeIn(label_AB, run_time=0.7)` |
| 2.8s | 高亮BC + 标注长度 | `高亮 + FadeIn(label_BC, run_time=0.7)` |
| 3.5s | 高亮CA + 标注长度 | `高亮 + FadeIn(label_CA, run_time=0.7)` |
| 4.2s | 创建△DEF | `Create(triangle_DEF, run_time=1.0)` |
| 5.2s | 标记顶点DEF | `Write(labels_DEF, run_time=0.6)` |
| 5.8s | 高亮DE + 标注 | `高亮 + FadeIn(label_DE, run_time=0.7)` |
| 6.5s | 高亮EF + 标注 | `高亮 + FadeIn(label_EF, run_time=0.7)` |
| 7.2s | 高亮FD + 标注 | `高亮 + FadeIn(label_FD, run_time=0.7)` |
| 7.9s | 显示第一个比例 | `Write(ratio1, run_time=0.6)` |
| 8.5s | 显示第二个比例 | `Write(ratio2, run_time=0.6)` |
| 9.1s | 显示第三个比例 | `Write(ratio3, run_time=0.6)` |
| 9.7s | 合并比例公式 | `Transform到统一比例, run_time=0.8)` |
| 10.5s | 显示判定公式 | `Write(formula, run_time=1.0)` |
| 11.5s | 显示结论 | `FadeIn(conclusion, scale=1.1, run_time=0.6)` |
| 12.1s | 打勾确认 | `DrawBorderThenFill(checkmark, run_time=0.5)` |
| 12.6s | 等待理解 | `Wait(2.5)` |

### 几何计算
```python
# △ABC (使用海伦公式确保可构造)
self.SSS_A = np.array([-2.5, 1.5, 0])
self.SSS_B = np.array([2.5, -0.5, 0])

length_AB = np.linalg.norm(self.SSS_B - self.SSS_A)  # c = 5.39
length_BC = 4.0  # a
length_CA = 3.5  # b

# 通过余弦定理计算C点
cos_B = (length_AB**2 + length_BC**2 - length_CA**2) / (2 * length_AB * length_BC)
angle_B = np.arccos(np.clip(cos_B, -1, 1))

# C点位置
direction_BA = (self.SSS_A - self.SSS_B) / length_AB
rotation_matrix = np.array([
    [np.cos(angle_B), -np.sin(angle_B), 0],
    [np.sin(angle_B), np.cos(angle_B), 0],
    [0, 0, 1]
])
direction_BC = rotation_matrix @ direction_BA
self.SSS_C = self.SSS_B + length_BC * direction_BC

# △DEF (相似比例 k = 0.7)
k = 0.7
offset = DOWN * 2.3

centroid_ABC = (self.SSS_A + self.SSS_B + self.SSS_C) / 3
self.SSS_D = (self.SSS_A - centroid_ABC) * k + offset
self.SSS_E = (self.SSS_B - centroid_ABC) * k + offset
self.SSS_F = (self.SSS_C - centroid_ABC) * k + offset

# 验证比例
length_DE = np.linalg.norm(self.SSS_E - self.SSS_D)
length_EF = np.linalg.norm(self.SSS_F - self.SSS_E)
length_FD = np.linalg.norm(self.SSS_D - self.SSS_F)

ratio1 = length_AB / length_DE
ratio2 = length_BC / length_EF
ratio3 = length_CA / length_FD

assert abs(ratio1 - k) < 0.01 and abs(ratio2 - k) < 0.01 and abs(ratio3 - k) < 0.01
```

### 公式内容
```latex
AB/DE = BC/EF = CA/FD = k ⟹ △ABC ∽ △DEF
```

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 6: 三种方法对比汇总 (60-70秒)

**目的**: 对比总结三种判定方法

### 元素
1. 标题: "三种判定方法对比"
2. 三个判定卡片并列
3. 核心要点总结

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title, run_time=0.6)` |
| 0.6s | AA卡片滑入 | `card_AA.animate.shift(RIGHT, run_time=0.5)` |
| 1.1s | SAS卡片滑入 | `card_SAS.animate.shift(RIGHT, run_time=0.5)` |
| 1.6s | SSS卡片滑入 | `card_SSS.animate.shift(RIGHT, run_time=0.5)` |
| 2.1s | 卡片排列 | `VGroup.arrange(DOWN, run_time=0.8)` |
| 2.9s | 高亮关键词 | `依次Flash各关键词, run_time=1.5)` |
| 4.4s | 显示总结 | `FadeIn(summary, run_time=0.8)` |
| 5.2s | 等待理解 | `Wait(2.5)` |

### 卡片详细内容
```
AA: 两角对应相等 → 最简单
SAS: 两边成比例 + 夹角相等 → 常用
SSS: 三边对应成比例 → 最严格
```

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 7: 应用提示 (70-75秒)

**目的**: 给出实际应用建议

### 元素
1. 标题: "判定技巧"
2. 三个技巧提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title, run_time=0.6)` |
| 0.6s | 技巧1淡入 | `FadeIn(tip1, shift=UP*0.3, run_time=0.5)` |
| 1.1s | 技巧2淡入 | `FadeIn(tip2, shift=UP*0.3, run_time=0.5)` |
| 1.6s | 技巧3淡入 | `FadeIn(tip3, shift=UP*0.3, run_time=0.5)` |
| 2.1s | 等待阅读 | `Wait(1.5)` |

### 技巧内容
```
1. 优先找角度 - AA最快
2. 注意对应关系 - 顺序很重要
3. 比例要统一 - k值必须相同
```

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 8: 片尾关注 (75-80秒)

**目的**: 引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息放大 | `Transform(author_info, large_author, run_time=0.8)` |
| 0.8s | ID显示 | `FadeIn(author_id, shift=UP*0.3, run_time=0.5)` |
| 1.3s | 关注文字 | `FadeIn(follow_text, scale=1.1, run_time=0.6)` |
| 1.9s | 三角形装饰旋转 | `Rotate(decorations, run_time=1.5)` |
| 3.4s | 等待结束 | `Wait(0.5)` |

### 清理
- FadeOut: 全部淡出

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 全程保留 |
| intro_triangles | Scene 1 | Scene 1 | 开场演示 |
| AA_triangles | Scene 3 | Scene 3 | AA判定演示 |
| SAS_triangles | Scene 4 | Scene 4 | SAS判定演示 |
| SSS_triangles | Scene 5 | Scene 5 | SSS判定演示 |
| summary_cards | Scene 6 | Scene 6 | 对比汇总 |

---

## 关键几何验证点

### 验证1: AA场景角度
- ∠A = ∠D = 60° (误差 < 0.1°)
- ∠B = ∠E = 50° (误差 < 0.1°)
- 角度和 = 180°

### 验证2: SAS场景比例
- AB/DE = AC/DF = k (误差 < 1%)
- ∠A = ∠D = 70° (误差 < 0.1°)

### 验证3: SSS场景比例
- AB/DE = BC/EF = CA/FD = k (误差 < 1%)

---

## 字体大小规范（TikTok竖屏）

| 类型 | 大小 | 用途 |
|------|------|------|
| title | 36 | 场景标题 |
| subtitle | 28 | 副标题、公式 |
| body | 22 | 说明文字 |
| label | 20 | 顶点标签、数值 |
| small | 18 | 小字说明 |
| author | 20 | 作者信息 |

---

## 总时长分配

| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1 | 5s | 5s |
| Scene 2 | 5s | 10s |
| Scene 3 | 15s | 25s |
| Scene 4 | 17s | 42s |
| Scene 5 | 18s | 60s |
| Scene 6 | 10s | 70s |
| Scene 7 | 5s | 75s |
| Scene 8 | 5s | 80s |
| **总计** | **80s** | - |