# 平方差公式 (Difference of Squares Formula) - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 初中基础
- 目标受众: 七年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要公式
COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调部分
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_POSITIVE = "#2ecc71"     # 绿色 - 正数/加法
COLOR_NEGATIVE = "#e67e22"     # 橙色 - 负数/减法
COLOR_SQUARE_A = "#9b59b6"     # 紫色 - a² 区域
COLOR_SQUARE_B = "#1abc9c"     # 青色 - b² 区域
COLOR_AUXILIARY = GRAY_B       # 辅助线
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 大正方形边长 | a (参数化) | self.a = 2.5 |
| 小正方形边长 | b (参数化) | self.b = 1.0 |
| 大正方形中心 | 原点偏移 | self.square_a_center = UP * 1.5 |
| 小正方形位置 | 右上角对齐 | self.square_b_pos |
| 矩形宽度 | a - b | self.rect_width |
| 矩形高度 | a | self.rect_height |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 抓住注意力，提出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字)
3. 公式预览

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` - "计算 (x+2)(x-2) = ?" |
| 1.5s | 问号闪烁强调 | `Flash(question_mark, color=YELLOW)` |
| 2.5s | 等待思考 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text
- 保留: author_info

---

## Scene 2: 公式引入 (5-6秒)
**目的**: 展示平方差公式的标准形式

### 元素
1. 公式标题
2. 标准公式: (a+b)(a-b) = a² - b²
3. 公式解释

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title)` - "平方差公式" |
| 0.8s | 公式左侧出现 | `Write(formula_left)` - "(a+b)(a-b)" |
| 1.5s | 等号出现 | `Write(equals)` |
| 2.0s | 公式右侧出现 | `Write(formula_right)` - "a² - b²" |
| 3.0s | 高亮公式特点 | `Indicate(formula)` |
| 4.0s | 文字说明淡入 | `FadeIn(explanation)` - "两数和 × 两数差 = 两数平方差" |

### 清理
- FadeOut: title, explanation
- Transform: formula 移到顶部作为参考

---

## Scene 3: 几何证明 - 构建大正方形 (6-8秒)
**目的**: 通过面积直观理解公式

### 元素
1. 边长为 a 的正方形
2. 标注边长 a
3. 面积标注 a²

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 引导文字 | "让我们用面积来理解这个公式" |
| 1.0s | 绘制大正方形 | `Create(square_a)` |
| 2.0s | 标注边长 | `Write(label_a)` - 四条边都标 "a" |
| 3.0s | 填充颜色 | `square_a.animate.set_fill(COLOR_SQUARE_A, opacity=0.3)` |
| 4.0s | 面积标注 | `Write(area_a)` - "面积 = a²" |
| 5.0s | 等待理解 | `Wait(1.0)` |

### 清理
- 保留: square_a, labels
- FadeOut: 引导文字

---

## Scene 4: 几何证明 - 减去小正方形 (7-9秒)
**目的**: 展示减法操作的几何意义

### 元素
1. 边长为 b 的小正方形 (右上角)
2. 标注边长 b
3. 面积标注 b²
4. 阴影区域 (a² - b²)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 引导文字 | "从中减去一个边长为 b 的正方形" |
| 1.0s | 小正方形淡入 | `FadeIn(square_b, scale=0.5)` - 从中心放大到右上角 |
| 2.0s | 标注边长 b | `Write(label_b)` |
| 2.5s | 填充颜色 | `square_b.animate.set_fill(COLOR_SQUARE_B, opacity=0.5)` |
| 3.5s | 面积标注 | `Write(area_b)` - "b²" |
| 4.5s | 高亮剩余区域 | 剩余L形区域闪烁 |
| 5.5s | 剩余面积标注 | `Write(remaining_area)` - "剩余面积 = a² - b²" |
| 6.5s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: 引导文字, area_labels
- 保留: square_a, square_b, L形区域

---

## Scene 5: 几何证明 - 重组为矩形 (10-12秒)
**目的**: 展示如何将L形区域重组为矩形

### 元素
1. L形区域分割为两个矩形
2. 上方矩形: (a-b) × b
3. 右侧矩形: a × (a-b)
4. 移动动画
5. 组合后的大矩形: (a+b) × (a-b)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 引导文字 | "将剩余部分重新排列" |
| 1.0s | 分割线出现 | `Create(division_line)` - 虚线分割 |
| 2.0s | 上方矩形高亮 | 颜色变化 + 标注 "(a-b) × b" |
| 3.0s | 右侧矩形高亮 | 颜色变化 + 标注 "a × (a-b)" |
| 4.0s | 上方矩形下移 | `rect_top.animate.shift(DOWN * distance)` |
| 5.5s | 组合成大矩形 | 两个矩形对齐 |
| 6.5s | 标注总尺寸 | 宽 = "a + b", 高 = "a - b" |
| 7.5s | 面积公式 | `Write(final_area)` - "(a+b)(a-b)" |
| 9.0s | 等待理解 | `Wait(2.0)` - 关键步骤 |

### 清理
- FadeOut: 几何图形, labels
- 保留: 最终公式

---

## Scene 6: 具体例子 - (x+2)(x-2) (8-10秒)
**目的**: 用具体数字例子巩固理解

### 元素
1. 原问题回顾: (x+2)(x-2)
2. 套用公式过程
3. 计算结果: x² - 4

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 例子标题 | "让我们计算 (x+2)(x-2)" |
| 1.0s | 原式出现 | `Write(example)` - "(x+2)(x-2)" |
| 2.0s | 标识 a 和 b | 高亮 x (a) 和 2 (b) |
| 3.0s | 套用公式 | `TransformMatchingTex()` - 显示对应关系 |
| 4.0s | 中间步骤 | "= x² - 2²" |
| 5.0s | 最终结果 | `Write(result)` - "= x² - 4" |
| 6.0s | 结果高亮 | `Indicate(result, color=YELLOW)` |
| 7.0s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: 所有例子元素

---

## Scene 7: 逆用公式提示 + 片尾 (6-8秒)
**目的**: 提示逆向使用（因式分解）+ 关注提示

### 元素
1. 逆用公式: a² - b² = (a+b)(a-b)
2. 应用场景提示
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 逆用标题 | "公式也可以反过来用!" |
| 1.0s | 逆向公式 | `Write(reverse_formula)` - "a² - b² = (a+b)(a-b)" |
| 2.5s | 应用提示 | "用于因式分解" |
| 3.5s | 例子闪现 | "如: x² - 9 = (x+3)(x-3)" |
| 5.0s | 淡出过渡 | `FadeOut(all_content)` |
| 5.5s | 作者信息放大 | `Transform(author_info, author_large)` |
| 6.5s | 关注提示 | "关注我，学更多数学技巧!" |
| 7.5s | 结束 | 装饰图案动画 |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留在顶部 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| formula_reference | Scene 2 | Scene 7 | 移到顶部作为参考 |
| square_a | Scene 3 | Scene 5 | 大正方形 |
| square_b | Scene 4 | Scene 5 | 小正方形 |
| rectangles | Scene 5 | Scene 5 | 重组矩形 |
| example_calc | Scene 6 | Scene 6 | 具体例子 |
| reverse_formula | Scene 7 | Scene 7 | 逆用公式 |

---

## 关键技术点

### 1. 正方形和矩形的精确定位
```python
# 大正方形：边长 a，中心在 UP * 1.5
self.a = 2.5
self.square_a_center = UP * 1.5
self.A_TL = self.square_a_center + UL * self.a / 2  # 左上
self.A_TR = self.square_a_center + UR * self.a / 2  # 右上
self.A_BL = self.square_a_center + DL * self.a / 2  # 左下
self.A_BR = self.square_a_center + DR * self.a / 2  # 右下

# 小正方形：边长 b，右上角对齐大正方形右上角
self.b = 1.0
self.square_b_center = self.A_TR + DL * self.b / 2
```

### 2. L形区域分割
```python
# 上方矩形：宽 = a, 高 = b
top_rect_width = self.a
top_rect_height = self.b
top_rect_center = self.square_a_center + UP * (self.a - self.b) / 2

# 下方矩形：宽 = a - b, 高 = a - b
bottom_rect_width = self.a - self.b
bottom_rect_height = self.a - self.b
bottom_rect_center = self.square_a_center + DOWN * self.b / 2 + LEFT * self.b / 2
```

### 3. 文字和公式的对齐
- 中文使用 Text("...", font="Noto Sans CJK SC")
- 数学公式使用 MathTex(r"...")
- 混合使用 VGroup 组合对齐

### 4. 颜色渐变和高亮
- 使用 set_fill() 设置填充透明度
- 使用 Indicate() 强调重要元素
- 使用 Flash() 制造闪烁效果

---

## 节奏控制
- 开场钩子: 快节奏 (3s)
- 公式引入: 中速 (5s)
- 几何证明: 慢速详细 (25s) - **核心部分**
- 具体例子: 中速 (8s)
- 逆用+片尾: 快节奏 (8s)
- **总计: 约 65 秒**

---

## 音效建议 (可选)
- 公式出现: 轻快的"叮"声
- 几何变换: 滑动音效
- 关键步骤: 强调音
- 片尾: 温馨提示音

---

## 验证检查清单
- [ ] 所有坐标精确计算，无臆想
- [ ] 中文使用 Text()，数学使用 MathTex()
- [ ] 元素在安全边界内 (x ∈ [-4, 4], y ∈ [-7, 7])
- [ ] 字体大小符合规范
- [ ] 颜色对比度足够
- [ ] 动画节奏流畅
- [ ] 难点有足够停留时间
- [ ] 开头有钩子，结尾有关注提示