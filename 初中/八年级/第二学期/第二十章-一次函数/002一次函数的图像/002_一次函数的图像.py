from manim import *

class 一次函数的图像Animation(Scene):
    """一次函数的图像的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("一次函数的图像", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("与y轴交点：(0, b)")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Axes, FunctionGraph, Dot, Line, MathTex, Arrow, Text
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 002_一次函数的图像.py 一次函数的图像Animation
    pass
