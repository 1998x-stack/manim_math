"""
005_小数点移动引起小数大小的变化.py — 小数点移动引起小数大小的变化 教学动画

知识点: 小数点向右移动一位→扩大10倍；向右移动两位→扩大100倍；
        小数点向左移动一位→缩小到原数的1/10；向左移动两位→缩小到原数的1/100
年级: 四年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 小数点右移 — 扩大
  3. 小数点左移 — 缩小
  4. 规律总结
  5. 片尾
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
BG_COLOR    = "#1a1a2e"
COLOR_RIGHT = "#22c55e"   # 绿色 — 右移/扩大
COLOR_LEFT  = "#ef4444"   # 红色 — 左移/缩小
COLOR_DOT   = "#f59e0b"   # 橙色 — 小数点
COLOR_HL    = "#fbbf24"   # 黄色高亮
COLOR_RULE  = "#a78bfa"   # 紫色 — 规律
COLOR_DIGIT = "#60a5fa"   # 蓝色 — 数字
COLOR_AUTHOR = "#6b7280"
FONT = "Noto Sans CJK SC"


# ======================================================================
# 辅助函数
# ======================================================================

def make_decimal_display(number_str: str, dot_color=COLOR_DOT,
                          digit_color=WHITE, font_size=52):
    """
    将数字字符串拆成单个字符，返回 VGroup，小数点单独着色。
    number_str: e.g. "3.5", "35", "0.35"
    """
    chars = []
    for ch in number_str:
        if ch == ".":
            t = Text(ch, font=FONT, font_size=font_size, color=dot_color,
                     weight=BOLD)
        else:
            t = Text(ch, font=FONT, font_size=font_size, color=digit_color,
                     weight=BOLD)
        chars.append(t)
    group = VGroup(*chars).arrange(RIGHT, buff=0.04)
    return group


# ======================================================================
# 主场景
# ======================================================================

class DecimalPointMoveLesson(Scene):
    """
    小数点移动引起小数大小的变化 教学动画
    场景:
      1. 开场钩子
      2. 小数点右移（扩大）
      3. 小数点左移（缩小）
      4. 规律总结
      5. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_move_right()
        self.scene_3_move_left()
        self.scene_4_summary()
        self.scene_5_outro()

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
            "一个小小的点", font=FONT, font_size=46, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "移动一下就能让数变大10倍？",
            font=FONT, font_size=32, color=COLOR_HL
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 展示 3.5 → 35
        disp_before = make_decimal_display("3.5", font_size=56).move_to(UP * 2.5)
        arrow_sym = MathTex(r"\Rightarrow", font_size=48, color=COLOR_RIGHT).next_to(
            disp_before, RIGHT, buff=0.3
        )
        disp_after = make_decimal_display("35", digit_color=COLOR_RIGHT, font_size=56).next_to(
            arrow_sym, RIGHT, buff=0.3
        )

        self.play(FadeIn(disp_before, scale=0.7), run_time=0.6)
        self.play(FadeIn(arrow_sym), run_time=0.4)
        self.play(FadeIn(disp_after, scale=0.7), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(VGroup(hook1, hook2, disp_before, arrow_sym, disp_after)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 2: 小数点右移 — 扩大
    # ------------------------------------------------------------------

    def scene_2_move_right(self):
        title = Text(
            "小数点向右移动", font=FONT, font_size=36,
            color=COLOR_RIGHT, weight=BOLD
        ).move_to(UP * 5.8)
        subtitle = Text(
            "数变大（扩大）", font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 5.1)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        self.play(FadeIn(subtitle, shift=DOWN * 0.2), run_time=0.4)

        # ── 起始数 3.5 ────────────────────────────────────────────────
        origin_label = Text(
            "原数：", font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 3.8 + LEFT * 2.0)
        origin_num = make_decimal_display("3.5", font_size=52).next_to(
            origin_label, RIGHT, buff=0.25
        )
        self.play(FadeIn(origin_label), FadeIn(origin_num), run_time=0.5)
        self.wait(0.3)

        # ── 右移1位 → 35，×10 ─────────────────────────────────────
        self._show_right_shift_step(
            from_str="3.5",
            to_str="35",
            factor_str="× 10",
            y_top=2.3,
            shift_desc="右移 1 位",
            result_desc="扩大到原数的 10 倍",
        )

        # ── 右移2位 → 350，×100 ───────────────────────────────────
        self._show_right_shift_step(
            from_str="3.5",
            to_str="350",
            factor_str="× 100",
            y_top=0.3,
            shift_desc="右移 2 位",
            result_desc="扩大到原数的 100 倍",
        )

        # ── 右移3位 → 3500，×1000 ─────────────────────────────────
        self._show_right_shift_step(
            from_str="3.5",
            to_str="3500",
            factor_str="× 1000",
            y_top=-1.7,
            shift_desc="右移 3 位",
            result_desc="扩大到原数的 1000 倍",
        )

        # 小结
        rule_box = self._make_rule_box(
            lines=[
                "小数点向右移动一位，",
                "小数扩大到原数的 10 倍",
                "移动两位 → 100 倍",
                "移动三位 → 1000 倍  …",
            ],
            color=COLOR_RIGHT,
            y_center=-4.8,
        )
        self.play(FadeIn(rule_box, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(
                title, subtitle, origin_label, origin_num,
                rule_box,
            )),
            run_time=0.5
        )

    def _show_right_shift_step(self, from_str, to_str, factor_str,
                                y_top, shift_desc, result_desc):
        """
        在 y_top 处绘制一行：原数 ──右移箭头──> 结果，并附说明。
        使用固定坐标避免 get_right() 在未添加到场景时报错。
        """
        row_y = y_top

        # 说明文字
        desc_txt = Text(
            shift_desc, font=FONT, font_size=22, color=COLOR_RIGHT
        ).move_to(UP * (row_y + 0.5) + LEFT * 1.5)
        self.play(FadeIn(desc_txt, shift=RIGHT * 0.3), run_time=0.3)

        # 原数显示（固定在左侧）
        from_disp = make_decimal_display(from_str, font_size=44).move_to(
            UP * row_y + LEFT * 3.2
        )
        self.play(FadeIn(from_disp), run_time=0.3)

        # 右箭头 — 使用绝对坐标，不依赖 get_right()
        arrow_start = np.array([-1.8, row_y, 0])
        arrow_end   = np.array([-0.5, row_y, 0])
        arrow = Arrow(
            start=arrow_start, end=arrow_end,
            color=COLOR_RIGHT, buff=0, stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        factor_lbl = Text(factor_str, font=FONT, font_size=18, color=COLOR_RIGHT).next_to(
            arrow, UP, buff=0.08
        )
        self.play(Create(arrow), FadeIn(factor_lbl), run_time=0.4)

        # 结果（固定在右侧）
        to_disp = make_decimal_display(to_str, digit_color=COLOR_RIGHT, font_size=44).move_to(
            UP * row_y + RIGHT * 1.5
        )
        self.play(FadeIn(to_disp, scale=0.8), run_time=0.4)

        # 倍数结论
        concl = Text(
            result_desc, font=FONT, font_size=18, color=COLOR_HL
        ).move_to(UP * (row_y - 0.5) + RIGHT * 0.5)
        self.play(FadeIn(concl, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        if not hasattr(self, "_right_mobs"):
            self._right_mobs = VGroup()
        self._right_mobs.add(desc_txt, from_disp, arrow, factor_lbl, to_disp, concl)

    def _make_rule_box(self, lines, color, y_center):
        """创建规律文本框"""
        texts = VGroup(*[
            Text(line, font=FONT, font_size=20, color=WHITE)
            for line in lines
        ]).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        bg = RoundedRectangle(
            width=texts.width + 0.8, height=texts.height + 0.5,
            corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=color, stroke_width=2.5
        )
        group = VGroup(bg, texts)
        group.move_to(UP * y_center)
        texts.move_to(bg.get_center())
        return group

    # ------------------------------------------------------------------
    # Scene 3: 小数点左移 — 缩小
    # ------------------------------------------------------------------

    def scene_3_move_left(self):
        # 清理上一场景积累的 mobs
        if hasattr(self, "_right_mobs"):
            self.play(FadeOut(self._right_mobs), run_time=0.4)
            del self._right_mobs

        title = Text(
            "小数点向左移动", font=FONT, font_size=36,
            color=COLOR_LEFT, weight=BOLD
        ).move_to(UP * 5.8)
        subtitle = Text(
            "数变小（缩小）", font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 5.1)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        self.play(FadeIn(subtitle, shift=DOWN * 0.2), run_time=0.4)

        origin_label = Text(
            "原数：", font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 3.8 + LEFT * 2.0)
        origin_num = make_decimal_display("350", digit_color=WHITE, font_size=52).next_to(
            origin_label, RIGHT, buff=0.25
        )
        self.play(FadeIn(origin_label), FadeIn(origin_num), run_time=0.5)
        self.wait(0.3)

        # 左移1位 → 35，÷10
        self._show_left_shift_step(
            from_str="350",
            to_str="35",
            factor_str="÷ 10",
            y_top=2.3,
            shift_desc="左移 1 位",
            result_desc="缩小到原数的 1/10",
        )

        # 左移2位 → 3.5，÷100
        self._show_left_shift_step(
            from_str="350",
            to_str="3.5",
            factor_str="÷ 100",
            y_top=0.3,
            shift_desc="左移 2 位",
            result_desc="缩小到原数的 1/100",
        )

        # 左移3位 → 0.35，÷1000
        self._show_left_shift_step(
            from_str="350",
            to_str="0.35",
            factor_str="÷ 1000",
            y_top=-1.7,
            shift_desc="左移 3 位",
            result_desc="缩小到原数的 1/1000",
        )

        # 小结
        rule_box = self._make_rule_box(
            lines=[
                "小数点向左移动一位，",
                "小数缩小到原数的 1/10",
                "移动两位 → 1/100",
                "移动三位 → 1/1000  …",
            ],
            color=COLOR_LEFT,
            y_center=-4.8,
        )
        self.play(FadeIn(rule_box, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(
                title, subtitle, origin_label, origin_num, rule_box,
            )),
            run_time=0.5
        )

        if hasattr(self, "_left_mobs"):
            self.play(FadeOut(self._left_mobs), run_time=0.4)
            del self._left_mobs

    def _show_left_shift_step(self, from_str, to_str, factor_str,
                               y_top, shift_desc, result_desc):
        """左移一行演示，使用固定坐标避免 get_right() 问题。"""
        row_y = y_top

        desc_txt = Text(
            shift_desc, font=FONT, font_size=22, color=COLOR_LEFT
        ).move_to(UP * (row_y + 0.5) + LEFT * 1.5)
        self.play(FadeIn(desc_txt, shift=LEFT * 0.3), run_time=0.3)

        # 原数（固定左侧）
        from_disp = make_decimal_display(from_str, digit_color=WHITE, font_size=44).move_to(
            UP * row_y + LEFT * 3.2
        )
        self.play(FadeIn(from_disp), run_time=0.3)

        # 箭头（固定坐标）
        arrow_start = np.array([-1.8, row_y, 0])
        arrow_end   = np.array([-0.5, row_y, 0])
        arrow = Arrow(
            start=arrow_start, end=arrow_end,
            color=COLOR_LEFT, buff=0, stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        factor_lbl = Text(factor_str, font=FONT, font_size=18, color=COLOR_LEFT).next_to(
            arrow, UP, buff=0.08
        )
        self.play(Create(arrow), FadeIn(factor_lbl), run_time=0.4)

        # 结果（固定右侧）
        to_disp = make_decimal_display(to_str, dot_color=COLOR_DOT,
                                       digit_color=COLOR_LEFT, font_size=44).move_to(
            UP * row_y + RIGHT * 1.5
        )
        self.play(FadeIn(to_disp, scale=0.8), run_time=0.4)

        concl = Text(
            result_desc, font=FONT, font_size=18, color=COLOR_HL
        ).move_to(UP * (row_y - 0.5) + RIGHT * 0.5)
        self.play(FadeIn(concl, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        if not hasattr(self, "_left_mobs"):
            self._left_mobs = VGroup()
        self._left_mobs.add(desc_txt, from_disp, arrow, factor_lbl, to_disp, concl)

    # ------------------------------------------------------------------
    # Scene 4: 规律总结
    # ------------------------------------------------------------------

    def scene_4_summary(self):
        sum_title = Text(
            "规律总结", font=FONT, font_size=40,
            color=COLOR_RULE, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(FadeIn(sum_title, shift=DOWN * 0.3), run_time=0.5)

        # ── 核心规律表 ──────────────────────────────────────────────
        tbl_data = [
            ("右移 1 位", "扩大 10 倍",    COLOR_RIGHT),
            ("右移 2 位", "扩大 100 倍",   COLOR_RIGHT),
            ("右移 3 位", "扩大 1000 倍",  COLOR_RIGHT),
            ("左移 1 位", "缩小到 1/10",   COLOR_LEFT),
            ("左移 2 位", "缩小到 1/100",  COLOR_LEFT),
            ("左移 3 位", "缩小到 1/1000", COLOR_LEFT),
        ]

        rows = VGroup()
        for move_desc, effect_desc, col in tbl_data:
            arrow_sym = Text("→", font=FONT, font_size=22, color=col)
            move_t = Text(move_desc, font=FONT, font_size=22, color=col)
            eff_t   = Text(effect_desc, font=FONT, font_size=22, color=WHITE)
            row = VGroup(move_t, arrow_sym, eff_t).arrange(RIGHT, buff=0.25)
            rows.add(row)

        rows.arrange(DOWN, buff=0.30, aligned_edge=LEFT).move_to(UP * 3.0)
        for i, row in enumerate(rows):
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.3)
            self.wait(0.15)

        self.wait(0.5)

        # ── 核心口诀 ────────────────────────────────────────────────
        rhyme_bg = RoundedRectangle(
            width=7.8, height=3.2,
            corner_radius=0.25,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_RULE, stroke_width=2.5
        ).move_to(DOWN * 3.3)

        rhyme_lines = VGroup(
            Text("小数点右移，数就变大；", font=FONT, font_size=24, color=COLOR_RIGHT),
            Text("小数点左移，数就变小。", font=FONT, font_size=24, color=COLOR_LEFT),
            Text("移几位，变 10 的几次方倍！", font=FONT, font_size=22, color=COLOR_HL),
        ).arrange(DOWN, buff=0.35).move_to(rhyme_bg.get_center())

        self.play(FadeIn(rhyme_bg), run_time=0.3)
        for line in rhyme_lines:
            self.play(Write(line), run_time=0.6)
            self.wait(0.2)

        self.wait(2.0)

        # ── 应用示例 ────────────────────────────────────────────────
        ex_title = Text(
            "小试牛刀：", font=FONT, font_size=28, color=COLOR_RULE
        ).move_to(DOWN * 5.2)
        self.play(FadeIn(ex_title, shift=UP * 0.2), run_time=0.4)

        ex_row = VGroup(
            make_decimal_display("3.5", font_size=40),
            Text("右移 2 位", font=FONT, font_size=22, color=COLOR_RIGHT),
            MathTex(r"\Rightarrow", font_size=36, color=COLOR_RIGHT),
            make_decimal_display("350", digit_color=COLOR_RIGHT, font_size=40),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 6.2)
        self.play(FadeIn(ex_row, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(sum_title, rows, rhyme_bg, rhyme_lines, ex_title, ex_row)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 片尾
    # ------------------------------------------------------------------

    def scene_5_outro(self):
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

        # 小装饰：闪烁的小数点
        dot_dec = Dot(ORIGIN + DOWN * 2.0, radius=0.14, color=COLOR_DOT)
        self.play(FadeIn(dot_dec, scale=0.5), run_time=0.3)
        self.play(dot_dec.animate.scale(2.5).set_opacity(0.5), run_time=0.4)
        self.play(dot_dec.animate.scale(0.4).set_opacity(1.0), run_time=0.3)
        self.wait(1.2)

        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, dot_dec)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 005_小数点移动引起小数大小的变化.py DecimalPointMoveLesson
#   中等质量:  manim -qm  005_小数点移动引起小数大小的变化.py DecimalPointMoveLesson
#   高质量:    manim -qh  005_小数点移动引起小数大小的变化.py DecimalPointMoveLesson
# ======================================================================
