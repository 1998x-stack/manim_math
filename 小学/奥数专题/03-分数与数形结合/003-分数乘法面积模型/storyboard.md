# 003 分数乘法面积模型｜五年级起
来源：自拟 3/4×2/3。将一个整体等分为 4 列、3 行，先选 3 列，再在这些列中选 2 行；重叠 3×2=6 格，整体 4×3=12 格，得 6/12=1/2。条件：等面积小格，分子分母均为整数，分母正且选择量不超过分母。图形为面积份额证明，不用不等面积的格子代替。

## 镜头与核验
1. learning_fact: 提出 3/4×2/3；objects: title/prompt 创建；check: 所有公式为纯 LaTeX。
2. learning_fact: 蓝色为 3/4；objects: 12 个等大方格创建，蓝色填 9 格；motion: 分列填色；check: 3×3=9。
3. learning_fact: 上两行界定 2/3 的范围；objects: band 创建、说明替换；motion: 框选两行并将与蓝色重叠的 6 格变黄；check: 正好 6 格，不将未选列错误涂成乘积。
4. learning_fact: 乘积为 1/2；objects: answer/note 创建；check: area_product(3,4,2,3)==Fraction(1,2)。

验收状态：待语法/数学回归/AST/实际视频与截图单独核验。
