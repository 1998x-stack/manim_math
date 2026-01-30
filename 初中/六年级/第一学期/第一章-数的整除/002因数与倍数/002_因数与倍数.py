from manim import *

class 因数与倍数Animation(Scene):
    """因数与倍数的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("因数与倍数", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("若 a = b × q（q为正整数），则b是a的因数，a是b的倍数")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: NumberLine, Dot, MathTex, Arrow, Table, VGroup, Text, SurroundingRectangle
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 002_因数与倍数.py 因数与倍数Animation
    pass
