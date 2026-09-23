# 杨辉三角形里有分形？｜数学规格与分镜

- audience：初中拓展／高中数学兴趣；先修：杨辉三角形、奇偶数、二项式系数可选。
- source：独立探索；制作依据 `.claude/skills/manim-video-production/SKILL.md`；不冒称任何教材章节。
- objective：用杨辉三角形逐层递推生成奇偶图案，观察 2 的幂次行数附近的自相似结构。
- format：9×16，1080×1920，深色；约 11–16 s，纯几何点阵无外部媒体。

## 数学规格

- claim：第 n 行（从 n=0 起）第 k 项为二项式系数 C(n,k)；内部数满足相邻两数求和。对各项模 2，奇数亮、偶数暗，会出现谢尔宾斯基式三角形图案。
- assumptions/domain：n≥0、0≤k≤n，边界项均为 1。第 0 行绘制在三角形顶端。
- justification：C(n,k)=C(n−1,k−1)+C(n−1,k)（仅内部 k），奇偶性等价于按模 2 的相加；镜头实际计算整数系数，不用手工伪造分形图案。
- counterexample/edge：前 32 行只是有限图像，不宣称已经“画出无限分形”；第 n=0 行无内部递推项；偶数点虽变暗但仍保留其位置，不可将“暗点”误读为二项式系数为 0。
- tests：`test_math.py::VisualMathTests.test_pascal_parity` 核验系数和、对称、相邻相加、2 的幂次相关行的奇偶规律。

## 分镜

| shot | learning_fact | 画面／对象状态 | 动画／约时 | check |
| --- | --- | --- | --- | --- |
| 01 | 奇偶着色规则来源于杨辉三角形递推 | title、lead、recurrence 创建并保持 | 文字与递推公式出现，约 2 s | 递推仅对内部项成立；边界项由数学规格明确说明 |
| 02 | 前 8 行已可看见三角形空洞 | 根据 `parity_row` 计算并创建第 0–7 行圆点，奇亮偶暗；stage 显示“前 8 行” | 自上而下淡入，约 2 s | 圆点数量 1+…+8，行列位置同数学数据 |
| 03 | 递归形状随着行数增加而更明显 | 保留已有行；新增第 8–15 行、第 16–31 行；同一 stage 对象用 `Transform` 更新 | 分两次展示至 16、32 行，约 4 s | 偶数点不消失，32 行底部宽度不越界 |
| 04 | 有限图案呈现自相似 | 创建解释字幕，其余对象保留 | 结语停留，约 2 s | 字幕使用“自相似”而非宣称有限图案具有无限细节 |

- layout：顶端字幕 y≈6.35/5.2，三角阵 y≈3.9 至 −2.7，底部递推 y≈−4.3、结论 y≈−5.65。
- verification：math、syntax、ast、unit_tests、frame_review、ffprobe 均 not_run；manim_render blocked（本次环境无 Manim）；audio_review not_run（无音轨）。
