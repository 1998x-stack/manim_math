# 004 事件的关系与运算 · 数学模型与可验收分镜

## 数学规格
- 固定样本空间 `Ω={1,2,3,4,5,6}`，公平六面骰；第1、2、4、5镜 `A={1,3,5}`（奇数），`B={2,3,5}`（质数）。
- 第3镜为演示包含关系，**明确重新定义** `A={3}`、`B={2,3,5}`，避免将原来的奇数集合误说成质数集合的子集。
- 第6镜互斥例子重新定义 `A={1}`、`B={2,4,6}`，3和5均不属于并集，证明“互斥不一定对立”；对立例子使用原奇数 A 与其补集 `{2,4,6}`，两事件交集为空、并集为 Ω。
- 韦恩图是同一六元素集合的示意布局：Ω 内6个数字和真实成员关系一致。重叠部分实际标 3、5，而非单凭圆面积声称某一概率。计算 `P(A)=|A|/6` 的前提为六个基本事件等可能。

## 逐镜对应关系
| 场景 | learning_fact | observable_state | check | 验收 |
|---|---|---|---|---|
| 1 开场 | 六个等可能基本事件；A 奇数、B 质数 | 6格骰子及 A/B 数字 | `test_initial_six_outcomes` | 待渲染 |
| 2 韦恩图 | `A∩B={3,5}`，Ω 还包含 A/B 以外的4、6 | 六数位置和重叠圆 | `test_overlap_and_union_include_common_outcomes_once`；逐帧检查数字位置 | 待渲染 |
| 3 包含 | 此镜 `A={3}⊆B={2,3,5}`，`P(A)≤P(B)` | 内圆完全位于大圆，文字指出重新定义 | `test_subset_and_monotonicity`，中心距0.35+半径0.65<外圆1.45 | 待渲染 |
| 4 并集 | `A∪B={1,2,3,5}`，概率 4/6；重叠只计一次 | 金色高亮这四数、一般加法公式及数值演算 | `test_overlap_and_union_include_common_outcomes_once` | 待渲染 |
| 5 交集 | `A∩B={3,5}`，概率 2/6 | 仅3、5高亮，交集概率及不等式 | `test_overlap_and_union_include_common_outcomes_once` | 待渲染 |
| 6 互斥与对立 | 互斥不要求覆盖全样本空间；对立还要求并集为 Ω | 两组分别说明的集合、空交与补事件公式 | `test_exclusive_is_not_necessarily_complementary`、`test_complementary_covers_all_outcomes` | 待渲染 |
| 7 总结 | 一般并集公式、互斥与补集区别 | 文字与纯数学公式 | 公式与各镜一致，检查9:16关键帧 | 待渲染 |

## 验证顺序
1. `python -m py_compile event_relations_animation.py event_relations_math.py test_event_relations_math.py`；`python -m unittest -v test_event_relations_math.py`。
2. `python .opencode/skills/manim-video-production/scripts/audit_scene.py event_relations_animation.py --json`，人工复核 WARN。
3. 确认 Manim、中文字体和 LaTeX 可用后：`manim -pql event_relations_animation.py EventRelations`。检查韦恩图 3/5 的位置、4/6 在圆外且在 Ω 内、内含与空交、中文文字及动画对象包围盒。
4. 真实渲染完成再逐帧审查及 ffprobe；原 MP4、音轨不覆盖。数学/语法/AST/Manim/逐帧/媒体各自记录 pass/fail/blocked。
