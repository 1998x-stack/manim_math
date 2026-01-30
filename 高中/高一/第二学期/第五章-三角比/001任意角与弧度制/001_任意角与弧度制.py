from manim import *

class 任意角与弧度制Animation(Scene):
    """任意角与弧度制的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("任意角与弧度制", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("π rad = 180°")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Circle, Arc, Angle, Line, MathTex, Text, Arrow, Sector
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 001_任意角与弧度制.py 任意角与弧度制Animation
    pass
