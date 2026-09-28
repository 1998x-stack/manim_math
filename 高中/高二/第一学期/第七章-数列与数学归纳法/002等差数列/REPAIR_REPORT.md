# 002 等差数列｜逐课修复记录

## 输入与范围

- 原 `arithmetic_sequence.py`、`description.json`、`storyboard.md`，以及 `.opencode/skills/manim-video-production/SKILL.md`。
- Scene 入口仍是 `ArithmeticSequenceLesson`，顺序仍为开场、定义、通项、前 n 项和、等差中项、图形、性质与应用、总结共八镜；输出仍为竖屏 9:16。
- 保留品牌文字；不修改、不覆盖任何原 MP4/音轨。
- 这次对原场景进行了较大幅度的结构调整，**并非最小差异补丁**；需渲染逐镜比对，未验收前不合并。

## 观察到的旧版问题与修正

1. 公差场景把多组 `d` 标签 `Transform` 到同一坐标；新场景使用分别就位的增量标记，不再使多个不同对象重叠。
2. 求和、通项、应用题旧版在单行追加长公式，存在横向越界风险；新脚本将求和例题按推导分行显示，所有 Text/MathTex 根据实际宽度收缩至 7.3 逻辑单位以内。宽度检查不能代替渲染后关键帧的完整包围盒检查。
3. 旧图像镜头直接绘制连续 `axes.plot`，而数列仅在整数下标有定义；新脚本先出现离散点，另以有说明的虚线帮助观察共线性。
4. 原 `description.json` 把性质结论的 `a_q` 误写成 `aₓ`，已统一更正。
5. 新增不依赖 Manim 的 `arithmetic_model.py` 与 `test_arithmetic_model.py`，覆盖负/零/正公差、n=1、前 n 项和与倒序公式、等差中项、有效及无效下标；高二现有静态 CI 增加本课语法和七项数学回归步骤。

## 数学契约与注意事项

- `a_n=a_1+(n-1)d`、`S_n=n(a_1+a_n)/2` 取正整数 `n`，相邻差公式从 `n=1` 开始；无穷序列不会因为展示七项就被假定只有七项。
- `m+n=p+q => a_m+a_n=a_p+a_q` 的四个下标应为正整数且来自**同一**等差数列。
- 算术平均 `A=(a+b)/2` 适用于实数 `a,b`；数轴中点的画面只用 `5,8,11` 这一按升序排列的例子示意，不用单一图形代替一般证明。
- 最终图形镜头的辅助虚线**不是**定义在实数区间的数列函数图像。
- `description.json` 还包含 `a_n=a_m+(n-m)d` 与内部项判定式 `2a_n=a_{n-1}+a_{n+1}`；本片重点覆盖前述八镜内容，完整课程覆盖仍需对照原分镜审阅。

## 验收状态（按层分开）

| 环节 | 状态 | 证据／阻塞 |
|---|---|---|
| math | pending_ci | `python -m unittest -v test_arithmetic_model.py` |
| syntax | pending_ci | `python -m py_compile arithmetic_sequence.py arithmetic_model.py test_arithmetic_model.py` |
| ast | pending_ci | `Grade 11 static audit`；INFO 辅助模块无 Scene 不是故障 |
| manim_render | not_run | 需要目标 Manim/字体/TeX 环境实渲染 |
| frame_review | not_run | 需检查所有场景首帧、关键帧、字形、重叠、安全区和文本停留时长 |
| ffprobe / audio_review | not_run | 不修改旧成片或音轨 |

预览命令（在本课目录中运行）：`manim -pql arithmetic_sequence.py ArithmeticSequenceLesson`。原 `storyboard.md` 对应旧实现，需以实渲结果重校节奏，不得将旧时间轴视为新成片通过。
