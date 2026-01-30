from manim import *

class 特殊角的三角比值Animation(Scene):
    """特殊角的三角比值的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("特殊角的三角比值", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("sin 30° = 1/2，cos 30° = √3/2，tan 30° = √3/3")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Polygon, RightAngle, Angle, MathTex, Text, Table
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 002_特殊角的三角比值.py 特殊角的三角比值Animation
    pass
