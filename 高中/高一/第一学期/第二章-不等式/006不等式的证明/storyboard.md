# 不等式的证明 - 动画分镜脚本

## 元信息
- 目标时长: 60-90 秒
- 场景数量: 7 个
- 难度等级: 中等
- 目标观众: 高一学生

## 颜色配置
```python
COLOR_PROOF_METHOD = BLUE
COLOR_FORMULA = WHITE
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
BACKGROUND_COLOR = "#1a1a2e"
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 示例a值 | 3 | self.example_a |
| 示例b值 | 2 | self.example_b |
| a-b值 | a-b | self.diff_ab |
| ab值 | a*b | self.prod_ab |

---

## Scene 1: 开场 (3-4秒)
**目的**: 钩子 + 引出不等式证明的概念

### 元素
1. 作者标识 (顶部小字)
2. 主标题 (不等式的证明)
3. 钩子问题 ("如何证明a² + b² ≥ 2ab？")

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 标题书写 | `Write(title)` |
| 1.1s | 钩子问题出现 | `Write(hook_question)` |
| 2.1s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_question
- 保留: title, author_info

---

## Scene 2: 比较法证明 (8-10秒)
**目的**: 演示作差比较法 (a-b≥0 ⟺ a≥b)

### 元素
1. 比较法公式展示
2. 证明示例 a²+b² ≥ 2ab
3. 作差 a²+b²-2ab = (a-b)² ≥ 0

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 显示比较法原理 | `Write(comparison_principle: a≥b ⟺ a-b≥0)` |
| 1.0s | 显示待证明不等式 | `Write(inequality_to_prove: a²+b² ≥ 2ab)` |
| 2.0s | 作差运算 | `Transform(inequality, diff_expr: a²+b²-2ab)` |
| 3.0s | 因式分解 | `Transform(diff_expr, factored: (a-b)²)` |
| 4.0s | 说明平方非负 | `Write(square_non_negative: (a-b)² ≥ 0)` |
| 5.0s | 得出结论 | `Write(conclusion: ∴ a²+b² ≥ 2ab)` |

### 清理
- 保留: principle, conclusion

---

## Scene 3: 综合法证明 (8-10秒)
**目的**: 演示从已知条件出发逐步推导

### 元素
1. 综合法思路展示
2. 基于基本不等式推导其他不等式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 综合法原理 | `Write(synthetic_method: 已知→...→结论)` |
| 1.0s | 基础不等式 | `Write(basic_inequality: (a-b)² ≥ 0)` |
| 2.0s | 展开平方 | `Transform(basic_inequality, expanded: a²-2ab+b² ≥ 0)` |
| 3.0s | 移项 | `Transform(expanded, rearranged: a²+b² ≥ 2ab)` |
| 4.0s | 推广形式 | `Write(general_form: a²+b² ≥ 2|ab|)` |

### 清理
- 保留: general_form

---

## Scene 4: 分析法证明 (8-10秒)
**目的**: 演示从结论出发寻求充分条件

### 元素
1. 分析法思路展示
2. 逆向推理过程

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 分析法原理 | `Write(analytic_method: 结论←...←已知)` |
| 1.0s | 待证结论 | `Write(target: a/b + b/a ≥ 2, a,b同号)` |
| 2.0s | 通分变换 | `Transform(target, transformed: (a²+b²)/ab ≥ 2)` |
| 3.0s | 乘以ab | `Transform(transformed, multiplied: a²+b² ≥ 2ab)` |
| 4.0s | 移项 | `Transform(multiplied, rearranged: a²-2ab+b² ≥ 0)` |
| 5.0s | 因式分解 | `Transform(rearranged, factored: (a-b)² ≥ 0)` |

### 清理
- 保留: factored_result

---

## Scene 5: 反证法证明 (6-8秒)
**目的**: 演示假设结论不成立推出矛盾

### 元素
1. 反证法思路展示
2. 矛盾推导过程

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 反证法原理 | `Write(contradiction_method: ¬结论→...→矛盾)` |
| 1.0s | 假设相反 | `Write(assumption: 假设a²+b² < 2ab)` |
| 2.0s | 移项变形 | `Transform(assumption, rearranged: a²-2ab+b² < 0)` |
| 3.0s | 因式分解 | `Transform(rearranged, factored: (a-b)² < 0)` |
| 4.0s | 显示矛盾 | `Write(contradiction: 但这与(a-b)²≥0矛盾!)` |
| 5.0s | 得出原结论 | `Write(original_conclusion: ∴ a²+b² ≥ 2ab)` |

### 清理
- 保留: original_conclusion

---

## Scene 6: 放缩法证明 (6-8秒)
**目的**: 演示通过放大或缩小证明不等式

### 元素
1. 放缩法思路展示
2. 具体示例演示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 放缩法原理 | `Write(estimate_method: 适当放大/缩小)` |
| 1.0s | 示例不等式 | `Write(example: 1/(n²) < 1/(n(n-1)), n≥2)` |
| 2.0s | 右侧变形 | `Transform(example[2], equivalent: = 1/(n-1) - 1/n)` |
| 3.0s | 应用技巧 | `Write(technique: 裂项相消)` |
| 4.0s | 累加结果 | `Write(sum_result: Σ1/k² < 2-1/n)` |

### 清理
- 保留: sum_result

---

## Scene 7: 总结回顾 (4-5秒)
**目的**: 回顾各种证明方法 + 片尾关注

### 元素
1. 五种证明方法总结
2. 作者信息
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 方法总结 | `Write(method_summary: 1.比较法 2.综合法 3.分析法 4.反证法 5.放缩法)` |
| 1.5s | 作者信息出现 | `FadeIn(final_author_info)` |
| 2.5s | 关注提示 | `Write(follow_hint: 关注我，获得更多数学技巧!)` |
| 3.5s | 等待结束 | `Wait(1.0)` |

### 清理
- 保留: all

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| title | Scene 1 | End | 主标题 |
| hook_question | Scene 1 | Scene 1 | 钩子问题 |
| comparison_principle | Scene 2 | End | 比较法原理 |
| synthetic_method | Scene 3 | End | 综合法原理 |
| analytic_method | Scene 4 | End | 分析法原理 |
| contradiction_method | Scene 5 | End | 反证法原理 |
| estimate_method | Scene 6 | End | 放缩法原理 |
| method_summary | Scene 7 | End | 方法总结 |

---

## 数学公式
- 比较法: a ≥ b ⟺ a - b ≥ 0
- 作商法: a ≥ b > 0 ⟺ a/b ≥ 1 (b > 0)
- 基本不等式: a² + b² ≥ 2ab
- 柯西不等式: (a² + b²)(c² + d²) ≥ (ac + bd)²

## 相关知识点
- 比较法
- 综合法
- 分析法
- 反证法
- 放缩法
