from manim import *

class 解简易方程Animation(Scene):
    """解简易方程的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("解简易方程", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("x + 5 = 10 → x = 10 - 5 → x = 5")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: MathTex, Arrow, Brace, Text, VGroup, Transform, Indicate
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 004_解简易方程.py 解简易方程Animation
    pass
