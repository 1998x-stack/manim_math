# 二倍角与半角公式 - 动画分镜脚本

## 📋 元信息
- **标题**: 二倍角与半角公式
- **目标时长**: 75-85 秒
- **场景数量**: 8 个
- **难度等级**: 中等偏上
- **目标年级**: 高一第二学期
- **知识点**: 二倍角公式、半角公式、降幂公式

---

## 🎨 颜色配置

```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要角度α
COLOR_SECONDARY = "#e74c3c"      # 红色 - 二倍角2α
COLOR_HALF_ANGLE = "#2ecc71"     # 绿色 - 半角α/2
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 强调重点
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_CIRCLE = WHITE             # 白色 - 单位圆
BACKGROUND = "#1a1a2e"           # 深蓝色背景
```

---

## 📐 几何预计算清单

| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 单位圆圆心 | `UP * 1.5` | `self.center` | 向上偏移避免与底部公式重叠 |
| 单位圆半径 | `1.8` | `self.RADIUS` | 足够大以清晰展示，但不超边界 |
| 示例角度α | `PI / 6` | `self.ALPHA` | 30度，方便计算和展示 |
| α点坐标 | `center + R*(cos α, sin α, 0)` | `self.P_alpha` | 精确计算，必须在圆上 |
| 2α点坐标 | `center + R*(cos 2α, sin 2α, 0)` | `self.P_2alpha` | 精确计算，必须在圆上 |
| α/2点坐标 | `center + R*(cos α/2, sin α/2, 0)` | `self.P_half_alpha` | 精确计算，必须在圆上 |
| α点x投影 | `center + (R*cos α, 0, 0)` | `self.P_alpha_x` | 垂直投影到x轴 |
| α点y投影 | `center + (0, R*sin α, 0)` | `self.P_alpha_y` | 垂直投影到y轴 |

### 几何验证约束
```python
# 所有点必须在圆上
assert abs(np.linalg.norm(P - center) - RADIUS) < 1e-6

# 投影必须垂直
assert abs(np.dot(proj_line, axis_direction)) < 1e-6

# 角度关系正确
assert abs(angle(P_2alpha) - 2*angle(P_alpha)) < 1e-6
```

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
TITLE_Y = 6.0          # 标题位置
AUTHOR_Y = 7.0         # 作者信息
CIRCLE_CENTER_Y = 1.5  # 单位圆中心
FORMULA_Y = -4.0       # 公式推导区域中心
```

---

## 🎬 详细分镜

### Scene 1: 开场钩子 (3-4秒)
**目的**: 快速吸引注意力，引出主题

#### 视觉元素
1. 作者标识 (顶部，y=7)
2. 钩子问题文字
   - 第一行: "你知道 sin²α + cos²α = 1"
   - 第二行: "那 sin 2α 等于多少?" (黄色高亮)
3. 问号符号 (放大+闪烁)

#### 动画时间线
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)`, run_time=0.3 | 从上方滑入 |
| 0.3s | 第一行文字书写 | `Write(hook_line1)`, run_time=1.0 | 手写效果 |
| 1.3s | 第二行文字书写 | `Write(hook_line2)`, run_time=1.0 | 黄色高亮 |
| 2.3s | 问号出现 | `FadeIn(mystery, scale=2)`, run_time=0.5 | 放大出现 |
| 2.8s | 问号闪烁 | `Flash(mystery)`, run_time=0.5 | 红色闪光 |
| 3.3s | 等待 | `Wait(0.5)` | 停顿 |
| 3.8s | 全部淡出 | `FadeOut(VGroup)`, run_time=0.5 | 清理场景 |

#### 几何元素
- 无

#### 清理
- FadeOut: hook_line1, hook_line2, mystery
- 保留: author_info

---

### Scene 2: 建立单位圆基础 (6-8秒)
**目的**: 建立几何基础，展示角度α和三角函数定义

#### 视觉元素
1. 标题 "单位圆与三角函数" (y=6)
2. 坐标轴系统 (简化，不显示刻度)
3. 单位圆 (白色，圆心在 UP*1.5)
4. 角α扇形 (蓝色，30度)
5. 点P(cosα, sinα)
6. 投影线段 (虚线)
7. 标签: cosα, sinα, α

#### 动画时间线
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 标题淡入 | `FadeIn(title, shift=DOWN*0.3)`, run_time=0.6 | 黄色标题 |
| 0.6s | 坐标轴创建 | `Create(axes)`, run_time=1.0 | 灰色坐标轴 |
| 1.6s | 单位圆创建 | `Create(circle)`, run_time=1.2 | 白色圆 |
| 2.8s | 角α扇形扫出 | `Create(angle_sector)`, run_time=1.0 | 蓝色扇形 |
| 3.8s | 点P出现 | `FadeIn(dot_P, scale=0.5)`, run_time=0.5 | 缩放出现 |
| 4.3s | 投影线绘制 | `Create(proj_x), Create(proj_y)`, run_time=0.8 | 虚线 |
| 5.1s | 标注cosα,sinα | `Write(labels)`, run_time=0.8 | 坐标标签 |
| 5.9s | 角度标注α | `Write(angle_label)`, run_time=0.5 | 角度符号 |
| 6.4s | 等待 | `Wait(1.0)` | 理解停顿 |
| 7.4s | 部分清理 | `FadeOut(投影, 标签)`, run_time=0.5 | 保留主要元素 |

#### 几何验证
```python
# 点P必须在圆上
assert abs(np.linalg.norm(P_alpha - center) - RADIUS) < 1e-6

# 投影必须垂直
proj_to_x = P_alpha - P_alpha_x
assert abs(np.dot(proj_to_x[:2], [1,0])) < 1e-6
```

#### 清理
- FadeOut: title, proj_x, proj_y, label_cos, label_sin
- 保留: axes, circle, angle_alpha_sector, dot_P, label_P, angle_label

---

### Scene 3: 二倍角sin公式推导 (12-15秒)
**目的**: 几何直观展示并推导 sin 2α = 2sin α cos α

#### 视觉元素
1. 标题 "二倍角公式: sin 2α" (红色)
2. 角2α扇形 (红色，60度)
3. 点Q(cos2α, sin2α)
4. 公式推导步骤 (底部区域)

#### 动画时间线
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 标题更新 | `FadeIn(title)`, run_time=0.6 | 红色标题 |
| 0.6s | α角变淡 | `angle_alpha.animate.set_fill(opacity=0.15)`, run_time=0.5 | 降低不透明度 |
| 1.1s | 2α扇形创建 | `Create(angle_2alpha_sector)`, run_time=1.2 | 红色扇形 |
| 2.3s | 点Q出现 | `FadeIn(dot_Q, scale=0.5)`, run_time=0.5 | 2α对应点 |
| 2.8s | 角度标注2α | `Write(angle_2alpha_label)`, run_time=0.5 | 角度符号 |
| 3.3s | 等待 | `Wait(0.5)` | 观察角度关系 |
| 3.8s | 问题 | `Write(question)` "sin 2α = ?", run_time=0.8 | 底部公式区 |
| 4.6s | 等待 | `Wait(0.5)` | 思考 |
| 5.1s | 提示 | `FadeIn(hint)` "利用两角和公式", run_time=0.6 | 灰色提示 |
| 5.7s | 等待 | `Wait(0.8)` | 阅读提示 |
| 6.5s | 步骤1 | `TransformMatchingTex` sin 2α = sin(α+α), run_time=1.0 | 展开 |
| 7.5s | 步骤2 | `Write(step2)` = sinα cosα + cosα sinα, run_time=1.2 | 两角和公式 |
| 8.7s | 最终公式 | `Write(final)` = 2sinα cosα, run_time=1.0 | 黄色高亮 |
| 9.7s | 高亮强调 | `Circumscribe(final, color=YELLOW)`, run_time=1.2 | 圈住公式 |
| 10.9s | 等待 | `Wait(1.5)` | **难点停留** |
| 12.4s | 清理 | `FadeOut(...)`, run_time=0.6 | 移除临时元素 |
| 13.0s | 公式小化 | `Transform(final, final_small)`, run_time=0.5 | 移到顶部保留 |

#### 公式推导逻辑
```
sin 2α = ?
      ↓ (令 β = α)
sin(α + α) = sin α cos α + cos α sin α
           = 2 sin α cos α
```

#### 清理
- FadeOut: title, question, hint, step1, step2, angle_2alpha_sector, dot_Q, angle_2alpha_label
- 保留 (小字): final_formula (移至顶部 y=5.5)

---

### Scene 4: 二倍角cos公式展示 (10-12秒)
**目的**: 展示 cos 2α 的三种等价形式

#### 视觉元素
1. 标题 "二倍角公式: cos 2α"
2. 三个等价公式并列
3. 提示文字

#### 动画时间线
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 标题 | `FadeIn(title)`, run_time=0.6 | 红色 |
| 0.6s | 第一形式 | `Write(form1)` cos²α - sin²α, run_time=1.0 | 基本形式 |
| 1.6s | 等待 | `Wait(0.8)` | 阅读 |
| 2.4s | 提示 | `FadeIn(hint)` "利用 sin²α + cos²α = 1", run_time=0.6 | 恒等式 |
| 3.0s | 等待 | `Wait(0.6)` | 理解 |
| 3.6s | 第二形式 | `Write(form2)` 2cos²α - 1, run_time=1.0 | 变形1 |
| 4.6s | 等待 | `Wait(0.6)` | 对比 |
| 5.2s | 第三形式 | `Write(form3)` 1 - 2sin²α, run_time=1.0 | 变形2 |
| 6.2s | 框选 | `Create(box)`, run_time=0.8 | 黄色边框 |
| 7.0s | 等待 | `Wait(1.5)` | **难点停留** |
| 8.5s | 清理 | `FadeOut(...)`, run_time=0.6 | 全部移除 |

#### 公式关系
```
cos 2α = cos²α - sin²α         (基本)
       = cos²α - (1 - cos²α)   (代入 sin²α = 1 - cos²α)
       = 2cos²α - 1             (化简)
       
cos 2α = (1 - sin²α) - sin²α  (代入 cos²α = 1 - sin²α)
       = 1 - 2sin²α             (化简)
```

#### 清理
- FadeOut: 全部

---

### Scene 5: 二倍角tan公式 (8-10秒)
**目的**: 快速展示 tan 2α 公式

#### 动画时间线
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 标题 | `Write(title)` "二倍角公式: tan 2α", run_time=0.6 | 红色 |
| 0.6s | 推导思路 | `Write(hint)` tan 2α = sin 2α / cos 2α, run_time=1.0 | 定义 |
| 1.6s | 等待 | `Wait(0.8)` | 理解 |
| 2.4s | 代入 | `Write(step1)` 代入已知公式, run_time=1.2 | 分步 |
| 3.6s | 说明 | `FadeIn(step2)` "分子分母同除以 cos²α", run_time=0.6 | 技巧 |
| 4.2s | 最终公式 | `Write(final)` 2tanα/(1-tan²α), run_time=1.0 | 黄色 |
| 5.2s | 高亮 | `Circumscribe(final)`, run_time=1.0 | 强调 |
| 6.2s | 等待 | `Wait(1.2)` | 停留 |
| 7.4s | 清理 | `FadeOut(...)`, run_time=0.6 | 全部 |

#### 清理
- FadeOut: 全部

---

### Scene 6: 半角公式推导 (12-15秒)
**目的**: 从二倍角推导半角公式

#### 视觉元素
1. 标题 "半角公式" (绿色)
2. 角α/2扇形 (绿色，15度)
3. 点R(cos(α/2), sin(α/2))
4. 三个半角公式

#### 动画时间线
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 标题 | `FadeIn(title)`, run_time=0.6 | 绿色 |
| 0.6s | α角变淡 | `angle_alpha.animate.set_fill(opacity=0.15)`, run_time=0.5 | 降低 |
| 1.1s | α/2扇形 | `Create(angle_half_sector)`, run_time=1.0 | 绿色 |
| 2.1s | 点R出现 | `FadeIn(dot_R, scale=0.5)`, run_time=0.5 | 半角点 |
| 2.6s | 角度标注 | `Write(angle_half_label)` α/2, run_time=0.5 | 分数 |
| 3.1s | 等待 | `Wait(0.5)` | 观察 |
| 3.6s | 提示 | `FadeIn(hint)` "令 2α→α, α→α/2", run_time=0.8 | 替换思路 |
| 4.4s | 等待 | `Wait(0.8)` | 理解替换 |
| 5.2s | sin²公式 | `Write(sin_half)` sin²(α/2)=(1-cosα)/2, run_time=1.0 | 第一个 |
| 6.2s | 等待 | `Wait(0.6)` | 阅读 |
| 6.8s | cos²公式 | `Write(cos_half)` cos²(α/2)=(1+cosα)/2, run_time=1.0 | 第二个 |
| 7.8s | 等待 | `Wait(0.6)` | 对比 |
| 8.4s | tan公式 | `Write(tan_half)` tan(α/2)=sinα/(1+cosα), run_time=1.0 | 第三个 |
| 9.4s | 框选 | `Create(box)`, run_time=0.8 | 绿色边框 |
| 10.2s | 等待 | `Wait(1.5)` | **难点停留** |
| 11.7s | 清理 | `FadeOut(...)`, run_time=0.6 | 全部 |

#### 推导逻辑
```
cos 2α = 1 - 2sin²α
      ↓ (令 2α → α, α → α/2)
cos α = 1 - 2sin²(α/2)
2sin²(α/2) = 1 - cos α
sin²(α/2) = (1 - cos α) / 2

同理:
cos²(α/2) = (1 + cos α) / 2
```

#### 清理
- FadeOut: 全部

---

### Scene 7: 降幂公式与总结 (10-12秒)
**目的**: 展示降幂公式，汇总所有公式

#### 视觉元素
1. 标题 "降幂公式"
2. 两个降幂公式
3. 公式汇总网格 (8个公式卡片)

#### 动画时间线 - 第一部分:降幂公式
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 圆淡出 | `FadeOut(circle, axes, ...)`, run_time=0.6 | 清空舞台 |
| 0.6s | 标题 | `FadeIn(title)` "降幂公式", run_time=0.6 | 金色 |
| 1.2s | sin²公式 | `Write(power_sin)` sin²α=(1-cos2α)/2, run_time=1.0 | 从半角推导 |
| 2.2s | 等待 | `Wait(0.6)` | 阅读 |
| 2.8s | cos²公式 | `Write(power_cos)` cos²α=(1+cos2α)/2, run_time=1.0 | 对比 |
| 3.8s | 等待 | `Wait(1.0)` | 理解 |
| 4.8s | 清理 | `FadeOut(title, formulas)`, run_time=0.5 | 准备汇总 |

#### 动画时间线 - 第二部分:公式汇总
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 5.3s | 汇总标题 | `FadeIn(summary_title)` "公式汇总", run_time=0.6 | 金色大字 |
| 5.9s | 卡片1 | `FadeIn(card, shift=RIGHT*0.5)`, run_time=0.3 | 二倍角sin |
| 6.2s | 卡片2 | 同上 | 二倍角cos |
| 6.5s | 卡片3 | 同上 | 二倍角tan |
| 6.8s | 卡片4 | 同上 | 半角sin² |
| 7.1s | 卡片5 | 同上 | 半角cos² |
| 7.4s | 卡片6 | 同上 | 半角tan |
| 7.7s | 卡片7 | 同上 | 降幂sin² |
| 8.0s | 卡片8 | 同上 | 降幂cos² |
| 8.3s | 等待 | `Wait(1.5)` | 整体浏览 |
| 9.8s | 逐个闪烁 | `Indicate(cards, lag_ratio=0.1)`, run_time=1.5 | 黄色强调 |
| 11.3s | 等待 | `Wait(1.0)` | 记忆 |
| 12.3s | 清理 | `FadeOut(...)`, run_time=0.6 | 进入片尾 |

#### 公式卡片布局
```
[■] sin 2α = 2sinα cosα
[■] cos 2α = cos²α - sin²α
[■] tan 2α = 2tanα/(1-tan²α)
[■] sin²(α/2) = (1-cosα)/2
[■] cos²(α/2) = (1+cosα)/2
[■] tan(α/2) = sinα/(1+cosα)
[■] sin²α = (1-cos2α)/2
[■] cos²α = (1+cos2α)/2

颜色: 红色-二倍角, 绿色-半角, 金色-降幂
```

#### 清理
- FadeOut: 全部

---

### Scene 8: 片尾关注 (6-8秒)
**目的**: 品牌宣传，引导关注

#### 视觉元素
1. 作者名称放大
2. 作者ID
3. 关注提示
4. 装饰符号

#### 动画时间线
| 时间 | 动作 | 参数 | 说明 |
|------|------|------|------|
| 0.0s | 作者名放大 | `Transform(author_info, author_name)`, run_time=0.8 | "上海初高中数学直通车" |
| 0.8s | ID显示 | `FadeIn(author_id, shift=UP*0.3)`, run_time=0.5 | @emptyandcalm |
| 1.3s | 关注提示 | `FadeIn(follow_text, scale=1.1)`, run_time=0.6 | 黄色 |
| 1.9s | 装饰符号 | `FadeIn(symbols, lag_ratio=0.2)`, run_time=0.8 | sin, cos, tan, α |
| 2.7s | 等待 | `Wait(1.5)` | 停留展示 |
| 4.2s | 全部淡出 | `FadeOut(...)`, run_time=1.0 | 结束 |

#### 清理
- FadeOut: 全部

---

## 📊 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 最大生命周期 | 备注 |
|------|---------|---------|-------------|------|
| author_info | Scene 1 | Scene 8 | 整个视频 | 始终在顶部 |
| axes | Scene 2 | Scene 7 | 5个场景 | 坐标系统 |
| circle | Scene 2 | Scene 7 | 5个场景 | 单位圆 |
| angle_alpha_sector | Scene 2 | Scene 7 | 5个场景 | 角α扇形 |
| dot_P | Scene 2 | Scene 7 | 5个场景 | 点P |
| angle_2alpha_sector | Scene 3 | Scene 3 | 1个场景 | 临时: 2α扇形 |
| dot_Q | Scene 3 | Scene 3 | 1个场景 | 临时: 点Q |
| angle_half_sector | Scene 6 | Scene 6 | 1个场景 | 临时: α/2扇形 |
| dot_R | Scene 6 | Scene 6 | 1个场景 | 临时: 点R |
| sin_formula_saved | Scene 3 | Scene 7 | 4个场景 | 小字保留 |

---

## ⏱️ 总时长估算

| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1: 开场 | 3.8s | 3.8s |
| Scene 2: 单位圆 | 7.4s | 11.2s |
| Scene 3: sin 2α | 13.0s | 24.2s |
| Scene 4: cos 2α | 8.5s | 32.7s |
| Scene 5: tan 2α | 7.4s | 40.1s |
| Scene 6: 半角 | 11.7s | 51.8s |
| Scene 7: 汇总 | 12.3s | 64.1s |
| Scene 8: 片尾 | 4.2s | 68.3s |
| **总计** | **~68s** | **68.3s** |

目标范围: 75-85秒
实际时长: 68秒
状态: ✓ 在目标范围内 (可适当增加等待时间)

---

## 🎯 字体大小规范

| 用途 | 字号 | 颜色 | 示例 |
|------|------|------|------|
| 主标题 | 36-38 | 分类色/GOLD | "二倍角公式: sin 2α" |
| 副标题 | 28-32 | WHITE/GRAY_A | "单位圆与三角函数" |
| 主要公式 | 32-36 | HIGHLIGHT | sin 2α = 2sinα cosα |
| 推导步骤 | 26-30 | WHITE | 中间变换 |
| 说明文字 | 22-24 | GRAY_A | "利用两角和公式" |
| 标签 | 20-24 | WHITE | P, Q, R, α |
| 作者信息 | 20 | GRAY_B | @emptyandcalm |
| 汇总卡片 | 24 | WHITE | 公式列表 |

---

## 🛡️ 安全检查清单

### 几何约束 ✓
- [x] 所有点在圆上 (`verify_points_on_circle()`)
- [x] 角度关系正确 (`verify_angles()`)
- [x] 投影垂直 (`verify_projections()`)

### 边界约束 ✓
- [x] 单位圆在安全区内 (x ∈ [-1.8, 1.8], y ∈ [-0.3, 3.3])
- [x] 标题不超上边界 (y=6 < 7.5)
- [x] 公式不超下边界 (y=-6 > -7.5)

### LaTeX约束 ✓
- [x] 无中文在 MathTex 中
- [x] 使用原始字符串 r"..."
- [x] 度数使用 ^\circ 而非 °

### 动画节奏 ✓
- [x] 难点有足够停留 (1.5-2.0s)
- [x] 过渡流畅 (0.5-0.8s)
- [x] 总时长合理 (~68s)

---

## 💡 教学要点

### 核心概念
1. **二倍角公式** - 从两角和公式推导
2. **半角公式** - 通过替换从二倍角得出
3. **降幂公式** - 半角公式的逆向应用
4. **公式之间的联系** - 强调三者的内在逻辑

### 视觉化策略
1. 用单位圆建立直观认识
2. 颜色区分不同类型公式 (红-二倍角, 绿-半角, 金-降幂)
3. 逐步推导而非直接给出
4. 最后汇总形成知识网络

### 难点处理
1. cos 2α 的三种形式 - 强调等价性
2. 半角公式的替换思路 - 明确指出替换规则
3. 降幂与半角的关系 - 展示互逆关系

---

## 🔧 代码实现建议

### 关键函数
```python
def setup_geometry(self):
    """统一初始化所有几何数据"""
    # 所有坐标计算在此完成
    
def verify_geometry(self):
    """验证几何计算正确性"""
    # 运行所有几何约束检查
    
def create_formula_card(self, formula_text, color):
    """创建统一风格的公式卡片"""
    # 左侧色标 + 公式文字
```

### 动画技巧
1. 使用 `TransformMatchingTex` 进行公式变换
2. 用 `Circumscribe` 强调重点公式
3. 用 `Indicate` 制作闪烁效果
4. 用 `VGroup.arrange` 整齐排列

---

## 📝 备注

1. **验证脚本**: 运行 `python3 verify_geometry.py` 确保几何正确
2. **预览命令**: `manim -pql double_angle_formulas.py DoubleAngleFormulas`
3. **高质量渲染**: `manim -qh double_angle_formulas.py DoubleAngleFormulas`
4. **调试建议**: 先确保单场景正确，再组合所有场景

---

**分镜脚本版本**: v1.0
**创建日期**: 2026-02-11
**适用代码**: double_angle_formulas.py