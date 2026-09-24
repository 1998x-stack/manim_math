# 005 二次根式的乘除法｜逐镜可验分镜

- 源码：`radical_mul_div.py`，真实 Scene：`RadicalMultDiv`；11 段方法，逻辑画幅 9×16，输出目标 1080×1920。
- 核心前提：`√a·√b=√(ab)` 需 `a≥0,b≥0`；`√a/√b=√(a/b)` 需 `a≥0,b>0`；`n/√a=n√a/a` 需 `a>0`。不要只记操作而遗漏分母不能为零。
- 本课纯数学函数：`root_product`、`root_quotient`、`rationalize`；数值和域由 `test_radical_mul_div_math.py` 验证。

| 镜头 / 方法 | learning_fact → 实际可见内容 | check / 关键帧 |
|---|---|---|
| 1 `scene_opening` | 直观对比 `√3·√5=√15`、`√12÷√3=2` | 两张卡片均显示完整算式 |
| 2 `scene_mul_formula` | 乘法性质及 `a≥0,b≥0`、零边界 `√0·√5=0` | 条件属于同一公式；负值拒绝由数学测试覆盖 |
| 3 `scene_mul_ex1` | `√3·√5→√(3·5)→√15`，最简结果 | 每一步与同一组数据一致 |
| 4 `scene_mul_ex2` | `√2·√8=√16=4`；画长方形两边对应 √8、√2，面积 4 | 示意边长比例 `√8/√2=2` 对应显示宽高 `3.8/1.9=2`，强调画面单位整体缩放；检查图形与标签位置 |
| 5 `scene_div_formula` | `√a/√b=√(a/b)`、`a≥0,b>0`，并示范 b=0 的反例 | `root_quotient(5,0)` 拒绝，不出现分母 0 可计算的结论 |
| 6 `scene_div_ex1` | `√12/√3→√(12/3)=√4→2` | 分子分母同根号，最终结果一致 |
| 7 `scene_rationalize_intro` | `1/√3` 乘以 `√3/√3=1`，化成 `√3/3`；通式 a>0 | 同乘分子分母而非仅分母，分母非零 |
| 8 `scene_rationalize_ex` | `6/√3→6√3/(√3·√3)→6√3/3=2√3` | 取消原横向追加长标签导致的潜在卡片越界；各步骤独立框内 |
| 9 `scene_quick_practice` | 乘法、除法、有理化三个正确式及 `√5/√0` 的无意义例 | 数学真假由纯函数验证；中文字用 `Text`，公式用 `MathTex` |
| 10 `scene_summary` | 三条公式及各自适用条件同框复盘 | 不能遗落有理化的 a>0 和除法的 b>0 |
| 11 `scene_outro` | `6/√3=2√3` 和分母非零的提醒 | 全场单次清理当前对象，最后移除作者水印 |

## 生命周期及渲染验收

`author` 在 `construct` 创建并全程保留，11 段各自 `_clear()` 只淡出当前 `self.mobjects` 的顶层对象，片尾另行 FadeOut。卡片根据实际公式宽高缩放内容，但**只有真实渲染关键帧**能验证字体、公式编译、所有完整包围盒、动画状态及图形标签关系。旧 MP4、prompt、音轨均不覆盖。

分层结果需记录：`math`（独立测试）、`syntax`（`py_compile`）、`ast`（Skill `audit_scene.py`）、`manim_render`、`frame_review`、`ffprobe`、`audio_review`。后三项和真实 Manim 渲染未执行时写 `not_run`，不得标记为视频验收通过。
