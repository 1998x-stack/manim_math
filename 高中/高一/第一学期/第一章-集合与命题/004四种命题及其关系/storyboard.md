# 四种命题及其关系 - 动画分镜脚本

## 元信息
- 目标时长: 70-85 秒
- 场景数量: 9 个
- 难度等级: 高一
- 知识点: 原命题、逆命题、否命题、逆否命题及其等价关系

## 颜色配置
```python
COLOR_ORIGINAL = "#e74c3c"      # 红色 - 原命题
COLOR_CONVERSE = "#3498db"      # 蓝色 - 逆命题
COLOR_INVERSE = "#2ecc71"       # 绿色 - 否命题
COLOR_CONTRAPOSITIVE = "#f39c12"  # 橙色 - 逆否命题
COLOR_HIGHLIGHT = YELLOW
COLOR_ARROW = "#95a5a6"         # 灰色 - 箭头
COLOR_EQUIV = "#9b59b6"         # 紫色 - 等价关系
BACKGROUND_COLOR = "#1a1a2e"
```

## 元素位置规划
| 元素类型 | 位置 | 说明 |
|---------|------|------|
| 标题 | UP * 6.5 | 场景标题 |
| 命题框 | UP * 3 到 DOWN * 2 | 主内容区 |
| 说明文字 | DOWN * 4 | 解释说明 |
| 关系图 | ORIGIN | 四种命题关系图 |

---

## Scene 1: 开场介绍 (4-5秒)
**目的**: 钩子 + 引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题
3. 四个命题框预览

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author)` |
| 0.3s | 钩子标题 | `Write(hook)` |
| 1.0s | 四个命题框闪现 | `FadeIn(boxes)` |
| 3.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook, preview_boxes
- 保留: author_info

---

## Scene 2: 什么是命题 (6-7秒)
**目的**: 定义命题

### 元素
1. 标题："命题"
2. 定义文字
3. 示例

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title)` |
| 0.6s | 定义展示 | `FadeIn(definition)` |
| 1.5s | 示例展示 | `Write(example)` |
| 4.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: all
- 保留: none

---

## Scene 3: 原命题 (7-8秒)
**目的**: 介绍原命题形式

### 元素
1. 标题："原命题"
2. 形式：若 p 则 q
3. 具体例子
4. 命题框

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title)` |
| 0.6s | 形式展示 | `Write(form)` |
| 1.5s | 命题框创建 | `Create(box)` |
| 2.5s | 例子展示 | `Write(example)` |
| 5.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, form
- 保留: original_box, example

---

## Scene 4: 逆命题 (7-8秒)
**目的**: 介绍逆命题（交换条件和结论）

### 元素
1. 标题："逆命题"
2. 形式：若 q 则 p
3. 从原命题变换的动画
4. 具体例子

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title)` |
| 0.6s | 原命题框移到左边 | `original_box.animate.shift(LEFT*2)` |
| 1.5s | 箭头指示变换 | `Create(arrow)` |
| 2.0s | 逆命题框创建 | `Create(converse_box)` |
| 3.0s | 高亮交换 | `Indicate(p_q)` |
| 5.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, arrow
- 保留: original_box, converse_box

---

## Scene 5: 否命题 (7-8秒)
**目的**: 介绍否命题（否定条件和结论）

### 元素
1. 标题："否命题"
2. 形式：若 ¬p 则 ¬q
3. 从原命题变换的动画
4. 具体例子

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title)` |
| 0.6s | 重新排列命题框 | `ReplacementTransform` |
| 1.5s | 箭头指示变换 | `Create(arrow)` |
| 2.0s | 否命题框创建 | `Create(inverse_box)` |
| 3.0s | 高亮否定符号 | `Indicate(neg)` |
| 5.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, arrow
- 保留: original_box, converse_box, inverse_box

---

## Scene 6: 逆否命题 (7-8秒)
**目的**: 介绍逆否命题（交换并否定）

### 元素
1. 标题："逆否命题"
2. 形式：若 ¬q 则 ¬p
3. 从原命题变换的动画
4. 具体例子

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title)` |
| 0.6s | 重新排列命题框 | `ReplacementTransform` |
| 1.5s | 箭头指示变换 | `Create(arrow)` |
| 2.0s | 逆否命题框创建 | `Create(contrapositive_box)` |
| 3.0s | 高亮变换 | `Indicate` |
| 5.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, arrow
- 保留: 四个命题框

---

## Scene 7: 关系图 (10-12秒)
**目的**: 展示四种命题的关系结构

### 元素
1. 四个命题框排列成矩形
2. 箭头连接
3. 等价关系标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 四个框移动到矩形位置 | `animate.move_to` |
| 1.5s | 绘制连接箭头 | `Create(arrows)` |
| 3.0s | 标注"互逆" | `FadeIn(labels)` |
| 4.5s | 高亮等价关系 | `Indicate(equiv_pairs)` |
| 7.0s | 等待理解 | `Wait(3.0)` |

### 清理
- FadeOut: arrows, labels
- 保留: boxes

---

## Scene 8: 等价关系强调 (8-10秒)
**目的**: 强调等价命题的应用

### 元素
1. 标题："等价关系"
2. 公式：(p → q) ⟺ (¬q → ¬p)
3. 应用说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `Write(title)` |
| 0.6s | 等价公式 | `Write(equiv_formula)` |
| 1.5s | 原命题和逆否命题高亮 | `Indicate` |
| 3.0s | 说明文字 | `FadeIn(explanation)` |
| 5.0s | 例子展示 | `Write(example)` |
| 7.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: all
- 保留: none

---

## Scene 9: 片尾关注 (4-5秒)
**目的**: 引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰元素（四个命题框小图标）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息放大 | `Transform(author)` |
| 0.8s | 关注提示 | `FadeIn(follow)` |
| 1.5s | 装饰动画 | `Rotate` |
| 3.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: all

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 9 | 作者信息 |
| original_box | Scene 3 | Scene 8 | 原命题框 |
| converse_box | Scene 4 | Scene 8 | 逆命题框 |
| inverse_box | Scene 5 | Scene 8 | 否命题框 |
| contrapositive_box | Scene 6 | Scene 8 | 逆否命题框 |

---

## 动画节奏说明
- 开场快速引入 (4-5秒)
- 概念逐个介绍 (每个7-8秒)
- 关系图详细展示 (10-12秒，重点)
- 等价关系强调 (8-10秒)
- 片尾引导 (4-5秒)
- 总时长: 70-85秒

---

## 设计要点
1. **视觉层次清晰**: 用不同颜色区分四种命题
2. **变换动画流畅**: 展示命题之间的转换关系
3. **符号使用规范**: p, q, ¬, →, ⟺
4. **关系图直观**: 矩形排列，箭头连接
5. **重点突出**: 等价关系用特殊颜色标注