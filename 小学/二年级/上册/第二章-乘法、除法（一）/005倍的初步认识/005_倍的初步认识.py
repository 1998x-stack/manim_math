from manim import *

class 倍的初步认识Animation(Scene):
    """倍的初步认识的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("倍的初步认识", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("5的3倍 = 5 × 3 = 15")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Rectangle, VGroup, MathTex, Arrow, Brace, Text, Indicate
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 005_倍的初步认识.py 倍的初步认识Animation
    pass
