"""
乘法交换律与结合律 - Multiplication Commutative & Associative Laws
TikTok 竖屏教学动画 (1080×1920)
四年级 第二学期 第一章-复习与提高
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ── 全局配置 TikTok 竖屏 ──────────────────────────────────────────
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ── 颜色主题 ────────────────────────────────────────────────────────
BG_COLOR     = "#1a1a2e"
GOLD_COLOR   = "#f5c518"
TEAL_COLOR   = "#00b4d8"
ORANGE_COLOR = "#f4845f"
GREEN_COLOR  = "#57cc99"
PINK_COLOR   = "#e07ab1"
GRAY_TEXT    = "#9ca3af"
WHITE_TEXT   = "#f1f5f9"
PURPLE_COLOR = "#9d4edd"


class MultiplicationLawLesson(Scene):
    """
    乘法交换律与结合律教学动画

    场景顺序:
    1. 开场 – 钩子问题，激发好奇心
    2. 交换律 – 图形演示 a×b = b×a
    3. 结合律 – 图形演示 (a×b)×c = a×(b×c)
    4. 简便运算 – 示例 25×4×17 = 1700
    5. 总结 + 片尾
    """

    # ── construct ────────────────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG_COLOR

        # 作者标识（全程保留顶部）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color=GRAY_TEXT,
        ).move_to(UP * 7.0)
        self.add(self.author)

        self.scene_1_hook()
        self.scene_2_commutative()
        self.scene_3_associative()
        self.scene_4_simplify()
        self.scene_5_outro()

    # ─────────────────────────────────────────────────────────────────
    # 场景 1 · 开场钩子
    # ─────────────────────────────────────────────────────────────────
    def scene_1_hook(self):
        # 主标题
        title = Text(
            "乘法的两个秘密武器",
            font="PingFang SC",
            font_size=44,
            color=GOLD_COLOR,
        ).move_to(UP * 5.5)

        subtitle = Text(
            "交换律  ×  结合律",
            font="PingFang SC",
            font_size=30,
            color=WHITE_TEXT,
        ).move_to(UP * 4.6)

        # 钩子问题
        q_line1 = Text(
            "25 × 4 × 17",
            font="PingFang SC",
            font_size=48,
            color=TEAL_COLOR,
        ).move_to(UP * 2.8)

        q_line2 = Text(
            "你能秒算出来吗？",
            font="PingFang SC",
            font_size=32,
            color=ORANGE_COLOR,
        ).move_to(UP * 1.8)

        question_mark = Text(
            "？",
            font="PingFang SC",
            font_size=120,
            color=GOLD_COLOR,
        ).move_to(DOWN * 0.5)

        hint = Text(
            "学完今天，轻松算！",
            font="PingFang SC",
            font_size=28,
            color=GREEN_COLOR,
        ).move_to(DOWN * 2.5)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.play(Write(q_line1), run_time=0.6)
        self.play(FadeIn(q_line2), run_time=0.4)
        self.play(GrowFromCenter(question_mark), run_time=0.6)
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(q_line1),
            FadeOut(q_line2),
            FadeOut(question_mark),
            FadeOut(hint),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────────────────────────
    # 场景 2 · 乘法交换律
    # ─────────────────────────────────────────────────────────────────
    def scene_2_commutative(self):
        # ── 标题 ──────────────────────────────────────────────────────
        sec_title = Text(
            "乘法交换律",
            font="PingFang SC",
            font_size=44,
            color=TEAL_COLOR,
        ).move_to(UP * 6.3)

        sec_sub = Text(
            "交换因数位置，积不变",
            font="PingFang SC",
            font_size=26,
            color=GRAY_TEXT,
        ).move_to(UP * 5.6)

        self.play(Write(sec_title), run_time=0.6)
        self.play(FadeIn(sec_sub), run_time=0.4)

        # ── 示例：3 × 4 用小方格可视化 ──────────────────────────────
        # 左侧：3行4列方格 → 表示 3×4
        grid_left  = self._make_grid(rows=3, cols=4,
                                     cell_color=TEAL_COLOR,
                                     center=np.array([-2.2, 2.0, 0]))
        label_left_top = Text("3 行", font="PingFang SC",
                              font_size=22, color=WHITE_TEXT)
        label_left_top.next_to(grid_left, LEFT, buff=0.15)
        label_left_bot = Text("4 列", font="PingFang SC",
                              font_size=22, color=WHITE_TEXT)
        label_left_bot.next_to(grid_left, DOWN, buff=0.12)

        formula_left = MathTex(r"3 \times 4 = 12",
                               font_size=38, color=TEAL_COLOR)
        formula_left.next_to(grid_left, DOWN, buff=0.45)

        # 右侧：4行3列方格 → 表示 4×3
        grid_right = self._make_grid(rows=4, cols=3,
                                     cell_color=ORANGE_COLOR,
                                     center=np.array([2.2, 2.0, 0]))
        label_right_top = Text("4 行", font="PingFang SC",
                               font_size=22, color=WHITE_TEXT)
        label_right_top.next_to(grid_right, RIGHT, buff=0.15)
        label_right_bot = Text("3 列", font="PingFang SC",
                               font_size=22, color=WHITE_TEXT)
        label_right_bot.next_to(grid_right, DOWN, buff=0.12)

        formula_right = MathTex(r"4 \times 3 = 12",
                                font_size=38, color=ORANGE_COLOR)
        formula_right.next_to(grid_right, DOWN, buff=0.45)

        # 等号链接
        equal_sign = Text("=", font="PingFang SC",
                          font_size=40, color=GOLD_COLOR)
        equal_sign.move_to(np.array([0, formula_left.get_center()[1], 0]))

        self.play(Create(grid_left), run_time=0.8)
        self.play(
            FadeIn(label_left_top), FadeIn(label_left_bot),
            Write(formula_left), run_time=0.6,
        )
        self.wait(0.4)
        self.play(Create(grid_right), run_time=0.8)
        self.play(
            FadeIn(label_right_top), FadeIn(label_right_bot),
            Write(formula_right), run_time=0.6,
        )
        self.play(FadeIn(equal_sign), run_time=0.3)
        self.wait(0.8)

        # ── 公式展示 ──────────────────────────────────────────────────
        law_box_bg = RoundedRectangle(
            width=7.5, height=1.4,
            corner_radius=0.3,
            fill_color="#0f3460",
            fill_opacity=0.95,
            stroke_color=TEAL_COLOR,
            stroke_width=2,
        ).move_to(DOWN * 0.2)

        law_formula = MathTex(r"a \times b = b \times a",
                              font_size=46, color=WHITE_TEXT)
        law_formula.move_to(law_box_bg.get_center())

        self.play(FadeIn(law_box_bg), Write(law_formula), run_time=0.8)
        self.wait(1.5)

        # ── 直观"交换"箭头动画 ──────────────────────────────────────
        a_box = self._make_factor_box("a", TEAL_COLOR,
                                      pos=np.array([-1.8, -1.6, 0]))
        b_box = self._make_factor_box("b", ORANGE_COLOR,
                                      pos=np.array([1.8, -1.6, 0]))

        times1 = Text("×", font="PingFang SC",
                      font_size=36, color=WHITE_TEXT).move_to(np.array([0, -1.6, 0]))

        self.play(FadeIn(a_box), FadeIn(times1), FadeIn(b_box), run_time=0.5)
        self.wait(0.4)

        # 交换箭头
        arrow_ab = CurvedArrow(
            np.array([-1.4, -1.1, 0]),
            np.array([1.4, -1.1, 0]),
            angle=-TAU / 5,
            color=GOLD_COLOR,
            stroke_width=3,
        )
        swap_text = Text("交换！", font="PingFang SC",
                         font_size=24, color=GOLD_COLOR)
        swap_text.move_to(np.array([0, -0.5, 0]))

        self.play(Create(arrow_ab), FadeIn(swap_text), run_time=0.6)
        self.wait(0.3)

        # 实际交换 a 和 b
        a_box_copy = a_box.copy()
        b_box_copy = b_box.copy()
        self.play(
            a_box_copy.animate.move_to(np.array([1.8, -1.6, 0])),
            b_box_copy.animate.move_to(np.array([-1.8, -1.6, 0])),
            run_time=0.8,
        )
        self.wait(0.6)

        result_same = Text(
            "积一样！",
            font="PingFang SC",
            font_size=30,
            color=GREEN_COLOR,
        ).move_to(np.array([0, -2.6, 0]))
        self.play(FadeIn(result_same, shift=UP * 0.2), run_time=0.4)
        self.wait(1.2)

        # 清场
        scene2_objects = VGroup(
            sec_title, sec_sub,
            grid_left, grid_right,
            label_left_top, label_left_bot,
            label_right_top, label_right_bot,
            formula_left, formula_right, equal_sign,
            law_box_bg, law_formula,
            a_box, b_box, a_box_copy, b_box_copy,
            times1, arrow_ab, swap_text, result_same,
        )
        self.play(FadeOut(scene2_objects), run_time=0.5)

    # ─────────────────────────────────────────────────────────────────
    # 场景 3 · 乘法结合律
    # ─────────────────────────────────────────────────────────────────
    def scene_3_associative(self):
        # ── 标题 ──────────────────────────────────────────────────────
        sec_title = Text(
            "乘法结合律",
            font="PingFang SC",
            font_size=44,
            color=PURPLE_COLOR,
        ).move_to(UP * 6.3)

        sec_sub = Text(
            "三数相乘，先乘哪两个都一样",
            font="PingFang SC",
            font_size=26,
            color=GRAY_TEXT,
        ).move_to(UP * 5.5)

        self.play(Write(sec_title), run_time=0.6)
        self.play(FadeIn(sec_sub), run_time=0.4)

        # ── 方式 A：先算 (2×3)×4 ───────────────────────────────────
        way_a_title = Text(
            "方式 A",
            font="PingFang SC",
            font_size=28,
            color=TEAL_COLOR,
        ).move_to(UP * 4.5)

        step_a1 = MathTex(r"(2 \times 3) \times 4",
                          font_size=40, color=WHITE_TEXT)
        step_a1.move_to(UP * 3.7)

        step_a2 = MathTex(r"= 6 \times 4",
                          font_size=40, color=TEAL_COLOR)
        step_a2.next_to(step_a1, DOWN, buff=0.3)

        step_a3 = MathTex(r"= 24",
                          font_size=40, color=GREEN_COLOR)
        step_a3.next_to(step_a2, DOWN, buff=0.3)

        brace_a = Brace(
            VGroup(step_a1[0][1], step_a1[0][3]),   # 括 "2×3"
            DOWN, color=TEAL_COLOR, buff=0.05
        )

        self.play(FadeIn(way_a_title), Write(step_a1), run_time=0.6)
        self.play(FadeIn(brace_a), run_time=0.3)
        self.play(Write(step_a2), run_time=0.5)
        self.play(Write(step_a3), run_time=0.5)
        self.wait(0.6)

        # 分隔线
        divider = Line(
            np.array([-3.8, 2.0, 0]), np.array([3.8, 2.0, 0]),
            color=GRAY_TEXT, stroke_width=1.5
        )
        self.play(Create(divider), run_time=0.3)

        # ── 方式 B：先算 2×(3×4) ───────────────────────────────────
        way_b_title = Text(
            "方式 B",
            font="PingFang SC",
            font_size=28,
            color=ORANGE_COLOR,
        ).move_to(UP * 1.5)

        step_b1 = MathTex(r"2 \times (3 \times 4)",
                          font_size=40, color=WHITE_TEXT)
        step_b1.move_to(UP * 0.7)

        step_b2 = MathTex(r"= 2 \times 12",
                          font_size=40, color=ORANGE_COLOR)
        step_b2.next_to(step_b1, DOWN, buff=0.3)

        step_b3 = MathTex(r"= 24",
                          font_size=40, color=GREEN_COLOR)
        step_b3.next_to(step_b2, DOWN, buff=0.3)

        self.play(FadeIn(way_b_title), Write(step_b1), run_time=0.6)
        self.play(Write(step_b2), run_time=0.5)
        self.play(Write(step_b3), run_time=0.5)
        self.wait(0.6)

        # ── 结论：公式 ────────────────────────────────────────────────
        equal_result = Text(
            "结果相同！",
            font="PingFang SC",
            font_size=32,
            color=GOLD_COLOR,
        ).move_to(DOWN * 1.2)

        law_box_bg = RoundedRectangle(
            width=7.8, height=1.5,
            corner_radius=0.3,
            fill_color="#16213e",
            fill_opacity=0.95,
            stroke_color=PURPLE_COLOR,
            stroke_width=2,
        ).move_to(DOWN * 2.5)

        law_formula = MathTex(
            r"(a \times b) \times c = a \times (b \times c)",
            font_size=34, color=WHITE_TEXT,
        )
        law_formula.move_to(law_box_bg.get_center())

        self.play(FadeIn(equal_result, scale=1.1), run_time=0.5)
        self.play(FadeIn(law_box_bg), Write(law_formula), run_time=0.8)
        self.wait(2.0)

        scene3_objects = VGroup(
            sec_title, sec_sub,
            way_a_title, step_a1, step_a2, step_a3, brace_a,
            divider,
            way_b_title, step_b1, step_b2, step_b3,
            equal_result, law_box_bg, law_formula,
        )
        self.play(FadeOut(scene3_objects), run_time=0.5)

    # ─────────────────────────────────────────────────────────────────
    # 场景 4 · 简便运算示例
    # ─────────────────────────────────────────────────────────────────
    def scene_4_simplify(self):
        # ── 标题 ──────────────────────────────────────────────────────
        sec_title = Text(
            "活学活用 · 简便运算",
            font="PingFang SC",
            font_size=38,
            color=GOLD_COLOR,
        ).move_to(UP * 6.3)

        problem = Text(
            "计算  25 × 4 × 17",
            font="PingFang SC",
            font_size=40,
            color=WHITE_TEXT,
        ).move_to(UP * 5.2)

        self.play(Write(sec_title), run_time=0.5)
        self.play(Write(problem), run_time=0.6)
        self.wait(0.5)

        # ── 策略提示 ──────────────────────────────────────────────────
        tip_bg = RoundedRectangle(
            width=7.0, height=0.9,
            corner_radius=0.25,
            fill_color="#0f3460",
            fill_opacity=0.9,
            stroke_color=TEAL_COLOR,
            stroke_width=1.5,
        ).move_to(UP * 4.0)

        tip_text = Text(
            "发现：25 × 4 = 100，整数好算！",
            font="PingFang SC",
            font_size=24,
            color=TEAL_COLOR,
        ).move_to(tip_bg.get_center())

        self.play(FadeIn(tip_bg), Write(tip_text), run_time=0.7)
        self.wait(0.4)

        # ── 步骤 1：原式 ─────────────────────────────────────────────
        step_label_1 = Text("原式", font="PingFang SC",
                            font_size=24, color=GRAY_TEXT)
        step_label_1.move_to(np.array([-3.0, 2.7, 0]))

        step1 = MathTex(r"= 25 \times 4 \times 17",
                        font_size=40, color=WHITE_TEXT)
        step1.move_to(np.array([0.8, 2.7, 0]))

        self.play(FadeIn(step_label_1), Write(step1), run_time=0.6)

        # 高亮 25×4 部分
        highlight_rect = SurroundingRectangle(
            VGroup(step1[0][1:6]),   # "25×4"
            color=GOLD_COLOR,
            buff=0.08,
            stroke_width=2,
        )
        self.play(Create(highlight_rect), run_time=0.4)
        self.wait(0.3)

        # ── 步骤 2：使用结合律调整括号 ───────────────────────────────
        step_label_2 = Text("结合律", font="PingFang SC",
                            font_size=24, color=PURPLE_COLOR)
        step_label_2.move_to(np.array([-3.0, 1.7, 0]))

        step2 = MathTex(r"= (25 \times 4) \times 17",
                        font_size=40, color=PURPLE_COLOR)
        step2.move_to(np.array([0.8, 1.7, 0]))

        self.play(
            FadeOut(highlight_rect),
            FadeIn(step_label_2),
            TransformMatchingShapes(step1.copy(), step2),
            run_time=0.8,
        )
        self.wait(0.4)

        # ── 步骤 3：计算括号内 ────────────────────────────────────────
        step_label_3 = Text("计算", font="PingFang SC",
                            font_size=24, color=TEAL_COLOR)
        step_label_3.move_to(np.array([-3.0, 0.7, 0]))

        step3 = MathTex(r"= 100 \times 17",
                        font_size=40, color=TEAL_COLOR)
        step3.move_to(np.array([0.8, 0.7, 0]))

        hundred_note = Text(
            "25×4=100",
            font="PingFang SC",
            font_size=22,
            color=GOLD_COLOR,
        ).next_to(step3, RIGHT, buff=0.3)

        self.play(FadeIn(step_label_3), Write(step3), run_time=0.6)
        self.play(FadeIn(hundred_note), run_time=0.3)
        self.wait(0.4)

        # ── 步骤 4：得出答案 ─────────────────────────────────────────
        step_label_4 = Text("答案", font="PingFang SC",
                            font_size=24, color=GREEN_COLOR)
        step_label_4.move_to(np.array([-3.0, -0.3, 0]))

        step4 = MathTex(r"= 1700",
                        font_size=56, color=GREEN_COLOR)
        step4.move_to(np.array([0.8, -0.3, 0]))

        self.play(FadeIn(step_label_4), Write(step4, run_time=0.6))
        self.play(
            Flash(step4, color=GOLD_COLOR, flash_radius=0.8),
            run_time=0.6,
        )
        self.wait(0.5)

        # ── 对比：普通算法 vs 简便算法 ───────────────────────────────
        compare_bg = RoundedRectangle(
            width=7.8, height=3.0,
            corner_radius=0.3,
            fill_color="#16213e",
            fill_opacity=0.95,
            stroke_color=GRAY_TEXT,
            stroke_width=1.2,
        ).move_to(DOWN * 2.3)

        compare_title = Text(
            "对比一下",
            font="PingFang SC",
            font_size=26,
            color=GRAY_TEXT,
        ).move_to(np.array([0, -1.3, 0]))

        old_label = Text("普通算法：", font="PingFang SC",
                         font_size=22, color=ORANGE_COLOR)
        old_steps = MathTex(r"25 \times 4 = 100,\ 100 \times 17",
                            font_size=28, color=ORANGE_COLOR)
        old_row = VGroup(old_label, old_steps).arrange(RIGHT, buff=0.1)
        old_row.move_to(np.array([0, -2.0, 0]))

        new_label = Text("简便算法：", font="PingFang SC",
                         font_size=22, color=GREEN_COLOR)
        new_steps = MathTex(r"(25 \times 4) \times 17 = 100 \times 17",
                            font_size=28, color=GREEN_COLOR)
        new_row = VGroup(new_label, new_steps).arrange(RIGHT, buff=0.1)
        new_row.move_to(np.array([0, -2.8, 0]))

        faster_text = Text(
            "利用规律，速度更快！",
            font="PingFang SC",
            font_size=26,
            color=GOLD_COLOR,
        ).move_to(np.array([0, -3.6, 0]))

        self.play(FadeIn(compare_bg), Write(compare_title), run_time=0.5)
        self.play(FadeIn(old_row), run_time=0.5)
        self.play(FadeIn(new_row), run_time=0.5)
        self.play(FadeIn(faster_text, scale=1.05), run_time=0.4)
        self.wait(2.0)

        scene4_objects = VGroup(
            sec_title, problem,
            tip_bg, tip_text,
            step_label_1, step1,
            step_label_2, step2,
            step_label_3, step3, hundred_note,
            step_label_4, step4,
            compare_bg, compare_title, old_row, new_row, faster_text,
        )
        self.play(FadeOut(scene4_objects), run_time=0.5)

    # ─────────────────────────────────────────────────────────────────
    # 场景 5 · 总结 + 片尾
    # ─────────────────────────────────────────────────────────────────
    def scene_5_outro(self):
        # ── 总结卡片 ──────────────────────────────────────────────────
        summary_title = Text(
            "今日总结",
            font="PingFang SC",
            font_size=44,
            color=GOLD_COLOR,
        ).move_to(UP * 6.0)

        self.play(Write(summary_title), run_time=0.5)

        # 交换律卡片
        card1_bg = RoundedRectangle(
            width=7.5, height=2.0,
            corner_radius=0.3,
            fill_color="#0f3460",
            fill_opacity=0.95,
            stroke_color=TEAL_COLOR,
            stroke_width=2,
        ).move_to(UP * 4.0)

        card1_name = Text(
            "乘法交换律",
            font="PingFang SC",
            font_size=30,
            color=TEAL_COLOR,
        ).move_to(UP * 4.5)

        card1_formula = MathTex(r"a \times b = b \times a",
                                font_size=36, color=WHITE_TEXT)
        card1_formula.move_to(UP * 3.8)

        card1_desc = Text(
            "交换因数位置，积不变",
            font="PingFang SC",
            font_size=22,
            color=GRAY_TEXT,
        ).move_to(UP * 3.2)

        # 结合律卡片
        card2_bg = RoundedRectangle(
            width=7.5, height=2.3,
            corner_radius=0.3,
            fill_color="#16213e",
            fill_opacity=0.95,
            stroke_color=PURPLE_COLOR,
            stroke_width=2,
        ).move_to(UP * 1.5)

        card2_name = Text(
            "乘法结合律",
            font="PingFang SC",
            font_size=30,
            color=PURPLE_COLOR,
        ).move_to(UP * 2.2)

        card2_formula = MathTex(
            r"(a \times b) \times c = a \times (b \times c)",
            font_size=28, color=WHITE_TEXT,
        )
        card2_formula.move_to(UP * 1.55)

        card2_desc = Text(
            "改变运算顺序，积不变",
            font="PingFang SC",
            font_size=22,
            color=GRAY_TEXT,
        ).move_to(UP * 0.85)

        # 应用提示卡片
        card3_bg = RoundedRectangle(
            width=7.5, height=1.6,
            corner_radius=0.3,
            fill_color="#0f3460",
            fill_opacity=0.95,
            stroke_color=ORANGE_COLOR,
            stroke_width=2,
        ).move_to(DOWN * 0.5)

        card3_name = Text(
            "灵活应用",
            font="PingFang SC",
            font_size=28,
            color=ORANGE_COLOR,
        ).move_to(DOWN * 0.0)

        card3_example = MathTex(
            r"25 \times 4 \times 17 = (25 \times 4) \times 17 = 1700",
            font_size=26, color=GOLD_COLOR,
        )
        card3_example.move_to(DOWN * 0.8)

        # 动画逐个展示
        self.play(
            FadeIn(card1_bg), Write(card1_name), run_time=0.5
        )
        self.play(Write(card1_formula), FadeIn(card1_desc), run_time=0.5)
        self.wait(0.3)
        self.play(
            FadeIn(card2_bg), Write(card2_name), run_time=0.5
        )
        self.play(Write(card2_formula), FadeIn(card2_desc), run_time=0.5)
        self.wait(0.3)
        self.play(
            FadeIn(card3_bg), Write(card3_name), run_time=0.4
        )
        self.play(Write(card3_example), run_time=0.5)
        self.wait(1.5)

        # ── 片尾作者信息 ──────────────────────────────────────────────
        outro_bg = RoundedRectangle(
            width=7.8, height=3.8,
            corner_radius=0.4,
            fill_color="#0a0a1a",
            fill_opacity=0.97,
            stroke_color=GOLD_COLOR,
            stroke_width=2,
        ).move_to(DOWN * 3.5)

        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=32,
            color=WHITE_TEXT,
        ).move_to(DOWN * 2.7)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=26,
            color=TEAL_COLOR,
        ).move_to(DOWN * 3.3)

        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=GOLD_COLOR,
        ).move_to(DOWN * 4.0)

        follow_sub = Text(
            "每天一个知识点，轻松拿满分",
            font="PingFang SC",
            font_size=22,
            color=GRAY_TEXT,
        ).move_to(DOWN * 4.7)

        # 装饰星星
        stars = VGroup(*[
            Star(n=5, outer_radius=0.18, inner_radius=0.08,
                 fill_color=GOLD_COLOR, fill_opacity=1.0,
                 stroke_width=0)
            .move_to(
                DOWN * 5.3 + RIGHT * (-1.5 + i * 0.75)
            )
            for i in range(5)
        ])

        self.play(FadeIn(outro_bg), run_time=0.4)
        self.play(Write(author_name), run_time=0.5)
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(FadeIn(follow_text, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(follow_sub), run_time=0.4)
        self.play(
            *[GrowFromCenter(s) for s in stars],
            run_time=0.6,
        )
        self.wait(2.5)

    # ─────────────────────────────────────────────────────────────────
    # 辅助方法
    # ─────────────────────────────────────────────────────────────────
    def _make_grid(self, rows, cols, cell_color, center):
        """生成 rows×cols 的小方格阵"""
        cell_size = 0.35
        gap = 0.05
        step = cell_size + gap
        grid = VGroup()
        total_w = cols * step - gap
        total_h = rows * step - gap
        origin_x = center[0] - total_w / 2 + cell_size / 2
        origin_y = center[1] + total_h / 2 - cell_size / 2
        for r in range(rows):
            for c in range(cols):
                sq = Square(
                    side_length=cell_size,
                    fill_color=cell_color,
                    fill_opacity=0.8,
                    stroke_color=WHITE,
                    stroke_width=1.5,
                ).move_to(
                    np.array([
                        origin_x + c * step,
                        origin_y - r * step,
                        0,
                    ])
                )
                grid.add(sq)
        return grid

    def _make_factor_box(self, label_str, box_color, pos):
        """创建带标签的因数方框"""
        box = RoundedRectangle(
            width=1.3, height=1.0,
            corner_radius=0.2,
            fill_color=box_color,
            fill_opacity=0.3,
            stroke_color=box_color,
            stroke_width=2.5,
        ).move_to(pos)
        label = MathTex(label_str, font_size=44, color=box_color)
        label.move_to(pos)
        return VGroup(box, label)
