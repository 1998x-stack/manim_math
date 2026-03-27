"""
复式条形统计图 - Double Bar Chart Animation
小学四年级第一学期 第六章整理与提高

内容: 在单式条形图基础上，学习用不同颜色表示不同类别数据，进行对比分析
目标观众: 四年级小学生
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


class DoubleBarChartLesson(Scene):
    """
    复式条形统计图教学动画场景

    场景顺序:
    1. 开场钩子 - 引出问题
    2. 单式条形图回顾
    3. 复式条形图介绍
    4. 图例与读图方法
    5. 对比分析
    6. 知识要点总结
    7. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.COLOR_BOY = "#4a90e2"        # 蓝色 - 男生
        self.COLOR_GIRL = "#e74c8b"       # 粉色 - 女生
        self.COLOR_AXIS = "#b0bec5"       # 轴线颜色
        self.COLOR_TITLE = "#f5c842"      # 标题金色
        self.COLOR_HIGHLIGHT = "#2ecc71"  # 绿色高亮
        self.COLOR_TEXT = "#ecf0f1"       # 正文白色
        self.COLOR_GRID = "#2d3561"       # 网格线颜色

        # 数据定义
        self.subjects = ["语文", "数学", "英语", "科学", "体育"]
        self.boys_scores = [85, 92, 78, 88, 95]
        self.girls_scores = [90, 86, 94, 82, 88]

        # 执行各场景
        self.scene_1_opening()
        self.scene_2_single_bar_review()
        self.scene_3_double_bar_intro()
        self.scene_4_legend_and_reading()
        self.scene_5_comparison_analysis()
        self.scene_6_summary()
        self.scene_7_outro()

    # ─────────────────────────────────────────────
    # 辅助方法
    # ─────────────────────────────────────────────

    def make_bar_chart(
        self,
        data_sets,
        colors,
        labels,
        chart_origin,
        chart_width=6.5,
        chart_height=4.0,
        y_max=100,
        y_step=20,
        bar_gap=0.06,
        group_gap=0.25,
        show_values=False,
        font_size_axis=17,
    ):
        """
        手工绘制复式条形图。
        返回 (all_objects_vgroup, bars_list, value_labels_vgroup)
        """
        n_groups = len(labels)
        n_bars = len(data_sets)

        # 轴
        x_axis = Line(
            chart_origin,
            chart_origin + RIGHT * chart_width,
            color=self.COLOR_AXIS,
            stroke_width=2.5,
        )
        y_axis = Line(
            chart_origin,
            chart_origin + UP * chart_height,
            color=self.COLOR_AXIS,
            stroke_width=2.5,
        )

        axis_group = VGroup(x_axis, y_axis)
        tick_group = VGroup()
        grid_group = VGroup()
        tick_label_group = VGroup()

        # y轴刻度和网格线
        n_ticks = int(y_max / y_step)
        for i in range(1, n_ticks + 1):
            y_val = i * y_step
            y_pos = chart_origin[1] + (y_val / y_max) * chart_height

            tick = Line(
                np.array([chart_origin[0] - 0.12, y_pos, 0]),
                np.array([chart_origin[0], y_pos, 0]),
                color=self.COLOR_AXIS,
                stroke_width=1.5,
            )
            grid_line = DashedLine(
                np.array([chart_origin[0], y_pos, 0]),
                np.array([chart_origin[0] + chart_width, y_pos, 0]),
                color=self.COLOR_GRID,
                stroke_width=1,
                dash_length=0.15,
            )
            tick_label = Text(
                str(y_val),
                font="Noto Sans CJK SC",
                font_size=font_size_axis,
                color=self.COLOR_AXIS,
            ).next_to(tick, LEFT, buff=0.08)

            tick_group.add(tick)
            grid_group.add(grid_line)
            tick_label_group.add(tick_label)

        # 计算每个分组宽度
        group_width = chart_width / n_groups

        bars_list = []
        value_labels = VGroup()
        x_labels_group = VGroup()

        for g_idx, label in enumerate(labels):
            total_bar_span = group_width - group_gap
            bar_width = (total_bar_span - bar_gap * (n_bars - 1)) / n_bars
            group_x_start = chart_origin[0] + g_idx * group_width + group_gap / 2

            # x轴标签中心
            x_center = group_x_start + total_bar_span / 2
            x_lbl = Text(
                label,
                font="Noto Sans CJK SC",
                font_size=font_size_axis,
                color=self.COLOR_TEXT,
            ).move_to(np.array([x_center, chart_origin[1] - 0.32, 0]))
            x_labels_group.add(x_lbl)

            for d_idx, (data, color) in enumerate(zip(data_sets, colors)):
                val = data[g_idx]
                bar_h = (val / y_max) * chart_height
                bar_x = group_x_start + d_idx * (bar_width + bar_gap)

                bar = Rectangle(
                    width=bar_width,
                    height=bar_h,
                    fill_color=color,
                    fill_opacity=0.85,
                    stroke_color=color,
                    stroke_width=1,
                ).move_to(
                    np.array([
                        bar_x + bar_width / 2,
                        chart_origin[1] + bar_h / 2,
                        0,
                    ])
                )
                bars_list.append(bar)

                if show_values:
                    val_lbl = Text(
                        str(val),
                        font="Noto Sans CJK SC",
                        font_size=15,
                        color=color,
                    ).move_to(
                        np.array([
                            bar_x + bar_width / 2,
                            chart_origin[1] + bar_h + 0.22,
                            0,
                        ])
                    )
                    value_labels.add(val_lbl)

        bars_vgroup = VGroup(*bars_list)
        all_objects = VGroup(
            axis_group,
            tick_group,
            grid_group,
            tick_label_group,
            x_labels_group,
        )

        return all_objects, bars_list, value_labels

    def make_legend(self, position, items):
        """创建图例。items: [(color, label_text), ...]"""
        legend = VGroup()
        for color, lbl_str in items:
            rect = Rectangle(
                width=0.38,
                height=0.22,
                fill_color=color,
                fill_opacity=0.9,
                stroke_color=color,
                stroke_width=1,
            )
            lbl = Text(
                lbl_str,
                font="Noto Sans CJK SC",
                font_size=20,
                color=self.COLOR_TEXT,
            )
            row = VGroup(rect, lbl).arrange(RIGHT, buff=0.15)
            legend.add(row)
        legend.arrange(RIGHT, buff=0.55)
        legend.move_to(position)
        return legend

    # ─────────────────────────────────────────────
    # 场景 1: 开场钩子
    # ─────────────────────────────────────────────

    def scene_1_opening(self):
        # 作者信息
        self.author_tag = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_tag, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook_line1 = Text(
            "男生和女生",
            font="Noto Sans CJK SC",
            font_size=46,
            color=self.COLOR_TITLE,
        ).move_to(UP * 5.2)
        hook_line2 = Text(
            "谁的成绩更好？",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_TEXT,
        ).move_to(UP * 4.3)

        self.play(Write(hook_line1), run_time=0.7)
        self.play(Write(hook_line2), run_time=0.6)

        # 两色方块代表男女
        boy_block = Rectangle(
            width=1.2, height=1.2,
            fill_color=self.COLOR_BOY,
            fill_opacity=0.9,
            stroke_width=0,
        )
        boy_block_label = Text(
            "男生", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_BOY
        )
        boy_group = VGroup(boy_block, boy_block_label).arrange(DOWN, buff=0.18)
        boy_group.move_to(LEFT * 2.0 + UP * 2.2)

        girl_block = Rectangle(
            width=1.2, height=1.2,
            fill_color=self.COLOR_GIRL,
            fill_opacity=0.9,
            stroke_width=0,
        )
        girl_block_label = Text(
            "女生", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_GIRL
        )
        girl_group = VGroup(girl_block, girl_block_label).arrange(DOWN, buff=0.18)
        girl_group.move_to(RIGHT * 2.0 + UP * 2.2)

        vs_text = Text(
            "VS", font="Noto Sans CJK SC", font_size=38, color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)

        self.play(
            FadeIn(boy_group, shift=RIGHT * 0.3),
            FadeIn(girl_group, shift=LEFT * 0.3),
            run_time=0.6,
        )
        self.play(Write(vs_text), run_time=0.4)

        guide = Text(
            "用复式条形统计图来看看！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 0.8)
        self.play(FadeIn(guide, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            FadeOut(boy_group),
            FadeOut(girl_group),
            FadeOut(vs_text),
            FadeOut(guide),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # 场景 2: 单式条形图回顾
    # ─────────────────────────────────────────────

    def scene_2_single_bar_review(self):
        title = Text(
            "单式条形统计图",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.COLOR_TITLE,
        ).move_to(UP * 5.8)

        subtitle = Text(
            "只能表示一组数据",
            font="Noto Sans CJK SC",
            font_size=24,
            color="#aab0bb",
        ).move_to(UP * 5.1)

        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 只画男生的单式条形图
        chart_origin = np.array([-3.5, -2.8, 0])

        chart_axes, bars_list, val_labels = self.make_bar_chart(
            data_sets=[self.boys_scores],
            colors=[self.COLOR_BOY],
            labels=self.subjects,
            chart_origin=chart_origin,
            chart_width=6.8,
            chart_height=4.0,
            y_max=100,
            y_step=20,
            bar_gap=0.0,
            group_gap=0.35,
            show_values=True,
            font_size_axis=17,
        )

        chart_title = Text(
            "男生各科成绩统计图",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_BOY,
        ).move_to(np.array([chart_origin[0] + 3.4, chart_origin[1] + 4.6, 0]))

        y_label = Text(
            "分数",
            font="Noto Sans CJK SC",
            font_size=17,
            color=self.COLOR_AXIS,
        ).move_to(np.array([chart_origin[0] - 0.65, chart_origin[1] + 2.0, 0]))

        self.play(Create(chart_axes[0]), run_time=0.5)  # 轴
        self.play(
            FadeIn(chart_axes[1]),  # 刻度
            FadeIn(chart_axes[2]),  # 网格
            FadeIn(chart_axes[3]),  # 刻度数字
            FadeIn(chart_axes[4]),  # x标签
            FadeIn(chart_title),
            FadeIn(y_label),
            run_time=0.5,
        )

        # 条形从底部升起
        bars_vgroup = VGroup(*bars_list)
        for bar in bars_list:
            bar.save_state()
            orig_h = bar.height
            bar.stretch_to_fit_height(0.01)
            bar.align_to(chart_origin, DOWN)

        self.play(
            *[bar.animate.restore() for bar in bars_list],
            run_time=1.2,
            lag_ratio=0.15,
        )
        self.play(FadeIn(val_labels), run_time=0.4)
        self.wait(0.5)

        problem = Text(
            "问题：女生的数据放哪里？",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_GIRL,
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(problem, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(chart_axes),
            FadeOut(bars_vgroup),
            FadeOut(val_labels),
            FadeOut(chart_title),
            FadeOut(y_label),
            FadeOut(problem),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # 场景 3: 复式条形图介绍
    # ─────────────────────────────────────────────

    def scene_3_double_bar_intro(self):
        self._scene3_title = Text(
            "复式条形统计图",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_TITLE,
        ).move_to(UP * 5.8)

        self._scene3_subtitle = Text(
            "同时表示多组数据，方便对比！",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.1)

        self.play(Write(self._scene3_title), run_time=0.6)
        self.play(FadeIn(self._scene3_subtitle), run_time=0.4)

        # 复式条形图
        self._chart_origin = np.array([-3.6, -3.3, 0])

        chart_axes, bars_list, _ = self.make_bar_chart(
            data_sets=[self.boys_scores, self.girls_scores],
            colors=[self.COLOR_BOY, self.COLOR_GIRL],
            labels=self.subjects,
            chart_origin=self._chart_origin,
            chart_width=7.0,
            chart_height=4.0,
            y_max=100,
            y_step=20,
            bar_gap=0.05,
            group_gap=0.18,
            show_values=False,
            font_size_axis=16,
        )

        self._chart_axes = chart_axes
        self._bars_list = bars_list

        # 分离男生/女生条形
        self._boy_bars = [bars_list[i] for i in range(0, len(bars_list), 2)]
        self._girl_bars = [bars_list[i] for i in range(1, len(bars_list), 2)]

        self._y_label = Text(
            "分数",
            font="Noto Sans CJK SC",
            font_size=17,
            color=self.COLOR_AXIS,
        ).move_to(np.array([self._chart_origin[0] - 0.65, self._chart_origin[1] + 2.0, 0]))

        self._legend = self.make_legend(
            position=np.array([0.0, self._chart_origin[1] - 0.72, 0]),
            items=[(self.COLOR_BOY, "男生"), (self.COLOR_GIRL, "女生")],
        )

        # 显示轴与网格
        self.play(Create(chart_axes[0]), FadeIn(self._y_label), run_time=0.5)
        self.play(
            FadeIn(chart_axes[1]),
            FadeIn(chart_axes[2]),
            FadeIn(chart_axes[3]),
            FadeIn(chart_axes[4]),
            run_time=0.4,
        )

        # 男生条形升起
        for bar in self._boy_bars:
            bar.save_state()
            bar.stretch_to_fit_height(0.01)
            bar.align_to(self._chart_origin, DOWN)

        boy_tip = Text(
            "蓝色 = 男生数据",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_BOY,
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(boy_tip), run_time=0.3)
        self.play(
            *[bar.animate.restore() for bar in self._boy_bars],
            run_time=1.0,
            lag_ratio=0.15,
        )
        self.wait(0.4)

        # 女生条形升起
        for bar in self._girl_bars:
            bar.save_state()
            bar.stretch_to_fit_height(0.01)
            bar.align_to(self._chart_origin, DOWN)

        girl_tip = Text(
            "粉色 = 女生数据",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_GIRL,
        ).move_to(DOWN * 4.5)
        self.play(ReplacementTransform(boy_tip, girl_tip), run_time=0.3)
        self.play(
            *[bar.animate.restore() for bar in self._girl_bars],
            run_time=1.0,
            lag_ratio=0.15,
        )
        self.wait(0.3)

        # 显示图例
        self.play(FadeOut(girl_tip), FadeIn(self._legend), run_time=0.4)
        self.wait(1.0)

    # ─────────────────────────────────────────────
    # 场景 4: 图例与读图
    # ─────────────────────────────────────────────

    def scene_4_legend_and_reading(self):
        new_title = Text(
            "如何读图？",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_TITLE,
        ).move_to(UP * 5.8)

        self.play(
            ReplacementTransform(self._scene3_title, new_title),
            FadeOut(self._scene3_subtitle),
            run_time=0.5,
        )

        step1 = Text(
            "① 看图例：蓝=男生，粉=女生",
            font="Noto Sans CJK SC",
            font_size=21,
            color=self.COLOR_TEXT,
        ).move_to(UP * 5.08)
        self.play(FadeIn(step1, shift=RIGHT * 0.3), run_time=0.4)

        legend_box = SurroundingRectangle(
            self._legend, color=self.COLOR_HIGHLIGHT, stroke_width=2, buff=0.1
        )
        self.play(Create(legend_box), run_time=0.4)
        self.wait(0.4)
        self.play(FadeOut(legend_box), run_time=0.3)

        step2 = Text(
            "② 找科目：看横轴的类别名称",
            font="Noto Sans CJK SC",
            font_size=21,
            color=self.COLOR_TEXT,
        ).move_to(UP * 4.55)
        self.play(FadeIn(step2, shift=RIGHT * 0.3), run_time=0.4)

        # 高亮"数学"那一组（index=1）
        math_boy_bar = self._boy_bars[1]
        math_girl_bar = self._girl_bars[1]
        highlight_box = SurroundingRectangle(
            VGroup(math_boy_bar, math_girl_bar),
            color=self.COLOR_TITLE,
            stroke_width=2.5,
            buff=0.08,
        )
        math_label = Text(
            "数学", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_TITLE
        ).next_to(highlight_box, DOWN, buff=0.1)
        self.play(Create(highlight_box), Write(math_label), run_time=0.4)
        self.wait(0.5)

        step3 = Text(
            "③ 读高度：对应纵轴的数值",
            font="Noto Sans CJK SC",
            font_size=21,
            color=self.COLOR_TEXT,
        ).move_to(UP * 4.05)
        self.play(
            FadeOut(highlight_box),
            FadeOut(math_label),
            FadeIn(step3, shift=RIGHT * 0.3),
            run_time=0.4,
        )

        # 虚线标出数学成绩
        co = self._chart_origin
        boy_top = math_boy_bar.get_top()
        girl_top = math_girl_bar.get_top()

        boy_h_line = DashedLine(
            np.array([co[0], boy_top[1], 0]),
            np.array([boy_top[0], boy_top[1], 0]),
            color=self.COLOR_BOY, stroke_width=2, dash_length=0.12,
        )
        girl_h_line = DashedLine(
            np.array([co[0], girl_top[1], 0]),
            np.array([girl_top[0], girl_top[1], 0]),
            color=self.COLOR_GIRL, stroke_width=2, dash_length=0.12,
        )
        boy_score_lbl = Text(
            "92分", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_BOY
        ).next_to(math_boy_bar, UP, buff=0.1)
        girl_score_lbl = Text(
            "86分", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_GIRL
        ).next_to(math_girl_bar, UP, buff=0.1)

        self.play(Create(boy_h_line), Create(girl_h_line), run_time=0.5)
        self.play(FadeIn(boy_score_lbl), FadeIn(girl_score_lbl), run_time=0.4)

        read_result = Text(
            "数学：男生92分，女生86分",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(read_result, shift=UP * 0.3), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(step1), FadeOut(step2), FadeOut(step3),
            FadeOut(boy_h_line), FadeOut(girl_h_line),
            FadeOut(boy_score_lbl), FadeOut(girl_score_lbl),
            FadeOut(read_result), FadeOut(new_title),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # 场景 5: 对比分析
    # ─────────────────────────────────────────────

    def scene_5_comparison_analysis(self):
        title = Text(
            "对比分析",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_TITLE,
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        comparisons = [
            ("语文", 85, 90, self.COLOR_GIRL, "女生领先"),
            ("数学", 92, 86, self.COLOR_BOY, "男生领先"),
            ("英语", 78, 94, self.COLOR_GIRL, "女生领先"),
            ("科学", 88, 82, self.COLOR_BOY, "男生领先"),
            ("体育", 95, 88, self.COLOR_BOY, "男生领先"),
        ]

        for i, (subject, boy_s, girl_s, winner_color, winner_text) in enumerate(comparisons):
            boy_bar = self._boy_bars[i]
            girl_bar = self._girl_bars[i]

            highlight = SurroundingRectangle(
                VGroup(boy_bar, girl_bar),
                color=self.COLOR_TITLE, stroke_width=2, buff=0.05,
            )

            boy_val = Text(
                f"男: {boy_s}分",
                font="Noto Sans CJK SC", font_size=22, color=self.COLOR_BOY,
            )
            girl_val = Text(
                f"女: {girl_s}分",
                font="Noto Sans CJK SC", font_size=22, color=self.COLOR_GIRL,
            )
            compare_row = VGroup(boy_val, girl_val).arrange(RIGHT, buff=0.5)
            compare_row.move_to(UP * 5.05)

            winner_label = Text(
                winner_text,
                font="Noto Sans CJK SC", font_size=28, color=winner_color,
            ).move_to(UP * 4.38)

            self.play(Create(highlight), FadeIn(compare_row), run_time=0.35)
            self.play(FadeIn(winner_label, shift=UP * 0.2), run_time=0.3)
            self.wait(0.45)
            self.play(FadeOut(highlight), FadeOut(compare_row), FadeOut(winner_label), run_time=0.25)

        # 综合结论
        boy_total = sum(self.boys_scores)
        girl_total = sum(self.girls_scores)
        boy_avg = boy_total / len(self.boys_scores)
        girl_avg = girl_total / len(self.girls_scores)

        conclusion_bg = Rectangle(
            width=7.2, height=2.4,
            fill_color="#0d1b3e", fill_opacity=0.95,
            stroke_color=self.COLOR_HIGHLIGHT, stroke_width=2,
        ).move_to(UP * 4.62)

        conclusion_title = Text(
            "综合结论",
            font="Noto Sans CJK SC", font_size=26, color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.42)

        boy_stat = Text(
            f"男生总分：{boy_total}分  平均：{boy_avg:.0f}分",
            font="Noto Sans CJK SC", font_size=21, color=self.COLOR_BOY,
        ).move_to(UP * 4.85)
        girl_stat = Text(
            f"女生总分：{girl_total}分  平均：{girl_avg:.0f}分",
            font="Noto Sans CJK SC", font_size=21, color=self.COLOR_GIRL,
        ).move_to(UP * 4.32)

        if boy_avg > girl_avg:
            final_text = Text(
                "男生平均分更高！",
                font="Noto Sans CJK SC", font_size=24, color=self.COLOR_BOY,
            )
        else:
            final_text = Text(
                "女生平均分更高！",
                font="Noto Sans CJK SC", font_size=24, color=self.COLOR_GIRL,
            )
        final_text.move_to(UP * 3.78)

        self.play(FadeIn(conclusion_bg), run_time=0.3)
        self.play(FadeIn(conclusion_title), FadeIn(boy_stat), FadeIn(girl_stat), run_time=0.5)
        self.play(FadeIn(final_text, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(conclusion_bg),
            FadeOut(conclusion_title),
            FadeOut(boy_stat),
            FadeOut(girl_stat),
            FadeOut(final_text),
            FadeOut(self._chart_axes),
            FadeOut(VGroup(*self._bars_list)),
            FadeOut(self._legend),
            FadeOut(self._y_label),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────
    # 场景 6: 知识要点总结
    # ─────────────────────────────────────────────

    def scene_6_summary(self):
        title = Text(
            "知识要点",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_TITLE,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        points_data = [
            ("①", "复式条形图可同时\n显示多组数据", self.COLOR_BOY),
            ("②", "不同颜色区分\n不同数据组", self.COLOR_GIRL),
            ("③", "必须有图例说明\n颜色含义", self.COLOR_HIGHLIGHT),
            ("④", "横轴=类别\n纵轴=数量", self.COLOR_TITLE),
            ("⑤", "方便进行\n数据对比分析", self.COLOR_HIGHLIGHT),
        ]

        point_groups = VGroup()
        for num_str, text_str, color in points_data:
            num_t = Text(
                num_str, font="Noto Sans CJK SC", font_size=30, color=color,
            )
            content_t = Text(
                text_str, font="Noto Sans CJK SC", font_size=22,
                color=self.COLOR_TEXT, line_spacing=1.2,
            )
            row = VGroup(num_t, content_t).arrange(RIGHT, buff=0.3, aligned_edge=UP)
            point_groups.add(row)

        point_groups.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        point_groups.move_to(UP * 0.5 + LEFT * 0.5)

        for pg in point_groups:
            self.play(FadeIn(pg, shift=RIGHT * 0.4), run_time=0.38)
            self.wait(0.15)

        self.wait(1.2)

        # 小练习
        practice_bg = Rectangle(
            width=7.4, height=1.5,
            fill_color="#1e3a5f", fill_opacity=0.9,
            stroke_color=self.COLOR_BOY, stroke_width=2,
        ).move_to(DOWN * 5.0)
        practice_q1 = Text(
            "练一练：", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_TITLE,
        )
        practice_q2 = Text(
            "哪科男女差距最大？", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_TEXT,
        )
        practice_row = VGroup(practice_q1, practice_q2).arrange(RIGHT, buff=0.15)
        practice_row.move_to(practice_bg.get_center())

        self.play(FadeIn(practice_bg), FadeIn(practice_row), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title),
            FadeOut(point_groups),
            FadeOut(practice_bg),
            FadeOut(practice_row),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # 场景 7: 片尾
    # ─────────────────────────────────────────────

    def scene_7_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC", font_size=36, color=WHITE,
        ).move_to(UP * 1.5)
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC", font_size=28, color="#aab0bb",
        ).move_to(UP * 0.7)
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="Noto Sans CJK SC", font_size=30, color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.2)

        # 装饰小条形图
        deco_bars = VGroup()
        heights_deco = [0.5, 0.9, 0.7, 1.2, 0.4, 0.8, 0.65, 1.0]
        deco_colors = [self.COLOR_BOY, self.COLOR_GIRL] * 4
        for i, (h, c) in enumerate(zip(heights_deco, deco_colors)):
            bar = Rectangle(
                width=0.28, height=h,
                fill_color=c, fill_opacity=0.75, stroke_width=0,
            ).move_to(np.array([-1.65 + i * 0.48, -2.4 + h / 2, 0]))
            deco_bars.add(bar)

        self.play(Transform(self.author_tag, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.5)
        self.play(
            *[FadeIn(bar, shift=UP * 0.4) for bar in deco_bars],
            run_time=0.8, lag_ratio=0.1,
        )

        tip = Text(
            "复式条形图 = 多组数据对比神器",
            font="Noto Sans CJK SC", font_size=20, color="#aab0bb",
        ).move_to(DOWN * 4.3)
        self.play(FadeIn(tip), run_time=0.4)

        self.wait(1.8)

        self.play(
            FadeOut(self.author_tag),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(deco_bars),
            FadeOut(tip),
            run_time=0.8,
        )
