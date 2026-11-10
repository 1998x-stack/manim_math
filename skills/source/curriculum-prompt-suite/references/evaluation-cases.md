# Skill Creator 验证场景与回归标准

正向案例：小学 001数一数核对 1–10 个对象和读数；初中 001代数式与整式的概念核对单项式系数/次数及多项式边界；高中 001集合的概念与表示核对确定性、互异性、无序性和论域。三课必须分别生成相同变量名的三份 prompt.txt、正确的 SOURCE_PROMPT 以及对应平台标记。

反例：不存在的原路径；../ 路径穿越；符号链接；多个 problem 块；非法 JSON；顶层数组；正文年级与目录不同；DURATION_S=0 或非数字；SCENE_CLASS 含空格；不合法的 QUALITY；删掉一个平台入口造成漂移；源文件改动而 index 的 Git blob SHA 没更新；存在旧视频但未渲染新成品。错误必须可见，不能静默修复或误报 pass。

评分：前五项 1/0 且全部通过才允许宣布 Prompt 工程迁移完成：全覆盖 3×N、变量一致性、目录与源一致、源数据不变、冲突透明。课程生产另验数学证明/测试、分镜生命周期、运行时真实 Scene、媒体探测与素材授权；后五项只有实际运行才能记 pass。

建议命令：python skills/source/curriculum-prompt-suite/scripts/prompt_suite.py check --root .；python -m unittest discover -s skills/source/curriculum-prompt-suite/scripts -p 'test_*.py' -v；python tools/sync_skills.py --check。
