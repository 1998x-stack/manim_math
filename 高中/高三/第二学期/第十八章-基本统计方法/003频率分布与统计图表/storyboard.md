# 第十八章 003 频率分布与统计图表 · 数据驱动分镜

## 数据规范
- `frequency_distribution_math.SCORES` 是教学设定的**同一组40个**成绩；分组边界为50、60、70、80、90、100，各组均左闭右开，包括最后一组 `[90,100)`。全部样本都在50到100之间，分组计数必须由原始值生成，不可另写互不一致的柱高。
- 频数 `[3,8,14,10,5]`，总量40。每组频率 `f_i=n_i/40`；密度/柱高 `h_i=f_i/d_i`，本例组距都为10。**直方图各柱面积总和=1**；连接顶端中点并在两端补零得到的**折线下方面积不一定=1**，本课实测模型面积19/20。
- 各组右边界累计频率分别 `3/40,11/40,25/40,35/40,40/40`；低于80分实际25人占62.5%。组内累计曲线只是连接分组边界的插值示意，不能解释为观测到精确组内分布。
- 茎叶镜显示的12个原始数是40人数据的确切子集 `STEM_SUBSET`，而不是另造与前述成绩不相容的数据；与40人的统计分布保持区别。

## 学习命题 → 屏上对象 → 验证
| 镜头 | learning_fact | observable_state | check | render_frame |
|---|---|---|---|---|
| 0 开场 | 40个设定成绩，表/图基于同批值，茎叶为其中12值 | n=40、数据说明 | `test_all_groups_come_from_forty_actual_scores` | 首帧与声明无遮挡 |
| 1 分布表 | 五组计数、频率、频率密度一致 | 分组表 `[50,60)` 至 `[90,100)`、五组数据及和为1 | 计数与每行公式由 `distribution()` 生成 | 每行值与区间对应 |
| 2 直方图 | 横宽组距10、柱高频率/组距，面积总和1 | 五根柱、坐标轴、70～80占35% | `test_frequencies_densities_and_histogram_area` | 首帧、全部柱顶及结论帧 |
| 3 频率折线 | 与直方图同组中点；折线下面积未必1 | 同一组柱、组中点折线、正确面积提示 | `test_polygon_area_is_not_histogram_area`，本课为19/20 | 折线首末点与范围检查 |
| 4 累计频率 | 在80边界为25/40；末端累计1 | 六边界点、累计数值字幕 | `test_cumulative_frequency_is_consistent_with_score_threshold` | 80的坐标点、文案25人同帧 |
| 5 茎叶 | 12份成绩原始值保持可重构 | 四行茎叶、58读值示例 | `test_stem_leaf_represents_real_subset_without_losing_repetitions` | 茎叶位数和重复值逐项核对 |
| 6 总结 | 不混淆柱面积、折线面积、累计组界值 | 五种表现形式及求和公式 | 回归所用数据均来自同一常量 `SCORES` | 各说明文字无遮挡 |
| 7 片尾 | 数据、画面、结论一一对应 | 总结和品牌文字 | 前七镜数学结论未变 | 末帧安全区 |

## 分层验收
- `python -m py_compile freq_dist_animation.py frequency_distribution_math.py test_frequency_distribution_math.py`。
- `python -m unittest -v test_frequency_distribution_math.py`，再运行本项目 `.opencode/skills/manim-video-production/scripts/audit_scene.py` 做 AST 检查并审核 WARN。
- 目标 Manim、字体和 TeX 就绪时：`manim -pql freq_dist_animation.py FreqDistAnimation`；检查表格、直方柱、折线首末点、80边界、茎叶及 9:16 实际 Mobject 包围盒。
- 只有新视频真正渲染成功才做逐帧、ffprobe与音轨验收；现阶段渲染/关键帧/媒体等级为 `not_run`，原有视频不得覆盖。
