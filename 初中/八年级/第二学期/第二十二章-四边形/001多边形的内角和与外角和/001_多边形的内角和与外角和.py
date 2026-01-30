from manim import *

class 多边形的内角和与外角和Animation(Scene):
    """多边形的内角和与外角和的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("多边形的内角和与外角和", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("n边形内角和 = (n-2) × 180°")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Polygon, Angle, MathTex, Text, DashedLine, Arc
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 001_多边形的内角和与外角和.py 多边形的内角和与外角和Animation
    pass
