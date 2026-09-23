# 006 相遇问题｜五年级起
来源：自拟例题。条件：甲乙相距 200 千米同时相向匀速出发，速度分别为 60、40 千米/时，直到相遇均不停走；相遇时间 t=200/(60+40)=2 小时。画面水平长度 6 单位代表 200 千米；甲运动 3.6 单位、乙运动 2.4 单位，两点在 x=0.6 相遇。若两人皆静止，模型拒绝求相遇时间。

## 镜头与核验
1. learning_fact: 问题的距离、速度和方向；objects: title/question/track/起点标签 创建；check: 给定 200、60、40 与后续公式一致。
2. learning_fact: 剩余距离 200-(60+40)t；objects: shrinking 创建；motion: 两点匀速向 x=0.6 运动；check: 同一动画运行时间内，位移比 3.6:2.4=60:40。
3. learning_fact: 两点恰在同一位置相遇；objects: meeting 替换两点；check: 两点终点坐标相同。
4. learning_fact: 时间为 2 小时；objects: formula/note 创建；check: encounter_time(200,60,40)==2，单位 km/(km/h)=h。

验收状态：动态图层、交点瞬间、字幕布局与帧边界均需实际渲染审阅。
