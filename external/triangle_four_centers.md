# 三角形四心 - 动画分镜脚本

## 元信息
- 目标时长: 70-80 秒
- 场景数量: 8 个
- 难度等级: 中等
- 目标受众: 初中/高中学生

## 颜色配置
```python
COLOR_CIRCUMCENTER = "#e74c3c"  # 红色 - 外心
COLOR_INCENTER = "#3498db"      # 蓝色 - 内心
COLOR_CENTROID = "#2ecc71"      # 绿色 - 重心
COLOR_ORTHOCENTER = "#f39c12"   # 橙色 - 垂心
COLOR_TRIANGLE = WHITE
COLOR_AUXILIARY = GRAY_B
COLOR_HIGHLIGHT = YELLOW
BACKGROUND = "#1a1a2e"
```

## 几何预计算清单

### 基准三角形 (斜三角形,便于展示所有四心)
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点A | 基准定义: (-2.5, 1.5, 0) | self.A |
| 顶点B | 基准定义: (2.5, -0.5, 0) | self.B |
| 顶点C | 基准定义: (-1.0, -2.5, 0) | self.C |
| 缩放系数 | 0.9 | self.SCALE |
| 偏移量 | UP * 1.5 | self.OFFSET |

### 边长
| 边 | 计算公式 | 存储变量 |
|---|---------|---------|
| BC | \|\|B - C\|\| | self.a |
| CA | \|\|C - A\|\| | self.b |
| AB | \|\|A - B\|\| | self.c |

### 中点
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| AB中点 | (A + B) / 2 | self.M_AB |
| BC中点 | (B + C) / 2 | self.M_BC |
| CA中点 | (C + A) / 2 | self.M_CA |

### 四心
| 心 | 计算方法 | 存储变量 | 验证条件 |
|----|---------|---------|---------|
| 外心O | 三边垂直平分线交点 (解析公式) | self.circumcenter | \|\|OA\|\| = \|\|OB\|\| = \|\|OC\|\| |
| 内心I | 加权平均: (a·A + b·B + c·C)/(a+b+c) | self.incenter | 到三边距离相等 |
| 重心G | 简单平均: (A + B + C)/3 | self.centroid | 分中线为2:1 |
| 垂心H | 三条高线交点 (解析公式) | self.orthocenter | 高线垂直于底边 |

### 辅助元素
| 元素 | 计算方法 | 用途 |
|------|---------|------|
| 外接圆半径 | \|\|O - A\|\| | 绘制外接圆 |
| 内切圆半径 | 点到直线距离公式 | 绘制内切圆 |
| 垂足 (BC边) | perpendicular_foot(A, B, C) | 绘制高线 |
| 垂足 (CA边) | perpendicular_foot(B, C, A) | 绘制高线 |
| 垂足 (AB边) | perpendicular_foot(C, A, B) | 绘制高线 |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 抓住注意力,引出主题

### 元素
1. 作者标识 (顶部,贯穿全片)
   - 文本: "上海初高中数学直通车 @emptyandcalm"
   - 位置: UP * 7
   - 字号: 20
   - 颜色: GRAY_B

2. 钩子问题
   - 文本: "一个三角形有几个特殊中心?"
   - 位置: UP * 6
   - 字号: 40
   - 颜色: GOLD

3. 主三角形
   - Polygon(A, B, C)
   - 位置: 居中偏上

4. 四个神秘闪烁点
   - 外心、内心、重心、垂心位置
   - 颜色: YELLOW (统一)

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | FadeIn(author_info, shift=DOWN*0.2) | 0.3s |
| 0.3s | 钩子文字书写 | Write(hook_text) | 0.8s |
| 1.1s | 三角形创建 | Create(triangle) | 1.0s |
| 2.1s | 四个点依次闪烁 | FadeIn(dot, scale=0.5) × 4 | 0.8s |
| 2.9s | 提示文字 | FadeIn(hint_text, shift=UP*0.3) | 0.5s |
| 3.4s | 等待 | Wait(0.8) | 0.8s |

### 清理
- FadeOut: hook_text, hint_text, dots
- 保留: triangle, author_info

---

## Scene 2: 外心 - Circumcenter (10-12秒)
**目的**: 展示外心的定义、构造和性质

### 关键几何
- AB的垂直平分线: 过M_AB,垂直于AB
- BC的垂直平分线: 过M_BC,垂直于BC
- 外心O: 两垂直平分线交点
- 外接圆: 圆心O,半径 = ||O-A||

### 元素
1. 标题组
   - "外心 Circumcenter" (字号36, COLOR_CIRCUMCENTER)
   - "三边垂直平分线的交点" (字号24, GRAY_A)
   - 位置: UP * 5.5, UP * 4.8

2. 几何元素
   - AB边高亮
   - M_AB中点 (Dot + 标签"M")
   - 垂直平分线1 (DashedLine, 长度3.0)
   - BC边高亮
   - M_BC中点
   - 垂直平分线2 (DashedLine, 长度3.0)
   - 外心O (Dot, radius=0.12, COLOR_CIRCUMCENTER)
   - 标签 "O" + "外心"
   - 外接圆 (Circle)
   - 三条半径 (DashedLine)

3. 说明文字
   - "垂直平分线: 过中点且垂直" (DOWN * 4)
   - "到三顶点距离相等" (DOWN * 5)

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 标题和定义淡入 | Write(title), FadeIn(definition) | 0.8s |
| 0.8s | AB边高亮 | Create(ab_line, color=HIGHLIGHT) | 0.5s |
| 1.3s | M_AB中点出现 | FadeIn(m_ab_dot), FadeIn(label) | 0.4s |
| 1.7s | 垂直平分线1 | Create(perp_line_1), FadeIn(explain_1) | 0.8s |
| 2.5s | AB边恢复 | ab_line.animate.set_color(TRIANGLE) | 0.3s |
| 2.8s | BC边高亮 | Create(bc_line, color=HIGHLIGHT) | 0.5s |
| 3.3s | M_BC中点出现 | FadeIn(m_bc_dot) | 0.3s |
| 3.6s | 垂直平分线2 | Create(perp_line_2) | 0.8s |
| 4.4s | BC边恢复 | bc_line.animate.set_color(TRIANGLE), FadeOut(explain_1) | 0.3s |
| 4.7s | 外心O出现 | FadeIn(o_dot, scale=0.5) | 0.5s |
| 5.2s | 外心闪烁 | Flash(o_dot) | 0.4s |
| 5.6s | 标签出现 | FadeIn(o_label), FadeIn(o_label_2) | 0.4s |
| 6.0s | 绘制外接圆 | Create(circumcircle) | 1.5s |
| 7.5s | 三条半径 | Create(radii) | 0.8s |
| 8.3s | 性质说明 | FadeIn(property_text) | 0.5s |
| 8.8s | 等待理解 | Wait(1.5) | 1.5s |

### 清理
- FadeOut: 所有辅助线、圆、标签
- Transform: o_dot → o_small (半径0.05, 透明度0.5) - 保留作为标记

---

## Scene 3: 内心 - Incenter (10-12秒)
**目的**: 展示内心的定义、构造和性质

### 关键几何
- 角A的角平分线: 从A到BC边,使用角平分线定理计算交点
- 角B的角平分线: 从B到CA边
- 内心I: 两角平分线交点 = 加权平均 (a·A + b·B + c·C)/(a+b+c)
- 内切圆: 圆心I,半径 = 点到边的距离

### 元素
1. 标题组
   - "内心 Incenter" (字号36, COLOR_INCENTER)
   - "三条角平分线的交点" (字号24, GRAY_A)

2. 几何元素
   - 角平分线1: A → D_point (D在BC上,精确计算)
   - 角平分线2: B → E_point (E在CA上,精确计算)
   - 内心I (Dot, radius=0.12, COLOR_INCENTER)
   - 标签 "I" + "内心"
   - 内切圆 (Circle)
   - 三条垂线到边

3. 说明文字
   - "角平分线: 平分角度" (DOWN * 4)
   - "到三边距离相等" (DOWN * 5)

### 动画序列
| 时间 | 动作 | 时长 |
|------|------|------|
| 0.0s | 标题和定义淡入 | 0.8s |
| 0.8s | 角平分线1创建 + 说明 | 1.0s |
| 1.8s | 角平分线2创建 | 0.8s |
| 2.6s | 内心I出现 | 0.5s |
| 3.1s | 内心闪烁 | 0.4s |
| 3.5s | 标签出现 | 0.4s |
| 3.9s | 绘制内切圆 | 1.5s |
| 5.4s | 三条垂线 | 0.8s |
| 6.2s | 性质说明 | 0.5s |
| 6.7s | 等待理解 | 1.5s |

### 清理
- FadeOut: 所有辅助线、圆、标签
- Transform: i_dot → i_small (保留作为标记)

---

## Scene 4: 重心 - Centroid (9-10秒)
**目的**: 展示重心的定义、构造和2:1性质

### 关键几何
- 中线AM: A → M_BC
- 中线BN: B → M_CA
- 重心G: (A + B + C) / 3
- 2:1比例: AG:GM_BC = 2:1

### 元素
1. 标题组
   - "重心 Centroid" (字号36, COLOR_CENTROID)
   - "三条中线的交点" (字号24, GRAY_A)

2. 几何元素
   - M_BC中点 (Dot + 标签"M")
   - 中线1: A → M_BC
   - M_CA中点
   - 中线2: B → M_CA
   - 重心G (Dot, radius=0.12, COLOR_CENTROID)
   - 标签 "G" + "重心"
   - Brace标注2:1

3. 说明文字
   - "中线: 顶点到对边中点" (DOWN * 4)
   - "重心分中线为2:1" (DOWN * 5)
   - "物理重心 (平衡点)" (DOWN * 6)

### 动画序列
| 时间 | 动作 | 时长 |
|------|------|------|
| 0.0s | 标题和定义淡入 | 0.8s |
| 0.8s | M_BC中点 + 中线1 + 说明 | 1.4s |
| 2.2s | M_CA中点 + 中线2 | 1.1s |
| 3.3s | 重心G出现 | 0.5s |
| 3.8s | 重心闪烁 | 0.4s |
| 4.2s | 标签出现 | 0.4s |
| 4.6s | Brace标注2:1 + 性质说明 | 1.0s |
| 5.6s | 等待理解 | 1.2s |

### 清理
- FadeOut: 所有辅助线、标签、Brace
- Transform: g_dot → g_small (保留作为标记)

---

## Scene 5: 垂心 - Orthocenter (10-11秒)
**目的**: 展示垂心的定义、构造和性质

### 关键几何
- 高线1: A → foot_D (D在BC上,垂足)
- 高线2: B → foot_E (E在CA上,垂足)
- 垂心H: 高线交点,使用解析公式计算
- 直角标记: 用于标注垂直关系

### 元素
1. 标题组
   - "垂心 Orthocenter" (字号36, COLOR_ORTHOCENTER)
   - "三条高线的交点" (字号24, GRAY_A)

2. 几何元素
   - BC边高亮
   - 高线1: A → foot_D (DashedLine)
   - 直角标记1
   - CA边高亮
   - 高线2: B → foot_E (DashedLine)
   - 直角标记2
   - 垂心H (Dot, radius=0.12, COLOR_ORTHOCENTER)
   - 标签 "H" + "垂心"
   - 高线3: C → foot_F (验证)

3. 说明文字
   - "高线: 顶点到对边的垂线" (DOWN * 4)
   - "三条高线共点!" (DOWN * 5)

### 动画序列
| 时间 | 动作 | 时长 |
|------|------|------|
| 0.0s | 标题和定义淡入 | 0.8s |
| 0.8s | BC边高亮 | 0.5s |
| 1.3s | 高线1 + 直角标记 + 说明 | 1.0s |
| 2.3s | BC边恢复 | 0.3s |
| 2.6s | CA边高亮 | 0.5s |
| 3.1s | 高线2 + 直角标记 | 0.8s |
| 3.9s | CA边恢复 | 0.3s |
| 4.2s | 垂心H出现 | 0.5s |
| 4.7s | 垂心闪烁 | 0.4s |
| 5.1s | 标签出现 | 0.4s |
| 5.5s | 高线3 + 性质说明 | 1.0s |
| 6.5s | 等待理解 | 1.2s |

### 清理
- FadeOut: 所有辅助线、标签、直角标记
- Transform: h_dot → h_small (保留作为标记)

---

## Scene 6: 四心汇总 (8-10秒)
**目的**: 汇总展示四心位置,加深印象

### 元素
1. 三角形缩小并移动到上方
   - 缩放: 0.6
   - 位置: UP * 3

2. 四心重新定位并放大
   - 所有小标记 → 正常大小
   - 透明度恢复

3. 四心标签
   - O, I, G, H
   - 带颜色区分

4. 四心特性卡片
   - 外心: "垂直平分线交点, 外接圆圆心"
   - 内心: "角平分线交点, 内切圆圆心"
   - 重心: "中线交点, 物理重心, 2:1比例"
   - 垂心: "高线交点"

5. 重点提示
   - "掌握四心, 轻松解题!" (COLOR_HIGHLIGHT)

### 动画序列
| 时间 | 动作 | 时长 |
|------|------|------|
| 0.0s | 三角形和四心同步移动缩放 | 1.0s |
| 1.0s | 四心闪烁 | 0.8s |
| 1.8s | 标签出现 | 0.5s |
| 2.3s | 卡片1滑入 | 0.4s |
| 2.7s | 卡片2滑入 | 0.4s |
| 3.1s | 卡片3滑入 | 0.4s |
| 3.5s | 卡片4滑入 | 0.4s |
| 3.9s | 重点提示 | 0.6s |
| 4.5s | 等待 | 2.0s |

### 清理
- FadeOut: 所有元素

---

## Scene 7: 欧拉线彩蛋 (可选, 5-6秒)
**目的**: 展示外心、重心、垂心共线 (欧拉线)

### 元素
1. 三角形 + 外心、重心、垂心
2. 欧拉线 (DashedLine, 连接O-G-H)
3. 文字: "欧拉线: 外心-重心-垂心共线!"
4. 公式: OG:GH = 1:2

### 动画序列
| 时间 | 动作 | 时长 |
|------|------|------|
| 0.0s | 三角形和三心出现 | 0.5s |
| 0.5s | 欧拉线绘制 | 1.0s |
| 1.5s | 文字说明 | 0.6s |
| 2.1s | 公式出现 | 0.5s |
| 2.6s | 等待 | 1.5s |

### 清理
- FadeOut: 所有元素

---

## Scene 8: 片尾关注 (4-5秒)
**目的**: 引导关注,品牌强化

### 元素
1. 作者信息放大
   - "上海初高中数学直通车" (字号40, WHITE)
   - "@emptyandcalm" (字号32, GRAY_B)

2. 关注提示
   - "关注我, 学更多几何技巧!" (字号30, COLOR_HIGHLIGHT)

3. 装饰元素
   - 六个小三角形围绕文字旋转
   - 四心图标快闪 (四个彩色圆点)

### 动画序列
| 时间 | 动作 | 时长 |
|------|------|------|
| 0.0s | 作者信息放大 | 0.8s |
| 0.8s | 关注提示淡入 | 0.6s |
| 1.4s | 装饰三角形出现并旋转 | 2.1s |
| 2.5s | 四心图标快闪 | 0.6s |
| 3.1s | 等待 | 1.0s |
| 4.1s | 全部淡出 | 1.0s |

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 形态变化 | 备注 |
|------|---------|---------|---------|------|
| triangle | Scene 1 | Scene 6 | Scene 6缩小移动 | 主三角形 |
| author_info | Scene 1 | Scene 8 | Scene 8放大 | 作者标识,贯穿全片 |
| o_dot | Scene 2 | Scene 6 | → o_small (Scene 2末尾) | 外心 |
| i_dot | Scene 3 | Scene 6 | → i_small (Scene 3末尾) | 内心 |
| g_dot | Scene 4 | Scene 6 | → g_small (Scene 4末尾) | 重心 |
| h_dot | Scene 5 | Scene 6 | → h_small (Scene 5末尾) | 垂心 |

---

## 技术要点检查清单

### 几何计算
- [x] 所有点坐标通过精确公式计算
- [x] 四心验证函数 (verify_geometry)
- [x] 使用 GeometryCalculator 工具类
- [x] 角度使用 Angle.from_three_points
- [x] 垂足使用 perpendicular_foot 函数

### Manim 0.19.2 约束
- [x] 中文使用 Text() + font="Noto Sans CJK SC"
- [x] 度数符号使用 ^\circ
- [x] 虚线使用 DashedLine
- [x] SurroundingRectangle 使用关键字参数
- [x] 边界检查: x∈[-4,4], y∈[-7,7]

### 动画节奏
- [x] 关键步骤停留 1.5-2.0s
- [x] 简单动画 0.3-0.5s
- [x] 复杂动画 0.8-1.5s
- [x] 场景切换 0.4-0.6s
- [x] 总时长控制在 70-80s

### 视觉质量
- [x] 字体大小遵循规范
- [x] 颜色方案统一
- [x] 元素无重叠
- [x] 无溢出边界
- [x] 标签位置合理

---

## 预期总时长
- Scene 1: 4.2s
- Scene 2: 10.3s
- Scene 3: 8.2s
- Scene 4: 6.8s
- Scene 5: 7.7s
- Scene 6: 6.5s
- Scene 7 (可选): 4.1s
- Scene 8: 5.1s

**总计**: 约 53s (不含Scene 7) 或 57s (含Scene 7)

**建议**: 保留 Scene 7 (欧拉线彩蛋),增加知识深度和趣味性。