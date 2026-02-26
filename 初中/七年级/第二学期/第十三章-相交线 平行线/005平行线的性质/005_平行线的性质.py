from manim import *

class 平行线的性质Animation(Scene):
    """平行线的性质的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("平行线的性质", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = Text("两直线平行 ⟹ 同位角相等", font="Noto Sans CJK SC", font_size=36)
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Line, Angle, Arc, MathTex, VGroup, Text, Arrow
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 005_平行线的性质.py 平行线的性质Animation
    pass
