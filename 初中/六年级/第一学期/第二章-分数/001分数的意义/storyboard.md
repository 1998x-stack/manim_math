# 分数的意义 - 动画分镜脚本

<!-- /root/code/sss/media/videos/fraction_meaning/1920p60/FractionMeaning.mp4 -->

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 简单 (六年级)
- 目标受众: 小学六年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调部分
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_FRACTION_PART = "#2ecc71"  # 绿色 - 分数部分
COLOR_WHOLE = "#9b59b6"        # 紫色 - 整体
```

## 几何预计算清单

### 圆形切分 (Scene 2-3)
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆心 | ORIGIN + UP*2 | self.circle_center |
| 半径 | 1.5 | self.circle_radius |
| 扇形角度 (1/4) | 2π/4 = π/2 | self.sector_angle_quarter |
| 扇形角度 (3/8) | 2π * 3/8 | self.sector_angle_3_8 |
| 扇形起始角 | π/2 | self.start_angle |

### 矩形切分 (Scene 4)
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 矩形中心 | ORIGIN + UP*1.5 | self.rect_center |
| 矩形宽度 | 6.0 | self.rect_width |
| 矩形高度 | 2.0 | self.rect_height |
| 每份宽度 | 6.0 / 6 = 1.0 | self.segment_width |
| 分割线位置 | [i * segment_width for i in range(1,6)] | self.divider_positions |

### 数轴展示 (Scene 5)
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 数轴中心 | ORIGIN + DOWN*1 | self.numberline_center |
| 数轴范围 | [0, 2] | self.numberline_range |
| 刻度间距 | 1.0 | self.tick_spacing |
| 分数点位置 (2/3) | 2/3 * unit_length | self.fraction_point |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出"什么是分数"的问题

### 视觉元素
1. 作者标识 (顶部)
2. 钩子问题 (大字，居中)
3. 简单图形暗示 (圆形阴影)

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 顶部小字 |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=1.0)` | "一个披萨切成4份,你吃了1份..." |
| 1.5s | 问题文字淡入 | `FadeIn(question, shift=UP*0.3)` | "你吃了多少?" |
| 2.0s | 圆形阴影脉动 | `circle_shadow.animate.scale(1.1).set_opacity(0.3)` | 暗示即将出现 |
| 2.5s | 等待 | `self.wait(0.8)` | 让学生思考 |

### 清理
- FadeOut: hook_text, question, circle_shadow
- 保留: author_info

---

## Scene 2: 分数的基本概念 - 圆形演示 (10-12秒)
**目的**: 用圆形披萨展示 1/4 的含义

### 视觉元素
1. 完整圆形 (披萨)
2. 四条等分线
3. 其中1份高亮
4. 分数符号 1/4

### 几何计算
```python
# 圆心和半径
circle_center = UP * 2
circle_radius = 1.5

# 四个扇形的起始角度 (从正上方顺时针)
sector_angles = [PI/2, PI, 3*PI/2, 0]  # 每个扇形90度
```

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 标题出现 | `Write(title)` | "分数的意义" |
| 0.5s | 完整圆创建 | `Create(full_circle, run_time=1.0)` | 整体披萨 |
| 1.5s | 说明文字 | `FadeIn(explain_1)` | "把披萨平均分成4份" |
| 2.0s | 绘制分割线 | `Create(dividing_lines, lag_ratio=0.3)` | 十字分割 |
| 3.0s | 等待理解 | `self.wait(0.8)` | |
| 3.8s | 高亮1份 | `sector_1.animate.set_fill(COLOR_FRACTION_PART, 0.7)` | 扇形着色 |
| 4.5s | 分数出现 | `Write(fraction_1_4)` | "1/4" |
| 5.5s | 解释文字 | `FadeIn(explain_2)` | "取其中1份" |
| 6.5s | 等待 | `self.wait(1.5)` | 重要概念停留 |

### 清理
- FadeOut: explain_1, explain_2, dividing_lines
- 保留: full_circle (变淡), fraction_1_4, sector_1
- Transform: title → 移到顶部缩小

---

## Scene 3: 分数的扩展 - 3/8 (8-10秒)
**目的**: 展示分子>1的情况，理解"几份"

### 视觉元素
1. 新圆形 (8等分)
2. 3个扇形高亮
3. 分数 3/8
4. 对比说明

### 几何计算
```python
# 8等分圆
circle_center_2 = UP * 1.5
circle_radius_2 = 1.5
sector_angle = 2*PI / 8  # 每份45度

# 高亮3个扇形 (连续)
highlight_sectors = [0, 1, 2]  # 索引
```

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 清理上场景 | `FadeOut(VGroup(...))` | 圆形淡化 |
| 0.5s | 新圆创建 | `Create(circle_8)` | 8等分圆 |
| 1.0s | 说明 | `FadeIn(explain_3)` | "分成8份" |
| 1.5s | 绘制分割线 | `Create(lines_8, lag_ratio=0.2)` | 8条线 |
| 2.5s | 依次高亮3份 | `AnimationGroup(sector_fills, lag_ratio=0.3)` | 逐个着色 |
| 4.0s | 分数出现 | `Write(fraction_3_8)` | "3/8" |
| 4.8s | 解释 | `FadeIn(explain_4)` | "取其中3份" |
| 6.0s | 等待 | `self.wait(1.5)` | |

### 清理
- FadeOut: 全部元素
- 转场准备

---

## Scene 4: 矩形分数 - 多样化理解 (8-10秒)
**目的**: 用矩形展示分数，理解不同形状同样适用

### 视觉元素
1. 矩形条 (6等分)
5. 高亮 5/6
3. 分数符号

### 几何计算
```python
# 矩形参数
rect_center = UP * 1.5
rect_width = 6.0
rect_height = 1.5
num_parts = 6
segment_width = rect_width / num_parts

# 每个小矩形的位置
small_rects_positions = [
    rect_center + LEFT * (rect_width/2 - segment_width/2 - i*segment_width)
    for i in range(num_parts)
]
```

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 矩形创建 | `Create(big_rect)` | 整条 |
| 0.8s | 说明 | `FadeIn(explain_5)` | "也可以用矩形" |
| 1.3s | 分割线出现 | `Create(vertical_lines, lag_ratio=0.2)` | 5条分割线 |
| 2.5s | 高亮5份 | `AnimationGroup(rect_fills, lag_ratio=0.15)` | 从左到右 |
| 4.0s | 分数 | `Write(fraction_5_6)` | "5/6" |
| 5.0s | 等待 | `self.wait(1.5)` | |

### 清理
- FadeOut: 全部
- 转场

---

## Scene 5: 分数与除法的关系 (10-12秒)
**目的**: 建立 a÷b = a/b 的联系

### 视觉元素
1. 除法算式
2. 转换箭头
3. 分数形式
4. 具体例子

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 标题 | `Write(subtitle)` | "分数与除法" |
| 0.6s | 除法式 | `Write(division_eq)` | "3 ÷ 4" |
| 1.5s | 等号和箭头 | `FadeIn(arrow)` | 转换标识 |
| 2.0s | 分数形式 | `Write(fraction_eq)` | "= 3/4" |
| 3.0s | 公式框 | `Create(formula_box)` | 框住公式 |
| 3.5s | 通用公式 | `Write(general_formula)` | "a ÷ b = a/b (b≠0)" |
| 5.0s | 例子1 | `FadeIn(example_1)` | "1÷2 = 1/2" |
| 6.0s | 例子2 | `FadeIn(example_2)` | "5÷8 = 5/8" |
| 7.0s | 等待 | `self.wait(2.0)` | 关键理解 |

### 清理
- FadeOut: 全部
- 转场

---

## Scene 6: 分数的组成部分 (8-10秒)
**目的**: 认识分子、分母、分数线

### 视觉元素
1. 大分数 3/4 (中心)
2. 标注箭头和名称
3. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 标题 | `Write(subtitle_2)` | "分数的组成" |
| 0.6s | 分数出现 | `Write(large_fraction)` | "3/4" 大字 |
| 1.5s | 分子箭头 | `GrowArrow(arrow_numerator)` | 指向3 |
| 2.0s | 分子标签 | `FadeIn(label_numerator)` | "分子" |
| 2.5s | 分子说明 | `FadeIn(explain_numerator)` | "表示取了几份" |
| 3.5s | 分数线箭头 | `GrowArrow(arrow_line)` | 指向横线 |
| 4.0s | 分数线标签 | `FadeIn(label_line)` | "分数线" |
| 4.5s | 分母箭头 | `GrowArrow(arrow_denominator)` | 指向4 |
| 5.0s | 分母标签 | `FadeIn(label_denominator)` | "分母" |
| 5.5s | 分母说明 | `FadeIn(explain_denominator)` | "表示平均分成几份" |
| 7.0s | 等待 | `self.wait(1.5)` | |

### 清理
- FadeOut: 全部元素
- 转场

---

## Scene 7: 片尾总结与关注 (6-8秒)
**目的**: 强化记忆，引导关注

### 视觉元素
1. 关键点总结
2. 作者信息放大
3. 关注提示
4. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 总结标题 | `Write(summary_title)` | "记住这些!" |
| 0.6s | 要点1 | `FadeIn(point_1, shift=LEFT)` | "分数 = 分子/分母" |
| 1.2s | 要点2 | `FadeIn(point_2, shift=LEFT)` | "a÷b = a/b" |
| 1.8s | 要点3 | `FadeIn(point_3, shift=LEFT)` | "表示部分与整体的关系" |
| 2.5s | 作者放大 | `author_info.animate.scale(2).move_to(UP)` | |
| 3.0s | 关注文字 | `Write(follow_text)` | "关注我,学更多数学!" |
| 4.0s | 图标闪烁 | `Flash(icons, color=YELLOW)` | 装饰 |
| 5.0s | 等待 | `self.wait(1.5)` | |
| 6.5s | 全部淡出 | `FadeOut(everything)` | 结束 |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 持续存在,仅变换 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| title | Scene 2 | Scene 2 | 主标题,后缩小到顶部 |
| full_circle | Scene 2 | Scene 3 | 圆形披萨 |
| fraction_1_4 | Scene 2 | Scene 3 | 第一个分数 |
| circle_8 | Scene 3 | Scene 3 | 8等分圆 |
| fraction_3_8 | Scene 3 | Scene 3 | 第二个分数 |
| big_rect | Scene 4 | Scene 4 | 矩形条 |
| fraction_5_6 | Scene 4 | Scene 4 | 第三个分数 |
| division_eq | Scene 5 | Scene 5 | 除法算式 |
| general_formula | Scene 5 | Scene 5 | 通用公式 |
| large_fraction | Scene 6 | Scene 6 | 大分数展示 |
| summary_points | Scene 7 | Scene 7 | 总结要点 |

---

## 字体大小配置
```python
FONT_SIZES = {
    "title": 40,          # 场景标题
    "subtitle": 32,       # 副标题
    "body": 26,           # 正文说明
    "label": 22,          # 标签 (分子、分母)
    "small": 20,          # 小字/注释
    "author": 22,         # 作者信息
    "formula": 36,        # 数学公式 (分数)
    "large_formula": 48,  # 大公式 (Scene 6)
}
```

---

## 关键动画节奏
- Scene 1 (钩子): 3秒 - 快速抓住注意力
- Scene 2 (1/4): 8秒 - 慢,核心概念
- Scene 3 (3/8): 8秒 - 中等,扩展理解
- Scene 4 (矩形): 8秒 - 中等,多样化
- Scene 5 (除法): 10秒 - 慢,重要关联
- Scene 6 (组成): 8秒 - 中等,术语认知
- Scene 7 (总结): 7秒 - 快速结束

**总计**: 约 52-60 秒

---

## 教学要点检查清单
- [✓] 分数的基本定义 (平均分)
- [✓] 分子、分母的含义
- [✓] 分数与除法的关系
- [✓] 多种图形展示 (圆、矩形)
- [✓] 具体数值示例
- [✓] 避免过于抽象的表述
- [✓] 视觉化引导学习

---

## 备注
1. 所有图形使用精确的NumPy计算,避免臆想坐标
2. 中文文字全部使用 `Text()` 而非 `MathTex()`
3. 分数符号使用 `MathTex(r"\frac{a}{b}")` 格式
4. 颜色使用对比鲜明的配色,便于学生识别
5. 每个关键步骤后有足够等待时间 (1-2秒)
6. 避免信息过载,一次只展示一个概念