# 二次函数图像平移 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 6 个
- 难度等级: 中等
- 知识点: 二次函数图像的平移规律

## 颜色配置
```python
COLOR_PRIMARY = "#e74c3c"      # 红色 - 原始函数
COLOR_VERTICAL = "#3498db"     # 蓝色 - 上下平移
COLOR_HORIZONTAL = "#2ecc71"   # 绿色 - 左右平移
COLOR_COMBINED = "#f39c12"     # 橙色 - 综合平移
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
COLOR_AXIS = WHITE
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 坐标系原点 | ORIGIN | - |
| x轴范围 | [-4, 4, 1] | axes.x_range |
| y轴范围 | [-2, 6, 1] | axes.y_range |
| 原始抛物线 | y = x² | graph_original |
| 上移抛物线 | y = x² + 2 | graph_up |
| 下移抛物线 | y = x² - 1 | graph_down |
| 右移抛物线 | y = (x-2)² | graph_right |
| 左移抛物线 | y = (x+1)² | graph_left |
| 综合平移 | y = (x-1)² + 2 | graph_combined |

## 关键动画参数
- 函数绘制时间: 1.5s
- 平移动画时间: 1.2s
- 公式变换时间: 0.8s
- 理解停顿: 1.5-2.0s
- 场景切换: 0.5s

---

## Scene 1: 开场钩子 (4秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题文字
3. 简单的抛物线示意

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_text)` - "抛物线会跳舞?" |
| 1.2s | 小抛物线图示淡入 | `FadeIn(demo_parabola)` |
| 2.0s | 抛物线上下移动演示 | `demo_parabola.animate.shift(UP*0.5)` |
| 2.5s | 抛物线左右移动演示 | `demo_parabola.animate.shift(RIGHT*0.5)` |
| 3.2s | 等待 | `Wait(0.8)` |

### 清理
- FadeOut: hook_text, demo_parabola
- 保留: author_info

---

## Scene 2: 建立坐标系与基准函数 (5秒)
**目的**: 展示坐标系，绘制 y = x²

### 元素
1. 坐标系 (Axes)
2. 原始函数 y = x²
3. 函数标签 "y = x²"
4. 顶点标记

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 创建坐标系 | `Create(axes)` |
| 1.0s | 绘制 y = x² | `Create(graph_original)` |
| 2.5s | 添加函数标签 | `FadeIn(label_original)` |
| 3.0s | 标记顶点 (0,0) | `FadeIn(vertex_dot, scale=0.5)` + `Flash` |
| 3.5s | 顶点坐标标签 | `FadeIn(vertex_label)` - "(0, 0)" |
| 4.0s | 等待理解 | `Wait(1.0)` |

### 清理
- 保留: axes, graph_original (变灰色)
- FadeOut: vertex_dot, vertex_label

---

## Scene 3: 上下平移 (12秒)
**目的**: 演示 y = x² ± k 的平移规律

### 元素
1. 标题: "上下平移"
2. 公式: y = x² → y = x² + k
3. 上移示例: y = x² + 2
4. 下移示例: y = x² - 1
5. 箭头指示
6. 口诀文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title_vertical)` - "上下平移" |
| 0.5s | 公式出现 | `Write(formula_vertical)` - "y = x² → y = x² + k" |
| 1.2s | **上移演示开始** | - |
| 1.2s | 公式变化 k=2 | `TransformMatchingTex` 到 "y = x² + 2" |
| 1.8s | 绘制上移抛物线 | `Create(graph_up)` |
| 3.0s | 向上箭头 | `GrowArrow(arrow_up)` |
| 3.4s | 新顶点标记 (0,2) | `FadeIn(vertex_up_dot)` + `Flash` |
| 4.0s | 提示文字 | `FadeIn(hint_up)` - "k>0 向上平移" |
| 5.0s | 等待理解 | `Wait(1.0)` |
| 6.0s | **下移演示开始** | - |
| 6.0s | 清理上移元素 | `FadeOut(graph_up, arrow_up, vertex_up_dot, hint_up)` |
| 6.5s | 公式变化 k=-1 | `TransformMatchingTex` 到 "y = x² - 1" |
| 7.0s | 绘制下移抛物线 | `Create(graph_down)` |
| 8.2s | 向下箭头 | `GrowArrow(arrow_down)` |
| 8.6s | 新顶点标记 (0,-1) | `FadeIn(vertex_down_dot)` + `Flash` |
| 9.2s | 提示文字 | `FadeIn(hint_down)` - "k<0 向下平移" |
| 10.2s | 口诀 | `FadeIn(slogan_v)` - "上加下减" |
| 11.2s | 等待理解 | `Wait(1.0)` |

### 清理
- FadeOut: title_vertical, formula_vertical, graph_up, graph_down, 所有箭头和标签
- 保留: axes, graph_original (恢复颜色)

---

## Scene 4: 左右平移 (12秒)
**目的**: 演示 y = (x ± h)² 的平移规律

### 元素
1. 标题: "左右平移"
2. 公式: y = x² → y = (x - h)²
3. 右移示例: y = (x - 2)²
4. 左移示例: y = (x + 1)²
5. 箭头指示
6. 口诀文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title_horizontal)` - "左右平移" |
| 0.5s | 公式出现 | `Write(formula_horizontal)` - "y = x² → y = (x - h)²" |
| 1.2s | **右移演示开始** | - |
| 1.2s | 公式变化 h=2 | `TransformMatchingTex` 到 "y = (x - 2)²" |
| 1.8s | 绘制右移抛物线 | `Create(graph_right)` |
| 3.0s | 向右箭头 | `GrowArrow(arrow_right)` |
| 3.4s | 新顶点标记 (2,0) | `FadeIn(vertex_right_dot)` + `Flash` |
| 4.0s | 提示文字 | `FadeIn(hint_right)` - "h>0 向右平移" |
| 4.6s | 特别提示 | `FadeIn(warning)` - "注意: (x - 2) 向右!" |
| 5.6s | 等待理解 | `Wait(1.0)` |
| 6.6s | **左移演示开始** | - |
| 6.6s | 清理右移元素 | `FadeOut(graph_right, arrow_right, vertex_right_dot, hint_right, warning)` |
| 7.1s | 公式变化 h=-1 | `TransformMatchingTex` 到 "y = (x + 1)²" |
| 7.6s | 绘制左移抛物线 | `Create(graph_left)` |
| 8.8s | 向左箭头 | `GrowArrow(arrow_left)` |
| 9.2s | 新顶点标记 (-1,0) | `FadeIn(vertex_left_dot)` + `Flash` |
| 9.8s | 提示文字 | `FadeIn(hint_left)` - "(x + 1) 向左!" |
| 10.8s | 口诀 | `FadeIn(slogan_h)` - "左加右减" |
| 11.8s | 等待理解 | `Wait(1.0)` |

### 清理
- FadeOut: title_horizontal, formula_horizontal, graph_right, graph_left, 所有箭头和标签
- 保留: axes, graph_original (恢复颜色)

---

## Scene 5: 综合平移 (10秒)
**目的**: 演示 y = a(x - h)² + k 的综合平移

### 元素
1. 标题: "综合平移"
2. 公式: y = (x - 1)² + 2
3. 分步箭头 (先水平，后垂直)
4. 中间状态抛物线
5. 最终抛物线
6. 顶点标记

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title_combined)` - "综合平移" |
| 0.5s | 完整公式 | `Write(formula_combined)` - "y = (x - 1)² + 2" |
| 1.2s | **步骤1: 水平平移** | - |
| 1.2s | 提示 | `FadeIn(step1_text)` - "① 先向右平移1" |
| 1.8s | 绘制中间状态 | `Create(graph_mid)` - y = (x-1)² |
| 3.0s | 向右箭头 | `GrowArrow(arrow_h)` |
| 3.5s | 中间顶点 (1,0) | `FadeIn(vertex_mid_dot)` |
| 4.5s | **步骤2: 垂直平移** | - |
| 4.5s | 提示 | `FadeIn(step2_text)` - "② 再向上平移2" |
| 5.0s | 中间抛物线变换 | `graph_mid.animate.shift(UP*某个单位)` |
| 6.2s | 向上箭头 | `GrowArrow(arrow_v)` |
| 6.6s | 最终顶点 (1,2) | `Transform(vertex_mid_dot, vertex_final_dot)` + `Flash` |
| 7.2s | 最终顶点标签 | `FadeIn(vertex_final_label)` - "(1, 2)" |
| 8.2s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title_combined, formula_combined, graph_mid, 所有箭头和标签
- 保留: axes

---

## Scene 6: 总结与口诀 (8秒)
**目的**: 强化记忆，展示完整口诀

### 元素
1. 标题: "平移口诀"
2. 通用公式: y = a(x - h)² + k
3. 口诀卡片
4. 四个方向的小示例

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title_summary)` - "平移口诀" |
| 0.6s | 通用公式出现 | `Write(formula_general)` - "y = a(x - h)² + k" |
| 1.4s | 口诀卡片1 | `FadeIn(card1)` - "左加右减" |
| 2.0s | 口诀卡片2 | `FadeIn(card2)` - "上加下减" |
| 2.6s | 完整口诀 | `FadeIn(full_slogan)` - "左加右减,上加下减!" |
| 3.4s | 四个小抛物线示例 | `FadeIn(demo_group)` 依次淡入 |
| 5.4s | 高亮公式参数 | 参数 h, k 变色高亮 |
| 6.4s | 等待理解 | `Wait(2.0)` |

### 清理
- 全部淡出准备片尾

---

## Scene 7: 片尾 (6秒)
**目的**: 作者信息与关注引导

### 元素
1. 作者名称放大
2. 抖音ID
3. 关注提示
4. 小抛物线装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者名称放大 | `Transform(author_info, author_large)` |
| 0.6s | 抖音ID淡入 | `FadeIn(douyin_id)` |
| 1.2s | 关注提示 | `FadeIn(follow_text)` - "关注我,学更多数学技巧!" |
| 2.0s | 装饰抛物线动画 | 多个小抛物线波动 |
| 4.0s | 等待 | `Wait(2.0)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终存在顶部 |
| axes | Scene 2 | Scene 6 | 主坐标系 |
| graph_original | Scene 2 | Scene 5 | 灰色保留作参考 |
| graph_up | Scene 3 | Scene 3 | 临时演示 |
| graph_down | Scene 3 | Scene 3 | 临时演示 |
| graph_right | Scene 4 | Scene 4 | 临时演示 |
| graph_left | Scene 4 | Scene 4 | 临时演示 |
| graph_mid | Scene 5 | Scene 5 | 中间过渡状态 |
| graph_combined | Scene 5 | Scene 5 | 最终平移结果 |

## 关键技术要点
1. **坐标精确计算**: 所有抛物线顶点位置必须精确计算，不能臆想
2. **颜色一致性**: 同类平移使用相同颜色
3. **动画流畅性**: 平移动画使用 `.animate.shift()` 保证流畅
4. **文字与数学分离**: 中文用 `Text()`, 公式用 `MathTex()`
5. **边界控制**: 确保所有元素在竖屏边界内 (x∈[-4,4], y∈[-7,7])

## 预期效果验证
- [ ] 所有抛物线顶点位置正确
- [ ] 平移方向与公式一致
- [ ] 口诀清晰易记
- [ ] 动画节奏合理
- [ ] 无元素溢出边界
- [ ] 中文显示正常