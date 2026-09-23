# 分镜｜梯形蝴蝶：等积两翼、分段高与四区验算

- 受众：小学五至六年级奥数；先修：三角形面积、同底等高、两三角形相似与简单比例。
- 数学源：`area_model.py` 的坐标、面积和投影高度；`lesson.py` 负责图形表达，不能把颜色或数值示意当作证明。
- 画幅：逻辑 9×16，默认 1080×1920/30fps；`MANIM_PREVIEW=1` 低分辨率预览。时长仅为分镜估计，尚未进行实际媒体测量。
- 前提：凸梯形 ABCD，AB∥CD，AB=6 cm，CD=3 cm，两底距离 4 cm，O=AC∩BD。图中采用对称的本课示例，但两翼相等对任意非退化凸梯形都成立。

## Scene 01｜真实梯形与可见的完整高
- learning_fact：上、下底平行，高是两底间的垂直距离，不是梯形腰的长度。
- diagram：A=(-3,-2),B=(3,-2),C=(1.5,2),D=(-1.5,2)；上底标 3、下底标 6，右侧单独作高=4 的金色虚线和直角记号。
- objects_and_state：title/subtitle/conditions/outline/base_labels/outer_height/outer_guides/outer_angle/height_label 创建并保持。
- check：上下底 y 差 4，高线 x 常数、两个端点位于两底所在直线；高线不可与斜腰混淆。

## Scene 02｜对角线造出四块蝴蝶
- learning_fact：AC、BD 相交于 O=(0,2/3)。四块分别为 △AOB（蓝）、△COD（金）、△AOD（绿）、△BOC（粉）。
- diagram：两条对角线、五点字母和四色四区；填色在轮廓/对角线后方，标点文字置顶。
- check：O 同时在 AC、BD；四区内部不重叠，面积相加等于梯形面积；不能将 O 误标到高线与底边的交点。

## Scene 03｜先证明左右两翼相等
- learning_fact：△ABD 和 △ABC 共底 AB 且顶点 D、C 位于同一条平行上底，所以两个大三角形面积均为 6×4/2=12。
- diagram：依次为大三角形 ABD 描绿色高亮轮廓、再变为 ABC 的粉色高亮轮廓；保留梯形结构与 O 的对应关系。
- check：ABD 不是 ACD；两个大三角形的第三顶点位于上底，因此各自垂直高为 4。

## Scene 04｜减去公共 △ABO，留下相等的翅膀
- learning_fact：O 位于 BD、AC 上，故 △ABD=△ABO+△AOD，△ABC=△ABO+△BOC。两边均减去公共 △ABO=8，得到两翼 △AOD、△BOC 都为 4。
- diagram：先单独高亮蓝色 △ABO 并在其中放 8；再同时高亮绿色和粉色两翼，分别写 4；底部公式 `S_AOD=S_BOC=12−8=4`。
- objects_and_state：高亮大三角形须离场后才覆盖公共区；公共区和两翼高亮仅服务证明，转入高线分割场景时整体退场；基础四色块与顶点仍保留。
- check：按实际边界划分，ABO 与 AOD 拼出 ABD，ABO 与 BOC 拼出 ABC；不把 △ABO 当成任意两翼的公共组成部分。

## Scene 05｜从 O 作到上下两底的两段垂线
- learning_fact：相似三角形给出 AO:OC=AB:CD=2:1。O 到下底的垂直距离为 8/3，到上底为 4/3，总高 4。
- diagram：从 O=(0,2/3) 分别向 y=-2、y=2 画蓝/金竖直虚线，并在对应垂足显示直角；高的数字置于正确的那一段旁边；在主图上方保留比例式。
- check：高不等于斜线段 AO 或 OC；(8/3)+(4/3)=4，比例 2:1 来自平行线下的相似三角形而非观察绘图大小。

## Scene 06｜用底与对应高计算上、下两块
- learning_fact：`S_COD=3×(4/3)/2=2`；`S_AOB=6×(8/3)/2=8`。上下的面积比是 (3/6)²=1:4。
- diagram：公式一条一条出现；结束清理临时高线、直角记号、数字与公式，露出完整四色四区。
- check：上三角形底为 CD=3、对应高为 O 到上底的 4/3；下三角形底为 AB=6、对应高为 O 到下底的 8/3。

## Scene 07｜四区合计与可推广结论
- learning_fact：两翼 4 与 4、上方 2、下方 8，相加 18 cm²；梯形面积也为 (6+3)×4/2=18 cm²。
- diagram：四块颜色及其各自内部数字显示，底部独立显示 `S_COD:S_AOB=3²:6²=1:4` 和总面积式。
- check：数字坐标与对应真实三角形内域核对；推导条件限于正长度、非退化凸梯形，面积比不要遗漏平方。

## 质量验收（逐层报告）

| 检查 | 状态 | 证据与命令 |
| --- | --- | --- |
| math | 待本分支 CI | `python -m unittest discover -s . -p 'test_area_model.py'`，含错位梯形、分段高、公共部分、退化测试 |
| syntax | 待本分支 CI | `python -m py_compile lesson.py area_model.py test_area_model.py` |
| ast | not_run | `python .claude/skills/manim-video-production/scripts/audit_scene.py <本课绝对路径>/lesson.py` |
| manim_render | not_run | `MANIM_PREVIEW=1 manim lesson.py TrapezoidButterflyArea` |
| frame_review | not_run | 对角线交点、完整高、公共区替换、两段高、内部数字、文字与图形包围盒 |
| ffprobe | not_run | 正式渲染后核对 1080×1920、30fps、时长 |
| audio_review | not_run | 不改原视频、不添加音轨 |
