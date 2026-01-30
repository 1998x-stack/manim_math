from manim import *

class 位置的表示方法(数对)Animation(Scene):
    """位置的表示方法(数对)的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("位置的表示方法(数对)", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("(列,行)")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: NumberPlane, Dot, Text, Arrow, VGroup, Line, FadeIn
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 003_位置的表示方法(数对).py 位置的表示方法(数对)Animation
    pass
