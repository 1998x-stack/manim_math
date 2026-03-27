"""
004_按比例分配.py — 按比例分配 教学动画

知识点: 按比例分配的方法与应用
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 什么是按比例分配
  2. 方法步骤: 总份数 -> 每份 -> 各部分
  3. 具体例题: 将100按2:3:5分配
  4. 条形可视化验证
  5. 实际应用题
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
COLOR_PART1 = "#ef4444"      # 红色 - 第一份
COLOR_PART2 = "#3b82f6"      # 蓝色 - 第二份
COLOR_PART3 = "#22c55e"      # 绿色 - 第三份
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_FORMULA = "#8b5cf6"    # 紫色公式
COLOR_STEP = "#14b8a6"       # 青色步骤
COLOR_TOTAL = "#f97316"      # 橙色 - 总量
COLOR_AUTHOR = "#6b7280"
FONT = "Noto Sans CJK SC"


class ProportionalDistributionLesson(Scene):
    """
    按比例分配教学动画
    场景:
      1. 开场钩子
      2. 概念引入 (什么是按比例分配)
      3. 方法步骤
      4. 条形可视化 (将100按2:3:5分配)
      5. 计算过程
      6. 总结 + 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_concept()
        self.scene_3_method()
        self.scene_4_visual_bar()
        self.scene_5_calculation()
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
            "100元奖金", font=FONT, font_size=44, color=WHITE
        ).move_to(UP * 5.0)
        hook2 = Text(
            "按 2 : 3 : 5 分给三人", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 3.8)
        hook3 = Text(
            "每人分多少？", font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 2.4)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.play(Write(hook3), run_time=0.6)
        self.wait(0.5)

        # 三个问号人物用彩色圆表示
        person_a = VGroup(
            Circle(radius=0.4, color=COLOR_PART1, fill_opacity=0.8),
            MathTex(r"?", font_size=36, color=WHITE),
        ).move_to(DOWN * 0.2 + LEFT * 2.5)
        person_a[1].move_to(person_a[0].get_center())

        person_b = VGroup(
            Circle(radius=0.4, color=COLOR_PART2, fill_opacity=0.8),
            MathTex(r"?", font_size=36, color=WHITE),
        ).move_to(DOWN * 0.2)
        person_b[1].move_to(person_b[0].get_center())

        person_c = VGroup(
            Circle(radius=0.4, color=COLOR_PART3, fill_opacity=0.8),
            MathTex(r"?", font_size=36, color=WHITE),
        ).move_to(DOWN * 0.2 + RIGHT * 2.5)
        person_c[1].move_to(person_c[0].get_center())

        pa_label = Text("2", font=FONT, font_size=28, color=COLOR_PART1).next_to(person_a, DOWN, buff=0.2)
        pb_label = Text("3", font=FONT, font_size=28, color=COLOR_PART2).next_to(person_b, DOWN, buff=0.2)
        pc_label = Text("5", font=FONT, font_size=28, color=COLOR_PART3).next_to(person_c, DOWN, buff=0.2)

        people = VGroup(person_a, person_b, person_c, pa_label, pb_label, pc_label)

        self.play(
            FadeIn(person_a, scale=0.5),
            FadeIn(person_b, scale=0.5),
            FadeIn(person_c, scale=0.5),
            run_time=0.6
        )
        self.play(FadeIn(pa_label), FadeIn(pb_label), FadeIn(pc_label), run_time=0.4)
        self.wait(1.0)

        # 引导问题
        question = Text(
            "这就是按比例分配!", font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(VGroup(hook1, hook2, hook3, people, question)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: 概念引入
    # ------------------------------------------------------------------
    def scene_2_concept(self):
        title = Text(
            "什么是按比例分配？", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 定义
        def_text1 = Text(
            "把一个量按照一定的比", font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 4.2)
        def_text2 = Text(
            "分成若干份", font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 3.5)
        self.play(FadeIn(def_text1), run_time=0.5)
        self.play(FadeIn(def_text2), run_time=0.5)
        self.wait(0.5)

        # 对比: 平均分 vs 按比例分
        vs_title = Text(
            "平均分 vs 按比例分", font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 2.2)
        self.play(FadeIn(vs_title), run_time=0.4)

        # 平均分 bar (3等份)
        avg_label = Text("平均分:", font=FONT, font_size=22, color=GRAY_A).move_to(UP * 1.4 + LEFT * 2.8)
        bar_width = 6.0
        bar_height = 0.6
        avg_bar = VGroup()
        avg_colors = [COLOR_PART1, COLOR_PART2, COLOR_PART3]
        for i in range(3):
            seg_w = bar_width / 3
            rect = Rectangle(
                width=seg_w, height=bar_height,
                fill_color=avg_colors[i], fill_opacity=0.6,
                stroke_color=WHITE, stroke_width=1.5
            )
            rect.move_to(LEFT * (bar_width / 2 - seg_w / 2) + RIGHT * i * seg_w + UP * 0.5)
            avg_bar.add(rect)

        self.play(FadeIn(avg_label), run_time=0.3)
        self.play(*[FadeIn(r) for r in avg_bar], run_time=0.6)

        # 按比例分 bar (2:3:5)
        prop_label = Text("按 2:3:5 分:", font=FONT, font_size=22, color=GRAY_A).move_to(DOWN * 0.8 + LEFT * 2.5)
        prop_bar = VGroup()
        ratios = [2, 3, 5]
        total_ratio = sum(ratios)
        x_start = -bar_width / 2
        for i, r in enumerate(ratios):
            seg_w = bar_width * r / total_ratio
            rect = Rectangle(
                width=seg_w, height=bar_height,
                fill_color=avg_colors[i], fill_opacity=0.6,
                stroke_color=WHITE, stroke_width=1.5
            )
            rect.move_to(np.array([x_start + seg_w / 2, -1.7, 0]))
            x_start += seg_w
            prop_bar.add(rect)

        self.play(FadeIn(prop_label), run_time=0.3)
        self.play(*[FadeIn(r) for r in prop_bar], run_time=0.6)

        # Labels on proportional bar
        ratio_labels = VGroup(
            Text("2", font=FONT, font_size=22, color=COLOR_PART1),
            Text("3", font=FONT, font_size=22, color=COLOR_PART2),
            Text("5", font=FONT, font_size=22, color=COLOR_PART3),
        )
        for i, lbl in enumerate(ratio_labels):
            lbl.move_to(prop_bar[i].get_center())
        self.play(FadeIn(ratio_labels), run_time=0.4)

        diff_text = Text(
            "份数不同，分到的量也不同!", font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(diff_text, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(VGroup(title, def_text1, def_text2, vs_title,
                           avg_label, avg_bar, prop_label, prop_bar,
                           ratio_labels, diff_text)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 方法步骤
    # ------------------------------------------------------------------
    def scene_3_method(self):
        title = Text(
            "三步搞定按比例分配", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # Step 1
        s1_num = Text("1", font=FONT, font_size=36, color="#1a1a2e", weight=BOLD)
        s1_circle = Circle(radius=0.35, color=COLOR_STEP, fill_opacity=1.0, stroke_width=0)
        s1_num.move_to(s1_circle.get_center())
        s1_icon = VGroup(s1_circle, s1_num).move_to(UP * 4.0 + LEFT * 3.0)

        s1_title = Text("求总份数", font=FONT, font_size=28, color=WHITE)
        s1_desc = Text("把比的各项加起来", font=FONT, font_size=22, color=GRAY_A)
        s1_text = VGroup(s1_title, s1_desc).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        s1_text.next_to(s1_icon, RIGHT, buff=0.3)

        s1_formula = MathTex(r"2 + 3 + 5 = 10", font_size=40, color=COLOR_STEP).move_to(UP * 2.6)
        s1_label = Text("总份数", font=FONT, font_size=20, color=COLOR_STEP).next_to(s1_formula, RIGHT, buff=0.3)

        self.play(FadeIn(s1_icon, scale=0.5), FadeIn(s1_text, shift=RIGHT * 0.3), run_time=0.6)
        self.play(Write(s1_formula), FadeIn(s1_label), run_time=0.7)
        self.wait(0.5)

        # Step 2
        s2_num = Text("2", font=FONT, font_size=36, color="#1a1a2e", weight=BOLD)
        s2_circle = Circle(radius=0.35, color=COLOR_FORMULA, fill_opacity=1.0, stroke_width=0)
        s2_num.move_to(s2_circle.get_center())
        s2_icon = VGroup(s2_circle, s2_num).move_to(UP * 1.3 + LEFT * 3.0)

        s2_title = Text("求每份是多少", font=FONT, font_size=28, color=WHITE)
        s2_desc = Text("总量 / 总份数", font=FONT, font_size=22, color=GRAY_A)
        s2_text = VGroup(s2_title, s2_desc).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        s2_text.next_to(s2_icon, RIGHT, buff=0.3)

        s2_formula = MathTex(
            r"100 \div 10 = 10", font_size=40, color=COLOR_FORMULA
        ).move_to(DOWN * 0.1)
        s2_label = Text("每份", font=FONT, font_size=20, color=COLOR_FORMULA).next_to(s2_formula, RIGHT, buff=0.3)

        self.play(FadeIn(s2_icon, scale=0.5), FadeIn(s2_text, shift=RIGHT * 0.3), run_time=0.6)
        self.play(Write(s2_formula), FadeIn(s2_label), run_time=0.7)
        self.wait(0.5)

        # Step 3
        s3_num = Text("3", font=FONT, font_size=36, color="#1a1a2e", weight=BOLD)
        s3_circle = Circle(radius=0.35, color=COLOR_TOTAL, fill_opacity=1.0, stroke_width=0)
        s3_num.move_to(s3_circle.get_center())
        s3_icon = VGroup(s3_circle, s3_num).move_to(DOWN * 1.5 + LEFT * 3.0)

        s3_title = Text("求各部分量", font=FONT, font_size=28, color=WHITE)
        s3_desc = Text("每份 x 对应比数", font=FONT, font_size=22, color=GRAY_A)
        s3_text = VGroup(s3_title, s3_desc).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        s3_text.next_to(s3_icon, RIGHT, buff=0.3)

        s3_f1 = MathTex(r"10 \times 2 = 20", font_size=36, color=COLOR_PART1).move_to(DOWN * 3.0)
        s3_f2 = MathTex(r"10 \times 3 = 30", font_size=36, color=COLOR_PART2).move_to(DOWN * 3.8)
        s3_f3 = MathTex(r"10 \times 5 = 50", font_size=36, color=COLOR_PART3).move_to(DOWN * 4.6)

        self.play(FadeIn(s3_icon, scale=0.5), FadeIn(s3_text, shift=RIGHT * 0.3), run_time=0.6)
        self.play(Write(s3_f1), run_time=0.5)
        self.play(Write(s3_f2), run_time=0.5)
        self.play(Write(s3_f3), run_time=0.5)
        self.wait(0.5)

        # Verify
        verify = MathTex(
            r"20 + 30 + 50 = 100", font_size=40, color=COLOR_HL
        ).move_to(DOWN * 5.8)
        check_label = Text("验证", font=FONT, font_size=20, color=COLOR_HL).next_to(verify, LEFT, buff=0.3)
        self.play(Write(verify), FadeIn(check_label), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title,
                           s1_icon, s1_text, s1_formula, s1_label,
                           s2_icon, s2_text, s2_formula, s2_label,
                           s3_icon, s3_text, s3_f1, s3_f2, s3_f3,
                           verify, check_label)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 条形可视化
    # ------------------------------------------------------------------
    def scene_4_visual_bar(self):
        title = Text(
            "直观感受按比例分配", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        desc = Text(
            "100元按 2:3:5 分配", font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 4.6)
        self.play(FadeIn(desc), run_time=0.4)

        # Full bar representing 100
        bar_width = 7.0
        bar_height = 1.0
        full_bar = Rectangle(
            width=bar_width, height=bar_height,
            color=COLOR_TOTAL, fill_opacity=0.3,
            stroke_color=COLOR_TOTAL, stroke_width=2
        ).move_to(UP * 3.0)
        full_label = Text(
            "100 元", font=FONT, font_size=24, color=COLOR_TOTAL
        ).next_to(full_bar, UP, buff=0.15)

        self.play(FadeIn(full_bar), FadeIn(full_label), run_time=0.5)
        self.wait(0.3)

        # Split into 10 equal parts
        ten_parts = VGroup()
        seg_w = bar_width / 10
        x_start = full_bar.get_left()[0] + seg_w / 2
        for i in range(10):
            seg = Rectangle(
                width=seg_w * 0.95, height=bar_height * 0.9,
                fill_color=GRAY_B, fill_opacity=0.3,
                stroke_color=WHITE, stroke_width=1
            )
            seg.move_to(np.array([x_start + i * seg_w, UP[1] * 3.0, 0]))
            ten_parts.add(seg)

        ten_label = Text(
            "10 份", font=FONT, font_size=22, color=GRAY_A
        ).next_to(full_bar, DOWN, buff=0.15)

        self.play(
            FadeIn(ten_parts, lag_ratio=0.05),
            FadeIn(ten_label),
            run_time=1.0
        )
        self.wait(0.5)

        # Color the segments: 2 red, 3 blue, 5 green
        colors = [COLOR_PART1] * 2 + [COLOR_PART2] * 3 + [COLOR_PART3] * 5
        color_anims = []
        for i, c in enumerate(colors):
            color_anims.append(ten_parts[i].animate.set_fill(c, opacity=0.7))
        self.play(*color_anims, run_time=1.0)
        self.wait(0.3)

        # Arrows pointing down to grouped bars
        arrow_y = UP * 1.5

        # Group bars: 2 parts
        group1_bar = Rectangle(
            width=seg_w * 2, height=1.2,
            fill_color=COLOR_PART1, fill_opacity=0.7,
            stroke_color=WHITE, stroke_width=2
        ).move_to(np.array([full_bar.get_left()[0] + seg_w, 0, 0]))
        g1_label = Text("20 元", font=FONT, font_size=24, color=WHITE).move_to(group1_bar.get_center())
        g1_ratio = Text("2 份", font=FONT, font_size=20, color=COLOR_PART1).next_to(group1_bar, DOWN, buff=0.15)

        # Group bars: 3 parts
        group2_bar = Rectangle(
            width=seg_w * 3, height=1.2,
            fill_color=COLOR_PART2, fill_opacity=0.7,
            stroke_color=WHITE, stroke_width=2
        ).move_to(np.array([full_bar.get_left()[0] + seg_w * 2 + seg_w * 1.5, 0, 0]))
        g2_label = Text("30 元", font=FONT, font_size=24, color=WHITE).move_to(group2_bar.get_center())
        g2_ratio = Text("3 份", font=FONT, font_size=20, color=COLOR_PART2).next_to(group2_bar, DOWN, buff=0.15)

        # Group bars: 5 parts
        group3_bar = Rectangle(
            width=seg_w * 5, height=1.2,
            fill_color=COLOR_PART3, fill_opacity=0.7,
            stroke_color=WHITE, stroke_width=2
        ).move_to(np.array([full_bar.get_left()[0] + seg_w * 5 + seg_w * 2.5, 0, 0]))
        g3_label = Text("50 元", font=FONT, font_size=24, color=WHITE).move_to(group3_bar.get_center())
        g3_ratio = Text("5 份", font=FONT, font_size=20, color=COLOR_PART3).next_to(group3_bar, DOWN, buff=0.15)

        # Arrows from 10-parts to grouped bars
        arrow1 = Arrow(
            ten_parts[0].get_bottom(), group1_bar.get_top(),
            color=COLOR_PART1, buff=0.1, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        arrow2 = Arrow(
            ten_parts[3].get_bottom(), group2_bar.get_top(),
            color=COLOR_PART2, buff=0.1, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        arrow3 = Arrow(
            ten_parts[7].get_bottom(), group3_bar.get_top(),
            color=COLOR_PART3, buff=0.1, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )

        self.play(
            FadeIn(group1_bar), FadeIn(g1_label), FadeIn(g1_ratio),
            Create(arrow1),
            run_time=0.6
        )
        self.play(
            FadeIn(group2_bar), FadeIn(g2_label), FadeIn(g2_ratio),
            Create(arrow2),
            run_time=0.6
        )
        self.play(
            FadeIn(group3_bar), FadeIn(g3_label), FadeIn(g3_ratio),
            Create(arrow3),
            run_time=0.6
        )
        self.wait(0.5)

        # Formula below
        formula_text = Text(
            "份数越多，分到越多!", font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(formula_text, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, desc, full_bar, full_label, ten_parts, ten_label,
                group1_bar, g1_label, g1_ratio,
                group2_bar, g2_label, g2_ratio,
                group3_bar, g3_label, g3_ratio,
                arrow1, arrow2, arrow3,
                formula_text
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 完整计算过程 (另一种方法: 分数法)
    # ------------------------------------------------------------------
    def scene_5_calculation(self):
        title = Text(
            "分数法 (更快!)", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        desc = Text(
            "直接用分数求各部分", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.7)
        self.play(FadeIn(desc), run_time=0.4)

        # Problem
        prob = Text(
            "100元 按 2:3:5 分配", font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 3.6)
        self.play(FadeIn(prob), run_time=0.4)

        # Total parts
        total_line = VGroup(
            Text("总份数:", font=FONT, font_size=24, color=GRAY_A),
            MathTex(r"2 + 3 + 5 = 10", font_size=36, color=COLOR_STEP),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.5)
        self.play(FadeIn(total_line), run_time=0.5)

        # Part 1: fraction method
        part1_label = Text("第一份:", font=FONT, font_size=22, color=COLOR_PART1)
        part1_formula = MathTex(
            r"100 \times \frac{2}{10} = 20",
            font_size=38, color=COLOR_PART1
        )
        part1_line = VGroup(part1_label, part1_formula).arrange(RIGHT, buff=0.3).move_to(UP * 1.2)

        self.play(FadeIn(part1_label), Write(part1_formula), run_time=0.7)

        # Highlight the fraction
        frac_box1 = SurroundingRectangle(
            part1_formula[0][4:8], color=COLOR_HL, buff=0.06, corner_radius=0.08
        )
        frac_note1 = Text(
            "占总量的比", font=FONT, font_size=18, color=COLOR_HL
        ).next_to(frac_box1, DOWN, buff=0.1)
        self.play(Create(frac_box1), FadeIn(frac_note1), run_time=0.5)
        self.wait(0.3)
        self.play(FadeOut(frac_box1), FadeOut(frac_note1), run_time=0.3)

        # Part 2
        part2_label = Text("第二份:", font=FONT, font_size=22, color=COLOR_PART2)
        part2_formula = MathTex(
            r"100 \times \frac{3}{10} = 30",
            font_size=38, color=COLOR_PART2
        )
        part2_line = VGroup(part2_label, part2_formula).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.2)
        self.play(FadeIn(part2_label), Write(part2_formula), run_time=0.7)

        # Part 3
        part3_label = Text("第三份:", font=FONT, font_size=22, color=COLOR_PART3)
        part3_formula = MathTex(
            r"100 \times \frac{5}{10} = 50",
            font_size=38, color=COLOR_PART3
        )
        part3_line = VGroup(part3_label, part3_formula).arrange(RIGHT, buff=0.3).move_to(DOWN * 1.5)
        self.play(FadeIn(part3_label), Write(part3_formula), run_time=0.7)
        self.wait(0.5)

        # Verify
        verify_line = VGroup(
            Text("验证:", font=FONT, font_size=22, color=COLOR_HL),
            MathTex(r"20 + 30 + 50 = 100", font_size=38, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 3.0)
        self.play(FadeIn(verify_line), run_time=0.5)

        check = MathTex(r"\checkmark", font_size=48, color=COLOR_HL).next_to(verify_line, RIGHT, buff=0.3)
        self.play(FadeIn(check, scale=1.5), run_time=0.4)

        # Key takeaway
        key_text = Text(
            "分数法公式:", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 4.5)
        key_formula_label = Text("各部分 = 总量", font=FONT, font_size=22, color=WHITE)
        key_formula_math = MathTex(
            r"\times \frac{" + r"\text{corresponding ratio}}{\text{sum of ratios}}",
            font_size=28, color=WHITE
        )
        # Use Chinese text instead for the formula explanation
        key_formula = VGroup(
            Text("各部分量", font=FONT, font_size=24, color=WHITE),
            MathTex(r"=", font_size=30, color=WHITE),
            Text("总量", font=FONT, font_size=24, color=COLOR_TOTAL),
            MathTex(r"\times", font_size=30, color=WHITE),
            MathTex(r"\frac{\text{ratio}}{\text{total}}",
                    font_size=30, color=COLOR_FORMULA),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 5.5)

        self.play(FadeIn(key_text), FadeIn(key_formula), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(
                title, desc, prob, total_line,
                part1_line, part2_line, part3_line,
                verify_line, check,
                key_text, key_formula
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 总结 + 片尾
    # ------------------------------------------------------------------
    def scene_6_outro(self):
        # Summary
        summary_title = Text(
            "总结", font=FONT, font_size=40, color=COLOR_HL
        ).move_to(UP * 5.0)
        self.play(Write(summary_title), run_time=0.5)

        points = [
            ("1. 求总份数", "比的各项相加", UP * 3.5),
            ("2. 求各部分占总量的比", "各项 / 总份数", UP * 1.8),
            ("3. 求各部分量", "总量 x 对应分数", UP * 0.1),
        ]

        point_mobs = []
        for pt_title, pt_desc, pos in points:
            pt = VGroup(
                Text(pt_title, font=FONT, font_size=28, color=WHITE),
                Text(pt_desc, font=FONT, font_size=22, color=GRAY_A),
            ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to(pos)
            point_mobs.append(pt)
            self.play(FadeIn(pt, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        # Example recap
        recap = MathTex(
            r"100 \xrightarrow{2:3:5} 20, 30, 50",
            font_size=38, color=COLOR_FORMULA
        ).move_to(DOWN * 1.8)
        self.play(Write(recap), run_time=0.7)
        self.wait(1.5)

        # Clean up summary
        all_summary = VGroup(summary_title, *point_mobs, recap)
        self.play(FadeOut(all_summary), run_time=0.5)

        # Outro
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
