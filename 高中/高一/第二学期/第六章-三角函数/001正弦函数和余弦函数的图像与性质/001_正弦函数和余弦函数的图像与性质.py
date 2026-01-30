from manim import *

class 正弦函数和余弦函数的图像与性质Animation(Scene):
    """正弦函数和余弦函数的图像与性质的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("正弦函数和余弦函数的图像与性质", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("y = sin x：定义域R，值域[-1,1]，周期2π")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Axes, FunctionGraph, Dot, DashedLine, MathTex, Text, VGroup
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 001_正弦函数和余弦函数的图像与性质.py 正弦函数和余弦函数的图像与性质Animation
    pass
