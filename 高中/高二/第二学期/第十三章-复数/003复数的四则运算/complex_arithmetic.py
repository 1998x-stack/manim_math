"""
复数的四则运算 - Complex Number Arithmetic Animation
Manim 0.19.2 | TikTok 竖屏 1080×1920
目标: 高中生 | 知识点: 复数加减乘除
作者标识: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ========== 全局配置 ==========
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class ComplexArithmetic(Scene):
    """
    复数四则运算教学动画
    z₁ = 1+i, z₂ = 2-i 作为示例
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.C_Z1 = "#e74c3c"       # 红 z₁
        self.C_Z2 = "#3498db"       # 蓝 z₂
        self.C_RES = "#2ecc71"      # 绿 结果
        self.C_I2 = "#f39c12"       # 橙 i²
        self.C_CONJ = "#9b59b6"     # 紫 共轭

        # 示例数
        self.z1_a, self.z1_b = 1, 1   # z₁ = 1+i
        self.z2_c, self.z2_d = 2, -1  # z₂ = 2-i

        self.scene_1_opening()
        self.scene_2_addition()
        self.scene_3_subtraction()
        self.scene_4_multiplication()
        self.scene_5_division()
        self.scene_6_i_powers()
        self.scene_7_outro()

    # =========================================================
    # 工具函数
    # =========================================================

    def make_title(self, text_cn, color=WHITE, y=6.2):
        return Text(text_cn, font="Noto Sans CJK SC", font_size=36, color=color).move_to(UP * y)

    def make_sub(self, text_cn, color=GRAY_A, y=5.4):
        return Text(text_cn, font="Noto Sans CJK SC", font_size=24, color=color).move_to(UP * y)

    def make_body(self, text_cn, color=GRAY_A):
        return Text(text_cn, font="Noto Sans CJK SC", font_size=22, color=color)

    def make_explain(self, text_cn, y=-5.0, color=GRAY_A):
        return Text(text_cn, font="Noto Sans CJK SC", font_size=20, color=color).move_to(UP * y)

    def section_divider(self, elements_to_fade):
        """场景清理"""
        if elements_to_fade:
            self.play(*[FadeOut(e) for e in elements_to_fade], run_time=0.5)

    def highlight_box(self, mobject, color=YELLOW, buff=0.15):
        return SurroundingRectangle(mobject, color=color, buff=buff, corner_radius=0.1)

    # =========================================================
    # Scene 1: 开场 (0-4s)
    # =========================================================

    def scene_1_opening(self):
        # 作者信息 (永久显示)
        self.author_bar = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_B
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.3)

        # 钩子问题
        hook_line1 = Text("复数也能", font="Noto Sans CJK SC",
                          font_size=52, color=WHITE).move_to(UP * 3.5)
        hook_line2 = Text("加减乘除？", font="Noto Sans CJK SC",
                          font_size=52, color=YELLOW).move_to(UP * 2.5)

        self.play(Write(hook_line1), run_time=0.7)
        self.play(Write(hook_line2), run_time=0.7)

        # z₁ z₂ 出现
        z1_tex = MathTex(r"z_1 = 1+i", font_size=40, color=self.C_Z1).move_to(UP * 0.5)
        z2_tex = MathTex(r"z_2 = 2-i", font_size=40, color=self.C_Z2).move_to(DOWN * 0.5)

        self.play(FadeIn(z1_tex, shift=RIGHT * 0.3), FadeIn(z2_tex, shift=LEFT * 0.3), run_time=0.6)

        # 问号符号
        q_marks = VGroup(
            MathTex(r"z_1 + z_2 = ?", font_size=32, color="#aaaacc").move_to(DOWN * 2.2),
            MathTex(r"z_1 \times z_2 = ?", font_size=32, color="#aaaacc").move_to(DOWN * 3.0),
            MathTex(r"z_1 \div z_2 = ?", font_size=32, color="#aaaacc").move_to(DOWN * 3.8),
        )
        for q in q_marks:
            self.play(FadeIn(q), run_time=0.25)

        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(hook_line1), FadeOut(hook_line2),
            FadeOut(z1_tex), FadeOut(z2_tex),
            FadeOut(q_marks),
            run_time=0.5
        )

    # =========================================================
    # Scene 2: 加法 (4-18s)
    # =========================================================

    def scene_2_addition(self):
        title = self.make_title("复数加法", color="#e8d5a3", y=6.8)
        self.play(FadeIn(title), run_time=0.4)

        # ---- 通用公式 ----
        formula_general = MathTex(
            r"(a+bi)+(c+di)",
            r"=",
            r"(a+c)+(b+d)i",
            font_size=28
        ).move_to(UP * 5.6)
        formula_general[0].set_color(GRAY_A)
        formula_general[2].set_color(self.C_RES)

        self.play(Write(formula_general), run_time=1.0)

        rule_text = Text(
            "实部相加，虚部相加",
            font="Noto Sans CJK SC", font_size=22, color=YELLOW
        ).move_to(UP * 4.9)
        self.play(FadeIn(rule_text), run_time=0.4)
        self.wait(0.5)

        # ---- 复平面示意 ----
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-2, 3, 1],
            x_length=6,
            y_length=4.5,
            axis_config={"include_numbers": True, "font_size": 18},
            tips=False,
        ).move_to(UP * 1.8)

        x_label = Text("实轴", font="Noto Sans CJK SC", font_size=18).next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
        y_label = Text("虚轴", font="Noto Sans CJK SC", font_size=18).next_to(axes.y_axis.get_end(), UP, buff=0.1)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=0.8)

        # z₁ = 1+i 向量
        z1_pt = axes.c2p(1, 1)
        z1_vec = Arrow(axes.c2p(0, 0), z1_pt, color=self.C_Z1, buff=0, stroke_width=4)
        z1_dot = Dot(z1_pt, color=self.C_Z1, radius=0.07)
        z1_lbl = MathTex(r"z_1=1+i", font_size=22, color=self.C_Z1).next_to(z1_dot, UL, buff=0.08)

        # z₂ = 2-i 向量
        z2_pt = axes.c2p(2, -1)
        z2_vec = Arrow(axes.c2p(0, 0), z2_pt, color=self.C_Z2, buff=0, stroke_width=4)
        z2_dot = Dot(z2_pt, color=self.C_Z2, radius=0.07)
        z2_lbl = MathTex(r"z_2=2-i", font_size=22, color=self.C_Z2).next_to(z2_dot, DR, buff=0.08)

        self.play(Create(z1_vec), FadeIn(z1_dot), FadeIn(z1_lbl), run_time=0.6)
        self.play(Create(z2_vec), FadeIn(z2_dot), FadeIn(z2_lbl), run_time=0.6)

        # 平行四边形法则
        # 从z₁末端画平行于z₂的虚线
        z2_shift_from_z1 = Arrow(z1_pt, axes.c2p(3, 0), color=self.C_Z2,
                                  buff=0, stroke_width=2, stroke_opacity=0.6)
        z1_shift_from_z2 = Arrow(z2_pt, axes.c2p(3, 0), color=self.C_Z1,
                                  buff=0, stroke_width=2, stroke_opacity=0.6)

        # 结果 z₁+z₂ = 3+0i = 3
        res_pt = axes.c2p(3, 0)
        res_vec = Arrow(axes.c2p(0, 0), res_pt, color=self.C_RES, buff=0, stroke_width=5)
        res_dot = Dot(res_pt, color=self.C_RES, radius=0.08)
        res_lbl = MathTex(r"z_1+z_2=3", font_size=24, color=self.C_RES).next_to(res_dot, UR, buff=0.1)

        self.play(Create(z2_shift_from_z1), Create(z1_shift_from_z2), run_time=0.6)
        self.play(Create(res_vec), FadeIn(res_dot), run_time=0.5)
        self.play(FadeIn(res_lbl), run_time=0.4)

        # 计算步骤文字
        step_box = VGroup(
            MathTex(r"(1+i)+(2-i)", font_size=26),
            MathTex(r"=(1+2)+( 1+(-1))i", font_size=26),
            MathTex(r"= 3 + 0 \cdot i = 3", font_size=26, color=self.C_RES),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(DOWN * 4.2)

        self.play(Write(step_box[0]), run_time=0.5)
        self.play(Write(step_box[1]), run_time=0.5)
        self.play(Write(step_box[2]), run_time=0.5)

        box = self.highlight_box(step_box[2], color=self.C_RES)
        self.play(Create(box), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(formula_general), FadeOut(rule_text),
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(z1_vec), FadeOut(z1_dot), FadeOut(z1_lbl),
            FadeOut(z2_vec), FadeOut(z2_dot), FadeOut(z2_lbl),
            FadeOut(z2_shift_from_z1), FadeOut(z1_shift_from_z2),
            FadeOut(res_vec), FadeOut(res_dot), FadeOut(res_lbl),
            FadeOut(step_box), FadeOut(box),
            run_time=0.5
        )

    # =========================================================
    # Scene 3: 减法 (18-28s)
    # =========================================================

    def scene_3_subtraction(self):
        title = self.make_title("复数减法", color="#e8d5a3", y=6.8)
        self.play(FadeIn(title), run_time=0.4)

        formula_general = MathTex(
            r"(a+bi)-(c+di)",
            r"=",
            r"(a-c)+(b-d)i",
            font_size=28
        ).move_to(UP * 5.6)
        formula_general[0].set_color(GRAY_A)
        formula_general[2].set_color(self.C_RES)

        self.play(Write(formula_general), run_time=0.8)

        rule_text = Text(
            "实部相减，虚部相减",
            font="Noto Sans CJK SC", font_size=22, color=YELLOW
        ).move_to(UP * 4.9)
        self.play(FadeIn(rule_text), run_time=0.4)
        self.wait(0.4)

        # 步骤展示 - 大字
        head = MathTex(r"z_1 - z_2", font_size=40).move_to(UP * 3.5)
        self.play(Write(head), run_time=0.5)

        steps = VGroup(
            MathTex(r"= (1+i)-(2-i)", font_size=34),
            MathTex(r"= (1-2) + (1-(-1))i", font_size=34),
            MathTex(r"= -1 + 2i", font_size=40, color=self.C_RES),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 1.5)

        for step in steps:
            self.play(Write(step), run_time=0.6)
            self.wait(0.2)

        box = self.highlight_box(steps[2], color=self.C_RES)
        self.play(Create(box), run_time=0.4)

        # 彩色解析
        color_explain = VGroup(
            Text("实部: 1-2 = -1", font="Noto Sans CJK SC", font_size=22, color=self.C_Z1),
            Text("虚部: 1-(-1) = 2", font="Noto Sans CJK SC", font_size=22, color=self.C_Z2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(DOWN * 2.5)

        self.play(FadeIn(color_explain), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(formula_general), FadeOut(rule_text),
            FadeOut(head), FadeOut(steps), FadeOut(box), FadeOut(color_explain),
            run_time=0.5
        )

    # =========================================================
    # Scene 4: 乘法 (28-46s)
    # =========================================================

    def scene_4_multiplication(self):
        title = self.make_title("复数乘法", color="#e8d5a3", y=6.8)
        self.play(FadeIn(title), run_time=0.4)

        # 关键提示
        key_tip = MathTex(r"i^2 = -1", font_size=40, color=self.C_I2).move_to(UP * 5.5)
        tip_box = self.highlight_box(key_tip, color=self.C_I2)
        self.play(Write(key_tip), Create(tip_box), run_time=0.6)

        # 展开过程
        step0 = MathTex(r"z_1 \cdot z_2 = (1+i)(2-i)", font_size=32).move_to(UP * 4.3)
        self.play(Write(step0), run_time=0.6)

        # FOIL展开
        foil_label = Text("展开（FOIL法）:", font="Noto Sans CJK SC",
                          font_size=22, color=GRAY_A).move_to(UP * 3.4)
        self.play(FadeIn(foil_label), run_time=0.3)

        step1 = MathTex(
            r"= 1 \cdot 2 + 1 \cdot (-i) + i \cdot 2 + i \cdot (-i)",
            font_size=28
        ).move_to(UP * 2.7)
        self.play(Write(step1), run_time=0.8)

        step2 = MathTex(
            r"= 2 - i + 2i - i^2",
            font_size=34
        ).move_to(UP * 1.8)
        self.play(Write(step2), run_time=0.6)

        # 高亮 i² 部分
        i2_highlight = Text("注意: i² = -1 !", font="Noto Sans CJK SC",
                            font_size=24, color=self.C_I2).move_to(UP * 0.9)
        arrow_to_i2 = Arrow(
            i2_highlight.get_top(),
            step2.get_right() + LEFT * 0.5,
            color=self.C_I2, stroke_width=3, buff=0.1
        )
        self.play(FadeIn(i2_highlight), run_time=0.4)

        step3 = MathTex(
            r"= 2 - i + 2i - (",
            r"-1",
            r")",
            font_size=34
        ).move_to(UP * 0)
        step3[1].set_color(self.C_I2)
        self.play(Write(step3), run_time=0.6)

        step4 = MathTex(r"= 2 + 1 + (-1+2)i", font_size=34).move_to(DOWN * 0.9)
        self.play(Write(step4), run_time=0.6)

        step5 = MathTex(r"= 3 + i", font_size=44, color=self.C_RES).move_to(DOWN * 2.0)
        self.play(Write(step5), run_time=0.6)

        box5 = self.highlight_box(step5, color=self.C_RES)
        self.play(Create(box5), run_time=0.4)

        # 通用公式展示
        general = MathTex(
            r"(a+bi)(c+di) = (ac-bd)+(ad+bc)i",
            font_size=22, color="#aaaacc"
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(general), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(key_tip), FadeOut(tip_box),
            FadeOut(step0), FadeOut(foil_label), FadeOut(step1),
            FadeOut(step2), FadeOut(i2_highlight),
            FadeOut(step3), FadeOut(step4), FadeOut(step5), FadeOut(box5),
            FadeOut(general),
            run_time=0.5
        )

    # =========================================================
    # Scene 5: 除法 (46-64s)
    # =========================================================

    def scene_5_division(self):
        title = self.make_title("复数除法", color="#e8d5a3", y=6.8)
        self.play(FadeIn(title), run_time=0.4)

        # 问题
        problem = MathTex(
            r"\frac{z_1}{z_2} = \frac{1+i}{2-i}",
            font_size=38
        ).move_to(UP * 5.5)
        self.play(Write(problem), run_time=0.6)

        # 引入共轭
        q_text = Text("如何去掉分母的虚数？", font="Noto Sans CJK SC",
                      font_size=26, color=YELLOW).move_to(UP * 4.4)
        self.play(FadeIn(q_text), run_time=0.4)
        self.wait(0.4)

        # 共轭复数
        conj_intro = Text("关键: 使用共轭复数", font="Noto Sans CJK SC",
                          font_size=26, color=self.C_CONJ).move_to(UP * 3.5)
        self.play(FadeIn(conj_intro), run_time=0.4)

        conj_formula = MathTex(
            r"\overline{2-i} = 2+i",
            font_size=36, color=self.C_CONJ
        ).move_to(UP * 2.7)
        conj_box = self.highlight_box(conj_formula, color=self.C_CONJ)
        self.play(Write(conj_formula), Create(conj_box), run_time=0.6)

        # 说明共轭的作用
        conj_product = MathTex(
            r"(2-i)(2+i) = 4 + 1 = 5",
            font_size=30, color=self.C_CONJ
        ).move_to(UP * 1.8)
        conj_explain = Text("→ 分母变成实数！", font="Noto Sans CJK SC",
                            font_size=22, color=YELLOW).next_to(conj_product, RIGHT, buff=0.2)
        # 实际上横向排布可能超界，放到下面
        conj_explain2 = Text("分母变成实数！", font="Noto Sans CJK SC",
                             font_size=24, color=YELLOW).move_to(UP * 1.1)

        self.play(Write(conj_product), run_time=0.6)
        self.play(FadeIn(conj_explain2), run_time=0.4)
        self.wait(0.4)

        # 分子分母同乘共轭
        step_mult = MathTex(
            r"= \frac{(1+i)(2+i)}{(2-i)(2+i)}",
            font_size=36
        ).move_to(UP * 0.0)
        self.play(Write(step_mult), run_time=0.6)

        # 展开分子
        numer = MathTex(
            r"(1+i)(2+i) = 2+i+2i+i^2 = 2+3i-1 = 1+3i",
            font_size=26
        ).move_to(DOWN * 0.9)
        self.play(Write(numer), run_time=0.8)

        # 最终结果
        step_final = MathTex(
            r"= \frac{1+3i}{5} = \frac{1}{5} + \frac{3}{5}i",
            font_size=36, color=self.C_RES
        ).move_to(DOWN * 2.0)
        self.play(Write(step_final), run_time=0.7)

        box_final = self.highlight_box(step_final, color=self.C_RES)
        self.play(Create(box_final), run_time=0.4)

        # 通用公式
        general_div = MathTex(
            r"\frac{a+bi}{c+di} = \frac{(ac+bd)+(bc-ad)i}{c^2+d^2}",
            font_size=22, color="#aaaacc"
        ).move_to(DOWN * 3.4)
        self.play(FadeIn(general_div), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(problem), FadeOut(q_text),
            FadeOut(conj_intro), FadeOut(conj_formula), FadeOut(conj_box),
            FadeOut(conj_product), FadeOut(conj_explain2),
            FadeOut(step_mult), FadeOut(numer),
            FadeOut(step_final), FadeOut(box_final),
            FadeOut(general_div),
            run_time=0.5
        )

    # =========================================================
    # Scene 6: i 的幂次 (64-72s)
    # =========================================================

    def scene_6_i_powers(self):
        title = self.make_title("i 的幂次规律", color=YELLOW, y=6.8)
        self.play(FadeIn(title), run_time=0.4)

        sub = Text("每4个为一个周期！", font="Noto Sans CJK SC",
                   font_size=26, color=self.C_I2).move_to(UP * 5.8)
        self.play(FadeIn(sub), run_time=0.4)

        # 四个幂次
        powers = [
            (r"i^1 = i", self.C_Z1),
            (r"i^2 = -1", self.C_I2),
            (r"i^3 = -i", self.C_Z2),
            (r"i^4 = 1", self.C_RES),
        ]

        power_group = VGroup()
        for i, (tex, color) in enumerate(powers):
            card_bg = RoundedRectangle(
                width=4.5, height=1.1, corner_radius=0.2,
                fill_color=color, fill_opacity=0.15,
                stroke_color=color, stroke_width=2
            )
            formula = MathTex(tex, font_size=40, color=color)
            card = VGroup(card_bg, formula)
            power_group.add(card)

        power_group.arrange(DOWN, buff=0.3).move_to(UP * 2.5)

        for card in power_group:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.35)

        # 循环箭头（文字说明代替复杂箭头）
        cycle_text = Text(
            "i → -1 → -i → 1 → i → ...",
            font="Noto Sans CJK SC", font_size=22, color=GRAY_A
        ).move_to(DOWN * 1.8)
        self.play(FadeIn(cycle_text), run_time=0.5)

        tip = Text(
            "求 iⁿ: 看 n 除以4的余数",
            font="Noto Sans CJK SC", font_size=24, color=YELLOW
        ).move_to(DOWN * 3.0)
        tip_box = SurroundingRectangle(tip, color=YELLOW, buff=0.2, corner_radius=0.1)
        self.play(FadeIn(tip), Create(tip_box), run_time=0.6)

        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(power_group), FadeOut(cycle_text),
            FadeOut(tip), FadeOut(tip_box),
            run_time=0.5
        )

    # =========================================================
    # Scene 7: 总结 + 片尾 (72-80s)
    # =========================================================

    def scene_7_outro(self):
        title = self.make_title("四则运算总结", color=GOLD, y=7.0)
        self.play(FadeIn(title), run_time=0.4)

        # 总结卡片
        cards_data = [
            ("加法", r"(a+c)+(b+d)i", "#e74c3c"),
            ("减法", r"(a-c)+(b-d)i", "#3498db"),
            ("乘法", r"(ac-bd)+(ad+bc)i", "#f39c12"),
            ("除法", r"\frac{(ac+bd)+(bc-ad)i}{c^2+d^2}", "#2ecc71"),
        ]

        summary_cards = VGroup()
        for label_cn, formula_str, color in cards_data:
            label = Text(label_cn, font="Noto Sans CJK SC",
                         font_size=26, color=color)
            formula = MathTex(formula_str, font_size=24, color=WHITE)
            line = Line(LEFT * 3, RIGHT * 3, stroke_width=1, color=color)
            card = VGroup(label, formula).arrange(RIGHT, buff=0.4)
            summary_cards.add(card)

        summary_cards.arrange(DOWN, aligned_edge=LEFT, buff=0.45).move_to(UP * 3.5)

        for card in summary_cards:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.3)

        # 核心技巧
        trick1 = Text("关键: i² = -1", font="Noto Sans CJK SC",
                      font_size=28, color=self.C_I2).move_to(DOWN * 0.8)
        trick2 = Text("除法: 分子分母乘共轭", font="Noto Sans CJK SC",
                      font_size=26, color=self.C_CONJ).move_to(DOWN * 1.6)
        tricks_box = SurroundingRectangle(
            VGroup(trick1, trick2), color=YELLOW, buff=0.3, corner_radius=0.15
        )

        self.play(FadeIn(trick1), FadeIn(trick2), Create(tricks_box), run_time=0.8)
        self.wait(1.2)

        # 片尾
        self.play(
            FadeOut(title), FadeOut(summary_cards),
            FadeOut(trick1), FadeOut(trick2), FadeOut(tricks_box),
            run_time=0.5
        )

        # 作者信息放大
        final_author = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC", font_size=40, color=WHITE
        ).move_to(UP * 2.0)
        final_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC", font_size=32, color=GRAY_B
        ).move_to(UP * 0.9)
        follow = Text(
            "关注我，获得更多数学技巧!",
            font="Noto Sans CJK SC", font_size=30, color=YELLOW
        ).move_to(DOWN * 0.3)

        self.play(
            Transform(self.author_bar, final_author),
            run_time=0.6
        )
        self.play(FadeIn(final_id), FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 装饰小星星
        stars = VGroup(*[
            Star(n=5, outer_radius=0.2, color=GOLD, fill_opacity=0.9)
            .move_to(follow.get_center() + 3.0 * np.array([
                np.cos(i * TAU / 5), np.sin(i * TAU / 5), 0
            ]))
            for i in range(5)
        ])
        self.play(*[FadeIn(s, scale=0.3) for s in stars], run_time=0.5)
        self.play(Rotate(stars, angle=TAU / 10, run_time=1.0))
        self.wait(1.0)


# ========== 渲染命令 ==========
# 快速预览: manim -pql complex_arithmetic.py ComplexArithmetic
# 高质量:   manim -qh complex_arithmetic.py ComplexArithmetic