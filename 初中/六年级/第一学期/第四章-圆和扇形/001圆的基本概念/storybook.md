# 圆的基本概念 - 动画分镜脚本
<!-- /root/code/sss/media/videos/circle_basic_concepts/1920p60/CircleBasicConcepts.mp4 -->
## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 初级 (六年级)
- 格式: TikTok 竖屏 (1080×1920)

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主圆
COLOR_SECONDARY = "#e74c3c"      # 红色 - 圆心
COLOR_RADIUS = "#2ecc71"         # 绿色 - 半径
COLOR_DIAMETER = "#f39c12"       # 橙色 - 直径
COLOR_CHORD = "#9b59b6"          # 紫色 - 弦
COLOR_ARC = "#1abc9c"            # 青色 - 弧
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆心O | 固定点 | self.O |
| 半径r | 固定长度 | self.radius |
| 直径端点 | O ± r*方向 | self.D1, self.D2 |
| 弦端点 | 圆上两点 | self.C1, self.C2 |
| 弧端点 | 圆上两点 | self.A1, self.A2 |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出主题

### 元素
1. 作者标识 (顶部)
2. 钩子问题文字
3. 圆形图案闪现

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子问题书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 多个圆形闪现 | `Create(circles)` | 1.0s |
| 2.1s | 等待 | `Wait(1.0)` | 1.0s |

### 清理
- FadeOut: hook_text, circles (小圆)
- 保留: author_info

---

## Scene 2: 圆的定义 (8-10秒)
**目的**: 展示圆的数学定义

### 元素
1. 标题："什么是圆？"
2. 定义文字
3. 动态演示：固定点+动点

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 0.5s | 圆心点出现 | `FadeIn(center_dot, scale=0.5)` | 0.4s |
| 0.9s | 半径线段旋转绘制圆 | `Rotate(radius_line)` + `Create(circle)` | 2.0s |
| 2.9s | 定义文字出现 | `Write(definition)` | 1.5s |
| 4.4s | 公式显示 | `Write(formula)` | 1.0s |
| 5.4s | 等待理解 | `Wait(2.0)` | 2.0s |

### 清理
- FadeOut: title, definition
- 保留: circle, center_dot, formula (移到上方)

---

## Scene 3: 圆心 O (5-6秒)
**目的**: 介绍圆心概念

### 元素
1. 标题："圆心 O"
2. 圆心标注
3. 强调动画

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题出现 | `FadeIn(title)` | 0.4s |
| 0.4s | 圆心闪烁放大 | `Flash(center_dot)` + `Scale` | 0.6s |
| 1.0s | 标签"O"出现 | `FadeIn(label_O)` | 0.4s |
| 1.4s | 说明文字 | `Write(explanation)` | 1.0s |
| 2.4s | 等待 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: title, explanation
- 保留: circle, center_dot, label_O

---

## Scene 4: 半径 r (7-8秒)
**目的**: 介绍半径概念

### 元素
1. 标题："半径 r"
2. 多条半径线段
3. 公式：r = |PO|

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题出现 | `FadeIn(title)` | 0.4s |
| 0.4s | 第一条半径绘制 | `Create(radius_1)` | 0.6s |
| 1.0s | 标注点和标签 | `FadeIn(point_P, label_P)` | 0.4s |
| 1.4s | 多条半径依次出现 | `Create(radius_2,3,4)` | 1.2s |
| 2.6s | 说明：到圆心距离相等 | `Write(explanation)` | 1.0s |
| 3.6s | 公式 | `Write(formula)` | 0.8s |
| 4.4s | 等待 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: title, explanation, extra radii
- 保留: circle, center_dot, one radius line

---

## Scene 5: 直径 d (7-8秒)
**目的**: 介绍直径概念及与半径关系

### 元素
1. 标题："直径 d"
2. 直径线段
3. 公式：d = 2r

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题出现 | `FadeIn(title)` | 0.4s |
| 0.4s | 清除半径线 | `FadeOut(radius_line)` | 0.3s |
| 0.7s | 直径线段绘制 | `Create(diameter)` | 0.8s |
| 1.5s | 端点标注 | `FadeIn(points, labels)` | 0.4s |
| 1.9s | 说明文字 | `Write(explanation)` | 1.0s |
| 2.9s | 公式 d=2r 出现 | `Write(formula)` | 0.8s |
| 3.7s | 公式变换演示 | `Transform` | 0.6s |
| 4.3s | 等待 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: title, explanation, diameter, labels
- 保留: circle, center_dot

---

## Scene 6: 弦和弧 (8-10秒)
**目的**: 介绍弦和弧的概念

### 元素
1. 标题："弦和弧"
2. 弦线段
3. 弧（圆的一部分）
4. 对比直径是最长的弦

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题出现 | `FadeIn(title)` | 0.4s |
| 0.4s | 弦线段绘制 | `Create(chord)` | 0.6s |
| 1.0s | 端点标注 | `FadeIn(points, labels)` | 0.4s |
| 1.4s | 弦说明 | `Write(chord_explanation)` | 1.0s |
| 2.4s | 弧高亮显示 | `Create(arc, color=HIGHLIGHT)` | 0.8s |
| 3.2s | 弧说明 | `Write(arc_explanation)` | 1.0s |
| 4.2s | 直径对比 | `Create(diameter)` + 文字 | 1.5s |
| 5.7s | 等待 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: title, explanations, chord, arc, diameter
- 保留: circle, center_dot

---

## Scene 7: 对称性 (8-10秒)
**目的**: 展示圆的轴对称性质

### 元素
1. 标题："圆的对称性"
2. 多条对称轴（直径）
3. 动画演示对称

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题出现 | `FadeIn(title)` | 0.4s |
| 0.4s | 第一条对称轴 | `Create(axis_1)` | 0.6s |
| 1.0s | 圆沿轴翻转动画 | `Rotate(circle_copy)` | 1.2s |
| 2.2s | 多条对称轴旋转出现 | `Create(axes)` + `Rotate` | 1.5s |
| 3.7s | 说明文字 | `Write(explanation)` | 1.2s |
| 4.9s | 等待 | `Wait(2.0)` | 2.0s |

### 清理
- FadeOut: title, explanation, axes
- 保留: circle, center_dot

---

## Scene 8: 总结回顾 (8-10秒)
**目的**: 快速回顾所有概念

### 元素
1. 标题："圆的基本要素"
2. 所有元素同时显示
3. 卡片式总结

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题出现 | `FadeIn(title)` | 0.5s |
| 0.5s | 圆缩小移到上方 | `circle.animate.scale(0.7).shift(UP*2)` | 0.8s |
| 1.3s | 5个要素卡片依次滑入 | `card.animate.shift(RIGHT)` | 2.0s |
| 3.3s | 重点提示 | `FadeIn(highlight_text)` | 0.6s |
| 3.9s | 等待 | `Wait(2.5)` | 2.5s |

### 清理
- FadeOut: 所有元素
- 准备结尾

---

## Scene 9: 片尾关注 (4-5秒)
**目的**: 引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者名放大 | `Transform(author_info)` | 0.8s |
| 0.8s | ID出现 | `FadeIn(author_id)` | 0.4s |
| 1.2s | 关注文字 | `FadeIn(follow_text, scale=1.1)` | 0.6s |
| 1.8s | 圆形装饰旋转 | `Rotate(circles)` | 1.5s |
| 3.3s | 全部淡出 | `FadeOut(all)` | 1.0s |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 9 | 贯穿全片 |
| main_circle | Scene 2 | Scene 8 | 主圆形 |
| center_dot | Scene 2 | Scene 8 | 圆心点 |
| label_O | Scene 3 | Scene 8 | 圆心标签 |
| radius_line | Scene 4 | Scene 5 | 半径线段 |
| diameter | Scene 5 | Scene 5 | 直径线段 |
| chord | Scene 6 | Scene 6 | 弦线段 |
| arc | Scene 6 | Scene 6 | 弧 |
| symmetry_axes | Scene 7 | Scene 7 | 对称轴 |
| summary_cards | Scene 8 | Scene 8 | 总结卡片 |

---

## 技术要点
1. **中文字体**: 使用 "Noto Sans CJK SC" 或 "SimHei"
2. **公式**: 使用 MathTex，不含中文
3. **虚线**: 使用 DashedLine
4. **坐标验证**: 所有点在 setup_geometry() 中计算
5. **边界控制**: x ∈ [-4, 4], y ∈ [-7, 7]
6. **颜色一致性**: 每个元素类型使用固定颜色
7. **节奏控制**: 难点停留 2-3秒，简单部分 0.5-1秒

---

## 预期效果
- 清晰易懂的圆的概念讲解
- 视觉化展示各个基本元素
- 符合六年级学生认知水平
- TikTok 竖屏格式，吸引眼球
- 专业的数学教学动画质量