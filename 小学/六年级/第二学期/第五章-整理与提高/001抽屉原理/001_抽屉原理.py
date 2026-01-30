from manim import *

class 抽屉原理Animation(Scene):
    """抽屉原理的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("抽屉原理", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("n+1个物体, n个抽屉 → 至少有1个抽屉放≥2个")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Rectangle, Circle, Dot, Text, VGroup, Arrow, Transform
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 001_抽屉原理.py 抽屉原理Animation
    pass
