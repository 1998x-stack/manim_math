# 整式的除法 - Manim动画分镜脚本

<!-- /root/code/sss/media/videos/polynomial_division/1920p60/PolynomialDivision.mp4 -->
## 元信息
- 目标时长: 60-75秒
- 场景数量: 6个
- 难度等级: 七年级（初中）
- 知识点: 单项式除以单项式、多项式除以单项式

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"       # 蓝色 - 主要公式
COLOR_SECONDARY = "#e74c3c"     # 红色 - 系数
COLOR_HIGHLIGHT = "#f39c12"     # 橙色 - 高亮部分
COLOR_COEFFICIENT = "#e74c3c"   # 红色 - 系数
COLOR_VARIABLE = "#2ecc71"      # 绿色 - 变量
COLOR_EXPONENT = "#9b59b6"      # 紫色 - 指数
COLOR_RESULT = "#f1c40f"        # 黄色 - 结果
COLOR_AUXILIARY = "#95a5a6"     # 灰色 - 辅助线
COLOR_BACKGROUND = "#1a1a2e"    # 深蓝灰 - 背景
```

## 几何预计算清单
本动画主要涉及公式和文本，不涉及复杂几何图形。
主要元素：MathTex、Text、VGroup、Arrow、SurroundingRectangle

---

## Scene 1: 开场引入 (3-5秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (引发思考)
3. 题目展示

### 动画序列
| 时间 | 动作 | 代码参考 | y坐标 |
|------|------|---------|-------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | y=7 |
| 0.3s | 钩子问题书写 | `Write(hook_text)` | y=5.5 |
| 1.2s | 示例题目淡入 | `FadeIn(problem)` | y=3 |
| 2.5s | 等待理解 | `Wait(1.0)` | - |

### 钩子问题
"乘法会算，那除法呢？"

### 示例题目
"6x³ ÷ 2x = ?"

### 清理
- FadeOut: hook_text, problem (转场到下一场景)
- 保留: author_info

---

## Scene 2: 回顾幂的运算法则 (6-8秒)
**目的**: 复习基础知识，为除法做铺垫

### 元素
1. 标题: "复习: 幂的运算"
2. 公式: aᵐ ÷ aⁿ = aᵐ⁻ⁿ (a≠0, m≥n)
3. 具体例子: x⁵ ÷ x² = x³

### 动画序列
| 时间 | 动作 | 代码参考 | y坐标 |
|------|------|---------|-------|
| 0.0s | 标题淡入 | `FadeIn(title)` | y=5.5 |
| 0.5s | 幂的法则书写 | `Write(power_rule)` | y=3.5 |
| 1.5s | 示例淡入 | `FadeIn(example)` | y=1.5 |
| 2.5s | 高亮指数变化 | `Indicate(exponents)` | - |
| 3.5s | 说明文字 | `FadeIn(explanation)` | y=-2 |
| 5.0s | 等待理解 | `Wait(1.5)` | - |

### 说明文字
"同底数幂相除，底数不变，指数相减"

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 3: 单项式除以单项式 - 规则 (10-12秒)
**目的**: 讲解单项式除法的两步法则

### 元素
1. 标题: "单项式 ÷ 单项式"
2. 规则框
3. 示例公式: 6x³ ÷ 2x
4. 拆解步骤

### 动画序列
| 时间 | 动作 | 代码参考 | y坐标 |
|------|------|---------|-------|
| 0.0s | 标题书写 | `Write(title)` | y=5.5 |
| 0.8s | 原式展示 | `FadeIn(original)` | y=3.5 |
| 1.5s | 规则1淡入 | `FadeIn(rule1_box)` | y=1.5 |
| 2.5s | 系数分离高亮 | `Indicate(coefficients)` | - |
| 3.5s | 系数除法 | `TransformMatchingTex(step1, step2)` | y=0 |
| 5.0s | 规则2淡入 | `FadeIn(rule2_box)` | y=-1.5 |
| 6.0s | 变量分离高亮 | `Indicate(variables)` | - |
| 7.0s | 变量除法 | `TransformMatchingTex(step2, step3)` | y=-3 |
| 9.0s | 等待理解 | `Wait(1.5)` | - |

### 规则框内容
**规则1**: "系数相除"
**规则2**: "同底数幂相除"

### 拆解步骤
```
6x³ ÷ 2x
= (6 ÷ 2) × (x³ ÷ x)     [拆分]
= 3 × x²                  [计算]
= 3x²                     [结果]
```

### 清理
- FadeOut: 规则框
- 保留: 最终结果 (移至顶部)

---

## Scene 4: 单项式除法 - 完整示例 (10-12秒)
**目的**: 通过动画演示完整计算过程

### 元素
1. 新题目: -12a⁴b² ÷ 3a²b
2. 步骤动画
3. 颜色标注 (系数红色、变量绿色、指数紫色)

### 动画序列
| 时间 | 动作 | 代码参考 | y坐标 |
|------|------|---------|-------|
| 0.0s | 新题目淡入 | `FadeIn(problem2)` | y=4 |
| 1.0s | 系数部分框选 | `Create(coef_rect)` | - |
| 1.8s | 系数除法 | `Transform(coef_calc)` | y=2 |
| 3.0s | a的幂框选 | `Create(a_rect)` | - |
| 3.8s | a的幂除法 | `Transform(a_calc)` | y=0 |
| 5.0s | b的幂框选 | `Create(b_rect)` | - |
| 5.8s | b的幂除法 | `Transform(b_calc)` | y=-2 |
| 7.0s | 组合结果 | `FadeIn(final_result)` | y=-4 |
| 8.5s | 闪烁强调 | `Flash(final_result)` | - |
| 9.5s | 等待 | `Wait(1.0)` | - |

### 计算步骤
```
-12a⁴b² ÷ 3a²b
= (-12 ÷ 3) × (a⁴ ÷ a²) × (b² ÷ b)
= -4 × a² × b¹
= -4a²b
```

### 清理
- FadeOut: 所有框选和中间步骤
- 保留: 最终答案 (淡化)

---

## Scene 5: 多项式除以单项式 - 规则 (12-15秒)
**目的**: 讲解多项式除法的分配律应用

### 元素
1. 标题: "多项式 ÷ 单项式"
2. 核心规则
3. 示例: (6x³ + 4x²) ÷ 2x
4. 拆分动画

### 动画序列
| 时间 | 动作 | 代码参考 | y坐标 |
|------|------|---------|-------|
| 0.0s | 标题书写 | `Write(title)` | y=5.5 |
| 0.8s | 原式展示 | `FadeIn(original)` | y=3.5 |
| 1.5s | 规则框淡入 | `FadeIn(rule_box)` | y=1.5 |
| 3.0s | 拆分箭头1 | `GrowArrow(arrow1)` | - |
| 3.5s | 第一项除法 | `FadeIn(term1_calc)` | y=0 |
| 5.0s | 拆分箭头2 | `GrowArrow(arrow2)` | - |
| 5.5s | 第二项除法 | `FadeIn(term2_calc)` | y=-1.5 |
| 7.0s | 加号连接 | `FadeIn(plus_sign)` | y=-0.75 |
| 8.0s | 最终结果 | `FadeIn(final)` | y=-3 |
| 9.5s | 公式框 | `Create(formula_box)` | - |
| 11.0s | 等待理解 | `Wait(2.0)` | - |

### 规则框内容
"把多项式的每一项分别除以单项式，再把商相加"

### 拆分过程
```
(6x³ + 4x²) ÷ 2x
= 6x³ ÷ 2x  +  4x² ÷ 2x     [分配]
= 3x²       +  2x           [分别计算]
= 3x² + 2x                  [相加]
```

### 清理
- FadeOut: 中间步骤、箭头
- 保留: 最终结果和规则框 (淡化)

---

## Scene 6: 综合练习 + 总结 (12-15秒)
**目的**: 巩固知识，强化记忆

### 元素
1. 综合例题: (8a³b - 12a²b²) ÷ 4ab
2. 快速演示
3. 总结卡片
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | y坐标 |
|------|------|---------|-------|
| 0.0s | 题目淡入 | `FadeIn(problem3)` | y=4.5 |
| 1.0s | 拆分展示 | `Transform(split_terms)` | y=2.5 |
| 2.5s | 第一项计算 | `FadeIn(result1)` | y=1 |
| 3.5s | 第二项计算 | `FadeIn(result2)` | y=1 |
| 4.5s | 最终答案 | `FadeIn(final_answer)` | y=-0.5 |
| 6.0s | 总结卡片1 | `FadeIn(summary1, shift=LEFT)` | y=-2 |
| 7.0s | 总结卡片2 | `FadeIn(summary2, shift=LEFT)` | y=-3.5 |
| 8.0s | 总结卡片3 | `FadeIn(summary3, shift=LEFT)` | y=-5 |
| 10.0s | 关注提示 | `Write(follow_text)` | y=-6.5 |
| 12.0s | 装饰闪烁 | `Flash(decorations)` | - |
| 13.0s | 全部淡出 | `FadeOut(all)` | - |

### 计算过程 (快速展示)
```
(8a³b - 12a²b²) ÷ 4ab
= 8a³b ÷ 4ab - 12a²b² ÷ 4ab
= 2a² - 3ab
```

### 总结卡片
1. **单项式 ÷ 单项式**: 系数相除，同底数幂相除
2. **多项式 ÷ 单项式**: 每一项分别除，再相加
3. **关键**: 整式除法是乘法的逆运算

### 关注文字
"关注我，掌握更多数学技巧！"

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 始终保持在顶部 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| power_rule | Scene 2 | Scene 2 | 幂的法则 |
| rule1_box | Scene 3 | Scene 3 | 规则1框 |
| rule2_box | Scene 3 | Scene 3 | 规则2框 |
| problem2 | Scene 4 | Scene 4 | 示例2 |
| rule_box | Scene 5 | Scene 5 | 多项式规则 |
| summary_cards | Scene 6 | Scene 6 | 总结卡片 |

---

## 时间轴总览
```
0-5s:    Scene 1 - 开场引入
5-13s:   Scene 2 - 幂的运算复习
13-25s:  Scene 3 - 单项式除法规则
25-37s:  Scene 4 - 单项式除法示例
37-52s:  Scene 5 - 多项式除法规则
52-67s:  Scene 6 - 综合练习与总结
总时长: 约67秒
```

---

## 字体大小规范
```python
FONT_SIZES = {
    "title": 36,          # 场景标题
    "subtitle": 28,       # 副标题
    "formula": 32,        # 主要公式
    "formula_small": 24,  # 小公式
    "body": 22,           # 说明文字
    "label": 20,          # 标签
    "author": 20,         # 作者信息
}
```

---

## 配色细节说明
1. **系数** (红色 #e74c3c): 数字部分，如 6, -12, 3
2. **变量** (绿色 #2ecc71): 字母部分，如 x, a, b
3. **指数** (紫色 #9b59b6): 上标数字，如 ³, ², ⁴
4. **结果** (黄色 #f1c40f): 最终答案
5. **高亮** (橙色 #f39c12): 当前操作步骤
6. **辅助** (灰色 #95a5a6): 辅助线、框、箭头

---

## 关键技术点
1. **TransformMatchingTex**: 用于公式步骤间的平滑过渡
2. **SurroundingRectangle**: 框选特定部分
3. **Indicate**: 闪烁高亮效果
4. **VGroup**: 组合多个元素统一管理
5. **set_color_by_tex**: 按LaTeX内容着色

---

## 注意事项
1. 中文文本必须使用 `Text("...", font="Noto Sans CJK SC")`
2. 数学公式使用 `MathTex(r"...")`
3. 避免在 MathTex 中使用中文
4. 度数符号使用 `^\circ`
5. 分数使用 `\frac{}{}`
6. 所有坐标保证在安全区域内 (x∈[-4,4], y∈[-7,7])
7. 每个场景结束前明确清理临时元素