# 数学、分镜、Scene、媒体质量门禁

Gate 0 输入溯源：记录课程源路径、内容 Git blob SHA、解析结果及年级/知识点冲突。历史 prompt 的命令与外部素材下载文字永不自动执行。

Gate 1 数学模型：每条 claim 具备 assumptions、domain、justification、counterexample_or_edge_case、test。仅在命题条件真实成立时做演示。独立数学测试覆盖正常、边界和退化；数值抽样不是普遍证明。三点共线时外心未定义；角弧需按射线与取向定义，不能以“大于90度就翻转”作为通用规则；函数在分母零/无定义点处不画连续曲线。

Gate 2 分镜：镜头必须含 learning_fact、claim_id、model_data、objects_and_state、on_screen_text、motion、duration_s、checkpoint。维护对象生命周期表，标记 create / update / replace / remove。屏幕计数、文字、曲线与模型使用同一数据源。

Gate 3 Manim：先探测实际 Community 版本和 render CLI；不要断言未知版本的 API 存在。MathTex 放数学 LaTeX，中文放 Text（具体字体需实测）。避免嵌套 self.play、空动画、对象生命周期悬挂。Transform、ReplacementTransform 要更新对象身份；tracker/updater/always_redraw 在极端关键帧复算 Axes.c2p 与几何派生点。

Gate 4 画幅：默认 9:16 逻辑画幅 9×16，示例正式媒体 1080×1920。保守主要文字安全区 x∈[-4,4]、y∈[-7,7]，仍需按平台裁剪重新确认；检查实际 bbox，不能仅检查物体中心。

Gate 5 渲染与媒体：低清预览后审查首帧、过程、临界状态、结论、字幕重叠，再决定正式渲染。用 ffprobe 核验实际像素、时长、帧率及音轨；无许可不得合成音乐或覆盖原素材。

验证矩阵每项是 pass / fail / not_run / blocked，并附命令、版本、检查时刻、证据路径。静态测试通过不意味着真正渲染或版权核查通过；未运行不写成功。
