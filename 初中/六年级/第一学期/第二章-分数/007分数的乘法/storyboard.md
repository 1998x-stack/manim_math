# 分数的乘法 (Fraction Multiplication) - 动画分镜脚本

## 元信息
- 目标时长: 70-85 秒
- 场景数量: 7 个
- 难度等级: 初级 (六年级)
- 视频格式: TikTok 竖屏 (1080×1920)

## 颜色配置
```python
COLOR_FRACTION_1 = "#3498db"      # 蓝色 - 第一个分数
COLOR_FRACTION_2 = "#e74c3c"      # 红色 - 第二个分数
COLOR_RESULT = "#2ecc71"          # 绿色 - 结果
COLOR_HIGHLIGHT = YELLOW          # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B          # 灰色 - 辅助
COLOR_GRID = WHITE                # 白色 - 网格
COLOR_SIMPLIFY = "#9b59b6"        # 紫色 - 约分
```

## 视觉元素设计

### 矩形网格参数
```python
# 用于可视化分数
GRID_WIDTH = 3.0          # 网格宽度
GRID_HEIGHT = 2.0         # 网格高度
GRID_POSITION = UP * 1    # 网格位置
```

## 知识点架构

### 核心公式
1. `a/b × c/d = (a×c)/(b×d)` - 分数乘分数
2. `a/b × n = (a×n)/b` - 分数乘整数
3. 先约分再相乘可简化计算

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题
3. 两个分数闪烁

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author)` | UP * 7 |
| 0.3s | 钩子问题 | `Write(hook_text)` | UP * 6 |
| 1.5s | 分数 2/3 出现 | `FadeIn(frac_1)` | LEFT * 1.5 + UP * 3.5 |
| 2.0s | 乘号出现 | `FadeIn(times_sign)` | UP * 3.5 |
| 2.5s | 分数 3/4 出现 | `FadeIn(frac_2)` | RIGHT * 1.5 + UP * 3.5 |
| 3.0s | 问号闪烁 | `Flash(question)` | RIGHT * 3 + UP * 3.5 |
| 4.0s | 提示文字 | `FadeIn(hint)` | UP * 2 |

### 钩子文字
- hook_text: "分数相乘，怎么算?"
- hint: "很简单! 让我来教你"

### 清理
- FadeOut: hook_text, hint, question
- 保留: author_info, frac_1, times_sign, frac_2

---

## Scene 2: 视觉化理解 (5-18秒)
**目的**: 用矩形网格直观展示 2/3 × 3/4

### 元素
1. 矩形网格
2. 分割线
3. 阴影区域

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 5.0s | 公式移到顶部 | `公式组.animate.move_to(UP*5.5)` | - |
| 5.5s | 标题出现 | `Write(title)` | UP * 4.5 |
| 6.5s | 矩形出现 | `Create(rectangle)` | ORIGIN |
| 7.5s | 水平分3份 | `Create(h_lines)` | - |
| 8.0s | 阴影2/3 (蓝色) | `FadeIn(shade_2_3)` | 上面2行 |
| 9.0s | 说明1 | `FadeIn(explain_1)` | DOWN * 3.5 |
| 10.0s | 垂直分4份 | `Create(v_lines)` | - |
| 10.5s | 阴影3/4 (红色叠加) | `FadeIn(shade_3_4)` | 左边3列 |
| 11.5s | 说明2 | `FadeIn(explain_2)` | DOWN * 4.5 |
| 12.5s | 重叠区域高亮 | `Indicate(overlap)` | 2×3=6格 |
| 13.5s | 说明3 | `FadeIn(explain_3)` | DOWN * 5.5 |
| 15.0s | 答案出现 | `FadeIn(answer)` | DOWN * 2 |
| 16.5s | 等待理解 | `Wait(1.5)` | - |

### 说明文字
- title: "视觉化理解"
- explain_1: "先取 2/3"
- explain_2: "再从中取 3/4"
- explain_3: "重叠部分 = 6格/12格 = 1/2"

### 清理
- FadeOut: rectangle, lines, shades, explains, title, answer
- 移动公式回中心
- 保留: author_info

---

## Scene 3: 乘法法则 (18-32秒)
**目的**: 展示核心计算规则

### 元素
1. 分步公式
2. 箭头指示
3. 高亮效果

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 18.0s | 标题 | `Write(title)` | UP * 5.5 |
| 19.0s | 原式 | `Write(step_0)` | UP * 3.5 |
| 20.0s | 分子×分子箭头 | `GrowArrow(arrow_num)` | - |
| 20.5s | 分子计算 | `FadeIn(num_calc)` | UP * 2 |
| 21.5s | 分母×分母箭头 | `GrowArrow(arrow_den)` | - |
| 22.0s | 分母计算 | `FadeIn(den_calc)` | UP * 1 |
| 23.0s | 结果 | `TransformMatchingTex(step_0, step_1)` | UP * 0 |
| 24.0s | 约分标题 | `FadeIn(simplify_title)` | DOWN * 1 |
| 25.0s | 约分过程 | `TransformMatchingTex(step_1, step_2)` | DOWN * 2 |
| 26.5s | 最终答案闪烁 | `Flash(final_answer)` | DOWN * 3.5 |
| 28.0s | 法则卡片 | `FadeIn(rule_card)` | DOWN * 5 |
| 30.0s | 等待理解 | `Wait(2.0)` | - |

### 法则卡片
"分数乘法: 分子相乘作分子，分母相乘作分母"

### 清理
- FadeOut: 所有计算步骤
- 保留: author_info

---

## Scene 4: 更多例子 (32-48秒)
**目的**: 巩固理解，展示不同类型

### 例子1: 1/2 × 4/5 (32-38秒)

| 时间 | 动作 | 元素位置 |
|------|------|---------|
| 32.0s | 例题1标题 | UP * 5 |
| 33.0s | 原式 | UP * 3 |
| 34.0s | 计算步骤 | UP * 1 |
| 35.0s | 结果 | DOWN * 1 |
| 36.5s | 检查是否能约分 | DOWN * 3 |

### 例子2: 2/3 × 9 (先转换) (38-44秒)

| 时间 | 动作 | 元素位置 |
|------|------|---------|
| 38.0s | 例题2标题 | UP * 5 |
| 39.0s | 原式 | UP * 3 |
| 40.0s | 转换为分数 | UP * 1 |
| 41.0s | 计算 | DOWN * 1 |
| 42.0s | 约分 | DOWN * 3 |
| 43.0s | 最终答案 | DOWN * 4.5 |

### 例子3: 先约分 3/4 × 8/9 (44-48秒)

| 时间 | 动作 | 元素位置 |
|------|------|---------|
| 44.0s | 例题3标题 | UP * 5 |
| 45.0s | 原式 | UP * 3 |
| 45.5s | 约分提示 | UP * 1.5 |
| 46.0s | 交叉约分 | UP * 0.5 |
| 46.5s | 简化后计算 | DOWN * 1.5 |
| 47.5s | 结果 | DOWN * 3 |

### 清理
- FadeOut: 所有例题
- 保留: author_info

---

## Scene 5: 运算律 (48-58秒)
**目的**: 展示分数乘法满足的运算律

### 元素
1. 三个运算律卡片
2. 示例公式

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 48.0s | 标题 | `Write(title)` | UP * 6 |
| 49.0s | 交换律卡片 | `FadeIn(card_1)` | UP * 4 |
| 50.5s | 结合律卡片 | `FadeIn(card_2)` | UP * 2 |
| 52.0s | 分配律卡片 | `FadeIn(card_3)` | UP * 0 |
| 53.5s | 示例公式 | `FadeIn(example)` | DOWN * 2.5 |
| 55.0s | 卡片闪烁 | `Indicate(cards)` | - |
| 57.0s | 等待 | `Wait(1.0)` | - |

### 运算律内容
- card_1: "交换律: a/b × c/d = c/d × a/b"
- card_2: "结合律: (a/b × c/d) × e/f = a/b × (c/d × e/f)"
- card_3: "分配律: a/b × (c/d + e/f) = a/b × c/d + a/b × e/f"

### 清理
- FadeOut: 所有卡片
- 保留: author_info

---

## Scene 6: 技巧总结 (58-70秒)
**目的**: 总结计算技巧

### 元素
1. 技巧卡片列表
2. 动画示例

### 动画序列
| 时间 | 动作 | 元素位置 |
|------|------|---------|
| 58.0s | 标题 | UP * 6 |
| 59.0s | 技巧1 | UP * 4.5 |
| 60.5s | 技巧2 | UP * 3.5 |
| 62.0s | 技巧3 | UP * 2.5 |
| 63.5s | 技巧4 | UP * 1.5 |
| 65.0s | 示例动画 | DOWN * 1 |
| 68.0s | 等待 | - |

### 技巧内容
1. "分子相乘，分母相乘"
2. "整数转化为分数 (分母为1)"
3. "能约分先约分，计算更简单"
4. "最后结果要化简"

### 清理
- FadeOut: 所有技巧卡片
- 保留: author_info

---

## Scene 7: 结尾与关注 (70-85秒)
**目的**: 总结回顾，引导关注

### 动画序列
| 时间 | 动作 | 元素位置 |
|------|------|---------|
| 70.0s | 总结标题 | UP * 6 |
| 71.0s | 关键点1 | UP * 4 |
| 72.0s | 关键点2 | UP * 3 |
| 73.0s | 关键点3 | UP * 2 |
| 74.5s | 作者信息放大 | UP * 0 |
| 76.0s | 关注文字 | DOWN * 2 |
| 77.0s | 装饰元素 | 周围 |
| 79.0s | 等待 | - |
| 81.0s | 全部淡出 | - |

### 关键点
1. "分子×分子，分母×分母"
2. "先约分再计算更简单"
3. "结果记得化简"

### 关注文字
"关注我，学更多数学技巧!"

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保留 |
| frac_1, frac_2 | Scene 1 | Scene 2 | 示例分数 |
| rectangle_grid | Scene 2 | Scene 2 | 可视化网格 |
| formula_steps | Scene 3 | Scene 3 | 计算步骤 |
| examples | Scene 4 | Scene 4 | 练习题 |
| law_cards | Scene 5 | Scene 5 | 运算律 |
| tips | Scene 6 | Scene 6 | 技巧总结 |
| summary | Scene 7 | Scene 7 | 最终总结 |

---

## 字体大小规范
```python
FONT_SIZES = {
    "title": 36,          # 大标题
    "subtitle": 28,       # 副标题
    "body": 22,           # 正文说明
    "formula": 32,        # 数学公式
    "label": 20,          # 标签
    "small": 18,          # 小字
    "author": 20,         # 作者信息
}
```

## 动画节奏控制
- 公式书写: 0.6-1.0s
- 图形创建: 0.8-1.2s
- 变换动画: 0.8-1.0s
- 理解停顿: 1.5-2.0s
- 场景切换: 0.5-0.7s

## 注意事项
1. 分数使用 `\frac{}{}`，不用 `\over`
2. 所有中文用 `Text()`
3. 颜色对比清晰
4. 网格精确绘制（使用循环）
5. 约分过程要清晰展示