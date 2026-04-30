"""
002_平均数中位数众数.py — 平均数、中位数、众数 教学动画

知识点: 平均数、中位数、众数的概念、求法及适用场景
年级: 六年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 引入数据集
  3. 平均数: 定义、计算、特点
  4. 中位数: 定义、求法、特点
  5. 众数: 定义、求法、特点
  6. 三者对比: 受极端值影响
  7. 实际应用: 选择合适的统计量
  8. 总结
  9. 片尾
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
COLOR_MEAN = "#3b82f6"          # 蓝色 平均数
COLOR_MEDIAN = "#22c55e"        # 绿色 中位数
COLOR_MODE = "#f59e0b"          # 橙色 众数
COLOR_HL = "#fbbf24"            # 黄色高亮
COLOR_ACCENT = "#a78bfa"        # 紫色强调
COLOR_DATA = "#38bdf8"          # 天蓝色 数据
COLOR_EXTREME = "#ef4444"       # 红色 极端值
COLOR_AUTHOR = "#6b7280"        # 灰色作者信息
COLOR_BAR = "#60a5fa"           # 柱状图颜色
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class MeanMedianModeLesson(Scene):
    """
    平均数、中位数、众数教学动画
    场景顺序:
      1. 开场钩子
      2. 引入数据集
      3. 平均数
      4. 中位数
      5. 众数
      6. 三者对比 (极端值影响)
      7. 实际应用场景
      8. 总结
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_introduce_data()
        self.scene_3_mean()
        self.scene_4_median()
        self.scene_5_mode()
        self.scene_6_comparison()
        self.scene_7_application()
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

        # 钩子
        hook1 = Text(
            "一组数据的",
            font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 4.5)

        hook2 = Text(
            '"代表"是谁?',
            font=FONT, font_size=44, color=COLOR_HL
        ).move_to(UP * 3.5)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.5)

        # 三个关键词预览
        kw_mean = Text("平均数", font=FONT, font_size=32, color=COLOR_MEAN)
        kw_median = Text("中位数", font=FONT, font_size=32, color=COLOR_MEDIAN)
        kw_mode = Text("众数", font=FONT, font_size=32, color=COLOR_MODE)
        kw_group = VGroup(kw_mean, kw_median, kw_mode).arrange(RIGHT, buff=0.8).move_to(UP * 1.5)

        self.play(
            FadeIn(kw_mean, shift=UP * 0.3),
            FadeIn(kw_median, shift=UP * 0.3),
            FadeIn(kw_mode, shift=UP * 0.3),
            run_time=0.8
        )

        # 问号
        question = Text(
            "它们有什么区别?",
            font=FONT, font_size=28, color=GRAY_A
        ).move_to(UP * 0.3)
        self.play(FadeIn(question), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook1), FadeOut(hook2),
            FadeOut(kw_group), FadeOut(question),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: 引入数据集
    # ------------------------------------------------------------------

    def scene_2_introduce_data(self):
        title = Text(
            "先来看一组成绩数据",
            font=FONT, font_size=32, color=WHITE
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 数据: 5个同学的成绩
        self.data_values = [85, 90, 78, 90, 92]
        data_label = Text(
            "5位同学的数学成绩:",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.2)
        self.play(FadeIn(data_label), run_time=0.4)

        # 展示数据 - 以卡片形式
        cards = VGroup()
        for i, v in enumerate(self.data_values):
            bg = RoundedRectangle(
                corner_radius=0.15, width=1.2, height=1.4,
                fill_color="#2a2a4a", fill_opacity=0.9,
                stroke_color=COLOR_DATA, stroke_width=2
            )
            num = Text(str(v), font=FONT, font_size=28, color=WHITE)
            label = Text(
                ["A", "B", "C", "D", "E"][i],
                font=FONT, font_size=18, color=GRAY_B
            )
            card = VGroup(bg, num, label)
            num.move_to(bg.get_center() + UP * 0.15)
            label.move_to(bg.get_center() + DOWN * 0.4)
            cards.add(card)

        cards.arrange(RIGHT, buff=0.3).move_to(UP * 2.5)

        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.3), run_time=0.25)
        self.wait(0.5)

        # 简单柱状图可视化
        bar_group = VGroup()
        max_val = max(self.data_values)
        bar_height_scale = 3.5 / max_val
        bar_width = 0.9

        for i, v in enumerate(self.data_values):
            h = v * bar_height_scale
            bar = Rectangle(
                width=bar_width, height=h,
                fill_color=COLOR_BAR, fill_opacity=0.7,
                stroke_color=COLOR_BAR, stroke_width=1
            )
            bar.move_to(ORIGIN)
            val_text = Text(str(v), font=FONT, font_size=18, color=WHITE)
            val_text.next_to(bar, UP, buff=0.1)
            bar_group.add(VGroup(bar, val_text))

        bar_group.arrange(RIGHT, buff=0.3, aligned_edge=DOWN).move_to(DOWN * 1.5)

        self.play(
            *[GrowFromEdge(bg[0], DOWN) for bg in bar_group],
            run_time=1.0
        )
        self.play(
            *[FadeIn(bg[1]) for bg in bar_group],
            run_time=0.4
        )
        self.wait(0.8)

        hint = Text(
            "如何用一个数代表这组数据?",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 保存引用并清理
        self.play(
            FadeOut(title), FadeOut(data_label),
            FadeOut(cards), FadeOut(bar_group),
            FadeOut(hint),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 平均数
    # ------------------------------------------------------------------

    def scene_3_mean(self):
        # 标题
        title = Text("平均数", font=FONT, font_size=40, color=COLOR_MEAN)
        title.move_to(UP * 5.5)
        underline = Line(
            title.get_left() + DOWN * 0.15, title.get_right() + DOWN * 0.15,
            color=COLOR_MEAN, stroke_width=3
        )
        self.play(Write(title), Create(underline), run_time=0.6)

        # 定义
        defn = Text(
            "= 所有数据的总和 / 数据个数",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(FadeIn(defn), run_time=0.4)

        # 公式
        formula_cn = Text("平均数", font=FONT, font_size=24, color=COLOR_MEAN)
        formula_eq = MathTex(r"=", font_size=28, color=WHITE)
        formula_frac = MathTex(
            r"\frac{\text{sum}}{n}",
            font_size=32, color=WHITE
        )
        formula_row = VGroup(formula_cn, formula_eq, formula_frac).arrange(RIGHT, buff=0.2)
        formula_row.move_to(UP * 3.5)
        self.play(FadeIn(formula_row), run_time=0.5)
        self.wait(0.5)

        # 计算过程
        step1_cn = Text("总和 =", font=FONT, font_size=22, color=GRAY_A)
        step1_math = MathTex(
            r"85 + 90 + 78 + 90 + 92",
            font_size=24, color=WHITE
        )
        step1 = VGroup(step1_cn, step1_math).arrange(RIGHT, buff=0.2).move_to(UP * 2.2)

        step2_math = MathTex(r"= 435", font_size=28, color=WHITE).move_to(UP * 1.4)

        step3_cn = Text("平均数 =", font=FONT, font_size=22, color=COLOR_MEAN)
        step3_math = MathTex(
            r"\frac{435}{5} = 87",
            font_size=32, color=COLOR_MEAN
        )
        step3 = VGroup(step3_cn, step3_math).arrange(RIGHT, buff=0.2).move_to(UP * 0.3)

        self.play(Write(step1_cn), Write(step1_math), run_time=0.8)
        self.play(Write(step2_math), run_time=0.5)
        self.play(Write(step3_cn), Write(step3_math), run_time=0.7)
        self.wait(0.5)

        # 可视化: 数轴上标注平均数
        number_line = NumberLine(
            x_range=[70, 100, 5],
            length=7,
            include_numbers=True,
            font_size=18,
            color=GRAY_B
        ).move_to(DOWN * 2.0)
        self.play(Create(number_line), run_time=0.8)

        # 数据点
        data_dots = VGroup()
        for v in self.data_values:
            dot = Dot(
                number_line.n2p(v),
                color=COLOR_DATA, radius=0.08
            )
            data_dots.add(dot)

        self.play(*[FadeIn(d, scale=0.5) for d in data_dots], run_time=0.5)

        # 平均数标记
        mean_val = 87
        mean_line = DashedLine(
            number_line.n2p(mean_val) + UP * 0.6,
            number_line.n2p(mean_val) + DOWN * 0.6,
            color=COLOR_MEAN, dash_length=0.08
        )
        mean_label = Text(
            "87", font=FONT, font_size=22, color=COLOR_MEAN
        ).next_to(mean_line, UP, buff=0.15)
        mean_text = Text(
            "平均数", font=FONT, font_size=16, color=COLOR_MEAN
        ).next_to(mean_label, UP, buff=0.05)

        self.play(Create(mean_line), FadeIn(mean_label), FadeIn(mean_text), run_time=0.6)
        self.wait(0.5)

        # 特点
        feature = Text(
            "反映数据的整体水平",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 4.5)
        warn = Text(
            "但容易受极端值影响!",
            font=FONT, font_size=22, color=COLOR_EXTREME
        ).move_to(DOWN * 5.3)
        self.play(FadeIn(feature), run_time=0.4)
        self.play(FadeIn(warn), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(underline), FadeOut(defn),
            FadeOut(formula_row),
            FadeOut(step1), FadeOut(step2_math), FadeOut(step3),
            FadeOut(number_line), FadeOut(data_dots),
            FadeOut(mean_line), FadeOut(mean_label), FadeOut(mean_text),
            FadeOut(feature), FadeOut(warn),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 中位数
    # ------------------------------------------------------------------

    def scene_4_median(self):
        title = Text("中位数", font=FONT, font_size=40, color=COLOR_MEDIAN)
        title.move_to(UP * 5.5)
        underline = Line(
            title.get_left() + DOWN * 0.15, title.get_right() + DOWN * 0.15,
            color=COLOR_MEDIAN, stroke_width=3
        )
        self.play(Write(title), Create(underline), run_time=0.6)

        defn = Text(
            "排序后位于中间位置的数",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(FadeIn(defn), run_time=0.4)

        # Step 1: 原始数据
        step_label = Text(
            "第一步: 排序",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(UP * 3.5)
        self.play(FadeIn(step_label), run_time=0.3)

        # 原始顺序卡片
        orig_values = [85, 90, 78, 90, 92]
        orig_cards = VGroup()
        for v in orig_values:
            bg = RoundedRectangle(
                corner_radius=0.1, width=1.0, height=0.8,
                fill_color="#2a2a4a", fill_opacity=0.9,
                stroke_color=GRAY_B, stroke_width=1
            )
            num = Text(str(v), font=FONT, font_size=24, color=WHITE)
            num.move_to(bg.get_center())
            orig_cards.add(VGroup(bg, num))

        orig_cards.arrange(RIGHT, buff=0.25).move_to(UP * 2.5)
        self.play(FadeIn(orig_cards), run_time=0.5)
        self.wait(0.3)

        # 排序后
        sorted_values = sorted(orig_values)  # [78, 85, 90, 90, 92]
        sorted_cards = VGroup()
        for v in sorted_values:
            bg = RoundedRectangle(
                corner_radius=0.1, width=1.0, height=0.8,
                fill_color="#2a2a4a", fill_opacity=0.9,
                stroke_color=COLOR_MEDIAN, stroke_width=2
            )
            num = Text(str(v), font=FONT, font_size=24, color=WHITE)
            num.move_to(bg.get_center())
            sorted_cards.add(VGroup(bg, num))

        sorted_cards.arrange(RIGHT, buff=0.25).move_to(UP * 1.0)

        arrow_down = Arrow(
            orig_cards.get_bottom() + DOWN * 0.1,
            sorted_cards.get_top() + UP * 0.1,
            buff=0.1, color=COLOR_MEDIAN, stroke_width=2
        )
        sort_text = Text(
            "从小到大", font=FONT, font_size=18, color=COLOR_MEDIAN
        ).next_to(arrow_down, RIGHT, buff=0.1)

        self.play(GrowArrow(arrow_down), FadeIn(sort_text), run_time=0.4)
        self.play(FadeIn(sorted_cards), run_time=0.5)
        self.wait(0.3)

        # Step 2: 找中间位置
        step_label2 = Text(
            "第二步: 找中间",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 0.3)
        self.play(FadeIn(step_label2), run_time=0.3)

        # 高亮中间的数 (index 2 = 90)
        highlight_rect = SurroundingRectangle(
            sorted_cards[2], color=COLOR_HL, stroke_width=3, buff=0.08
        )

        mid_arrow = Arrow(
            sorted_cards[2].get_bottom() + DOWN * 0.1,
            sorted_cards[2].get_bottom() + DOWN * 0.8,
            buff=0.05, color=COLOR_HL, stroke_width=2
        )
        mid_label = Text(
            "中位数 = 90",
            font=FONT, font_size=26, color=COLOR_MEDIAN
        ).next_to(mid_arrow, DOWN, buff=0.1)

        self.play(Create(highlight_rect), run_time=0.4)
        self.play(GrowArrow(mid_arrow), Write(mid_label), run_time=0.6)
        self.wait(0.5)

        # 奇数/偶数个数据的规则
        rule_box = RoundedRectangle(
            corner_radius=0.15, width=7.5, height=2.8,
            fill_color="#1e1e3a", fill_opacity=0.9,
            stroke_color=COLOR_MEDIAN, stroke_width=1.5
        ).move_to(DOWN * 3.8)

        rule_title = Text(
            "中位数求法", font=FONT, font_size=22, color=COLOR_MEDIAN
        ).move_to(rule_box.get_top() + DOWN * 0.35)

        rule1 = Text(
            "奇数个: 正中间那个数",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(rule_box.get_center() + UP * 0.15)

        rule2 = Text(
            "偶数个: 中间两个数的平均值",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(rule_box.get_center() + DOWN * 0.5)

        self.play(FadeIn(rule_box), Write(rule_title), run_time=0.5)
        self.play(FadeIn(rule1), FadeIn(rule2), run_time=0.5)

        # 特点
        feature = Text(
            "不受极端值影响!",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 6.0)
        self.play(FadeIn(feature), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(underline), FadeOut(defn),
            FadeOut(step_label), FadeOut(orig_cards),
            FadeOut(arrow_down), FadeOut(sort_text),
            FadeOut(sorted_cards), FadeOut(step_label2),
            FadeOut(highlight_rect), FadeOut(mid_arrow), FadeOut(mid_label),
            FadeOut(rule_box), FadeOut(rule_title),
            FadeOut(rule1), FadeOut(rule2),
            FadeOut(feature),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 众数
    # ------------------------------------------------------------------

    def scene_5_mode(self):
        title = Text("众数", font=FONT, font_size=40, color=COLOR_MODE)
        title.move_to(UP * 5.5)
        underline = Line(
            title.get_left() + DOWN * 0.15, title.get_right() + DOWN * 0.15,
            color=COLOR_MODE, stroke_width=3
        )
        self.play(Write(title), Create(underline), run_time=0.6)

        defn = Text(
            "出现次数最多的数",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(FadeIn(defn), run_time=0.4)

        # 数据展示 (同组数据)
        data_label = Text(
            "数据: 85, 90, 78, 90, 92",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 3.5)
        self.play(FadeIn(data_label), run_time=0.4)

        # 频次统计表
        table_data = [
            ("78", "1"),
            ("85", "1"),
            ("90", "2"),
            ("92", "1"),
        ]

        table_group = VGroup()
        # 表头
        header_bg = Rectangle(
            width=5.0, height=0.6,
            fill_color="#3a3a5a", fill_opacity=0.9,
            stroke_color=GRAY_B, stroke_width=1
        )
        header_val = Text("数值", font=FONT, font_size=20, color=WHITE).move_to(
            header_bg.get_center() + LEFT * 1.2
        )
        header_cnt = Text("次数", font=FONT, font_size=20, color=WHITE).move_to(
            header_bg.get_center() + RIGHT * 1.2
        )
        header = VGroup(header_bg, header_val, header_cnt)
        table_group.add(header)

        for val, cnt in table_data:
            row_bg = Rectangle(
                width=5.0, height=0.55,
                fill_color="#2a2a4a", fill_opacity=0.8,
                stroke_color=GRAY_B, stroke_width=0.5
            )
            val_text = Text(val, font=FONT, font_size=20, color=WHITE).move_to(
                row_bg.get_center() + LEFT * 1.2
            )
            cnt_text = Text(cnt, font=FONT, font_size=20, color=WHITE).move_to(
                row_bg.get_center() + RIGHT * 1.2
            )
            # highlight 90
            if val == "90":
                row_bg.set_fill(color="#3a3a2a", opacity=0.9)
                row_bg.set_stroke(color=COLOR_MODE, width=2)
                val_text.set_color(COLOR_MODE)
                cnt_text.set_color(COLOR_MODE)
            row = VGroup(row_bg, val_text, cnt_text)
            table_group.add(row)

        table_group.arrange(DOWN, buff=0.0).move_to(UP * 1.0)
        self.play(FadeIn(table_group), run_time=0.8)
        self.wait(0.5)

        # 高亮90的行
        highlight_rect = SurroundingRectangle(
            table_group[3], color=COLOR_MODE, stroke_width=3, buff=0.05
        )
        self.play(Create(highlight_rect), run_time=0.4)

        result = Text(
            "众数 = 90 (出现2次, 最多)",
            font=FONT, font_size=24, color=COLOR_MODE
        ).move_to(DOWN * 1.5)
        self.play(Write(result), run_time=0.6)
        self.wait(0.5)

        # 注意事项
        note_box = RoundedRectangle(
            corner_radius=0.15, width=7.5, height=2.4,
            fill_color="#1e1e3a", fill_opacity=0.9,
            stroke_color=COLOR_MODE, stroke_width=1.5
        ).move_to(DOWN * 3.8)

        note_title = Text(
            "注意", font=FONT, font_size=22, color=COLOR_MODE
        ).move_to(note_box.get_top() + DOWN * 0.35)

        note1 = Text(
            "众数可以不止一个",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(note_box.get_center() + UP * 0.1)

        note2 = Text(
            "众数反映数据的集中趋势",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(note_box.get_center() + DOWN * 0.5)

        self.play(FadeIn(note_box), Write(note_title), run_time=0.4)
        self.play(FadeIn(note1), FadeIn(note2), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(underline), FadeOut(defn),
            FadeOut(data_label), FadeOut(table_group),
            FadeOut(highlight_rect), FadeOut(result),
            FadeOut(note_box), FadeOut(note_title),
            FadeOut(note1), FadeOut(note2),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 三者对比 (极端值影响)
    # ------------------------------------------------------------------

    def scene_6_comparison(self):
        title = Text(
            "极端值的影响", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 原数据
        orig_label = Text(
            "原数据: 85, 90, 78, 90, 92",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(FadeIn(orig_label), run_time=0.4)

        # 原数据三值
        orig_results = VGroup(
            self._make_stat_card("平均数", "87", COLOR_MEAN),
            self._make_stat_card("中位数", "90", COLOR_MEDIAN),
            self._make_stat_card("众数", "90", COLOR_MODE),
        ).arrange(RIGHT, buff=0.4).move_to(UP * 3.0)

        self.play(FadeIn(orig_results), run_time=0.6)
        self.wait(0.5)

        # 加入极端值
        change_label = Text(
            "加入极端值 200 分:",
            font=FONT, font_size=22, color=COLOR_EXTREME
        ).move_to(UP * 1.5)
        new_data_label = Text(
            "78, 85, 90, 90, 92, 200",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 0.8)

        self.play(FadeIn(change_label), FadeIn(new_data_label), run_time=0.5)
        self.wait(0.3)

        # 新数据三值
        # mean = (78+85+90+90+92+200)/6 = 635/6 ≈ 105.8
        # median = (90+90)/2 = 90
        # mode = 90
        new_results = VGroup(
            self._make_stat_card("平均数", "105.8", COLOR_MEAN),
            self._make_stat_card("中位数", "90", COLOR_MEDIAN),
            self._make_stat_card("众数", "90", COLOR_MODE),
        ).arrange(RIGHT, buff=0.4).move_to(DOWN * 0.5)

        self.play(FadeIn(new_results), run_time=0.6)
        self.wait(0.5)

        # 变化对比箭头和标注
        change_arrow = Arrow(
            orig_results[0].get_bottom() + DOWN * 0.05,
            new_results[0].get_top() + UP * 0.05,
            buff=0.1, color=COLOR_EXTREME, stroke_width=3
        )
        change_text = Text(
            "+18.8!", font=FONT, font_size=20, color=COLOR_EXTREME
        ).next_to(change_arrow, RIGHT, buff=0.1)

        no_change1 = Text(
            "不变", font=FONT, font_size=18, color=COLOR_MEDIAN
        ).move_to(
            (orig_results[1].get_bottom() + new_results[1].get_top()) / 2
        )
        no_change2 = Text(
            "不变", font=FONT, font_size=18, color=COLOR_MODE
        ).move_to(
            (orig_results[2].get_bottom() + new_results[2].get_top()) / 2
        )

        self.play(
            GrowArrow(change_arrow), FadeIn(change_text),
            FadeIn(no_change1), FadeIn(no_change2),
            run_time=0.6
        )
        self.wait(0.5)

        # 结论
        conclusion_box = RoundedRectangle(
            corner_radius=0.15, width=7.5, height=2.8,
            fill_color="#1e1e3a", fill_opacity=0.9,
            stroke_color=COLOR_HL, stroke_width=1.5
        ).move_to(DOWN * 3.5)

        c_title = Text(
            "结论", font=FONT, font_size=24, color=COLOR_HL
        ).move_to(conclusion_box.get_top() + DOWN * 0.35)

        c1 = VGroup(
            Text("平均数", font=FONT, font_size=20, color=COLOR_MEAN),
            Text(" 容易受极端值影响", font=FONT, font_size=20, color=GRAY_A)
        ).arrange(RIGHT, buff=0.1).move_to(conclusion_box.get_center() + UP * 0.2)

        c2 = VGroup(
            Text("中位数", font=FONT, font_size=20, color=COLOR_MEDIAN),
            Text("和", font=FONT, font_size=20, color=GRAY_A),
            Text("众数", font=FONT, font_size=20, color=COLOR_MODE),
            Text(" 不受极端值影响", font=FONT, font_size=20, color=GRAY_A),
        ).arrange(RIGHT, buff=0.1).move_to(conclusion_box.get_center() + DOWN * 0.4)

        self.play(FadeIn(conclusion_box), Write(c_title), run_time=0.4)
        self.play(FadeIn(c1), FadeIn(c2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(orig_label),
            FadeOut(orig_results), FadeOut(change_label),
            FadeOut(new_data_label), FadeOut(new_results),
            FadeOut(change_arrow), FadeOut(change_text),
            FadeOut(no_change1), FadeOut(no_change2),
            FadeOut(conclusion_box), FadeOut(c_title),
            FadeOut(c1), FadeOut(c2),
            run_time=0.5
        )

    def _make_stat_card(self, label_text, value_text, color):
        """创建统计值卡片"""
        bg = RoundedRectangle(
            corner_radius=0.12, width=2.2, height=1.6,
            fill_color="#2a2a4a", fill_opacity=0.9,
            stroke_color=color, stroke_width=2
        )
        label = Text(label_text, font=FONT, font_size=18, color=color)
        value = Text(value_text, font=FONT, font_size=28, color=WHITE)
        label.move_to(bg.get_center() + UP * 0.3)
        value.move_to(bg.get_center() + DOWN * 0.2)
        return VGroup(bg, label, value)

    # ------------------------------------------------------------------
    # Scene 7: 实际应用场景
    # ------------------------------------------------------------------

    def scene_7_application(self):
        title = Text(
            "什么时候用哪个?", font=FONT, font_size=34, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 三个应用场景卡片
        # Card 1: 平均数
        card1 = self._make_app_card(
            "平均数",
            "算全班平均分",
            "了解整体水平",
            COLOR_MEAN,
            UP * 3.0
        )

        # Card 2: 中位数
        card2 = self._make_app_card(
            "中位数",
            "调查居民收入",
            "避免极端值干扰",
            COLOR_MEDIAN,
            UP * 0.5
        )

        # Card 3: 众数
        card3 = self._make_app_card(
            "众数",
            "商店进货决策",
            "找最受欢迎的尺码",
            COLOR_MODE,
            DOWN * 2.0
        )

        self.play(FadeIn(card1, shift=RIGHT * 0.5), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(card2, shift=RIGHT * 0.5), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(card3, shift=RIGHT * 0.5), run_time=0.6)
        self.wait(0.3)

        # 总结语
        tip = Text(
            "根据实际问题选择合适的统计量!",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(card1), FadeOut(card2), FadeOut(card3),
            FadeOut(tip),
            run_time=0.5
        )

    def _make_app_card(self, stat_name, example, reason, color, position):
        """创建应用场景卡片"""
        bg = RoundedRectangle(
            corner_radius=0.15, width=7.5, height=2.0,
            fill_color="#2a2a4a", fill_opacity=0.85,
            stroke_color=color, stroke_width=2
        )

        icon = Circle(
            radius=0.3, fill_color=color, fill_opacity=0.9,
            stroke_width=0
        ).move_to(bg.get_left() + RIGHT * 0.8)

        stat_label = Text(
            stat_name, font=FONT, font_size=22, color=color
        ).move_to(icon.get_center())

        example_text = Text(
            example, font=FONT, font_size=22, color=WHITE
        ).next_to(icon, RIGHT, buff=0.5)

        reason_text = Text(
            reason, font=FONT, font_size=18, color=GRAY_A
        ).next_to(example_text, DOWN, buff=0.15, aligned_edge=LEFT)

        card = VGroup(bg, icon, stat_label, example_text, reason_text)
        card.move_to(position)
        return card

    # ------------------------------------------------------------------
    # Scene 8: 总结
    # ------------------------------------------------------------------

    def scene_8_summary(self):
        title = Text(
            "总结", font=FONT, font_size=40, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 总结表格
        table_bg = RoundedRectangle(
            corner_radius=0.15, width=8.0, height=8.0,
            fill_color="#1e1e3a", fill_opacity=0.9,
            stroke_color=GRAY_B, stroke_width=1
        ).move_to(UP * 0.5)
        self.play(FadeIn(table_bg), run_time=0.3)

        # 表头
        headers = VGroup(
            Text("", font=FONT, font_size=18, color=WHITE),
            Text("平均数", font=FONT, font_size=20, color=COLOR_MEAN),
            Text("中位数", font=FONT, font_size=20, color=COLOR_MEDIAN),
            Text("众数", font=FONT, font_size=20, color=COLOR_MODE),
        )
        col_positions = [-2.8, -0.8, 1.2, 3.0]
        y_start = 3.8
        for i, h in enumerate(headers):
            h.move_to(np.array([col_positions[i], y_start, 0]))

        header_line = Line(
            np.array([-3.8, y_start - 0.3, 0]),
            np.array([3.8, y_start - 0.3, 0]),
            color=GRAY_B, stroke_width=1
        )

        self.play(FadeIn(headers), Create(header_line), run_time=0.4)

        # 行数据
        rows_data = [
            ("定义", "总和/个数", "中间的数", "最多的数"),
            ("公式", "sum / n", "排序取中", "频次最高"),
            ("特点", "整体水平", "中等水平", "集中趋势"),
            ("极端值", "受影响", "不受影响", "不受影响"),
            ("个数", "唯一", "唯一", "可多个"),
        ]

        row_groups = VGroup()
        for r_idx, (row_label, v1, v2, v3) in enumerate(rows_data):
            y_pos = y_start - 0.8 - r_idx * 1.2

            label = Text(row_label, font=FONT, font_size=18, color=GRAY_A)
            label.move_to(np.array([col_positions[0], y_pos, 0]))

            t1 = Text(v1, font=FONT, font_size=17, color=WHITE)
            t1.move_to(np.array([col_positions[1], y_pos, 0]))

            t2 = Text(v2, font=FONT, font_size=17, color=WHITE)
            t2.move_to(np.array([col_positions[2], y_pos, 0]))

            t3 = Text(v3, font=FONT, font_size=17, color=WHITE)
            t3.move_to(np.array([col_positions[3], y_pos, 0]))

            # Special coloring for extreme value row
            if row_label == "极端值":
                t1.set_color(COLOR_EXTREME)
                t2.set_color(COLOR_MEDIAN)
                t3.set_color(COLOR_MODE)

            row_group = VGroup(label, t1, t2, t3)
            row_groups.add(row_group)

        for rg in row_groups:
            self.play(FadeIn(rg), run_time=0.35)

        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(table_bg),
            FadeOut(headers), FadeOut(header_line),
            FadeOut(row_groups),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 9: 片尾
    # ------------------------------------------------------------------

    def scene_9_outro(self):
        # 作者名放大
        author_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=36, color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(
            Transform(self.author_mob, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)

        # 三色圆点装饰
        dots_deco = VGroup(
            Dot(LEFT * 1.5 + DOWN * 2.5, radius=0.15, color=COLOR_MEAN),
            Dot(ORIGIN + DOWN * 2.5, radius=0.15, color=COLOR_MEDIAN),
            Dot(RIGHT * 1.5 + DOWN * 2.5, radius=0.15, color=COLOR_MODE),
        )
        labels_deco = VGroup(
            Text("平均数", font=FONT, font_size=16, color=COLOR_MEAN).next_to(dots_deco[0], DOWN, buff=0.1),
            Text("中位数", font=FONT, font_size=16, color=COLOR_MEDIAN).next_to(dots_deco[1], DOWN, buff=0.1),
            Text("众数", font=FONT, font_size=16, color=COLOR_MODE).next_to(dots_deco[2], DOWN, buff=0.1),
        )

        self.play(
            *[FadeIn(d, scale=0.5) for d in dots_deco],
            *[FadeIn(l) for l in labels_deco],
            run_time=0.6
        )
        self.wait(1.5)

        # 淡出
        self.play(
            FadeOut(self.author_mob),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(dots_deco),
            FadeOut(labels_deco),
            run_time=1.0
        )
