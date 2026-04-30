"""
复数的几何表示 - Complex Numbers Geometric Representation
高二数学 · 第十三章 · 复数

TikTok 竖屏格式 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ═══ 全局配置 ═══
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ═══ 颜色常量 ═══
BG_COLOR = "#1a1a2e"
C_AXIS   = "#90caf9"   # 坐标轴
C_REAL   = "#4fc3f7"   # 实轴/实部
C_IMAG   = "#ef5350"   # 虚轴/虚部
C_Z      = "#66bb6a"   # 复数向量
C_MOD    = "#ffca28"   # 模
C_ARG    = "#ff7043"   # 辐角
C_POLAR  = "#ab47bc"   # 三角形式
C_CONJ   = "#ce93d8"   # 共轭
C_TITLE  = "#ffffff"
C_BODY   = "#cfd8dc"
C_ACCENT = "#ffca28"
C_GRAY   = "#78909c"

FONT = "PingFang SC"

# ═══ 示例复数 z = 3 + 4i  (经典 3-4-5 勾股三角形) ═══
_A = 3.0   # 实部
_B = 4.0   # 虚部


class ComplexGeo(Scene):
    """
    复数的几何表示教学动画
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── 几何数据统一初始化 ──
        self.setup_geometry()

        # ── 常驻作者标识 ──
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=C_GRAY
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        # ── 场景序列 ──
        self.scene1_hook()
        self.scene2_complex_plane()
        self.scene3_point_and_vector()
        self.scene4_modulus()
        self.scene5_argument()
        self.scene6_polar_form()
        self.scene7_conjugate()
        self.scene8_outro()

    # ══════════════════════════════════════════════════
    # 几何数据初始化
    # ══════════════════════════════════════════════════
    def setup_geometry(self):
        """统一计算所有几何数据，不使用臆想坐标"""
        self.a = _A
        self.b = _B

        # 模（精确计算）
        self.r = np.sqrt(self.a**2 + self.b**2)   # = 5.0

        # 辐角（弧度）
        self.theta = np.arctan2(self.b, self.a)    # ≈ 0.9273 rad ≈ 53.13°

        # 叉积验证辐角方向（v1 = 实轴正方向, v2 = OZ方向）
        v1 = np.array([1.0, 0.0])
        v2 = np.array([self.a, self.b]) / self.r
        self.cross_z = float(v1[0]*v2[1] - v1[1]*v2[0])
        # cross_z > 0 → 逆时针 → other_angle=False

        # Axes 参数（屏幕中部偏上）
        self.AX_X_RANGE   = [-2, 6, 1]
        self.AX_Y_RANGE   = [-5, 6, 1]
        self.AX_X_LENGTH  = 5.6
        self.AX_Y_LENGTH  = 5.6
        self.AX_CENTER    = np.array([0.0, 1.2, 0.0])

        # 单位缩放（用于验证）
        self.ax_scale_x = self.AX_X_LENGTH / (self.AX_X_RANGE[1] - self.AX_X_RANGE[0])
        self.ax_scale_y = self.AX_Y_LENGTH / (self.AX_Y_RANGE[1] - self.AX_Y_RANGE[0])

        # 验证
        self._verify()

    def _verify(self):
        eps = 1e-10
        # 勾股定理验证
        assert abs(self.a**2 + self.b**2 - self.r**2) < eps, "模计算错误"
        # 辐角验证
        assert abs(np.cos(self.theta) - self.a/self.r) < eps, "cosθ 错误"
        assert abs(np.sin(self.theta) - self.b/self.r) < eps, "sinθ 错误"
        # 方向验证
        assert self.cross_z > 0, "辐角方向计算错误：预期逆时针"
        print(f"✓ setup_geometry 验证通过: r={self.r}, θ={np.degrees(self.theta):.2f}°, "
              f"cross={self.cross_z:.4f}")

    # ── 辅助：创建坐标轴对象 ──
    def _make_axes(self):
        ax = Axes(
            x_range=self.AX_X_RANGE,
            y_range=self.AX_Y_RANGE,
            x_length=self.AX_X_LENGTH,
            y_length=self.AX_Y_LENGTH,
            axis_config={
                "color": C_AXIS,
                "stroke_width": 2,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15,
                "include_ticks": True,
                "tick_size": 0.06,
            },
        ).move_to(self.AX_CENTER)
        return ax

    # ══════════════════════════════════════════════════
    # Scene 1: 开场钩子
    # ══════════════════════════════════════════════════
    def scene1_hook(self):
        q = Text("复数能画出来吗?", font=FONT, font_size=46, color=C_TITLE)
        q.move_to(UP * 5.3)

        nums = VGroup(
            MathTex(r"3 + 4i",   font_size=52, color=C_Z),
            MathTex(r"-1 + 2i",  font_size=44, color=C_MOD),
            MathTex(r"5i",       font_size=44, color=C_IMAG),
            MathTex(r"2 - 3i",   font_size=44, color=C_CONJ),
        ).arrange(DOWN, buff=0.4).move_to(UP * 2.8)

        arrow = Text("↓ 找到它们的位置!", font=FONT, font_size=28, color=C_ACCENT)
        arrow.move_to(DOWN * 0.5)

        self.play(Write(q), run_time=0.6)
        for n in nums:
            self.play(FadeIn(n, shift=LEFT * 0.3, scale=1.1), run_time=0.3)
        self.play(FadeIn(arrow, shift=UP * 0.2), run_time=0.4)
        self.wait(0.6)

        self.play(FadeOut(q), FadeOut(nums), FadeOut(arrow), run_time=0.5)

    # ══════════════════════════════════════════════════
    # Scene 2: 建立复平面
    # ══════════════════════════════════════════════════
    def scene2_complex_plane(self):
        title = Text("复平面（高斯平面）", font=FONT, font_size=38, color=C_TITLE)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # ── 坐标轴 ──
        self.ax = self._make_axes()
        self.play(Create(self.ax), run_time=1.0)

        # 轴标签
        o_label = MathTex("O", font_size=24, color=C_AXIS)
        o_label.next_to(self.ax.get_origin(), DL, buff=0.12)

        x_label = Text("实轴", font=FONT, font_size=22, color=C_REAL)
        x_label.next_to(self.ax.x_axis.get_right(), RIGHT, buff=0.1)

        y_label = Text("虚轴", font=FONT, font_size=22, color=C_IMAG)
        y_label.next_to(self.ax.y_axis.get_top(), UP, buff=0.05)

        self.play(
            Write(o_label), Write(x_label), Write(y_label),
            run_time=0.6
        )

        # 刻度数字 (精选几个)
        ticks = VGroup()
        for v, pos in [(1, self.ax.c2p(1, 0)), (2, self.ax.c2p(2, 0)),
                       (3, self.ax.c2p(3, 0)), (4, self.ax.c2p(4, 0)),
                       (5, self.ax.c2p(5, 0))]:
            t = MathTex(str(v), font_size=18, color=C_BODY)
            t.next_to(pos, DOWN, buff=0.08)
            ticks.add(t)
        for v, pos in [(1, self.ax.c2p(0, 1)), (2, self.ax.c2p(0, 2)),
                       (3, self.ax.c2p(0, 3)), (4, self.ax.c2p(0, 4))]:
            t = MathTex(str(v) + "i", font_size=18, color=C_BODY)
            t.next_to(pos, LEFT, buff=0.08)
            ticks.add(t)

        self.play(FadeIn(ticks), run_time=0.4)

        explain = Text(
            "z = a + bi  ←→  点 Z(a, b)",
            font=FONT, font_size=26, color=C_BODY
        ).move_to(DOWN * 4.0)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(FadeOut(title), FadeOut(explain), run_time=0.4)

        # 保留给后续场景使用
        self.ax_labels = VGroup(o_label, x_label, y_label, ticks)
        self.scene2_title_ref = title

    # ══════════════════════════════════════════════════
    # Scene 3: 复数对应的点与向量
    # ══════════════════════════════════════════════════
    def scene3_point_and_vector(self):
        title = Text("复数 z = 3 + 4i 的位置", font=FONT, font_size=36, color=C_TITLE)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        ax = self.ax
        z_screen = ax.c2p(self.a, self.b)      # 点 Z(3, 4)
        origin    = ax.c2p(0, 0)
        foot_x    = ax.c2p(self.a, 0)          # (3, 0)
        foot_y    = ax.c2p(0, self.b)          # (0, 4)

        # ── 投影辅助线（虚线） ──
        dash_to_x = DashedLine(z_screen, foot_x, color=C_REAL,
                               dash_length=0.08, stroke_width=1.5)
        dash_to_y = DashedLine(z_screen, foot_y, color=C_IMAG,
                               dash_length=0.08, stroke_width=1.5)

        # 实部标注
        a_label = MathTex(r"a = 3", font_size=26, color=C_REAL)
        a_label.next_to(ax.c2p(1.5, 0), DOWN, buff=0.25)

        b_label = MathTex(r"b = 4", font_size=26, color=C_IMAG)
        b_label.next_to(ax.c2p(0, 2.0), LEFT, buff=0.28)

        # ── 点 Z ──
        z_dot = Dot(z_screen, color=C_Z, radius=0.12)
        z_label = MathTex(r"Z(3,\;4)", font_size=28, color=C_Z)
        z_label.next_to(z_dot, UR, buff=0.18)

        # ── 向量 OZ ──
        z_vector = Arrow(
            origin, z_screen,
            color=C_Z, buff=0,
            stroke_width=3.5,
            max_tip_length_to_length_ratio=0.10,
        )

        formula_line = MathTex(
            r"z = 3 + 4i  \Longleftrightarrow  Z(3,\;4)",
            font_size=30, color=C_BODY
        ).move_to(DOWN * 3.8)

        # ── 动画 ──
        self.play(Create(dash_to_x), Create(dash_to_y), run_time=0.7)
        self.play(Write(a_label), Write(b_label), run_time=0.5)
        self.play(FadeIn(z_dot, scale=0.5), run_time=0.4)
        self.play(Flash(z_dot, color=C_Z, flash_radius=0.3), run_time=0.4)
        self.play(Write(z_label), run_time=0.4)
        self.play(GrowArrow(z_vector), run_time=0.8)
        self.play(FadeIn(formula_line, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 清理辅助线，保留点和向量
        self.play(
            FadeOut(title), FadeOut(dash_to_x), FadeOut(dash_to_y),
            FadeOut(a_label), FadeOut(b_label), FadeOut(formula_line),
            run_time=0.4
        )

        # 保存到实例
        self.z_dot     = z_dot
        self.z_vector  = z_vector
        self.z_label   = z_label
        self.z_screen  = z_screen
        self.origin_pt = origin

    # ══════════════════════════════════════════════════
    # Scene 4: 模 |z|
    # ══════════════════════════════════════════════════
    def scene4_modulus(self):
        title = Text("复数的模  |z|", font=FONT, font_size=38, color=C_MOD)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        ax = self.ax
        origin = self.origin_pt
        z_screen = self.z_screen
        foot_x = ax.c2p(self.a, 0)

        # ── 直角三角形三边 ──
        side_a = Line(origin,   foot_x,   color=C_REAL,  stroke_width=3)
        side_b = Line(foot_x,   z_screen, color=C_IMAG,  stroke_width=3)
        hyp    = Line(origin,   z_screen, color=C_MOD,   stroke_width=4)

        # 直角符号
        vec_xa = (foot_x - origin)[:2]; vec_xa /= np.linalg.norm(vec_xa)
        vec_xb = (z_screen - foot_x)[:2]; vec_xb /= np.linalg.norm(vec_xb)
        sz = 0.16
        ra_pts = [
            foot_x,
            foot_x + np.append(vec_xa * sz, 0),
            foot_x + np.append(vec_xa * sz + vec_xb * sz, 0),
            foot_x + np.append(vec_xb * sz, 0),
        ]
        right_mark = Polygon(*ra_pts, color=C_ACCENT,
                             stroke_width=1.5, fill_opacity=0)

        # 边长标注
        lbl_a = MathTex(r"a=3", font_size=24, color=C_REAL)
        lbl_a.next_to(ax.c2p(1.5, 0), DOWN, buff=0.22)

        lbl_b = MathTex(r"b=4", font_size=24, color=C_IMAG)
        lbl_b.next_to(ax.c2p(self.a, self.b / 2), RIGHT, buff=0.18)

        lbl_r = MathTex(r"|z|=r", font_size=26, color=C_MOD)
        mid_hyp = (origin + z_screen) / 2
        lbl_r.next_to(mid_hyp, LEFT, buff=0.22)

        # 公式推导
        formula1 = MathTex(
            r"|z| = \sqrt{a^2 + b^2}",
            font_size=38, color=C_MOD
        ).move_to(DOWN * 3.4)

        formula2 = MathTex(
            r"= \sqrt{3^2 + 4^2} = \sqrt{25} = 5",
            font_size=34, color=C_MOD
        ).move_to(DOWN * 4.3)

        # 模的圆
        circ = Circle(
            radius=self.r * self.ax_scale_x,
            color=C_MOD, stroke_width=2, stroke_opacity=0.6
        ).move_to(self.origin_pt)

        # ── 动画 ──
        self.play(Create(side_a), Create(side_b), run_time=0.6)
        self.play(FadeIn(right_mark), run_time=0.3)
        self.play(Write(lbl_a), Write(lbl_b), run_time=0.5)
        self.play(Create(hyp), Write(lbl_r), run_time=0.6)
        self.play(Write(formula1), run_time=0.6)
        self.play(Write(formula2), run_time=0.6)
        self.wait(0.5)
        self.play(Create(circ), run_time=1.0)

        circle_note = Text("|z|=5 是 Z 到原点的距离", font=FONT, font_size=24, color=C_BODY)
        circle_note.move_to(DOWN * 5.3)
        self.play(FadeIn(circle_note), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(title),
            FadeOut(side_a), FadeOut(side_b), FadeOut(hyp),
            FadeOut(right_mark),
            FadeOut(lbl_a), FadeOut(lbl_b), FadeOut(lbl_r),
            FadeOut(formula1), FadeOut(formula2),
            FadeOut(circ), FadeOut(circle_note),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════
    # Scene 5: 辐角 θ
    # ══════════════════════════════════════════════════
    def scene5_argument(self):
        title = Text("辐角  arg(z) = θ", font=FONT, font_size=38, color=C_ARG)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        ax      = self.ax
        origin  = self.origin_pt
        z_sc    = self.z_screen

        # 实轴正方向上一点（用于构造角弧）
        real_pt = ax.c2p(2.0, 0)   # 实轴上的参考点

        # ── 辐角弧（cross_z > 0 → 逆时针 → other_angle=False） ──
        line_real = Line(origin, real_pt)
        line_oz   = Line(origin, z_sc)

        arg_arc = Angle(
            line_real, line_oz,
            radius=0.55,
            color=C_ARG,
            stroke_width=3,
            other_angle=False,      # cross_z > 0，逆时针
            quadrant=(1, 1),
        )

        theta_label = MathTex(r"\theta", font_size=30, color=C_ARG)
        # 放在弧中间偏外
        arc_mid_angle = self.theta / 2
        arc_label_pos = origin + np.array([
            0.75 * np.cos(arc_mid_angle),
            0.75 * np.sin(arc_mid_angle),
            0
        ])
        theta_label.move_to(arc_label_pos)

        # 公式
        f1 = MathTex(r"\tan\theta = \frac{b}{a}", font_size=38, color=C_ARG)
        f1.move_to(DOWN * 3.3)

        f2 = MathTex(
            r"= \frac{4}{3} \approx 1.333",
            font_size=34, color=C_ARG
        ).move_to(DOWN * 4.2)

        f3 = MathTex(
            r"\theta \approx 53.13^\circ",
            font_size=36, color=C_ACCENT
        ).move_to(DOWN * 5.2)

        # 实轴正方向延伸参考线
        ref_line = DashedLine(
            origin, ax.c2p(2.2, 0),
            color=C_ARG, stroke_width=1.5, dash_length=0.08
        )

        # ── 动画 ──
        self.play(Create(ref_line), run_time=0.4)
        self.play(Create(arg_arc), run_time=0.8)
        self.play(Write(theta_label), run_time=0.4)
        self.play(Write(f1), run_time=0.6)
        self.play(Write(f2), run_time=0.5)
        self.play(Write(f3), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(ref_line),
            FadeOut(f1), FadeOut(f2), FadeOut(f3),
            run_time=0.4
        )
        # 保留辐角弧和θ标注供下一场景
        self.arg_arc    = arg_arc
        self.theta_lbl  = theta_label

    # ══════════════════════════════════════════════════
    # Scene 6: 三角形式
    # ══════════════════════════════════════════════════
    def scene6_polar_form(self):
        title = Text("三角形式", font=FONT, font_size=42, color=C_POLAR)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 辐角弧颜色变换
        self.play(self.arg_arc.animate.set_color(C_POLAR), run_time=0.3)

        # r 标注
        origin = self.origin_pt
        z_sc   = self.z_screen
        mid_oz = (origin + z_sc) / 2
        r_label = MathTex(r"r = |z| = 5", font_size=26, color=C_POLAR)
        r_label.next_to(mid_oz, LEFT, buff=0.22)
        self.play(Write(r_label), run_time=0.5)

        # 推导公式
        derive1 = MathTex(
            r"a = r\cos\theta,\quad b = r\sin\theta",
            font_size=30, color=C_BODY
        ).move_to(DOWN * 3.2)

        derive2 = MathTex(
            r"z = a + bi = r\cos\theta + ir\sin\theta",
            font_size=28, color=C_BODY
        ).move_to(DOWN * 4.1)

        polar_box = MathTex(
            r"z = r(\cos\theta + i\sin\theta)",
            font_size=40, color=C_POLAR
        ).move_to(DOWN * 5.2)

        # 高亮框
        box_rect = SurroundingRectangle(
            polar_box, color=C_POLAR, buff=0.18, corner_radius=0.1
        )
        # Note: RoundedRectangle style via SurroundingRectangle is fine

        example = MathTex(
            r"= 5(\cos53.13^\circ + i\sin53.13^\circ)",
            font_size=28, color=C_ACCENT
        ).move_to(DOWN * 6.2)

        self.play(Write(derive1), run_time=0.6)
        self.play(Write(derive2), run_time=0.6)
        self.play(Write(polar_box), run_time=0.7)
        self.play(Create(box_rect), run_time=0.4)
        self.play(Write(example), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(r_label),
            FadeOut(self.arg_arc), FadeOut(self.theta_lbl),
            FadeOut(derive1), FadeOut(derive2),
            FadeOut(polar_box), FadeOut(box_rect), FadeOut(example),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════
    # Scene 7: 共轭复数（关于实轴对称）
    # ══════════════════════════════════════════════════
    def scene7_conjugate(self):
        title = Text("共轭复数  z̄ 关于实轴对称", font=FONT, font_size=32, color=C_CONJ)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        ax     = self.ax
        origin = self.origin_pt
        z_sc   = self.z_screen

        # 共轭点 z̄ = 3 - 4i → Z̄(3, -4)
        zbar_screen = ax.c2p(self.a, -self.b)

        zbar_dot = Dot(zbar_screen, color=C_CONJ, radius=0.12)
        zbar_label = MathTex(r"\bar{Z}(3,\;-4)", font_size=26, color=C_CONJ)
        zbar_label.next_to(zbar_dot, DR, buff=0.18)

        zbar_vector = Arrow(
            origin, zbar_screen,
            color=C_CONJ, buff=0,
            stroke_width=3.5,
            max_tip_length_to_length_ratio=0.10,
        )

        # 对称轴（实轴高亮段）
        real_highlight = Line(
            ax.c2p(-1, 0), ax.c2p(5, 0),
            color=C_ACCENT, stroke_width=3.5
        )

        # 对称连线
        sym_line = DashedLine(
            z_sc, zbar_screen,
            color=C_ACCENT, dash_length=0.10, stroke_width=2
        )

        # 对称交点标注（实轴上 (3,0)）
        mid_pt = (z_sc + zbar_screen) / 2
        mid_dot = Dot(mid_pt, color=C_ACCENT, radius=0.07)

        formulas = VGroup(
            MathTex(r"z = 3 + 4i", font_size=32, color=C_Z),
            MathTex(r"\bar{z} = 3 - 4i", font_size=32, color=C_CONJ),
            MathTex(r"|z| = |\bar{z}| = 5", font_size=30, color=C_BODY),
            MathTex(r"z \cdot \bar{z} = 3^2 + 4^2 = 25", font_size=28, color=C_BODY),
        ).arrange(DOWN, buff=0.32).move_to(DOWN * 4.5)

        # ── 动画 ──
        self.play(Flash(real_highlight, color=C_ACCENT), run_time=0.3)
        self.play(Create(real_highlight), run_time=0.4)
        self.play(Create(sym_line), FadeIn(mid_dot), run_time=0.5)
        self.play(FadeIn(zbar_dot, scale=0.5), run_time=0.4)
        self.play(GrowArrow(zbar_vector), Write(zbar_label), run_time=0.6)
        self.wait(0.3)

        for f in formulas:
            self.play(FadeIn(f, shift=LEFT * 0.2), run_time=0.35)

        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(real_highlight), FadeOut(sym_line), FadeOut(mid_dot),
            FadeOut(zbar_dot), FadeOut(zbar_vector), FadeOut(zbar_label),
            FadeOut(self.z_dot), FadeOut(self.z_vector), FadeOut(self.z_label),
            FadeOut(self.ax), FadeOut(self.ax_labels),
            FadeOut(formulas),
            run_time=0.7
        )

    # ══════════════════════════════════════════════════
    # Scene 8: 片尾总结
    # ══════════════════════════════════════════════════
    def scene8_outro(self):
        # 核心公式总结卡片
        summary_title = Text("复数几何表示  核心公式", font=FONT, font_size=32, color=C_ACCENT)
        summary_title.move_to(UP * 5.0)

        formulas = VGroup(
            MathTex(r"z = a+bi \;\Longleftrightarrow\; Z(a,\,b)", font_size=30, color=C_TITLE),
            MathTex(r"|z| = \sqrt{a^2 + b^2}", font_size=32, color=C_MOD),
            MathTex(r"\arg(z) = \theta,\;\tan\theta = \dfrac{b}{a}", font_size=30, color=C_ARG),
            MathTex(r"z = r(\cos\theta + i\sin\theta)", font_size=32, color=C_POLAR),
            MathTex(r"\bar{z} = a - bi", font_size=28, color=C_CONJ),
        ).arrange(DOWN, buff=0.42).move_to(UP * 2.2)

        # MathTex 中不允许中文，将第5行改为纯公式
        # 共轭说明用独立 Text
        conj_note = Text("z̄: reflection across real axis", font=FONT, font_size=22, color=C_CONJ)
        conj_note.next_to(formulas[-1], DOWN, buff=0.05)

        # 作者放大
        author_big = Text("上海初高中数学直通车", font=FONT, font_size=36, color=C_TITLE)
        author_big.move_to(DOWN * 1.8)

        author_id = Text("@emptyandcalm", font=FONT, font_size=28, color=C_GRAY)
        author_id.move_to(DOWN * 2.7)

        follow = Text("关注我，学更多高中数学!", font=FONT, font_size=30, color=C_ACCENT)
        follow.move_to(DOWN * 3.8)

        self.play(Write(summary_title), run_time=0.5)
        for f in formulas:
            self.play(Write(f), run_time=0.4)
        self.play(FadeIn(conj_note), run_time=0.3)
        self.wait(0.4)

        self.play(Transform(self.author, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow, scale=1.05), run_time=0.5)
        self.wait(1.8)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)