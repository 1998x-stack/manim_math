from manim import *

class 圆锥的侧面积与全面积Animation(Scene):
    """圆锥的侧面积与全面积的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("圆锥的侧面积与全面积", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("侧面积：S侧 = πrl（l为母线长）")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: Cone, Circle, Sector, Line, MathTex, Text, Arrow
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 012_圆锥的侧面积与全面积.py 圆锥的侧面积与全面积Animation
    pass
