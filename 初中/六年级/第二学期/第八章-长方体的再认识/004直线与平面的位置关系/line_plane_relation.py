"""
直线与平面的位置关系
六年级 第二学期 第八章 - 长方体的再认识
manim -qh line_plane_relation.py LineAndPlane3D


TikTok 竖屏 1080×1920  |  作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ─── TikTok 竖屏配置 ───────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ─── 品牌 & 字体 ──────────────────────────────────────────────
FONT      = "Noto Sans CJK SC"
AUTHOR    = "上海初高中数学直通车"
AUTHOR_ID = "@emptyandcalm"

# ─── 调色板 ───────────────────────────────────────────────────
C_BG        = "#1a1a2e"
C_PLANE     = "#3a86ff"
C_IN        = "#2ecc71"
C_PARALLEL  = "#f39c12"
C_INTERSECT = "#e74c3c"
C_PERP      = "#bf5af2"

# ─── 几何常量（与 verify_geometry.py 一致）───────────────────
PLANE_W = 3.8
PLANE_D = 2.8


class LineAndPlane3D(ThreeDScene):
    """直线与平面三种位置关系 3D 教学动画"""

    # ═══════════════════════════════════════════════
    #  主构建流程
    # ═══════════════════════════════════════════════
    def construct(self):
        self.camera.background_color = C_BG
        self.setup_geometry()
        self.scene_opening()
        self.scene_case1_in_plane()
        self.scene_case2_parallel()
        self.scene_case3_intersect()
        self.scene_case4_perpendicular()
        self.scene_summary()
        self.scene_outro()

    # ═══════════════════════════════════════════════
    #  几何初始化（统一精确计算，禁止臆想坐标）
    # ═══════════════════════════════════════════════
    def setup_geometry(self):
        w, d = PLANE_W, PLANE_D

        # 平面四顶点（z = 0 平面）
        self.PL_A = np.array([-w/2, -d/2, 0.0])
        self.PL_B = np.array([ w/2, -d/2, 0.0])
        self.PL_C = np.array([ w/2,  d/2, 0.0])
        self.PL_D = np.array([-w/2,  d/2, 0.0])

        # 情况1：直线在平面内（z=0 同平面，沿 x 方向）
        self.ln_in_s = np.array([-w/2 - 0.6,  0.4,  0.0])
        self.ln_in_e = np.array([ w/2 + 0.6,  0.4,  0.0])

        # 情况2：直线平行于平面（z = 1.6，方向同情况1）
        self.ln_par_s = np.array([-w/2 - 0.6,  0.4,  1.6])
        self.ln_par_e = np.array([ w/2 + 0.6,  0.4,  1.6])

        # 情况3：直线与平面相交（斜线，从 z=+2 穿到 z=-2）
        self.ln_int_s = np.array([-0.8, -d/2 - 0.5,  2.0])
        self.ln_int_e = np.array([ 0.8,  d/2 + 0.5, -2.0])
        # 精确计算交点：令 z=0，参数化 P = s + t*(e-s)
        t_int = -self.ln_int_s[2] / (self.ln_int_e[2] - self.ln_int_s[2])
        self.int_point = self.ln_int_s + t_int * (self.ln_int_e - self.ln_int_s)
        # → int_point = (0, 0, 0)，在平面中心

        # 情况4：直线垂直于平面（沿 z 轴方向）
        fx, fy = 0.5, 0.3
        self.ln_perp_s  = np.array([fx, fy, -1.8])
        self.ln_perp_e  = np.array([fx, fy,  1.8])
        self.perp_foot  = np.array([fx, fy,  0.0])   # 垂足（精确）

        print("✅ 几何初始化完成")
        print(f"   交点坐标: {self.int_point}")
        print(f"   垂足坐标: {self.perp_foot}")

    # ═══════════════════════════════════════════════
    #  工具函数
    # ═══════════════════════════════════════════════
    def make_plane(self, color=C_PLANE, opacity=0.35, sw=2.5):
        """创建半透明平面多边形"""
        return Polygon(
            self.PL_A, self.PL_B, self.PL_C, self.PL_D,
            fill_color=color, fill_opacity=opacity,
            stroke_color=color, stroke_width=sw
        )

    def make_alpha_label(self):
        """在平面左上角放置 α 标签（3D 世界坐标）"""
        lbl = MathTex(r"\alpha", font_size=38, color=C_PLANE)
        lbl.move_to(self.PL_D + np.array([-0.35, 0.3, 0.1]))
        return lbl

    def make_right_angle_mark(self, corner, toward_line, toward_plane, sz=0.22):
        """在垂足处创建直角小方块（3D 世界坐标）"""
        v1 = (toward_line  - corner)
        v1 = v1 / np.linalg.norm(v1) * sz
        v2 = (toward_plane - corner)
        v2 = v2 / np.linalg.norm(v2) * sz
        return Polygon(
            corner, corner + v1, corner + v1 + v2, corner + v2,
            color=YELLOW, stroke_width=2.5, fill_opacity=0
        )

    def ftext(self, txt, size, color, pos, bold=False):
        """创建 fixed_in_frame 中文文本（2D 覆层）"""
        t = Text(txt, font=FONT, font_size=size, color=color,
                 weight=BOLD if bold else NORMAL)
        t.move_to(pos)
        self.add_fixed_in_frame_mobjects(t)
        return t

    def fmath(self, tex, size, color, pos):
        """创建 fixed_in_frame 数学公式（2D 覆层）"""
        t = MathTex(tex, font_size=size, color=color)
        t.move_to(pos)
        self.add_fixed_in_frame_mobjects(t)
        return t

    def fade_remove(self, *mobs):
        """淡出并从 fixed_in_frame 中移除"""
        self.play(*[FadeOut(m) for m in mobs], run_time=0.45)
        self.remove_fixed_in_frame_mobjects(*mobs)

    # ═══════════════════════════════════════════════
    #  Scene 1 – 开场钩子
    # ═══════════════════════════════════════════════
    def scene_opening(self):
        self.set_camera_orientation(phi=72*DEGREES, theta=-50*DEGREES)

        # 作者标识（常驻顶部）
        self._author_badge = self.ftext(
            f"{AUTHOR}  {AUTHOR_ID}", 18, GRAY_B, UP * 7.3
        )
        self.play(FadeIn(self._author_badge, shift=DOWN * 0.15), run_time=0.3)

        # 标题
        title = self.ftext("直线与平面", 58, GOLD, UP * 5.8, bold=True)
        sub   = self.ftext("三种位置关系", 36, WHITE, UP * 4.8)
        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)

        # 3D 平面淡入
        plane = self.make_plane()
        self.play(Create(plane), run_time=0.9)

        # 三条线依次出现
        l1 = Line3D(self.ln_in_s,  self.ln_in_e,  color=C_IN,        thickness=0.04)
        l2 = Line3D(self.ln_par_s, self.ln_par_e, color=C_PARALLEL,  thickness=0.04)
        l3 = Line3D(self.ln_int_s, self.ln_int_e, color=C_INTERSECT, thickness=0.04)
        self.play(
            LaggedStart(Create(l1), Create(l2), Create(l3), lag_ratio=0.28),
            run_time=1.2
        )

        # 环境旋转增强立体感
        hook = self.ftext("这条线和这个面\n有几种位置关系?", 30, YELLOW, DOWN * 5.2)
        self.play(FadeIn(hook, shift=UP * 0.2), run_time=0.5)
        self.begin_ambient_camera_rotation(rate=0.12)
        self.wait(2.2)
        self.stop_ambient_camera_rotation()

        # 复位角度
        self.move_camera(phi=72*DEGREES, theta=-50*DEGREES, run_time=0.6)

        # 清理
        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(hook),
            FadeOut(l1), FadeOut(l2), FadeOut(l3), FadeOut(plane),
            run_time=0.5
        )
        self.remove_fixed_in_frame_mobjects(title, sub, hook)

    # ═══════════════════════════════════════════════
    #  Scene 2 – 情况一：直线在平面内  l ⊂ α
    # ═══════════════════════════════════════════════
    def scene_case1_in_plane(self):
        # ─ 2D 覆层 ─
        title   = self.ftext("情况一  直线在平面内", 34, C_IN,     UP * 6.3, bold=True)
        tag     = self.fmath(r"l \subset \alpha",    44, C_IN,     DOWN * 4.2)
        prop    = self.ftext("有无数个公共点",         26, GRAY_A,  DOWN * 5.4)

        # ─ 3D 对象 ─
        plane = self.make_plane()
        alpha = self.make_alpha_label()
        line  = Line3D(self.ln_in_s, self.ln_in_e, color=C_IN, thickness=0.06)
        l_lbl = MathTex("l", font_size=38, color=C_IN)
        l_lbl.move_to(self.ln_in_e + np.array([0.4, 0.2, 0.1]))

        self.play(FadeIn(title, shift=DOWN * 0.2), Create(plane), run_time=0.7)
        self.play(Create(line), FadeIn(alpha), run_time=0.9)
        self.play(FadeIn(l_lbl), run_time=0.3)

        # 无数个公共点动画：沿线分布黄点
        dots = VGroup(*[
            Dot3D(
                self.ln_in_s + t * (self.ln_in_e - self.ln_in_s),
                color=YELLOW, radius=0.09
            )
            for t in np.linspace(0.1, 0.9, 7)
        ])
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.3) for d in dots], lag_ratio=0.1),
            run_time=0.9
        )
        self.play(Write(tag), FadeIn(prop), run_time=0.7)
        self.wait(2.0)

        # ─ 清理 ─
        self.fade_remove(title, tag, prop)
        self.play(
            FadeOut(plane), FadeOut(alpha), FadeOut(line),
            FadeOut(l_lbl), FadeOut(dots),
            run_time=0.45
        )

    # ═══════════════════════════════════════════════
    #  Scene 3 – 情况二：直线与平面平行  l ∥ α
    # ═══════════════════════════════════════════════
    def scene_case2_parallel(self):
        title  = self.ftext("情况二  直线与平面平行", 34, C_PARALLEL, UP * 6.3, bold=True)
        tag    = self.fmath(r"l \parallel \alpha",   44, C_PARALLEL, DOWN * 4.2)
        prop   = self.ftext("没有公共点",              26, GRAY_A,    DOWN * 5.4)

        plane = self.make_plane()
        alpha = self.make_alpha_label()
        line  = Line3D(self.ln_par_s, self.ln_par_e, color=C_PARALLEL, thickness=0.06)
        l_lbl = MathTex("l", font_size=38, color=C_PARALLEL)
        l_lbl.move_to(self.ln_par_e + np.array([0.4, 0.2, 0.1]))

        self.play(FadeIn(title, shift=DOWN * 0.2), Create(plane), run_time=0.7)
        self.play(Create(line), FadeIn(alpha), FadeIn(l_lbl), run_time=0.9)

        # 虚线展示"距离"（无公共点的视觉证据）
        gap_lines = VGroup()
        for t in [0.2, 0.5, 0.8]:
            pt   = self.ln_par_s + t * (self.ln_par_e - self.ln_par_s)
            foot = np.array([pt[0], pt[1], 0.0])   # 垂直投影到 z=0
            gap_lines.add(
                DashedLine(pt, foot, color=GRAY_B,
                           dash_length=0.1, stroke_width=1.8)
            )
        self.play(Create(gap_lines), run_time=0.7)
        self.play(Write(tag), FadeIn(prop), run_time=0.7)

        # 小幅俯仰镜头，突出"悬空"效果
        self.move_camera(phi=60*DEGREES, theta=-50*DEGREES, run_time=0.9)
        self.wait(0.8)
        self.move_camera(phi=72*DEGREES, theta=-50*DEGREES, run_time=0.8)
        self.wait(0.6)

        self.fade_remove(title, tag, prop)
        self.play(
            FadeOut(plane), FadeOut(alpha), FadeOut(line),
            FadeOut(l_lbl), FadeOut(gap_lines),
            run_time=0.45
        )

    # ═══════════════════════════════════════════════
    #  Scene 4 – 情况三：直线与平面相交  l ∩ α = {P}
    # ═══════════════════════════════════════════════
    def scene_case3_intersect(self):
        title  = self.ftext("情况三  直线与平面相交", 34, C_INTERSECT, UP * 6.3, bold=True)
        tag    = self.fmath(r"l \cap \alpha = \{P\}", 40, C_INTERSECT, DOWN * 4.2)
        prop   = self.ftext("有且只有一个公共点",       26, GRAY_A,     DOWN * 5.4)

        plane = self.make_plane()
        alpha = self.make_alpha_label()
        line  = Line3D(self.ln_int_s, self.ln_int_e, color=C_INTERSECT, thickness=0.06)
        l_lbl = MathTex("l", font_size=38, color=C_INTERSECT)
        l_lbl.move_to(self.ln_int_s + np.array([-0.1, 0.0, 0.35]))

        self.play(FadeIn(title, shift=DOWN * 0.2), Create(plane), run_time=0.7)
        self.play(Create(line), FadeIn(alpha), FadeIn(l_lbl), run_time=1.0)

        # 唯一交点：闪光强调
        p_dot = Dot3D(self.int_point, color=YELLOW, radius=0.15)
        p_lbl = Text("P", font=FONT, font_size=28, color=YELLOW)
        p_lbl.move_to(self.int_point + np.array([0.38, 0.38, 0.12]))

        self.play(FadeIn(p_dot, scale=0.2), run_time=0.4)
        self.play(Flash(p_dot, color=YELLOW, flash_radius=0.55, num_lines=10),
                  run_time=0.45)
        self.play(FadeIn(p_lbl), run_time=0.3)
        self.play(Write(tag), FadeIn(prop), run_time=0.7)

        # 短暂旋转，让学生看清"穿透"效果
        self.move_camera(phi=72*DEGREES, theta=-25*DEGREES, run_time=1.0)
        self.wait(0.6)
        self.move_camera(phi=72*DEGREES, theta=-50*DEGREES, run_time=0.8)
        self.wait(0.8)

        self.fade_remove(title, tag, prop)
        self.play(
            FadeOut(plane), FadeOut(alpha), FadeOut(line),
            FadeOut(l_lbl), FadeOut(p_dot), FadeOut(p_lbl),
            run_time=0.45
        )

    # ═══════════════════════════════════════════════
    #  Scene 5 – 特殊情况：线面垂直  l ⊥ α
    # ═══════════════════════════════════════════════
    def scene_case4_perpendicular(self):
        title  = self.ftext("特殊情况  线面垂直",  38, C_PERP,   UP * 6.3, bold=True)
        note   = self.ftext("(相交的特殊情况)",    22, GRAY_B,   UP * 5.55)
        tag    = self.fmath(r"l \perp \alpha",   52, C_PERP,   DOWN * 4.2)
        prop   = self.ftext("垂直于平面内所有直线", 24, GRAY_A,  DOWN * 5.4)

        plane = self.make_plane()
        alpha = self.make_alpha_label()
        line  = Line3D(self.ln_perp_s, self.ln_perp_e, color=C_PERP, thickness=0.07)
        l_lbl = MathTex("l", font_size=38, color=C_PERP)
        l_lbl.move_to(self.ln_perp_e + np.array([0.4, 0.0, 0.15]))

        self.play(
            FadeIn(title, shift=DOWN * 0.2), FadeIn(note),
            Create(plane), run_time=0.7
        )
        self.play(Create(line), FadeIn(alpha), FadeIn(l_lbl), run_time=1.0)

        # 垂足
        foot_dot = Dot3D(self.perp_foot, color=YELLOW, radius=0.11)
        self.play(FadeIn(foot_dot, scale=0.3), run_time=0.4)

        # 直角标记（手动 Polygon 方式，兼容 3D）
        ra = self.make_right_angle_mark(
            self.perp_foot,
            self.ln_perp_e,                          # 朝向直线上方
            self.perp_foot + np.array([0.4, 0.0, 0]) # 朝向平面内 x 方向
        )
        self.play(Create(ra), run_time=0.4)

        # 平面内多条线 → 全部与垂线垂直
        plane_lines = VGroup()
        for ang in np.linspace(0, np.pi, 5):
            d_vec = np.array([np.cos(ang), np.sin(ang), 0]) * 1.7
            plane_lines.add(
                DashedLine(
                    self.perp_foot - d_vec, self.perp_foot + d_vec,
                    color=GRAY_B, dash_length=0.1, stroke_width=1.5
                )
            )
        self.play(
            LaggedStart(*[Create(pl) for pl in plane_lines], lag_ratio=0.15),
            run_time=0.9
        )
        self.play(Write(tag), FadeIn(prop), run_time=0.7)

        # 旋转一圈，感受"和所有方向都垂直"
        self.move_camera(phi=72*DEGREES, theta=-50 * DEGREES, run_time=0.3)
        self.begin_ambient_camera_rotation(rate=0.18)
        self.wait(3.0)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=72*DEGREES, theta=-50*DEGREES, run_time=0.5)

        self.fade_remove(title, note, tag, prop)
        self.play(
            FadeOut(plane), FadeOut(alpha), FadeOut(line), FadeOut(l_lbl),
            FadeOut(foot_dot), FadeOut(ra), FadeOut(plane_lines),
            run_time=0.45
        )

    # ═══════════════════════════════════════════════
    #  Scene 6 – 总结
    # ═══════════════════════════════════════════════
    def scene_summary(self):
        # 摄像机切到正视（近似 2D）
        self.move_camera(phi=0*DEGREES, theta=-90*DEGREES, run_time=0.8)

        title = self.ftext("总结：三种位置关系", 40, GOLD, UP * 6.3, bold=True)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)

        rows = [
            # (名称,              公式字符串,                     描述,            颜色,       Y坐标)
            ("① 直线在平面内",   r"l \subset \alpha",            "无数个公共点",  C_IN,        UP  * 3.8),
            ("② 直线与平面平行", r"l \parallel \alpha",          "没有公共点",    C_PARALLEL,  UP  * 1.5),
            ("③ 直线与平面相交", r"l \cap \alpha = \{P\}",       "一个公共点",    C_INTERSECT, DOWN* 0.8),
        ]

        all_row_mobs = []
        for name, tex, desc, color, ypos in rows:
            # 行名称
            n = self.ftext(name, 27, color, ypos + LEFT * 0.8)
            # 公式
            f = self.fmath(tex, 32, WHITE, ypos + RIGHT * 2.7)
            # 描述（稍下方）
            d = self.ftext(desc, 21, GRAY_A, ypos + DOWN * 0.46)
            # 分割线
            sep = Line(LEFT * 3.6, RIGHT * 3.6, stroke_width=1, color="#2d3561")
            sep.move_to(ypos + DOWN * 0.78)
            self.add_fixed_in_frame_mobjects(sep)

            self.play(
                FadeIn(n, shift=RIGHT * 0.15),
                Write(f),
                FadeIn(d),
                Create(sep),
                run_time=0.55
            )
            all_row_mobs += [n, f, d, sep]
            self.wait(0.2)

        # 线面垂直特殊说明
        star_txt = self.ftext("⭐ 垂直是相交的特殊情况", 24, C_PERP, DOWN * 2.5)
        star_tex = self.fmath(r"l \perp \alpha", 42, C_PERP, DOWN * 3.55)
        self.play(FadeIn(star_txt, shift=UP * 0.1), Write(star_tex), run_time=0.8)

        self.wait(2.2)

        # 清理所有总结元素
        self.fade_remove(title, star_txt, star_tex, *all_row_mobs)

    # ═══════════════════════════════════════════════
    #  Scene 7 – 片尾
    # ═══════════════════════════════════════════════
    def scene_outro(self):
        a_name = self.ftext(AUTHOR,          44, WHITE,  UP * 1.8, bold=True)
        a_id   = self.ftext(AUTHOR_ID,       30, GRAY_B, UP * 0.8)
        follow = self.ftext("关注我，获得更多数学技巧!", 28, YELLOW, DOWN * 0.8)

        self.play(FadeIn(a_name, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(a_id),                   run_time=0.4)
        self.play(FadeIn(follow, scale=1.08),      run_time=0.5)

        # 四色小圆装饰
        icons = VGroup(*[
            Circle(radius=0.23,
                   fill_color=c, fill_opacity=0.92, stroke_width=0)
            .move_to(DOWN * 2.5 + RIGHT * (i - 1.5) * 1.1)
            for i, c in enumerate([C_IN, C_PARALLEL, C_INTERSECT, C_PERP])
        ])
        for ic in icons:
            self.add_fixed_in_frame_mobjects(ic)
        self.play(
            LaggedStart(*[GrowFromCenter(ic) for ic in icons], lag_ratio=0.18),
            run_time=0.8
        )
        self.wait(1.5)
        self.play(
            FadeOut(a_name), FadeOut(a_id), FadeOut(follow), FadeOut(icons),
            FadeOut(self._author_badge),
            run_time=0.7
        )
        self.remove_fixed_in_frame_mobjects(a_name, a_id, follow, *icons,
                                            self._author_badge)