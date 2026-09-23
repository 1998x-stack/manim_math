# 008 方格最短路径｜五至六年级
来源：自拟 3 右 2 上的网格。条件：只能沿网格线向右或向上，每步长度相同，不走回头路；最短路径恰有 5 步，其中 2 次向上，数量 C(5,2)=10。路径数 F(x,y)=F(x-1,y)+F(x,y-1)（非负整数坐标，边界起点 F(0,0)=1，越界视为 0）。若允许倒退，则不能使用此计数模型。

## 镜头与核验
1. learning_fact: 明确 3 右 2 上与最短路径；objects: title/subtitle/edges 创建；check: 网格有 4 列交点、3 行交点。
2. learning_fact: 每个交点的路径数依赖左/下；objects: 每个 disk/number 按 x+y 递增出现；motion: 对角线序填数；check: 首点为 1，终点 table[2][3]=10；边界行列均为 1。
3. learning_fact: 黄色实例是一条有效最短路径；objects: route 创建；motion: 依次沿边 (0,0)→(1,0)→(2,0)→(2,1)→(3,1)→(3,2)；check: 3 次右、2 次上，不遮盖节点数字。
4. learning_fact: 数量 10；objects: clue/answer 创建；check: path_table(3,2)[2][3]==comb(5,2)==10。

验收状态：需要运行数学测试、真实预览及关键帧，确认路径高亮不遮挡表格值。
