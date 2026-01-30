from manim import *

class 解直角三角形的应用Animation(Scene):
    """解直角三角形的应用的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("解直角三角形的应用", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("坡度 i = tan α = 垂直高度/水平距离")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Polygon, RightAngle, Angle, Line, DashedLine, MathTex, Text, ImageMobject, Arc
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 005_解直角三角形的应用.py 解直角三角形的应用Animation
    pass
