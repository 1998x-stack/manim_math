from manim import *

class 图形的放大与缩小Animation(Scene):
    """图形的放大与缩小的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("图形的放大与缩小", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("按比例k放大: 边长×k, 面积×k²")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Polygon, Text, VGroup, Transform, Scale, Indicate
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 003_图形的放大与缩小.py 图形的放大与缩小Animation
    pass
