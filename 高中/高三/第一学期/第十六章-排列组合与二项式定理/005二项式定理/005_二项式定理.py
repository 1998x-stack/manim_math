from manim import *

class 二项式定理Animation(Scene):
    """二项式定理的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("二项式定理", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("(a+b)ⁿ = ΣC(n,k)a^(n-k)b^k")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: MathTex, Text, VGroup, Brace, Table, Triangle, Transform
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 005_二项式定理.py 二项式定理Animation
    pass
