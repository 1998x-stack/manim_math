# 圆柱教学动画 - 分镜脚本

## 元信息
- 目标时长: ~55 秒
- 场景数量: 7 个
- 背景色: #1a1a2e (深夜蓝)
- 格式: TikTok 竖屏 1080×1920, 9×16 frame

## 颜色配置
```python
BG = "#1a1a2e"
C_CYL = "#4a90d9"       # 圆柱蓝
C_BASE = "#7ec8e3"      # 底面浅蓝
C_AXIS = "#f39c12"      # 轴橙色
C_HIGHLIGHT = "#f1c40f" # 黄色高亮
C_FORMULA = "#2ecc71"   # 公式绿
C_ACCENT = "#e74c3c"    # 强调红
```

## 几何参数
- CYL_R = 1.3 (圆柱半径)
- CYL_H = 2.6 (圆柱高度)
- Camera: phi=75°, theta=-45°
- Cylinder direction=UP (y轴为轴)
- 旋转动画: Surface(u_range=[0,theta], v_range=[0,1])

## 固定在frame的文本坐标
- 标题区: y=6.8
- 副标题区: y=6.0
- 作者区: y=7.2
- 底部说明: y=[-4.5, -5.5]
- 底部关注: y=-6.5

---

## Scene 1: 开场 (0-4s)
- 作者信息淡入 (顶部)
- "圆柱" 大标题 Write
- 副标题: "旋转体中的重要几何体"
- 3D圆柱 Create + 旋转1.5s
- 钩子问题: "你知道圆柱的公式怎么推?" FadeIn
- Wait 1s
- FadeOut all

## Scene 2: 定义 - 矩形旋转 (4-12s)
- 标题: "圆柱的定义"
- 在 xy 平面显示矩形 (x:0→r, y:-h/2→h/2)
- 显示旋转轴 (y轴, 橙色虚线)
- 说明: "以矩形一边为旋转轴"
- ValueTracker t: 0→2π
  - always_redraw Surface(r*cos(u), v*h-h/2, r*sin(u)), u_range=[0,t]
  - 移动边 always_redraw Line3D at angle t
- 动画3s旋转完成
- FadeOut矩形, FadeIn完整 Cylinder
- 说明: "旋转一周得到圆柱(旋转体)"

## Scene 3: 各部分标注 (12-19s)
- 标题: "圆柱的各部分"
- 3D 圆柱 (半透明)
- 虚线轴: y轴, 橙色
- 标注: 轴 (右侧)
- 高亮顶面圆: 底面
- 标注: 底面(圆) r=?
- 标注: 侧面
- r 线段: 顶圆半径
- h 线段: 高度
- Labels: MathTex r, h

## Scene 4: 侧面展开 (19-27s)
- 标题: "侧面展开图"
- 显示圆柱
- 说明: "将侧面展开..."
- Camera move to front 2D view
- FadeOut cylinder, FadeIn 展开矩形
- 矩形: width=5.5 (代表2πr), height proportional
- Brace 下方: "长 = 2πr"
- Brace 右方: "宽 = h"
- 公式: S_侧 = 2πrh 渐显

## Scene 5: 公式汇总 (27-40s)
- 标题: "圆柱公式"
- 小圆柱 3D 在左侧
- 右侧逐行显示公式:
  - 体积: V = πr²h (绿色)
  - 侧面积: S = 2πrh (蓝色)
  - 表面积: S = 2πr² + 2πrh (红色)
  - 化简: = 2πr(r+h)
- 每行间隔 0.5s

## Scene 6: 轴截面 (40-47s)
- 标题: "轴截面"
- 3D 圆柱 + 过轴切面 (黄色平面)
- Camera 转到侧面看截面
- FadeOut 3D, 显示2D 矩形截面
- Braces: 宽=2r, 高=h
- 公式: 轴截面面积 S = 2rh

## Scene 7: 片尾 (47-55s)
- 旋转的圆柱
- 公式汇总 (小字)
- 作者信息大字
- "关注我，获得更多数学技巧!"

## 元素生命周期
| 元素 | 创建 | 销毁 |
|------|------|------|
| author_info | Scene1 | Scene1 |
| opening_cyl | Scene1 | Scene1 |
| sweep_surface | Scene2 | Scene2 |
| parts_cyl | Scene3 | Scene3 |
| unfold_rect | Scene4 | Scene4 |
| formula_cyl | Scene5 | Scene5 |
| cross_cyl | Scene6 | Scene6 |
| outro_cyl | Scene7 | Scene7 |