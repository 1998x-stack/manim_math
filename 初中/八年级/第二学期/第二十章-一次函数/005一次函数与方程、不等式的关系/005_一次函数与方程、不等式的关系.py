from manim import *

class 一次函数与方程、不等式的关系Animation(Scene):
    """一次函数与方程、不等式的关系的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("一次函数与方程、不等式的关系", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("kx + b = 0 的解 ⟺ 图像与x轴交点横坐标")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Axes, FunctionGraph, Line, Brace, MathTex, Text, NumberLine
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 005_一次函数与方程、不等式的关系.py 一次函数与方程、不等式的关系Animation
    pass
