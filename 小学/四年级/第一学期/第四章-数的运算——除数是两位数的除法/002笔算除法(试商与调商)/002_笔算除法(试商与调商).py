from manim import *

class 笔算除法(试商与调商)Animation(Scene):
    """笔算除法(试商与调商)的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("笔算除法(试商与调商)", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("试商:看除数最高位")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: MathTex, VGroup, Rectangle, Line, Arrow, Text, Write, Transform
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 002_笔算除法(试商与调商).py 笔算除法(试商与调商)Animation
    pass
