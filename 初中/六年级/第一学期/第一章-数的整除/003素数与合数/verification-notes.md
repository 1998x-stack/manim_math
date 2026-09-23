# 003 素数与合数：逐镜数学规格和分层验证

## 本课前提

分类对象是正整数。`n>1` 且**恰有两个正因数**时，n 是素数；`n>1` 且**至少三个正因数**时，n 是合数。1 只有一个正因数，所以既不是素数也不是合数。2 是唯一偶素数：大于 2 的偶数还有正因数 2，因此属于合数。`is_prime` 对 n<2 返回 False，`get_factors` 不接受零、负数与非整数；分类范围为 1 至 20。

## 逐镜可追溯项

| Scene 方法 | learning_fact → 实际数据 → 屏上状态 | 渲染后必须核对 |
|---|---|---|
| `show_opening` | 素数 2、3、5、7、11 和合数 4、6、8、9、10，由 `is_prime` 得到配色 | 两组圆形与数字文字分离、颜色清楚 |
| `show_factors_review` | 6 的全部正因数 `(1,2,3,6)` → 四个环绕节点 | 节点与连线准确，不与说明文字冲突 |
| `show_prime_definition` | 7 的正因数 `(1,7)` → 两节点且说明 `n>1` | 计数、圆形数字及解释吻合 |
| `show_composite_definition` | 6 的正因数 `(1,2,3,6)` → 仅对已经出现的 2、3 节点背景高亮 | 字体保持白色，不能对同一对象并行 FadeIn 和 animate |
| `show_special_cases` | 1 有一个正因数、2 恰有两个；大于 2 的偶数还有因数 2 | 左右标签和环绕因数节点没有重叠 |
| `show_classification` | 1—20 由 `classify` 同源生成：8 素数、11 合数、1 特殊 | 数字白色不随背景颜色变化；20 个号码各出现一次 |
| `show_outro` | 概括两个定义与 1、2 的特例 | 中文可读，9:16 画面所有对象在安全区 |

## 分层状态

| 验证项 | 状态 | 证据与限制 |
|---|---|---|
| math | `pass`（人工核对定义与 1—20 分类） | `verify_primes_composites.py` 是真实源代码算法的数学回归，需结合 CI 最终结果更新 |
| syntax | `not_run` | 需运行 `python -m py_compile primes_composites.py verify_primes_composites.py` |
| ast | `not_run` | 需运行 Skill `audit_scene.py primes_composites.py --json`，分类告警逐条复核 |
| unit_tests | `not_run` | 需执行 `python verify_primes_composites.py`；AST 检查并非 Manim 运行 |
| manim_render | `blocked` | 目前未配置可用的 Manim、LaTeX、CJK 字体渲染环境；未生成新视频 |
| frame_review | `not_run` | 需真实渲染后检查每镜关键帧及实际 Mobject 包围盒 |
| ffprobe | `not_run` | 旧 MP4 未覆盖，不能拿旧片冒充当前分支的成片验证 |
| audio_review | `not_run` | 旧视频、讲解和配乐未变更 |

不以静态或数学测试成功宣称视频画面验收成功。
