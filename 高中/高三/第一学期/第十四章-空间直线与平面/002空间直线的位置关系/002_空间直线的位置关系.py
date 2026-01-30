from manim import *

class 空间直线的位置关系Animation(Scene):
    """空间直线的位置关系的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("空间直线的位置关系", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("相交：有唯一公共点")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Line3D, Dot3D, Angle3D, ThreeDAxes, Surface, Text3D, DashedLine3D
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 002_空间直线的位置关系.py 空间直线的位置关系Animation
    pass
