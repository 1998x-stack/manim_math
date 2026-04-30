"""
乘法的引入 - Multiplication Introduction Animation
小学二年级上册 第二章 乘法、除法（一）

内容: 乘法的引入 — 从连加到乘法
目标观众: 小学二年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ─── 全局配置 TikTok 竖屏 ───────────────────────────────────────────────────
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ─── 配色方案 ────────────────────────────────────────────────────────────────
C_BG         = "#1a1a2e"
C_TITLE      = "#f9c74f"
C_APPLE      = "#e63946"
C_BOX        = "#4cc9f0"
C_BOX_FILL   = "#023e8a"
C_ARROW      = "#06d6a0"
C_MULT       = "#f77f00"
C_LABEL      = "#b5ead7"
C_DIM        = "#6b7280"
C_WHITE      = WHITE
C_HIGHLIGHT  = "#ffd166"


class MultiplicationIntroLesson(Scene):
    """
    场景顺序:
    1. 开场 / 钩子
    2. 情境引入 — 3组苹果
    3. 连加算式
    4. 发现规律 — 相同加数
    5. 引入乘号与乘法算式
    6. 各部分名称
    7. 总结
    8. 片尾
    """

    def construct(self):
        self.camera.background_color = C_BG

        # 作者标识（全程保留在顶部）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color=C_DIM,
        ).move_to(UP * 7.0)
        self.add(self.author)

        self.scene_1_hook()
        self.scene_2_apples()
        self.scene_3_addition()
        self.scene_4_same_addend()
        self.scene_5_multiplication()
        self.scene_6_parts()
        self.scene_7_summary()
        self.scene_8_outro()

    # ═══════════════════════════════════════════════════════════════════════
    # Scene 1 — 钩子 (Hook)
    # ═══════════════════════════════════════════════════════════════════════
    def scene_1_hook(self):
        title = Text(
            "乘法的引入",
            font="PingFang SC",
            font_size=54,
            color=C_TITLE,
            weight=BOLD,
        ).move_to(UP * 5.5)

        sub = Text(
            "连加太麻烦？用乘法更简单！",
            font="PingFang SC",
            font_size=28,
            color=C_LABEL,
        ).move_to(UP * 4.4)

        self.play(Write(title), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)

        self.play(FadeOut(title), FadeOut(sub), run_time=0.5)

    # ═══════════════════════════════════════════════════════════════════════
    # Scene 2 — 情境：3 组苹果，每组 4 个
    # ═══════════════════════════════════════════════════════════════════════
    def scene_2_apples(self):
        prompt = Text(
            "每盘放 4 个苹果，放了 3 盘",
            font="PingFang SC",
            font_size=30,
            color=C_LABEL,
        ).move_to(UP * 6.0)

        question = Text(
            "一共有多少个苹果？",
            font="PingFang SC",
            font_size=34,
            color=C_HIGHLIGHT,
        ).move_to(UP * 5.1)

        self.play(FadeIn(prompt, shift=DOWN * 0.2), run_time=0.6)
        self.play(Write(question), run_time=0.7)
        self.wait(0.4)

        # 创建3组苹果盘
        # 每盘是一个圆形容器 + 4个苹果圆点
        plates = VGroup()
        plate_centers = [
            np.array([-2.6, 1.5, 0]),
            np.array([0.0,  1.5, 0]),
            np.array([2.6,  1.5, 0]),
        ]

        apple_positions_per_plate = [
            [np.array([-0.35,  0.25, 0]), np.array([0.35,  0.25, 0]),
             np.array([-0.35, -0.25, 0]), np.array([0.35, -0.25, 0])],
        ]

        self.plates_group = VGroup()
        self.apple_groups = []

        for idx, center in enumerate(plate_centers):
            # 盘子
            plate = Circle(
                radius=0.8,
                color=C_BOX,
                fill_color=C_BOX_FILL,
                fill_opacity=0.35,
                stroke_width=3,
            ).move_to(center)

            # 4个苹果
            apple_offsets = [
                np.array([-0.28,  0.22, 0]),
                np.array([ 0.28,  0.22, 0]),
                np.array([-0.28, -0.22, 0]),
                np.array([ 0.28, -0.22, 0]),
            ]
            apples = VGroup(*[
                Circle(
                    radius=0.18,
                    color=C_APPLE,
                    fill_color=C_APPLE,
                    fill_opacity=0.9,
                    stroke_width=0,
                ).move_to(center + offset)
                for offset in apple_offsets
            ])

            # 标签 "4个"
            count_label = Text(
                "4个",
                font="PingFang SC",
                font_size=22,
                color=C_HIGHLIGHT,
            ).next_to(plate, DOWN, buff=0.15)

            group = VGroup(plate, apples, count_label)
            plates.add(group)
            self.plates_group.add(group)
            self.apple_groups.append(apples)

        # 盘序号
        plate_labels = VGroup(*[
            Text(
                f"第{['一','二','三'][i]}盘",
                font="PingFang SC",
                font_size=20,
                color=C_DIM,
            ).next_to(plates[i], UP, buff=0.12)
            for i in range(3)
        ])

        # 逐盘出现
        for i in range(3):
            self.play(
                FadeIn(plates[i], scale=0.8),
                FadeIn(plate_labels[i], shift=DOWN * 0.1),
                run_time=0.55,
            )
            self.wait(0.15)

        self.wait(1.0)
        self.prompt_text = prompt
        self.question_text = question
        self.plate_labels = plate_labels

    # ═══════════════════════════════════════════════════════════════════════
    # Scene 3 — 连加算式
    # ═══════════════════════════════════════════════════════════════════════
    def scene_3_addition(self):
        step_title = Text(
            "列出连加算式",
            font="PingFang SC",
            font_size=32,
            color=C_TITLE,
        ).move_to(UP * 3.8)

        self.play(
            FadeOut(self.prompt_text),
            FadeOut(self.question_text),
            FadeIn(step_title, shift=DOWN * 0.2),
            run_time=0.6,
        )

        # 连加算式逐段显示
        # "4 + 4 + 4 = 12"
        parts = [
            MathTex(r"4", font_size=52, color=C_APPLE),
            MathTex(r"+", font_size=52, color=C_WHITE),
            MathTex(r"4", font_size=52, color=C_APPLE),
            MathTex(r"+", font_size=52, color=C_WHITE),
            MathTex(r"4", font_size=52, color=C_APPLE),
            MathTex(r"=", font_size=52, color=C_WHITE),
            MathTex(r"12", font_size=52, color=C_HIGHLIGHT),
        ]

        addition_eq = VGroup(*parts).arrange(RIGHT, buff=0.18).move_to(UP * 2.7)

        # 先显示前三个4，对应3盘苹果
        self.play(Write(parts[0]), run_time=0.4)
        self.play(
            Flash(self.apple_groups[0], color=C_APPLE, flash_radius=0.5),
            run_time=0.3,
        )
        self.play(Write(parts[1]), Write(parts[2]), run_time=0.4)
        self.play(
            Flash(self.apple_groups[1], color=C_APPLE, flash_radius=0.5),
            run_time=0.3,
        )
        self.play(Write(parts[3]), Write(parts[4]), run_time=0.4)
        self.play(
            Flash(self.apple_groups[2], color=C_APPLE, flash_radius=0.5),
            run_time=0.3,
        )
        self.play(Write(parts[5]), Write(parts[6]), run_time=0.5)
        self.wait(1.0)

        # 保存引用
        self.addition_eq = addition_eq
        self.step_title_3 = step_title

    # ═══════════════════════════════════════════════════════════════════════
    # Scene 4 — 发现规律：相同加数
    # ═══════════════════════════════════════════════════════════════════════
    def scene_4_same_addend(self):
        observe_title = Text(
            "发现规律",
            font="PingFang SC",
            font_size=32,
            color=C_TITLE,
        ).move_to(UP * 3.8)

        self.play(
            ReplacementTransform(self.step_title_3, observe_title),
            run_time=0.5,
        )

        # 高亮三个 4
        for idx in [0, 2, 4]:
            self.play(
                self.addition_eq[idx].animate.set_color(C_HIGHLIGHT).scale(1.3),
                run_time=0.3,
            )
        self.wait(0.4)

        rule_line1 = Text(
            "加数相同：都是 4",
            font="PingFang SC",
            font_size=28,
            color=C_LABEL,
        ).move_to(UP * 1.8)

        rule_line2 = Text(
            "加数的个数：3 个",
            font="PingFang SC",
            font_size=28,
            color=C_LABEL,
        ).move_to(UP * 1.1)

        rule_box = SurroundingRectangle(
            VGroup(rule_line1, rule_line2),
            corner_radius=0.2,
            color=C_BOX,
            buff=0.2,
        )

        self.play(FadeIn(rule_line1, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(rule_line2, shift=RIGHT * 0.3), run_time=0.5)
        self.play(Create(rule_box), run_time=0.4)
        self.wait(1.2)

        # 标注"几个几"
        how_many = Text(
            "3 个 4 相加",
            font="PingFang SC",
            font_size=34,
            color=C_MULT,
            weight=BOLD,
        ).move_to(DOWN * 0.1)

        self.play(Write(how_many), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(observe_title),
            FadeOut(rule_line1),
            FadeOut(rule_line2),
            FadeOut(rule_box),
            FadeOut(how_many),
            run_time=0.6,
        )

        # 恢复颜色
        for idx in [0, 2, 4]:
            self.addition_eq[idx].set_color(C_APPLE).scale(1 / 1.3)

    # ═══════════════════════════════════════════════════════════════════════
    # Scene 5 — 引入乘号与乘法算式
    # ═══════════════════════════════════════════════════════════════════════
    def scene_5_multiplication(self):
        intro_title = Text(
            "引入乘法",
            font="PingFang SC",
            font_size=32,
            color=C_TITLE,
        ).move_to(UP * 3.8)

        self.play(FadeIn(intro_title, shift=DOWN * 0.2), run_time=0.5)

        # 连加算式还在 UP*2.7
        arrow = Arrow(
            start=UP * 2.15,
            end=UP * 1.35,
            color=C_ARROW,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25,
        )

        self.play(GrowArrow(arrow), run_time=0.5)

        # 乘法算式
        mult_eq = MathTex(
            r"4 \times 3 = 12",
            font_size=58,
            color=C_MULT,
        ).move_to(UP * 0.7)

        self.play(Write(mult_eq), run_time=0.9)
        self.wait(0.5)

        # 乘号放大强调
        times_highlight = Text(
            '×  读作 "乘"',
            font="PingFang SC",
            font_size=32,
            color=C_HIGHLIGHT,
        ).move_to(DOWN * 0.3)

        self.play(FadeIn(times_highlight, scale=1.2), run_time=0.6)
        self.wait(1.0)

        # 也可以写成 3×4
        also_text = Text(
            "也可以写成",
            font="PingFang SC",
            font_size=26,
            color=C_LABEL,
        ).move_to(DOWN * 1.3)
        also_eq = MathTex(
            r"3 \times 4 = 12",
            font_size=52,
            color=C_MULT,
        ).move_to(DOWN * 2.1)

        self.play(FadeIn(also_text), run_time=0.4)
        self.play(Write(also_eq), run_time=0.7)
        self.wait(1.0)

        # 说明连加与乘法等价
        equiv_text = Text(
            "连加算式 → 乘法算式",
            font="PingFang SC",
            font_size=24,
            color=C_DIM,
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(equiv_text, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(intro_title),
            FadeOut(arrow),
            FadeOut(times_highlight),
            FadeOut(also_text),
            FadeOut(also_eq),
            FadeOut(equiv_text),
            FadeOut(self.plates_group),
            FadeOut(self.plate_labels),
            run_time=0.7,
        )

        # 将连加 & 主乘法式留在屏幕
        self.mult_eq = mult_eq

    # ═══════════════════════════════════════════════════════════════════════
    # Scene 6 — 各部分名称
    # ═══════════════════════════════════════════════════════════════════════
    def scene_6_parts(self):
        parts_title = Text(
            "各部分名称",
            font="PingFang SC",
            font_size=32,
            color=C_TITLE,
        ).move_to(UP * 5.5)

        self.play(FadeIn(parts_title, shift=DOWN * 0.2), run_time=0.5)

        # 将 addition_eq 移走，只保留主乘法式并移到中央偏上
        self.play(
            self.addition_eq.animate.move_to(UP * 3.5).set_opacity(0.4),
            self.mult_eq.animate.move_to(UP * 2.2),
            run_time=0.7,
        )

        # 乘法算式: 4 × 3 = 12
        # 在公式下方用 Brace + 标签 说明各部分

        # 整个公式边界框用于定位
        eq_center = self.mult_eq.get_center()
        # MathTex "4 \times 3 = 12" 各子式索引
        # [0]='4', [1]='×', [2]='3', [3]='=', [4]='12'

        # 我们手动用位置标注
        eq_left   = self.mult_eq.get_left()
        eq_right  = self.mult_eq.get_right()
        eq_bottom = self.mult_eq.get_bottom()

        # 第一个乘数 "4"
        part4 = self.mult_eq[0][0]
        # 乘号 "×"
        part_times = self.mult_eq[0][1]
        # 第二个乘数 "3"
        part3 = self.mult_eq[0][2]
        # 积 "12"
        part12 = self.mult_eq[0][4]

        # Braces
        brace_4 = Brace(part4, DOWN, color=C_LABEL, buff=0.05)
        label_4 = Text("乘数", font="PingFang SC", font_size=24, color=C_LABEL).next_to(brace_4, DOWN, buff=0.1)

        brace_3 = Brace(part3, DOWN, color=C_LABEL, buff=0.05)
        label_3 = Text("乘数", font="PingFang SC", font_size=24, color=C_LABEL).next_to(brace_3, DOWN, buff=0.1)

        brace_12 = Brace(part12, DOWN, color=C_HIGHLIGHT, buff=0.05)
        label_12 = Text("积", font="PingFang SC", font_size=24, color=C_HIGHLIGHT).next_to(brace_12, DOWN, buff=0.1)

        # 乘号标注
        times_note = Text(
            "乘号",
            font="PingFang SC",
            font_size=22,
            color=C_MULT,
        ).next_to(part_times, UP, buff=0.35)
        times_arrow = Arrow(
            start=times_note.get_bottom() + DOWN * 0.05,
            end=part_times.get_top() + UP * 0.05,
            color=C_MULT,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3,
            buff=0.05,
        )

        self.play(
            FadeIn(brace_4), Write(label_4),
            run_time=0.5,
        )
        self.wait(0.3)
        self.play(
            FadeIn(times_note), GrowArrow(times_arrow),
            run_time=0.5,
        )
        self.wait(0.3)
        self.play(
            FadeIn(brace_3), Write(label_3),
            run_time=0.5,
        )
        self.wait(0.3)
        self.play(
            FadeIn(brace_12), Write(label_12),
            run_time=0.5,
        )
        self.wait(1.2)

        # 公式总结行
        formula_summary = VGroup(
            Text("乘数", font="PingFang SC", font_size=28, color=C_LABEL),
            MathTex(r"\times", font_size=36, color=C_MULT),
            Text("乘数", font="PingFang SC", font_size=28, color=C_LABEL),
            MathTex(r"=", font_size=36, color=C_WHITE),
            Text("积", font="PingFang SC", font_size=28, color=C_HIGHLIGHT),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.3)

        formula_box = SurroundingRectangle(
            formula_summary,
            corner_radius=0.25,
            color=C_MULT,
            buff=0.25,
            stroke_width=2.5,
        )

        self.play(
            Write(formula_summary),
            Create(formula_box),
            run_time=0.9,
        )
        self.wait(2.0)

        self.play(
            FadeOut(parts_title),
            FadeOut(brace_4), FadeOut(label_4),
            FadeOut(brace_3), FadeOut(label_3),
            FadeOut(brace_12), FadeOut(label_12),
            FadeOut(times_note), FadeOut(times_arrow),
            FadeOut(formula_summary), FadeOut(formula_box),
            FadeOut(self.addition_eq),
            run_time=0.7,
        )

    # ═══════════════════════════════════════════════════════════════════════
    # Scene 7 — 总结
    # ═══════════════════════════════════════════════════════════════════════
    def scene_7_summary(self):
        summary_title = Text(
            "本节要点",
            font="PingFang SC",
            font_size=36,
            color=C_TITLE,
            weight=BOLD,
        ).move_to(UP * 5.5)

        self.play(
            FadeIn(summary_title, shift=DOWN * 0.2),
            self.mult_eq.animate.move_to(UP * 4.2).set_color(C_MULT),
            run_time=0.6,
        )

        points = [
            "① 乘法是求几个相同加数之和",
            '② 乘号 × 读作"乘"',
            "③ 乘数 × 乘数 = 积",
            "④ 4 + 4 + 4 = 4 × 3 = 3 × 4 = 12",
        ]

        point_mobs = VGroup()
        for i, pt in enumerate(points):
            mob = Text(
                pt,
                font="PingFang SC",
                font_size=26,
                color=C_LABEL,
            )
            point_mobs.add(mob)

        point_mobs.arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 1.5)

        for mob in point_mobs:
            self.play(FadeIn(mob, shift=RIGHT * 0.4), run_time=0.5)
            self.wait(0.25)

        self.wait(2.0)

        self.play(
            FadeOut(summary_title),
            FadeOut(self.mult_eq),
            FadeOut(point_mobs),
            run_time=0.7,
        )

    # ═══════════════════════════════════════════════════════════════════════
    # Scene 8 — 片尾
    # ═══════════════════════════════════════════════════════════════════════
    def scene_8_outro(self):
        # 作者名称放大
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=38,
            color=C_WHITE,
            weight=BOLD,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=C_DIM,
        ).move_to(UP * 0.6)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=30,
            color=C_HIGHLIGHT,
        ).move_to(DOWN * 0.4)

        # 装饰：小乘号群
        deco = VGroup(*[
            MathTex(r"\times", font_size=28, color=C_MULT)
            .move_to(
                np.array([3.0 * np.cos(i * TAU / 8), 3.0 * np.sin(i * TAU / 8), 0])
                + DOWN * 2.2
            )
            for i in range(8)
        ])

        self.play(
            self.author.animate.move_to(UP * 7.0).set_opacity(0),
            FadeIn(author_big, shift=UP * 0.3),
            run_time=0.7,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        self.play(Write(follow_text), run_time=0.6)
        self.play(
            LaggedStart(*[FadeIn(m, scale=0.5) for m in deco], lag_ratio=0.08),
            run_time=0.8,
        )
        self.play(Rotate(deco, angle=PI, run_time=1.2))
        self.wait(1.0)

        self.play(
            FadeOut(author_big),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(deco),
            run_time=0.8,
        )
