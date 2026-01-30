from manim import *

class 分数乘整数和分数乘分数Animation(Scene):
    """分数乘整数和分数乘分数的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("分数乘整数和分数乘分数", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("a/b × c/d = (a×c)/(b×d)")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: MathTex, Rectangle, Line, Arrow, Text, VGroup, Transform
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 001_分数乘整数和分数乘分数.py 分数乘整数和分数乘分数Animation
    pass
