# 001 整数和整除的意义：修复与分层验收

## 本课数学前提

- 整数 `a,b` 且 `b ≠ 0`：`b | a` 当且仅当存在整数 `q` 使 `a = bq`。
- 本课方块分组使用 `a ≥ 0`、`b > 0`：`a = bq+r`、`0 ≤ r < b`。
- “因数 ≤ 对应倍数”仅在正整数因数与倍数语境下成立；对零或负整数不能直接推广。
- 不将 `12 ÷ 5 = 2 ... 2` 之类口语化余数记法当作普通等式；本课改用 `12=5×2+2`。

## 逐镜追溯和待验帧

| Scene 方法 | learning_fact / 给定条件 | 可见画面（同一引用） | check / 待检查关键帧 |
|---|---|---|---|
| `show_opening` | 12 个苹果平均分给 3 人 | 开场提问和顶部署名 | 文字无遮挡，`12//3 == 4` |
| `show_concept` | `a,b∈ℤ` 且 `b≠0` | `a=bq`、`b\mid a` 和中文定义 | 定义无遗漏，TeX 正常编译 |
| `show_example_divisible` | 12 个方块平均分 3 组 | 同一批 12 个 Square 移动为 3 组，每组标 4 | `3*4==12`；动画结束时确有 3 组，每组 4 块 |
| `show_example_not_divisible` | 12 个方块平均分 5 组 | 5 组各 2 块 + 同一批方块中剩余 2 块 | `5*2+2==12`、`0≤2<5`，字幕/方块/公式匹配 |
| `show_factor_multiple` | `12=3×4`，只讨论正整数 | 3、4 的因数关系与 12 的倍数关系 | 条件与因数比较在同一镜头显示 |
| `show_notation` | `3|12`、`5∤12` | 两条符号分别与解释对应 | `12%3==0`、`12%5!=0`，符号方向正确 |
| `show_outro` | 回顾整数条件、零余数、正整数范围 | 数学结论、署名 | 总结不被旧对象遮挡，所有文本在安全区 |

## 验证状态（更新时需填真实证据）

| 层级 | 状态 | 证据与限制 |
|---|---|---|
| math | `pass`（人工核对核心例题） | `12=3×4`、`12=5×2+2`、整除定义和范围已核对；数学专项脚本另需运行 |
| syntax | `not_run` | 需执行 `python -m py_compile divisibility_meaning.py` |
| ast | `not_run` | 需执行 `python .opencode/skills/manim-video-production/scripts/audit_scene.py <本课脚本路径> --json` |
| unit_tests | `not_run` | 执行本目录 `python verify_divisibility.py`，独立测试不能替代渲染 |
| manim_render | `blocked` | 当前执行环境未安装 Manim，且不具备可联网安装依赖的容器 |
| frame_review | `not_run` | 需实际渲染后检查开场、分组终态、两种结论、符号、片尾以及完整 Mobject 包围盒 |
| ffprobe | `not_run` | 本次未产出新 MP4，现有旧视频不构成修复后的渲染证据 |
| audio_review | `not_run` | 未修改既有视频与音轨 |

> 本文件只记录当前课件的修复与验收，不用静态代码检查冒充视频质量认证。
