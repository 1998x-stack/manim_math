# 角的概念 - 动画分镜脚本

<!-- /root/code/sss/media/videos/angle_concept/1920p60/AngleConcept.mp4 -->

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 六年级基础
- 知识点: 角的定义、表示方法、度量单位

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要射线
COLOR_SECONDARY = "#e74c3c"    # 红色 - 次要射线
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_ARC = "#2ecc71"          # 绿色 - 角度弧
COLOR_VERTEX = "#f39c12"       # 橙色 - 顶点
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点O | ORIGIN | self.O |
| 射线OA端点 | O + 2.5*RIGHT | self.A |
| 射线OB端点 | O + 2.5*(cos60°, sin60°, 0) | self.B |
| 角度弧中心 | O | self.O |
| 角度弧半径 | 0.8 | self.arc_radius |
| 旋转角度 | 60° (PI/3) | self.angle_value |

---

## Scene 1: 开场钩子 (3秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题
3. 简单的角闪烁

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.3s | 简单角图形创建 | `Create(simple_angle)` |
| 2.3s | 角闪烁 | `Flash(angle_arc)` |

### 清理
- FadeOut: hook_text, simple_angle
- 保留: author_info

---

## Scene 2: 角的定义 (8-10秒)
**目的**: 讲解角的基本构成

### 元素
1. 标题 "角的定义"
2. 顶点O (橙色大点)
3. 两条射线 (蓝色、红色)
4. 文字说明

### 动画序列
| 时间 | 动作 | 说明 |
|------|------|------|
| 0.0s | 标题淡入 | 大标题 + 副标题 |
| 0.5s | 顶点出现 | 橙色点，带标签"O" |
| 1.0s | 第一条射线生长 | 从O点向右，带箭头 |
| 2.0s | 第二条射线生长 | 从O点旋转60度，带箭头 |
| 3.0s | 角度弧出现 | 绿色弧线连接两射线 |
| 3.5s | 说明文字淡入 | "两条射线，共同端点" |
| 5.5s | 标注"顶点"和"边" | 指示线标注 |

### 精确坐标计算
```python
self.O = ORIGIN + UP * 1.5  # 顶点位置
self.A = self.O + np.array([2.5, 0, 0])  # 右侧射线端点
angle_rad = PI / 3  # 60度
self.B = self.O + np.array([2.5 * np.cos(angle_rad), 2.5 * np.sin(angle_rad), 0])
```

### 清理
- FadeOut: 说明文字，部分标注
- 保留: 角的主体结构

---

## Scene 3: 角的表示方法 (8-10秒)
**目的**: 教学三种表示法

### 元素
1. 标题 "角的表示方法"
2. 已有的角 (从Scene 2)
3. 三种表示方法卡片

### 动画序列
| 时间 | 动作 | 说明 |
|------|------|------|
| 0.0s | 标题切换 | "角的表示方法" |
| 0.5s | 方法1出现 | ∠AOB (三个点) |
| 1.5s | 高亮顶点和边 | 闪烁效果 |
| 2.5s | 方法2出现 | ∠O (顶点) |
| 3.5s | 方法3出现 | ∠α (希腊字母) |
| 5.0s | 三种表示法汇总 | 并排显示 |

### LaTeX公式
```python
method1 = MathTex(r"\angle AOB")
method2 = MathTex(r"\angle O")
method3 = MathTex(r"\angle \alpha")
```

### 清理
- FadeOut: 标题，表示法卡片
- 保留: 角的主体

---

## Scene 4: 角的度量单位 (10-12秒)
**目的**: 介绍度分秒系统

### 元素
1. 标题 "角的度量"
2. 度、分、秒关系图
3. 换算公式

### 动画序列
| 时间 | 动作 | 说明 |
|------|------|------|
| 0.0s | 标题淡入 | "角的度量单位" |
| 0.5s | 度符号出现 | 1° |
| 1.5s | 分的关系 | 1° = 60' |
| 2.5s | 秒的关系 | 1' = 60" |
| 4.0s | 完整公式展示 | 1° = 60' = 3600" |
| 5.5s | 示例: 60° | 在原角上标注度数 |

### LaTeX公式
```python
degree_def = MathTex(r"1^\circ = 60'")
minute_def = MathTex(r"1' = 60''")
full_relation = MathTex(r"1^\circ = 60' = 3600''")
```

### 清理
- FadeOut: 公式，标题
- 保留: 标注了度数的角

---

## Scene 5: 角的旋转形成 (10-12秒)
**目的**: 动态展示角的形成过程

### 元素
1. 标题 "角的形成"
2. 固定射线
3. 旋转射线 (动画)
4. ValueTracker 控制旋转

### 动画序列
| 时间 | 动作 | 说明 |
|------|------|------|
| 0.0s | 标题淡入 | "角是旋转形成的" |
| 0.5s | 固定射线 | 水平射线 |
| 1.0s | 旋转开始 | 从0°旋转到60° |
| 3.5s | 角度实时显示 | 0° → 60° |
| 4.5s | 停留在60° | 最终角度 |
| 5.5s | 说明文字 | "射线绕端点旋转" |

### ValueTracker实现
```python
angle_tracker = ValueTracker(0)
rotating_ray = always_redraw(lambda: 
    Arrow(self.O, 
          self.O + 2.5 * np.array([np.cos(angle_tracker.get_value()), 
                                    np.sin(angle_tracker.get_value()), 0]),
          color=COLOR_SECONDARY)
)
self.play(angle_tracker.animate.set_value(PI/3), run_time=3)
```

### 清理
- FadeOut: 说明文字
- 保留: 形成的角

---

## Scene 6: 特殊角介绍 (10-12秒)
**目的**: 介绍周角和平角

### 元素
1. 标题 "特殊的角"
2. 周角示意图 (360°)
3. 平角示意图 (180°)

### 动画序列
| 时间 | 动作 | 说明 |
|------|------|------|
| 0.0s | 标题淡入 | "特殊的角" |
| 0.5s | 周角出现 | 完整圆 + 360° |
| 2.0s | 周角公式 | "周角 = 360°" |
| 3.5s | 平角出现 | 直线 + 180° |
| 5.0s | 平角公式 | "平角 = 180°" |
| 6.5s | 两者对比 | 并排显示 |

### 坐标计算
```python
# 周角 - 完整圆
full_circle = Circle(radius=1.2, color=COLOR_ARC).move_to(LEFT * 2 + UP * 2)

# 平角 - 直线加弧
straight_line = Line(LEFT * 1.5, RIGHT * 1.5, color=COLOR_PRIMARY)
half_arc = Arc(radius=0.5, angle=PI, color=COLOR_ARC)
```

### 清理
- FadeOut: 所有元素
- 准备结尾

---

## Scene 7: 片尾总结 (6-8秒)
**目的**: 总结关键点，引导关注

### 元素
1. 关键点列表
2. 作者信息放大
3. 关注提示
4. 装饰元素

### 动画序列
| 时间 | 动作 | 说明 |
|------|------|------|
| 0.0s | 关键点卡片滑入 | 4个要点 |
| 2.0s | 作者信息放大 | 从顶部到中心 |
| 3.0s | 关注提示 | "关注我，学更多数学!" |
| 4.0s | 装饰动画 | 小角度图标旋转 |
| 6.0s | 全部淡出 | 结束 |

### 关键点内容
```python
key_points = [
    "角 = 两条射线 + 公共端点",
    "表示: ∠AOB, ∠O, ∠α",
    "度量: 1° = 60' = 3600\"",
    "周角360°, 平角180°"
]
```

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保留顶部 |
| hook_text | Scene 1 | Scene 1 | 开场即清理 |
| main_angle | Scene 2 | Scene 6 | 主要角结构 |
| vertex_O | Scene 2 | Scene 6 | 顶点 |
| ray_OA | Scene 2 | Scene 6 | 射线1 |
| ray_OB | Scene 2 | Scene 6 | 射线2 |
| angle_arc | Scene 2 | Scene 6 | 角度弧 |
| title (各场景) | 当前场景 | 当前场景 | 标题切换 |
| explanation_text | 各场景 | 各场景 | 临时说明 |

---

## 技术注意事项

### 1. 字体处理
- 中文: `Text("角", font="Noto Sans CJK SC")`
- 数学: `MathTex(r"\angle AOB")`
- 度数符号: `MathTex(r"60^\circ")` 或 `Text("60°")`

### 2. 边界安全
- 主内容区: y ∈ [-3, 5]
- 顶部作者: y = 7
- 底部文字: y ∈ [-6, -4]

### 3. 动画节奏
- 简单元素: 0.5-1.0s
- 关键概念: 1.5-2.5s
- 理解停顿: 1.0-2.0s

### 4. 颜色一致性
- 保持整个视频颜色方案统一
- 顶点始终橙色
- 射线蓝红配色
- 角度弧绿色

---

## 验证清单
- [ ] 所有坐标在setup_geometry()计算
- [ ] 中文文本使用Text()
- [ ] 数学符号使用MathTex()
- [ ] 度数符号正确: `^\circ`
- [ ] 元素位置在安全边界内
- [ ] 动画节奏合理
- [ ] 元素生命周期清晰
- [ ] 颜色方案一致