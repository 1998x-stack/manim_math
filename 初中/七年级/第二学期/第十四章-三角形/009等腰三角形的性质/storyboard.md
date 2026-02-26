# 等腰三角形的性质 - 动画分镜脚本

## 元信息
- 目标时长: 70-85 秒
- 场景数量: 7 个
- 难度等级: 初中 七年级

## 颜色配置
```python
BG_COLOR      = "#1a1a2e"
COLOR_TRIANGLE = WHITE
COLOR_WAIST   = "#e74c3c"   # 红色 - 腰（等边）
COLOR_BASE    = "#f39c12"   # 橙色 - 底边
COLOR_ANGLE   = "#3498db"   # 蓝色 - 等角
COLOR_MEDIAN  = "#2ecc71"   # 绿色 - 中线
COLOR_ALTITUDE= "#9b59b6"   # 紫色 - 高线
COLOR_BISECT  = "#e67e22"   # 橙色 - 角平分线
COLOR_AXIS    = "#1abc9c"   # 青色 - 对称轴
COLOR_HIGHLIGHT="#f1c40f"   # 金色 - 高亮
COLOR_AUX     = "#95a5a6"   # 灰色 - 辅助
COLOR_SUCCESS = "#2ecc71"   # 绿色 - 成功
```

## 关键几何设计
- 等腰三角形：A(顶角，顶部中央)，B(左下)，C(右下)
- AB = AC（腰），BC为底边
- M = (B+C)/2 = 底边中点
- AM 同时是：底边上的中线、高线、顶角平分线
- 对称轴：直线AM（即底边垂直平分线）

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点A | 固定坐标 | self.A |
| 顶点B | 固定坐标左下 | self.B |
| 顶点C | 固定坐标右下 | self.C |
| 底边中点M | (B+C)/2 | self.M |
| AB=AC边长 | linalg.norm | self.AB_len |
| ∠B, ∠C角度 | arccos | self.angle_B, self.angle_C |
| ∠BAM, ∠CAM | 检验三线合一 | self.angle_BAM, self.angle_CAM |
| AM垂直BC | 点积=0检验 | 验证 |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 展示等腰三角形，引出"神奇性质"

### 动画序列
- 作者信息淡入顶部
- 章节标题
- "等腰三角形有哪些神奇性质？"
- 绘制等腰三角形 + 刻度标记腰相等

---

## Scene 2: 性质一 - 等边对等角 (12-15秒)
**目的**: AB=AC → ∠B=∠C

### 动画序列
1. 标注腰 AB=AC（红色高亮+刻度）
2. 创建角弧 ∠B 和 ∠C（蓝色）
3. 两角弧动画对比"叠合"效果
4. 公式出现：AB=AC → ∠B=∠C
5. 规则总结框

---

## Scene 3: 性质二 - 三线合一 (20-25秒)
**目的**: 底边中线=高线=顶角平分线

### 子场景序列
3a. 先画底边中线 AM（M是BC中点）
3b. 再画高线（从A做BC的垂线）→ 发现落在同一点M
3c. 再画顶角平分线 → 发现也是AM
3d. 三线合并动画："三线合一！"

---

## Scene 4: 性质三 - 轴对称 (12-15秒)
**目的**: 等腰三角形关于底边垂直平分线对称

### 动画序列
1. 绘制对称轴（AM延长线）
2. 标注对称轴
3. "折叠"效果：B沿对称轴映射到C（用Transform）
4. 强调"轴对称图形"

---

## Scene 5: 综合性质展示 (8-10秒)
**目的**: 三种性质同时显示

---

## Scene 6: 总结 + 片尾 (6-8秒)
**目的**: 总结三大性质，引导关注

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 |
|------|---------|---------|
| author_bar | Scene 1 | 保留→Outro |
| main_triangle | Scene 1 | Scene 6 end |
| waist_AB/AC | Scene 2 | Scene 2 end |
| angle_arcs | Scene 2 | Scene 2 end |
| median_AM | Scene 3 | Scene 3 end |
| altitude_AM | Scene 3 | Scene 3 end |
| bisector_AM | Scene 3 | Scene 3 end |
| axis_line | Scene 4 | Scene 4 end |

## 角度方向注意事项（来自几何验证）
- ∠B (顶点B, 从A到C): 叉积为负 → other_angle=True ⚠️
- ∠C (顶点C, 从A到B): 叉积为正 → other_angle=False
- ∠BAM (顶点A, 从B到M): 需验证
- ∠CAM (顶点A, 从C到M): 需验证