# 全等三角形判定——ASA与AAS - 分镜脚本

## 元信息
- 目标时长: 75-90 秒
- 场景数量: 6 个
- 难度等级: 七年级

## 配色方案
```python
C_BG        = "#1a1a2e"
C_TRI1      = WHITE              # △ABC 白色
C_TRI2      = "#a8d8ea"          # △DEF 浅蓝色
C_ANGLE1    = "#e74c3c"          # 第一对等角 红色
C_ANGLE2    = "#3498db"          # 第二对等角 蓝色
C_SIDE      = "#f1c40f"          # 等边 金色
C_CONGRUENT = "#2ecc71"          # 全等结论 绿色
C_WRONG     = "#e74c3c"          # 反例 红色
C_HIGHLIGHT = "#f1c40f"          # 高亮金色
C_AUX       = "#95a5a6"          # 灰色辅助
```

## 几何设计
### 主三角形 △ABC（左侧，scalene）
```
A = (-2.3,  2.8, 0)
B = (-3.5,  0.5, 0)
C = (-0.5,  0.5, 0)
```
- ∠A ≈ 65.7°，∠B ≈ 62.5°，∠C ≈ 51.8°（scalene，三角不等）
- AB ≈ 2.60，AC ≈ 2.93，BC = 3.0

### 全等三角形 △DEF（右侧，平移 +4.4）
```
D = (2.1,  2.8, 0)
E = (0.9,  0.5, 0)
F = (3.9,  0.5, 0)
```
- 与 △ABC 完全全等，三边三角对应相等

## 角度方向预判（待 verify_geometry.py 确认）
- ∠A (vertex A, L(A,B)/L(A,C)): cross_z > 0 → other_angle=False
- ∠B (vertex B, L(B,A)/L(B,C)): cross_z < 0 → other_angle=True ⚠️
- ∠C (vertex C, L(C,A)/L(C,B)): cross_z > 0 → other_angle=False
- △DEF 方向与 △ABC 对应相同

---

## Scene 1: 开场钩子 (4秒)
**目的**: 钩住注意力，提问"怎么证明两个三角形全等？"

### 动画序列
1. 作者信息淡入顶部
2. 大标题"全等三角形的判定"
3. 两个相同形状三角形从左右飞入
4. 钩子问句："已知两角和一条边——能判定全等吗？"

---

## Scene 2: 回顾"全等"概念 (5秒)
**目的**: 快速回顾全等定义，引出判定方法

### 动画序列
1. 两个三角形叠合动画（Transform）
2. 文字："形状和大小完全相同 = 全等"
3. 符号：≌

---

## Scene 3: ASA 判定 (20秒)
**目的**: 角-边-角 = 两角夹一边

### 子场景
3a. 标出 ∠A = ∠D（红色角弧，标注）
3b. 标出 AB = DE（金色边，刻度）——"夹边"强调
3c. 标出 ∠B = ∠E（蓝色角弧，标注）
3d. 夹边说明：AB 在 ∠A 和 ∠B 之间
3e. 结论框：ASA → △ABC ≌ △DEF
3f. 图形叠合验证

---

## Scene 4: AAS 判定 (20秒)
**目的**: 角-角-边 = 两角及其中一角的对边

### 子场景
4a. 标出 ∠A = ∠D（红色）
4b. 标出 ∠B = ∠E（蓝色）
4c. 标出 BC = EF（金色）——"非夹边"，强调是 ∠A 的对边 BC
4d. 与 ASA 对比：边的位置不同！
4e. 结论框：AAS → △ABC ≌ △DEF
4f. 对比提示：BC 是 ∠A 的对边（而非 ∠A 和 ∠B 的夹边）

---

## Scene 5: AAA 反例 (12秒)
**目的**: 三角对应相等 ≠ 全等（只能相似！）

### 子场景
5a. 展示两个三角对应相等但大小不同的三角形
5b. 尝试叠合 → 无法重合（动画）
5c. 红色 ✗ 标注："三角对应相等 ≠ 全等"
5d. 结论："AAA 只能说明相似，不能判定全等"

---

## Scene 6: 总结 + 片尾 (8秒)
**目的**: 对比 ASA / AAS，引导关注

### 内容
- ASA：∠A=∠D, AB=DE（夹边）, ∠B=∠E → 全等
- AAS：∠A=∠D, ∠B=∠E, BC=EF（对边）→ 全等
- 区别记忆：夹 vs 对

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 |
|------|---------|---------|
| author_bar | Scene 1 | 保留→Outro |
| tri_ABC | Scene 1 | Scene 5 |
| tri_DEF | Scene 1 | Scene 5 |
| arc_A_red | Scene 3 | Scene 3 end |
| arc_D_red | Scene 3 | Scene 3 end |
| side_AB_gold | Scene 3 | Scene 3 end |
| arc_B_blue | Scene 3 | Scene 3 end |
| asa_rule_box | Scene 3 | Scene 3 end |
| arc_A2_red | Scene 4 | Scene 4 end |
| arc_B2_blue | Scene 4 | Scene 4 end |
| side_BC_gold | Scene 4 | Scene 4 end |
| aas_rule_box | Scene 4 | Scene 4 end |
| tri_big, tri_small | Scene 5 | Scene 5 end |