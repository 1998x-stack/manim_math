"""
cylinder_animation.py - 圆柱知识点教学动画
目标: 高三学生, TikTok 竖屏, 约55秒
作者: 上海初高中数学直通车 @emptyandcalm

运行:
  manim -pql cylinder_animation.py CylinderLesson   # 快速预览
  manim -qh  cylinder_animation.py CylinderLesson   # 高质量
"""

from manim import *
import numpy as np

# ======================================================
# 全局配置 - TikTok 竖屏
# ======================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ======================================================
# 常量
# ======================================================
FONT        = "PingFang SC"
BG          = "#1a1a2e"
AUTHOR_NAME = "上海初高中数学直通车"
AUTHOR_ID   = "@emptyandcalm"

# 圆柱几何参数
CYL_R = 1.3   # 半径
CYL_H = 2.6   # 高

# 配色
C_CYL       = "#4a90d9"   # 圆柱侧面蓝
C_BASE      = "#7ec8e3"   # 底面浅蓝
C_AXIS      = "#f39c12"   # 轴橙色
C_HL        = "#f1c40f"   # 高亮黄
C_FORMULA   = "#2ecc71"   # 公式绿
C_ACCENT    = "#e74c3c"   # 强调红


# ======================================================
# 辅助函数
# ======================================================
def cn(text, size=24, color=WHITE, y=None, x=0):
    """快速创建中文 Text"""
    t = Text(text, font=FONT, font_size=size, color=color)
    if y is not None:
        t.move_to([x, y, 0])
    return t

def fml(latex, size=30, color=WHITE):
    """快速创建 MathTex (ASCII only!)"""
    return MathTex(latex, font_size=size, color=color)


def make_cylinder(r=CYL_R, h=CYL_H, opacity=0.65):
    """创建圆柱 (direction=UP, y轴为轴)"""
    cyl = Cylinder(
        radius=r, height=h,
        direction=UP,
        fill_color=C_CYL,
        fill_opacity=opacity,
        stroke_color=WHITE,
        stroke_width=0.4,
        resolution=(32, 16),
    )
    return cyl


def make_circle_cap(r, y_pos, color=C_BASE):
    """在给定 y 位置创建水平圆盖"""
    # direction=UP 的 Cylinder: 底面在 y=-h/2, 顶面在 y=h/2
    # 圆盖是 xz-plane 内的圆, 需要绕 x 轴旋转 90°
    cap = Circle(radius=r, color=color, fill_color=color, fill_opacity=0.6, stroke_width=1.5)
    cap.rotate(PI / 2, axis=RIGHT)   # 从 xy-plane → xz-plane (即水平)
    cap.move_to([0, y_pos, 0])
    return cap


# ======================================================
# 主场景
# ======================================================
class CylinderLesson(ThreeDScene):

    def construct(self):
        self.camera.background_color = BG
        self._scene_opening()
        self._scene_definition()
        self._scene_parts()
        self._scene_unfold()
        self._scene_formulas()
        self._scene_cross_section()
        self._scene_outro()

    # --------------------------------------------------
    # Scene 1: 开场 (~4s)
    # --------------------------------------------------
    def _scene_opening(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # 作者信息 (固定在 frame 顶部)
        author = cn(AUTHOR_NAME + "  " + AUTHOR_ID, size=18, color=GRAY_B, y=7.2)
        self.add_fixed_in_frame_mobjects(author)
        self.add(author)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.3)

        # 大标题
        title = cn("圆柱", size=60, color=C_HL, y=5.8)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.8)

        subtitle = cn("旋转体中的重要几何体", size=26, color=GRAY_A, y=4.9)
        self.add_fixed_in_frame_mobjects(subtitle)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 3D 圆柱
        cyl = make_cylinder()
        self.play(Create(cyl), run_time=1.2)
        self.begin_ambient_camera_rotation(rate=0.35)
        self.wait(1.5)
        self.stop_ambient_camera_rotation()

        # 钩子
        hook = cn("知道圆柱的公式怎么来吗?", size=28, color=C_HL, y=-5.2)
        self.add_fixed_in_frame_mobjects(hook)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(subtitle), FadeOut(hook),
            FadeOut(cyl), FadeOut(author),
            run_time=0.5
        )

    # --------------------------------------------------
    # Scene 2: 定义 - 矩形旋转 (~10s)
    # --------------------------------------------------
    def _scene_definition(self):
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, run_time=0.3)

        r, h = CYL_R, CYL_H

        title = cn("圆柱的定义", size=34, color=C_HL, y=6.8)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.6)

        # ---- 旋转轴 (y 轴方向虚线) ----
        axis_line = DashedLine(
            start=np.array([0, -h / 2 - 0.4, 0]),
            end=np.array([0,  h / 2 + 0.4, 0]),
            color=C_AXIS, dash_length=0.15, stroke_width=3
        )
        self.play(Create(axis_line), run_time=0.5)

        axis_lbl = cn("旋转轴", size=22, color=C_AXIS, y=3.8, x=-3.0)
        self.add_fixed_in_frame_mobjects(axis_lbl)
        self.play(FadeIn(axis_lbl), run_time=0.3)

        # ---- 初始矩形 (在 xz-plane 的竖直面: x ∈ [0,r], y ∈ [-h/2, h/2]) ----
        # 在 xy-plane 中: corners → Polygon
        rect = Polygon(
            [0, -h / 2, 0],
            [r, -h / 2, 0],
            [r,  h / 2, 0],
            [0,  h / 2, 0],
            color=WHITE,
            fill_color=TEAL_D,
            fill_opacity=0.55,
            stroke_width=2
        )
        self.play(Create(rect), run_time=0.7)

        explain1 = cn("以矩形一边为轴旋转360°", size=24, color=GRAY_A, y=-5.0)
        self.add_fixed_in_frame_mobjects(explain1)
        self.play(FadeIn(explain1), run_time=0.4)
        self.wait(0.4)

        # ---- 旋转动画: Surface 扫面 ----
        # 参数化: (r*cos(u), v*h - h/2, r*sin(u)), u∈[0,theta], v∈[0,1]
        t_track = ValueTracker(0.01)

        def get_sweep():
            theta = t_track.get_value()
            n_u = max(int(theta / PI * 20) + 2, 2)
            surf = Surface(
                lambda u, v: np.array([r * np.cos(u), v * h - h / 2, r * np.sin(u)]),
                u_range=[0, theta],
                v_range=[0, 1],
                resolution=(n_u, 8),
                fill_color=C_CYL,
                fill_opacity=0.60,
                stroke_color=WHITE,
                stroke_width=0.3,
            )
            return surf

        def get_moving_edge():
            theta = t_track.get_value()
            return Line3D(
                start=np.array([r * np.cos(theta), -h / 2, r * np.sin(theta)]),
                end=np.array([r * np.cos(theta),  h / 2, r * np.sin(theta)]),
                color=C_HL, stroke_width=3
            )

        sweep       = always_redraw(get_sweep)
        moving_edge = always_redraw(get_moving_edge)
        self.add(sweep, moving_edge)

        self.play(
            t_track.animate.set_value(2 * PI),
            run_time=3.0,
            rate_func=linear
        )
        self.wait(0.4)

        # ---- 显示完整圆柱 ----
        final_cyl = make_cylinder(r, h)
        self.play(
            FadeOut(rect), FadeOut(sweep), FadeOut(moving_edge),
            FadeIn(final_cyl),
            run_time=0.7
        )

        explain2 = cn("得到圆柱 (旋转体)", size=26, color=C_HL, y=-5.0)
        self.add_fixed_in_frame_mobjects(explain2)
        self.play(FadeOut(explain1), FadeIn(explain2), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(axis_lbl), FadeOut(explain2),
            FadeOut(axis_line), FadeOut(final_cyl),
            run_time=0.5
        )

    # --------------------------------------------------
    # Scene 3: 各部分标注 (~8s)
    # --------------------------------------------------
    def _scene_parts(self):
        self.move_camera(phi=75 * DEGREES, theta=-50 * DEGREES, run_time=0.3)

        r, h = CYL_R, CYL_H

        title = cn("圆柱的各部分", size=34, color=C_HL, y=6.8)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.6)

        # 圆柱
        cyl = make_cylinder(r, h, opacity=0.45)
        self.play(Create(cyl), run_time=1.0)

        # ---- 轴 ----
        axis_line = DashedLine(
            np.array([0, -h / 2, 0]),
            np.array([0,  h / 2, 0]),
            color=C_AXIS, dash_length=0.13, stroke_width=2.5
        )
        self.play(Create(axis_line), run_time=0.5)

        axis_lbl = cn("轴", size=26, color=C_AXIS, y=3.8, x=2.0)
        self.add_fixed_in_frame_mobjects(axis_lbl)
        self.play(FadeIn(axis_lbl), run_time=0.3)

        # ---- 侧面标注 ----
        side_lbl = cn("侧面", size=26, color=C_CYL, y=0.5, x=3.5)
        self.add_fixed_in_frame_mobjects(side_lbl)
        self.play(FadeIn(side_lbl), run_time=0.3)

        # ---- 底面圆盖 ----
        top_cap = make_circle_cap(r, h / 2)
        bot_cap = make_circle_cap(r, -h / 2)
        self.play(Create(top_cap), Create(bot_cap), run_time=0.6)

        base_lbl = cn("底面 (圆)", size=24, color=C_BASE, y=4.2, x=3.0)
        self.add_fixed_in_frame_mobjects(base_lbl)
        self.play(FadeIn(base_lbl), run_time=0.3)

        # ---- 半径 r ----
        # 从轴到边的线段 (在顶面位置)
        r_line = Line3D(
            start=np.array([0, h / 2, 0]),
            end=np.array([r, h / 2, 0]),
            color=C_HL, stroke_width=4
        )
        self.play(Create(r_line), run_time=0.5)
        r_lbl = fml("r", size=34, color=C_HL)
        r_lbl.move_to([0.5, 5.2, 0])
        self.add_fixed_in_frame_mobjects(r_lbl)
        self.play(FadeIn(r_lbl), run_time=0.3)

        # ---- 高 h ----
        h_line = Line3D(
            start=np.array([r + 0.35, -h / 2, 0]),
            end=np.array([r + 0.35,  h / 2, 0]),
            color=C_FORMULA, stroke_width=4
        )
        self.play(Create(h_line), run_time=0.5)
        h_lbl = fml("h", size=34, color=C_FORMULA)
        h_lbl.move_to([3.8, 0.0, 0])
        self.add_fixed_in_frame_mobjects(h_lbl)
        self.play(FadeIn(h_lbl), run_time=0.3)

        self.wait(1.5)

        fixed_objs = [title, axis_lbl, side_lbl, base_lbl, r_lbl, h_lbl]
        scene_objs = [cyl, top_cap, bot_cap, axis_line, r_line, h_line]
        self.play(
            *[FadeOut(o) for o in fixed_objs + scene_objs],
            run_time=0.5
        )

    # --------------------------------------------------
    # Scene 4: 侧面展开 (~9s)
    # --------------------------------------------------
    def _scene_unfold(self):
        r, h = CYL_R, CYL_H

        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, run_time=0.3)

        title = cn("侧面展开图", size=34, color=C_HL, y=6.8)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.6)

        # 显示圆柱
        cyl = make_cylinder(r, h)
        self.play(Create(cyl), run_time=0.8)
        self.wait(0.4)

        # 过渡说明
        explain = cn("将侧面展开...", size=26, color=GRAY_A, y=-4.8)
        self.add_fixed_in_frame_mobjects(explain)
        self.play(FadeIn(explain), run_time=0.4)
        self.wait(0.5)

        # 切换为正视图
        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, run_time=0.8)

        self.play(FadeOut(cyl), FadeOut(explain), run_time=0.4)

        # ---- 展开矩形 ----
        # 真实尺寸: 长 = 2πr ≈ 8.17, 高 = h = 2.6
        # 缩放到显示尺寸
        circumf = 2 * np.pi * r      # ~8.17
        scale_f = 5.6 / circumf       # 压缩到宽 5.6
        disp_w  = circumf * scale_f   # 5.6
        disp_h  = h * scale_f         # ~1.78

        unfolded = Rectangle(
            width=disp_w, height=disp_h,
            color=C_CYL, fill_color=C_CYL, fill_opacity=0.45,
            stroke_width=2
        )
        unfolded.move_to([0, 1.0, 0])
        self.add_fixed_in_frame_mobjects(unfolded)
        self.play(FadeIn(unfolded, scale=0.6), run_time=0.8)

        # ---- 底部 Brace: 长 = 2πr ----
        w_brace = Brace(unfolded, DOWN, color=C_HL)
        w_cn    = cn("底面周长", size=20, color=C_HL)
        w_math  = fml(r"= 2\pi r", size=26, color=C_HL)
        w_grp   = VGroup(w_cn, w_math).arrange(RIGHT, buff=0.15)
        w_grp.next_to(w_brace, DOWN, buff=0.15)
        self.add_fixed_in_frame_mobjects(w_brace, w_grp)
        self.play(FadeIn(w_brace), Write(w_grp), run_time=0.8)

        # ---- 右侧 Brace: 高 = h ----
        h_brace = Brace(unfolded, RIGHT, color=C_FORMULA)
        h_math  = fml(r"h", size=30, color=C_FORMULA)
        h_math.next_to(h_brace, RIGHT, buff=0.15)
        self.add_fixed_in_frame_mobjects(h_brace, h_math)
        self.play(FadeIn(h_brace), Write(h_math), run_time=0.5)

        self.wait(0.5)

        # ---- 侧面积公式 ----
        f_cn    = cn("侧面积:", size=26, color=WHITE)
        f_math  = fml(r"S = 2\pi r h", size=32, color=C_FORMULA)
        f_grp   = VGroup(f_cn, f_math).arrange(RIGHT, buff=0.25)
        f_grp.move_to([0, -5.5, 0])
        self.add_fixed_in_frame_mobjects(f_grp)
        self.play(FadeIn(f_cn), Write(f_math), run_time=0.8)

        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(unfolded),
            FadeOut(w_brace), FadeOut(w_grp),
            FadeOut(h_brace), FadeOut(h_math), FadeOut(f_grp),
            run_time=0.5
        )

    # --------------------------------------------------
    # Scene 5: 公式汇总 (~11s)
    # --------------------------------------------------
    def _scene_formulas(self):
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, run_time=0.5)

        r, h = CYL_R * 0.75, CYL_H * 0.75   # 小圆柱

        title = cn("圆柱的公式", size=34, color=C_HL, y=6.8)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.5)

        # 小圆柱在左侧 3D
        cyl = make_cylinder(r, h, opacity=0.5)
        cyl.shift(LEFT * 2)
        self.play(Create(cyl), run_time=0.8)
        self.begin_ambient_camera_rotation(rate=0.15)

        # 公式列表 (右侧, fixed-in-frame)
        formulas_data = [
            ("体积",   r"V = \pi r^2 h",         C_FORMULA, 2.5),
            ("侧面积", r"S_{\rm lat} = 2\pi r h", BLUE_C,    0.8),
            ("表面积", r"S = 2\pi r^2 + 2\pi r h",C_ACCENT, -0.9),
        ]

        row_objs = []
        for name_str, latex, color, y_pos in formulas_data:
            n_txt = cn(name_str + ":", size=22, color=WHITE)
            f_tex = fml(latex, size=28, color=color)
            row   = VGroup(n_txt, f_tex).arrange(RIGHT, buff=0.2)
            row.move_to([1.5, y_pos, 0])
            self.add_fixed_in_frame_mobjects(row)
            row_objs.append(row)
            self.play(FadeIn(n_txt), Write(f_tex), run_time=0.7)
            self.wait(0.3)

        # 化简表面积
        simp_cn   = cn("即", size=22, color=WHITE)
        simp_math = fml(r"= 2\pi r(r + h)", size=28, color=C_ACCENT)
        simp_grp  = VGroup(simp_cn, simp_math).arrange(RIGHT, buff=0.2)
        simp_grp.move_to([1.5, -2.0, 0])
        self.add_fixed_in_frame_mobjects(simp_grp)
        self.play(Write(simp_grp), run_time=0.6)

        self.wait(2.0)
        self.stop_ambient_camera_rotation()

        self.play(
            FadeOut(title), FadeOut(cyl), FadeOut(simp_grp),
            *[FadeOut(r) for r in row_objs],
            run_time=0.5
        )

    # --------------------------------------------------
    # Scene 6: 轴截面 (~8s)
    # --------------------------------------------------
    def _scene_cross_section(self):
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, run_time=0.3)

        r, h = CYL_R, CYL_H

        title = cn("轴截面", size=34, color=C_HL, y=6.8)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.6)

        # 透明圆柱
        cyl = make_cylinder(r, h, opacity=0.35)
        self.play(Create(cyl), run_time=0.8)

        # 截面: 过轴的竖直矩形 (在 xy-plane)
        cut_rect = Rectangle(
            width=r * 2, height=h,
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.35,
            stroke_width=2.5
        )
        # 这个矩形已经在 xy-plane (z=0), 即过 y 轴的平面, 正是轴截面
        self.play(FadeIn(cut_rect), run_time=0.7)

        explain = cn("过轴的截面 = 矩形", size=24, color=YELLOW, y=-4.5)
        self.add_fixed_in_frame_mobjects(explain)
        self.play(FadeIn(explain), run_time=0.4)

        self.wait(0.5)

        # 转到正视图查看截面
        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, run_time=1.0)

        self.play(FadeOut(cyl), FadeOut(explain), run_time=0.4)

        # 2D 截面矩形 (固定在 frame)
        cross_2d = Rectangle(
            width=r * 2 * 1.8,   # 缩放以适应屏幕
            height=h * 1.8,
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.30,
            stroke_width=2.5
        )
        cross_2d.move_to([0, 1.0, 0])
        self.add_fixed_in_frame_mobjects(cross_2d)
        self.play(FadeIn(cross_2d), FadeOut(cut_rect), run_time=0.6)

        # Brace: 宽 = 2r
        w_brace = Brace(cross_2d, DOWN, color=C_HL)
        w_math  = fml(r"2r", size=30, color=C_HL)
        w_math.next_to(w_brace, DOWN, buff=0.15)
        self.add_fixed_in_frame_mobjects(w_brace, w_math)
        self.play(FadeIn(w_brace), Write(w_math), run_time=0.5)

        # Brace: 高 = h
        hb_brace = Brace(cross_2d, RIGHT, color=C_FORMULA)
        hb_math  = fml(r"h", size=30, color=C_FORMULA)
        hb_math.next_to(hb_brace, RIGHT, buff=0.15)
        self.add_fixed_in_frame_mobjects(hb_brace, hb_math)
        self.play(FadeIn(hb_brace), Write(hb_math), run_time=0.5)

        # 面积公式
        a_cn   = cn("轴截面面积:", size=24, color=WHITE)
        a_math = fml(r"S = 2rh", size=30, color=C_HL)
        a_grp  = VGroup(a_cn, a_math).arrange(RIGHT, buff=0.2)
        a_grp.move_to([0, -5.5, 0])
        self.add_fixed_in_frame_mobjects(a_grp)
        self.play(Write(a_grp), run_time=0.8)

        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(cross_2d),
            FadeOut(w_brace), FadeOut(w_math),
            FadeOut(hb_brace), FadeOut(hb_math), FadeOut(a_grp),
            run_time=0.5
        )

    # --------------------------------------------------
    # Scene 7: 片尾 (~5s)
    # --------------------------------------------------
    def _scene_outro(self):
        self.move_camera(phi=70 * DEGREES, theta=-40 * DEGREES, run_time=0.5)

        # 旋转圆柱
        cyl = make_cylinder(CYL_R, CYL_H, opacity=0.55)
        self.play(Create(cyl), run_time=0.8)
        self.begin_ambient_camera_rotation(rate=0.25)

        # 公式摘要 (上方)
        summary = [
            (r"V = \pi r^2 h",         C_FORMULA),
            (r"S_{\rm lat} = 2\pi r h", BLUE_C),
            (r"S = 2\pi r(r+h)",        C_ACCENT),
            (r"S_{\rm axial} = 2rh",    C_HL),
        ]
        sum_objs = []
        for i, (latex, color) in enumerate(summary):
            f = fml(latex, size=24, color=color)
            f.move_to([0, 4.8 - i * 0.85, 0])
            self.add_fixed_in_frame_mobjects(f)
            sum_objs.append(f)
        self.play(*[FadeIn(o) for o in sum_objs], run_time=0.7)

        # 作者信息
        auth_name = cn(AUTHOR_NAME, size=30, color=WHITE, y=-4.5)
        auth_id   = cn(AUTHOR_ID,   size=24, color=GRAY_B, y=-5.3)
        follow    = cn("关注我，获得更多数学技巧!", size=26, color=C_HL, y=-6.2)
        self.add_fixed_in_frame_mobjects(auth_name, auth_id, follow)
        self.play(
            FadeIn(auth_name, shift=UP * 0.3),
            FadeIn(auth_id),
            FadeIn(follow, scale=1.05),
            run_time=0.8
        )

        self.wait(2.5)
        self.stop_ambient_camera_rotation()

        # 最终淡出
        all_objs = sum_objs + [auth_name, auth_id, follow, cyl]
        self.play(*[FadeOut(o) for o in all_objs], run_time=1.0)