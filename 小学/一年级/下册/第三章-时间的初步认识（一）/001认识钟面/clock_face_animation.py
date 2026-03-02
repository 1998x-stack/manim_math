"""
认识钟面 - 一年级时间初步认识
Clock Face Recognition Animation - Grade 1

知识点: 钟面结构 - 时针(短粗)、分针(长细)、12大格、60小格
格式: TikTok 竖屏 1080×1920
"""

from manim import *
import numpy as np

# ===== 全局配置 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ===== 颜色 =====
BG_COLOR      = "#1a1a2e"
COLOR_RIM     = "#c8a84b"   # 表圈金色
COLOR_FACE    = "#fdf6e3"   # 表盘米白
COLOR_NUMBER  = "#2c3e50"   # 数字深色
COLOR_TICK_BIG   = "#4a4a4a"
COLOR_TICK_SMALL = "#9a9a9a"
COLOR_HOUR_HAND  = "#1a237e"  # 时针深蓝（短粗）
COLOR_MIN_HAND   = "#c62828"  # 分针深红（长细）
COLOR_HIGHLIGHT  = "#f9ca24"
COLOR_LABEL_H    = "#1565c0"
COLOR_LABEL_M    = "#b71c1c"

AUTHOR_FONT = "Noto Sans CJK SC"

# ===== 钟面几何参数（已由 verify_clock_face.py 验证）=====
CLOCK_CENTER = np.array([0.0, 1.2, 0.0])
R = 2.8          # 表圈半径
R_NUM = 2.25     # 数字半径
R_BIG_OUT  = 2.8
R_BIG_IN   = 2.50
R_SML_OUT  = 2.8
R_SML_IN   = 2.65
HOUR_LEN   = 1.55
MIN_LEN    = 2.25


def clock_pos(hour_num, radius, center=CLOCK_CENTER):
    """
    将钟面小时数(0-12)转换为坐标。
    12在最上方，顺时针排列。
    angle = 90° - hour_num * 30°
    """
    angle_rad = np.radians(90.0 - hour_num * 30.0)
    return center + np.array([radius * np.cos(angle_rad),
                               radius * np.sin(angle_rad), 0.0])


def tick_line(i, n_total, r_out, r_in, center=CLOCK_CENTER, **kwargs):
    """创建第 i 个刻度线（共 n_total 个），从外到内"""
    angle_rad = np.radians(90.0 - i * (360.0 / n_total))
    outer = center + np.array([r_out * np.cos(angle_rad),
                                r_out * np.sin(angle_rad), 0.0])
    inner = center + np.array([r_in * np.cos(angle_rad),
                                r_in * np.sin(angle_rad), 0.0])
    return Line(outer, inner, **kwargs)


class ClockFaceAnimation(Scene):
    """认识钟面教学动画"""

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 作者信息（贯穿全程）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=AUTHOR_FONT, font_size=18, color=GRAY_B
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        # 预构建钟面元素（各场景复用）
        self._build_clock_parts()

        self.scene_1_hook()
        self.scene_2_face()
        self.scene_3_big_ticks()
        self.scene_4_small_ticks()
        self.scene_5_hands()
        self.scene_6_outro()

    # ─────────────────────────────────────────────
    # 预构建所有钟面元件（不添加到场景）
    # ─────────────────────────────────────────────
    def _build_clock_parts(self):
        cx = CLOCK_CENTER

        # 表圈
        self.clock_rim = Circle(
            radius=R, color=COLOR_RIM,
            stroke_width=10, fill_opacity=0
        ).move_to(cx)

        # 表盘
        self.clock_face = Circle(
            radius=R - 0.05, color=COLOR_FACE,
            fill_opacity=1.0, stroke_width=0
        ).move_to(cx)

        # 12个数字
        self.clock_nums = VGroup()
        num_texts = ["12","1","2","3","4","5","6","7","8","9","10","11"]
        for i, txt in enumerate(num_texts):
            pos = clock_pos(i, R_NUM)
            num = Text(txt, font=AUTHOR_FONT, font_size=28,
                       color=COLOR_NUMBER, weight=BOLD)
            num.move_to(pos)
            self.clock_nums.add(num)

        # 中心点
        self.clock_center_dot = Dot(cx, radius=0.12, color=COLOR_TICK_BIG)

        # 12个大刻度
        self.big_ticks = VGroup(*[
            tick_line(i, 12, R_BIG_OUT, R_BIG_IN,
                      stroke_width=4, color=COLOR_TICK_BIG)
            for i in range(12)
        ])

        # 60个小刻度（跳过大刻度位置，仅绘制非5的倍数）
        self.small_ticks = VGroup(*[
            tick_line(i, 60, R_SML_OUT, R_SML_IN,
                      stroke_width=2, color=COLOR_TICK_SMALL)
            for i in range(60) if i % 5 != 0
        ])

        # 时针（初始指向12 = UP方向，由圆心向上）
        self.hour_hand = Line(
            cx, cx + np.array([0, HOUR_LEN, 0]),
            stroke_width=11, color=COLOR_HOUR_HAND,
            stroke_linecap=CapStyleType.ROUND
        )
        # 加圆头（视觉感）
        self.hour_tip = Dot(cx + np.array([0, HOUR_LEN, 0]),
                            radius=0.13, color=COLOR_HOUR_HAND)

        # 分针（初始指向12）
        self.min_hand = Line(
            cx, cx + np.array([0, MIN_LEN, 0]),
            stroke_width=5, color=COLOR_MIN_HAND,
            stroke_linecap=CapStyleType.ROUND
        )
        self.min_tip = Dot(cx + np.array([0, MIN_LEN, 0]),
                           radius=0.07, color=COLOR_MIN_HAND)

        # 中心圆帽（覆盖指针根部）
        self.center_cap = Dot(cx, radius=0.15, color=COLOR_RIM)

        # 完整时钟组（包含所有可见元件）
        self.full_clock = VGroup(
            self.clock_face, self.clock_rim,
            self.big_ticks, self.small_ticks,
            self.clock_nums, self.clock_center_dot,
            self.hour_hand, self.min_hand,
            self.center_cap
        )

    # ─────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────
    def scene_1_hook(self):
        hook_q = Text(
            "你认识钟表吗？",
            font=AUTHOR_FONT, font_size=54, color=COLOR_HIGHLIGHT
        ).move_to(UP * 5.3)

        self.play(Write(hook_q), run_time=0.9)

        # 快速显示时钟轮廓（预告）
        preview_clock = VGroup(
            self.clock_face.copy().set_fill(opacity=0.6),
            self.clock_rim.copy()
        )
        self.play(FadeIn(preview_clock, scale=0.5), run_time=0.7)
        self.wait(0.4)

        hook_a = Text(
            "今天认识钟面！",
            font=AUTHOR_FONT, font_size=44, color=WHITE
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(hook_a, shift=UP * 0.4), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(hook_q), FadeOut(hook_a),
                  FadeOut(preview_clock), run_time=0.5)

    # ─────────────────────────────────────────────
    # Scene 2: 钟面整体出现
    # ─────────────────────────────────────────────
    def scene_2_face(self):
        title = Text(
            "认识钟面", font=AUTHOR_FONT,
            font_size=44, color=COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 表圈+表盘
        self.play(
            Create(self.clock_rim),
            FadeIn(self.clock_face),
            run_time=0.9
        )

        # 12个数字顺时针依次出现
        self.play(
            LaggedStart(
                *[FadeIn(n, scale=0.4) for n in self.clock_nums],
                lag_ratio=0.12
            ),
            run_time=1.6
        )

        desc = Text(
            "这就是钟面！",
            font=AUTHOR_FONT, font_size=36, color=WHITE
        ).move_to(DOWN * 4.2)
        self.play(FadeIn(desc, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(desc), FadeOut(title), run_time=0.4)

    # ─────────────────────────────────────────────
    # Scene 3: 12个大格
    # ─────────────────────────────────────────────
    def scene_3_big_ticks(self):
        title = Text(
            "12 个大格",
            font=AUTHOR_FONT, font_size=40, color=COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # 大刻度出现
        self.play(
            LaggedStart(
                *[Create(t) for t in self.big_ticks],
                lag_ratio=0.08
            ),
            run_time=1.0
        )

        # 依次高亮12个扇形区域（顺时针，用弧段）
        sector_anims = []
        sector_arcs = VGroup()
        for i in range(12):
            start_ang = np.radians(90.0 - i * 30.0)
            end_ang   = np.radians(90.0 - (i + 1) * 30.0)
            arc = Arc(
                radius=(R_BIG_IN + R_NUM) / 2,
                start_angle=end_ang,
                angle=np.radians(30.0),
                arc_center=CLOCK_CENTER,
                stroke_width=18,
                color=COLOR_HIGHLIGHT,
                stroke_opacity=0.5
            )
            sector_arcs.add(arc)

        self.play(
            LaggedStart(
                *[Create(a) for a in sector_arcs],
                lag_ratio=0.15
            ),
            run_time=2.0
        )

        # 计数文字
        count_label = VGroup(
            Text("共 ", font=AUTHOR_FONT, font_size=34, color=WHITE),
            Text("12", font=AUTHOR_FONT, font_size=40, color=COLOR_HIGHLIGHT, weight=BOLD),
            Text(" 个大格", font=AUTHOR_FONT, font_size=34, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 4.0)

        self.play(Write(count_label), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(sector_arcs),
            FadeOut(count_label),
            FadeOut(title),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 4: 60个小格
    # ─────────────────────────────────────────────
    def scene_4_small_ticks(self):
        title = Text(
            "60 个小格",
            font=AUTHOR_FONT, font_size=40, color=COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # 小刻度出现
        self.play(
            LaggedStart(
                *[Create(t) for t in self.small_ticks],
                lag_ratio=0.01
            ),
            run_time=1.0
        )

        # 放大显示 12→1 段（5个小格）
        zoom_label = Text(
            "12 到 1 之间有几个小格？",
            font=AUTHOR_FONT, font_size=30, color=YELLOW
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(zoom_label, shift=UP * 0.2), run_time=0.5)

        # 高亮 12→1 段的5个小刻度
        highlight_small = VGroup(*[
            tick_line(i, 60, R_SML_OUT, R_SML_IN,
                      stroke_width=5, color=YELLOW)
            for i in range(1, 5)
        ])
        self.play(Create(highlight_small), run_time=0.6)

        # 弧段覆盖提示
        arc_zoom = Arc(
            radius=(R_SML_IN + R_BIG_IN) / 2,
            start_angle=np.radians(90.0 - 30.0),  # 1点
            angle=np.radians(30.0),                # 到12点
            arc_center=CLOCK_CENTER,
            stroke_width=20,
            color=YELLOW,
            stroke_opacity=0.4
        )
        self.play(Create(arc_zoom), run_time=0.5)

        count_5 = VGroup(
            Text("5 个小格", font=AUTHOR_FONT, font_size=34, color=YELLOW, weight=BOLD),
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(count_5), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(arc_zoom),
            FadeOut(highlight_small),
            FadeOut(zoom_label),
            FadeOut(count_5),
            run_time=0.4
        )

        # 总结
        formula_group = VGroup(
            Text("12 个大格  ×  5 = ", font=AUTHOR_FONT, font_size=30, color=WHITE),
            Text("60", font=AUTHOR_FONT, font_size=38, color=COLOR_HIGHLIGHT, weight=BOLD),
            Text(" 个小格", font=AUTHOR_FONT, font_size=30, color=WHITE),
        ).arrange(RIGHT, buff=0.08).move_to(DOWN * 4.0)

        self.play(Write(formula_group), run_time=1.0)
        self.play(Flash(formula_group[1], color=COLOR_HIGHLIGHT, flash_radius=0.7), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(formula_group), FadeOut(title), run_time=0.4)

    # ─────────────────────────────────────────────
    # Scene 5: 认识时针与分针
    # ─────────────────────────────────────────────
    def scene_5_hands(self):
        title = Text(
            "认识指针",
            font=AUTHOR_FONT, font_size=40, color=COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        cx = CLOCK_CENTER

        # ── 时针出现 ──
        self.play(
            Create(self.hour_hand),
            FadeIn(self.clock_center_dot),
            run_time=0.7
        )

        # 标注"时针"
        h_label = VGroup(
            Text("时针", font=AUTHOR_FONT, font_size=32,
                 color=COLOR_LABEL_H, weight=BOLD),
            Text("  短  •  粗", font=AUTHOR_FONT, font_size=26,
                 color=COLOR_LABEL_H),
        ).arrange(DOWN, buff=0.1).move_to(np.array([-3.0, -3.5, 0]))

        h_arrow = Arrow(
            start=h_label.get_right() + RIGHT * 0.1,
            end=cx + np.array([0.3, HOUR_LEN * 0.7, 0]),
            color=COLOR_LABEL_H, stroke_width=3,
            max_tip_length_to_length_ratio=0.25
        )

        self.play(
            FadeIn(h_label, shift=RIGHT * 0.3),
            Create(h_arrow),
            self.hour_hand.animate.set_stroke(color=COLOR_LABEL_H),
            run_time=0.7
        )
        self.wait(1.2)

        # ── 分针出现 ──
        self.play(
            Create(self.min_hand),
            run_time=0.7
        )

        m_label = VGroup(
            Text("分针", font=AUTHOR_FONT, font_size=32,
                 color=COLOR_LABEL_M, weight=BOLD),
            Text("  长  •  细", font=AUTHOR_FONT, font_size=26,
                 color=COLOR_LABEL_M),
        ).arrange(DOWN, buff=0.1).move_to(np.array([3.0, -3.5, 0]))

        m_arrow = Arrow(
            start=m_label.get_left() - RIGHT * 0.1,
            end=cx + np.array([0.2, MIN_LEN * 0.8, 0]),
            color=COLOR_LABEL_M, stroke_width=3,
            max_tip_length_to_length_ratio=0.25
        )

        self.play(
            FadeIn(m_label, shift=LEFT * 0.3),
            Create(m_arrow),
            self.min_hand.animate.set_stroke(color=COLOR_LABEL_M),
            run_time=0.7
        )
        # 恢复颜色
        self.play(
            self.hour_hand.animate.set_stroke(color=COLOR_HOUR_HAND),
            self.min_hand.animate.set_stroke(color=COLOR_MIN_HAND),
            run_time=0.3
        )
        self.wait(1.0)

        # ── 对比表格 ──
        self.play(
            FadeOut(h_arrow), FadeOut(m_arrow),
            FadeOut(h_label), FadeOut(m_label),
            run_time=0.4
        )

        # 对比卡片
        compare_bg = RoundedRectangle(
            corner_radius=0.3, width=7.8, height=2.2,
            fill_color="#0d1b2a", fill_opacity=1.0,
            stroke_color=GRAY_B, stroke_width=2
        ).move_to(np.array([0, -4.4, 0]))

        # 表头
        header = VGroup(
            Text("", font=AUTHOR_FONT, font_size=22, color=GRAY_A),
            Text("时针", font=AUTHOR_FONT, font_size=26,
                 color=COLOR_HOUR_HAND, weight=BOLD),
            Text("分针", font=AUTHOR_FONT, font_size=26,
                 color=COLOR_MIN_HAND, weight=BOLD),
        ).arrange(RIGHT, buff=0.8).move_to(np.array([0, -3.8, 0]))

        divider = Line(
            np.array([-3.7, -4.2, 0]),
            np.array([3.7, -4.2, 0]),
            stroke_width=1, color=GRAY_B
        )

        row1 = VGroup(
            Text("长短", font=AUTHOR_FONT, font_size=24, color=GRAY_B),
            Text("短", font=AUTHOR_FONT, font_size=28, color=COLOR_HOUR_HAND),
            Text("长", font=AUTHOR_FONT, font_size=28, color=COLOR_MIN_HAND),
        ).arrange(RIGHT, buff=0.95).move_to(np.array([0.1, -4.6, 0]))

        row2 = VGroup(
            Text("粗细", font=AUTHOR_FONT, font_size=24, color=GRAY_B),
            Text("粗", font=AUTHOR_FONT, font_size=28, color=COLOR_HOUR_HAND),
            Text("细", font=AUTHOR_FONT, font_size=28, color=COLOR_MIN_HAND),
        ).arrange(RIGHT, buff=0.95).move_to(np.array([0.1, -5.2, 0]))

        self.play(
            FadeIn(compare_bg),
            FadeIn(header),
            Create(divider),
            run_time=0.5
        )
        self.play(FadeIn(row1), FadeIn(row2), run_time=0.5)
        self.wait(0.8)

        # ── 时针转一圈演示 ──
        demo_text = Text(
            "时针走 1 圈 = 12 小时",
            font=AUTHOR_FONT, font_size=28, color=COLOR_HOUR_HAND
        ).move_to(np.array([0, -6.4, 0]))
        self.play(FadeIn(demo_text), run_time=0.4)

        # 时针顺时针转一圈（rotate -2π 绕圆心）
        # 使用 Rotate 绕 CLOCK_CENTER 旋转
        self.play(
            Rotate(self.hour_hand, angle=-2 * PI,
                   about_point=CLOCK_CENTER, run_time=2.5, rate_func=linear)
        )

        self.play(FadeOut(demo_text), run_time=0.3)

        # ── 分针转一圈演示 ──
        demo_text2 = Text(
            "分针走 1 圈 = 60 分钟",
            font=AUTHOR_FONT, font_size=28, color=COLOR_MIN_HAND
        ).move_to(np.array([0, -6.4, 0]))
        self.play(FadeIn(demo_text2), run_time=0.4)

        self.play(
            Rotate(self.min_hand, angle=-2 * PI,
                   about_point=CLOCK_CENTER, run_time=2.5, rate_func=linear)
        )

        self.play(FadeOut(demo_text2), run_time=0.3)
        self.wait(0.5)

        # 中心圆帽
        self.play(FadeIn(self.center_cap), run_time=0.3)

        # 清场
        self.play(
            FadeOut(compare_bg),
            FadeOut(header),
            FadeOut(divider),
            FadeOut(row1),
            FadeOut(row2),
            FadeOut(title),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 6: 总结 + 片尾
    # ─────────────────────────────────────────────
    def scene_6_outro(self):
        # 缩小钟面放到左上角
        clock_small = VGroup(
            self.clock_face, self.clock_rim,
            self.big_ticks, self.small_ticks,
            self.clock_nums, self.clock_center_dot,
            self.hour_hand, self.min_hand,
            self.center_cap
        )
        self.play(
            clock_small.animate.scale(0.45).move_to(np.array([0, 3.8, 0])),
            run_time=0.8
        )

        # 知识要点
        points_data = [
            ("①", "钟面有 12 个数字", COLOR_HIGHLIGHT),
            ("②", "有 12 个大格", "#2ecc71"),
            ("③", "有 60 个小格", "#3498db"),
            ("④", "时针：短 + 粗", COLOR_HOUR_HAND),
            ("⑤", "分针：长 + 细", COLOR_MIN_HAND),
        ]

        cards = VGroup()
        for num, text, color in points_data:
            bg = RoundedRectangle(
                corner_radius=0.25, width=7.2, height=0.82,
                fill_color="#0d1b2a", fill_opacity=1.0,
                stroke_color=color, stroke_width=2
            )
            num_t = Text(num, font=AUTHOR_FONT, font_size=26,
                         color=color, weight=BOLD)
            txt_t = Text(text, font=AUTHOR_FONT, font_size=24, color=WHITE)
            row = VGroup(num_t, txt_t).arrange(RIGHT, buff=0.35)
            row.move_to(bg.get_center())
            cards.add(VGroup(bg, row))

        cards.arrange(DOWN, buff=0.22)
        cards.move_to(np.array([0, 0.0, 0]))

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.3)

        self.wait(0.6)

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=AUTHOR_FONT, font_size=32, color=WHITE
        ).move_to(np.array([0, -3.5, 0]))
        author_id = Text(
            "@emptyandcalm",
            font=AUTHOR_FONT, font_size=26, color=GRAY_B
        ).move_to(np.array([0, -4.4, 0]))
        follow = Text(
            "关注我，学更多小学数学！",
            font=AUTHOR_FONT, font_size=28, color=COLOR_HIGHLIGHT
        ).move_to(np.array([0, -5.5, 0]))

        self.play(
            Transform(self.author, author_big),
            run_time=0.5
        )
        self.play(FadeIn(author_id), FadeIn(follow), run_time=0.5)

        # 小时钟动画装饰
        deco_clock = Circle(
            radius=0.35, color=COLOR_RIM,
            stroke_width=4, fill_color=COLOR_FACE, fill_opacity=0.9
        ).move_to(np.array([-3.5, -6.2, 0]))
        deco_h = Line(
            np.array([-3.5, -6.2, 0]),
            np.array([-3.5, -5.9, 0]),
            stroke_width=5, color=COLOR_HOUR_HAND
        )
        deco_m = Line(
            np.array([-3.5, -6.2, 0]),
            np.array([-3.5, -5.85, 0]),
            stroke_width=3, color=COLOR_MIN_HAND
        )
        self.play(
            FadeIn(deco_clock), FadeIn(deco_h), FadeIn(deco_m),
            run_time=0.4
        )
        self.play(
            Rotate(deco_m, angle=-2 * PI,
                   about_point=np.array([-3.5, -6.2, 0]),
                   run_time=1.5, rate_func=linear)
        )

        self.wait(1.0)

        self.play(
            FadeOut(clock_small), FadeOut(cards),
            FadeOut(author_id), FadeOut(follow),
            FadeOut(self.author), FadeOut(deco_clock),
            FadeOut(deco_h), FadeOut(deco_m),
            run_time=1.0
        )


# 渲染命令:
#   快速预览: manim -pql clock_face_animation.py ClockFaceAnimation
#   高质量:   manim -qh  clock_face_animation.py ClockFaceAnimation