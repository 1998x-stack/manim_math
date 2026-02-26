# 棱锥 Pyramid - TikTok 3D 动画分镜脚本

## 元信息
- 目标时长: ~70 秒
- 场景数量: 7 个
- 格式: TikTok 竖屏 1080×1920
- 类型: ThreeDScene（3D 动画）

## 配色方案
```python
BG_COLOR = "#1a1a2e"
BASE_COLOR = "#4ecdc4"      # 底面：青色
SIDE_COLOR_1 = "#ff6b6b"    # 侧面1：红色
SIDE_COLOR_2 = "#ffd93d"    # 侧面2：黄色
SIDE_COLOR_3 = "#6bcb77"    # 侧面3：绿色
SIDE_COLOR_4 = "#a29bfe"    # 侧面4：紫色
EDGE_COLOR = WHITE
APEX_COLOR = "#ffd93d"
HEIGHT_COLOR = "#74b9ff"
SLANT_COLOR = "#fd79a8"
LABEL_COLOR = WHITE
HIGHLIGHT = YELLOW
```

## 3D 几何预计算清单

| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 底面边长 | a = 2.4 | self.a |
| 棱锥高 | h = 2.0 | self.h |
| 底面面积 | S_base = a² | self.S_base |
| 斜高 | l = sqrt(h² + (a/2)²) | self.slant_h |
| 侧棱长 | e = sqrt(h² + (a/√2)²) | self.edge_len |
| 体积 | V = 1/3 * S * h | self.volume |
| 侧面积 | S_side = 1/2 * perimeter * l | self.S_side |

## 相机设置
```python
# 初始视角
phi_init = 65 * DEGREES
theta_init = -45 * DEGREES

# 主视角（展示棱锥）
phi_main = 70 * DEGREES
theta_main = -30 * DEGREES
```

---

## Scene 1: 开场钩子 (5秒)
**目的**: 震撼开场，引出棱锥

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 作者信息固定帧顶部 |
| 0.3s | 问题文字浮现："棱锥的秘密" |
| 1.0s | 3D正四棱锥从无到有生长出来 |
| 2.5s | 相机缓慢旋转一圈 |
| 4.0s | 相机定位到主视角 |

---

## Scene 2: 棱锥定义 (8秒)
**目的**: 明确棱锥定义，展示底面

### 动画序列
- 底面高亮闪烁
- 侧面依次出现
- 定义文字：底面是多边形，侧面是三角形，共享一个顶点

---

## Scene 3: 各部分标注 (15秒)
**目的**: 标注 顶点P、底面、侧面△PAB、侧棱PA、高、斜高

### 标注顺序
1. 顶点 P（顶点 = 公共顶点）
2. 底面 ABCD
3. 侧面（一个三角形高亮）
4. 侧棱 PA
5. 高 h（从P到底面的垂线）
6. 斜高 l（从P到底边中点）

---

## Scene 4: 正棱锥性质 (10秒)
**目的**: 正棱锥 = 底面正多边形 + 顶点在底面中心正上方

### 性质
- 侧棱相等
- 侧面是等腰三角形
- 斜高相等
- 顶点在底面中心正上方

---

## Scene 5: 体积公式 (15秒)
**目的**: V = ⅓ S底 × h，直观演示

### 关键动画
- 展示高 h
- 展示底面面积 S
- 公式推导：切割演示（类比棱柱 1/3）

---

## Scene 6: 表面积公式 (10秒)
**目的**: S = S底 + S侧 = S底 + ½ × 周长 × 斜高

---

## Scene 7: 片尾 (5秒)
**目的**: 关注提示

---

## 元素生命周期表

| 元素 | 创建 | 销毁 | 备注 |
|------|------|------|------|
| pyramid_base | Scene 1 | Scene 7 | 持续显示 |
| pyramid_edges | Scene 1 | Scene 7 | 持续显示 |
| pyramid_faces | Scene 1 | Scene 7 | 透明侧面 |
| height_line | Scene 3 | Scene 3 | 临时 |
| slant_line | Scene 3 | Scene 3 | 临时 |
| formula_vol | Scene 5 | Scene 6 | 固定帧 |