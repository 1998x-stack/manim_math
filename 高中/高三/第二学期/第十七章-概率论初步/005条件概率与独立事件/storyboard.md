# 005 条件概率与独立事件 · 数学规格与可验收分镜

## 公共模型与前提
- 场景1、2、3、6：十张等可能票 `Ω={1,...,10}`，`B={1,2,3,4}`，`A={1,5,6,7,8}`。因此 `P(B)=4/10`、`P(A∩B)=1/10`、`P(A|B)=1/4`、`P(A)=1/2`；`B` 补集中4张命中 A，`P(A|B̄)=4/6`。所有票的可见高亮均由相同数学集合驱动，不拿任意面积比例代表概率。
- 场景4：**切换样本模型**，两次独立公平硬币结果为 HH、HT、TH、TT，A 表示第一次正面，B 表示第二次正面。`P(A∩B)=1/4=P(A)P(B)`；十张票的原 A/B 并不独立，不能复用其结论。
- 场景5：三次独立公平抛币，八种等可能有序结果；恰好2次正面为 HHT、HTH、THH，概率3/8。二项分布的前提是 n 次独立重复、单次成功概率 p 不变、0≤k≤n。
- 通用条件：`P(A|B)` 只在 `P(B)>0` 下定义；全概率中每个非空分区两两互斥、覆盖全集，并要求所用条件概率的分母大于零。

## 可追溯分镜
| Scene | learning_fact | observable_state | check | 验收 |
|---|---|---|---|---|
| 1 开场 | 十张等可能票，B发生后 A 的条件概率 | 10格、A/B定义、1/4 | `test_initial_model_counts` | 待渲染 |
| 2 条件 | P(A|B)=P(A∩B)/P(B)，P(B)>0 | B为蓝色4格，A∩B金边1格，概率1/4 | `test_conditional_multiplication_identity`、零分母测试 | 待渲染 |
| 3 乘法 | 事件交集的路径概率可用条件概率相乘 | 0.4、0.25、0.1 来自同一十票模型 | `test_conditional_multiplication_identity` | 待渲染 |
| 4 独立 | 两枚独立公平硬币的四条有序路径 | HH/HT/TH/TT，1/4=1/2×1/2 | `test_two_independent_fair_coin_tosses` 和原样本非独立测试 | 待渲染 |
| 5 二项 | 三次投掷恰有两次正面概率3/8 | 八种路径，其中HHT/HTH/THH高亮；公式k=2 | `test_binomial_three_tosses` 和非法参数测试 | 待渲染 |
| 6 全概率 | 同一十票模型按 B、B̄ 划分后合计1/2 | 10格，`4/10·1/4+6/10·4/6=1/2` | `test_total_probability_same_model` | 待渲染 |
| 7 总结 | 区分条件、独立、二项与全概率的适用条件 | 5条公式；对分母与独立前提的说明 | 与1–6镜模型一致，复核9:16安全区 | 待渲染 |

## 分层验证
1. `python -m py_compile cond_prob_animation.py conditional_probability_math.py test_conditional_probability_math.py`；`python -m unittest -v test_conditional_probability_math.py`。
2. `python .opencode/skills/manim-video-production/scripts/audit_scene.py cond_prob_animation.py --json`，人工复核 WARN。
3. 确认 Manim / 字体 / TeX 后真实预览 `manim -pql cond_prob_animation.py CondProbAnimation`，检查十格背景与金边是否一致、两次投币模型切换提示、八个三次投币样本、所有公式、逐帧包围盒。
4. 仅在实际新视频产生后 ffprobe 与关键帧验收；不覆盖原有视频或音轨。静态测试结果不能视为 Scene 完整验收。
