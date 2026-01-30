from manim import *

class 列举法求概率Animation(Scene):
    """列举法求概率的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("列举法求概率", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("步骤：①列出所有等可能结果；②数出事件A包含的结果数m；③数出总结果数n；④P(A) = m/n")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Table, Graph, Tree, Text, MathTex, Arrow, Dot
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 003_列举法求概率.py 列举法求概率Animation
    pass
