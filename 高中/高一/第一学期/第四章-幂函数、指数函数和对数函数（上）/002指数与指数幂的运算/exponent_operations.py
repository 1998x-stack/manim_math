"""
指数与指数幂的运算 - Exponent Operations Teaching Animation
高一数学第四章

TikTok 竖屏格式 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""
from manim import *
import numpy as np

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


class ExponentOperations(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a2e"

        self.C_RULE    = "#f1c40f"   # 法则公式黄
        self.C_EG      = "#3498db"   # 例子蓝
        self.C_HL      = "#e74c3c"   # 高亮红
        self.C_INC     = "#2ecc71"   # 绿
        self.C_AUX     = GRAY_B
        self.C_SPECIAL = "#9b59b6"   # 特殊指数紫

        self.scene_1_opening()
        self.scene_2_four_rules()
        self.scene_3_special()
        self.scene_4_rational()
        self.scene_5_outro()

    # ══════════════════════════════════════════════
    # 工具：创建「法则 + 例子」卡片行
    # ══════════════════════════════════════════════
    def _rule_card(self, rule_tex, example_tex, y_center,
                   rule_color=None, eg_color=None):
        rc = rule_color or self.C_RULE
        ec = eg_color   or self.C_EG

        rule_mob = MathTex(rule_tex,    font_size=30, color=rc)
        eg_mob   = MathTex(example_tex, font_size=26, color=ec)

        card = VGroup(rule_mob, eg_mob).arrange(DOWN, buff=0.3).move_to(UP * y_center)
        return card, rule_mob, eg_mob

    # ══════════════════════════════════════════════
    # Scene 1: 开场
    # ══════════════════════════════════════════════
    def scene_1_opening(self):
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font="Noto Sans CJK SC", font_size=20, color=self.C_AUX,
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        title = Text("指数幂的运算法则",
                      font="Noto Sans CJK SC", font_size=44, color=GOLD
                      ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        hook = Text(
            "记住这 4 条，指数计算不发愁！",
            font="Noto Sans CJK SC", font_size=26, color=WHITE,
        ).move_to(UP * 5.2)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.5)

        # 快速预览 4 个公式
        preview = VGroup(
            MathTex(r"a^m \cdot a^n = a^{m+n}", font_size=24, color=self.C_RULE),
            MathTex(r"\frac{a^m}{a^n} = a^{m-n}", font_size=24, color=self.C_RULE),
            MathTex(r"(a^m)^n = a^{mn}", font_size=24, color=self.C_RULE),
            MathTex(r"(ab)^n = a^n b^n", font_size=24, color=self.C_RULE),
        ).arrange(DOWN, buff=0.45).move_to(UP * 3.2)

        for row in preview:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.3)
        self.wait(0.8)

        self.play(FadeOut(title), FadeOut(hook), FadeOut(preview), run_time=0.4)

    # ══════════════════════════════════════════════
    # Scene 2: 四大法则逐一讲解
    # ══════════════════════════════════════════════
    def scene_2_four_rules(self):
        rules = [
            {
                "name": "法则 ①  同底相乘，指数相加",
                "rule": r"a^m \cdot a^n = a^{m+n}",
                "eg":   r"2^3 \cdot 2^4 = 2^{3+4} = 2^7 = 128",
                "tip":  "底数不变，指数做加法",
            },
            {
                "name": "法则 ②  同底相除，指数相减",
                "rule": r"\frac{a^m}{a^n} = a^{m-n}",
                "eg":   r"\frac{3^5}{3^2} = 3^{5-2} = 3^3 = 27",
                "tip":  "底数不变，指数做减法",
            },
            {
                "name": "法则 ③  幂的乘方，指数相乘",
                "rule": r"(a^m)^n = a^{mn}",
                "eg":   r"(2^3)^4 = 2^{3 \times 4} = 2^{12} = 4096",
                "tip":  "底数不变，指数做乘法",
            },
            {
                "name": "法则 ④  积的乘方，分别乘方",
                "rule": r"(ab)^n = a^n b^n",
                "eg":   r"(2 \times 3)^4 = 2^4 \cdot 3^4 = 16 \times 81 = 1296",
                "tip":  "分配律：每个因子都乘方",
            },
        ]

        for rule in rules:
            self._show_rule_card(rule)

    def _show_rule_card(self, rule):
        # 法则名称
        name_mob = Text(
            rule["name"], font="Noto Sans CJK SC",
            font_size=26, color=self.C_HL,
        ).move_to(UP * 6.0)
        self.play(Write(name_mob), run_time=0.5)

        # 核心公式（大号）
        rule_mob = MathTex(rule["rule"], font_size=44, color=self.C_RULE
                            ).move_to(UP * 4.8)
        box = SurroundingRectangle(rule_mob, color=self.C_RULE, buff=0.25,
                                   corner_radius=0.12)
        self.play(Write(rule_mob), Create(box), run_time=0.7)

        # 例子
        eg_label = Text("例：", font="Noto Sans CJK SC",
                         font_size=24, color=self.C_AUX).move_to(UP * 3.4 + LEFT * 2.5)
        eg_mob = MathTex(rule["eg"], font_size=30, color=self.C_EG
                          ).move_to(UP * 3.4)
        self.play(FadeIn(eg_label), Write(eg_mob), run_time=0.7)

        # 箭头指向变化的部分 + tip
        tip_mob = Text(
            rule["tip"], font="Noto Sans CJK SC",
            font_size=22, color=self.C_INC,
        ).move_to(UP * 2.2)
        self.play(FadeIn(tip_mob, shift=UP * 0.2), run_time=0.4)

        # 记忆口诀高亮框
        hint_border = SurroundingRectangle(tip_mob, color=self.C_INC, buff=0.15,
                                            corner_radius=0.08)
        self.play(Create(hint_border), run_time=0.4)
        self.wait(1.8)

        self.play(
            FadeOut(name_mob), FadeOut(rule_mob), FadeOut(box),
            FadeOut(eg_label), FadeOut(eg_mob),
            FadeOut(tip_mob), FadeOut(hint_border),
            run_time=0.4,
        )

    # ══════════════════════════════════════════════
    # Scene 3: 特殊指数（零次幂 + 负整数幂）
    # ══════════════════════════════════════════════
    def scene_3_special(self):
        sc_title = Text("特殊指数",
                         font="Noto Sans CJK SC", font_size=34, color=self.C_SPECIAL
                         ).move_to(UP * 6.2)
        self.play(Write(sc_title), run_time=0.5)

        # ── 零次幂 ──
        zero_title = Text("零次幂",
                           font="Noto Sans CJK SC", font_size=28, color=WHITE
                           ).move_to(UP * 5.2)
        zero_formula = MathTex(r"a^0 = 1 \quad (a \neq 0)",
                                font_size=40, color=self.C_RULE).move_to(UP * 4.3)
        zero_why = Text("理解：a³ ÷ a³ = a³⁻³ = a⁰，同时 = 1",
                         font="Noto Sans CJK SC", font_size=20, color=self.C_AUX
                         ).move_to(UP * 3.5)
        zero_eg = MathTex(r"5^0 = 1,\quad (-3)^0 = 1,\quad \pi^0 = 1",
                           font_size=26, color=self.C_EG).move_to(UP * 2.7)

        self.play(Write(zero_title), run_time=0.4)
        self.play(Write(zero_formula), run_time=0.6)
        self.play(FadeIn(zero_why), FadeIn(zero_eg), run_time=0.5)
        self.wait(1.2)

        # ── 负整数幂 ──
        neg_title = Text("负整数幂",
                          font="Noto Sans CJK SC", font_size=28, color=WHITE
                          ).move_to(UP * 1.5)
        neg_formula = MathTex(r"a^{-n} = \frac{1}{a^n} \quad (a \neq 0)",
                               font_size=40, color=self.C_RULE).move_to(UP * 0.5)
        neg_eg = MathTex(
            r"2^{-3} = \frac{1}{2^3} = \frac{1}{8},\quad 10^{-2} = 0.01",
            font_size=26, color=self.C_EG).move_to(DOWN * 0.5)

        self.play(Write(neg_title), run_time=0.4)
        self.play(Write(neg_formula), run_time=0.6)
        self.play(Write(neg_eg), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(sc_title),
            FadeOut(zero_title), FadeOut(zero_formula),
            FadeOut(zero_why),   FadeOut(zero_eg),
            FadeOut(neg_title),  FadeOut(neg_formula), FadeOut(neg_eg),
            run_time=0.5,
        )

    # ══════════════════════════════════════════════
    # Scene 4: 有理数指数幂（根式）
    # ══════════════════════════════════════════════
    def scene_4_rational(self):
        sc_title = Text("有理数指数幂",
                         font="Noto Sans CJK SC", font_size=34, color=GOLD
                         ).move_to(UP * 6.2)
        self.play(Write(sc_title), run_time=0.5)

        # 公式
        rational_formula = MathTex(
            r"a^{\frac{m}{n}} = \sqrt[n]{a^m} \quad (a > 0)",
            font_size=36, color=self.C_RULE,
        ).move_to(UP * 5.0)
        box = SurroundingRectangle(rational_formula, color=GOLD, buff=0.2,
                                    corner_radius=0.12)
        self.play(Write(rational_formula), Create(box), run_time=0.8)

        # 直觉说明
        intuition = Text(
            "分子是指数，分母是根号次数",
            font="Noto Sans CJK SC", font_size=22, color=self.C_AUX,
        ).move_to(UP * 3.9)
        self.play(FadeIn(intuition), run_time=0.4)

        # 例 1
        eg1_label = Text("例 1：", font="Noto Sans CJK SC",
                          font_size=24, color=self.C_AUX).move_to(UP * 3.0 + LEFT * 2.5)
        eg1 = MathTex(
            r"8^{\frac{2}{3}} = \sqrt[3]{8^2} = \sqrt[3]{64} = 4",
            font_size=30, color=self.C_EG,
        ).move_to(UP * 3.0 + RIGHT * 0.5)
        self.play(FadeIn(eg1_label), Write(eg1), run_time=0.7)

        # 例 2
        eg2_label = Text("例 2：", font="Noto Sans CJK SC",
                          font_size=24, color=self.C_AUX).move_to(UP * 2.0 + LEFT * 2.5)
        eg2 = MathTex(
            r"4^{\frac{3}{2}} = \sqrt{4^3} = \sqrt{64} = 8",
            font_size=30, color=self.C_EG,
        ).move_to(UP * 2.0 + RIGHT * 0.5)
        self.play(FadeIn(eg2_label), Write(eg2), run_time=0.7)

        # 例 3（分数指数→根号互化）
        eg3_label = Text("例 3：", font="Noto Sans CJK SC",
                          font_size=24, color=self.C_AUX).move_to(UP * 1.0 + LEFT * 2.5)
        eg3 = MathTex(
            r"\sqrt[4]{a^3} = a^{\frac{3}{4}}",
            font_size=30, color=self.C_EG,
        ).move_to(UP * 1.0 + RIGHT * 0.3)
        self.play(FadeIn(eg3_label), Write(eg3), run_time=0.7)

        # 总结提示
        summary = Text(
            "根式 ⟺ 分数指数  随时互换！",
            font="Noto Sans CJK SC", font_size=24, color=self.C_INC,
        ).move_to(DOWN * 0.3)
        sum_box = SurroundingRectangle(summary, color=self.C_INC, buff=0.2,
                                       corner_radius=0.1)
        self.play(Write(summary), Create(sum_box), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(sc_title), FadeOut(rational_formula), FadeOut(box),
            FadeOut(intuition),
            FadeOut(eg1_label), FadeOut(eg1),
            FadeOut(eg2_label), FadeOut(eg2),
            FadeOut(eg3_label), FadeOut(eg3),
            FadeOut(summary), FadeOut(sum_box),
            run_time=0.5,
        )

    # ══════════════════════════════════════════════
    # Scene 5: 总结 + 片尾
    # ══════════════════════════════════════════════
    def scene_5_outro(self):
        sc_title = Text("指数运算口诀", font="Noto Sans CJK SC",
                         font_size=34, color=GOLD).move_to(UP * 6.2)
        self.play(Write(sc_title), run_time=0.5)

        rules_summary = VGroup(
            VGroup(
                Text("①", font="Noto Sans CJK SC", font_size=26, color=self.C_HL),
                MathTex(r"a^m \cdot a^n = a^{m+n}", font_size=26, color=self.C_RULE),
                Text("加", font="Noto Sans CJK SC", font_size=22, color=self.C_INC),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("②", font="Noto Sans CJK SC", font_size=26, color=self.C_HL),
                MathTex(r"\frac{a^m}{a^n} = a^{m-n}", font_size=26, color=self.C_RULE),
                Text("减", font="Noto Sans CJK SC", font_size=22, color=self.C_INC),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("③", font="Noto Sans CJK SC", font_size=26, color=self.C_HL),
                MathTex(r"(a^m)^n = a^{mn}", font_size=26, color=self.C_RULE),
                Text("乘", font="Noto Sans CJK SC", font_size=22, color=self.C_INC),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("④", font="Noto Sans CJK SC", font_size=26, color=self.C_HL),
                MathTex(r"(ab)^n = a^n b^n", font_size=26, color=self.C_RULE),
                Text("分配", font="Noto Sans CJK SC", font_size=22, color=self.C_INC),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.55, aligned_edge=LEFT).move_to(UP * 3.8)

        for row in rules_summary:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.45)

        special_lines = VGroup(
            MathTex(r"a^0 = 1", font_size=28, color=self.C_SPECIAL),
            MathTex(r"a^{-n} = \tfrac{1}{a^n}", font_size=28, color=self.C_SPECIAL),
            MathTex(r"a^{\frac{m}{n}} = \sqrt[n]{a^m}", font_size=28, color=self.C_SPECIAL),
        ).arrange(RIGHT, buff=0.6).move_to(DOWN * 0.5)
        spec_box = SurroundingRectangle(special_lines, color=self.C_SPECIAL,
                                        buff=0.2, corner_radius=0.12)
        self.play(Write(special_lines), Create(spec_box), run_time=0.7)
        self.wait(1.5)

        # 片尾
        self.play(
            FadeOut(sc_title), FadeOut(rules_summary),
            FadeOut(special_lines), FadeOut(spec_box),
            run_time=0.4,
        )

        name_big = Text("上海初高中数学直通车",
                         font="Noto Sans CJK SC", font_size=40, color=WHITE
                         ).move_to(UP * 1.5)
        id_text  = Text("@emptyandcalm",
                         font="Noto Sans CJK SC", font_size=28, color=self.C_AUX
                         ).move_to(UP * 0.6)
        call     = Text("关注我，获得更多数学技巧！",
                         font="Noto Sans CJK SC", font_size=28, color=GOLD
                         ).move_to(DOWN * 0.3)

        self.play(Transform(self.author, name_big), run_time=0.7)
        self.play(FadeIn(id_text, shift=UP * 0.3), run_time=0.4)
        self.play(FadeIn(call, scale=1.1), run_time=0.5)
        self.wait(1.2)
        self.play(FadeOut(self.author), FadeOut(id_text),
                  FadeOut(call), run_time=0.8)