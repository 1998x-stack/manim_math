# 两直线的位置关系 - 动画分镜脚本

## 元信息
- 目标时长: ~75 秒
- 场景数量: 7 个
- 难度等级: 高二

## 颜色配置
```python
BG_COLOR = "#1a1a2e"
COLOR_L1 = "#e74c3c"       # 红色 - 直线l₁
COLOR_L2 = "#3498db"       # 蓝色 - 直线l₂
COLOR_PARALLEL = "#f39c12" # 橙色 - 平行标注
COLOR_INTERSECT = "#2ecc71" # 绿色 - 交点
COLOR_COINCIDE = "#9b59b6" # 紫色 - 重合
AXES_COLOR = GRAY_B
HIGHLIGHT = YELLOW
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 平行线交点 | 无交点 | None |
| 相交点 | 联立方程组 | self.intersection_pt |
| 直线端点 | x_range映射 | self.line_*_start/end |

---

## Scene 1: 开场钩子 (5秒)
**目的**: 吸引注意力 + 引出问题

### 元素
1. 作者标识 (顶部)
2. 标题文字
3. 三种情况的快闪预览

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 作者信息淡入 |
| 0.5s | 标题书写 |
| 1.5s | 问题引导文字 |
| 2.5s | 三对线快速展示 |
| 4.5s | 清理，进入正题 |

---

## Scene 2: 坐标系建立 (4秒)
**目的**: 建立基础坐标系，介绍两直线

### 元素
- Axes (坐标轴)
- 直线l₁: y = x + 2
- 直线l₂: y = x - 1

---

## Scene 3: 平行 (12秒)
**目的**: 展示平行条件 k₁=k₂, b₁≠b₂

### 关键点
- 同斜率 → 平行
- 用平行箭头标注
- 展示公式

---

## Scene 4: 重合 (10秒)
**目的**: 展示重合条件 k₁=k₂, b₁=b₂

### 关键点
- 完全相同的方程
- 高亮叠加效果

---

## Scene 5: 相交 (14秒)
**目的**: 展示相交条件 k₁≠k₂，计算交点

### 关键点
- l₁: y = x + 1, l₂: y = -x + 3
- 交点 (1, 2) 精确计算
- 联立方程组动画

---

## Scene 6: 总结公式 (12秒)
**目的**: 三种关系统一展示

---

## Scene 7: 片尾 (3秒)
**目的**: 作者信息 + 关注引导

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 |
|------|---------|---------|
| author_info | Scene 1 | Scene 7 |
| axes | Scene 2 | Scene 6 |
| line1_parallel | Scene 3 | Scene 3 |
| line2_parallel | Scene 3 | Scene 3 |
| line1_coincide | Scene 4 | Scene 4 |
| line1_intersect | Scene 5 | Scene 6 |
| line2_intersect | Scene 5 | Scene 6 |
| intersection_dot | Scene 5 | Scene 6 |