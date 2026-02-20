# 椭圆的定义与标准方程 - 动画分镜脚本

## 元信息
- 目标时长: 70-85 秒
- 场景数量: 8 个
- 难度等级: 中等偏难
- 目标观众: 高二学生

## 颜色配置
```python
COLOR_PRIMARY = "#e74c3c"      # 红色 - 椭圆
COLOR_FOCUS = "#f39c12"        # 橙色 - 焦点
COLOR_HIGHLIGHT = YELLOW        # 高亮色
COLOR_AUXILIARY = GRAY_B        # 辅助线
COLOR_AXIS_MAJOR = "#3498db"   # 蓝色 - 长轴
COLOR_AXIS_MINOR = "#2ecc71"   # 绿色 - 短轴
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 | 数值 |
|------|---------|---------|------|
| 长半轴 | a | self.a | 3.0 |
| 短半轴 | b | self.b | 2.0 |
| 半焦距 | c = √(a²-b²) | self.c | 2.236 |
| 左焦点 | (-c, 0) | self.F1 | (-2.236, 0) |
| 右焦点 | (c, 0) | self.F2 | (2.236, 0) |
| 顶点A1 | (-a, 0) | self.A1 | (-3, 0) |
| 顶点A2 | (a, 0) | self.A2 | (3, 0) |
| 顶点B1 | (0, -b) | self.B1 | (0, -2) |
| 顶点B2 | (0, b) | self.B2 | (0, 2) |
| 椭圆上点P | 参数方程 | self.point_P | 动态 |

---

## Scene 1: 开场钩子 (5秒)
**目的**: 抓住注意力，引出椭圆

### 元素
1. 作者标识（顶部）
2. 钩子问题："椭圆是怎么画出来的？"
3. 坐标系
4. 椭圆预览

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.1s | 坐标系创建 | `Create(axes)` |
| 2.0s | 椭圆闪现 | `Create(ellipse)` |
| 3.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: hook_text
- 保留: axes, ellipse, author_info

---

## Scene 2: 椭圆的定义 (10秒)
**目的**: 展示定义 - 到两焦点距离之和恒定

### 元素
1. 标题："椭圆的定义"
2. 两个焦点 F₁, F₂（橙色大点）
3. 椭圆上一点P（可移动）
4. 连线 PF₁ 和 PF₂
5. 距离标注
6. 定义文字："|PF₁| + |PF₂| = 2a"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | 椭圆淡化 | `ellipse.animate.set_opacity(0.3)` |
| 1.0s | 左焦点闪烁 | `Flash(F1)` |
| 1.5s | 右焦点闪烁 | `Flash(F2)` |
| 2.0s | 点P出现 | `FadeIn(point_P)` |
| 2.5s | 连线PF₁创建 | `Create(line_PF1)` |
| 3.0s | 连线PF₂创建 | `Create(line_PF2)` |
| 3.8s | 距离标注 | `FadeIn(distance_labels)` |
| 4.5s | 定义公式 | `Write(definition)` |
| 6.0s | P点移动 | `point_P.animate.move_to()` |
| 8.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, lines, labels, definition
- 恢复: ellipse opacity
- 保留: axes, ellipse, F1, F2

---

## Scene 3: 动态绘制椭圆 (8秒)
**目的**: 用定义动态生成椭圆

### 元素
1. 标题："用定义画椭圆"
2. 点P沿椭圆轨迹移动
3. 始终显示 |PF₁| + |PF₂| = 2a
4. 留下轨迹

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | 椭圆消失 | `FadeOut(ellipse)` |
| 1.0s | P点从右顶点开始 | `point_P.move_to(A2)` |
| 1.5s | P点沿轨迹移动 | `MoveAlongPath` |
| 1.5s | 实时连线更新 | `always_redraw(lambda: ...)` |
| 1.5s | 距离和显示 | `DecimalNumber + updater` |
| 6.0s | 轨迹完成 | 椭圆重新出现 |
| 7.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, 实时连线
- 保留: ellipse, F1, F2

---

## Scene 4: 标准方程（焦点在x轴）(10秒)
**目的**: 展示焦点在x轴的标准方程

### 元素
1. 标题："标准方程"
2. 副标题："焦点在x轴"
3. 方程：x²/a² + y²/b² = 1
4. 参数标注：a > b > 0
5. 焦点标注：F₁(-c, 0), F₂(c, 0)
6. 长轴、短轴标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.5s | 副标题出现 | `FadeIn(subtitle)` |
| 1.0s | 标准方程书写 | `Write(equation)` |
| 2.5s | 长轴高亮 | `line_major.set_color(HIGHLIGHT)` |
| 3.0s | a标注 | `FadeIn(a_label)` |
| 3.8s | 短轴高亮 | `line_minor.set_color(HIGHLIGHT)` |
| 4.3s | b标注 | `FadeIn(b_label)` |
| 5.0s | 焦点标注 | `FadeIn(focus_labels)` |
| 6.0s | c标注 | `FadeIn(c_label)` |
| 7.5s | 等待 | `Wait(2.5)` |

### 清理
- FadeOut: title, subtitle, equation, labels
- 保留: ellipse, F1, F2

---

## Scene 5: 标准方程（焦点在y轴）(8秒)
**目的**: 展示焦点在y轴的标准方程

### 元素
1. 副标题："焦点在y轴"
2. 方程：x²/b² + y²/a² = 1
3. 椭圆旋转90°效果
4. 焦点移动到y轴

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题出现 | `Write(subtitle)` |
| 0.6s | 原椭圆淡出 | `FadeOut(ellipse)` |
| 1.0s | 新椭圆淡入 | `FadeIn(ellipse_vertical)` |
| 1.5s | 焦点移动 | `Transform(F1, F1_new)` |
| 2.2s | 方程书写 | `Write(equation_vertical)` |
| 3.5s | 参数对比 | 显示a、b位置互换 |
| 5.5s | 等待 | `Wait(2.5)` |

### 清理
- FadeOut: subtitle, equation, ellipse_vertical
- 恢复: 原椭圆和焦点
- 保留: axes

---

## Scene 6: a、b、c的关系 (9秒)
**目的**: 展示 a² = b² + c²

### 元素
1. 标题："a、b、c的关系"
2. 直角三角形（构造）
3. 三边标注：a, b, c
4. 关系式：a² = b² + c²
5. 动画验证

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | 椭圆淡化 | `set_opacity(0.2)` |
| 1.0s | 构造三角形 | `Create(triangle)` |
| 2.0s | 边长标注 | `FadeIn(labels)` |
| 3.0s | 直角标记 | `FadeIn(right_angle)` |
| 4.0s | 关系式书写 | `Write(relation)` |
| 5.5s | 数值验证 | 显示 9 = 4 + 5 |
| 7.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, triangle, labels, relation
- 恢复: ellipse opacity
- 保留: ellipse

---

## Scene 7: 四个顶点 (8秒)
**目的**: 标注椭圆的四个顶点

### 元素
1. 标题："椭圆的顶点"
2. 四个顶点标记
3. 坐标标注
4. 顶点分类：长轴顶点、短轴顶点

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | 长轴顶点闪烁 | `Flash(A1), Flash(A2)` |
| 1.2s | 长轴顶点标注 | `FadeIn(labels_major)` |
| 2.5s | 短轴顶点闪烁 | `Flash(B1), Flash(B2)` |
| 3.1s | 短轴顶点标注 | `FadeIn(labels_minor)` |
| 4.5s | 总结文字 | "四个顶点：(±a,0), (0,±b)" |
| 6.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: title, labels
- 保留: ellipse

---

## Scene 8: 总结 + 片尾 (10秒)
**目的**: 知识点总结和引导关注

### 元素
1. 总结卡片：定义、方程、关系
2. 作者信息放大
3. 关注提示
4. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清空场景 | `FadeOut(all)` |
| 0.6s | 总结标题 | `Write("椭圆知识总结")` |
| 1.2s | 三个要点卡片 | 依次滑入 |
| 4.5s | 等待 | `Wait(1.0)` |
| 5.5s | 卡片淡出 | `FadeOut(cards)` |
| 6.0s | 作者信息放大 | `Transform(author)` |
| 7.0s | 关注提示 | `FadeIn(follow_text)` |
| 8.0s | 装饰椭圆 | 多个小椭圆旋转 |
| 9.0s | 全部淡出 | `FadeOut(all)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 作者标识 |
| axes | Scene 1 | Scene 7 | 坐标系 |
| ellipse | Scene 1 | Scene 7 | 主椭圆 |
| F1, F2 | Scene 2 | Scene 7 | 焦点 |
| point_P | Scene 2 | Scene 3 | 椭圆上的点 |

---

## 关键技术点
1. 使用参数方程生成椭圆上的点：x=a*cos(t), y=b*sin(t)
2. 使用 always_redraw 实时更新连线
3. 使用 ValueTracker 控制点的移动
4. 精确计算 c = √(a²-b²)
5. 验证距离和恒定：|PF₁| + |PF₂| = 2a

## 几何验证重点
- ✓ 验证 a² = b² + c²
- ✓ 验证椭圆定义：距离和恒定
- ✓ 验证焦点位置
- ✓ 验证顶点坐标
- ✓ 验证元素在安全边界内