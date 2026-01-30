from manim import *

class 复数的几何表示Animation(Scene):
    """复数的几何表示的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("复数的几何表示", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("复数z = a + bi ⟺ 点Z(a, b)")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Axes, Dot, Vector, Circle, Angle, MathTex, Text, Arc
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 002_复数的几何表示.py 复数的几何表示Animation
    pass
