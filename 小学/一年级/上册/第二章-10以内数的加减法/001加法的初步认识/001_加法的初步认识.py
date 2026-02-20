from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class AdditionIntroductionAnimation(Scene):
    """加法的初步认识的Manim动画演示"""
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        CIRCLE_COLOR = BLUE
        ADDITION_COLOR = YELLOW
        TEXT_COLOR = WHITE
        
        # 标题
        title = Text("加法的初步认识", font="Noto Sans CJK SC", font_size=36, color=ADDITION_COLOR)
        title.move_to(UP * 6.5)
        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.wait(1)
        
        # 展示加法含义：合并两部分，求一共多少
        # 第一部分：左边2个圆圈
        left_circles = VGroup(*[
            Circle(radius=0.3, color=CIRCLE_COLOR, fill_opacity=1).shift(LEFT * 2 + UP * i * 0.7)
            for i in range(2)
        ])
        
        # 第二部分：右边1个圆圈
        right_circle = Circle(radius=0.3, color=CIRCLE_COLOR, fill_opacity=1).shift(RIGHT * 2)
        
        # 显示左右两部分
        self.play(
            Create(left_circles[0]),
            Create(right_circle)
        )
        self.wait(0.5)
        self.play(Create(left_circles[1]))
        self.wait(1)
        
        # 加号符号
        plus_sign = MathTex("+", color=ADDITION_COLOR, font_size=48).move_to(ORIGIN)
        self.play(Write(plus_sign))
        self.wait(1)
        
        # 等号符号
        equals_sign = MathTex("=", color=ADDITION_COLOR, font_size=48).move_to(RIGHT * 1)
        self.play(Write(equals_sign))
        self.wait(1)
        
        # 合并动画：左右圆圈移动到中间
        all_circles = VGroup(*left_circles, right_circle)
        target_positions = [
            LEFT * 0.5 + UP * 0.4,
            LEFT * 0.5 + DOWN * 0.4,
            RIGHT * 0.5
        ]
        
        # 移动圆圈到中间位置
        self.play(
            left_circles[0].animate.move_to(target_positions[0]),
            left_circles[1].animate.move_to(target_positions[1]),
            right_circle.animate.move_to(target_positions[2])
        )
        self.wait(1)
        
        # 显示结果数字
        result_number = MathTex("3", color=ADDITION_COLOR, font_size=48).move_to(RIGHT * 2.5)
        self.play(Write(result_number))
        self.wait(1)
        
        # 完整的加法公式
        full_formula = MathTex("2 + 1 = 3", color=ADDITION_COLOR, font_size=48).move_to(DOWN * 2)
        self.play(Write(full_formula))
        self.wait(2)
        
        # 添加第二个例子：1 + 3 = 4
        self.play(
            FadeOut(all_circles),
            FadeOut(result_number),
            Transform(full_formula, MathTex("1 + 3 = ?", color=ADDITION_COLOR, font_size=48).move_to(DOWN * 2))
        )
        self.wait(1)
        
        # 新的加法演示：1个圆圈和3个圆圈
        left_single_circle = Circle(radius=0.3, color=CIRCLE_COLOR, fill_opacity=1).move_to(LEFT * 2 + UP * 0.7)
        right_group_circles = VGroup(*[
            Circle(radius=0.3, color=CIRCLE_COLOR, fill_opacity=1).shift(RIGHT * 2 + UP * i * 0.7 - DOWN * 0.7)
            for i in range(3)
        ])
        
        self.play(Create(left_single_circle))
        self.play(*[Create(circle) for circle in right_group_circles])
        self.wait(1)
        
        # 合并到中间
        new_target_positions = [
            LEFT * 0.5 + UP * 0.7,
            RIGHT * 0.5 + UP * 0.2,
            RIGHT * 0.5 + DOWN * 0.3,
            RIGHT * 0.5 + DOWN * 0.8
        ]
        
        self.play(
            left_single_circle.animate.move_to(new_target_positions[0]),
            right_group_circles[0].animate.move_to(new_target_positions[1]),
            right_group_circles[1].animate.move_to(new_target_positions[2]),
            right_group_circles[2].animate.move_to(new_target_positions[3])
        )
        self.wait(1)
        
        # 显示答案
        new_result = MathTex("4", color=ADDITION_COLOR, font_size=48).move_to(RIGHT * 2.5)
        self.play(Transform(full_formula, MathTex("1 + 3 = 4", color=ADDITION_COLOR, font_size=48).move_to(DOWN * 2)))
        self.play(Write(new_result))
        self.wait(2)
        
        # 添加结论文字
        conclusion = Text(
            "加法就是把两部分合并\n求一共有多少", 
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
    # 运行命令: manim -pql 001_加法的初步认识.py AdditionIntroductionAnimation
    pass
