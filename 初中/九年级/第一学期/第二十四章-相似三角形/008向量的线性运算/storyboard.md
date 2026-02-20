# 向量的线性运算 - 动画分镜脚本

## 元信息
- **目标时长**: 70-85秒
- **场景数量**: 7个
- **难度等级**: 中等
- **年级**: 九年级第一学期
- **知识点**: 向量的线性运算（加法、减法、数乘、基底分解）

## 颜色配置
```python
COLOR_VECTOR_A = "#e74c3c"        # 红色 - 向量a
COLOR_VECTOR_B = "#3498db"        # 蓝色 - 向量b
COLOR_VECTOR_SUM = "#2ecc71"      # 绿色 - 和向量
COLOR_BASIS_E1 = "#f39c12"        # 橙色 - 基向量e1
COLOR_BASIS_E2 = "#9b59b6"        # 紫色 - 基向量e2
COLOR_HIGHLIGHT = YELLOW          # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B          # 灰色 - 辅助线
COLOR_AXES = WHITE                # 白色 - 坐标轴
```

## 几何预计算清单

### 向量定义
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 原点O | 基准点 | `self.origin` | [0, 0, 0] |
| 向量a起点 | 基准点 | `self.a_start` | 通常为原点 |
| 向量a终点 | 起点 + 方向向量 | `self.a_end` | [2, 1, 0] |
| 向量b起点 | 基准点 | `self.b_start` | 通常为原点 |
| 向量b终点 | 起点 + 方向向量 | `self.b_end` | [1, 2, 0] |
| 向量a方向 | a_end - a_start | `self.vec_a` | 纯方向向量 |
| 向量b方向 | b_end - b_start | `self.vec_b` | 纯方向向量 |

### 向量加法
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 平移后b起点 | a_end | `self.b_shifted_start` | 首尾相接 |
| 平移后b终点 | a_end + vec_b | `self.b_shifted_end` | - |
| 和向量a+b终点 | origin + vec_a + vec_b | `self.sum_end` | - |

### 向量数乘
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 数乘系数λ | 常数 | `self.lambda_val` | 如 2, -1, 0.5 |
| λa终点 | origin + λ * vec_a | `self.scaled_end` | - |

### 基底分解
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 基向量e1 | 单位向量 | `self.e1` | [1, 0, 0] |
| 基向量e2 | 单位向量 | `self.e2` | [0, 1, 0] |
| 系数λ1 | 投影 | `self.lambda1` | a在e1上的分量 |
| 系数λ2 | 投影 | `self.lambda2` | a在e2上的分量 |
| λ1·e1终点 | origin + λ1 * e1 | `self.lambda1_e1_end` | - |
| λ2·e2终点 | origin + λ2 * e2 | `self.lambda2_e2_end` | - |

### 验证项
- [ ] 向量加法：a + b = b + a（交换律）
- [ ] 向量终点位置正确
- [ ] 数乘方向：λ > 0 同向，λ < 0 反向
- [ ] 基底分解：λ1·e1 + λ2·e2 = a
- [ ] 平行向量：a = λb

---

## Scene 1: 开场钩子 (0-4秒)
**目的**: 引出向量概念，抓住注意力

### 元素
1. 作者标识（顶部）
2. 钩子问题："什么是向量？它有什么用？"
3. 简单箭头示意

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子问题书写 | `Write(hook_text)` | 1.0s |
| 1.3s | 几个不同方向的箭头出现 | `GrowArrow(arrow)` | 1.2s |
| 2.5s | 箭头闪烁 | `Flash(arrows)` | 0.5s |
| 3.0s | 等待 | `Wait(1.0)` | 1.0s |

### 清理
- FadeOut: hook_text, example_arrows
- 保留: author_info

---

## Scene 2: 向量加法 (4-18秒)
**目的**: 展示向量加法的几何意义（三角形法则和平行四边形法则）

### 元素
1. 标题："向量的加法"
2. 坐标系（可选）
3. 向量a（红色箭头）
4. 向量b（蓝色箭头）
5. 平移后的向量b
6. 和向量a+b（绿色箭头）
7. 平行四边形辅助线

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 4.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 4.5s | 绘制向量a | `GrowArrow(arrow_a)` | 0.8s |
| 5.3s | 标签"→a" | `Write(label_a)` | 0.4s |
| 5.7s | 绘制向量b | `GrowArrow(arrow_b)` | 0.8s |
| 6.5s | 标签"→b" | `Write(label_b)` | 0.4s |
| 6.9s | 说明："首尾相接" | `FadeIn(explanation)` | 0.8s |
| 7.7s | 向量b平移到a的终点 | `Transform(arrow_b, arrow_b_shifted)` | 1.2s |
| 8.9s | 绘制和向量a+b | `GrowArrow(arrow_sum)` | 1.0s |
| 9.9s | 标签"→a+→b" | `Write(label_sum)` | 0.6s |
| 10.5s | 等待理解 | `Wait(1.0)` | 1.0s |
| 11.5s | 过渡："平行四边形法则" | `FadeIn(transition)` | 0.8s |
| 12.3s | 绘制平行四边形虚线 | `Create(parallelogram_lines)` | 1.5s |
| 13.8s | 强调："两种方法，同一结果" | `Flash(arrow_sum)` | 0.8s |
| 14.6s | 等待理解 | `Wait(2.0)` | 2.0s |

### 几何计算要点
```python
# 向量加法：首尾相接
vec_a = a_end - a_start
vec_b = b_end - b_start

# 平移向量b
b_shifted_start = a_end
b_shifted_end = a_end + vec_b

# 和向量
sum_end = origin + vec_a + vec_b
```

### 清理
- FadeOut: title, explanation, parallelogram_lines, all labels
- 保留: arrow_a, arrow_b（将在下一场景继续使用）

---

## Scene 3: 向量数乘 (18-32秒)
**目的**: 展示数乘对向量长度和方向的影响

### 元素
1. 标题："向量的数乘"
2. 原向量a
3. 2a（同向，长度加倍）
4. 0.5a（同向，长度减半）
5. -a（反向，长度相同）
6. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 18.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 18.5s | 保持向量a | `Indicate(arrow_a)` | 0.5s |
| 19.0s | 说明："λ > 0，同向" | `FadeIn(explanation_positive)` | 0.8s |
| 19.8s | 创建2a | `GrowArrow(arrow_2a)` | 1.0s |
| 20.8s | 标签"2→a" | `Write(label_2a)` | 0.5s |
| 21.3s | 创建0.5a | `GrowArrow(arrow_half_a)` | 1.0s |
| 22.3s | 标签"0.5→a" | `Write(label_half_a)` | 0.5s |
| 22.8s | 等待 | `Wait(1.0)` | 1.0s |
| 23.8s | 说明："λ < 0，反向" | `FadeIn(explanation_negative)` | 0.8s |
| 24.6s | 创建-a | `GrowArrow(arrow_neg_a)` | 1.0s |
| 25.6s | 标签"-→a" | `Write(label_neg_a)` | 0.5s |
| 26.1s | 强调："方向相反，长度相同" | `Flash(arrow_neg_a)` | 0.8s |
| 26.9s | 等待理解 | `Wait(2.0)` | 2.0s |

### 几何计算要点
```python
# 数乘
vec_2a = 2 * vec_a
vec_half_a = 0.5 * vec_a
vec_neg_a = -1 * vec_a

# 终点
end_2a = origin + vec_2a
end_half_a = origin + vec_half_a
end_neg_a = origin + vec_neg_a
```

### 清理
- FadeOut: 所有内容
- 保留: author_info

---

## Scene 4: 基底概念引入 (32-42秒)
**目的**: 引入基向量的概念

### 元素
1. 标题："基底"
2. 坐标系
3. 两个不共线的基向量e1, e2
4. 说明："两个不共线的向量作为基底"

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 32.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 32.5s | 创建坐标系 | `Create(axes)` | 1.0s |
| 33.5s | 绘制基向量e1 | `GrowArrow(arrow_e1)` | 0.8s |
| 34.3s | 标签"→e₁" | `Write(label_e1)` | 0.4s |
| 34.7s | 绘制基向量e2 | `GrowArrow(arrow_e2)` | 0.8s |
| 35.5s | 标签"→e₂" | `Write(label_e2)` | 0.4s |
| 35.9s | 说明："不共线！" | `FadeIn(explanation)` | 0.8s |
| 36.7s | 强调：两向量不共线 | `Wiggle(arrow_e1), Wiggle(arrow_e2)` | 1.0s |
| 37.7s | 过渡文字："任意向量都可以分解" | `FadeIn(transition)` | 1.2s |
| 38.9s | 等待理解 | `Wait(2.0)` | 2.0s |

### 几何计算要点
```python
# 基向量（示例：不平行于坐标轴）
e1 = np.array([1, 0, 0])
e2 = np.array([0.5, 1, 0])  # 确保不共线

# 验证不共线
cross_product = np.cross(e1[:2], e2[:2])
assert abs(cross_product) > 1e-10, "基向量共线！"
```

### 清理
- FadeOut: explanation, transition
- 保留: axes, arrow_e1, arrow_e2, labels

---

## Scene 5: 向量分解 (42-58秒)
**目的**: 展示任意向量表示为基向量的线性组合

### 元素
1. 标题："向量的分解"
2. 保留的基向量e1, e2
3. 新向量a
4. λ1·e1（红色虚线）
5. λ2·e2（蓝色虚线）
6. 平行四边形构造
7. 公式：→a = λ₁→e₁ + λ₂→e₂

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 42.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 42.5s | 绘制目标向量a | `GrowArrow(arrow_a)` | 1.0s |
| 43.5s | 标签"→a" | `Write(label_a)` | 0.4s |
| 43.9s | 说明："如何用e1和e2表示a？" | `FadeIn(question)` | 1.0s |
| 44.9s | 从a终点画平行于e2的辅助线 | `Create(parallel_e2)` | 1.0s |
| 45.9s | 从a终点画平行于e1的辅助线 | `Create(parallel_e1)` | 1.0s |
| 46.9s | 高亮λ1·e1部分 | `Indicate(lambda1_e1)` | 0.8s |
| 47.7s | 绘制λ1·e1向量 | `GrowArrow(arrow_lambda1_e1)` | 0.8s |
| 48.5s | 高亮λ2·e2部分 | `Indicate(lambda2_e2)` | 0.8s |
| 49.3s | 绘制λ2·e2向量 | `GrowArrow(arrow_lambda2_e2)` | 0.8s |
| 50.1s | 公式淡入 | `FadeIn(formula)` | 1.0s |
| 51.1s | 具体数值："→a = 2→e₁ + 1.5→e₂" | `Transform(formula, specific_formula)` | 1.2s |
| 52.3s | 强调 | `Flash(formula)` | 0.5s |
| 52.8s | 等待理解 | `Wait(2.0)` | 2.0s |

### 几何计算要点
```python
# 选择目标向量a
vec_a = np.array([2, 1.5, 0])

# 计算系数（通过解方程组）
# vec_a = lambda1 * e1 + lambda2 * e2
# 即：
# [a_x]   [e1_x  e2_x] [lambda1]
# [a_y] = [e1_y  e2_y] [lambda2]

A_matrix = np.column_stack([e1[:2], e2[:2]])
lambdas = np.linalg.solve(A_matrix, vec_a[:2])
lambda1, lambda2 = lambdas[0], lambdas[1]

# 验证
vec_reconstructed = lambda1 * e1 + lambda2 * e2
assert np.allclose(vec_a, vec_reconstructed), "分解错误！"
```

### 清理
- FadeOut: question, parallel_e1, parallel_e2
- 保留: axes, arrow_e1, arrow_e2, arrow_a, formula

---

## Scene 6: 平行向量 (58-68秒)
**目的**: 展示平行向量的特殊性质

### 元素
1. 标题："平行向量"
2. 向量a
3. 向量b = 2a（平行）
4. 公式：→a ∥ →b ⟺ →a = λ→b

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 58.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 58.5s | 清空场景，重新绘制向量a | `FadeOut(previous), GrowArrow(arrow_a)` | 1.0s |
| 59.5s | 绘制平行向量b | `GrowArrow(arrow_b_parallel)` | 1.0s |
| 60.5s | 平行符号标记 | `Create(parallel_symbol)` | 0.5s |
| 61.0s | 公式淡入 | `FadeIn(formula)` | 1.0s |
| 62.0s | 说明："方向相同或相反" | `FadeIn(explanation)` | 1.0s |
| 63.0s | 示例："→b = 2→a" | `Write(example)` | 1.0s |
| 64.0s | 强调 | `Flash(arrow_b_parallel)` | 0.5s |
| 64.5s | 等待理解 | `Wait(2.0)` | 2.0s |

### 几何计算要点
```python
# 平行向量
vec_a = np.array([2, 1, 0])
lambda_parallel = 2
vec_b_parallel = lambda_parallel * vec_a

# 验证平行
cross = np.cross(vec_a[:2], vec_b_parallel[:2])
assert abs(cross) < 1e-10, "向量不平行！"
```

### 清理
- FadeOut: 所有内容（除 author_info）

---

## Scene 7: 总结 + 片尾 (68-85秒)
**目的**: 总结关键知识点，引导关注

### 元素
1. 总结卡片
2. 关键公式
3. 作者信息
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 68.0s | 卡片1："向量加法 - 首尾相接" | `FadeIn(card_1)` | 0.8s |
| 68.8s | 卡片2："向量数乘 - 伸缩变换" | `FadeIn(card_2)` | 0.8s |
| 69.6s | 卡片3："基底分解 - →a=λ₁→e₁+λ₂→e₂" | `FadeIn(card_3)` | 0.8s |
| 70.4s | 卡片4："平行向量 - →a=λ→b" | `FadeIn(card_4)` | 0.8s |
| 71.2s | 所有卡片闪烁 | `Flash(all_cards)` | 0.6s |
| 71.8s | 关键提示："理解向量，掌握线性代数基础！" | `Write(key_point)` | 1.2s |
| 73.0s | 作者信息放大 | `Transform(author_info, author_name)` | 0.8s |
| 73.8s | 关注提示 | `FadeIn(follow_text)` | 0.8s |
| 74.6s | 装饰动画（箭头旋转） | `Rotate(arrows)` | 2.0s |
| 76.6s | 全部淡出 | `FadeOut(all)` | 1.0s |

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 类型 | 备注 |
|------|---------|---------|------|------|
| author_info | Scene 1 | Scene 7 | Text | 始终保留 |
| axes | Scene 4 | Scene 6 | Axes | 坐标系 |
| arrow_a | Scene 2 | Scene 3 | Arrow | 向量a |
| arrow_b | Scene 2 | Scene 3 | Arrow | 向量b |
| arrow_sum | Scene 2 | Scene 2 | Arrow | 和向量 |
| arrow_e1 | Scene 4 | Scene 6 | Arrow | 基向量e1 |
| arrow_e2 | Scene 4 | Scene 6 | Arrow | 基向量e2 |
| arrow_2a | Scene 3 | Scene 3 | Arrow | 数乘2a |
| arrow_neg_a | Scene 3 | Scene 3 | Arrow | 数乘-a |
| parallelogram | Scene 2 | Scene 2 | DashedLine | 平行四边形 |
| formula_decomposition | Scene 5 | Scene 5 | MathTex | 分解公式 |
| summary_cards | Scene 7 | Scene 7 | VGroup | 总结卡片 |

---

## 关键技术难点

### 1. 向量符号的LaTeX表示
```python
# ❌ 错误：直接使用→符号
label = MathTex(r"→a")  # 可能不显示

# ✅ 正确：使用 \vec 命令
label = MathTex(r"\vec{a}")

# ✅ 更好：使用 \overrightarrow
label = MathTex(r"\overrightarrow{a}")
```

### 2. Arrow vs Vector
```python
# Manim的Arrow类
arrow = Arrow(start=ORIGIN, end=point, color=RED, buff=0)

# 或者使用Vector（专门用于向量）
vector = Vector(direction=point, color=RED)

# Vector会自动从原点开始
```

### 3. 向量加法的平移
```python
# 方法1：创建新的Arrow
arrow_b_shifted = Arrow(
    start=arrow_a.get_end(),
    end=arrow_a.get_end() + vec_b,
    color=COLOR_VECTOR_B,
    buff=0
)

# 方法2：使用shift
arrow_b_copy = arrow_b.copy().shift(vec_a)
```

### 4. 基向量分解的精确计算
```python
# 解线性方程组
# vec_a = lambda1 * e1 + lambda2 * e2
A_matrix = np.column_stack([e1[:2], e2[:2]])
lambdas = np.linalg.solve(A_matrix, vec_a[:2])

# 验证
reconstructed = lambdas[0] * e1 + lambdas[1] * e2
assert np.allclose(vec_a, reconstructed), "分解验证失败"
```

---

## 预期效果验证

运行 verify_geometry.py 应该输出：
```
✓ 向量加法验证: a + b = b + a
✓ 数乘验证: λa 方向和长度正确
✓ 基底不共线验证通过
✓ 向量分解验证: λ₁e₁ + λ₂e₂ = a
✓ 平行向量验证: a = λb
✓ 所有元素在安全边界内
✓ 所有向量关系验证通过！
```

---

## 总时长分配

| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1: 开场 | 4s | 4s |
| Scene 2: 向量加法 | 14s | 18s |
| Scene 3: 向量数乘 | 14s | 32s |
| Scene 4: 基底概念 | 10s | 42s |
| Scene 5: 向量分解 | 16s | 58s |
| Scene 6: 平行向量 | 10s | 68s |
| Scene 7: 总结 | 9s | 77s |
| **总计** | **77s** | - |

留出 3-8s 缓冲时间，总时长控制在 80-85s 以内。