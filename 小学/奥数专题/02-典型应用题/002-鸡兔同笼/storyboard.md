# 002 鸡兔同笼｜四年级起
来源：自拟 8 头 22 腿例题。条件：鸡有 2 条腿、兔有 4 条腿，每只恰有一个头；数量为非负整数。假设全部是鸡：16 条腿；比实际少 6 条；每只兔比鸡多 2 条，故兔 3、鸡 5。无整数或不在 [2H,4H] 的腿数不得展示假解。

## 镜头与核验
1. learning_fact: 给出 H=8,L=22；objects: title/given 创建；check: 给定与模型输入相同。
2. learning_fact: 8 只鸡共 16 条腿；objects: 8 个真实的鸡图标及每只 2 条可见腿、提示、base 创建；motion: 逐只出现；check: 8×2=16。
3. learning_fact: 每替换一只兔，腿数增加 2；objects: 原 3 只鸡的同一引用用 ReplacementTransform 替换为 3 只兔，每只图标 4 条腿；motion: 变换 3 个动物；check: 剩余 5 鸡+3 兔=8 头、22 腿。
4. learning_fact: 解为鸡 5、兔 3；objects: answer/conclude 创建；check: solve_chicken_rabbit(8,22)==(5,3)。

验收状态：需实际核验字体、动物图标腿线可辨、画面包围盒和动态变换；尚不把源码交付视作渲染完成。
