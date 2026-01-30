# 有理数的概念 - 动画分镜脚本

## 元信息
- 目标时长: 75-90 秒
- 场景数量: 7 个
- 难度等级: 初级 (六年级)
- 目标: 理解有理数的定义和分类

## 颜色配置
```python
COLOR_INTEGER = "#3498db"        # 蓝色 - 整数
COLOR_FRACTION = "#e74c3c"       # 红色 - 分数
COLOR_POSITIVE = "#2ecc71"       # 绿色 - 正数
COLOR_NEGATIVE = "#f39c12"       # 橙色 - 负数
COLOR_ZERO = "#9b59b6"           # 紫色 - 零
COLOR_RATIONAL = "#1abc9c"       # 青色 - 有理数整体
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
BACKGROUND = "#1a1a2e"
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 数轴中心 | ORIGIN + DOWN*1 | self.numberline_center |
| 树状图根节点 | UP*3 | self.tree_root |
| 分类框位置 | 计算布局 | self.box_positions |
| 示例数字位置 | 均匀分布 | self.example_positions |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字醒目)
3. 数字云团动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` "这些数字有什么共同点?" |
| 1.0s | 数字云团出现 | `FadeIn(numbers_cloud)` 显示: 3, -5, 1/2, 0, -2.5, 0.333... |
| 2.5s | 数字闪烁强调 | `Indicate(numbers)` |
| 3.0s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_text, numbers_cloud
- 保留: author_info

---

## Scene 2: 引入定义 (8-10秒)
**目的**: 给出有理数的数学定义

### 元素
1. 标题: "有理数 Rational Numbers"
2. 定义框
3. 公式展示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title)` |
| 0.8s | 定义框淡入 | `FadeIn(definition_box)` |
| 1.2s | 文字说明 | `Write(text)` "整数和分数的统称" |
| 2.5s | 公式出现 | `Write(formula)` Q = {p/q \| p,q∈Z, q≠0} |
| 4.0s | 公式高亮 | `Indicate(formula)` |
| 5.0s | 补充说明 | `FadeIn(note)` "可表示为两个整数之比" |
| 6.5s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: definition_box, note
- 保留: title (移到顶部缩小)

---

## Scene 3: 分类方法一 - 按符号 (12-15秒)
**目的**: 展示按符号分类：正有理数、零、负有理数

### 元素
1. 数轴
2. 三个分类框
3. 示例数字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题 | `Write(subtitle)` "分类方法一: 按符号" |
| 0.8s | 数轴创建 | `Create(numberline)` |
| 1.5s | 零点标记 | `FadeIn(zero_dot)` 紫色高亮 |
| 2.0s | 正数区域 | `FadeIn(positive_region)` 绿色阴影 |
| 2.5s | 负数区域 | `FadeIn(negative_region)` 橙色阴影 |
| 3.0s | 示例数字飞入 | `FadeIn(examples)` 3, 1/2, 0.5 → 正; 0; -2, -1/3, -0.8 → 负 |
| 5.0s | 分类框出现 | `Create(classification_boxes)` |
| 6.0s | 数字归类动画 | `Transform(examples → boxes)` |
| 8.0s | 标签添加 | `Write(labels)` "正有理数", "零", "负有理数" |
| 9.5s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: subtitle, classification_boxes, examples
- 保留: numberline (淡化)

---

## Scene 4: 分类方法二 - 按类型 (12-15秒)
**目的**: 展示按类型分类：整数、分数

### 元素
1. 树状图结构
2. 两个主分支
3. 示例数字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题 | `Write(subtitle)` "分类方法二: 按类型" |
| 0.8s | 根节点 | `FadeIn(root_node)` "有理数" |
| 1.5s | 第一层分支 | `GrowFromCenter(branches)` → "整数" 和 "分数" |
| 2.5s | 整数展开 | `GrowFromCenter(integer_sub)` → "正整数", "零", "负整数" |
| 3.8s | 分数展开 | `GrowFromCenter(fraction_sub)` → "正分数", "负分数" |
| 5.0s | 示例填充-整数 | `FadeIn(int_examples)` 3, 0, -5 |
| 6.0s | 示例填充-分数 | `FadeIn(frac_examples)` 1/2, -3/4 |
| 7.5s | 树状图整体缩放 | `tree.animate.scale(0.85)` |
| 8.5s | 等待理解 | `Wait(2.5)` |

### 清理
- 保留: tree (移到上方缩小)

---

## Scene 5: 小数表示 (10-12秒)
**目的**: 说明有理数可表示为有限或循环小数

### 元素
1. 转换动画
2. 小数示例
3. 循环标记

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题 | `Write(subtitle)` "小数表示" |
| 0.8s | 分数示例 | `Write(fraction)` 1/2, 1/3, 1/4 |
| 1.5s | 转换箭头 | `GrowArrow(arrows)` |
| 2.0s | 小数结果 | `Write(decimals)` 0.5, 0.333..., 0.25 |
| 3.5s | 循环标记 | `Create(repeat_mark)` 在0.333...上方画循环符号 |
| 4.5s | 说明文字 | `FadeIn(note)` "有限小数或无限循环小数" |
| 6.0s | 反例提示 | `FadeIn(counter_example)` "注: √2, π 不是有理数" |
| 8.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: 全部元素

---

## Scene 6: 实例演练 (12-15秒)
**目的**: 判断数字是否为有理数，巩固理解

### 元素
1. 数字卡片
2. 判断框（是/否）
3. 勾叉动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题 | `Write(subtitle)` "判断练习" |
| 0.8s | 判断框 | `Create(yes_no_boxes)` 左边"是", 右边"否" |
| 1.5s | 数字1出现 | `FadeIn(num1)` "7" |
| 2.0s | 移动到"是" | `num1.animate.move_to(yes_box)` |
| 2.5s | 打勾 | `Create(checkmark)` |
| 3.0s | 数字2出现 | `FadeIn(num2)` "-3/5" |
| 3.5s | 移动到"是" | `num2.animate.move_to(yes_box)` |
| 4.0s | 打勾 | `Create(checkmark)` |
| 4.5s | 数字3出现 | `FadeIn(num3)` "0.666..." |
| 5.0s | 移动到"是" | `num3.animate.move_to(yes_box)` |
| 5.5s | 打勾 | `Create(checkmark)` |
| 6.0s | 数字4出现 | `FadeIn(num4)` "√3" |
| 6.5s | 移动到"否" | `num4.animate.move_to(no_box)` |
| 7.0s | 打叉 | `Create(crossmark)` |
| 7.5s | 说明 | `FadeIn(explanation)` "无理数!" |
| 9.0s | 等待 | `Wait(2.5)` |

### 清理
- FadeOut: 全部元素

---

## Scene 7: 总结与片尾 (8-10秒)
**目的**: 知识点总结，品牌露出

### 元素
1. 关键要点卡片
2. 公式回顾
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` "有理数 - 知识要点" |
| 1.0s | 要点1 | `FadeIn(point1)` "① 整数和分数的统称" |
| 2.0s | 要点2 | `FadeIn(point2)` "② 可表示为 p/q (q≠0)" |
| 3.0s | 要点3 | `FadeIn(point3)` "③ 有限或循环小数" |
| 4.5s | 公式回顾 | `Write(formula)` Q = {整数} ∪ {分数} |
| 6.0s | 作者信息放大 | `author_info.animate.scale(2)` |
| 7.0s | 关注提示 | `FadeIn(follow_text)` "关注我，学更多数学技巧!" |
| 8.5s | 全部淡出 | `FadeOut(all)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| title | Scene 2 | Scene 2 | 后续缩小移至顶部 |
| numberline | Scene 3 | Scene 4 | 淡化后保留 |
| tree | Scene 4 | Scene 5 | 缩小后清除 |
| examples | Scene 3/4 | 各自场景 | 临时展示 |
| formulas | Scene 2/7 | 各自场景 | 关键公式 |

---

## 时间节奏控制
- 定义场景: 慢 (2.0s 等待)
- 分类展示: 中速 (1.5s 等待)
- 练习判断: 快速 (0.5s 间隔)
- 总结场景: 中速 (1.5s 等待)

## 字体大小使用
- 标题: 36-40
- 副标题: 28-32
- 正文: 22-24
- 公式: 28-32
- 小字说明: 18-20