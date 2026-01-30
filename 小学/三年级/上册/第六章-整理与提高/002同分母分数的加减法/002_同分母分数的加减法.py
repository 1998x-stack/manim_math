from manim import *

class 同分母分数的加减法Animation(Scene):
    """同分母分数的加减法的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("同分母分数的加减法", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("⅓ + ⅔ = 1")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: MathTex, Circle, Rectangle, Arrow, Text, Transform, VGroup
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 002_同分母分数的加减法.py 同分母分数的加减法Animation
    pass
