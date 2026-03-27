"""
002_数轴的初步认识.py — 数轴的初步认识 教学动画

知识点: 数轴三要素(原点、正方向、单位长度)，在数轴上表示正数、0和负数，
        理解数轴上右边的数总大于左边的数，比较正数、0、负数的大小
年级: 五年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景顺序:
  1. 开场钩子
  2. 数轴的引入 — 温度计类比
  3. 数轴三要素介绍
  4. 在数轴上标记正数
  5. 在数轴上标记负数和0
  6. 大小比较规律
  7. 例题: 5 > 3 > 0 > -2 > -5
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
COLOR_POS = "#3b82f6"        # 蓝色 — 正数
COLOR_NEG = "#ef4444"        # 红色 — 负数
COLOR_ZERO = "#22c55e"       # 绿色 — 零/原点
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_AXIS = "#e2e8f0"       # 数轴颜色
COLOR_ACCENT = "#a78bfa"     # 紫色强调
COLOR_AUTHOR = "#6b7280"     # 灰色作者信息
COLOR_TICK = "#94a3b8"       # 刻度颜色
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class NumberLineLesson(Scene):
    """
    数轴的初步认识教学动画
    场景顺序:
      1. 开场钩子
      2. 温度计引入数轴概念
      3. 数轴三要素
      4. 在数轴上标记正数
      5. 在数轴上标记负数和零
      6. 大小比较规律
      7. 综合例题
      8. 总结
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_thermometer_intro()
        self.scene_3_three_elements()
        self.scene_4_positive_numbers()
        self.scene_5_negative_and_zero()
        self.scene_6_comparison_rule()
        self.scene_7_example()
        self.scene_8_summary()
        self.scene_9_outro()

    # ------------------------------------------------------------------
    # 辅助函数: 创建数轴
    # ------------------------------------------------------------------

    def _make_number_line(self, x_range=(-5, 5, 1), length=7.0,
                          center=None, include_numbers=False):
        """
        构建一条水平数轴，带箭头和刻度，返回 (line_group, coord_fn)
        coord_fn(x) -> 屏幕坐标 np.array([x_screen, y_screen, 0])
        """
        if center is None:
            center = np.array([0.0, 0.0, 0.0])

        x_min, x_max, step = x_range
        unit_length = length / (x_max - x_min)

        left_x = center[0] - length / 2
        right_x = center[0] + length / 2
        cy = center[1]

        def coord_fn(x):
            screen_x = left_x + (x - x_min) * unit_length
            return np.array([screen_x, cy, 0])

        # 主轴线 (带右箭头)
        axis_line = Arrow(
            start=np.array([left_x - 0.15, cy, 0]),
            end=np.array([right_x + 0.15, cy, 0]),
            color=COLOR_AXIS,
            stroke_width=3,
            buff=0,
            tip_length=0.25,
        )

        group = VGroup(axis_line)

        # 刻度线和数字
        x_val = x_min
        while x_val <= x_max + 1e-9:
            x_rounded = round(x_val, 6)
            pos = coord_fn(x_rounded)
            tick = Line(
                start=pos + UP * 0.15,
                end=pos + DOWN * 0.15,
                color=COLOR_TICK,
                stroke_width=2,
            )
            group.add(tick)

            if include_numbers:
                if x_rounded == 0:
                    lbl = MathTex(r"0", font_size=28, color=COLOR_ZERO)
                elif x_rounded > 0:
                    lbl = MathTex(str(int(x_rounded)), font_size=28, color=COLOR_POS)
                else:
                    lbl = MathTex(str(int(x_rounded)), font_size=28, color=COLOR_NEG)
                lbl.next_to(pos + DOWN * 0.15, DOWN, buff=0.12)
                group.add(lbl)

            x_val += step

        return group, coord_fn

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: 数轴 — 一把神奇的数学尺!"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 标题
        hook1 = Text(
            "数轴的初步认识",
            font=FONT, font_size=46, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)

        hook2 = Text(
            "一把神奇的数学直尺！",
            font=FONT, font_size=32, color=COLOR_HL
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.7)
        self.play(Write(hook2), run_time=0.6)

        # 快速预览: 展示一个简单数轴
        preview_group, preview_coord = self._make_number_line(
            x_range=(-3, 3, 1),
            length=6.0,
            center=np.array([0.0, 1.5, 0]),
            include_numbers=True,
        )
        self.play(Create(preview_group), run_time=1.0)

        # 标示负数、零、正数
        neg_dot = Dot(preview_coord(-2), color=COLOR_NEG, radius=0.12)
        zero_dot = Dot(preview_coord(0), color=COLOR_ZERO, radius=0.12)
        pos_dot = Dot(preview_coord(2), color=COLOR_POS, radius=0.12)

        neg_lbl = Text("负数", font=FONT, font_size=24, color=COLOR_NEG).next_to(neg_dot, UP, buff=0.3)
        zero_lbl = Text("0", font=FONT, font_size=24, color=COLOR_ZERO).next_to(zero_dot, UP, buff=0.3)
        pos_lbl = Text("正数", font=FONT, font_size=24, color=COLOR_POS).next_to(pos_dot, UP, buff=0.3)

        self.play(
            FadeIn(neg_dot), FadeIn(zero_dot), FadeIn(pos_dot),
            run_time=0.5
        )
        self.play(
            FadeIn(neg_lbl, shift=UP * 0.2),
            FadeIn(zero_lbl, shift=UP * 0.2),
            FadeIn(pos_lbl, shift=UP * 0.2),
            run_time=0.6
        )
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(VGroup(hook1, hook2, preview_group,
                           neg_dot, zero_dot, pos_dot,
                           neg_lbl, zero_lbl, pos_lbl)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: 温度计引入
    # ------------------------------------------------------------------

    def scene_2_thermometer_intro(self):
        """用温度计类比引入数轴概念"""

        title = Text(
            "生活中的数轴", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 绘制温度计外形
        tube_height = 5.0
        tube_width = 0.5
        bulb_radius = 0.4

        tube = Rectangle(
            width=tube_width, height=tube_height,
            fill_color="#1e293b", fill_opacity=1,
            stroke_color=COLOR_TICK, stroke_width=2,
        ).move_to(LEFT * 2.5 + UP * 0.5)

        bulb_center = np.array([-2.5, 0.5 - tube_height / 2 - bulb_radius * 0.4, 0])
        bulb = Circle(
            radius=bulb_radius,
            fill_color=COLOR_NEG, fill_opacity=0.9,
            stroke_color=COLOR_TICK, stroke_width=2,
        ).move_to(bulb_center)

        # 温度计内液柱
        liquid_height = 2.5
        liquid_bottom_y = 0.5 - tube_height / 2
        liquid_center_y = liquid_bottom_y + liquid_height / 2
        liquid = Rectangle(
            width=tube_width * 0.55, height=liquid_height,
            fill_color=COLOR_NEG, fill_opacity=0.9,
            stroke_width=0,
        ).move_to(np.array([-2.5, liquid_center_y, 0]))

        self.play(Create(tube), Create(bulb), run_time=0.6)
        self.play(FadeIn(liquid), run_time=0.4)

        # 刻度标注
        thermo_cx = -2.5
        thermo_bottom_y = 0.5 - tube_height / 2
        thermo_top_y = 0.5 + tube_height / 2
        temps = [-20, -10, 0, 10, 20]
        thermo_unit = (thermo_top_y - thermo_bottom_y) / (temps[-1] - temps[0])

        temp_ticks = VGroup()
        for t in temps:
            ty = thermo_bottom_y + (t - temps[0]) * thermo_unit
            tick = Line(
                start=np.array([thermo_cx + tube_width / 2, ty, 0]),
                end=np.array([thermo_cx + tube_width / 2 + 0.3, ty, 0]),
                color=COLOR_TICK, stroke_width=2
            )
            if t == 0:
                c = COLOR_ZERO
            elif t > 0:
                c = COLOR_POS
            else:
                c = COLOR_NEG

            lbl_str = f"+{t}" if t > 0 else str(t)
            lbl = Text(lbl_str, font=FONT, font_size=22, color=c).next_to(
                np.array([thermo_cx + tube_width / 2 + 0.3, ty, 0]),
                RIGHT, buff=0.15
            )
            temp_ticks.add(tick, lbl)

        self.play(Create(temp_ticks), run_time=0.8)

        # 说明文字
        explain1 = Text(
            "温度计就像竖着的数轴",
            font=FONT, font_size=26, color=WHITE
        ).move_to(RIGHT * 1.2 + UP * 3.5)

        explain2 = Text(
            "0°C 是分界点",
            font=FONT, font_size=25, color=COLOR_ZERO
        ).move_to(RIGHT * 1.2 + UP * 2.6)

        explain3 = Text(
            "零上是正数",
            font=FONT, font_size=25, color=COLOR_POS
        ).move_to(RIGHT * 1.2 + UP * 1.9)

        explain4 = Text(
            "零下是负数",
            font=FONT, font_size=25, color=COLOR_NEG
        ).move_to(RIGHT * 1.2 + UP * 1.2)

        self.play(Write(explain1), run_time=0.6)
        self.play(FadeIn(explain2), run_time=0.4)
        self.play(FadeIn(explain3), run_time=0.4)
        self.play(FadeIn(explain4), run_time=0.4)
        self.wait(0.8)

        # 连接到数轴概念
        bridge = Text(
            "把它横过来，就是数轴！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(bridge, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(VGroup(title, tube, bulb, liquid, temp_ticks,
                           explain1, explain2, explain3, explain4, bridge)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 数轴三要素
    # ------------------------------------------------------------------

    def scene_3_three_elements(self):
        """介绍数轴的三要素: 原点、正方向、单位长度"""

        title = Text(
            "数轴的三要素", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 绘制基础数轴 (不带数字)
        axis_group, coord_fn = self._make_number_line(
            x_range=(-4, 4, 1),
            length=7.0,
            center=np.array([0.0, 1.5, 0]),
            include_numbers=False,
        )
        self.play(Create(axis_group), run_time=0.8)

        # === 要素1: 原点 ===
        elem1_title = Text(
            "① 原点 (O)",
            font=FONT, font_size=32, color=COLOR_ZERO, weight=BOLD
        ).move_to(UP * 4.3)
        self.play(FadeIn(elem1_title, shift=LEFT * 0.2), run_time=0.5)

        origin_pos = coord_fn(0)
        origin_dot = Dot(origin_pos, color=COLOR_ZERO, radius=0.14)
        origin_label = Text("O", font=FONT, font_size=28, color=COLOR_ZERO).next_to(origin_dot, DOWN, buff=0.25)
        origin_desc = Text(
            "数轴上的零点，正负数的分界",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 3.5)

        self.play(
            GrowFromCenter(origin_dot),
            Write(origin_label),
            run_time=0.6
        )
        self.play(FadeIn(origin_desc), run_time=0.4)
        self.play(Indicate(origin_dot, color=COLOR_ZERO, scale_factor=1.5), run_time=0.5)
        self.wait(0.4)

        # === 要素2: 正方向 ===
        elem2_title = Text(
            "② 正方向",
            font=FONT, font_size=32, color=COLOR_POS, weight=BOLD
        ).move_to(UP * 4.3)
        self.play(ReplacementTransform(elem1_title, elem2_title), run_time=0.4)

        dir_arrow = Arrow(
            start=coord_fn(0.4),
            end=coord_fn(3.2),
            color=COLOR_POS,
            stroke_width=4,
            buff=0,
            tip_length=0.25,
        )
        dir_label = Text("正方向", font=FONT, font_size=24, color=COLOR_POS).next_to(
            coord_fn(2.0), UP, buff=0.3
        )
        dir_desc = Text(
            "箭头所指方向为正方向（向右）",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 3.5)

        self.play(FadeOut(origin_desc), run_time=0.2)
        self.play(
            GrowArrow(dir_arrow),
            FadeIn(dir_label, shift=DOWN * 0.1),
            run_time=0.6
        )
        self.play(FadeIn(dir_desc), run_time=0.4)
        self.wait(0.4)

        # === 要素3: 单位长度 ===
        elem3_title = Text(
            "③ 单位长度",
            font=FONT, font_size=32, color=COLOR_ACCENT, weight=BOLD
        ).move_to(UP * 4.3)
        self.play(ReplacementTransform(elem2_title, elem3_title), run_time=0.4)

        # 标出从0到1的单位长度
        unit_start = coord_fn(0)
        unit_end = coord_fn(1)
        brace_unit = BraceBetweenPoints(unit_start, unit_end, direction=UP)
        brace_label = Text("单位长度", font=FONT, font_size=24, color=COLOR_ACCENT).next_to(brace_unit, UP, buff=0.15)
        unit_desc = Text(
            "相邻整数间距离相等",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 3.5)

        self.play(FadeOut(dir_desc), run_time=0.2)
        self.play(Create(brace_unit), FadeIn(brace_label), run_time=0.6)
        self.play(FadeIn(unit_desc), run_time=0.4)
        self.wait(0.6)

        # 小结: 三要素合并显示
        self.play(
            FadeOut(VGroup(elem3_title, dir_arrow, dir_label,
                           brace_unit, brace_label, unit_desc)),
            run_time=0.4
        )

        summary_box_bg = RoundedRectangle(
            width=7.5, height=3.0,
            corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_HL, stroke_width=2,
        ).move_to(UP * 3.5)

        s1 = Text("① 原点 — 零点，正负分界", font=FONT, font_size=26, color=COLOR_ZERO)
        s2 = Text("② 正方向 — 箭头方向（向右）", font=FONT, font_size=26, color=COLOR_POS)
        s3 = Text("③ 单位长度 — 间距相等", font=FONT, font_size=26, color=COLOR_ACCENT)
        summary_lines = VGroup(s1, s2, s3).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(UP * 3.5)

        self.play(FadeIn(summary_box_bg), run_time=0.3)
        self.play(Write(s1), run_time=0.4)
        self.play(Write(s2), run_time=0.4)
        self.play(Write(s3), run_time=0.4)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(VGroup(title, axis_group, origin_dot, origin_label,
                           summary_box_bg, s1, s2, s3)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 在数轴上标记正数
    # ------------------------------------------------------------------

    def scene_4_positive_numbers(self):
        """逐步在数轴上标记正整数"""

        title = Text(
            "在数轴上表示正数",
            font=FONT, font_size=38, color=COLOR_POS, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)

        # 数轴 (带数字)
        axis_group, coord_fn = self._make_number_line(
            x_range=(-5, 5, 1),
            length=7.5,
            center=np.array([0.0, 2.0, 0]),
            include_numbers=True,
        )
        # 原点标记
        origin_dot = Dot(coord_fn(0), color=COLOR_ZERO, radius=0.1)
        origin_lbl = Text("O", font=FONT, font_size=24, color=COLOR_ZERO).next_to(
            coord_fn(0) + DOWN * 0.15, DOWN, buff=0.35
        )

        self.play(Create(axis_group), FadeIn(origin_dot), FadeIn(origin_lbl), run_time=0.8)

        # 说明文字
        explain_pos = Text(
            "原点右边是正数",
            font=FONT, font_size=30, color=COLOR_POS
        ).move_to(UP * 0.3)
        self.play(FadeIn(explain_pos, shift=UP * 0.2), run_time=0.5)

        # 逐一标出正数 1, 2, 3, 4, 5
        pos_dots = VGroup()
        pos_labels = VGroup()

        for x in [1, 2, 3, 4, 5]:
            dot = Dot(coord_fn(x), color=COLOR_POS, radius=0.14)
            lbl = Text(f"+{x}", font=FONT, font_size=24, color=COLOR_POS).next_to(
                coord_fn(x), UP, buff=0.3
            )
            pos_dots.add(dot)
            pos_labels.add(lbl)
            self.play(
                GrowFromCenter(dot),
                FadeIn(lbl, shift=DOWN * 0.1),
                run_time=0.35
            )

        self.wait(0.5)

        # 强调: 正数在原点右边
        right_arrow = Arrow(
            start=coord_fn(0) + UP * 0.65,
            end=coord_fn(3) + UP * 0.65,
            color=COLOR_POS, stroke_width=3,
            buff=0, tip_length=0.2,
        )
        right_txt = Text("正数在右边", font=FONT, font_size=26, color=COLOR_POS).next_to(
            right_arrow, UP, buff=0.1
        )
        self.play(GrowArrow(right_arrow), FadeIn(right_txt), run_time=0.6)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(VGroup(title, axis_group, origin_dot, origin_lbl,
                           pos_dots, pos_labels, explain_pos,
                           right_arrow, right_txt)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 在数轴上标记负数和0
    # ------------------------------------------------------------------

    def scene_5_negative_and_zero(self):
        """在数轴上标记负数和0，强调对称性"""

        title = Text(
            "在数轴上表示负数",
            font=FONT, font_size=38, color=COLOR_NEG, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)

        # 数轴
        axis_group, coord_fn = self._make_number_line(
            x_range=(-5, 5, 1),
            length=7.5,
            center=np.array([0.0, 2.0, 0]),
            include_numbers=True,
        )
        origin_dot = Dot(coord_fn(0), color=COLOR_ZERO, radius=0.1)
        origin_lbl = Text("O", font=FONT, font_size=24, color=COLOR_ZERO).next_to(
            coord_fn(0) + DOWN * 0.15, DOWN, buff=0.35
        )
        self.play(Create(axis_group), FadeIn(origin_dot), FadeIn(origin_lbl), run_time=0.8)

        # 先放正数参考点
        pos_dots = VGroup()
        for x in [1, 2, 3, 4, 5]:
            dot = Dot(coord_fn(x), color=COLOR_POS, radius=0.1)
            pos_dots.add(dot)
        self.play(FadeIn(pos_dots), run_time=0.4)

        # 说明
        explain_neg = Text(
            "原点左边是负数",
            font=FONT, font_size=30, color=COLOR_NEG
        ).move_to(UP * 0.3)
        self.play(FadeIn(explain_neg, shift=UP * 0.2), run_time=0.5)

        # 逐一标出负数
        neg_dots = VGroup()
        neg_labels = VGroup()

        for x in [-1, -2, -3, -4, -5]:
            dot = Dot(coord_fn(x), color=COLOR_NEG, radius=0.14)
            lbl = MathTex(str(x), font_size=30, color=COLOR_NEG).next_to(
                coord_fn(x), UP, buff=0.3
            )
            neg_dots.add(dot)
            neg_labels.add(lbl)
            self.play(
                GrowFromCenter(dot),
                FadeIn(lbl, shift=DOWN * 0.1),
                run_time=0.35
            )

        self.wait(0.5)

        # 强调对称性: -3 和 +3 距原点相等
        sym_line_pos = DashedLine(
            start=coord_fn(0) + UP * 0.5,
            end=coord_fn(3) + UP * 0.5,
            color=COLOR_HL, stroke_width=2.5, dash_length=0.12
        )
        sym_line_neg = DashedLine(
            start=coord_fn(0) + UP * 0.5,
            end=coord_fn(-3) + UP * 0.5,
            color=COLOR_HL, stroke_width=2.5, dash_length=0.12
        )

        sym_txt = Text(
            "-3 与 +3 距原点相等",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 0.5)

        self.play(Create(sym_line_pos), Create(sym_line_neg), run_time=0.5)
        self.play(FadeIn(sym_txt, shift=UP * 0.2), run_time=0.5)
        self.play(
            Indicate(neg_dots[2], color=COLOR_HL, scale_factor=1.5),
            Indicate(pos_dots[2], color=COLOR_HL, scale_factor=1.5),
            run_time=0.6
        )
        self.wait(0.6)

        # 零的特殊性
        zero_note = Text(
            "0 既不是正数，也不是负数",
            font=FONT, font_size=28, color=COLOR_ZERO
        ).move_to(DOWN * 1.5)
        self.play(
            FadeIn(zero_note, shift=UP * 0.2),
            Indicate(origin_dot, color=COLOR_ZERO, scale_factor=1.8),
            run_time=0.7
        )
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(VGroup(title, axis_group, origin_dot, origin_lbl,
                           pos_dots, neg_dots, neg_labels,
                           explain_neg, sym_line_pos, sym_line_neg,
                           sym_txt, zero_note)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 大小比较规律
    # ------------------------------------------------------------------

    def scene_6_comparison_rule(self):
        """数轴上右边的数总是大于左边的数"""

        title = Text(
            "数轴上的大小规律",
            font=FONT, font_size=38, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 数轴
        axis_group, coord_fn = self._make_number_line(
            x_range=(-5, 5, 1),
            length=7.5,
            center=np.array([0.0, 2.5, 0]),
            include_numbers=True,
        )
        origin_dot = Dot(coord_fn(0), color=COLOR_ZERO, radius=0.1)
        self.play(Create(axis_group), FadeIn(origin_dot), run_time=0.7)

        # 核心规律框
        rule_bg = RoundedRectangle(
            width=7.5, height=1.5,
            corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=2.5,
        ).move_to(UP * 1.0)

        rule_text_1 = Text("右边的数", font=FONT, font_size=30, color=COLOR_POS)
        rule_text_op = Text(" 总大于 ", font=FONT, font_size=30, color=WHITE)
        rule_text_2 = Text("左边的数", font=FONT, font_size=30, color=COLOR_NEG)
        rule_line = VGroup(rule_text_1, rule_text_op, rule_text_2).arrange(RIGHT).move_to(UP * 1.0)

        self.play(FadeIn(rule_bg), run_time=0.3)
        self.play(Write(rule_line), run_time=0.7)
        self.wait(0.4)

        # 例子1: 3 > -2
        ex1_a = coord_fn(3)
        ex1_b = coord_fn(-2)
        dot_a = Dot(ex1_a, color=COLOR_POS, radius=0.15)
        dot_b = Dot(ex1_b, color=COLOR_NEG, radius=0.15)
        lbl_a = MathTex(r"3", font_size=36, color=COLOR_POS).next_to(dot_a, UP, buff=0.3)
        lbl_b = MathTex(r"-2", font_size=36, color=COLOR_NEG).next_to(dot_b, UP, buff=0.3)

        self.play(GrowFromCenter(dot_a), GrowFromCenter(dot_b), run_time=0.5)
        self.play(FadeIn(lbl_a), FadeIn(lbl_b), run_time=0.4)

        compare_arrow = Arrow(
            start=ex1_b + UP * 0.85,
            end=ex1_a + UP * 0.85,
            color=COLOR_HL, stroke_width=3,
            buff=0, tip_length=0.2,
        )
        self.play(GrowArrow(compare_arrow), run_time=0.5)

        ex1_result = VGroup(
            MathTex(r"3", font_size=40, color=COLOR_POS),
            MathTex(r">", font_size=40, color=WHITE),
            MathTex(r"-2", font_size=40, color=COLOR_NEG),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 0.3)

        self.play(FadeIn(ex1_result, scale=0.7), run_time=0.5)
        self.wait(0.5)

        # 例子2: 0 > -3
        self.play(
            FadeOut(VGroup(dot_a, dot_b, lbl_a, lbl_b, compare_arrow, ex1_result)),
            run_time=0.3
        )

        ex2_a = coord_fn(0)
        ex2_b = coord_fn(-3)
        dot_c = Dot(ex2_a, color=COLOR_ZERO, radius=0.15)
        dot_d = Dot(ex2_b, color=COLOR_NEG, radius=0.15)
        lbl_c = MathTex(r"0", font_size=36, color=COLOR_ZERO).next_to(dot_c, UP, buff=0.3)
        lbl_d = MathTex(r"-3", font_size=36, color=COLOR_NEG).next_to(dot_d, UP, buff=0.3)

        self.play(GrowFromCenter(dot_c), GrowFromCenter(dot_d), run_time=0.4)
        self.play(FadeIn(lbl_c), FadeIn(lbl_d), run_time=0.4)

        compare_arrow2 = Arrow(
            start=ex2_b + UP * 0.85,
            end=ex2_a + UP * 0.85,
            color=COLOR_HL, stroke_width=3,
            buff=0, tip_length=0.2,
        )
        self.play(GrowArrow(compare_arrow2), run_time=0.5)

        ex2_result = VGroup(
            MathTex(r"0", font_size=40, color=COLOR_ZERO),
            MathTex(r">", font_size=40, color=WHITE),
            MathTex(r"-3", font_size=40, color=COLOR_NEG),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 0.3)

        self.play(FadeIn(ex2_result, scale=0.7), run_time=0.5)
        self.wait(0.5)

        # 总结规律公式
        self.play(
            FadeOut(VGroup(dot_c, dot_d, lbl_c, lbl_d, compare_arrow2, ex2_result)),
            run_time=0.3
        )

        formula_bg = RoundedRectangle(
            width=7.2, height=1.2,
            corner_radius=0.2,
            fill_color="#1e1b4b", fill_opacity=0.95,
            stroke_color=COLOR_ACCENT, stroke_width=2,
        ).move_to(DOWN * 1.0)

        formula = VGroup(
            Text("正数", font=FONT, font_size=32, color=COLOR_POS),
            MathTex(r">", font_size=36, color=WHITE),
            MathTex(r"0", font_size=36, color=COLOR_ZERO),
            MathTex(r">", font_size=36, color=WHITE),
            Text("负数", font=FONT, font_size=32, color=COLOR_NEG),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.0)

        self.play(FadeIn(formula_bg), run_time=0.3)
        self.play(Write(formula), run_time=0.8)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(VGroup(title, axis_group, origin_dot,
                           rule_bg, rule_line, formula_bg, formula)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 7: 综合例题 5 > 3 > 0 > -2 > -5
    # ------------------------------------------------------------------

    def scene_7_example(self):
        """例题: 在数轴上比较 5, 3, 0, -2, -5 的大小"""

        title = Text(
            "例题：比较大小",
            font=FONT, font_size=38, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)

        # 问题
        question = Text(
            "比较 5, 3, 0, -2, -5 的大小",
            font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 4.6)
        self.play(Write(question), run_time=0.6)

        # 数轴 (范围稍大)
        axis_group, coord_fn = self._make_number_line(
            x_range=(-6, 6, 1),
            length=7.5,
            center=np.array([0.0, 2.0, 0]),
            include_numbers=False,
        )
        self.play(Create(axis_group), run_time=0.7)

        # 原点
        origin_dot = Dot(coord_fn(0), color=COLOR_ZERO, radius=0.1)
        origin_lbl = MathTex(r"0", font_size=28, color=COLOR_ZERO).next_to(
            coord_fn(0) + DOWN * 0.15, DOWN, buff=0.15
        )
        self.play(FadeIn(origin_dot), FadeIn(origin_lbl), run_time=0.3)

        # 逐一放置五个点
        points_data = [
            (5,   COLOR_POS,  r"+5"),
            (3,   COLOR_POS,  r"+3"),
            (0,   COLOR_ZERO, r"0"),
            (-2,  COLOR_NEG,  r"-2"),
            (-5,  COLOR_NEG,  r"-5"),
        ]

        point_dots = VGroup()
        point_lbls = VGroup()

        for x, col, label_str in points_data:
            pos = coord_fn(x)
            dot = Dot(pos, color=col, radius=0.16)
            lbl = MathTex(label_str, font_size=30, color=col).next_to(pos, UP, buff=0.3)
            point_dots.add(dot)
            point_lbls.add(lbl)
            self.play(
                GrowFromCenter(dot),
                FadeIn(lbl, shift=DOWN * 0.15),
                run_time=0.4
            )

        self.wait(0.4)

        # 从右到左标序号 — 越右越大
        order_labels = VGroup()
        order_positions = [5, 3, 0, -2, -5]
        order_nums = ["①最大", "②", "③", "④", "⑤最小"]
        order_colors = [COLOR_POS, COLOR_POS, COLOR_ZERO, COLOR_NEG, COLOR_NEG]

        for x, num, col in zip(order_positions, order_nums, order_colors):
            pos = coord_fn(x)
            lbl = Text(num, font=FONT, font_size=20, color=col).next_to(
                pos + DOWN * 0.15, DOWN, buff=0.5
            )
            order_labels.add(lbl)
            self.play(FadeIn(lbl, shift=UP * 0.1), run_time=0.3)

        self.wait(0.4)

        # 显示最终大小排列
        result_bg = RoundedRectangle(
            width=8.0, height=1.4,
            corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=2,
        ).move_to(DOWN * 1.0)

        result_eq = VGroup(
            MathTex(r"5", font_size=36, color=COLOR_POS),
            MathTex(r">", font_size=32, color=WHITE),
            MathTex(r"3", font_size=36, color=COLOR_POS),
            MathTex(r">", font_size=32, color=WHITE),
            MathTex(r"0", font_size=36, color=COLOR_ZERO),
            MathTex(r">", font_size=32, color=WHITE),
            MathTex(r"-2", font_size=36, color=COLOR_NEG),
            MathTex(r">", font_size=32, color=WHITE),
            MathTex(r"-5", font_size=36, color=COLOR_NEG),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.0)

        self.play(FadeIn(result_bg), run_time=0.3)
        self.play(Write(result_eq), run_time=1.0)
        self.wait(0.8)

        # 规律总结
        rule_remind = Text(
            "在数轴上，越靠右，数越大！",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 2.3)
        self.play(FadeIn(rule_remind, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(VGroup(title, question, axis_group, origin_dot, origin_lbl,
                           point_dots, point_lbls, order_labels,
                           result_bg, result_eq, rule_remind)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 8: 总结
    # ------------------------------------------------------------------

    def scene_8_summary(self):
        """总结数轴知识点"""

        title = Text(
            "本节总结", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 小数轴示意
        axis_group, coord_fn = self._make_number_line(
            x_range=(-4, 4, 1),
            length=7.0,
            center=np.array([0.0, 3.8, 0]),
            include_numbers=True,
        )
        origin_dot = Dot(coord_fn(0), color=COLOR_ZERO, radius=0.12)
        o_lbl = Text("O", font=FONT, font_size=22, color=COLOR_ZERO).next_to(
            coord_fn(0) + DOWN * 0.15, DOWN, buff=0.35
        )

        neg_arrow = Arrow(
            start=coord_fn(0) + DOWN * 0.05,
            end=coord_fn(-3.5) + DOWN * 0.05,
            color=COLOR_NEG, stroke_width=4,
            buff=0, tip_length=0.2,
        )
        pos_arrow = Arrow(
            start=coord_fn(0) + DOWN * 0.05,
            end=coord_fn(3.5) + DOWN * 0.05,
            color=COLOR_POS, stroke_width=4,
            buff=0, tip_length=0.2,
        )
        neg_region = Text("负数区", font=FONT, font_size=22, color=COLOR_NEG).move_to(
            coord_fn(-2.0) + DOWN * 0.55
        )
        pos_region = Text("正数区", font=FONT, font_size=22, color=COLOR_POS).move_to(
            coord_fn(2.0) + DOWN * 0.55
        )

        self.play(Create(axis_group), FadeIn(origin_dot), FadeIn(o_lbl), run_time=0.7)
        self.play(GrowArrow(neg_arrow), GrowArrow(pos_arrow), run_time=0.5)
        self.play(FadeIn(neg_region), FadeIn(pos_region), run_time=0.4)

        # 知识卡片
        cards_data = [
            ("数轴三要素", "原点 · 正方向 · 单位长度", COLOR_ACCENT),
            ("大小规律",   "右边的数 > 左边的数",      COLOR_HL),
            ("位置关系",   "正数在右 | 0居中 | 负数在左", COLOR_ZERO),
            ("核心结论",   "正数 > 0 > 负数",          WHITE),
        ]

        card_group = VGroup()
        y_positions = [UP * 1.5, UP * 0.2, DOWN * 1.1, DOWN * 2.4]

        for i, (card_title, card_content, col) in enumerate(cards_data):
            bg = RoundedRectangle(
                width=7.5, height=1.1,
                corner_radius=0.15,
                fill_color="#0f172a", fill_opacity=0.9,
                stroke_color=col, stroke_width=1.8,
            ).move_to(y_positions[i])

            ct = Text(card_title, font=FONT, font_size=25, color=col, weight=BOLD).move_to(
                y_positions[i] + LEFT * 2.0
            )
            cc = Text(card_content, font=FONT, font_size=23, color=GRAY_A).move_to(
                y_positions[i] + RIGHT * 0.8
            )
            card_group.add(bg, ct, cc)

        for i in range(len(cards_data)):
            self.play(
                FadeIn(card_group[i * 3]),
                FadeIn(card_group[i * 3 + 1], shift=RIGHT * 0.2),
                FadeIn(card_group[i * 3 + 2], shift=LEFT * 0.2),
                run_time=0.45
            )

        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(title, axis_group, origin_dot, o_lbl,
                           neg_arrow, pos_arrow, neg_region, pos_region,
                           card_group)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 9: 片尾
    # ------------------------------------------------------------------

    def scene_9_outro(self):
        """片尾: 作者信息 + 关注提示"""

        # 作者名放大居中
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE, weight=BOLD
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 0.4)

        self.play(
            Transform(self.author_mob, author_big),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=32, color=COLOR_HL
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 装饰: 一条小数轴，点从左到右扫一遍
        outro_axis, outro_coord = self._make_number_line(
            x_range=(-3, 3, 1),
            length=5.5,
            center=np.array([0.0, -2.5, 0]),
            include_numbers=True,
        )
        self.play(Create(outro_axis), run_time=0.8)

        sweep_dot = Dot(outro_coord(-3), color=COLOR_HL, radius=0.16)
        self.play(FadeIn(sweep_dot), run_time=0.2)
        self.play(
            sweep_dot.animate.move_to(outro_coord(3)),
            run_time=1.2,
            rate_func=smooth
        )
        self.play(Flash(sweep_dot, color=COLOR_HL, flash_radius=0.35), run_time=0.4)
        self.wait(0.6)

        # 全部淡出
        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow_text,
                           outro_axis, sweep_dot)),
            run_time=1.0
        )
