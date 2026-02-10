# 函数的最值 - 动画分镜脚本

## 元信息
- 题目：函数的最值
- 年级：高一第一学期
- 目标时长：60-75 秒
- 场景数量：6 个
- 难度等级：中等

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主函数曲线
COLOR_SECONDARY = "#e74c3c"      # 红色 - 最大值点
COLOR_TERTIARY = "#2ecc71"       # 绿色 - 最小值点
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_AXES = WHITE               # 白色 - 坐标轴
```

## 坐标系配置
```python
# 主坐标系配置
AXES_CONFIG = {
    "x_range": [-3, 3, 1],
    "y_range": [-2, 4, 1],
    "x_length": 7,
    "y_length": 8,
    "axis_config": {
        "include_numbers": True,
        "font_size": 20,
    }
}

# 坐标系位置：y = 0.5 (居中偏上)
AXES_POSITION = UP * 0.5
```

## 函数定义
```python
# 主函数：二次函数 f(x) = -(x-1)² + 3
def main_function(x):
    return -(x - 1)**2 + 3

# 关键点：
# - 最大值点：(1, 3)
# - 定义域：[-2, 2]（闭区间）
# - 端点值：f(-2) = -6, f(2) = 2
```

## 几何/坐标预计算清单
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 坐标轴 | Axes(...) | self.axes | 主坐标系 |
| 函数曲线 | axes.plot(f, x_range=[-2,2]) | self.graph | 完整曲线 |
| 最大值点 | (1, 3) | self.max_point | 顶点 |
| 左端点 | (-2, f(-2)) | self.left_endpoint | 定义域左端 |
| 右端点 | (2, f(2)) | self.right_endpoint | 定义域右端 |
| 最大值坐标 | axes.c2p(1, 3) | self.max_coords | 屏幕坐标 |
| 左端坐标 | axes.c2p(-2, f(-2)) | self.left_coords | 屏幕坐标 |
| 右端坐标 | axes.c2p(2, f(2)) | self.right_coords | 屏幕坐标 |

---

## Scene 1: 开场钩子 (0-4秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识（顶部）
2. 钩子问题（大字）
3. 函数示意图（简化版）

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 简化曲线创建 | `Create(simple_curve)` | 1.0s |
| 2.1s | 问号闪烁 | `Flash(question_mark)` | 0.5s |
| 2.6s | 等待 | `Wait(1.4)` | 1.4s |

### 具体内容
- **作者信息**: "上海初高中数学直通车 @emptyandcalm" (y=7, 小字)
- **钩子问题**: "函数有最高点吗?" (y=5.5, 大字 48pt)
- **简化曲线**: 抛物线示意，无坐标轴

### 清理
- FadeOut: hook_text, simple_curve
- 保留: author_info

---

## Scene 2: 定义引入 (4-12秒)
**目的**: 介绍最值的数学定义

### 元素
1. 标题："函数的最值"
2. 定义文字（分步显示）
3. 数学公式

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 4.0s | 标题书写 | `Write(title)` | 0.8s |
| 4.8s | 定义1淡入 | `FadeIn(def_1, shift=UP*0.2)` | 0.6s |
| 5.4s | 公式1书写 | `Write(formula_1)` | 1.0s |
| 6.4s | 定义2淡入 | `FadeIn(def_2, shift=UP*0.2)` | 0.6s |
| 7.0s | 公式2书写 | `Write(formula_2)` | 1.0s |
| 8.0s | 关键提示淡入 | `FadeIn(note)` | 0.5s |
| 8.5s | 等待 | `Wait(3.5)` | 3.5s |

### 具体内容
- **标题**: "函数的最值" (y=5.5, 36pt)
- **定义1**: "最大值: 函数在定义域内的最高点" (y=4.2, 22pt)
- **公式1**: `$\forall x \in D, f(x) \leq f(x_0)$` (y=3.5, 26pt)
- **定义2**: "最小值: 函数在定义域内的最低点" (y=2.5, 22pt)
- **公式2**: `$\forall x \in D, f(x) \geq f(x_0)$` (y=1.8, 26pt)
- **关键提示**: "注意: 最值是整体概念!" (y=0.8, 20pt, YELLOW)

### 清理
- FadeOut: title, def_1, formula_1, def_2, formula_2, note
- 保留: author_info

---

## Scene 3: 坐标系与函数 (12-20秒)
**目的**: 绘制坐标系和函数曲线

### 元素
1. 坐标轴
2. 函数曲线（闭区间）
3. 函数表达式标签
4. 定义域标注

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 12.0s | 坐标轴创建 | `Create(axes)` | 1.2s |
| 13.2s | 函数曲线绘制 | `Create(graph)` | 1.5s |
| 14.7s | 函数标签淡入 | `FadeIn(func_label)` | 0.5s |
| 15.2s | 定义域标注 | `Create(domain_brace), Write(domain_text)` | 0.8s |
| 16.0s | 端点标记 | `FadeIn(left_dot), FadeIn(right_dot)` | 0.5s |
| 16.5s | 等待 | `Wait(3.5)` | 3.5s |

### 具体内容
- **坐标轴**: x ∈ [-3, 3], y ∈ [-2, 4]
- **函数**: f(x) = -(x-1)² + 3, x ∈ [-2, 2]
- **函数标签**: `$f(x) = -(x-1)^2 + 3$` (右上方)
- **定义域**: 用 Brace 标注 x ∈ [-2, 2]
- **端点**: 实心点标记 x=-2 和 x=2

### 清理
- 保留: axes, graph, author_info
- FadeOut: func_label, domain_brace, domain_text（会在后续场景重新引入）

---

## Scene 4: 标记最大值 (20-32秒)
**目的**: 找到并标注最大值点

### 元素
1. 最大值点及标签
2. 虚线辅助线（垂直+水平）
3. 最大值说明文字
4. 数值标注

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 20.0s | 扫描动画 | `tracker.animate.set_value(1)` | 1.5s |
| 21.5s | 最大值点放大 | `FadeIn(max_dot, scale=0.5), Flash(max_dot)` | 0.6s |
| 22.1s | 虚线绘制 | `Create(v_line), Create(h_line)` | 0.8s |
| 22.9s | 坐标标签 | `Write(x_label), Write(y_label)` | 0.6s |
| 23.5s | 最大值说明 | `FadeIn(max_text)` | 0.5s |
| 24.0s | 数学表达式 | `Write(max_formula)` | 0.8s |
| 24.8s | 高亮闪烁 | `Indicate(max_dot)` | 0.5s |
| 25.3s | 等待 | `Wait(6.7)` | 6.7s |

### 具体内容
- **扫描动画**: 小点沿曲线移动，寻找最高点
- **最大值点**: 红色大点，坐标 (1, 3)
- **虚线**: 从点到 x 轴和 y 轴的虚线
- **坐标**: x₀ = 1, f(x₀) = 3
- **说明**: "最大值: f(1) = 3" (y=-3.5, 24pt, RED)
- **公式**: `$\forall x \in [-2,2], f(x) \leq 3$` (y=-4.5, 22pt)

### 清理
- 保留: axes, graph, max_dot, author_info
- FadeOut: v_line, h_line, x_label, y_label, max_text, max_formula

---

## Scene 5: 对比端点值 (32-45秒)
**目的**: 说明最值可能在端点取得

### 元素
1. 端点标记和标签
2. 对比箭头
3. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 32.0s | 端点强调 | `Indicate(left_dot), Indicate(right_dot)` | 0.8s |
| 32.8s | 端点值标签 | `FadeIn(left_value), FadeIn(right_value)` | 0.6s |
| 33.4s | 对比箭头 | `GrowArrow(arrow_1), GrowArrow(arrow_2)` | 0.8s |
| 34.2s | 说明文字1 | `FadeIn(explain_1)` | 0.5s |
| 34.7s | 说明文字2 | `FadeIn(explain_2)` | 0.5s |
| 35.2s | 总结强调 | `FadeIn(summary, scale=1.1)` | 0.6s |
| 35.8s | 等待 | `Wait(9.2)` | 9.2s |

### 具体内容
- **左端点**: x = -2, f(-2) = -6 (GREEN 绿色点)
- **右端点**: x = 2, f(2) = 2 (GREEN 绿色点)
- **对比箭头**: 从端点指向最大值点
- **说明1**: "端点值: f(-2) = -6" (LEFT, 20pt)
- **说明2**: "端点值: f(2) = 2" (RIGHT, 20pt)
- **总结**: "最大值在顶点, 最小值在左端点!" (y=-5, 24pt, YELLOW)

### 清理
- 保留: axes, graph, max_dot, author_info
- FadeOut: left_dot, right_dot, left_value, right_value, arrow_1, arrow_2, explain_1, explain_2, summary

---

## Scene 6: 方法总结 (45-60秒)
**目的**: 总结求最值的方法

### 元素
1. 方法卡片（4种方法）
2. 关键提示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 45.0s | 标题淡入 | `FadeIn(methods_title)` | 0.5s |
| 45.5s | 方法1卡片 | `card_1.animate.shift(RIGHT*0)` | 0.4s |
| 45.9s | 方法2卡片 | `card_2.animate.shift(RIGHT*0)` | 0.4s |
| 46.3s | 方法3卡片 | `card_3.animate.shift(RIGHT*0)` | 0.4s |
| 46.7s | 方法4卡片 | `card_4.animate.shift(RIGHT*0)` | 0.4s |
| 47.1s | 关键提示 | `FadeIn(key_note, scale=1.1)` | 0.6s |
| 47.7s | 等待 | `Wait(12.3)` | 12.3s |

### 具体内容
- **标题**: "求最值的方法" (y=5, 32pt)
- **方法1**: "① 单调性 (闭区间端点)" (y=3, 22pt)
- **方法2**: "② 配方法 (二次函数)" (y=2, 22pt)
- **方法3**: "③ 基本不等式" (y=1, 22pt)
- **方法4**: "④ 数形结合 (图像法)" (y=0, 22pt)
- **关键**: "记住: 最值≠极值!" (y=-2, 24pt, YELLOW)

### 清理
- FadeOut: 全部元素（除了 author_info）
- 保留: author_info（片尾需要）

---

## Scene 7: 片尾关注 (60-75秒)
**目的**: 引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 60.0s | 作者信息放大 | `Transform(author_info, author_large)` | 0.8s |
| 60.8s | ID显示 | `FadeIn(author_id)` | 0.5s |
| 61.3s | 关注文字 | `FadeIn(follow_text, scale=1.1)` | 0.6s |
| 61.9s | 装饰动画 | `FadeIn(decorations), Rotate(decorations)` | 1.5s |
| 63.4s | 图标闪烁 | `FadeIn(icons)` | 0.6s |
| 64.0s | 等待 | `Wait(1.0)` | 1.0s |
| 65.0s | 全部淡出 | `FadeOut(VGroup(*))` | 1.0s |

### 具体内容
- **作者名**: "上海初高中数学直通车" (40pt)
- **作者ID**: "@emptyandcalm" (32pt)
- **关注**: "关注我, 学更多数学技巧!" (30pt, YELLOW)
- **装饰**: 旋转的小图标

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| axes | Scene 3 | Scene 6 | 主坐标系 |
| graph | Scene 3 | Scene 6 | 函数曲线 |
| max_dot | Scene 4 | Scene 6 | 最大值点 |
| hook_text | Scene 1 | Scene 1 | 临时钩子 |
| title (Scene 2) | Scene 2 | Scene 2 | 临时标题 |
| methods_title | Scene 6 | Scene 6 | 临时标题 |

---

## 边界安全检查
```python
# 安全边界（TikTok竖屏）
SAFE_BOUNDS = {
    "x_min": -4.0,
    "x_max": 4.0,
    "y_min": -7.0,
    "y_max": 7.0
}

# 关键元素位置检查
# - author_info: y=7 (边界)
# - 主内容区: y ∈ [-3, 5.5]
# - 坐标轴中心: y=0.5
# - 底部文字: y ∈ [-6, -3]
```

---

## 技术约束检查清单
- [ ] 所有坐标通过 axes.c2p() 精确计算
- [ ] 中文使用 Text()，数学公式使用 MathTex()
- [ ] 度数符号使用 `^\circ` 而非 °
- [ ] 虚线使用 DashedLine
- [ ] 所有元素在安全边界内
- [ ] 字体大小符合规范
- [ ] 动画节奏符合指南
- [ ] 难点有足够停留时间

---

## 总时长分配
| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1: 开场 | 4s | 4s |
| Scene 2: 定义 | 8s | 12s |
| Scene 3: 函数 | 8s | 20s |
| Scene 4: 最大值 | 12s | 32s |
| Scene 5: 端点对比 | 13s | 45s |
| Scene 6: 方法总结 | 15s | 60s |
| Scene 7: 片尾 | 6s | 66s |
| **总计** | **66s** | - |

目标：60-75秒 ✅