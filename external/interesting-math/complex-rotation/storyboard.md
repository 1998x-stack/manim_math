# 复数乘法 = 平面旋转？｜数学规格与分镜

- audience：高中拓展／复数基础；先修：复平面、三角函数、复数模。
- source：独立探索；制作依据 `.claude/skills/manim-video-production/SKILL.md`；非特定课本课时。
- objective：看出乘以单位复数 cosθ+i sinθ 会保持模并把辐角增加 θ。
- format：9×16、1080×1920、深色、无音轨；约 16–23 s。

## 数学规格

- claim：任意 z∈C 和任意实数 θ，z′=z(cosθ+i sinθ) 满足 |z′|=|z|。当 z≠0 时辐角增加 θ（模 2π）。
- assumptions/domain：z 为复数，θ 为实数；动画固定 z=1.2+0.5i、θ 从 0 逐步到 2π；绘图比例 x/y 一致。
- justification：令 z=a+bi，则 z′=(a cosθ−b sinθ)+i(a sinθ+b cosθ)，两坐标组成旋转矩阵；|cosθ+i sinθ|=1，故模保持。画面用于解释性质，而非凭单次轨迹证明所有 z。
- counterexample/edge：z=0 仍满足模恒等式，但零向量的辐角无定义；乘以模不为 1 的复数还会缩放；θ 取负表示反方向旋转。
- tests：`test_math.py::VisualMathTests.test_complex_rotation` 核验零向量／非零向量模保持、周期性、角度叠加关系。

## 分镜

| shot | learning_fact | 对象创建／更新 | 动画／约时 | check |
| --- | --- | --- | --- | --- |
| 01 | 一个复数对应平面上的一个点与箭头 | title、hint、NumberPlane、orbit、formula、value_label、value、invariant 创建 | 出现复平面与保持模的圆轨道，约 2 s | 单位长横纵比例相同；轨道半径与初始模一致 |
| 02 | 乘以单位复数时长度不变、角度增加 | vector/point/projection 用同一个 `rotate_complex(z0,theta)` 和同一个 ValueTracker 驱动 | θ 依次到 π/2、π、3π/2、2π，约 9 s | 坐标点落在圆上；虚线投影与点的实部一致；角度数字和动画同步 |
| 03 | 复数模是旋转不变量 | 保留所有主要对象；最终停留在旋转一周后的初始位置 | 约 2 s | θ/π=2.00、位置复原；严禁把模保持外推为所有复数乘法都保持模 |

- layout：plane 6×6、中心 y≈0.6；公式 y≈−4，角度 y≈−5，结论 y≈−6.1；最终以 Mobject 全包围盒复查。
- lifecycle：`always_redraw` 绑定的是同一个 ValueTracker；`DecimalNumber` 的 updater 读取同一 θ，末尾清除数字 updater。
- verification：math、syntax、ast、unit_tests、frame_review、ffprobe 均 not_run；manim_render blocked（本次环境无 Manim）；audio_review not_run（无音轨）。
