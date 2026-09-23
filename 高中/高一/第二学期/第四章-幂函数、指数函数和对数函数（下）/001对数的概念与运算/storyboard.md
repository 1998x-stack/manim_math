# 对数的概念与运算｜逐镜验收分镜

场景入口：`LogarithmConcepts`；源文件：`logarithm_concepts.py`；高一第二学期第四章 001。比例 9:16；作者标识固定于底部。旧 MP4 保留，不能作为当前源码的渲染验收依据。

## 数学规格

所有对数均在实数范围：底数 `a>0, a≠1`，真数 `N>0`。乘除法额外要求 `M,N>0`；幂法则要求 `M>0, t∈R`；换底要求 `a,c>0` 且 `a,c≠1`，`b>0`。样例 `log₂8=3` 是精确等式；`e≈2.71828` 是近似值，不能混用等号。

| 镜头 / Scene 方法 | learning_fact（数学事实） | observable_state（可见状态） | data_assertion（对应检查） | 关键帧/验收点 |
|---|---|---|---|---|
| 1 `scene_1_opening` | `2³=8 ⇔ log₂8=3`，对数表示要求的指数 | 从 `2⁰` 到 `2³` 四行方块，数量分别为 1/2/4/8；出现两个等价式 | `2**3 == 8` 与 `log_base(8,2)==3` | 四行逐一出现、答案首帧和退场；核对数量与文字 |
| 2 `scene_2_definition` | 指数和对数互逆，底数/真数均有定义域 | 指数式与对数式、一般形式及 `a>0,a≠1,N>0` 的可见条件 | 非法底数与非正真数抛出异常 | 条件出现时公式不遮挡、标题与底栏不重叠 |
| 3 `scene_3_special_logs` | `lg` 底数 10，`ln` 底数 e | 常用对数和自然对数两张卡；`lg100=2`、`ln e=1` | 特殊底数示例的数值回归 | 卡片完全进入安全区；中文与纯公式分别渲染 |
| 4 `scene_4_identities` | `a^(log_a N)=N`、`log_a(a^t)=t` | 恒等式与 `log_a1=0`、`log_a a=1` | 用 `a=0.5,2,3` 与正真数、负指数回归 | 逐张卡片显示；负指数仍满足互逆 |
| 5 `scene_5_operations_part1` | 乘法变加法、除法变减法，`M,N>0` | `log₂(4×8)=5`、`log₂(8/4)=1` | 乘积和商性质对不同合法底数成立 | 每张公式卡、例题与条件同时可见 |
| 6 `scene_6_operations_part2` | 幂法则与换底公式 | `log₂(8²)=6`、`log₂8=lg8/lg2=3` | 幂次含负数、小数；换底含 `0<a<1` | 不把近似小数标作精确等式；检查所有分母非零 |
| 7 `scene_7_outro` | 回顾定义、恒等式、乘法及换底 | 四张总结卡和条件提示 | 源码 AST 中七个方法与常量公式均存在 | 四张卡全部可读，不遮挡作者栏 |

## 对应修复与证据分级

- 已在源码纠正原镜头 1 将指数等式直接称为对数的表述（数学表述问题）。
- 原镜头 6 的 `lg 8` 与 `lg 2` 曾以三位小数和等号连续代入，精确性不足；现在改用准确的符号换底，近似只用于 e 值。
- 原代码作者信息靠近竖屏上边、公式宽度与对象退场依赖人工检查；改为底栏定位、长公式缩放与保留相同显示引用；这些属于静态可见的预防性调整，**不是已复现的渲染故障**。
- `verify_logarithms.py` 是无需 Manim 的数学与静态结构测试；通过它不代表 LaTeX 编译、字体、真实包围盒、视频帧或音轨通过。

## 验收命令与状态

```bash
python -m py_compile logarithm_concepts.py verify_logarithms.py
python -m unittest verify_logarithms.py -v
python ../../../../../.opencode/skills/manim-video-production/scripts/audit_scene.py logarithm_concepts.py --json
manim -ql logarithm_concepts.py LogarithmConcepts
ffprobe -v error -show_streams -show_format <新生成的视频路径>
```

已提交源码与数学专项测试；`syntax / ast / unit_tests / manim_render / frame_review / ffprobe / audio_review` 以实际 CI 或本地检查记录为准，未执行项目不能标记为通过。检查第一帧、四行方块、每镜条件文本、四张总结卡与最终消失帧；旧 MP4 与音轨不覆盖。
