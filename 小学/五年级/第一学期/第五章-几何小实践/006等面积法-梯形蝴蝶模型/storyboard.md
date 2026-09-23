# 分镜｜梯形蝴蝶模型与面积比例

- 受众：小学五至六年级奥数；先修：三角形面积、同底等高、简单比例。
- 源材料：本目录 `prompt.md`；面积数据由 `area_model.butterfly_areas` 提供。
- 画幅：逻辑 9×16、深色背景；正式默认 1080×1920/30fps，预览 270×480/15fps。
- 时长：动画约 19–26 秒（非实测视频时长）；教学难点可延长停顿。

## Scene 01｜给出梯形与条件（约 4 秒）
- learning_fact：AB∥CD，AB=6 cm、CD=3 cm、高=4 cm。
- screen：标题、条件公式、梯形 ABCD。
- objects_and_state：title、subtitle、conditions、outline 创建。
- check：A=(-3,-2)、B=(3,-2)、C=(1.5,2)、D=(-1.5,2)；上下底均水平且点标对应真实顶点。

## Scene 02｜交叉分割成四块（约 3 秒）
- learning_fact：连接 AC 和 BD 得内部交点 O，分成 AOB/COD/AOD/BOC 四个三角形。
- screen：绘制两条对角线、O 与五个字母；四块依次蓝、金、绿、粉填色。
- objects_and_state：diagonals、dots、labels、parts 创建，描边和标签置前避免被填色遮挡。
- check：O 同时在 AC 和 BD；四块无交叠内区，总面积与整个梯形面积相等。

## Scene 03｜算上下两块（约 4 秒）
- learning_fact：`AO:OC=AB:CD=2:1`，所以 O 到下底的距离为 8/3 cm、到上底为 4/3 cm；底部面积 8 cm²、顶部面积 2 cm²。
- screen：比例公式，内部底部 8、顶部 2 两个数字。
- objects_and_state：ratio、upper_number、lower_number 创建。
- check：比例来自 AB∥CD（相似三角形）；高的两个分段之和恰好是 4 cm；上/下三角形面积分别为 2/8。

## Scene 04｜同底等高减去共同部分（约 4 秒）
- learning_fact：△ABD 和 △ABC 共底 AB、顶点 D 和 C 在平行上底，故两者面积同为 12 cm²。
- screen：`S_ABD=S_ABC=6×4÷2=12`；两大三角形都包含已知公共 △ABO=8。
- objects_and_state：same_base 创建；轮廓及四块面积保留不清空。
- check：两个大三角形减去相同 8，分别只余左翼 AOD 与右翼 BOC，不能把它们误作 ABD 与 ACD。

## Scene 05｜蝴蝶等面积结论（约 5 秒）
- learning_fact：两翼面积同为 `12−8=4 cm²`；四块合计 `2+4+4+8=18 cm²`。
- screen：左右两翼各出现数字 4；展示 `S_AOD=S_BOC=12−8=4` 与梯形总面积公式。
- objects_and_state：wing_numbers、wing_formula、total 创建；所有数学标签与图形持续可见。
- check：数字 2/8/4/4 显示在正确色块；`(6+3)×4÷2=18` 与分块和一致；公式/标签完整处于安全区。

## 对象生命周期

| object_id | create_scene | update_scene | remove_scene | reason |
| --- | --- | --- | --- | --- |
| outline / dots / labels | 01–02 | 02 置于填色前景 | 保留至片尾 | 几何标签贯穿证明 |
| diagonals / parts | 02 | 02 置于轮廓下方 | 保留至片尾 | 公共部分直观可见 |
| ratio / numbers | 03–05 | 数字逐步添加 | 保留至片尾 | 结论有据可追溯 |

## 验收清单（创建时状态）

| check | status | evidence / command |
| --- | --- | --- |
| math | specified | `python -m unittest discover -s . -p 'test_area_model.py'`，含非对称梯形与退化情况 |
| syntax | not_run | `python -m py_compile lesson.py area_model.py test_area_model.py` |
| ast | not_run | `.claude/skills/manim-video-production/scripts/audit_scene.py` |
| manim_render | not_run | `MANIM_PREVIEW=1 manim lesson.py TrapezoidButterflyArea` |
| frame_review | not_run | 审查交点、四块数字、字幕安全区 |
| ffprobe | not_run | 正式渲染后测量分辨率、帧率与实际时长 |
| audio_review | not_run | 本课不含外部音轨 |
