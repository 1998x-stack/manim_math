# 配方法 - 动画分镜脚本

## 元信息
- 目标时长: 75-90 秒
- 场景数量: 8 个
- 难度等级: 初中进阶
- 知识点: 一元二次方程的配方法

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主公式
COLOR_SECONDARY = "#e74c3c"      # 红色 - 关键步骤
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助
COLOR_SUCCESS = "#2ecc71"        # 绿色 - 正确答案
COLOR_GEOMETRY = "#9b59b6"       # 紫色 - 几何图形
COLOR_BACKGROUND = "#1a1a2e"     # 深蓝背景
```

## 几何预计算清单

### 配方几何可视化（Scene 3）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 大正方形边长 | x | side_x |
| 小正方形1 | x×x | square_x2 |
| 矩形1 | x×3 | rect1 |
| 矩形2 | x×3 | rect2 |
| 补充小正方形 | 3×3 | square_9 |
| 完整正方形边长 | x+3 | side_total |

**位置计算**:
```python
# 中心位置
center = np.array([0, 2, 0])

# 主正方形 (x²)
square_x2_pos = center + np.array([-1.5, 1.5, 0])

# 矩形1 (3x) - 右侧
rect1_pos = square_x2_pos + np.array([square_size, 0, 0])

# 矩形2 (3x) - 下方
rect2_pos = square_x2_pos + np.array([0, -square_size, 0])

# 小正方形 (9) - 右下角
square_9_pos = rect1_pos + np.array([0, -square_size, 0])
```

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 引出配方法的需求

### 元素
1. 作者标识 (顶部)
2. 问题: x² + 6x + 5 = 0
3. 疑问: "不能直接开平方，怎么办？"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info)` |
| 0.3s | 问题方程书写 | `Write(problem_eq)` |
| 1.0s | 问号出现 | `FadeIn(question_mark, scale=0.5)` |
| 1.5s | 疑问文字 | `Write(question_text)` |
| 2.5s | 闪烁强调 | `Flash(problem_eq)` |
| 3.0s | 等待 | `self.wait(0.5)` |

### 清理
- FadeOut: problem_eq, question_mark, question_text
- 保留: author_info

---

## Scene 2: 复习完全平方公式 (5-12秒)
**目的**: 为配方法做铺垫

### 元素
1. 标题: "回顾：完全平方公式"
2. 公式: (a+b)² = a² + 2ab + b²
3. 示例: (x+3)² = x² + 6x + 9

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.8s | 公式展开 | `Write(formula)` |
| 1.5s | 箭头指示 | `GrowArrow(arrow)` |
| 2.0s | 示例书写 | `Write(example)` |
| 3.0s | 高亮对应项 | `Indicate(terms)` |
| 4.5s | 等待理解 | `self.wait(1.5)` |

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 3: 配方的几何意义 (12-25秒)
**目的**: 用正方形面积直观展示配方

### 元素（几何图形）
1. 正方形 x² (蓝色)
2. 矩形 3x × 2 (两个，分别放右侧和下方)
3. 小正方形 3² (紫色，补全缺口)
4. 标注和箭头

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题"几何理解" | `Write(geo_title)` |
| 0.8s | x² 正方形出现 | `FadeIn(square_x2)` |
| 1.3s | 标注 x² | `Write(label_x2)` |
| 2.0s | 6x 文字提示 | `Write(hint_6x)` |
| 2.5s | 矩形1 滑入右侧 | `rect1.animate.shift(RIGHT)` |
| 3.2s | 矩形2 滑入下方 | `rect2.animate.shift(DOWN)` |
| 4.0s | 标注 3x | `Write(labels_3x)` |
| 5.0s | 提示"缺少什么？" | `Write(missing_hint)` |
| 5.8s | 虚线框闪烁 | `Flash(dotted_square)` |
| 6.5s | 小正方形淡入 | `FadeIn(square_9)` |
| 7.2s | 标注 9 | `Write(label_9)` |
| 8.0s | 整体框线 | `Create(big_square_outline)` |
| 8.8s | 标注 (x+3)² | `Write(label_total)` |
| 10.0s | 公式对照 | `Write(formula_correspondence)` |
| 11.5s | 等待 | `self.wait(1.5)` |

### 清理
- FadeOut: 所有几何元素
- 保留: author_info

---

## Scene 4: 配方法步骤讲解 (25-38秒)
**目的**: 展示配方法的标准步骤

### 元素
1. 标题: "配方法步骤"
2. 步骤卡片（4个）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title)` |
| 0.8s | 步骤1卡片滑入 | `step1.animate.shift(RIGHT)` |
| 1.5s | 步骤2卡片滑入 | `step2.animate.shift(RIGHT)` |
| 2.2s | 步骤3卡片滑入 | `step3.animate.shift(RIGHT)` |
| 2.9s | 步骤4卡片滑入 | `step4.animate.shift(RIGHT)` |
| 3.8s | 关键步骤闪烁 | `Flash(step3)` |
| 5.0s | 等待 | `self.wait(1.5)` |

**步骤内容**:
1. 移项（常数项→右边）
2. 二次项系数化为1
3. 两边加 (p/2)²
4. 配成完全平方式

### 清理
- FadeOut: 所有步骤卡片
- 保留: author_info

---

## Scene 5: 例题1 - x² + 6x + 5 = 0 (38-53秒)
**目的**: 详细演示配方过程

### 元素
1. 原方程
2. 每个步骤的变换
3. 最终答案

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 例题标签 | `Write(example_label)` |
| 0.5s | 原方程 | `Write(original)` |
| 1.5s | 步骤1：移项 | `TransformMatchingTex(step1)` |
| 2.5s | 标注"x²+6x" | `Indicate(left_side)` |
| 3.5s | 提示"(6/2)²=9" | `Write(hint_calc)` |
| 4.5s | 步骤2：两边+9 | `TransformMatchingTex(step2)` |
| 5.5s | 步骤3：配方 | `TransformMatchingTex(step3)` |
| 6.8s | 高亮(x+3)² | `Indicate(perfect_square)` |
| 8.0s | 步骤4：开平方 | `TransformMatchingTex(step4)` |
| 9.0s | 步骤5：解出x | `TransformMatchingTex(step5)` |
| 10.5s | 答案框 | `SurroundingRectangle(answer)` |
| 12.0s | 等待 | `self.wait(1.5)` |

### 清理
- FadeOut: 所有步骤
- 保留: author_info

---

## Scene 6: 例题2 - 2x² - 8x + 3 = 0 (53-68秒)
**目的**: 演示需要先化系数的情况

### 元素
1. 原方程（二次项系数≠1）
2. 强调先化系数
3. 配方求解

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 例题2标签 | `Write(example2_label)` |
| 0.5s | 原方程 | `Write(original)` |
| 1.5s | 高亮系数2 | `Indicate(coefficient)` |
| 2.3s | 提示"先除以2" | `Write(hint_divide)` |
| 3.3s | 化简为x²-4x | `TransformMatchingTex(simplified)` |
| 4.3s | 移项 | `TransformMatchingTex(moved)` |
| 5.3s | 提示"(-4/2)²=4" | `Write(hint_calc2)` |
| 6.3s | 两边+4 | `TransformMatchingTex(added)` |
| 7.3s | 配方(x-2)² | `TransformMatchingTex(completed)` |
| 8.5s | 开平方 | `TransformMatchingTex(sqrt)` |
| 9.5s | 最终答案 | `Write(final_answer)` |
| 11.0s | 答案框 | `SurroundingRectangle(answer)` |
| 12.5s | 等待 | `self.wait(1.0)` |

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 7: 配方法的应用 (68-75秒)
**目的**: 说明配方法的重要性

### 元素
1. 应用场景卡片
2. 关键提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题"配方法的意义" | `Write(title)` |
| 1.0s | 应用1：推导求根公式 | `FadeIn(app1)` |
| 2.0s | 应用2：化标准形式 | `FadeIn(app2)` |
| 3.0s | 应用3：求最值 | `FadeIn(app3)` |
| 4.5s | 闪烁强调 | `Flash(all_apps)` |
| 6.0s | 等待 | `self.wait(1.0)` |

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 8: 总结与关注 (75-90秒)
**目的**: 总结要点，引导关注

### 元素
1. 关键要点总结（4条）
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 总结标题 | `Write(summary_title)` |
| 1.0s | 要点1滑入 | `FadeIn(point1, shift=RIGHT)` |
| 1.8s | 要点2滑入 | `FadeIn(point2, shift=RIGHT)` |
| 2.6s | 要点3滑入 | `FadeIn(point3, shift=RIGHT)` |
| 3.4s | 要点4滑入 | `FadeIn(point4, shift=RIGHT)` |
| 5.0s | 要点闪烁 | `Flash(all_points)` |
| 6.0s | 作者信息放大 | `Transform(author_info)` |
| 7.5s | 关注文字 | `FadeIn(follow_text)` |
| 9.0s | 几何装饰旋转 | `Rotate(decorations)` |
| 12.0s | 全部淡出 | `FadeOut(all)` |

### 清理
- FadeOut: 全部

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 始终保持顶部 |
| problem_eq | Scene 1 | Scene 1 | 钩子问题 |
| perfect_square_formula | Scene 2 | Scene 2 | 完全平方公式 |
| geometry_squares | Scene 3 | Scene 3 | 几何可视化 |
| steps_cards | Scene 4 | Scene 4 | 步骤卡片 |
| example1 | Scene 5 | Scene 5 | 例题1 |
| example2 | Scene 6 | Scene 6 | 例题2 |
| applications | Scene 7 | Scene 7 | 应用场景 |
| summary | Scene 8 | Scene 8 | 总结要点 |

---

## 特殊注意事项

### LaTeX 使用规范
- ✅ 使用 `r"..."` 原始字符串
- ✅ 中文用 `Text()` 而非 `MathTex()`
- ✅ 分数用 `\frac{p}{2}`
- ✅ 平方用 `^2`
- ✅ 括号用 `\left( \right)`

### 几何元素约束
- 正方形边长: 基础单位 1.0
- 缩放因子: 0.8（适应竖屏）
- 中心位置: (0, 2, 0)
- 标签偏移: 0.2-0.3

### 边界约束
- 几何图形区域: y ∈ [1, 4]
- 公式主区域: y ∈ [-2, 5]
- 底部说明: y ∈ [-6, -4]
- 顶部作者: y = 7

### 字体大小
- 标题: 36-40
- 公式: 28-32
- 说明: 22-24
- 几何标签: 20-24
- 作者: 20

### 动画节奏
- 几何元素出现: 0.5-0.8s
- 公式变换: 1.0-1.5s
- 理解停顿: 1.5-2.0s
- 关键步骤: 额外停顿 2.0s

### 配方几何可视化关键点
1. x² 正方形要足够明显
2. 两个 3x 矩形要对称放置
3. 补充的 9 要用不同颜色高亮
4. 最终的 (x+3)² 要用粗边框标注
5. 公式要和几何图形对应显示