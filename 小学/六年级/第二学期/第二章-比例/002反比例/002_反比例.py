"""
反比例 - Inverse Proportion Animation
六年级第二学期 第二章 比例

内容: 反比例的意义、表达式、图像、判断与应用
目标观众: 小学六年级学生
格式: TikTok竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# Global configuration - TikTok portrait
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class InverseProportionLesson(Scene):
    """
    反比例教学动画

    Scene flow:
    1. Opening hook
    2. Real-life example (area = 24, length x width)
    3. Data table showing inverse proportion
    4. Definition and formula
    5. Graph (hyperbola)
    6. Interactive dot on curve
    7. Judgment practice
    8. Outro
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # Color scheme
        self.COLOR_PRIMARY = "#4fc3f7"
        self.COLOR_SECONDARY = "#81c784"
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_ACCENT = "#ff8a65"
        self.COLOR_FORMULA = "#ce93d8"
        self.COLOR_CURVE = "#4fc3f7"
        self.COLOR_TABLE_HEADER = "#5c6bc0"
        self.COLOR_TABLE_CELL = "#37474f"
        self.FONT = "Noto Sans CJK SC"

        self.scene_1_opening()
        self.scene_2_real_life_example()
        self.scene_3_data_table()
        self.scene_4_definition()
        self.scene_5_graph()
        self.scene_6_judgment()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # Scene 1: Opening Hook
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT, font_size=18, color="#6b7280"
        ).move_to(UP * 7.0)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.author = author

        hook = Text(
            "面积不变，长变长，\n宽会怎样？",
            font=self.FONT, font_size=38, color=self.COLOR_HIGHLIGHT,
            line_spacing=1.4
        ).move_to(UP * 4.5)
        self.play(Write(hook), run_time=1.0)
        self.wait(0.8)

        # Quick rectangle morph to illustrate
        rect1 = Rectangle(width=2, height=3, color=self.COLOR_PRIMARY,
                           fill_opacity=0.3, stroke_width=3).move_to(UP * 1.0)
        label_l1 = MathTex(r"4", color=WHITE, font_size=24).next_to(rect1, DOWN, buff=0.15)
        label_w1 = MathTex(r"6", color=WHITE, font_size=24).next_to(rect1, RIGHT, buff=0.15)

        self.play(FadeIn(rect1), FadeIn(label_l1), FadeIn(label_w1), run_time=0.6)
        self.wait(0.5)

        rect2 = Rectangle(width=4, height=1.5, color=self.COLOR_ACCENT,
                           fill_opacity=0.3, stroke_width=3).move_to(UP * 1.0)
        label_l2 = MathTex(r"8", color=WHITE, font_size=24).next_to(rect2, DOWN, buff=0.15)
        label_w2 = MathTex(r"3", color=WHITE, font_size=24).next_to(rect2, RIGHT, buff=0.15)

        self.play(
            Transform(rect1, rect2),
            Transform(label_l1, label_l2),
            Transform(label_w1, label_w2),
            run_time=1.0
        )
        self.wait(0.6)

        hint = Text(
            "长变大 -> 宽变小！",
            font=self.FONT, font_size=26, color=GRAY_A
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # Cleanup
        self.play(
            FadeOut(hook), FadeOut(rect1), FadeOut(label_l1),
            FadeOut(label_w1), FadeOut(hint),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: Real-life example -- rectangle area = 24
    # ------------------------------------------------------------------
    def scene_2_real_life_example(self):
        title = Text("生活中的反比例", font=self.FONT, font_size=34,
                      color=self.COLOR_PRIMARY).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # Show rectangle with area = 24
        area_text = VGroup(
            Text("长方形面积 = ", font=self.FONT, font_size=24, color=WHITE),
            MathTex(r"24", font_size=32, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.15).move_to(UP * 4.5)
        self.play(FadeIn(area_text), run_time=0.5)

        # Animate several rectangles with area = 24
        combos = [(2, 12), (3, 8), (4, 6), (6, 4), (8, 3), (12, 2)]
        scale_factor = 0.28

        rect_group = VGroup()
        prev_rect = None
        prev_labels = None

        for i, (l, w) in enumerate(combos):
            rw = l * scale_factor
            rh = w * scale_factor
            rect = Rectangle(width=rw, height=rh, color=self.COLOR_PRIMARY,
                              fill_opacity=0.25, stroke_width=2.5).move_to(UP * 1.8)

            l_label = VGroup(
                Text("长=", font=self.FONT, font_size=20, color=GRAY_A),
                MathTex(str(l), font_size=24, color=WHITE)
            ).arrange(RIGHT, buff=0.08).next_to(rect, DOWN, buff=0.2)

            w_label = VGroup(
                Text("宽=", font=self.FONT, font_size=20, color=GRAY_A),
                MathTex(str(w), font_size=24, color=WHITE)
            ).arrange(RIGHT, buff=0.08).next_to(rect, RIGHT, buff=0.2)

            product_label = VGroup(
                MathTex(f"{l}", font_size=22, color=self.COLOR_PRIMARY),
                MathTex(r"\times", font_size=22, color=WHITE),
                MathTex(f"{w}", font_size=22, color=self.COLOR_ACCENT),
                MathTex(r"= 24", font_size=22, color=self.COLOR_HIGHLIGHT)
            ).arrange(RIGHT, buff=0.1).move_to(DOWN * 0.5)

            labels = VGroup(l_label, w_label, product_label)

            if prev_rect is None:
                self.play(FadeIn(rect), FadeIn(labels), run_time=0.6)
            else:
                self.play(
                    Transform(prev_rect, rect),
                    Transform(prev_labels, labels),
                    run_time=0.5
                )

            if prev_rect is None:
                prev_rect = rect
                prev_labels = labels

            self.wait(0.3)

        conclusion = Text(
            "乘积始终 = 24", font=self.FONT, font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.5)

        conclusion2 = Text(
            "长变大，宽变小\n长变小，宽变大", font=self.FONT, font_size=22,
            color=GRAY_A, line_spacing=1.3
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(conclusion2), run_time=0.5)
        self.wait(1.2)

        # Cleanup
        self.play(
            FadeOut(title), FadeOut(area_text),
            FadeOut(prev_rect), FadeOut(prev_labels),
            FadeOut(conclusion), FadeOut(conclusion2),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: Data table
    # ------------------------------------------------------------------
    def scene_3_data_table(self):
        title = Text("数据表格", font=self.FONT, font_size=34,
                      color=self.COLOR_PRIMARY).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        subtitle = Text(
            "速度和时间（路程=120千米）",
            font=self.FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.7)
        self.play(FadeIn(subtitle), run_time=0.4)

        # Table data: speed x time = 120
        speeds = [20, 30, 40, 60, 120]
        times = [6, 4, 3, 2, 1]

        # Build the table manually
        table_top = UP * 3.8
        col_width = 1.3
        row_height = 0.7
        n_cols = len(speeds) + 1  # header col + data cols
        n_rows = 3  # header + speed + time

        # Header row
        headers = [
            Text("", font=self.FONT, font_size=18),
            *[MathTex(str(i + 1), font_size=20, color=GRAY_A) for i in range(len(speeds))]
        ]

        row_labels = [
            VGroup(
                Text("速度", font=self.FONT, font_size=18, color=WHITE),
                Text("(km/h)", font=self.FONT, font_size=14, color=GRAY_B)
            ).arrange(DOWN, buff=0.05),
            VGroup(
                Text("时间", font=self.FONT, font_size=18, color=WHITE),
                Text("(h)", font=self.FONT, font_size=14, color=GRAY_B)
            ).arrange(DOWN, buff=0.05),
        ]

        all_cells = VGroup()
        all_values = VGroup()

        for r in range(n_rows):
            for c in range(n_cols):
                x = -3.2 + c * col_width
                y_val = table_top[1] - r * row_height

                if r == 0:
                    bg_color = self.COLOR_TABLE_HEADER
                    opacity = 0.6
                else:
                    bg_color = self.COLOR_TABLE_CELL
                    opacity = 0.3 if r % 2 == 1 else 0.15

                cell = RoundedRectangle(
                    width=col_width - 0.05, height=row_height - 0.05,
                    corner_radius=0.08,
                    fill_color=bg_color, fill_opacity=opacity,
                    stroke_color=GRAY_B, stroke_width=1
                ).move_to(np.array([x, y_val, 0]))
                all_cells.add(cell)

        self.play(FadeIn(all_cells), run_time=0.5)

        # Fill header row
        header_texts = VGroup()
        for c in range(n_cols):
            x = -3.2 + c * col_width
            y_val = table_top[1]
            if c == 0:
                t = Text("组别", font=self.FONT, font_size=16, color=WHITE)
            else:
                t = MathTex(str(c), font_size=18, color=WHITE)
            t.move_to(np.array([x, y_val, 0]))
            header_texts.add(t)
        self.play(FadeIn(header_texts), run_time=0.3)

        # Fill row labels
        for r_idx, label in enumerate(row_labels):
            x = -3.2
            y_val = table_top[1] - (r_idx + 1) * row_height
            label.move_to(np.array([x, y_val, 0]))
        self.play(FadeIn(row_labels[0]), FadeIn(row_labels[1]), run_time=0.3)

        # Fill data cells one by one
        speed_texts = VGroup()
        time_texts = VGroup()
        for idx in range(len(speeds)):
            c = idx + 1
            x = -3.2 + c * col_width

            s_text = MathTex(str(speeds[idx]), font_size=22, color=self.COLOR_PRIMARY)
            s_text.move_to(np.array([x, table_top[1] - row_height, 0]))
            speed_texts.add(s_text)

            t_text = MathTex(str(times[idx]), font_size=22, color=self.COLOR_ACCENT)
            t_text.move_to(np.array([x, table_top[1] - 2 * row_height, 0]))
            time_texts.add(t_text)

        self.play(
            *[FadeIn(s, shift=DOWN * 0.1) for s in speed_texts],
            run_time=0.6
        )
        self.play(
            *[FadeIn(t, shift=DOWN * 0.1) for t in time_texts],
            run_time=0.6
        )
        self.wait(0.5)

        # Show products
        product_title = Text(
            "每组的乘积：", font=self.FONT, font_size=22, color=WHITE
        ).move_to(UP * 0.8)
        self.play(FadeIn(product_title), run_time=0.3)

        product_texts = VGroup()
        for idx in range(len(speeds)):
            pt = VGroup(
                MathTex(f"{speeds[idx]}", font_size=20, color=self.COLOR_PRIMARY),
                MathTex(r"\times", font_size=20, color=WHITE),
                MathTex(f"{times[idx]}", font_size=20, color=self.COLOR_ACCENT),
                MathTex(r"= 120", font_size=20, color=self.COLOR_HIGHLIGHT),
            ).arrange(RIGHT, buff=0.08)
            product_texts.add(pt)

        product_texts.arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(DOWN * 0.8)

        for pt in product_texts:
            self.play(FadeIn(pt), run_time=0.3)

        self.wait(0.5)

        # Highlight: product is constant
        box = SurroundingRectangle(
            product_texts, color=self.COLOR_HIGHLIGHT, buff=0.2,
            corner_radius=0.1, stroke_width=2
        )
        box_label = Text(
            "乘积一定！", font=self.FONT, font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).next_to(box, DOWN, buff=0.3)
        self.play(Create(box), FadeIn(box_label), run_time=0.6)
        self.wait(1.5)

        # Cleanup
        self.play(
            FadeOut(title), FadeOut(subtitle), FadeOut(all_cells),
            FadeOut(header_texts), FadeOut(row_labels[0]), FadeOut(row_labels[1]),
            FadeOut(speed_texts), FadeOut(time_texts),
            FadeOut(product_title), FadeOut(product_texts),
            FadeOut(box), FadeOut(box_label),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: Definition and Formula
    # ------------------------------------------------------------------
    def scene_4_definition(self):
        title = Text("反比例的定义", font=self.FONT, font_size=34,
                      color=self.COLOR_PRIMARY).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # Definition text
        def_lines = VGroup(
            Text("两种相关联的量，", font=self.FONT, font_size=22, color=WHITE),
            Text("一种量变化，另一种量也随着变化，", font=self.FONT, font_size=22, color=WHITE),
            Text("如果这两种量中", font=self.FONT, font_size=22, color=WHITE),
            Text("相对应的两个数的乘积一定，", font=self.FONT, font_size=24,
                 color=self.COLOR_HIGHLIGHT),
            Text("这两种量就叫做", font=self.FONT, font_size=22, color=WHITE),
            Text("成反比例的量。", font=self.FONT, font_size=26, color=self.COLOR_ACCENT),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(UP * 3.0)

        for line in def_lines:
            self.play(FadeIn(line, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(1.0)

        # Formula
        formula_box = RoundedRectangle(
            width=7.0, height=2.8, corner_radius=0.2,
            fill_color="#1e3a5f", fill_opacity=0.5,
            stroke_color=self.COLOR_FORMULA, stroke_width=2
        ).move_to(DOWN * 1.0)

        formula_title = Text(
            "数学表达式", font=self.FONT, font_size=22, color=self.COLOR_FORMULA
        ).move_to(formula_box.get_top() + DOWN * 0.35)

        formula1 = MathTex(
            r"x \times y = k",
            font_size=36, color=WHITE
        ).move_to(formula_box.get_center() + UP * 0.15)

        formula1_note = VGroup(
            MathTex(r"(k", font_size=22, color=GRAY_A),
            Text("为常数，", font=self.FONT, font_size=18, color=GRAY_A),
            MathTex(r"k \neq 0)", font_size=22, color=GRAY_A),
        ).arrange(RIGHT, buff=0.08).next_to(formula1, DOWN, buff=0.15)

        or_text = Text("或", font=self.FONT, font_size=20, color=GRAY_B
                        ).next_to(formula1_note, DOWN, buff=0.15)

        formula2 = MathTex(
            r"y = \frac{k}{x}",
            font_size=36, color=WHITE
        ).next_to(or_text, DOWN, buff=0.15)

        self.play(FadeIn(formula_box), run_time=0.4)
        self.play(Write(formula_title), run_time=0.3)
        self.play(Write(formula1), run_time=0.6)
        self.play(FadeIn(formula1_note), run_time=0.3)
        self.play(FadeIn(or_text), run_time=0.2)
        self.play(Write(formula2), run_time=0.6)
        self.wait(1.0)

        # Key point
        key_point = VGroup(
            Text("关键词：", font=self.FONT, font_size=22, color=WHITE),
            Text("乘积一定", font=self.FONT, font_size=28, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 4.0)

        vs_text = VGroup(
            Text("对比正比例：", font=self.FONT, font_size=20, color=GRAY_A),
            Text("比值一定", font=self.FONT, font_size=22, color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 5.0)

        self.play(FadeIn(key_point, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(vs_text), run_time=0.4)
        self.wait(1.5)

        # Cleanup
        self.play(
            FadeOut(title), FadeOut(def_lines), FadeOut(formula_box),
            FadeOut(formula_title), FadeOut(formula1), FadeOut(formula1_note),
            FadeOut(or_text), FadeOut(formula2),
            FadeOut(key_point), FadeOut(vs_text),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: Graph (hyperbola)
    # ------------------------------------------------------------------
    def scene_5_graph(self):
        title = Text("反比例的图像", font=self.FONT, font_size=34,
                      color=self.COLOR_PRIMARY).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        subtitle = VGroup(
            MathTex(r"y = \frac{24}{x}", font_size=28, color=self.COLOR_FORMULA),
            Text("  的图像", font=self.FONT, font_size=22, color=GRAY_A)
        ).arrange(RIGHT, buff=0.1).move_to(UP * 4.7)
        self.play(FadeIn(subtitle), run_time=0.4)

        # Create axes
        axes = Axes(
            x_range=[0, 14, 2],
            y_range=[0, 14, 2],
            x_length=6.5,
            y_length=6.5,
            axis_config={
                "include_numbers": True,
                "font_size": 18,
                "color": GRAY_B,
                "include_tip": True,
                "tip_length": 0.2,
            },
        ).move_to(UP * 0.5)

        x_label = MathTex(r"x", font_size=22, color=GRAY_A).next_to(
            axes.x_axis.get_end(), RIGHT, buff=0.15)
        y_label = MathTex(r"y", font_size=22, color=GRAY_A).next_to(
            axes.y_axis.get_end(), UP, buff=0.15)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=1.0)

        # Plot the curve y = 24/x for x in [1.8, 13]
        k_val = 24
        curve = axes.plot(
            lambda x: k_val / x,
            x_range=[1.85, 13, 0.05],
            color=self.COLOR_CURVE,
            stroke_width=3
        )
        self.play(Create(curve), run_time=1.5)

        # Label the curve
        curve_label = Text(
            "光滑曲线（双曲线）", font=self.FONT, font_size=18,
            color=self.COLOR_CURVE
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(curve_label), run_time=0.4)
        self.wait(0.5)

        # Plot specific points
        data_points = [(2, 12), (3, 8), (4, 6), (6, 4), (8, 3), (12, 2)]
        dots = VGroup()
        dot_labels = VGroup()

        for (px, py) in data_points:
            pos = axes.c2p(px, py)
            d = Dot(pos, radius=0.08, color=self.COLOR_ACCENT)
            dots.add(d)
            lbl = MathTex(
                f"({px},{py})", font_size=16, color=WHITE
            ).next_to(d, UR, buff=0.1)
            dot_labels.add(lbl)

        self.play(
            *[FadeIn(d, scale=0.5) for d in dots],
            run_time=0.6
        )
        self.play(
            *[FadeIn(l) for l in dot_labels],
            run_time=0.5
        )
        self.wait(0.8)

        # Moving dot demonstration
        self.play(FadeOut(dot_labels), run_time=0.3)

        tracker = ValueTracker(2.0)
        moving_dot = always_redraw(
            lambda: Dot(
                axes.c2p(tracker.get_value(), k_val / tracker.get_value()),
                radius=0.1, color=YELLOW
            )
        )
        moving_label = always_redraw(
            lambda: MathTex(
                f"({tracker.get_value():.1f},\\,{k_val / tracker.get_value():.1f})",
                font_size=18, color=YELLOW
            ).next_to(
                axes.c2p(tracker.get_value(), k_val / tracker.get_value()),
                UR, buff=0.15
            )
        )

        # Dashed lines to axes
        h_dash = always_redraw(
            lambda: DashedLine(
                axes.c2p(0, k_val / tracker.get_value()),
                axes.c2p(tracker.get_value(), k_val / tracker.get_value()),
                color=YELLOW, stroke_width=1, dash_length=0.08
            )
        )
        v_dash = always_redraw(
            lambda: DashedLine(
                axes.c2p(tracker.get_value(), 0),
                axes.c2p(tracker.get_value(), k_val / tracker.get_value()),
                color=YELLOW, stroke_width=1, dash_length=0.08
            )
        )

        self.play(
            FadeIn(moving_dot), FadeIn(moving_label),
            FadeIn(h_dash), FadeIn(v_dash),
            run_time=0.5
        )

        explain = Text(
            "x 增大 -> y 减小", font=self.FONT, font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.2)
        self.play(FadeIn(explain), run_time=0.3)

        self.play(tracker.animate.set_value(12.0), run_time=3.0, rate_func=smooth)
        self.wait(0.3)

        explain2 = Text(
            "x 减小 -> y 增大", font=self.FONT, font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.2)
        self.play(Transform(explain, explain2), run_time=0.3)

        self.play(tracker.animate.set_value(2.0), run_time=3.0, rate_func=smooth)
        self.wait(0.5)

        product_note = VGroup(
            Text("始终满足: ", font=self.FONT, font_size=20, color=WHITE),
            MathTex(r"x \times y = 24", font_size=26, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 5.5)
        self.play(FadeIn(product_note), run_time=0.4)
        self.wait(1.5)

        # Cleanup
        self.play(
            FadeOut(title), FadeOut(subtitle), FadeOut(axes),
            FadeOut(x_label), FadeOut(y_label), FadeOut(curve),
            FadeOut(curve_label), FadeOut(dots),
            FadeOut(moving_dot), FadeOut(moving_label),
            FadeOut(h_dash), FadeOut(v_dash),
            FadeOut(explain), FadeOut(product_note),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: Judgment Practice
    # ------------------------------------------------------------------
    def scene_6_judgment(self):
        title = Text("判断练习", font=self.FONT, font_size=34,
                      color=self.COLOR_PRIMARY).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        hint = Text(
            "哪些是反比例关系？", font=self.FONT, font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.7)
        self.play(FadeIn(hint), run_time=0.3)

        # Question items
        questions = [
            ("1. 总价一定，单价和数量", True),
            ("2. 长方形面积一定，长和宽", True),
            ("3. 每天看页数一定，\n   总页数和天数", False),
            ("4. 全班人数一定，\n   每组人数和组数", True),
        ]

        q_group = VGroup()
        y_start = 3.5

        for idx, (q_text, is_inverse) in enumerate(questions):
            q_label = Text(
                q_text, font=self.FONT, font_size=20, color=WHITE,
                line_spacing=1.2
            ).move_to(UP * (y_start - idx * 2.0) + LEFT * 0.5)
            q_label.align_to(LEFT * 3.5, LEFT)
            q_group.add(q_label)

        # Show questions one by one
        for idx, q in enumerate(q_group):
            self.play(FadeIn(q, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.8)

            # Show answer
            is_inverse = questions[idx][1]
            if is_inverse:
                mark = MathTex(r"\checkmark", font_size=30, color=GREEN)
                reason = Text(
                    "乘积一定", font=self.FONT, font_size=16,
                    color=self.COLOR_SECONDARY
                )
            else:
                mark = MathTex(r"\times", font_size=30, color=RED)
                reason = Text(
                    "比值一定（正比例）", font=self.FONT, font_size=16,
                    color=RED_B
                )

            mark.next_to(q, RIGHT, buff=0.3)
            reason.next_to(mark, RIGHT, buff=0.15)

            self.play(FadeIn(mark, scale=1.5), FadeIn(reason), run_time=0.4)
            self.wait(0.5)

        # Summary
        summary_box = RoundedRectangle(
            width=7.5, height=1.4, corner_radius=0.15,
            fill_color="#1e3a5f", fill_opacity=0.4,
            stroke_color=self.COLOR_HIGHLIGHT, stroke_width=2
        ).move_to(DOWN * 5.5)

        summary_text = VGroup(
            Text("判断方法：看两个量的", font=self.FONT, font_size=20, color=WHITE),
            Text("乘积", font=self.FONT, font_size=24, color=self.COLOR_HIGHLIGHT),
            Text("是否一定", font=self.FONT, font_size=20, color=WHITE),
        ).arrange(RIGHT, buff=0.08).move_to(summary_box.get_center())

        self.play(FadeIn(summary_box), FadeIn(summary_text), run_time=0.5)
        self.wait(2.0)

        # Cleanup
        self.play(
            FadeOut(title), FadeOut(hint), FadeOut(q_group),
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 7: Outro
    # ------------------------------------------------------------------
    def scene_7_outro(self):
        # Summary card
        summary_title = Text(
            "反比例 - 知识总结", font=self.FONT, font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.0)
        self.play(Write(summary_title), run_time=0.5)

        points = VGroup(
            VGroup(
                Text("1. ", font=self.FONT, font_size=20, color=self.COLOR_ACCENT),
                Text("乘积一定 -> 反比例", font=self.FONT, font_size=22, color=WHITE),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("2. ", font=self.FONT, font_size=20, color=self.COLOR_ACCENT),
                Text("公式: ", font=self.FONT, font_size=22, color=WHITE),
                MathTex(r"x \times y = k", font_size=26, color=self.COLOR_FORMULA),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("3. ", font=self.FONT, font_size=20, color=self.COLOR_ACCENT),
                Text("图像: 光滑曲线（双曲线）", font=self.FONT, font_size=22, color=WHITE),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("4. ", font=self.FONT, font_size=20, color=self.COLOR_ACCENT),
                Text("一个量增大，另一个量减小", font=self.FONT, font_size=22, color=WHITE),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 2.5)

        for p in points:
            self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.3)

        self.wait(1.0)

        # Author info
        self.play(FadeOut(summary_title), FadeOut(points), run_time=0.4)

        author_name = Text(
            "上海初高中数学直通车", font=self.FONT, font_size=38, color=WHITE
        ).move_to(UP * 1.5)
        author_id = Text(
            "@emptyandcalm", font=self.FONT, font_size=28, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(
            FadeOut(self.author),
            FadeIn(author_name, shift=DOWN * 0.3),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = Text(
            "关注我，学更多数学技巧！", font=self.FONT, font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(author_name), FadeOut(author_id), FadeOut(follow),
            run_time=0.8
        )
