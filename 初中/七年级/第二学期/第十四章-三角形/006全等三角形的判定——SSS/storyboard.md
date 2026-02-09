# SSS全等三角形判定 - 动画分镜脚本

## 元信息
- 目标时长: 60-75秒
- 场景数量: 8个
- 难度等级: 中等
- 知识点: 全等三角形的判定——SSS（边边边）

## 颜色配置
```python
COLOR_TRIANGLE_1 = BLUE          # 三角形ABC
COLOR_TRIANGLE_2 = RED           # 三角形DEF
COLOR_HIGHLIGHT = YELLOW         # 高亮显示
COLOR_EQUAL_MARK = GREEN         # 相等标记
COLOR_AUXILIARY = GRAY_B         # 辅助线/文字
COLOR_SUCCESS = GREEN            # 成功/全等标记
```

## 几何预计算清单

### 三角形ABC（左侧）
| 元素 | 计算公式 | 存储变量 | 值 |
|------|---------|---------|-----|
| 顶点A | 预设坐标 | self.A | [-3, 0, 0] * 0.8 + LEFT*1 + UP*1 |
| 顶点B | 预设坐标 | self.B | [-1, 0, 0] * 0.8 + LEFT*1 + UP*1 |
| 顶点C | 预设坐标 | self.C | [-2, 1.5, 0] * 0.8 + LEFT*1 + UP*1 |
| 边长AB | norm(B-A) | self.AB_length | 精确计算 |
| 边长BC | norm(C-B) | self.BC_length | 精确计算 |
| 边长CA | norm(A-C) | self.CA_length | 精确计算 |

### 三角形DEF（右侧）
| 元素 | 计算公式 | 存储变量 | 值 |
|------|---------|---------|-----|
| 顶点D | 基于AB长度精确构造 | self.D | [1, 0, 0] * 0.8 + RIGHT*1 + UP*1 |
| 顶点E | 基于AB长度精确构造 | self.E | D + AB_length * RIGHT |
| 顶点F | 基于BC、CA长度精确构造 | self.F | 两圆交点法计算 |

**关键**: 三角形DEF的顶点必须通过精确的几何计算得到，确保：
- DE = AB (第一对对应边)
- EF = BC (第二对对应边)  
- FD = CA (第三对对应边)

### 验证要求
```python
assert abs(DE_length - AB_length) < 1e-6
assert abs(EF_length - BC_length) < 1e-6
assert abs(FD_length - CA_length) < 1e-6
```

---

## Scene 1: 开场钩子 (0-4秒)

**目的**: 抓住注意力，提出问题

### 元素
1. 作者标识（顶部小字）
2. 钩子问题（大字，引人入胜）
3. 两个神秘的三角形轮廓（半透明）

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 补充提示文字 | `FadeIn(subtitle)` | 0.4s |
| 1.5s | 两个三角形轮廓淡入 | `FadeIn(triangle_ABC, triangle_DEF, fill_opacity=0.2)` | 0.8s |
| 2.3s | 三角形闪烁（吸引注意） | `Indicate(VGroup(triangle_ABC, triangle_DEF))` | 0.6s |
| 2.9s | 等待 | `Wait(1.1)` | 1.1s |

### 文案
- **钩子**: "两个三角形什么时候全等？"
- **副标题**: "只知道边长就够了！"

### 清理
- FadeOut: hook_text, subtitle
- 保留: author_info, triangle_ABC (降低透明度), triangle_DEF (降低透明度)

---

## Scene 2: 引入两个三角形 (4-10秒)

**目的**: 清晰展示两个三角形及其顶点标注

### 元素
1. 三角形ABC（蓝色，左侧）
2. 三角形DEF（红色，右侧）
3. 顶点标签（A, B, C, D, E, F）

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 4.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 4.5s | 三角形ABC绘制 | `Create(triangle_ABC)` | 1.0s |
| 5.5s | ABC顶点标签书写 | `Write(label_A, label_B, label_C)` | 0.6s |
| 6.1s | 三角形DEF绘制 | `Create(triangle_DEF)` | 1.0s |
| 7.1s | DEF顶点标签书写 | `Write(label_D, label_E, label_F)` | 0.6s |
| 7.7s | 说明文字 | `FadeIn(explain_text)` | 0.5s |
| 8.2s | 等待（让学生观察） | `Wait(1.8)` | 1.8s |

### 文案
- **标题**: "SSS判定法则"（顶部，y=5.5）
- **说明**: "三边分别相等 → 全等"（y=4.8）

### 清理
- FadeOut: explain_text, title
- 保留: triangle_ABC, triangle_DEF, 所有顶点标签

---

## Scene 3: 标注第一对边相等 AB=DE (10-16秒)

**目的**: 演示第一对对应边相等

### 元素
1. AB边高亮（黄色加粗）
2. DE边高亮（黄色加粗）
3. 边长标注（数字）
4. 等号标记（双刻度线）
5. 公式显示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 10.0s | 步骤提示 | `FadeIn(step_1_text)` | 0.4s |
| 10.4s | AB边变黄加粗 | `triangle_ABC.animate.set_color(YELLOW)` (仅AB边) | 0.5s |
| 10.9s | DE边变黄加粗 | `triangle_DEF.animate.set_color(YELLOW)` (仅DE边) | 0.5s |
| 11.4s | AB长度标注淡入 | `FadeIn(length_AB)` | 0.4s |
| 11.8s | DE长度标注淡入 | `FadeIn(length_DE)` | 0.4s |
| 12.2s | 等号标记绘制（AB上双刻度线） | `Create(equal_mark_AB)` | 0.3s |
| 12.5s | 等号标记绘制（DE上双刻度线） | `Create(equal_mark_DE)` | 0.3s |
| 12.8s | 公式显示 | `Write(formula_1: "AB = DE")` | 0.6s |
| 13.4s | 闪烁强调 | `Flash(formula_1)` | 0.4s |
| 13.8s | 等待 | `Wait(2.2)` | 2.2s |

### 几何计算
```python
# AB边中点用于放置等号标记
M_AB = (self.A + self.B) / 2
# DE边中点
M_DE = (self.D + self.E) / 2

# 等号标记（双刻度线）方向垂直于边
dir_AB = (self.B - self.A)
perp_AB = np.array([-dir_AB[1], dir_AB[0], 0]) / norm(dir_AB) * 0.15
```

### 文案
- **步骤提示**: "第一步：比较AB和DE"（y=-4）
- **公式**: "AB = DE"（y=-5）

### 清理
- AB、DE边恢复原色
- FadeOut: step_1_text
- 保留: equal_mark_AB, equal_mark_DE, formula_1（移至左侧汇总区）

---

## Scene 4: 标注第二对边相等 BC=EF (16-22秒)

**目的**: 演示第二对对应边相等

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 16.0s | 步骤提示 | `FadeIn(step_2_text)` | 0.4s |
| 16.4s | BC边变黄加粗 | `BC边高亮` | 0.5s |
| 16.9s | EF边变黄加粗 | `EF边高亮` | 0.5s |
| 17.4s | BC长度标注 | `FadeIn(length_BC)` | 0.4s |
| 17.8s | EF长度标注 | `FadeIn(length_EF)` | 0.4s |
| 18.2s | 等号标记（三刻度线） | `Create(equal_mark_BC, equal_mark_EF)` | 0.6s |
| 18.8s | 公式显示 | `Write(formula_2: "BC = EF")` | 0.6s |
| 19.4s | 闪烁强调 | `Flash(formula_2)` | 0.4s |
| 19.8s | 等待 | `Wait(2.2)` | 2.2s |

### 文案
- **步骤提示**: "第二步：比较BC和EF"
- **公式**: "BC = EF"

### 清理
- BC、EF边恢复原色
- FadeOut: step_2_text
- 保留: 所有等号标记，formula_2（移至汇总区）

---

## Scene 5: 标注第三对边相等 CA=FD (22-28秒)

**目的**: 演示第三对对应边相等

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 22.0s | 步骤提示 | `FadeIn(step_3_text)` | 0.4s |
| 22.4s | CA边变黄加粗 | `CA边高亮` | 0.5s |
| 22.9s | FD边变黄加粗 | `FD边高亮` | 0.5s |
| 23.4s | CA长度标注 | `FadeIn(length_CA)` | 0.4s |
| 23.8s | FD长度标注 | `FadeIn(length_FD)` | 0.4s |
| 24.2s | 等号标记（单刻度线） | `Create(equal_mark_CA, equal_mark_FD)` | 0.6s |
| 24.8s | 公式显示 | `Write(formula_3: "CA = FD")` | 0.6s |
| 25.4s | 闪烁强调 | `Flash(formula_3)` | 0.4s |
| 25.8s | 等待 | `Wait(2.2)` | 2.2s |

### 文案
- **步骤提示**: "第三步：比较CA和FD"
- **公式**: "CA = FD"

### 清理
- CA、FD边恢复原色
- FadeOut: step_3_text
- 保留: 所有等号标记，formula_3（移至汇总区）

---

## Scene 6: 演示全等（重合动画） (28-38秒)

**目的**: 视觉化展示两个三角形全等

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 28.0s | 提示文字 | `FadeIn(congruence_hint)` | 0.5s |
| 28.5s | 等号标记全部闪烁 | `Indicate(all_equal_marks)` | 0.6s |
| 29.1s | 三角形DEF复制为半透明 | `triangle_DEF_copy = triangle_DEF.copy().set_opacity(0.5)` | 0.3s |
| 29.4s | DEF移动到ABC上方 | `triangle_DEF_copy.animate.move_to(ABC位置).rotate(旋转角度)` | 2.0s |
| 31.4s | DEF完全重合ABC | `triangle_DEF_copy.animate.set_color(GREEN).set_opacity(1)` | 0.8s |
| 32.2s | 全等符号闪现 | `Write(congruence_symbol: "≌")` | 0.6s |
| 32.8s | 完整公式显示 | `Write(final_formula)` | 1.0s |
| 33.8s | 庆祝动画（闪光） | `Flash(VGroup(triangles), color=GREEN)` | 0.8s |
| 34.6s | 等待 | `Wait(3.4)` | 3.4s |

### 几何计算（重合变换）
```python
# 计算旋转角度和平移向量，使DEF重合到ABC
# 需要精确计算使D对应A，E对应B，F对应C
rotation_angle = 计算从DE到AB的旋转角
translation = self.A - self.D（旋转后）
```

### 文案
- **提示**: "三边相等，两个三角形..."（y=-4）
- **完整公式**: "△ABC ≌ △DEF (SSS)"（y=-5.5，大字，绿色）

### 清理
- FadeOut: triangle_DEF_copy, congruence_hint
- 保留: triangle_ABC, triangle_DEF（原位置），final_formula

---

## Scene 7: 总结SSS判定法则 (38-50秒)

**目的**: 强化记忆，归纳要点

### 元素
1. 三角形缩小移至顶部
2. SSS法则卡片
3. 记忆口诀
4. 关键要点列表

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 38.0s | 清理屏幕 | `FadeOut(所有标记和标签)` | 0.6s |
| 38.6s | 三角形缩小移至顶部 | `triangles.animate.scale(0.5).move_to(UP*5)` | 1.0s |
| 39.6s | 法则标题卡片 | `FadeIn(sss_title_card)` | 0.5s |
| 40.1s | 定义文字 | `Write(definition)` | 1.2s |
| 41.3s | 口诀卡片滑入 | `口诀.animate.shift(LEFT*10 to ORIGIN)` | 0.8s |
| 42.1s | 要点1淡入 | `FadeIn(point_1)` | 0.5s |
| 42.6s | 要点2淡入 | `FadeIn(point_2)` | 0.5s |
| 43.1s | 要点3淡入 | `FadeIn(point_3)` | 0.5s |
| 43.6s | 强调框出现 | `Create(emphasis_box)` | 0.6s |
| 44.2s | 等待（记忆时间） | `Wait(5.8)` | 5.8s |

### 文案
- **标题**: "SSS判定法则"（y=3，金色，大字）
- **定义**: "三边分别对应相等的两个三角形全等"（y=1.5）
- **口诀**: "边边边，三边等，全等定！"（y=0，黄色高亮）
- **要点1**: "✓ 只需证明三对边相等"（y=-1.5）
- **要点2**: "✓ 不需要证明角的关系"（y=-2.5）
- **要点3**: "✓ 注意对应关系要正确"（y=-3.5）

### 清理
- 准备淡出所有内容
- 保留: author_info

---

## Scene 8: 片尾关注 (50-60秒)

**目的**: 引导关注，加深品牌印象

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 50.0s | 清空屏幕 | `FadeOut(VGroup(所有元素))` | 0.8s |
| 50.8s | 作者名放大居中 | `author_name.animate.scale(1.5).move_to(UP*1.5)` | 0.8s |
| 51.6s | 账号ID显示 | `FadeIn(author_id)` | 0.5s |
| 52.1s | 关注文字滑入 | `FadeIn(follow_text, shift=UP*0.3)` | 0.6s |
| 52.7s | 三角形图标旋转装饰 | `Rotate(decoration_triangles)` | 1.5s |
| 54.2s | SSS图标闪烁 | `Flash(sss_icons)` | 0.8s |
| 55.0s | 结束语 | `Write(outro_text)` | 1.0s |
| 56.0s | 最终等待 | `Wait(4.0)` | 4.0s |

### 文案
- **作者名**: "上海初高中数学直通车"（白色，40号字）
- **账号**: "@emptyandcalm"（灰色，32号字）
- **关注文字**: "关注我，掌握更多全等判定方法！"（黄色，30号字）
- **结束语**: "SAS、ASA、AAS...下期见！"（灰色，24号字）

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8（保留到最后） | 顶部作者信息 |
| triangle_ABC | Scene 1 | Scene 7 | 蓝色三角形 |
| triangle_DEF | Scene 1 | Scene 7 | 红色三角形 |
| labels (A-F) | Scene 2 | Scene 6 | 顶点标签 |
| equal_mark_AB, equal_mark_DE | Scene 3 | Scene 7 | 双刻度线 |
| equal_mark_BC, equal_mark_EF | Scene 4 | Scene 7 | 三刻度线 |
| equal_mark_CA, equal_mark_FD | Scene 5 | Scene 7 | 单刻度线 |
| formula_1 (AB=DE) | Scene 3 | Scene 7 | 移至汇总区 |
| formula_2 (BC=EF) | Scene 4 | Scene 7 | 移至汇总区 |
| formula_3 (CA=FD) | Scene 5 | Scene 7 | 移至汇总区 |
| final_formula | Scene 6 | Scene 7 | 全等公式 |
| sss_title_card | Scene 7 | Scene 8 | 法则卡片 |
| decoration_triangles | Scene 8 | Scene 8（最后） | 装饰图标 |

---

## 技术要点

### 1. 精确几何计算
**三角形DEF的构造必须通过数学计算**：
```python
# 方法：两圆交点法
# 已知：D点位置，DE长度（=AB长度），EF长度（=BC长度），FD长度（=CA长度）
# 求：F点位置

# 以D为圆心，半径=CA_length的圆
# 以E为圆心，半径=BC_length的圆
# 两圆交点即为F

circle1_center = D
circle1_radius = CA_length

circle2_center = E  
circle2_radius = BC_length

# 解两圆交点方程
F = calculate_circle_intersection(D, CA_length, E, BC_length)
```

### 2. 等号标记设计
- AB=DE: 双刻度线（| |）
- BC=EF: 三刻度线（| | |）
- CA=FD: 单刻度线（|）

位置：放置在边的中点，方向垂直于边

### 3. 重合动画关键
```python
# 计算从DEF到ABC的变换
# 1. 平移：使D对准A
# 2. 旋转：使DE对准AB
# 3. 可能需要翻转（镜像）

def calculate_congruence_transform():
    # 平移向量
    translation = A - D
    
    # 旋转角度
    vec_DE = E - D
    vec_AB = B - A
    angle = np.arctan2(vec_AB[1], vec_AB[0]) - np.arctan2(vec_DE[1], vec_DE[0])
    
    return translation, angle
```

---

## 验证清单

### 几何验证
- [ ] AB长度 = DE长度（误差 < 1e-6）
- [ ] BC长度 = EF长度（误差 < 1e-6）
- [ ] CA长度 = FD长度（误差 < 1e-6）
- [ ] 三角形ABC内角和 = 180°
- [ ] 三角形DEF内角和 = 180°
- [ ] 等号标记位于边的精确中点
- [ ] 等号标记方向垂直于边

### 动画验证
- [ ] 所有元素在边界内（x∈[-4,4], y∈[-7,7]）
- [ ] 文字无重叠
- [ ] 节奏流畅，难点有足够停留
- [ ] 总时长 60-75秒
- [ ] 开头有钩子，结尾有作者信息

### 内容验证
- [ ] 数学概念准确
- [ ] 符号使用规范（≌ 表示全等）
- [ ] 对应关系清晰（AB对应DE等）
- [ ] 口诀易记

---

## 备注

1. **颜色一致性**: 三角形ABC始终蓝色，DEF始终红色，除非特殊高亮
2. **字体使用**: 所有中文使用 "Noto Sans CJK SC"，LaTeX公式使用MathTex
3. **音效建议**（后期添加）：
   - 边高亮时：轻快"叮"声
   - 等号标记出现：确认"咔"声
   - 重合完成：成功"叮铃"声
   - 公式显示：书写"沙沙"声

4. **易错点提醒**:
   - 确保三角形DEF是精确计算构造的，不是臆想坐标
   - 重合动画可能需要镜像翻转（如果两三角形手性不同）
   - 等号标记数量要与常规标注一致（避免混淆）