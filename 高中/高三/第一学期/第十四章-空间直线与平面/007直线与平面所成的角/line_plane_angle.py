"""
直线与平面所成的角 - Line-Plane Angle
高三数学第十四章：空间直线与平面
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#1a1a2e"
C_ALPHA   = "#4FC3F7"
C_SLANT   = "#FFD54F"   # 斜线
C_PROJ    = "#F06292"   # 射影
C_ANGLE   = "#A5D6A7"   # 角
C_PERP    = "#CE93D8"   # 垂线（辅助）
C_POINT   = "#FF8A65"
C_GOLD    = "#FFD700"
C_GRAY    = GRAY_B
FONT_CN   = "PingFang SC"


def iso(x, y, z, sx=0.80, sy=0.52):
    px = (x - y) * sx * 0.5
    py = (x + y) * sy * 0.35 + z * sy
    return np.array([px, py, 0])


def right_angle_sq(corner, v1, v2, size=0.22, color=C_ANGLE):
    u1 = v1 / np.linalg.norm(v1) * size
    u2 = v2 / np.linalg.norm(v2) * size
    return Polygon(corner, corner+u1, corner+u1+u2, corner+u2,
                   color=color, stroke_width=1.8, fill_opacity=0)


class LinePlaneAngleScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()
        self.scene_1_opening()
        self.scene_2_oblique_line()
        self.scene_3_definition()
        self.scene_4_method()
        self.scene_5_minimum_angle()
        self.scene_6_summary()
        self.scene_7_outro()

    # ============================================================
    def setup_geometry(self):
        """
        核心几何：斜线 PA, 斜足 A（在平面α上），
        垂足 H（A在α上, H=A因为PA直接斜插平面），
        射影 OA'（斜线在平面上的正射影），
        线面角 θ = ∠PAO'
        """
        # 平面 α (z=0)
        self.plane_verts = [
            iso(-3.0, -1.8, 0), iso(3.0, -1.8, 0),
            iso(3.0,   1.8, 0), iso(-3.0,  1.8, 0),
        ]

        # 斜足 A（斜线与平面的交点）
        self.A     = iso( 0.5, -0.2, 0)    # 平面上
        # 斜线上一点 P（在平面上方）
        self.P     = iso(-1.0, -0.2, 2.2)  # 斜线端点（上方）
        # 从P向α作垂线，垂足 H
        # 在等角投影中：P的z=2.2, H是P正下方 (x=P_3d_x, y=P_3d_y, z=0)
        # 已知 P = iso(-1, -0.2, 2.2), 则 H = iso(-1, -0.2, 0)
        self.H     = iso(-1.0, -0.2, 0)   # P在α上的垂足
        # 射影 A'：连接斜足A和垂足H的线段（HA' 就是射影方向）
        # 实际上射影是从斜足A到垂足H的连线在平面内
        # 但更清晰的定义：斜线 PA 在平面 α 上的射影 = 直线 AH（射影线）
        # 线面角 θ = ∠PAH（斜线PA与射影AH的夹角）

        # 3D坐标
        P3d = np.array([-1.0, -0.2, 2.2])
        A3d = np.array([ 0.5, -0.2, 0.0])
        H3d = np.array([-1.0, -0.2, 0.0])  # P正下方

        # 斜线方向 AP
        PA3d  = P3d - A3d
        # 射影方向 AH
        AH3d  = H3d - A3d

        # 验证 PH ⊥ α（PH沿z轴）
        PH3d  = H3d - P3d
        self.PH_perp_alpha = (abs(PH3d[0]) < 1e-9 and abs(PH3d[1]) < 1e-9)

        # 验证 H 在射影上（AH在平面内）
        self.H_in_proj = abs(H3d[2]) < 1e-9

        # 线面角 (3D)
        cos_theta = np.dot(PA3d, AH3d) / (np.linalg.norm(PA3d) * np.linalg.norm(AH3d))
        self.theta_deg = np.degrees(np.arccos(np.clip(abs(cos_theta), 0, 1)))

        # 2D 投影中的角弧计算
        self.v_AP_2d = self.P - self.A    # 2D 向量 A→P
        self.v_AH_2d = self.H - self.A    # 2D 向量 A→H（射影）
        n_AP = self.v_AP_2d[:2] / np.linalg.norm(self.v_AP_2d[:2])
        n_AH = self.v_AH_2d[:2] / np.linalg.norm(self.v_AH_2d[:2])
        cos2d = np.dot(n_AP, n_AH)
        self.angle_2d_deg = np.degrees(np.arccos(np.clip(cos2d, -1, 1)))
        # 叉积判断方向
        self.cross2d = n_AP[0]*n_AH[1] - n_AP[1]*n_AH[0]

        # ---- Scene 5: 最小角定理 ----
        # 在平面内过A作不同方向的直线，与PA所成角 ≥ 线面角
        # 展示 3 条方向线
        dirs_2d = [
            iso( 2.0,  0.5, 0) - self.A,   # 射影方向（最小角）
            iso( 1.5,  1.5, 0) - self.A,   # 偏左方向（较大角）
            iso( 2.0, -0.8, 0) - self.A,   # 偏右方向（较大角）
        ]
        self.s5_dirs = dirs_2d
        self.s5_A    = self.A

        # ---- 边界检查 ----
        all_pts = [self.A, self.P, self.H]
        for pt in all_pts:
            assert abs(pt[0]) <= 4.5, f"X超界: {pt}"
            assert abs(pt[1]) <= 7.0, f"Y超界: {pt}"

        assert self.PH_perp_alpha, "PH 应垂直于平面α"
        assert self.H_in_proj, "H 应在平面α上"
        assert 0 < self.theta_deg <= 90, f"线面角应在(0°,90°], 实际: {self.theta_deg:.1f}°"

        print("✓ 几何数据初始化完成")
        print(f"  线面角 (3D) = {self.theta_deg:.1f}°")
        print(f"  2D投影显示角 = {self.angle_2d_deg:.1f}° (仅视觉参考)")

    # ============================================================
    def scene_1_opening(self):
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT_CN, font_size=18, color=C_GRAY
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author, shift=DOWN*0.2), run_time=0.4)

        hook = Text("斜线与平面所成的角怎么求？",
                    font=FONT_CN, font_size=36, color=C_GOLD).move_to(UP * 5.6)
        sub  = Text("关键：找射影，算夹角",
                    font=FONT_CN, font_size=26, color=C_GRAY).move_to(UP * 4.8)
        self.play(Write(hook), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(hook), FadeOut(sub), run_time=0.4)

    # ============================================================
    def scene_2_oblique_line(self):
        """展示斜线的概念"""
        title = Text("斜线的概念", font=FONT_CN, font_size=36,
                     color=C_SLANT).move_to(UP * 6.1)
        self.play(Write(title), run_time=0.5)

        plane = Polygon(*self.plane_verts, color=C_ALPHA, fill_color=C_ALPHA,
                        fill_opacity=0.13, stroke_width=2)
        alpha_lbl = MathTex(r"\alpha", color=C_ALPHA, font_size=40).move_to(
            iso(2.7, 1.5, 0))
        self.play(Create(plane), Write(alpha_lbl), run_time=0.7)

        # 斜线 PA
        slant = Line(self.A, self.P, color=C_SLANT, stroke_width=3.5)
        dot_A = Dot(self.A, radius=0.10, color=C_POINT)
        dot_P = Dot(self.P, radius=0.10, color=C_POINT)
        lA    = Text("A", font=FONT_CN, font_size=22, color=C_POINT).next_to(
            self.A, DOWN+RIGHT, buff=0.07)
        lP    = Text("P", font=FONT_CN, font_size=22, color=C_POINT).next_to(
            self.P, UP, buff=0.07)
        self.play(Create(slant), FadeIn(dot_A), FadeIn(dot_P),
                  Write(lA), Write(lP), run_time=0.7)

        desc1 = Text("与平面相交但不垂直的直线", font=FONT_CN, font_size=24,
                     color=WHITE).move_to(DOWN * 3.0)
        desc2 = Text("叫做平面的斜线", font=FONT_CN, font_size=22,
                     color=C_SLANT).move_to(DOWN * 3.7)
        desc3 = Text("A 称为斜足", font=FONT_CN, font_size=20,
                     color=C_GRAY).move_to(DOWN * 4.4)
        self.play(FadeIn(desc1, shift=UP*0.2), run_time=0.4)
        self.play(FadeIn(desc2), FadeIn(desc3), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(plane), FadeOut(alpha_lbl),
            FadeOut(slant), FadeOut(dot_A), FadeOut(dot_P),
            FadeOut(lA), FadeOut(lP),
            FadeOut(desc1), FadeOut(desc2), FadeOut(desc3),
            run_time=0.5
        )

    # ============================================================
    def scene_3_definition(self):
        """线面角的定义"""
        title = Text("线面角的定义", font=FONT_CN, font_size=36,
                     color=C_ANGLE).move_to(UP * 6.1)
        self.play(Write(title), run_time=0.5)

        plane = Polygon(*self.plane_verts, color=C_ALPHA, fill_color=C_ALPHA,
                        fill_opacity=0.13, stroke_width=2)
        alpha_lbl = MathTex(r"\alpha", color=C_ALPHA, font_size=38).move_to(
            iso(2.7, 1.5, 0))
        self.play(Create(plane), Write(alpha_lbl), run_time=0.6)

        # 斜线 PA
        slant = Line(self.A, self.P, color=C_SLANT, stroke_width=3.5)
        dot_A = Dot(self.A, radius=0.10, color=C_POINT)
        dot_P = Dot(self.P, radius=0.10, color=C_POINT)
        lA    = Text("A", font=FONT_CN, font_size=22, color=C_POINT).next_to(
            self.A, DOWN+RIGHT, buff=0.07)
        lP    = Text("P", font=FONT_CN, font_size=22, color=C_POINT).next_to(
            self.P, UP, buff=0.07)
        self.play(Create(slant), FadeIn(dot_A), FadeIn(dot_P),
                  Write(lA), Write(lP), run_time=0.6)

        # 垂线 PH（虚线）
        perp_v = DashedLine(self.P, self.H, color=C_PERP,
                            dash_length=0.1, stroke_width=2)
        dot_H  = Dot(self.H, radius=0.09, color=C_PERP)
        lH     = Text("H", font=FONT_CN, font_size=20, color=C_PERP).next_to(
            self.H, DOWN, buff=0.07)
        perp_note = Text("PH ⊥ α", font=FONT_CN, font_size=20,
                         color=C_PERP).move_to(np.array([-2.8, -0.5, 0]))
        self.play(Create(perp_v), FadeIn(dot_H), Write(lH), run_time=0.5)
        self.play(FadeIn(perp_note), run_time=0.3)

        # 垂足处直角符号
        v_ph2d = (self.H - self.P) / np.linalg.norm(self.H - self.P)
        h_dir  = np.array([1, 0, 0])
        ra_ph  = right_angle_sq(self.H, v_ph2d, h_dir, size=0.20, color=C_PERP)
        self.play(Create(ra_ph), run_time=0.3)

        # 射影 AH（红线）
        proj_line = Line(self.A, self.H, color=C_PROJ, stroke_width=3.5)
        proj_note = Text("AH = PA 在 α 上的射影", font=FONT_CN, font_size=20,
                         color=C_PROJ).move_to(DOWN * 3.5)
        self.play(Create(proj_line), run_time=0.5)
        self.play(FadeIn(proj_note, shift=UP*0.2), run_time=0.4)

        # 角弧：∠PAH
        n_AP = self.v_AP_2d[:2] / np.linalg.norm(self.v_AP_2d[:2])
        n_AH = self.v_AH_2d[:2] / np.linalg.norm(self.v_AH_2d[:2])
        start_ang  = np.arctan2(n_AH[1], n_AH[0])
        sweep_ang  = np.arccos(np.clip(np.dot(n_AP, n_AH), -1, 1))
        if self.cross2d < 0:
            sweep_ang = -sweep_ang

        arc = Arc(radius=0.52, start_angle=start_ang, angle=sweep_ang,
                  color=C_ANGLE, stroke_width=2.5)
        arc.move_arc_center_to(self.A)

        mid_n = n_AH + n_AP
        if np.linalg.norm(mid_n) > 0.01:
            mid_n = mid_n / np.linalg.norm(mid_n)
        theta_pos = self.A + np.array([mid_n[0], mid_n[1], 0]) * 0.8
        theta_lbl = MathTex(r"\theta", color=C_ANGLE, font_size=30).move_to(theta_pos)
        self.play(Create(arc), Write(theta_lbl), run_time=0.6)

        formula = MathTex(r"\theta \in [0,\,\tfrac{\pi}{2}]",
                          color=C_GOLD, font_size=36).move_to(DOWN * 4.8)
        self.play(Write(formula), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(plane), FadeOut(alpha_lbl),
            FadeOut(slant), FadeOut(dot_A), FadeOut(dot_P),
            FadeOut(lA), FadeOut(lP),
            FadeOut(perp_v), FadeOut(dot_H), FadeOut(lH), FadeOut(perp_note),
            FadeOut(ra_ph),
            FadeOut(proj_line), FadeOut(proj_note),
            FadeOut(arc), FadeOut(theta_lbl), FadeOut(formula),
            run_time=0.5
        )

    # ============================================================
    def scene_4_method(self):
        """求线面角的方法"""
        title = Text("求线面角的方法", font=FONT_CN, font_size=34,
                     color=C_GOLD).move_to(UP * 6.1)
        self.play(Write(title), run_time=0.5)

        steps = [
            ("Step 1", "确定斜足 A（斜线与平面的交点）",   C_SLANT),
            ("Step 2", "作 PH ⊥ α，垂足为 H",             C_PERP),
            ("Step 3", "连 AH（即斜线的射影）",             C_PROJ),
            ("Step 4", "∠PAH 即为线面角 θ",               C_ANGLE),
        ]
        y = 4.4
        groups = VGroup()
        for (step, desc, col) in steps:
            t1 = Text(step, font=FONT_CN, font_size=24, color=col)
            t2 = Text(desc, font=FONT_CN, font_size=20, color=WHITE)
            row = VGroup(t1, t2).arrange(RIGHT, buff=0.4)
            row.move_to(np.array([0, y, 0]))
            groups.add(row)
            self.play(FadeIn(row, shift=RIGHT*0.3), run_time=0.4)
            y -= 1.5

        # 三角形关系图示
        plane_s = Polygon(*self.plane_verts, color=C_ALPHA, fill_color=C_ALPHA,
                          fill_opacity=0.10, stroke_width=1.5)
        slant_s   = Line(self.A, self.P, color=C_SLANT, stroke_width=2.5)
        perp_vs   = DashedLine(self.P, self.H, color=C_PERP, dash_length=0.08, stroke_width=2)
        proj_s    = Line(self.A, self.H, color=C_PROJ, stroke_width=2.5)
        da = Dot(self.A, radius=0.08, color=C_POINT)
        dp = Dot(self.P, radius=0.08, color=C_POINT)
        dh = Dot(self.H, radius=0.08, color=C_PERP)

        # 公式
        formula = VGroup(
            MathTex(r"\sin\theta = \frac{PH}{PA}", font_size=30, color=WHITE),
            MathTex(r"\cos\theta = \frac{AH}{PA}", font_size=30, color=WHITE),
        ).arrange(RIGHT, buff=0.8).move_to(DOWN * 0.5)

        self.play(
            Create(plane_s), Create(slant_s), Create(perp_vs), Create(proj_s),
            FadeIn(da), FadeIn(dp), FadeIn(dh),
            run_time=0.6
        )
        self.play(Write(formula), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(groups),
            FadeOut(plane_s), FadeOut(slant_s), FadeOut(perp_vs), FadeOut(proj_s),
            FadeOut(da), FadeOut(dp), FadeOut(dh), FadeOut(formula),
            run_time=0.5
        )

    # ============================================================
    def scene_5_minimum_angle(self):
        """最小角定理"""
        title = Text("最小角定理", font=FONT_CN, font_size=36,
                     color=C_GOLD).move_to(UP * 6.1)
        sub   = Text("斜线与平面内各直线所成角中，",
                     font=FONT_CN, font_size=22, color=C_GRAY).move_to(UP * 5.4)
        sub2  = Text("与射影所成角最小",
                     font=FONT_CN, font_size=24, color=C_PROJ).move_to(UP * 4.8)
        self.play(Write(title), FadeIn(sub), FadeIn(sub2), run_time=0.7)

        plane = Polygon(*self.plane_verts, color=C_ALPHA, fill_color=C_ALPHA,
                        fill_opacity=0.11, stroke_width=1.5)
        slant = Line(self.A, self.P, color=C_SLANT, stroke_width=3.5)
        da    = Dot(self.A, radius=0.10, color=C_POINT)
        dp    = Dot(self.P, radius=0.10, color=C_POINT)
        self.play(Create(plane), Create(slant), FadeIn(da), FadeIn(dp), run_time=0.6)

        # 射影（最小角方向，绿色）
        proj_e   = iso(-1.0, -0.2, 0)   # H 投影端点
        proj_ext = Line(self.A, proj_e,  color=C_PROJ, stroke_width=3.5)
        self.play(Create(proj_ext), run_time=0.4)

        # 其他两条方向线（较大角，灰色）
        end1 = self.A + np.array([1.8, 1.0, 0])
        end2 = self.A + np.array([1.6, -0.8, 0])
        dir1 = Line(self.A, end1, color=C_GRAY, stroke_width=2)
        dir2 = Line(self.A, end2, color=C_GRAY, stroke_width=2)
        self.play(Create(dir1), Create(dir2), run_time=0.4)

        # 标注：射影方向角最小
        arrow_min = CurvedArrow(
            np.array([-3.2, 1.5, 0]),
            proj_e + np.array([0, 0.1, 0]),
            color=C_PROJ, angle=-0.5
        )
        min_lbl = Text("最小角 θ", font=FONT_CN, font_size=22,
                       color=C_PROJ).move_to(np.array([-3.0, 1.9, 0]))
        self.play(Create(arrow_min), Write(min_lbl), run_time=0.5)

        note = Text("「最小角」= 线面角", font=FONT_CN, font_size=24,
                    color=WHITE).move_to(DOWN * 3.5)
        self.play(FadeIn(note, shift=UP*0.2), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(sub2),
            FadeOut(plane), FadeOut(slant), FadeOut(da), FadeOut(dp),
            FadeOut(proj_ext), FadeOut(dir1), FadeOut(dir2),
            FadeOut(arrow_min), FadeOut(min_lbl), FadeOut(note),
            run_time=0.5
        )

    # ============================================================
    def scene_6_summary(self):
        title = Text("核心总结", font=FONT_CN, font_size=36, color=C_GOLD).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        items = [
            ("斜线",    "与面相交但不垂直，交点=斜足",        C_SLANT),
            ("射影",    "过斜足，从斜线上一点向面作垂线连足",  C_PROJ),
            ("线面角",  "斜线 PA 与射影 AH 的夹角 ∠PAH",     C_ANGLE),
            ("范围",    r"θ ∈ [0, π/2]",                      C_GOLD),
            ("最小角",  "线面角是所有面内直线中最小角",         C_GRAY),
        ]
        y = 4.5
        groups = VGroup()
        for (name, desc, col) in items:
            box = RoundedRectangle(width=7.6, height=1.1, corner_radius=0.18,
                                   color=col, fill_color=col, fill_opacity=0.07,
                                   stroke_width=1.4).move_to(np.array([0, y, 0]))
            t1 = Text(name, font=FONT_CN, font_size=22, color=col)
            # Convert both colors to hex strings for comparison to avoid ManimColor vs str error
            col_hex = col if isinstance(col, str) else col.to_hex()
            c_gold_hex = C_GOLD if isinstance(C_GOLD, str) else C_GOLD.to_hex()
            if col_hex == c_gold_hex and "∈" in desc:
                t2 = MathTex(r"\theta \in [0,\,\tfrac{\pi}{2}]", font_size=22, color=WHITE)
            else:
                t2 = Text(desc, font=FONT_CN, font_size=18, color=WHITE)
            VGroup(t1, t2).arrange(RIGHT, buff=0.3).move_to(box.get_center())
            grp = VGroup(box, t1, t2)
            groups.add(grp)
            self.play(FadeIn(grp, shift=RIGHT*0.3), run_time=0.35)
            y -= 1.55

        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(groups), run_time=0.5)

    # ============================================================
    def scene_7_outro(self):
        big = Text("上海初高中数学直通车", font=FONT_CN, font_size=38, color=WHITE).move_to(UP * 1.5)
        uid = Text("@emptyandcalm", font=FONT_CN, font_size=28, color=C_GRAY).move_to(UP * 0.5)
        flw = Text("关注我，获得更多数学技巧！",
                   font=FONT_CN, font_size=30, color=C_GOLD).move_to(DOWN * 0.5)
        self.play(Transform(self.author, big), run_time=0.6)
        self.play(FadeIn(uid, shift=UP*0.2), run_time=0.4)
        self.play(FadeIn(flw, scale=1.05), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(self.author), FadeOut(uid), FadeOut(flw), run_time=0.8)