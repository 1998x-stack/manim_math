from manim import *

class 古典概型Animation(Scene):
    """古典概型的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("古典概型", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("P(A) = m/n = A包含的基本事件数/总基本事件数")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Dice, Coin, Circle, Rectangle, Dot, Text, MathTex, VGroup
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 002_古典概型.py 古典概型Animation
    pass
