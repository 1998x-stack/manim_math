"""
认识整时 - 一年级时间初步认识
Whole Hour Recognition Animation - Grade 1

知识点: 分针指12，时针指几就是几时。读写：8时 = 8:00
格式: TikTok 竖屏 1080×1920
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR       = "#1a1a2e"
COLOR_RIM      = "#c8a84b"
COLOR_FACE     = "#fdf6e3"
COLOR_NUMBER   = "#2c3e50"
COLOR_TICK_BIG = "#4a4a4a"
COLOR_TICK_SML = "#9a9a9a"
COLOR_HOUR     = "#1a237e"   # 时针深蓝
COLOR_MIN      = "#b71c1c"   # 分针深红
COLOR_HIGHLIGHT = "#f9ca24"
COLOR_CORRECT  = "#27ae60"
COLOR_DIGITAL  = "#1565c0"

AUTHOR_FONT = "PingFang SC"

# 钟面参数（已验证）
CLOCK_CENTER = np.array([0.0, 1.8, 0.0])
R      = 2.5
R_NUM  = 2.05
R_BI_O = 2.5
R_BI_I = 2.25
R_SM_O = 2.5
R_SM_I = 2.37
HOUR_LEN = 1.40
MIN_LEN  = 2.00


def clock_pos(hour_num, radius, center=CLOCK_CENTER):
    ang = np.radians(90.0 - (hour_num % 12) * 30.0)
    return center + np.array([radius * np.cos(ang),
                               radius * np.sin(ang), 0.0])


def build_clock(center=CLOCK_CENTER, show_hands=True, hour=12):
    """
    构建完整钟面 VGroup。
    show_hands: 是否包含指针
    hour: 时针位置（整时，分针恒指12）
    返回 (clock_vgroup, hour_hand, min_hand)
    """
    # 表盘/表圈
    face = Circle(radius=R - 0.04, color=COLOR_FACE,
                  fill_opacity=1.0, stroke_width=0).move_to(center)
    rim  = Circle(radius=R, color=COLOR_RIM,
                  stroke_width=8, fill_opacity=0).move_to(center)

    # 大刻度
    big_ticks = VGroup()
    for i in range(12):
        ang = np.radians(90.0 - i * 30.0)
        outer = center + R_BI_O * np.array([np.cos(ang), np.sin(ang), 0])
        inner = center + R_BI_I * np.array([np.cos(ang), np.sin(ang), 0])
        big_ticks.add(Line(outer, inner, stroke_width=4, color=COLOR_TICK_BIG))

    # 小刻度
    small_ticks = VGroup()
    for i in range(60):
        if i % 5 == 0:
            continue
        ang = np.radians(90.0 - i * 6.0)
        outer = center + R_SM_O * np.array([np.cos(ang), np.sin(ang), 0])
        inner = center + R_SM_I * np.array([np.cos(ang), np.sin(ang), 0])
        small_ticks.add(Line(outer, inner, stroke_width=1.5, color=COLOR_TICK_SML))

    # 数字
    nums = VGroup()
    num_texts = ["12","1","2","3","4","5","6","7","8","9","10","11"]
    for i, t in enumerate(num_texts):
        pos = clock_pos(i, R_NUM, center)
        nums.add(Text(t, font=AUTHOR_FONT, font_size=26,
                      color=COLOR_NUMBER, weight=BOLD).move_to(pos))

    # 中心点
    center_dot = Dot(center, radius=0.12, color=COLOR_TICK_BIG)

    if not show_hands:
        return VGroup(face, rim, big_ticks, small_ticks, nums, center_dot), None, None

    # 时针（初始指12，然后在函数外用 Rotate 转到目标位置）
    h_tip = center + np.array([0, HOUR_LEN, 0])
    hour_hand = Line(center, h_tip,
                     stroke_width=11, color=COLOR_HOUR)

    # 分针（整时恒指12）
    m_tip = center + np.array([0, MIN_LEN, 0])
    min_hand = Line(center, m_tip,
                    stroke_width=5, color=COLOR_MIN)

    # 中心帽
    cap = Dot(center, radius=0.13, color=COLOR_RIM)

    # 立即把时针转到 hour 位置
    # hour * 30° 顺时针 = rotate(-hour * PI/6) 绕圆心
    if hour % 12 != 0:
        hour_hand.rotate(
            -np.radians((hour % 12) * 30.0),
            about_point=center
        )

    clock_vg = VGroup(face, rim, big_ticks, small_ticks, nums,
                      hour_hand, min_hand, cap, center_dot)
    return clock_vg, hour_hand, min_hand


class WholeHourAnimation(Scene):
    """认识整时教学动画"""

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=AUTHOR_FONT, font_size=18, color=GRAY_B
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        self.scene_1_hook()
        self.scene_2_rule()
        self.scene_3_examples()
        self.scene_4_read_write()
        self.scene_5_quiz()
        self.scene_6_outro()

    # ─────────────────────────────────────────────
    # Scene 1: 钩子
    # ─────────────────────────────────────────────
    def scene_1_hook(self):
        q = Text("几时了？", font=AUTHOR_FONT,
                 font_size=62, color=COLOR_HIGHLIGHT).move_to(UP * 5.3)
        self.play(Write(q), run_time=0.8)

        # 预览 8:00 的时钟
        preview, ph, pm = build_clock(CLOCK_CENTER, show_hands=True, hour=8)
        self.play(FadeIn(preview, scale=0.6), run_time=0.7)
        self.wait(0.5)

        sub = Text("今天学会认读整时！",
                   font=AUTHOR_FONT, font_size=38, color=WHITE
                   ).move_to(DOWN * 3.5)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(q), FadeOut(sub), FadeOut(preview), run_time=0.5)

    # ─────────────────────────────────────────────
    # Scene 2: 整时规律
    # ─────────────────────────────────────────────
    def scene_2_rule(self):
        title = Text("整时怎么认？",
                     font=AUTHOR_FONT, font_size=42, color=COLOR_HIGHLIGHT
                     ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # 创建 12时 的钟（两针都指12）
        clock_vg, h_hand, m_hand = build_clock(CLOCK_CENTER, show_hands=True, hour=12)
        self.play(FadeIn(clock_vg, scale=0.7), run_time=0.8)
        self.wait(0.3)

        # 高亮分针
        rule1_box = SurroundingRectangle(
            m_hand, color=COLOR_MIN, buff=0.15, corner_radius=0.1
        )
        rule1_text = VGroup(
            Text("①", font=AUTHOR_FONT, font_size=30, color=COLOR_MIN, weight=BOLD),
            Text(" 分针指向 ", font=AUTHOR_FONT, font_size=28, color=WHITE),
            Text("12", font=AUTHOR_FONT, font_size=34, color=COLOR_HIGHLIGHT, weight=BOLD),
        ).arrange(RIGHT, buff=0.06).move_to(np.array([0, -3.8, 0]))

        self.play(Create(rule1_box),
                  m_hand.animate.set_stroke(color=YELLOW, width=8),
                  run_time=0.6)
        self.play(Write(rule1_text), run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(rule1_box),
            m_hand.animate.set_stroke(color=COLOR_MIN, width=5),
            run_time=0.3
        )

        # 高亮时针
        rule2_box = SurroundingRectangle(
            h_hand, color=COLOR_HOUR, buff=0.15, corner_radius=0.1
        )
        rule2_text = VGroup(
            Text("②", font=AUTHOR_FONT, font_size=30, color=COLOR_HOUR, weight=BOLD),
            Text(" 时针指向几 → 就是几时", font=AUTHOR_FONT, font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.06).move_to(np.array([0, -5.0, 0]))

        self.play(Create(rule2_box),
                  h_hand.animate.set_stroke(color=YELLOW, width=14),
                  FadeIn(rule2_text, shift=UP * 0.2),
                  run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(rule2_box),
            h_hand.animate.set_stroke(color=COLOR_HOUR, width=11),
            FadeOut(rule1_text), FadeOut(rule2_text),
            FadeOut(clock_vg), FadeOut(title),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 3: 三个例子（3时、8时、12时）
    # ─────────────────────────────────────────────
    def scene_3_examples(self):
        examples = [
            (3,  "3 时",  "3:00",  "#1565c0"),
            (8,  "8 时",  "8:00",  "#6a1b9a"),
            (12, "12 时", "12:00", "#2e7d32"),
        ]

        title = Text("看钟认时间",
                     font=AUTHOR_FONT, font_size=42, color=COLOR_HIGHLIGHT
                     ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        for hour, label, digital, accent_color in examples:
            self._show_one_example(hour, label, digital, accent_color)

        self.play(FadeOut(title), run_time=0.3)

    def _show_one_example(self, hour, label, digital, accent_color):
        """展示一个整时例子"""
        # 先展示两针都指12的钟
        clock_vg, h_hand, m_hand = build_clock(
            CLOCK_CENTER, show_hands=True, hour=12
        )
        self.play(FadeIn(clock_vg, scale=0.7), run_time=0.6)

        # 分针高亮 → 指12
        min_hl = Text("分针指 12 ✓",
                      font=AUTHOR_FONT, font_size=30, color=COLOR_MIN
                      ).move_to(np.array([0, -3.8, 0]))
        self.play(
            m_hand.animate.set_stroke(color=YELLOW, width=8),
            FadeIn(min_hl, shift=UP * 0.2),
            run_time=0.5
        )
        self.wait(0.4)
        self.play(
            m_hand.animate.set_stroke(color=COLOR_MIN, width=5),
            FadeOut(min_hl),
            run_time=0.3
        )

        # 时针动画转到目标位置
        # 旋转角度 = -(hour % 12) * 30°（顺时针）
        # 注意：build_clock 中已把时针初始化在 hour=12 的位置（UP方向）
        rot_angle = -np.radians((hour % 12) * 30.0)

        if hour % 12 != 0:
            rotate_text = Text(
                f"时针转到 {hour}",
                font=AUTHOR_FONT, font_size=28, color=COLOR_HOUR
            ).move_to(np.array([0, -3.8, 0]))
            self.play(FadeIn(rotate_text), run_time=0.3)
            self.play(
                Rotate(h_hand, angle=rot_angle,
                       about_point=CLOCK_CENTER, run_time=1.2,
                       rate_func=smooth)
            )
            self.play(FadeOut(rotate_text), run_time=0.2)
        else:
            # 12时，不需要转
            pass

        # 高亮时针指向的数字
        num_pos = clock_pos(hour % 12, R_NUM)
        num_highlight = Circle(
            radius=0.35, color=accent_color,
            stroke_width=4, fill_opacity=0
        ).move_to(num_pos)
        self.play(Create(num_highlight), run_time=0.4)

        # 时间读法
        time_label = Text(
            label,
            font=AUTHOR_FONT, font_size=52,
            color=accent_color, weight=BOLD
        ).move_to(np.array([0, -4.2, 0]))

        digital_group = VGroup(
            Text("写作：", font=AUTHOR_FONT, font_size=28, color=GRAY_B),
            Text(digital, font=AUTHOR_FONT, font_size=44,
                 color=accent_color, weight=BOLD),
        ).arrange(RIGHT, buff=0.2).move_to(np.array([0, -5.5, 0]))

        self.play(FadeIn(time_label, scale=1.2), run_time=0.5)
        self.play(FadeIn(digital_group, shift=UP * 0.2), run_time=0.4)
        self.wait(1.2)

        # 清场
        self.play(
            FadeOut(clock_vg),
            FadeOut(num_highlight),
            FadeOut(time_label),
            FadeOut(digital_group),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 4: 读写规律总结
    # ─────────────────────────────────────────────
    def scene_4_read_write(self):
        title = Text("整时读写规律",
                     font=AUTHOR_FONT, font_size=40, color=COLOR_HIGHLIGHT
                     ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # 规律卡片
        card_data = [
            ("分针指向 12", COLOR_MIN),
            ("时针指向 几  →  几时", COLOR_HOUR),
            ("写法：  几 : 00", COLOR_DIGITAL),
        ]

        cards = VGroup()
        for i, (text, color) in enumerate(card_data):
            bg = RoundedRectangle(
                corner_radius=0.3, width=7.6, height=1.0,
                fill_color="#0d1b2a", fill_opacity=1.0,
                stroke_color=color, stroke_width=2.5
            )
            t = Text(text, font=AUTHOR_FONT, font_size=28,
                     color=color, weight=BOLD)
            t.move_to(bg.get_center())
            cards.add(VGroup(bg, t))

        cards.arrange(DOWN, buff=0.35).move_to(np.array([0, 2.5, 0]))

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.4)

        # 示例行
        eg_bg = RoundedRectangle(
            corner_radius=0.25, width=7.6, height=1.8,
            fill_color="#16213e", fill_opacity=1.0,
            stroke_color=GRAY_B, stroke_width=1.5
        ).move_to(np.array([0, -0.2, 0]))

        eg_row = VGroup(
            Text("例：", font=AUTHOR_FONT, font_size=26, color=GRAY_B),
            Text("8", font=AUTHOR_FONT, font_size=36,
                 color=COLOR_HOUR, weight=BOLD),
            Text("时", font=AUTHOR_FONT, font_size=30, color=WHITE),
            Text(" = ", font=AUTHOR_FONT, font_size=30, color=GRAY_B),
            Text("8:00", font=AUTHOR_FONT, font_size=36,
                 color=COLOR_DIGITAL, weight=BOLD),
        ).arrange(RIGHT, buff=0.15).move_to(np.array([0, -0.2, 0]))

        self.play(FadeIn(eg_bg), Write(eg_row), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(cards),
            FadeOut(eg_bg), FadeOut(eg_row),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 5: 小测验（展示3个时钟，猜时间）
    # ─────────────────────────────────────────────
    def scene_5_quiz(self):
        title = Text("你能认出来吗？",
                     font=AUTHOR_FONT, font_size=40, color=COLOR_HIGHLIGHT
                     ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        quiz_items = [
            (6,  "6 时",  "6:00",  "#e65100"),
            (10, "10 时", "10:00", "#4a148c"),
        ]

        for hour, answer, digital, color in quiz_items:
            clock_vg, h_hand, m_hand = build_clock(
                CLOCK_CENTER, show_hands=True, hour=hour
            )
            self.play(FadeIn(clock_vg, scale=0.7), run_time=0.6)

            # 问号
            question = Text("几时了？",
                            font=AUTHOR_FONT, font_size=42,
                            color=YELLOW).move_to(np.array([0, -4.0, 0]))
            self.play(FadeIn(question), run_time=0.4)
            self.wait(1.5)   # 留给学生思考

            # 揭晓
            self.play(FadeOut(question), run_time=0.2)
            ans_text = Text(answer,
                            font=AUTHOR_FONT, font_size=54,
                            color=color, weight=BOLD
                            ).move_to(np.array([0, -4.0, 0]))
            dig_text = Text(digital,
                            font=AUTHOR_FONT, font_size=38,
                            color=COLOR_DIGITAL
                            ).move_to(np.array([0, -5.3, 0]))

            self.play(FadeIn(ans_text, scale=1.3), run_time=0.5)
            self.play(FadeIn(dig_text, shift=UP * 0.2), run_time=0.4)
            self.wait(1.0)

            self.play(
                FadeOut(clock_vg),
                FadeOut(ans_text),
                FadeOut(dig_text),
                run_time=0.5
            )

        self.play(FadeOut(title), run_time=0.3)

    # ─────────────────────────────────────────────
    # Scene 6: 总结片尾
    # ─────────────────────────────────────────────
    def scene_6_outro(self):
        # 小钟表装饰
        mini_clock, mh, mm = build_clock(
            np.array([0, 3.5, 0]), show_hands=True, hour=8
        )
        mini_clock.scale(0.5)
        self.play(FadeIn(mini_clock, scale=0.5), run_time=0.5)

        # 要点
        points = [
            ("分针指 12", COLOR_MIN),
            ("时针指几 → 几时", COLOR_HOUR),
            ("写法：几 : 00", COLOR_DIGITAL),
        ]
        pt_cards = VGroup()
        for txt, col in points:
            bg = RoundedRectangle(
                corner_radius=0.25, width=7.2, height=0.85,
                fill_color="#0d1b2a", fill_opacity=1.0,
                stroke_color=col, stroke_width=2
            )
            t = Text(txt, font=AUTHOR_FONT, font_size=26, color=col)
            t.move_to(bg.get_center())
            pt_cards.add(VGroup(bg, t))
        pt_cards.arrange(DOWN, buff=0.25).move_to(np.array([0, 0.8, 0]))

        for card in pt_cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.3)

        # 作者
        author_big = Text("上海初高中数学直通车",
                          font=AUTHOR_FONT, font_size=32, color=WHITE
                          ).move_to(np.array([0, -2.8, 0]))
        author_id = Text("@emptyandcalm",
                         font=AUTHOR_FONT, font_size=26, color=GRAY_B
                         ).move_to(np.array([0, -3.8, 0]))
        follow = Text("关注我，学更多小学数学！",
                      font=AUTHOR_FONT, font_size=28, color=COLOR_HIGHLIGHT
                      ).move_to(np.array([0, -5.0, 0]))

        self.play(
            Transform(self.author, author_big),
            run_time=0.5
        )
        self.play(FadeIn(author_id), FadeIn(follow), run_time=0.5)

        # 动画时钟走动
        self.play(
            Rotate(mh, angle=-2 * PI,
                   about_point=mini_clock.get_center(),
                   run_time=2.0, rate_func=linear)
        )
        self.wait(0.5)

        self.play(
            FadeOut(mini_clock), FadeOut(pt_cards),
            FadeOut(author_id), FadeOut(follow),
            FadeOut(self.author), run_time=0.8
        )


# 渲染:
#   manim -pql whole_hour_animation.py WholeHourAnimation
#   manim -qh  whole_hour_animation.py WholeHourAnimation