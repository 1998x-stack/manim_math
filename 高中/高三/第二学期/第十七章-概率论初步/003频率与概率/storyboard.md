# 003 频率与概率 · 逐镜可验收分镜

## 数学规格与实际数据
- 模型：独立重复投掷公平硬币，正面记 1，反面记 0；理论概率 `P(A)=1/2`。
- `frequency_math.experiment(200, seed=42)` 采用局部 RNG，统一生成每镜图像、频率、正面次数与字幕；`f_n(A)=m_n/n`，`n>=1`。
- 两段曲线分别显示**同一**200次样本的前30个点、前200个点，不重新抽样。关键检查点 n=10、30、50、100、200 由相同源数组读取。
- 大数定律适用于独立、同分布且单次事件概率固定的重复试验；`f_n(A)` 依概率收敛于 `P(A)`，并不保证每个样本路径每一步误差都下降，也不保证任何固定 n 的频率恰等于理论值。图示仅为一次样本，不充当证明。

## 对照表
| Scene | learning_fact / 必要前提 | observable_state（屏上对象） | check / 对应测试 | 状态 |
|---|---|---|---|---|
| 1 开场 | 公平硬币正面理论概率为 1/2；1000 次不保证恰好 500 次 | `P(H)=1/2` 与开场提问 | `test_theoretical_probability`、核对文案 | 待渲染 |
| 2 定义 | `f_n(A)=m_n/n`、`0≤f_n≤1`，n≥1 | 实际前10次的 m、精确生成的小数、频率公式 | `test_exact_counts_match_every_displayed_frequency` | 待渲染 |
| 3 小样本 | 单次频率有随机波动 | 前30次折线、0.5 基准线、n=30 的 m 与 f | 两端索引、`Fraction(m,n)`；检查首帧折线至少2点 | 待渲染 |
| 4 大样本 | 大数定律不是逐次单调逼近；前提为独立同分布 | 同一数据前200点折线、n=200 字幕、依概率收敛记号 | `test_frequency_need_not_improve_every_step` 和全部关键检查点 | 待渲染 |
| 5 对比 | 频率是实验统计量，概率是模型中事件的固定数值 | 两条定义、频率与理论概率的公式 | 检查 `MathTex` 不含中文；与 Scene 2 数据一致 | 待渲染 |
| 6 总结 | 定义、取值范围与实验/理论区分 | 公式及总结字幕 | 检查底部安全区和文字阅读节奏 | 待渲染 |

## 生产与验证
1. `python -m py_compile freq_prob_animation.py frequency_math.py test_frequency_math.py`。
2. `python -m unittest -v test_frequency_math.py`；运行 `.opencode/skills/manim-video-production/scripts/audit_scene.py` 对当前源代码做 AST 审计，审慎检查 WARN。
3. 核实 Manim、中文字体与 LaTeX 后运行 `manim -pql freq_prob_animation.py FreqProbAnimation`，检查 6 个场景首末帧、曲线首点、n=10/30/200 文案、对象 9:16 包围盒。
4. 有真实输出后再以 ffprobe 核对媒体；原 MP4 和音轨不覆盖。`syntax`/`math`/`ast`/`render`/`frame_review`/`ffprobe` 分项报告，不把静态测试视为视频验收。
