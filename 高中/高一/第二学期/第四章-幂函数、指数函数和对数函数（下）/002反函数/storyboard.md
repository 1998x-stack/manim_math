# 002 反函数｜修复后分镜与验收记录

本分镜对应 `inverse_functions.py` 内实际入口 `InverseFunctions` 和七段 `scene_1_opening` 至 `scene_7_outro`。画幅 9:16（逻辑 9×16）；目标时长仅是制作建议，实际时长以完整渲染文件为准。`description.json` 是知识点输入，不作为已验证画面。原 MP4 与新源码之间没有完成重新渲染的证据。

## 数学规格

设 `f:A→B`，其中 `B=f(A)`；只有当 `f` 在 A 上单射时，每个 y∈B 才有唯一原像，`f^{-1}:B→A` 才定义。`f^{-1}(f(x))=x` 要求 `x∈A`；`f(f^{-1}(y))=y` 要求 `y∈B`。`f(x)=2^x` 的定义域为 R、值域为 `(0,+∞)`；`f^{-1}(x)=log₂x` 的定义域为 `(0,+∞)`、值域为 R。严格单调保证单射，但不能把它表述为存在反函数的必要条件。图像与直线 y=x 对称不依赖有限采样点证明。

## 实际 Scene 分镜

| Scene | learning_fact / 前提 | observable_state / 生命周期 | check / 验证 |
|---|---|---|---|
| 1 opening | `2^x=y ⇔ x=log₂y`，前提 y>0 | 指数式、解出 x、函数式依次出现；片尾按原引用清理 | `verify_inverse.py::test_exponential_inverse_on_domain` |
| 2 definition | 定义域 A 与值域 B 交换，唯一原像为存在条件 | `f:A→B`、正向/反向映射、复合公式的域逐一出现后清理 | `verify_inverse.py::test_inverse_exponential_on_positive_domain`；人工检查域标签 |
| 3 symmetry | `2^x` 和 `log₂x` 关于 y=x 对称 | Axes x/y 范围均 `[-1,5]`，指数 x∈`[-1,log₂5]`，对数 x∈`[0.5,5]`；三组点逐对出现并逐对清理 | `test_exponential_graph_inside_axes`、`test_logarithm_graph_inside_axes`、`test_symmetric_points`；渲染关键帧检查轴域和标签 |
| 4 verification | `(a,b)∈G_f ⇔ (b,a)∈G_{f^{-1}}` | `(0,1)↔(1,0)`、`(1,2)↔(2,1)`、`(2,4)↔(4,2)`，仅作为示例 | 人工确认讲解没有把有限示例称为普遍证明 |
| 5 properties | 两种复合恒等式在各自正确的定义域成立 | 两式、互逆式与 `2^{log₂4}=4` 等示例出现；逐镜移除 | 检查各公式中的 `x∈A`、`y∈B`，不得漏域 |
| 6 monotonic | 严格单调是充分条件；水平线与图像“至多”交一点 | 先画 `x/2`，清理后画 `x²−1`；`y=0` 与抛物线交于两点 | `test_horizontal_line_counterexample`、`test_nonmonotone_but_injective_exists` |
| 7 outro | 唯一性、域/值域交换、对称性和充分条件 | 四项总结与公式按同一引用清理，保留原 Scene 入口 | 渲染结尾与作者标识检查 |

## 分层验收状态

`syntax` / `unit_tests` / `ast`：以本 PR 对应 GitHub Actions 作证；`math`：独立公式与边界值回归；`manim_render`、`frame_review`、`ffprobe`、`audio_review`：尚未执行。`DYNAMIC_TEX` 仅能据固定数值点对进行静态复核，仍须目标环境真实编译。旧 MP4 不作为新版源码的渲染验证。
