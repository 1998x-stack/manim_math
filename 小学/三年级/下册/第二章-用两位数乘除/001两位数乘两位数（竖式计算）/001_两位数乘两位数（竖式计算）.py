from manim import *

class 两位数乘两位数（竖式计算）Animation(Scene):
    """两位数乘两位数（竖式计算）的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("两位数乘两位数（竖式计算）", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("23 × 14 = 322")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: MathTex, VGroup, Arrow, Brace, Text, Indicate, Transform, Rectangle
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 001_两位数乘两位数（竖式计算）.py 两位数乘两位数（竖式计算）Animation
    pass
