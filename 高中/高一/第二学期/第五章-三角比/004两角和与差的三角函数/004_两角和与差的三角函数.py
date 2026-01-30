from manim import *

class 两角和与差的三角函数Animation(Scene):
    """两角和与差的三角函数的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("两角和与差的三角函数", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("cos(α + β) = cos α cos β - sin α sin β")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Axes, Circle, Dot, Line, Angle, MathTex, Text, VGroup, Transform
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 004_两角和与差的三角函数.py 两角和与差的三角函数Animation
    pass
