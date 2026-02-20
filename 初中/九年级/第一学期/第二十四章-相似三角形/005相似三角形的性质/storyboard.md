# 相似三角形的性质 - 动画分镜脚本

## 元信息
- **目标时长**: 60-75秒
- **场景数量**: 7个
- **难度等级**: 中等
- **年级**: 九年级第一学期
- **知识点**: 相似三角形的性质（对应边成比例、对应高/中线/角平分线比例、周长比、面积比）

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 原三角形
COLOR_SECONDARY = "#e74c3c"    # 红色 - 相似三角形
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调元素
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_FORMULA = WHITE          # 白色 - 公式
```

## 几何预计算清单

### 原三角形 ABC (较大)
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 顶点A | 基准点 | `self.A` | [-2.5, 1, 0] |
| 顶点B | 基准点 | `self.B` | [2.5, -1, 0] |
| 顶点C | 基准点 | `self.C` | [0, 2.5, 0] |
| 边长a | `norm(B-C)` | `self.a` | BC边长 |
| 边长b | `norm(C-A)` | `self.b` | CA边长 |
| 边长c | `norm(A-B)` | `self.c` | AB边长 |
| 周长 | `a+b+c` | `self.perimeter` | - |
| 面积 | 海伦公式 | `self.area` | - |
| 高hA | 从A到BC的垂足 | `self.h_A`, `self.foot_A` | 对BC的高 |
| 高hB | 从B到CA的垂足 | `self.h_B`, `self.foot_B` | 对CA的高 |
| 中线mA | (B+C)/2 | `self.M_BC`, `self.m_A` | A到BC中点 |
| 角平分线lA | 角平分线定理 | `self.bisector_A_point`, `self.l_A` | ∠A的平分线长 |

### 相似三角形 A'B'C' (较小，相似比k=0.6)
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 相似比 | 常数 | `self.k = 0.6` | - |
| 顶点A' | 基准点 | `self.A_prime` | 独立定位 |
| 顶点B' | A' + k*(B-A) 旋转 | `self.B_prime` | 保持形状相似 |
| 顶点C' | A' + k*(C-A) 旋转 | `self.C_prime` | 保持形状相似 |
| 边长a' | `k * a` | `self.a_prime` | - |
| 边长b' | `k * b` | `self.b_prime` | - |
| 边长c' | `k * c` | `self.c_prime` | - |
| 高h'A | `k * h_A` | `self.h_A_prime` | - |
| 中线m'A | `k * m_A` | `self.m_A_prime` | - |
| 角平分线l'A | `k * l_A` | `self.l_A_prime` | - |

### 验证项
- [ ] 对应角相等（验证三个角）
- [ ] 对应边比例 = k
- [ ] 高之比 = k
- [ ] 中线之比 = k
- [ ] 角平分线之比 = k
- [ ] 周长比 = k
- [ ] 面积比 = k²

---

## Scene 1: 开场钩子 (0-4秒)
**目的**: 抓住注意力，引出"相似"概念

### 元素
1. 作者标识（顶部）
2. 钩子问题（大字）："两个形状一样的三角形，有什么神奇的关系？"
3. 两个三角形（一大一小，形状相同）

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子问题书写 | `Write(hook_text)` | 1.0s |
| 1.3s | 大三角形创建 | `Create(triangle_ABC)` | 0.8s |
| 2.1s | 小三角形创建（不同位置） | `Create(triangle_A_prime)` | 0.8s |
| 2.9s | 两个三角形同时闪烁 | `Flash(...)` | 0.6s |
| 3.5s | 等待 | `Wait(0.5)` | 0.5s |

### 清理
- FadeOut: hook_text
- 保留: triangle_ABC, triangle_A_prime, author_info

---

## Scene 2: 定义相似三角形 (4-10秒)
**目的**: 介绍相似的基本概念和记号

### 元素
1. 标题："相似三角形"
2. 定义文字："形状相同，大小可以不同"
3. 数学符号："△ABC ∽ △A'B'C'"
4. 对应角标记（角弧）
5. 对应边标记（相同颜色）

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 4.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 4.5s | 定义文字书写 | `Write(definition)` | 1.0s |
| 5.5s | 相似符号书写 | `Write(similarity_symbol)` | 0.8s |
| 6.3s | 标记对应角（依次闪烁） | `Flash(angle_A), Flash(angle_A_prime)...` | 1.5s |
| 7.8s | 标记对应边（颜色变化） | `Set color...` | 1.2s |
| 9.0s | 等待理解 | `Wait(1.0)` | 1.0s |

### 清理
- FadeOut: title, definition, similarity_symbol
- 保留: 两个三角形及标记

---

## Scene 3: 性质1 - 对应边成比例 (10-20秒)
**目的**: 展示并验证对应边成比例关系

### 元素
1. 标题："性质1：对应边成比例"
2. 边长标签（用 Brace 标注）
3. 公式：`a'/a = b'/b = c'/c = k`
4. 数值验证（具体数字）

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 10.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 10.5s | 大三角形边长标注 | `Brace + label` | 1.2s |
| 11.7s | 小三角形边长标注 | `Brace + label` | 1.2s |
| 12.9s | 公式淡入 | `FadeIn(formula)` | 0.8s |
| 13.7s | 计算展示（具体数值） | `Transform` | 1.5s |
| 15.2s | 结论："相似比 k = 0.6" | `Write(conclusion)` | 1.0s |
| 16.2s | 强调闪烁 | `Flash(formula)` | 0.5s |
| 16.7s | 等待理解 | `Wait(2.0)` | 2.0s |

### 注意事项
- 使用 DecimalNumber 显示具体数值
- 计算要精确到小数点后1位

### 清理
- FadeOut: title, all braces, labels, formula, conclusion
- 保留: 两个三角形

---

## Scene 4: 性质2 - 对应高之比 (20-32秒)
**目的**: 展示对应高的比例关系

### 元素
1. 标题："性质2：对应高之比 = k"
2. 从A到BC的高线（虚线）
3. 从A'到B'C'的高线（虚线）
4. 高的长度标注
5. 比例公式：`h'_A / h_A = k`

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 20.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 20.5s | 大三角形：BC边高亮 | `BC.set_color(YELLOW)` | 0.4s |
| 20.9s | 绘制高线（A到BC） | `Create(altitude_A)` | 1.0s |
| 21.9s | 垂直符号标记 | `Create(right_angle_mark)` | 0.4s |
| 22.3s | 高度标注 | `Brace + label` | 0.8s |
| 23.1s | 小三角形：B'C'边高亮 | `B_prime_C_prime.set_color(YELLOW)` | 0.4s |
| 23.5s | 绘制高线（A'到B'C'） | `Create(altitude_A_prime)` | 1.0s |
| 24.5s | 高度标注 | `Brace + label` | 0.8s |
| 25.3s | 比例公式淡入 | `FadeIn(formula)` | 0.8s |
| 26.1s | 数值计算展示 | `Transform to specific values` | 1.5s |
| 27.6s | 验证："0.6 = k ✓" | `Write(verification)` | 1.0s |
| 28.6s | 等待理解 | `Wait(2.0)` | 2.0s |

### 几何计算要点
```python
# 高的垂足精确计算
foot_A = GeometryCalculator.foot_of_perpendicular(A, B, C)
h_A = np.linalg.norm(A - foot_A)
```

### 清理
- FadeOut: title, altitudes, marks, formula, verification
- 恢复: BC, B'C' 颜色为原色
- 保留: 两个三角形

---

## Scene 5: 性质3 - 对应中线/角平分线之比 (32-42秒)
**目的**: 快速展示中线和角平分线的比例（简化处理）

### 元素
1. 标题："对应中线之比 = 角平分线之比 = k"
2. 中线示意（从A到BC中点M）
3. 对应中线（从A'到B'C'中点M'）
4. 简化公式

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 32.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 32.5s | BC中点标记 | `Dot(M) + label` | 0.5s |
| 33.0s | 绘制中线AM | `Create(median_A)` | 0.8s |
| 33.8s | B'C'中点标记 | `Dot(M_prime) + label` | 0.5s |
| 34.3s | 绘制中线A'M' | `Create(median_A_prime)` | 0.8s |
| 35.1s | 公式："m'_A / m_A = k" | `Write(formula)` | 1.0s |
| 36.1s | 同样地，角平分线也是 | `FadeIn(note)` | 1.5s |
| 37.6s | 等待理解 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: 所有元素（除三角形）
- 保留: 两个三角形

---

## Scene 6: 性质4 - 周长比和面积比 (42-55秒)
**目的**: 展示周长比和面积比的关系（重点）

### 元素
1. 标题："周长比 = k，面积比 = k²"
2. 周长计算展示
3. 面积填充动画
4. 公式对比

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 42.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 42.5s | 周长公式："L = a+b+c" | `Write(perimeter_formula)` | 1.0s |
| 43.5s | 大三角形周长计算 | `Transform to value` | 1.0s |
| 44.5s | 小三角形周长计算 | `Transform to value` | 1.0s |
| 45.5s | 比值："L'/L = k" | `Write(ratio)` | 1.0s |
| 46.5s | 过渡："而面积呢？" | `FadeIn(transition)` | 0.8s |
| 47.3s | 大三角形填充（半透明） | `FadeIn(fill_ABC)` | 0.8s |
| 48.1s | 小三角形填充（半透明） | `FadeIn(fill_A_prime)` | 0.8s |
| 48.9s | 面积比公式："S'/S = k²" | `Write(area_formula)` | 1.2s |
| 50.1s | 数值验证："0.36 = 0.6²" | `Write(verification)` | 1.0s |
| 51.1s | 强调："注意是平方!" | `Flash + note` | 1.5s |
| 52.6s | 等待理解 | `Wait(2.0)` | 2.0s |

### 几何计算要点
```python
# 使用海伦公式计算面积
s = (a + b + c) / 2
area = sqrt(s * (s-a) * (s-b) * (s-c))
```

### 清理
- FadeOut: 所有公式和填充
- 保留: 两个三角形

---

## Scene 7: 总结 + 片尾 (55-75秒)
**目的**: 总结四大性质，引导关注

### 元素
1. 性质总结表格
2. 关键公式汇总
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 55.0s | 三角形缩小并移至顶部 | `scale + move_to` | 1.0s |
| 56.0s | 总结卡片1："对应边成比例 = k" | `FadeIn(card_1)` | 0.8s |
| 56.8s | 总结卡片2："对应高/中线/角平分线之比 = k" | `FadeIn(card_2)` | 0.8s |
| 57.6s | 总结卡片3："周长比 = k" | `FadeIn(card_3)` | 0.8s |
| 58.4s | 总结卡片4："面积比 = k²" | `FadeIn(card_4)` | 0.8s |
| 59.2s | 四张卡片同时闪烁 | `Flash(all_cards)` | 0.6s |
| 59.8s | 关键提示："记住 k² !" | `Write(key_point)` | 1.0s |
| 60.8s | 作者信息放大 | `Transform(author)` | 0.8s |
| 61.6s | 关注提示："关注我，学更多数学技巧!" | `FadeIn(follow_text)` | 1.0s |
| 62.6s | 装饰动画（三角形旋转） | `Rotate(decorations)` | 2.0s |
| 64.6s | 全部淡出 | `FadeOut(all)` | 1.0s |

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 类型 | 备注 |
|------|---------|---------|------|------|
| author_info | Scene 1 | Scene 7 | Text | 始终保留 |
| triangle_ABC | Scene 1 | Scene 7 | Polygon | 主三角形（大） |
| triangle_A_prime | Scene 1 | Scene 7 | Polygon | 相似三角形（小） |
| hook_text | Scene 1 | Scene 1 | Text | 钩子问题 |
| angle_marks | Scene 2 | Scene 2 | VGroup | 角度标记 |
| edge_colors | Scene 2 | Scene 6 | - | 边颜色标记 |
| altitude_A | Scene 4 | Scene 4 | DashedLine | 高线 |
| altitude_A_prime | Scene 4 | Scene 4 | DashedLine | 对应高线 |
| median_A | Scene 5 | Scene 5 | Line | 中线 |
| median_A_prime | Scene 5 | Scene 5 | Line | 对应中线 |
| fill_ABC | Scene 6 | Scene 6 | Polygon(fill) | 面积填充 |
| fill_A_prime | Scene 6 | Scene 6 | Polygon(fill) | 对应面积填充 |
| summary_cards | Scene 7 | Scene 7 | VGroup | 总结卡片 |

---

## 关键技术难点

### 1. 相似三角形的精确构造
```python
# 确保形状完全相似：先缩放，再旋转，最后平移
def construct_similar_triangle(original_A, original_B, original_C, scale_factor, rotation_angle, position):
    # Step 1: 以原点为基准缩放
    scaled_A = original_A * scale_factor
    scaled_B = original_B * scale_factor
    scaled_C = original_C * scale_factor
    
    # Step 2: 旋转（可选）
    rotation_matrix = np.array([
        [np.cos(rotation_angle), -np.sin(rotation_angle), 0],
        [np.sin(rotation_angle), np.cos(rotation_angle), 0],
        [0, 0, 1]
    ])
    rotated_A = rotation_matrix @ scaled_A
    rotated_B = rotation_matrix @ scaled_B
    rotated_C = rotation_matrix @ scaled_C
    
    # Step 3: 平移到目标位置
    offset = position - rotated_A
    final_A = rotated_A + offset
    final_B = rotated_B + offset
    final_C = rotated_C + offset
    
    return final_A, final_B, final_C
```

### 2. 高线的精确计算
```python
# 使用投影公式
def calculate_altitude(vertex, base_start, base_end):
    foot = GeometryCalculator.foot_of_perpendicular(vertex, base_start, base_end)
    height = np.linalg.norm(vertex - foot)
    return foot, height
```

### 3. 面积的精确计算
```python
# 海伦公式
def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = np.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
```

---

## 预期效果验证

运行 verify_geometry.py 应该输出：
```
✓ 对应边比例验证: a'/a = 0.600, b'/b = 0.600, c'/c = 0.600
✓ 相似比 k = 0.600
✓ 高之比验证: h'_A/h_A = 0.600 = k
✓ 中线之比验证: m'_A/m_A = 0.600 = k
✓ 周长比验证: L'/L = 0.600 = k
✓ 面积比验证: S'/S = 0.360 = k² = 0.600²
✓ 所有几何关系验证通过！
```

---

## 总时长分配

| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1: 开场 | 4s | 4s |
| Scene 2: 定义 | 6s | 10s |
| Scene 3: 对应边 | 10s | 20s |
| Scene 4: 对应高 | 12s | 32s |
| Scene 5: 中线/角平分线 | 10s | 42s |
| Scene 6: 周长/面积 | 13s | 55s |
| Scene 7: 总结 | 10s | 65s |
| **总计** | **65s** | - |

留出 5-10s 缓冲时间，总时长控制在 70-75s 以内。