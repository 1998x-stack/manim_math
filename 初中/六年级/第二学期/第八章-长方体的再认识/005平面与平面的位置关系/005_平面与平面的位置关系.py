from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class PlanePlaneRelationshipAnimation(Scene):
    """平面与平面的位置关系的Manim动画演示"""
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        PLANE_COLOR = BLUE
        HIGHLIGHT_COLOR = YELLOW
        TEXT_COLOR = WHITE
        
        # 标题
        title = Text("平面与平面的位置关系", font="Noto Sans CJK SC", font_size=36, color=HIGHLIGHT_COLOR)
        title.move_to(UP * 6.5)
        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.wait(1)
        
        # 创建3D场景用于展示平面关系
        # 首先展示两个平行平面
        plane1 = Rectangle(width=4, height=3, color=PLANE_COLOR, fill_opacity=0.3)
        plane1.shift(IN * 0.5)  # 移到前面
        plane1.shift(LEFT * 1.5)
        
        plane2 = Rectangle(width=4, height=3, color=PLANE_COLOR, fill_opacity=0.3)
        plane2.shift(IN * -0.5)  # 移到后面
        plane2.shift(LEFT * 1.5)
        
        # 平行关系标签
        parallel_label = Tex(r"$\alpha \parallel \beta$", font_size=32).next_to(plane1, RIGHT, buff=0.5)
        
        # 动画序列 - 展示平行平面
        self.play(Create(plane1), Create(plane2))
        self.play(Write(parallel_label))
        self.wait(2)
        
        # 清除平行平面，准备展示相交平面
        self.play(
            FadeOut(plane1),
            FadeOut(plane2),
            FadeOut(parallel_label)
        )
        
        # 展示两个相交平面
        # 第一个平面（水平）
        intersecting_plane1 = Rectangle(width=4, height=4, color=PLANE_COLOR, fill_opacity=0.3)
        intersecting_plane1.shift(LEFT * 1.5)
        
        # 第二个平面（垂直于第一个）
        intersecting_plane2 = Rectangle(width=4, height=4, color=GREEN, fill_opacity=0.3)
        intersecting_plane2.rotate(PI/2, axis=RIGHT)  # 旋转90度使其垂直
        intersecting_plane2.shift(LEFT * 1.5)
        
        # 相交线
        intersection_line = Line(
            start=LEFT * 1.5 + DOWN * 1.5,
            end=LEFT * 1.5 + UP * 1.5,
            color=YELLOW,
            stroke_width=6
        )
        
        # 相交关系标签
        intersect_label = Tex(r"$\alpha \cap \beta = l$", font_size=32).next_to(intersecting_plane1, RIGHT, buff=0.5)
        
        # 动画序列 - 展示相交平面
        self.play(Create(intersecting_plane1))
        self.play(Create(intersecting_plane2))
        self.play(Create(intersection_line), Write(intersect_label))
        self.wait(2)
        
        # 最后展示垂直平面的情况
        # 清除之前的图形
        self.play(
            FadeOut(intersecting_plane1),
            FadeOut(intersecting_plane2),
            FadeOut(intersection_line),
            FadeOut(intersect_label)
        )
        
        # 创建垂直平面
        vertical_plane1 = Rectangle(width=4, height=3, color=PLANE_COLOR, fill_opacity=0.3)
        vertical_plane1.shift(LEFT * 1.5)
        
        vertical_plane2 = Rectangle(width=4, height=3, color=RED, fill_opacity=0.3)
        vertical_plane2.rotate(PI/2, axis=RIGHT)  # 旋转90度使其垂直
        vertical_plane2.shift(LEFT * 1.5)
        
        # 垂直关系标签
        perpendicular_label = Tex(r"$\alpha \perp \beta$", font_size=32).next_to(vertical_plane1, RIGHT, buff=0.5)
        
        # 动画序列 - 展示垂直平面
        self.play(Create(vertical_plane1))
        self.play(Create(vertical_plane2))
        self.play(Write(perpendicular_label))
        self.wait(2)
        
        # 添加结论文本
        conclusion = Text(
            "结论：两平面位置关系\n1. 平行：无公共点\n2. 相交：一条公共直线\n3. 垂直：特殊相交", 
            font="Noto Sans CJK SC",
            font_size=24,
            color=TEXT_COLOR
        ).move_to(DOWN * 4)
        
        self.play(Write(conclusion))
        self.wait(2)
        
        # 添加作者信息
        author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(author_info, shift=DOWN * 0.2))
        self.wait(2)
        
if __name__ == "__main__":
    # 运行命令: manim -pql 005_平面与平面的位置关系.py 平面与平面的位置关系Animation
    pass
