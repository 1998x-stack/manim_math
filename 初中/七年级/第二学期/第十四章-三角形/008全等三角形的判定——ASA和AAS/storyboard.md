# 全等三角形判定（ASA 和 AAS）- 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等
- 目标受众: 七年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 第一个三角形
COLOR_SECONDARY = "#e74c3c"    # 红色 - 第二个三角形
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮强调
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_MATCH = GREEN            # 绿色 - 匹配成功
```

## 几何预计算清单

### 三角形 ABC（左侧）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点A | 基准点 | self.A1 = np.array([-3, 0, 0]) * SCALE + OFFSET |
| 顶点B | 固定边长 | self.B1 = self.A1 + np.array([2.5, 0, 0]) |
| 顶点C | 通过角度计算 | self.C1 = self.A1 + rotate_vector([2, 0, 0], angle_A) |
| 角A | 设定值 50° | self.angle_A1 = 50° |
| 角B | 设定值 60° | self.angle_B1 = 60° |
| 边AB | 固定长度 | self.AB1 = 2.5 * SCALE |

### 三角形 DEF（右侧）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点D | 基准点（右侧） | self.D1 = np.array([1, -1, 0]) * SCALE + OFFSET |
| 顶点E | 对应 AB 边长 | self.E1 = self.D1 + np.array([2.5, 0, 0]) |
| 顶点F | 通过角度匹配 | self.F1 = self.D1 + rotate_vector([2, 0, 0], angle_D) |

### 关键角度验证
- ∠A = ∠D = 50° （精确验证）
- ∠B = ∠E = 60° （精确验证）
- AB = DE（长度验证，误差 < 1e-6）

---

## Scene 1: 开场钩子 (0-4秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识（顶部）
2. 钩子问题："如何判断两个三角形全等？"
3. 两个看起来"差不多"的三角形

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_question, run_time=1.0)` |
| 1.3s | 两个三角形依次创建 | `Create(triangle1), Create(triangle2)` |
| 2.8s | 问号闪烁 | `Flash(question_mark)` |
| 3.5s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_question, question_mark
- 保留: triangle1, triangle2, author_info

---

## Scene 2: ASA 判定介绍 (4-18秒)
**目的**: 引入 ASA（角边角）判定定理

### 元素
1. 标题："ASA 判定法"
2. 定义文字："两角及其夹边分别对应相等"
3. 三角形 ABC 和 DEF
4. 标注：∠A、边AB、∠B

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 4.0s | 清除问号，标题写入 | `Write(title_asa)` |
| 4.7s | 定义文字淡入 | `FadeIn(definition_asa)` |
| 5.5s | 高亮∠A（左） | `angle_A.set_color(YELLOW), Flash(angle_A)` |
| 6.2s | 高亮∠D（右） | `angle_D.set_color(YELLOW), Flash(angle_D)` |
| 6.9s | 显示角度相等 | `Write(angle_equation: "∠A = ∠D = 50°")` |
| 8.0s | 高亮边AB（左） | `ab_line.set_stroke(YELLOW, 5)` |
| 8.7s | 高亮边DE（右） | `de_line.set_stroke(YELLOW, 5)` |
| 9.4s | 显示边长相等 | `Write(side_equation: "AB = DE")` |
| 10.5s | 高亮∠B（左） | `angle_B.set_color(YELLOW), Flash(angle_B)` |
| 11.2s | 高亮∠E（右） | `angle_E.set_color(YELLOW), Flash(angle_E)` |
| 11.9s | 显示角度相等 | `Write(angle_equation2: "∠B = ∠E = 60°")` |
| 13.0s | 关键词强调："夹边" | `Indicate(keyword_box)` |
| 14.0s | 等待理解 | `Wait(1.0)` |

### 几何验证点
- ∠A 的角弧方向：使用 `other_angle` 参数确保在正确侧
- AB 边的长度：精确 2.5 单位
- ∠B 的角弧位置：quadrant 参数正确设置

### 清理
- 保留: triangle1, triangle2, 所有标注
- 为下一步叠加做准备

---

## Scene 3: ASA 叠加验证 (18-28秒)
**目的**: 通过动画叠加证明全等

### 元素
1. 三角形 DEF 移动并旋转
2. 叠加动画
3. 全等符号："△ABC ≌ △DEF"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 18.0s | 提示文字："让我们叠加看看" | `FadeIn(hint_text)` |
| 19.0s | DEF 半透明化 | `triangle2.animate.set_fill_opacity(0.5)` |
| 19.5s | DEF 移动到 ABC | `triangle2.animate.move_to(triangle1)` |
| 21.0s | DEF 旋转对齐 | `triangle2.animate.rotate(angle)` |
| 22.5s | 完美重合闪光 | `Flash(overlap_group, color=GREEN)` |
| 23.5s | 全等符号书写 | `Write(congruence_symbol)` |
| 25.0s | 等待 | `Wait(1.5)` |

### 关键几何约束
- DEF 的移动目标：self.A1（精确坐标）
- 旋转角度：精确计算两三角形的方向差
- 验证：重合后所有顶点距离 < 1e-6

### 清理
- FadeOut: 叠加的 triangle2, hint_text, congruence_symbol
- 恢复: triangle1, triangle2 到原位置

---

## Scene 4: AAS 判定介绍 (28-42秒)
**目的**: 引入 AAS（角角边）判定定理

### 元素
1. 标题："AAS 判定法"
2. 定义文字："两角及其中一角的对边分别对应相等"
3. 新的三角形对（演示 AAS）
4. 标注：∠A、∠B、边BC

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 28.0s | 三角形淡出，标题切换 | `FadeOut(triangle1, triangle2), Write(title_aas)` |
| 29.0s | 新三角形淡入 | `FadeIn(triangle3, triangle4)` |
| 29.7s | 定义文字出现 | `FadeIn(definition_aas)` |
| 30.5s | 高亮∠A（左） | `angle_A2.set_color(YELLOW)` |
| 31.2s | 高亮∠D（右） | `angle_D2.set_color(YELLOW)` |
| 31.9s | 显示角度相等 | `Write("∠A = ∠D = 55°")` |
| 33.0s | 高亮∠B（左） | `angle_B2.set_color(YELLOW)` |
| 33.7s | 高亮∠E（右） | `angle_E2.set_color(YELLOW)` |
| 34.4s | 显示角度相等 | `Write("∠B = ∠E = 65°")` |
| 35.5s | 高亮边BC（左）- 对边 | `bc_line.set_stroke(YELLOW, 5)` |
| 36.2s | 高亮边EF（右）- 对边 | `ef_line.set_stroke(YELLOW, 5)` |
| 36.9s | 显示边长相等 | `Write("BC = EF")` |
| 38.0s | 关键词强调："对边" | `Indicate(keyword_box2)` |
| 39.5s | 等待理解 | `Wait(1.5)` |

### 几何验证点
- 边BC 是∠A 的对边（不是夹边）
- 所有角度精确计算
- 第三个角通过 180° - ∠A - ∠B 计算

### 清理
- 保留: triangle3, triangle4, 标注

---

## Scene 5: AAS 叠加验证 (42-52秒)
**目的**: 通过动画叠加证明 AAS 也能判定全等

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 42.0s | 提示文字："AAS 也能判定全等" | `FadeIn(hint_text2)` |
| 43.0s | triangle4 半透明化 | `triangle4.animate.set_fill_opacity(0.5)` |
| 43.5s | triangle4 移动并旋转 | `triangle4.animate.move_to(...).rotate(...)` |
| 45.5s | 完美重合闪光 | `Flash(overlap_group2, color=GREEN)` |
| 46.5s | 全等符号书写 | `Write("△ABC ≌ △DEF")` |
| 48.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有三角形和标注

---

## Scene 6: AAA 反例 (52-62秒)
**目的**: 强调 AAA 不能判定全等（只能判定相似）

### 元素
1. 警告标题："注意！AAA 不能判定全等"
2. 两个三角形：角度相同但大小不同
3. 相似符号："△ABC ∽ △DEF"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 52.0s | 警告标题闪烁 | `Write(warning_title, color=RED)` |
| 53.0s | 大三角形创建 | `Create(big_triangle)` |
| 54.0s | 小三角形创建 | `Create(small_triangle)` |
| 55.0s | 标注三个角相等 | `Write(angle_labels)` |
| 56.5s | 尝试叠加 - 失败 | `small_triangle.animate.move_to(...).scale(...)` |
| 58.0s | X 标记出现 | `Create(cross_mark, color=RED)` |
| 59.0s | 相似符号 | `Write("仅能判定相似 ∽")` |
| 60.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有元素

---

## Scene 7: 总结 + 片尾 (62-75秒)
**目的**: 总结要点，引导关注

### 元素
1. 总结卡片
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 62.0s | 总结标题 | `Write("全等三角形判定方法")` |
| 63.0s | ASA 卡片滑入 | `card1.animate.shift(RIGHT)` |
| 64.0s | AAS 卡片滑入 | `card2.animate.shift(RIGHT)` |
| 65.0s | AAA 警告卡片滑入 | `card3.animate.shift(RIGHT)` |
| 66.5s | 作者信息放大 | `author_info.animate.scale(1.5)` |
| 68.0s | 关注提示 | `FadeIn("关注我，学更多数学技巧!")` |
| 70.0s | 装饰动画 | `Rotate(decorations)` |
| 72.0s | 等待 | `Wait(2.0)` |
| 74.0s | 全部淡出 | `FadeOut(VGroup(*))` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| triangle1 (ABC) | Scene 1 | Scene 4 | ASA 演示用 |
| triangle2 (DEF) | Scene 1 | Scene 4 | ASA 演示用 |
| triangle3 (ABC2) | Scene 4 | Scene 6 | AAS 演示用 |
| triangle4 (DEF2) | Scene 4 | Scene 6 | AAS 演示用 |
| big_triangle | Scene 6 | Scene 6 | AAA 反例 |
| small_triangle | Scene 6 | Scene 6 | AAA 反例 |
| angle_arcs | 各场景 | 各场景 | 临时高亮 |
| labels | 各场景 | 各场景 | 临时标注 |

---

## 关键验证点清单

### 几何精度验证
- [ ] 所有角度误差 < 0.1°
- [ ] 所有边长误差 < 1e-6
- [ ] 角弧方向正确（使用 quadrant 和 other_angle）
- [ ] 叠加后顶点距离 < 1e-6

### 边界检查
- [ ] 所有元素 x ∈ [-4, 4]
- [ ] 所有元素 y ∈ [-7, 7]
- [ ] 标签无重叠

### 动画节奏
- [ ] 难点（夹边 vs 对边）停留 ≥ 2 秒
- [ ] 简单动画 ≤ 1 秒
- [ ] 总时长 60-75 秒

---

## 配色方案详细

```python
# 主三角形
TRIANGLE_1_COLOR = "#3498db"  # 蓝色
TRIANGLE_2_COLOR = "#e74c3c"  # 红色

# 角度标记
ANGLE_COLOR_DEFAULT = WHITE
ANGLE_COLOR_HIGHLIGHT = YELLOW
ANGLE_COLOR_MATCH = GREEN

# 边标记
EDGE_COLOR_DEFAULT = WHITE
EDGE_COLOR_HIGHLIGHT = YELLOW
EDGE_COLOR_MATCH = GREEN

# 文字
TEXT_COLOR_TITLE = GOLD
TEXT_COLOR_DEFINITION = GRAY_A
TEXT_COLOR_WARNING = RED
TEXT_COLOR_HINT = YELLOW

# 背景
BACKGROUND_COLOR = "#1a1a2e"
```

---

## 字体大小规范

```python
FONT_SIZES = {
    "title": 36,           # 场景标题
    "subtitle": 28,        # 定义文字
    "body": 22,            # 说明文字
    "label": 20,           # 顶点标签 (A, B, C)
    "equation": 24,        # 等式 (∠A = ∠D)
    "author": 20,          # 作者信息
    "warning": 32,         # 警告文字
}
```