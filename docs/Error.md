Name: manim
Version: 0.19.2(latest)
1. Chinese characters cannot be used in MathTex; Only supports LaTeX/ASCII
2. 度数符号问题：度数符号需要使用 ^\circ 或 ^{\circ} 表示，而不是直接使用 °。
3. inner_radius and outer_radius is allowed in AnnularSector and forbidden in Sector(radius only)
4. 问题仍然在LaTeX编译阶段。错误信息显示 you need another { and }，这通常表示LaTeX公式语法有问题。\over 命令在LaTeX中需要正确的分组。有双花括号 {{...}} 导致Manim解析错误
5. 新版本的Manim中Arrow类的scale()方法不再支持scale_tips参数
6. ❌ Original (causes error): Tex(r"周角 $= 360^\circ$"); ✅ Fixed: chinese = Text("周角 =", font="Noto Sans CJK SC")    math = MathTex(r"360^\circ")    VGroup(chinese, math).arrange(RIGHT)
7. corner_radius is allowed in RoundedRectangle and forbidden in Rectangle