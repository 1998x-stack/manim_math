# 多边形内角和与外角和 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等
- 年级: 八年级

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主图形
COLOR_SECONDARY = "#e74c3c"      # 红色 - 内角
COLOR_EXTERIOR = "#2ecc71"       # 绿色 - 外角
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_DIAGONAL = "#9b59b6"       # 紫色 - 对角线
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 正五边形顶点 | 极坐标转换 | self.pentagon_vertices |
| 正六边形顶点 | 极坐标转换 | self.hexagon_vertices |
| 一般n边形顶点 | 参数化生成 | self.polygon_vertices |
| 对角线终点 | 从顶点0到顶点2,3,...,n-2 | self.diagonals |
| 内角弧度 | (n-2)×180°/n | self.interior_angle |
| 外角弧度 | 360°/n | self.exterior_angle |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字动画)
3. 多个多边形闪现

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` 文字: "正五边形的内角和是多少?" |
| 1.5s | 三角形、四边形、五边形、六边形依次闪现 | `Succession(FadeIn, FadeOut)` |
| 3.0s | 问号放大跳动 | `Indicate(question_mark)` |

### 清理
- FadeOut: hook_text, 所有多边形
- 保留: author_info

---

## Scene 2: 三角形引入 (5-6秒)
**目的**: 从已知知识点（三角形内角和180°）开始

### 元素
1. 等边三角形
2. 三个内角标记
3. 公式: 180°

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` "从三角形开始" |
| 0.5s | 三角形绘制 | `Create(triangle)` |
| 1.5s | 三个角依次标记 | `Succession(Create(angle1), Create(angle2), Create(angle3))` |
| 2.5s | 角度标签出现 | `FadeIn(angle_labels)` "60°, 60°, 60°" |
| 3.5s | 公式书写 | `Write(formula)` "60° + 60° + 60° = 180°" |
| 4.5s | 强调 | `Indicate(formula)` |

### 清理
- Transform: triangle → 缩小到左上角保留
- FadeOut: title, angle_labels, formula
- 保留: 小三角形（作为参考）

---

## Scene 3: 四边形分割 (8-10秒)
**目的**: 展示将四边形分割为两个三角形

### 元素
1. 正方形
2. 对角线
3. 两个三角形的内角标记
4. 计算过程

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` "四边形的内角和" |
| 0.5s | 正方形绘制 | `Create(square)` |
| 1.5s | 对角线绘制 | `Create(diagonal)` |
| 2.5s | 两个三角形分别闪烁 | `Indicate(triangle1), Indicate(triangle2)` |
| 3.5s | 公式出现 | `Write(formula)` "2 × 180° = 360°" |
| 5.0s | 验证: 四个角标记 | `Create(angles)` 每个90° |
| 6.5s | 验证公式 | `Write(verify)` "90° × 4 = 360°" |

### 清理
- FadeOut: title, diagonal, angles, formulas
- 保留: square（缩小到左上角）

---

## Scene 4: 五边形分割 (10-12秒)
**目的**: 展示n=5时，分割为(n-2)=3个三角形

### 元素
1. 正五边形
2. 从一个顶点引出的对角线
3. 三个三角形标记
4. 通用公式推导

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` "五边形的内角和" |
| 0.5s | 五边形绘制 | `Create(pentagon)` |
| 1.5s | 顶点A标记 | `FadeIn(vertex_label)` |
| 2.5s | 对角线1绘制 | `Create(diagonal1)` A到C |
| 3.5s | 对角线2绘制 | `Create(diagonal2)` A到D |
| 4.5s | 三个三角形依次闪烁 | `Succession(Indicate(...))` |
| 6.0s | 公式书写 | `Write(formula)` "3 × 180° = 540°" |
| 7.5s | 关键观察 | `FadeIn(observation)` "对角线数 = 顶点数 - 3" |
| 9.0s | 三角形数公式 | `Write(key_formula)` "三角形数 = n - 2" |

### 清理
- FadeOut: title, observation, diagonals
- Transform: pentagon → 缩小
- 保留: key_formula（移到顶部）

---

## Scene 5: 通用公式推导 (12-15秒)
**目的**: 推导n边形内角和公式

### 元素
1. 一般n边形示意图
2. 分割过程动画
3. 公式推导步骤

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` "n边形内角和公式" |
| 0.5s | n边形绘制（n=7） | `Create(heptagon)` |
| 1.5s | 从一个顶点引所有对角线 | `Succession(Create(diag_i))` |
| 3.5s | 三角形数量标注 | `FadeIn(triangle_count)` "n - 2 个三角形" |
| 5.0s | 公式推导步骤1 | `Write(step1)` "每个三角形 180°" |
| 6.5s | 公式推导步骤2 | `Write(step2)` "(n-2) 个三角形" |
| 8.0s | 最终公式 | `Write(final)` "内角和 = (n-2) × 180°" |
| 9.5s | 框住公式强调 | `Create(box), Indicate(final)` |

### 清理
- FadeOut: title, heptagon, diagonals, steps
- 保留: final formula（移到顶部）

---

## Scene 6: 外角和证明 (15-18秒)
**目的**: 展示任意多边形外角和都是360°

### 元素
1. 多边形（五边形）
2. 外角标记
3. 外角动画拼接演示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` "外角和的秘密" |
| 0.5s | 五边形重新绘制 | `Create(pentagon)` |
| 1.5s | 延长一条边 | `Create(extended_side)` |
| 2.5s | 标记外角 | `Create(exterior_angle_arc)` |
| 3.5s | 说明文字 | `FadeIn(explanation)` "外角 = 180° - 内角" |
| 5.0s | 五个外角依次标记 | `Succession(Create(ext_angle_i))` |
| 8.0s | 外角"拆下"动画 | `ApplyMethod(angle.move_to, center)` |
| 10.0s | 拼成一个完整圆 | `Rotate(angles, about_point=center)` |
| 12.0s | 圆周标注 | `Write(conclusion)` "外角和 = 360°" |
| 14.0s | 强调 | `Flash(conclusion), Indicate(circle)` |

### 清理
- FadeOut: pentagon, angles, explanation
- 保留: conclusion（移到底部）

---

## Scene 7: 总结与应用 (8-10秒)
**目的**: 总结公式，展示应用

### 元素
1. 公式卡片
2. 示例计算
3. 作者信息

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` "公式总结" |
| 0.5s | 公式卡片1滑入 | `card1.animate.shift(LEFT*10 to 0)` |
| 1.5s | 公式卡片2滑入 | `card2.animate.shift(LEFT*10 to 0)` |
| 2.5s | 示例题目 | `Write(example)` "正八边形每个内角?" |
| 4.0s | 计算步骤1 | `Write(calc1)` "(8-2) × 180° ÷ 8" |
| 5.5s | 计算步骤2 | `Write(calc2)` "= 1080° ÷ 8 = 135°" |
| 7.0s | 关注提示 | `FadeIn(follow_text)` "关注我，获得更多数学技巧!" |
| 8.0s | 作者信息放大 | `author.animate.scale(1.5)` |

### 清理
- 全部元素准备淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保留顶部 |
| triangle | Scene 2 | Scene 2 | 缩小保留 |
| square | Scene 3 | Scene 3 | 缩小保留 |
| pentagon | Scene 4 | Scene 6 | 主要演示图形 |
| interior_formula | Scene 5 | Scene 7 | 移到顶部保留 |
| exterior_formula | Scene 6 | Scene 7 | 移到底部保留 |

---

## 几何计算验证清单
- [ ] 所有多边形顶点使用极坐标精确计算
- [ ] 对角线端点使用顶点索引精确引用
- [ ] 内角弧度使用Arc精确绘制
- [ ] 外角延长线方向精确计算
- [ ] 所有元素位置在安全边界内 (x∈[-4,4], y∈[-7,7])

---

## 动画节奏设计
- 快节奏: 多边形绘制 (0.8-1.0s)
- 中节奏: 对角线绘制 (0.6-0.8s)
- 慢节奏: 公式推导 (1.5-2.0s，需要理解时间）
- 停顿: 关键公式后停留 1.5-2.0s

---

## 字幕文字规划
| 场景 | 主要文字内容 |
|------|-------------|
| Scene 1 | "正五边形的内角和是多少?" |
| Scene 2 | "从三角形开始", "内角和 = 180°" |
| Scene 3 | "四边形 = 2个三角形", "内角和 = 360°" |
| Scene 4 | "五边形 = 3个三角形", "规律: n-2个三角形" |
| Scene 5 | "n边形内角和 = (n-2) × 180°" |
| Scene 6 | "外角和恒为 360°", "与边数无关!" |
| Scene 7 | "掌握公式，轻松解题!" |