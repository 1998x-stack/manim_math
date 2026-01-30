from manim import *

class 线段、射线、直线Animation(Scene):
    """线段、射线、直线的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("线段、射线、直线", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("线段AB:有限长度")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Line, Arrow, Dot, Text, VGroup, DashedLine, FadeIn, GrowArrow
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 001_线段、射线、直线.py 线段、射线、直线Animation
    pass
