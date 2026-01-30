from manim import *

class 素数与合数Animation(Scene):
    """素数与合数的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("素数与合数", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("素数定义：因数只有1和p本身")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: NumberLine, Circle, MathTex, VGroup, Text, Table, Cross, Checkmark, ColoredRectangle
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 003_素数与合数.py 素数与合数Animation
    pass
