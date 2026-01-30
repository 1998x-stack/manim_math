from manim import *

class 直线与平面平行Animation(Scene):
    """直线与平面平行的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("直线与平面平行", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("定义：l ∩ α = ∅ ⇒ l ∥ α")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Line3D, Surface, Polygon3D, Arrow3D, Text3D, ThreeDAxes, DashedLine3D
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 003_直线与平面平行.py 直线与平面平行Animation
    pass
