# 平面直角坐标系的概念 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 基础
- 目标观众: 七年级学生

## 颜色配置
```python
COLOR_X_AXIS = "#e74c3c"          # 红色 - x轴
COLOR_Y_AXIS = "#3498db"          # 蓝色 - y轴
COLOR_ORIGIN = "#f39c12"          # 橙色 - 原点
COLOR_QUADRANT_I = "#2ecc71"      # 绿色 - 第一象限
COLOR_QUADRANT_II = "#9b59b6"     # 紫色 - 第二象限
COLOR_QUADRANT_III = "#e67e22"    # 橙色 - 第三象限
COLOR_QUADRANT_IV = "#1abc9c"     # 青色 - 第四象限
COLOR_GRID = GRAY_B               # 灰色 - 网格
COLOR_HIGHLIGHT = YELLOW          # 黄色 - 高亮
COLOR_POINT = "#ff6b6b"           # 红色 - 示例点
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 原点O | (0, 0, 0) | self.origin |
| x轴范围 | [-4, 4] | self.x_range |
| y轴范围 | [-6, 6] | self.y_range |
| 示例点A | (2, 3, 0) | self.point_A |
| 示例点B | (-3, 2, 0) | self.point_B |
| 示例点C | (-2, -3, 0) | self.point_C |
| 示例点D | (3, -2, 0) | self.point_D |
| 象限中心I | (2, 3, 0) | self.quad_I_center |
| 象限中心II | (-2, 3, 0) | self.quad_II_center |
| 象限中心III | (-2, -3, 0) | self.quad_III_center |
| 象限中心IV | (2, -3, 0) | self.quad_IV_center |

---

## Scene 1: 开场钩子 (0-4秒)
**目的**: 引起学生兴趣，提出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题: "如何在平面上精确定位一个点?"
3. 背景：几个随机闪烁的点

### 动画序列
| 时间 | 动作 | 代码参考 | 参数 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author)` | shift=DOWN*0.2 |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | run_time=1.0 |
| 1.5s | 随机点闪烁 | `LaggedStart(*[Flash(dot)])` | lag_ratio=0.2 |
| 3.5s | 等待 | `Wait()` | 0.5 |

### 清理
- FadeOut: hook_text, random_dots
- 保留: author_info

---

## Scene 2: 数轴回顾 (4-10秒)
**目的**: 复习数轴概念，为坐标系做铺垫

### 元素
1. 水平数轴（x轴）
2. 数轴上的刻度和数字
3. 标注"横轴"

### 动画序列
| 时间 | 动作 | 代码参考 | 参数 |
|------|------|---------|------|
| 4.0s | 标题出现 | `FadeIn(title)` | "复习: 数轴" |
| 4.5s | 绘制数轴 | `Create(x_axis)` | run_time=1.0 |
| 5.5s | 刻度和数字 | `Write(ticks)` | run_time=0.8 |
| 6.3s | 标注"横轴" | `FadeIn(label)` | shift=UP*0.2 |
| 7.0s | 等待 | `Wait()` | 1.0 |

### 清理
- FadeOut: title
- 保留: x_axis及其标注

---

## Scene 3: 引入第二条数轴 (10-16秒)
**目的**: 展示两条垂直数轴的组合

### 元素
1. 保留的x轴
2. 新的y轴（垂直）
3. 标注"纵轴"
4. 强调"互相垂直"

### 动画序列
| 时间 | 动作 | 代码参考 | 参数 |
|------|------|---------|------|
| 10.0s | 说明文字 | `FadeIn(explain)` | "再加一条垂直的数轴" |
| 10.5s | 绘制y轴 | `Create(y_axis)` | run_time=1.0 |
| 11.5s | y轴刻度 | `Write(y_ticks)` | run_time=0.8 |
| 12.3s | 标注"纵轴" | `FadeIn(y_label)` | shift=RIGHT*0.2 |
| 13.0s | 直角标记 | `Create(right_angle)` | at origin |
| 13.5s | 强调垂直 | `Indicate(right_angle)` | scale=1.2 |
| 14.5s | 等待 | `Wait()` | 0.5 |

### 清理
- FadeOut: explain, right_angle
- 保留: x_axis, y_axis, labels

---

## Scene 4: 标注原点 (16-20秒)
**目的**: 强调原点的概念

### 元素
1. 原点O的标记（点）
2. 标签"O"
3. 定义文字："原点 - 两轴交点"

### 动画序列
| 时间 | 动作 | 代码参考 | 参数 |
|------|------|---------|------|
| 16.0s | 原点闪烁 | `Flash(origin_dot)` | color=ORANGE |
| 16.5s | 原点出现 | `FadeIn(origin_dot)` | scale=0.5 |
| 17.0s | 标签O | `Write(origin_label)` | next_to=UR |
| 17.5s | 定义文字 | `FadeIn(definition)` | position=DOWN*4.5 |
| 19.0s | 等待 | `Wait()` | 1.0 |

### 清理
- FadeOut: definition
- 保留: origin_dot, origin_label, axes

---

## Scene 5: 引入象限概念 (20-35秒)
**目的**: 展示四个象限的划分和命名

### 元素
1. 四个象限的背景色（半透明）
2. 象限标记：Ⅰ, Ⅱ, Ⅲ, Ⅳ
3. 象限符号特征：(+,+), (-,+), (-,-), (+,-)

### 动画序列
| 时间 | 动作 | 代码参考 | 参数 |
|------|------|---------|------|
| 20.0s | 标题 | `FadeIn(title)` | "四个象限" |
| 20.5s | 第一象限背景 | `FadeIn(quad_I_bg)` | fill_opacity=0.2 |
| 21.0s | 标记Ⅰ | `Write(quad_I_label)` | |
| 21.5s | 符号(+,+) | `FadeIn(quad_I_sign)` | |
| 22.5s | 第二象限背景 | `FadeIn(quad_II_bg)` | fill_opacity=0.2 |
| 23.0s | 标记Ⅱ | `Write(quad_II_label)` | |
| 23.5s | 符号(-,+) | `FadeIn(quad_II_sign)` | |
| 24.5s | 第三象限背景 | `FadeIn(quad_III_bg)` | fill_opacity=0.2 |
| 25.0s | 标记Ⅲ | `Write(quad_III_label)` | |
| 25.5s | 符号(-,-) | `FadeIn(quad_III_sign)` | |
| 26.5s | 第四象限背景 | `FadeIn(quad_IV_bg)` | fill_opacity=0.2 |
| 27.0s | 标记Ⅳ | `Write(quad_IV_label)` | |
| 27.5s | 符号(+,-) | `FadeIn(quad_IV_sign)` | |
| 28.5s | 说明文字 | `FadeIn(explain)` | "按逆时针方向命名" |
| 30.0s | 逆时针箭头 | `Create(arrow_path)` | 绕原点 |
| 32.0s | 等待 | `Wait()` | 2.0 |

### 清理
- FadeOut: title, explain, arrow_path, background colors
- 保留: axes, quadrant labels and signs

---

## Scene 6: 示例点定位 (35-50秒)
**目的**: 展示如何用坐标表示点的位置

### 元素
1. 四个示例点：A(2,3), B(-3,2), C(-2,-3), D(3,-2)
2. 从点到轴的虚线
3. 坐标标注

### 动画序列
| 时间 | 动作 | 代码参考 | 参数 |
|------|------|---------|------|
| 35.0s | 说明 | `FadeIn(explain)` | "用有序数对表示点的位置" |
| 36.0s | 点A出现 | `FadeIn(point_A)` | scale=0.5 |
| 36.5s | 标签A(2,3) | `Write(label_A)` | |
| 37.0s | x坐标线 | `Create(dash_x_A)` | 垂直虚线 |
| 37.5s | y坐标线 | `Create(dash_y_A)` | 水平虚线 |
| 38.5s | 点B出现 | `FadeIn(point_B)` | scale=0.5 |
| 39.0s | 标签B(-3,2) | `Write(label_B)` | |
| 39.5s | B坐标线 | `Create(dashes_B)` | |
| 40.5s | 点C出现 | `FadeIn(point_C)` | scale=0.5 |
| 41.0s | 标签C(-2,-3) | `Write(label_C)` | |
| 41.5s | C坐标线 | `Create(dashes_C)` | |
| 42.5s | 点D出现 | `FadeIn(point_D)` | scale=0.5 |
| 43.0s | 标签D(3,-2) | `Write(label_D)` | |
| 43.5s | D坐标线 | `Create(dashes_D)` | |
| 45.0s | 强调 | `Indicate(all_points)` | scale=1.15 |
| 47.0s | 等待 | `Wait()` | 2.0 |

### 清理
- FadeOut: explain, dashed lines, some labels
- 保留: points, axes

---

## Scene 7: 总结 + 片尾 (50-75秒)
**目的**: 总结要点，引导关注

### 元素
1. 关键概念总结
2. 定义卡片
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 参数 |
|------|------|---------|------|
| 50.0s | 场景简化 | `FadeOut(points)` | 只保留坐标系 |
| 51.0s | 标题 | `Write(summary_title)` | "平面直角坐标系" |
| 52.0s | 卡片1 | `FadeIn(card_1)` | "x轴: 横轴" |
| 53.0s | 卡片2 | `FadeIn(card_2)` | "y轴: 纵轴" |
| 54.0s | 卡片3 | `FadeIn(card_3)` | "O: 原点" |
| 55.0s | 卡片4 | `FadeIn(card_4)` | "四个象限" |
| 57.0s | 缩小坐标系 | `axes.animate.scale(0.5)` | move_to=UP*3 |
| 58.0s | 作者信息放大 | `Transform(author)` | font_size=40 |
| 59.0s | 关注提示 | `FadeIn(follow_text)` | "关注我，学更多数学知识!" |
| 60.0s | 装饰动画 | `Create(decorations)` | 小图标 |
| 65.0s | 等待 | `Wait()` | 3.0 |
| 68.0s | 全部淡出 | `FadeOut(everything)` | run_time=1.5 |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 贯穿全程 |
| x_axis | Scene 2 | Scene 7 | 主坐标轴 |
| y_axis | Scene 3 | Scene 7 | 主坐标轴 |
| origin_dot | Scene 4 | Scene 7 | 原点标记 |
| quadrant_labels | Scene 5 | Scene 7 | 象限标记 |
| quadrant_signs | Scene 5 | Scene 7 | 象限符号 |
| point_A, B, C, D | Scene 6 | Scene 7 | 示例点 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| random_dots | Scene 1 | Scene 1 | 背景装饰 |
| dashed_lines | Scene 6 | Scene 6 | 坐标辅助线 |

---

## 关键帧截图说明

### 关键帧1 (t=3s): 开场钩子
- 画面：钩子问题 + 闪烁的点
- 目的：吸引注意力

### 关键帧2 (t=8s): 数轴
- 画面：单一水平数轴
- 目的：复习基础

### 关键帧3 (t=14s): 双轴系统
- 画面：垂直的x轴和y轴
- 目的：建立坐标系概念

### 关键帧4 (t=18s): 原点
- 画面：原点O被高亮
- 目的：强调原点

### 关键帧5 (t=30s): 四象限
- 画面：四个象限都有颜色和标记
- 目的：展示象限划分

### 关键帧6 (t=45s): 点定位
- 画面：四个示例点及其坐标
- 目的：应用坐标

### 关键帧7 (t=62s): 总结
- 画面：关键概念卡片
- 目的：强化记忆

---

## 动画节奏说明

### 慢节奏部分 (需要理解时间)
- Scene 3: 引入y轴，强调垂直关系 (2秒停留)
- Scene 5: 象限概念，每个象限1.5秒
- Scene 6: 点定位演示，每个点2秒

### 快节奏部分 (过渡)
- Scene 1→2: 0.5秒过渡
- Scene 2→3: 0.3秒过渡

### 停顿点
- 直角标记出现后: 1秒
- 所有象限展示完: 2秒
- 所有点展示完: 2秒
- 总结卡片全部出现后: 3秒

---

## 验证检查清单

### 几何验证 (verify_geometry.py)
- [ ] 原点坐标精确为(0, 0, 0)
- [ ] x轴和y轴严格垂直（点积=0）
- [ ] 示例点坐标精确
- [ ] 象限中心位置正确
- [ ] 虚线起止点精确

### 视觉验证
- [ ] 所有元素在边界内 (x∈[-4,4], y∈[-7,7])
- [ ] 文字无重叠
- [ ] 颜色对比度足够
- [ ] 字体大小符合规范

### 动画验证
- [ ] 总时长60-75秒
- [ ] 关键概念停留时间充足
- [ ] 过渡流畅自然
- [ ] 无突兀的跳转