from manim import *

class 分解素因数Animation(Scene):
    """分解素因数的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("分解素因数", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("30 = 2 × 3 × 5")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: MathTex, VGroup, Arrow, Table, Tree, Text, Rectangle, AnimationGroup
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 004_分解素因数.py 分解素因数Animation
    pass
