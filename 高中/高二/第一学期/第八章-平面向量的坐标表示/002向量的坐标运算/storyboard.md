# 平面向量的坐标运算 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等
- 年级: 高二

## 颜色配置
```python
COLOR_VECTOR_A = "#e74c3c"      # 红色 - 向量a
COLOR_VECTOR_B = "#3498db"      # 蓝色 - 向量b
COLOR_RESULT = "#2ecc71"        # 绿色 - 结果向量
COLOR_HIGHLIGHT = "#f39c12"     # 橙色 - 高亮
COLOR_AUXILIARY = "#95a5a6"     # 灰色 - 辅助线
COLOR_COORDINATE = WHITE        # 白色 - 坐标轴
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 向量a起点 | ORIGIN | self.a_start |
| 向量a终点 | [2, 1, 0] | self.a_end |
| 向量b起点 | ORIGIN | self.b_start |
| 向量b终点 | [1, 2, 0] | self.b_end |
| a+b终点 | a_end + b_end | self.sum_end |
| a-b终点 | a_end - b_end | self.diff_end |
| 2a终点 | 2 * a_end | self.scaled_end |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 抓住注意力 + 引出主题

### 元素
1. 作者标识（顶部）
2. 钩子问题："向量怎么算？"
3. 坐标系预览

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.2s | 坐标系创建 | `Create(axes)` |
| 2.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text
- 保留: axes, author_info

---

## Scene 2: 向量表示 (8秒)
**目的**: 介绍向量的坐标表示

### 元素
1. 向量a⃗ = (2, 1)
2. 向量b⃗ = (1, 2)
3. 坐标标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题显示 | `FadeIn(title)` |
| 0.5s | 绘制向量a | `GrowArrow(vector_a)` |
| 1.0s | 坐标标注a | `Write(label_a)` |
| 2.0s | 绘制向量b | `GrowArrow(vector_b)` |
| 2.5s | 坐标标注b | `Write(label_b)` |
| 3.5s | 公式显示 | `Write(formula)` |
| 5.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, formula
- 保留: vector_a, vector_b, labels

---

## Scene 3: 向量加法 (10秒)
**目的**: 演示向量加法 a⃗ + b⃗ = (x₁+x₂, y₁+y₂)

### 元素
1. 向量平移演示
2. 平行四边形法则
3. 结果向量

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题显示 | `FadeIn(title_add)` |
| 0.5s | 复制向量b并平移 | `Transform(b_copy)` |
| 1.5s | 绘制平行四边形 | `Create(parallelogram)` |
| 2.5s | 绘制结果向量 | `GrowArrow(result)` |
| 3.5s | 公式显示 | `Write(formula_add)` |
| 4.5s | 计算过程 | `Write(calculation)` |
| 6.0s | 高亮结果 | `Indicate(result)` |
| 7.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: parallelogram, b_copy, formula, calculation
- 保留: result (变淡)

---

## Scene 4: 向量减法 (10秒)
**目的**: 演示向量减法 a⃗ - b⃗ = (x₁-x₂, y₁-y₂)

### 元素
1. -b⃗ 向量
2. 减法转化为加法
3. 结果向量

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题显示 | `FadeIn(title_sub)` |
| 0.5s | 绘制-b向量 | `GrowArrow(neg_b)` |
| 1.5s | 说明转换 | `Write(explanation)` |
| 2.5s | 绘制结果向量 | `GrowArrow(diff_result)` |
| 3.5s | 公式显示 | `Write(formula_sub)` |
| 4.5s | 计算过程 | `Write(calculation)` |
| 6.0s | 高亮结果 | `Indicate(diff_result)` |
| 7.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: neg_b, explanation, formula, calculation
- 保留: diff_result (变淡)

---

## Scene 5: 数乘运算 (10秒)
**目的**: 演示数乘 λa⃗ = (λx₁, λy₁)

### 元素
1. 2a⃗ 向量
3. 长度变化演示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题显示 | `FadeIn(title_scalar)` |
| 0.5s | 向量a变化为2a | `Transform(a_copy, scaled_a)` |
| 2.0s | 公式显示 | `Write(formula_scalar)` |
| 3.0s | 计算过程 | `Write(calculation)` |
| 4.5s | 长度对比 | `Create(braces)` |
| 6.0s | 等待 | `Wait(2.5)` |

### 清理
- FadeOut: scaled_a, formula, calculation, braces

---

## Scene 6: 平行条件 (10秒)
**目的**: 介绍向量平行的坐标条件

### 元素
1. 平行向量示例
2. 叉积公式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题显示 | `FadeIn(title_parallel)` |
| 0.5s | 绘制平行向量 | `GrowArrow(parallel_vectors)` |
| 2.0s | 公式显示 | `Write(formula_parallel)` |
| 3.5s | 计算验证 | `Write(verification)` |
| 5.0s | 高亮关键 | `Indicate(key_part)` |
| 6.5s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: parallel_vectors, formula, verification

---

## Scene 7: 总结与关注 (8秒)
**目的**: 总结知识点 + 引导关注

### 元素
1. 公式汇总卡片
2. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题显示 | `FadeIn(title_summary)` |
| 0.5s | 公式卡片滑入 | `FadeIn(cards, shift=LEFT)` |
| 3.0s | 关注提示 | `Write(follow_text)` |
| 4.5s | 装饰动画 | `Flash(decorations)` |
| 6.0s | 等待 | `Wait(2.0)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| axes | Scene 1 | Scene 7 | 坐标系 |
| author_info | Scene 1 | Scene 7 | 作者信息 |
| vector_a | Scene 2 | Scene 5 | 向量a |
| vector_b | Scene 2 | Scene 4 | 向量b |
| result_sum | Scene 3 | Scene 3 | 加法结果 |
| result_diff | Scene 4 | Scene 4 | 减法结果 |
| scaled_vector | Scene 5 | Scene 5 | 数乘结果 |

## 关键技术点
1. ✅ 所有坐标通过 NumPy 精确计算
2. ✅ 向量使用 Arrow 类，带箭头
3. ✅ 坐标标注清晰，位置避免重叠
4. ✅ 公式使用 MathTex，中文用 Text
5. ✅ 边界检查：x ∈ [-4, 4], y ∈ [-7, 7]
6. ✅ 动画节奏：难点停留2-3秒