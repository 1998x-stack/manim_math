# 相反数 (Opposite Numbers) - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 6 个
- 难度等级: 初级 (六年级)
- 视频格式: TikTok 竖屏 (1080×1920)

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要数字
COLOR_SECONDARY = "#e74c3c"    # 红色 - 相反数
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_ORIGIN = "#2ecc71"       # 绿色 - 原点
COLOR_NUMBERLINE = WHITE       # 白色 - 数轴
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 数轴长度 | 固定值 | `NUMBER_LINE_LENGTH = 7` | 从 -5 到 5 |
| 数轴位置 | 固定值 | `NUMBER_LINE_Y = 0` | 居中位置 |
| 单位长度 | `NUMBER_LINE_LENGTH / 10` | `UNIT_LENGTH` | 每单位在数轴上的长度 |
| 数字位置 | `ORIGIN + RIGHT * n * UNIT_LENGTH` | `point_n` | 数字 n 的位置 |
| 对称点位置 | `ORIGIN - RIGHT * n * UNIT_LENGTH` | `point_neg_n` | -n 的位置 |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字)
3. 两个神秘数字闪烁

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | UP * 7 |
| 0.3s | 钩子问题书写 | `Write(hook_text)` | UP * 6 |
| 1.5s | 数字 3 淡入 | `FadeIn(num_3, scale=1.2)` | LEFT * 2 + UP * 3 |
| 2.0s | 数字 -3 淡入 | `FadeIn(num_neg3, scale=1.2)` | RIGHT * 2 + UP * 3 |
| 2.5s | 两数字闪烁 | `Flash()` | - |
| 3.0s | 提示文字 | `FadeIn(hint)` | UP * 1.5 |
| 4.0s | 等待 | `Wait(1.0)` | - |

### 清理
- FadeOut: hook_text, hint, num_3, num_neg3
- 保留: author_info

---

## Scene 2: 数轴引入 (5-15秒)
**目的**: 建立数轴概念，展示原点

### 元素
1. 数轴 (NumberLine)
2. 原点标记
3. 正负方向标注

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 5.0s | 数轴生长 | `Create(number_line)` | y = 0 |
| 6.0s | 刻度线创建 | `Create(tick_marks)` | - |
| 6.5s | 数字标签依次出现 | `FadeIn(labels, lag_ratio=0.1)` | - |
| 8.0s | 原点高亮 | `Indicate(origin_dot)` | ORIGIN |
| 8.5s | 原点标签 | `FadeIn(origin_label)` | DOWN * 0.5 |
| 9.0s | 方向箭头 | `GrowArrow(pos_arrow), GrowArrow(neg_arrow)` | 数轴两端 |
| 9.5s | 方向文字 | `FadeIn(pos_text), FadeIn(neg_text)` | 箭头旁边 |
| 10.5s | 说明文字 | `FadeIn(explanation)` | DOWN * 4 |
| 12.0s | 等待理解 | `Wait(1.5)` | - |

### 清理
- FadeOut: explanation, pos_arrow, neg_arrow, pos_text, neg_text
- 保留: number_line, tick_marks, labels, origin_dot, origin_label

---

## Scene 3: 相反数定义 (15-30秒)
**目的**: 通过具体例子展示相反数概念

### 元素
1. 数字 3 和 -3 在数轴上
2. 虚线连接到原点
3. 距离标注
4. 定义文字

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 15.0s | 标题出现 | `Write(title)` | UP * 5.5 |
| 16.0s | 点 3 出现 | `FadeIn(dot_3, scale=1.5)` | RIGHT * 3 * UNIT |
| 16.5s | 标签 3 | `FadeIn(label_3)` | dot_3 上方 |
| 17.5s | 点 -3 出现 | `FadeIn(dot_neg3, scale=1.5)` | LEFT * 3 * UNIT |
| 18.0s | 标签 -3 | `FadeIn(label_neg3)` | dot_neg3 上方 |
| 19.0s | 到原点虚线 (3) | `Create(dash_3)` | 3 → 0 |
| 19.5s | 到原点虚线 (-3) | `Create(dash_neg3)` | -3 → 0 |
| 20.0s | 距离标注 (3) | `FadeIn(dist_3)` | dash_3 中点 |
| 20.5s | 距离标注 (-3) | `FadeIn(dist_neg3)` | dash_neg3 中点 |
| 21.0s | 高亮距离相等 | `Indicate(dist_3), Indicate(dist_neg3)` | - |
| 22.0s | 定义文字 1 | `FadeIn(def_1)` | DOWN * 3.5 |
| 23.5s | 定义文字 2 | `FadeIn(def_2)` | DOWN * 4.5 |
| 25.0s | 等待理解 | `Wait(2.0)` | - |

### 定义文字
- def_1: "只有符号不同的两个数"
- def_2: "叫做互为相反数"

### 清理
- FadeOut: title, dash_3, dash_neg3, dist_3, dist_neg3, def_1, def_2
- 保留: number_line, labels, origin_dot, origin_label, dot_3, dot_neg3, label_3, label_neg3

---

## Scene 4: 更多例子 (30-45秒)
**目的**: 展示多组相反数，加深理解

### 元素
1. 多组数字对
2. 对称动画
3. 公式卡片

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 30.0s | 清理前例 | `FadeOut(dot_3, dot_neg3, label_3, label_neg3)` | - |
| 31.0s | 例子 2: 点 5 | `FadeIn(dot_5)` | RIGHT * 5 * UNIT |
| 31.5s | 对称生成 -5 | `TransformFromCopy(dot_5, dot_neg5)` | LEFT * 5 * UNIT |
| 32.5s | 标签同步 | `FadeIn(label_5, label_neg5)` | - |
| 33.5s | 例子 3: 点 1.5 | `FadeIn(dot_1_5)` | RIGHT * 1.5 * UNIT |
| 34.0s | 对称生成 -1.5 | `TransformFromCopy(dot_1_5, dot_neg1_5)` | LEFT * 1.5 * UNIT |
| 35.0s | 标签同步 | `FadeIn(label_1_5, label_neg1_5)` | - |
| 36.0s | 公式卡片 1 | `FadeIn(formula_1)` | UP * 3 |
| 37.5s | 公式卡片 2 | `FadeIn(formula_2)` | UP * 2 |
| 39.0s | 公式卡片 3 | `FadeIn(formula_3)` | UP * 1 |
| 41.0s | 等待理解 | `Wait(2.0)` | - |

### 公式卡片
- formula_1: "a 的相反数是 -a"
- formula_2: "-(-a) = a"
- formula_3: "a + (-a) = 0"

### 清理
- FadeOut: 所有点和标签
- FadeOut: formula_1, formula_2, formula_3
- 保留: number_line, tick_marks, labels, origin_dot, origin_label

---

## Scene 5: 特殊情况 (45-55秒)
**目的**: 强调 0 的相反数是 0

### 元素
1. 原点高亮
2. 特殊说明文字
3. 强调动画

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 45.0s | 原点放大 | `origin_dot.animate.scale(2)` | ORIGIN |
| 45.5s | 原点闪烁 | `Flash(origin_dot)` | - |
| 46.0s | 特殊标题 | `Write(special_title)` | UP * 5 |
| 47.0s | 说明 1 | `FadeIn(special_1)` | UP * 3 |
| 48.5s | 说明 2 | `FadeIn(special_2)` | UP * 2 |
| 50.0s | 公式高亮 | `FadeIn(special_formula, scale=1.3)` | ORIGIN |
| 52.0s | 等待理解 | `Wait(1.5)` | - |

### 特殊说明
- special_title: "特殊情况"
- special_1: "0 的相反数是 0"
- special_2: "因为 0 到原点的距离是 0"
- special_formula: "0 + 0 = 0"

### 清理
- FadeOut: special_title, special_1, special_2, special_formula
- origin_dot.animate.scale(0.5) # 恢复原大小
- 保留: number_line, labels, origin_dot, origin_label

---

## Scene 6: 总结与关注 (55-75秒)
**目的**: 总结关键点，引导关注

### 元素
1. 关键点卡片
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 元素位置 |
|------|------|---------|---------|
| 55.0s | 数轴淡出 | `FadeOut(number_line, labels, origin_dot, origin_label)` | - |
| 56.0s | 总结标题 | `Write(summary_title)` | UP * 6 |
| 57.0s | 要点 1 | `FadeIn(point_1, shift=UP*0.3)` | UP * 4 |
| 58.0s | 要点 2 | `FadeIn(point_2, shift=UP*0.3)` | UP * 3 |
| 59.0s | 要点 3 | `FadeIn(point_3, shift=UP*0.3)` | UP * 2 |
| 60.0s | 要点 4 | `FadeIn(point_4, shift=UP*0.3)` | UP * 1 |
| 62.0s | 作者放大 | `Transform(author_info, author_large)` | UP * 0 |
| 63.0s | 关注文字 | `FadeIn(follow_text, scale=1.2)` | DOWN * 2 |
| 64.0s | 装饰元素 | `FadeIn(decorations)` | 周围 |
| 66.0s | 等待 | `Wait(2.0)` | - |
| 68.0s | 全部淡出 | `FadeOut(everything)` | - |

### 总结要点
- summary_title: "相反数知识点总结"
- point_1: "① 符号不同,绝对值相等"
- point_2: "② 在数轴上关于原点对称"
- point_3: "③ a + (-a) = 0"
- point_4: "④ 0 的相反数是 0"

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 始终保留在顶部 |
| number_line | Scene 2 | Scene 6 | 主要教学元素 |
| tick_marks | Scene 2 | Scene 6 | 数轴刻度 |
| labels | Scene 2 | Scene 6 | 数字标签 |
| origin_dot | Scene 2 | Scene 6 | 原点标记 |
| hook_text | Scene 1 | Scene 1 | 临时钩子 |
| dot_3, dot_neg3 | Scene 3 | Scene 4 | 示例点 |
| formulas | Scene 4 | Scene 4 | 公式卡片 |
| special_elements | Scene 5 | Scene 5 | 特殊说明 |
| summary_elements | Scene 6 | Scene 6 | 总结卡片 |

---

## 字体大小规范
```python
FONT_SIZES = {
    "title": 36,          # 大标题
    "subtitle": 28,       # 副标题
    "body": 22,           # 正文说明
    "label": 24,          # 数字标签
    "small": 18,          # 小字/注释
    "author": 20,         # 作者信息
    "formula": 28,        # 数学公式
}
```

## 动画节奏控制
- 简单出现: 0.3-0.5s
- 数字/点出现: 0.5-0.8s
- 文字书写: 0.6-1.0s
- 理解停顿: 1.5-2.0s
- 场景切换: 0.5-0.8s

## 注意事项
1. 所有数字位置必须精确计算
2. 对称关系必须完美 (距离原点相等)
3. 中文使用 Text(), 数学公式使用 MathTex()
4. 颜色对比要清晰 (正数蓝,负数红)
5. 原点必须特别标注 (绿色)