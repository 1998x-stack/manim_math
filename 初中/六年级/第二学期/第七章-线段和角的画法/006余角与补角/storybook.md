# 余角与补角 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 六年级（入门）
- 视频格式: TikTok 竖屏 (1080×1920)

## 颜色配置
```python
COLOR_COMPLEMENTARY = "#3498db"  # 蓝色 - 余角
COLOR_SUPPLEMENTARY = "#e74c3c"  # 红色 - 补角
COLOR_RIGHT_ANGLE = "#2ecc71"    # 绿色 - 直角
COLOR_STRAIGHT_ANGLE = "#f39c12" # 橙色 - 平角
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
COLOR_TRIANGLE = WHITE
```

## 几何预计算清单

### 余角场景
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点O | 原点 | self.O = ORIGIN |
| 射线OA | 水平向右 | self.A_end = RIGHT * 3 |
| 射线OB | 与OA成α角 | self.B_end = 计算旋转向量 |
| 射线OC | 与OB成β角(α+β=90°) | self.C_end = UP * 3 |
| 角α弧心 | O点 | self.O |
| 角β弧心 | O点 | self.O |
| 角α弧半径 | 0.8 | self.arc_radius_small |
| 角β弧半径 | 1.2 | self.arc_radius_large |

### 补角场景
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点O | 原点 | self.O = ORIGIN |
| 射线OA | 水平向左 | self.A_end_supp = LEFT * 3 |
| 射线OB | 水平向右 | self.B_end_supp = RIGHT * 3 |
| 射线OC | 与OA成α角 | self.C_end_supp = 计算旋转向量 |
| 角α弧心 | O点 | self.O |
| 角β弧心 | O点 | self.O |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字 + 动画)
3. 两个神秘角度

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2, run_time=0.3)` | 顶部 y=7 |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` | "两个角相加会怎样?" y=6 |
| 1.1s | 两个角闪现 | `Create(angle1), Create(angle2)` | 一个30°，一个60° |
| 2.1s | 角度闪烁 | `Flash(angle1), Flash(angle2)` | 引起注意 |
| 2.8s | 提示文字 | `FadeIn(hint, run_time=0.5)` | "竟然有特殊名称?" |
| 3.8s | 等待 | `Wait(0.7)` | 让观众思考 |

### 几何计算
```python
# 角1: 30度
angle1_start = RIGHT * 2
angle1_end = rotate_vector(RIGHT * 2, 30 * DEGREES)

# 角2: 60度  
angle2_start = angle1_end
angle2_end = UP * 2
```

### 清理
- FadeOut: hook_text, hint, angle1, angle2
- 保留: author_info

---

## Scene 2: 余角定义 (5-15秒)
**目的**: 介绍余角的定义和记号

### 元素
1. 标题: "余角 Complementary Angles"
2. 定义文字
3. 两个互余的角 (α + β = 90°)
4. 直角符号

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 5.0s | 标题写入 | `Write(title, run_time=0.8)` | y=5.5 |
| 5.8s | 定义淡入 | `FadeIn(definition, run_time=0.6)` | y=4.8 |
| 6.4s | 绘制射线OA | `Create(ray_OA, run_time=0.5)` | 水平向右 |
| 6.9s | 绘制射线OB | `Create(ray_OB, run_time=0.5)` | 旋转30° |
| 7.4s | 绘制角α弧 | `Create(arc_alpha, run_time=0.5)` | 蓝色弧 |
| 7.9s | 标注α | `FadeIn(label_alpha, run_time=0.3)` | "α" |
| 8.2s | 绘制射线OC | `Create(ray_OC, run_time=0.5)` | 垂直向上 |
| 8.7s | 绘制角β弧 | `Create(arc_beta, run_time=0.5)` | 蓝色弧 |
| 9.2s | 标注β | `FadeIn(label_beta, run_time=0.3)` | "β" |
| 9.5s | 直角符号 | `FadeIn(right_angle_mark, run_time=0.4)` | 绿色小方块 |
| 9.9s | 公式出现 | `Write(formula1, run_time=1.0)` | "α + β = 90°" |
| 11.4s | 等待理解 | `Wait(1.5)` | 关键概念停留 |

### 几何精确计算
```python
def setup_complementary_geometry(self):
    """余角场景的几何设置"""
    self.O = ORIGIN + UP * 1.5  # 顶点偏移
    
    # 角度设置
    self.alpha_angle = 30 * DEGREES  # 30度
    self.beta_angle = 60 * DEGREES   # 60度，确保和为90度
    
    # 射线端点（精确计算）
    self.A_end = self.O + RIGHT * 2.5
    self.B_end = self.O + np.array([
        2.5 * np.cos(self.alpha_angle),
        2.5 * np.sin(self.alpha_angle),
        0
    ])
    self.C_end = self.O + UP * 2.5  # 垂直，确保90度
    
    # 弧的半径
    self.arc_radius_alpha = 0.8
    self.arc_radius_beta = 1.2
    
    # 验证角度和
    calculated_sum = self.alpha_angle + self.beta_angle
    assert abs(calculated_sum - PI/2) < 1e-6, "余角和必须为90度!"
```

### 清理
- FadeOut: title, definition, 保留图形进入下一场景

---

## Scene 3: 余角实例 (15-25秒)
**目的**: 用具体例子加深理解

### 元素
1. 说明文字: "举个例子"
2. 具体数值: 30° 和 60°
3. 计算过程演示

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 15.0s | 清空之前的标注 | `FadeOut(old_labels)` | 准备新内容 |
| 15.5s | 标注具体度数 | `FadeIn(angle_30, angle_60)` | "30°", "60°" |
| 16.2s | 计算式出现 | `Write(calc, run_time=0.8)` | "30° + 60° = 90°" |
| 17.0s | 高亮显示 | `arc_alpha.animate.set_color(YELLOW)` | 强调角α |
| 17.5s | 高亮显示 | `arc_beta.animate.set_color(YELLOW)` | 强调角β |
| 18.0s | 结论文字 | `FadeIn(conclusion, run_time=0.6)` | "∴ 30°与60°互为余角" |
| 19.0s | 等待 | `Wait(1.5)` | 消化信息 |

### 另一组例子（可选，时间允许）
- 45° + 45° = 90°
- 20° + 70° = 90°

### 清理
- FadeOut: 所有余角相关图形
- 准备补角场景

---

## Scene 4: 补角定义 (25-35秒)
**目的**: 介绍补角的定义和记号

### 元素
1. 标题: "补角 Supplementary Angles"
2. 定义文字
3. 两个互补的角 (α + β = 180°)
4. 平角线

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 25.0s | 标题写入 | `Write(title2, run_time=0.8)` | y=5.5 红色主题 |
| 25.8s | 定义淡入 | `FadeIn(definition2, run_time=0.6)` | y=4.8 |
| 26.4s | 绘制基准线 | `Create(base_line, run_time=0.6)` | 水平线OA-OB |
| 27.0s | 绘制射线OC | `Create(ray_OC_supp, run_time=0.5)` | 从O点向上 |
| 27.5s | 绘制角α弧 | `Create(arc_alpha_supp, run_time=0.5)` | 红色弧 |
| 28.0s | 标注α | `FadeIn(label_alpha_supp, run_time=0.3)` | "α" |
| 28.3s | 绘制角β弧 | `Create(arc_beta_supp, run_time=0.5)` | 红色弧 |
| 28.8s | 标注β | `FadeIn(label_beta_supp, run_time=0.3)` | "β" |
| 29.1s | 平角标注 | `FadeIn(straight_angle_mark)` | 橙色标记 |
| 29.5s | 公式出现 | `Write(formula2, run_time=1.0)` | "α + β = 180°" |
| 31.0s | 等待理解 | `Wait(1.5)` | 关键概念停留 |

### 几何精确计算
```python
def setup_supplementary_geometry(self):
    """补角场景的几何设置"""
    self.O_supp = ORIGIN + UP * 1.5  # 顶点
    
    # 角度设置
    self.alpha_angle_supp = 120 * DEGREES  # 120度
    self.beta_angle_supp = 60 * DEGREES    # 60度，确保和为180度
    
    # 射线端点（精确计算）
    self.A_end_supp = self.O_supp + LEFT * 3   # 平角左端
    self.B_end_supp = self.O_supp + RIGHT * 3  # 平角右端
    self.C_end_supp = self.O_supp + np.array([
        2.5 * np.cos(self.alpha_angle_supp),
        2.5 * np.sin(self.alpha_angle_supp),
        0
    ])
    
    # 弧的半径
    self.arc_radius_alpha_supp = 0.9
    self.arc_radius_beta_supp = 1.3
    
    # 验证角度和
    calculated_sum = self.alpha_angle_supp + self.beta_angle_supp
    assert abs(calculated_sum - PI) < 1e-6, "补角和必须为180度!"
```

### 清理
- FadeOut: title2, definition2, 保留图形

---

## Scene 5: 补角实例 (35-45秒)
**目的**: 用具体例子加深理解

### 元素
1. 说明文字: "举个例子"
2. 具体数值: 120° 和 60°
3. 计算过程演示

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 35.0s | 清空标注 | `FadeOut(old_labels)` | 准备新内容 |
| 35.5s | 标注具体度数 | `FadeIn(angle_120, angle_60)` | "120°", "60°" |
| 36.2s | 计算式出现 | `Write(calc2, run_time=0.8)` | "120° + 60° = 180°" |
| 37.0s | 高亮显示 | `arc_alpha_supp.animate.set_color(YELLOW)` | 强调角α |
| 37.5s | 高亮显示 | `arc_beta_supp.animate.set_color(YELLOW)` | 强调角β |
| 38.0s | 结论文字 | `FadeIn(conclusion2, run_time=0.6)` | "∴ 120°与60°互为补角" |
| 39.0s | 等待 | `Wait(1.5)` | 消化信息 |

### 清理
- FadeOut: 所有补角相关图形

---

## Scene 6: 性质总结 (45-55秒)
**目的**: 强调重要性质

### 元素
1. 标题: "重要性质"
2. 性质1: 同角（或等角）的余角相等
3. 性质2: 同角（或等角）的补角相等
4. 图示说明

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 45.0s | 标题写入 | `Write(property_title, run_time=0.6)` | y=5.5 |
| 45.6s | 性质1出现 | `FadeIn(property1, shift=LEFT*0.3)` | 左侧卡片 |
| 46.4s | 图示1 | `Create(diagram1)` | 余角性质图 |
| 47.4s | 性质2出现 | `FadeIn(property2, shift=LEFT*0.3)` | 右侧卡片 |
| 48.2s | 图示2 | `Create(diagram2)` | 补角性质图 |
| 49.2s | 强调文字 | `FadeIn(emphasis, scale=1.1)` | "必须掌握!" |
| 50.2s | 等待 | `Wait(1.8)` | 重点停留 |

### 性质说明图示
```python
# 性质1图示: 角α的两个余角β1和β2相等
# 如果 α + β1 = 90° 且 α + β2 = 90°
# 则 β1 = β2

# 性质2图示: 角α的两个补角β1和β2相等  
# 如果 α + β1 = 180° 且 α + β2 = 180°
# 则 β1 = β2
```

### 清理
- FadeOut: 所有图形
- 保留: author_info

---

## Scene 7: 结尾关注 (55-65秒)
**目的**: 总结 + 引导关注

### 元素
1. 核心公式回顾
2. 作者信息放大
3. 关注提示
4. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 55.0s | 核心公式滑入 | `FadeIn(formulas, shift=DOWN)` | 两个核心公式 |
| 55.8s | 公式闪烁 | `Indicate(formulas)` | 强调 |
| 56.6s | 作者信息放大 | `author_info.animate.scale(1.5)` | 移到中心 |
| 57.4s | 关注文字 | `FadeIn(follow_text, scale=1.1)` | "关注我..." |
| 58.4s | 装饰动画 | `Create(decorations)` | 角的图标 |
| 59.4s | 旋转装饰 | `Rotate(decorations, PI)` | 1秒旋转 |
| 60.4s | 等待 | `Wait(1.0)` | 最后停留 |
| 61.4s | 全部淡出 | `FadeOut(*all_objects)` | 结束 |

### 装饰元素
- 6个小角图标围绕关注文字旋转
- 颜色交替：蓝色（余角）和红色（补角）

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| complementary_angles | Scene 2 | Scene 4 | 余角图形 |
| formula1 | Scene 2 | Scene 4 | α + β = 90° |
| supplementary_angles | Scene 4 | Scene 6 | 补角图形 |
| formula2 | Scene 4 | Scene 6 | α + β = 180° |
| property_diagrams | Scene 6 | Scene 6 | 性质图示 |
| decorations | Scene 7 | Scene 7 | 结尾装饰 |

---

## 关键技术要点

### 1. 角度弧的精确绘制
```python
# 使用 Angle 类或 Arc 类
from manim import Angle, Arc

# 方法1: 使用 Angle (推荐)
angle = Angle(ray1, ray2, radius=0.8, color=BLUE)

# 方法2: 使用 Arc (更灵活)
arc = Arc(
    radius=0.8,
    start_angle=0,
    angle=30*DEGREES,
    color=BLUE,
    arc_center=ORIGIN
)
```

### 2. 直角标记
```python
def create_right_angle_mark(corner, p1, p2, size=0.15):
    """创建直角标记（小方块）"""
    v1 = (p1 - corner) / np.linalg.norm(p1 - corner) * size
    v2 = (p2 - corner) / np.linalg.norm(p2 - corner) * size
    
    square = Polygon(
        corner,
        corner + v1,
        corner + v1 + v2,
        corner + v2,
        color=GREEN,
        stroke_width=2
    )
    return square
```

### 3. 平角标记
```python
# 用不同颜色的弧或箭头标记平角
straight_mark = DoubleArrow(
    start=LEFT*3,
    end=RIGHT*3,
    color=ORANGE,
    stroke_width=2,
    buff=0
).shift(DOWN*0.2)
```

### 4. 中文字体处理
```python
# 所有中文使用 Text 类
Text("余角", font="Noto Sans CJK SC", font_size=36)

# 数学符号使用 MathTex
MathTex(r"\alpha + \beta = 90^\circ")
```

### 5. 颜色主题一致性
- 余角：蓝色系 (#3498db)
- 补角：红色系 (#e74c3c)
- 直角：绿色 (#2ecc71)
- 平角：橙色 (#f39c12)
- 高亮：黄色 (YELLOW)

---

## 质量检查点

### 渲染前
- [ ] 所有角度计算验证正确（90° 和 180°）
- [ ] 中文使用 Text，数学使用 MathTex
- [ ] 元素位置在安全边界内
- [ ] 字体大小符合规范
- [ ] 颜色主题一致

### 渲染后
- [ ] 无元素溢出边界
- [ ] 文字清晰可读
- [ ] 动画节奏流畅
- [ ] 关键概念停留时间足够
- [ ] 总时长在60-75秒

---

## 预期效果

1. **教学效果**: 通过视觉动画清晰展示余角和补角的概念
2. **记忆点**: 90°直角（绿色方块）和180°平角（橙色线）
3. **互动性**: 具体数值例子让学生容易代入
4. **专业性**: 精确的几何计算和流畅的动画
5. **品牌识别**: 一致的作者标识和配色方案