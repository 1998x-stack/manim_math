# 轴对称（翻折）教学动画 - 分镜脚本

<!-- /root/code/sss/media/videos/axial_symmetry/1920p60/AxialSymmetry.mp4 -->

## 元信息
- 目标时长: 60-75秒
- 场景数量: 7个
- 难度等级: 七年级
- 知识点: 轴对称的定义、性质和应用

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 原图形
COLOR_SYMMETRIC = "#e74c3c"      # 红色 - 对称图形
COLOR_AXIS = "#f39c12"           # 橙色 - 对称轴
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_CONNECTING = "#9b59b6"     # 紫色 - 连接线
```

## 几何预计算清单

### 主要图形 (三角形示例)
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点A | 基准点 | self.A = [-2, 1, 0] |
| 顶点B | 基准点 | self.B = [-1, -1.5, 0] |
| 顶点C | 基准点 | self.C = [-3, -1, 0] |
| 对称轴 | y轴 | self.axis_start, self.axis_end |
| A的对称点A' | 关于y轴对称 | self.A_prime = [2, 1, 0] |
| B的对称点B' | 关于y轴对称 | self.B_prime = [1, -1.5, 0] |
| C的对称点C' | 关于y轴对称 | self.C_prime = [3, -1, 0] |
| 垂足M_A | A到对称轴的垂足 | self.M_A = [0, 1, 0] |
| 垂足M_B | B到对称轴的垂足 | self.M_B = [0, -1.5, 0] |
| 垂足M_C | C到对称轴的垂足 | self.M_C = [0, -1, 0] |

### 验证点
- AM = MA' (对称性)
- 连线AA'垂直于对称轴
- M是AA'的中点

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力，引出轴对称的日常应用

### 元素
1. 作者标识（顶部）
2. 钩子问题："蝴蝶为什么这么美？"
3. 蝴蝶图形（简化版，左右对称）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_text)` |
| 1.0s | 蝴蝶左半边创建 | `Create(butterfly_left)` |
| 1.8s | 对称轴闪烁 | `Flash(axis)` |
| 2.3s | 蝴蝶右半边镜像出现 | `Create(butterfly_right)` |
| 3.5s | 提示文字："秘密在于轴对称!" | `FadeIn(hint_text)` |
| 4.5s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_text, butterfly, hint_text
- 保留: author_info

---

## Scene 2: 定义讲解 (5-12秒)
**目的**: 介绍轴对称的定义

### 元素
1. 标题："什么是轴对称？"
2. 定义文字
3. 简单图形（三角形）
4. 对称轴（虚线）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 5.0s | 标题淡入 | `FadeIn(title)` |
| 5.5s | 定义文字书写 | `Write(definition)` |
| 6.5s | 三角形创建 | `Create(triangle)` |
| 7.5s | 对称轴绘制 | `Create(axis)` |
| 8.5s | 说明："沿对称轴对折" | `FadeIn(fold_text)` |
| 9.0s | 三角形折叠动画 | `Rotate(triangle, PI, axis=RIGHT)` |
| 10.5s | 说明："能完全重合" | `FadeIn(overlap_text)` |
| 11.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, definition, fold_text, overlap_text
- 保留: triangle, axis

---

## Scene 3: 性质1 - 对应点连线垂直于对称轴 (12-22秒)
**目的**: 展示第一个性质

### 元素
1. 标题："性质1：垂直关系"
2. 原三角形ABC
3. 对称三角形A'B'C'
4. 连接线AA', BB', CC'
5. 垂直标记

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 12.0s | 标题淡入 | `FadeIn(property1_title)` |
| 12.5s | 对称三角形创建 | `Create(triangle_prime)` |
| 13.5s | 标注顶点A, A' | `FadeIn(labels)` |
| 14.0s | 绘制连接线AA' | `Create(line_AA)` |
| 14.8s | 高亮垂直关系 | `Flash(perpendicular_mark)` |
| 15.5s | 公式："AA' ⊥ 对称轴" | `Write(formula1)` |
| 16.5s | 依次绘制BB', CC' | `Create(line_BB), Create(line_CC)` |
| 17.5s | 说明："所有对应点连线都垂直于对称轴" | `FadeIn(explanation)` |
| 19.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: property1_title, formula1, explanation
- 保留: triangle, triangle_prime, axis, connecting_lines

---

## Scene 4: 性质2 - 对称轴平分对应点连线 (22-32秒)
**目的**: 展示第二个性质

### 元素
1. 标题："性质2：平分关系"
2. 中点M标记
3. 距离标注（AM = MA'）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 22.0s | 标题淡入 | `FadeIn(property2_title)` |
| 22.5s | 标记中点M | `FadeIn(midpoint_M)` |
| 23.5s | 高亮AM段 | `line_AM.animate.set_color(YELLOW)` |
| 24.5s | 高亮MA'段 | `line_MA.animate.set_color(YELLOW)` |
| 25.5s | 标注距离相等 | `Write(distance_labels)` |
| 26.5s | 公式："M是AA'的中点" | `Write(formula2)` |
| 27.5s | 说明："对称轴平分连线" | `FadeIn(explanation2)` |
| 29.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: property2_title, formula2, explanation2, distance_labels
- 保留: triangle, triangle_prime, axis, midpoint_M

---

## Scene 5: 性质3 - 对应线段和角相等 (32-42秒)
**目的**: 展示第三个性质

### 元素
1. 标题："性质3：全等性质"
2. 边长标注
3. 角度标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 32.0s | 标题淡入 | `FadeIn(property3_title)` |
| 32.5s | 标注对应边AB和A'B' | `FadeIn(side_labels)` |
| 33.5s | 显示边长相等 | `Write(equal_sides)` |
| 34.5s | 标注对应角∠A和∠A' | `Create(angle_marks)` |
| 35.5s | 显示角度相等 | `Write(equal_angles)` |
| 36.5s | 公式："对应线段相等，对应角相等" | `Write(formula3)` |
| 38.0s | 说明："轴对称是全等变换" | `FadeIn(explanation3)` |
| 40.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: property3_title, formula3, explanation3, labels
- 保留: triangle, triangle_prime, axis

---

## Scene 6: 实际应用示例 (42-55秒)
**目的**: 展示轴对称的实际应用

### 元素
1. 标题："轴对称在生活中"
2. 三个示例图形：
   - 汉字"中"（上下对称）
   - 正方形（四条对称轴）
   - 字母"A"（左右对称）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 42.0s | 清空主区域 | `FadeOut(triangle, triangle_prime)` |
| 42.5s | 标题淡入 | `FadeIn(application_title)` |
| 43.0s | 示例1：汉字"中" | `Create(chinese_char)` |
| 44.0s | 显示对称轴 | `Create(axis_horizontal)` |
| 45.0s | 示例2：正方形 | `Create(square)` |
| 46.0s | 显示四条对称轴 | `Create(four_axes)` |
| 47.5s | 示例3：字母A | `Create(letter_A)` |
| 48.5s | 显示对称轴 | `Create(axis_vertical)` |
| 50.0s | 提示："生活中处处有对称!" | `FadeIn(life_hint)` |
| 52.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: all examples
- 保留: author_info

---

## Scene 7: 总结和片尾 (55-75秒)
**目的**: 总结知识点，引导关注

### 元素
1. 三条性质总结卡片
2. 关键公式
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 55.0s | 总结标题 | `Write(summary_title)` |
| 56.0s | 性质1卡片滑入 | `card1.animate.shift(RIGHT*0)` |
| 57.0s | 性质2卡片滑入 | `card2.animate.shift(RIGHT*0)` |
| 58.0s | 性质3卡片滑入 | `card3.animate.shift(RIGHT*0)` |
| 59.0s | 关键提示："掌握轴对称，解题更轻松!" | `FadeIn(key_tip)` |
| 61.0s | 作者信息放大 | `author_info.animate.scale(1.5)` |
| 62.0s | 关注文字 | `FadeIn(follow_text)` |
| 63.0s | 装饰动画（对称图形旋转） | `Rotate(decoration)` |
| 66.0s | 等待 | `Wait(2.0)` |
| 68.0s | 全部淡出 | `self.play(*[FadeOut(m) for m in self.mobjects])` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| triangle | Scene 2 | Scene 6 | 主三角形 |
| triangle_prime | Scene 3 | Scene 6 | 对称三角形 |
| axis | Scene 2 | Scene 6 | 对称轴 |
| connecting_lines | Scene 3 | Scene 5 | 连接线AA'等 |
| midpoint_M | Scene 4 | Scene 5 | 中点标记 |
| butterfly | Scene 1 | Scene 1 | 开场示例 |
| examples | Scene 6 | Scene 6 | 生活应用示例 |
| summary_cards | Scene 7 | Scene 7 | 总结卡片 |

---

## 技术要点备注

### 1. 对称变换的精确实现
```python
def reflect_point(point, axis_point, axis_direction):
    """计算点关于直线的对称点"""
    # 1. 计算垂足
    foot = calculate_foot(point, axis_point, axis_point + axis_direction)
    # 2. 对称点 = 2*垂足 - 原点
    return 2 * foot - point
```

### 2. 折叠动画
- 使用 `Rotate` + `axis` 参数模拟折叠
- 或使用 `Transform` 直接变换到对称位置

### 3. 垂直标记
```python
def create_perpendicular_mark(intersection, direction1, direction2, size=0.15):
    """创建垂直符号（小正方形）"""
    v1 = direction1 / np.linalg.norm(direction1) * size
    v2 = direction2 / np.linalg.norm(direction2) * size
    return Polygon(
        intersection,
        intersection + v1,
        intersection + v1 + v2,
        intersection + v2,
        stroke_width=1.5,
        color=YELLOW
    )
```

### 4. 中点标记
- 使用小圆点 + 标签
- 通过 `(P1 + P2) / 2` 精确计算

### 5. 汉字显示
```python
Text("中", font="Noto Sans CJK SC", font_size=60)
```

---

## 时长分配总结
- Scene 1 (开场): 5秒
- Scene 2 (定义): 7秒
- Scene 3 (性质1): 10秒
- Scene 4 (性质2): 10秒
- Scene 5 (性质3): 10秒
- Scene 6 (应用): 13秒
- Scene 7 (总结): 20秒
- **总计**: 75秒

---

## 难点提示
1. **对称变换的数学实现** - 需要精确计算垂足和对称点
2. **折叠动画** - 使用3D旋转或Transform实现
3. **中文字符** - 必须使用Text类，不能用MathTex
4. **垂直标记** - 使用小正方形，不是简单的角度弧
5. **边界控制** - 确保所有图形在竖屏范围内（x∈[-4,4], y∈[-7,7]）