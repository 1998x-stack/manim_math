"""
001_统计条形统计图二.py -- 条形统计图(二) 教学动画

知识点: 认识以一当二或以一当五的条形统计图
年级: 二年级下册
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 回顾以一当一的条形统计图
  2. 引出问题: 数据很大时格子不够画
  3. 以一当二的条形统计图
  4. 以一当五的条形统计图
  5. 读图分析: 最多/最少/多多少/总和
  6. 总结
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
COLOR_BAR_1 = "#ef4444"       # 红色
COLOR_BAR_2 = "#3b82f6"       # 蓝色
COLOR_BAR_3 = "#22c55e"       # 绿色
COLOR_BAR_4 = "#f59e0b"       # 橙色
COLOR_AXIS = "#94a3b8"        # 灰蓝坐标轴
COLOR_GRID = "#334155"        # 深灰网格
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_FORMULA = "#22c55e"     # 绿色
COLOR_AUTHOR = "#6b7280"      # 灰色作者
COLOR_TITLE = "#e879f9"       # 紫粉标题
FONT = "PingFang SC"

BAR_COLORS = [COLOR_BAR_1, COLOR_BAR_2, COLOR_BAR_3, COLOR_BAR_4]

# ======================================================================
# 数据
# ======================================================================
# 场景一: 以一当一 (小数据)
FRUITS_SMALL = ["apple", "banana", "grape", "orange"]
FRUIT_NAMES = ["苹果", "香蕉", "葡萄", "橘子"]
DATA_SMALL = [3, 5, 2, 4]

# 场景二: 以一当二
SPORTS_NAMES = ["跑步", "跳绳", "游泳", "踢球"]
DATA_BY2 = [6, 10, 4, 8]

# 场景三: 以一当五
ANIMALS_NAMES = ["小猫", "小狗", "小兔", "小鸟"]
DATA_BY5 = [15, 25, 10, 20]


# ======================================================================
# 主场景
# ======================================================================

class BarChartTwoLesson(Scene):
    """
    条形统计图(二) 教学动画
    场景顺序:
      1. 开场钩子
      2. 回顾以一当一
      3. 引出问题 -- 数据变大怎么办
      4. 以一当二的条形统计图
      5. 以一当五的条形统计图
      6. 读图分析练习
      7. 总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_review_one_by_one()
        self.scene_3_problem_intro()
        self.scene_4_one_represents_two()
        self.scene_5_one_represents_five()
        self.scene_6_analysis()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # Helper: author watermark
    # ------------------------------------------------------------------
    def _author_mark(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)

    # ------------------------------------------------------------------
    # Helper: build a simple bar chart manually
    # ------------------------------------------------------------------
    def _build_bar_chart(self, names, values, unit_value=1,
                         y_max=None, y_step=None,
                         chart_center=ORIGIN,
                         bar_width=0.55, chart_width=7.0, chart_height=5.0):
        """
        Build a manual bar chart that fits the vertical frame.
        Returns dict with keys: group, bars, labels, y_labels, axes_group, grid_lines
        """
        n = len(names)
        if y_max is None:
            y_max = max(values) + unit_value
        if y_step is None:
            y_step = unit_value

        # Axes origin (bottom-left of chart area)
        origin = np.array([
            chart_center[0] - chart_width / 2,
            chart_center[1] - chart_height / 2,
            0
        ])

        # x-axis and y-axis
        x_axis = Line(
            origin, origin + RIGHT * chart_width,
            color=COLOR_AXIS, stroke_width=2
        )
        y_axis = Line(
            origin, origin + UP * chart_height,
            color=COLOR_AXIS, stroke_width=2
        )
        axes_group = VGroup(x_axis, y_axis)

        # Y-axis labels and grid lines
        y_labels = VGroup()
        grid_lines = VGroup()
        num_ticks = int(y_max / y_step) + 1
        for i in range(num_ticks):
            val = i * y_step
            y_pos = origin[1] + (val / y_max) * chart_height
            # tick mark
            tick = Line(
                np.array([origin[0] - 0.1, y_pos, 0]),
                np.array([origin[0] + 0.1, y_pos, 0]),
                color=COLOR_AXIS, stroke_width=1.5
            )
            # label
            lbl = Text(str(int(val)), font=FONT, font_size=16, color=COLOR_AXIS)
            lbl.next_to(tick, LEFT, buff=0.1)
            y_labels.add(VGroup(tick, lbl))
            # grid line
            if i > 0:
                gl = DashedLine(
                    np.array([origin[0], y_pos, 0]),
                    np.array([origin[0] + chart_width, y_pos, 0]),
                    color=COLOR_GRID, stroke_width=0.8, dash_length=0.08
                )
                grid_lines.add(gl)

        # Bars and x-labels
        spacing = chart_width / (n + 1)
        bars = VGroup()
        x_labels = VGroup()

        for i in range(n):
            x_center = origin[0] + spacing * (i + 1)
            bar_height = (values[i] / y_max) * chart_height

            bar = Rectangle(
                width=bar_width,
                height=max(bar_height, 0.01),
                fill_color=BAR_COLORS[i % len(BAR_COLORS)],
                fill_opacity=0.85,
                stroke_color=WHITE,
                stroke_width=1
            )
            bar.move_to(np.array([
                x_center,
                origin[1] + bar_height / 2,
                0
            ]))
            bars.add(bar)

            # value label on top
            val_label = Text(
                str(values[i]), font=FONT, font_size=18, color=WHITE
            )
            val_label.next_to(bar, UP, buff=0.1)
            bars.add(val_label)

            # x-axis label
            name_label = Text(
                names[i], font=FONT, font_size=18, color=WHITE
            )
            name_label.move_to(np.array([x_center, origin[1] - 0.35, 0]))
            x_labels.add(name_label)

        # Unit label on y-axis
        unit_text_str = "1" if unit_value == 1 else str(unit_value)
        unit_note = Text(
            "1格=" + unit_text_str, font=FONT, font_size=16, color=COLOR_HL
        )
        unit_note.next_to(y_axis, UP, buff=0.15)

        everything = VGroup(axes_group, y_labels, grid_lines, bars, x_labels, unit_note)

        return {
            "group": everything,
            "bars": bars,
            "x_labels": x_labels,
            "y_labels": y_labels,
            "axes_group": axes_group,
            "grid_lines": grid_lines,
            "unit_note": unit_note,
        }

    # ------------------------------------------------------------------
    # Scene 1: Opening hook
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        author = self._author_mark()
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.author = author

        # Hook question
        hook = Text(
            "数据很多,\n格子不够画怎么办?",
            font=FONT, font_size=38, color=COLOR_HL,
            line_spacing=1.4
        ).move_to(UP * 3.5)

        self.play(Write(hook), run_time=1.0)
        self.wait(0.8)

        # Show a tiny bar overflowing comically
        tiny_axes = VGroup(
            Line(LEFT * 1.5 + DOWN * 1, RIGHT * 1.5 + DOWN * 1, color=COLOR_AXIS, stroke_width=2),
            Line(LEFT * 1.5 + DOWN * 1, LEFT * 1.5 + UP * 2, color=COLOR_AXIS, stroke_width=2),
        )
        # a bar that is too tall
        tall_bar = Rectangle(
            width=0.6, height=4.5,
            fill_color=COLOR_BAR_1, fill_opacity=0.8,
            stroke_color=WHITE, stroke_width=1
        ).move_to(DOWN * 1 + UP * 2.25)

        overflow_label = Text(
            "25", font=FONT, font_size=22, color=WHITE
        ).next_to(tall_bar, UP, buff=0.1)

        # question marks
        qmarks = Text("???", font=FONT, font_size=36, color=COLOR_HL).move_to(UP * 1.8 + RIGHT * 1.5)

        self.play(Create(tiny_axes), run_time=0.5)
        self.play(GrowFromEdge(tall_bar, DOWN), run_time=0.8)
        self.play(FadeIn(overflow_label), FadeIn(qmarks), run_time=0.5)
        self.wait(1.0)

        # subtitle
        subtitle = Text(
            "今天来学: 条形统计图(二)",
            font=FONT, font_size=28, color=WHITE
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(hook), FadeOut(tiny_axes), FadeOut(tall_bar),
            FadeOut(overflow_label), FadeOut(qmarks), FadeOut(subtitle),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: Review one-by-one bar chart
    # ------------------------------------------------------------------
    def scene_2_review_one_by_one(self):
        title = Text(
            "回顾: 以一当一", font=FONT, font_size=34, color=COLOR_TITLE
        ).move_to(UP * 5.5)

        desc = Text(
            "每一格代表1个",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.8)

        self.play(Write(title), FadeIn(desc), run_time=0.8)

        # Chart title
        chart_title = Text(
            "最喜欢的水果", font=FONT, font_size=22, color=WHITE
        ).move_to(UP * 4.0)
        self.play(FadeIn(chart_title), run_time=0.4)

        # Build chart
        chart = self._build_bar_chart(
            FRUIT_NAMES, DATA_SMALL,
            unit_value=1, y_max=6, y_step=1,
            chart_center=UP * 1.5,
            chart_height=4.0, chart_width=6.5
        )

        # Animate axes, grid, labels
        self.play(Create(chart["axes_group"]), run_time=0.5)
        self.play(FadeIn(chart["y_labels"]), FadeIn(chart["grid_lines"]), run_time=0.5)
        self.play(FadeIn(chart["x_labels"]), run_time=0.4)
        self.play(FadeIn(chart["unit_note"]), run_time=0.3)

        # Grow bars one by one
        bar_items = [chart["bars"][i] for i in range(0, len(chart["bars"]), 2)]
        val_items = [chart["bars"][i] for i in range(1, len(chart["bars"]), 2)]

        for bar, val in zip(bar_items, val_items):
            self.play(GrowFromEdge(bar, DOWN), run_time=0.4)
            self.play(FadeIn(val), run_time=0.2)

        explain = Text(
            "数据小的时候,\n一格代表1个就够了",
            font=FONT, font_size=22, color=GRAY_A,
            line_spacing=1.3
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(desc), FadeOut(chart_title),
            FadeOut(chart["group"]), FadeOut(explain),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: Problem -- data is too big
    # ------------------------------------------------------------------
    def scene_3_problem_intro(self):
        title = Text(
            "问题来了!", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.6)

        # Show big data
        data_card = VGroup()
        header = Text(
            "同学们最喜欢的运动", font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 4.5)
        data_card.add(header)

        items = VGroup()
        for i, (name, val) in enumerate(zip(SPORTS_NAMES, DATA_BY2)):
            row = VGroup(
                Text(name, font=FONT, font_size=22, color=BAR_COLORS[i]),
                Text(": " + str(val) + " 人", font=FONT, font_size=22, color=WHITE)
            ).arrange(RIGHT, buff=0.1)
            items.add(row)
        items.arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(UP * 2.5)
        data_card.add(items)

        self.play(FadeIn(header), run_time=0.4)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.3)

        # Ask the question
        question = Text(
            "如果还是一格代表1个...\n那10人要画10格, 太多了!",
            font=FONT, font_size=24, color=COLOR_HL,
            line_spacing=1.3
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.8)
        self.wait(1.0)

        # Solution hint
        solution = Text(
            "聪明的办法:\n让一格代表多个!",
            font=FONT, font_size=28, color=COLOR_FORMULA,
            line_spacing=1.3
        ).move_to(DOWN * 3.5)

        self.play(FadeIn(solution, scale=1.1), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(data_card),
            FadeOut(question), FadeOut(solution),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: One represents two
    # ------------------------------------------------------------------
    def scene_4_one_represents_two(self):
        title = Text(
            "以一当二", font=FONT, font_size=36, color=COLOR_TITLE
        ).move_to(UP * 5.5)

        desc = Text(
            "每一格代表2个", font=FONT, font_size=26, color=COLOR_HL
        ).move_to(UP * 4.8)

        self.play(Write(title), FadeIn(desc), run_time=0.8)

        chart_title = Text(
            "最喜欢的运动 (人数)", font=FONT, font_size=22, color=WHITE
        ).move_to(UP * 4.1)
        self.play(FadeIn(chart_title), run_time=0.4)

        # Build chart with unit_value=2
        chart = self._build_bar_chart(
            SPORTS_NAMES, DATA_BY2,
            unit_value=2, y_max=12, y_step=2,
            chart_center=UP * 1.2,
            chart_height=4.5, chart_width=7.0
        )

        self.play(Create(chart["axes_group"]), run_time=0.5)
        self.play(FadeIn(chart["y_labels"]), FadeIn(chart["grid_lines"]), run_time=0.5)
        self.play(FadeIn(chart["x_labels"]), run_time=0.4)

        # Highlight the unit note
        self.play(FadeIn(chart["unit_note"]), run_time=0.3)
        highlight_box = SurroundingRectangle(
            chart["unit_note"], color=COLOR_HL, buff=0.12, stroke_width=2
        )
        self.play(Create(highlight_box), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(highlight_box), run_time=0.3)

        # Explain the reading
        explain = Text(
            "6人 = 3格\n10人 = 5格",
            font=FONT, font_size=22, color=GRAY_A,
            line_spacing=1.3
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(explain), run_time=0.5)

        # Grow bars one by one
        bar_items = [chart["bars"][i] for i in range(0, len(chart["bars"]), 2)]
        val_items = [chart["bars"][i] for i in range(1, len(chart["bars"]), 2)]

        for bar, val in zip(bar_items, val_items):
            self.play(GrowFromEdge(bar, DOWN), run_time=0.5)
            self.play(FadeIn(val), run_time=0.2)

        self.wait(0.5)

        # Reading demo: point at "跳绳" bar
        arrow = Arrow(
            start=DOWN * 4.5 + RIGHT * 1,
            end=val_items[1].get_bottom() + DOWN * 0.1,
            color=COLOR_HL, stroke_width=3
        )
        read_text = Text(
            "跳绳: 5格 x 2 = 10人",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 5.0)

        self.play(
            FadeOut(explain),
            Create(arrow), FadeIn(read_text),
            run_time=0.6
        )
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(desc), FadeOut(chart_title),
            FadeOut(chart["group"]),
            FadeOut(arrow), FadeOut(read_text),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: One represents five
    # ------------------------------------------------------------------
    def scene_5_one_represents_five(self):
        title = Text(
            "以一当五", font=FONT, font_size=36, color=COLOR_TITLE
        ).move_to(UP * 5.5)

        desc = Text(
            "每一格代表5个", font=FONT, font_size=26, color=COLOR_HL
        ).move_to(UP * 4.8)

        self.play(Write(title), FadeIn(desc), run_time=0.8)

        chart_title = Text(
            "动物园里的小动物 (只)", font=FONT, font_size=22, color=WHITE
        ).move_to(UP * 4.1)
        self.play(FadeIn(chart_title), run_time=0.4)

        # Build chart with unit_value=5
        chart = self._build_bar_chart(
            ANIMALS_NAMES, DATA_BY5,
            unit_value=5, y_max=30, y_step=5,
            chart_center=UP * 1.2,
            chart_height=4.5, chart_width=7.0
        )

        self.play(Create(chart["axes_group"]), run_time=0.5)
        self.play(FadeIn(chart["y_labels"]), FadeIn(chart["grid_lines"]), run_time=0.5)
        self.play(FadeIn(chart["x_labels"]), run_time=0.4)

        # Highlight the unit note
        self.play(FadeIn(chart["unit_note"]), run_time=0.3)
        highlight_box = SurroundingRectangle(
            chart["unit_note"], color=COLOR_HL, buff=0.12, stroke_width=2
        )
        self.play(Create(highlight_box), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(highlight_box), run_time=0.3)

        # Grow bars one by one
        bar_items = [chart["bars"][i] for i in range(0, len(chart["bars"]), 2)]
        val_items = [chart["bars"][i] for i in range(1, len(chart["bars"]), 2)]

        for bar, val in zip(bar_items, val_items):
            self.play(GrowFromEdge(bar, DOWN), run_time=0.5)
            self.play(FadeIn(val), run_time=0.2)

        explain = Text(
            "25只 = 5格\n数据再大也不怕!",
            font=FONT, font_size=22, color=COLOR_FORMULA,
            line_spacing=1.3
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(desc), FadeOut(chart_title),
            FadeOut(chart["group"]), FadeOut(explain),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: Analysis exercise
    # ------------------------------------------------------------------
    def scene_6_analysis(self):
        title = Text(
            "读图分析", font=FONT, font_size=34, color=COLOR_TITLE
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.6)

        # Show the "by-5" chart again, smaller
        chart = self._build_bar_chart(
            ANIMALS_NAMES, DATA_BY5,
            unit_value=5, y_max=30, y_step=5,
            chart_center=UP * 2.5,
            chart_height=3.5, chart_width=6.0,
            bar_width=0.45
        )

        self.play(
            FadeIn(chart["group"]),
            run_time=0.6
        )

        # Question 1: most / least
        q1 = Text(
            "哪种动物最多? 哪种最少?",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(q1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        a1 = Text(
            "最多: 小狗 25只   最少: 小兔 10只",
            font=FONT, font_size=22, color=COLOR_FORMULA
        ).move_to(DOWN * 1.3)
        self.play(FadeIn(a1), run_time=0.5)
        self.wait(1.0)

        # Question 2: difference
        q2 = Text(
            "小狗比小兔多多少只?",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(q2, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        a2 = MathTex(r"25 - 10 = 15", font_size=30, color=COLOR_FORMULA)
        a2_text = Text("只", font=FONT, font_size=22, color=COLOR_FORMULA)
        a2_group = VGroup(a2, a2_text).arrange(RIGHT, buff=0.15).move_to(DOWN * 3.3)
        self.play(FadeIn(a2_group), run_time=0.5)
        self.wait(0.8)

        # Question 3: total
        q3 = Text(
            "一共有多少只小动物?",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(q3, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        a3 = MathTex(r"15 + 25 + 10 + 20 = 70", font_size=28, color=COLOR_FORMULA)
        a3_text = Text("只", font=FONT, font_size=22, color=COLOR_FORMULA)
        a3_group = VGroup(a3, a3_text).arrange(RIGHT, buff=0.15).move_to(DOWN * 5.3)
        self.play(FadeIn(a3_group), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(chart["group"]),
            FadeOut(q1), FadeOut(a1),
            FadeOut(q2), FadeOut(a2_group),
            FadeOut(q3), FadeOut(a3_group),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 7: Summary
    # ------------------------------------------------------------------
    def scene_7_summary(self):
        title = Text(
            "总结", font=FONT, font_size=36, color=COLOR_TITLE
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # Summary cards
        cards = VGroup()

        # Card 1
        c1_icon = Circle(radius=0.25, fill_color=COLOR_BAR_1, fill_opacity=1, stroke_width=0)
        c1_title = Text("以一当一", font=FONT, font_size=26, color=WHITE)
        c1_desc = Text("数据小的时候用\n1格=1个", font=FONT, font_size=20, color=GRAY_A, line_spacing=1.2)
        c1 = VGroup(c1_icon, c1_title, c1_desc).arrange(DOWN, buff=0.2)
        cards.add(c1)

        # Card 2
        c2_icon = Circle(radius=0.25, fill_color=COLOR_BAR_2, fill_opacity=1, stroke_width=0)
        c2_title = Text("以一当二", font=FONT, font_size=26, color=WHITE)
        c2_desc = Text("数据较大时用\n1格=2个", font=FONT, font_size=20, color=GRAY_A, line_spacing=1.2)
        c2 = VGroup(c2_icon, c2_title, c2_desc).arrange(DOWN, buff=0.2)
        cards.add(c2)

        # Card 3
        c3_icon = Circle(radius=0.25, fill_color=COLOR_BAR_3, fill_opacity=1, stroke_width=0)
        c3_title = Text("以一当五", font=FONT, font_size=26, color=WHITE)
        c3_desc = Text("数据很大时用\n1格=5个", font=FONT, font_size=20, color=GRAY_A, line_spacing=1.2)
        c3 = VGroup(c3_icon, c3_title, c3_desc).arrange(DOWN, buff=0.2)
        cards.add(c3)

        cards.arrange(DOWN, buff=0.8).move_to(UP * 1.5)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.5)
            self.wait(0.3)

        # Key point
        key_point = Text(
            "看清每格代表多少,\n才能正确读出数据!",
            font=FONT, font_size=28, color=COLOR_HL,
            line_spacing=1.3
        ).move_to(DOWN * 3.0)

        box = SurroundingRectangle(
            key_point, color=COLOR_HL, buff=0.25,
            corner_radius=0.15, stroke_width=2
        )

        self.play(FadeIn(key_point, shift=UP * 0.3), Create(box), run_time=0.8)
        self.wait(2.0)

        # Tips for analysis
        tips = Text(
            "读图分析小技巧:\n最多 / 最少 / 多多少 / 总和",
            font=FONT, font_size=22, color=GRAY_A,
            line_spacing=1.3
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(tips), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(cards),
            FadeOut(key_point), FadeOut(box), FadeOut(tips),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 8: Outro
    # ------------------------------------------------------------------
    def scene_8_outro(self):
        # Author info big
        author_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(
            Transform(self.author, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 1.0)

        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # decorative bars
        deco_bars = VGroup()
        colors_deco = [COLOR_BAR_1, COLOR_BAR_2, COLOR_BAR_3, COLOR_BAR_4]
        heights_deco = [1.2, 2.0, 0.8, 1.6]
        for i in range(4):
            bar = Rectangle(
                width=0.5, height=heights_deco[i],
                fill_color=colors_deco[i], fill_opacity=0.7,
                stroke_width=0
            )
            deco_bars.add(bar)
        deco_bars.arrange(RIGHT, buff=0.3, aligned_edge=DOWN).move_to(DOWN * 3.5)

        self.play(
            *[GrowFromEdge(b, DOWN) for b in deco_bars],
            run_time=0.8
        )
        self.wait(1.5)

        self.play(
            FadeOut(self.author), FadeOut(author_id),
            FadeOut(follow_text), FadeOut(deco_bars),
            run_time=1.0
        )


# 运行命令:
# manim -pql 001_统计条形统计图二.py BarChartTwoLesson     # 快速预览
# manim -qm 001_统计条形统计图二.py BarChartTwoLesson      # 中等质量
# manim -qh 001_统计条形统计图二.py BarChartTwoLesson       # 高质量
