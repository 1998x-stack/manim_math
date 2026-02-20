"""
一元二次方程的概念 - Quadratic Equation Concept Animation
使用 Manim 创建的初中数学教学视频

内容: 一元二次方程的定义、标准形式、系数意义
目标观众: 初中学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class 一元二次方程的概念Animation(Scene):
    """
    一元二次方程概念教学动画场景
    
    场景顺序:
    1. 开场介绍
    2. 一元二次方程定义
    3. 一般形式展示  
    4. 系数解释
    5. 对比其他方程
    6. 总结回顾
    """
    
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        
        self.COLOR_PRIMARY = "#3498db"      
        self.COLOR_SECONDARY = "#2ecc71"    
        self.COLOR_HIGHLIGHT = "#f1c40f"    
        self.COLOR_AUXILIARY = "#95a5a6"    
        self.COLOR_AUTHOR = "#e74c3c"       
        
        self.setup_geometry()
        
        self.show_opening()
        self.show_definition()
        self.show_general_form()
        self.show_coefficient_explanation()
        self.show_comparison()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化几何布局和定位点"""
        self.TOP_REGION_Y = 7.0     
        self.CONTENT_REGION_Y = 2.0 
        self.BOTTOM_REGION_Y = -5.0 
        
        self.VERTICAL_SPACING = 1.0
        self.HORIZONTAL_CENTER = 0.0
        self.LEFT_SIDE = -3.5
        self.RIGHT_SIDE = 3.5
        
        self.SAFE_LEFT = -4.0
        self.SAFE_RIGHT = 4.0
        self.SAFE_TOP = 7.5
        self.SAFE_BOTTOM = -7.5
        
        print("✓ 几何布局初始化完成")
    
    def show_opening(self):
        """场景1: 开场介绍"""
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_AUTHOR
        ).move_to(UP * self.TOP_REGION_Y + LEFT * 0.5)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.5)
        
        title = Text(
            "一元二次方程的概念",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * (self.TOP_REGION_Y - 1.2))
        
        subtitle = Text(
            "Quadratic Equation Concept",
            font="Arial",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * (self.TOP_REGION_Y - 2.0))
        
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(subtitle), run_time=0.5)
        
        decoration = VGroup()
        for i in range(5):
            dot = Dot(
                point=np.array([
                    -2 + i * 1.0, 
                    self.TOP_REGION_Y - 2.8, 
                    0
                ]),
                radius=0.08,
                color=self.COLOR_PRIMARY
            )
            decoration.add(dot)
        
        self.play(LaggedStart(*[Create(dot) for dot in decoration], lag_ratio=0.2), run_time=1.0)
        
        self.wait(1.5)
        
        self.play(
            FadeOut(decoration),
            FadeOut(subtitle),
            title.animate.move_to(UP * 6.5).scale(0.8),
            run_time=0.8
        )
    
    def show_definition(self):
        """场景2: 一元二次方程定义"""
        definition_text = Text(
            "只含有一个未知数，\n且未知数的最高次数是2的\n整式方程叫做一元二次方程",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_PRIMARY,
            line_spacing=1.2
        ).move_to(UP * self.CONTENT_REGION_Y)
        
        self.play(Write(definition_text), run_time=2.0)
        self.wait(1.0)
        
        word1 = Text(
            "一个未知数", 
            font="Noto Sans CJK SC", 
            font_size=32, 
            color=self.COLOR_HIGHLIGHT
        ).next_to(definition_text, DOWN, buff=0.8)
        
        word2 = Text(
            "最高次数是2", 
            font="Noto Sans CJK SC",
            font_size=32, 
            color=self.COLOR_HIGHLIGHT
        ).next_to(word1, DOWN, buff=0.5)
        
        word3 = Text(
            "整式方程", 
            font="Noto Sans CJK SC", 
            font_size=32, 
            color=self.COLOR_HIGHLIGHT
        ).next_to(word2, DOWN, buff=0.5)
        
        self.play(
            Create(SurroundingRectangle(word1, color=self.COLOR_HIGHLIGHT, buff=0.1)),
            Write(word1),
            run_time=0.8
        )
        self.wait(0.8)
        
        self.play(
            Create(SurroundingRectangle(word2, color=self.COLOR_HIGHLIGHT, buff=0.1)),
            Write(word2),
            run_time=0.8
        )
        self.wait(0.8)
        
        self.play(
            Create(SurroundingRectangle(word3, color=self.COLOR_HIGHLIGHT, buff=0.1)),
            Write(word3),
            run_time=0.8
        )
        self.wait(1.5)
        
        self.play(
            FadeOut(word1), 
            FadeOut(word2), 
            FadeOut(word3),
            FadeOut(SurroundingRectangle(word1).set_opacity(0)),
            FadeOut(SurroundingRectangle(word2).set_opacity(0)),
            FadeOut(SurroundingRectangle(word3).set_opacity(0)),
            run_time=0.5
        )
    
    def show_general_form(self):
        """场景3: 一般形式展示"""
        general_form = MathTex(
            "ax^2", "+", "bx", "+", "c", "=", "0", 
            color=WHITE,
            font_size=42
        ).move_to(UP * self.CONTENT_REGION_Y)
        
        condition = MathTex(
            "(a \\neq 0)", 
            color=self.COLOR_HIGHLIGHT,
            font_size=32
        ).next_to(general_form, DOWN, buff=0.5)
        
        quad_term = general_form[0]  
        lin_term = general_form[2]   
        const_term = general_form[4] 
        
        self.play(Write(general_form), run_time=1.5)
        self.play(Write(condition), run_time=0.8)
        self.wait(1.0)
        
        quad_rect = SurroundingRectangle(quad_term, color=self.COLOR_HIGHLIGHT, buff=0.1)
        quad_label = Text(
            "二次项", 
            font="Noto Sans CJK SC", 
            font_size=24, 
            color=self.COLOR_HIGHLIGHT
        ).next_to(quad_rect, UP, buff=0.2)
        
        self.play(
            Create(quad_rect),
            Write(quad_label),
            run_time=0.8
        )
        self.wait(0.8)
        
        lin_rect = SurroundingRectangle(lin_term, color=self.COLOR_SECONDARY, buff=0.1)
        lin_label = Text(
            "一次项", 
            font="Noto Sans CJK SC", 
            font_size=24, 
            color=self.COLOR_SECONDARY
        ).next_to(lin_rect, UP, buff=0.2)
        
        self.play(
            ReplacementTransform(quad_rect, lin_rect),
            ReplacementTransform(quad_label, lin_label),
            run_time=0.8
        )
        self.wait(0.8)
        
        const_rect = SurroundingRectangle(const_term, color=self.COLOR_AUXILIARY, buff=0.1)
        const_label = Text(
            "常数项", 
            font="Noto Sans CJK SC", 
            font_size=24, 
            color=self.COLOR_AUXILIARY
        ).next_to(const_rect, UP, buff=0.2)
        
        self.play(
            ReplacementTransform(lin_rect, const_rect),
            ReplacementTransform(lin_label, const_label),
            run_time=0.8
        )
        self.wait(1.0)
        
        full_equation = VGroup(general_form, condition)
        self.play(
            FadeOut(const_rect),
            FadeOut(const_label),
            full_equation.animate.move_to(UP * (self.CONTENT_REGION_Y - 1.0)).scale(0.9),
            run_time=0.8
        )
    
    def show_coefficient_explanation(self):
        """场景4: 系数解释"""
        general_form = MathTex(
            "ax^2", "+", "bx", "+", "c", "=", "0", 
            color=WHITE,
            font_size=36
        ).move_to(UP * (self.CONTENT_REGION_Y + 1.0))
        
        coeff_a = VGroup(
            MathTex("a", color=self.COLOR_HIGHLIGHT, font_size=40),
            Text(": 二次项系数", font="Noto Sans CJK SC", font_size=28, color=WHITE)
        ).arrange(RIGHT, buff=0.3).move_to(UP * self.CONTENT_REGION_Y)
        
        coeff_b = VGroup(
            MathTex("b", color=self.COLOR_SECONDARY, font_size=40),
            Text(": 一次项系数", font="Noto Sans CJK SC", font_size=28, color=WHITE)
        ).arrange(RIGHT, buff=0.3).move_to(UP * (self.CONTENT_REGION_Y - 1.2))
        
        coeff_c = VGroup(
            MathTex("c", color=self.COLOR_AUXILIARY, font_size=40),
            Text(": 常数项", font="Noto Sans CJK SC", font_size=28, color=WHITE)
        ).arrange(RIGHT, buff=0.3).move_to(UP * (self.CONTENT_REGION_Y - 2.4))
        
        a_condition = MathTex(
            "a \\neq 0", 
            color=self.COLOR_HIGHLIGHT,
            font_size=36
        ).move_to(UP * (self.CONTENT_REGION_Y - 3.6))
        
        condition_exp = Text(
            "这是关键条件！", 
            font="Noto Sans CJK SC", 
            font_size=28, 
            color=self.COLOR_HIGHLIGHT
        ).next_to(a_condition, DOWN, buff=0.3)
        
        self.play(TransformFromCopy(general_form[0][0:1], coeff_a[0]))
        self.play(Write(coeff_a[1]), run_time=0.6)
        self.wait(1.0)
        
        self.play(TransformFromCopy(general_form[2][0:1], coeff_b[0]))
        self.play(Write(coeff_b[1]), run_time=0.6)
        self.wait(1.0)
        
        self.play(TransformFromCopy(general_form[4], coeff_c[0]))
        self.play(Write(coeff_c[1]), run_time=0.6)
        self.wait(1.0)
        
        self.play(Write(a_condition), run_time=0.8)
        self.play(Write(condition_exp), run_time=0.6)
        
        self.play(
            Flash(a_condition, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=1.0
        )
        self.wait(1.5)
    
    def show_comparison(self):
        """场景5: 对比其他方程"""
        quadratic_eq = MathTex(
            "ax^2 + bx + c = 0", 
            color=self.COLOR_HIGHLIGHT,
            font_size=36
        ).move_to(UP * (self.CONTENT_REGION_Y - 0.5))
        
        linear_eq = MathTex(
            "ax + b = 0", 
            color=self.COLOR_SECONDARY,
            font_size=36
        ).move_to(UP * (self.CONTENT_REGION_Y - 1.8))
        
        cubic_eq = MathTex(
            "ax^3 + bx^2 + cx + d = 0", 
            color=self.COLOR_AUXILIARY,
            font_size=36
        ).move_to(UP * (self.CONTENT_REGION_Y - 3.1))
        
        comparison_title = Text(
            "对比不同类型的方程", 
            font="Noto Sans CJK SC", 
            font_size=32, 
            color=WHITE
        ).move_to(UP * (self.CONTENT_REGION_Y + 1.0))
        
        self.play(Write(comparison_title), run_time=0.8)
        self.wait(0.5)
        
        self.play(Write(quadratic_eq), run_time=1.0)
        self.wait(0.5)
        
        self.play(Write(linear_eq), run_time=1.0)
        self.wait(0.5)
        
        self.play(Write(cubic_eq), run_time=1.0)
        self.wait(1.0)
        
        quad_highlights = VGroup(
            SurroundingRectangle(quadratic_eq[0][0:4], color=self.COLOR_HIGHLIGHT, buff=0.1),  
            Text("二次项", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_HIGHLIGHT)
                .next_to(quadratic_eq[0][0:4], DOWN, buff=0.2)
        )
        
        linear_highlights = VGroup(
            Text("无二次项", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_SECONDARY)
                .next_to(linear_eq, DOWN, buff=0.2)
        )
        
        cubic_highlights = VGroup(
            Text("三次项", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_AUXILIARY)
                .next_to(cubic_eq[0][0:4], DOWN, buff=0.2)
        )
        
        self.play(Create(quad_highlights[0]), Write(quad_highlights[1]), run_time=0.8)
        self.wait(0.8)
        
        self.play(Write(linear_highlights[0]), run_time=0.8)
        self.wait(0.8)
        
        self.play(Write(cubic_highlights[0]), run_time=0.8)
        self.wait(1.5)
    
    def show_summary(self):
        """场景6: 总结与回顾"""
        key_points = VGroup(
            Text("✓ 只含一个未知数", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_PRIMARY),
            Text("✓ 最高次数为2", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_PRIMARY),
            Text("✓ 标准形式: ax²+bx+c=0", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_PRIMARY),
            Text("✓ a≠0 (关键条件)", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_HIGHLIGHT)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 1.0)
        
        final_formula = MathTex(
            "ax^2 + bx + c = 0 \\quad (a \\neq 0)", 
            color=WHITE,
            font_size=40
        ).move_to(UP * (self.CONTENT_REGION_Y - 2.5))
        
        final_author = Text(
            "上海初高中数学直通车", 
            font="Noto Sans CJK SC", 
            font_size=32, 
            color=self.COLOR_AUTHOR
        ).move_to(UP * (self.BOTTOM_REGION_Y + 1.0))
        
        follow_prompt = Text(
            "@emptyandcalm", 
            font="Noto Sans CJK SC", 
            font_size=28, 
            color=GRAY_A
        ).next_to(final_author, DOWN, buff=0.3)
        
        subscribe_msg = Text(
            "关注我，获得更多数学技巧!", 
            font="Noto Sans CJK SC", 
            font_size=26, 
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * (self.BOTTOM_REGION_Y - 1.0))
        
        self.play(Write(final_formula), run_time=1.0)
        self.wait(0.5)
        
        for point in key_points:
            self.play(Write(point), run_time=0.8)
            self.wait(0.4)
        
        self.wait(1.5)
        
        self.play(Write(final_author), run_time=0.8)
        self.play(Write(follow_prompt), run_time=0.6)
        self.play(Write(subscribe_msg), run_time=0.8)
        
        self.play(
            Flash(final_formula, color=self.COLOR_HIGHLIGHT, flash_radius=0.8),
            run_time=1.5
        )
        
        self.wait(2.0)


if __name__ == "__main__":
    # 运行命令: manim -pql 001_一元二次方程的概念.py 一元二次方程的概念Animation
    scene = 一元二次方程的概念Animation()
    scene.render()
    print("渲染完成！")
