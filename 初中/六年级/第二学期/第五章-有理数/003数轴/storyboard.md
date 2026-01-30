# 数轴 (Number Line) - 动画分镜脚本

<!-- /root/code/sss/media/videos/number_line_lesson/1920p60/NumberLineLesson.mp4 -->
## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 基础（六年级）
- 目标受众: 小学六年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要元素
COLOR_SECONDARY = "#e74c3c"      # 红色 - 重点强调
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_POSITIVE = "#2ecc71"       # 绿色 - 正数
COLOR_NEGATIVE = "#e67e22"       # 橙色 - 负数
COLOR_ORIGIN = "#9b59b6"         # 紫色 - 原点
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 数轴中心 | ORIGIN | self.number_line_center |
| 数轴长度 | 7 单位 | self.line_length |
| 单位长度 | 0.8 | self.unit_length |
| 数轴位置 | UP * 2 | self.line_position |
| 各整数点位置 | center + i * unit_length | self.point_positions |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，提出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字)
3. 神秘的点和箭头

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` - "有理数怎么排队?" |
| 1.1s | 神秘点闪烁 | `Flash(mystery_dots)` - 5个彩色点 |
| 2.1s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text, mystery_dots
- 保留: author_info

---

## Scene 2: 引入数轴 (6-8秒)
**目的**: 介绍数轴的定义和基本概念

### 元素
1. 标题 "数轴 Number Line"
2. 定义文字
3. 基本数轴（不带刻度）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title)` |
| 0.6s | 定义淡入 | `FadeIn(definition)` - "规定了原点、正方向和单位长度的直线" |
| 1.4s | 数轴创建 | `Create(number_line)` - 基础直线 |
| 2.4s | 等待 | `Wait(0.8)` |

### 清理
- FadeOut: title, definition
- 保留: number_line, author_info

---

## Scene 3: 三要素之一 - 原点 (8-10秒)
**目的**: 强调原点的重要性

### 元素
1. 标题 "第一要素: 原点"
2. 原点标记（紫色大点）
3. 原点标签 "O" 和 "0"
4. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(element_title_1)` - "要素1: 原点" |
| 0.4s | 原点闪现 | `GrowFromCenter(origin_dot)` + `Flash` |
| 1.0s | 标签出现 | `FadeIn(origin_label)` - "O" 和 "0" |
| 1.6s | 说明淡入 | `FadeIn(explanation_1)` - "确定数轴的基准位置" |
| 2.6s | 原点脉冲 | `origin_dot.animate.scale(1.3).set_opacity(0.8)` 然后恢复 |
| 3.4s | 等待 | `Wait(0.6)` |

### 清理
- FadeOut: element_title_1, explanation_1
- 保留: number_line, origin_dot, origin_label, author_info

---

## Scene 4: 三要素之二 - 正方向 (8-10秒)
**目的**: 说明正方向的作用

### 元素
1. 标题 "第二要素: 正方向"
2. 箭头指示
3. 说明文字
4. 动态箭头动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(element_title_2)` - "要素2: 正方向" |
| 0.4s | 箭头生长 | `GrowArrow(direction_arrow)` - 从原点向右 |
| 1.2s | 箭头闪烁 | `Flash(arrow_tip, color=COLOR_POSITIVE)` |
| 1.8s | 说明淡入 | `FadeIn(explanation_2)` - "通常向右为正" |
| 2.4s | 流动箭头 | 多个小箭头从左向右流动 |
| 3.6s | 等待 | `Wait(0.6)` |

### 清理
- FadeOut: element_title_2, explanation_2, flow_arrows
- 保留: number_line, origin_dot, origin_label, direction_arrow, author_info

---

## Scene 5: 三要素之三 - 单位长度 (10-12秒)
**目的**: 演示单位长度的作用

### 元素
1. 标题 "第三要素: 单位长度"
2. 刻度标记
3. 单位长度标注（括号）
4. 整数标签
5. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(element_title_3)` - "要素3: 单位长度" |
| 0.4s | 第一个刻度 | `Create(tick_1)` 在位置1 |
| 0.8s | 单位长度标注 | `FadeIn(unit_brace)` - 括号标注"单位长度" |
| 1.4s | 其他正数刻度 | `Create(ticks_positive)` - 连续创建2,3,4 |
| 2.2s | 负数刻度 | `Create(ticks_negative)` - 连续创建-1,-2,-3,-4 |
| 3.0s | 所有数字标签 | `FadeIn(all_labels)` |
| 3.8s | 说明淡入 | `FadeIn(explanation_3)` - "确定刻度的间隔" |
| 4.8s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: element_title_3, unit_brace, explanation_3
- 保留: 完整数轴（带所有刻度和标签）, author_info

---

## Scene 6: 数轴与有理数的对应 (12-15秒)
**目的**: 展示数轴上的点与有理数的对应关系

### 元素
1. 标题 "数轴上的点 ↔ 有理数"
2. 多个有理数示例点
3. 对应关系连线
4. 小数和分数示例

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(correspondence_title)` |
| 0.5s | 整数点高亮 | 所有整数点同时闪烁 |
| 1.2s | 添加2.5的点 | `FadeIn(dot_2_5)` + 标签 "2.5" |
| 1.8s | 添加-1.5的点 | `FadeIn(dot_neg_1_5)` + 标签 "-1.5" |
| 2.4s | 添加分数1/2 | `FadeIn(dot_half)` + 标签 "1/2" |
| 3.0s | 添加分数-3/2 | `FadeIn(dot_neg_3_2)` + 标签 "-3/2" |
| 3.8s | 说明淡入 | `FadeIn(explanation_4)` - "每个点对应一个有理数" |
| 5.2s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: correspondence_title, explanation_4, 小数和分数点
- 保留: 基本数轴, author_info

---

## Scene 7: 比较大小规则 (12-15秒)
**目的**: 演示如何用数轴比较有理数大小

### 元素
1. 标题 "比较大小: 右边的数 > 左边的数"
2. 两个数的比较示例
3. 动态比较动画
4. 多个比较示例

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(comparison_title)` |
| 0.6s | 示例1: 比较2和-1 | 两个点高亮，箭头指示 |
| 1.4s | 公式显示 | `Write(formula_1)` - "2 > -1" |
| 2.2s | 示例2: 比较-2和-3 | 两个点高亮，箭头指示 |
| 3.0s | 公式显示 | `Write(formula_2)` - "-2 > -3" |
| 3.8s | 动态滑动比较 | 一个点从左向右移动，数值增大 |
| 5.2s | 总结淡入 | `FadeIn(summary)` - "位置越靠右，数值越大" |
| 6.4s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: comparison_title, formulas, comparison_dots, summary
- 保留: 基本数轴, author_info

---

## Scene 8: 总结与片尾 (8-10秒)
**目的**: 巩固知识点，引导关注

### 元素
1. 总结卡片（三要素）
2. 数轴完整展示
3. 关注提示
4. 作者信息放大

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 数轴缩小移至上方 | `number_line.animate.scale(0.7).move_to(UP*4)` |
| 0.8s | 三要素卡片滑入 | `cards.animate.shift(RIGHT)` - 依次出现 |
| 2.6s | 重点提示 | `FadeIn(highlight_text)` - "数轴是有理数的直观表示!" |
| 3.6s | 作者信息放大 | `Transform(author_info, author_large)` |
| 4.4s | 关注提示 | `FadeIn(follow_text)` - "关注我，学更多数学技巧!" |
| 5.2s | 装饰动画 | 小数字图标环绕旋转 |
| 7.2s | 全部淡出 | `FadeOut(everything)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 作者标识，贯穿全程 |
| number_line | Scene 2 | Scene 8 | 基本数轴 |
| origin_dot | Scene 3 | Scene 8 | 原点标记 |
| origin_label | Scene 3 | Scene 8 | 原点标签 |
| direction_arrow | Scene 4 | Scene 8 | 正方向箭头 |
| ticks | Scene 5 | Scene 8 | 刻度标记 |
| tick_labels | Scene 5 | Scene 8 | 数字标签 |
| mystery_dots | Scene 1 | Scene 1 | 开场神秘点 |
| hook_text | Scene 1 | Scene 1 | 钩子问题 |
| flow_arrows | Scene 4 | Scene 4 | 流动箭头（临时） |
| unit_brace | Scene 5 | Scene 5 | 单位长度标注（临时） |
| rational_dots | Scene 6 | Scene 6 | 小数/分数点（临时） |
| comparison_elements | Scene 7 | Scene 7 | 比较示例（临时） |
| summary_cards | Scene 8 | Scene 8 | 总结卡片 |

---

## 关键技术要点

### 1. NumberLine 使用
```python
number_line = NumberLine(
    x_range=[-4, 4, 1],  # [起点, 终点, 步长]
    length=7,            # 实际长度
    include_numbers=True,
    numbers_to_include=range(-4, 5),
    include_ticks=True,
    tick_size=0.1,
    color=COLOR_PRIMARY
)
```

### 2. 精确点位置计算
```python
# 数轴上数字x对应的坐标
def get_number_position(x):
    return number_line.number_to_point(x)

# 示例：获取2.5的位置
pos_2_5 = number_line.number_to_point(2.5)
```

### 3. 动态标签
```python
# 整数标签
for i in range(-4, 5):
    label = MathTex(str(i), font_size=20)
    label.next_to(number_line.number_to_point(i), DOWN, buff=0.2)

# 分数标签
frac_label = MathTex(r"\frac{1}{2}", font_size=18)
frac_label.next_to(number_line.number_to_point(0.5), UP, buff=0.2)
```

### 4. 避免错误
- ❌ 不要在MathTex中使用中文
- ❌ 不要使用 `°` 符号，使用 `^\circ`
- ✅ 中文用Text，数学用MathTex
- ✅ 使用NumberLine的内置方法定位点

---

## 预期效果
- 清晰展示数轴的三要素
- 直观演示数与点的对应关系
- 生动展示比较大小的方法
- 适合六年级学生理解
- 总时长控制在60-75秒