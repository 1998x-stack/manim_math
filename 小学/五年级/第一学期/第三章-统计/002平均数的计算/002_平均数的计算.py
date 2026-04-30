"""
002_平均数的计算.py — 平均数的计算 教学动画

知识点: 基本平均数公式和加权平均数
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 基本公式: 平均数 = 总数 ÷ 份数
  2. 移多补少法的直观理解
  3. 加权平均: 考试成绩例子
     10人90分, 15人85分, 5人80分
     平均分 = (90×10 + 85×15 + 80×5) ÷ 30 = 85.5
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
COLOR_BAR1 = "#3b82f6"      # 蓝色
COLOR_BAR2 = "#22c55e"       # 绿色
COLOR_BAR3 = "#f59e0b"       # 橙色
COLOR_BAR4 = "#ef4444"       # 红色
COLOR_AVG = "#a78bfa"        # 紫色平均线
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_AUTHOR = "#6b7280"
FONT = "PingFang SC"


class AverageCalculationLesson(Scene):
    """
    平均数的计算教学动画
    场景:
      1. 开场钩子
      2. 基本概念: 移多补少
      3. 基本公式
      4. 加权平均数
      5. 公式总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_level_bars()
        self.scene_3_basic_formula()
        self.scene_4_weighted_average()
        self.scene_5_summary()
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
            "平均数", font=FONT, font_size=52, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "到底怎么算？", font=FONT, font_size=40, color=COLOR_HL
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 移多补少法 (直观理解)
    # ------------------------------------------------------------------

    def scene_2_level_bars(self):
        title = Text(
            "移多补少", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 四个人的糖果数: 2, 6, 4, 8 → 平均 5
        data = [2, 6, 4, 8]
        avg_val = sum(data) / len(data)  # = 5.0
        colors = [COLOR_BAR1, COLOR_BAR2, COLOR_BAR3, COLOR_BAR4]
        bar_width = 1.2
        scale = 0.45  # 每单位高度
        base_y = -0.5

        # 画柱子
        bars = VGroup()
        labels = VGroup()
        for i, (val, col) in enumerate(zip(data, colors)):
            x = (i - 1.5) * (bar_width + 0.3)
            bar = Rectangle(
                width=bar_width, height=val * scale,
                fill_color=col, fill_opacity=0.7,
                stroke_color=col, stroke_width=2
            )
            bar.move_to(np.array([x, base_y + val * scale / 2, 0.0]))
            bars.add(bar)

            num = MathTex(str(val), font_size=28, color=WHITE)
            num.move_to(np.array([x, base_y + val * scale + 0.3, 0.0]))
            labels.add(num)

        self.play(*[GrowFromEdge(b, DOWN) for b in bars], run_time=0.8)
        self.play(*[FadeIn(l) for l in labels], run_time=0.4)

        desc = Text(
            "四个人分别有 2, 6, 4, 8 颗糖",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 3.0)
        self.play(Write(desc), run_time=0.6)
        self.wait(0.5)

        # 平均线
        avg_y = base_y + avg_val * scale
        avg_line = DashedLine(
            np.array([-3.5, avg_y, 0.0]),
            np.array([3.5, avg_y, 0.0]),
            color=COLOR_AVG, dash_length=0.12, stroke_width=2.5
        )
        avg_label = VGroup(
            Text("平均 ", font=FONT, font_size=22, color=COLOR_AVG),
            MathTex(str(int(avg_val)), font_size=28, color=COLOR_AVG),
        ).arrange(RIGHT, buff=0.05).move_to(np.array([3.5, avg_y + 0.3, 0.0]))

        self.play(Create(avg_line), FadeIn(avg_label), run_time=0.6)
        self.wait(0.3)

        # 动画: 所有柱子变成相同高度
        desc2 = Text(
            "把多的移给少的，变得一样高",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 3.0)
        self.play(FadeOut(desc), FadeIn(desc2, shift=UP * 0.2), run_time=0.4)

        new_bars = VGroup()
        new_labels = VGroup()
        for i, col in enumerate(colors):
            x = (i - 1.5) * (bar_width + 0.3)
            bar = Rectangle(
                width=bar_width, height=avg_val * scale,
                fill_color=col, fill_opacity=0.7,
                stroke_color=col, stroke_width=2
            )
            bar.move_to(np.array([x, base_y + avg_val * scale / 2, 0.0]))
            new_bars.add(bar)

            num = MathTex(str(int(avg_val)), font_size=28, color=WHITE)
            num.move_to(np.array([x, base_y + avg_val * scale + 0.3, 0.0]))
            new_labels.add(num)

        self.play(
            *[Transform(bars[i], new_bars[i]) for i in range(4)],
            *[Transform(labels[i], new_labels[i]) for i in range(4)],
            run_time=1.5
        )
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, bars, labels, avg_line, avg_label, desc2)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 基本公式
    # ------------------------------------------------------------------

    def scene_3_basic_formula(self):
        title = Text(
            "基本公式", font=FONT, font_size=38,
            color=COLOR_BAR1, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 总数
        step1 = VGroup(
            Text("总数 = ", font=FONT, font_size=26, color=WHITE),
            MathTex(r"2 + 6 + 4 + 8 = 20", font_size=32, color=COLOR_BAR2),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 3.0)
        self.play(FadeIn(step1, shift=UP * 0.2), run_time=0.6)

        # 份数
        step2 = VGroup(
            Text("份数 = ", font=FONT, font_size=26, color=WHITE),
            MathTex(r"4", font_size=32, color=COLOR_BAR3),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 1.8)
        self.play(FadeIn(step2, shift=UP * 0.2), run_time=0.5)

        # 公式
        formula_box = RoundedRectangle(
            width=7.5, height=2.0,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(DOWN * 0.2)

        f_lhs = Text("平均数 = ", font=FONT, font_size=28, color=WHITE)
        f_rhs = MathTex(r"\frac{20}{4} = 5", font_size=40, color=COLOR_HL)
        formula = VGroup(f_lhs, f_rhs).arrange(RIGHT, buff=0.1).move_to(DOWN * 0.2)

        self.play(FadeIn(formula_box), run_time=0.3)
        self.play(Write(formula), run_time=0.8)
        self.wait(0.5)

        # 通用公式
        general = VGroup(
            Text("平均数", font=FONT, font_size=26, color=WHITE),
            MathTex(r"=", font_size=30, color=WHITE),
            Text("总数", font=FONT, font_size=26, color=COLOR_BAR2),
            MathTex(r"\div", font_size=30, color=WHITE),
            Text("份数", font=FONT, font_size=26, color=COLOR_BAR3),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 2.5)

        self.play(FadeIn(general, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, step1, step2, formula_box, formula, general)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 加权平均数
    # ------------------------------------------------------------------

    def scene_4_weighted_average(self):
        title = Text(
            "加权平均数", font=FONT, font_size=38,
            color=COLOR_BAR3, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 题目
        problem = Text(
            "某班考试成绩如下：",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.0)
        self.play(Write(problem), run_time=0.5)

        # 数据表 (手动排列)
        header = VGroup(
            Text("分数", font=FONT, font_size=22, color=COLOR_HL),
            Text("人数", font=FONT, font_size=22, color=COLOR_HL),
        ).arrange(RIGHT, buff=2.5).move_to(UP * 3.0)

        row1 = VGroup(
            MathTex(r"90", font_size=28, color=COLOR_BAR1),
            MathTex(r"10", font_size=28, color=WHITE),
        ).arrange(RIGHT, buff=2.8).move_to(UP * 2.3)

        row2 = VGroup(
            MathTex(r"85", font_size=28, color=COLOR_BAR2),
            MathTex(r"15", font_size=28, color=WHITE),
        ).arrange(RIGHT, buff=2.8).move_to(UP * 1.6)

        row3 = VGroup(
            MathTex(r"80", font_size=28, color=COLOR_BAR3),
            MathTex(r"5", font_size=28, color=WHITE),
        ).arrange(RIGHT, buff=3.0).move_to(UP * 0.9)

        table = VGroup(header, row1, row2, row3)

        # 分隔线
        h_line = Line(LEFT * 2.5, RIGHT * 2.5, color=GRAY, stroke_width=1).move_to(UP * 2.65)

        self.play(FadeIn(table), Create(h_line), run_time=0.6)
        self.wait(0.5)

        # 计算过程
        step1_lhs = Text("总分 = ", font=FONT, font_size=22, color=WHITE)
        step1_rhs = MathTex(
            r"90 \times 10 + 85 \times 15 + 80 \times 5",
            font_size=24, color=COLOR_BAR2
        )
        step1 = VGroup(step1_lhs, step1_rhs).arrange(RIGHT, buff=0.1).move_to(DOWN * 0.5)
        self.play(FadeIn(step1, shift=UP * 0.2), run_time=0.6)

        step2 = VGroup(
            Text("     = ", font=FONT, font_size=22, color=WHITE),
            MathTex(r"900 + 1275 + 400 = 2575", font_size=24, color=COLOR_BAR2),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.3)
        self.play(FadeIn(step2, shift=UP * 0.2), run_time=0.5)

        step3 = VGroup(
            Text("总人数 = ", font=FONT, font_size=22, color=WHITE),
            MathTex(r"10 + 15 + 5 = 30", font_size=24, color=COLOR_BAR3),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 2.1)
        self.play(FadeIn(step3, shift=UP * 0.2), run_time=0.5)

        # 结果
        result_lhs = Text("平均分 = ", font=FONT, font_size=26, color=WHITE)
        result_rhs = MathTex(
            r"\frac{2575}{30} \approx 85.8",
            font_size=34, color=COLOR_HL
        )
        result = VGroup(result_lhs, result_rhs).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.5)

        self.play(FadeIn(result, shift=UP * 0.3), run_time=0.7)
        self.play(Indicate(result_rhs, scale_factor=1.1, color=COLOR_HL), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, problem, table, h_line, step1, step2, step3, result)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 公式总结
    # ------------------------------------------------------------------

    def scene_5_summary(self):
        box = RoundedRectangle(
            width=8.0, height=5.5,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)

        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "平均数的计算", font=FONT,
            font_size=32, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 2.8)
        self.play(Write(sum_title), run_time=0.5)

        # 基本公式
        f1_title = Text("基本公式", font=FONT, font_size=24, color=COLOR_BAR1, weight=BOLD)
        f1 = VGroup(
            Text("平均数 = 总数 ", font=FONT, font_size=22, color=WHITE),
            MathTex(r"\div", font_size=26, color=WHITE),
            Text(" 份数", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.05)
        block1 = VGroup(f1_title, f1).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        block1.move_to(UP * 1.3)

        self.play(FadeIn(block1, shift=RIGHT * 0.3), run_time=0.6)

        sep = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY, stroke_width=1).move_to(UP * 0.2)
        self.play(Create(sep), run_time=0.3)

        # 加权平均
        f2_title = Text("加权平均", font=FONT, font_size=24, color=COLOR_BAR3, weight=BOLD)
        f2_line1 = Text("总数 = 各数据 × 对应人数 之和", font=FONT, font_size=20, color=WHITE)
        f2_line2 = Text("平均数 = 总数 ÷ 总人数", font=FONT, font_size=20, color=WHITE)
        block2 = VGroup(f2_title, f2_line1, f2_line2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        block2.move_to(DOWN * 1.2)

        self.play(FadeIn(block2, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(VGroup(box, sum_title, block1, sep, block2)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------

    def scene_6_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_A
        ).move_to(UP * 1.0)

        self.play(Transform(self.author_mob, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 002_平均数的计算.py AverageCalculationLesson
#   高质量:    manim -qh  002_平均数的计算.py AverageCalculationLesson
#   4K:        manim -qk  002_平均数的计算.py AverageCalculationLesson
# ======================================================================
