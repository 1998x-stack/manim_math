# 001 任意角与弧度制｜修复后的教学分镜

对应 `001_任意角与弧度制.py` 内的真实 Scene `任意角与弧度制Animation`，9:16 竖屏，八段。逻辑图半径为 2.3 个画面单位，只作为数学半径 r 的比例示意；示例题另取 r=3。原 MP4 不作为这份新代码的渲染证据。

## 数学规格

逆时针旋转角取正、顺时针取负。角度与弧度换算为 `180°=π rad`；有向角 θ 的对应弧长为 `l=r|θ|`（r>0，θ 以弧度计）。普通扇形的单层面积 `S=r²|θ|/2=rl/2` 在本课限制于 `0≤|θ|≤2π`，不把多周重复覆盖面积当作普通扇形面积。终边相同当且仅当角之差是 `2kπ`（k∈Z）；同终边不表示旋转过程相同。

## 八镜：数学命题 → 屏上状态 → 检查

| 实际方法 | learning_fact 与条件 | observable_state 与对象生命周期 | check |
|---|---|---|---|
| `show_opening` | 正角、负角及超过一周的角都存在 | 45°、−45°、405° 与主题依次显示，按引用清除 | `verify_radians.py::test_angle_conversions_positive_and_negative` |
| `show_arbitrary_angle` | 同起始边、不同方向可得到 ±45° | 同一圆心先展示 +45° 逆时针弧和终边，清除后展示 −45° 顺时针弧和终边；整镜清除圆与坐标轴 | `test_coterminal_angles_same_endpoint`，首末帧目测旋转方向 |
| `show_radian_measure` | 1 rad 的弧长等于半径 | 圆周角 1 与对应等半径长度弧、两条半径线；只显示同一圆的几何数据 | `test_one_radian_has_arc_length_equal_radius`；截图检验弧线角度与端点 |
| `show_conversion` | `180°=π rad`，负角换算同理 | 等式及 90°、60°、−45° 示例逐行出现，结束按原引用淡出 | `test_angle_conversions_positive_and_negative` |
| `show_arc_length` | `l=r|θ|`，θ 为弧度 | 图中展示 π/3 的夹角；独立数值例题采用 r=3、θ=π/3、l=π，明确数值例题不是图中世界坐标测长 | `test_arc_length_and_signed_angle` |
| `show_sector_area` | 普通扇形 `|θ|≤2π`、`S=r²|θ|/2` | 半径和夹角由同一圆心派生；独立例题采用 r=3 得 S=3π/2 | `test_sector_area_in_valid_range`；关键帧检验图形与字幕条件 |
| `show_terminal_angle` | α、α+2kπ 同终边 | 45° 终边和 405°、−315° 文字对应，不将三种旋转角视为同一过程 | `test_coterminal_angles_same_endpoint` |
| `show_outro` | 按适用条件归纳转换、弧长、扇形面积与同终边 | 每条公式依次出现，最后清理总结、标题和作者标识 | 视频结尾和字幕包围盒目视复核 |

## 验收分级

`syntax` / `math` / `unit_tests` / `ast`：由本 PR 的专项 GitHub Actions 记录；`manim_render` / `frame_review` / `ffprobe` / `audio_review`：尚未执行。数学点位检查不能替代实际 Manim Mobject 完整包围盒、字号、TeX/中文字体及成片音轨检查。