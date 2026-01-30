from manim import *

class 平面的基本性质Animation(Scene):
    """平面的基本性质的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("平面的基本性质", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("公理1：A ∈ l, B ∈ l, A ∈ α, B ∈ α ⇒ l ⊂ α")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Surface, Polygon3D, Line3D, Dot3D, Text3D, Arrow3D, ThreeDAxes
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 001_平面的基本性质.py 平面的基本性质Animation
    pass
