from manim import *

class 棱锥Animation(Scene):
    """棱锥的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("棱锥", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("体积：V = ⅓S底 · h")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Pyramid, Cone, Polygon3D, Line3D, Dot3D, Surface, Text3D, ThreeDAxes
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 003_棱锥.py 棱锥Animation
    pass
