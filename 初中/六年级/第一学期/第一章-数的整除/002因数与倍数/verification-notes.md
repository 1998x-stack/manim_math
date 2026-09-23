# 002 因数与倍数：分镜核对与分层验收

## 数学规格

在正整数课件段落中，只讨论 `n>0` 的**正因数**和**正倍数**。若 `a=bq` 且 `a,b,q` 都是正整数，则 `b`、`q` 是 `a` 的正因数，`a` 是 `b`、`q` 的正倍数。正整数 `n` 的正因数有限，包含 `1`、`n`；正倍数 `n,2n,3n,...` 无限，最小值为 `n`。**扩展到整数域**时，若 `b` 是非零整数，则 `0=b×0`，因此 0 是 b 的整数倍数，但不是正倍数。不可把这两个讨论域的结论直接混放在同一张无限/最小值表格中。

## 逐镜检查清单

| Scene | learning_fact | 可见画面和数据 | 必须核对的关键帧 |
|---|---|---|---|
| `show_opening` | 12 颗糖可以平均分给不同正整数人数 | 实际 12 个圆点；提出 2、3、4、6 人的示例 | 圆点数量 12，文字不以省略号暗示人数无限 |
| `show_definition` | `a=bq`，a、b、q 都为正整数 | `12=3×4`，3、4 与 12 的对应关系 | 公式清楚且未误指整体公式边缘 |
| `show_find_factors` | 12 的正因数共有 6 个 | 1×12、2×6、3×4 三幅由实际 Square 组成的数组 | 三幅实际方块数各为 12；完整列出 1,2,3,4,6,12 |
| `show_find_multiples` | 3 的正倍数可继续延伸 | 数轴的 3、6、9、12、15、18 各有一个 Dot | Dot 坐标与标签一致；箭头仍在安全区 |
| `show_special_rules` | 区分正整数因数结论和整数域的零倍数 | `n=1×n` 与 `0=b×0, b≠0` 分开显示 | 不把零混入上一镜的正倍数列表 |
| `show_summary` | n 的正因数和正倍数数量、最小/最大值 | 正整数条件与对应结论同屏；0 的补充独立显示 | 末帧对象确实在 Scene 中，没有消失的滑入文字 |

## 验证分层

- `math`: 逐镜数学事实人工复核；`verify_factors_multiples.py` 从当前 Scene AST 提取纯数学函数测试，待 GitHub Actions 或目标环境实际运行。
- `syntax`: 必须执行 `python -m py_compile factors_multiples.py verify_factors_multiples.py`，记录真实 CI 结果。
- `ast`: 必须执行仓库 Skill 的 `audit_scene.py` 并审阅 warnings。
- `unit_tests`: 必须执行 `python verify_factors_multiples.py`，不能以仅提交测试文件替代运行。
- `manim_render`: 当前容器未安装 Manim，也无法联网安装，未进行完整 Scene 渲染。
- `frame_review`: 需检查开场、每个方块数组、数轴终态、零倍数解释、总结末帧，验证完整 Mobject 包围盒。
- `ffprobe`、`audio_review`: 未生成新视频；保留原始 MP4 和音轨，不以旧视频作为新源码渲染的证明。
