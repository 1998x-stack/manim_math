"""
年、月、日 - 三年级时间知识教学动画
知识点：大月、小月、平月、平年、闰年
格式：TikTok竖屏 (1080×1920)
作者：上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class YearMonthDayLesson(Scene):
    """
    年、月、日教学动画

    场景顺序：
    1. 开场钩子
    2. 一年12个月
    3. 大月（31天）
    4. 小月（30天）
    5. 2月（平月）
    6. 平年与闰年
    7. 判断闰年方法
    8. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.COLOR_BIG_MONTH = "#e74c3c"    # 大月 - 红色
        self.COLOR_SMALL_MONTH = "#3498db"  # 小月 - 蓝色
        self.COLOR_FEB = "#f39c12"          # 2月 - 橙色
        self.COLOR_LEAP = "#2ecc71"         # 闰年 - 绿色
        self.COLOR_NORMAL = "#9b59b6"       # 平年 - 紫色
        self.COLOR_TITLE = "#f1c40f"        # 标题 - 金色
        self.COLOR_HIGHLIGHT = "#f1c40f"    # 高亮 - 金色

        # 月份天数数据
        self.months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.month_names = ["1月", "2月", "3月", "4月", "5月", "6月",
                            "7月", "8月", "9月", "10月", "11月", "12月"]

        # 执行各场景
        self.scene_opening()
        self.scene_twelve_months()
        self.scene_big_months()
        self.scene_small_months()
        self.scene_february()
        self.scene_normal_vs_leap()
        self.scene_leap_rule()
        self.scene_outro()

    # ─────────────────────────────────────────
    # 场景1：开场钩子
    # ─────────────────────────────────────────
    def scene_opening(self):
        # 作者信息（顶部固定）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Heiti SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook = Text(
            "你知道一年有几天吗？",
            font="Heiti SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.2)

        sub_hook = Text(
            "平年？还是闰年？",
            font="Heiti SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 4.3)

        self.play(Write(hook), run_time=0.9)
        self.play(FadeIn(sub_hook, shift=UP * 0.3), run_time=0.5)

        # 大标题
        title = Text(
            "年  月  日",
            font="Heiti SC",
            font_size=72,
            color=self.COLOR_TITLE
        ).move_to(UP * 2.5)

        subtitle = Text(
            "三年级 · 时间的认识",
            font="Heiti SC",
            font_size=26,
            color="#9ca3af"
        ).move_to(UP * 1.3)

        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(subtitle), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(sub_hook),
            FadeOut(title),
            FadeOut(subtitle),
            run_time=0.6
        )

    # ─────────────────────────────────────────
    # 场景2：一年12个月
    # ─────────────────────────────────────────
    def scene_twelve_months(self):
        # 场景标题
        scene_title = Text(
            "一年有12个月",
            font="Heiti SC",
            font_size=44,
            color=self.COLOR_TITLE
        ).move_to(UP * 5.8)

        self.play(Write(scene_title), run_time=0.7)

        # 公式
        formula_label = Text(
            "1年 = 12个月",
            font="Heiti SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 4.8)

        self.play(FadeIn(formula_label, shift=UP * 0.3), run_time=0.6)

        # 绘制12格月份格子（4列×3行）
        month_rects = VGroup()
        month_texts = VGroup()

        cols, rows = 4, 3
        cell_w, cell_h = 1.8, 1.1
        start_x = -(cols - 1) * cell_w / 2
        start_y = 2.8

        for idx in range(12):
            r = idx // cols
            c = idx % cols
            cx = start_x + c * cell_w
            cy = start_y - r * cell_h

            days = self.months_days[idx]
            if days == 31:
                fill_col = self.COLOR_BIG_MONTH
            elif days == 30:
                fill_col = self.COLOR_SMALL_MONTH
            else:
                fill_col = self.COLOR_FEB

            rect = Rectangle(
                width=cell_w - 0.12,
                height=cell_h - 0.12,
                fill_color=fill_col,
                fill_opacity=0.25,
                stroke_color=fill_col,
                stroke_width=2
            ).move_to(np.array([cx, cy, 0]))

            month_text = Text(
                self.month_names[idx],
                font="Heiti SC",
                font_size=22,
                color=WHITE
            ).move_to(np.array([cx, cy + 0.18, 0]))

            days_text = Text(
                f"{days}天",
                font="Heiti SC",
                font_size=17,
                color=fill_col
            ).move_to(np.array([cx, cy - 0.22, 0]))

            month_rects.add(rect)
            month_texts.add(VGroup(month_text, days_text))

        # 逐行动画显示
        for row_idx in range(3):
            row_rects = VGroup(*[month_rects[row_idx * 4 + c] for c in range(4)])
            row_texts = VGroup(*[month_texts[row_idx * 4 + c] for c in range(4)])
            self.play(
                LaggedStart(*[FadeIn(r, scale=0.8) for r in row_rects], lag_ratio=0.15),
                run_time=0.7
            )
            self.play(
                LaggedStart(*[Write(t) for t in row_texts], lag_ratio=0.12),
                run_time=0.6
            )

        self.wait(1.0)

        # 图例
        legend = VGroup()
        for label, col in [("大月(31天)", self.COLOR_BIG_MONTH),
                            ("小月(30天)", self.COLOR_SMALL_MONTH),
                            ("2月(28/29天)", self.COLOR_FEB)]:
            dot = Circle(radius=0.1, fill_color=col, fill_opacity=1,
                         stroke_width=0)
            txt = Text(label, font="Heiti SC",
                       font_size=19, color=col)
            item = VGroup(dot, txt).arrange(RIGHT, buff=0.15)
            legend.add(item)
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(DOWN * 4.2 + LEFT * 1.5)

        self.play(FadeIn(legend, shift=UP * 0.3), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(scene_title),
            FadeOut(formula_label),
            FadeOut(month_rects),
            FadeOut(month_texts),
            FadeOut(legend),
            run_time=0.6
        )

    # ─────────────────────────────────────────
    # 场景3：大月（31天）
    # ─────────────────────────────────────────
    def scene_big_months(self):
        scene_title = Text(
            "大月 = 31天",
            font="Heiti SC",
            font_size=48,
            color=self.COLOR_BIG_MONTH
        ).move_to(UP * 5.8)
        self.play(Write(scene_title), run_time=0.6)

        # 大月列表
        big_months = ["1月", "3月", "5月", "7月", "8月", "10月", "12月"]
        subtitle = Text(
            "共 7 个大月",
            font="Heiti SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 4.9)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 展示大月方块
        big_rects = VGroup()
        for i, name in enumerate(big_months):
            rect = Rectangle(
                width=1.7, height=1.5,
                fill_color=self.COLOR_BIG_MONTH,
                fill_opacity=0.3,
                stroke_color=self.COLOR_BIG_MONTH,
                stroke_width=2.5
            )
            txt = Text(name, font="Heiti SC", font_size=24, color=WHITE)
            days_t = Text("31天", font="Heiti SC",
                          font_size=19, color=self.COLOR_BIG_MONTH)
            item = VGroup(txt, days_t).arrange(DOWN, buff=0.1)
            card = VGroup(rect, item)
            big_rects.add(card)

        # 排列成两行：4+3
        row1 = VGroup(*big_rects[:4]).arrange(RIGHT, buff=0.2)
        row2 = VGroup(*big_rects[4:]).arrange(RIGHT, buff=0.2)
        grid = VGroup(row1, row2).arrange(DOWN, buff=0.3).move_to(UP * 2.8)

        self.play(
            LaggedStart(*[FadeIn(c, scale=0.8) for c in big_rects], lag_ratio=0.12),
            run_time=1.2
        )

        # 口诀
        mnemonic_title = Text(
            "记忆口诀",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.0)

        mnemonic_line1 = Text(
            "一三五七八十腊，",
            font="Heiti SC",
            font_size=34,
            color=self.COLOR_BIG_MONTH
        ).move_to(DOWN * 0.8)

        mnemonic_line2 = Text(
            "三十一天永不差！",
            font="Heiti SC",
            font_size=34,
            color=self.COLOR_BIG_MONTH
        ).move_to(DOWN * 1.6)

        note = Text(
            "（腊 = 12月）",
            font="Heiti SC",
            font_size=22,
            color="#9ca3af"
        ).move_to(DOWN * 2.4)

        self.play(FadeIn(mnemonic_title), run_time=0.4)
        self.play(Write(mnemonic_line1), run_time=0.8)
        self.play(Write(mnemonic_line2), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)

        # 高亮各大月
        self.play(
            LaggedStart(*[Indicate(c, color=self.COLOR_HIGHLIGHT, scale_factor=1.1)
                          for c in big_rects], lag_ratio=0.1),
            run_time=1.5
        )
        self.wait(1.0)

        self.play(
            FadeOut(scene_title), FadeOut(subtitle),
            FadeOut(big_rects),
            FadeOut(mnemonic_title), FadeOut(mnemonic_line1),
            FadeOut(mnemonic_line2), FadeOut(note),
            run_time=0.6
        )

    # ─────────────────────────────────────────
    # 场景4：小月（30天）
    # ─────────────────────────────────────────
    def scene_small_months(self):
        scene_title = Text(
            "小月 = 30天",
            font="Heiti SC",
            font_size=48,
            color=self.COLOR_SMALL_MONTH
        ).move_to(UP * 5.8)
        self.play(Write(scene_title), run_time=0.6)

        small_months = ["4月", "6月", "9月", "11月"]
        subtitle = Text(
            "共 4 个小月",
            font="Heiti SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 4.9)
        self.play(FadeIn(subtitle), run_time=0.4)

        small_rects = VGroup()
        for name in small_months:
            rect = Rectangle(
                width=2.0, height=1.8,
                fill_color=self.COLOR_SMALL_MONTH,
                fill_opacity=0.3,
                stroke_color=self.COLOR_SMALL_MONTH,
                stroke_width=2.5
            )
            txt = Text(name, font="Heiti SC", font_size=26, color=WHITE)
            days_t = Text("30天", font="Heiti SC",
                          font_size=21, color=self.COLOR_SMALL_MONTH)
            item = VGroup(txt, days_t).arrange(DOWN, buff=0.12)
            card = VGroup(rect, item)
            small_rects.add(card)

        small_rects.arrange(RIGHT, buff=0.35).move_to(UP * 3.0)

        self.play(
            LaggedStart(*[FadeIn(c, scale=0.8) for c in small_rects], lag_ratio=0.18),
            run_time=1.0
        )

        # 简单记忆法
        tip_bg = Rectangle(
            width=7.5, height=2.8,
            fill_color="#16213e",
            fill_opacity=1,
            stroke_color=self.COLOR_SMALL_MONTH,
            stroke_width=2
        ).move_to(DOWN * 0.5)

        tip_title = Text(
            "记忆技巧",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.1)  # will be repositioned

        tip_content = Text(
            "四六九十一 = 小月(30天)\n除了2月，其余都是大月",
            font="Heiti SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 1.0)

        self.play(FadeIn(tip_bg), run_time=0.4)
        self.play(Write(tip_title.move_to(DOWN * 0.1 + UP * 0.9)), run_time=0.4)
        self.play(Write(tip_content), run_time=0.8)

        # 汇总对比
        compare = VGroup()
        for label, count, col in [
            ("大月", "7个", self.COLOR_BIG_MONTH),
            ("小月", "4个", self.COLOR_SMALL_MONTH),
            ("2月", "1个", self.COLOR_FEB),
        ]:
            l_text = Text(f"{label}：{count}", font="Heiti SC",
                          font_size=24, color=col)
            compare.add(l_text)
        compare.arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(DOWN * 3.5)

        self.play(LaggedStart(*[FadeIn(c) for c in compare], lag_ratio=0.2), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(scene_title), FadeOut(subtitle),
            FadeOut(small_rects),
            FadeOut(tip_bg), FadeOut(tip_title), FadeOut(tip_content),
            FadeOut(compare),
            run_time=0.6
        )

    # ─────────────────────────────────────────
    # 场景5：2月（平月）
    # ─────────────────────────────────────────
    def scene_february(self):
        scene_title = Text(
            "特殊的 2 月",
            font="Heiti SC",
            font_size=48,
            color=self.COLOR_FEB
        ).move_to(UP * 5.8)
        self.play(Write(scene_title), run_time=0.6)

        # 大圆形展示2月
        circle = Circle(
            radius=2.2,
            fill_color=self.COLOR_FEB,
            fill_opacity=0.18,
            stroke_color=self.COLOR_FEB,
            stroke_width=3
        ).move_to(UP * 3.0)

        feb_label = Text(
            "2月",
            font="Heiti SC",
            font_size=72,
            color=self.COLOR_FEB
        ).move_to(UP * 3.4)

        q_mark = Text(
            "28天 或 29天",
            font="Heiti SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 2.5)

        self.play(Create(circle), run_time=0.8)
        self.play(Write(feb_label), run_time=0.6)
        self.play(FadeIn(q_mark, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)

        # 解释
        explain_bg = Rectangle(
            width=7.8, height=3.8,
            fill_color="#16213e",
            fill_opacity=1,
            stroke_color=self.COLOR_FEB,
            stroke_width=2
        ).move_to(DOWN * 1.2)

        plain_year = Text(
            "平年：2月 = 28天",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_NORMAL
        ).move_to(DOWN * 0.5)

        leap_year = Text(
            "闰年：2月 = 29天",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_LEAP
        ).move_to(DOWN * 1.3)

        arrow_plain = Text("←", font="Heiti SC",
                           font_size=28, color=self.COLOR_NORMAL).next_to(plain_year, RIGHT, buff=0.2)
        arrow_leap = Text("←", font="Heiti SC",
                          font_size=28, color=self.COLOR_LEAP).next_to(leap_year, RIGHT, buff=0.2)

        extra_day = Text(
            "闰年多1天",
            font="Heiti SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.3)

        self.play(FadeIn(explain_bg), run_time=0.3)
        self.play(Write(plain_year), run_time=0.6)
        self.play(Write(leap_year), run_time=0.6)
        self.play(FadeIn(extra_day, shift=UP * 0.3), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(scene_title), FadeOut(circle),
            FadeOut(feb_label), FadeOut(q_mark),
            FadeOut(explain_bg), FadeOut(plain_year), FadeOut(leap_year),
            FadeOut(arrow_plain), FadeOut(arrow_leap),
            FadeOut(extra_day),
            run_time=0.6
        )

    # ─────────────────────────────────────────
    # 场景6：平年与闰年天数对比
    # ─────────────────────────────────────────
    def scene_normal_vs_leap(self):
        scene_title = Text(
            "平年 vs 闰年",
            font="Heiti SC",
            font_size=48,
            color=self.COLOR_TITLE
        ).move_to(UP * 5.8)
        self.play(Write(scene_title), run_time=0.6)

        # 左：平年
        normal_bg = Rectangle(
            width=3.5, height=4.5,
            fill_color="#16213e",
            fill_opacity=1,
            stroke_color=self.COLOR_NORMAL,
            stroke_width=3
        ).move_to(UP * 2.5 + LEFT * 2.1)

        normal_title = Text(
            "平年",
            font="Heiti SC",
            font_size=38,
            color=self.COLOR_NORMAL
        ).move_to(UP * 4.1 + LEFT * 2.1)

        normal_days = Text(
            "365天",
            font="Heiti SC",
            font_size=48,
            color=self.COLOR_NORMAL
        ).move_to(UP * 3.0 + LEFT * 2.1)

        normal_feb = Text(
            "2月 = 28天",
            font="Heiti SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 2.0 + LEFT * 2.1)

        normal_weeks = Text(
            "= 52周 + 1天",
            font="Heiti SC",
            font_size=19,
            color="#9ca3af"
        ).move_to(UP * 1.4 + LEFT * 2.1)

        # 右：闰年
        leap_bg = Rectangle(
            width=3.5, height=4.5,
            fill_color="#16213e",
            fill_opacity=1,
            stroke_color=self.COLOR_LEAP,
            stroke_width=3
        ).move_to(UP * 2.5 + RIGHT * 2.1)

        leap_title = Text(
            "闰年",
            font="Heiti SC",
            font_size=38,
            color=self.COLOR_LEAP
        ).move_to(UP * 4.1 + RIGHT * 2.1)

        leap_days = Text(
            "366天",
            font="Heiti SC",
            font_size=48,
            color=self.COLOR_LEAP
        ).move_to(UP * 3.0 + RIGHT * 2.1)

        leap_feb = Text(
            "2月 = 29天",
            font="Heiti SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 2.0 + RIGHT * 2.1)

        leap_weeks = Text(
            "= 52周 + 2天",
            font="Heiti SC",
            font_size=19,
            color="#9ca3af"
        ).move_to(UP * 1.4 + RIGHT * 2.1)

        # VS 分隔符
        vs_text = Text(
            "VS",
            font="Heiti SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)

        self.play(
            FadeIn(normal_bg), FadeIn(leap_bg),
            run_time=0.5
        )
        self.play(
            Write(normal_title), Write(leap_title),
            Write(vs_text),
            run_time=0.6
        )
        self.play(
            Write(normal_days), Write(leap_days),
            run_time=0.7
        )
        self.play(
            FadeIn(normal_feb), FadeIn(leap_feb),
            run_time=0.5
        )
        self.play(
            FadeIn(normal_weeks), FadeIn(leap_weeks),
            run_time=0.5
        )

        # 差值说明
        diff_arrow = Arrow(
            start=UP * 3.0 + LEFT * 0.6,
            end=UP * 3.0 + RIGHT * 0.6,
            color=self.COLOR_HIGHLIGHT,
            buff=0
        )
        diff_text = Text(
            "+1天",
            font="Heiti SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.5)

        self.play(GrowArrow(diff_arrow), run_time=0.5)
        self.play(FadeIn(diff_text), run_time=0.4)

        self.wait(1.5)

        self.play(
            FadeOut(scene_title),
            FadeOut(normal_bg), FadeOut(normal_title),
            FadeOut(normal_days), FadeOut(normal_feb), FadeOut(normal_weeks),
            FadeOut(leap_bg), FadeOut(leap_title),
            FadeOut(leap_days), FadeOut(leap_feb), FadeOut(leap_weeks),
            FadeOut(vs_text), FadeOut(diff_arrow), FadeOut(diff_text),
            run_time=0.6
        )

    # ─────────────────────────────────────────
    # 场景7：判断闰年的规则
    # ─────────────────────────────────────────
    def scene_leap_rule(self):
        scene_title = Text(
            "怎样判断闰年？",
            font="Heiti SC",
            font_size=44,
            color=self.COLOR_TITLE
        ).move_to(UP * 5.8)
        self.play(Write(scene_title), run_time=0.6)

        # 规则1
        rule1_bg = Rectangle(
            width=7.8, height=1.6,
            fill_color="#16213e",
            fill_opacity=1,
            stroke_color=self.COLOR_LEAP,
            stroke_width=2
        ).move_to(UP * 4.2)

        rule1_num = Text(
            "规则①",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_LEAP
        ).move_to(UP * 4.5 + LEFT * 2.5)

        rule1_text = Text(
            "年份 ÷ 4 = 整除",
            font="Heiti SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 4.5 + RIGHT * 0.5)

        rule1_note = Text(
            "→ 一般是闰年",
            font="Heiti SC",
            font_size=22,
            color=self.COLOR_LEAP
        ).move_to(UP * 3.95 + RIGHT * 0.5)

        self.play(FadeIn(rule1_bg), run_time=0.3)
        self.play(Write(rule1_num), Write(rule1_text), run_time=0.6)
        self.play(FadeIn(rule1_note), run_time=0.4)

        # 规则2（整百年特殊）
        rule2_bg = Rectangle(
            width=7.8, height=1.6,
            fill_color="#16213e",
            fill_opacity=1,
            stroke_color=self.COLOR_FEB,
            stroke_width=2
        ).move_to(UP * 2.8)

        rule2_num = Text(
            "规则②",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_FEB
        ).move_to(UP * 3.1 + LEFT * 2.5)

        rule2_text = Text(
            "整百年 ÷ 400 = 整除",
            font="Heiti SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 3.1 + RIGHT * 0.8)

        rule2_note = Text(
            "→ 才是闰年（特殊情况！）",
            font="Heiti SC",
            font_size=20,
            color=self.COLOR_FEB
        ).move_to(UP * 2.55 + RIGHT * 0.8)

        self.play(FadeIn(rule2_bg), run_time=0.3)
        self.play(Write(rule2_num), Write(rule2_text), run_time=0.6)
        self.play(FadeIn(rule2_note), run_time=0.4)

        # 例子
        examples_title = Text(
            "举例",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        self.play(FadeIn(examples_title), run_time=0.3)

        examples = [
            ("2024年", "÷4=506", "是闰年", True),
            ("2100年", "整百年÷400有余", "不是闰年", False),
            ("2000年", "÷400=5", "是闰年", True),
        ]

        example_group = VGroup()
        for year, calc, result, is_leap in examples:
            col = self.COLOR_LEAP if is_leap else self.COLOR_BIG_MONTH
            year_t = Text(year, font="Heiti SC", font_size=24, color=WHITE)
            calc_t = Text(calc, font="Heiti SC", font_size=20, color="#9ca3af")
            res_t = Text(result, font="Heiti SC", font_size=22, color=col)
            row = VGroup(year_t, calc_t, res_t).arrange(RIGHT, buff=0.4)
            example_group.add(row)

        example_group.arrange(DOWN, aligned_edge=LEFT, buff=0.28).move_to(DOWN * 0.5)

        self.play(
            LaggedStart(*[FadeIn(e, shift=RIGHT * 0.3) for e in example_group], lag_ratio=0.25),
            run_time=1.0
        )
        self.wait(0.8)

        # 关键总结框
        summary_bg = Rectangle(
            width=7.8, height=1.5,
            fill_color="#0f3460",
            fill_opacity=1,
            stroke_color=self.COLOR_HIGHLIGHT,
            stroke_width=2.5
        ).move_to(DOWN * 2.5)

        summary_text = Text(
            "整百年必须÷400整除才是闰年！",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)

        self.play(FadeIn(summary_bg), Write(summary_text), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(scene_title),
            FadeOut(rule1_bg), FadeOut(rule1_num), FadeOut(rule1_text), FadeOut(rule1_note),
            FadeOut(rule2_bg), FadeOut(rule2_num), FadeOut(rule2_text), FadeOut(rule2_note),
            FadeOut(examples_title), FadeOut(example_group),
            FadeOut(summary_bg), FadeOut(summary_text),
            run_time=0.6
        )

    # ─────────────────────────────────────────
    # 场景8：片尾
    # ─────────────────────────────────────────
    def scene_outro(self):
        # 知识总结卡
        summary_cards = [
            ("1年 = 12个月", "#f1c40f"),
            ("大月(7个) = 31天", self.COLOR_BIG_MONTH),
            ("小月(4个) = 30天", self.COLOR_SMALL_MONTH),
            ("平年 = 365天  2月=28天", self.COLOR_NORMAL),
            ("闰年 = 366天  2月=29天", self.COLOR_LEAP),
        ]

        card_group = VGroup()
        for text, col in summary_cards:
            bg = Rectangle(
                width=7.2, height=0.9,
                fill_color="#16213e",
                fill_opacity=1,
                stroke_color=col,
                stroke_width=2
            )
            txt = Text(text, font="Heiti SC", font_size=22, color=col)
            card = VGroup(bg, txt)
            card_group.add(card)

        card_group.arrange(DOWN, buff=0.18).move_to(UP * 2.5)

        self.play(
            LaggedStart(*[FadeIn(c, shift=RIGHT * 0.4) for c in card_group], lag_ratio=0.18),
            run_time=1.5
        )
        self.wait(1.0)

        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.0)

        author_big = Text(
            "上海初高中数学直通车",
            font="Heiti SC",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 3.0)

        author_id = Text(
            "@emptyandcalm",
            font="Heiti SC",
            font_size=24,
            color="#6b7280"
        ).move_to(DOWN * 3.7)

        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(author_big), FadeIn(author_id), run_time=0.5)

        # 装饰小圆点
        dots = VGroup(*[
            Dot(
                point=np.array([3.2 * np.cos(i * TAU / 6), -5.0 + 0.5 * np.sin(i * TAU / 6), 0]),
                radius=0.08,
                color=[self.COLOR_BIG_MONTH, self.COLOR_SMALL_MONTH,
                       self.COLOR_FEB, self.COLOR_LEAP, self.COLOR_NORMAL,
                       self.COLOR_HIGHLIGHT][i]
            )
            for i in range(6)
        ])
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.1),
            run_time=0.6
        )

        self.wait(2.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
