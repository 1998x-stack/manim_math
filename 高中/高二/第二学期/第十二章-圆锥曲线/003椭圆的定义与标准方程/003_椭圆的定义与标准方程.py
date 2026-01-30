from manim import *

class 椭圆的定义与标准方程Animation(Scene):
    """椭圆的定义与标准方程的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("椭圆的定义与标准方程", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("定义：|PF₁| + |PF₂| = 2a")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Axes, Ellipse, Dot, Line, MathTex, Text, DashedLine, Brace
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 003_椭圆的定义与标准方程.py 椭圆的定义与标准方程Animation
    pass
