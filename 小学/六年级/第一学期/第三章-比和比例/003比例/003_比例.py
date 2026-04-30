"""
003_比例.py — 比例 教学动画

知识点: 比例的意义、比例的基本性质、解比例
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 比例的意义: 两个比相等的式子 a:b = c:d
  2. 比例的各部分名称: 外项和内项
  3. 比例的基本性质: 外项积 = 内项积 (a*d = b*c)
  4. 解比例: 已知三项求第四项
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR = "#1a1a2e"
COLOR_OUTER = "#ef4444"       # 红色 - 外项
COLOR_INNER = "#3b82f6"       # 蓝色 - 内项
COLOR_EQUAL = "#22c55e"       # 绿色 - 等号/结果
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_FORMULA = "#8b5cf6"     # 紫色公式
COLOR_STEP = "#14b8a6"        # 青色步骤
COLOR_AUTHOR = "#6b7280"
FONT = "PingFang SC"


class ProportionLesson(Scene):
    """
    比例教学动画
    场景:
      1. 开场钩子
      2. 比例的意义 (两个比相等的式子)
      3. 内项和外项
      4. 比例的基本性质 (交叉相乘)
      5. 解比例实例
      6. 总结 + 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_meaning()
        self.scene_3_terms()
        self.scene_4_property()
        self.scene_5_solve()
        self.scene_6_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text(
            "两个比相等", font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 5.0)
        hook2 = Text(
            "就构成了比例！", font=FONT, font_size=48, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.8)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 展示两个比
        ratio1 = MathTex(r"2 : 3", font_size=56, color=COLOR_OUTER)
        eq_sign = MathTex(r"=", font_size=56, color=COLOR_EQUAL)
        ratio2 = MathTex(r"4 : 6", font_size=56, color=COLOR_INNER)
        demo = VGroup(ratio1, eq_sign, ratio2).arrange(RIGHT, buff=0.4).move_to(UP * 1.5)

        self.play(Write(ratio1), run_time=0.5)
        self.play(Write(eq_sign), run_time=0.3)
        self.play(Write(ratio2), run_time=0.5)

        # 验证
        check1 = MathTex(r"\frac{2}{3}", font_size=44, color=COLOR_OUTER)
        check_eq = MathTex(r"=", font_size=44, color=COLOR_EQUAL)
        check2 = MathTex(r"\frac{4}{6}", font_size=44, color=COLOR_INNER)
        check_eq2 = MathTex(r"=", font_size=44, color=COLOR_EQUAL)
        check3 = MathTex(r"\frac{2}{3}", font_size=44, color=COLOR_EQUAL)
        check_line = VGroup(check1, check_eq, check2, check_eq2, check3).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.5)

        self.play(FadeIn(check_line), run_time=0.8)
        self.play(Indicate(check3, scale_factor=1.3, color=COLOR_HL), run_time=0.6)
        self.wait(1.0)

        # 问题引出
        question = Text(
            "比例有什么神奇的性质？", font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(VGroup(hook1, hook2, demo, check_line, question)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: 比例的意义
    # ------------------------------------------------------------------
    def scene_2_meaning(self):
        title = Text(
            "比例的意义", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 定义
        def_text = Text(
            "表示两个比相等的式子", font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 4.5)
        self.play(FadeIn(def_text), run_time=0.5)

        # 记法说明
        note_label = Text("记作:", font=FONT, font_size=24, color=GRAY_A).move_to(UP * 3.2 + LEFT * 2.5)

        form1 = MathTex(r"a : b = c : d", font_size=48, color=WHITE).move_to(UP * 2.2)
        or_text = Text("或", font=FONT, font_size=24, color=GRAY_A).move_to(UP * 1.2)
        form2 = MathTex(r"\frac{a}{b} = \frac{c}{d}", font_size=48, color=WHITE).move_to(UP * 0.2)

        self.play(FadeIn(note_label), run_time=0.3)
        self.play(Write(form1), run_time=0.8)
        self.play(FadeIn(or_text), run_time=0.3)
        self.play(Write(form2), run_time=0.8)
        self.wait(0.5)

        # 具体例子
        ex_label = Text("例如:", font=FONT, font_size=24, color=GRAY_A).move_to(DOWN * 1.2 + LEFT * 2.5)
        ex1 = MathTex(r"2 : 5 = 4 : 10", font_size=40, color=COLOR_STEP).move_to(DOWN * 2.2)
        ex2 = MathTex(r"1 : 3 = 3 : 9", font_size=40, color=COLOR_STEP).move_to(DOWN * 3.2)

        self.play(FadeIn(ex_label), run_time=0.3)
        self.play(Write(ex1), run_time=0.6)
        self.play(Write(ex2), run_time=0.6)

        # 验证
        verify1 = Text(
            "比值都相等!", font=FONT, font_size=24, color=COLOR_EQUAL
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(verify1, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(VGroup(title, def_text, note_label, form1, or_text, form2,
                           ex_label, ex1, ex2, verify1)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 内项和外项
    # ------------------------------------------------------------------
    def scene_3_terms(self):
        title = Text(
            "比例的各部分名称", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 大字显示比例
        # Build a : b = c : d with individual parts for coloring
        prop_a = MathTex(r"a", font_size=64, color=COLOR_OUTER)
        prop_colon1 = MathTex(r":", font_size=64, color=WHITE)
        prop_b = MathTex(r"b", font_size=64, color=COLOR_INNER)
        prop_eq = MathTex(r"=", font_size=64, color=WHITE)
        prop_c = MathTex(r"c", font_size=64, color=COLOR_INNER)
        prop_colon2 = MathTex(r":", font_size=64, color=WHITE)
        prop_d = MathTex(r"d", font_size=64, color=COLOR_OUTER)

        prop_group = VGroup(
            prop_a, prop_colon1, prop_b, prop_eq, prop_c, prop_colon2, prop_d
        ).arrange(RIGHT, buff=0.25).move_to(UP * 3.0)

        self.play(Write(prop_group), run_time=1.0)
        self.wait(0.5)

        # 标注外项
        outer_label = Text("外项", font=FONT, font_size=28, color=COLOR_OUTER).move_to(UP * 0.8)
        outer_brace_left = Brace(prop_a, DOWN, buff=0.15, color=COLOR_OUTER)
        outer_brace_right = Brace(prop_d, DOWN, buff=0.15, color=COLOR_OUTER)

        # Curved arrow connecting a and d (outer terms)
        outer_arrow = CurvedArrow(
            prop_a.get_bottom() + DOWN * 0.6,
            prop_d.get_bottom() + DOWN * 0.6,
            angle=-TAU / 4,
            color=COLOR_OUTER,
            stroke_width=3
        )

        self.play(
            FadeIn(outer_brace_left), FadeIn(outer_brace_right),
            run_time=0.5
        )
        self.play(
            Create(outer_arrow),
            FadeIn(outer_label),
            run_time=0.6
        )
        self.play(
            Indicate(prop_a, color=COLOR_OUTER, scale_factor=1.3),
            Indicate(prop_d, color=COLOR_OUTER, scale_factor=1.3),
            run_time=0.5
        )
        self.wait(0.5)

        # 标注内项
        inner_label = Text("内项", font=FONT, font_size=28, color=COLOR_INNER).move_to(DOWN * 1.5)
        inner_brace = Brace(
            VGroup(prop_b, prop_eq, prop_c), DOWN, buff=0.15, color=COLOR_INNER
        )

        inner_arrow = CurvedArrow(
            prop_b.get_bottom() + DOWN * 0.6,
            prop_c.get_bottom() + DOWN * 0.6,
            angle=-TAU / 6,
            color=COLOR_INNER,
            stroke_width=3
        )

        self.play(
            FadeIn(inner_brace),
            run_time=0.5
        )
        self.play(
            Create(inner_arrow),
            FadeIn(inner_label),
            run_time=0.6
        )
        self.play(
            Indicate(prop_b, color=COLOR_INNER, scale_factor=1.3),
            Indicate(prop_c, color=COLOR_INNER, scale_factor=1.3),
            run_time=0.5
        )
        self.wait(0.5)

        # 具体数字例子
        ex_title = Text("例子:", font=FONT, font_size=24, color=GRAY_A).move_to(DOWN * 3.0 + LEFT * 2.5)

        num_2 = MathTex(r"2", font_size=52, color=COLOR_OUTER)
        num_colon1 = MathTex(r":", font_size=52, color=WHITE)
        num_3 = MathTex(r"3", font_size=52, color=COLOR_INNER)
        num_eq = MathTex(r"=", font_size=52, color=WHITE)
        num_4 = MathTex(r"4", font_size=52, color=COLOR_INNER)
        num_colon2 = MathTex(r":", font_size=52, color=WHITE)
        num_6 = MathTex(r"6", font_size=52, color=COLOR_OUTER)

        num_group = VGroup(
            num_2, num_colon1, num_3, num_eq, num_4, num_colon2, num_6
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 4.2)

        self.play(FadeIn(ex_title), run_time=0.3)
        self.play(Write(num_group), run_time=0.8)

        # Label outer terms
        outer_ex_label = Text("外项: 2, 6", font=FONT, font_size=22, color=COLOR_OUTER).move_to(DOWN * 5.5)
        inner_ex_label = Text("内项: 3, 4", font=FONT, font_size=22, color=COLOR_INNER).move_to(DOWN * 6.2)
        self.play(FadeIn(outer_ex_label), FadeIn(inner_ex_label), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, prop_group,
                outer_label, outer_brace_left, outer_brace_right, outer_arrow,
                inner_label, inner_brace, inner_arrow,
                ex_title, num_group, outer_ex_label, inner_ex_label
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 比例的基本性质
    # ------------------------------------------------------------------
    def scene_4_property(self):
        title = Text(
            "比例的基本性质", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        subtitle = Text(
            "在比例里", font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 4.6)
        self.play(FadeIn(subtitle), run_time=0.3)

        # 性质陈述
        prop_text1 = Text(
            "两个外项的积", font=FONT, font_size=30, color=COLOR_OUTER
        )
        prop_text2 = Text(
            " = ", font=FONT, font_size=30, color=WHITE
        )
        prop_text3 = Text(
            "两个内项的积", font=FONT, font_size=30, color=COLOR_INNER
        )
        prop_statement = VGroup(prop_text1, prop_text2, prop_text3).arrange(RIGHT, buff=0.1).move_to(UP * 3.6)
        self.play(FadeIn(prop_statement), run_time=0.6)

        # 公式
        formula = MathTex(r"a \times d = b \times c", font_size=52, color=WHITE).move_to(UP * 2.3)
        self.play(Write(formula), run_time=0.8)

        # 高亮外项部分 a*d
        box_ad = SurroundingRectangle(
            formula[0][0:3],  # a * d
            color=COLOR_OUTER, buff=0.1, corner_radius=0.1
        )
        label_ad = Text("外项积", font=FONT, font_size=20, color=COLOR_OUTER).next_to(box_ad, UP, buff=0.1)
        self.play(Create(box_ad), FadeIn(label_ad), run_time=0.5)
        self.wait(0.3)

        # 高亮内项部分 b*c
        box_bc = SurroundingRectangle(
            formula[0][4:7],  # b * c
            color=COLOR_INNER, buff=0.1, corner_radius=0.1
        )
        label_bc = Text("内项积", font=FONT, font_size=20, color=COLOR_INNER).next_to(box_bc, DOWN, buff=0.1)
        self.play(Create(box_bc), FadeIn(label_bc), run_time=0.5)
        self.wait(0.5)

        # 用具体数字验证
        self.play(FadeOut(VGroup(box_ad, label_ad, box_bc, label_bc)), run_time=0.3)

        verify_title = Text("验证:", font=FONT, font_size=26, color=GRAY_A).move_to(DOWN * 0.0 + LEFT * 2.5)
        self.play(FadeIn(verify_title), run_time=0.3)

        # 2:3 = 4:6
        ex_prop = MathTex(r"2 : 3 = 4 : 6", font_size=44, color=WHITE).move_to(DOWN * 1.0)
        self.play(Write(ex_prop), run_time=0.6)

        # 外项积
        outer_calc = MathTex(r"2 \times 6 = 12", font_size=40, color=COLOR_OUTER).move_to(DOWN * 2.3)
        outer_label2 = Text("外项积", font=FONT, font_size=20, color=COLOR_OUTER).next_to(outer_calc, LEFT, buff=0.3)
        self.play(Write(outer_calc), FadeIn(outer_label2), run_time=0.6)

        # 内项积
        inner_calc = MathTex(r"3 \times 4 = 12", font_size=40, color=COLOR_INNER).move_to(DOWN * 3.3)
        inner_label2 = Text("内项积", font=FONT, font_size=20, color=COLOR_INNER).next_to(inner_calc, LEFT, buff=0.3)
        self.play(Write(inner_calc), FadeIn(inner_label2), run_time=0.6)

        # 结论
        equal_sign = MathTex(r"12 = 12", font_size=48, color=COLOR_EQUAL).move_to(DOWN * 4.6)
        check_mark = Text("  !", font=FONT, font_size=28, color=COLOR_EQUAL).next_to(equal_sign, RIGHT, buff=0.2)

        self.play(Write(equal_sign), run_time=0.5)
        self.play(FadeIn(check_mark, scale=1.5), run_time=0.4)

        # 交叉相乘示意图
        cross_label = Text(
            "交叉相乘", font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 5.8)
        self.play(FadeIn(cross_label, shift=UP * 0.2), run_time=0.4)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(
                title, subtitle, prop_statement, formula,
                verify_title, ex_prop,
                outer_calc, outer_label2, inner_calc, inner_label2,
                equal_sign, check_mark, cross_label
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 解比例
    # ------------------------------------------------------------------
    def scene_5_solve(self):
        title = Text(
            "解比例", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        desc = Text(
            "已知三项，求第四项", font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 4.6)
        self.play(FadeIn(desc), run_time=0.4)

        # 题目
        prob_label = Text("例题:", font=FONT, font_size=26, color=WHITE).move_to(UP * 3.5 + LEFT * 2.0)
        prob = MathTex(r"x : 3 = 4 : 6", font_size=48, color=WHITE).move_to(UP * 2.5)
        self.play(FadeIn(prob_label), Write(prob), run_time=0.8)
        self.wait(0.5)

        # Step 1: 根据基本性质
        step1_label = Text("第一步:", font=FONT, font_size=22, color=COLOR_STEP).move_to(UP * 1.2 + LEFT * 2.5)
        step1_desc = Text(
            "外项积 = 内项积", font=FONT, font_size=22, color=GRAY_A
        ).next_to(step1_label, RIGHT, buff=0.2)
        step1 = MathTex(r"x \times 6 = 3 \times 4", font_size=44, color=WHITE).move_to(UP * 0.3)

        self.play(FadeIn(step1_label), FadeIn(step1_desc), run_time=0.4)
        self.play(Write(step1), run_time=0.8)

        # 高亮外项和内项
        # x is outer, 6 is outer
        box_x = SurroundingRectangle(prob[0][0], color=COLOR_OUTER, buff=0.08, corner_radius=0.05)
        box_6 = SurroundingRectangle(prob[0][5], color=COLOR_OUTER, buff=0.08, corner_radius=0.05)
        box_3 = SurroundingRectangle(prob[0][2], color=COLOR_INNER, buff=0.08, corner_radius=0.05)
        box_4 = SurroundingRectangle(prob[0][4], color=COLOR_INNER, buff=0.08, corner_radius=0.05)

        self.play(Create(box_x), Create(box_6), run_time=0.4)
        self.play(Create(box_3), Create(box_4), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(VGroup(box_x, box_6, box_3, box_4)), run_time=0.3)

        # Step 2: 计算
        step2_label = Text("第二步:", font=FONT, font_size=22, color=COLOR_STEP).move_to(DOWN * 1.0 + LEFT * 2.5)
        step2_desc = Text(
            "计算已知项", font=FONT, font_size=22, color=GRAY_A
        ).next_to(step2_label, RIGHT, buff=0.2)
        step2 = MathTex(r"6x = 12", font_size=44, color=WHITE).move_to(DOWN * 2.0)

        self.play(FadeIn(step2_label), FadeIn(step2_desc), run_time=0.4)
        self.play(Write(step2), run_time=0.6)

        # Step 3: 求解
        step3_label = Text("第三步:", font=FONT, font_size=22, color=COLOR_STEP).move_to(DOWN * 3.2 + LEFT * 2.5)
        step3_desc = Text(
            "求x", font=FONT, font_size=22, color=GRAY_A
        ).next_to(step3_label, RIGHT, buff=0.2)
        step3 = MathTex(r"x = 12 \div 6 = 2", font_size=44, color=WHITE).move_to(DOWN * 4.2)

        self.play(FadeIn(step3_label), FadeIn(step3_desc), run_time=0.4)
        self.play(Write(step3), run_time=0.8)

        # 高亮答案
        answer_box = SurroundingRectangle(
            step3[0][-1], color=COLOR_EQUAL, buff=0.12, corner_radius=0.1
        )
        self.play(Create(answer_box), run_time=0.4)

        # 验证
        verify = Text(
            "验证: 2:3 = 4:6", font=FONT, font_size=24, color=COLOR_EQUAL
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(verify, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(
                title, desc, prob_label, prob,
                step1_label, step1_desc, step1,
                step2_label, step2_desc, step2,
                step3_label, step3_desc, step3,
                answer_box, verify
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 总结 + 片尾
    # ------------------------------------------------------------------
    def scene_6_outro(self):
        # 总结
        summary_title = Text(
            "总结", font=FONT, font_size=40, color=COLOR_HL
        ).move_to(UP * 5.0)
        self.play(Write(summary_title), run_time=0.5)

        # 三个要点
        points = [
            ("1. 比例的意义", "两个比相等的式子", UP * 3.2),
            ("2. 基本性质", "外项积 = 内项积", UP * 1.4),
            ("3. 解比例", "已知三项，求第四项", DOWN * 0.4),
        ]

        point_mobs = []
        for pt_title, pt_desc, pos in points:
            pt = VGroup(
                Text(pt_title, font=FONT, font_size=28, color=WHITE),
                Text(pt_desc, font=FONT, font_size=22, color=GRAY_A),
            ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).move_to(pos)
            point_mobs.append(pt)

        # 对应公式
        formulas = [
            MathTex(r"a : b = c : d", font_size=36, color=COLOR_FORMULA).move_to(UP * 2.2),
            MathTex(r"a \times d = b \times c", font_size=36, color=COLOR_FORMULA).move_to(UP * 0.4),
            MathTex(r"x : 3 = 4 : 6 \Rightarrow x = 2", font_size=34, color=COLOR_FORMULA).move_to(DOWN * 1.4),
        ]

        for pt, fm in zip(point_mobs, formulas):
            self.play(FadeIn(pt, shift=RIGHT * 0.3), run_time=0.5)
            self.play(Write(fm), run_time=0.5)
            self.wait(0.3)

        self.wait(1.5)

        # 清理总结
        all_summary = VGroup(summary_title, *point_mobs, *formulas)
        self.play(FadeOut(all_summary), run_time=0.5)

        # 片尾
        author_name = Text(
            "上海初高中数学直通车", font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 1.5)
        author_id = Text(
            "@emptyandcalm", font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(
            Transform(self.author_mob, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow_text = Text(
            "关注我，获得更多数学技巧!", font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(self.author_mob),
            FadeOut(author_id),
            FadeOut(follow_text),
            run_time=1.0
        )
