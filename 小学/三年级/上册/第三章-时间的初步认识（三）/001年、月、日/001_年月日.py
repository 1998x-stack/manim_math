"""
年、月、日 - 三年级上册 第三章 时间的初步认识（三）
大月、小月、平月、平年与闰年教学动画

内容:
  - 一年有12个月
  - 大月(31天): 1,3,5,7,8,10,12月 — 口诀: 一三五七八十腊，三十一天永不差
  - 小月(30天): 4,6,9,11月
  - 平月(28或29天): 2月
  - 平年365天，闰年366天
  - 闰年判断: 公历年份是4的倍数一般是闰年，整百数必须是400的倍数

格式: TikTok竖屏 (1080x1920)
时长: 约60-90秒
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# 颜色配置
BG_COLOR = "#1a1a2e"
FONT = "PingFang SC"

COLOR_BIG = "#e74c3c"       # 大月 - 红色
COLOR_SMALL = "#3498db"     # 小月 - 蓝色
COLOR_FEB = "#f39c12"       # 2月 - 橙色
COLOR_LEAP = "#2ecc71"      # 闰年 - 绿色
COLOR_NORMAL = "#9b59b6"    # 平年 - 紫色
COLOR_TITLE = "#f1c40f"     # 标题 - 金色
COLOR_HIGHLIGHT = "#f1c40f" # 高亮 - 金色
COLOR_DIM = "#6b7280"       # 暗色文字
COLOR_CARD_BG = "#16213e"   # 卡片背景
COLOR_KEY_BG = "#0f3460"    # 重点框背景


class YearMonthDay(Scene):
    """
    年、月、日教学动画

    场景顺序:
    1. 开场钩子 — "一年有多少天?"
    2. 12个月概览 — 日历网格展示
    3. 大月与小月 — 31天/30天对比，口诀记忆
    4. 特殊的2月 — 28天 vs 29天
    5. 平年与闰年 — 365天 vs 366天
    6. 闰年判断方法 — 除以4规则 + 整百年例外
    7. 知识总结 — 核心知识卡片
    8. 片尾 — 关注CTA
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 月份数据
        self.months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.month_names = [
            "1月", "2月", "3月", "4月", "5月", "6月",
            "7月", "8月", "9月", "10月", "11月", "12月"
        ]

        # 作者信息（全程保留）
        self.author_label = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT,
            font_size=18,
            color=COLOR_DIM
        ).move_to(UP * 7.0)
        self.add(self.author_label)

        # 执行各场景
        self.scene_1_opening()
        self.scene_2_twelve_months()
        self.scene_3_big_and_small()
        self.scene_4_february()
        self.scene_5_normal_vs_leap()
        self.scene_6_leap_rule()
        self.scene_7_summary()
        self.scene_8_outro()

    # ─────────────────────────────────────────────────────────
    # 辅助函数
    # ─────────────────────────────────────────────────────────

    def month_color(self, days):
        """根据天数返回月份对应颜色"""
        if days == 31:
            return COLOR_BIG
        elif days == 30:
            return COLOR_SMALL
        return COLOR_FEB

    def make_month_card(self, name, days, color, width=1.65, height=1.0):
        """创建一个月份卡片(矩形+月名+天数)"""
        rect = Rectangle(
            width=width, height=height,
            fill_color=color, fill_opacity=0.22,
            stroke_color=color, stroke_width=2
        )
        name_t = Text(name, font=FONT, font_size=20, color=WHITE)
        days_t = Text(f"{days}天", font=FONT, font_size=16, color=color)
        content = VGroup(name_t, days_t).arrange(DOWN, buff=0.08)
        return VGroup(rect, content)

    def make_info_card(self, text, color, width=7.2, height=0.85):
        """创建一个信息卡片(背景矩形+文字)"""
        bg = Rectangle(
            width=width, height=height,
            fill_color=COLOR_CARD_BG, fill_opacity=1,
            stroke_color=color, stroke_width=2
        )
        txt = Text(text, font=FONT, font_size=22, color=color)
        return VGroup(bg, txt)

    def fade_out_all(self, *mobjects, run_time=0.5):
        """淡出一组对象"""
        if mobjects:
            self.play(*[FadeOut(m) for m in mobjects], run_time=run_time)

    # ─────────────────────────────────────────────────────────
    # 场景1: 开场钩子
    # ─────────────────────────────────────────────────────────

    def scene_1_opening(self):
        # 钩子问题
        hook = Text(
            "一年有多少天？",
            font=FONT, font_size=40,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 4.8)

        sub_hook = Text(
            "是365天，还是366天？",
            font=FONT, font_size=28,
            color=WHITE
        ).move_to(UP * 3.9)

        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(sub_hook, shift=UP * 0.3), run_time=0.5)
        self.wait(0.6)

        # 大标题
        title = Text(
            "年  月  日",
            font=FONT, font_size=68,
            color=COLOR_TITLE
        ).move_to(UP * 1.8)

        subtitle = Text(
            "三年级 · 时间的初步认识",
            font=FONT, font_size=24,
            color=COLOR_DIM
        ).move_to(UP * 0.7)

        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(subtitle), run_time=0.4)
        self.wait(0.8)

        # 简化日历图标
        cal_body = Rectangle(
            width=2.0, height=2.2,
            fill_color=COLOR_CARD_BG, fill_opacity=1,
            stroke_color=COLOR_HIGHLIGHT, stroke_width=2
        )
        cal_header = Rectangle(
            width=2.0, height=0.45,
            fill_color=COLOR_HIGHLIGHT, fill_opacity=0.8,
            stroke_width=0
        ).next_to(cal_body, UP, buff=0)
        cal_num = Text(
            "12", font=FONT, font_size=48, color=COLOR_HIGHLIGHT
        ).move_to(cal_body.get_center())
        cal_icon = VGroup(cal_body, cal_header, cal_num).move_to(DOWN * 2.0)

        self.play(FadeIn(cal_icon, scale=0.8), run_time=0.5)
        self.wait(0.5)

        self.fade_out_all(hook, sub_hook, title, subtitle, cal_icon)

    # ─────────────────────────────────────────────────────────
    # 场景2: 一年12个月 — 日历网格
    # ─────────────────────────────────────────────────────────

    def scene_2_twelve_months(self):
        scene_title = Text(
            "一年有12个月",
            font=FONT, font_size=42,
            color=COLOR_TITLE
        ).move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.6)

        formula = Text(
            "1年 = 12个月",
            font=FONT, font_size=34,
            color=WHITE
        ).move_to(UP * 5.3)
        self.play(FadeIn(formula, shift=UP * 0.3), run_time=0.5)

        # 12月网格: 4列 x 3行
        cols, rows = 4, 3
        cell_w, cell_h = 1.85, 1.15
        start_x = -(cols - 1) * cell_w / 2
        start_y = 3.2

        month_cards = VGroup()
        for idx in range(12):
            r, c = idx // cols, idx % cols
            cx = start_x + c * cell_w
            cy = start_y - r * cell_h
            days = self.months_days[idx]
            color = self.month_color(days)

            card = self.make_month_card(
                self.month_names[idx], days, color,
                width=cell_w - 0.15, height=cell_h - 0.12
            )
            card.move_to(np.array([cx, cy, 0]))
            month_cards.add(card)

        # 逐行显示
        for row_idx in range(rows):
            row = VGroup(*[month_cards[row_idx * cols + c] for c in range(cols)])
            self.play(
                LaggedStart(
                    *[FadeIn(card, scale=0.85) for card in row],
                    lag_ratio=0.12
                ),
                run_time=0.6
            )
        self.wait(0.6)

        # 图例
        legend = VGroup()
        for label, col in [
            ("大月(31天)", COLOR_BIG),
            ("小月(30天)", COLOR_SMALL),
            ("2月(28/29天)", COLOR_FEB),
        ]:
            dot = Circle(
                radius=0.1, fill_color=col,
                fill_opacity=1, stroke_width=0
            )
            txt = Text(label, font=FONT, font_size=18, color=col)
            item = VGroup(dot, txt).arrange(RIGHT, buff=0.15)
            legend.add(item)
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(DOWN * 1.5)

        self.play(FadeIn(legend, shift=UP * 0.3), run_time=0.5)
        self.wait(1.2)

        self.fade_out_all(scene_title, formula, month_cards, legend)

    # ─────────────────────────────────────────────────────────
    # 场景3: 大月与小月
    # ─────────────────────────────────────────────────────────

    def scene_3_big_and_small(self):
        # ── 大月部分 ──
        big_title = Text(
            "大月 = 31天",
            font=FONT, font_size=44,
            color=COLOR_BIG
        ).move_to(UP * 6.2)
        self.play(Write(big_title), run_time=0.5)

        big_sub = Text(
            "共 7 个月",
            font=FONT, font_size=26,
            color=WHITE
        ).move_to(UP * 5.4)
        self.play(FadeIn(big_sub), run_time=0.3)

        # 大月卡片: 4+3 两行
        big_names = ["1月", "3月", "5月", "7月", "8月", "10月", "12月"]
        big_cards = VGroup()
        for name in big_names:
            card = self.make_month_card(name, 31, COLOR_BIG, width=1.6, height=1.3)
            big_cards.add(card)

        row1 = VGroup(*big_cards[:4]).arrange(RIGHT, buff=0.2)
        row2 = VGroup(*big_cards[4:]).arrange(RIGHT, buff=0.2)
        big_grid = VGroup(row1, row2).arrange(DOWN, buff=0.25).move_to(UP * 3.3)

        self.play(
            LaggedStart(
                *[FadeIn(c, scale=0.85) for c in big_cards],
                lag_ratio=0.1
            ),
            run_time=1.0
        )

        # 口诀
        mnemonic_label = Text(
            "记忆口诀",
            font=FONT, font_size=26,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 1.2)

        mnemonic_bg = Rectangle(
            width=7.5, height=2.6,
            fill_color=COLOR_CARD_BG, fill_opacity=1,
            stroke_color=COLOR_BIG, stroke_width=2
        ).move_to(DOWN * 0.2)

        line1 = Text(
            "一三五七八十腊，",
            font=FONT, font_size=36,
            color=COLOR_BIG
        ).move_to(UP * 0.3)

        line2 = Text(
            "三十一天永不差！",
            font=FONT, font_size=36,
            color=COLOR_BIG
        ).move_to(DOWN * 0.4)

        note = Text(
            "（腊 = 腊月 = 12月）",
            font=FONT, font_size=20,
            color=COLOR_DIM
        ).move_to(DOWN * 1.1)

        self.play(FadeIn(mnemonic_label), run_time=0.3)
        self.play(FadeIn(mnemonic_bg), run_time=0.3)
        self.play(Write(line1), run_time=0.7)
        self.play(Write(line2), run_time=0.7)
        self.play(FadeIn(note), run_time=0.3)

        # 高亮闪烁
        self.play(
            LaggedStart(
                *[Indicate(c, color=COLOR_HIGHLIGHT, scale_factor=1.08)
                  for c in big_cards],
                lag_ratio=0.08
            ),
            run_time=1.2
        )
        self.wait(0.8)

        self.fade_out_all(
            big_title, big_sub, big_grid,
            mnemonic_label, mnemonic_bg, line1, line2, note
        )

        # ── 小月部分 ──
        small_title = Text(
            "小月 = 30天",
            font=FONT, font_size=44,
            color=COLOR_SMALL
        ).move_to(UP * 6.2)
        self.play(Write(small_title), run_time=0.5)

        small_sub = Text(
            "共 4 个月",
            font=FONT, font_size=26,
            color=WHITE
        ).move_to(UP * 5.4)
        self.play(FadeIn(small_sub), run_time=0.3)

        small_names = ["4月", "6月", "9月", "11月"]
        small_cards = VGroup()
        for name in small_names:
            card = self.make_month_card(name, 30, COLOR_SMALL, width=1.8, height=1.5)
            small_cards.add(card)
        small_cards.arrange(RIGHT, buff=0.3).move_to(UP * 3.5)

        self.play(
            LaggedStart(
                *[FadeIn(c, scale=0.85) for c in small_cards],
                lag_ratio=0.15
            ),
            run_time=0.8
        )

        # 记忆技巧
        tip_bg = Rectangle(
            width=7.5, height=2.0,
            fill_color=COLOR_CARD_BG, fill_opacity=1,
            stroke_color=COLOR_SMALL, stroke_width=2
        ).move_to(UP * 1.2)

        tip_label = Text(
            "记忆技巧",
            font=FONT, font_size=24,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 1.7)

        tip_text = Text(
            "四六九冬三十天",
            font=FONT, font_size=30,
            color=COLOR_SMALL
        ).move_to(UP * 1.0)

        tip_note = Text(
            "（冬 = 11月）",
            font=FONT, font_size=18,
            color=COLOR_DIM
        ).move_to(UP * 0.5)

        self.play(FadeIn(tip_bg), run_time=0.3)
        self.play(Write(tip_label), run_time=0.3)
        self.play(Write(tip_text), run_time=0.6)
        self.play(FadeIn(tip_note), run_time=0.3)

        # 月份分类汇总
        summary_items = VGroup()
        for label, count, col in [
            ("大月(31天)", "7个月", COLOR_BIG),
            ("小月(30天)", "4个月", COLOR_SMALL),
            ("2月(特殊)", "1个月", COLOR_FEB),
            ("合计", "12个月", COLOR_HIGHLIGHT),
        ]:
            dot = Circle(
                radius=0.1, fill_color=col,
                fill_opacity=1, stroke_width=0
            )
            l_text = Text(
                f"{label}：{count}",
                font=FONT, font_size=22, color=col
            )
            row = VGroup(dot, l_text).arrange(RIGHT, buff=0.15)
            summary_items.add(row)
        summary_items.arrange(DOWN, aligned_edge=LEFT, buff=0.22).move_to(DOWN * 1.5)

        self.play(
            LaggedStart(
                *[FadeIn(item, shift=RIGHT * 0.3) for item in summary_items],
                lag_ratio=0.15
            ),
            run_time=0.8
        )
        self.wait(1.0)

        self.fade_out_all(
            small_title, small_sub, small_cards,
            tip_bg, tip_label, tip_text, tip_note,
            summary_items
        )

    # ─────────────────────────────────────────────────────────
    # 场景4: 特殊的2月
    # ─────────────────────────────────────────────────────────

    def scene_4_february(self):
        scene_title = Text(
            "特殊的 2 月",
            font=FONT, font_size=44,
            color=COLOR_FEB
        ).move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.5)

        # 大圆形突出2月
        circle = Circle(
            radius=2.0,
            fill_color=COLOR_FEB, fill_opacity=0.15,
            stroke_color=COLOR_FEB, stroke_width=3
        ).move_to(UP * 3.5)

        feb_big = Text(
            "2月",
            font=FONT, font_size=68,
            color=COLOR_FEB
        ).move_to(UP * 3.8)

        question = Text(
            "28天？还是29天？",
            font=FONT, font_size=28,
            color=WHITE
        ).move_to(UP * 2.8)

        self.play(Create(circle), run_time=0.6)
        self.play(Write(feb_big), run_time=0.5)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # 两个对比卡片
        # 左: 平年
        n_bg = Rectangle(
            width=3.3, height=3.5,
            fill_color=COLOR_CARD_BG, fill_opacity=1,
            stroke_color=COLOR_NORMAL, stroke_width=2.5
        ).move_to(DOWN * 0.5 + LEFT * 2.1)

        n_label = Text(
            "平年", font=FONT, font_size=32, color=COLOR_NORMAL
        ).move_to(DOWN * -0.7 + LEFT * 2.1)

        n_days = Text(
            "28天", font=FONT, font_size=44, color=COLOR_NORMAL
        ).move_to(DOWN * 0.3 + LEFT * 2.1)

        n_note = Text(
            "4周整", font=FONT, font_size=20, color=COLOR_DIM
        ).move_to(DOWN * 1.1 + LEFT * 2.1)

        # 右: 闰年
        l_bg = Rectangle(
            width=3.3, height=3.5,
            fill_color=COLOR_CARD_BG, fill_opacity=1,
            stroke_color=COLOR_LEAP, stroke_width=2.5
        ).move_to(DOWN * 0.5 + RIGHT * 2.1)

        l_label = Text(
            "闰年", font=FONT, font_size=32, color=COLOR_LEAP
        ).move_to(DOWN * -0.7 + RIGHT * 2.1)

        l_days = Text(
            "29天", font=FONT, font_size=44, color=COLOR_LEAP
        ).move_to(DOWN * 0.3 + RIGHT * 2.1)

        l_note = Text(
            "4周+1天", font=FONT, font_size=20, color=COLOR_DIM
        ).move_to(DOWN * 1.1 + RIGHT * 2.1)

        vs = Text(
            "VS", font=FONT, font_size=30,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(n_bg), FadeIn(l_bg), run_time=0.4)
        self.play(
            Write(n_label), Write(l_label),
            FadeIn(vs),
            run_time=0.5
        )
        self.play(Write(n_days), Write(l_days), run_time=0.6)
        self.play(FadeIn(n_note), FadeIn(l_note), run_time=0.4)

        # 关键提示
        key_bg = Rectangle(
            width=6.0, height=0.9,
            fill_color=COLOR_KEY_BG, fill_opacity=1,
            stroke_color=COLOR_HIGHLIGHT, stroke_width=2
        ).move_to(DOWN * 3.0)

        key_text = Text(
            "闰年的2月多1天！",
            font=FONT, font_size=28,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.0)

        self.play(FadeIn(key_bg), run_time=0.3)
        self.play(Write(key_text), run_time=0.5)
        self.wait(1.5)

        self.fade_out_all(
            scene_title, circle, feb_big, question,
            n_bg, n_label, n_days, n_note,
            l_bg, l_label, l_days, l_note,
            vs, key_bg, key_text
        )

    # ─────────────────────────────────────────────────────────
    # 场景5: 平年 vs 闰年
    # ─────────────────────────────────────────────────────────

    def scene_5_normal_vs_leap(self):
        scene_title = Text(
            "平年 与 闰年",
            font=FONT, font_size=44,
            color=COLOR_TITLE
        ).move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.5)

        # 左: 平年
        n_bg = Rectangle(
            width=3.6, height=5.5,
            fill_color=COLOR_CARD_BG, fill_opacity=1,
            stroke_color=COLOR_NORMAL, stroke_width=3
        ).move_to(UP * 2.2 + LEFT * 2.1)

        n_title = Text(
            "平 年", font=FONT, font_size=36, color=COLOR_NORMAL
        ).move_to(UP * 4.3 + LEFT * 2.1)

        n_days = Text(
            "365", font=FONT, font_size=56, color=COLOR_NORMAL
        ).move_to(UP * 3.2 + LEFT * 2.1)

        n_unit = Text(
            "天", font=FONT, font_size=28, color=COLOR_NORMAL
        ).next_to(n_days, RIGHT, buff=0.08)

        n_feb = Text(
            "2月 = 28天", font=FONT, font_size=22, color=WHITE
        ).move_to(UP * 2.2 + LEFT * 2.1)

        n_weeks = Text(
            "52周 + 1天", font=FONT, font_size=18, color=COLOR_DIM
        ).move_to(UP * 1.6 + LEFT * 2.1)

        n_example = Text(
            "如: 2023年", font=FONT, font_size=18, color=COLOR_DIM
        ).move_to(UP * 1.0 + LEFT * 2.1)

        # 右: 闰年
        l_bg = Rectangle(
            width=3.6, height=5.5,
            fill_color=COLOR_CARD_BG, fill_opacity=1,
            stroke_color=COLOR_LEAP, stroke_width=3
        ).move_to(UP * 2.2 + RIGHT * 2.1)

        l_title = Text(
            "闰 年", font=FONT, font_size=36, color=COLOR_LEAP
        ).move_to(UP * 4.3 + RIGHT * 2.1)

        l_days = Text(
            "366", font=FONT, font_size=56, color=COLOR_LEAP
        ).move_to(UP * 3.2 + RIGHT * 2.1)

        l_unit = Text(
            "天", font=FONT, font_size=28, color=COLOR_LEAP
        ).next_to(l_days, RIGHT, buff=0.08)

        l_feb = Text(
            "2月 = 29天", font=FONT, font_size=22, color=WHITE
        ).move_to(UP * 2.2 + RIGHT * 2.1)

        l_weeks = Text(
            "52周 + 2天", font=FONT, font_size=18, color=COLOR_DIM
        ).move_to(UP * 1.6 + RIGHT * 2.1)

        l_example = Text(
            "如: 2024年", font=FONT, font_size=18, color=COLOR_DIM
        ).move_to(UP * 1.0 + RIGHT * 2.1)

        vs = Text(
            "VS", font=FONT, font_size=34,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 2.2)

        # 动画
        self.play(FadeIn(n_bg), FadeIn(l_bg), run_time=0.4)
        self.play(
            Write(n_title), Write(l_title),
            FadeIn(vs),
            run_time=0.5
        )
        self.play(
            Write(n_days), Write(l_days),
            FadeIn(n_unit), FadeIn(l_unit),
            run_time=0.6
        )
        self.play(FadeIn(n_feb), FadeIn(l_feb), run_time=0.4)
        self.play(FadeIn(n_weeks), FadeIn(l_weeks), run_time=0.4)
        self.play(FadeIn(n_example), FadeIn(l_example), run_time=0.4)

        # 差异箭头
        diff_arrow = Arrow(
            start=UP * 3.2 + LEFT * 0.5,
            end=UP * 3.2 + RIGHT * 0.5,
            color=COLOR_HIGHLIGHT, stroke_width=3, buff=0
        )
        diff_label = Text(
            "+1天", font=FONT, font_size=24, color=COLOR_HIGHLIGHT
        ).move_to(UP * 3.7)

        self.play(GrowArrow(diff_arrow), run_time=0.4)
        self.play(FadeIn(diff_label), run_time=0.3)

        # 底部要点
        key_bg = Rectangle(
            width=7.0, height=0.8,
            fill_color=COLOR_KEY_BG, fill_opacity=1,
            stroke_color=COLOR_HIGHLIGHT, stroke_width=2
        ).move_to(DOWN * 1.5)

        key_text = Text(
            "区别在于2月: 28天 vs 29天",
            font=FONT, font_size=24, color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)

        self.play(FadeIn(key_bg), run_time=0.2)
        self.play(Write(key_text), run_time=0.5)
        self.wait(1.5)

        self.fade_out_all(
            scene_title,
            n_bg, n_title, n_days, n_unit, n_feb, n_weeks, n_example,
            l_bg, l_title, l_days, l_unit, l_feb, l_weeks, l_example,
            vs, diff_arrow, diff_label, key_bg, key_text
        )

    # ─────────────────────────────────────────────────────────
    # 场景6: 闰年判断方法
    # ─────────────────────────────────────────────────────────

    def scene_6_leap_rule(self):
        scene_title = Text(
            "怎样判断闰年？",
            font=FONT, font_size=42,
            color=COLOR_TITLE
        ).move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.5)

        # 规则1: 除以4
        r1_bg = Rectangle(
            width=7.5, height=1.8,
            fill_color=COLOR_CARD_BG, fill_opacity=1,
            stroke_color=COLOR_LEAP, stroke_width=2
        ).move_to(UP * 4.4)

        r1_badge = Text(
            "规则一", font=FONT, font_size=22, color=COLOR_LEAP
        ).move_to(UP * 4.9 + LEFT * 2.5)

        r1_text = Text(
            "年份 ÷ 4 = 整除 → 一般是闰年",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 4.3)

        self.play(FadeIn(r1_bg), run_time=0.3)
        self.play(Write(r1_badge), run_time=0.3)
        self.play(Write(r1_text), run_time=0.6)

        # 规则2: 整百年特殊
        r2_bg = Rectangle(
            width=7.5, height=1.8,
            fill_color=COLOR_CARD_BG, fill_opacity=1,
            stroke_color=COLOR_FEB, stroke_width=2
        ).move_to(UP * 2.6)

        r2_badge = Text(
            "规则二", font=FONT, font_size=22, color=COLOR_FEB
        ).move_to(UP * 3.1 + LEFT * 2.5)

        r2_text = Text(
            "整百年 ÷ 400 = 整除 → 才是闰年",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 2.5)

        r2_note = Text(
            "（整百年特殊！）",
            font=FONT, font_size=18, color=COLOR_FEB
        ).move_to(UP * 1.95)

        self.play(FadeIn(r2_bg), run_time=0.3)
        self.play(Write(r2_badge), run_time=0.3)
        self.play(Write(r2_text), run_time=0.6)
        self.play(FadeIn(r2_note), run_time=0.3)

        # 举例验证
        ex_title = Text(
            "举例验证",
            font=FONT, font_size=28, color=COLOR_HIGHLIGHT
        ).move_to(UP * 0.8)
        self.play(FadeIn(ex_title), run_time=0.3)

        examples = [
            ("2024年", "2024 ÷ 4 = 506", "闰年", True),
            ("2023年", "2023 ÷ 4 = 505…3", "平年", False),
            ("2000年", "2000 ÷ 400 = 5", "闰年", True),
            ("1900年", "1900 ÷ 400 = 4…300", "平年", False),
        ]

        ex_group = VGroup()
        for year, calc, result, is_leap in examples:
            col = COLOR_LEAP if is_leap else COLOR_BIG
            year_t = Text(year, font=FONT, font_size=22, color=WHITE)
            calc_t = Text(calc, font=FONT, font_size=18, color=COLOR_DIM)
            # 用圆形标记替代勾叉
            mark = Circle(
                radius=0.15,
                fill_color=col, fill_opacity=0.8,
                stroke_width=0
            )
            res_t = Text(result, font=FONT, font_size=22, color=col)
            row = VGroup(mark, year_t, calc_t, res_t).arrange(RIGHT, buff=0.25)
            ex_group.add(row)

        ex_group.arrange(DOWN, aligned_edge=LEFT, buff=0.28).move_to(DOWN * 1.0)

        self.play(
            LaggedStart(
                *[FadeIn(e, shift=RIGHT * 0.3) for e in ex_group],
                lag_ratio=0.2
            ),
            run_time=1.0
        )
        self.wait(0.5)

        # 重点框
        warn_bg = Rectangle(
            width=7.5, height=1.2,
            fill_color=COLOR_KEY_BG, fill_opacity=1,
            stroke_color=COLOR_HIGHLIGHT, stroke_width=2.5
        ).move_to(DOWN * 3.5)

        warn_text = Text(
            "整百年必须 ÷ 400 整除才是闰年！",
            font=FONT, font_size=24, color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)

        self.play(FadeIn(warn_bg), Write(warn_text), run_time=0.6)
        self.wait(2.0)

        self.fade_out_all(
            scene_title,
            r1_bg, r1_badge, r1_text,
            r2_bg, r2_badge, r2_text, r2_note,
            ex_title, ex_group,
            warn_bg, warn_text
        )

    # ─────────────────────────────────────────────────────────
    # 场景7: 知识总结
    # ─────────────────────────────────────────────────────────

    def scene_7_summary(self):
        scene_title = Text(
            "知识总结",
            font=FONT, font_size=42,
            color=COLOR_TITLE
        ).move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.5)

        # 7条核心知识卡片
        data = [
            ("1年 = 12个月", COLOR_HIGHLIGHT),
            ("大月(7个): 1,3,5,7,8,10,12月 = 31天", COLOR_BIG),
            ("小月(4个): 4,6,9,11月 = 30天", COLOR_SMALL),
            ("2月: 平年28天 / 闰年29天", COLOR_FEB),
            ("平年 = 365天", COLOR_NORMAL),
            ("闰年 = 366天", COLOR_LEAP),
            ("闰年: 年份÷4整除 (整百÷400)", COLOR_HIGHLIGHT),
        ]

        cards = VGroup()
        for text, col in data:
            card = self.make_info_card(text, col, width=7.5, height=0.85)
            cards.add(card)
        cards.arrange(DOWN, buff=0.15).move_to(UP * 2.0)

        self.play(
            LaggedStart(
                *[FadeIn(c, shift=RIGHT * 0.4) for c in cards],
                lag_ratio=0.15
            ),
            run_time=1.8
        )

        # 口诀框
        mnemonic_bg = Rectangle(
            width=7.5, height=1.6,
            fill_color=COLOR_KEY_BG, fill_opacity=1,
            stroke_color=COLOR_BIG, stroke_width=2.5
        ).move_to(DOWN * 2.5)

        mnemonic_text = Text(
            "一三五七八十腊，三十一天永不差！",
            font=FONT, font_size=26, color=COLOR_BIG
        ).move_to(DOWN * 2.5)

        self.play(FadeIn(mnemonic_bg), run_time=0.3)
        self.play(Write(mnemonic_text), run_time=0.8)
        self.wait(2.5)

        self.fade_out_all(scene_title, cards, mnemonic_bg, mnemonic_text)

    # ─────────────────────────────────────────────────────────
    # 场景8: 片尾
    # ─────────────────────────────────────────────────────────

    def scene_8_outro(self):
        follow = Text(
            "关注我，学习更多数学知识！",
            font=FONT, font_size=30,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 2.0)

        author_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=28,
            color=WHITE
        ).move_to(UP * 0.8)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=24,
            color=COLOR_DIM
        ).move_to(UP * 0.1)

        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(author_name), FadeIn(author_id), run_time=0.5)

        # 装饰小点
        colors = [COLOR_BIG, COLOR_SMALL, COLOR_FEB, COLOR_LEAP, COLOR_NORMAL, COLOR_HIGHLIGHT]
        dots = VGroup()
        for i in range(6):
            angle = i * TAU / 6
            dot = Dot(
                point=np.array([
                    2.8 * np.cos(angle),
                    -2.5 + 0.6 * np.sin(angle),
                    0
                ]),
                radius=0.1,
                color=colors[i]
            )
            dots.add(dot)

        self.play(
            LaggedStart(
                *[FadeIn(d, scale=0.5) for d in dots],
                lag_ratio=0.08
            ),
            run_time=0.5
        )

        self.wait(2.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
