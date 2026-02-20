# 平行线分线段成比例定理 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 6 个
- 难度等级: 中等
- 目标观众: 九年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要线段
COLOR_SECONDARY = "#e74c3c"    # 红色 - 次要线段
COLOR_PARALLEL = "#2ecc71"     # 绿色 - 平行线
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助元素
COLOR_FORMULA = "#f39c12"      # 橙色 - 公式
```

## 几何预计算清单

### 场景2：三条平行线截两条直线
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 直线1起点 | 固定点 | self.L1_start |
| 直线1终点 | 起点 + 方向向量 | self.L1_end |
| 直线2起点 | 固定点 | self.L2_start |
| 直线2终点 | 起点 + 方向向量 | self.L2_end |
| 平行线1与L1交点 | 直线交点计算 | self.A |
| 平行线1与L2交点 | 直线交点计算 | self.D |
| 平行线2与L1交点 | 直线交点计算 | self.B |
| 平行线2与L2交点 | 直线交点计算 | self.E |
| 平行线3与L1交点 | 直线交点计算 | self.C |
| 平行线3与L2交点 | 直线交点计算 | self.F |

### 场景3：三角形推论
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 三角形顶点A | 固定点 | self.tri_A |
| 三角形顶点B | 固定点 | self.tri_B |
| 三角形顶点C | 固定点 | self.tri_C |
| 点D在AB上 | A + t*(B-A) | self.tri_D |
| 点E在AC上 | A + t*(C-A) | self.tri_E |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力 + 引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题："平行线有什么神奇性质?"
3. 三条平行线快闪

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.2s | 三条平行线依次创建 | `Create(line1), Create(line2), Create(line3)` |
| 2.5s | 等待 | `Wait(0.8)` |

### 清理
- FadeOut: hook_text, parallel_lines
- 保留: author_info

---

## Scene 2: 三条平行线截两条直线 (12-15秒)
**目的**: 展示基本定理 - l₁ ∥ l₂ ∥ l₃ → AB/BC = DE/EF

### 元素
1. 两条相交直线 L1, L2
2. 三条平行线 l₁, l₂, l₃
3. 交点标记 A, B, C, D, E, F
4. 线段标注 AB, BC, DE, EF
5. 比例公式

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 标题淡入 | `Write(title)` | "定理：三条平行线截两条直线" |
| 0.8s | 创建两条直线 | `Create(L1), Create(L2)` | 灰色，细线 |
| 1.6s | 创建平行线1 | `Create(l1)` | 绿色，加粗 |
| 2.1s | 标记交点 A, D | `FadeIn(dot_A), Write(label_A)` | |
| 2.8s | 创建平行线2 | `Create(l2)` | 绿色，加粗 |
| 3.3s | 标记交点 B, E | `FadeIn(dot_B), Write(label_E)` | |
| 4.0s | 创建平行线3 | `Create(l3)` | 绿色，加粗 |
| 4.5s | 标记交点 C, F | `FadeIn(dot_C), Write(label_F)` | |
| 5.2s | 高亮线段AB | `AB.set_color(YELLOW)` | 闪烁效果 |
| 5.8s | 高亮线段BC | `BC.set_color(YELLOW)` | |
| 6.4s | 高亮线段DE | `DE.set_color(YELLOW)` | |
| 7.0s | 高亮线段EF | `EF.set_color(YELLOW)` | |
| 7.8s | 显示比例公式 | `Write(formula)` | AB/BC = DE/EF |
| 9.5s | 等待理解 | `Wait(2.0)` | 关键停留 |

### 清理
- FadeOut: 全部元素
- 保留: 无

---

## Scene 3: 三角形推论 (15-18秒)
**目的**: 展示推论 - DE ∥ BC → AD/DB = AE/EC

### 元素
1. 三角形 ABC
2. 平行线 DE ∥ BC
3. 点 D 在 AB 上，点 E 在 AC 上
4. 线段标注
5. 比例公式

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 标题淡入 | `Write(title)` | "推论：三角形中的平行线" |
| 0.8s | 创建三角形ABC | `Create(triangle)` | |
| 1.5s | 标记顶点 | `Write(label_A), Write(label_B), Write(label_C)` | |
| 2.2s | 点D在AB上滑动 | `dot_D.animate.move_to(D_pos)` | 动态效果 |
| 2.8s | 点E在AC上滑动 | `dot_E.animate.move_to(E_pos)` | 同步运动 |
| 3.5s | 创建线段DE | `Create(line_DE)` | 虚线 |
| 4.2s | 标注平行符号 | `Write(parallel_mark)` | DE ∥ BC |
| 5.0s | 高亮 AD | `AD.set_color(YELLOW)` | |
| 5.5s | 高亮 DB | `DB.set_color(RED)` | |
| 6.0s | 高亮 AE | `AE.set_color(YELLOW)` | |
| 6.5s | 高亮 EC | `EC.set_color(RED)` | |
| 7.2s | 显示公式 | `Write(formula)` | AD/DB = AE/EC |
| 9.0s | 等待理解 | `Wait(2.0)` | 关键停留 |

### 清理
- FadeOut: 部分元素
- 保留: triangle (用于下一场景)

---

## Scene 4: 逆定理 (12-15秒)
**目的**: 展示逆定理 - AD/DB = AE/EC → DE ∥ BC

### 元素
1. 三角形 ABC (延续)
2. 比例条件
3. 平行线验证

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 标题淡入 | `Write(title)` | "逆定理：比例相等则平行" |
| 0.8s | 显示比例条件 | `Write(condition)` | "已知: AD/DB = AE/EC" |
| 1.8s | 创建线段DE | `Create(line_DE)` | 初始为普通线 |
| 2.5s | 验证平行 | `Flash(parallel_mark)` | 闪烁平行符号 |
| 3.2s | DE变为平行标记 | `line_DE.set_color(GREEN)` | |
| 4.0s | 显示结论 | `Write(conclusion)` | "∴ DE ∥ BC" |
| 5.5s | 等待理解 | `Wait(2.0)` | |

### 清理
- FadeOut: 全部元素
- 保留: 无

---

## Scene 5: 应用示例 (10-12秒)
**目的**: 实际应用计算

### 元素
1. 具体数值的三角形
2. 计算过程
3. 答案

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 标题淡入 | `Write(title)` | "例题：计算未知线段" |
| 0.8s | 创建带数值的图形 | `Create(triangle)` | AD=2, DB=3, AE=4 |
| 1.8s | 标注已知量 | `Write(known_values)` | |
| 2.8s | 列出比例式 | `Write(equation)` | AD/DB = AE/EC |
| 4.0s | 代入数值 | `Transform(equation, numeric_eq)` | 2/3 = 4/EC |
| 5.2s | 求解 | `Write(solution)` | EC = 6 |
| 6.5s | 标注答案 | `Flash(answer)` | |
| 8.0s | 等待 | `Wait(1.5)` | |

### 清理
- FadeOut: 全部元素
- 保留: 无

---

## Scene 6: 片尾关注 (8-10秒)
**目的**: 品牌强化 + 引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息放大 | `Transform(author, author_large)` |
| 0.8s | 关注文字淡入 | `FadeIn(follow_text)` |
| 1.5s | 平行线图标旋转 | `Rotate(icon, PI)` |
| 3.5s | 等待 | `Wait(2.0)` |
| 5.5s | 全部淡出 | `FadeOut(*)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 贯穿全片 |
| parallel_lines_demo | Scene 2 | Scene 2 | 基本定理演示 |
| triangle | Scene 3 | Scene 4 | 三角形推论 |
| example_triangle | Scene 5 | Scene 5 | 例题专用 |

## 关键验证点
1. **平行性验证**: 三条平行线必须真正平行（叉积为0）
2. **交点精确**: 所有交点必须用精确计算，不能臆想坐标
3. **比例验证**: 显示的比例必须数值正确
4. **边界检查**: 所有元素在安全区域内 (x∈[-4,4], y∈[-7,7])

## 特殊注意事项
1. 平行线的绘制：使用相同的方向向量确保真正平行
2. 交点计算：使用 GeometryCalculator.line_intersection()
3. 动态点的移动：确保始终在线段上（参数化表示）
4. 比例数值：需要在 verify_geometry() 中验证