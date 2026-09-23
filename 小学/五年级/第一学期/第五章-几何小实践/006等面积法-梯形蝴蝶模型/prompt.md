# 小学奥数｜等面积法 02：梯形蝴蝶模型

> 适用：小学五至六年级奥数；先修：梯形、三角形面积公式与比例（可辅以相似图形直观解释）。制作依据：仓库 `.claude/skills/manim-video-production/SKILL.md`。

## 数学规格与严格证明

在非退化凸梯形 ABCD 中，AB∥CD，A、B 在下底且按从左至右排列，D、C 在上底且按从左至右排列，两条对角线 AC 与 BD 交于梯形内部 O。四小三角形依次为底部 AOB、顶部 COD、左翼 AOD、右翼 BOC。

**等面积法核心**：△ABD 与 △ABC 共底 AB，而 D、C 位于平行于 AB 的同一直线上，所以面积相等。它们包含相同的 △ABO；分别减去 △ABO，严格得到 `S(AOD)=S(BOC)`。这与梯形是否左右对称无关。

**面积比例进阶**：设下底 b>0、上底 a>0、高 h>0。由 AB∥CD 和两条对角线交点可得 `AO:OC=BO:OD=b:a`；O 到下底、上底的垂直距离分别为 `hb/(a+b)`、`ha/(a+b)`。因此底部、顶部、左翼、右翼四块面积为 `hb²/[2(a+b)]`、`ha²/[2(a+b)]`、`hab/[2(a+b)]`、`hab/[2(a+b)]`。上/下两块面积比为 `a²:b²`，两个翅膀面积相等；底边不是平行、交点不在梯形内部或任一长度为零时，不得直接套用模型。

## 完整数值例题

下底 AB=6 cm，上底 CD=3 cm，高 h=4 cm。为可视化选取 A=(-3,-2)，B=(3,-2)，C=(1.5,2)，D=(-1.5,2)，交点 O=(0,2/3)。由 AO:OC=2:1 得 O 到下底高为 8/3 cm、到上底高为 4/3 cm。

- 底部 △AOB：`6×(8/3)÷2=8 cm²`。
- 顶部 △COD：`3×(4/3)÷2=2 cm²`。
- 整个 △ABD、△ABC：`6×4÷2=12 cm²`。
- 两翼：`S(AOD)=S(BOC)=12−8=4 cm²`。
- 核对梯形总面积：`2+4+4+8=18 cm²=(6+3)×4÷2`。

不要凭色块的视觉外形声称面积相等；必须同步显示共同底边、相等的高、公共部分以及最终减法。相似三角形比例是本课进阶先修，若听众尚未学习，允许教师先将交点到两底的距离作为已知数据，**但不得在未解释的情况下把面积 2、8 当作明显事实**。

## 视觉与制作约束

采用 9:16 深色画布；在中央画梯形及两条对角线，并按“上金、下蓝、左绿、右粉”标注四块。动画先呈现平行上下底和交点，再显示 `AO:OC=2:1`、顶部 2/底部 8、共有大三角形面积 12、等面积两翼各 4，最后汇总为 18 cm²。顶点字母必须对应真实交点，避免覆盖颜色数字或误把上下底画成不同的非平行线。

文件：`lesson.py` 中 `TrapezoidButterflyArea`、纯数学 `area_model.py`、专项回归 `test_area_model.py`、逐镜 `storyboard.md`。中文用 `Text`，公式用 `MathTex`；`area_model` 的数学函数不依赖 Manim。预览：`MANIM_PREVIEW=1 manim lesson.py TrapezoidButterflyArea`；正式渲染：`manim lesson.py TrapezoidButterflyArea`；语法：`python -m py_compile lesson.py area_model.py test_area_model.py`；数学回归：`python -m unittest discover -s . -p 'test_area_model.py'`。还需使用 Skill 审计工具、实际逐帧核验和 `ffprobe`；未经运行不声称已生成最终 MP4。
