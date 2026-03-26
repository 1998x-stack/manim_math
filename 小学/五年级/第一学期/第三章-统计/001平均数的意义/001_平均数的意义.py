"""
001_平均数的意义.py — 平均数的意义 教学动画

知识点: 平均数代表一组数据的一般水平，是虚拟代表值，受极端值影响
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 平均数是"一般水平"的代表
  2. 平均数不一定是原始数据中的某个数
  3. 极端值对平均数的影响
  4. 平均数的作用与局限
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
COLOR_BAR = ["#3b82f6", "#22c55e", "#f59e0b", "#ef4444", "#8b5cf6"]
COLOR_AVG = "#a78bfa"        # 紫色平均线
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_EXTREME = "#ef4444"    # 红色极端值
COLOR_AUTHOR = "#6b7280"
FONT = "Noto Sans CJK SC"


class AverageMeaningLesson(Scene):
    """
    平均数的意义教学动画
    场景:
      1. 开场钩子
      2. 代表一般水平 (柱状图 + 平均线)
      3. 不一定是原始数据
      4. 极端值的影响
      5. 总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_general_level()
        self.scene_3_virtual_number()
        self.scene_4_extreme_value()
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
            "到底代表什么？", font=FONT, font_size=40, color=COLOR_HL
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 代表一般水平
    # ------------------------------------------------------------------

    def scene_2_general_level(self):
        title = Text(
            "代表一般水平", font=FONT, font_size=38,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 5个同学的身高: 140, 145, 142, 148, 135
        data = [140, 145, 142, 148, 135]
        names = ["小明", "小红", "小刚", "小丽", "小华"]
        avg_val = sum(data) / len(data)  # = 142

        bar_width = 1.0
        scale = 0.04  # 缩放: 每cm = 0.04单位高
        base_y = -1.5
        offset = 130  # 基线偏移

        # 柱子
        bars = VGroup()
        name_labels = VGroup()
        val_labels = VGroup()
        for i, (val, name) in enumerate(zip(data, names)):
            x = (i - 2) * (bar_width + 0.5)
            h = (val - offset) * scale
            bar = Rectangle(
                width=bar_width, height=h,
                fill_color=COLOR_BAR[i], fill_opacity=0.7,
                stroke_color=COLOR_BAR[i], stroke_width=2
            )
            bar.move_to(np.array([x, base_y + h / 2, 0.0]))
            bars.add(bar)

            nm = Text(name, font=FONT, font_size=18, color=GRAY_A)
            nm.move_to(np.array([x, base_y - 0.3, 0.0]))
            name_labels.add(nm)

            vl = MathTex(str(val), font_size=22, color=WHITE)
            vl.move_to(np.array([x, base_y + h + 0.25, 0.0]))
            val_labels.add(vl)

        desc = Text(
            "5位同学的身高(cm)", font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 3.5)
        self.play(Write(desc), run_time=0.4)

        self.play(*[GrowFromEdge(b, DOWN) for b in bars], run_time=0.8)
        self.play(*[FadeIn(n) for n in name_labels], *[FadeIn(v) for v in val_labels], run_time=0.4)

        # 平均线
        avg_h = (avg_val - offset) * scale
        avg_y = base_y + avg_h
        avg_line = DashedLine(
            np.array([-3.8, avg_y, 0.0]),
            np.array([3.8, avg_y, 0.0]),
            color=COLOR_AVG, dash_length=0.12, stroke_width=2.5
        )
        avg_label = VGroup(
            Text("平均 ", font=FONT, font_size=20, color=COLOR_AVG),
            MathTex(str(int(avg_val)), font_size=26, color=COLOR_AVG),
        ).arrange(RIGHT, buff=0.05).next_to(avg_line, RIGHT, buff=0.1)

        self.play(Create(avg_line), FadeIn(avg_label), run_time=0.6)

        explain = Text(
            "平均数代表这组数据的「一般水平」",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 3.5)
        self.play(Write(explain), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, desc, bars, name_labels, val_labels,
                          avg_line, avg_label, explain)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 平均数不一定是原始数据
    # ------------------------------------------------------------------

    def scene_3_virtual_number(self):
        title = Text(
            "虚拟的代表值", font=FONT, font_size=36,
            color=COLOR_AVG, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 数据
        data_text = VGroup(
            Text("数据：", font=FONT, font_size=24, color=WHITE),
            MathTex(r"3,\ 5,\ 7,\ 9", font_size=32, color=COLOR_BAR[0]),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 3.0)
        self.play(FadeIn(data_text), run_time=0.5)

        # 计算
        calc = VGroup(
            Text("平均数 = ", font=FONT, font_size=24, color=WHITE),
            MathTex(r"\frac{3+5+7+9}{4} = \frac{24}{4} = 6", font_size=30, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 1.5)
        self.play(Write(calc), run_time=0.8)
        self.wait(0.5)

        # 6 不在原始数据中
        highlight = Text(
            "6 不是原始数据中的任何一个！",
            font=FONT, font_size=26, color=COLOR_EXTREME, weight=BOLD
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(highlight, shift=UP * 0.3), run_time=0.6)

        # 数轴展示
        number_line = NumberLine(
            x_range=[2, 10, 1],
            length=7,
            include_numbers=True,
            font_size=22,
        ).move_to(DOWN * 2.5)

        dots = VGroup(*[
            Dot(number_line.n2p(v), color=COLOR_BAR[0], radius=0.1)
            for v in [3, 5, 7, 9]
        ])
        avg_dot = Dot(number_line.n2p(6), color=COLOR_AVG, radius=0.12)
        avg_mark = MathTex(r"\bar{x}=6", font_size=24, color=COLOR_AVG)
        avg_mark.next_to(avg_dot, UP, buff=0.3)

        self.play(Create(number_line), run_time=0.6)
        self.play(*[FadeIn(d, scale=0.3) for d in dots], run_time=0.4)
        self.play(FadeIn(avg_dot, scale=0.3), FadeIn(avg_mark), run_time=0.5)

        explain = Text(
            "平均数是一个虚拟的代表值",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 4.5)
        self.play(Write(explain), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, data_text, calc, highlight,
                          number_line, dots, avg_dot, avg_mark, explain)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 极端值的影响
    # ------------------------------------------------------------------

    def scene_4_extreme_value(self):
        title = Text(
            "极端值的影响", font=FONT, font_size=36,
            color=COLOR_EXTREME, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 正常数据
        d1_text = VGroup(
            Text("工资：", font=FONT, font_size=22, color=WHITE),
            MathTex(r"3,\ 4,\ 4,\ 5,\ 4", font_size=28, color=COLOR_BAR[1]),
            Text("（万元）", font=FONT, font_size=18, color=GRAY_A),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 3.5)
        self.play(FadeIn(d1_text), run_time=0.5)

        avg1 = VGroup(
            Text("平均 = ", font=FONT, font_size=22, color=WHITE),
            MathTex(r"4", font_size=30, color=COLOR_AVG),
            Text(" 万元", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(UP * 2.5)
        self.play(Write(avg1), run_time=0.5)
        self.wait(0.5)

        # 加入极端值
        d2_text = VGroup(
            Text("加入老板：", font=FONT, font_size=22, color=WHITE),
            MathTex(r"3,\ 4,\ 4,\ 5,\ 4,\ ", font_size=28, color=COLOR_BAR[1]),
            MathTex(r"100", font_size=28, color=COLOR_EXTREME),
        ).arrange(RIGHT, buff=0.05).move_to(UP * 1.0)
        self.play(FadeIn(d2_text), run_time=0.5)

        avg2 = VGroup(
            Text("平均 = ", font=FONT, font_size=22, color=WHITE),
            MathTex(r"20", font_size=30, color=COLOR_EXTREME),
            Text(" 万元", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 0.0)
        self.play(Write(avg2), run_time=0.5)
        self.wait(0.3)

        # 对比
        compare = Text(
            "一个极端值让平均数翻了5倍！",
            font=FONT, font_size=26, color=COLOR_EXTREME, weight=BOLD
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(compare, shift=UP * 0.3), run_time=0.6)

        warning = Text(
            "平均数容易受极端值影响",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 2.8)
        self.play(Write(warning), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, d1_text, avg1, d2_text, avg2, compare, warning)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 总结
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
            "平均数的意义", font=FONT,
            font_size=32, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 2.8)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 代表一组数据的一般水平", font=FONT, font_size=22, color=WHITE),
            Text("2. 不一定是原始数据中的数", font=FONT, font_size=22, color=WHITE),
            Text("3. 是一个虚拟的代表值", font=FONT, font_size=22, color=WHITE),
            Text("4. 容易受极端值影响", font=FONT, font_size=22, color=COLOR_EXTREME),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 0.5)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        tip = Text(
            "使用时要注意数据的分布！",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(VGroup(box, sum_title, items, tip)), run_time=0.5)

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
#   快速预览:  manim -pql 001_平均数的意义.py AverageMeaningLesson
#   高质量:    manim -qh  001_平均数的意义.py AverageMeaningLesson
#   4K:        manim -qk  001_平均数的意义.py AverageMeaningLesson
# ======================================================================
