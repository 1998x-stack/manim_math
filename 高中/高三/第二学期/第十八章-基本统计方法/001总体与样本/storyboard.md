# 第十八章 001 总体与样本 · 逐镜可验收分镜

## 数学规格和数据来源
- 教学模型：总体是20个不同编号的模拟个体 `POPULATION=(1,...,20)`，不是任何真实人群的调查结果。个体 i 对应人为设置测量值 `x_i=50+2i`，总体均值是 `(Σx_i)/20=71`。
- 样本使用独立的局部伪随机生成器 `random.Random(42).sample(POPULATION,6)`，无放回得到六个不同编号。`PopulationSample.selected` 是图格高亮、编号字幕与样本测量值的**唯一数据源**。固定随机种子只为视频复现一次实际抽样，不等于硬编码选择。
- 简单随机抽样方案：在20个个体中等可能选择大小为6的每个子集，总共有 `C(20,6)=38760` 种；单个指定个体入样概率 `6/20=3/10`。无放回抽样下不同个体的入样事件并不相互独立。
- 样本均值 `x̄=Σ_{i∈S} x_i/6` 由被选编号映射到测量值后计算。不要将样本均值直接说成总体均值，或声称一次随机抽样一定具有代表性。

## 逐镜教学命题 → 可见状态 → 检验
| 镜头 | learning_fact | observable_state | check | render_frame |
|---|---|---|---|---|
| 1 开场 | 总体为20个模拟个体；样本不是全部个体 | 20个编号图格、模拟声明 | `test_population_and_measurements` | 首帧：格数、标题与免责声明无遮挡 |
| 2 总体与个体 | N=20，个体有互异编号 | 20格与 `N=20` | `test_population_and_measurements` | 所有格子可读 |
| 3 样本 | 实际无放回随机选出的六人属于总体 | 正好六格蓝色并显示同一组六编号 | `test_six_distinct_members_from_population`、局部 RNG 测试 | 高亮与字幕编号逐个对照 |
| 4 容量 | 样本容量为六个个体，不是数据总和 | 仍只高亮六格、`n=6,N=20` | `test_six_distinct_members_from_population` | 最后一格与公式同帧可读 |
| 5 简单随机抽样 | 所有大小六的子集等可能；单人入样率为3/10 | `C(20,6)=38760`、`P(i∈S)=6/20`、高亮该次样本 | `test_all_fixed_size_subsets_are_symmetric` | 公式和缩小图格不重叠 |
| 6 均值 | 按真正选出的编号取六个测量值计算 x̄ | 六个自设数据、精确分数形式的样本均值、总体均值71 | `test_mean_uses_actual_sample_ids` 与边界测试 | 分子等于六个可见数值之和，分母6 |
| 7 统计推断 | 抽样→计算→估计不保证绝对代表性 | 总体、样本和推断流程字幕 | 不将一次样本描述为确定的总体结论 | 逐行可见 |
| 8 片尾 | 总体、样本、容量和抽样机制区别 | `N=20,n=6` 与总结 | 全程与模型一致 | 片尾安全区 |

## 验证与交付记录
- `python -m py_compile population_sample_animation.py population_sample_math.py test_population_sample_math.py`。
- `python -m unittest -v test_population_sample_math.py`；按 `.opencode/skills/manim-video-production/scripts/audit_scene.py` 静态审计。数学回归不能验证 Manim 对象边界。
- 在确认 Manim、TeX 和中文字体后运行 `manim -pql population_sample_animation.py PopulationSample`，对八镜关键帧、对象实际包围盒、数值标签、动画清场逐项审查。
- 真正生成新视频后方可做 ffprobe/音轨/视觉验收；旧 MP4 和旧音轨不覆盖。现阶段 `manim_render`、`frame_review`、`ffprobe`、`audio_review` 均待验证，不能以静态检查或旧视频替代。
