# 圆的面积 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 小学六年级
- 核心知识点: 圆的面积公式 S=πr²，推导方法（转化思想）

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"       # 主蓝色 - 圆
COLOR_SECONDARY = "#e74c3c"     # 红色 - 扇形
COLOR_HIGHLIGHT = YELLOW        # 高亮黄色
COLOR_AUXILIARY = GRAY_B        # 辅助灰色
COLOR_FORMULA = "#2ecc71"       # 绿色 - 公式
COLOR_TRANSFORM = "#9b59b6"     # 紫色 - 变换后的图形
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆心 | ORIGIN | self.center |
| 半径 | 1.8 单位 | self.radius |
| 圆 | Circle(radius=r) | self.circle |
| 扇形数量 | 16 等份 | self.num_sectors |
| 扇形顶点 | 圆周上等分点 | self.sector_points |
| 拼接后宽度 | πr | self.rect_width |
| 拼接后高度 | r | self.rect_height |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 "如何求圆的面积？"
3. 一个完整的圆（带问号）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入顶部 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子问题大字书写 | `Write(hook_question)` |
| 1.0s | 圆形从中心生长 | `GrowFromCenter(circle)` |
| 1.8s | 问号闪烁出现 | `FadeIn(question_mark, scale=1.5)` |
| 2.5s | 等待思考 | `Wait(0.8)` |
| 3.3s | 问号淡出 | `FadeOut(question_mark)` |
| 3.8s | 钩子问题淡出 | `FadeOut(hook_question)` |

### 清理
- FadeOut: hook_question, question_mark
- 保留: circle, author_info

---

## Scene 2: 展示已知信息 (5-12秒)
**目的**: 标注圆的半径，建立基础认知

### 元素
1. 圆（从场景1保留）
2. 半径线段
3. 半径标签 "r"
4. 说明文字 "已知半径为 r"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 5.0s | 圆轻微缩放强调 | `circle.animate.scale(1.1).scale(1/1.1)` |
| 5.5s | 半径线段绘制（从圆心到边） | `Create(radius_line)` |
| 6.3s | 半径标签写入 | `Write(radius_label)` |
| 7.0s | 说明文字淡入底部 | `FadeIn(explanation)` |
| 8.0s | 等待 | `Wait(1.0)` |
| 9.0s | 说明文字淡出 | `FadeOut(explanation)` |

### 清理
- FadeOut: explanation
- 保留: circle, radius_line, radius_label, author_info

---

## Scene 3: 转化思想引入 (12-20秒)
**目的**: 引出"化圆为方"的核心思想

### 元素
1. 标题 "转化思想: 化圆为方"
2. 圆分割示意（4等份预览）
3. 箭头指向长方形轮廓

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 12.0s | 标题从上方滑入 | `FadeIn(title, shift=DOWN*0.3)` |
| 13.0s | 圆分割成4份（虚线） | `Create(sector_lines_4)` |
| 14.5s | 扇形轻微分离 | `sectors.animate.arrange_in_grid(2,2)` |
| 16.0s | 箭头出现 | `GrowArrow(arrow)` |
| 16.8s | 长方形轮廓淡入 | `FadeIn(rect_outline)` |
| 18.0s | 说明文字 "面积不变！" | `Write(area_constant_text)` |
| 19.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, sector_lines_4, arrow, rect_outline, area_constant_text
- 保留: circle (重置为完整圆), author_info

---

## Scene 4: 精细分割演示 (20-35秒)
**目的**: 展示分割越细，越接近长方形

### 元素
1. 说明文字 "分得越细，越接近长方形"
2. 圆分割成16等份
3. 扇形依次高亮
4. 扇形重新排列成近似长方形

### 几何计算
```python
# 16个扇形的顶点坐标
angles = [i * 2*PI / 16 for i in range(17)]  # 0到2π，17个点
points = [(center + radius*np.array([cos(θ), sin(θ), 0])) for θ in angles]

# 每个扇形: Polygon(center, points[i], points[i+1])
sectors = [
    Polygon(center, points[i], points[i+1], ...)
    for i in range(16)
]

# 拼接排列:
# 奇数扇形: 顶点向上
# 偶数扇形: 顶点向下（旋转180度）
# 横向排列成行
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 20.0s | 说明文字淡入 | `FadeIn(explanation)` |
| 21.0s | 圆分割成16份（放射状线） | `Create(sector_lines)` |
| 22.5s | 扇形依次闪烁高亮 | `Flash(sector[i])` 循环 |
| 25.0s | 说明文字淡出 | `FadeOut(explanation)` |
| 25.5s | 扇形分离并重排列 | `sectors.animate.arrange(...)` |
| 28.0s | 形成近似长方形 | 最终位置调整 |
| 29.0s | 外轮廓高亮 | `Create(rect_frame)` |
| 30.5s | 等待观察 | `Wait(2.0)` |

### 清理
- FadeOut: sector_lines（分割线）
- 保留: sectors（排列后的扇形）, rect_frame, author_info

---

## Scene 5: 标注长方形尺寸 (35-47秒)
**目的**: 建立圆周长与长方形长、半径与宽的关系

### 元素
1. 长方形的长（上边）标注
2. 长的标签 "周长的一半 = πr"
3. 长方形的宽（侧边）标注
4. 宽的标签 "r"
5. 说明文字

### 几何计算
```python
# 长方形实际尺寸
rect_width = PI * radius  # 圆周长2πr的一半
rect_height = radius

# 标注位置
length_brace_pos = rect.get_top() + UP*0.3
width_brace_pos = rect.get_right() + RIGHT*0.3
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 35.0s | 上边Brace出现 | `Create(length_brace)` |
| 35.8s | 长标签写入 | `Write(length_label)` |
| 37.0s | 侧边Brace出现 | `Create(width_brace)` |
| 37.8s | 宽标签写入 | `Write(width_label)` |
| 39.0s | 说明文字 "拼成的长方形" | `FadeIn(explanation)` |
| 41.0s | 等待理解 | `Wait(2.5)` |

### 清理
- 保留: sectors, rect_frame, length_brace, length_label, width_brace, width_label
- FadeOut: explanation

---

## Scene 6: 推导面积公式 (47-60秒)
**目的**: 由长方形面积公式推导出圆的面积公式

### 元素
1. 长方形面积公式
2. 替换步骤
3. 最终圆面积公式
4. 公式高亮

### 公式演变
```python
# Step 1: 长方形面积
formula_1 = MathTex(r"S", r"=", r"\text{长}", r"\times", r"\text{宽}")

# Step 2: 替换长和宽
formula_2 = MathTex(r"S", r"=", r"\pi r", r"\times", r"r")

# Step 3: 简化
formula_3 = MathTex(r"S", r"=", r"\pi r^2")
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 47.0s | 图形整体缩小上移 | `group.animate.scale(0.6).to_edge(UP)` |
| 48.0s | 公式1书写（底部） | `Write(formula_1)` |
| 49.5s | 等待 | `Wait(0.8)` |
| 50.3s | 变换到公式2 | `TransformMatchingTex(formula_1, formula_2)` |
| 52.0s | 等待 | `Wait(1.0)` |
| 53.0s | 变换到公式3 | `TransformMatchingTex(formula_2, formula_3)` |
| 54.5s | 公式放大并高亮 | `formula_3.animate.scale(1.3).set_color(YELLOW)` |
| 56.0s | 外框闪烁 | `Flash(formula_3)` |
| 57.0s | 等待庆祝 | `Wait(2.0)` |

### 清理
- FadeOut: sectors, rect_frame, braces, labels（除公式外全部）
- 保留: formula_3, author_info

---

## Scene 7: 片尾总结 (60-75秒)
**目的**: 强化记忆，引导关注

### 元素
1. 核心公式 S=πr²（居中放大）
2. 知识点卡片
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 60.0s | 公式移动到上方 | `formula_3.animate.move_to(UP*3)` |
| 61.0s | 知识点卡片1淡入 | "记住半径 r" |
| 62.5s | 知识点卡片2淡入 | "π ≈ 3.14" |
| 64.0s | 知识点卡片3淡入 | "面积单位: 平方" |
| 66.0s | 示例圆+计算 | 小圆r=2, S=4π≈12.56 |
| 69.0s | 作者信息放大 | `Transform(author_info, author_big)` |
| 70.0s | 关注提示 | "关注我，获得更多数学技巧！" |
| 72.0s | 装饰元素（圆圈旋转） | `Rotate(circles)` |
| 74.0s | 全部淡出 | `FadeOut(everything)` |

### 清理
- FadeOut: 所有元素

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 作者标识，贯穿全程 |
| circle | Scene 1 | Scene 4 | 完整圆，在分割前 |
| hook_question | Scene 1 | Scene 1 | 钩子问题 |
| radius_line | Scene 2 | Scene 4 | 半径线段 |
| radius_label | Scene 2 | Scene 4 | 半径标签r |
| sectors | Scene 4 | Scene 6 | 16个扇形 |
| rect_frame | Scene 4 | Scene 6 | 长方形外框 |
| length_brace | Scene 5 | Scene 6 | 长的标注 |
| width_brace | Scene 5 | Scene 6 | 宽的标注 |
| formula_3 | Scene 6 | Scene 7 | 最终公式 |

---

## 特殊注意事项

### 1. 扇形精确拼接
- 奇数扇形（1,3,5...）：顶点向上
- 偶数扇形（2,4,6...）：旋转180度，顶点向下
- 横向紧密排列，形成波浪边的长方形

### 2. 坐标安全边界
- 主内容区域: y ∈ [-2, +4]
- 公式区域: y ∈ [-5, -2]
- 顶部作者: y = +7
- 避免元素超出 y=±8

### 3. 字体大小遵循规范
- 标题: 36
- 公式: 28-32
- 说明文字: 22
- 标签: 20

### 4. 动画节奏
- 关键推导步骤: 停留2-3秒
- 简单动画: 0.5-1秒
- 总时长控制在75秒内

### 5. 颜色语义
- 蓝色: 原始圆形
- 红/紫色: 变换后的图形
- 黄色: 强调和高亮
- 绿色: 最终公式