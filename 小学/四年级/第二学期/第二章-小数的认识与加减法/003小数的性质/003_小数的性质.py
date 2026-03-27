"""
小数的性质 - Decimal Property Animation
四年级第二学期 - 第二章 小数的认识与加减法

内容: 小数末尾添0或去掉0，大小不变
目标观众: 四年级小学生
格式: TikTok竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class DecimalPropertyLesson(Scene):
    """
    小数的性质教学动画

    场景顺序:
    1. 开场 - 钩子问题
    2. 核心性质揭示
    3. 格子图直观演示 0.3 = 0.30
    4. 化简练习
    5. 注意点 - 末尾 vs 中间/开头
    6. 练习巩固
    7. 片尾总结
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_PRIMARY = "#4fc3f7"    # 亮蓝
        self.COLOR_SECONDARY = "#81c784"  # 绿
        self.COLOR_HIGHLIGHT = "#ffd54f"  # 黄
        self.COLOR_DANGER = "#ef5350"     # 红
        self.COLOR_ACCENT = "#ce93d8"     # 紫
        self.COLOR_TEXT = "#e0e0e0"
        self.COLOR_DIM = "#9e9e9e"

        self.scene_1_opening()
        self.scene_2_property_reveal()
        self.scene_3_grid_demo()
        self.scene_4_simplify()
        self.scene_5_caution()
        self.scene_6_practice()
        self.scene_7_outro()

    # ─────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者信息 (顶部)
        self.author_bar = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.3)

        # 标题
        title = Text(
            "小数的性质",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)

        subtitle = Text(
            "末尾添0或去0，大小不变？",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_TEXT,
        ).move_to(UP * 4.5)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)

        # 钩子：三个数字
        eq_group = VGroup(
            MathTex(r"0.3", font_size=64, color=self.COLOR_PRIMARY),
            MathTex(r"0.30", font_size=64, color=self.COLOR_SECONDARY),
            MathTex(r"0.300", font_size=64, color=self.COLOR_ACCENT),
        ).arrange(DOWN, buff=0.55).move_to(UP * 1.8)

        for mob in eq_group:
            self.play(FadeIn(mob, scale=0.8), run_time=0.4)

        question = Text(
            "它们相等吗？",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 1.2)
        self.play(Write(question), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(eq_group),
            FadeOut(question),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 2: 核心性质揭示
    # ─────────────────────────────────────────────
    def scene_2_property_reveal(self):
        label = Text(
            "小数的性质",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 6.5)
        self.play(Write(label), run_time=0.6)

        prop_line1 = Text(
            '小数末尾添上"0"或去掉"0"，',
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_TEXT,
        ).move_to(UP * 5.3)

        prop_line2 = Text(
            "小数的大小不变。",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 4.5)

        self.play(FadeIn(prop_line1, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(prop_line2, shift=RIGHT * 0.3), run_time=0.6)

        box = SurroundingRectangle(
            prop_line2, color=self.COLOR_HIGHLIGHT, buff=0.15, stroke_width=2
        )
        self.play(Create(box), run_time=0.5)
        self.wait(0.6)

        # 演示：末尾添0
        arrow_add = Arrow(
            start=LEFT * 2.2 + UP * 2.8,
            end=RIGHT * 2.2 + UP * 2.8,
            color=self.COLOR_SECONDARY,
            buff=0,
            stroke_width=4,
        )
        add_label = Text(
            "末尾添 0",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_SECONDARY,
        ).next_to(arrow_add, UP, buff=0.1)

        demo_left = MathTex(r"0.3", font_size=52, color=self.COLOR_PRIMARY).move_to(
            LEFT * 3.0 + UP * 2.8
        )
        demo_right = MathTex(r"0.30", font_size=52, color=self.COLOR_PRIMARY).move_to(
            RIGHT * 3.0 + UP * 2.8
        )

        self.play(FadeIn(demo_left), run_time=0.4)
        self.play(GrowArrow(arrow_add), FadeIn(add_label), run_time=0.5)
        self.play(FadeIn(demo_right), run_time=0.4)

        eq_pair1 = VGroup(
            MathTex(r"0.3", font_size=46, color=self.COLOR_PRIMARY),
            MathTex(r"=", font_size=46, color=self.COLOR_HIGHLIGHT),
            MathTex(r"0.30", font_size=46, color=self.COLOR_SECONDARY),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 1.7)
        self.play(FadeIn(eq_pair1), run_time=0.6)
        self.wait(0.4)

        # 演示：末尾去0
        arrow_rm = Arrow(
            start=RIGHT * 2.2 + UP * 0.5,
            end=LEFT * 2.2 + UP * 0.5,
            color=self.COLOR_DANGER,
            buff=0,
            stroke_width=4,
        )
        rm_label = Text(
            "末尾去 0",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_DANGER,
        ).next_to(arrow_rm, UP, buff=0.1)

        demo_left2 = MathTex(r"2.080", font_size=52, color=self.COLOR_PRIMARY).move_to(
            LEFT * 3.0 + UP * 0.5
        )
        demo_right2 = MathTex(r"2.08", font_size=52, color=self.COLOR_SECONDARY).move_to(
            RIGHT * 3.0 + UP * 0.5
        )

        self.play(FadeIn(demo_right2), run_time=0.4)
        self.play(GrowArrow(arrow_rm), FadeIn(rm_label), run_time=0.5)
        self.play(FadeIn(demo_left2), run_time=0.4)

        eq_pair2 = VGroup(
            MathTex(r"2.080", font_size=46, color=self.COLOR_PRIMARY),
            MathTex(r"=", font_size=46, color=self.COLOR_HIGHLIGHT),
            MathTex(r"2.08", font_size=46, color=self.COLOR_SECONDARY),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.6)
        self.play(FadeIn(eq_pair2), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(label),
            FadeOut(prop_line1),
            FadeOut(prop_line2),
            FadeOut(box),
            FadeOut(arrow_add),
            FadeOut(add_label),
            FadeOut(demo_left),
            FadeOut(demo_right),
            FadeOut(eq_pair1),
            FadeOut(arrow_rm),
            FadeOut(rm_label),
            FadeOut(demo_left2),
            FadeOut(demo_right2),
            FadeOut(eq_pair2),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 3: 格子图直观演示
    # ─────────────────────────────────────────────
    def scene_3_grid_demo(self):
        title = Text(
            "用格子图理解",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 6.8)
        self.play(Write(title), run_time=0.5)

        # ── 左侧: 0.3 (10格，3格涂色) ──
        left_label = Text(
            "0.3（十分之三）",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_PRIMARY,
        ).move_to(LEFT * 2.2 + UP * 5.8)

        cell_w = 0.33
        cell_h = 0.48
        n_cells_10 = 10
        grid_w_10 = cell_w * n_cells_10
        left_center = np.array([-2.2, 4.8, 0])
        left_origin = left_center - np.array([grid_w_10 / 2, 0, 0])

        cells_10 = VGroup()
        filled_10 = VGroup()
        for i in range(n_cells_10):
            cx = left_origin[0] + i * cell_w + cell_w / 2
            cy = left_center[1]
            rect = Rectangle(
                width=cell_w, height=cell_h,
                stroke_color=self.COLOR_DIM,
                stroke_width=1.5,
                fill_opacity=0,
            ).move_to(np.array([cx, cy, 0]))
            cells_10.add(rect)
            if i < 3:
                filled = Rectangle(
                    width=cell_w, height=cell_h,
                    fill_color=self.COLOR_PRIMARY,
                    fill_opacity=0.75,
                    stroke_color=self.COLOR_DIM,
                    stroke_width=1.5,
                ).move_to(np.array([cx, cy, 0]))
                filled_10.add(filled)

        formula_10 = VGroup(
            MathTex(r"\frac{3}{10}", font_size=34, color=self.COLOR_PRIMARY),
            MathTex(r"= 0.3", font_size=34, color=self.COLOR_PRIMARY),
        ).arrange(RIGHT, buff=0.2).move_to(LEFT * 2.2 + UP * 3.9)

        # ── 右侧: 0.30 (10x10格，30格涂色) ──
        right_label = Text(
            "0.30（百分之三十）",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_SECONDARY,
        ).move_to(RIGHT * 2.2 + UP * 5.8)

        cell_s = 0.19
        n_r, n_c = 10, 10
        grid_s_w = cell_s * n_c
        grid_s_h = cell_s * n_r
        right_center = np.array([2.2, 4.6, 0])
        right_origin = right_center - np.array([grid_s_w / 2, grid_s_h / 2, 0])

        cells_100 = VGroup()
        filled_100 = VGroup()
        count = 0
        for row in range(n_r):
            for col in range(n_c):
                cx = right_origin[0] + col * cell_s + cell_s / 2
                cy = right_origin[1] + row * cell_s + cell_s / 2
                rect = Rectangle(
                    width=cell_s, height=cell_s,
                    stroke_color=self.COLOR_DIM,
                    stroke_width=0.6,
                    fill_opacity=0,
                ).move_to(np.array([cx, cy, 0]))
                cells_100.add(rect)
                if count < 30:
                    filled = Rectangle(
                        width=cell_s, height=cell_s,
                        fill_color=self.COLOR_SECONDARY,
                        fill_opacity=0.75,
                        stroke_color=self.COLOR_DIM,
                        stroke_width=0.6,
                    ).move_to(np.array([cx, cy, 0]))
                    filled_100.add(filled)
                count += 1

        formula_100 = VGroup(
            MathTex(r"\frac{30}{100}", font_size=34, color=self.COLOR_SECONDARY),
            MathTex(r"= 0.30", font_size=34, color=self.COLOR_SECONDARY),
        ).arrange(RIGHT, buff=0.2).move_to(RIGHT * 2.2 + UP * 3.5)

        self.play(FadeIn(left_label), FadeIn(right_label), run_time=0.4)
        self.play(Create(cells_10), Create(cells_100), run_time=0.8)
        self.play(FadeIn(filled_10), FadeIn(filled_100), run_time=0.7)
        self.play(Write(formula_10), Write(formula_100), run_time=0.7)
        self.wait(0.5)

        equal_note = Text(
            "两者涂色面积相同  →  大小相等！",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 2.8)
        self.play(FadeIn(equal_note, shift=UP * 0.3), run_time=0.6)

        big_eq = VGroup(
            MathTex(r"0.3", font_size=54, color=self.COLOR_PRIMARY),
            MathTex(r"=", font_size=54, color=self.COLOR_HIGHLIGHT),
            MathTex(r"0.30", font_size=54, color=self.COLOR_SECONDARY),
            MathTex(r"=", font_size=54, color=self.COLOR_HIGHLIGHT),
            MathTex(r"0.300", font_size=54, color=self.COLOR_ACCENT),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 1.8)
        self.play(FadeIn(big_eq), run_time=0.7)
        self.wait(2.0)

        tip = Text(
            "末尾每多一个0，分母变大10倍，\n分子也变大10倍，分数值不变。",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_DIM,
        ).move_to(UP * 0.5)
        self.play(FadeIn(tip), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(left_label),
            FadeOut(right_label),
            FadeOut(cells_10),
            FadeOut(filled_10),
            FadeOut(cells_100),
            FadeOut(filled_100),
            FadeOut(formula_10),
            FadeOut(formula_100),
            FadeOut(equal_note),
            FadeOut(big_eq),
            FadeOut(tip),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 4: 化简小数
    # ─────────────────────────────────────────────
    def scene_4_simplify(self):
        title = Text(
            "化简小数",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 6.8)
        self.play(Write(title), run_time=0.5)

        task_label = Text(
            "去掉多余的末尾0",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_TEXT,
        ).move_to(UP * 5.9)
        self.play(FadeIn(task_label), run_time=0.4)

        # 例1: 2.080 → 2.08
        ex1_title = Text(
            "例1：化简  2.080",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_PRIMARY,
        ).move_to(UP * 4.8)
        self.play(Write(ex1_title), run_time=0.6)

        num_2080 = MathTex(
            r"2.08", r"0",
            font_size=72,
            color=WHITE,
        ).move_to(UP * 3.5)
        self.play(Write(num_2080), run_time=0.7)

        # 高亮末尾0
        trailing_box = SurroundingRectangle(
            num_2080[1], color=self.COLOR_DANGER, buff=0.08, stroke_width=3
        )
        trailing_note = Text(
            "末尾的 0，可以去掉",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_DANGER,
        ).next_to(trailing_box, RIGHT, buff=0.2)

        self.play(Create(trailing_box), FadeIn(trailing_note), run_time=0.5)
        self.wait(0.5)

        # 划掉末尾0
        cross_line = Line(
            num_2080[1].get_corner(DL) + LEFT * 0.05,
            num_2080[1].get_corner(UR) + RIGHT * 0.05,
            color=self.COLOR_DANGER,
            stroke_width=5,
        )
        self.play(Create(cross_line), run_time=0.4)
        self.wait(0.4)

        result_1 = VGroup(
            MathTex(r"2.080", font_size=58, color=self.COLOR_PRIMARY),
            MathTex(r"=", font_size=58, color=self.COLOR_HIGHLIGHT),
            MathTex(r"2.08", font_size=58, color=self.COLOR_SECONDARY),
        ).arrange(RIGHT, buff=0.35).move_to(UP * 1.8)

        self.play(
            FadeOut(num_2080),
            FadeOut(trailing_box),
            FadeOut(trailing_note),
            FadeOut(cross_line),
            FadeIn(result_1),
            run_time=0.6,
        )
        self.wait(0.6)

        # 例2: 0.3000 → 0.3
        ex2_title = Text(
            "例2：化简  0.3000",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_PRIMARY,
        ).move_to(UP * 0.6)
        self.play(Write(ex2_title), run_time=0.6)

        num_03000 = MathTex(
            r"0.3", r"000",
            font_size=72,
            color=WHITE,
        ).move_to(DOWN * 0.7)
        self.play(Write(num_03000), run_time=0.6)
        self.wait(0.3)

        note2 = Text(
            "末尾连续3个0，全部去掉",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_DIM,
        ).move_to(DOWN * 1.8)
        self.play(FadeIn(note2), run_time=0.4)

        result_2 = VGroup(
            MathTex(r"0.3000", font_size=58, color=self.COLOR_PRIMARY),
            MathTex(r"=", font_size=58, color=self.COLOR_HIGHLIGHT),
            MathTex(r"0.3", font_size=58, color=self.COLOR_SECONDARY),
        ).arrange(RIGHT, buff=0.35).move_to(DOWN * 3.2)
        self.play(FadeIn(result_2), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(title),
            FadeOut(task_label),
            FadeOut(ex1_title),
            FadeOut(result_1),
            FadeOut(ex2_title),
            FadeOut(num_03000),
            FadeOut(note2),
            FadeOut(result_2),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 5: 注意点 - 末尾 vs 中间/整数
    # ─────────────────────────────────────────────
    def scene_5_caution(self):
        title = Text(
            "注意！",
            font="PingFang SC",
            font_size=46,
            color=self.COLOR_DANGER,
        ).move_to(UP * 6.8)
        self.play(Write(title), run_time=0.5)

        subtitle = Text(
            '只有"末尾"的0才能去掉',
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_TEXT,
        ).move_to(UP * 5.9)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 正确示例
        correct_label = Text(
            "正确做法",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_SECONDARY,
        ).move_to(UP * 5.0)
        self.play(FadeIn(correct_label), run_time=0.3)

        correct_ex = VGroup(
            MathTex(r"2.00", font_size=50, color=WHITE),
            MathTex(r"=", font_size=50, color=self.COLOR_HIGHLIGHT),
            MathTex(r"2.0", font_size=50, color=self.COLOR_SECONDARY),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 4.1)
        check_mark = Text("  OK", font="PingFang SC", font_size=32, color=self.COLOR_SECONDARY)
        check_mark.next_to(correct_ex, RIGHT, buff=0.2)

        correct_note = Text(
            "末尾的0 → 可以去掉",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_SECONDARY,
        ).move_to(UP * 3.2)

        self.play(FadeIn(correct_ex), FadeIn(check_mark), run_time=0.5)
        self.play(FadeIn(correct_note), run_time=0.4)

        # 分割线
        sep = Line(LEFT * 3.5, RIGHT * 3.5, color=self.COLOR_DIM, stroke_width=1.5).move_to(UP * 2.5)
        self.play(Create(sep), run_time=0.3)

        # 错误示例1: 去中间的0
        wrong_label1 = Text(
            "错误示例 1：去掉中间的0",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_DANGER,
        ).move_to(UP * 2.0)
        self.play(FadeIn(wrong_label1), run_time=0.3)

        wrong_ex1 = VGroup(
            MathTex(r"2.008", font_size=50, color=WHITE),
            MathTex(r"\rightarrow", font_size=40, color=self.COLOR_DANGER),
            MathTex(r"2.8", font_size=50, color=self.COLOR_DANGER),
            Text("  NG", font="PingFang SC", font_size=32, color=self.COLOR_DANGER),
        ).arrange(RIGHT, buff=0.25).move_to(UP * 1.1)

        wrong_note1 = Text(
            "中间的0不能去！2.008 变成 2.8 了！",
            font="PingFang SC",
            font_size=21,
            color=self.COLOR_DANGER,
        ).move_to(UP * 0.2)

        self.play(FadeIn(wrong_ex1), run_time=0.5)
        self.play(FadeIn(wrong_note1), run_time=0.4)
        self.wait(0.8)

        # 错误示例2: 去整数部分的0
        sep2 = Line(LEFT * 3.5, RIGHT * 3.5, color=self.COLOR_DIM, stroke_width=1.5).move_to(DOWN * 0.6)
        self.play(Create(sep2), run_time=0.3)

        wrong_label2 = Text(
            "错误示例 2：去掉整数部分的0",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_DANGER,
        ).move_to(DOWN * 1.2)
        self.play(FadeIn(wrong_label2), run_time=0.3)

        wrong_ex2 = VGroup(
            MathTex(r"0.3", font_size=50, color=WHITE),
            MathTex(r"\rightarrow", font_size=40, color=self.COLOR_DANGER),
            MathTex(r".3", font_size=50, color=self.COLOR_DANGER),
            Text("  NG", font="PingFang SC", font_size=32, color=self.COLOR_DANGER),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 2.1)

        wrong_note2 = Text(
            "整数位的0不能去！",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_DANGER,
        ).move_to(DOWN * 3.0)

        self.play(FadeIn(wrong_ex2), run_time=0.5)
        self.play(FadeIn(wrong_note2), run_time=0.4)
        self.wait(0.8)

        # 总结框
        summary_text = Text(
            "只有小数末尾的0才能添或去！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 4.3)
        summary_box = SurroundingRectangle(
            summary_text, color=self.COLOR_HIGHLIGHT, buff=0.2, stroke_width=2
        )
        self.play(FadeIn(summary_text), Create(summary_box), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(correct_label),
            FadeOut(correct_ex),
            FadeOut(check_mark),
            FadeOut(correct_note),
            FadeOut(sep),
            FadeOut(wrong_label1),
            FadeOut(wrong_ex1),
            FadeOut(wrong_note1),
            FadeOut(sep2),
            FadeOut(wrong_label2),
            FadeOut(wrong_ex2),
            FadeOut(wrong_note2),
            FadeOut(summary_text),
            FadeOut(summary_box),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 6: 练习巩固
    # ─────────────────────────────────────────────
    def scene_6_practice(self):
        title = Text(
            "练一练",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 6.8)
        self.play(Write(title), run_time=0.5)

        prompt = Text(
            "化简下列小数",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_TEXT,
        ).move_to(UP * 5.9)
        self.play(FadeIn(prompt), run_time=0.3)

        # 题目
        questions_data = [
            (r"3.500", r"3.5"),
            (r"10.070", r"10.07"),
            (r"0.9090", r"0.909"),
        ]

        q_mobs = []
        for i, (q, _) in enumerate(questions_data):
            q_mob = VGroup(
                MathTex(q, font_size=50, color=WHITE),
                MathTex(r"= \ ?", font_size=50, color=self.COLOR_DIM),
            ).arrange(RIGHT, buff=0.25).move_to(UP * (4.6 - i * 1.7))
            self.play(FadeIn(q_mob), run_time=0.4)
            q_mobs.append(q_mob)

        self.wait(1.5)

        # 答案揭示
        ans_mobs = []
        for i, (q, ans) in enumerate(questions_data):
            eq_full = VGroup(
                MathTex(q, font_size=50, color=self.COLOR_PRIMARY),
                MathTex(r"=", font_size=50, color=self.COLOR_HIGHLIGHT),
                MathTex(ans, font_size=50, color=self.COLOR_SECONDARY),
            ).arrange(RIGHT, buff=0.3).move_to(UP * (4.6 - i * 1.7))
            self.play(ReplacementTransform(q_mobs[i], eq_full), run_time=0.5)
            ans_mobs.append(eq_full)
            self.wait(0.4)

        self.wait(0.5)

        # 等值改写 (添0)
        sep = Line(LEFT * 3.5, RIGHT * 3.5, color=self.COLOR_DIM, stroke_width=1.5).move_to(DOWN * 0.8)
        self.play(Create(sep), run_time=0.3)

        prompt2 = Text(
            "改写成百分位的小数（末尾添0）",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_TEXT,
        ).move_to(DOWN * 1.4)
        self.play(FadeIn(prompt2), run_time=0.3)

        add_q = VGroup(
            MathTex(r"1.4", font_size=50, color=WHITE),
            MathTex(r"= \ ?", font_size=50, color=self.COLOR_DIM),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 2.5)
        self.play(FadeIn(add_q), run_time=0.4)
        self.wait(1.0)

        add_ans = VGroup(
            MathTex(r"1.4", font_size=50, color=self.COLOR_PRIMARY),
            MathTex(r"=", font_size=50, color=self.COLOR_HIGHLIGHT),
            MathTex(r"1.40", font_size=50, color=self.COLOR_SECONDARY),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 2.5)
        self.play(ReplacementTransform(add_q, add_ans), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(prompt),
            *[FadeOut(m) for m in ans_mobs],
            FadeOut(sep),
            FadeOut(prompt2),
            FadeOut(add_ans),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 7: 片尾总结
    # ─────────────────────────────────────────────
    def scene_7_outro(self):
        summary_title = Text(
            "小数的性质 — 总结",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)
        self.play(Write(summary_title), run_time=0.7)

        points = VGroup(
            Text(
                "1. 末尾添0  →  大小不变",
                font="PingFang SC",
                font_size=26,
                color=self.COLOR_SECONDARY,
            ),
            Text(
                "2. 末尾去0  →  大小不变",
                font="PingFang SC",
                font_size=26,
                color=self.COLOR_SECONDARY,
            ),
            Text(
                "3. 只能操作末尾的0！",
                font="PingFang SC",
                font_size=26,
                color=self.COLOR_DANGER,
            ),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 3.7)

        for pt in points:
            self.play(FadeIn(pt, shift=RIGHT * 0.3), run_time=0.4)

        # 最终等式
        final_eq = VGroup(
            MathTex(r"0.3", font_size=52, color=self.COLOR_PRIMARY),
            MathTex(r"=", font_size=52, color=self.COLOR_HIGHLIGHT),
            MathTex(r"0.30", font_size=52, color=self.COLOR_SECONDARY),
            MathTex(r"=", font_size=52, color=self.COLOR_HIGHLIGHT),
            MathTex(r"0.300", font_size=52, color=self.COLOR_ACCENT),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 1.5)
        self.play(FadeIn(final_eq), run_time=0.7)
        self.wait(0.5)

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=34,
            color=WHITE,
        ).move_to(DOWN * 1.2)
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_DIM,
        ).move_to(DOWN * 2.1)

        self.play(Transform(self.author_bar, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 3.3)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰星星
        star_positions = [
            np.array([-3.0, -4.6, 0]),
            np.array([-1.5, -5.0, 0]),
            np.array([0.0, -4.5, 0]),
            np.array([1.5, -5.0, 0]),
            np.array([3.0, -4.6, 0]),
        ]
        stars = VGroup(
            *[
                Text("*", font="PingFang SC", font_size=32, color=self.COLOR_HIGHLIGHT)
                .move_to(pos)
                for pos in star_positions
            ]
        )
        self.play(*[FadeIn(s, scale=0.5) for s in stars], run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(summary_title),
            FadeOut(points),
            FadeOut(final_eq),
            FadeOut(self.author_bar),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(stars),
            run_time=1.0,
        )
