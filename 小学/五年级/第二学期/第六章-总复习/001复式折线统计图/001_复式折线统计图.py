"""
001_复式折线统计图.py — 复式折线统计图 教学动画

知识点: 两条折线在同一张图上，方便对比趋势
年级: 五年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  单式 vs 复式折线统计图
  例题: 甲乙两城市 1-6 月气温变化
    甲城: 2, 5, 10, 16, 22, 28 (°C)
    乙城: 8, 10, 14, 18, 22, 25 (°C)
  绘制方法: 标题、横轴(月份)、纵轴(温度)、两条折线、图例
  读图分析: 温差、趋势、交点
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
COLOR_CITY_A = "#ef4444"      # 红色 — 甲城
COLOR_CITY_B = "#3b82f6"      # 蓝色 — 乙城
COLOR_AXIS = "#94a3b8"        # 灰蓝色坐标轴
COLOR_GRID = "#334155"        # 深灰网格线
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_FORMULA = "#22c55e"     # 绿色公式/结论
COLOR_AUTHOR = "#6b7280"      # 灰色作者信息
COLOR_SINGLE = "#a78bfa"      # 紫色 — 单式折线
COLOR_DIFF = "#f59e0b"        # 橙色 — 温差
FONT = "PingFang SC"

# ======================================================================
# 数据
# ======================================================================
MONTHS = [1, 2, 3, 4, 5, 6]
TEMPS_A = [2, 5, 10, 16, 22, 28]   # 甲城
TEMPS_B = [8, 10, 14, 18, 22, 25]  # 乙城


# ======================================================================
# 主场景
# ======================================================================

class DoubleLineGraphLesson(Scene):
    """
    复式折线统计图教学动画
    场景顺序:
      1. 开场钩子
      2. 单式折线统计图回顾
      3. 引入复式折线统计图 (核心)
      4. 绘制复式折线统计图
      5. 读图分析
      6. 总结优点
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_single_line_review()
        self.scene_3_introduce_double()
        self.scene_4_draw_double_graph()
        self.scene_5_analysis()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 辅助方法
    # ------------------------------------------------------------------

    def _build_axes(self, y_range_top=32, y_step=4):
        """构建竖屏适配的坐标轴"""
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, y_range_top, y_step],
            x_length=7.0,
            y_length=5.0,
            axis_config={
                "color": COLOR_AXIS,
                "stroke_width": 2,
                "include_ticks": True,
                "tick_size": 0.08,
            },
            x_axis_config={
                "numbers_to_include": [],
            },
            y_axis_config={
                "numbers_to_include": list(range(0, y_range_top + 1, y_step)),
                "font_size": 20,
                "decimal_number_config": {"num_decimal_places": 0},
            },
        )
        return axes

    def _add_x_labels(self, axes):
        """为横轴添加中文月份标签"""
        labels = VGroup()
        for m in MONTHS:
            lbl = Text(f"{m}月", font=FONT, font_size=18, color=COLOR_AXIS)
            lbl.next_to(axes.c2p(m, 0), DOWN, buff=0.15)
            labels.add(lbl)
        return labels

    def _add_grid_lines(self, axes, y_range_top=32, y_step=4):
        """添加水平网格线"""
        grid = VGroup()
        for y_val in range(y_step, y_range_top + 1, y_step):
            line = DashedLine(
                axes.c2p(0, y_val), axes.c2p(7, y_val),
                color=COLOR_GRID, stroke_width=0.8, dash_length=0.08
            )
            grid.add(line)
        return grid

    def _plot_line_with_dots(self, axes, temps, color, dot_radius=0.08):
        """绘制折线 + 数据点"""
        points = [axes.c2p(m, t) for m, t in zip(MONTHS, temps)]
        line = VMobject(color=color, stroke_width=3)
        line.set_points_as_corners(points)
        dots = VGroup(*[
            Dot(p, radius=dot_radius, color=color)
            for p in points
        ])
        return line, dots

    def _add_temp_labels(self, axes, temps, color, direction=UP):
        """在数据点上方/下方添加温度标签"""
        labels = VGroup()
        for m, t in zip(MONTHS, temps):
            lbl = Text(
                f"{t}°C", font=FONT, font_size=14, color=color
            )
            lbl.next_to(axes.c2p(m, t), direction, buff=0.15)
            labels.add(lbl)
        return labels

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: '一张图就能比较两组数据？'"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text(
            "一张图就能比较", font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            "两组数据的变化？", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 两条示意小折线 (装饰用)
        line_a_pts = [
            LEFT * 2.5 + DOWN * 0.5,
            LEFT * 1.0 + UP * 0.3,
            RIGHT * 0.5 + DOWN * 0.2,
            RIGHT * 2.5 + UP * 1.0,
        ]
        line_b_pts = [
            LEFT * 2.5 + UP * 0.5,
            LEFT * 1.0 + DOWN * 0.3,
            RIGHT * 0.5 + UP * 0.5,
            RIGHT * 2.5 + DOWN * 0.2,
        ]
        deco_a = VMobject(color=COLOR_CITY_A, stroke_width=4)
        deco_a.set_points_as_corners(line_a_pts)
        deco_b = VMobject(color=COLOR_CITY_B, stroke_width=4)
        deco_b.set_points_as_corners(line_b_pts)
        deco_group = VGroup(deco_a, deco_b).move_to(DOWN * 0.5)

        self.play(Create(deco_a), Create(deco_b), run_time=1.2)

        # 问号
        q = Text("?", font=FONT, font_size=72, color=COLOR_HL, weight=BOLD)
        q.move_to(DOWN * 2.5)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(0.8)

        # 清理钩子
        self.play(FadeOut(VGroup(hook1, hook2, deco_group, q)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 单式折线统计图回顾
    # ------------------------------------------------------------------

    def scene_2_single_line_review(self):
        """回顾单式折线统计图 — 只展示甲城一条线"""

        title = Text(
            "单式折线统计图", font=FONT, font_size=38,
            color=COLOR_SINGLE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        subtitle = Text(
            "只能展示一组数据的变化趋势",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.7)
        self.play(Write(subtitle), run_time=0.5)

        # 构建坐标轴 — 单式图
        axes = self._build_axes()
        axes.move_to(DOWN * 0.5)

        x_labels = self._add_x_labels(axes)
        grid = self._add_grid_lines(axes)

        # 纵轴标题
        y_title = Text("温度/°C", font=FONT, font_size=18, color=COLOR_AXIS)
        y_title.next_to(axes.y_axis.get_top(), UP, buff=0.15)

        # 图表标题
        chart_title = Text(
            "甲城1-6月气温变化", font=FONT, font_size=22, color=WHITE
        ).next_to(axes, UP, buff=0.35)

        self.play(
            Create(axes), FadeIn(grid),
            run_time=0.8
        )
        self.play(
            FadeIn(x_labels), FadeIn(y_title), Write(chart_title),
            run_time=0.6
        )

        # 甲城折线
        line_a, dots_a = self._plot_line_with_dots(axes, TEMPS_A, COLOR_CITY_A)
        temp_labels_a = self._add_temp_labels(axes, TEMPS_A, COLOR_CITY_A, UP)

        self.play(Create(line_a), run_time=1.0)
        self.play(
            *[FadeIn(d, scale=0.5) for d in dots_a],
            run_time=0.5
        )
        self.play(FadeIn(temp_labels_a), run_time=0.5)
        self.wait(0.8)

        # 提出问题
        question = Text(
            "如果还想看乙城的变化呢？",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)

        # 保存供下一场景复用
        self.single_axes = axes
        self.single_grid = grid
        self.single_x_labels = x_labels
        self.single_y_title = y_title
        self.single_chart_title = chart_title
        self.single_line_a = line_a
        self.single_dots_a = dots_a
        self.single_temp_labels_a = temp_labels_a

        # 清理
        self.play(
            FadeOut(VGroup(
                title, subtitle, question,
                axes, grid, x_labels, y_title, chart_title,
                line_a, dots_a, temp_labels_a
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 引入复式折线统计图
    # ------------------------------------------------------------------

    def scene_3_introduce_double(self):
        """概念引入: 复式 = 两条折线 + 图例"""

        title = Text(
            "复式折线统计图", font=FONT, font_size=38,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 对比说明
        single_box = RoundedRectangle(
            width=3.5, height=2.8, corner_radius=0.2,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_SINGLE, stroke_width=2
        ).move_to(LEFT * 2.2 + UP * 2.5)

        single_title = Text(
            "单式", font=FONT, font_size=28, color=COLOR_SINGLE, weight=BOLD
        ).move_to(single_box.get_top() + DOWN * 0.4)

        single_desc = VGroup(
            Text("一组数据", font=FONT, font_size=20, color=WHITE),
            Text("一条折线", font=FONT, font_size=20, color=WHITE),
        ).arrange(DOWN, buff=0.15).move_to(single_box.get_center() + DOWN * 0.15)

        # 单式小图示 — 一条紫线
        s_pts = [
            single_box.get_center() + LEFT * 1.0 + DOWN * 0.9,
            single_box.get_center() + LEFT * 0.3 + DOWN * 0.55,
            single_box.get_center() + RIGHT * 0.3 + DOWN * 0.75,
            single_box.get_center() + RIGHT * 1.0 + DOWN * 0.4,
        ]
        s_line = VMobject(color=COLOR_SINGLE, stroke_width=3)
        s_line.set_points_as_corners(s_pts)

        double_box = RoundedRectangle(
            width=3.5, height=2.8, corner_radius=0.2,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_HL, stroke_width=2
        ).move_to(RIGHT * 2.2 + UP * 2.5)

        double_title = Text(
            "复式", font=FONT, font_size=28, color=COLOR_HL, weight=BOLD
        ).move_to(double_box.get_top() + DOWN * 0.4)

        double_desc = VGroup(
            Text("两组或多组", font=FONT, font_size=20, color=WHITE),
            Text("多条折线", font=FONT, font_size=20, color=WHITE),
            Text("便于对比", font=FONT, font_size=20, color=COLOR_FORMULA),
        ).arrange(DOWN, buff=0.12).move_to(double_box.get_center() + DOWN * 0.05)

        # 复式小图示 — 两条线
        d_pts_a = [
            double_box.get_center() + LEFT * 1.0 + DOWN * 0.85,
            double_box.get_center() + LEFT * 0.3 + DOWN * 0.5,
            double_box.get_center() + RIGHT * 0.3 + DOWN * 0.7,
            double_box.get_center() + RIGHT * 1.0 + DOWN * 0.3,
        ]
        d_pts_b = [
            double_box.get_center() + LEFT * 1.0 + DOWN * 0.55,
            double_box.get_center() + LEFT * 0.3 + DOWN * 0.75,
            double_box.get_center() + RIGHT * 0.3 + DOWN * 0.45,
            double_box.get_center() + RIGHT * 1.0 + DOWN * 0.65,
        ]
        d_line_a = VMobject(color=COLOR_CITY_A, stroke_width=3)
        d_line_a.set_points_as_corners(d_pts_a)
        d_line_b = VMobject(color=COLOR_CITY_B, stroke_width=3)
        d_line_b.set_points_as_corners(d_pts_b)

        # 箭头
        arrow = Arrow(
            single_box.get_right() + RIGHT * 0.1,
            double_box.get_left() + LEFT * 0.1,
            color=COLOR_HL, stroke_width=3, buff=0.05,
            max_tip_length_to_length_ratio=0.2
        )

        self.play(FadeIn(single_box), Write(single_title), run_time=0.5)
        self.play(FadeIn(single_desc), Create(s_line), run_time=0.5)
        self.play(Create(arrow), run_time=0.4)
        self.play(FadeIn(double_box), Write(double_title), run_time=0.5)
        self.play(FadeIn(double_desc), run_time=0.4)
        self.play(Create(d_line_a), Create(d_line_b), run_time=0.6)
        self.wait(0.5)

        # 关键要素列表
        key_label = Text(
            "复式折线统计图的要素：", font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 0.5)
        elements = VGroup(
            Text("1. 标题", font=FONT, font_size=22, color=GRAY_A),
            Text("2. 横轴（类别）和纵轴（数量）", font=FONT, font_size=22, color=GRAY_A),
            Text("3. 两条不同颜色的折线", font=FONT, font_size=22, color=GRAY_A),
            Text("4. 图例（标明每条线代表什么）", font=FONT, font_size=22, color=COLOR_HL),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(DOWN * 2.2)

        self.play(Write(key_label), run_time=0.5)
        for elem in elements:
            self.play(FadeIn(elem, shift=RIGHT * 0.3), run_time=0.35)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(VGroup(
                title,
                single_box, single_title, single_desc, s_line,
                arrow,
                double_box, double_title, double_desc, d_line_a, d_line_b,
                key_label, elements
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 绘制复式折线统计图 (核心)
    # ------------------------------------------------------------------

    def scene_4_draw_double_graph(self):
        """完整绘制甲乙两城气温复式折线统计图"""

        title = Text(
            "绘制复式折线统计图", font=FONT, font_size=36,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # ===== 建立坐标系 =====
        axes = self._build_axes()
        axes.move_to(DOWN * 0.8)

        x_labels = self._add_x_labels(axes)
        grid = self._add_grid_lines(axes)

        y_title = Text("温度/°C", font=FONT, font_size=18, color=COLOR_AXIS)
        y_title.next_to(axes.y_axis.get_top(), UP, buff=0.15)

        chart_title = Text(
            "甲乙两城1-6月气温变化统计图",
            font=FONT, font_size=22, color=WHITE
        ).next_to(axes, UP, buff=0.35)

        # Step 1: 画坐标轴
        step1 = Text(
            "第一步: 画坐标轴", font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.7)
        self.play(Write(step1), run_time=0.4)
        self.play(Create(axes), FadeIn(grid), run_time=0.8)
        self.play(FadeIn(x_labels), FadeIn(y_title), Write(chart_title), run_time=0.6)
        self.wait(0.4)

        # Step 2: 描点连线 — 甲城
        step2 = Text(
            "第二步: 描点连线", font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.7)
        self.play(ReplacementTransform(step1, step2), run_time=0.3)

        line_a, dots_a = self._plot_line_with_dots(axes, TEMPS_A, COLOR_CITY_A)
        temp_labels_a = self._add_temp_labels(axes, TEMPS_A, COLOR_CITY_A, UP)

        city_a_label = Text(
            "甲城 (红色)", font=FONT, font_size=20, color=COLOR_CITY_A
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(city_a_label), run_time=0.3)

        # 逐点绘制甲城
        for i in range(len(MONTHS)):
            anims = [FadeIn(dots_a[i], scale=0.5)]
            if i > 0:
                # 绘制从前一点到当前点的线段
                seg_pts = [axes.c2p(MONTHS[i - 1], TEMPS_A[i - 1]),
                           axes.c2p(MONTHS[i], TEMPS_A[i])]
                seg = VMobject(color=COLOR_CITY_A, stroke_width=3)
                seg.set_points_as_corners(seg_pts)
                anims.append(Create(seg))
            anims.append(FadeIn(temp_labels_a[i]))
            self.play(*anims, run_time=0.35)

        # 用完整折线替换各段（已通过逐段绘制展示了过程）
        self.wait(0.3)

        # Step 3: 描点连线 — 乙城
        line_b, dots_b = self._plot_line_with_dots(axes, TEMPS_B, COLOR_CITY_B)
        temp_labels_b = self._add_temp_labels(axes, TEMPS_B, COLOR_CITY_B, DOWN * 1.2)

        # 调整乙城标签避免与甲城重叠
        for i, (ta, tb) in enumerate(zip(TEMPS_A, TEMPS_B)):
            if abs(ta - tb) <= 3:
                temp_labels_b[i].next_to(axes.c2p(MONTHS[i], tb), DOWN, buff=0.15)
            else:
                temp_labels_b[i].next_to(axes.c2p(MONTHS[i], tb), UP, buff=0.15)
        # 5月两城相同，特殊处理
        temp_labels_b[4].next_to(axes.c2p(5, 22), DOWN, buff=0.15)

        city_b_label = Text(
            "乙城 (蓝色)", font=FONT, font_size=20, color=COLOR_CITY_B
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(city_b_label), run_time=0.3)

        # 逐点绘制乙城
        for i in range(len(MONTHS)):
            anims = [FadeIn(dots_b[i], scale=0.5)]
            if i > 0:
                seg_pts = [axes.c2p(MONTHS[i - 1], TEMPS_B[i - 1]),
                           axes.c2p(MONTHS[i], TEMPS_B[i])]
                seg = VMobject(color=COLOR_CITY_B, stroke_width=3)
                seg.set_points_as_corners(seg_pts)
                anims.append(Create(seg))
            anims.append(FadeIn(temp_labels_b[i]))
            self.play(*anims, run_time=0.35)

        self.wait(0.3)

        # Step 4: 添加图例
        step3 = Text(
            "第三步: 添加图例", font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.7)
        self.play(ReplacementTransform(step2, step3), run_time=0.3)

        # 图例
        legend_box = RoundedRectangle(
            width=3.5, height=1.0, corner_radius=0.15,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_AXIS, stroke_width=1.5
        ).move_to(DOWN * 5.0)

        legend_a_line = Line(LEFT * 0.4, RIGHT * 0.4, color=COLOR_CITY_A, stroke_width=4)
        legend_a_dot = Dot(ORIGIN, radius=0.06, color=COLOR_CITY_A)
        legend_a_text = Text("甲城", font=FONT, font_size=18, color=COLOR_CITY_A)
        legend_a = VGroup(legend_a_line, legend_a_dot, legend_a_text).arrange(RIGHT, buff=0.12)

        legend_b_line = Line(LEFT * 0.4, RIGHT * 0.4, color=COLOR_CITY_B, stroke_width=4)
        legend_b_dot = Dot(ORIGIN, radius=0.06, color=COLOR_CITY_B)
        legend_b_text = Text("乙城", font=FONT, font_size=18, color=COLOR_CITY_B)
        legend_b = VGroup(legend_b_line, legend_b_dot, legend_b_text).arrange(RIGHT, buff=0.12)

        legend_content = VGroup(legend_a, legend_b).arrange(RIGHT, buff=0.8)
        legend_content.move_to(legend_box.get_center())

        # 清除之前的城市标签，替换为正式图例
        self.play(
            FadeOut(city_a_label), FadeOut(city_b_label),
            FadeIn(legend_box), FadeIn(legend_content),
            run_time=0.6
        )
        self.play(
            Indicate(legend_content, scale_factor=1.05, color=COLOR_HL),
            run_time=0.5
        )
        self.wait(1.0)

        # 保存供后续场景使用
        self.graph_group = VGroup(
            axes, grid, x_labels, y_title, chart_title,
            dots_a, dots_b,
            temp_labels_a, temp_labels_b,
            legend_box, legend_content
        )
        self.axes = axes
        self.dots_a = dots_a
        self.dots_b = dots_b
        self.temp_labels_a = temp_labels_a
        self.temp_labels_b = temp_labels_b

        # 清理步骤标签
        self.play(FadeOut(step3), run_time=0.3)

    # ------------------------------------------------------------------
    # Scene 5: 读图分析
    # ------------------------------------------------------------------

    def scene_5_analysis(self):
        """读图分析: 温差、趋势、交点"""

        title = Text(
            "读图分析", font=FONT, font_size=36,
            color=COLOR_FORMULA, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # ----- 问题1: 哪个月温差最大？ -----
        q1 = Text(
            "问题1: 哪个月温差最大？",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(UP * 4.7)
        self.play(Write(q1), run_time=0.5)

        # 计算温差并高亮1月
        diffs = [abs(a - b) for a, b in zip(TEMPS_A, TEMPS_B)]
        max_diff_idx = diffs.index(max(diffs))  # = 0 (1月, 差6°C)

        # 高亮1月的两个点 + 画温差线
        hl_dot_a = self.dots_a[max_diff_idx].copy().set_color(COLOR_DIFF).scale(1.8)
        hl_dot_b = self.dots_b[max_diff_idx].copy().set_color(COLOR_DIFF).scale(1.8)
        diff_line = Line(
            self.axes.c2p(MONTHS[max_diff_idx], TEMPS_A[max_diff_idx]),
            self.axes.c2p(MONTHS[max_diff_idx], TEMPS_B[max_diff_idx]),
            color=COLOR_DIFF, stroke_width=4
        )
        diff_label = Text(
            f"差{diffs[max_diff_idx]}°C",
            font=FONT, font_size=20, color=COLOR_DIFF, weight=BOLD
        ).next_to(diff_line, RIGHT, buff=0.15)

        self.play(
            FadeIn(hl_dot_a), FadeIn(hl_dot_b),
            Create(diff_line), run_time=0.6
        )
        self.play(FadeIn(diff_label), run_time=0.4)

        ans1 = Text(
            "1月温差最大，相差6°C",
            font=FONT, font_size=22, color=WHITE
        ).move_to(DOWN * 6.2)
        self.play(FadeIn(ans1, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清理问题1标注
        self.play(
            FadeOut(VGroup(q1, hl_dot_a, hl_dot_b, diff_line, diff_label, ans1)),
            run_time=0.4
        )

        # ----- 问题2: 何时温度相同？ -----
        q2 = Text(
            "问题2: 哪个月两城温度相同？",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(UP * 4.7)
        self.play(Write(q2), run_time=0.5)

        # 5月两城都是22°C
        cross_idx = 4  # 5月
        cross_circle = Circle(
            radius=0.3, color=COLOR_HL, stroke_width=3
        ).move_to(self.axes.c2p(5, 22))
        cross_label = Text(
            "5月: 都是22°C",
            font=FONT, font_size=20, color=COLOR_HL, weight=BOLD
        ).next_to(cross_circle, RIGHT + UP, buff=0.15)

        self.play(Create(cross_circle), run_time=0.5)
        self.play(FadeIn(cross_label), run_time=0.4)

        ans2 = Text(
            "5月两城气温相同，均为22°C",
            font=FONT, font_size=22, color=WHITE
        ).move_to(DOWN * 6.2)
        self.play(FadeIn(ans2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(q2, cross_circle, cross_label, ans2)),
            run_time=0.4
        )

        # ----- 问题3: 总体趋势如何？ -----
        q3 = Text(
            "问题3: 两城气温变化趋势？",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(UP * 4.7)
        self.play(Write(q3), run_time=0.5)

        # 趋势箭头 — 甲城上升趋势
        trend_arrow_a = Arrow(
            self.axes.c2p(1, 2) + LEFT * 0.3 + DOWN * 0.3,
            self.axes.c2p(6, 28) + RIGHT * 0.3 + UP * 0.3,
            color=COLOR_CITY_A, stroke_width=2.5, buff=0.1,
            max_tip_length_to_length_ratio=0.08
        )
        trend_lbl_a = Text(
            "甲城升温快", font=FONT, font_size=18, color=COLOR_CITY_A
        ).next_to(trend_arrow_a, RIGHT, buff=0.1)

        # 乙城上升趋势
        trend_arrow_b = Arrow(
            self.axes.c2p(1, 8) + LEFT * 0.3 + DOWN * 0.3,
            self.axes.c2p(6, 25) + RIGHT * 0.3 + UP * 0.3,
            color=COLOR_CITY_B, stroke_width=2.5, buff=0.1,
            max_tip_length_to_length_ratio=0.08
        )
        trend_lbl_b = Text(
            "乙城升温缓", font=FONT, font_size=18, color=COLOR_CITY_B
        ).next_to(trend_arrow_b, LEFT, buff=0.1)

        self.play(
            Create(trend_arrow_a), FadeIn(trend_lbl_a),
            run_time=0.6
        )
        self.play(
            Create(trend_arrow_b), FadeIn(trend_lbl_b),
            run_time=0.6
        )

        ans3 = VGroup(
            Text("两城气温均逐月上升", font=FONT, font_size=22, color=WHITE),
            Text("甲城升温幅度更大", font=FONT, font_size=22, color=COLOR_CITY_A),
        ).arrange(DOWN, buff=0.12).move_to(DOWN * 6.3)
        self.play(FadeIn(ans3, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 清理本场景分析元素
        self.play(
            FadeOut(VGroup(
                title, q3,
                trend_arrow_a, trend_lbl_a,
                trend_arrow_b, trend_lbl_b,
                ans3
            )),
            run_time=0.5
        )

        # 清理整个图表
        self.play(FadeOut(self.graph_group), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 6: 总结
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        """总结复式折线统计图的优点"""

        title = Text(
            "总结", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 核心结论框
        box = RoundedRectangle(
            width=7.8, height=5.5,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 1.5)

        box_title = Text(
            "复式折线统计图", font=FONT, font_size=32,
            color=COLOR_HL, weight=BOLD
        ).move_to(box.get_top() + DOWN * 0.5)

        points = VGroup(
            Text("用两条或多条折线表示", font=FONT, font_size=24, color=WHITE),
            Text("不同数据组的变化趋势", font=FONT, font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.1).move_to(box.get_center() + UP * 0.6)

        self.play(FadeIn(box), Write(box_title), run_time=0.6)
        self.play(FadeIn(points, shift=UP * 0.2), run_time=0.5)

        # 优点列表
        adv_title = Text(
            "优点：", font=FONT, font_size=26, color=COLOR_FORMULA
        ).move_to(box.get_center() + DOWN * 0.3 + LEFT * 2.5)

        advantages = VGroup(
            Text("1. 便于比较不同组数据", font=FONT, font_size=22, color=WHITE),
            Text("2. 直观看出变化趋势的差异", font=FONT, font_size=22, color=WHITE),
            Text("3. 容易找到交点和极值", font=FONT, font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to(
            box.get_center() + DOWN * 1.2
        )

        self.play(Write(adv_title), run_time=0.4)
        for adv in advantages:
            self.play(FadeIn(adv, shift=RIGHT * 0.3), run_time=0.35)
        self.wait(0.5)

        # 关键要素提醒
        remind_box = RoundedRectangle(
            width=7.8, height=3.2,
            corner_radius=0.3,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_FORMULA, stroke_width=2
        ).move_to(DOWN * 3.5)

        remind_title = Text(
            "绘图要素", font=FONT, font_size=26,
            color=COLOR_FORMULA, weight=BOLD
        ).move_to(remind_box.get_top() + DOWN * 0.4)

        remind_items = VGroup(
            Text("标题   横轴   纵轴", font=FONT, font_size=22, color=GRAY_A),
            Text("不同颜色的折线", font=FONT, font_size=22, color=GRAY_A),
            Text("图例（最重要！）", font=FONT, font_size=24, color=COLOR_HL, weight=BOLD),
        ).arrange(DOWN, buff=0.2).move_to(remind_box.get_center() + DOWN * 0.15)

        self.play(FadeIn(remind_box), Write(remind_title), run_time=0.5)
        for item in remind_items:
            self.play(FadeIn(item, shift=UP * 0.2), run_time=0.35)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, box, box_title, points,
                adv_title, advantages,
                remind_box, remind_title, remind_items
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        """作者信息放大 + 关注提示"""

        # 作者名放大居中
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

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰: 6个小圆点，双色交替，围绕旋转
        colors = [COLOR_CITY_A, COLOR_CITY_B, COLOR_FORMULA,
                  COLOR_DIFF, COLOR_SINGLE, COLOR_HL]
        mini_dots = VGroup(*[
            Dot(
                point=DOWN * 2.8 + np.array([
                    np.cos(i * PI / 3) * 2.2,
                    np.sin(i * PI / 3) * 0.7,
                    0.0
                ]),
                radius=0.12,
                color=c
            )
            for i, c in enumerate(colors)
        ])
        self.play(*[FadeIn(d, scale=0.3) for d in mini_dots], run_time=0.5)
        self.play(Rotate(mini_dots, angle=2 * PI / 3, run_time=1.2, rate_func=smooth))
        self.wait(0.8)

        # 全部淡出
        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, mini_dots)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 001_复式折线统计图.py DoubleLineGraphLesson
#   高质量:    manim -qh  001_复式折线统计图.py DoubleLineGraphLesson
#   4K:        manim -qk  001_复式折线统计图.py DoubleLineGraphLesson
# ======================================================================
