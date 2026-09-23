# 004 等底等高｜五年级起
来源：基础面积定理。条件：底边 AB 从 (-3,-2) 至 (3,-2)，长度 6；顶点 P 在 y=2 的平行线上，垂距始终 4；S=6×4/2=12。P 的 x 从 -2.5 连续移动到 2.5；任意中间帧均在平行线上，底与高不变。底为 0 的退化三角形不作为本例。

## 镜头与核验
1. learning_fact: 明确底不变、问面积；objects: title/given 创建；check: 坐标单位一致。
2. learning_fact: 三角形及垂高可见；objects: base/top_line/triangle/altitude/apex 创建；motion: 顶点与垂高均绑定同一 ValueTracker；check: 高的端点横坐标与顶点一致，端点在 y=-2。
3. learning_fact: 动点不改变面积；objects: lengths/result 保留；motion: P 从 -2.5 向 2.5 移动；check: 所有帧 base=6,height=4,S=12。
4. learning_fact: 总结等底等高；objects: conclusion 创建；check: triangle_area(6,4)==12，拒绝负高。

验收状态：动态几何包围盒、中文字体、公式与实际播放帧尚需渲染后审查。
