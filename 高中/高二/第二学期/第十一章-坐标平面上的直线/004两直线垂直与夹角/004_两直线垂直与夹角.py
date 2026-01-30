from manim import *

class 两直线垂直与夹角Animation(Scene):
    """两直线垂直与夹角的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("两直线垂直与夹角", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("垂直：k₁ · k₂ = -1")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Axes, Line, Angle, RightAngle, Dot, MathTex, Text, Arc
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 004_两直线垂直与夹角.py 两直线垂直与夹角Animation
    pass
