"""
分数的初步认识 - Fractions Basic Introduction
三年级数学 · 第六章 · 整理与提高

内容: 分数的引入、几分之一与几分之几、分子分母含义、大小比较
目标观众: 三年级小学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class FractionBasicLesson(Scene):
    """
    分数的初步认识教学动画

    场景顺序:
    1. 开场钩子 - 分蛋糕问题
    2. 认识二分之一 (1/2)
    3. 分子分母的含义
    4. 认识几分之一 (1/4, 1/3)
    5. 认识几分之几 (2/3)
    6. 同分母分数大小比较
    7. 同分子分数大小比较
    8. 片尾总结
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_MAIN = "#f0c27f"       # 暖黄 - 主色
        self.COLOR_ACCENT = "#e74c3c"     # 红色 - 强调
        self.COLOR_BLUE = "#3498db"       # 蓝色
        self.COLOR_GREEN = "#2ecc71"      # 绿色
        self.COLOR_PURPLE = "#9b59b6"     # 紫色
        self.COLOR_ORANGE = "#f39c12"     # 橙色
        self.COLOR_FILL_DARK = "#16213e"  # 深蓝填充

        # 作者信息 (顶部常驻)
        self.author_label = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.add(self.author_label)

        # 执行各场景
        self.scene_01_opening()
        self.scene_02_half()
        self.scene_03_numerator_denominator()
        self.scene_04_unit_fractions()
        self.scene_05_non_unit_fraction()
        self.scene_06_compare_same_denominator()
        self.scene_07_compare_same_numerator()
        self.scene_08_outro()

    # ───────────────────────────────────────────────
    # 辅助：画扇形（蛋糕切片）
    # ───────────────────────────────────────────────

    def make_sector(self, center, radius, start_angle, angle,
                    stroke_color, fill_color, fill_opacity=0.9):
        """画扇形，用于分割蛋糕"""
        sector = Sector(
            radius=radius,
            start_angle=start_angle,
            angle=angle,
            color=stroke_color,
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_width=2
        )
        sector.move_to(center)
        return sector

    def make_fraction_math(self, latex_str, font_size=52, color=WHITE):
        """用 MathTex 创建纯数字分数"""
        return MathTex(latex_str, font_size=font_size, color=color)

    def make_rect_bar(self, center, total_width, bar_height,
                      num_parts, filled_parts,
                      fill_color, bg_color="#3a2a1a"):
        """
        创建矩形进度条，表示分数。
        返回 VGroup(bg_rect, filled_rect, dividers)
        """
        bg = Rectangle(width=total_width, height=bar_height,
                       color=WHITE, stroke_width=2,
                       fill_color=bg_color, fill_opacity=0.6)
        bg.move_to(center)

        seg_w = total_width / num_parts
        filled_w = seg_w * filled_parts
        filled = Rectangle(
            width=filled_w, height=bar_height,
            fill_color=fill_color, fill_opacity=0.92,
            stroke_width=0
        )
        filled.move_to(center + LEFT * (total_width / 2) + RIGHT * (filled_w / 2))

        divs = VGroup()
        for i in range(1, num_parts):
            dl = Line(
                center + LEFT * (total_width / 2) + RIGHT * i * seg_w + UP * (bar_height / 2),
                center + LEFT * (total_width / 2) + RIGHT * i * seg_w + DOWN * (bar_height / 2),
                color=WHITE, stroke_width=1.5
            )
            divs.add(dl)

        return VGroup(bg, filled, divs)

    # ───────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ───────────────────────────────────────────────
    def scene_01_opening(self):
        # 标题
        title = Text("分数的初步认识", font="Noto Sans CJK SC",
                     font_size=44, color=self.COLOR_MAIN)
        title.move_to(UP * 5.8)

        question = Text("分蛋糕，怎么表示一半？",
                        font="Noto Sans CJK SC", font_size=30,
                        color=WHITE)
        question.move_to(UP * 4.8)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(0.4)

        # 画一个大蛋糕（圆形）
        cake_center = UP * 2.5
        cake = Circle(radius=1.5, color=self.COLOR_MAIN, stroke_width=4,
                      fill_color="#8d5524", fill_opacity=0.85)
        cake.move_to(cake_center)

        self.play(Create(cake), run_time=0.7)

        # 问号
        q_mark = Text("?", font="Noto Sans CJK SC",
                       font_size=72, color=self.COLOR_MAIN)
        q_mark.move_to(cake_center)
        self.play(FadeIn(q_mark, scale=0.5), run_time=0.4)
        self.wait(0.4)

        # 一刀切开（垂直线）
        cut_line = Line(cake_center + UP * 1.5,
                        cake_center + DOWN * 1.5,
                        color=WHITE, stroke_width=3)
        self.play(FadeOut(q_mark), run_time=0.2)
        self.play(Create(cut_line), run_time=0.6)

        # 替换为两个扇形
        left_half = self.make_sector(cake_center, 1.5,
                                     PI / 2, PI,
                                     WHITE, "#a0522d")
        right_half = self.make_sector(cake_center, 1.5,
                                      PI / 2 + PI, PI,
                                      WHITE, "#c68642")

        self.play(
            FadeOut(cake), FadeOut(cut_line),
            FadeIn(left_half), FadeIn(right_half),
            run_time=0.4
        )

        # 分开两半
        self.play(
            left_half.animate.shift(LEFT * 1.0),
            right_half.animate.shift(RIGHT * 1.0),
            run_time=0.8
        )

        label_left = Text("一半", font="Noto Sans CJK SC",
                          font_size=28, color=YELLOW)
        label_left.next_to(left_half, DOWN, buff=0.2)
        label_right = Text("一半", font="Noto Sans CJK SC",
                           font_size=28, color=YELLOW)
        label_right.next_to(right_half, DOWN, buff=0.2)

        self.play(FadeIn(label_left), FadeIn(label_right), run_time=0.5)
        self.wait(0.3)

        hint = Text("用什么数字来表示这一半？",
                    font="Noto Sans CJK SC", font_size=26, color=GRAY_A)
        hint.move_to(DOWN * 1.5)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清场
        self.play(
            FadeOut(title), FadeOut(question),
            FadeOut(left_half), FadeOut(right_half),
            FadeOut(label_left), FadeOut(label_right),
            FadeOut(hint),
            run_time=0.5
        )

    # ───────────────────────────────────────────────
    # Scene 2: 认识 1/2
    # ───────────────────────────────────────────────
    def scene_02_half(self):
        title = Text("认识二分之一", font="Noto Sans CJK SC",
                     font_size=40, color=self.COLOR_MAIN)
        title.move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 蛋糕
        cake_center = UP * 3.5
        cake = Circle(radius=1.3, color=WHITE, stroke_width=3,
                      fill_color="#8d5524", fill_opacity=0.85)
        cake.move_to(cake_center)
        self.play(Create(cake), run_time=0.6)

        # 切成两等份并显示
        line_v = Line(cake_center + UP * 1.3,
                      cake_center + DOWN * 1.3,
                      color=WHITE, stroke_width=3)
        self.play(Create(line_v), run_time=0.5)

        equal_label = Text("平均分成2份",
                           font="Noto Sans CJK SC", font_size=26, color=GRAY_A)
        equal_label.move_to(UP * 1.9)
        self.play(FadeIn(equal_label), run_time=0.4)
        self.wait(0.3)

        # 高亮左半
        left_sector = self.make_sector(cake_center, 1.3,
                                       PI / 2, PI,
                                       YELLOW, "#f0a500", fill_opacity=0.95)
        right_sector = self.make_sector(cake_center, 1.3,
                                        PI / 2 + PI, PI,
                                        WHITE, "#8d5524", fill_opacity=0.7)

        self.play(
            FadeOut(cake), FadeOut(line_v),
            FadeIn(left_sector), FadeIn(right_sector),
            run_time=0.5
        )

        one_label = Text("取其中 1 份",
                         font="Noto Sans CJK SC", font_size=26,
                         color=YELLOW)
        one_label.move_to(UP * 1.3)
        self.play(FadeIn(one_label), run_time=0.4)
        self.wait(0.3)

        # 显示分数 1/2
        frac_half = self.make_fraction_math(r"\frac{1}{2}",
                                             font_size=88,
                                             color=self.COLOR_MAIN)
        frac_half.move_to(DOWN * 0.2)
        self.play(Write(frac_half), run_time=1.0)

        # 读法 & 写法
        read_label = Text("读作：二分之一", font="Noto Sans CJK SC",
                          font_size=28, color=WHITE)
        read_label.move_to(DOWN * 1.8)
        self.play(FadeIn(read_label, shift=UP * 0.2), run_time=0.5)

        meaning = Text("表示把蛋糕平均分成2份，取其中1份",
                       font="Noto Sans CJK SC", font_size=22, color=GRAY_A)
        meaning.move_to(DOWN * 2.6)
        self.play(FadeIn(meaning), run_time=0.4)
        self.wait(1.8)

        # 清场
        self.play(
            FadeOut(title), FadeOut(left_sector), FadeOut(right_sector),
            FadeOut(equal_label), FadeOut(one_label),
            FadeOut(frac_half), FadeOut(read_label), FadeOut(meaning),
            run_time=0.5
        )

    # ───────────────────────────────────────────────
    # Scene 3: 分子与分母的含义
    # ───────────────────────────────────────────────
    def scene_03_numerator_denominator(self):
        title = Text("分子和分母", font="Noto Sans CJK SC",
                     font_size=42, color=self.COLOR_MAIN)
        title.move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 大分数
        frac = self.make_fraction_math(r"\frac{1}{2}", font_size=110,
                                        color=WHITE)
        frac.move_to(UP * 3.8)
        self.play(Write(frac), run_time=0.8)
        self.wait(0.3)

        # 分数线标注（向右引出）
        line_tip = frac.get_center() + DOWN * 0.0
        line_label = Text("分数线", font="Noto Sans CJK SC",
                          font_size=28, color=YELLOW)
        line_label.move_to(UP * 3.8 + RIGHT * 2.8)
        line_arrow = Arrow(
            start=line_label.get_left() + LEFT * 0.05,
            end=frac.get_center() + RIGHT * 0.65,
            color=YELLOW, buff=0.1, stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        self.play(FadeIn(line_label), GrowArrow(line_arrow), run_time=0.6)
        self.wait(0.2)

        # 分母标注（向下引）
        den_label = Text("分母：平均分成几份",
                         font="Noto Sans CJK SC", font_size=25,
                         color=self.COLOR_BLUE)
        den_label.move_to(UP * 2.3 + RIGHT * 1.8)
        den_arrow = Arrow(
            start=den_label.get_left() + LEFT * 0.05,
            end=frac.get_bottom() + DOWN * 0.05 + RIGHT * 0.0,
            color=self.COLOR_BLUE, buff=0.1, stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        self.play(FadeIn(den_label), GrowArrow(den_arrow), run_time=0.6)
        self.wait(0.2)

        # 分子标注（向上引）
        num_label = Text("分子：取了几份",
                         font="Noto Sans CJK SC", font_size=25,
                         color=self.COLOR_ACCENT)
        num_label.move_to(UP * 5.2 + RIGHT * 1.8)
        num_arrow = Arrow(
            start=num_label.get_left() + LEFT * 0.05,
            end=frac.get_top() + UP * 0.05 + RIGHT * 0.0,
            color=self.COLOR_ACCENT, buff=0.1, stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        self.play(FadeIn(num_label), GrowArrow(num_arrow), run_time=0.6)
        self.wait(0.5)

        # 口诀框
        rule = Text("分母在下，分子在上\n中间一横是分数线",
                    font="Noto Sans CJK SC", font_size=24,
                    color=YELLOW, line_spacing=1.4)
        rule_box = SurroundingRectangle(rule, color=YELLOW,
                                        buff=0.3, corner_radius=0)
        rule.move_to(DOWN * 0.5)
        rule_box.move_to(DOWN * 0.5)
        self.play(Create(rule_box), FadeIn(rule, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        # 清场
        self.play(
            FadeOut(title), FadeOut(frac),
            FadeOut(line_label), FadeOut(line_arrow),
            FadeOut(den_label), FadeOut(den_arrow),
            FadeOut(num_label), FadeOut(num_arrow),
            FadeOut(rule_box), FadeOut(rule),
            run_time=0.5
        )

    # ───────────────────────────────────────────────
    # Scene 4: 认识几分之一 (1/4, 1/3)
    # ───────────────────────────────────────────────
    def scene_04_unit_fractions(self):
        title = Text("几分之一", font="Noto Sans CJK SC",
                     font_size=42, color=self.COLOR_MAIN)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # ---- 四分之一 ----
        subtitle_4 = Text("平均分成4份，取1份  →  四分之一",
                          font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        subtitle_4.move_to(UP * 5.4)
        self.play(FadeIn(subtitle_4), run_time=0.4)

        cake_c = UP * 3.5
        colors_4 = ["#a0522d", "#c68642", "#a0522d", "#c68642"]
        sectors_4 = VGroup()
        for i in range(4):
            s = self.make_sector(cake_c, 1.2,
                                 PI / 2 + i * PI / 2, PI / 2,
                                 WHITE, colors_4[i], fill_opacity=0.8)
            sectors_4.add(s)

        hl_4 = self.make_sector(cake_c, 1.2,
                                PI / 2, PI / 2,
                                YELLOW, "#f0c27f", fill_opacity=0.98)

        self.play(FadeIn(sectors_4), run_time=0.5)
        self.play(FadeIn(hl_4), run_time=0.4)

        frac_q = self.make_fraction_math(r"\frac{1}{4}",
                                          font_size=68,
                                          color=self.COLOR_ORANGE)
        frac_q.move_to(UP * 1.8)
        self.play(Write(frac_q), run_time=0.7)

        read_4 = Text("读作：四分之一", font="Noto Sans CJK SC",
                      font_size=26, color=WHITE)
        read_4.move_to(UP * 1.0)
        self.play(FadeIn(read_4), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(subtitle_4), FadeOut(sectors_4), FadeOut(hl_4),
            FadeOut(frac_q), FadeOut(read_4),
            run_time=0.4
        )

        # ---- 三分之一 ----
        subtitle_3 = Text("平均分成3份，取1份  →  三分之一",
                          font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        subtitle_3.move_to(UP * 5.4)
        self.play(FadeIn(subtitle_3), run_time=0.4)

        colors_3 = ["#8d5524", "#a0522d", "#c68642"]
        sectors_3 = VGroup()
        for i in range(3):
            s = self.make_sector(cake_c, 1.2,
                                 PI / 2 + i * 2 * PI / 3, 2 * PI / 3,
                                 WHITE, colors_3[i], fill_opacity=0.8)
            sectors_3.add(s)

        hl_3 = self.make_sector(cake_c, 1.2,
                                PI / 2, 2 * PI / 3,
                                YELLOW, "#f0c27f", fill_opacity=0.98)

        self.play(FadeIn(sectors_3), run_time=0.5)
        self.play(FadeIn(hl_3), run_time=0.4)

        frac_t = self.make_fraction_math(r"\frac{1}{3}",
                                          font_size=68,
                                          color=self.COLOR_GREEN)
        frac_t.move_to(UP * 1.8)
        self.play(Write(frac_t), run_time=0.7)

        read_3 = Text("读作：三分之一", font="Noto Sans CJK SC",
                      font_size=26, color=WHITE)
        read_3.move_to(UP * 1.0)
        self.play(FadeIn(read_3), run_time=0.4)
        self.wait(0.5)

        # 规律提示
        rule = Text("分成几份 → 分母写几",
                    font="Noto Sans CJK SC", font_size=26,
                    color=self.COLOR_GREEN)
        rule_box = SurroundingRectangle(rule, color=self.COLOR_GREEN,
                                        buff=0.2, corner_radius=0)
        rule.move_to(DOWN * 0.2)
        rule_box.move_to(DOWN * 0.2)
        self.play(Create(rule_box), FadeIn(rule), run_time=0.5)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(title), FadeOut(subtitle_3),
            FadeOut(sectors_3), FadeOut(hl_3),
            FadeOut(frac_t), FadeOut(read_3),
            FadeOut(rule_box), FadeOut(rule),
            run_time=0.5
        )

    # ───────────────────────────────────────────────
    # Scene 5: 认识几分之几 (2/3)
    # ───────────────────────────────────────────────
    def scene_05_non_unit_fraction(self):
        title = Text("几分之几", font="Noto Sans CJK SC",
                     font_size=42, color=self.COLOR_MAIN)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        subtitle = Text("平均分成3份，取其中2份",
                        font="Noto Sans CJK SC", font_size=26, color=GRAY_A)
        subtitle.move_to(UP * 5.4)
        self.play(FadeIn(subtitle), run_time=0.4)

        cake_c = UP * 3.5
        colors_base = ["#8d5524", "#a0522d", "#c68642"]
        sectors_base = VGroup()
        for i in range(3):
            s = self.make_sector(cake_c, 1.2,
                                 PI / 2 + i * 2 * PI / 3, 2 * PI / 3,
                                 WHITE, colors_base[i], fill_opacity=0.6)
            sectors_base.add(s)

        self.play(FadeIn(sectors_base), run_time=0.6)

        # 逐一高亮两份
        hl1 = self.make_sector(cake_c, 1.2,
                               PI / 2, 2 * PI / 3,
                               YELLOW, "#f0c27f", fill_opacity=0.98)
        hl2 = self.make_sector(cake_c, 1.2,
                               PI / 2 + 2 * PI / 3, 2 * PI / 3,
                               YELLOW, "#e8a838", fill_opacity=0.98)
        self.play(FadeIn(hl1), run_time=0.35)
        self.play(FadeIn(hl2), run_time=0.35)

        # 份数标签
        angles_label = [PI / 2 + PI / 3, PI / 2 + PI, PI / 2 + 5 * PI / 3]
        labels_text = ["1", "2", "3"]
        label_colors = [WHITE, WHITE, GRAY_B]
        lbl_group = VGroup()
        for ang, txt, col in zip(angles_label, labels_text, label_colors):
            lbl = Text(txt, font="Noto Sans CJK SC", font_size=30, color=col)
            lbl.move_to(cake_c + 0.72 * np.array([np.cos(ang), np.sin(ang), 0]))
            lbl_group.add(lbl)
        self.play(FadeIn(lbl_group), run_time=0.4)

        # 分数
        frac_23 = self.make_fraction_math(r"\frac{2}{3}",
                                           font_size=84,
                                           color=self.COLOR_PURPLE)
        frac_23.move_to(UP * 1.7)
        self.play(Write(frac_23), run_time=0.8)

        read_label = Text("读作：三分之二", font="Noto Sans CJK SC",
                          font_size=28, color=WHITE)
        read_label.move_to(UP * 0.7)
        self.play(FadeIn(read_label, shift=UP * 0.2), run_time=0.5)

        # 解读
        explain_num = Text("分子 2 → 取了 2 份", font="Noto Sans CJK SC",
                           font_size=24, color=self.COLOR_ACCENT)
        explain_den = Text("分母 3 → 总共 3 份", font="Noto Sans CJK SC",
                           font_size=24, color=self.COLOR_BLUE)
        explain_group = VGroup(explain_num, explain_den).arrange(DOWN, buff=0.2)
        explain_group.move_to(DOWN * 0.5)
        self.play(FadeIn(explain_num), run_time=0.4)
        self.play(FadeIn(explain_den), run_time=0.4)
        self.wait(1.8)

        # 清场
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(sectors_base), FadeOut(hl1), FadeOut(hl2),
            FadeOut(lbl_group), FadeOut(frac_23),
            FadeOut(read_label), FadeOut(explain_group),
            run_time=0.5
        )

    # ───────────────────────────────────────────────
    # Scene 6: 同分母大小比较 (1/4 vs 3/4)
    # ───────────────────────────────────────────────
    def scene_06_compare_same_denominator(self):
        title = Text("比较大小（同分母）",
                     font="Noto Sans CJK SC", font_size=36,
                     color=self.COLOR_MAIN)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        rule_intro = Text("分母相同时，怎么比大小？",
                          font="Noto Sans CJK SC", font_size=26,
                          color=GRAY_A)
        rule_intro.move_to(UP * 5.4)
        self.play(FadeIn(rule_intro), run_time=0.4)

        rect_w = 3.2
        rect_h = 0.85

        # 上方: 1/4
        up_c = UP * 4.0
        bar_14 = self.make_rect_bar(up_c, rect_w, rect_h,
                                     4, 1, self.COLOR_BLUE)
        frac_14 = self.make_fraction_math(r"\frac{1}{4}", font_size=52,
                                           color=self.COLOR_BLUE)
        frac_14.next_to(bar_14, RIGHT, buff=0.4)

        # 下方: 3/4
        down_c = UP * 2.8
        bar_34 = self.make_rect_bar(down_c, rect_w, rect_h,
                                     4, 3, self.COLOR_ACCENT)
        frac_34 = self.make_fraction_math(r"\frac{3}{4}", font_size=52,
                                           color=self.COLOR_ACCENT)
        frac_34.next_to(bar_34, RIGHT, buff=0.4)

        self.play(
            FadeIn(bar_14), Write(frac_14),
            run_time=0.6
        )
        self.play(
            FadeIn(bar_34), Write(frac_34),
            run_time=0.6
        )
        self.wait(0.3)

        # 对比箭头 + 说明
        more_lbl = Text("多！", font="Noto Sans CJK SC",
                        font_size=24, color=self.COLOR_ACCENT)
        more_lbl.next_to(bar_34[1], DOWN, buff=0.08)
        less_lbl = Text("少", font="Noto Sans CJK SC",
                        font_size=24, color=self.COLOR_BLUE)
        less_lbl.next_to(bar_14[1], DOWN, buff=0.08)

        self.play(FadeIn(more_lbl), FadeIn(less_lbl), run_time=0.4)
        self.wait(0.3)

        # 不等号
        compare = MathTex(r"\frac{1}{4} < \frac{3}{4}",
                          font_size=56, color=YELLOW)
        compare.move_to(UP * 1.5)
        self.play(Write(compare), run_time=0.8)

        # 规律框
        rule_text = Text("分母相同：分子越大，分数越大",
                         font="Noto Sans CJK SC", font_size=25,
                         color=self.COLOR_GREEN)
        rule_box = SurroundingRectangle(rule_text, color=self.COLOR_GREEN,
                                        buff=0.2, corner_radius=0)
        rule_text.move_to(UP * 0.4)
        rule_box.move_to(UP * 0.4)
        self.play(Create(rule_box), FadeIn(rule_text), run_time=0.5)
        self.wait(2.2)

        # 清场
        self.play(
            FadeOut(title), FadeOut(rule_intro),
            FadeOut(bar_14), FadeOut(frac_14),
            FadeOut(bar_34), FadeOut(frac_34),
            FadeOut(more_lbl), FadeOut(less_lbl),
            FadeOut(compare), FadeOut(rule_box), FadeOut(rule_text),
            run_time=0.5
        )

    # ───────────────────────────────────────────────
    # Scene 7: 同分子大小比较 (1/2 vs 1/4)
    # ───────────────────────────────────────────────
    def scene_07_compare_same_numerator(self):
        title = Text("比较大小（同分子）",
                     font="Noto Sans CJK SC", font_size=36,
                     color=self.COLOR_MAIN)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        rule_intro = Text("分子相同时，分母大的分数反而小！",
                          font="Noto Sans CJK SC", font_size=24,
                          color=GRAY_A)
        rule_intro.move_to(UP * 5.4)
        self.play(FadeIn(rule_intro), run_time=0.4)

        rect_w = 3.2
        rect_h = 0.85

        # 上方: 1/2（分成2份取1份，每份更大）
        up_c = UP * 4.0
        bar_12 = self.make_rect_bar(up_c, rect_w, rect_h,
                                     2, 1, self.COLOR_BLUE)
        frac_12 = self.make_fraction_math(r"\frac{1}{2}", font_size=52,
                                           color=self.COLOR_BLUE)
        frac_12.next_to(bar_12, RIGHT, buff=0.4)

        # 下方: 1/4（分成4份取1份，每份更小）
        down_c = UP * 2.8
        bar_14 = self.make_rect_bar(down_c, rect_w, rect_h,
                                     4, 1, self.COLOR_ACCENT)
        frac_14 = self.make_fraction_math(r"\frac{1}{4}", font_size=52,
                                           color=self.COLOR_ACCENT)
        frac_14.next_to(bar_14, RIGHT, buff=0.4)

        self.play(FadeIn(bar_12), Write(frac_12), run_time=0.6)
        self.play(FadeIn(bar_14), Write(frac_14), run_time=0.6)
        self.wait(0.3)

        # 视觉说明
        big_lbl = Text("份大！", font="Noto Sans CJK SC",
                       font_size=24, color=self.COLOR_BLUE)
        big_lbl.next_to(bar_12[1], DOWN, buff=0.08)
        small_lbl = Text("份小", font="Noto Sans CJK SC",
                         font_size=24, color=self.COLOR_ACCENT)
        small_lbl.next_to(bar_14[1], DOWN, buff=0.08)
        self.play(FadeIn(big_lbl), FadeIn(small_lbl), run_time=0.4)

        # 不等式
        compare = MathTex(r"\frac{1}{2} > \frac{1}{4}",
                          font_size=56, color=YELLOW)
        compare.move_to(UP * 1.5)
        self.play(Write(compare), run_time=0.8)

        # 规律框
        rule_text = Text("分子相同：分母越大，每份越小\n所以分数反而越小",
                         font="Noto Sans CJK SC", font_size=23,
                         color=self.COLOR_ORANGE, line_spacing=1.4)
        rule_box = SurroundingRectangle(rule_text, color=self.COLOR_ORANGE,
                                        buff=0.2, corner_radius=0)
        rule_text.move_to(UP * 0.2)
        rule_box.move_to(UP * 0.2)
        self.play(Create(rule_box), FadeIn(rule_text), run_time=0.5)

        # 记忆技巧
        tip = Text("记：分的份数越多，每份就越小！",
                   font="Noto Sans CJK SC", font_size=22, color=GRAY_A)
        tip.move_to(DOWN * 1.2)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.4)
        self.wait(2.2)

        # 清场
        self.play(
            FadeOut(title), FadeOut(rule_intro),
            FadeOut(bar_12), FadeOut(frac_12),
            FadeOut(bar_14), FadeOut(frac_14),
            FadeOut(big_lbl), FadeOut(small_lbl),
            FadeOut(compare), FadeOut(rule_box), FadeOut(rule_text),
            FadeOut(tip),
            run_time=0.5
        )

    # ───────────────────────────────────────────────
    # Scene 8: 片尾总结
    # ───────────────────────────────────────────────
    def scene_08_outro(self):
        # 总结标题
        summary_title = Text("今日小结", font="Noto Sans CJK SC",
                             font_size=48, color=self.COLOR_MAIN)
        summary_title.move_to(UP * 5.8)
        self.play(Write(summary_title), run_time=0.6)

        # 四条要点
        points_data = [
            ("①", "平均分无法整除时，用分数表示",  self.COLOR_BLUE),
            ("②", "分母 = 总份数，分子 = 取的份数", self.COLOR_GREEN),
            ("③", "同分母：分子大 → 分数大",       self.COLOR_ORANGE),
            ("④", "同分子：分母大 → 分数小",       self.COLOR_ACCENT),
        ]

        point_rows = VGroup()
        for num_str, text_str, col in points_data:
            num_t = Text(num_str, font="Noto Sans CJK SC",
                         font_size=28, color=col)
            txt_t = Text(text_str, font="Noto Sans CJK SC",
                         font_size=24, color=WHITE)
            row = VGroup(num_t, txt_t).arrange(RIGHT, buff=0.25,
                                               aligned_edge=UP)
            point_rows.add(row)

        point_rows.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        point_rows.move_to(UP * 3.2)

        for row in point_rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.1)

        self.wait(0.4)

        # 分数展示
        fracs_row = VGroup(
            self.make_fraction_math(r"\frac{1}{2}", font_size=44,
                                     color=self.COLOR_BLUE),
            self.make_fraction_math(r"\frac{1}{4}", font_size=44,
                                     color=self.COLOR_GREEN),
            self.make_fraction_math(r"\frac{2}{3}", font_size=44,
                                     color=self.COLOR_PURPLE),
            self.make_fraction_math(r"\frac{3}{4}", font_size=44,
                                     color=self.COLOR_ORANGE),
        )
        fracs_row.arrange(RIGHT, buff=0.7)
        fracs_row.move_to(UP * 0.5)
        self.play(FadeIn(fracs_row, shift=UP * 0.3), run_time=0.8)
        self.wait(0.4)

        # 关注提示
        follow = Text("关注我，获得更多数学技巧！",
                      font="Noto Sans CJK SC", font_size=30,
                      color=YELLOW)
        follow.move_to(DOWN * 1.2)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 作者信息
        author_big = Text("上海初高中数学直通车",
                          font="Noto Sans CJK SC", font_size=34,
                          color=WHITE)
        author_id = Text("@emptyandcalm",
                         font="Noto Sans CJK SC", font_size=26,
                         color=GRAY_B)
        author_group = VGroup(author_big, author_id).arrange(DOWN, buff=0.2)
        author_group.move_to(DOWN * 3.0)
        self.play(FadeIn(author_group, shift=UP * 0.3), run_time=0.6)
        self.wait(2.5)

        # 淡出
        self.play(
            FadeOut(summary_title), FadeOut(point_rows),
            FadeOut(fracs_row), FadeOut(follow),
            FadeOut(author_group), FadeOut(self.author_label),
            run_time=1.0
        )
