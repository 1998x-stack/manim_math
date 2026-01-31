# 分数的基本性质 - Manim动画分镜脚本

## 元信息
- **目标时长**: 60-75秒
- **场景数量**: 7个主要场景
- **难度等级**: 六年级适用
- **核心概念**: 分数的分子和分母同时乘以或除以同一个不为零的数,分数的值不变

## 颜色配置
```python
COLOR_FRACTION_BASE = "#3498db"      # 蓝色 - 基础分数
COLOR_MULTIPLY = "#e74c3c"           # 红色 - 乘法操作
COLOR_DIVIDE = "#2ecc71"             # 绿色 - 除法操作
COLOR_HIGHLIGHT = YELLOW             # 黄色 - 高亮强调
COLOR_AUXILIARY = GRAY_B             # 灰色 - 辅助线/说明
COLOR_EQUAL = "#f39c12"              # 橙色 - 等号/等值
```

## 几何预计算清单
| 元素 | 计算方式 | 存储变量 | 用途 |
|------|---------|---------|------|
| 分数条基准位置 | UP * 2 | self.BAR_CENTER | 可视化分数条的中心 |
| 分数条宽度 | 6.0 | self.BAR_WIDTH | 分数条总宽度 |
| 分数条高度 | 0.8 | self.BAR_HEIGHT | 单个分数条高度 |
| 公式区域中心 | DOWN * 2 | self.FORMULA_CENTER | 数学公式显示区域 |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 抓住注意力,引出分数的神奇性质

### 元素
1. 作者标识 (顶部)
2. 引导性问题 (大字)
3. 三个不同外观的分数

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 顶部小字 |
| 0.3s | 钩子问题书写 | `Write(hook_text)` | "这三个分数相等吗?" |
| 1.0s | 第一个分数出现 | `FadeIn(frac_1)` | 1/2 |
| 1.3s | 第二个分数出现 | `FadeIn(frac_2)` | 2/4 |
| 1.6s | 第三个分数出现 | `FadeIn(frac_3)` | 3/6 |
| 2.0s | 问号闪烁 | `Flash(question_mark)` | 制造悬念 |
| 3.0s | 等待 | `Wait(0.5)` | - |

### 清理
- FadeOut: hook_text, question_mark
- 保留: author_info, frac_1, frac_2, frac_3

---

## Scene 2: 视觉验证 - 分数条展示 (8-10秒)
**目的**: 通过可视化证明三个分数相等

### 元素
1. 三个分数条 (不同分割方式)
2. 阴影部分 (代表分数值)
3. 等号连接

### 几何计算
```python
# 分数条1 (1/2): 分成2份,填充1份
bar_1_parts = 2
bar_1_filled = 1

# 分数条2 (2/4): 分成4份,填充2份  
bar_2_parts = 4
bar_2_filled = 2

# 分数条3 (3/6): 分成6份,填充3份
bar_3_parts = 6
bar_3_filled = 3

# 每个分数条的小格宽度
part_width_1 = self.BAR_WIDTH / bar_1_parts
part_width_2 = self.BAR_WIDTH / bar_2_parts
part_width_3 = self.BAR_WIDTH / bar_3_parts
```

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 分数移动到顶部 | `frac_group.animate.move_to(UP*5)` | - |
| 0.5s | 第一个分数条创建 | `Create(bar_1)` | 1/2的矩形框 |
| 1.0s | 分割线出现 | `Create(division_lines_1)` | 垂直线 |
| 1.5s | 阴影填充动画 | `FadeIn(filled_parts_1)` | 左半部分 |
| 2.5s | 第二个分数条创建 | `Create(bar_2)` | 2/4 |
| 3.0s | 分割线出现 | `Create(division_lines_2)` | 4条垂直线 |
| 3.5s | 阴影填充动画 | `FadeIn(filled_parts_2)` | 前两部分 |
| 4.5s | 第三个分数条创建 | `Create(bar_3)` | 3/6 |
| 5.0s | 分割线出现 | `Create(division_lines_3)` | 6条垂直线 |
| 5.5s | 阴影填充动画 | `FadeIn(filled_parts_3)` | 前三部分 |
| 6.5s | 等号连接 | `Write(equal_signs)` | = = |
| 7.5s | 结论文字 | `FadeIn(conclusion)` | "它们确实相等!" |
| 8.5s | 等待 | `Wait(1.0)` | - |

### 清理
- FadeOut: 所有分数条, equal_signs, conclusion
- 保留: author_info, frac_1 (移回中心)

---

## Scene 3: 核心概念引入 (5-6秒)
**目的**: 明确说明分数的基本性质

### 元素
1. 标题文字
2. 性质描述
3. 高亮框

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 标题书写 | `Write(title)` | "分数的基本性质" |
| 0.8s | 性质说明淡入 | `FadeIn(property_text)` | "分子和分母同时..." |
| 2.0s | 高亮框出现 | `Create(highlight_box)` | 包围关键文字 |
| 3.5s | 公式预告 | `FadeIn(formula_preview)` | "用公式表达:" |
| 4.5s | 等待 | `Wait(1.0)` | - |

### 清理
- FadeOut: title, property_text, highlight_box, formula_preview
- 保留: author_info

---

## Scene 4: 乘法性质演示 (12-15秒)
**目的**: 展示分子分母同时乘以相同数,分数值不变

### 元素
1. 基础分数 1/2
2. 乘法箭头和数字
3. 变换后的分数 2/4, 3/6
4. 数学公式

### 几何计算
```python
# 分数位置
base_fraction_pos = LEFT * 3 + UP * 1.5
multiply_k_pos = ORIGIN + UP * 2.5
result_fraction_pos = RIGHT * 3 + UP * 1.5

# 箭头
arrow_1_start = base_fraction_pos + RIGHT * 0.8
arrow_1_end = result_fraction_pos + LEFT * 0.8
```

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 基础分数出现 | `FadeIn(base_frac)` | 1/2在左侧 |
| 0.5s | 说明文字 | `FadeIn(explain_1)` | "同时乘以2" |
| 1.0s | 乘号和数字出现 | `Write(multiply_symbol)` | ×2 |
| 1.5s | 分子分母同时高亮 | `Indicate(numerator), Indicate(denominator)` | 强调"同时" |
| 2.5s | 箭头动画 | `GrowArrow(arrow_1)` | 指向右侧 |
| 3.0s | 变换后分数出现 | `FadeIn(result_frac_1)` | 2/4 |
| 4.0s | 等号连接 | `Write(equal_sign_1)` | 1/2 = 2/4 |
| 5.0s | 再次乘以 | `FadeIn(explain_2)` | "再乘以3" |
| 5.5s | 第二次变换 | `Transform` | 2/4 → 6/12 或回到 1/2 → 3/6 |
| 7.0s | 等号连接 | `Write(equal_sign_2)` | 1/2 = 3/6 |
| 8.0s | 公式总结 | `Write(formula)` | a/b = (a×k)/(b×k) |
| 9.5s | 高亮k≠0 | `Indicate(k_condition)` | 闪烁提醒 |
| 11.0s | 等待 | `Wait(1.5)` | - |

### 清理
- FadeOut: 所有元素除了公式
- 保留: author_info, formula (移到顶部)

---

## Scene 5: 除法性质演示 (12-15秒)
**目的**: 展示分子分母同时除以相同数,分数值不变 (约分)

### 元素
1. 大分数 6/12
2. 除法箭头和数字
3. 约分后的分数 3/6, 1/2
4. 数学公式

### 几何计算
```python
# 分数位置 (与乘法对称)
large_fraction_pos = LEFT * 3 + UP * 1.5
divide_k_pos = ORIGIN + UP * 2.5
simplified_fraction_pos = RIGHT * 3 + UP * 1.5
```

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 大分数出现 | `FadeIn(large_frac)` | 6/12在左侧 |
| 0.5s | 说明文字 | `FadeIn(explain_3)` | "同时除以2" |
| 1.0s | 除号和数字出现 | `Write(divide_symbol)` | ÷2 |
| 1.5s | 分子分母同时高亮 | `Indicate(numerator), Indicate(denominator)` | 强调"同时" |
| 2.5s | 除法动画 | 使用划线或淡化 | 6→3, 12→6 |
| 3.5s | 简化后分数出现 | `FadeIn(simplified_frac_1)` | 3/6 |
| 4.5s | 等号连接 | `Write(equal_sign_3)` | 6/12 = 3/6 |
| 5.5s | 再次除以 | `FadeIn(explain_4)` | "再除以3" |
| 6.5s | 第二次约分 | `Transform` | 3/6 → 1/2 |
| 8.0s | 等号连接 | `Write(equal_sign_4)` | 3/6 = 1/2 |
| 9.0s | 公式总结 | `Write(formula_2)` | a/b = (a÷k)/(b÷k) |
| 10.5s | 高亮k≠0且能整除 | `Indicate(k_condition_2)` | 闪烁提醒 |
| 12.0s | 等待 | `Wait(1.5)` | - |

### 清理
- FadeOut: 所有元素除了两个公式
- 保留: author_info, formula, formula_2 (并排显示)

---

## Scene 6: 应用示例 - 通分与约分 (10-12秒)
**目的**: 展示实际应用场景

### 元素
1. 两个不同分数需要通分
2. 通分过程动画
3. 约分示例

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 问题出现 | `FadeIn(question)` | "如何比较 1/3 和 1/4?" |
| 1.0s | 两个分数出现 | `FadeIn(frac_a, frac_b)` | 1/3 和 1/4 |
| 2.0s | 说明通分 | `FadeIn(explain_5)` | "通分:找公分母12" |
| 3.0s | 分别变换 | `Transform` | 1/3→4/12, 1/4→3/12 |
| 5.0s | 比较结果 | `FadeIn(comparison)` | 4/12 > 3/12 |
| 6.5s | 约分示例引入 | `FadeIn(simplify_example)` | "约分: 8/12" |
| 7.5s | 约分过程 | `Transform` | 8/12 → 4/6 → 2/3 |
| 9.0s | 最简分数标注 | `FadeIn(final_form)` | "最简分数" |
| 10.0s | 等待 | `Wait(1.5)` | - |

### 清理
- FadeOut: 所有应用示例
- 保留: author_info

---

## Scene 7: 总结与关注 (8-10秒)
**目的**: 总结要点,引导关注

### 元素
1. 核心要点卡片
2. 关键公式回顾
3. 作者信息和关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 要点标题 | `Write(summary_title)` | "记住这三点" |
| 1.0s | 要点1淡入 | `FadeIn(point_1)` | "同时乘或除" |
| 2.0s | 要点2淡入 | `FadeIn(point_2)` | "数值不能为0" |
| 3.0s | 要点3淡入 | `FadeIn(point_3)` | "应用:通分约分" |
| 4.5s | 公式回顾 | `FadeIn(formula_recap)` | 两个核心公式 |
| 6.0s | 作者信息放大 | `author_info.animate.scale(1.5)` | - |
| 6.8s | 关注提示 | `FadeIn(follow_text)` | "关注我,学更多数学!" |
| 7.5s | 小装饰动画 | `Rotate(decorations)` | 分数符号旋转 |
| 9.0s | 等待 | `Wait(1.0)` | - |

### 清理
- 全部淡出

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保留在顶部 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| frac_1, frac_2, frac_3 | Scene 1 | Scene 2 | 三个示例分数 |
| bar_group | Scene 2 | Scene 2 | 分数条可视化 |
| property_text | Scene 3 | Scene 3 | 性质说明 |
| formula | Scene 4 | Scene 7 | 乘法公式 |
| formula_2 | Scene 5 | Scene 7 | 除法公式 |
| application_examples | Scene 6 | Scene 6 | 通分约分示例 |
| summary_points | Scene 7 | Scene 7 | 总结要点 |

---

## 技术注意事项

### 1. 分数显示
```python
# 使用MathTex创建分数
frac = MathTex(r"\frac{1}{2}")

# 访问分子分母(如果需要独立操作)
frac = MathTex(r"\frac{", "1", "}{", "2", "}")
numerator = frac[1]
denominator = frac[3]
```

### 2. 分数条精确绘制
```python
def create_fraction_bar(parts, filled, position):
    """
    parts: 总份数
    filled: 填充份数
    position: 中心位置
    """
    # 外框
    outline = Rectangle(width=self.BAR_WIDTH, height=self.BAR_HEIGHT)
    outline.move_to(position)
    
    # 分割线
    lines = VGroup()
    part_width = self.BAR_WIDTH / parts
    for i in range(1, parts):
        x_pos = -self.BAR_WIDTH/2 + i * part_width
        line = Line(
            position + UP*self.BAR_HEIGHT/2 + RIGHT*x_pos,
            position + DOWN*self.BAR_HEIGHT/2 + RIGHT*x_pos,
            color=GRAY
        )
        lines.add(line)
    
    # 填充部分
    filled_parts = VGroup()
    for i in range(filled):
        x_start = -self.BAR_WIDTH/2 + i * part_width
        rect = Rectangle(
            width=part_width,
            height=self.BAR_HEIGHT,
            fill_color=BLUE,
            fill_opacity=0.6,
            stroke_width=0
        )
        rect.move_to(position + RIGHT*(x_start + part_width/2))
        filled_parts.add(rect)
    
    return VGroup(outline, lines, filled_parts)
```

### 3. 动画节奏控制
- 简单分数出现: 0.5s
- 复杂变换: 1.0-1.5s
- 关键步骤停留: 1.5-2.0s
- 场景过渡: 0.5s

### 4. 字体大小一致性
- 标题: 40-48
- 分数: 36-40
- 说明文字: 24-28
- 小注释: 18-20

---

## 预期总时长分配

| 场景 | 预期时长 | 累计时长 |
|------|---------|---------|
| Scene 1: 开场 | 3-4s | 4s |
| Scene 2: 视觉验证 | 8-10s | 14s |
| Scene 3: 核心概念 | 5-6s | 20s |
| Scene 4: 乘法性质 | 12-15s | 35s |
| Scene 5: 除法性质 | 12-15s | 50s |
| Scene 6: 应用示例 | 10-12s | 62s |
| Scene 7: 总结关注 | 8-10s | 72s |

**总计**: 约70-75秒 (符合TikTok短视频最佳时长)