# 直线的倾斜角与斜率 - 动画分镜脚本

## 元信息
- 目标时长: 80 秒
- 场景数量: 7 个
- 难度等级: 高中
- 核心示例: 过A(1,1)和B(3,3)的直线，斜率k=1

## 颜色配置
```python
BG_COLOR = "#1a1a2e"
COLOR_LINE1 = "#e74c3c"    # 红色 - k>0 直线
COLOR_LINE2 = "#3498db"    # 蓝色 - k<0 直线
COLOR_LINE3 = "#2ecc71"    # 绿色 - k=0
COLOR_LINE4 = "#9b59b6"    # 紫色 - 无斜率
COLOR_ANGLE = "#f39c12"    # 橙色 - 倾斜角弧
COLOR_XAXIS = WHITE
COLOR_AUX = GRAY_B
HL = YELLOW
```

## 几何预计算清单
| 元素 | 计算方式 | 存储变量 |
|------|---------|---------|
| x轴方向向量 | np.array([1,0,0]) | self.x_dir |
| 直线方向向量 | 由两点计算 | self.line_dir |
| 倾斜角 | arctan2(dy, dx) | self.alpha |
| 斜率 | tan(alpha) | self.slope_k |
| 两点坐标 | 精确定义 | self.pt_A, self.pt_B |

## 场景规划

### Scene 1: 开场钩子 (0-4s)
- 问题钩子: 直线有多"斜"?
- 倾斜角示意图快速展示
- 作者信息

### Scene 2: 倾斜角定义 (4-15s)
- 建立坐标系
- 一条直线 (45°倾斜) 缓慢出现
- 标注倾斜角 α
- 强调: α ∈ [0°, 180°)
- x轴正方向→直线向上方向

### Scene 3: 斜率 k = tan α (15-28s)
- 展示 k = tan α 公式
- 三种情况:
  a. α=45°, k=1
  b. α=135°, k=-1  
  c. α=0°, k=0
- 垂直直线: α=90°, 斜率不存在

### Scene 4: 两点公式 (28-46s)
- 具体例子: A(1,1), B(3,3)
- 展示 k = (y₂-y₁)/(x₂-x₁) = (3-1)/(3-1) = 1
- 动画高亮分子分母
- 强调 x₁≠x₂

### Scene 5: 四种直线类型 (46-62s)
- 同一图上展示四条直线
- k>0: 左下到右上 (锐角)
- k<0: 左上到右下 (钝角)
- k=0: 水平
- 无斜率: 垂直
- 颜色对应标注

### Scene 6: 总结口诀 (62-70s)
- 公式卡片汇总
- 核心要点

### Scene 7: 片尾 (70-80s)
- 作者信息放大
- 关注提示

---

## 关键几何约束
- 倾斜角 α 始终在 [0, π) 范围内
- 角弧从x轴正方向逆时针测量
- 使用 Arc(start_angle=0, angle=alpha) 直接绘制
- 避免使用 Angle.from_three_points (容易出现方向bug)

## 元素生命周期
| 元素 | 创建 | 销毁 |
|------|------|------|
| author_bar | Scene 1 | 最后 |
| axes (主坐标系) | Scene 2 | Scene 4 end |
| line_demo | Scene 2 | Scene 3 end |
| alpha_arc | Scene 2 | Scene 3 end |