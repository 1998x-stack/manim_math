"""
圆锥 (Cone) 3D 教学动画
知识点: 圆锥的定义、母线、侧面展开图、完整公式体系
目标受众: 高三学生
格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ── 全局配置 (TikTok 竖屏) ───────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ── 统一颜色方案 ─────────────────────────────────────────
BG_COLOR        = "#1a1a2e"
CONE_COLOR      = "#4ecdc4"
APEX_COLOR      = "#f7dc6f"
BASE_COLOR      = "#85c1e9"
SLANT_COLOR     = "#f39c12"
AXIS_COLOR      = "#a9cce3"
HIGHLIGHT_COLOR = "#ff6b6b"
FORMULA_COLOR   = "#d5f5e3"
SECTOR_COLOR    = "#bb8fce"


# ─────────────────────────────────────────────────────────
#  辅助: 精确几何计算
# ─────────────────────────────────────────────────────────
def cone_params(r, h):
    """返回 (l, theta_rad, theta_deg) — 所有派生量统一计算"""
    l         = np.sqrt(r**2 + h**2)
    theta_rad = 2 * PI * r / l        # 展开扇形圆心角 (弧度)
    theta_deg = np.degrees(theta_rad)
    return l, theta_rad, theta_deg


def verify_cone(r, h):
    """verify_geometry: 验证圆锥几何参数"""
    l, theta_rad, theta_deg = cone_params(r, h)
    arc_len = l * theta_rad
    expected_arc = 2 * PI * r
    assert abs(arc_len - expected_arc) < 1e-8, \
        f"弧长验证失败: {arc_len:.6f} ≠ {expected_arc:.6f}"
    assert 0 < theta_deg < 360, \
        f"扇形角度超出范围: {theta_deg:.2f}°"
    print(f"[✓] 圆锥验证通过 | r={r}, h={h} | l={l:.4f}, θ={theta_deg:.2f}°")
    return l, theta_rad, theta_deg


def verify_boundaries(positions, frame_w=9, frame_h=16, margin=0.4):
    """verify_boundaries: 检查所有标注点是否在安全边界内"""
    MAX_X = frame_w/2 - margin
    MAX_Y = frame_h/2 - margin
    for name, pos in positions.items():
        x, y = pos[0], pos[1]
        ok = abs(x) <= MAX_X and abs(y) <= MAX_Y
        status = "✓" if ok else "⚠ 越界!"
        print(f"  [{status}] {name}: ({x:.2f}, {y:.2f})")


# ── 全局几何常量 ─────────────────────────────────────────
R, H = 1.5, 2.6
L, THETA_RAD, THETA_DEG = verify_cone(R, H)

APEX_PT   = np.array([0,  H, 0])
BASE_C_PT = np.array([0,  0, 0])
RIM_PT    = np.array([R,  0, 0])


# ─────────────────────────────────────────────────────────
#  Scene 1 ── 开场钩子
# ─────────────────────────────────────────────────────────
class ConeScene1_Opening(ThreeDScene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # 作者信息 (固定在画面)
        author = Text("上海初高中数学直通车 @emptyandcalm",
                      font="Noto Sans CJK SC", font_size=18, color=GRAY_B)
        author.move_to(UP * 7.4)
        self.add_fixed_in_frame_mobjects(author)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)

        # 大标题
        title = Text("认识圆锥",
                     font="Noto Sans CJK SC", font_size=56, color=APEX_COLOR)
        sub = Text("母线 · 侧面积 · 展开图",
                   font="Noto Sans CJK SC", font_size=28, color=GRAY_A)
        title_grp = VGroup(title, sub).arrange(DOWN, buff=0.45)
        title_grp.move_to(UP * 5.3)
        self.add_fixed_in_frame_mobjects(title_grp)
        self.play(Write(title), run_time=0.9)
        self.play(FadeIn(sub), run_time=0.4)

        # 3-D 圆锥登场
        self.set_camera_orientation(phi=70 * DEGREES, theta=-60 * DEGREES)
        cone = Cone(base_radius=1.6, height=2.8, direction=UP,
                    fill_color=CONE_COLOR, fill_opacity=0.55,
                    stroke_color=CONE_COLOR, stroke_width=1.5)
        cone.shift(DOWN * 0.5)
        self.play(Create(cone), run_time=1.4)

        # 慢速旋转展示立体感
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(2.0)
        self.stop_ambient_camera_rotation()

        # 钩子问句
        hook = Text("冰淇淋筒展开后是什么形状?",
                    font="Noto Sans CJK SC", font_size=28,
                    color=HIGHLIGHT_COLOR)
        hook.move_to(DOWN * 5.5)
        self.add_fixed_in_frame_mobjects(hook)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(cone), FadeOut(hook),
                  FadeOut(title_grp), FadeOut(author), run_time=0.5)


# ─────────────────────────────────────────────────────────
#  Scene 2 ── 定义: 旋转生成圆锥
# ─────────────────────────────────────────────────────────
class ConeScene2_Definition(ThreeDScene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.set_camera_orientation(phi=65 * DEGREES, theta=-55 * DEGREES)

        # 标题
        title = Text("圆锥的定义",
                     font="Noto Sans CJK SC", font_size=42, color=APEX_COLOR)
        title.move_to(UP * 6.8)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title), run_time=0.4)

        # ── 旋转轴 ──
        axis = Arrow3D(start=np.array([0, -0.4, 0]),
                       end=np.array([0, H + 0.5, 0]),
                       color=AXIS_COLOR, thickness=0.022)
        axis_lbl = Text("旋转轴", font="Noto Sans CJK SC",
                        font_size=22, color=AXIS_COLOR)
        axis_lbl.move_to(UP * 4.0 + RIGHT * 1.8)
        self.add_fixed_in_frame_mobjects(axis_lbl)
        self.play(Create(axis), FadeIn(axis_lbl), run_time=0.7)

        # ── 直角三角形 ──
        tri = Polygon(BASE_C_PT, RIM_PT, APEX_PT,
                      stroke_color=WHITE, stroke_width=2.5,
                      fill_color=BLUE_E, fill_opacity=0.32)
        self.play(Create(tri), run_time=0.9)

        # 标注三边
        h_lbl = Text("h", font="Noto Sans CJK SC", font_size=22, color=AXIS_COLOR)
        h_lbl.move_to(LEFT * 0.4 + UP * 1.3)
        r_lbl = Text("r", font="Noto Sans CJK SC", font_size=22, color=BASE_COLOR)
        r_lbl.move_to(RIGHT * 0.75 + DOWN * 0.3)
        l_lbl = Text("l (母线)", font="Noto Sans CJK SC", font_size=22, color=SLANT_COLOR)
        l_lbl.move_to(RIGHT * 1.15 + UP * 1.45)
        self.add_fixed_in_frame_mobjects(h_lbl, r_lbl, l_lbl)

        # 母线高亮
        slant = Line3D(start=APEX_PT, end=RIM_PT,
                       color=SLANT_COLOR, thickness=0.025)
        self.play(FadeIn(h_lbl), FadeIn(r_lbl), run_time=0.5)
        self.play(Create(slant), FadeIn(l_lbl), run_time=0.6)

        # 说明文字
        explain = Text("以直角边所在直线为轴，旋转一周",
                       font="Noto Sans CJK SC", font_size=22, color=GRAY_A)
        explain.move_to(DOWN * 5.0)
        self.add_fixed_in_frame_mobjects(explain)
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(0.8)

        # ── 旋转动画 ──
        rotating_lbl = Text("旋转一周 →",
                            font="Noto Sans CJK SC", font_size=26,
                            color=HIGHLIGHT_COLOR)
        rotating_lbl.move_to(DOWN * 5.0)
        self.add_fixed_in_frame_mobjects(rotating_lbl)
        self.play(FadeOut(explain), FadeIn(rotating_lbl), run_time=0.3)
        self.play(Rotate(tri, angle=2 * PI, axis=UP,
                         about_point=ORIGIN, run_time=2.2, rate_func=smooth))

        # ── 圆锥登场 ──
        cone = Cone(base_radius=R, height=H, direction=UP,
                    fill_color=CONE_COLOR, fill_opacity=0.50,
                    stroke_color=CONE_COLOR, stroke_width=1.2)
        cone.shift(UP * (H / 2))
        self.play(
            Create(cone),
            FadeOut(tri), FadeOut(slant), FadeOut(rotating_lbl),
            run_time=1.2
        )

        # 标注各部分
        apex_dot = Sphere(radius=0.09, color=APEX_COLOR).move_to(APEX_PT)
        base_dot = Sphere(radius=0.07, color=BASE_COLOR).move_to(BASE_C_PT)
        self.play(FadeIn(apex_dot), FadeIn(base_dot), run_time=0.4)

        parts = [
            ("顶点", APEX_PT + np.array([0.5, 0.3, 0]),   APEX_COLOR),
            ("底面", BASE_C_PT + np.array([0.6, -0.4, 0]), BASE_COLOR),
            ("轴",   np.array([-0.7, H / 2, 0]),           AXIS_COLOR),
        ]
        for txt, pos, col in parts:
            lbl = Text(txt, font="Noto Sans CJK SC", font_size=20, color=col)
            lbl.move_to(pos)
            self.add_fixed_in_frame_mobjects(lbl)
            self.play(FadeIn(lbl), run_time=0.3)

        self.wait(1.6)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# ─────────────────────────────────────────────────────────
#  Scene 3 ── 母线: 定义与公式
# ─────────────────────────────────────────────────────────
class ConeScene3_Slant(ThreeDScene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.set_camera_orientation(phi=68 * DEGREES, theta=-50 * DEGREES)

        title = Text("母线 l",
                     font="Noto Sans CJK SC", font_size=42, color=SLANT_COLOR)
        title.move_to(UP * 6.8)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title), run_time=0.4)

        # 圆锥
        cone = Cone(base_radius=R, height=H, direction=UP,
                    fill_color=CONE_COLOR, fill_opacity=0.40,
                    stroke_color=CONE_COLOR, stroke_width=1.2)
        cone.shift(UP * (H / 2))
        self.play(Create(cone), run_time=1.0)

        # ── 展示多条母线 ──
        N_LINES = 10
        slant_lines = VGroup(*[
            Line3D(
                start=np.array([0, H, 0]),
                end=np.array([R * np.cos(2*PI*i/N_LINES), 0,
                              R * np.sin(2*PI*i/N_LINES)]),
                color=SLANT_COLOR, thickness=0.018
            )
            for i in range(N_LINES)
        ])
        self.play(Create(slant_lines), run_time=1.3)

        explain = Text("顶点到底面圆周上任意一点的线段均为母线",
                       font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        explain.move_to(DOWN * 4.8)
        self.add_fixed_in_frame_mobjects(explain)
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.0)

        # ── 母线公式 ──
        formula_lbl = Text("母线公式:",
                           font="Noto Sans CJK SC", font_size=24, color=WHITE)
        formula_lbl.move_to(DOWN * 6.2 + LEFT * 1.3)
        formula_tex = MathTex(r"l = \sqrt{r^2 + h^2}",
                              font_size=38, color=SLANT_COLOR)
        formula_tex.next_to(formula_lbl, RIGHT, buff=0.3)
        self.add_fixed_in_frame_mobjects(formula_lbl, formula_tex)
        self.play(FadeOut(explain), Write(formula_lbl), Write(formula_tex), run_time=0.9)

        # 旋转欣赏
        self.begin_ambient_camera_rotation(rate=0.28)
        self.wait(2.5)
        self.stop_ambient_camera_rotation()

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# ─────────────────────────────────────────────────────────
#  Scene 4 ── 侧面展开图 (2-D 扇形, 精确几何)
# ─────────────────────────────────────────────────────────
class ConeScene4_Unroll(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── 标题 ──
        title = Text("侧面展开图 — 扇形",
                     font="Noto Sans CJK SC", font_size=36, color=SECTOR_COLOR)
        title.move_to(UP * 6.5)
        self.play(FadeIn(title), run_time=0.4)

        # ── 左: 圆锥轮廓 (2-D) ──
        CONE_SCALE = 1.05
        cone_apex   = np.array([0,  0, 0])
        cone_left   = np.array([-CONE_SCALE, -2.0 * CONE_SCALE, 0])
        cone_right  = np.array([ CONE_SCALE, -2.0 * CONE_SCALE, 0])
        cone_base_c = (cone_left + cone_right) / 2

        cone_outline = VGroup(
            Line(cone_apex, cone_left,  color=CONE_COLOR,  stroke_width=2.5),
            Line(cone_apex, cone_right, color=CONE_COLOR,  stroke_width=2.5),
            Arc(radius=CONE_SCALE, start_angle=PI, angle=PI,
                arc_center=cone_base_c, color=BASE_COLOR, stroke_width=2.0),
        ).move_to(LEFT * 3.0 + UP * 2.8)

        cone_r_lbl = MathTex("r", font_size=28, color=BASE_COLOR)
        cone_r_lbl.move_to(LEFT * 2.3 + UP * 0.6)
        cone_h_lbl = MathTex("h", font_size=28, color=AXIS_COLOR)
        cone_h_lbl.move_to(LEFT * 3.8 + UP * 1.6)
        cone_l_lbl = MathTex("l", font_size=28, color=SLANT_COLOR)
        cone_l_lbl.move_to(LEFT * 2.1 + UP * 2.5)

        self.play(Create(cone_outline), run_time=0.8)
        self.play(Write(cone_r_lbl), Write(cone_h_lbl), Write(cone_l_lbl), run_time=0.5)

        # 剪开箭头
        arrow = Arrow(LEFT * 0.2 + UP * 2.8, RIGHT * 0.5 + UP * 2.8,
                      color=HIGHLIGHT_COLOR, buff=0.1)
        arrow_lbl = Text("剪开展开!",
                         font="Noto Sans CJK SC", font_size=22,
                         color=HIGHLIGHT_COLOR)
        arrow_lbl.next_to(arrow, UP, buff=0.15)
        self.play(GrowArrow(arrow), FadeIn(arrow_lbl), run_time=0.5)
        self.wait(0.3)

        # ── 右: 扇形 (精确圆心角) ──
        SECTOR_R  = 2.1                     # 扇形半径 (代表母线 l)
        SECTOR_CX = np.array([3.0, 4.2, 0]) # 扇形圆心位置

        # 精确使用 THETA_RAD 确保弧长 = 2πr
        sector = Sector(
            outer_radius=SECTOR_R,
            angle=THETA_RAD,
            start_angle=-THETA_RAD / 2,     # 对称放置
            color=SECTOR_COLOR,
            fill_opacity=0.45,
            stroke_color=SECTOR_COLOR,
            stroke_width=2.0
        ).move_to(SECTOR_CX)

        self.play(Create(sector), run_time=1.2)

        # 扇形半径线 (= 母线 l)
        r1_end = SECTOR_CX + SECTOR_R * np.array([
            np.cos(-THETA_RAD / 2), np.sin(-THETA_RAD / 2), 0])
        r2_end = SECTOR_CX + SECTOR_R * np.array([
            np.cos( THETA_RAD / 2), np.sin( THETA_RAD / 2), 0])
        radius_line = DashedLine(SECTOR_CX, r1_end,
                                  color=SLANT_COLOR, stroke_width=1.5)
        sec_l_lbl = MathTex("l", font_size=30, color=SLANT_COLOR)
        sec_l_lbl.next_to(r1_end, DOWN * 0.5 + RIGHT * 0.3)

        # 圆心角弧 & 标注
        angle_arc = Arc(radius=0.6,
                        start_angle=-THETA_RAD / 2, angle=THETA_RAD,
                        color=APEX_COLOR, stroke_width=2).move_to(SECTOR_CX)
        angle_lbl = MathTex(r"\theta", font_size=28, color=APEX_COLOR)
        angle_lbl.move_to(SECTOR_CX + np.array([0.85, 0, 0]))

        # 弧长说明
        arc_lbl = MathTex(r"\overset{\frown}{AB} = 2\pi r",
                          font_size=24, color=BASE_COLOR)
        arc_lbl.move_to(SECTOR_CX + np.array([2.5, 0.1, 0]))

        self.play(Create(radius_line), Write(sec_l_lbl), run_time=0.6)
        self.play(Create(angle_arc),   Write(angle_lbl),  run_time=0.5)
        self.play(Write(arc_lbl),                         run_time=0.5)
        self.wait(0.8)

        # ── 公式推导卡片 ──
        card_bg = RoundedRectangle(
            width=8.2, height=4.2, corner_radius=0.3,
            fill_color="#0d1b2a", fill_opacity=0.90,
            stroke_color=SECTOR_COLOR, stroke_width=1.8
        ).move_to(DOWN * 3.6)

        f_theta = MathTex(r"\theta = \frac{2\pi r}{l}",
                          font_size=30, color=APEX_COLOR)
        f_side  = MathTex(r"S_{\text{side}} = \pi r l",
                          font_size=30, color=SLANT_COLOR)
        f_base  = MathTex(r"S_{\text{base}} = \pi r^2",
                          font_size=30, color=BASE_COLOR)
        f_total = MathTex(r"S_{\text{total}} = \pi r(r + l)",
                          font_size=30, color=FORMULA_COLOR)
        VGroup(f_theta, f_side, f_base, f_total).arrange(DOWN, buff=0.42
                                                          ).move_to(DOWN * 3.6)

        self.play(FadeIn(card_bg), run_time=0.4)
        for f in [f_theta, f_side, f_base, f_total]:
            self.play(Write(f), run_time=0.5)
            self.wait(0.15)

        self.wait(2.0)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)


# ─────────────────────────────────────────────────────────
#  Scene 5 ── 体积公式 & 轴截面 (3-D)
# ─────────────────────────────────────────────────────────
class ConeScene5_Volume(ThreeDScene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.set_camera_orientation(phi=70 * DEGREES, theta=-40 * DEGREES)

        title = Text("体积 & 轴截面",
                     font="Noto Sans CJK SC", font_size=38, color=FORMULA_COLOR)
        title.move_to(UP * 6.8)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title), run_time=0.4)

        # 圆锥
        cone = Cone(base_radius=R, height=H, direction=UP,
                    fill_color=CONE_COLOR, fill_opacity=0.45,
                    stroke_color=CONE_COLOR, stroke_width=1.2)
        cone.shift(UP * (H / 2))
        self.play(Create(cone), run_time=1.0)

        # ── 体积公式 ──
        vol_lbl = Text("体积公式:",
                       font="Noto Sans CJK SC", font_size=26, color=WHITE)
        vol_lbl.move_to(DOWN * 4.8 + LEFT * 1.2)
        vol_tex = MathTex(r"V = \dfrac{1}{3}\pi r^2 h",
                          font_size=40, color=FORMULA_COLOR)
        vol_tex.next_to(vol_lbl, RIGHT, buff=0.3)
        self.add_fixed_in_frame_mobjects(vol_lbl, vol_tex)
        self.play(Write(vol_lbl), Write(vol_tex), run_time=0.9)
        self.wait(0.8)

        # 强调 1/3
        note = Text("比同底等高圆柱体积的 1/3",
                    font="Noto Sans CJK SC", font_size=22,
                    color=HIGHLIGHT_COLOR)
        note.move_to(DOWN * 6.2)
        self.add_fixed_in_frame_mobjects(note)
        self.play(FadeIn(note, scale=1.1), run_time=0.5)
        self.wait(1.0)
        self.play(FadeOut(note), run_time=0.3)

        # ── 轴截面 ──
        cross_lbl = Text("轴截面 = 等腰三角形",
                         font="Noto Sans CJK SC", font_size=26,
                         color=HIGHLIGHT_COLOR)
        cross_lbl.move_to(DOWN * 6.0)
        self.add_fixed_in_frame_mobjects(cross_lbl)
        self.play(FadeIn(cross_lbl), run_time=0.4)

        # 等腰三角形 (过轴的截面)
        cross_tri = Polygon(
            np.array([0,  H, 0]),
            np.array([-R, 0, 0]),
            np.array([ R, 0, 0]),
            stroke_color=HIGHLIGHT_COLOR, stroke_width=3,
            fill_color=RED_E, fill_opacity=0.32
        )
        self.play(Create(cross_tri), run_time=0.9)

        # 底边 2r 标注
        base_dash = DashedLine(np.array([-R, 0, 0]), np.array([R, 0, 0]),
                               color=BASE_COLOR, stroke_width=1.5)
        base_lbl = MathTex("2r", font_size=28, color=BASE_COLOR)
        base_lbl.move_to(np.array([0, -0.4, 0]))
        self.play(Create(base_dash), Write(base_lbl), run_time=0.6)
        self.wait(1.2)

        # 旋转欣赏
        self.begin_ambient_camera_rotation(rate=0.22)
        self.wait(2.5)
        self.stop_ambient_camera_rotation()

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# ─────────────────────────────────────────────────────────
#  Scene 6 ── 公式汇总 & 结尾
# ─────────────────────────────────────────────────────────
class ConeScene6_Summary(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # 标题
        title = Text("圆锥公式大汇总",
                     font="Noto Sans CJK SC", font_size=42, color=APEX_COLOR)
        title.move_to(UP * 6.5)
        self.play(Write(title), run_time=0.7)

        # 公式卡片列表
        rows = [
            ("母线",          r"l = \sqrt{r^2 + h^2}",          SLANT_COLOR),
            ("侧面积",        r"S_{\text{side}} = \pi r l",       SECTOR_COLOR),
            ("底面积",        r"S_{\text{base}} = \pi r^2",       BASE_COLOR),
            ("表面积",        r"S = \pi r(r + l)",                FORMULA_COLOR),
            ("体积",          r"V = \dfrac{1}{3}\pi r^2 h",       HIGHLIGHT_COLOR),
            ("展开扇形圆心角", r"\theta = \dfrac{360^\circ r}{l}", APEX_COLOR),
        ]

        cards = VGroup()
        for name_str, formula_str, col in rows:
            bg = RoundedRectangle(
                width=7.8, height=1.15, corner_radius=0.22,
                fill_color="#0d1b2a", fill_opacity=0.88,
                stroke_color=col, stroke_width=1.8
            )
            name_t = Text(name_str, font="Noto Sans CJK SC",
                          font_size=20, color=WHITE)
            name_t.move_to(bg.get_left() + RIGHT * 1.65)
            form_t = MathTex(formula_str, font_size=28, color=col)
            form_t.move_to(bg.get_right() + LEFT * 2.4)
            cards.add(VGroup(bg, name_t, form_t))

        cards.arrange(DOWN, buff=0.26).move_to(UP * 1.8)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.38)
            self.wait(0.1)
        self.wait(1.5)

        # ── 结尾 ──
        self.play(FadeOut(cards), FadeOut(title), run_time=0.6)

        outro_name = Text("上海初高中数学直通车",
                          font="Noto Sans CJK SC", font_size=40, color=WHITE)
        outro_name.move_to(UP * 1.5)
        outro_id = Text("@emptyandcalm",
                        font="Noto Sans CJK SC", font_size=30, color=GRAY_B)
        outro_id.move_to(UP * 0.5)
        outro_cta = Text("关注我，获得更多数学技巧!",
                         font="Noto Sans CJK SC", font_size=28,
                         color=APEX_COLOR)
        outro_cta.move_to(DOWN * 0.6)

        self.play(FadeIn(outro_name, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(outro_id),                   run_time=0.4)
        self.play(FadeIn(outro_cta, scale=1.1),        run_time=0.6)

        # 小圆锥图标旋转装饰
        deco = VGroup(*[
            Triangle(color=CONE_COLOR, fill_opacity=0.7).scale(0.28)
            .move_to(np.array([
                2.6 * np.cos(a),
                2.6 * np.sin(a) - 2.2,
                0
            ]))
            for a in np.linspace(0, 2*PI, 7, endpoint=False)
        ])
        self.play(*[FadeIn(d, scale=0.5) for d in deco], run_time=0.7)
        self.play(Rotate(deco, angle=2*PI, run_time=2.5, rate_func=smooth))
        self.wait(0.8)