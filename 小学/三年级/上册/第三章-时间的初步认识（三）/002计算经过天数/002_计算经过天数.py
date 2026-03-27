"""
002_计算经过天数.py — 计算经过天数 教学动画

知识点: 计算两个日期之间经过的天数
  - 方法1：数数法（在日历上一天天数）
  - 方法2：分段法（拆分月份计算）
    7月15日 → 8月20日
    7月：31 - 15 = 16天
    8月：20天
    共：16 + 20 = 36天
  - 方法3：列式计算法

年级: 三年级上册
格式: TikTok 竖屏 (1080×1920)
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
BG_COLOR       = "#1a1a2e"
COLOR_JULY     = "#3b82f6"   # 蓝色 – 7月
COLOR_AUG      = "#f59e0b"   # 橙色 – 8月
COLOR_HL       = "#fbbf24"   # 黄色 高亮
COLOR_START    = "#22c55e"   # 绿色 起始日
COLOR_END      = "#ef4444"   # 红色 结束日
COLOR_FORMULA  = "#a78bfa"   # 紫色 公式
COLOR_AUTHOR   = "#6b7280"   # 灰色 作者
FONT           = "Hiragino Sans GB"


# ======================================================================
# 主场景
# ======================================================================

class CountingDaysLesson(Scene):
    """
    计算经过天数教学动画

    场景顺序:
      1. 开场钩子 – 从7月15日到8月20日共几天?
      2. 方法介绍 – 三种算法概览
      3. 数数法 – 在日历上一天天数
      4. 分段法 – 7月剩余 + 8月已过
      5. 列式计算展示
      6. 知识总结
      7. 片尾
    """

    # ------------------------------------------------------------------
    # 构造入口
    # ------------------------------------------------------------------

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_data()

        self.scene_1_opening()
        self.scene_2_overview()
        self.scene_3_counting_method()
        self.scene_4_segment_method()
        self.scene_5_formula_method()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 数据初始化（无几何计算，但统一管理日历数据）
    # ------------------------------------------------------------------

    def setup_data(self):
        """统一初始化日历数据和布局常量"""
        # 7月天数
        self.july_days = 31
        # 起始日、结束日
        self.start_day  = 15   # 7月15日
        self.end_day    = 20   # 8月20日

        # 分段计算结果
        self.july_remaining = self.july_days - self.start_day   # 31 - 15 = 16
        self.aug_elapsed    = self.end_day                       # 20
        self.total_days     = self.july_remaining + self.aug_elapsed  # 36

        assert self.july_remaining == 16
        assert self.total_days == 36
        print(f"Data check: July remaining={self.july_remaining}, Aug={self.aug_elapsed}, Total={self.total_days}")

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        """创建顶部作者标识"""
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT,
            font_size=18,
            color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def make_calendar_grid(self, month_name, days_in_month, color,
                           highlight_days=None, start_weekday=0,
                           cell_w=0.85, cell_h=0.72):
        """
        绘制一个简化日历格子（7列，若干行）
        month_name: str  月份文字
        days_in_month: int 本月天数
        color: 主色
        highlight_days: list[int] 要高亮的日期
        start_weekday: 0=周日, 1=周一, …
        返回 VGroup，中心在 ORIGIN（调用者自行移位）
        """
        highlight_days = highlight_days or []
        col_count = 7
        rows_needed = ((days_in_month + start_weekday - 1) // col_count) + 1

        header_texts = ["日", "一", "二", "三", "四", "五", "六"]

        cells = VGroup()

        # 表头
        header_group = VGroup()
        for ci, hd in enumerate(header_texts):
            lbl = Text(hd, font=FONT, font_size=16, color=color)
            lbl.move_to(np.array([(ci - 3) * cell_w, (rows_needed) * cell_h, 0.0]))
            header_group.add(lbl)
        cells.add(header_group)

        # 日期格
        day = 1
        for row in range(rows_needed):
            for col in range(col_count):
                if row == 0 and col < start_weekday:
                    continue
                if day > days_in_month:
                    break

                x = (col - 3) * cell_w
                y = (rows_needed - 1 - row) * cell_h

                is_hl = day in highlight_days
                # 背景框
                box = Square(
                    side_length=min(cell_w, cell_h) * 0.88,
                    color=color if is_hl else GRAY_D,
                    stroke_width=1.5 if not is_hl else 2.5,
                    fill_color=color if is_hl else BG_COLOR,
                    fill_opacity=0.5 if is_hl else 0.15,
                ).move_to(np.array([x, y, 0.0]))

                num_color = WHITE if is_hl else GRAY_B
                num_text = Text(str(day), font=FONT, font_size=15, color=num_color)
                num_text.move_to(np.array([x, y, 0.0]))

                cells.add(box, num_text)
                day += 1

        return cells

    def make_month_title(self, text, color, font_size=30):
        return Text(text, font=FONT, font_size=font_size, color=color)

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 主钩子问题
        hook_line1 = Text(
            "7月15日 到 8月20日",
            font=FONT, font_size=36, color=COLOR_HL,
        ).move_to(UP * 4.8)

        hook_line2 = Text(
            "共经过了几天?",
            font=FONT, font_size=42, color=WHITE,
        ).move_to(UP * 3.9)

        self.play(Write(hook_line1), run_time=0.8)
        self.play(Write(hook_line2), run_time=0.6)
        self.wait(0.8)

        # 简单时间线示意
        tl_start = np.array([-3.2, 2.4, 0.0])
        tl_end   = np.array([ 3.2, 2.4, 0.0])

        timeline = Line(tl_start, tl_end, color=GRAY_B, stroke_width=3)
        dot_start = Dot(tl_start, color=COLOR_START, radius=0.12)
        dot_end   = Dot(tl_end,   color=COLOR_END,   radius=0.12)

        lbl_start = Text("7月15日", font=FONT, font_size=22, color=COLOR_START)
        lbl_start.next_to(dot_start, DOWN, buff=0.25)

        lbl_end = Text("8月20日", font=FONT, font_size=22, color=COLOR_END)
        lbl_end.next_to(dot_end, DOWN, buff=0.25)

        question_brace = Brace(timeline, direction=UP, buff=0.1, color=COLOR_HL)
        question_text  = Text("? 天", font=FONT, font_size=26, color=COLOR_HL)
        question_text.next_to(question_brace, UP, buff=0.1)

        self.play(
            Create(timeline),
            FadeIn(dot_start, scale=0.5),
            FadeIn(dot_end,   scale=0.5),
            run_time=0.8,
        )
        self.play(
            FadeIn(lbl_start, shift=UP * 0.2),
            FadeIn(lbl_end,   shift=UP * 0.2),
            run_time=0.5,
        )
        self.play(
            GrowFromCenter(question_brace),
            FadeIn(question_text, shift=UP * 0.2),
            run_time=0.6,
        )
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(hook_line1), FadeOut(hook_line2),
            FadeOut(timeline), FadeOut(dot_start), FadeOut(dot_end),
            FadeOut(lbl_start), FadeOut(lbl_end),
            FadeOut(question_brace), FadeOut(question_text),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 三种方法概览
    # ------------------------------------------------------------------

    def scene_2_overview(self):
        title = Text("计算经过天数的方法", font=FONT, font_size=34, color=COLOR_HL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.7)

        methods = [
            ("方法①", "数数法", "在日历上一天天数", COLOR_JULY),
            ("方法②", "分段法", "分月计算再相加", COLOR_AUG),
            ("方法③", "列式法", "直接列算式计算", COLOR_FORMULA),
        ]

        cards = VGroup()
        y_positions = [3.5, 1.2, -1.1]

        for i, (tag, name, desc, col) in enumerate(methods):
            tag_t  = Text(tag,  font=FONT, font_size=22, color=col)
            name_t = Text(name, font=FONT, font_size=28, color=WHITE)
            desc_t = Text(desc, font=FONT, font_size=19, color=GRAY_A)

            row = VGroup(tag_t, name_t).arrange(RIGHT, buff=0.25)
            card = VGroup(row, desc_t).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
            card.move_to(LEFT * 0.5 + UP * y_positions[i])

            underline = Line(
                card.get_left() + DOWN * 0.05,
                card.get_right() + DOWN * 0.05,
                color=col, stroke_width=1.5,
            ).next_to(card, DOWN, buff=0.1)

            full_card = VGroup(card, underline)
            cards.add(full_card)

            self.play(FadeIn(full_card, shift=RIGHT * 0.4), run_time=0.5)
            self.wait(0.3)

        self.wait(1.5)

        # 清理
        self.play(FadeOut(title), FadeOut(cards), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 3: 数数法（日历展示）
    # ------------------------------------------------------------------

    def scene_3_counting_method(self):
        title = Text("方法① 数数法", font=FONT, font_size=34, color=COLOR_JULY)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        subtitle = Text(
            "在日历上一天一天数出来",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(UP * 4.8)
        self.play(FadeIn(subtitle), run_time=0.4)

        # ── 7月日历（仅显示15日以后的日期区间，简化版5列×2行）
        # 真实7月2023年从周六开始，此处为教学简化，start_weekday=6
        july_title = self.make_month_title("7 月", COLOR_JULY)
        july_title.move_to(UP * 3.8 + LEFT * 1.8)

        # 简化版7月日历：只显示15-31，高亮16-31
        july_highlight = list(range(16, 32))   # 16到31（不含15本身，从15之后开始数）
        july_calendar = self.make_calendar_grid(
            "7月", 31, COLOR_JULY,
            highlight_days=july_highlight,
            start_weekday=6,
            cell_w=0.72, cell_h=0.60,
        )
        july_calendar.scale(0.88).move_to(LEFT * 1.8 + UP * 1.5)

        # 标注15日（起点）
        start_mark = Text("出发!", font=FONT, font_size=18, color=COLOR_START)
        start_mark.move_to(UP * 3.8 + RIGHT * 1.0)

        self.play(FadeIn(july_title), run_time=0.4)
        self.play(FadeIn(july_calendar, shift=UP * 0.3), run_time=1.0)

        # 数字气泡：16天
        count_16 = VGroup(
            Text("7月剩余", font=FONT, font_size=22, color=COLOR_JULY),
            MathTex(r"16", font_size=36, color=COLOR_JULY),
            Text("天", font=FONT, font_size=22, color=COLOR_JULY),
        ).arrange(RIGHT, buff=0.15).move_to(RIGHT * 2.8 + UP * 2.2)

        self.play(FadeIn(count_16, scale=0.8), run_time=0.6)
        self.wait(0.8)

        # ── 8月日历
        aug_title = self.make_month_title("8 月", COLOR_AUG)
        aug_title.move_to(DOWN * 0.0 + LEFT * 1.8)

        aug_highlight = list(range(1, 21))
        aug_calendar = self.make_calendar_grid(
            "8月", 31, COLOR_AUG,
            highlight_days=aug_highlight,
            start_weekday=2,     # 2023年8月1日 周二
            cell_w=0.72, cell_h=0.60,
        )
        aug_calendar.scale(0.88).move_to(LEFT * 1.8 + DOWN * 1.7)

        self.play(FadeIn(aug_title), run_time=0.4)
        self.play(FadeIn(aug_calendar, shift=UP * 0.3), run_time=1.0)

        count_20 = VGroup(
            Text("8月已过", font=FONT, font_size=22, color=COLOR_AUG),
            MathTex(r"20", font_size=36, color=COLOR_AUG),
            Text("天", font=FONT, font_size=22, color=COLOR_AUG),
        ).arrange(RIGHT, buff=0.15).move_to(RIGHT * 2.8 + DOWN * 1.5)

        self.play(FadeIn(count_20, scale=0.8), run_time=0.6)
        self.wait(0.8)

        # 总计
        total_text = VGroup(
            Text("共", font=FONT, font_size=26, color=WHITE),
            MathTex(r"16 + 20 =", font_size=32, color=WHITE),
            MathTex(r"36", font_size=40, color=COLOR_HL),
            Text("天", font=FONT, font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.18).move_to(DOWN * 4.0)

        self.play(FadeIn(total_text, scale=0.9), run_time=0.8)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(july_title), FadeOut(july_calendar),
            FadeOut(aug_title), FadeOut(aug_calendar),
            FadeOut(count_16), FadeOut(count_20),
            FadeOut(total_text),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 4: 分段法（核心动画）
    # ------------------------------------------------------------------

    def scene_4_segment_method(self):
        title = Text("方法② 分段法", font=FONT, font_size=34, color=COLOR_AUG)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        subtitle = Text(
            "把跨月的天数分段计算",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(UP * 4.8)
        self.play(FadeIn(subtitle), run_time=0.4)

        # ── 时间轴
        tl_y = 3.6
        tl_left  = np.array([-3.8, tl_y, 0.0])
        tl_right = np.array([ 3.8, tl_y, 0.0])

        timeline = Line(tl_left, tl_right, color=GRAY_B, stroke_width=3)

        # 三个关键点
        p_july15  = np.array([-3.2, tl_y, 0.0])
        p_july31  = np.array([ 0.3, tl_y, 0.0])  # 7月底/8月初
        p_aug20   = np.array([ 3.2, tl_y, 0.0])

        dot_july15 = Dot(p_july15, color=COLOR_START, radius=0.13)
        dot_july31 = Dot(p_july31, color=GRAY_B,      radius=0.10)
        dot_aug20  = Dot(p_aug20,  color=COLOR_END,   radius=0.13)

        lbl_july15 = Text("7月15日", font=FONT, font_size=20, color=COLOR_START)
        lbl_july15.next_to(dot_july15, DOWN, buff=0.25)

        lbl_july31 = Text("7月31日\n/8月1日", font=FONT, font_size=18, color=GRAY_A)
        lbl_july31.next_to(dot_july31, DOWN, buff=0.25)

        lbl_aug20 = Text("8月20日", font=FONT, font_size=20, color=COLOR_END)
        lbl_aug20.next_to(dot_aug20, DOWN, buff=0.25)

        self.play(Create(timeline), run_time=0.5)
        self.play(
            FadeIn(dot_july15, scale=0.5),
            FadeIn(dot_july31, scale=0.5),
            FadeIn(dot_aug20,  scale=0.5),
            run_time=0.5,
        )
        self.play(
            FadeIn(lbl_july15, shift=UP * 0.2),
            FadeIn(lbl_july31, shift=UP * 0.2),
            FadeIn(lbl_aug20,  shift=UP * 0.2),
            run_time=0.5,
        )
        self.wait(0.5)

        # ── 第一段: 7月15日 → 7月31日（16天）
        seg1_line = Line(p_july15, p_july31, color=COLOR_JULY, stroke_width=8)
        seg1_brace = Brace(seg1_line, direction=UP, buff=0.08, color=COLOR_JULY)

        seg1_lbl = VGroup(
            Text("7月剩余", font=FONT, font_size=20, color=COLOR_JULY),
            MathTex(r"16", font_size=30, color=COLOR_JULY),
            Text("天", font=FONT, font_size=20, color=COLOR_JULY),
        ).arrange(RIGHT, buff=0.1)
        seg1_lbl.next_to(seg1_brace, UP, buff=0.1)

        # 推导式: 31 - 15 = 16
        july_formula = VGroup(
            MathTex(r"31", font_size=28, color=COLOR_JULY),
            MathTex(r"-", font_size=28, color=WHITE),
            MathTex(r"15", font_size=28, color=COLOR_START),
            MathTex(r"=", font_size=28, color=WHITE),
            MathTex(r"16", font_size=32, color=COLOR_HL),
            Text("天", font=FONT, font_size=22, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.12).move_to(UP * 1.8)

        explain_july = Text(
            "7月共31天, 从15日出发,\n还剩 31-15=16 天",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(UP * 0.4)

        self.play(Create(seg1_line), run_time=0.8)
        self.play(GrowFromCenter(seg1_brace), FadeIn(seg1_lbl), run_time=0.6)
        self.play(FadeIn(july_formula, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(explain_july), run_time=0.5)
        self.wait(1.5)

        # ── 第二段: 8月1日 → 8月20日（20天）
        seg2_line = Line(p_july31, p_aug20, color=COLOR_AUG, stroke_width=8)
        seg2_brace = Brace(seg2_line, direction=UP, buff=0.08, color=COLOR_AUG)

        seg2_lbl = VGroup(
            Text("8月已过", font=FONT, font_size=20, color=COLOR_AUG),
            MathTex(r"20", font_size=30, color=COLOR_AUG),
            Text("天", font=FONT, font_size=20, color=COLOR_AUG),
        ).arrange(RIGHT, buff=0.1)
        seg2_lbl.next_to(seg2_brace, UP, buff=0.1)

        aug_formula = VGroup(
            Text("8月过了", font=FONT, font_size=28, color=COLOR_AUG),
            MathTex(r"20", font_size=32, color=COLOR_AUG),
            Text("天", font=FONT, font_size=28, color=COLOR_AUG),
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 0.9)

        self.play(
            FadeOut(explain_july),
            run_time=0.3,
        )
        self.play(Create(seg2_line), run_time=0.8)
        self.play(GrowFromCenter(seg2_brace), FadeIn(seg2_lbl), run_time=0.6)
        self.play(FadeIn(aug_formula, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(1.2)

        # ── 合计
        total_box_bg = RoundedRectangle(
            width=6.5, height=1.4,
            corner_radius=0.25,
            color=COLOR_HL,
            stroke_width=2.5,
            fill_color=COLOR_HL,
            fill_opacity=0.08,
        ).move_to(DOWN * 2.8)

        total_line = VGroup(
            MathTex(r"16", font_size=34, color=COLOR_JULY),
            MathTex(r"+", font_size=34, color=WHITE),
            MathTex(r"20", font_size=34, color=COLOR_AUG),
            MathTex(r"=", font_size=34, color=WHITE),
            MathTex(r"36", font_size=42, color=COLOR_HL),
            Text("天", font=FONT, font_size=30, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.8)

        self.play(FadeIn(total_box_bg), run_time=0.4)
        self.play(FadeIn(total_line, scale=0.9), run_time=0.8)

        answer_confirm = Text(
            "共经过 36 天！",
            font=FONT, font_size=28, color=WHITE,
        ).move_to(DOWN * 4.3)

        self.play(FadeIn(answer_confirm, shift=UP * 0.3), run_time=0.6)
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(timeline),
            FadeOut(dot_july15), FadeOut(dot_july31), FadeOut(dot_aug20),
            FadeOut(lbl_july15), FadeOut(lbl_july31), FadeOut(lbl_aug20),
            FadeOut(seg1_line), FadeOut(seg1_brace), FadeOut(seg1_lbl),
            FadeOut(seg2_line), FadeOut(seg2_brace), FadeOut(seg2_lbl),
            FadeOut(july_formula), FadeOut(aug_formula),
            FadeOut(total_box_bg), FadeOut(total_line),
            FadeOut(answer_confirm),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 5: 列式计算法
    # ------------------------------------------------------------------

    def scene_5_formula_method(self):
        title = Text("方法③ 列式计算", font=FONT, font_size=34, color=COLOR_FORMULA)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 问题重述
        problem = VGroup(
            Text("从", font=FONT, font_size=28, color=WHITE),
            Text("7月15日", font=FONT, font_size=28, color=COLOR_START),
            Text("到", font=FONT, font_size=28, color=WHITE),
            Text("8月20日", font=FONT, font_size=28, color=COLOR_END),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 4.5)
        self.play(FadeIn(problem), run_time=0.5)

        # 步骤卡片
        step_y = [3.2, 1.5, -0.2]

        # Step 1: 7月剩余天数
        step1_tag = Text("第①步", font=FONT, font_size=22, color=COLOR_JULY)
        step1_desc = Text("算7月剩余天数", font=FONT, font_size=24, color=WHITE)
        step1_formula = VGroup(
            MathTex(r"31", font_size=34, color=COLOR_JULY),
            MathTex(r"-", font_size=34, color=WHITE),
            MathTex(r"15", font_size=34, color=COLOR_START),
            MathTex(r"=", font_size=34, color=WHITE),
            MathTex(r"16", font_size=38, color=COLOR_HL),
            Text("(天)", font=FONT, font_size=24, color=GRAY_A),
        ).arrange(RIGHT, buff=0.14)
        step1 = VGroup(
            VGroup(step1_tag, step1_desc).arrange(RIGHT, buff=0.2),
            step1_formula,
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        step1.move_to(UP * step_y[0])

        self.play(FadeIn(step1, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(0.8)

        # Step 2: 8月已过天数
        step2_tag = Text("第②步", font=FONT, font_size=22, color=COLOR_AUG)
        step2_desc = Text("算8月已过天数", font=FONT, font_size=24, color=WHITE)
        step2_formula = VGroup(
            Text("8月过了", font=FONT, font_size=28, color=COLOR_AUG),
            MathTex(r"20", font_size=38, color=COLOR_AUG),
            Text("天", font=FONT, font_size=28, color=GRAY_A),
        ).arrange(RIGHT, buff=0.14)
        step2 = VGroup(
            VGroup(step2_tag, step2_desc).arrange(RIGHT, buff=0.2),
            step2_formula,
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        step2.move_to(UP * step_y[1])

        self.play(FadeIn(step2, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(0.8)

        # Step 3: 相加
        step3_tag = Text("第③步", font=FONT, font_size=22, color=COLOR_FORMULA)
        step3_desc = Text("两段相加", font=FONT, font_size=24, color=WHITE)
        step3_formula = VGroup(
            MathTex(r"16", font_size=34, color=COLOR_JULY),
            MathTex(r"+", font_size=34, color=WHITE),
            MathTex(r"20", font_size=34, color=COLOR_AUG),
            MathTex(r"=", font_size=34, color=WHITE),
            MathTex(r"36", font_size=42, color=COLOR_HL),
            Text("(天)", font=FONT, font_size=24, color=GRAY_A),
        ).arrange(RIGHT, buff=0.14)
        step3 = VGroup(
            VGroup(step3_tag, step3_desc).arrange(RIGHT, buff=0.2),
            step3_formula,
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        step3.move_to(UP * step_y[2])

        self.play(FadeIn(step3, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(0.8)

        # 最终答案框
        ans_box = RoundedRectangle(
            width=7.0, height=1.6,
            corner_radius=0.3,
            color=COLOR_HL,
            stroke_width=3,
            fill_color=COLOR_HL,
            fill_opacity=0.1,
        ).move_to(DOWN * 2.5)

        ans_text = VGroup(
            Text("答：共经过", font=FONT, font_size=30, color=WHITE),
            MathTex(r"36", font_size=44, color=COLOR_HL),
            Text("天", font=FONT, font_size=30, color=WHITE),
        ).arrange(RIGHT, buff=0.18).move_to(DOWN * 2.5)

        self.play(FadeIn(ans_box), run_time=0.4)
        self.play(FadeIn(ans_text, scale=0.9), run_time=0.7)
        self.play(Indicate(ans_text, color=COLOR_HL, scale_factor=1.08), run_time=0.8)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(problem),
            FadeOut(step1), FadeOut(step2), FadeOut(step3),
            FadeOut(ans_box), FadeOut(ans_text),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 6: 知识总结
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        title = Text("知识总结", font=FONT, font_size=36, color=COLOR_HL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        card_bg = RoundedRectangle(
            width=7.8, height=10.0,
            corner_radius=0.35,
            color=WHITE,
            stroke_width=2,
            fill_color=WHITE,
            fill_opacity=0.04,
        ).move_to(UP * 0.0)
        self.play(FadeIn(card_bg), run_time=0.4)

        # 核心题目回顾
        prob_recap = VGroup(
            Text("例题", font=FONT, font_size=22, color=GRAY_A),
            Text("7月15日 → 8月20日 共几天?", font=FONT, font_size=24, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.25).move_to(UP * 3.8)
        self.play(FadeIn(prob_recap, shift=UP * 0.2), run_time=0.5)

        divider = Line(
            np.array([-3.5, 3.2, 0.0]),
            np.array([ 3.5, 3.2, 0.0]),
            color=GRAY_D, stroke_width=1.5,
        )
        self.play(Create(divider), run_time=0.3)

        # 方法一
        m1_title = Text("分段法（推荐）", font=FONT, font_size=26, color=COLOR_JULY)
        m1_step1 = VGroup(
            Text("7月：", font=FONT, font_size=22, color=COLOR_JULY),
            MathTex(r"31 - 15 = 16", font_size=26, color=WHITE),
            Text("天", font=FONT, font_size=22, color=GRAY_A),
        ).arrange(RIGHT, buff=0.12)
        m1_step2 = VGroup(
            Text("8月：", font=FONT, font_size=22, color=COLOR_AUG),
            MathTex(r"20", font_size=26, color=WHITE),
            Text("天", font=FONT, font_size=22, color=GRAY_A),
        ).arrange(RIGHT, buff=0.12)
        m1_step3 = VGroup(
            Text("共：", font=FONT, font_size=22, color=COLOR_HL),
            MathTex(r"16 + 20 = 36", font_size=26, color=COLOR_HL),
            Text("天", font=FONT, font_size=22, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.12)

        m1_block = VGroup(m1_title, m1_step1, m1_step2, m1_step3).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT
        ).move_to(UP * 1.8 + LEFT * 0.4)

        self.play(FadeIn(m1_block, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(0.5)

        divider2 = Line(
            np.array([-3.5, 0.4, 0.0]),
            np.array([ 3.5, 0.4, 0.0]),
            color=GRAY_D, stroke_width=1.5,
        )
        self.play(Create(divider2), run_time=0.3)

        # 关键公式提示
        key_title = Text("记住公式", font=FONT, font_size=26, color=COLOR_FORMULA)
        key_line = VGroup(
            Text("本月剩余天数", font=FONT, font_size=20, color=COLOR_JULY),
            MathTex(r"=", font_size=24, color=WHITE),
            Text("本月天数", font=FONT, font_size=20, color=WHITE),
            MathTex(r"-", font_size=24, color=WHITE),
            Text("出发日", font=FONT, font_size=20, color=COLOR_START),
        ).arrange(RIGHT, buff=0.12)
        key_note = Text(
            "（注意：不含出发当天）",
            font=FONT, font_size=18, color=GRAY_B,
        )
        key_block = VGroup(key_title, key_line, key_note).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT
        ).move_to(DOWN * 1.2 + LEFT * 0.3)

        self.play(FadeIn(key_block, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(0.5)

        divider3 = Line(
            np.array([-3.5, -2.8, 0.0]),
            np.array([ 3.5, -2.8, 0.0]),
            color=GRAY_D, stroke_width=1.5,
        )
        self.play(Create(divider3), run_time=0.3)

        # 最终答案
        final_ans = VGroup(
            Text("最终答案：共经过", font=FONT, font_size=26, color=WHITE),
            MathTex(r"36", font_size=40, color=COLOR_HL),
            Text("天", font=FONT, font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.18).move_to(DOWN * 3.5)

        self.play(FadeIn(final_ans, scale=0.9), run_time=0.7)
        self.play(Indicate(final_ans, color=COLOR_HL, scale_factor=1.06), run_time=0.8)

        self.wait(3.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(prob_recap), FadeOut(divider),
            FadeOut(m1_block),
            FadeOut(divider2), FadeOut(key_block),
            FadeOut(divider3), FadeOut(final_ans),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_B,
        ).move_to(UP * 0.6)

        self.play(
            ReplacementTransform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我，学更多小学数学!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 0.8)

        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 日历装饰：几个小方块模拟日历格
        deco = VGroup()
        cols = [COLOR_JULY, COLOR_AUG, COLOR_FORMULA, COLOR_START, COLOR_END]
        for i, col in enumerate(cols):
            sq = Square(
                side_length=0.5,
                color=col,
                fill_color=col,
                fill_opacity=0.6,
                stroke_width=2,
            ).move_to(DOWN * 2.8 + LEFT * 2.0 + RIGHT * i * 1.0)
            deco.add(sq)

        self.play(*[FadeIn(d, scale=0.5) for d in deco], run_time=0.6)
        self.play(
            *[d.animate.set_fill(opacity=0.3) for d in deco],
            *[d.animate.set_fill(opacity=0.8) for d in deco],
            run_time=1.0,
        )
        self.wait(2.0)

        # 全淡出
        self.play(
            FadeOut(author_big),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(deco),
            run_time=1.0,
        )


# 运行命令:
# manim -pql 002_计算经过天数.py CountingDaysLesson   # 快速预览
# manim -qm  002_计算经过天数.py CountingDaysLesson   # 中等质量
# manim -qh  002_计算经过天数.py CountingDaysLesson   # 高质量
