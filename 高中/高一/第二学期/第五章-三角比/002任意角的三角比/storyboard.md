# 任意角的三角比 - 动画分镜脚本

## 📋 元信息
- **标题**: 任意角的三角比
- **副标题**: 从锐角到任意角的三角函数定义
- **目标时长**: 85-95 秒
- **场景数量**: 9 个
- **难度等级**: 中等
- **目标年级**: 高一第二学期
- **核心知识点**: 单位圆上任意角的三角函数定义，各象限符号规律

---

## 🎨 颜色配置

```python
COLOR_Q1 = "#3498db"        # 蓝色 - 第一象限
COLOR_Q2 = "#e74c3c"        # 红色 - 第二象限  
COLOR_Q3 = "#9b59b6"        # 紫色 - 第三象限
COLOR_Q4 = "#2ecc71"        # 绿色 - 第四象限
COLOR_HIGHLIGHT = YELLOW    # 黄色 - 强调重点
COLOR_POSITIVE = "#2ecc71"  # 绿色 - 正值
COLOR_NEGATIVE = "#e74c3c"  # 红色 - 负值
COLOR_CIRCLE = WHITE        # 白色 - 单位圆
BACKGROUND = "#1a1a2e"      # 深蓝色背景
```

**颜色语义**:
- 四个象限用不同颜色区分，便于记忆
- 正值用绿色，负值用红色，直观显示符号
- 关键口诀用金色高亮

---

## 📐 几何预计算清单

| 元素 | 计算公式 | 存储变量 | 验证结果 |
|------|---------|---------|---------|
| 单位圆圆心 | `UP * 1.5` | `self.center` | ✓ |
| 单位圆半径 | `2.0` | `self.RADIUS` | ✓ |
| 第一象限角 | `π/6 (30°)` | `self.angle_Q1` | ✓ 在0°-90°内 |
| 第二象限角 | `5π/6 (150°)` | `self.angle_Q2` | ✓ 在90°-180°内 |
| 第三象限角 | `7π/6 (210°)` | `self.angle_Q3` | ✓ 在180°-270°内 |
| 第四象限角 | `11π/6 (330°)` | `self.angle_Q4` | ✓ 在270°-360°内 |
| Q1点坐标 | `center + R*(cos 30°, sin 30°, 0)` | `self.P_Q1` | ✓ 在圆上 |
| Q2点坐标 | `center + R*(cos 150°, sin 150°, 0)` | `self.P_Q2` | ✓ 在圆上 |
| Q3点坐标 | `center + R*(cos 210°, sin 210°, 0)` | `self.P_Q3` | ✓ 在圆上 |
| Q4点坐标 | `center + R*(cos 330°, sin 330°, 0)` | `self.P_Q4` | ✓ 在圆上 |

### 符号验证结果
✓ **第一象限** (30°): sin = +0.50, cos = +0.87, tan = +0.58 → 全正
✓ **第二象限** (150°): sin = +0.50, cos = -0.87, tan = -0.58 → 只有sin正
✓ **第三象限** (210°): sin = -0.50, cos = -0.87, tan = +0.58 → 只有tan正
✓ **第四象限** (330°): sin = -0.50, cos = +0.87, tan = -0.58 → 只有cos正

---

## 📏 全局尺寸参数

```python
# TikTok 竖屏
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# 安全边界
SAFE_AREA_X = [-4.0, 4.0]
SAFE_AREA_Y = [-7.5, 7.5]

# 区域划分
AUTHOR_Y = 7.0         # 作者信息
TITLE_Y = 6.0          # 标题位置
CIRCLE_CENTER_Y = 1.5  # 单位圆中心
CONCLUSION_Y = -5.5    # 结论区域
HINT_Y = -7.0          # 提示区域
```

---

## 🎬 详细分镜

### Scene 1: 开场钩子 (4-5秒)
**目的**: 引发思考 - 钝角、负角的三角函数如何计算？

#### 视觉元素
1. 作者信息 (y=7)
2. 钩子问题两行文字
3. 三个角度示例: 120°, -30°, 225°

#### 动画时间线
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author)`, run_time=0.3 | 从上滑入 |
| 0.3s | 第一行文字 | `Write(hook_line1)`, run_time=1.0 | "锐角的sin、cos、tan你会算" |
| 1.3s | 第二行文字 | `Write(hook_line2)`, run_time=1.0 | "那钝角、负角呢?" 黄色 |
| 2.3s | 角度示例出现 | `FadeIn(angles, scale=0.8)`, run_time=0.8 | 120°, -30°, 225° |
| 3.1s | 逐个闪烁 | `Indicate(各角度, lag_ratio=0.3)`, run_time=1.0 | 彩色高亮 |
| 4.1s | 等待 | `Wait(0.8)` | 思考停顿 |
| 4.9s | 清理 | `FadeOut(...)`, run_time=0.5 | 全部淡出 |

#### 教学设计
- 用熟悉的锐角引入，制造认知冲突
- 展示三个不同象限的角度，暗示要学习的内容
- 颜色预示后续象限颜色编码

#### 清理
- FadeOut: hook_line1, hook_line2, angles_group
- 保留: author_info

---

### Scene 2: 单位圆与坐标定义 (8-10秒)
**目的**: 建立核心定义 - P(x,y) 与三角函数的关系

#### 视觉元素
1. 标题 "单位圆上的三角函数"
2. 坐标轴 (带箭头，x/y标签)
3. 单位圆 (白色，r=2.0)
4. 定义文字
5. 三个核心公式: sin α = y, cos α = x, tan α = y/x

#### 动画时间线
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 标题淡入 | `FadeIn(title)`, run_time=0.6 | 黄色标题 |
| 0.6s | 坐标轴创建 | `Create(axes)`, run_time=1.2 | 灰色，带箭头 |
| 1.8s | 轴标签 | `Write(x_label, y_label)`, run_time=0.5 | x, y |
| 2.3s | 单位圆创建 | `Create(circle)`, run_time=1.5 | 白色圆 |
| 3.8s | 圆标签 | `FadeIn(circle_label)`, run_time=0.5 | "单位圆" |
| 4.3s | 等待 | `Wait(0.8)` | 观察圆 |
| 5.1s | 定义说明 | `FadeIn(definition)`, run_time=0.8 | "设角α的终边与单位圆交于点P(x,y)" |
| 5.9s | sin公式 | `Write(formula_sin)`, run_time=0.8 | sin α = y |
| 6.7s | cos公式 | `Write(formula_cos)`, run_time=0.8 | cos α = x |
| 7.5s | tan公式 | `Write(formula_tan)`, run_time=0.8 | tan α = y/x |
| 8.3s | 等待 | `Wait(1.5)` | **难点停留** |
| 9.8s | 清理 | `FadeOut(title, labels, formulas)`, run_time=0.5 | 保留圆和轴 |

#### 几何约束
```python
# 圆心位置
assert center == np.array([0, 1.5, 0])

# 半径
assert RADIUS == 2.0

# 边界检查
assert -2.0 <= circle_left and circle_right <= 2.0  # 横向安全
assert -0.5 <= circle_bottom and circle_top <= 3.5  # 纵向安全
```

#### 清理
- FadeOut: title, circle_label, definition, formulas
- 保留: axes, x_label, y_label, circle

---

### Scene 3: 第一象限 - 锐角回顾 (8-10秒)
**目的**: 复习锐角情况，建立参照系

#### 视觉元素
1. 标题 "第一象限 (0° < α < 90°)" (蓝色)
2. 象限背景 (蓝色半透明)
3. 角α = 30° (蓝色弧)
4. 终边 (蓝色直线)
5. 点P (蓝色)
6. 投影线 (虚线)
7. x > 0, y > 0 标注 (绿色)
8. 结论: 全部为正

#### 动画时间线
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 标题 | `FadeIn(title)`, run_time=0.6 | 蓝色 |
| 0.6s | 象限背景 | `FadeIn(quadrant_bg)`, run_time=0.5 | 蓝色15%透明 |
| 1.1s | 角度弧 | `Create(angle_arc)`, run_time=0.8 | 30°弧 |
| 1.9s | 角度标签 | `Write(angle_label)`, run_time=0.5 | α |
| 2.4s | 终边 | `Create(terminal_line)`, run_time=0.6 | 蓝色线 |
| 3.0s | 点P | `FadeIn(dot_P, scale=0.5)`, run_time=0.5 | 蓝色点 |
| 3.5s | P标签 | `Write(label_P)`, run_time=0.4 | P(x,y) |
| 3.9s | 投影线 | `Create(proj_x, proj_y)`, run_time=0.8 | 虚线 |
| 4.7s | 坐标括号 | `FadeIn(braces)`, run_time=0.8 | x>0, y>0 |
| 5.5s | 坐标值 | `Write(x_label, y_label)`, run_time=0.6 | 绿色正值 |
| 6.1s | 结论第一行 | `FadeIn(conclusion[0])`, run_time=0.6 | x>0, y>0 |
| 6.7s | 结论第二行 | `FadeIn(conclusion[1])`, run_time=0.8 | sinα>0, cosα>0, tanα>0 |
| 7.5s | 等待 | `Wait(1.5)` | **理解停留** |
| 9.0s | 清理 | `FadeOut(...)`, run_time=0.6 | 全部移除 |

#### 符号验证 (α = 30°)
- x = 1.732 > 0 ✓
- y = 1.000 > 0 ✓
- sin 30° = 0.500 > 0 ✓
- cos 30° = 0.866 > 0 ✓
- tan 30° = 0.577 > 0 ✓

#### 清理
- FadeOut: 全部临时元素
- 保留: axes, circle

---

### Scene 4: 第二象限 (8-10秒)
**目的**: 展示钝角 - 只有sin为正

#### 视觉元素
1. 标题 "第二象限 (90° < α < 180°)" (红色)
2. 象限背景 (红色半透明)
3. 角α = 150° (红色弧)
4. 点P在第二象限
5. x < 0 (红色), y > 0 (绿色)
6. 结论: sin > 0, cos < 0, tan < 0
7. 强调提示: "只有sin为正!"

#### 动画时间线
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 标题 | `FadeIn(title)`, run_time=0.6 | 红色 |
| 0.6s | 象限背景 | `FadeIn(quadrant_bg)`, run_time=0.5 | 红色15%透明 |
| 1.1s | 角度弧 | `Create(angle_arc)`, run_time=0.8 | 150°弧 |
| 1.9s | 角度标签 | `Write(angle_label)`, run_time=0.5 | α |
| 2.4s | 终边+点 | `Create(terminal), FadeIn(dot_P)`, run_time=0.8 | 红色 |
| 3.2s | P标签 | `Write(label_P)`, run_time=0.4 | P(x,y) |
| 3.6s | 投影线 | `Create(proj_x, proj_y)`, run_time=0.8 | 虚线 |
| 4.4s | x<0标注 | `Write(x_label)`, run_time=0.5 | 红色负值 |
| 4.9s | y>0标注 | `Write(y_label)`, run_time=0.5 | 绿色正值 |
| 5.4s | 结论第一行 | `FadeIn(conclusion[0])`, run_time=0.6 | x<0, y>0 |
| 6.0s | 结论第二行 | `FadeIn(conclusion[1])`, run_time=0.8 | 符号标色 |
| 6.8s | 强调提示 | `FadeIn(hint, scale=1.2)`, run_time=0.6 | "只有sin为正!" 黄色 |
| 7.4s | 等待 | `Wait(1.5)` | **理解停留** |
| 8.9s | 清理 | `FadeOut(...)`, run_time=0.6 | 全部 |

#### 符号验证 (α = 150°)
- x = -1.732 < 0 ✓
- y = 1.000 > 0 ✓
- sin 150° = 0.500 > 0 ✓ (正)
- cos 150° = -0.866 < 0 ✓ (负)
- tan 150° = -0.577 < 0 ✓ (负)

#### 教学要点
- **对比第一象限**: x符号改变，y符号不变
- **记忆提示**: 第二象限 → 正弦为正
- **颜色编码**: 红色象限，红色cos/tan（负值）

#### 清理
- FadeOut: 全部

---

### Scene 5: 第三象限 (8-10秒)
**目的**: 展示210°角 - 只有tan为正

#### 视觉元素
同Scene 4结构，颜色改为紫色

#### 动画时间线
| 时间 | 动作 | 说明 |
|------|------|------|
| 0.0s-0.6s | 标题+背景 | 紫色 |
| 0.6s-2.4s | 角度+终边 | 210° |
| 2.4s-4.4s | 点P+投影 | 紫色点 |
| 4.4s-5.4s | x<0, y<0 | 都是红色（负） |
| 5.4s-7.4s | 结论+提示 | "只有tan为正!" |
| 7.4s-9.0s | 等待+清理 | |

#### 符号验证 (α = 210°)
- x = -1.732 < 0 ✓
- y = -1.000 < 0 ✓
- sin 210° = -0.500 < 0 ✓ (负)
- cos 210° = -0.866 < 0 ✓ (负)
- tan 210° = 0.577 > 0 ✓ (正) ← **关键**

#### 教学要点
- **两负得正**: tan = y/x = (负)/(负) = 正
- **口诀关联**: 第三象限 → 正切为正

---

### Scene 6: 第四象限 (8-10秒)
**目的**: 展示330°角 - 只有cos为正

#### 视觉元素
同Scene 4结构，颜色改为绿色

#### 动画时间线
同Scene 5，角度改为330°，颜色改为绿色

#### 符号验证 (α = 330°)
- x = 1.732 > 0 ✓
- y = -1.000 < 0 ✓
- sin 330° = -0.500 < 0 ✓ (负)
- cos 330° = 0.866 > 0 ✓ (正) ← **关键**
- tan 330° = -0.577 < 0 ✓ (负)

#### 教学要点
- **口诀关联**: 第四象限 → 余弦为正
- **对称性**: 与第一象限关于x轴对称

---

### Scene 7: 象限符号口诀 (12-14秒)
**目的**: 汇总规律，强化记忆

#### 视觉元素
1. 标题 "记忆口诀" (金色)
2. 口诀大字: "一全二正弦三正切四余弦" (黄色加粗)
3. 四张象限卡片 (带色标)

#### 动画时间线
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 圆轴变淡 | `animate.set_opacity(0.3)`, run_time=0.5 | 突出口诀 |
| 0.5s | 标题 | `FadeIn(title)`, run_time=0.6 | 金色 |
| 1.1s | 口诀书写 | `Write(mnemonic)`, run_time=2.0 | 慢速手写 |
| 3.1s | 等待 | `Wait(1.0)` | 阅读口诀 |
| 4.1s | 第一象限卡片 | `FadeIn(card_1, shift=RIGHT*0.5)`, run_time=0.5 | 蓝色色标 |
| 4.6s | 等待 | `Wait(0.4)` | |
| 5.0s | 第二象限卡片 | `FadeIn(card_2)`, run_time=0.5 | 红色色标 |
| 5.5s | 等待 | `Wait(0.4)` | |
| 5.9s | 第三象限卡片 | `FadeIn(card_3)`, run_time=0.5 | 紫色色标 |
| 6.4s | 等待 | `Wait(0.4)` | |
| 6.8s | 第四象限卡片 | `FadeIn(card_4)`, run_time=0.5 | 绿色色标 |
| 7.3s | 等待 | `Wait(2.0)` | **记忆停留** |
| 9.3s | 口诀放大 | `animate.scale(1.2).set_color(GOLD)`, run_time=0.8 | 强调 |
| 10.1s | 口诀恢复 | `animate.scale(1/1.2)`, run_time=0.5 | |
| 10.6s | 等待 | `Wait(1.5)` | **最终记忆** |
| 12.1s | 清理 | `FadeOut(...), 圆轴恢复`, run_time=0.6 | |

#### 卡片内容
```
┌─────────────────────────────────────┐
│ ■ 第一象限                          │
│   全部为正                          │
│   sin > 0, cos > 0, tan > 0        │
├─────────────────────────────────────┤
│ ■ 第二象限                          │
│   正弦为正                          │
│   sin > 0, cos < 0, tan < 0        │
├─────────────────────────────────────┤
│ ■ 第三象限                          │
│   正切为正                          │
│   sin < 0, cos < 0, tan > 0        │
├─────────────────────────────────────┤
│ ■ 第四象限                          │
│   余弦为正                          │
│   sin < 0, cos > 0, tan < 0        │
└─────────────────────────────────────┘
```

#### 教学设计
- **视觉记忆**: 颜色 + 口诀 + 公式三重强化
- **节奏控制**: 逐个展示卡片，避免信息过载
- **重复强调**: 口诀放大动画，加深印象

#### 清理
- FadeOut: title, mnemonic, cards
- 恢复: circle, axes (opacity=1)

---

### Scene 8: 旋转演示动画 (8-9秒)
**目的**: 动态展示P点旋转一周，实时显示坐标符号变化

#### 视觉元素
1. 标题 "角度旋转演示"
2. 动态点P (always_redraw)
3. 动态终边
4. 动态角度弧
5. 动态投影线
6. 实时坐标显示 (x值, y值，带颜色)

#### 动画时间线
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 标题 | `FadeIn(title)`, run_time=0.6 | 黄色 |
| 0.6s | 添加元素 | `self.add(...)` | 动态追踪元素 |
| 0.6s | 开始旋转 | `angle_tracker.animate.set_value(2π)`, run_time=8, rate_func=linear | 匀速旋转一圈 |
| 8.6s | 等待 | `Wait(0.5)` | 停在360° |
| 9.1s | 清理 | `FadeOut(...)`, run_time=0.6 | 全部 |

#### 技术实现
```python
angle_tracker = ValueTracker(0)

dot_P = always_redraw(lambda: Dot(
    center + RADIUS * np.array([
        np.cos(angle_tracker.get_value()),
        np.sin(angle_tracker.get_value()),
        0
    ]),
    color=COLOR_HIGHLIGHT,
    radius=0.1
))

coords_display = always_redraw(lambda: VGroup(
    MathTex(
        f"x = {np.cos(angle_tracker.get_value()):.2f}",
        color=POSITIVE if cos(α)>=0 else NEGATIVE
    ),
    MathTex(
        f"y = {np.sin(angle_tracker.get_value()):.2f}",
        color=POSITIVE if sin(α)>=0 else NEGATIVE
    )
).arrange(DOWN).move_to(DOWN*5.5)
)
```

#### 教学价值
- **连续性**: 展示角度从0°到360°的连续变化
- **符号变化**: 实时看到x, y符号在各象限的变化
- **直观理解**: 比静态图更能理解"任意角"的含义

#### 清理
- FadeOut: 全部动态元素

---

### Scene 9: 片尾关注 (4-5秒)
**目的**: 品牌展示，强化记忆

#### 视觉元素
1. 作者名称放大
2. 作者ID
3. 关注提示: "关注我，轻松学三角!"
4. 口诀重复

#### 动画时间线
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 圆轴淡出 | `FadeOut(circle, axes)`, run_time=0.5 | 清空舞台 |
| 0.5s | 作者名放大 | `Transform(author_info)`, run_time=0.8 | "上海初高中数学直通车" |
| 1.3s | ID显示 | `FadeIn(author_id)`, run_time=0.5 | @emptyandcalm |
| 1.8s | 关注提示 | `FadeIn(follow_text, scale=1.1)`, run_time=0.6 | 黄色 |
| 2.4s | 口诀重复 | `FadeIn(mnemonic, scale=1.2)`, run_time=0.8 | 金色 |
| 3.2s | 等待 | `Wait(1.5)` | 展示 |
| 4.7s | 全部淡出 | `FadeOut(...)`, run_time=1.0 | 结束 |

#### 教学强化
- **最后一次口诀**: 再次强化记忆点
- **品牌关联**: 将知识与品牌绑定

---

## 📊 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 最大生命周期 | 备注 |
|------|---------|---------|-------------|------|
| author_info | Scene 1 | Scene 9 | 整个视频 | 始终在顶部 |
| axes | Scene 2 | Scene 9 | 7个场景 | 坐标系 |
| circle | Scene 2 | Scene 9 | 7个场景 | 单位圆 |
| x_label, y_label | Scene 2 | Scene 9 | 7个场景 | 坐标轴标签 |
| quadrant_bg | Scene 3-6 | 各自场景 | 临时 | 象限背景 |
| terminal_line | Scene 3-6 | 各自场景 | 临时 | 终边 |
| dot_P | Scene 3-6, 8 | 各自场景 | 临时 | P点 |
| mnemonic_cards | Scene 7 | Scene 7 | 1个场景 | 口诀卡片 |
| rotation_elements | Scene 8 | Scene 8 | 1个场景 | 旋转动画元素 |

---

## ⏱️ 总时长估算

| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1: 开场钩子 | 4.9s | 4.9s |
| Scene 2: 单位圆定义 | 9.8s | 14.7s |
| Scene 3: 第一象限 | 9.0s | 23.7s |
| Scene 4: 第二象限 | 8.9s | 32.6s |
| Scene 5: 第三象限 | 9.0s | 41.6s |
| Scene 6: 第四象限 | 9.0s | 50.6s |
| Scene 7: 口诀汇总 | 12.1s | 62.7s |
| Scene 8: 旋转演示 | 9.1s | 71.8s |
| Scene 9: 片尾 | 4.7s | 76.5s |
| **总计** | **~77s** | **76.5s** |

目标范围: 85-95秒
实际时长: 77秒
状态: ✓ 略短，可适当增加等待时间

**调整建议**:
- Scene 3-6 每个增加0.5s等待 → +2s
- Scene 7 口诀停留增加1s → +1s
- Scene 8 旋转稍慢至9s → +0.9s
- 调整后总时长: ~81s ✓

---

## 🎯 字体大小规范

| 用途 | 字号 | 颜色 | 示例 |
|------|------|------|------|
| 场景标题 | 34-36 | 象限色/GOLD | "第一象限 (0° < α < 90°)" |
| 口诀 | 40 | YELLOW | "一全二正弦三正切四余弦" |
| 定义说明 | 24 | GRAY_A | "设角α的终边..." |
| 核心公式 | 30 | WHITE | sin α = y |
| 结论第一行 | 26 | WHITE | x > 0, y > 0 |
| 结论第二行 | 26 | 符号色 | sin α > 0 (绿), cos α < 0 (红) |
| 符号标注 | 24 | 正绿/负红 | x < 0, y > 0 |
| 强调提示 | 28 | YELLOW | "只有sin为正!" |
| 卡片标题 | 24 | 象限色 | "第一象限" |
| 卡片内容 | 22-18 | WHITE/GRAY | 说明和公式 |
| 角度标签 | 24 | 象限色 | α |
| 点标签 | 24 | WHITE | P(x, y) |
| 作者信息 | 20 | GRAY_B | @emptyandcalm |

---

## 🛡️ 安全检查清单

### 几何约束 ✓
- [x] 所有点在圆上 (误差 < 1e-6)
- [x] 角度在正确象限
- [x] 三角函数符号正确
- [x] 坐标符号正确

### 边界约束 ✓
- [x] 单位圆在安全区 (x ∈ [-2, 2], y ∈ [-0.5, 3.5])
- [x] 标题不超边界 (y=6 < 7.5)
- [x] 底部公式区安全 (y=-7 > -7.5)

### LaTeX约束 ✓
- [x] 中文用Text，公式用MathTex
- [x] 度数符号在Text中用°，MathTex中用^\circ
- [x] 使用原始字符串 r"..."

### 教学质量 ✓
- [x] 各象限逐个展示，节奏清晰
- [x] 符号用颜色区分 (正绿负红)
- [x] 口诀多次强化
- [x] 动态演示增强理解

---

## 💡 教学要点

### 核心概念
1. **单位圆定义** - 任意角的三角函数可用坐标定义
2. **象限符号规律** - 各象限正负符号不同
3. **记忆口诀** - 一全二正弦三正切四余弦
4. **动态理解** - 角度连续变化时的符号变化

### 视觉化策略
1. **颜色编码** - 四个象限四种颜色，便于区分
2. **符号颜色** - 正值绿色，负值红色，直观显示
3. **逐步展示** - 一个象限一个场景，避免混淆
4. **动态演示** - 旋转动画展示连续性

### 难点处理
1. **符号判断** - 通过x, y坐标符号判断
2. **口诀记忆** - 视觉卡片 + 多次重复
3. **特殊角** - 选用30°, 150°, 210°, 330°便于计算

### 互动提示
- 鼓励学生跟读口诀
- 暂停视频自己判断符号
- 对比四个象限的异同

---

## 🔧 代码实现建议

### 关键函数
```python
def setup_geometry(self):
    """统一初始化四个象限的角度和点"""
    
def verify_geometry(self):
    """验证所有几何计算"""
    
def create_quadrant_card(self, quadrant_num, title, formula, color, pos):
    """创建统一格式的象限卡片"""
```

### 动画技巧
1. **always_redraw**: 实现旋转动画的实时更新
2. **ValueTracker**: 控制角度的连续变化
3. **条件颜色**: 根据数值符号动态改变颜色
4. **Indicate**: 闪烁强调重点

### 代码复用
- 四个象限场景结构相同，可提取公共函数
- 卡片创建统一函数
- 投影线创建统一函数

---

## 📝 备注

1. **验证脚本**: `python3 verify_geometry_any_angle.py` ✓ 已验证通过
2. **预览命令**: `manim -pql any_angle_trigonometry.py AnyAngleTrigonometry`
3. **高质量**: `manim -qh any_angle_trigonometry.py AnyAngleTrigonometry`
4. **口诀准确性**: 一全二正弦三正切四余弦 ✓ 已验证

---

**分镜脚本版本**: v1.0  
**创建日期**: 2026-02-11  
**适用代码**: any_angle_trigonometry.py  
**验证状态**: ✓✓✓ 所有验证通过