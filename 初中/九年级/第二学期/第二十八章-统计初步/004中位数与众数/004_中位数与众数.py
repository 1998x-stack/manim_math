from manim import *

class 中位数与众数Animation(Scene):
    """中位数与众数的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("中位数与众数", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("n为奇数：中位数 = 第(n+1)/2个数")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: NumberLine, Dot, MathTex, Text, Brace, SurroundingRectangle
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 004_中位数与众数.py 中位数与众数Animation
    pass
