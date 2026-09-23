# 第十八章 004 数据的集中趋势 · 逐镜可验收分镜

## 数学规格和数据
- 所有数据均为本课人为设置的教学示例，位于 `central_tendency_math.py`；每一镜明确所用数据集，**不得将不同人数、不同分布的示例混作同一调查**。
- 九个成绩 ODD：`52,63,71,74,78,82,85,85,90`，总和680，精确均值680/9（≈75.56），中位数78。偶数例 EVEN：`62,68,74,78,85,91`，中位数(74+78)/2=76。
- 加权例：成绩85、70；权重3/5、2/5；分母总权重为1，结果79。一般权重应非负且总和正，未归一时需除以总权重。
- 众数例：`71,74,78,78,78,82,85,90`，78重复3次是唯一众数；并列众数可以多个。“无重复众数”的表述按本课约定，不将所有不重复值机械宣布为唯一众数。
- 极端值控制比较：原8数 `60,62,65,68,70,72,75,78` 只把末尾78换成200。原均值68.75、原中位数69；新均值84、新中位数仍为69。**仅断言本次替换造成的结果**，不宣称所有极端值都绝对不能改变中位数。

## 分镜数学命题与实际屏上状态
| 场景 | learning_fact | observable_state | check | frame_review |
|---|---|---|---|---|
| 0 开场 | 9个模拟成绩，比较三种指标 | ODD的九个数值与模拟说明 | `test_odd_sample_mean_and_median` | 首帧、数字顺序和说明 |
| 1 均值 | 680/9≈75.56；九个数都参与计算 | 9格、总和680、均值公式 | `test_odd_sample_mean_and_median` | 分子与显示九格之和一致 |
| 2 加权 | 85×0.6+70×0.4=79，权重和为1 | 两数两权重、带分母的一般公式、79 | `test_weighted_mean_from_visible_scores` | 公式和权重字幕同帧 |
| 3 中位数 | 九数取第5个78；六数取第3、4个74、78均值76 | 奇/偶各一页，正确索引高亮 | `test_odd_sample_mean_and_median`、`test_even_sample_median` | 两种页的排序与数字逐项核查 |
| 4 众数 | 78出现3次，支持并列/无重复边界 | 八格中只高亮三个78，结论78 | `test_unique_multiple_and_no_repeated_mode` | 高亮出现次数和其他数正确 |
| 5 极端值 | 只替换一个78→200，均值68.75→84、中位数保持69 | 替换前后两组各8数，唯一改动的200高亮，两指标对比 | `test_outlier_is_one_controlled_replacement` | 前后其余7数不变；两组数字清晰 |
| 6 总结 | 按实际问题区分三种指标，避免绝对化判断 | 精确九数均值与中位数、三类定义 | 数学测试与1–5镜对应 | 文字和公式布局检查 |
| 7 片尾 | 先求和、先排序、计频次 | 三种处理原则和提示 | 与全部演示数据及适用条件一致 | 安全区、结尾帧 |

## 分层验证
- `python -m py_compile central_tendency_animation.py central_tendency_math.py test_central_tendency_math.py`。
- `python -m unittest -v test_central_tendency_math.py`；`python .opencode/skills/manim-video-production/scripts/audit_scene.py central_tendency_animation.py --json` 并逐条复核 WARN。
- 确认 Manim、中文字体和 TeX 后运行 `manim -pql central_tendency_animation.py CentralTendency`，检查奇偶数据排列、众数重复、高亮对象、极端值前后对照、9:16所有关键帧包围盒。
- 真实视频、逐帧、ffprobe与音轨验收尚待执行；不得以纯数学测试或旧成片证明新视频已通过，不覆盖旧 MP4 或音轨。
