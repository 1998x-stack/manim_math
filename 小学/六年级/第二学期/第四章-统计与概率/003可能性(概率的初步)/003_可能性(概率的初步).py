from manim import *

class 可能性(概率的初步)Animation(Scene):
    """可能性(概率的初步)的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("可能性(概率的初步)", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("P(事件) = 事件发生的结果数 / 总结果数")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Circle, Rectangle, Text, MathTex, VGroup, Transform, FadeIn
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 003_可能性(概率的初步).py 可能性(概率的初步)Animation
    pass
