# 相似三角形的概念 - 动画分镜脚本

## 元信息
- 目标时长: 70-85 秒
- 场景数量: 7 个
- 难度等级: 中等
- 目标观众: 九年级学生

## 颜色配置
```python
COLOR_TRIANGLE_1 = "#3498db"    # 蓝色 - 小三角形
COLOR_TRIANGLE_2 = "#e74c3c"    # 红色 - 大三角形
COLOR_ANGLE = "#2ecc71"         # 绿色 - 角度标记
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助元素
COLOR_FORMULA = "#f39c12"       # 橙色 - 公式
```

## 几何预计算清单

### 三角形1（小）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点A | 固定点 | self.A1 |
| 顶点B | 固定点 | self.B1 |
| 顶点C | 固定点 | self.C1 |
| 边长AB | norm(B1-A1) | self.ab1 |
| 边长BC | norm(C1-B1) | self.bc1 |
| 边长CA | norm(A1-C1) | self.ca1 |
| 角A | angle_at_vertex(C1,A1,B1) | self.angle_A1 |
| 角B | angle_at_vertex(A1,B1,C1) | self.angle_B1 |
| 角C | angle_at_vertex(B1,C1,A1) | self.angle_C1 |

### 三角形2（大，相似比k=2）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点D | 固定点 | self.A2 |
| 顶点E | A2 + k*(B1-A1) | self.B2 |
| 顶点F | A2 + k*(C1-A1) | self.C2 |
| 边长DE | k * ab1 | self.ab2 |
| 边长EF | k * bc1 | self.bc2 |
| 边长FD | k * ca1 | self.ca2 |
| 角D | 应等于 angle_A1 | self.angle_A2 |
| 角E | 应等于 angle_B1 | self.angle_B2 |
| 角F | 应等于 angle_C1 | self.angle_C2 |

### 关键验证点
- 角度相等：angle_A1 ≈ angle_A2，angle_B1 ≈ angle_B2，angle_C1 ≈ angle_C2
- 比例相等：ab2/ab1 ≈ bc2/bc1 ≈ ca2/ca1 ≈ k

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 引发思考 + 引出相似概念

### 元素
1. 作者标识
2. 钩子问题："两个形状'相似'意味着什么？"
3. 两个大小不同的三角形快闪

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.2s | 小三角形淡入 | `FadeIn(tri1, scale=0.5)` |
| 1.8s | 大三角形淡入 | `FadeIn(tri2, scale=0.5)` |
| 2.5s | 等待 | `Wait(0.8)` |

### 清理
- FadeOut: hook_text, triangles
- 保留: author_info

---

## Scene 2: 定义展示 (8-10秒)
**目的**: 给出相似三角形的定义

### 元素
1. 标题："什么是相似三角形？"
2. 两个三角形并排
3. 定义文字（分两部分）
4. 相似符号 ∽

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 标题淡入 | `Write(title)` | |
| 0.8s | 创建小三角形 | `Create(tri1)` | 左侧 |
| 1.5s | 创建大三角形 | `Create(tri2)` | 右侧 |
| 2.2s | 顶点标签淡入 | `Write(labels)` | A,B,C 和 D,E,F |
| 3.0s | 定义1淡入 | `FadeIn(def1)` | "对应角相等" |
| 4.0s | 定义2淡入 | `FadeIn(def2)` | "对应边成比例" |
| 5.0s | 相似符号出现 | `Write(similar_symbol)` | △ABC ∽ △DEF |
| 6.5s | 等待理解 | `Wait(2.0)` | 关键停留 |

### 清理
- FadeOut: title, def1, def2
- 保留: tri1, tri2, labels, similar_symbol

---

## Scene 3: 对应角相等 (12-15秒)
**目的**: 详细展示对应角相等的性质

### 元素
1. 副标题："条件1: 对应角相等"
2. 角度标记（用不同颜色的弧）
3. 角度数值
4. 相等符号

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 副标题淡入 | `Write(subtitle)` | |
| 0.8s | 标记角A | `Create(angle_A1)` | 绿色弧 |
| 1.3s | 标记角D | `Create(angle_A2)` | 绿色弧 |
| 1.8s | 显示角度值 | `Write(angle_value_A)` | ∠A = ∠D = 60° |
| 2.5s | 闪烁强调 | `Flash(both_angles)` | |
| 3.2s | 标记角B | `Create(angle_B1)` | 黄色弧 |
| 3.7s | 标记角E | `Create(angle_B2)` | 黄色弧 |
| 4.2s | 显示角度值 | `Write(angle_value_B)` | ∠B = ∠E = 80° |
| 5.0s | 标记角C | `Create(angle_C1)` | 橙色弧 |
| 5.5s | 标记角F | `Create(angle_C2)` | 橙色弧 |
| 6.0s | 显示角度值 | `Write(angle_value_C)` | ∠C = ∠F = 40° |
| 7.0s | 总结公式 | `Write(formula)` | ∠A=∠D, ∠B=∠E, ∠C=∠F |
| 9.0s | 等待理解 | `Wait(2.0)` | 关键停留 |

### 清理
- FadeOut: subtitle, angle_marks, angle_values, formula
- 保留: tri1, tri2, labels

---

## Scene 4: 对应边成比例 (12-15秒)
**目的**: 展示对应边成比例的性质

### 元素
1. 副标题："条件2: 对应边成比例"
2. 边长标注
3. 比例计算
4. 相似比 k

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 副标题淡入 | `Write(subtitle)` | |
| 0.8s | 高亮AB和DE | `Indicate(AB), Indicate(DE)` | 黄色闪烁 |
| 1.5s | 标注长度 | `Write(length_AB), Write(length_DE)` | AB=3, DE=6 |
| 2.5s | 显示比例 | `Write(ratio1)` | DE/AB = 2 |
| 3.5s | 高亮BC和EF | `Indicate(BC), Indicate(EF)` | |
| 4.2s | 标注长度 | `Write(length_BC), Write(length_EF)` | BC=4, EF=8 |
| 5.2s | 显示比例 | `Write(ratio2)` | EF/BC = 2 |
| 6.2s | 高亮CA和FD | `Indicate(CA), Indicate(FD)` | |
| 7.0s | 标注长度 | `Write(length_CA), Write(length_FD)` | CA=5, FD=10 |
| 8.0s | 显示比例 | `Write(ratio3)` | FD/CA = 2 |
| 9.0s | 相似比公式 | `Write(formula)` | AB/DE = BC/EF = CA/FD = k |
| 10.5s | 标注k=2 | `Write(k_value)` | k = 2（相似比） |
| 12.0s | 等待理解 | `Wait(2.0)` | 关键停留 |

### 清理
- FadeOut: subtitle, length_labels, ratios, formula
- 保留: tri1, tri2, labels

---

## Scene 5: 相似比的含义 (10-12秒)
**目的**: 解释相似比的几何意义

### 元素
1. 标题："相似比 k"
2. 变换动画（小三角形逐渐放大到大三角形）
3. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 标题淡入 | `Write(title)` | |
| 0.8s | 说明文字 | `FadeIn(explanation)` | "相似比 = 对应边的比值" |
| 1.8s | 小三角形移到中心 | `tri1.animate.move_to(CENTER)` | |
| 2.8s | 缩放动画 | `tri1.animate.scale(2)` | k=2，放大2倍 |
| 4.5s | 闪烁提示 | `Flash(tri1)` | |
| 5.0s | 重置 | `Transform(tri1, original)` | |
| 6.0s | k值说明 | `Write(k_explanation)` | "k>1: 放大, k<1: 缩小" |
| 8.0s | 等待 | `Wait(1.5)` | |

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 6: 全等是特殊情况 (8-10秒)
**目的**: 说明全等三角形是k=1的特殊相似

### 元素
1. 标题："特殊情况: 全等三角形"
2. 两个完全一样的三角形
3. k=1 的标注
4. 全等符号 ≌

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 标题淡入 | `Write(title)` | |
| 0.8s | 创建两个相同三角形 | `Create(tri1), Create(tri2)` | |
| 1.8s | 标注k=1 | `Write(k_equals_1)` | |
| 2.8s | 说明文字 | `FadeIn(explanation)` | "相似比为1的相似三角形" |
| 4.0s | 全等符号 | `Write(congruent_symbol)` | △ABC ≌ △DEF |
| 5.0s | 相似符号 | `Write(similar_symbol)` | △ABC ∽ △DEF |
| 6.0s | 强调关系 | `Write(relation)` | "全等 → 相似（k=1）" |
| 7.5s | 等待 | `Wait(1.5)` | |

### 清理
- FadeOut: 全部元素
- 保留: author_info

---

## Scene 7: 片尾关注 (8-10秒)
**目的**: 品牌强化 + 引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 相似三角形图标装饰

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息放大 | `Transform(author, author_large)` |
| 0.8s | 关注文字淡入 | `FadeIn(follow_text)` |
| 1.5s | 三角形图标 | `Create(icon_triangles)` |
| 2.5s | 旋转缩放动画 | `Rotate(icons), Scale(icons)` |
| 5.0s | 等待 | `Wait(2.0)` |
| 7.0s | 全部淡出 | `FadeOut(*)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 贯穿全片 |
| tri1（小三角形） | Scene 2 | Scene 5 | 主要演示对象 |
| tri2（大三角形） | Scene 2 | Scene 5 | 主要演示对象 |
| angle_marks | Scene 3 | Scene 3 | 角度演示 |
| length_labels | Scene 4 | Scene 4 | 边长演示 |

## 关键验证点
1. **角度验证**: 两个三角形的对应角必须相等（误差<0.01°）
2. **比例验证**: 三组对应边的比值必须相等（误差<0.001）
3. **相似比**: k = 2.0，所有边长比值都应该是2
4. **边界检查**: 两个三角形都在安全区域内
5. **Angle方向**: 确保角度弧线在正确的位置（可能需要 other_angle=True）

## 特殊注意事项
1. 两个三角形的构造：大三角形由小三角形按相似比k缩放得到
2. 对应关系：A↔D, B↔E, C↔F，必须明确标注
3. 角度标记：使用不同颜色区分不同的对应角
4. 数值精度：边长保留1位小数，角度保留整数
5. 动画节奏：对应角和对应边的展示要有节奏感，不要太快