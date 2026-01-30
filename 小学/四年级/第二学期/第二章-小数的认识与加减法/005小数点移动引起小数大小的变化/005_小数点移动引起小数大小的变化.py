from manim import *

class 小数点移动引起小数大小的变化Animation(Scene):
    """小数点移动引起小数大小的变化的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("小数点移动引起小数大小的变化", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("小数点右移1位→扩大10倍")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: MathTex, Arrow, Dot, Text, VGroup, Transform, Scale
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 005_小数点移动引起小数大小的变化.py 小数点移动引起小数大小的变化Animation
    pass
