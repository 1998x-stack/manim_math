from manim import *

class 数的读写与组成Animation(Scene):
    """数的读写与组成的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("数的读写与组成", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("304 = 3个百 + 0个十 + 4个一")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Text, MathTex, Table, VGroup, Rectangle, Arrow
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 002_数的读写与组成.py 数的读写与组成Animation
    pass
