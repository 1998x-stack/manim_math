# 正弦函数和余弦函数的图像与性质 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 高一
- 知识点: 三角函数的图像与性质

## 颜色配置
```python
COLOR_SINE = "#e74c3c"        # 红色 - 正弦
COLOR_COSINE = "#3498db"      # 蓝色 - 余弦
COLOR_HIGHLIGHT = YELLOW      # 高亮
COLOR_AUXILIARY = GRAY_B      # 辅助线
COLOR_GRID = "#2c3e50"        # 网格
COLOR_AXES = WHITE            # 坐标轴
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 坐标轴 | Axes(x_range=[-PI, 2*PI], y_range=[-1.5, 1.5]) | self.axes |
| 正弦曲线 | axes.plot(np.sin) | self.sin_graph |
| 余弦曲线 | axes.plot(np.cos) | self.cos_graph |
| 五个关键点 (sin) | (0,0), (π/2,1), (π,0), (3π/2,-1), (2π,0) | self.sin_key_points |
| 五个关键点 (cos) | (0,1), (π/2,0), (π,-1), (3π/2,0), (2π,1) | self.cos_key_points |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力 + 引入主题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字闪烁)
3. 单位圆旋转动画预览

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` - "正弦和余弦到底有什么区别?" |
| 1.5s | 单位圆快速旋转预览 | `Rotate(unit_circle)` |
| 3.0s | 淡出钩子 | `FadeOut(hook_text)` |

### 清理
- FadeOut: hook_text, preview animation
- 保留: author_info

---

## Scene 2: 正弦函数图像绘制 (10-12秒)
**目的**: 使用五点法绘制正弦曲线

### 元素
1. 坐标轴 (x轴标记 0, π/2, π, 3π/2, 2π)
2. 标题: "正弦函数 y = sin x"
3. 五个关键点
4. 平滑曲线

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 创建坐标轴 | `Create(axes)` |
| 1.0s | 标题淡入 | `FadeIn(title)` |
| 1.5s | 五点法说明 | `Write(five_point_text)` |
| 2.5s | 依次标记5个关键点 | `FadeIn(dots[i])` 循环 |
| 5.0s | 连接成平滑曲线 | `Create(sin_graph)` |
| 7.0s | 高亮周期 | `Indicate(period_brace)` |

### 清理
- FadeOut: five_point_text
- 保留: axes, sin_graph, title

---

## Scene 3: 正弦函数性质标注 (8-10秒)
**目的**: 标注定义域、值域、周期、奇偶性

### 元素
1. 定义域标注: R
2. 值域标注: [-1, 1]
3. 周期标注: 2π
4. 奇函数对称性演示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 定义域文字出现 | `FadeIn(domain_text)` |
| 1.0s | 值域高亮 | `Flash(y_axis)` + `FadeIn(range_text)` |
| 2.5s | 周期标记 | `Create(period_brace)` |
| 4.0s | 奇函数对称演示 | `Rotate(graph_copy)` 关于原点 |
| 6.5s | 单调性标注 | 高亮 [-π/2, π/2] 区间 |

### 清理
- FadeOut: property_texts
- 保留: axes, sin_graph

---

## Scene 4: 余弦函数图像绘制 (10-12秒)
**目的**: 使用五点法绘制余弦曲线

### 元素
1. 新标题: "余弦函数 y = cos x"
2. 余弦的五个关键点
3. 余弦曲线 (蓝色)
4. 与正弦对比

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题切换 | `Transform(old_title, new_title)` |
| 1.0s | 正弦曲线变灰 | `sin_graph.animate.set_opacity(0.3)` |
| 2.0s | 标记余弦5个关键点 | `FadeIn(cos_dots[i])` 循环 |
| 5.0s | 绘制余弦曲线 | `Create(cos_graph)` |
| 7.0s | 两条曲线对比 | 同时显示 |

### 清理
- 保留: axes, sin_graph (半透明), cos_graph

---

## Scene 5: 余弦函数性质标注 (8-10秒)
**目的**: 标注余弦的性质并与正弦对比

### 元素
1. 定义域、值域 (相同)
2. 周期 2π
3. 偶函数对称性演示
4. 单调性标注 [0, π]

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 性质文字出现 | `FadeIn(property_group)` |
| 2.0s | 偶函数对称演示 | `Reflect(graph_copy, axis=y_axis)` |
| 4.0s | 单调性高亮 | 高亮 [0, π] 递减区间 |
| 6.0s | 与正弦对比 | 并排显示性质 |

### 清理
- FadeOut: property_texts
- 保留: axes, sin_graph, cos_graph

---

## Scene 6: 正弦余弦关系 (12-15秒)
**目的**: 展示 cos x = sin(x + π/2) 和 sin x = cos(π/2 - x)

### 元素
1. 关系式1: cos x = sin(x + π/2)
2. 关系式2: sin x = cos(π/2 - x)
3. 动画演示平移关系
4. 单位圆辅助理解

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 公式1出现 | `Write(formula_1)` |
| 1.5s | 正弦曲线向左平移π/2 | `sin_graph.animate.shift(LEFT*pi/2)` |
| 3.5s | 高亮重合部分 | `Flash(overlap)` |
| 5.0s | 恢复并显示公式2 | `Write(formula_2)` |
| 7.0s | 单位圆演示 | 显示单位圆上的关系 |
| 10.0s | 两个公式并排 | 总结 |

### 清理
- FadeOut: formulas, unit_circle
- 保留: axes, sin_graph, cos_graph

---

## Scene 7: 总结与片尾 (8-10秒)
**目的**: 总结要点 + 关注提示

### 元素
1. 核心性质卡片
2. 关注提示
3. 作者信息

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 图像缩小移到上方 | `graphs.animate.scale(0.5).to_edge(UP)` |
| 1.5s | 性质卡片滑入 | `card.animate.shift(RIGHT)` |
| 4.0s | 关注文字放大 | `Write(follow_text)` |
| 6.0s | 装饰动画 | 波浪线装饰 |
| 8.0s | 全部淡出 | `FadeOut(VGroup(*))` |

### 清理
- 全部清空

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| axes | Scene 2 | Scene 7 | 坐标轴 |
| sin_graph | Scene 2 | Scene 7 | 正弦曲线 |
| cos_graph | Scene 4 | Scene 7 | 余弦曲线 |
| sin_dots | Scene 2 | Scene 2 | 临时关键点 |
| cos_dots | Scene 4 | Scene 4 | 临时关键点 |
| property_texts | Scene 3/5 | Scene 3/5 | 临时性质标注 |
| formulas | Scene 6 | Scene 6 | 临时公式 |

---

## 技术要点
1. **坐标轴配置**: 使用 Axes，x轴范围 [-π, 2.5π]，包含特殊点标记
2. **函数绘制**: 使用 axes.plot(lambda x: np.sin(x))
3. **五点法**: 精确标记 (0,0), (π/2,1), (π,0), (3π/2,-1), (2π,0)
4. **动画平滑**: 使用 rate_func=smooth 保证流畅度
5. **颜色对比**: 正弦红色，余弦蓝色，易于区分
6. **文字可读**: 中文使用 Text()，公式使用 MathTex()