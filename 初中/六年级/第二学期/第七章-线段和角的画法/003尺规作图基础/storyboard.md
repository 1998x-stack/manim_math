# 尺规作图基础 - 动画分镜脚本

<!-- /root/code/sss/media/videos/compass_straightedge/1920p60/CompassStraightedge.mp4 -->

## 元信息
- 目标时长: 60-75秒
- 场景数量: 7个
- 难度等级: 入门
- 目标观众: 六年级学生

## 颜色配置
```python
COLOR_RULER = "#3498db"           # 蓝色 - 直尺
COLOR_COMPASS = "#e74c3c"         # 红色 - 圆规
COLOR_CONSTRUCTION = "#2ecc71"    # 绿色 - 作图痕迹
COLOR_RESULT = "#f39c12"          # 橙色 - 最终结果
COLOR_HIGHLIGHT = YELLOW          # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B          # 灰色 - 辅助线
COLOR_BACKGROUND = "#1a1a2e"      # 深蓝背景
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 线段AB起点 | 固定坐标 | self.A_seg |
| 线段AB终点 | 固定坐标 | self.B_seg |
| 角顶点 | 固定坐标 | self.O_angle |
| 角的两边端点 | 固定坐标 | self.P1_angle, self.P2_angle |
| 线段中点 | (A+B)/2 | self.M |
| 弧线交点1 | 圆交点 | self.I1 |
| 弧线交点2 | 圆交点 | self.I2 |
| 角平分线终点 | 单位向量计算 | self.bisector_end |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出尺规作图概念

### 元素
1. 作者标识 (顶部)
2. 钩子问题大字
3. 直尺和圆规图标

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` "只用直尺和圆规，能画出什么？" |
| 1.5s | 直尺图标滑入 | `FadeIn(ruler_icon, shift=RIGHT)` |
| 2.0s | 圆规图标滑入 | `FadeIn(compass_icon, shift=LEFT)` |
| 3.0s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_text, ruler_icon, compass_icon
- 保留: author_info

---

## Scene 2: 什么是尺规作图 (6-8秒)
**目的**: 介绍尺规作图的定义和规则

### 元素
1. 标题 "尺规作图"
2. 定义文字
3. 两条规则提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题写入 | `Write(title)` |
| 0.8s | 定义文字淡入 | `FadeIn(definition)` |
| 1.8s | 规则1淡入 | `FadeIn(rule1)` "直尺：无刻度，只能连线" |
| 2.8s | 规则2淡入 | `FadeIn(rule2)` "圆规：可以画圆和弧" |
| 4.5s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: 全部元素
- 保留: author_info

---

## Scene 3: 作图1 - 作一条线段等于已知线段 (12-15秒)
**目的**: 演示第一个基本作图

### 几何计算
```python
# 已知线段AB
self.A_seg = np.array([-2.5, 2.0, 0])
self.B_seg = np.array([1.5, 2.0, 0])
self.seg_length = np.linalg.norm(self.B_seg - self.A_seg)

# 新线段起点
self.C_seg = np.array([-3.0, -1.0, 0])
# 新线段终点（待作图确定）
self.D_seg = self.C_seg + np.array([self.seg_length, 0, 0])
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` "作一条线段等于已知线段" |
| 0.8s | 已知线段AB出现 | `Create(segment_AB)` |
| 1.5s | 标记端点A、B | `FadeIn(dots_AB, labels_AB)` |
| 2.5s | 说明文字 | `FadeIn(explain)` "已知：线段AB" |
| 3.5s | 新点C出现 | `FadeIn(point_C)` |
| 4.0s | 说明 | `FadeIn(explain2)` "作法：取点C" |
| 5.0s | 圆规张开到AB长度 | `Create(compass_opening)` |
| 6.0s | 圆规中心移到C | `compass.animate.move_to(C)` |
| 7.0s | 以C为圆心画弧 | `Create(arc)` |
| 8.5s | 在弧上取点D | `FadeIn(point_D)` |
| 9.0s | 连接CD | `Create(segment_CD)` |
| 10.0s | 标注CD=AB | `FadeIn(result_text)` "CD = AB" |
| 11.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有元素（除author_info）

---

## Scene 4: 作图2 - 作一个角等于已知角 (15-18秒)
**目的**: 演示作角的方法

### 几何计算
```python
# 已知角∠AOB
self.O_angle = np.array([-1.5, 2.5, 0])
self.P1_angle = self.O_angle + np.array([2.0, 0, 0])
self.P2_angle = self.O_angle + np.array([1.5, 1.5, 0])

# 圆弧半径
self.r1 = 1.0

# 交点计算
self.I1 = self.O_angle + np.array([self.r1, 0, 0])
self.I2 = self.O_angle + self.r1 * normalize(self.P2_angle - self.O_angle)

# 两交点距离
self.chord_length = np.linalg.norm(self.I2 - self.I1)

# 新角顶点
self.O_new = np.array([-2.0, -2.0, 0])
self.P1_new = self.O_new + np.array([2.0, 0, 0])
# I1_new, I2_new 通过作图确定
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` "作一个角等于已知角" |
| 0.8s | 已知角出现 | `Create(angle_rays)` |
| 1.5s | 标记∠AOB | `FadeIn(angle_label)` |
| 2.5s | 以O为圆心画弧 | `Create(arc1)` |
| 3.5s | 弧与两边交于M、N | `FadeIn(points_MN)` |
| 4.5s | 测量MN距离 | `Create(dashed_MN)` |
| 5.5s | 新射线O'A'出现 | `Create(new_ray)` |
| 6.5s | 以O'为圆心画同样的弧 | `Create(arc2)` |
| 7.5s | 得到交点M' | `FadeIn(point_M_new)` |
| 8.5s | 以M'为圆心，MN为半径画弧 | `Create(arc3)` |
| 9.5s | 两弧交于N' | `FadeIn(point_N_new)` |
| 10.5s | 连接O'N' | `Create(ray_ON_new)` |
| 11.5s | 标注结果 | `FadeIn(result)` "∠A'O'N' = ∠AOB" |
| 13.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: 所有元素（除author_info）

---

## Scene 5: 作图3 - 作线段的中点 (10-12秒)
**目的**: 演示用圆规找中点的方法

### 几何计算
```python
# 线段AB
self.A_mid = np.array([-2.5, 1.5, 0])
self.B_mid = np.array([2.5, 1.5, 0])
self.M = (self.A_mid + self.B_mid) / 2

# 圆弧半径（大于AB的一半）
self.AB_length = np.linalg.norm(self.B_mid - self.A_mid)
self.r_mid = self.AB_length * 0.65

# 圆弧交点
# 以A为圆心，r为半径画弧（上下）
# 以B为圆心，r为半径画弧（上下）
# 两弧交点P、Q
dir_AB = normalize(self.B_mid - self.A_mid)
perpendicular = np.array([-dir_AB[1], dir_AB[0], 0])
h = np.sqrt(self.r_mid**2 - (self.AB_length/2)**2)
self.P = self.M + perpendicular * h
self.Q = self.M - perpendicular * h
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` "作线段的中点" |
| 0.8s | 线段AB出现 | `Create(segment)` |
| 1.5s | 标记A、B | `FadeIn(points_labels)` |
| 2.5s | 以A为圆心画弧（上下） | `Create(arc_A)` |
| 4.0s | 以B为圆心画弧（上下） | `Create(arc_B)` |
| 5.5s | 标记交点P、Q | `FadeIn(points_PQ)` |
| 6.5s | 连接PQ | `Create(line_PQ)` |
| 7.5s | 标记中点M | `FadeIn(point_M, flash)` |
| 8.5s | 验证AM=MB | `FadeIn(result)` |
| 9.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有元素（除author_info）

---

## Scene 6: 作图4 - 作角的平分线 (10-12秒)
**目的**: 演示角平分线作图

### 几何计算
```python
# 角∠AOB
self.O_bisect = np.array([0, 0.5, 0])
self.A_bisect = self.O_bisect + np.array([2.5, 1.5, 0])
self.B_bisect = self.O_bisect + np.array([2.5, -1.2, 0])

# 以O为圆心画弧，半径r
self.r_bisect = 1.8
vec_OA_unit = normalize(self.A_bisect - self.O_bisect)
vec_OB_unit = normalize(self.B_bisect - self.O_bisect)
self.M_bisect = self.O_bisect + vec_OA_unit * self.r_bisect
self.N_bisect = self.O_bisect + vec_OB_unit * self.r_bisect

# MN中垂线与OA、OB的关系
# 两弧交点P
self.r2 = np.linalg.norm(self.N_bisect - self.M_bisect) * 0.7
# 计算P（两圆交点）
bisector_dir = normalize(vec_OA_unit + vec_OB_unit)
self.P_bisect = self.O_bisect + bisector_dir * 3.0
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` "作角的平分线" |
| 0.8s | 角∠AOB出现 | `Create(angle)` |
| 1.5s | 以O为圆心画弧 | `Create(arc)` |
| 2.5s | 交两边于M、N | `FadeIn(points_MN)` |
| 3.5s | 以M为圆心画弧 | `Create(arc_M)` |
| 4.5s | 以N为圆心画弧（同半径） | `Create(arc_N)` |
| 5.5s | 两弧交于P | `FadeIn(point_P, flash)` |
| 6.5s | 连接OP | `Create(bisector)` |
| 7.5s | 标注 | `FadeIn(result)` "OP平分∠AOB" |
| 8.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有元素（除author_info）

---

## Scene 7: 总结与片尾 (8-10秒)
**目的**: 总结四个基本作图，引导关注

### 元素
1. 四个作图的图标总结
2. 关键提示
3. 关注引导

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` "四个基本尺规作图" |
| 1.0s | 四个小图标依次出现 | `FadeIn(icons, lag_ratio=0.2)` |
| 3.0s | 关键提示 | `FadeIn(hint)` "作图痕迹要保留！" |
| 4.5s | 作者信息放大 | `author.animate.scale(2).move_to(UP)` |
| 5.5s | 关注文字 | `Write(follow_text)` "关注我，学更多几何技巧！" |
| 7.0s | 装饰动画 | `Rotate(decorations)` |
| 8.5s | 淡出 | `FadeOut(all)` |

### 清理
- FadeOut: 全部元素

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 持续存在 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| ruler_icon | Scene 1 | Scene 1 | 直尺图标 |
| compass_icon | Scene 1 | Scene 1 | 圆规图标 |
| segment_AB | Scene 3 | Scene 3 | 已知线段 |
| arc | Scene 3-6 | Scene 3-6 | 各种圆弧 |
| result_text | Scene 3-6 | Scene 3-6 | 结果标注 |
| summary_icons | Scene 7 | Scene 7 | 总结图标 |

---

## 动画节奏说明

- **开场**: 快节奏（3秒），立即抓住注意力
- **定义**: 中等节奏（6秒），给学生理解时间
- **作图演示**: 慢节奏（每个10-15秒），详细展示步骤
  - 圆规画弧动画要流畅，用 `rate_func=smooth`
  - 交点出现时用闪光效果 `Flash()`
  - 关键步骤后等待1-2秒
- **总结**: 快节奏（8秒），简洁有力

## 技术要点

1. **圆弧绘制**: 使用 `Arc` 类，注意 `start_angle` 和 `angle`
2. **虚线**: 使用 `DashedLine(dash_length=0.1)`
3. **圆规动画**: 
   - 用 `VGroup` 组合圆规的各部分
   - 用 `Rotate` 和 `MoveTo` 模拟圆规运动
4. **交点高亮**: 用 `Flash(color=YELLOW, flash_radius=0.3)`
5. **保留作图痕迹**: 所有辅助线和弧都不要立即删除

## 预期总时长

Scene 1: 4秒
Scene 2: 7秒
Scene 3: 14秒
Scene 4: 16秒
Scene 5: 11秒
Scene 6: 11秒
Scene 7: 9秒

**总计: 约72秒**（符合TikTok短视频时长）