"""
不等式的基本性质 - 完整版 Manim教学动画
Inequality Properties - Full Version Teaching Animation

包含所有六大性质的详细展示
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class InequalityPropertiesFull(Scene):
    """完整版：包含全部6个性质"""
    
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.C_PRIMARY = "#3498db"
        self.C_SECONDARY = "#e74c3c"
        self.C_POSITIVE = "#2ecc71"
        self.C_NEGATIVE = "#e67e22"
        self.C_WARNING = "#f39c12"
        
        # 数轴配置
        self.nl_config = {
            "x_range": [-6, 6, 1],
            "length": 8,
            "include_numbers": True,
            "numbers_to_include": range(-6, 7),
            "font_size": 20
        }
        
        # 执行所有场景
        self.show_opening()
        self.show_property_1()  # 对称性
        self.show_property_2()  # 传递性
        self.show_property_3()  # 加法
        self.show_property_4()  # 乘正数
        self.show_property_5()  # 乘负数 ⚠️
        self.show_property_6()  # 平方
        self.show_summary()
        self.show_outro()
    
    def show_opening(self):
        """开场"""
        author = Text("上海初高中数学直通车 @emptyandcalm", font="Noto Sans CJK SC", font_size=20, color=GRAY_B).move_to(UP * 7)
        self.author_info = author
        self.play(FadeIn(author), run_time=0.3)
        
        hook1 = Text("3 > 1", font="Noto Sans CJK SC", font_size=52, color=YELLOW, weight=BOLD).move_to(UP * 3)
        hook2 = Text("两边同时乘以 -2", font="Noto Sans CJK SC", font_size=36, color=WHITE).move_to(UP * 1.5)
        hook3 = Text("会发生什么？", font="Noto Sans CJK SC", font_size=40, color=self.C_SECONDARY, weight=BOLD).move_to(ORIGIN)
        qmark = Text("?", font_size=80, color=self.C_WARNING).move_to(DOWN * 2)
        
        self.play(Write(hook1), run_time=0.8)
        self.play(FadeIn(hook2), run_time=0.6)
        self.wait(0.5)
        self.play(Write(hook3), FadeIn(qmark, scale=1.5), run_time=0.8)
        self.play(Wiggle(qmark), Flash(qmark), run_time=0.6)
        self.wait(1.2)
        self.play(FadeOut(VGroup(hook1, hook2, hook3, qmark)), run_time=0.5)
    
    def show_property_1(self):
        """性质1: 对称性"""
        title = Text("性质1：对称性", font="Noto Sans CJK SC", font_size=36, color=self.C_PRIMARY, weight=BOLD).move_to(UP * 6)
        self.play(FadeIn(title), run_time=0.5)
        
        nl = NumberLine(**self.nl_config).move_to(UP * 2.5)
        self.play(Create(nl), run_time=0.8)
        
        pos_a = nl.n2p(3)
        pos_b = nl.n2p(1)
        
        dot_a = Dot(pos_a, color=self.C_PRIMARY, radius=0.12)
        dot_b = Dot(pos_b, color=self.C_SECONDARY, radius=0.12)
        label_a = MathTex("a", color=self.C_PRIMARY, font_size=28).next_to(dot_a, UP, buff=0.2)
        label_b = MathTex("b", color=self.C_SECONDARY, font_size=28).next_to(dot_b, UP, buff=0.2)
        
        self.play(FadeIn(dot_a, scale=0.5), Write(label_a), FadeIn(dot_b, scale=0.5), Write(label_b), run_time=0.6)
        
        f1 = MathTex("a", ">", "b", font_size=40).move_to(ORIGIN)
        f1[0].set_color(self.C_PRIMARY)
        f1[2].set_color(self.C_SECONDARY)
        self.play(Write(f1), run_time=0.6)
        
        arrow1 = Arrow(pos_a + DOWN * 0.5, pos_b + DOWN * 0.5, color=YELLOW, buff=0.1, stroke_width=4)
        self.play(GrowArrow(arrow1), run_time=0.5)
        self.wait(0.5)
        
        f2 = MathTex("a", ">", "b", "\\Leftrightarrow", "b", "<", "a", font_size=40).move_to(ORIGIN)
        f2[0].set_color(self.C_PRIMARY)
        f2[2].set_color(self.C_SECONDARY)
        f2[4].set_color(self.C_SECONDARY)
        f2[6].set_color(self.C_PRIMARY)
        
        self.play(TransformMatchingTex(f1, f2), run_time=1.0)
        
        arrow2 = Arrow(pos_b + DOWN * 0.5, pos_a + DOWN * 0.5, color=self.C_SECONDARY, buff=0.1, stroke_width=4)
        self.play(Transform(arrow1, arrow2), run_time=0.8)
        
        exp = Text("不等号两边交换，方向改变", font="Noto Sans CJK SC", font_size=24, color=GRAY_A).move_to(DOWN * 3)
        self.play(FadeIn(exp), run_time=0.5)
        self.wait(1.2)
        
        self.play(FadeOut(VGroup(title, nl, dot_a, dot_b, label_a, label_b, f2, arrow1, exp)), run_time=0.5)
    
    def show_property_2(self):
        """性质2: 传递性"""
        title = Text("性质2：传递性", font="Noto Sans CJK SC", font_size=36, color=self.C_PRIMARY, weight=BOLD).move_to(UP * 6)
        self.play(FadeIn(title), run_time=0.5)
        
        nl = NumberLine(**self.nl_config).move_to(UP * 3)
        self.play(Create(nl), run_time=0.8)
        
        pos_a = nl.n2p(4)
        pos_b = nl.n2p(2)
        pos_c = nl.n2p(-1)
        
        dot_a = Dot(pos_a, color=self.C_PRIMARY, radius=0.12)
        dot_b = Dot(pos_b, color=YELLOW, radius=0.12)
        dot_c = Dot(pos_c, color=self.C_SECONDARY, radius=0.12)
        
        label_a = MathTex("a", color=self.C_PRIMARY, font_size=28).next_to(dot_a, UP, buff=0.2)
        label_b = MathTex("b", color=YELLOW, font_size=28).next_to(dot_b, UP, buff=0.2)
        label_c = MathTex("c", color=self.C_SECONDARY, font_size=28).next_to(dot_c, UP, buff=0.2)
        
        self.play(
            FadeIn(dot_a, scale=0.5), Write(label_a),
            FadeIn(dot_b, scale=0.5), Write(label_b),
            FadeIn(dot_c, scale=0.5), Write(label_c),
            run_time=1.0
        )
        
        f1 = MathTex("a", ">", "b", font_size=36).move_to(UP * 0.5)
        f1[0].set_color(self.C_PRIMARY)
        f1[2].set_color(YELLOW)
        
        f2 = MathTex("b", ">", "c", font_size=36).move_to(DOWN * 0.5)
        f2[0].set_color(YELLOW)
        f2[2].set_color(self.C_SECONDARY)
        
        self.play(Write(f1), run_time=0.6)
        self.play(Write(f2), run_time=0.6)
        
        arrow1 = Arrow(pos_a + DOWN * 0.8, pos_b + DOWN * 0.8, color=self.C_PRIMARY, buff=0.1)
        arrow2 = Arrow(pos_b + DOWN * 0.8, pos_c + DOWN * 0.8, color=YELLOW, buff=0.1)
        
        self.play(GrowArrow(arrow1), GrowArrow(arrow2), run_time=0.8)
        
        conclusion = MathTex("\\therefore", "a", ">", "c", font_size=40).move_to(DOWN * 2)
        conclusion[1].set_color(self.C_PRIMARY)
        conclusion[3].set_color(self.C_SECONDARY)
        
        self.play(Write(conclusion), run_time=0.8)
        
        arrow_direct = Arrow(pos_a + DOWN * 1.5, pos_c + DOWN * 1.5, color=self.C_WARNING, buff=0.1, stroke_width=6)
        self.play(GrowArrow(arrow_direct), run_time=0.6)
        self.play(Indicate(arrow_direct, scale_factor=1.2), run_time=0.5)
        
        exp = Text("大于关系可以传递", font="Noto Sans CJK SC", font_size=24, color=GRAY_A).move_to(DOWN * 4)
        self.play(FadeIn(exp), run_time=0.5)
        self.wait(1.2)
        
        self.play(FadeOut(VGroup(title, nl, dot_a, dot_b, dot_c, label_a, label_b, label_c, f1, f2, conclusion, arrow1, arrow2, arrow_direct, exp)), run_time=0.5)
    
    def show_property_3(self):
        """性质3: 加法"""
        title = Text("性质3：加法法则", font="Noto Sans CJK SC", font_size=36, color=self.C_PRIMARY, weight=BOLD).move_to(UP * 6)
        self.play(FadeIn(title), run_time=0.5)
        
        nl1 = NumberLine(**self.nl_config).move_to(UP * 3)
        self.play(Create(nl1), run_time=0.8)
        
        pos_a = nl1.n2p(3)
        pos_b = nl1.n2p(1)
        
        dot_a1 = Dot(pos_a, color=self.C_PRIMARY, radius=0.12)
        dot_b1 = Dot(pos_b, color=self.C_SECONDARY, radius=0.12)
        label_a1 = MathTex("a", color=self.C_PRIMARY, font_size=28).next_to(dot_a1, UP, buff=0.2)
        label_b1 = MathTex("b", color=self.C_SECONDARY, font_size=28).next_to(dot_b1, UP, buff=0.2)
        
        self.play(FadeIn(dot_a1, scale=0.5), Write(label_a1), FadeIn(dot_b1, scale=0.5), Write(label_b1), run_time=0.6)
        
        f1 = MathTex("a", ">", "b", font_size=36).move_to(UP * 1)
        f1[0].set_color(self.C_PRIMARY)
        f1[2].set_color(self.C_SECONDARY)
        self.play(Write(f1), run_time=0.6)
        
        add_text = Text("两边同时 +2", font="Noto Sans CJK SC", font_size=28, color=self.C_POSITIVE).move_to(ORIGIN)
        self.play(FadeIn(add_text), run_time=0.5)
        self.wait(0.5)
        
        nl2 = NumberLine(**self.nl_config).move_to(DOWN * 2)
        self.play(FadeIn(nl2), run_time=0.6)
        
        pos_a2 = nl2.n2p(5)
        pos_b2 = nl2.n2p(3)
        
        dot_a2 = Dot(pos_a2, color=self.C_PRIMARY, radius=0.12)
        dot_b2 = Dot(pos_b2, color=self.C_SECONDARY, radius=0.12)
        label_a2 = MathTex("a+2", color=self.C_PRIMARY, font_size=28).next_to(dot_a2, UP, buff=0.2)
        label_b2 = MathTex("b+2", color=self.C_SECONDARY, font_size=28).next_to(dot_b2, UP, buff=0.2)
        
        self.play(TransformFromCopy(dot_a1, dot_a2), TransformFromCopy(dot_b1, dot_b2), TransformFromCopy(label_a1, label_a2), TransformFromCopy(label_b1, label_b2), run_time=1.0)
        
        f2 = MathTex("a+2", ">", "b+2", font_size=36).move_to(DOWN * 4.5)
        f2[0].set_color(self.C_PRIMARY)
        f2[2].set_color(self.C_SECONDARY)
        self.play(Write(f2), run_time=0.6)
        
        exp = Text("两边同加，不等号不变", font="Noto Sans CJK SC", font_size=24, color=GRAY_A).move_to(DOWN * 6)
        self.play(FadeIn(exp), run_time=0.5)
        self.wait(1.2)
        
        self.play(FadeOut(VGroup(title, nl1, nl2, dot_a1, dot_b1, dot_a2, dot_b2, label_a1, label_b1, label_a2, label_b2, f1, f2, add_text, exp)), run_time=0.5)
    
    def show_property_4(self):
        """性质4: 乘正数"""
        title = Text("性质4：乘以正数", font="Noto Sans CJK SC", font_size=36, color=self.C_PRIMARY, weight=BOLD).move_to(UP * 6)
        self.play(FadeIn(title), run_time=0.5)
        
        nl1 = NumberLine(**self.nl_config).move_to(UP * 3)
        self.play(Create(nl1), run_time=0.8)
        
        pos_a = nl1.n2p(2)
        pos_b = nl1.n2p(1)
        
        dot_a1 = Dot(pos_a, color=self.C_PRIMARY, radius=0.12)
        dot_b1 = Dot(pos_b, color=self.C_SECONDARY, radius=0.12)
        label_a1 = MathTex("a", color=self.C_PRIMARY, font_size=28).next_to(dot_a1, UP, buff=0.2)
        label_b1 = MathTex("b", color=self.C_SECONDARY, font_size=28).next_to(dot_b1, UP, buff=0.2)
        
        self.play(FadeIn(dot_a1, scale=0.5), Write(label_a1), FadeIn(dot_b1, scale=0.5), Write(label_b1), run_time=0.6)
        
        f1 = MathTex("a", ">", "b", font_size=36).move_to(UP * 1)
        f1[0].set_color(self.C_PRIMARY)
        f1[2].set_color(self.C_SECONDARY)
        self.play(Write(f1), run_time=0.6)
        
        mul_text = Text("两边同时 ×2", font="Noto Sans CJK SC", font_size=28, color=self.C_POSITIVE, weight=BOLD).move_to(ORIGIN)
        pos_note = Text("(正数)", font="Noto Sans CJK SC", font_size=24, color=self.C_POSITIVE).next_to(mul_text, RIGHT, buff=0.2)
        
        self.play(FadeIn(VGroup(mul_text, pos_note)), run_time=0.5)
        self.wait(0.5)
        
        nl2 = NumberLine(**self.nl_config).move_to(DOWN * 2)
        self.play(FadeIn(nl2), run_time=0.6)
        
        pos_a2 = nl2.n2p(4)
        pos_b2 = nl2.n2p(2)
        
        dot_a2 = Dot(pos_a2, color=self.C_PRIMARY, radius=0.12)
        dot_b2 = Dot(pos_b2, color=self.C_SECONDARY, radius=0.12)
        label_a2 = MathTex("2a", color=self.C_PRIMARY, font_size=28).next_to(dot_a2, UP, buff=0.2)
        label_b2 = MathTex("2b", color=self.C_SECONDARY, font_size=28).next_to(dot_b2, UP, buff=0.2)
        
        self.play(TransformFromCopy(dot_a1, dot_a2), TransformFromCopy(dot_b1, dot_b2), TransformFromCopy(label_a1, label_a2), TransformFromCopy(label_b1, label_b2), run_time=1.0)
        
        f2 = MathTex("2a", ">", "2b", font_size=36).move_to(DOWN * 4.5)
        f2[0].set_color(self.C_PRIMARY)
        f2[2].set_color(self.C_SECONDARY)
        self.play(Write(f2), run_time=0.6)
        
        exp = Text("乘以正数，不等号不变", font="Noto Sans CJK SC", font_size=24, color=GRAY_A).move_to(DOWN * 6)
        self.play(FadeIn(exp), run_time=0.5)
        self.wait(1.2)
        
        self.play(FadeOut(VGroup(title, nl1, nl2, dot_a1, dot_b1, dot_a2, dot_b2, label_a1, label_b1, label_a2, label_b2, f1, f2, mul_text, pos_note, exp)), run_time=0.5)
    
    def show_property_5(self):
        """性质5: 乘负数 ⚠️ 重点"""
        title = Text("性质5：乘以负数", font="Noto Sans CJK SC", font_size=36, color=self.C_NEGATIVE, weight=BOLD).move_to(UP * 6)
        warning_icon = Text("⚠️", font_size=40, color=self.C_WARNING).next_to(title, LEFT, buff=0.3)
        warning_text = Text("易错点！", font="Noto Sans CJK SC", font_size=24, color=self.C_WARNING, weight=BOLD).next_to(title, RIGHT, buff=0.3)
        
        self.play(FadeIn(title), FadeIn(warning_icon, scale=1.5), FadeIn(warning_text), run_time=0.6)
        self.play(Flash(warning_icon, color=self.C_WARNING), Wiggle(warning_text), run_time=0.5)
        
        nl1 = NumberLine(**self.nl_config).move_to(UP * 3)
        self.play(Create(nl1), run_time=0.8)
        
        pos_a = nl1.n2p(3)
        pos_b = nl1.n2p(1)
        
        dot_a1 = Dot(pos_a, color=self.C_PRIMARY, radius=0.12)
        dot_b1 = Dot(pos_b, color=self.C_SECONDARY, radius=0.12)
        label_a1 = MathTex("a", color=self.C_PRIMARY, font_size=28).next_to(dot_a1, UP, buff=0.2)
        label_b1 = MathTex("b", color=self.C_SECONDARY, font_size=28).next_to(dot_b1, UP, buff=0.2)
        
        self.play(FadeIn(dot_a1, scale=0.5), Write(label_a1), FadeIn(dot_b1, scale=0.5), Write(label_b1), run_time=0.6)
        
        f1 = MathTex("a", ">", "b", font_size=36).move_to(UP * 0.8)
        f1[0].set_color(self.C_PRIMARY)
        f1[2].set_color(self.C_SECONDARY)
        
        self.play(Write(f1), run_time=0.6)
        box1 = SurroundingRectangle(f1, color=self.C_PRIMARY, buff=0.15)
        self.play(Create(box1), run_time=0.4)
        
        mul_text = Text("两边同时 ×(-2)", font="Noto Sans CJK SC", font_size=28, color=self.C_NEGATIVE, weight=BOLD).move_to(ORIGIN)
        neg_note = Text("(负数！)", font="Noto Sans CJK SC", font_size=24, color=self.C_WARNING, weight=BOLD).next_to(mul_text, RIGHT, buff=0.2)
        
        self.play(FadeIn(VGroup(mul_text, neg_note)), Flash(neg_note, color=self.C_WARNING), run_time=0.6)
        self.wait(0.8)
        
        nl2 = NumberLine(**self.nl_config).move_to(DOWN * 2)
        self.play(FadeIn(nl2, shift=UP * 0.3), run_time=0.6)
        
        pos_a2 = nl2.n2p(-6)
        pos_b2 = nl2.n2p(-2)
        
        dot_a2 = Dot(pos_a2, color=self.C_PRIMARY, radius=0.12)
        dot_b2 = Dot(pos_b2, color=self.C_SECONDARY, radius=0.12)
        label_a2 = MathTex("-6", color=self.C_PRIMARY, font_size=28).next_to(dot_a2, DOWN, buff=0.2)
        label_b2 = MathTex("-2", color=self.C_SECONDARY, font_size=28).next_to(dot_b2, DOWN, buff=0.2)
        
        self.play(TransformFromCopy(dot_a1, dot_a2), TransformFromCopy(dot_b1, dot_b2), TransformFromCopy(label_a1, label_a2), TransformFromCopy(label_b1, label_b2), run_time=1.2)
        
        f2 = MathTex("-6", "<", "-2", font_size=40).move_to(DOWN * 4.5)
        f2[0].set_color(self.C_PRIMARY)
        f2[1].set_color(self.C_SECONDARY)
        f2[2].set_color(self.C_SECONDARY)
        
        box2 = SurroundingRectangle(f2, color=self.C_SECONDARY, buff=0.15)
        
        self.play(Write(f2), Create(box2), run_time=0.8)
        self.play(Indicate(f2[1], scale_factor=1.5, color=self.C_WARNING), Flash(f2[1], color=self.C_WARNING), run_time=0.6)
        
        key_exp = Text("乘以负数，不等号要变向！", font="Noto Sans CJK SC", font_size=28, color=self.C_WARNING, weight=BOLD).move_to(UP * 4.8)
        
        self.play(FadeIn(key_exp, scale=1.2), run_time=0.6)
        self.play(Flash(key_exp, color=self.C_WARNING), Wiggle(key_exp), run_time=0.6)
        self.wait(2.0)
        
        self.play(FadeOut(VGroup(title, warning_icon, warning_text, nl1, nl2, dot_a1, dot_b1, dot_a2, dot_b2, label_a1, label_b1, label_a2, label_b2, f1, f2, box1, box2, mul_text, neg_note, key_exp)), run_time=0.6)
    
    def show_property_6(self):
        """性质6: 平方"""
        title = Text("性质6：平方性质", font="Noto Sans CJK SC", font_size=36, color=self.C_PRIMARY, weight=BOLD).move_to(UP * 6)
        self.play(FadeIn(title), run_time=0.5)
        
        condition = MathTex("a", ">", "b", ">", "0", font_size=32).move_to(UP * 4.8)
        condition[0].set_color(self.C_PRIMARY)
        condition[2].set_color(self.C_SECONDARY)
        self.play(Write(condition), run_time=0.6)
        
        sq_a = Square(side_length=2.5, color=self.C_PRIMARY, fill_opacity=0.3).move_to(LEFT * 2 + UP * 1)
        label_sq_a = MathTex("a", font_size=28, color=self.C_PRIMARY).next_to(sq_a, UP, buff=0.2)
        area_a = MathTex("a^2", font_size=32, color=self.C_PRIMARY).move_to(sq_a.get_center())
        
        self.play(Create(sq_a), Write(label_sq_a), run_time=0.8)
        self.play(FadeIn(area_a, scale=0.8), run_time=0.4)
        
        sq_b = Square(side_length=1.5, color=self.C_SECONDARY, fill_opacity=0.3).move_to(RIGHT * 2 + UP * 1)
        label_sq_b = MathTex("b", font_size=28, color=self.C_SECONDARY).next_to(sq_b, UP, buff=0.2)
        area_b = MathTex("b^2", font_size=32, color=self.C_SECONDARY).move_to(sq_b.get_center())
        
        self.play(Create(sq_b), Write(label_sq_b), run_time=0.8)
        self.play(FadeIn(area_b, scale=0.8), run_time=0.4)
        
        self.play(Indicate(sq_a, scale_factor=1.1, color=self.C_PRIMARY), Indicate(sq_b, scale_factor=1.1, color=self.C_SECONDARY), run_time=0.8)
        
        conclusion = MathTex("\\therefore", "a^2", ">", "b^2", font_size=40).move_to(DOWN * 1.5)
        conclusion[1].set_color(self.C_PRIMARY)
        conclusion[3].set_color(self.C_SECONDARY)
        self.play(Write(conclusion), run_time=0.8)
        
        exp = Text("正数平方，大小关系保持", font="Noto Sans CJK SC", font_size=24, color=GRAY_A).move_to(DOWN * 3.5)
        note = Text("(注意：必须都是正数)", font="Noto Sans CJK SC", font_size=20, color=GRAY_B).move_to(DOWN * 4.5)
        
        self.play(FadeIn(exp), FadeIn(note), run_time=0.5)
        self.wait(1.2)
        
        self.play(FadeOut(VGroup(title, condition, sq_a, sq_b, label_sq_a, label_sq_b, area_a, area_b, conclusion, exp, note)), run_time=0.5)
    
    def show_summary(self):
        """总结"""
        title = Text("不等式六大性质", font="Noto Sans CJK SC", font_size=42, color=GOLD, weight=BOLD).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.8)
        
        props = [
            ("1. 对称性", "a>b <=> b<a", WHITE),
            ("2. 传递性", "a>b, b>c => a>c", WHITE),
            ("3. 加法", "a>b => a+c>b+c", WHITE),
            ("4. 乘正数", "a>b, c>0 => ac>bc", self.C_POSITIVE),
            ("5. 乘负数", "a>b, c<0 => ac<bc", self.C_NEGATIVE),
            ("6. 平方", "a>b>0 => a^2>b^2", WHITE),
        ]
        
        cards = VGroup()
        for i, (name, formula, color) in enumerate(props):
            bg = RoundedRectangle(width=7.5, height=1.0, corner_radius=0.15, fill_opacity=0.1, fill_color=color, stroke_color=color, stroke_width=2).move_to(UP * (4.5 - i * 1.4))
            n = Text(name, font="Noto Sans CJK SC", font_size=24, color=color, weight=BOLD).move_to(bg.get_left() + RIGHT * 1.2)
            f = MathTex(formula, font_size=28, color=color).move_to(bg.get_right() + LEFT * 2.5)
            
            card = VGroup(bg, n, f)
            if i == 4:
                w = Text("⚠️", font_size=30, color=self.C_WARNING).next_to(bg, LEFT, buff=0.2)
                card.add(w)
            cards.add(card)
        
        for i, card in enumerate(cards):
            if i == 4:
                self.play(FadeIn(card, shift=UP * 0.2), Flash(card, color=self.C_WARNING), run_time=0.6)
            else:
                self.play(FadeIn(card, shift=UP * 0.2), run_time=0.4)
        
        self.wait(1.0)
        
        wbox = RoundedRectangle(width=7.5, height=1.2, corner_radius=0.2, fill_opacity=0.2, fill_color=self.C_WARNING, stroke_color=self.C_WARNING, stroke_width=3).move_to(DOWN * 5)
        wtext = Text("记住：乘以负数，不等号要变向！", font="Noto Sans CJK SC", font_size=26, color=self.C_WARNING, weight=BOLD).move_to(wbox)
        
        self.play(Create(wbox), FadeIn(wtext, scale=1.1), run_time=0.6)
        self.play(Flash(wbox, color=self.C_WARNING), Wiggle(wtext), run_time=0.6)
        self.wait(2.0)
        
        self.play(FadeOut(VGroup(title, cards, wbox, wtext)), run_time=0.6)
    
    def show_outro(self):
        """片尾"""
        author_name = Text("上海初高中数学直通车", font="Noto Sans CJK SC", font_size=40, color=WHITE, weight=BOLD).move_to(UP * 1.5)
        author_id = Text("@emptyandcalm", font="Noto Sans CJK SC", font_size=32, color=GRAY_B).move_to(UP * 0.5)
        
        self.play(Transform(self.author_info, author_name), run_time=0.8)
        self.play(FadeIn(author_id), run_time=0.5)
        
        follow = Text("关注我，学更多数学技巧！", font="Noto Sans CJK SC", font_size=32, color=YELLOW, weight=BOLD).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, scale=1.1), run_time=0.6)
        
        decs = VGroup(
            MathTex(">", font_size=50, color=self.C_PRIMARY),
            MathTex("<", font_size=50, color=self.C_SECONDARY),
            MathTex(">", font_size=50, color=self.C_POSITIVE),
            MathTex("<", font_size=50, color=self.C_NEGATIVE),
        ).arrange_in_grid(rows=2, cols=2, buff=1.5).move_to(DOWN * 3)
        
        self.play(*[FadeIn(d, scale=0.5) for d in decs], run_time=0.6)
        self.play(Rotate(decs, angle=PI/4, run_time=1.5), rate_func=there_and_back)
        self.wait(1.5)
        
        self.play(FadeOut(VGroup(self.author_info, author_id, follow, decs)), run_time=1.0)


# 运行命令:
# manim -pql inequality_properties_full.py InequalityPropertiesFull