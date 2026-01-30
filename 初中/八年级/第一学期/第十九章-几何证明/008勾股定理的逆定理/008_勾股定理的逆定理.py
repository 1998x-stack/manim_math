from manim import *

class 勾股定理的逆定理Animation(Scene):
    """勾股定理的逆定理的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("勾股定理的逆定理", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("若 a² + b² = c²，则 △ABC 是直角三角形，且∠C = 90°")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Polygon, RightAngle, ...
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 008_勾股定理的逆定理.py 勾股定理的逆定理Animation
    pass
