# 007 两集合容斥｜五年级起
来源：自拟偏好计数。条件：数学 A 有 12 人、科学 B 有 10 人、交集有 4 人；只数学 8、只科学 6，喜欢至少一门 8+4+6=18 人。未给出班级总人数，因此不能推断两者都不喜欢的人数。韦恩图仅展示集合的三块分区，不以圆的面积代表人数。

## 镜头与核验
1. learning_fact: 给出 12、10、4；objects: title/question 创建；check: 两个圈的总数为 8+4=12、4+6=10。
2. learning_fact: 可见三块分区 8、4、6；objects: left/right/counts/captions 创建；motion: 数字逐一出现；check: 中央 4 处于交集，8 与 6 在互斥区域。
3. learning_fact: 直接相加 22 重复计算交集；objects: wrong/correction 创建；motion: 错式变淡但不作为正确结论；check: 22-4=18。
4. learning_fact: 合计 18；objects: answer 创建；check: union_count(12,10,4)==18，交集不得大于任一集合。

验收状态：只对给定有限人数做确切推理，字体、重叠区域位置、渲染帧仍待检查。
