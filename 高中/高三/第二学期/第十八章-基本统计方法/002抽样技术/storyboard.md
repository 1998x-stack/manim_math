# 第十八章 002 抽样技术 · 逐镜可验收分镜

## 模型与限制
- 教学总体包含 40 个互异的编号 `1..40`；演示数据使用本课 `sampling_techniques_math.py` 的三个独立抽样模型，非真实调查。
- 简单随机抽样：无放回等可能选取40人中的任意5人子集，共 `C(40,5)=658008` 种，每人的入样概率 5/40。`simple_random(seed=7)` 是其中一个可复现的样本，画面高亮和字幕共用此数据。
- 系统抽样：按编号顺序分为 5 段，每段 8 人；首段从 `1..8` 中等可能抽起点 r，再选 `r,r+8,r+16,r+24,r+32`；`random_systematic(seed=13)` 生成一次实际随机起点并据此绘图。该设计仅有8种不同五人样本，不能宣称全部 `C(40,5)` 个子集等可能。每个个体入样概率 1/8，但入样事件间不独立。
- 比例分层：三层编号分别为 1..20、21..32、33..40，总量分别20、12、8，按 `5,3,2` 抽取共10人。各层内独立等可能无放回选取，单人入样概率均为 1/4。这个示例与前两例的样本容量不同，必须明确标注。
- 等入样概率并不等于三种抽样方案都允许任意固定样本量的子集；并非所有分层/系统方案在任意总体上都自动等概率。

## 逐镜验证表
| 场景 | learning_fact | observable_state | check | render_frame |
|---|---|---|---|---|
| 开场 | 总体是40名可区分个体 | 40个编号格、模拟声明 | `test_population_and_layers` | 首帧与全部格子 |
| 简单随机 | 全部大小5的子集等可能 | 5格高亮、同一组编号及 `C(40,5)`、单人入样率 | `test_simple_random_is_local_and_without_replacement` | 公式与高亮共屏，数字无错 |
| 等距系统 | 随机首段起点，间隔8；仅8种等距样本 | 同一随机起点与五格高亮及对应编号 | `test_systematic_numbering_and_start`、`test_random_systematic_reproducible_and_valid` | 每8号间隔是否视觉正确 |
| 比例分层 | 三个互斥层大小20/12/8，抽取5/3/2，总样本10 | 10个高亮格，三层各自编号和统一1/4入样比例 | `test_strata_are_actual_disjoint_samples`、`test_proportionate_allocation` | 逐层核对被选编号、行与层人数 |
| 对比 | 前两镜 n=5、分层镜 n=10，样本集合支持不同 | 三种规则与各自样本容量说明 | 测试数据、条件一致；不错误断言同一子集分布 | 逐行检查文字边界 |
| 片尾 | 抽样方法与数据保持一致 | 本课核心抽样规则、作者信息 | `test_invalid_parameters` | 安全区与清场 |

## 分层验收
1. `python -m py_compile sampling_techniques_animation.py sampling_techniques_math.py test_sampling_techniques_math.py`；`python -m unittest -v test_sampling_techniques_math.py`。
2. `python .opencode/skills/manim-video-production/scripts/audit_scene.py sampling_techniques_animation.py --json` 并逐项人工解释 WARN。
3. 确认 Manim、LaTeX、中文字体后运行 `manim -pql sampling_techniques_animation.py SamplingTechniques`；按六镜逐帧审查抽样编号与高亮一致性、图文安全区、公式真实编译与交叠问题。
4. 仅新视频实渲染完成后进行 ffprobe/音轨验收，原 MP4、音频不覆盖；静态通过不等于视频通过。
