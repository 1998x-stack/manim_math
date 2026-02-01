# 布罗卡点 (Brocard Points) - 动画分镜脚本

## 元信息
- 目标时长: 75-90 秒
- 场景数量: 8 个
- 难度等级: 高中/竞赛
- 目标受众: 高中生及几何爱好者

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"          # 蓝色 - 三角形
COLOR_BROCARD_1 = "#e74c3c"        # 红色 - 第一布罗卡点 Ω
COLOR_BROCARD_2 = "#f39c12"        # 橙色 - 第二布罗卡点 Ω'
COLOR_ANGLE = "#2ecc71"            # 绿色 - 布罗卡角
COLOR_CIRCLE = "#9b59b6"           # 紫色 - 辅助圆
COLOR_AUXILIARY = GRAY_B           # 灰色 - 辅助线
COLOR_HIGHLIGHT = YELLOW           # 黄色 - 高亮
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 三角形顶点 | 给定坐标 | A, B, C | 使用非等边三角形展示一般性 |
| 边长 | 欧氏距离 | a, b, c | a=BC, b=CA, c=AB |
| 三角形面积 | 海伦公式或叉积 | area | 用于计算布罗卡角 |
| 布罗卡角 ω | cot(ω) = (a²+b²+c²)/(4×area) | omega | 核心参数 |
| 第一布罗卡点 Ω | 三个特殊圆的交点 | brocard_1 | ∠ΩAB = ∠ΩBC = ∠ΩCA = ω |
| 第二布罗卡点 Ω' | 三个特殊圆的交点 | brocard_2 | ∠Ω'BA = ∠Ω'CB = ∠Ω'AC = ω |
| 外接圆圆心 | 三边垂直平分线交点 | circumcenter | 用于验证 |
| 重心 | (A+B+C)/3 | centroid | 参考点 |

## 关键几何计算

### 1. 布罗卡角计算
```python
# 使用余切公式
s = (a + b + c) / 2  # 半周长
area = sqrt(s * (s-a) * (s-b) * (s-c))  # 海伦公式
cot_omega = (a**2 + b**2 + c**2) / (4 * area)
omega = arctan(1 / cot_omega)  # 弧度制
```

### 2. 第一布罗卡点构造
需要找三个圆的交点：
- 圆1: 过A, B且与BC相切于B
- 圆2: 过B, C且与CA相切于C  
- 圆3: 过C, A且与AB相切于A

**计算步骤**:
1. 使用角度关系推导点的位置
2. 利用等角条件: ∠ΩAB = ∠ΩBC = ∠ΩCA = ω

### 3. 验证几何约束
```python
# 验证等角性质
angle_OAB = angle_between(Omega, A, B)
angle_OBC = angle_between(Omega, B, C)
angle_OCA = angle_between(Omega, C, A)
assert abs(angle_OAB - omega) < epsilon
assert abs(angle_OBC - omega) < epsilon
assert abs(angle_OCA - omega) < epsilon
```

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 抓住注意力，引出布罗卡点的神秘性

### 元素
1. 作者标识 (顶部)
2. 钩子问题
3. 三角形轮廓
4. 两个神秘点闪烁

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2, run_time=0.3)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` |
| 1.1s | 三角形创建 | `Create(triangle, run_time=1.0)` |
| 2.1s | 两个点闪烁 | `Flash(dot, color=RED)` |
| 3.5s | 提示文字 | `FadeIn(hint, shift=UP*0.3)` |
| 4.5s | 等待 | `Wait(0.5)` |

### 文案
- 钩子: "一个三角形中隐藏着神秘的孪生点"
- 提示: "它们满足优美的等角性质"

### 清理
- FadeOut: hook_text, hint
- 保留: triangle, author_info, 两个点变淡

---

## Scene 2: 定义第一布罗卡点 (5-18秒)
**目的**: 介绍第一布罗卡点及其等角性质

### 元素
1. 标题: "第一布罗卡点 Ω"
2. 定义文字
3. 三条有向线段: ΩA, ΩB, ΩC
4. 三个角弧: ∠ΩAB, ∠ΩBC, ∠ΩCA
5. 角度标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 5.0s | 标题出现 | `Write(title, run_time=0.8)` |
| 5.8s | 第一布罗卡点放大 | `omega_1.animate.scale(2).set_color(RED)` |
| 6.5s | 连线ΩA | `Create(line_OA)` |
| 7.2s | 标记∠ΩAB | `Create(angle_OAB)` |
| 7.8s | 显示角度值 | `FadeIn(angle_label)` |
| 8.5s | 连线ΩB | `Create(line_OB)` |
| 9.2s | 标记∠ΩBC | `Create(angle_OBC)` |
| 9.8s | 显示角度值 | `FadeIn(angle_label)` |
| 10.5s | 连线ΩC | `Create(line_OC)` |
| 11.2s | 标记∠ΩCA | `Create(angle_OCA)` |
| 11.8s | 显示角度值 | `FadeIn(angle_label)` |
| 12.5s | 高亮三个角 | `角弧同时闪烁` |
| 13.5s | 等角公式 | `MathTex("\angle\Omega AB = \angle\Omega BC = \angle\Omega CA = \omega")` |
| 15.0s | 停留理解 | `Wait(2.0)` |

### 几何约束
- 必须精确计算Ω的位置，确保三个角确实相等
- 角弧方向必须正确（使用quadrant参数）
- 角度标注位置不重叠

### 清理
- FadeOut: 连线, 角弧, 部分标注
- 保留: triangle, omega_1点, title缩小

---

## Scene 3: 定义第二布罗卡点 (18-28秒)
**目的**: 介绍第二布罗卡点的对称性质

### 元素
1. 副标题: "第二布罗卡点 Ω'"
2. 三条有向线段: Ω'A, Ω'B, Ω'C
3. 三个角弧: ∠Ω'BA, ∠Ω'CB, ∠Ω'AC
4. 对比说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 18.0s | 副标题出现 | `Write(subtitle)` |
| 18.8s | 第二布罗卡点放大 | `omega_2.animate.scale(2).set_color(ORANGE)` |
| 19.5s | 连线并标记三个角 | `依次Create` |
| 23.0s | 等角公式 | `MathTex("\angle\Omega' BA = \angle\Omega' CB = \angle\Omega' AC = \omega")` |
| 24.5s | 对比动画 | `两个点同时闪烁，显示对称性` |
| 26.0s | 停留 | `Wait(2.0)` |

### 清理
- FadeOut: 所有连线和角弧
- 保留: triangle, omega_1, omega_2

---

## Scene 4: 布罗卡角公式 (28-40秒)
**目的**: 展示布罗卡角的计算公式

### 元素
1. 标题: "布罗卡角 ω"
2. 公式1: cot ω = cot A + cot B + cot C
3. 公式2: cot ω = (a² + b² + c²) / (4Δ)
4. 数值示例

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 28.0s | 标题出现 | `Write(title)` |
| 28.8s | 公式1淡入 | `FadeIn(formula_1, shift=UP)` |
| 30.5s | 标注三角形内角 | `显示A, B, C角度` |
| 32.0s | 公式2淡入 | `TransformMatchingTex(formula_1, formula_2)` |
| 34.0s | 标注边长和面积 | `显示a, b, c, Δ` |
| 36.0s | 计算示例 | `逐步显示数值代入` |
| 38.0s | 得到ω值 | `ω ≈ 23.4°` |
| 39.0s | 停留 | `Wait(1.0)` |

### 清理
- FadeOut: 公式, 标注
- 保留: triangle, omega_1, omega_2, ω值显示

---

## Scene 5: 构造方法展示 (40-55秒)
**目的**: 展示如何尺规作图构造第一布罗卡点

### 元素
1. 标题: "如何找到布罗卡点?"
2. 辅助圆1: 过A, B且与BC相切于B
3. 辅助圆2: 过B, C且与CA相切于C
4. 交点即为Ω

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 40.0s | 标题 | `Write(title)` |
| 41.0s | 高亮边BC | `BC边变色` |
| 41.5s | 作圆1 | `Create(circle_1)` 过A, B切BC于B |
| 43.0s | 说明文字 | "过A, B且切BC于B的圆" |
| 44.5s | 高亮边CA | `CA边变色` |
| 45.0s | 作圆2 | `Create(circle_2)` 过B, C切CA于C |
| 46.5s | 说明文字 | "过B, C且切CA于C的圆" |
| 48.0s | 标记交点 | `Flash(intersection)` |
| 49.0s | 确认为Ω | `Ω点放大并标注` |
| 50.5s | 验证等角 | `快速显示三个角相等` |
| 52.5s | 停留 | `Wait(2.0)` |

### 几何约束
- 圆必须精确计算，确保：
  1. 过指定两点
  2. 与指定边相切于指定点
- 交点必须精确计算，不能臆想

### 清理
- FadeOut: 两个圆, 说明文字
- 保留: triangle, omega_1, omega_2

---

## Scene 6: 特殊三角形示例 (55-65秒)
**目的**: 展示等边三角形中的特殊性质

### 元素
1. 等边三角形
2. 计算: ω = 30°
3. 布罗卡点与重心重合

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 55.0s | 变换为等边三角形 | `Transform(triangle, equilateral)` |
| 56.5s | 计算公式 | `cot ω = 3 cot 60° = √3` |
| 58.0s | 得到ω=30° | `FadeIn(result)` |
| 59.0s | 布罗卡点移动到重心 | `omega_1.animate.move_to(centroid)` |
| 60.0s | 标注重心 | `"布罗卡点 = 重心"` |
| 61.5s | 四心合一提示 | `"等边三角形: 四心合一"` |
| 63.5s | 停留 | `Wait(1.5)` |

### 清理
- FadeOut: 等边三角形相关标注
- 变回原三角形

---

## Scene 7: 性质总结 (65-75秒)
**目的**: 总结布罗卡点的关键性质

### 元素
1. 特性卡片×4
2. 三角形及两个布罗卡点

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 65.0s | 标题 | `"布罗卡点的性质"` |
| 66.0s | 卡片1滑入 | `"等角共轭点"` |
| 67.2s | 卡片2滑入 | `"布罗卡角 0 < ω ≤ 30°"` |
| 68.4s | 卡片3滑入 | `"到三顶点距离关系"` |
| 69.6s | 卡片4滑入 | `"与外接圆、重心的关系"` |
| 71.0s | 高亮重点 | `"优美的几何对称性"` |
| 73.0s | 停留 | `Wait(2.0)` |

### 清理
- 全部淡出准备结尾

---

## Scene 8: 片尾关注 (75-80秒)
**目的**: 引导关注

### 元素
1. 作者信息放大
2. 关注文案
3. 装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 75.0s | 作者名放大 | `Transform(author_info, author_large)` |
| 76.0s | ID显示 | `FadeIn(author_id)` |
| 77.0s | 关注文案 | `"关注我，探索更多几何奥秘!"` |
| 78.0s | 三角形装饰旋转 | `Rotate(decorations)` |
| 79.0s | 全部淡出 | `FadeOut(ALL)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| triangle | Scene 1 | Scene 8 | 主三角形，贯穿全程 |
| author_info | Scene 1 | Scene 8 | 顶部作者标识 |
| omega_1 | Scene 1 | Scene 8 | 第一布罗卡点 |
| omega_2 | Scene 1 | Scene 8 | 第二布罗卡点 |
| angle_arcs | Scene 2 | Scene 2 | 角弧，临时 |
| auxiliary_circles | Scene 5 | Scene 5 | 辅助圆，临时 |
| property_cards | Scene 7 | Scene 7 | 性质卡片，临时 |

---

## 关键验证点

### 几何验证
```python
def verify_brocard_geometry():
    # 1. 验证第一布罗卡点等角性质
    angle_1 = angle_at_vertex(omega_1, A, B)
    angle_2 = angle_at_vertex(omega_1, B, C)
    angle_3 = angle_at_vertex(omega_1, C, A)
    assert abs(angle_1 - omega) < 1e-6
    assert abs(angle_2 - omega) < 1e-6
    assert abs(angle_3 - omega) < 1e-6
    
    # 2. 验证第二布罗卡点等角性质
    angle_4 = angle_at_vertex(omega_2, B, A)
    angle_5 = angle_at_vertex(omega_2, C, B)
    angle_6 = angle_at_vertex(omega_2, A, C)
    assert abs(angle_4 - omega) < 1e-6
    assert abs(angle_5 - omega) < 1e-6
    assert abs(angle_6 - omega) < 1e-6
    
    # 3. 验证布罗卡角计算
    cot_omega_calc = (a**2 + b**2 + c**2) / (4 * area)
    omega_calc = np.arctan(1 / cot_omega_calc)
    assert abs(omega - omega_calc) < 1e-6
    
    print("✓ 布罗卡点几何验证通过")
```

### 动画节奏检查
- 每个关键概念停留 1.5-2.5 秒
- 复杂计算过程分步展示
- 总时长控制在 75-90 秒

---

## 渲染配置

```bash
# 预览
manim -pql brocard_points.py BrocardPointsScene

# 高质量输出
manim -qh brocard_points.py BrocardPointsScene

# TikTok竖屏 (1080×1920)
# 已在config中设置
```

---

## 备注
- 布罗卡点的精确计算较为复杂，需要仔细推导
- 等角性质是核心，必须通过动画清晰展示
- 辅助圆的构造是难点，需要精确计算切点和圆心
- 等边三角形的特例很有教学价值