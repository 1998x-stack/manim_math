# 二次函数 y=a(x-h)²+k 的图像与性质 - 动画分镜脚本

## 元信息
- 目标时长: 60-75秒
- 场景数量: 7个
- 难度等级: 中等
- 主题: 顶点式二次函数的图像与性质

## 颜色配置
```python
COLOR_PARABOLA_POSITIVE = "#3498db"  # 蓝色 - a>0的抛物线
COLOR_PARABOLA_NEGATIVE = "#e74c3c"  # 红色 - a<0的抛物线
COLOR_VERTEX = "#f39c12"             # 橙色 - 顶点
COLOR_AXIS = "#2ecc71"               # 绿色 - 对称轴
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
```

## 几何预计算清单

### 坐标系设置
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 坐标系原点 | UP * 1.5 | self.axes_center |
| x轴范围 | [-4, 4] | x_range |
| y轴范围 | [-3, 5] | y_range |

### 抛物线参数 (a>0)
| 元素 | 数值 | 存储变量 |
|------|------|---------|
| a值 | 0.5 | self.a_positive |
| h值 (顶点x坐标) | 1 | self.h |
| k值 (顶点y坐标) | -2 | self.k |
| 顶点坐标 | (1, -2) | self.vertex |
| 对称轴方程 | x = 1 | self.axis_x |

### 抛物线参数 (a<0)
| 元素 | 数值 | 存储变量 |
|------|------|---------|
| a值 | -0.4 | self.a_negative |
| h值 | -1 | self.h2 |
| k值 | 2 | self.k2 |
| 顶点坐标 | (-1, 2) | self.vertex2 |

---

## Scene 1: 开场钩子 (0-4秒)

**目的**: 吸引注意力，引出顶点式

### 元素
1. 作者信息 (顶部)
2. 钩子问题文字
3. 通用二次函数公式

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入顶部 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook)` | 0.8s |
| 1.1s | 一般式公式出现 | `Write(general_form)` | 0.8s |
| 1.9s | 箭头指向 | `GrowArrow(arrow)` | 0.4s |
| 2.3s | 顶点式公式出现 | `Write(vertex_form)` | 1.0s |
| 3.3s | 高亮顶点式 | `Indicate(vertex_form)` | 0.6s |

### 文案内容
- 钩子: "如何一眼看出抛物线的顶点?"
- 一般式: y = ax² + bx + c
- 顶点式: y = a(x-h)² + k

### 清理
- FadeOut: hook, general_form, arrow
- 保留: author_info
- 移动: vertex_form → 顶部

---

## Scene 2: 建立坐标系和基本抛物线 (4-12秒)

**目的**: 建立坐标系，绘制第一条抛物线 (a>0)

### 元素
1. 坐标系 (带刻度)
2. 抛物线 y = 0.5(x-1)² - 2
3. 顶点点
4. 顶点坐标标签

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 4.0s | 坐标系创建 | `Create(axes)` | 1.2s |
| 5.2s | 抛物线从左到右绘制 | `Create(parabola)` | 1.5s |
| 6.7s | 顶点点闪烁出现 | `FadeIn(vertex_dot, scale=0.5)` + `Flash` | 0.6s |
| 7.3s | 顶点坐标标签淡入 | `FadeIn(vertex_label)` | 0.5s |
| 7.8s | 函数表达式出现 | `Write(function_eq)` | 0.8s |
| 8.6s | 理解停顿 | `Wait` | 1.0s |

### 几何精确计算
```python
# 顶点坐标 (坐标系中的实际位置)
self.vertex = self.axes.c2p(self.h, self.k)  # c2p = coords to point

# 抛物线函数
def parabola_func(x):
    return self.a_positive * (x - self.h)**2 + self.k

# 绘制范围: x ∈ [-3, 5] 确保能看到完整形状
```

### 清理
- 保留: axes, parabola, vertex_dot, vertex_label

---

## Scene 3: 标注顶点坐标 (12-18秒)

**目的**: 强调顶点 (h, k) 与公式的对应关系

### 元素
1. 顶点公式提示框
2. h和k的指示箭头
3. 括号高亮

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 12.0s | 提示框出现 | `FadeIn(hint_box, shift=UP*0.3)` | 0.5s |
| 12.5s | 公式中h高亮 | `Indicate(h_part)` | 0.6s |
| 13.1s | 箭头指向顶点x坐标 | `GrowArrow(h_arrow)` | 0.4s |
| 13.5s | h值标签出现 | `Write(h_label)` | 0.4s |
| 13.9s | 公式中k高亮 | `Indicate(k_part)` | 0.6s |
| 14.5s | 箭头指向顶点y坐标 | `GrowArrow(k_arrow)` | 0.4s |
| 14.9s | k值标签出现 | `Write(k_label)` | 0.4s |
| 15.3s | 整体顶点公式高亮 | `Flash(vertex_formula)` | 0.5s |
| 15.8s | 理解停顿 | `Wait` | 2.0s |

### 文案内容
- 提示框: "顶点坐标: (h, k)"
- 注意: h前面有负号!

### 清理
- FadeOut: hint_box, h_arrow, k_arrow, h_label, k_label
- 保留: axes, parabola, vertex_dot, vertex_label

---

## Scene 4: 对称轴 (18-25秒)

**目的**: 展示对称轴是直线 x = h

### 元素
1. 对称轴虚线
2. 对称轴方程标签
3. 对称性演示（左右对称点）

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 18.0s | 对称轴虚线创建 | `Create(axis_line)` | 0.8s |
| 18.8s | 对称轴方程出现 | `Write(axis_eq)` | 0.6s |
| 19.4s | 说明文字淡入 | `FadeIn(symmetry_text)` | 0.4s |
| 19.8s | 在抛物线上标记对称点对 | `FadeIn(point_left), FadeIn(point_right)` | 0.5s |
| 20.3s | 连线显示等距 | `Create(distance_lines)` | 0.6s |
| 20.9s | 等距标记 | `FadeIn(equal_marks)` | 0.4s |
| 21.3s | 理解停顿 | `Wait` | 1.5s |

### 几何精确计算
```python
# 对称轴: x = h = 1
axis_x_coord = self.h
axis_bottom = self.axes.c2p(axis_x_coord, -3)
axis_top = self.axes.c2p(axis_x_coord, 5)
axis_line = DashedLine(axis_bottom, axis_top, color=COLOR_AXIS)

# 对称点对示例: 在 y = 0 的高度
test_y = 0
# 解方程: 0.5(x-1)² - 2 = 0 → (x-1)² = 4 → x-1 = ±2 → x = 3 或 x = -1
x1 = self.h + 2  # = 3
x2 = self.h - 2  # = -1
point_left = self.axes.c2p(x2, test_y)
point_right = self.axes.c2p(x1, test_y)
```

### 清理
- FadeOut: point_left, point_right, distance_lines, equal_marks, symmetry_text
- 保留: axes, parabola, vertex_dot, vertex_label, axis_line, axis_eq

---

## Scene 5: a>0时的性质 (25-35秒)

**目的**: 展示开口向上，最小值

### 元素
1. a>0标注
2. 开口方向箭头
3. 最小值标注
4. 增减性区间标注

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 25.0s | a>0文字出现 | `Write(a_positive_text)` | 0.5s |
| 25.5s | 开口向上箭头 | `GrowArrow(upward_arrows)` | 0.6s |
| 26.1s | 最小值标注出现 | `FadeIn(min_value_box)` | 0.7s |
| 26.8s | 最小值高亮 | `Indicate(vertex_dot)` | 0.6s |
| 27.4s | 说明文字 | `FadeIn(property_text)` | 0.5s |
| 27.9s | 增减性区间标注 | `Create(decrease_region), Create(increase_region)` | 1.0s |
| 28.9s | 理解停顿 | `Wait` | 2.0s |

### 文案内容
- "当 a > 0 时:"
- "开口向上"
- "最小值 = k (在 x = h 处)"
- "x < h 时递减, x > h 时递增"

### 清理
- FadeOut: upward_arrows, min_value_box, property_text, decrease_region, increase_region, a_positive_text
- 保留: axes, parabola, vertex_dot, vertex_label, axis_line

---

## Scene 6: a<0时的对比 (35-50秒)

**目的**: 对比展示 a<0 的情况

### 元素
1. 新的抛物线 y = -0.4(x+1)² + 2 (a<0)
2. 新顶点
3. a<0标注
4. 最大值标注

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 35.0s | 原抛物线淡化 | `parabola.animate.set_opacity(0.3)` | 0.5s |
| 35.5s | 新抛物线绘制 | `Create(parabola2)` | 1.5s |
| 37.0s | 新顶点出现 | `FadeIn(vertex_dot2, scale=0.5)` + `Flash` | 0.6s |
| 37.6s | 新顶点坐标 | `FadeIn(vertex_label2)` | 0.5s |
| 38.1s | 新对称轴 | `Create(axis_line2)` | 0.8s |
| 38.9s | a<0文字 | `Write(a_negative_text)` | 0.5s |
| 39.4s | 开口向下箭头 | `GrowArrow(downward_arrows)` | 0.6s |
| 40.0s | 最大值标注 | `FadeIn(max_value_box)` | 0.7s |
| 40.7s | 最大值高亮 | `Indicate(vertex_dot2)` | 0.6s |
| 41.3s | 对比说明文字 | `FadeIn(comparison_text)` | 0.6s |
| 41.9s | 理解停顿 | `Wait` | 2.0s |

### 几何精确计算
```python
# 第二条抛物线参数
self.a_negative = -0.4
self.h2 = -1
self.k2 = 2
self.vertex2 = self.axes.c2p(self.h2, self.k2)

def parabola_func2(x):
    return self.a_negative * (x - self.h2)**2 + self.k2
```

### 文案内容
- "当 a < 0 时:"
- "开口向下"
- "最大值 = k (在 x = h 处)"

### 清理
- FadeOut: parabola2, vertex_dot2, vertex_label2, axis_line2, downward_arrows, max_value_box, comparison_text, a_negative_text
- 恢复: parabola (opacity=1)

---

## Scene 7: 总结与片尾 (50-65秒)

**目的**: 总结要点，强化记忆

### 元素
1. 关键公式汇总卡片
2. 性质对比表
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 50.0s | 清空场景 | `FadeOut(所有元素)` | 0.6s |
| 50.6s | 总结标题 | `Write(summary_title)` | 0.7s |
| 51.3s | 顶点式公式卡片 | `FadeIn(card1, shift=UP*0.3)` | 0.5s |
| 51.8s | 顶点坐标卡片 | `FadeIn(card2, shift=UP*0.3)` | 0.5s |
| 52.3s | 对称轴卡片 | `FadeIn(card3, shift=UP*0.3)` | 0.5s |
| 52.8s | a>0性质卡片 | `FadeIn(card4, shift=UP*0.3)` | 0.5s |
| 53.3s | a<0性质卡片 | `FadeIn(card5, shift=UP*0.3)` | 0.5s |
| 53.8s | 关键提示高亮 | `Indicate(key_reminder)` | 0.6s |
| 54.4s | 理解停顿 | `Wait` | 1.5s |
| 55.9s | 作者信息放大 | `Transform(author_info, author_large)` | 0.8s |
| 56.7s | 关注文字 | `FadeIn(follow_text, shift=UP*0.3)` | 0.6s |
| 57.3s | 装饰动画 | `Rotate(decoration)` | 1.5s |
| 58.8s | 最终停留 | `Wait` | 2.0s |

### 卡片内容
1. 公式: y = a(x-h)² + k
2. 顶点: (h, k)
3. 对称轴: x = h
4. a > 0: 开口向上, 最小值k
5. a < 0: 开口向下, 最大值k

### 文案内容
- 总结标题: "顶点式 - 一眼看透抛物线!"
- 关键提示: "记住: h前有负号!"
- 关注文字: "关注我, 学更多函数技巧!"

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 (transform) | 顶部常驻 |
| axes | Scene 2 | Scene 7 | 主坐标系 |
| parabola | Scene 2 | Scene 7 | 第一条抛物线 (a>0) |
| vertex_dot | Scene 2 | Scene 7 | 顶点标记 |
| vertex_label | Scene 2 | Scene 7 | 顶点坐标 |
| axis_line | Scene 4 | Scene 7 | 对称轴 |
| axis_eq | Scene 4 | Scene 7 | 对称轴方程 |
| parabola2 | Scene 6 | Scene 6 | 第二条抛物线 (a<0, 临时) |
| vertex_dot2 | Scene 6 | Scene 6 | 第二个顶点 (临时) |

---

## 验证清单

### 几何验证
- [x] 顶点坐标使用 axes.c2p() 计算
- [x] 抛物线函数使用精确数学公式
- [x] 对称轴位置 = 顶点x坐标
- [x] 对称点计算基于方程求解

### 边界检查
- [x] 坐标系范围: x∈[-4,4], y∈[-3,5]
- [x] 所有元素在可见范围内
- [x] 文字标签不重叠

### 动画节奏
- [x] 关键步骤停留 2秒
- [x] 简单动画 0.4-0.8秒
- [x] 总时长控制在 65秒内

### 字体与样式
- [x] 中文使用 Text() + font="Noto Sans CJK SC"
- [x] 数学公式使用 MathTex()
- [x] 度数符号使用 ^\circ
- [x] 字体大小符合规范

---

## 渲染命令

```bash
# 快速预览
manim -pql quadratic_function.py QuadraticFunctionVertex

# 高质量渲染
manim -qh quadratic_function.py QuadraticFunctionVertex
```