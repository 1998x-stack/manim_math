"""
认识半时 - 一年级时间初步认识
Half Hour Recognition Animation - Grade 1

知识点: 分针指6，时针走过几就是几时半。8时半=8:30
教学难点: 时针在X和X+1之间 → 读数是X（不是X+1）
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
COLOR_HOUR     = "#1a237e"
COLOR_MIN      = "#b71c1c"
COLOR_HIGHLIGHT = "#f9ca24"
COLOR_WRONG    = "#e53935"    # 错误提示红
COLOR_CORRECT  = "#27ae60"    # 正确提示绿
COLOR_DIGITAL  = "#1565c0"

AUTHOR_FONT = "Noto Sans CJK SC"

# 钟面参数（已由 verify_half_hour.py 验证）
CLOCK_CENTER = np.array([0.0, 1.8, 0.0])
R      = 2.5
R_NUM  = 2.05
R_BI_O = 2.5
R_BI_I = 2.25
R_SM_O = 2.5
R_SM_I = 2.37
HOUR_LEN = 1.38
MIN_LEN  = 2.00


def clock_pos(hour_num, radius, center=CLOCK_CENTER):
    ang = np.radians(90.0 - (hour_num % 12) * 30.0)
    return center + np.array([radius * np.cos(ang),
                               radius * np.sin(ang), 0.0])


def build_clock_base(center=CLOCK_CENTER):
    """构建钟面基座（不含指针）"""
    face = Circle(radius=R - 0.04, color=COLOR_FACE,
                  fill_opacity=1.0, stroke_width=0).move_to(center)
    rim  = Circle(radius=R, color=COLOR_RIM,
                  stroke_width=8, fill_opacity=0).move_to(center)

    big_ticks = VGroup()
    for i in range(12):
        ang = np.radians(90.0 - i * 30.0)
        outer = center + R_BI_O * np.array([np.cos(ang), np.sin(ang), 0])
        inner = center + R_BI_I * np.array([np.cos(ang), np.sin(ang), 0])
        big_ticks.add(Line(outer, inner, stroke_width=4, color=COLOR_TICK_BIG))

    small_ticks = VGroup()
    for i in range(60):
        if i % 5 == 0:
            continue
        ang = np.radians(90.0 - i * 6.0)
        outer = center + R_SM_O * np.array([np.cos(ang), np.sin(ang), 0])
        inner = center + R_SM_I * np.array([np.cos(ang), np.sin(ang), 0])
        small_ticks.add(Line(outer, inner, stroke_width=1.5, color=COLOR_TICK_SML))

    nums = VGroup()
    num_texts = ["12","1","2","3","4","5","6","7","8","9","10","11"]
    for i, t in enumerate(num_texts):
        pos = clock_pos(i, R_NUM, center)
        nums.add(Text(t, font=AUTHOR_FONT, font_size=26,
                      color=COLOR_NUMBER, weight=BOLD).move_to(pos))

    center_dot = Dot(center, radius=0.12, color=COLOR_TICK_BIG)
    cap = Dot(center, radius=0.13, color=COLOR_RIM)

    return face, rim, big_ticks, small_ticks, nums, center_dot, cap


def make_hour_hand(center=CLOCK_CENTER):
    """创建时针（初始指12=UP）"""
    tip = center + np.array([0, HOUR_LEN, 0])
    return Line(center, tip, stroke_width=11,
                color=COLOR_HOUR)


def make_min_hand(center=CLOCK_CENTER):
    """创建分针（初始指12=UP）"""
    tip = center + np.array([0, MIN_LEN, 0])
    return Line(center, tip, stroke_width=5,
                color=COLOR_MIN)


def build_half_clock(hour, center=CLOCK_CENTER):
    """
    构建显示 X时半 的静态时钟
    - 分针指6（顺时针 -PI）
    - 时针顺时针转 (hour + 0.5) * 30°（负角）
    返回 (clock_vgroup, hour_hand, min_hand)
    """
    face, rim, big_ticks, small_ticks, nums, center_dot, cap = build_clock_base(center)
    h_hand = make_hour_hand(center)
    m_hand = make_min_hand(center)

    # 分针旋转到6：顺时针 -PI
    m_hand.rotate(-PI, about_point=center)

    # 时针旋转到 (hour%12 + 0.5) * 30° 顺时针
    h_rot = -np.radians((hour % 12 + 0.5) * 30.0)
    h_hand.rotate(h_rot, about_point=center)

    clock_vg = VGroup(face, rim, big_ticks, small_ticks, nums,
                      h_hand, m_hand, cap, center_dot)
    return clock_vg, h_hand, m_hand


class HalfHourAnimation(Scene):
    """认识半时教学动画"""

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=AUTHOR_FONT, font_size=18, color=GRAY_B
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        self.scene_1_hook()
        self.scene_2_from_whole_to_half()
        self.scene_3_key_difficulty()
        self.scene_4_examples()
        self.scene_5_wrong_warning()
        self.scene_6_outro()

    # ─────────────────────────────────────────────
    # Scene 1: 钩子
    # ─────────────────────────────────────────────
    def scene_1_hook(self):
        q = Text("半时是几时？",
                 font=AUTHOR_FONT, font_size=56,
                 color=COLOR_HIGHLIGHT).move_to(UP * 5.3)
        self.play(Write(q), run_time=0.9)

        # 预览 8:30 时钟
        preview, _, _ = build_half_clock(8, CLOCK_CENTER)
        self.play(FadeIn(preview, scale=0.6), run_time=0.7)
        self.wait(0.5)

        sub = Text("8时半 还是 9时半？",
                   font=AUTHOR_FONT, font_size=36, color=WHITE
                   ).move_to(DOWN * 3.5)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(q), FadeOut(sub), FadeOut(preview), run_time=0.5)

    # ─────────────────────────────────────────────
    # Scene 2: 从整时到半时的过渡
    # ─────────────────────────────────────────────
    def scene_2_from_whole_to_half(self):
        title = Text("半时是怎么来的？",
                     font=AUTHOR_FONT, font_size=38,
                     color=COLOR_HIGHLIGHT).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # 从 8时整 开始
        face, rim, big_ticks, small_ticks, nums, center_dot, cap = build_clock_base()
        h_hand = make_hour_hand()
        m_hand = make_min_hand()

        # 时针指向8
        h_hand.rotate(-np.radians(8 * 30.0), about_point=CLOCK_CENTER)

        clock_vg = VGroup(face, rim, big_ticks, small_ticks, nums,
                          h_hand, m_hand, cap, center_dot)
        self.play(FadeIn(clock_vg, scale=0.7), run_time=0.7)

        label_8 = Text("8时整",
                       font=AUTHOR_FONT, font_size=38,
                       color=COLOR_DIGITAL, weight=BOLD
                       ).move_to(np.array([0, -4.0, 0]))
        self.play(FadeIn(label_8), run_time=0.4)
        self.wait(0.5)

        # 说明："分针再走半圈到6"
        explain = Text("分针再走半圈……",
                       font=AUTHOR_FONT, font_size=30,
                       color=COLOR_MIN).move_to(np.array([0, -5.2, 0]))
        self.play(FadeIn(explain), run_time=0.4)

        # 分针从12顺时针转到6（-PI）
        # 同时时针也走了半格（额外 -15°）
        self.play(
            Rotate(m_hand, angle=-PI,
                   about_point=CLOCK_CENTER, run_time=1.8, rate_func=smooth),
            Rotate(h_hand, angle=-np.radians(15.0),
                   about_point=CLOCK_CENTER, run_time=1.8, rate_func=smooth),
        )
        self.play(FadeOut(explain), FadeOut(label_8), run_time=0.3)

        # 高亮分针指6
        num_6_pos = clock_pos(6, R_NUM)
        circle_6 = Circle(radius=0.38, color=COLOR_MIN,
                          stroke_width=4, fill_opacity=0).move_to(num_6_pos)

        min_label = VGroup(
            Text("分针指向 ", font=AUTHOR_FONT, font_size=30, color=WHITE),
            Text("6", font=AUTHOR_FONT, font_size=38,
                 color=COLOR_MIN, weight=BOLD),
            Text(" ✓", font=AUTHOR_FONT, font_size=30, color=COLOR_CORRECT),
        ).arrange(RIGHT, buff=0.08).move_to(np.array([0, -4.0, 0]))

        self.play(Create(circle_6),
                  m_hand.animate.set_stroke(color=YELLOW, width=8),
                  FadeIn(min_label), run_time=0.6)
        self.wait(1.0)

        result_label = Text("8时半！  8:30",
                            font=AUTHOR_FONT, font_size=42,
                            color=COLOR_DIGITAL, weight=BOLD
                            ).move_to(np.array([0, -5.4, 0]))
        self.play(
            m_hand.animate.set_stroke(color=COLOR_MIN, width=5),
            FadeOut(min_label),
            FadeOut(circle_6),
            FadeIn(result_label, scale=1.1),
            run_time=0.6
        )
        self.wait(1.0)

        self.play(
            FadeOut(clock_vg), FadeOut(result_label), FadeOut(title),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 3: 核心难点——时针"走过了几"
    # ─────────────────────────────────────────────
    def scene_3_key_difficulty(self):
        title = Text("注意时针的位置！",
                     font=AUTHOR_FONT, font_size=38,
                     color=COLOR_HIGHLIGHT).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # 显示 8时半 的钟面
        clock_vg, h_hand, m_hand = build_half_clock(8, CLOCK_CENTER)
        self.play(FadeIn(clock_vg, scale=0.7), run_time=0.7)
        self.wait(0.3)

        # 标注8和9
        pos_8 = clock_pos(8, R_NUM)
        pos_9 = clock_pos(9, R_NUM)

        circle_8 = Circle(radius=0.38, color=COLOR_CORRECT,
                          stroke_width=4, fill_opacity=0).move_to(pos_8)
        circle_9 = Circle(radius=0.38, color=GRAY_B,
                          stroke_width=2, fill_opacity=0).move_to(pos_9)

        self.play(Create(circle_8), Create(circle_9), run_time=0.5)

        # 错误提示
        wrong_label = VGroup(
            Text("❌ ", font=AUTHOR_FONT, font_size=28, color=COLOR_WRONG),
            Text("以为是 9时半？", font=AUTHOR_FONT, font_size=28, color=COLOR_WRONG),
        ).arrange(RIGHT, buff=0.1).move_to(np.array([0, -4.0, 0]))
        self.play(FadeIn(wrong_label, shift=UP * 0.2), run_time=0.5)

        # 问: 时针走过了哪里？
        explain_q = Text("时针走过了……",
                         font=AUTHOR_FONT, font_size=28, color=GRAY_A
                         ).move_to(np.array([0, -5.2, 0]))
        self.play(FadeIn(explain_q), run_time=0.4)
        self.wait(0.6)
        self.play(FadeOut(wrong_label), FadeOut(explain_q), run_time=0.3)

        # 弧形轨迹：从0到8的弧（时针已走过的路）
        # 用弧线标注时针已走过8的区域
        arc_passed = Arc(
            radius=(R_BI_I + 0.15),
            start_angle=PI / 2,
            angle=-np.radians(8.5 * 30.0),   # 顺时针(负)走过8.5格
            arc_center=CLOCK_CENTER,
            stroke_width=8,
            color=COLOR_CORRECT,
            stroke_opacity=0.7
        )

        correct_label = VGroup(
            Text("✓ ", font=AUTHOR_FONT, font_size=28, color=COLOR_CORRECT),
            Text("时针走过了 8 → 是", font=AUTHOR_FONT, font_size=26, color=WHITE),
            Text("8时半", font=AUTHOR_FONT, font_size=32,
                 color=COLOR_CORRECT, weight=BOLD),
        ).arrange(RIGHT, buff=0.08).move_to(np.array([0, -4.0, 0]))

        self.play(
            Create(arc_passed),
            h_hand.animate.set_stroke(color=COLOR_CORRECT, width=14),
            FadeIn(correct_label, shift=UP * 0.2),
            run_time=0.8
        )
        self.wait(1.5)

        rule_box_bg = RoundedRectangle(
            corner_radius=0.3, width=7.6, height=1.1,
            fill_color="#0d1b2a", fill_opacity=1.0,
            stroke_color=COLOR_HIGHLIGHT, stroke_width=2.5
        ).move_to(np.array([0, -5.5, 0]))
        rule_text = VGroup(
            Text("时针", font=AUTHOR_FONT, font_size=26,
                 color=COLOR_HOUR, weight=BOLD),
            Text("走过几 →", font=AUTHOR_FONT, font_size=26, color=WHITE),
            Text("几时半", font=AUTHOR_FONT, font_size=30,
                 color=COLOR_HIGHLIGHT, weight=BOLD),
        ).arrange(RIGHT, buff=0.15).move_to(np.array([0, -5.5, 0]))

        self.play(FadeIn(rule_box_bg), Write(rule_text), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(clock_vg), FadeOut(circle_8), FadeOut(circle_9),
            FadeOut(arc_passed), FadeOut(correct_label),
            FadeOut(rule_box_bg), FadeOut(rule_text), FadeOut(title),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 4: 三个例子
    # ─────────────────────────────────────────────
    def scene_4_examples(self):
        examples = [
            (3,  "3时半",  "3:30",  "#1565c0"),
            (8,  "8时半",  "8:30",  "#6a1b9a"),
        ]

        title = Text("一起来认！",
                     font=AUTHOR_FONT, font_size=40,
                     color=COLOR_HIGHLIGHT).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        for hour, label, digital, color in examples:
            self._show_half_example(hour, label, digital, color)

        self.play(FadeOut(title), run_time=0.3)

    def _show_half_example(self, hour, label, digital, accent_color):
        """展示一个半时例子（分针从12动画到6）"""
        face, rim, big_ticks, small_ticks, nums, center_dot, cap = build_clock_base()
        h_hand = make_hour_hand()
        m_hand = make_min_hand()

        # 时针先到整时位置
        h_hand.rotate(-np.radians(hour % 12 * 30.0), about_point=CLOCK_CENTER)

        clock_vg = VGroup(face, rim, big_ticks, small_ticks, nums,
                          h_hand, m_hand, cap, center_dot)
        self.play(FadeIn(clock_vg, scale=0.7), run_time=0.6)

        # 说明分针指12（整时状态）
        label_whole = Text(f"{hour}时整",
                           font=AUTHOR_FONT, font_size=32,
                           color=GRAY_A).move_to(np.array([0, -4.0, 0]))
        self.play(FadeIn(label_whole), run_time=0.3)
        self.wait(0.4)

        # 分针动画到6，时针走半格
        self.play(
            Rotate(m_hand, angle=-PI,
                   about_point=CLOCK_CENTER, run_time=1.5, rate_func=smooth),
            Rotate(h_hand, angle=-np.radians(15.0),
                   about_point=CLOCK_CENTER, run_time=1.5, rate_func=smooth),
            FadeOut(label_whole),
            run_time=1.5
        )

        # 高亮
        num_6_pos = clock_pos(6, R_NUM)
        circle_6 = Circle(radius=0.38, color=COLOR_MIN,
                          stroke_width=4, fill_opacity=0).move_to(num_6_pos)
        self.play(
            Create(circle_6),
            m_hand.animate.set_stroke(color=YELLOW, width=8),
            run_time=0.4
        )

        time_text = Text(label,
                         font=AUTHOR_FONT, font_size=50,
                         color=accent_color, weight=BOLD
                         ).move_to(np.array([0, -4.2, 0]))
        dig_text  = Text(digital,
                         font=AUTHOR_FONT, font_size=38,
                         color=COLOR_DIGITAL
                         ).move_to(np.array([0, -5.5, 0]))

        self.play(
            m_hand.animate.set_stroke(color=COLOR_MIN, width=5),
            FadeOut(circle_6),
            FadeIn(time_text, scale=1.2),
            run_time=0.5
        )
        self.play(FadeIn(dig_text, shift=UP * 0.2), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(clock_vg), FadeOut(time_text), FadeOut(dig_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 5: 易错警示
    # ─────────────────────────────────────────────
    def scene_5_wrong_warning(self):
        title = Text("常见错误！",
                     font=AUTHOR_FONT, font_size=40,
                     color=COLOR_WRONG).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # 显示 8时半 钟面
        clock_vg, h_hand, m_hand = build_half_clock(8, CLOCK_CENTER)
        self.play(FadeIn(clock_vg, scale=0.7), run_time=0.7)

        # 错误回答框
        wrong_bg = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=1.0,
            fill_color="#3e0000", fill_opacity=1.0,
            stroke_color=COLOR_WRONG, stroke_width=2.5
        ).move_to(np.array([0, -4.0, 0]))
        wrong_text = VGroup(
            Text("❌ 误认为：", font=AUTHOR_FONT, font_size=26, color=COLOR_WRONG),
            Text("9时半", font=AUTHOR_FONT, font_size=32,
                 color=COLOR_WRONG, weight=BOLD),
        ).arrange(RIGHT, buff=0.2).move_to(np.array([0, -4.0, 0]))

        self.play(FadeIn(wrong_bg), FadeIn(wrong_text), run_time=0.5)

        # 高亮9的位置（错误的）
        pos_9 = clock_pos(9, R_NUM)
        circle_9_wrong = Circle(radius=0.42, color=COLOR_WRONG,
                                stroke_width=5, fill_opacity=0).move_to(pos_9)
        cross_9 = Cross(scale_factor=0.35, color=COLOR_WRONG,
                        stroke_width=4).move_to(pos_9)
        self.play(Create(circle_9_wrong), Create(cross_9), run_time=0.5)
        self.wait(0.6)

        # 更正
        self.play(FadeOut(wrong_bg), FadeOut(wrong_text),
                  FadeOut(circle_9_wrong), FadeOut(cross_9), run_time=0.3)

        # 画弧线说明"走过"的路
        arc_path = Arc(
            radius=(R_BI_I + 0.12),
            start_angle=PI / 2,
            angle=-np.radians(8 * 30.0),    # 只标到8（走过了8）
            arc_center=CLOCK_CENTER,
            stroke_width=7,
            color=COLOR_CORRECT,
            stroke_opacity=0.8
        )
        self.play(Create(arc_path), run_time=0.8)

        pos_8 = clock_pos(8, R_NUM)
        circle_8_right = Circle(radius=0.42, color=COLOR_CORRECT,
                                stroke_width=4, fill_opacity=0).move_to(pos_8)

        correct_bg = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=1.0,
            fill_color="#003000", fill_opacity=1.0,
            stroke_color=COLOR_CORRECT, stroke_width=2.5
        ).move_to(np.array([0, -4.0, 0]))
        correct_text = VGroup(
            Text("✓ 正确：走过了 8 →", font=AUTHOR_FONT, font_size=26, color=WHITE),
            Text("8时半", font=AUTHOR_FONT, font_size=32,
                 color=COLOR_CORRECT, weight=BOLD),
        ).arrange(RIGHT, buff=0.15).move_to(np.array([0, -4.0, 0]))

        self.play(
            Create(circle_8_right),
            FadeIn(correct_bg),
            FadeIn(correct_text),
            run_time=0.6
        )
        self.wait(1.5)

        # 关键规则
        key_bg = RoundedRectangle(
            corner_radius=0.3, width=7.6, height=1.1,
            fill_color="#0d1b2a", fill_opacity=1.0,
            stroke_color=COLOR_HIGHLIGHT, stroke_width=3
        ).move_to(np.array([0, -5.5, 0]))
        key_text = VGroup(
            Text("时针刚过几 = ", font=AUTHOR_FONT, font_size=26, color=WHITE),
            Text("几", font=AUTHOR_FONT, font_size=32,
                 color=COLOR_HIGHLIGHT, weight=BOLD),
            Text("时半", font=AUTHOR_FONT, font_size=28, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(np.array([0, -5.5, 0]))

        self.play(FadeIn(key_bg), Write(key_text), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(clock_vg), FadeOut(arc_path),
            FadeOut(circle_8_right), FadeOut(correct_bg),
            FadeOut(correct_text), FadeOut(key_bg),
            FadeOut(key_text), FadeOut(title),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    # Scene 6: 总结片尾
    # ─────────────────────────────────────────────
    def scene_6_outro(self):
        # 小时钟（8:30）
        mini_clk, mh, mm = build_half_clock(
            8, np.array([0, 3.8, 0])
        )
        mini_clk.scale(0.45)
        self.play(FadeIn(mini_clk, scale=0.5), run_time=0.5)

        # 要点卡片
        points = [
            ("分针指向 6", COLOR_MIN),
            ("时针刚过几 → 几时半", COLOR_HOUR),
            ("写法：几 : 30", COLOR_DIGITAL),
            ("别看下一个数字！", COLOR_WRONG),
        ]
        pt_cards = VGroup()
        for txt, col in points:
            bg = RoundedRectangle(
                corner_radius=0.25, width=7.2, height=0.82,
                fill_color="#0d1b2a", fill_opacity=1.0,
                stroke_color=col, stroke_width=2
            )
            t = Text(txt, font=AUTHOR_FONT, font_size=24, color=col)
            t.move_to(bg.get_center())
            pt_cards.add(VGroup(bg, t))
        pt_cards.arrange(DOWN, buff=0.22).move_to(np.array([0, 0.5, 0]))

        for card in pt_cards:
            self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.3)

        # 作者信息
        author_big = Text("上海初高中数学直通车",
                          font=AUTHOR_FONT, font_size=32, color=WHITE
                          ).move_to(np.array([0, -2.8, 0]))
        author_id  = Text("@emptyandcalm",
                          font=AUTHOR_FONT, font_size=26, color=GRAY_B
                          ).move_to(np.array([0, -3.8, 0]))
        follow     = Text("关注我，学更多小学数学！",
                          font=AUTHOR_FONT, font_size=28, color=COLOR_HIGHLIGHT
                          ).move_to(np.array([0, -5.0, 0]))

        self.play(Transform(self.author, author_big), run_time=0.5)
        self.play(FadeIn(author_id), FadeIn(follow), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(mini_clk), FadeOut(pt_cards),
            FadeOut(author_id), FadeOut(follow),
            FadeOut(self.author), run_time=0.8
        )


# 渲染:
#   manim -pql half_hour_animation.py HalfHourAnimation
#   manim -qh  half_hour_animation.py HalfHourAnimation