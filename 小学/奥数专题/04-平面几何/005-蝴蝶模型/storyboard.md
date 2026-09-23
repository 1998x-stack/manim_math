# 005 梯形蝴蝶模型｜五至六年级
来源：梯形对角线面积关系。条件：AB∥CD，AB=3、CD=6、高 h=4，对角线 AC 与 BD 交 O；A=(-1.5,2), B=(1.5,2), C=(3,-2), D=(-3,-2)。相似三角形 AOB 与 COD 的高及对应底比均为 1:2，面积比 1:4；本图四块面积依次为 2、4、4、8，总和 18=(3+6)×4/2。侧翼相等来自等底等高或解析面积，不把颜色示意当独立证明。仅要求非退化正底长、高。

## 镜头与核验
1. learning_fact: 给出梯形与平行条件；objects: title/given 创建；check: AB/CD 的可见数值与顶点坐标一致。
2. learning_fact: 对角线形成四块区域；objects: outline/diagonals/shapes 创建；motion: 顺序出现；check: O=A+(C-A)/3=(0,2/3)，四块无漏画、无越界。
3. learning_fact: 两翼相等、上下比 1:4；objects: markers 创建于对应三角形内部；check: butterfly_areas(3,6,4)==(2,4,8)。
4. learning_fact: S_AOB:S_COD=3²:6²；objects: relation/summary 创建；check: 面积比 2:8=1:4，总面积 18。

验收状态：需要单独运行数学回归，并在实际预览中查看数值标签是否被对角线遮挡。
