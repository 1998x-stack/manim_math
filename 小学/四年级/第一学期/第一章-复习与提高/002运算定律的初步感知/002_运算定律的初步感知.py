"""
运算定律的初步感知 - Arithmetic Laws Introduction
四年级第一学期 第一章 复习与提高

内容: 加法交换律、加法结合律、乘法交换律、乘法结合律的初步感知
目标观众: 四年级学生
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


class ArithmeticLawsIntroLesson(Scene):
    """
    运算定律的初步感知教学动画

    场景顺序:
    1. 开场钩子
    2. 加法交换律 (a + b = b + a)
    3. 加法结合律 ((a+b)+c = a+(b+c))
    4. 乘法交换律 (a × b = b × a)
    5. 乘法结合律 ((a×b)×c = a×(b×c))
    6. 汇总与片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.C_ADD = "#4fc3f7"       # 加法 - 浅蓝
        self.C_MUL = "#81c784"       # 乘法 - 浅绿
        self.C_COMM = "#ffb74d"      # 交换律 - 橙色
        self.C_ASSOC = "#f48fb1"     # 结合律 - 粉色
        self.C_HIGHLIGHT = "#ffd54f" # 高亮 - 金黄
        self.C_GRAY = "#9e9e9e"      # 灰色辅助

        # 作者标识 (贯穿全程)
        self.author_tag = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.add(self.author_tag)

        # 执行各场景
        self.scene_opening()
        self.scene_add_commutative()
        self.scene_add_associative()
        self.scene_mul_commutative()
        self.scene_mul_associative()
        self.scene_summary()
        self.scene_outro()

    # ─────────────────────────────────────────────
    # 场景 1: 开场钩子
    # ─────────────────────────────────────────────
    def scene_opening(self):
        hook = Text(
            "你知道加法和乘法\n有哪些神奇规律吗?",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.C_HIGHLIGHT,
            line_spacing=1.3,
        ).move_to(UP * 4.5)

        sub = Text(
            "运算定律的初步感知",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE,
        ).move_to(UP * 2.8)

        # 四个小公式卡片作为钩子
        formulas = VGroup(
            MathTex(r"a + b = b + a", font_size=28, color=self.C_ADD),
            MathTex(r"(a+b)+c = a+(b+c)", font_size=28, color=self.C_ADD),
            MathTex(r"a \times b = b \times a", font_size=28, color=self.C_MUL),
            MathTex(r"(a \times b) \times c = a \times (b \times c)", font_size=28, color=self.C_MUL),
        ).arrange(DOWN, buff=0.5).move_to(UP * 0.5)

        self.play(Write(hook), run_time=1.2)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=0.6)
        self.wait(0.4)

        for f in formulas:
            self.play(FadeIn(f, shift=LEFT * 0.3), run_time=0.35)

        self.wait(1.0)

        self.play(
            FadeOut(hook),
            FadeOut(sub),
            FadeOut(formulas),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────
    # 场景 2: 加法交换律
    # ─────────────────────────────────────────────
    def scene_add_commutative(self):
        # 标题
        title = Text("加法交换律", font="Noto Sans CJK SC", font_size=36, color=self.C_ADD)
        title.move_to(UP * 6.2)

        law_label = Text("交换加数的位置，和不变", font="Noto Sans CJK SC",
                         font_size=22, color=self.C_GRAY)
        law_label.move_to(UP * 5.4)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(law_label, shift=UP * 0.2), run_time=0.5)

        # ---- 具体数字示例 ----
        # 用苹果和橘子表示数量
        ex_label = Text("用具体数字感受一下：", font="Noto Sans CJK SC",
                        font_size=24, color=WHITE)
        ex_label.move_to(UP * 4.3)
        self.play(FadeIn(ex_label), run_time=0.4)

        # 左边: 36 + 48
        lhs1 = MathTex(r"36 + 48", font_size=48, color=self.C_ADD)
        eq_sign1 = MathTex(r"=", font_size=48, color=WHITE)
        rhs1 = MathTex(r"84", font_size=48, color=self.C_HIGHLIGHT)
        row1 = VGroup(lhs1, eq_sign1, rhs1).arrange(RIGHT, buff=0.3).move_to(UP * 3.2)

        # 右边: 48 + 36
        lhs2 = MathTex(r"48 + 36", font_size=48, color=self.C_COMM)
        eq_sign2 = MathTex(r"=", font_size=48, color=WHITE)
        rhs2 = MathTex(r"84", font_size=48, color=self.C_HIGHLIGHT)
        row2 = VGroup(lhs2, eq_sign2, rhs2).arrange(RIGHT, buff=0.3).move_to(UP * 2.2)

        self.play(Write(row1), run_time=0.8)
        self.wait(0.3)
        self.play(Write(row2), run_time=0.8)
        self.wait(0.4)

        # 连接两个84，说明相等
        double_arrow = DoubleArrow(
            rhs1.get_bottom() + DOWN * 0.1,
            rhs2.get_top() + UP * 0.1,
            color=self.C_HIGHLIGHT,
            buff=0.05,
            stroke_width=3,
        )
        same_label = Text("相等！", font="Noto Sans CJK SC",
                          font_size=22, color=self.C_HIGHLIGHT)
        same_label.next_to(double_arrow, RIGHT, buff=0.15)

        self.play(Create(double_arrow), FadeIn(same_label), run_time=0.6)
        self.wait(0.5)

        # 发现规律
        discover = Text("发现了什么规律？", font="Noto Sans CJK SC",
                        font_size=26, color=WHITE)
        discover.move_to(UP * 0.8)
        self.play(FadeIn(discover, shift=UP * 0.2), run_time=0.5)
        self.wait(0.6)

        # 结论框
        conclusion_bg = Rectangle(
            width=7.5, height=1.3,
            fill_color="#1e3a5f", fill_opacity=0.9,
            stroke_color=self.C_ADD, stroke_width=2,
        ).move_to(DOWN * 0.2)

        formula_comm = MathTex(r"a + b = b + a", font_size=44, color=self.C_HIGHLIGHT)
        formula_comm.move_to(DOWN * 0.2)

        self.play(Create(conclusion_bg), run_time=0.4)
        self.play(Write(formula_comm), run_time=0.8)

        # 高亮：左边a→右边b，左边b→右边a
        self.play(
            Indicate(formula_comm[0][0], color=self.C_COMM, scale_factor=1.5),
            run_time=0.5,
        )
        self.play(
            Indicate(formula_comm[0][4], color=self.C_COMM, scale_factor=1.5),
            run_time=0.5,
        )

        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title), FadeOut(law_label), FadeOut(ex_label),
            FadeOut(row1), FadeOut(row2),
            FadeOut(double_arrow), FadeOut(same_label),
            FadeOut(discover), FadeOut(conclusion_bg), FadeOut(formula_comm),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────
    # 场景 3: 加法结合律
    # ─────────────────────────────────────────────
    def scene_add_associative(self):
        title = Text("加法结合律", font="Noto Sans CJK SC", font_size=36, color=self.C_ADD)
        title.move_to(UP * 6.2)

        law_label = Text("先加哪两个数，和不变", font="Noto Sans CJK SC",
                         font_size=22, color=self.C_GRAY)
        law_label.move_to(UP * 5.4)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(law_label, shift=UP * 0.2), run_time=0.5)

        # 具体例子: 25 + 46 + 75
        ex_label = Text("计算 25 + 46 + 75，怎么简便？", font="Noto Sans CJK SC",
                        font_size=24, color=WHITE)
        ex_label.move_to(UP * 4.3)
        self.play(FadeIn(ex_label), run_time=0.4)

        # 方法一: (25 + 46) + 75
        label_m1 = Text("方法一：按顺序计算", font="Noto Sans CJK SC",
                        font_size=20, color=self.C_GRAY)
        label_m1.move_to(UP * 3.5)

        m1_step1 = MathTex(r"(25 + 46) + 75", font_size=40, color=self.C_ADD)
        m1_eq1 = MathTex(r"= 71 + 75", font_size=40, color=WHITE)
        m1_eq2 = MathTex(r"= 146", font_size=40, color=self.C_HIGHLIGHT)

        m1_group = VGroup(m1_step1, m1_eq1, m1_eq2).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        m1_group.move_to(UP * 2.2)

        self.play(FadeIn(label_m1), run_time=0.3)
        self.play(Write(m1_step1), run_time=0.6)
        self.play(Write(m1_eq1), run_time=0.5)
        self.play(Write(m1_eq2), run_time=0.5)
        self.wait(0.4)

        # 方法二: 25 + (46 + 75)  — 更简便
        label_m2 = Text("方法二：换个顺序（更简便！）", font="Noto Sans CJK SC",
                        font_size=20, color=self.C_COMM)
        label_m2.move_to(UP * 0.5)

        m2_step1 = MathTex(r"25 + (46 + 75)", font_size=40, color=self.C_COMM)
        m2_eq1 = MathTex(r"= 25 + 121", font_size=40, color=WHITE)
        m2_eq2 = MathTex(r"= 146", font_size=40, color=self.C_HIGHLIGHT)

        m2_group = VGroup(m2_step1, m2_eq1, m2_eq2).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        m2_group.move_to(DOWN * 0.8)

        self.play(FadeIn(label_m2), run_time=0.3)
        self.play(Write(m2_step1), run_time=0.6)
        self.play(Write(m2_eq1), run_time=0.5)
        self.play(Write(m2_eq2), run_time=0.5)
        self.wait(0.5)

        # 两个结果都是146
        result_note = Text("两种方法，结果相同！", font="Noto Sans CJK SC",
                           font_size=24, color=self.C_HIGHLIGHT)
        result_note.move_to(DOWN * 2.2)
        self.play(FadeIn(result_note, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 结论公式框
        conclusion_bg = Rectangle(
            width=8.2, height=1.4,
            fill_color="#1e3a5f", fill_opacity=0.9,
            stroke_color=self.C_ADD, stroke_width=2,
        ).move_to(DOWN * 3.4)

        formula_assoc = MathTex(r"(a+b)+c = a+(b+c)", font_size=38, color=self.C_HIGHLIGHT)
        formula_assoc.move_to(DOWN * 3.4)

        self.play(Create(conclusion_bg), run_time=0.4)
        self.play(Write(formula_assoc), run_time=0.9)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title), FadeOut(law_label), FadeOut(ex_label),
            FadeOut(label_m1), FadeOut(m1_group),
            FadeOut(label_m2), FadeOut(m2_group),
            FadeOut(result_note), FadeOut(conclusion_bg), FadeOut(formula_assoc),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────
    # 场景 4: 乘法交换律
    # ─────────────────────────────────────────────
    def scene_mul_commutative(self):
        title = Text("乘法交换律", font="Noto Sans CJK SC", font_size=36, color=self.C_MUL)
        title.move_to(UP * 6.2)

        law_label = Text("交换因数的位置，积不变", font="Noto Sans CJK SC",
                         font_size=22, color=self.C_GRAY)
        law_label.move_to(UP * 5.4)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(law_label, shift=UP * 0.2), run_time=0.5)

        # 可视化：矩形点阵
        # 4行×6列 = 6行×4列
        grid_label = Text("用点阵图来感受：", font="Noto Sans CJK SC",
                          font_size=24, color=WHITE)
        grid_label.move_to(UP * 4.5)
        self.play(FadeIn(grid_label), run_time=0.4)

        # 绘制 4×6 点阵
        rows1, cols1 = 4, 6
        dot_spacing = 0.38
        grid1_offset = np.array([-2.2, 2.4, 0])

        dots1 = VGroup()
        for r in range(rows1):
            for c in range(cols1):
                d = Dot(
                    point=grid1_offset + np.array([c * dot_spacing, -r * dot_spacing, 0]),
                    radius=0.12,
                    color=self.C_MUL,
                )
                dots1.add(d)

        label1_row = Text("4 行", font="Noto Sans CJK SC", font_size=18, color=self.C_MUL)
        label1_col = Text("6 列", font="Noto Sans CJK SC", font_size=18, color=self.C_MUL)
        label1_row.next_to(dots1, LEFT, buff=0.2)
        label1_col.next_to(dots1, UP, buff=0.15)

        formula1 = MathTex(r"4 \times 6 = 24", font_size=36, color=self.C_MUL)
        formula1.move_to(grid1_offset + np.array([1.0, -2.0, 0]))

        self.play(Create(dots1), run_time=0.8)
        self.play(FadeIn(label1_row), FadeIn(label1_col), run_time=0.4)
        self.play(Write(formula1), run_time=0.5)
        self.wait(0.4)

        # 绘制 6×4 点阵
        rows2, cols2 = 6, 4
        grid2_offset = np.array([1.8, 2.4, 0])

        dots2 = VGroup()
        for r in range(rows2):
            for c in range(cols2):
                d = Dot(
                    point=grid2_offset + np.array([c * dot_spacing, -r * dot_spacing, 0]),
                    radius=0.12,
                    color=self.C_COMM,
                )
                dots2.add(d)

        label2_row = Text("6 行", font="Noto Sans CJK SC", font_size=18, color=self.C_COMM)
        label2_col = Text("4 列", font="Noto Sans CJK SC", font_size=18, color=self.C_COMM)
        label2_row.next_to(dots2, LEFT, buff=0.2)
        label2_col.next_to(dots2, UP, buff=0.15)

        formula2 = MathTex(r"6 \times 4 = 24", font_size=36, color=self.C_COMM)
        formula2.move_to(grid2_offset + np.array([0.6, -2.8, 0]))

        self.play(Create(dots2), run_time=0.8)
        self.play(FadeIn(label2_row), FadeIn(label2_col), run_time=0.4)
        self.play(Write(formula2), run_time=0.5)
        self.wait(0.3)

        # 点数相同
        equal_note = Text("点的总数相同！", font="Noto Sans CJK SC",
                          font_size=26, color=self.C_HIGHLIGHT)
        equal_note.move_to(DOWN * 0.7)
        self.play(FadeIn(equal_note, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 结论框
        conclusion_bg = Rectangle(
            width=7.5, height=1.3,
            fill_color="#1a3325", fill_opacity=0.9,
            stroke_color=self.C_MUL, stroke_width=2,
        ).move_to(DOWN * 2.0)

        formula_mc = MathTex(r"a \times b = b \times a", font_size=44, color=self.C_HIGHLIGHT)
        formula_mc.move_to(DOWN * 2.0)

        self.play(Create(conclusion_bg), run_time=0.4)
        self.play(Write(formula_mc), run_time=0.8)

        self.play(
            Indicate(formula_mc[0][0], color=self.C_MUL, scale_factor=1.5),
            run_time=0.5,
        )
        self.play(
            Indicate(formula_mc[0][4], color=self.C_COMM, scale_factor=1.5),
            run_time=0.5,
        )

        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title), FadeOut(law_label), FadeOut(grid_label),
            FadeOut(dots1), FadeOut(label1_row), FadeOut(label1_col), FadeOut(formula1),
            FadeOut(dots2), FadeOut(label2_row), FadeOut(label2_col), FadeOut(formula2),
            FadeOut(equal_note), FadeOut(conclusion_bg), FadeOut(formula_mc),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────
    # 场景 5: 乘法结合律
    # ─────────────────────────────────────────────
    def scene_mul_associative(self):
        title = Text("乘法结合律", font="Noto Sans CJK SC", font_size=36, color=self.C_MUL)
        title.move_to(UP * 6.2)

        law_label = Text("先乘哪两个数，积不变", font="Noto Sans CJK SC",
                         font_size=22, color=self.C_GRAY)
        law_label.move_to(UP * 5.4)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(law_label, shift=UP * 0.2), run_time=0.5)

        # 具体例子: 2 × 5 × 8
        ex_label = Text("计算 2 × 5 × 8，哪种更快？", font="Noto Sans CJK SC",
                        font_size=24, color=WHITE)
        ex_label.move_to(UP * 4.5)
        self.play(FadeIn(ex_label), run_time=0.4)

        # 方法一: (2 × 5) × 8
        label_m1 = Text("方法一：", font="Noto Sans CJK SC",
                        font_size=22, color=self.C_GRAY)
        label_m1.move_to(LEFT * 2.8 + UP * 3.5)

        m1_step1 = MathTex(r"(2 \times 5) \times 8", font_size=38, color=self.C_MUL)
        m1_eq1 = MathTex(r"= 10 \times 8", font_size=38, color=WHITE)
        m1_eq2 = MathTex(r"= 80", font_size=38, color=self.C_HIGHLIGHT)
        m1_group = VGroup(m1_step1, m1_eq1, m1_eq2).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        m1_group.move_to(UP * 2.2)

        self.play(FadeIn(label_m1), run_time=0.3)
        self.play(Write(m1_step1), run_time=0.6)
        self.play(Write(m1_eq1), run_time=0.5)
        self.play(Write(m1_eq2), run_time=0.5)
        self.wait(0.4)

        # 方法二: 2 × (5 × 8)
        label_m2 = Text("方法二：", font="Noto Sans CJK SC",
                        font_size=22, color=self.C_COMM)
        label_m2.move_to(LEFT * 2.8 + UP * 0.5)

        m2_step1 = MathTex(r"2 \times (5 \times 8)", font_size=38, color=self.C_COMM)
        m2_eq1 = MathTex(r"= 2 \times 40", font_size=38, color=WHITE)
        m2_eq2 = MathTex(r"= 80", font_size=38, color=self.C_HIGHLIGHT)
        m2_group = VGroup(m2_step1, m2_eq1, m2_eq2).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        m2_group.move_to(DOWN * 0.8)

        self.play(FadeIn(label_m2), run_time=0.3)
        self.play(Write(m2_step1), run_time=0.6)
        self.play(Write(m2_eq1), run_time=0.5)
        self.play(Write(m2_eq2), run_time=0.5)
        self.wait(0.4)

        result_note = Text("先算 2×5=10 或先算 5×8=40，结果一样！",
                           font="Noto Sans CJK SC", font_size=20, color=self.C_HIGHLIGHT)
        result_note.move_to(DOWN * 2.4)
        self.play(FadeIn(result_note, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 结论框
        conclusion_bg = Rectangle(
            width=8.8, height=1.4,
            fill_color="#1a3325", fill_opacity=0.9,
            stroke_color=self.C_MUL, stroke_width=2,
        ).move_to(DOWN * 3.5)

        formula_ma = MathTex(
            r"(a \times b) \times c = a \times (b \times c)",
            font_size=34,
            color=self.C_HIGHLIGHT,
        )
        formula_ma.move_to(DOWN * 3.5)

        self.play(Create(conclusion_bg), run_time=0.4)
        self.play(Write(formula_ma), run_time=1.0)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title), FadeOut(law_label), FadeOut(ex_label),
            FadeOut(label_m1), FadeOut(m1_group),
            FadeOut(label_m2), FadeOut(m2_group),
            FadeOut(result_note), FadeOut(conclusion_bg), FadeOut(formula_ma),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────
    # 场景 6: 汇总
    # ─────────────────────────────────────────────
    def scene_summary(self):
        summary_title = Text("四大运算定律", font="Noto Sans CJK SC",
                             font_size=38, color=self.C_HIGHLIGHT)
        summary_title.move_to(UP * 6.5)
        self.play(Write(summary_title), run_time=0.7)

        # 四张卡片
        card_data = [
            ("加法交换律", r"a + b = b + a", self.C_ADD),
            ("加法结合律", r"(a+b)+c = a+(b+c)", self.C_ADD),
            ("乘法交换律", r"a \times b = b \times a", self.C_MUL),
            ("乘法结合律", r"(a \times b) \times c = a \times (b \times c)", self.C_MUL),
        ]

        card_positions = [
            UP * 4.8,
            UP * 2.8,
            UP * 0.8,
            DOWN * 1.2,
        ]

        cards = []
        for (name, formula_str, color), pos in zip(card_data, card_positions):
            bg = Rectangle(
                width=8.0, height=1.5,
                fill_color="#16213e", fill_opacity=0.95,
                stroke_color=color, stroke_width=2,
            ).move_to(pos)

            name_text = Text(name, font="Noto Sans CJK SC",
                             font_size=22, color=color)
            formula_obj = MathTex(formula_str, font_size=30, color=WHITE)

            content = VGroup(name_text, formula_obj).arrange(RIGHT, buff=0.4)
            content.move_to(pos)

            card_group = VGroup(bg, content)
            cards.append(card_group)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.45)

        self.wait(0.5)

        # 记忆口诀
        tip_bg = Rectangle(
            width=8.2, height=1.8,
            fill_color="#2d1b4e", fill_opacity=0.95,
            stroke_color=self.C_HIGHLIGHT, stroke_width=2,
        ).move_to(DOWN * 3.2)

        tip_line1 = Text("加法和乘法各有", font="Noto Sans CJK SC",
                         font_size=22, color=WHITE)
        tip_line2 = Text("交换律 和 结合律", font="Noto Sans CJK SC",
                         font_size=24, color=self.C_HIGHLIGHT)
        tip_line3 = Text("帮助我们简便计算！", font="Noto Sans CJK SC",
                         font_size=22, color=WHITE)
        tip_content = VGroup(tip_line1, tip_line2, tip_line3).arrange(DOWN, buff=0.15)
        tip_content.move_to(DOWN * 3.2)

        self.play(Create(tip_bg), run_time=0.4)
        self.play(FadeIn(tip_content), run_time=0.6)
        self.wait(1.5)

        # 指示所有四个公式
        for card in cards:
            self.play(Indicate(card[0], color=self.C_HIGHLIGHT, scale_factor=1.04), run_time=0.35)

        self.wait(0.8)

        self.play(
            *[FadeOut(c) for c in cards],
            FadeOut(summary_title),
            FadeOut(tip_bg),
            FadeOut(tip_content),
            run_time=0.7,
        )

    # ─────────────────────────────────────────────
    # 场景 7: 片尾
    # ─────────────────────────────────────────────
    def scene_outro(self):
        # 大字作者信息
        author_big = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE,
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.C_GRAY,
        ).move_to(UP * 1.2)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.C_HIGHLIGHT,
        ).move_to(UP * 0.1)

        # 四条彩色横线装饰
        lines = VGroup(
            Line(LEFT * 3.5, RIGHT * 3.5, color=self.C_ADD, stroke_width=3).move_to(DOWN * 0.9),
            Line(LEFT * 3.0, RIGHT * 3.0, color=self.C_MUL, stroke_width=3).move_to(DOWN * 1.3),
            Line(LEFT * 2.0, RIGHT * 2.0, color=self.C_COMM, stroke_width=3).move_to(DOWN * 1.7),
            Line(LEFT * 1.0, RIGHT * 1.0, color=self.C_ASSOC, stroke_width=3).move_to(DOWN * 2.1),
        )

        # 四个结论公式小字
        mini_formulas = VGroup(
            MathTex(r"a+b=b+a", font_size=22, color=self.C_ADD),
            MathTex(r"(a+b)+c=a+(b+c)", font_size=20, color=self.C_ADD),
            MathTex(r"a \times b=b \times a", font_size=22, color=self.C_MUL),
            MathTex(r"(a \times b) \times c=a \times (b \times c)", font_size=19, color=self.C_MUL),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 4.0)

        self.play(
            FadeIn(author_big, shift=UP * 0.4),
            run_time=0.7,
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.5)
        self.play(Create(lines), run_time=0.6)
        self.play(FadeIn(mini_formulas), run_time=0.7)
        self.wait(2.0)

        self.play(
            FadeOut(author_big), FadeOut(author_id), FadeOut(follow_text),
            FadeOut(lines), FadeOut(mini_formulas),
            run_time=0.8,
        )
