# 001 高斯求和｜四年级起
来源：第一批奥数专题自拟演示题。目标：通过首尾配对求 1+2+…+100，并归纳正整数求和。画幅：9:16，深色背景；时长依实际渲染。数学规格：n 为正整数；配对公式为 n(n+1)/2；偶数项可分 n/2 组，奇数项还需处理中项；n=1 仍符合公式。用五组作示意，不能冒充全部 50 组。

## 镜头与核验
1. learning_fact: 明确求和题；objects: title/question 创建；motion: 写入题目；check: 数字 1 至 100 与最终答案一致。
2. learning_fact: 首尾相加都是 101；objects: lines[0:5] 顺次创建；motion: 前 5 组一一出现；check: 1+100…5+96 的和均为 101，文字注明仅示意。
3. learning_fact: 100 个数形成 50 对；objects: note/result 创建；motion: 显示 50×101=5050；check: arithmetic_sum(100)==5050。
4. learning_fact: 推广至一般 n；objects: general 创建并保留至结尾；check: n=1,2,3,99,100 等边界与样例。

验收状态：数学/语法/AST/实际渲染/帧审查/媒体探测均须分别记录；创建源码不代表执行完成。
