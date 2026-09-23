# 第十八章 005 数据的离散程度 · 数学规格与可验收分镜

## 教学数据与定义
- `A=(3,4,5,6,7)`、`B=(1,2,5,8,9)`，各五个值，均值均为5。全片的数轴、标签、公式和比较均源于 `data_dispersion_math.py` 中这两组固定教学数据。
- 极差 A=7−3=4、B=9−1=8；以均值5为中心的偏差平方和 A=10、B=50。本课使用**描述性方差** `v=(1/n)Σ(x_i−x̄)^2`，所以 `v_A=2,v_B=10`；`σ_A=√2≈1.41, σ_B=√10≈3.16`。
- 若将五个观察值视为样本，用于无偏估计总体方差，在通常独立同分布、有限方差条件下使用 `(1/(n−1))Σ(x_i−x̄)^2`，此例对应5/2、25/2；不得将两种分母或数值无提示混用。
- 本课变异系数为 `CV=σ/|x̄|`，A≈28.3%、B≈63.2%，仅在均值非零且变量尺度适合时讨论；均值为0时不定义。本例两组同均值同单位，不以变异系数推断不同量纲数据自动可比。

## 逐镜数学命题 → 可见对象 → 检查
| 场景 | learning_fact | observable_state | check | render_frame |
|---|---|---|---|---|
| 1 开场 | 同均值5但分散程度不同 | A/B两条数轴和各自五个真实值、相同均值线 | `test_two_sets_have_same_mean` | 五点与数值对应、标题不重叠 |
| 2 极差 | A两端3/7给4；B两端1/9给8 | 两组的端点连线、正确公式 | `test_data_range_values` | 端点和连线确实覆盖正确值 |
| 3 描述性方差 | 用n=5分母，平方偏差和10、50 | 同两组数轴，2和10的完整算式、n分母说明 | `test_descriptive_variances_and_squared_deviations` 与n−1对照测试 | 数据五点/分子分母一致 |
| 4 标准差 | √2与√10为同组方差的非负平方根 | √公式与1.41/3.16近似值 | `test_standard_deviation_values` | 近似号与单位说明可读 |
| 5 变异系数 | 均值非零时可计算，n−1对应不同统计目的 | 28.3%/63.2%与分母区别 | `test_cv_uses_common_positive_mean`、零均值/零方差边界 | 不将CV误写为对零均值可算 |
| 6 片尾 | 区分极差、描述性方差、标准差 | 各对应公式与注意事项 | 数学回归与前五镜一致 | 末帧安全区 |

## 分层验收
1. `python -m py_compile data_dispersion.py data_dispersion_math.py test_data_dispersion_math.py`。
2. `python -m unittest -v test_data_dispersion_math.py`；用 `.opencode/skills/manim-video-production/scripts/audit_scene.py` 审计脚本并逐条评估 WARN。
3. 具备 Manim、中文字体及TeX后运行 `manim -pql data_dispersion.py DataDispersion`；逐镜检查实际点位/端点/均值线、公式编译、9:16屏幕包围盒与对象生命周期。
4. 真实新视频、关键帧、ffprobe和音轨仍待验收；原MP4、音轨保留，静态/纯数学测试不等于画面通过。
