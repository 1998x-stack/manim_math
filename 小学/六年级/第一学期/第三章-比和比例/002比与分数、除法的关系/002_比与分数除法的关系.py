"""
002_比与分数除法的关系.py — 比与分数、除法的关系 教学动画

知识点: 比与分数、除法的关系
  - 关系式: a:b = a / b = a/b (b != 0)
  - 区别: 比是关系, 除法是运算, 分数是数
  - 各部分名称对应
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
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
COLOR_RATIO = "#3b82f6"       # 蓝色 — 比
COLOR_DIV = "#f59e0b"         # 橙色 — 除法
COLOR_FRAC = "#22c55e"        # 绿色 — 分数
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_ACCENT = "#a78bfa"      # 紫色强调
COLOR_RED = "#ef4444"         # 红色
COLOR_AUTHOR = "#6b7280"      # 灰色作者信息
COLOR_FORMULA = "#38bdf8"     # 天蓝色 公式
COLOR_PINK = "#f472b6"        # 粉色
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class RatioFractionDivisionLesson(Scene):
    """
    比与分数、除法的关系 教学动画

    场景顺序:
      1. 开场钩子
      2. 三者的概念回顾
      3. 核心关系式 a:b = a / b = a/b
      4. 各部分名称对照表
      5. 具体例子验证
      6. 三者的区别
      7. 注意事项 (b != 0)
      8. 总结
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_review()
        self.scene_3_core_relation()
        self.scene_4_name_table()
        self.scene_5_example()
        self.scene_6_differences()
        self.scene_7_warning()
        self.scene_8_summary()
        self.scene_9_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        # 作者信息
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook1 = Text(
            "比、分数、除法", font=FONT, font_size=44, color=WHITE
        ).move_to(UP * 4.5)
        hook2 = Text(
            "它们之间有什么关系?", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 3.3)

        self.play(Write(hook1), run_time=0.8)
        self.play(Write(hook2), run_time=0.8)
        self.wait(0.5)

        # 三个概念圆
        circle_ratio = Circle(
            radius=1.1, color=COLOR_RATIO, stroke_width=3, fill_opacity=0.15
        ).move_to(LEFT * 2.5 + UP * 0.5)
        label_ratio = Text(
            "比", font=FONT, font_size=36, color=COLOR_RATIO
        ).move_to(circle_ratio.get_center())
        ex_ratio = MathTex(r"a : b", font_size=28, color=COLOR_RATIO).next_to(
            circle_ratio, DOWN, buff=0.2
        )

        circle_div = Circle(
            radius=1.1, color=COLOR_DIV, stroke_width=3, fill_opacity=0.15
        ).move_to(RIGHT * 2.5 + UP * 0.5)
        label_div = Text(
            "除法", font=FONT, font_size=36, color=COLOR_DIV
        ).move_to(circle_div.get_center())
        ex_div = MathTex(r"a \div b", font_size=28, color=COLOR_DIV).next_to(
            circle_div, DOWN, buff=0.2
        )

        circle_frac = Circle(
            radius=1.1, color=COLOR_FRAC, stroke_width=3, fill_opacity=0.15
        ).move_to(DOWN * 2.5)
        label_frac = Text(
            "分数", font=FONT, font_size=36, color=COLOR_FRAC
        ).move_to(circle_frac.get_center())
        ex_frac = MathTex(r"\frac{a}{b}", font_size=28, color=COLOR_FRAC).next_to(
            circle_frac, DOWN, buff=0.2
        )

        self.play(
            FadeIn(circle_ratio), FadeIn(label_ratio), FadeIn(ex_ratio),
            FadeIn(circle_div), FadeIn(label_div), FadeIn(ex_div),
            FadeIn(circle_frac), FadeIn(label_frac), FadeIn(ex_frac),
            run_time=1.0
        )
        self.wait(0.5)

        # 连接线
        line1 = Line(circle_ratio.get_right(), circle_div.get_left(), color=COLOR_HL, stroke_width=2)
        line2 = Line(circle_ratio.get_bottom() + DOWN * 0.15, circle_frac.get_left() + UP * 0.15, color=COLOR_HL, stroke_width=2)
        line3 = Line(circle_div.get_bottom() + DOWN * 0.15, circle_frac.get_right() + UP * 0.15, color=COLOR_HL, stroke_width=2)

        eq_sign = MathTex(r"=", font_size=32, color=COLOR_HL).move_to(
            (circle_ratio.get_center() + circle_div.get_center()) / 2 + UP * 0.6
        )

        self.play(
            Create(line1), Create(line2), Create(line3),
            FadeIn(eq_sign),
            run_time=0.8
        )

        question = Text(
            "三胞胎?", font=FONT, font_size=32, color=COLOR_PINK
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(question, scale=1.2), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook1), FadeOut(hook2),
            FadeOut(circle_ratio), FadeOut(label_ratio), FadeOut(ex_ratio),
            FadeOut(circle_div), FadeOut(label_div), FadeOut(ex_div),
            FadeOut(circle_frac), FadeOut(label_frac), FadeOut(ex_frac),
            FadeOut(line1), FadeOut(line2), FadeOut(line3),
            FadeOut(eq_sign), FadeOut(question),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 2: 三者的概念回顾
    # ------------------------------------------------------------------
    def scene_2_review(self):
        title = Text(
            "先来回顾", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 比的概念
        r_title = Text("比", font=FONT, font_size=30, color=COLOR_RATIO)
        r_desc = Text(
            "两个数的关系", font=FONT, font_size=22, color=GRAY_A
        )
        r_ex = MathTex(r"3 : 5", font_size=32, color=COLOR_RATIO)
        r_group = VGroup(r_title, r_desc, r_ex).arrange(DOWN, buff=0.2).move_to(UP * 3.8)

        r_box = RoundedRectangle(
            width=6, height=1.8, corner_radius=0.2,
            color=COLOR_RATIO, stroke_width=2, fill_opacity=0.05
        ).move_to(r_group.get_center())

        self.play(FadeIn(r_box), FadeIn(r_group), run_time=0.8)
        self.wait(0.3)

        # 除法的概念
        d_title = Text("除法", font=FONT, font_size=30, color=COLOR_DIV)
        d_desc = Text(
            "一种运算", font=FONT, font_size=22, color=GRAY_A
        )
        d_ex = MathTex(r"3 \div 5 = 0.6", font_size=32, color=COLOR_DIV)
        d_group = VGroup(d_title, d_desc, d_ex).arrange(DOWN, buff=0.2).move_to(UP * 1.0)

        d_box = RoundedRectangle(
            width=6, height=1.8, corner_radius=0.2,
            color=COLOR_DIV, stroke_width=2, fill_opacity=0.05
        ).move_to(d_group.get_center())

        self.play(FadeIn(d_box), FadeIn(d_group), run_time=0.8)
        self.wait(0.3)

        # 分数的概念
        f_title = Text("分数", font=FONT, font_size=30, color=COLOR_FRAC)
        f_desc = Text(
            "一个数", font=FONT, font_size=22, color=GRAY_A
        )
        f_ex = MathTex(r"\frac{3}{5}", font_size=36, color=COLOR_FRAC)
        f_group = VGroup(f_title, f_desc, f_ex).arrange(DOWN, buff=0.2).move_to(DOWN * 1.8)

        f_box = RoundedRectangle(
            width=6, height=1.8, corner_radius=0.2,
            color=COLOR_FRAC, stroke_width=2, fill_opacity=0.05
        ).move_to(f_group.get_center())

        self.play(FadeIn(f_box), FadeIn(f_group), run_time=0.8)
        self.wait(0.5)

        # 引导文字
        lead = Text(
            "看起来很不一样...", font=FONT, font_size=26, color=GRAY_A
        ).move_to(DOWN * 4.0)
        lead2 = Text(
            "但它们有紧密的联系!", font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 5.0)

        self.play(FadeIn(lead), run_time=0.5)
        self.play(FadeIn(lead2, shift=UP * 0.2), run_time=0.6)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(r_box), FadeOut(r_group),
            FadeOut(d_box), FadeOut(d_group),
            FadeOut(f_box), FadeOut(f_group),
            FadeOut(lead), FadeOut(lead2),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 3: 核心关系式
    # ------------------------------------------------------------------
    def scene_3_core_relation(self):
        title = Text(
            "核心关系", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 逐步展示公式
        part_ratio = MathTex(r"a : b", font_size=48, color=COLOR_RATIO)
        part_eq1 = MathTex(r"=", font_size=48, color=WHITE)
        part_div = MathTex(r"a \div b", font_size=48, color=COLOR_DIV)
        part_eq2 = MathTex(r"=", font_size=48, color=WHITE)
        part_frac = MathTex(r"\frac{a}{b}", font_size=48, color=COLOR_FRAC)

        # 先显示比
        part_ratio.move_to(UP * 4.0)
        self.play(Write(part_ratio), run_time=0.8)

        label_r = Text("比", font=FONT, font_size=20, color=COLOR_RATIO).next_to(
            part_ratio, DOWN, buff=0.2
        )
        self.play(FadeIn(label_r), run_time=0.3)
        self.wait(0.3)

        # 等号 + 除法
        part_eq1.next_to(part_ratio, RIGHT, buff=0.3)
        part_div.next_to(part_eq1, RIGHT, buff=0.3)
        self.play(Write(part_eq1), Write(part_div), run_time=0.8)

        label_d = Text("除法", font=FONT, font_size=20, color=COLOR_DIV).next_to(
            part_div, DOWN, buff=0.2
        )
        self.play(FadeIn(label_d), run_time=0.3)
        self.wait(0.3)

        # 整体居中调整
        formula_top = VGroup(part_ratio, part_eq1, part_div)

        # 第二行: = 分数
        part_eq2.move_to(UP * 2.0 + LEFT * 1.0)
        part_frac.next_to(part_eq2, RIGHT, buff=0.3)

        self.play(Write(part_eq2), Write(part_frac), run_time=0.8)

        label_f = Text("分数", font=FONT, font_size=20, color=COLOR_FRAC).next_to(
            part_frac, DOWN, buff=0.2
        )
        self.play(FadeIn(label_f), run_time=0.3)
        self.wait(0.5)

        # 条件
        condition = VGroup(
            MathTex(r"(", font_size=32, color=WHITE),
            MathTex(r"b \neq 0", font_size=32, color=COLOR_RED),
            MathTex(r")", font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=0.08).move_to(UP * 0.5)

        self.play(FadeIn(condition, scale=1.2), run_time=0.6)
        self.wait(0.5)

        # 高亮框
        all_formula = VGroup(
            part_ratio, part_eq1, part_div,
            part_eq2, part_frac, condition
        )
        highlight_box = SurroundingRectangle(
            all_formula, color=COLOR_HL, buff=0.4, corner_radius=0.2
        )
        self.play(Create(highlight_box), run_time=0.6)

        # 底部说明
        note = Text(
            "这就是比、除法、分数的关系!", font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(note, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(part_ratio), FadeOut(part_eq1), FadeOut(part_div),
            FadeOut(part_eq2), FadeOut(part_frac),
            FadeOut(label_r), FadeOut(label_d), FadeOut(label_f),
            FadeOut(condition), FadeOut(highlight_box), FadeOut(note),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 4: 各部分名称对照表
    # ------------------------------------------------------------------
    def scene_4_name_table(self):
        title = Text(
            "名称对照", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 表头
        header_y = 4.5
        col_x = [-2.8, 0, 2.8]
        header_texts = ["比", "除法", "分数"]
        header_colors = [COLOR_RATIO, COLOR_DIV, COLOR_FRAC]
        headers = []
        for i, (txt, clr) in enumerate(zip(header_texts, header_colors)):
            h = Text(txt, font=FONT, font_size=28, color=clr).move_to(
                np.array([col_x[i], header_y, 0])
            )
            headers.append(h)

        header_line = Line(
            LEFT * 4 + UP * (header_y - 0.4),
            RIGHT * 4 + UP * (header_y - 0.4),
            color=GRAY_B, stroke_width=1.5
        )

        self.play(*[FadeIn(h) for h in headers], Create(header_line), run_time=0.6)

        # 表格行
        row_data = [
            ("前项", "被除数", "分子", "a"),
            ("比号 (:)", "除号 (/)", "分数线 (--)", ""),
            ("后项", "除数", "分母", "b"),
            ("比值", "商", "分数值", ""),
        ]

        rows = []
        for r_idx, (c1, c2, c3, math_note) in enumerate(row_data):
            y = header_y - 1.2 - r_idx * 1.3
            t1 = Text(c1, font=FONT, font_size=22, color=COLOR_RATIO).move_to(
                np.array([col_x[0], y, 0])
            )
            t2 = Text(c2, font=FONT, font_size=22, color=COLOR_DIV).move_to(
                np.array([col_x[1], y, 0])
            )
            t3 = Text(c3, font=FONT, font_size=22, color=COLOR_FRAC).move_to(
                np.array([col_x[2], y, 0])
            )

            row_group = VGroup(t1, t2, t3)

            # 对应箭头
            arrow1 = MathTex(r"\leftrightarrow", font_size=22, color=GRAY_B).move_to(
                np.array([(col_x[0] + col_x[1]) / 2, y, 0])
            )
            arrow2 = MathTex(r"\leftrightarrow", font_size=22, color=GRAY_B).move_to(
                np.array([(col_x[1] + col_x[2]) / 2, y, 0])
            )

            row_all = VGroup(row_group, arrow1, arrow2)
            rows.append(row_all)

        # 逐行显示
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.6)
            self.wait(0.3)

        # 底部示意公式
        demo_formula = VGroup(
            MathTex(r"a", font_size=36, color=COLOR_RATIO),
            MathTex(r":", font_size=36, color=GRAY_A),
            MathTex(r"b", font_size=36, color=COLOR_RATIO),
            MathTex(r"=", font_size=36, color=WHITE),
            MathTex(r"a", font_size=36, color=COLOR_DIV),
            MathTex(r"\div", font_size=36, color=GRAY_A),
            MathTex(r"b", font_size=36, color=COLOR_DIV),
            MathTex(r"=", font_size=36, color=WHITE),
            MathTex(r"\frac{a}{b}", font_size=36, color=COLOR_FRAC),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 4.5)

        self.play(FadeIn(demo_formula, shift=UP * 0.3), run_time=0.8)
        self.wait(2.0)

        # 清理
        all_rows = VGroup(*rows)
        self.play(
            FadeOut(title), FadeOut(header_line),
            *[FadeOut(h) for h in headers],
            FadeOut(all_rows), FadeOut(demo_formula),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 5: 具体例子验证
    # ------------------------------------------------------------------
    def scene_5_example(self):
        title = Text(
            "举例验证", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 例子 1: 3:4
        ex_label = Text(
            "例1:", font=FONT, font_size=24, color=COLOR_ACCENT
        ).move_to(UP * 4.8 + LEFT * 3)

        ex_ratio = MathTex(r"3 : 4", font_size=40, color=COLOR_RATIO).move_to(UP * 3.8)
        self.play(FadeIn(ex_label), Write(ex_ratio), run_time=0.6)

        eq1 = MathTex(r"= 3 \div 4", font_size=36, color=COLOR_DIV).move_to(UP * 2.6)
        self.play(Write(eq1), run_time=0.6)

        eq2 = MathTex(r"= \frac{3}{4}", font_size=40, color=COLOR_FRAC).move_to(UP * 1.3)
        self.play(Write(eq2), run_time=0.6)

        eq3 = MathTex(r"= 0.75", font_size=36, color=WHITE).move_to(UP * 0.2)
        self.play(Write(eq3), run_time=0.6)

        check = Text(
            "三者结果一样!", font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(check, scale=1.1), run_time=0.5)
        self.wait(0.8)

        # 例子 2: 2:5
        ex_label2 = Text(
            "例2:", font=FONT, font_size=24, color=COLOR_ACCENT
        ).move_to(DOWN * 2.0 + LEFT * 3)

        ex2_line = VGroup(
            MathTex(r"2 : 5", font_size=36, color=COLOR_RATIO),
            MathTex(r"=", font_size=36, color=WHITE),
            MathTex(r"2 \div 5", font_size=36, color=COLOR_DIV),
            MathTex(r"=", font_size=36, color=WHITE),
            MathTex(r"\frac{2}{5}", font_size=40, color=COLOR_FRAC),
            MathTex(r"=", font_size=36, color=WHITE),
            MathTex(r"0.4", font_size=36, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 3.2)

        self.play(FadeIn(ex_label2), FadeIn(ex2_line), run_time=0.8)
        self.wait(0.5)

        confirm = Text(
            "比 = 除法 = 分数", font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 5.0)
        self.play(Write(confirm), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(ex_label), FadeOut(ex_ratio),
            FadeOut(eq1), FadeOut(eq2), FadeOut(eq3), FadeOut(check),
            FadeOut(ex_label2), FadeOut(ex2_line), FadeOut(confirm),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 6: 三者的区别
    # ------------------------------------------------------------------
    def scene_6_differences(self):
        title = Text(
            "联系 vs 区别", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        subtitle = Text(
            "虽然三者可以互相转化, 但本质不同",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 5.0)
        self.play(FadeIn(subtitle), run_time=0.5)

        # 比 — 关系
        card1_bg = RoundedRectangle(
            width=7.5, height=2.2, corner_radius=0.2,
            color=COLOR_RATIO, stroke_width=2, fill_opacity=0.08
        ).move_to(UP * 3.0)

        card1_icon = Circle(
            radius=0.3, color=COLOR_RATIO, fill_opacity=0.9, stroke_width=0
        ).move_to(card1_bg.get_left() + RIGHT * 0.6)
        card1_icon_text = Text(
            "比", font=FONT, font_size=22, color=WHITE
        ).move_to(card1_icon.get_center())

        card1_title = Text(
            "表示两个数的关系", font=FONT, font_size=24, color=WHITE
        ).move_to(card1_bg.get_center() + UP * 0.3 + RIGHT * 0.3)
        card1_detail = Text(
            "前项、比号、后项", font=FONT, font_size=18, color=GRAY_A
        ).move_to(card1_bg.get_center() + DOWN * 0.3 + RIGHT * 0.3)

        card1 = VGroup(card1_bg, card1_icon, card1_icon_text, card1_title, card1_detail)
        self.play(FadeIn(card1, shift=RIGHT * 0.5), run_time=0.7)
        self.wait(0.3)

        # 除法 — 运算
        card2_bg = RoundedRectangle(
            width=7.5, height=2.2, corner_radius=0.2,
            color=COLOR_DIV, stroke_width=2, fill_opacity=0.08
        ).move_to(UP * 0.3)

        card2_icon = Circle(
            radius=0.3, color=COLOR_DIV, fill_opacity=0.9, stroke_width=0
        ).move_to(card2_bg.get_left() + RIGHT * 0.6)
        card2_icon_text = Text(
            "除", font=FONT, font_size=22, color=WHITE
        ).move_to(card2_icon.get_center())

        card2_title = Text(
            "一种运算", font=FONT, font_size=24, color=WHITE
        ).move_to(card2_bg.get_center() + UP * 0.3 + RIGHT * 0.3)
        card2_detail = Text(
            "被除数、除号、除数、商", font=FONT, font_size=18, color=GRAY_A
        ).move_to(card2_bg.get_center() + DOWN * 0.3 + RIGHT * 0.3)

        card2 = VGroup(card2_bg, card2_icon, card2_icon_text, card2_title, card2_detail)
        self.play(FadeIn(card2, shift=RIGHT * 0.5), run_time=0.7)
        self.wait(0.3)

        # 分数 — 数
        card3_bg = RoundedRectangle(
            width=7.5, height=2.2, corner_radius=0.2,
            color=COLOR_FRAC, stroke_width=2, fill_opacity=0.08
        ).move_to(DOWN * 2.4)

        card3_icon = Circle(
            radius=0.3, color=COLOR_FRAC, fill_opacity=0.9, stroke_width=0
        ).move_to(card3_bg.get_left() + RIGHT * 0.6)
        card3_icon_text = Text(
            "分", font=FONT, font_size=22, color=WHITE
        ).move_to(card3_icon.get_center())

        card3_title = Text(
            "一个数", font=FONT, font_size=24, color=WHITE
        ).move_to(card3_bg.get_center() + UP * 0.3 + RIGHT * 0.3)
        card3_detail = Text(
            "分子、分数线、分母", font=FONT, font_size=18, color=GRAY_A
        ).move_to(card3_bg.get_center() + DOWN * 0.3 + RIGHT * 0.3)

        card3 = VGroup(card3_bg, card3_icon, card3_icon_text, card3_title, card3_detail)
        self.play(FadeIn(card3, shift=RIGHT * 0.5), run_time=0.7)
        self.wait(0.5)

        # 底部总结
        summary_line = VGroup(
            Text("比 = ", font=FONT, font_size=26, color=COLOR_RATIO),
            Text("关系", font=FONT, font_size=26, color=COLOR_RATIO),
            Text("    除法 = ", font=FONT, font_size=26, color=COLOR_DIV),
            Text("运算", font=FONT, font_size=26, color=COLOR_DIV),
            Text("    分数 = ", font=FONT, font_size=26, color=COLOR_FRAC),
            Text("数", font=FONT, font_size=26, color=COLOR_FRAC),
        ).arrange(RIGHT, buff=0.0).move_to(DOWN * 4.8)

        # Scale to fit if needed
        if summary_line.width > 8.0:
            summary_line.scale(8.0 / summary_line.width)

        self.play(FadeIn(summary_line, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(card1), FadeOut(card2), FadeOut(card3),
            FadeOut(summary_line),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 7: 注意事项 (b != 0)
    # ------------------------------------------------------------------
    def scene_7_warning(self):
        title = Text(
            "特别注意", font=FONT, font_size=36, color=COLOR_RED
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 大警告标识
        warning_icon = Text(
            "!", font=FONT, font_size=72, color=COLOR_RED
        ).move_to(UP * 4.0)
        warning_circle = Circle(
            radius=0.7, color=COLOR_RED, stroke_width=4
        ).move_to(warning_icon.get_center())

        self.play(FadeIn(warning_icon, scale=1.5), Create(warning_circle), run_time=0.6)

        # 条件
        cond_text = Text(
            "后项 / 除数 / 分母", font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 2.5)
        cond_neq = MathTex(
            r"\neq 0", font_size=48, color=COLOR_RED
        ).move_to(UP * 1.3)

        self.play(FadeIn(cond_text), run_time=0.5)
        self.play(Write(cond_neq), run_time=0.6)
        self.wait(0.5)

        # 解释
        explain1 = Text(
            "因为 0 不能做除数", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 0.3)
        explain2 = Text(
            "分母也不能为 0", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 1.3)
        explain3 = Text(
            "所以比的后项也不能为 0", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 2.3)

        self.play(FadeIn(explain1), run_time=0.5)
        self.play(FadeIn(explain2), run_time=0.5)
        self.play(FadeIn(explain3), run_time=0.5)
        self.wait(0.5)

        # 补充: 比的前项后项可以是小数
        extra_box = RoundedRectangle(
            width=7.5, height=1.8, corner_radius=0.2,
            color=COLOR_ACCENT, stroke_width=2, fill_opacity=0.08
        ).move_to(DOWN * 4.5)

        extra_text = Text(
            "比的前项和后项可以是小数、分数",
            font=FONT, font_size=22, color=WHITE
        ).move_to(extra_box.get_center() + UP * 0.25)
        extra_text2 = Text(
            "但分数的分子分母必须是整数",
            font=FONT, font_size=22, color=COLOR_ACCENT
        ).move_to(extra_box.get_center() + DOWN * 0.25)

        self.play(FadeIn(extra_box), FadeIn(extra_text), FadeIn(extra_text2), run_time=0.8)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(warning_icon), FadeOut(warning_circle),
            FadeOut(cond_text), FadeOut(cond_neq),
            FadeOut(explain1), FadeOut(explain2), FadeOut(explain3),
            FadeOut(extra_box), FadeOut(extra_text), FadeOut(extra_text2),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 8: 总结
    # ------------------------------------------------------------------
    def scene_8_summary(self):
        title = Text(
            "知识总结", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 核心公式
        core = VGroup(
            MathTex(r"a : b", font_size=44, color=COLOR_RATIO),
            MathTex(r"=", font_size=44, color=WHITE),
            MathTex(r"a \div b", font_size=44, color=COLOR_DIV),
            MathTex(r"=", font_size=44, color=WHITE),
            MathTex(r"\frac{a}{b}", font_size=48, color=COLOR_FRAC),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 4.2)
        cond = MathTex(r"(b \neq 0)", font_size=28, color=COLOR_RED).next_to(
            core, RIGHT, buff=0.3
        )
        # If too wide, scale
        core_all = VGroup(core, cond)
        if core_all.width > 8.0:
            core_all.scale(8.0 / core_all.width)

        core_box = SurroundingRectangle(core_all, color=COLOR_HL, buff=0.3, corner_radius=0.15)

        self.play(Write(core), FadeIn(cond), run_time=1.0)
        self.play(Create(core_box), run_time=0.5)
        self.wait(0.5)

        # 总结卡片
        cards_data = [
            ("1", "三者可以互相转化", COLOR_FORMULA),
            ("2", "比是关系, 除法是运算, 分数是数", COLOR_ACCENT),
            ("3", "前项=被除数=分子", COLOR_RATIO),
            ("4", "后项=除数=分母 (不为0)", COLOR_RED),
        ]

        cards = []
        y_start = 1.5
        for i, (num, text, color) in enumerate(cards_data):
            y = y_start - i * 1.6

            card_bg = RoundedRectangle(
                width=7.5, height=1.2, corner_radius=0.15,
                color=color, stroke_width=2, fill_opacity=0.08
            ).move_to(DOWN * (-y))

            num_circle = Circle(
                radius=0.28, color=color, fill_opacity=0.9, stroke_width=0
            ).move_to(card_bg.get_left() + RIGHT * 0.55)
            num_text = Text(
                num, font=FONT, font_size=22, color=WHITE
            ).move_to(num_circle.get_center())

            content = Text(
                text, font=FONT, font_size=22, color=WHITE
            ).move_to(card_bg.get_center() + RIGHT * 0.3)

            card = VGroup(card_bg, num_circle, num_text, content)
            cards.append(card)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.5)
            self.wait(0.2)

        self.wait(2.0)

        # 清理
        all_cards = VGroup(*cards)
        self.play(
            FadeOut(title), FadeOut(core), FadeOut(cond), FadeOut(core_box),
            FadeOut(all_cards),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 9: 片尾
    # ------------------------------------------------------------------
    def scene_9_outro(self):
        author_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(
            Transform(self.author_mob, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow_text = Text(
            "关注我, 获得更多数学技巧!",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)

        # 装饰
        icons = VGroup(
            Circle(radius=0.25, color=COLOR_RATIO, fill_opacity=0.8).shift(LEFT * 2),
            Circle(radius=0.25, color=COLOR_DIV, fill_opacity=0.8),
            Circle(radius=0.25, color=COLOR_FRAC, fill_opacity=0.8).shift(RIGHT * 2),
        ).move_to(DOWN * 2.5)

        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(self.author_mob),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )
