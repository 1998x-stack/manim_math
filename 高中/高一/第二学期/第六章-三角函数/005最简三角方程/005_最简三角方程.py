from manim import *

class 最简三角方程Animation(Scene):
    """最简三角方程的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("最简三角方程", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("sin x = a: x = arcsin a + 2kπ 或 x = π - arcsin a + 2kπ")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Axes, FunctionGraph, Circle, Dot, Line, MathTex, Text, Intersection
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 005_最简三角方程.py 最简三角方程Animation
    pass
