"""
认识分 - Understanding Minutes (Clock Face)
小学二年级下册第三章  时间的初步认识（二）

TikTok 竖屏格式 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

manim -pql clock_minutes.py ClockMinutes   # 快速预览
manim -qh  clock_minutes.py ClockMinutes   # 高质量 1080p

钟面知识点:
  - 12个大格, 每大格5个小格, 共60小格
  - 分针走1小格 = 1分钟
  - 分针走1大格 = 5分钟
  - 分针走一圈 = 60分钟 = 1小时
"""

from manim import *
import numpy as np

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


# ─── 颜色常量 ──────────────────────────────────────
C_BG        = "#1a1a2e"
C_CLOCK_RIM = "#f1c40f"      # 钟圈（金色）
C_MAJOR     = WHITE          # 大格刻度
C_MINOR     = "#aaaaaa"      # 小格刻度（灰）
C_MINOR_HL  = "#e74c3c"      # 高亮小格（红）
C_MAJOR_HL  = "#2ecc71"      # 高亮大格（绿）
C_NUM       = WHITE          # 数字
C_HOUR_HAND = "#95a5a6"      # 时针（浅灰）
C_MIN_HAND  = "#e74c3c"      # 分针（红）
C_ARC       = "#f39c12"      # 扇形弧（橙）
C_AUX       = GRAY_B         # 辅助色


# ─── 精确几何计算 ──────────────────────────────────
def clock_angle(minutes: float) -> float:
    """分钟值 → Manim 极坐标角度（12点正上方=PI/2，顺时针）"""
    return np.pi / 2 - (minutes / 60.0) * 2 * np.pi


def hand_vec(minutes: float, length: float) -> np.ndarray:
    """返回指针方向向量（从圆心出发）"""
    a = clock_angle(minutes)
    return length * np.array([np.cos(a), np.sin(a), 0])


class ClockMinutes(Scene):
    def construct(self):
        self.camera.background_color = C_BG
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_clock_structure()
        self.scene_3_major_sections()
        self.scene_4_minute_hand_move()
        self.scene_5_five_minutes()
        self.scene_6_full_circle()
        self.scene_7_outro()

    # ═══════════════════════════════════════════════
    #  统一几何初始化
    # ═══════════════════════════════════════════════
    def setup_geometry(self):
        self.R       = 2.8       # 钟面半径
        self.CENTER  = np.array([0.0, 1.2, 0.0])  # 钟面中心
        self.R_NUM   = self.R - 0.45   # 数字标注半径
        self.R_TICK_OUT = self.R - 0.02  # 刻度外端
        self.TICK_MAJ   = 0.32   # 大格刻度长
        self.TICK_MIN   = 0.16   # 小格刻度长
        self.MIN_LEN    = 2.2    # 分针长度
        self.HOUR_LEN   = 1.45   # 时针长度

        # 预计算60个刻度位置
        self._ticks = []  # (index, is_major, outer_pt, inner_pt)
        for i in range(60):
            a = clock_angle(i)
            outer = self.CENTER + self.R_TICK_OUT * np.array([np.cos(a), np.sin(a), 0])
            tick_len = self.TICK_MAJ if i % 5 == 0 else self.TICK_MIN
            inner = outer - tick_len * np.array([np.cos(a), np.sin(a), 0])
            self._ticks.append((i, i % 5 == 0, outer, inner))

        # 验证关键点
        tip_12 = self.CENTER + hand_vec(0, self.MIN_LEN)
        tip_3  = self.CENTER + hand_vec(15, self.MIN_LEN)
        assert abs(tip_12[0] - self.CENTER[0]) < 1e-9, "12点分针应在正上方"
        assert abs(tip_3[1]  - self.CENTER[1]) < 1e-9, "3点分针应在正右方"

    # ═══════════════════════════════════════════════
    #  构建完整钟面 VGroup（供多场景复用）
    # ═══════════════════════════════════════════════
    def _make_clock_face(self,
                         show_numbers=True,
                         highlight_major=False,
                         highlight_minor=False,
                         hour_time=10, min_time=0) -> VGroup:
        """
        构建静态钟面 VGroup，不添加到场景
        """
        g = VGroup()

        # 外圆（金色边框）
        rim = Circle(radius=self.R, color=C_CLOCK_RIM,
                     stroke_width=6, fill_color="#1a1a2e", fill_opacity=1)
        rim.move_to(self.CENTER)
        g.add(rim)

        # 刻度
        for i, is_major, outer, inner in self._ticks:
            color = (C_MAJOR_HL if (is_major and highlight_major)
                     else C_MINOR_HL if (not is_major and highlight_minor)
                     else C_MAJOR if is_major
                     else C_MINOR)
            sw = 3.5 if is_major else 1.5
            tick = Line(inner, outer, color=color, stroke_width=sw)
            g.add(tick)

        # 数字 1-12
        if show_numbers:
            for h in range(1, 13):
                m_eq = (h % 12) * 5
                a    = clock_angle(m_eq)
                pos  = self.CENTER + self.R_NUM * np.array([np.cos(a), np.sin(a), 0])
                num  = Text(str(h), font="Noto Sans CJK SC",
                            font_size=26, color=C_NUM,
                            weight=BOLD)
                num.move_to(pos)
                g.add(num)

        # 中心圆点
        center_dot = Dot(self.CENTER, radius=0.14,
                         color=C_CLOCK_RIM, fill_opacity=1)
        g.add(center_dot)

        # 时针
        hour_hand = Line(
            self.CENTER,
            self.CENTER + hand_vec(hour_time * 5, self.HOUR_LEN),
            color=C_HOUR_HAND, stroke_width=7,
        )
        g.add(hour_hand)

        # 分针
        min_hand = Line(
            self.CENTER,
            self.CENTER + hand_vec(min_time, self.MIN_LEN),
            color=C_MIN_HAND, stroke_width=4,
        )
        g.add(min_hand)

        return g

    def _make_hands(self, hour_time=10, min_time=0):
        """仅返回时针+分针 VGroup（用于动态更新）"""
        hour_hand = Line(
            self.CENTER,
            self.CENTER + hand_vec(hour_time * 5, self.HOUR_LEN),
            color=C_HOUR_HAND, stroke_width=7,
        )
        min_hand = Line(
            self.CENTER,
            self.CENTER + hand_vec(min_time, self.MIN_LEN),
            color=C_MIN_HAND, stroke_width=4,
        )
        return hour_hand, min_hand

    # ═══════════════════════════════════════════════
    #  Scene 1: 开场钩子
    # ═══════════════════════════════════════════════
    def scene_1_opening(self):
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font="Noto Sans CJK SC", font_size=20, color=C_AUX,
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        title = Text("认识「分」", font="Noto Sans CJK SC",
                      font_size=52, color=GOLD).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        hook = Text(
            "分针走一圈，到底有多少格？",
            font="Noto Sans CJK SC", font_size=26, color=WHITE,
        ).move_to(UP * 5.3)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.5)

        # 展示完整钟面（分针在12点）
        clock = self._make_clock_face(hour_time=10, min_time=0)
        self.play(FadeIn(clock, scale=0.6), run_time=0.8)

        # 分针快速旋转一圈（吸引注意）
        full_rot_angle = -2 * np.pi   # 顺时针一圈
        min_hand_mob = clock[-1]       # 分针是最后一个元素
        self.play(
            Rotate(min_hand_mob, angle=full_rot_angle,
                   about_point=self.CENTER, run_time=1.5, rate_func=smooth),
        )
        self.wait(0.4)

        self.play(FadeOut(title), FadeOut(hook), run_time=0.4)
        self.clock_opening = clock   # 保留钟面

    # ═══════════════════════════════════════════════
    #  Scene 2: 钟面结构（12大格 + 60小格）
    # ═══════════════════════════════════════════════
    def scene_2_clock_structure(self):
        sc_title = Text("认识钟面", font="Noto Sans CJK SC",
                         font_size=32, color=GOLD).move_to(UP * 6.2)
        self.play(Write(sc_title), run_time=0.5)

        # 过渡：让原来的钟面淡出，换一个结构清晰的版本
        clock2 = self._make_clock_face(hour_time=10, min_time=0)
        self.play(Transform(self.clock_opening, clock2), run_time=0.5)

        # ── 说明 12 个大格 ──
        note_12 = Text("钟面上有 12 个大格",
                        font="Noto Sans CJK SC", font_size=26, color=C_MAJOR_HL,
                        ).move_to(DOWN * 2.0)
        self.play(Write(note_12), run_time=0.5)

        # 用弧线依次高亮12个大格之间的间隔
        for i in range(12):
            start_m  = i * 5
            end_m    = (i + 1) * 5
            a_start  = clock_angle(start_m)
            a_end    = clock_angle(end_m)
            arc_span = a_end - a_start  # 负值（顺时针）

            arc = Arc(
                radius=self.R * 0.72,
                start_angle=a_start,
                angle=arc_span,
                color=C_MAJOR_HL,
                stroke_width=5,
            ).move_to(self.CENTER)
            self.play(Create(arc), run_time=0.12)

        self.wait(0.7)

        # ── 说明 5 个小格 ──
        note_5 = Text("每个大格里有 5 个小格",
                       font="Noto Sans CJK SC", font_size=26, color=C_MINOR_HL,
                       ).move_to(DOWN * 3.0)
        self.play(Write(note_5), run_time=0.5)

        # 放大高亮第一个大格的5个小格
        # 在12→1之间（0~5分位置）高亮5条小刻度
        for j in range(1, 5):  # j=1,2,3,4（第0和第5是大格刻度）
            tick_idx = j  # 小格 1~4
            _, _, outer, inner = self._ticks[tick_idx]
            hi_tick = Line(inner, outer, color=C_MINOR_HL, stroke_width=4)
            self.play(Create(hi_tick), run_time=0.18)

        self.wait(1.0)

        # ── 总计 60 小格 ──
        note_60 = Text("一共 60 个小格",
                        font="Noto Sans CJK SC", font_size=26, color=YELLOW,
                        ).move_to(DOWN * 4.0)
        self.play(Write(note_60), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(sc_title), FadeOut(note_12),
            FadeOut(note_5), FadeOut(note_60),
            run_time=0.4,
        )
        self.play(FadeOut(self.clock_opening), run_time=0.3)

    # ═══════════════════════════════════════════════
    #  Scene 3: 12大格 数字对应
    # ═══════════════════════════════════════════════
    def scene_3_major_sections(self):
        sc_title = Text("12个大格，分针怎么走？",
                         font="Noto Sans CJK SC", font_size=28, color=GOLD,
                         ).move_to(UP * 6.2)
        self.play(Write(sc_title), run_time=0.5)

        # 画只有大格刻度和数字的简洁钟面（无小格，突出结构）
        clock3 = self._make_clock_face(hour_time=10, min_time=0)
        self.play(FadeIn(clock3, scale=0.6), run_time=0.6)

        # 在12点旁放一个"起点"标记
        start_label = Text("出发！", font="Noto Sans CJK SC",
                            font_size=22, color=YELLOW,
                            ).next_to(self.CENTER + UP * (self.R + 0.4), UP, buff=0.05)
        start_arrow = Arrow(
            start=start_label.get_bottom() + DOWN * 0.05,
            end=self.CENTER + hand_vec(0, self.R - 0.1),
            buff=0.05, color=YELLOW, stroke_width=2, tip_length=0.18,
        )
        self.play(FadeIn(start_label), GrowArrow(start_arrow), run_time=0.5)
        self.wait(0.4)

        # 逐个高亮大格：分针从12走到1，再到2...
        hint_text = Text("分针每走一个大格 =",
                          font="Noto Sans CJK SC", font_size=24, color=WHITE,
                          ).move_to(DOWN * 2.2)
        self.play(FadeIn(hint_text), run_time=0.4)

        # 分针当前位置
        min_hand = clock3[-1]  # 分针

        for step in range(1, 4):  # 展示前3个大格的移动
            prev_m = (step - 1) * 5
            cur_m  = step * 5
            # 角度变化（顺时针 = Manim 负方向）
            d_angle = clock_angle(cur_m) - clock_angle(prev_m)  # 负值

            # 新分针
            new_min = Line(
                self.CENTER,
                self.CENTER + hand_vec(cur_m, self.MIN_LEN),
                color=C_MIN_HAND, stroke_width=4,
            )

            # 弧轨迹
            arc = Arc(
                radius=self.MIN_LEN * 0.75,
                start_angle=clock_angle(prev_m),
                angle=d_angle,
                color=C_ARC, stroke_width=2,
            ).move_to(self.CENTER)

            five_label = Text("5 分钟", font="Noto Sans CJK SC",
                               font_size=22, color=C_MAJOR_HL,
                               ).move_to(DOWN * 3.1)

            self.play(
                Transform(min_hand, new_min),
                Create(arc),
                run_time=0.6,
            )
            self.play(FadeIn(five_label), run_time=0.3)
            self.wait(0.2)
            self.play(FadeOut(five_label), FadeOut(arc), run_time=0.2)

        self.wait(0.8)
        self.play(
            FadeOut(sc_title), FadeOut(start_label), FadeOut(start_arrow),
            FadeOut(hint_text), FadeOut(clock3),
            run_time=0.4,
        )

    # ═══════════════════════════════════════════════
    #  Scene 4: 分针走1小格 = 1分钟
    # ═══════════════════════════════════════════════
    def scene_4_minute_hand_move(self):
        sc_title = Text("分针走 1 小格 = 1 分钟",
                         font="Noto Sans CJK SC", font_size=28, color=GOLD,
                         ).move_to(UP * 6.2)
        self.play(Write(sc_title), run_time=0.5)

        clock4 = self._make_clock_face(hour_time=10, min_time=0)
        self.play(FadeIn(clock4, scale=0.6), run_time=0.6)

        # 在12→1之间高亮5个小格（红色刻度）
        small_ticks_hl = VGroup()
        for j in range(1, 5):
            _, _, outer, inner = self._ticks[j]
            hl = Line(inner, outer, color=C_MINOR_HL, stroke_width=4)
            small_ticks_hl.add(hl)
        self.play(Create(small_ticks_hl), run_time=0.5)

        # 分针从12走到第1小格
        min_hand = clock4[-1]

        for step in range(1, 4):  # 走前3小格
            new_min = Line(
                self.CENTER,
                self.CENTER + hand_vec(step, self.MIN_LEN),
                color=C_MIN_HAND, stroke_width=4,
            )

            count_label = Text(
                f"第 {step} 格 → {step} 分钟",
                font="Noto Sans CJK SC", font_size=26, color=WHITE,
            ).move_to(DOWN * 2.3)

            self.play(Transform(min_hand, new_min), run_time=0.5)
            self.play(FadeIn(count_label), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(count_label), run_time=0.25)

        # 强调框
        key_box = Text("分针走 1 小格 = 1 分钟",
                        font="Noto Sans CJK SC", font_size=26, color=C_MINOR_HL,
                        ).move_to(DOWN * 2.3)
        key_border = SurroundingRectangle(key_box, color=C_MINOR_HL,
                                           buff=0.2, corner_radius=0.1)
        self.play(Write(key_box), Create(key_border), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(sc_title), FadeOut(clock4),
            FadeOut(small_ticks_hl), FadeOut(key_box), FadeOut(key_border),
            run_time=0.4,
        )

    # ═══════════════════════════════════════════════
    #  Scene 5: 分针走1大格 = 5分钟（动态演示）
    # ═══════════════════════════════════════════════
    def scene_5_five_minutes(self):
        sc_title = Text("分针走 1 大格 = 5 分钟",
                         font="Noto Sans CJK SC", font_size=28, color=GOLD,
                         ).move_to(UP * 6.2)
        self.play(Write(sc_title), run_time=0.5)

        clock5 = self._make_clock_face(hour_time=10, min_time=0)
        self.play(FadeIn(clock5, scale=0.6), run_time=0.6)

        min_hand = clock5[-1]

        # 高亮大格弧
        a_start = clock_angle(0)
        a_end   = clock_angle(5)
        major_arc = Arc(
            radius=self.R * 0.65,
            start_angle=a_start,
            angle=a_end - a_start,
            color=C_MAJOR_HL, stroke_width=6,
        ).move_to(self.CENTER)

        explain = Text("12 → 1 之间有 5 个小格",
                        font="Noto Sans CJK SC", font_size=24, color=C_MAJOR_HL,
                        ).move_to(DOWN * 2.2)
        self.play(Create(major_arc), Write(explain), run_time=0.7)

        # 分针逐格走到5
        for step in range(1, 6):
            new_min = Line(
                self.CENTER,
                self.CENTER + hand_vec(step, self.MIN_LEN),
                color=C_MIN_HAND, stroke_width=4,
            )
            self.play(Transform(min_hand, new_min), run_time=0.35)
            if step == 5:
                hit_label = Text("走到 1！= 5分钟",
                                  font="Noto Sans CJK SC", font_size=24,
                                  color=YELLOW).move_to(DOWN * 3.2)
                self.play(FadeIn(hit_label, scale=1.05), run_time=0.4)
                self.wait(0.6)
                self.play(FadeOut(hit_label), run_time=0.3)

        # 公式强调框
        formula_txt = Text("1 大格 = 5 小格 = 5 分钟",
                            font="Noto Sans CJK SC", font_size=28,
                            color=C_MAJOR_HL).move_to(DOWN * 3.3)
        formula_box = SurroundingRectangle(formula_txt, color=C_MAJOR_HL,
                                            buff=0.22, corner_radius=0.12)
        self.play(Write(formula_txt), Create(formula_box), run_time=0.7)
        self.wait(1.8)

        self.play(
            FadeOut(sc_title), FadeOut(clock5), FadeOut(major_arc),
            FadeOut(explain), FadeOut(formula_txt), FadeOut(formula_box),
            run_time=0.4,
        )

    # ═══════════════════════════════════════════════
    #  Scene 6: 分针走一圈 = 60分钟 = 1小时
    # ═══════════════════════════════════════════════
    def scene_6_full_circle(self):
        sc_title = Text("分针走一圈 = 60 分钟 = 1 小时",
                         font="Noto Sans CJK SC", font_size=26, color=GOLD,
                         ).move_to(UP * 6.2)
        self.play(Write(sc_title), run_time=0.5)

        clock6 = self._make_clock_face(hour_time=10, min_time=0)
        self.play(FadeIn(clock6, scale=0.6), run_time=0.6)

        # 计数显示
        counter_label = Text("0 分", font="Noto Sans CJK SC",
                              font_size=34, color=WHITE,
                              ).move_to(DOWN * 2.5)
        self.play(FadeIn(counter_label), run_time=0.3)

        min_hand = clock6[-1]

        # 每5分钟更新一次（展示12步）
        for step in range(1, 13):
            cur_m = step * 5
            new_min = Line(
                self.CENTER,
                self.CENTER + hand_vec(cur_m % 60, self.MIN_LEN),
                color=C_MIN_HAND, stroke_width=4,
            )
            new_label = Text(
                f"{cur_m} 分" if cur_m < 60 else "60 分 = 1 小时",
                font="Noto Sans CJK SC",
                font_size=34 if cur_m < 60 else 30,
                color=YELLOW if cur_m == 60 else WHITE,
            ).move_to(DOWN * 2.5)

            self.play(
                Transform(min_hand, new_min),
                Transform(counter_label, new_label),
                run_time=0.35,
            )

        # 强调一圈完成
        self.play(
            Flash(Dot(self.CENTER, radius=0.01), color=YELLOW,
                  flash_radius=self.R * 0.4, num_lines=14),
            run_time=0.6,
        )
        self.wait(0.5)

        # 三行公式汇总
        formulas = VGroup(
            Text("分针走 1 小格 = 1 分钟",
                  font="Noto Sans CJK SC", font_size=22, color=C_MINOR_HL),
            Text("分针走 1 大格 = 5 分钟",
                  font="Noto Sans CJK SC", font_size=22, color=C_MAJOR_HL),
            Text("分针走一圈  = 60 分钟 = 1 小时",
                  font="Noto Sans CJK SC", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(DOWN * 4.5)
        formula_box = SurroundingRectangle(formulas, color=GOLD,
                                            buff=0.25, corner_radius=0.12)
        self.play(Write(formulas), Create(formula_box), run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(sc_title), FadeOut(clock6),
            FadeOut(counter_label), FadeOut(formulas), FadeOut(formula_box),
            run_time=0.5,
        )

    # ═══════════════════════════════════════════════
    #  Scene 7: 总结 + 片尾
    # ═══════════════════════════════════════════════
    def scene_7_outro(self):
        # 最终小结卡片
        summary_title = Text("今天学会了什么？",
                              font="Noto Sans CJK SC", font_size=30, color=GOLD,
                              ).move_to(UP * 5.8)
        self.play(Write(summary_title), run_time=0.5)

        items = VGroup(
            Text("① 钟面有 12 大格，每格 5 小格，共 60 格",
                  font="Noto Sans CJK SC", font_size=22, color=WHITE),
            Text("② 分针走 1 小格 = 1 分钟",
                  font="Noto Sans CJK SC", font_size=22, color=C_MINOR_HL),
            Text("③ 分针走 1 大格 = 5 分钟",
                  font="Noto Sans CJK SC", font_size=22, color=C_MAJOR_HL),
            Text("④ 分针走一圈  = 60 分钟 = 1 小时",
                  font="Noto Sans CJK SC", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to(UP * 4.0)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.45)

        # 小钟面装饰
        mini_clock = self._make_clock_face(hour_time=10, min_time=0)
        mini_clock.scale(0.45).move_to(DOWN * 1.5)
        self.play(FadeIn(mini_clock, scale=0.5), run_time=0.6)

        # 闪烁中心提示
        self.play(
            Flash(Dot(mini_clock.get_center(), radius=0.01),
                  color=GOLD, flash_radius=0.6, num_lines=10),
            run_time=0.5,
        )
        self.wait(0.5)

        # 片尾
        name_big = Text("上海初高中数学直通车",
                         font="Noto Sans CJK SC", font_size=40, color=WHITE,
                         ).move_to(DOWN * 3.6)
        id_text  = Text("@emptyandcalm",
                         font="Noto Sans CJK SC", font_size=26, color=C_AUX,
                         ).move_to(DOWN * 4.5)
        call     = Text("关注我，获得更多数学技巧！",
                         font="Noto Sans CJK SC", font_size=26, color=GOLD,
                         ).move_to(DOWN * 5.4)

        self.play(Transform(self.author, name_big), run_time=0.7)
        self.play(FadeIn(id_text, shift=UP * 0.3), run_time=0.4)
        self.play(FadeIn(call, scale=1.1), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(summary_title), FadeOut(items),
            FadeOut(mini_clock),
            FadeOut(self.author), FadeOut(id_text), FadeOut(call),
            run_time=0.8,
        )