# 平行线的判定 — 动画分镜脚本

## 元信息
- 目标时长: ~55 秒
- 场景数量: 7 个
- 难度等级: 七年级初中
- 格式: TikTok竖屏 1080×1920

---

## 颜色配置
```python
BG_COLOR       = "#1a1a2e"
C_LINE1        = "#3498db"   # 蓝 — 直线 l
C_LINE2        = "#2ecc71"   # 绿 — 直线 m
C_TRANS        = "#e74c3c"   # 红 — 截线 t
C_ANGLE_YELLOW = "#f1c40f"   # 黄 — 第一个角
C_ANGLE_CYAN   = "#1abc9c"   # 青 — 第二个角
GOLD           = "#f39c12"
GRAY_A         = "#bdc3c7"
```

---

## 几何预计算清单

| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 截线角度 | arctan(2) ≈ 63.43° | `self.ta` |
| 截线方向向量 | (cos(ta), sin(ta), 0) | `self.td` |
| 上交点 P | 截线∩l1 | `self.P` |
| 下交点 Q | 截线∩l2 | `self.Q` |
| 同位角扇形(P) | start=0, angle=ta | ∠1 上右 |
| 同位角扇形(Q) | start=0, angle=ta | ∠5 上右 |
| 内错角扇形(P) | start=π, angle=ta | ∠3 下左 |
| 内错角扇形(Q) | start=0, angle=ta | ∠5 上右 |
| 同旁内角扇形(P) | start=π+ta, angle=π-ta | ∠4 下右 |
| 同旁内角扇形(Q) | start=0, angle=ta | ∠5 上右 |

角度数值验证:
- ta ≈ 63.43°
- π-ta ≈ 116.57°
- ∠1=∠3=∠5=∠7 = ta (相等角)
- ∠2=∠4=∠6=∠8 = π-ta (补角)
- 同旁内角 ∠4+∠5 = (π-ta)+ta = π ✓

---

## Scene 1: 开场钩子 (0–3s)
**目的**: 抓住注意力，引出核心问题

### 元素
- 作者标识 (顶部)
- 大字问题钩子
- 副标题

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 作者信息淡入 |
| 0.3s | 钩子文字 Write |
| 1.1s | 副标题 FadeIn |
| 1.8s | 等待 0.8s |
| 2.6s | FadeOut 钩子+副标题 |

### 清理
- FadeOut: hook_text, sub_text
- 保留: author_info

---

## Scene 2: 建立三线八角图示 (3–8s)
**目的**: 建立视觉基础

### 元素
- 蓝线 l (上)
- 绿线 m (下)
- 红截线 t
- 交点 P, Q (白色小圆点)
- 说明文字

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 标题"三线八角" Write |
| 0.6s | Create l1, 写标签 |
| 1.3s | Create l2, 写标签 |
| 2.0s | Create t, 写标签 |
| 2.7s | FadeIn P, Q 点 |
| 3.2s | 说明文字 FadeIn |
| 4.0s | 等待 0.8s |
| 4.8s | FadeOut 标题和说明 (保留图示) |

### 清理
- FadeOut: scene_title, explain
- 保留: self.diagram (l1, l2, t, labels, dots)

---

## Scene 3: 同位角相等 (8–19s)
**目的**: 展示判定方法一

### 元素
- 黄色扇形 at P (上右 ∠1)
- 青色扇形 at Q (上右 ∠5)
- 角标签 ∠1, ∠5
- 说明文字
- 结论框

### 关键角度
- ∠1 at P: start=0, angle=ta (上右扇形)
- ∠5 at Q: start=0, angle=ta (上右扇形，位置相同)
- 两角相同位置 → 同位角

### 动画序列
| 时间 | 动作 |
|------|------|
| 0.0s | 标题"方法一：同位角相等" Write |
| 0.6s | 角扇形P + arc + label FadeIn/Create |
| 1.2s | 角扇形Q + arc + label FadeIn/Create |
| 1.8s | 说明文字"位置相同 → 同位角" |
| 2.8s | FadeOut说明 |
| 3.0s | 两角变同色 (闪烁强调) |
| 3.5s | 结论框 Write |
| 4.5s | 等待 1.5s |
| 6.0s | FadeOut all |

---

## Scene 4: 内错角相等 (19–30s)
**目的**: 展示判定方法二

### 关键角度
- ∠3 at P: start=π, angle=ta (下左扇形，在两线间)
- ∠5 at Q: start=0, angle=ta (上右扇形，在两线间)
- 位于截线两侧，在两线内侧 → 内错角

---

## Scene 5: 同旁内角互补 (30–41s)
**目的**: 展示判定方法三

### 关键角度
- ∠4 at P: start=π+ta, angle=π-ta (下右扇形，大角)
- ∠5 at Q: start=0, angle=ta (上右扇形，小角)
- 同侧 (右侧)，和为180° → 同旁内角互补

---

## Scene 6: 总结 (41–51s)
**目的**: 汇总三种方法

### 三张卡片（从上到下依次出现）
1. 黄色: 同位角相等 ⟹ 两直线平行
2. 绿色: 内错角相等 ⟹ 两直线平行
3. 橙色: 同旁内角互补 ⟹ 两直线平行

### 记忆口诀
"等等补，线平行！"

---

## Scene 7: 片尾 (51–55s)
**目的**: 作者信息 + 关注引导

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 顶部常驻 |
| self.diagram | Scene 2 | Scene 6 | 三线八角主图 |
| angle_sectors | 各角场景 | 同场景末 | 临时高亮 |
| title_per_scene | 各场景开头 | 各场景末 | 临时 |
| summary_cards | Scene 6 | Scene 6 | 临时 |