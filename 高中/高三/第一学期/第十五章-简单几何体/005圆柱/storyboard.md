# 圆柱 (Cylinder) - 动画分镜脚本

## 元信息
- 目标时长: ~45 秒
- 场景数量: 7 个
- 格式: TikTok 竖屏 1080×1920
- 难度等级: 高三

## 几何参数
```python
R = 1.0      # 底面半径（显示单位）
H = 2.5      # 高度（显示单位）
CIRC = 2*pi  # 底面周长 ≈ 6.283
UNROLL_W = 5.5   # 侧面展开图显示宽度（缩放后）
UNROLL_H = 5.5 * H / CIRC  # ≈ 2.19
```

## 颜色配置
```python
BG_COLOR   = "#1a1a2e"   # 深蓝背景
CYL_COLOR  = "#26a8d4"   # 青蓝 - 圆柱主体
CYL_STROKE = "#7ee8fa"   # 浅蓝 - 圆柱描边
ACCENT_R   = "#ff6b6b"   # 红色 - 半径 r 标注
ACCENT_G   = "#a8e063"   # 绿色 - 高度 h 标注
GOLD       = "#ffd700"   # 金色 - 标题/公式
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 底面周长 | 2πR | CIRC |
| 展开矩形宽 | CIRC (缩放) | UNROLL_W = 5.5 |
| 展开矩形高 | H × (5.5/CIRC) | UNROLL_H |
| 圆柱体积 | πR²H = 2.5π | V_formula |
| 侧面积 | 2πRH = 5π | S_side |
| 全面积 | 2πR(R+H) = 7π | S_total |

---

## Scene 1: 开场 (5s)
**目的**: 视觉钩子 + 引出圆柱

### 元素
1. 作者信息 (top, fixed_frame)
2. 大标题 "圆 柱" (GOLD)
3. 旋转的3D圆柱

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | FadeIn author |
| 0.4s | Write 大标题 |
| 1.0s | 小副标题 hook 问题 |
| 1.8s | Create 3D cylinder |
| 2.5s | begin_ambient_rotation (rate=0.3) |
| 4.5s | stop rotation, FadeOut hook |

---

## Scene 2: 旋转体生成 (6s)
**目的**: 展示矩形旋转→圆柱

### 元素
1. 2D固定帧: 旋转轴线 + 矩形 + 旋转箭头
2. 说明文字: "矩形绕轴旋转一周"
3. 圆柱 FadeIn

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 标题变换 |
| 0.5s | 画旋转轴 (DashedLine) |
| 1.0s | 画矩形 (右侧) |
| 1.8s | 显示旋转箭头 + 说明 |
| 2.5s | 矩形 FadeOut + 圆柱 FadeIn |
| 3.5s | "旋转体 = 圆柱" 文字 |
| 5.0s | 清理 |

---

## Scene 3: 尺寸标注 (5s)
**目的**: 标注 r 和 h

### 元素
1. 3D圆柱 (中心)
2. 半径线 r (红色, 顶面)
3. 高度线 h (绿色, 右侧)
4. 说明: "底面半径 r, 高 h"

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 圆柱已在场景 |
| 0.5s | Create 半径线 r → Write label |
| 1.2s | Create 高度线 h → Write label |
| 2.0s | FadeIn 说明文字 |
| 4.0s | wait, 清理标注 |

---

## Scene 4: 侧面展开 (7s)
**目的**: 侧面展开图是矩形

### 元素
1. 圆柱 (fade out)
2. 展开矩形 (fixed_frame, 2D)
3. 宽度标注: 2πr
4. 高度标注: h
5. 公式: S侧 = 2πrh

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 标题"侧面展开图" |
| 0.5s | 说明"将侧面剪开展平..." |
| 1.0s | FadeOut cylinder |
| 1.5s | move_camera to front view |
| 2.0s | Create unrolled rectangle |
| 3.0s | DoublArrow width=2πr + label |
| 3.8s | DoubleArrow height=h + label |
| 4.5s | FadeIn 公式 S=2πrh |
| 6.5s | wait, 清理 |

---

## Scene 5: 公式汇总 (7s)
**目的**: 展示体积、侧面积、全面积公式

### 元素
1. 缩小的3D圆柱 (左上角参考)
2. 三个公式卡片 (fixed_frame)

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 标题"圆柱的公式" |
| 0.5s | FadeIn 小圆柱 |
| 1.0s | 公式1 滑入: V = πr²h |
| 2.2s | 公式2 滑入: S侧 = 2πrh |
| 3.4s | 公式3 滑入: S = 2πr(r+h) |
| 4.5s | 全部公式高亮 |
| 6.5s | 清理 |

---

## Scene 6: 截面 (5s)
**目的**: 平行截面(圆) + 轴截面(矩形)

### 元素
1. 3D圆柱
2. 平行截面: Circle (蓝色)
3. 轴截面: Rectangle (绿色, 宽2r, 高h)

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 标题"圆柱的截面" |
| 0.5s | FadeIn 圆柱 |
| 1.0s | 平行截面 Create + 说明 |
| 2.5s | FadeOut 截面 |
| 3.0s | 轴截面 Create + 说明 + 公式 S=2rh |
| 5.0s | 清理 |

---

## Scene 7: 片尾 (4s)
**目的**: 品牌 + CTA

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 旋转圆柱 + 公式总结 |
| 1.5s | "关注我，获得更多数学技巧！" |
| 3.5s | final wait |

---

## 元素生命周期追踪
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_text | Scene 1 | Scene 7 | 顶部固定 |
| main_title | Scene 1 | Scene 7 | 随场景变化 |
| cyl_main | Scene 1 | Scene 1 | 开场后清理 |
| cyl_dims | Scene 3 | Scene 3 | 标注用 |
| unrolled_rect | Scene 4 | Scene 4 | 固定帧 |
| formula_cards | Scene 5 | Scene 5 | 固定帧 |
| cyl_cross | Scene 6 | Scene 6 | 截面演示 |
| cyl_outro | Scene 7 | Scene 7 | 片尾旋转 |