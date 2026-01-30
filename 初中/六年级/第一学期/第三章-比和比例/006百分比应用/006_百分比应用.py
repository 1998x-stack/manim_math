from manim import *

class 百分比应用Animation(Scene):
    """百分比应用的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("百分比应用", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("折扣价 = 原价 × 折扣率")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: MathTex, Rectangle, VGroup, Text, Arrow, BarChart, Transform
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 006_百分比应用.py 百分比应用Animation
    pass
