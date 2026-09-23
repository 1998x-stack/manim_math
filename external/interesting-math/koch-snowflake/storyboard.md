# 无限周长，有限面积？｜数学规格与分镜

- audience：高中数学拓展／极限兴趣；先修：正三角形、等比数列、面积与周长。
- source：独立探索；制作依据 `.claude/skills/manim-video-production/SKILL.md`；不指定教材版本。
- objective：区分图形边界长度与围成面积，理解它们可能分别趋于无穷和有限值。
- format：逻辑 9×16、1080×1920、深色；无外部图像和音轨；约 15–22 s。

## 数学规格

- claim：对边长为 s>0 的初始正三角形，P_n=3s(4/3)^n→∞。设初始面积 A_0，则 A_n/A_0=1+(1/3)Σ_{j=0}^{n−1}(4/9)^j→8/5。
- assumptions/domain：n≥0 为整数；每条有向边三等分并向原三角形外侧加凸起；原始顶点按逆时针排列；每次凸起不发生内部重叠。
- justification：每条旧边变成四条 1/3 长的新边；第 k 次新增 3·4^(k−1) 个边长 s/3^k 的正三角形，其面积合计为 A_0·(1/3)(4/9)^(k−1)。非负面积增量构成公比 4/9 的等比级数。
- counterexample/edge：n=0 时 A_0 不加额外面积；有限的 4 次迭代不等于无穷分形，极限由解析公式而非屏上像素数推出；s=0 时周长不发散，因此数学结论要求 s>0。
- tests：`test_math.py::VisualMathTests.test_koch_area_and_perimeter` 用独立的折线长度和鞋带公式计算前五级，比较数值与解析式；同时检查退化输入。

## 分镜

| shot | learning_fact | 画面对象与生命周期 | 动画／约时 | check |
| --- | --- | --- | --- | --- |
| 01 | 从边长为 s 的正三角形出发 | title、lead、snowflake、step、current 创建 | 描边并显示 P_0、A_0，约 3 s | 初始轮廓逆时针，向外凸起约定明确 |
| 02 | 每一步新周长是旧周长的 4/3 | `koch_step` 输出下一轮顶点；同一 snowflake、step、current 分别用 `Transform` 更新，保留对象身份 | 迭代 n=1…4，约 9 s | 3·4^n 段；标签中的 n、面积近似与当前图形一致 |
| 03 | 趋于无限的周长不妨碍面积收敛 | 创建 result，保留当前第 4 轮轮廓 | 写出 P_n→∞、A_n→8A_0/5，约 3 s | 将可见的 4 轮样本和数学极限区分；不声称四轮已是无限周长 |

- layout：雪花位于 y≈0.35 附近，文字 y≈6.4/5.3/−3.5/−4.55/−6，动态外扩需抽帧检查。
- verification：math、syntax、ast、unit_tests、frame_review、ffprobe 均 not_run；manim_render blocked（本次环境无 Manim）；audio_review not_run（无音轨）。
