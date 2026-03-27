"""
002_从不同方向观察物体.py — 从不同方向观察物体 教学动画

知识点: 从正面、侧面、后面、上面观察物体，辨认视图
年级: 二年级上册
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 介绍一个立体小房子
  3. 从正面（前面）观察
  4. 从侧面观察
  5. 从后面观察
  6. 从上面（俯视）观察
  7. 四视图汇总对比
  8. 互动小练习
  9. 总结
  10. 片尾
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
COLOR_FRONT = "#3b82f6"       # 蓝色 - 正面
COLOR_SIDE = "#f59e0b"        # 橙色 - 侧面
COLOR_BACK = "#22c55e"        # 绿色 - 后面
COLOR_TOP = "#a78bfa"         # 紫色 - 上面
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_HOUSE = "#e2e8f0"       # 浅灰 - 房子颜色
COLOR_ROOF = "#ef4444"        # 红色 - 屋顶
COLOR_DOOR = "#92400e"        # 棕色 - 门
COLOR_WINDOW = "#60a5fa"      # 浅蓝 - 窗户
COLOR_AUTHOR = "#6b7280"      # 灰色作者信息
FONT = "PingFang SC"


# ======================================================================
# Helper: build a simplified 3D-looking house as 2D VGroup
# ======================================================================

def build_house_3d(scale=1.0, center=ORIGIN):
    """
    Build a pseudo-3D house using 2D polygons (isometric style).
    Returns a VGroup with labeled sub-parts.
    """
    s = scale
    # ----- front face (rectangle) -----
    front_bl = np.array([-1.2, -1.2, 0]) * s + center
    front_br = np.array([1.2, -1.2, 0]) * s + center
    front_tr = np.array([1.2, 0.6, 0]) * s + center
    front_tl = np.array([-1.2, 0.6, 0]) * s + center

    front_face = Polygon(
        front_bl, front_br, front_tr, front_tl,
        fill_color=COLOR_HOUSE, fill_opacity=0.9,
        stroke_color=WHITE, stroke_width=2,
    )

    # ----- roof (triangle on top of front face) -----
    roof_peak = np.array([0, 1.6, 0]) * s + center
    roof = Polygon(
        front_tl, front_tr, roof_peak,
        fill_color=COLOR_ROOF, fill_opacity=0.9,
        stroke_color=WHITE, stroke_width=2,
    )

    # ----- side face (parallelogram to the right) -----
    depth = np.array([0.8, 0.5, 0]) * s
    side_bl = front_br
    side_br = front_br + depth
    side_tr = front_tr + depth
    side_tl = front_tr

    side_face = Polygon(
        side_bl, side_br, side_tr, side_tl,
        fill_color="#b0bec5", fill_opacity=0.85,
        stroke_color=WHITE, stroke_width=2,
    )

    # ----- side roof (parallelogram) -----
    side_roof = Polygon(
        front_tr, front_tr + depth, roof_peak + depth, roof_peak,
        fill_color="#c62828", fill_opacity=0.85,
        stroke_color=WHITE, stroke_width=2,
    )

    # ----- door on front face -----
    door_bl = np.array([-0.35, -1.2, 0]) * s + center
    door_br = np.array([0.35, -1.2, 0]) * s + center
    door_tr = np.array([0.35, -0.15, 0]) * s + center
    door_tl = np.array([-0.35, -0.15, 0]) * s + center
    door = Polygon(
        door_bl, door_br, door_tr, door_tl,
        fill_color=COLOR_DOOR, fill_opacity=1,
        stroke_color=WHITE, stroke_width=1.5,
    )

    # ----- window on front face (left) -----
    win_size = 0.30 * s
    win_center_l = np.array([-0.7, 0.1, 0]) * s + center
    window_l = Square(
        side_length=win_size * 2,
        fill_color=COLOR_WINDOW, fill_opacity=0.9,
        stroke_color=WHITE, stroke_width=1.5,
    ).move_to(win_center_l)

    # cross in window
    win_h = Line(
        win_center_l + LEFT * win_size,
        win_center_l + RIGHT * win_size,
        stroke_width=1, color=WHITE
    )
    win_v = Line(
        win_center_l + UP * win_size,
        win_center_l + DOWN * win_size,
        stroke_width=1, color=WHITE
    )
    window_l_group = VGroup(window_l, win_h, win_v)

    # ----- window on front face (right) -----
    win_center_r = np.array([0.7, 0.1, 0]) * s + center
    window_r = Square(
        side_length=win_size * 2,
        fill_color=COLOR_WINDOW, fill_opacity=0.9,
        stroke_color=WHITE, stroke_width=1.5,
    ).move_to(win_center_r)

    win_h2 = Line(
        win_center_r + LEFT * win_size,
        win_center_r + RIGHT * win_size,
        stroke_width=1, color=WHITE
    )
    win_v2 = Line(
        win_center_r + UP * win_size,
        win_center_r + DOWN * win_size,
        stroke_width=1, color=WHITE
    )
    window_r_group = VGroup(window_r, win_h2, win_v2)

    house = VGroup(
        side_face, side_roof,
        front_face, roof,
        door, window_l_group, window_r_group
    )
    return house


def build_front_view(scale=1.0, center=ORIGIN):
    """Front view of the house: rectangle + triangle roof + door + 2 windows."""
    s = scale
    # wall
    wall = Rectangle(
        width=2.4 * s, height=1.8 * s,
        fill_color=COLOR_HOUSE, fill_opacity=0.9,
        stroke_color=COLOR_FRONT, stroke_width=3,
    ).move_to(center + DOWN * 0.1 * s)

    # roof
    wall_top = wall.get_top()
    roof = Polygon(
        wall_top + LEFT * 1.2 * s,
        wall_top + RIGHT * 1.2 * s,
        wall_top + UP * 1.0 * s,
        fill_color=COLOR_ROOF, fill_opacity=0.9,
        stroke_color=COLOR_FRONT, stroke_width=3,
    )

    # door
    door = Rectangle(
        width=0.55 * s, height=0.85 * s,
        fill_color=COLOR_DOOR, fill_opacity=1,
        stroke_color=COLOR_FRONT, stroke_width=2,
    ).move_to(center + DOWN * 0.58 * s)

    # windows
    w = 0.45 * s
    win_l = Square(
        side_length=w,
        fill_color=COLOR_WINDOW, fill_opacity=0.9,
        stroke_color=COLOR_FRONT, stroke_width=2,
    ).move_to(center + LEFT * 0.72 * s + UP * 0.2 * s)

    win_r = Square(
        side_length=w,
        fill_color=COLOR_WINDOW, fill_opacity=0.9,
        stroke_color=COLOR_FRONT, stroke_width=2,
    ).move_to(center + RIGHT * 0.72 * s + UP * 0.2 * s)

    return VGroup(wall, roof, door, win_l, win_r)


def build_side_view(scale=1.0, center=ORIGIN):
    """Side view: narrower rectangle + triangle roof (no door, maybe 1 window)."""
    s = scale
    wall = Rectangle(
        width=1.4 * s, height=1.8 * s,
        fill_color="#b0bec5", fill_opacity=0.9,
        stroke_color=COLOR_SIDE, stroke_width=3,
    ).move_to(center + DOWN * 0.1 * s)

    wall_top = wall.get_top()
    roof = Polygon(
        wall_top + LEFT * 0.7 * s,
        wall_top + RIGHT * 0.7 * s,
        wall_top + UP * 1.0 * s,
        fill_color="#c62828", fill_opacity=0.9,
        stroke_color=COLOR_SIDE, stroke_width=3,
    )

    # small window
    w = 0.40 * s
    win = Square(
        side_length=w,
        fill_color=COLOR_WINDOW, fill_opacity=0.9,
        stroke_color=COLOR_SIDE, stroke_width=2,
    ).move_to(center + UP * 0.2 * s)

    return VGroup(wall, roof, win)


def build_back_view(scale=1.0, center=ORIGIN):
    """Back view: same as front but NO door, no windows (or small window)."""
    s = scale
    wall = Rectangle(
        width=2.4 * s, height=1.8 * s,
        fill_color=COLOR_HOUSE, fill_opacity=0.9,
        stroke_color=COLOR_BACK, stroke_width=3,
    ).move_to(center + DOWN * 0.1 * s)

    wall_top = wall.get_top()
    roof = Polygon(
        wall_top + LEFT * 1.2 * s,
        wall_top + RIGHT * 1.2 * s,
        wall_top + UP * 1.0 * s,
        fill_color=COLOR_ROOF, fill_opacity=0.9,
        stroke_color=COLOR_BACK, stroke_width=3,
    )

    # one small window in back
    w = 0.40 * s
    win = Square(
        side_length=w,
        fill_color=COLOR_WINDOW, fill_opacity=0.9,
        stroke_color=COLOR_BACK, stroke_width=2,
    ).move_to(center + UP * 0.2 * s)

    return VGroup(wall, roof, win)


def build_top_view(scale=1.0, center=ORIGIN):
    """Top (bird's eye) view: rectangle for the roof footprint."""
    s = scale
    # Roof from above looks like a rectangle with a ridge line
    outer = Rectangle(
        width=2.4 * s, height=1.6 * s,
        fill_color=COLOR_ROOF, fill_opacity=0.85,
        stroke_color=COLOR_TOP, stroke_width=3,
    ).move_to(center)

    # Ridge line down the middle
    ridge = DashedLine(
        center + UP * 0.8 * s,
        center + DOWN * 0.8 * s,
        color=COLOR_TOP, stroke_width=2, dash_length=0.1
    )

    return VGroup(outer, ridge)


# ======================================================================
# 主场景
# ======================================================================

class ObservingObjectsLesson(Scene):
    """
    从不同方向观察物体 教学动画
    场景顺序:
      1. 开场钩子
      2. 展示3D小房子
      3. 正面观察
      4. 侧面观察
      5. 后面观察
      6. 上面（俯视）观察
      7. 四视图汇总
      8. 互动小练习
      9. 总结
      10. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_show_house()
        self.scene_3_front_view()
        self.scene_4_side_view()
        self.scene_5_back_view()
        self.scene_6_top_view()
        self.scene_7_four_views_summary()
        self.scene_8_quiz()
        self.scene_9_summary()
        self.scene_10_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        # Author
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # Hook
        hook = Text(
            "同一个物体，",
            font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 4.5)
        hook2 = Text(
            "从不同方向看，一样吗?",
            font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 3.5)

        self.play(Write(hook), run_time=0.8)
        self.play(Write(hook2), run_time=0.8)
        self.wait(1.0)

        # Question mark
        qmark = Text("?", font=FONT, font_size=80, color=WHITE).move_to(UP * 1.0)
        self.play(FadeIn(qmark, scale=0.5), run_time=0.5)
        self.play(qmark.animate.scale(1.3), run_time=0.3)
        self.play(qmark.animate.scale(1 / 1.3), run_time=0.3)
        self.wait(0.5)

        self.play(FadeOut(hook), FadeOut(hook2), FadeOut(qmark), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 2: 展示3D小房子
    # ------------------------------------------------------------------
    def scene_2_show_house(self):
        title = Text(
            "先来认识这座小房子",
            font=FONT, font_size=32, color=WHITE
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # Build the 3D house
        self.house_3d = build_house_3d(scale=1.5, center=UP * 1.5)
        self.play(FadeIn(self.house_3d, shift=UP * 0.5), run_time=1.2)

        # Label parts
        label_door = Text("门", font=FONT, font_size=20, color=COLOR_DOOR).move_to(
            self.house_3d.get_center() + DOWN * 1.1 + LEFT * 0.0
        )
        label_window = Text("窗", font=FONT, font_size=20, color=COLOR_WINDOW).move_to(
            self.house_3d.get_center() + UP * 0.2 + LEFT * 1.3
        )
        label_roof = Text("屋顶", font=FONT, font_size=20, color=COLOR_ROOF).move_to(
            self.house_3d.get_center() + UP * 2.0
        )

        self.play(FadeIn(label_door), FadeIn(label_window), FadeIn(label_roof), run_time=0.6)
        self.wait(1.0)

        # Explain directions
        explain = Text(
            "我们从不同方向来看看它!",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(explain, shift=UP * 0.3), run_time=0.5)

        # Add direction arrows around house
        arrow_front = Arrow(
            self.house_3d.get_bottom() + DOWN * 1.5,
            self.house_3d.get_bottom() + DOWN * 0.3,
            color=COLOR_FRONT, stroke_width=4, buff=0.1
        )
        label_f = Text("前面", font=FONT, font_size=18, color=COLOR_FRONT).next_to(
            arrow_front, DOWN, buff=0.1
        )

        arrow_side = Arrow(
            self.house_3d.get_right() + RIGHT * 1.8,
            self.house_3d.get_right() + RIGHT * 0.3,
            color=COLOR_SIDE, stroke_width=4, buff=0.1
        )
        label_s = Text("侧面", font=FONT, font_size=18, color=COLOR_SIDE).next_to(
            arrow_side, RIGHT, buff=0.1
        )

        arrow_top = Arrow(
            self.house_3d.get_top() + UP * 1.5,
            self.house_3d.get_top() + UP * 0.3,
            color=COLOR_TOP, stroke_width=4, buff=0.1
        )
        label_t = Text("上面", font=FONT, font_size=18, color=COLOR_TOP).next_to(
            arrow_top, UP, buff=0.1
        )

        self.play(
            GrowArrow(arrow_front), FadeIn(label_f),
            GrowArrow(arrow_side), FadeIn(label_s),
            GrowArrow(arrow_top), FadeIn(label_t),
            run_time=0.8
        )
        self.wait(1.5)

        # Cleanup
        self.play(
            FadeOut(title), FadeOut(explain),
            FadeOut(label_door), FadeOut(label_window), FadeOut(label_roof),
            FadeOut(arrow_front), FadeOut(label_f),
            FadeOut(arrow_side), FadeOut(label_s),
            FadeOut(arrow_top), FadeOut(label_t),
            run_time=0.5
        )
        # Keep house for next scenes
        self.play(
            self.house_3d.animate.scale(0.7).move_to(UP * 5.0),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 3: 正面（前面）观察
    # ------------------------------------------------------------------
    def scene_3_front_view(self):
        title = Text(
            "从前面看", font=FONT, font_size=36, color=COLOR_FRONT
        ).move_to(UP * 3.0)

        subtitle = Text(
            "正面视图", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 2.3)

        self.play(Write(title), FadeIn(subtitle), run_time=0.6)

        # Eye icon on the front
        eye_pos = UP * 5.0 + DOWN * 2.5
        eye = Text("👁", font_size=36).move_to(eye_pos + DOWN * 3.0)
        arrow = Arrow(
            eye.get_top(), eye_pos + DOWN * 0.5,
            color=COLOR_FRONT, stroke_width=3, buff=0.1
        )
        self.play(FadeIn(eye), GrowArrow(arrow), run_time=0.6)

        # Show front view
        front_view = build_front_view(scale=1.3, center=DOWN * 1.5)
        front_border = SurroundingRectangle(
            front_view, color=COLOR_FRONT, buff=0.3, corner_radius=0.1
        )

        self.play(FadeIn(front_view, shift=UP * 0.3), run_time=1.0)
        self.play(Create(front_border), run_time=0.5)

        # Annotations
        note1 = Text(
            "能看到: 门、两扇窗、屋顶",
            font=FONT, font_size=22, color=WHITE
        ).move_to(DOWN * 4.5)
        note2 = Text(
            "宽宽的、有三角形屋顶",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(DOWN * 5.2)

        self.play(FadeIn(note1), FadeIn(note2), run_time=0.5)
        self.wait(2.0)

        # Cleanup
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(eye), FadeOut(arrow),
            FadeOut(front_view), FadeOut(front_border),
            FadeOut(note1), FadeOut(note2),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 侧面观察
    # ------------------------------------------------------------------
    def scene_4_side_view(self):
        title = Text(
            "从侧面看", font=FONT, font_size=36, color=COLOR_SIDE
        ).move_to(UP * 3.0)

        subtitle = Text(
            "侧面视图", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 2.3)

        self.play(Write(title), FadeIn(subtitle), run_time=0.6)

        # Eye on the side
        eye = Text("👁", font_size=36).move_to(RIGHT * 3.5 + UP * 0.5)
        arrow = Arrow(
            eye.get_left(), RIGHT * 1.5 + UP * 0.5,
            color=COLOR_SIDE, stroke_width=3, buff=0.1
        )
        self.play(FadeIn(eye), GrowArrow(arrow), run_time=0.6)

        # Show side view
        side_view = build_side_view(scale=1.3, center=DOWN * 1.5)
        side_border = SurroundingRectangle(
            side_view, color=COLOR_SIDE, buff=0.3, corner_radius=0.1
        )

        self.play(FadeIn(side_view, shift=UP * 0.3), run_time=1.0)
        self.play(Create(side_border), run_time=0.5)

        # Annotations
        note1 = Text(
            "能看到: 一面墙、一扇小窗",
            font=FONT, font_size=22, color=WHITE
        ).move_to(DOWN * 4.5)
        note2 = Text(
            "窄窄的、有三角形屋顶",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(DOWN * 5.2)

        self.play(FadeIn(note1), FadeIn(note2), run_time=0.5)
        self.wait(2.0)

        # Cleanup
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(eye), FadeOut(arrow),
            FadeOut(side_view), FadeOut(side_border),
            FadeOut(note1), FadeOut(note2),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 后面观察
    # ------------------------------------------------------------------
    def scene_5_back_view(self):
        title = Text(
            "从后面看", font=FONT, font_size=36, color=COLOR_BACK
        ).move_to(UP * 3.0)

        subtitle = Text(
            "背面视图", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 2.3)

        self.play(Write(title), FadeIn(subtitle), run_time=0.6)

        # Eye on the back (top of screen)
        eye = Text("👁", font_size=36).move_to(UP * 6.5)
        arrow = Arrow(
            eye.get_bottom(), UP * 5.5,
            color=COLOR_BACK, stroke_width=3, buff=0.1
        )
        self.play(FadeIn(eye), GrowArrow(arrow), run_time=0.6)

        # Show back view
        back_view = build_back_view(scale=1.3, center=DOWN * 1.5)
        back_border = SurroundingRectangle(
            back_view, color=COLOR_BACK, buff=0.3, corner_radius=0.1
        )

        self.play(FadeIn(back_view, shift=UP * 0.3), run_time=1.0)
        self.play(Create(back_border), run_time=0.5)

        # Annotations
        note1 = Text(
            "能看到: 一面墙、一扇小窗",
            font=FONT, font_size=22, color=WHITE
        ).move_to(DOWN * 4.5)
        note2 = Text(
            "没有门! 和正面不一样",
            font=FONT, font_size=20, color=COLOR_HL
        ).move_to(DOWN * 5.2)

        self.play(FadeIn(note1), FadeIn(note2), run_time=0.5)
        self.wait(2.0)

        # Cleanup
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(eye), FadeOut(arrow),
            FadeOut(back_view), FadeOut(back_border),
            FadeOut(note1), FadeOut(note2),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 俯视（上面）观察
    # ------------------------------------------------------------------
    def scene_6_top_view(self):
        title = Text(
            "从上面看", font=FONT, font_size=36, color=COLOR_TOP
        ).move_to(UP * 3.0)

        subtitle = Text(
            "俯视图", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 2.3)

        self.play(Write(title), FadeIn(subtitle), run_time=0.6)

        # Eye above
        eye = Text("👁", font_size=36).move_to(UP * 1.5)
        arrow = Arrow(
            eye.get_bottom(), DOWN * 0.3,
            color=COLOR_TOP, stroke_width=3, buff=0.1
        )
        self.play(FadeIn(eye), GrowArrow(arrow), run_time=0.6)

        # Show top view
        top_view = build_top_view(scale=1.3, center=DOWN * 2.0)
        top_border = SurroundingRectangle(
            top_view, color=COLOR_TOP, buff=0.3, corner_radius=0.1
        )

        self.play(FadeIn(top_view, shift=UP * 0.3), run_time=1.0)
        self.play(Create(top_border), run_time=0.5)

        # Annotations
        note1 = Text(
            "能看到: 屋顶是长方形",
            font=FONT, font_size=22, color=WHITE
        ).move_to(DOWN * 4.5)
        note2 = Text(
            "看不到门和窗!",
            font=FONT, font_size=20, color=COLOR_HL
        ).move_to(DOWN * 5.2)

        self.play(FadeIn(note1), FadeIn(note2), run_time=0.5)
        self.wait(2.0)

        # Cleanup
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(eye), FadeOut(arrow),
            FadeOut(top_view), FadeOut(top_border),
            FadeOut(note1), FadeOut(note2),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 7: 四个视图汇总
    # ------------------------------------------------------------------
    def scene_7_four_views_summary(self):
        # Remove the small 3D house
        self.play(FadeOut(self.house_3d), run_time=0.4)

        title = Text(
            "四个方向看到的样子",
            font=FONT, font_size=32, color=WHITE
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # Build 4 small views in a 2x2 grid
        sc = 0.65
        positions = [
            UP * 3.0 + LEFT * 2.0,   # top-left: front
            UP * 3.0 + RIGHT * 2.0,  # top-right: side
            DOWN * 0.5 + LEFT * 2.0,  # bottom-left: back
            DOWN * 0.5 + RIGHT * 2.0, # bottom-right: top
        ]

        front_v = build_front_view(scale=sc, center=positions[0])
        side_v = build_side_view(scale=sc, center=positions[1])
        back_v = build_back_view(scale=sc, center=positions[2])
        top_v = build_top_view(scale=sc, center=positions[3])

        labels = [
            Text("正面", font=FONT, font_size=22, color=COLOR_FRONT),
            Text("侧面", font=FONT, font_size=22, color=COLOR_SIDE),
            Text("后面", font=FONT, font_size=22, color=COLOR_BACK),
            Text("上面", font=FONT, font_size=22, color=COLOR_TOP),
        ]

        views = [front_v, side_v, back_v, top_v]
        colors = [COLOR_FRONT, COLOR_SIDE, COLOR_BACK, COLOR_TOP]
        borders = []

        for i, (view, label, pos, color) in enumerate(
            zip(views, labels, positions, colors)
        ):
            border = SurroundingRectangle(
                view, color=color, buff=0.2, corner_radius=0.08
            )
            borders.append(border)
            label.next_to(border, UP, buff=0.15)

            self.play(
                FadeIn(view, shift=UP * 0.2),
                Create(border),
                FadeIn(label),
                run_time=0.5
            )
            self.wait(0.3)

        # Emphasize difference
        note = Text(
            "同一个物体，不同方向看不一样!",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 4.0)
        self.play(FadeIn(note, shift=UP * 0.3), run_time=0.5)
        self.wait(2.5)

        # Cleanup
        all_items = VGroup(
            title, note,
            *views, *borders, *labels
        )
        self.play(FadeOut(all_items), run_time=0.6)

    # ------------------------------------------------------------------
    # Scene 8: 互动小练习
    # ------------------------------------------------------------------
    def scene_8_quiz(self):
        title = Text(
            "小练习", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.5)

        question = Text(
            "下面这幅图，是从哪个方向看到的?",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 5.0)
        self.play(FadeIn(question), run_time=0.5)

        # Show the side view as the quiz image
        quiz_view = build_side_view(scale=1.2, center=UP * 2.0)
        quiz_border = SurroundingRectangle(
            quiz_view, color=WHITE, buff=0.3, corner_radius=0.1
        )
        self.play(FadeIn(quiz_view), Create(quiz_border), run_time=0.8)

        # Options
        opt_a = Text("A. 前面", font=FONT, font_size=26, color=COLOR_FRONT).move_to(
            DOWN * 1.5 + LEFT * 2.0
        )
        opt_b = Text("B. 侧面", font=FONT, font_size=26, color=COLOR_SIDE).move_to(
            DOWN * 1.5 + RIGHT * 2.0
        )
        opt_c = Text("C. 上面", font=FONT, font_size=26, color=COLOR_TOP).move_to(
            DOWN * 2.8 + LEFT * 2.0
        )
        opt_d = Text("D. 后面", font=FONT, font_size=26, color=COLOR_BACK).move_to(
            DOWN * 2.8 + RIGHT * 2.0
        )

        self.play(
            FadeIn(opt_a), FadeIn(opt_b),
            FadeIn(opt_c), FadeIn(opt_d),
            run_time=0.6
        )
        self.wait(2.0)

        # Reveal answer
        think = Text(
            "3...2...1...", font=FONT, font_size=28, color=GRAY_A
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(think), run_time=0.3)
        self.wait(1.5)
        self.play(FadeOut(think), run_time=0.2)

        # Highlight correct answer
        answer_box = SurroundingRectangle(
            opt_b, color=COLOR_HL, buff=0.15, corner_radius=0.08
        )
        self.play(Create(answer_box), run_time=0.5)

        answer_text = Text(
            "窄窄的、没有门 = 侧面!",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(answer_text, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # Cleanup
        self.play(
            FadeOut(title), FadeOut(question),
            FadeOut(quiz_view), FadeOut(quiz_border),
            FadeOut(opt_a), FadeOut(opt_b),
            FadeOut(opt_c), FadeOut(opt_d),
            FadeOut(answer_box), FadeOut(answer_text),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 9: 总结
    # ------------------------------------------------------------------
    def scene_9_summary(self):
        title = Text(
            "总结", font=FONT, font_size=36, color=WHITE
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.5)

        # Summary points
        points_data = [
            ("1.", "观察物体要选好方向", WHITE),
            ("2.", "正面、侧面、后面、上面", WHITE),
            ("3.", "每个方向看到的形状不同", COLOR_HL),
            ("4.", "注意门、窗等特征的位置", COLOR_HL),
        ]

        point_groups = []
        for i, (num, txt, color) in enumerate(points_data):
            num_mob = Text(num, font=FONT, font_size=24, color=color)
            txt_mob = Text(txt, font=FONT, font_size=24, color=color)
            row = VGroup(num_mob, txt_mob).arrange(RIGHT, buff=0.2)
            row.move_to(UP * (3.5 - i * 1.2))
            point_groups.append(row)

        for pg in point_groups:
            self.play(FadeIn(pg, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        # Key takeaway box
        key_box = RoundedRectangle(
            width=7.5, height=1.8,
            corner_radius=0.2,
            fill_color="#16213e", fill_opacity=0.9,
            stroke_color=COLOR_HL, stroke_width=2,
        ).move_to(DOWN * 2.0)

        key_text = Text(
            "同一个物体,\n从不同方向看, 形状不一样!",
            font=FONT, font_size=26, color=COLOR_HL,
            line_spacing=1.3
        ).move_to(key_box.get_center())

        self.play(FadeIn(key_box), Write(key_text), run_time=0.8)

        # Mini icons
        mini_front = build_front_view(scale=0.35, center=DOWN * 4.5 + LEFT * 3.0)
        mini_side = build_side_view(scale=0.35, center=DOWN * 4.5 + LEFT * 1.0)
        mini_back = build_back_view(scale=0.35, center=DOWN * 4.5 + RIGHT * 1.0)
        mini_top = build_top_view(scale=0.35, center=DOWN * 4.5 + RIGHT * 3.0)

        self.play(
            FadeIn(mini_front), FadeIn(mini_side),
            FadeIn(mini_back), FadeIn(mini_top),
            run_time=0.6
        )
        self.wait(2.5)

        # Cleanup
        all_items = VGroup(
            title, key_box, key_text,
            mini_front, mini_side, mini_back, mini_top,
            *point_groups
        )
        self.play(FadeOut(all_items), run_time=0.6)

    # ------------------------------------------------------------------
    # Scene 10: 片尾
    # ------------------------------------------------------------------
    def scene_10_outro(self):
        author_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(
            Transform(self.author_mob, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow = Text(
            "关注我, 学更多数学知识!",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.6)

        # Decorative small shapes
        shapes = VGroup(
            Square(side_length=0.4, color=COLOR_FRONT, fill_opacity=0.8).move_to(
                DOWN * 3.0 + LEFT * 2.5
            ),
            Triangle(color=COLOR_ROOF, fill_opacity=0.8).scale(0.3).move_to(
                DOWN * 3.0 + LEFT * 1.0
            ),
            Circle(radius=0.25, color=COLOR_SIDE, fill_opacity=0.8).move_to(
                DOWN * 3.0 + RIGHT * 0.5
            ),
            Square(side_length=0.4, color=COLOR_BACK, fill_opacity=0.8).move_to(
                DOWN * 3.0 + RIGHT * 2.0
            ),
            Triangle(color=COLOR_TOP, fill_opacity=0.8).scale(0.3).move_to(
                DOWN * 3.0 + RIGHT * 3.5
            ),
        )
        self.play(*[FadeIn(s, scale=0.5) for s in shapes], run_time=0.6)
        self.wait(1.5)

        # Final fade
        self.play(
            FadeOut(self.author_mob), FadeOut(author_id),
            FadeOut(follow), FadeOut(shapes),
            run_time=1.0
        )


# 运行命令:
# manim -pql 002_从不同方向观察物体.py ObservingObjectsLesson  # 快速预览
# manim -qm 002_从不同方向观察物体.py ObservingObjectsLesson   # 中等质量
