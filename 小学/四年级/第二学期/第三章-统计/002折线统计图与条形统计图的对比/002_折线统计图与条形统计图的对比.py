"""
折线统计图与条形统计图的对比
四年级 第二学期 第三章 统计

知识点：条形图优势（数量大小对比）vs 折线图优势（变化趋势）
格式：TikTok 竖屏 (1080×1920)
作者：上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# TikTok 竖屏配置
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# 颜色配置
COLOR_BAR = "#e74c3c"        # 条形图颜色 - 红色
COLOR_LINE = "#3498db"       # 折线图颜色 - 蓝色
COLOR_HIGHLIGHT = "#f1c40f"  # 高亮黄色
COLOR_BG = "#1a1a2e"         # 背景深蓝
COLOR_AXIS = "#95a5a6"       # 坐标轴灰色
COLOR_DOT = "#2ecc71"        # 折线点 - 绿色
COLOR_TEXT = "#ecf0f1"       # 正文白色
COLOR_CARD_BAR = "#c0392b"   # 条形卡片底色
COLOR_CARD_LINE = "#2980b9"  # 折线卡片底色


class LineBarChartCompareLesson(Scene):
    """
    折线统计图与条形统计图的对比 教学动画

    场景顺序：
    1. 开场钩子
    2. 认识条形统计图（什么时候用）
    3. 认识折线统计图（什么时候用）
    4. 同一组数据 — 两种图的对比
    5. 关键对比卡片总结
    6. 片尾
    """

    def construct(self):
        self.camera.background_color = COLOR_BG

        # ====== 全局数据 ======
        # 某同学1月~6月的月零花钱（元）
        self.months = ["1月", "2月", "3月", "4月", "5月", "6月"]
        self.values = [50, 80, 60, 90, 70, 100]

        # 四个城市2023年游客人数（万人）
        self.cities = ["北京", "上海", "广州", "成都"]
        self.city_vals = [120, 150, 90, 110]

        # 执行场景
        self.scene_1_opening()
        self.scene_2_bar_chart()
        self.scene_3_line_chart()
        self.scene_4_comparison()
        self.scene_5_summary()
        self.scene_6_outro()

    # ─────────────────────────────────────────
    #  场景 1：开场钩子
    # ─────────────────────────────────────────
    def scene_1_opening(self):
        # 作者标识（始终显示在顶部）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Heiti SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        # 钩子问题
        hook_line1 = Text(
            "条形图 vs 折线图",
            font="Heiti SC",
            font_size=40,
            color=COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)

        hook_line2 = Text(
            "你知道什么时候用哪个吗？",
            font="Heiti SC",
            font_size=28,
            color=COLOR_TEXT,
        ).move_to(UP * 4.6)

        self.play(Write(hook_line1), run_time=0.8)
        self.play(FadeIn(hook_line2, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 简单示意图：左边条形 右边折线
        bar_icon = self._make_mini_bar()
        bar_icon.move_to(LEFT * 2.2 + UP * 2.5)

        line_icon = self._make_mini_line()
        line_icon.move_to(RIGHT * 2.2 + UP * 2.5)

        vs_text = Text("VS", font="Heiti SC", font_size=36, color=COLOR_HIGHLIGHT)
        vs_text.move_to(UP * 2.5)

        bar_label = Text("条形图", font="Heiti SC", font_size=24, color=COLOR_BAR)
        bar_label.move_to(LEFT * 2.2 + UP * 1.2)
        line_label = Text("折线图", font="Heiti SC", font_size=24, color=COLOR_LINE)
        line_label.move_to(RIGHT * 2.2 + UP * 1.2)

        self.play(
            FadeIn(bar_icon, shift=RIGHT * 0.3),
            FadeIn(line_icon, shift=LEFT * 0.3),
            run_time=0.8
        )
        self.play(Write(vs_text), run_time=0.4)
        self.play(FadeIn(bar_label), FadeIn(line_label), run_time=0.4)
        self.wait(1.2)

        # 淡出
        self.play(
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            FadeOut(bar_icon),
            FadeOut(line_icon),
            FadeOut(vs_text),
            FadeOut(bar_label),
            FadeOut(line_label),
            run_time=0.5
        )

    # ─────────────────────────────────────────
    #  场景 2：条形统计图 — 适合比较数量大小
    # ─────────────────────────────────────────
    def scene_2_bar_chart(self):
        title = Text(
            "条形统计图",
            font="Heiti SC",
            font_size=36,
            color=COLOR_BAR
        ).move_to(UP * 6.2)

        subtitle = Text(
            "适合比较不同类别的数量大小",
            font="Heiti SC",
            font_size=22,
            color=COLOR_TEXT
        ).move_to(UP * 5.4)

        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 绘制条形图（城市游客人数）
        bar_group = self._build_bar_chart()
        bar_group.move_to(UP * 2.0)
        self.play(FadeIn(bar_group), run_time=0.5)

        # 逐条动画生长
        bars_vg, labels_vg, val_labels_vg, axes_vg = (
            bar_group[0], bar_group[1], bar_group[2], bar_group[3]
        )

        # 解说文字
        explain1 = Text(
            "一眼看出：上海游客最多",
            font="Heiti SC",
            font_size=24,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.0)

        explain2 = Text(
            "广州游客最少",
            font="Heiti SC",
            font_size=24,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.7)

        self.play(FadeIn(explain1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(explain2, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # 强调最高条
        highlight_rect = SurroundingRectangle(
            bars_vg[1], color=COLOR_HIGHLIGHT, buff=0.05, stroke_width=3
        )
        self.play(Create(highlight_rect), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(highlight_rect), run_time=0.3)

        # 优势总结
        advantage_box = self._make_advantage_card(
            "条形图优势",
            "直观显示数量多少\n便于不同类别的比较",
            COLOR_CARD_BAR
        ).move_to(DOWN * 3.5)

        self.play(FadeIn(advantage_box, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(bar_group),
            FadeOut(explain1),
            FadeOut(explain2),
            FadeOut(advantage_box),
            run_time=0.6
        )

    # ─────────────────────────────────────────
    #  场景 3：折线统计图 — 适合看变化趋势
    # ─────────────────────────────────────────
    def scene_3_line_chart(self):
        title = Text(
            "折线统计图",
            font="Heiti SC",
            font_size=36,
            color=COLOR_LINE
        ).move_to(UP * 6.2)

        subtitle = Text(
            "适合显示数据随时间的变化趋势",
            font="Heiti SC",
            font_size=22,
            color=COLOR_TEXT
        ).move_to(UP * 5.4)

        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 绘制折线图（月零花钱）
        line_group, dots_list, segments_list = self._build_line_chart()
        line_group.move_to(UP * 1.8)

        self.play(FadeIn(line_group[0], line_group[1]), run_time=0.5)  # 坐标轴 + 月份标签

        # 逐点出现
        for i, (dot, seg) in enumerate(zip(dots_list, segments_list)):
            dot_moved = dot.copy().move_to(
                line_group.get_center() + dot.get_center() - line_group[0].get_center()
            )
            if i == 0:
                self.play(FadeIn(dot), run_time=0.2)
            else:
                self.play(Create(seg), FadeIn(dot), run_time=0.3)

        # 显示其余图层
        for i in range(2, len(line_group)):
            self.play(FadeIn(line_group[i]), run_time=0.1)

        self.wait(0.3)

        # 说明趋势
        explain1 = Text(
            "整体呈上升趋势",
            font="Heiti SC",
            font_size=24,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.0)

        explain2 = Text(
            "3月有一次下降，5月又回落",
            font="Heiti SC",
            font_size=24,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.7)

        self.play(FadeIn(explain1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(explain2, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # 用箭头标出上升趋势
        trend_arrow = Arrow(
            start=LEFT * 2.0 + DOWN * 0.2,
            end=RIGHT * 2.0 + UP * 0.8,
            color=COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=3
        ).move_to(UP * 2.5)

        self.play(Create(trend_arrow), run_time=0.6)
        self.wait(0.5)
        self.play(FadeOut(trend_arrow), run_time=0.3)

        # 优势总结
        advantage_box = self._make_advantage_card(
            "折线图优势",
            "清楚显示数据的变化趋势\n能看出升降幅度",
            COLOR_CARD_LINE
        ).move_to(DOWN * 3.5)

        self.play(FadeIn(advantage_box, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(line_group),
            FadeOut(explain1),
            FadeOut(explain2),
            FadeOut(advantage_box),
            run_time=0.6
        )

    # ─────────────────────────────────────────
    #  场景 4：同一组数据 — 两种图的对比
    # ─────────────────────────────────────────
    def scene_4_comparison(self):
        title = Text(
            "同样的数据，选哪种图？",
            font="Heiti SC",
            font_size=32,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)

        self.play(Write(title), run_time=0.6)

        # 情景 A：比较城市人口 → 条形图
        scene_a_q = Text(
            "问题①：哪个城市的游客最多？",
            font="Heiti SC",
            font_size=22,
            color=COLOR_TEXT
        ).move_to(UP * 5.5)

        self.play(FadeIn(scene_a_q, shift=UP * 0.2), run_time=0.4)

        # 小条形图
        mini_bar = self._build_bar_chart_mini()
        mini_bar.move_to(UP * 3.0)
        self.play(FadeIn(mini_bar), run_time=0.5)

        answer_a = Text(
            "选条形图！对比各城市数量大小",
            font="Heiti SC",
            font_size=22,
            color=COLOR_BAR
        ).move_to(UP * 0.8)

        check_a = Dot(radius=0.15, color=COLOR_BAR)
        check_a.next_to(answer_a, LEFT, buff=0.2)

        self.play(FadeIn(answer_a), FadeIn(check_a), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(scene_a_q),
            FadeOut(mini_bar),
            FadeOut(answer_a),
            FadeOut(check_a),
            run_time=0.4
        )

        # 情景 B：月气温变化 → 折线图
        scene_b_q = Text(
            "问题②：气温如何随月份变化？",
            font="Heiti SC",
            font_size=22,
            color=COLOR_TEXT
        ).move_to(UP * 5.5)

        self.play(FadeIn(scene_b_q, shift=UP * 0.2), run_time=0.4)

        # 小折线图
        mini_line = self._build_line_chart_mini()
        mini_line.move_to(UP * 3.0)
        self.play(FadeIn(mini_line), run_time=0.5)

        answer_b = Text(
            "选折线图！看温度升降变化趋势",
            font="Heiti SC",
            font_size=22,
            color=COLOR_LINE
        ).move_to(UP * 0.8)

        check_b = Dot(radius=0.15, color=COLOR_LINE)
        check_b.next_to(answer_b, LEFT, buff=0.2)

        self.play(FadeIn(answer_b), FadeIn(check_b), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(scene_b_q),
            FadeOut(mini_line),
            FadeOut(answer_b),
            FadeOut(check_b),
            run_time=0.4
        )

        self.play(FadeOut(title), run_time=0.4)

    # ─────────────────────────────────────────
    #  场景 5：总结卡片
    # ─────────────────────────────────────────
    def scene_5_summary(self):
        title = Text(
            "记住这个口诀！",
            font="Heiti SC",
            font_size=36,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)

        self.play(Write(title), run_time=0.6)

        # 条形图卡片
        bar_card = self._make_summary_card(
            "条  形  图",
            "比较数量大小",
            "不同类别 → 谁多谁少",
            COLOR_BAR,
            UP * 3.8
        )

        # 折线图卡片
        line_card = self._make_summary_card(
            "折  线  图",
            "反映变化趋势",
            "同一事物 → 如何变化",
            COLOR_LINE,
            UP * 0.8
        )

        self.play(FadeIn(bar_card, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(line_card, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.5)

        # 公式口诀
        formula_bg = RoundedRectangle(
            width=7.5, height=2.2,
            corner_radius=0.3,
            fill_color="#16213e",
            fill_opacity=1,
            stroke_color=COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_to(DOWN * 2.5)

        formula_line1 = Text(
            "数量大小 → 条形图",
            font="Heiti SC",
            font_size=28,
            color=COLOR_BAR
        ).move_to(DOWN * 2.2)

        formula_line2 = Text(
            "变化趋势 → 折线图",
            font="Heiti SC",
            font_size=28,
            color=COLOR_LINE
        ).move_to(DOWN * 2.9)

        self.play(FadeIn(formula_bg), run_time=0.3)
        self.play(Write(formula_line1), run_time=0.5)
        self.play(Write(formula_line2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title),
            FadeOut(bar_card),
            FadeOut(line_card),
            FadeOut(formula_bg),
            FadeOut(formula_line1),
            FadeOut(formula_line2),
            run_time=0.6
        )

    # ─────────────────────────────────────────
    #  场景 6：片尾
    # ─────────────────────────────────────────
    def scene_6_outro(self):
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="Heiti SC",
            font_size=36,
            color=COLOR_TEXT
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font="Heiti SC",
            font_size=28,
            color="#6b7280"
        ).move_to(UP * 1.2)

        self.play(
            Transform(self.author, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Heiti SC",
            font_size=28,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 0.0)

        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.5)

        # 装饰小图标
        bar_deco = self._make_mini_bar().scale(0.5).move_to(LEFT * 2.0 + DOWN * 1.8)
        line_deco = self._make_mini_line().scale(0.5).move_to(RIGHT * 2.0 + DOWN * 1.8)

        self.play(
            FadeIn(bar_deco, shift=UP * 0.2),
            FadeIn(line_deco, shift=UP * 0.2),
            run_time=0.5
        )

        self.wait(2.0)

        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(bar_deco),
            FadeOut(line_deco),
            run_time=1.0
        )

    # ═══════════════════════════════════════════
    #  辅助方法
    # ═══════════════════════════════════════════

    def _make_mini_bar(self):
        """迷你条形图示意（用于开场和片尾）"""
        bar_heights = [0.4, 0.7, 0.5, 0.9]
        bars = VGroup()
        for i, h in enumerate(bar_heights):
            b = Rectangle(
                width=0.25, height=h,
                fill_color=COLOR_BAR,
                fill_opacity=0.85,
                stroke_width=0
            )
            b.move_to(RIGHT * i * 0.35 + UP * h / 2)
            bars.add(b)
        # 底线
        baseline = Line(LEFT * 0.1, RIGHT * 1.25, color=COLOR_AXIS, stroke_width=2)
        baseline.move_to(DOWN * 0.0)
        group = VGroup(bars, baseline)
        group.move_to(ORIGIN)
        return group

    def _make_mini_line(self):
        """迷你折线图示意（用于开场和片尾）"""
        pts = [
            np.array([0.0, 0.2, 0]),
            np.array([0.35, 0.5, 0]),
            np.array([0.7, 0.35, 0]),
            np.array([1.05, 0.75, 0]),
        ]
        dots = VGroup(*[Dot(p, radius=0.06, color=COLOR_DOT) for p in pts])
        segs = VGroup()
        for i in range(len(pts) - 1):
            segs.add(Line(pts[i], pts[i + 1], color=COLOR_LINE, stroke_width=2.5))
        baseline = Line(LEFT * 0.1, RIGHT * 1.15, color=COLOR_AXIS, stroke_width=2)
        baseline.move_to(DOWN * 0.0)
        group = VGroup(segs, dots, baseline)
        group.move_to(ORIGIN)
        return group

    def _build_bar_chart(self):
        """
        构建四城市游客条形图
        返回 VGroup(bars, city_labels, val_labels, axes)
        """
        # 轴
        x_len = 6.5
        y_len = 3.2
        origin = np.array([-3.0, -1.6, 0])

        # Y轴刻度: 0~160, step=40
        max_val = 160
        y_scale = y_len / max_val

        x_axis = Line(origin, origin + RIGHT * x_len, color=COLOR_AXIS, stroke_width=2)
        y_axis = Line(origin, origin + UP * y_len, color=COLOR_AXIS, stroke_width=2)

        # Y轴刻度和标签
        y_ticks = VGroup()
        y_labels = VGroup()
        for v in [40, 80, 120, 160]:
            y = origin[1] + v * y_scale
            tick = Line(
                np.array([origin[0] - 0.1, y, 0]),
                np.array([origin[0], y, 0]),
                color=COLOR_AXIS, stroke_width=1.5
            )
            label = Text(str(v), font="Heiti SC", font_size=14, color=COLOR_AXIS)
            label.move_to(np.array([origin[0] - 0.5, y, 0]))
            y_ticks.add(tick)
            y_labels.add(label)

        # 单位标签
        unit_label = Text("（万人）", font="Heiti SC", font_size=14, color=COLOR_AXIS)
        unit_label.move_to(np.array([origin[0] + 0.5, origin[1] + y_len + 0.3, 0]))

        axes_vg = VGroup(x_axis, y_axis, y_ticks, y_labels, unit_label)

        # 条形
        bar_width = 0.7
        bar_spacing = x_len / (len(self.cities) + 1)
        bars = VGroup()
        city_labels = VGroup()
        val_labels = VGroup()

        for i, (city, val) in enumerate(zip(self.cities, self.city_vals)):
            x = origin[0] + (i + 1) * bar_spacing
            bar_h = val * y_scale
            bar = Rectangle(
                width=bar_width, height=bar_h,
                fill_color=COLOR_BAR,
                fill_opacity=0.85,
                stroke_width=0
            )
            bar.move_to(np.array([x, origin[1] + bar_h / 2, 0]))
            bars.add(bar)

            city_lbl = Text(city, font="Heiti SC", font_size=16, color=COLOR_TEXT)
            city_lbl.move_to(np.array([x, origin[1] - 0.3, 0]))
            city_labels.add(city_lbl)

            val_lbl = Text(str(val), font="Heiti SC", font_size=14, color=COLOR_HIGHLIGHT)
            val_lbl.move_to(np.array([x, origin[1] + bar_h + 0.2, 0]))
            val_labels.add(val_lbl)

        chart_title = Text(
            "四城市2023年游客人数（万人）",
            font="Heiti SC",
            font_size=18,
            color=COLOR_TEXT
        ).move_to(np.array([origin[0] + x_len / 2, origin[1] + y_len + 0.65, 0]))

        return VGroup(bars, city_labels, val_labels, axes_vg, chart_title)

    def _build_line_chart(self):
        """
        构建月零花钱折线图
        返回 (VGroup(全图), dots_list, segments_list)
        """
        x_len = 6.0
        y_len = 3.0
        origin = np.array([-3.0, -1.4, 0])
        max_val = 120
        y_scale = y_len / max_val

        x_step = x_len / (len(self.months) - 1)

        x_axis = Line(origin, origin + RIGHT * x_len, color=COLOR_AXIS, stroke_width=2)
        y_axis = Line(origin, origin + UP * y_len, color=COLOR_AXIS, stroke_width=2)

        # Y轴刻度
        y_ticks = VGroup()
        y_labels = VGroup()
        for v in [20, 40, 60, 80, 100, 120]:
            y = origin[1] + v * y_scale
            tick = Line(
                np.array([origin[0] - 0.1, y, 0]),
                np.array([origin[0], y, 0]),
                color=COLOR_AXIS, stroke_width=1.5
            )
            label = Text(str(v), font="Heiti SC", font_size=14, color=COLOR_AXIS)
            label.move_to(np.array([origin[0] - 0.45, y, 0]))
            y_ticks.add(tick)
            y_labels.add(label)

        unit_label = Text("（元）", font="Heiti SC", font_size=14, color=COLOR_AXIS)
        unit_label.move_to(np.array([origin[0] + 0.3, origin[1] + y_len + 0.3, 0]))

        axes_part = VGroup(x_axis, y_axis, y_ticks, y_labels, unit_label)

        # X轴标签
        month_labels = VGroup()
        for i, m in enumerate(self.months):
            lbl = Text(m, font="Heiti SC", font_size=15, color=COLOR_TEXT)
            lbl.move_to(np.array([origin[0] + i * x_step, origin[1] - 0.3, 0]))
            month_labels.add(lbl)

        # 点坐标
        pts = []
        for i, v in enumerate(self.values):
            x = origin[0] + i * x_step
            y = origin[1] + v * y_scale
            pts.append(np.array([x, y, 0]))

        dots_list = [Dot(p, radius=0.1, color=COLOR_DOT) for p in pts]

        # 数值标签（点上方）
        val_labels = VGroup()
        for i, (p, v) in enumerate(zip(pts, self.values)):
            vl = Text(str(v), font="Heiti SC", font_size=14, color=COLOR_HIGHLIGHT)
            vl.move_to(p + UP * 0.28)
            val_labels.add(vl)

        # 线段列表
        segments_list = []
        for i in range(len(pts) - 1):
            seg = Line(pts[i], pts[i + 1], color=COLOR_LINE, stroke_width=3)
            segments_list.append(seg)

        chart_title = Text(
            "某同学1~6月零花钱（元）",
            font="Heiti SC",
            font_size=18,
            color=COLOR_TEXT
        ).move_to(np.array([origin[0] + x_len / 2, origin[1] + y_len + 0.62, 0]))

        all_segs = VGroup(*segments_list)
        all_dots = VGroup(*dots_list)

        full_group = VGroup(
            axes_part, month_labels, all_segs, all_dots, val_labels, chart_title
        )
        return full_group, dots_list, segments_list

    def _build_bar_chart_mini(self):
        """较小的条形图（用于对比场景）"""
        x_len = 5.5
        y_len = 2.5
        origin = np.array([-2.5, -1.2, 0])
        max_val = 160
        y_scale = y_len / max_val

        x_axis = Line(origin, origin + RIGHT * x_len, color=COLOR_AXIS, stroke_width=1.5)
        y_axis = Line(origin, origin + UP * y_len, color=COLOR_AXIS, stroke_width=1.5)

        bar_spacing = x_len / (len(self.cities) + 1)
        bars = VGroup()
        city_labels = VGroup()

        for i, (city, val) in enumerate(zip(self.cities, self.city_vals)):
            x = origin[0] + (i + 1) * bar_spacing
            bar_h = val * y_scale
            bar = Rectangle(
                width=0.55, height=bar_h,
                fill_color=COLOR_BAR,
                fill_opacity=0.8,
                stroke_width=0
            )
            bar.move_to(np.array([x, origin[1] + bar_h / 2, 0]))
            bars.add(bar)

            lbl = Text(city, font="Heiti SC", font_size=14, color=COLOR_TEXT)
            lbl.move_to(np.array([x, origin[1] - 0.28, 0]))
            city_labels.add(lbl)

        return VGroup(x_axis, y_axis, bars, city_labels)

    def _build_line_chart_mini(self):
        """较小的折线图（用于对比场景）"""
        x_len = 5.0
        y_len = 2.2
        origin = np.array([-2.5, -1.2, 0])
        max_val = 120
        y_scale = y_len / max_val
        x_step = x_len / (len(self.months) - 1)

        x_axis = Line(origin, origin + RIGHT * x_len, color=COLOR_AXIS, stroke_width=1.5)
        y_axis = Line(origin, origin + UP * y_len, color=COLOR_AXIS, stroke_width=1.5)

        pts = []
        for i, v in enumerate(self.values):
            x = origin[0] + i * x_step
            y = origin[1] + v * y_scale
            pts.append(np.array([x, y, 0]))

        dots = VGroup(*[Dot(p, radius=0.08, color=COLOR_DOT) for p in pts])
        segs = VGroup(*[
            Line(pts[i], pts[i + 1], color=COLOR_LINE, stroke_width=2.5)
            for i in range(len(pts) - 1)
        ])
        month_lbls = VGroup()
        for i, m in enumerate(self.months):
            lbl = Text(m, font="Heiti SC", font_size=12, color=COLOR_TEXT)
            lbl.move_to(np.array([origin[0] + i * x_step, origin[1] - 0.28, 0]))
            month_lbls.add(lbl)

        return VGroup(x_axis, y_axis, segs, dots, month_lbls)

    def _make_advantage_card(self, heading: str, content: str, bg_color: str):
        """创建优势说明卡片"""
        bg = RoundedRectangle(
            width=7.0, height=1.8,
            corner_radius=0.25,
            fill_color=bg_color,
            fill_opacity=0.85,
            stroke_width=0
        )
        h_text = Text(heading, font="Heiti SC", font_size=22, color=WHITE)
        h_text.move_to(bg.get_center() + UP * 0.45)

        c_text = Text(content, font="Heiti SC", font_size=18, color="#ecf0f1")
        c_text.move_to(bg.get_center() + DOWN * 0.2)

        return VGroup(bg, h_text, c_text)

    def _make_summary_card(
        self,
        heading: str,
        sub: str,
        detail: str,
        accent_color: str,
        position
    ):
        """创建总结卡片"""
        card_bg = RoundedRectangle(
            width=7.8, height=2.4,
            corner_radius=0.3,
            fill_color="#16213e",
            fill_opacity=1,
            stroke_color=accent_color,
            stroke_width=2.5
        )
        card_bg.move_to(position)

        # 左侧色块
        accent_bar = Rectangle(
            width=0.35, height=2.0,
            fill_color=accent_color,
            fill_opacity=1,
            stroke_width=0
        )
        accent_bar.move_to(position + LEFT * 3.73)

        h_text = Text(heading, font="Heiti SC", font_size=26, color=accent_color)
        h_text.move_to(position + UP * 0.55 + LEFT * 0.3)

        s_text = Text(sub, font="Heiti SC", font_size=22, color=COLOR_TEXT)
        s_text.move_to(position + DOWN * 0.1 + LEFT * 0.3)

        d_text = Text(detail, font="Heiti SC", font_size=18, color="#95a5a6")
        d_text.move_to(position + DOWN * 0.65 + LEFT * 0.3)

        return VGroup(card_bg, accent_bar, h_text, s_text, d_text)
