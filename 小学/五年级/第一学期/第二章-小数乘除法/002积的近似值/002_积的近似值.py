from manim import *

class 积的近似值Animation(Scene):
    """积的近似值的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("积的近似值", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("3.1415... ≈ 3.14 (保留两位小数)")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: MathTex, NumberLine, Dot, Arrow, Text, VGroup, Transform
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 002_积的近似值.py 积的近似值Animation
    pass
