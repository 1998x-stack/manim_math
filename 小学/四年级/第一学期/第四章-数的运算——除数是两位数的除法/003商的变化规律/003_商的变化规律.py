"""
003_商的变化规律.py — 商的变化规律 教学动画

知识点:
  ① 除数不变, 被除数乘(或除以)几(0除外), 商也乘(或除以)几
  ② 被除数不变, 除数乘(或除以)几(0除外), 商反而除以(或乘)几
  ③ 被除数和除数都乘(或除以)相同的数(0除外), 商不变
     应用: 360÷40 = 36÷4 = 9

年级: 四年级第一学期
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
# 颜色与字体常量
# ======================================================================
BG_COLOR       = "#1a1a2e"
COLOR_DIVIDEND = "#3b82f6"   # 蓝色  被除数
COLOR_DIVISOR  = "#f59e0b"   # 橙色  除数
COLOR_RESULT   = "#22c55e"   # 绿色  商
COLOR_ARROW    = "#a78bfa"   # 紫色  箭头/变换
COLOR_HL       = "#fbbf24"   # 黄色  高亮
COLOR_GRAY_TXT = "#9ca3af"   # 灰色  辅助文字
COLOR_AUTHOR   = "#6b7280"   # 灰色  作者信息
COLOR_RULE1    = "#38bdf8"   # 规律1
COLOR_RULE2    = "#fb923c"   # 规律2
COLOR_RULE3    = "#86efac"   # 规律3
FONT           = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class QuotientPatternLesson(Scene):
    """
    商的变化规律 教学动画

    场景顺序:
      1. 开场钩子 — 引出问题 360÷40 如何简算?
      2. 规律一   — 除数不变, 被除数×n, 商×n
      3. 规律二   — 被除数不变, 除数×n, 商÷n
      4. 规律三   — 商不变性质 (被除数除数同乘同除)
      5. 简便运算 — 应用规律三: 360÷40 = 36÷4 = 9
      6. 综合练习 — 三道练习题
      7. 总结     — 三条规律汇总
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_constants()

        self.scene_1_opening()
        self.scene_2_rule1()
        self.scene_3_rule2()
        self.scene_4_rule3()
        self.scene_5_simplification()
        self.scene_6_practice()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # 常量初始化
    # ------------------------------------------------------------------

    def setup_constants(self):
        """初始化基本参数"""
        self.BASE_DIVIDEND = 60
        self.BASE_DIVISOR  = 20
        self.BASE_QUOTIENT = 3   # 60 ÷ 20 = 3

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def make_title_bar(self, text, color=WHITE, font_size=32):
        return Text(text, font=FONT, font_size=font_size, color=color).move_to(UP * 5.8)

    def make_division_row(self, dividend_str, divisor_str, quotient_str,
                          d_color=COLOR_DIVIDEND, s_color=COLOR_DIVISOR, q_color=COLOR_RESULT,
                          font_size=44):
        """
        构建一行除法算式  被除数 ÷ 除数 = 商
        全部使用 Text，避免中文或特殊符号进入 MathTex
        """
        dnd     = Text(dividend_str,  font=FONT, font_size=font_size, color=d_color)
        div_sym = Text("÷",           font=FONT, font_size=font_size, color=WHITE)
        dsr     = Text(divisor_str,   font=FONT, font_size=font_size, color=s_color)
        eq      = Text("=",           font=FONT, font_size=font_size, color=WHITE)
        q       = Text(quotient_str,  font=FONT, font_size=font_size, color=q_color)
        return VGroup(dnd, div_sym, dsr, eq, q).arrange(RIGHT, buff=0.20)

    def draw_side_arrow(self, start, end, label_str, color=COLOR_ARROW, tip_side=LEFT):
        """画从 start 到 end 的箭头 + 旁边文字"""
        arr = Arrow(
            start=start, end=end,
            color=color, stroke_width=3,
            buff=0.05,
            max_tip_length_to_length_ratio=0.22,
        )
        lbl = Text(label_str, font=FONT, font_size=22, color=color)
        lbl.next_to(arr, tip_side, buff=0.15)
        return VGroup(arr, lbl)

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text(
            "360 ÷ 40 怎么口算?",
            font=FONT, font_size=38, color=COLOR_HL,
        ).move_to(UP * 5.0)
        self.play(Write(hook1), run_time=0.8)

        hook2 = Text(
            "末尾的 0 可以同时划掉!",
            font=FONT, font_size=30, color=COLOR_GRAY_TXT,
        ).move_to(UP * 4.0)
        self.play(FadeIn(hook2, shift=UP * 0.2), run_time=0.5)

        # 展示 360 ÷ 40
        demo_before = VGroup(
            Text("360", font=FONT, font_size=54, color=COLOR_DIVIDEND),
            Text("÷",   font=FONT, font_size=54, color=WHITE),
            Text("40",  font=FONT, font_size=54, color=COLOR_DIVISOR),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.0)
        self.play(FadeIn(demo_before), run_time=0.5)

        # 划去末尾0的红斜线
        cross1 = Line(
            demo_before[0].get_right() + LEFT * 0.32 + DOWN * 0.32,
            demo_before[0].get_right() + LEFT * 0.04 + UP * 0.32,
            color=RED, stroke_width=5,
        )
        cross2 = Line(
            demo_before[2].get_right() + LEFT * 0.32 + DOWN * 0.32,
            demo_before[2].get_right() + LEFT * 0.04 + UP * 0.32,
            color=RED, stroke_width=5,
        )
        self.play(Create(cross1), Create(cross2), run_time=0.5)

        arrow_right = Text("⇒", font=FONT, font_size=48, color=COLOR_ARROW).move_to(UP * 0.8)
        result_simple = VGroup(
            Text("36", font=FONT, font_size=54, color=COLOR_DIVIDEND),
            Text("÷",  font=FONT, font_size=54, color=WHITE),
            Text("4",  font=FONT, font_size=54, color=COLOR_DIVISOR),
            Text("=",  font=FONT, font_size=54, color=WHITE),
            Text("9",  font=FONT, font_size=54, color=COLOR_RESULT),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 0.2)

        self.play(Write(arrow_right), run_time=0.4)
        self.play(FadeIn(result_simple), run_time=0.6)
        self.wait(0.5)

        why_text = Text(
            "为什么可以这样做? 来看三条规律!",
            font=FONT, font_size=22, color=COLOR_GRAY_TXT,
        ).move_to(DOWN * 1.6)
        self.play(FadeIn(why_text, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(hook1), FadeOut(hook2),
            FadeOut(demo_before), FadeOut(cross1), FadeOut(cross2),
            FadeOut(arrow_right), FadeOut(result_simple), FadeOut(why_text),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 规律一 — 除数不变, 被除数×n, 商×n
    # ------------------------------------------------------------------

    def scene_2_rule1(self):
        title = self.make_title_bar("规律一", color=COLOR_RULE1)
        self.play(Write(title), run_time=0.4)

        rule_desc = Text(
            "除数不变, 被除数×几, 商也×几",
            font=FONT, font_size=26, color=COLOR_RULE1,
        ).move_to(UP * 4.9)
        self.play(FadeIn(rule_desc, shift=UP * 0.2), run_time=0.5)

        # 基础算式: 60 ÷ 20 = 3
        row0 = self.make_division_row("60", "20", "3", font_size=44).move_to(UP * 3.2)
        self.play(FadeIn(row0), run_time=0.5)
        self.wait(0.3)

        # --- 被除数 ×2 ---
        arr_dnd_x2 = self.draw_side_arrow(
            row0[0].get_bottom() + DOWN * 0.12,
            row0[0].get_bottom() + DOWN * 1.55,
            "×2", color=COLOR_RULE1, tip_side=LEFT,
        )
        arr_q_x2 = self.draw_side_arrow(
            row0[4].get_bottom() + DOWN * 0.12,
            row0[4].get_bottom() + DOWN * 1.55,
            "×2", color=COLOR_RESULT, tip_side=RIGHT,
        )
        fixed_lbl1 = Text("(不变)", font=FONT, font_size=18, color=COLOR_DIVISOR).move_to(
            row0[2].get_bottom() + DOWN * 0.85
        )

        row1 = self.make_division_row("120", "20", "6", font_size=44).move_to(
            row0.get_center() + DOWN * 1.8
        )

        self.play(Create(arr_dnd_x2[0]), FadeIn(arr_dnd_x2[1]), run_time=0.5)
        self.play(FadeIn(fixed_lbl1), run_time=0.3)
        self.play(FadeIn(row1), run_time=0.5)
        self.play(Create(arr_q_x2[0]), FadeIn(arr_q_x2[1]), run_time=0.4)
        self.wait(0.5)

        # --- 被除数 ×3 (从 row1) ---
        arr_dnd_x3 = self.draw_side_arrow(
            row1[0].get_bottom() + DOWN * 0.12,
            row1[0].get_bottom() + DOWN * 1.55,
            "×3", color=COLOR_RULE1, tip_side=LEFT,
        )
        arr_q_x3 = self.draw_side_arrow(
            row1[4].get_bottom() + DOWN * 0.12,
            row1[4].get_bottom() + DOWN * 1.55,
            "×3", color=COLOR_RESULT, tip_side=RIGHT,
        )
        fixed_lbl2 = Text("(不变)", font=FONT, font_size=18, color=COLOR_DIVISOR).move_to(
            row1[2].get_bottom() + DOWN * 0.85
        )

        row2 = self.make_division_row("360", "20", "18", font_size=44).move_to(
            row1.get_center() + DOWN * 1.8
        )

        self.play(Create(arr_dnd_x3[0]), FadeIn(arr_dnd_x3[1]), run_time=0.5)
        self.play(FadeIn(fixed_lbl2), run_time=0.3)
        self.play(FadeIn(row2), run_time=0.5)
        self.play(Create(arr_q_x3[0]), FadeIn(arr_q_x3[1]), run_time=0.4)
        self.wait(0.5)

        # 高亮规律框
        hl_box = SurroundingRectangle(rule_desc, color=COLOR_RULE1, stroke_width=2, buff=0.15)
        self.play(Create(hl_box), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(rule_desc), FadeOut(hl_box),
            FadeOut(row0), FadeOut(row1), FadeOut(row2),
            FadeOut(arr_dnd_x2), FadeOut(arr_q_x2), FadeOut(fixed_lbl1),
            FadeOut(arr_dnd_x3), FadeOut(arr_q_x3), FadeOut(fixed_lbl2),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 规律二 — 被除数不变, 除数×n, 商÷n
    # ------------------------------------------------------------------

    def scene_3_rule2(self):
        title = self.make_title_bar("规律二", color=COLOR_RULE2)
        self.play(Write(title), run_time=0.4)

        rule_desc = Text(
            "被除数不变, 除数×几, 商反而÷几",
            font=FONT, font_size=24, color=COLOR_RULE2,
        ).move_to(UP * 4.9)
        self.play(FadeIn(rule_desc, shift=UP * 0.2), run_time=0.5)

        # 基础算式: 240 ÷ 20 = 12
        row0 = self.make_division_row("240", "20", "12", font_size=44).move_to(UP * 3.2)
        self.play(FadeIn(row0), run_time=0.5)
        self.wait(0.3)

        # 被除数不变
        fixed_dnd1 = Text("(不变)", font=FONT, font_size=18, color=COLOR_DIVIDEND).move_to(
            row0[0].get_bottom() + DOWN * 0.85
        )

        # 除数 ×2 → 商 ÷2
        arr_s_x2 = self.draw_side_arrow(
            row0[2].get_bottom() + DOWN * 0.12,
            row0[2].get_bottom() + DOWN * 1.55,
            "×2", color=COLOR_DIVISOR, tip_side=RIGHT,
        )
        arr_q_d2 = self.draw_side_arrow(
            row0[4].get_bottom() + DOWN * 0.12,
            row0[4].get_bottom() + DOWN * 1.55,
            "÷2", color=COLOR_RESULT, tip_side=RIGHT,
        )

        row1 = self.make_division_row("240", "40", "6", font_size=44).move_to(
            row0.get_center() + DOWN * 1.8
        )

        self.play(FadeIn(fixed_dnd1), run_time=0.3)
        self.play(Create(arr_s_x2[0]), FadeIn(arr_s_x2[1]), run_time=0.5)
        self.play(FadeIn(row1), run_time=0.5)
        self.play(Create(arr_q_d2[0]), FadeIn(arr_q_d2[1]), run_time=0.4)
        self.wait(0.5)

        # 除数 ×3 → 商 ÷3
        fixed_dnd2 = Text("(不变)", font=FONT, font_size=18, color=COLOR_DIVIDEND).move_to(
            row1[0].get_bottom() + DOWN * 0.85
        )
        arr_s_x3 = self.draw_side_arrow(
            row1[2].get_bottom() + DOWN * 0.12,
            row1[2].get_bottom() + DOWN * 1.55,
            "×3", color=COLOR_DIVISOR, tip_side=RIGHT,
        )
        arr_q_d3 = self.draw_side_arrow(
            row1[4].get_bottom() + DOWN * 0.12,
            row1[4].get_bottom() + DOWN * 1.55,
            "÷3", color=COLOR_RESULT, tip_side=RIGHT,
        )
        row2 = self.make_division_row("240", "120", "2", font_size=44).move_to(
            row1.get_center() + DOWN * 1.8
        )

        self.play(FadeIn(fixed_dnd2), run_time=0.3)
        self.play(Create(arr_s_x3[0]), FadeIn(arr_s_x3[1]), run_time=0.5)
        self.play(FadeIn(row2), run_time=0.5)
        self.play(Create(arr_q_d3[0]), FadeIn(arr_q_d3[1]), run_time=0.4)
        self.wait(0.5)

        # 强调"反而"
        fanrui = Text(
            "注意: 除数变大, 商反而变小!",
            font=FONT, font_size=22, color=COLOR_HL,
        ).move_to(DOWN * 5.3)
        self.play(FadeIn(fanrui, shift=UP * 0.2), run_time=0.5)

        hl_box = SurroundingRectangle(rule_desc, color=COLOR_RULE2, stroke_width=2, buff=0.15)
        self.play(Create(hl_box), run_time=0.4)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(rule_desc), FadeOut(hl_box),
            FadeOut(row0), FadeOut(row1), FadeOut(row2),
            FadeOut(fixed_dnd1), FadeOut(fixed_dnd2),
            FadeOut(arr_s_x2), FadeOut(arr_q_d2),
            FadeOut(arr_s_x3), FadeOut(arr_q_d3),
            FadeOut(fanrui),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 4: 规律三 — 商不变性质
    # ------------------------------------------------------------------

    def scene_4_rule3(self):
        title = self.make_title_bar("规律三  (最重要!)", color=COLOR_RULE3)
        self.play(Write(title), run_time=0.4)

        rule_desc = Text(
            "被除数和除数同时×(或÷)同一个数,",
            font=FONT, font_size=22, color=COLOR_RULE3,
        ).move_to(UP * 4.85)
        rule_desc2 = Text(
            "商不变。",
            font=FONT, font_size=22, color=COLOR_RULE3,
        ).next_to(rule_desc, DOWN, buff=0.1)
        self.play(FadeIn(rule_desc), FadeIn(rule_desc2), run_time=0.5)

        # 基础: 60 ÷ 20 = 3
        row0 = self.make_division_row("60", "20", "3", font_size=44).move_to(UP * 3.4)
        self.play(FadeIn(row0), run_time=0.5)

        # 同时 ×2
        arr_dnd_x2 = self.draw_side_arrow(
            row0[0].get_bottom() + DOWN * 0.12,
            row0[0].get_bottom() + DOWN * 1.55,
            "×2", color=COLOR_DIVIDEND, tip_side=LEFT,
        )
        arr_dsr_x2 = self.draw_side_arrow(
            row0[2].get_bottom() + DOWN * 0.12,
            row0[2].get_bottom() + DOWN * 1.55,
            "×2", color=COLOR_DIVISOR, tip_side=RIGHT,
        )
        row1 = self.make_division_row("120", "40", "3", font_size=44).move_to(
            row0.get_center() + DOWN * 1.8
        )
        same_q1 = Text("商不变!", font=FONT, font_size=22, color=COLOR_RESULT).next_to(
            row1[4], RIGHT, buff=0.3
        )

        self.play(
            Create(arr_dnd_x2[0]), FadeIn(arr_dnd_x2[1]),
            Create(arr_dsr_x2[0]), FadeIn(arr_dsr_x2[1]),
            run_time=0.5,
        )
        self.play(FadeIn(row1), run_time=0.5)
        self.play(FadeIn(same_q1), run_time=0.3)
        self.play(Indicate(row1[4], color=COLOR_HL, scale_factor=1.3), run_time=0.5)
        self.wait(0.4)

        # 同时 ×5
        arr_dnd_x5 = self.draw_side_arrow(
            row1[0].get_bottom() + DOWN * 0.12,
            row1[0].get_bottom() + DOWN * 1.55,
            "×5", color=COLOR_DIVIDEND, tip_side=LEFT,
        )
        arr_dsr_x5 = self.draw_side_arrow(
            row1[2].get_bottom() + DOWN * 0.12,
            row1[2].get_bottom() + DOWN * 1.55,
            "×5", color=COLOR_DIVISOR, tip_side=RIGHT,
        )
        row2 = self.make_division_row("600", "200", "3", font_size=44).move_to(
            row1.get_center() + DOWN * 1.8
        )
        same_q2 = Text("商不变!", font=FONT, font_size=22, color=COLOR_RESULT).next_to(
            row2[4], RIGHT, buff=0.3
        )

        self.play(
            Create(arr_dnd_x5[0]), FadeIn(arr_dnd_x5[1]),
            Create(arr_dsr_x5[0]), FadeIn(arr_dsr_x5[1]),
            run_time=0.5,
        )
        self.play(FadeIn(row2), run_time=0.5)
        self.play(FadeIn(same_q2), run_time=0.3)
        self.play(Indicate(row2[4], color=COLOR_HL, scale_factor=1.3), run_time=0.5)
        self.wait(0.4)

        # 反向: 同时 ÷10
        arr_dnd_d10 = self.draw_side_arrow(
            row0[0].get_top() + UP * 0.12,
            row0[0].get_top() + UP * 1.55,
            "÷10", color=COLOR_DIVIDEND, tip_side=LEFT,
        )
        arr_dsr_d10 = self.draw_side_arrow(
            row0[2].get_top() + UP * 0.12,
            row0[2].get_top() + UP * 1.55,
            "÷10", color=COLOR_DIVISOR, tip_side=RIGHT,
        )
        row_up = self.make_division_row("6", "2", "3", font_size=44).move_to(
            row0.get_center() + UP * 1.8
        )
        same_q_up = Text("商不变!", font=FONT, font_size=22, color=COLOR_RESULT).next_to(
            row_up[4], RIGHT, buff=0.3
        )

        self.play(
            Create(arr_dnd_d10[0]), FadeIn(arr_dnd_d10[1]),
            Create(arr_dsr_d10[0]), FadeIn(arr_dsr_d10[1]),
            run_time=0.5,
        )
        self.play(FadeIn(row_up), run_time=0.5)
        self.play(FadeIn(same_q_up), run_time=0.3)
        self.play(Indicate(row_up[4], color=COLOR_HL, scale_factor=1.3), run_time=0.5)
        self.wait(0.5)

        hl_box = SurroundingRectangle(
            VGroup(rule_desc, rule_desc2), color=COLOR_RULE3, stroke_width=2, buff=0.15
        )
        self.play(Create(hl_box), run_time=0.4)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(rule_desc), FadeOut(rule_desc2), FadeOut(hl_box),
            FadeOut(row0), FadeOut(row1), FadeOut(row2), FadeOut(row_up),
            FadeOut(arr_dnd_x2), FadeOut(arr_dsr_x2), FadeOut(same_q1),
            FadeOut(arr_dnd_x5), FadeOut(arr_dsr_x5), FadeOut(same_q2),
            FadeOut(arr_dnd_d10), FadeOut(arr_dsr_d10), FadeOut(same_q_up),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 5: 简便运算 — 360÷40 = 36÷4 = 9
    # ------------------------------------------------------------------

    def scene_5_simplification(self):
        title = self.make_title_bar("简便运算", color=COLOR_HL)
        self.play(Write(title), run_time=0.4)

        intro = Text(
            "利用规律三, 末尾有0可同时划去!",
            font=FONT, font_size=24, color=COLOR_GRAY_TXT,
        ).move_to(UP * 4.9)
        self.play(FadeIn(intro, shift=UP * 0.2), run_time=0.5)

        # 展示 360 ÷ 40
        orig = VGroup(
            Text("360", font=FONT, font_size=60, color=COLOR_DIVIDEND),
            Text("÷",   font=FONT, font_size=60, color=WHITE),
            Text("40",  font=FONT, font_size=60, color=COLOR_DIVISOR),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 3.3)
        self.play(FadeIn(orig), run_time=0.5)

        # 标注
        note_div10 = Text(
            "被除数和除数同时 ÷10",
            font=FONT, font_size=22, color=COLOR_RULE3,
        ).move_to(UP * 2.2)
        self.play(FadeIn(note_div10), run_time=0.4)

        # 划去末尾0 — 红色斜线
        cross_360 = Line(
            orig[0].get_right() + LEFT * 0.36 + DOWN * 0.36,
            orig[0].get_right() + LEFT * 0.03 + UP * 0.36,
            color=RED, stroke_width=5,
        )
        cross_40 = Line(
            orig[2].get_right() + LEFT * 0.36 + DOWN * 0.36,
            orig[2].get_right() + LEFT * 0.03 + UP * 0.36,
            color=RED, stroke_width=5,
        )
        self.play(Create(cross_360), Create(cross_40), run_time=0.5)
        self.wait(0.3)

        arrow_eq = Text("⇒", font=FONT, font_size=52, color=COLOR_ARROW).move_to(UP * 1.2)
        self.play(Write(arrow_eq), run_time=0.4)

        # 简化后: 36 ÷ 4 = 9
        simplified = VGroup(
            Text("36", font=FONT, font_size=60, color=COLOR_DIVIDEND),
            Text("÷",  font=FONT, font_size=60, color=WHITE),
            Text("4",  font=FONT, font_size=60, color=COLOR_DIVISOR),
            Text("=",  font=FONT, font_size=60, color=WHITE),
            Text("9",  font=FONT, font_size=60, color=COLOR_RESULT),
        ).arrange(RIGHT, buff=0.28).move_to(UP * 0.1)
        self.play(FadeIn(simplified), run_time=0.6)
        self.wait(0.4)
        self.play(Indicate(simplified[4], color=COLOR_HL, scale_factor=1.3), run_time=0.5)

        # 完整等式
        full_eq = Text(
            "所以 360÷40 = 36÷4 = 9",
            font=FONT, font_size=28, color=WHITE,
        ).move_to(DOWN * 1.4)
        self.play(FadeIn(full_eq, shift=UP * 0.2), run_time=0.5)

        verify = Text(
            "商不变! (规律三)",
            font=FONT, font_size=24, color=COLOR_RULE3,
        ).move_to(DOWN * 2.4)
        self.play(FadeIn(verify), run_time=0.4)
        self.wait(0.5)

        # 再举一例: 480 ÷ 60
        sep = Line(LEFT * 3.8, RIGHT * 3.8, color=GRAY_B, stroke_width=1).move_to(DOWN * 3.2)
        self.play(Create(sep), run_time=0.3)

        ex2_label = Text("再练一个:", font=FONT, font_size=24, color=COLOR_ARROW).move_to(DOWN * 3.8)
        self.play(FadeIn(ex2_label), run_time=0.3)

        ex2_row = VGroup(
            Text("480", font=FONT, font_size=38, color=COLOR_DIVIDEND),
            Text("÷",   font=FONT, font_size=38, color=WHITE),
            Text("60",  font=FONT, font_size=38, color=COLOR_DIVISOR),
            Text("=",   font=FONT, font_size=38, color=WHITE),
            Text("48",  font=FONT, font_size=38, color=COLOR_DIVIDEND),
            Text("÷",   font=FONT, font_size=38, color=WHITE),
            Text("6",   font=FONT, font_size=38, color=COLOR_DIVISOR),
            Text("=",   font=FONT, font_size=38, color=WHITE),
            Text("8",   font=FONT, font_size=38, color=COLOR_RESULT),
        ).arrange(RIGHT, buff=0.16).move_to(DOWN * 4.9)
        self.play(FadeIn(ex2_row), run_time=0.6)
        self.play(Indicate(ex2_row[8], color=COLOR_HL, scale_factor=1.3), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(intro),
            FadeOut(orig), FadeOut(cross_360), FadeOut(cross_40),
            FadeOut(note_div10), FadeOut(arrow_eq), FadeOut(simplified),
            FadeOut(full_eq), FadeOut(verify),
            FadeOut(sep), FadeOut(ex2_label), FadeOut(ex2_row),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 6: 综合练习
    # ------------------------------------------------------------------

    def scene_6_practice(self):
        title = self.make_title_bar("综合练习", color=COLOR_HL)
        self.play(Write(title), run_time=0.4)

        practice_label = Text(
            "利用规律完成下面各题:",
            font=FONT, font_size=24, color=COLOR_GRAY_TXT,
        ).move_to(UP * 4.9)
        self.play(FadeIn(practice_label), run_time=0.4)

        # --- 练习 1: 规律一 ---
        p1_title = Text("练习 1  (规律一)", font=FONT, font_size=22, color=COLOR_RULE1).move_to(UP * 4.0)
        self.play(FadeIn(p1_title), run_time=0.3)

        # 已知 80÷40=2  → 拆分为多个 Text
        p1_given = VGroup(
            Text("已知 ", font=FONT, font_size=26, color=COLOR_GRAY_TXT),
            Text("80",   font=FONT, font_size=26, color=COLOR_DIVIDEND),
            Text("÷",    font=FONT, font_size=26, color=WHITE),
            Text("40",   font=FONT, font_size=26, color=COLOR_DIVISOR),
            Text("=",    font=FONT, font_size=26, color=WHITE),
            Text("2",    font=FONT, font_size=26, color=COLOR_RESULT),
        ).arrange(RIGHT, buff=0.08).move_to(UP * 3.2)
        self.play(FadeIn(p1_given), run_time=0.4)

        p1_q = VGroup(
            Text("则 ", font=FONT, font_size=26, color=COLOR_GRAY_TXT),
            Text("240", font=FONT, font_size=26, color=COLOR_DIVIDEND),
            Text("÷",   font=FONT, font_size=26, color=WHITE),
            Text("40",  font=FONT, font_size=26, color=COLOR_DIVISOR),
            Text("= ?", font=FONT, font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.08).move_to(UP * 2.3)
        self.play(FadeIn(p1_q), run_time=0.4)

        p1_think = Text(
            "被除数 80×3=240, 除数不变",
            font=FONT, font_size=20, color=COLOR_GRAY_TXT,
        ).move_to(UP * 1.5)
        self.play(FadeIn(p1_think), run_time=0.4)

        p1_ans = VGroup(
            Text("240÷40", font=FONT, font_size=32, color=WHITE),
            Text("=",      font=FONT, font_size=32, color=WHITE),
            Text("2×3",    font=FONT, font_size=32, color=COLOR_RESULT),
            Text("=",      font=FONT, font_size=32, color=WHITE),
            Text("6",      font=FONT, font_size=38, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.6)
        self.play(FadeIn(p1_ans), run_time=0.6)
        self.play(Indicate(p1_ans[4], color=COLOR_HL, scale_factor=1.3), run_time=0.5)
        self.wait(1.0)

        sep1 = Line(LEFT * 3.8, RIGHT * 3.8, color=GRAY_B, stroke_width=1).move_to(DOWN * 0.2)
        self.play(Create(sep1), run_time=0.3)

        # --- 练习 2: 规律三 (简便) ---
        p2_title = Text("练习 2  (规律三)", font=FONT, font_size=22, color=COLOR_RULE3).move_to(DOWN * 0.7)
        self.play(FadeIn(p2_title), run_time=0.3)

        p2_q = Text(
            "计算 720÷90",
            font=FONT, font_size=28, color=WHITE,
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(p2_q), run_time=0.4)

        p2_ans = VGroup(
            Text("720", font=FONT, font_size=32, color=COLOR_DIVIDEND),
            Text("÷",   font=FONT, font_size=32, color=WHITE),
            Text("90",  font=FONT, font_size=32, color=COLOR_DIVISOR),
            Text("=",   font=FONT, font_size=32, color=WHITE),
            Text("72",  font=FONT, font_size=32, color=COLOR_DIVIDEND),
            Text("÷",   font=FONT, font_size=32, color=WHITE),
            Text("9",   font=FONT, font_size=32, color=COLOR_DIVISOR),
            Text("=",   font=FONT, font_size=32, color=WHITE),
            Text("8",   font=FONT, font_size=38, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.5)
        self.play(FadeIn(p2_ans), run_time=0.6)
        self.play(Indicate(p2_ans[8], color=COLOR_HL, scale_factor=1.3), run_time=0.5)

        p2_note = Text(
            "末尾各去掉一个0, 商不变",
            font=FONT, font_size=20, color=COLOR_RULE3,
        ).move_to(DOWN * 3.4)
        self.play(FadeIn(p2_note), run_time=0.4)
        self.wait(1.0)

        sep2 = Line(LEFT * 3.8, RIGHT * 3.8, color=GRAY_B, stroke_width=1).move_to(DOWN * 4.1)
        self.play(Create(sep2), run_time=0.3)

        # --- 练习 3: 规律二 ---
        p3_title = Text("练习 3  (规律二)", font=FONT, font_size=22, color=COLOR_RULE2).move_to(DOWN * 4.7)
        self.play(FadeIn(p3_title), run_time=0.3)

        p3_q = Text(
            "已知 80÷20=4, 则 80÷40=?",
            font=FONT, font_size=22, color=WHITE,
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(p3_q), run_time=0.4)

        p3_ans = VGroup(
            Text("除数×2, 商÷2", font=FONT, font_size=24, color=COLOR_GRAY_TXT),
            Text("⇒",             font=FONT, font_size=28, color=COLOR_ARROW),
            Text("4÷2=",          font=FONT, font_size=28, color=WHITE),
            Text("2",             font=FONT, font_size=32, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 6.5)
        self.play(FadeIn(p3_ans), run_time=0.5)
        self.play(Indicate(p3_ans[3], color=COLOR_HL, scale_factor=1.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(practice_label),
            FadeOut(p1_title), FadeOut(p1_given), FadeOut(p1_q),
            FadeOut(p1_think), FadeOut(p1_ans),
            FadeOut(sep1),
            FadeOut(p2_title), FadeOut(p2_q), FadeOut(p2_ans), FadeOut(p2_note),
            FadeOut(sep2),
            FadeOut(p3_title), FadeOut(p3_q), FadeOut(p3_ans),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 7: 总结 — 三条规律汇总
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        title = self.make_title_bar("商的变化规律  总结", color=COLOR_HL)
        self.play(Write(title), run_time=0.5)

        # 背景卡片
        card_bg = RoundedRectangle(
            width=8.0, height=11.0,
            corner_radius=0.35,
            color=WHITE, stroke_width=2,
            fill_color=WHITE, fill_opacity=0.04,
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(card_bg), run_time=0.4)

        # --- 规律一 ---
        badge1 = VGroup(
            Circle(radius=0.3, color=COLOR_RULE1,
                   fill_color=COLOR_RULE1, fill_opacity=0.3, stroke_width=2),
            Text("①", font=FONT, font_size=20, color=COLOR_RULE1),
        )
        badge1[1].move_to(badge1[0].get_center())
        badge1.move_to(UP * 3.8 + LEFT * 3.3)

        r1_lines = VGroup(
            Text("除数不变,", font=FONT, font_size=22, color=WHITE),
            Text("被除数×n  →  商×n", font=FONT, font_size=22, color=COLOR_RULE1),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(UP * 3.8 + RIGHT * 0.3)

        r1_ex = VGroup(
            Text("60÷20=3", font=FONT, font_size=24, color=COLOR_GRAY_TXT),
            Text("⇒",       font=FONT, font_size=24, color=COLOR_ARROW),
            Text("120÷20=6", font=FONT, font_size=24, color=COLOR_GRAY_TXT),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 3.0)

        self.play(FadeIn(badge1), FadeIn(r1_lines), run_time=0.5)
        self.play(FadeIn(r1_ex, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(0.3)

        # --- 规律二 ---
        badge2 = VGroup(
            Circle(radius=0.3, color=COLOR_RULE2,
                   fill_color=COLOR_RULE2, fill_opacity=0.3, stroke_width=2),
            Text("②", font=FONT, font_size=20, color=COLOR_RULE2),
        )
        badge2[1].move_to(badge2[0].get_center())
        badge2.move_to(UP * 1.7 + LEFT * 3.3)

        r2_lines = VGroup(
            Text("被除数不变,", font=FONT, font_size=22, color=WHITE),
            Text("除数×n  →  商÷n", font=FONT, font_size=22, color=COLOR_RULE2),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(UP * 1.7 + RIGHT * 0.5)

        r2_ex = VGroup(
            Text("240÷20=12", font=FONT, font_size=24, color=COLOR_GRAY_TXT),
            Text("⇒",         font=FONT, font_size=24, color=COLOR_ARROW),
            Text("240÷40=6",  font=FONT, font_size=24, color=COLOR_GRAY_TXT),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.9)

        self.play(FadeIn(badge2), FadeIn(r2_lines), run_time=0.5)
        self.play(FadeIn(r2_ex, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(0.3)

        # --- 规律三 ---
        badge3 = VGroup(
            Circle(radius=0.3, color=COLOR_RULE3,
                   fill_color=COLOR_RULE3, fill_opacity=0.3, stroke_width=2),
            Text("③", font=FONT, font_size=20, color=COLOR_RULE3),
        )
        badge3[1].move_to(badge3[0].get_center())
        badge3.move_to(DOWN * 0.5 + LEFT * 3.3)

        r3_lines = VGroup(
            Text("被除数、除数同时×(÷)n,", font=FONT, font_size=20, color=WHITE),
            Text("商不变!",                   font=FONT, font_size=24, color=COLOR_RULE3),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(DOWN * 0.5 + RIGHT * 0.6)

        r3_ex = VGroup(
            Text("360÷40", font=FONT, font_size=28, color=COLOR_DIVIDEND),
            Text("=",      font=FONT, font_size=28, color=WHITE),
            Text("36÷4",   font=FONT, font_size=28, color=COLOR_DIVIDEND),
            Text("=",      font=FONT, font_size=28, color=WHITE),
            Text("9",      font=FONT, font_size=32, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.4)

        self.play(FadeIn(badge3), FadeIn(r3_lines), run_time=0.5)
        self.play(FadeIn(r3_ex, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.3)

        # 应用提示
        sep_line = Line(LEFT * 3.8, RIGHT * 3.8, color=GRAY_B, stroke_width=1).move_to(DOWN * 2.2)
        self.play(Create(sep_line), run_time=0.3)

        app_title = Text("应用技巧", font=FONT, font_size=24, color=COLOR_HL).move_to(DOWN * 2.8)
        app_body = Text(
            "末尾有0时, 同时划去相同数量的0, 商不变",
            font=FONT, font_size=19, color=COLOR_GRAY_TXT,
        ).move_to(DOWN * 3.6)

        app_ex = VGroup(
            Text("4800", font=FONT, font_size=28, color=COLOR_DIVIDEND),
            Text("÷",    font=FONT, font_size=28, color=WHITE),
            Text("600",  font=FONT, font_size=28, color=COLOR_DIVISOR),
            Text("=",    font=FONT, font_size=28, color=WHITE),
            Text("48",   font=FONT, font_size=28, color=COLOR_DIVIDEND),
            Text("÷",    font=FONT, font_size=28, color=WHITE),
            Text("6",    font=FONT, font_size=28, color=COLOR_DIVISOR),
            Text("=",    font=FONT, font_size=28, color=WHITE),
            Text("8",    font=FONT, font_size=32, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.16).move_to(DOWN * 4.7)

        self.play(FadeIn(app_title), FadeIn(app_body), run_time=0.5)
        self.play(FadeIn(app_ex), run_time=0.5)
        self.play(Indicate(app_ex[8], color=COLOR_HL, scale_factor=1.3), run_time=0.5)
        self.wait(3.0)

        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(badge1), FadeOut(r1_lines), FadeOut(r1_ex),
            FadeOut(badge2), FadeOut(r2_lines), FadeOut(r2_ex),
            FadeOut(badge3), FadeOut(r3_lines), FadeOut(r3_ex),
            FadeOut(sep_line), FadeOut(app_title), FadeOut(app_body), FadeOut(app_ex),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=38, color=WHITE,
        ).move_to(UP * 1.5)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=GRAY_B,
        ).move_to(UP * 0.5)

        self.play(
            ReplacementTransform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 学更多数学技巧!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.5)

        # 三条规律小卡片
        cards_data = [
            ("① 除数不变, 被除数×n  →  商×n", COLOR_RULE1),
            ("② 被除数不变, 除数×n  →  商÷n", COLOR_RULE2),
            ("③ 同时×(÷)n  →  商不变!", COLOR_RULE3),
        ]
        cards = VGroup()
        for txt, clr in cards_data:
            c = Text(txt, font=FONT, font_size=20, color=clr)
            cards.add(c)
        cards.arrange(DOWN, buff=0.4).move_to(DOWN * 3.2)

        self.play(
            *[FadeIn(c, shift=RIGHT * 0.3) for c in cards],
            run_time=0.8,
        )
        self.wait(2.5)

        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(cards),
            run_time=1.0,
        )


# 运行命令:
# manim -qm 003_商的变化规律.py QuotientPatternLesson   # 中等质量
# manim -qh 003_商的变化规律.py QuotientPatternLesson   # 高质量
