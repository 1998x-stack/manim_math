"""
空间直线的位置关系 - Spatial Line Position Relationships
高三数学第十四章：空间直线与平面
目标受众: 高三学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ===== 颜色 =====
BG_COLOR   = "#1a1a2e"
C_FLOOR    = "#4FC3F7"   # 浅蓝  — 平面（地面）
C_LINE_A   = "#FFD54F"   # 金黄  — 直线a
C_LINE_B   = "#F06292"   # 粉红  — 直线b
C_POINT    = "#FF8A65"   # 橙红  — 点
C_ANGLE    = "#A5D6A7"   # 浅绿  — 角度
C_SKEW     = "#CE93D8"   # 紫色  — 异面
C_GOLD     = "#FFD700"
C_GRAY     = GRAY_B
FONT_CN    = "PingFang SC"


# ============================================================
# 透视辅助：3-D → 2-D 等角投影
# ============================================================
def iso(x, y, z, sx=0.85, sy=0.6, ox=0, oy=0):
    """
    简单等角投影: 3D坐标 → 2D屏幕坐标
    x轴: 向右下 (±45°)
    y轴: 向右上 (±45°)
    z轴: 向上
    """
    px = ox + sx * (x - y) * np.cos(np.radians(30))
    py = oy + sy * (x + y) * np.sin(np.radians(30)) + z * sy
    return np.array([px, py, 0])


def make_floor_plane(cx, cy, W=4.0, D=2.0, sx=0.85, sy=0.6, **kwargs):
    """在XY平面(z=0)上绘制矩形平面的透视四边形"""
    corners_3d = [
        (cx - W/2, cy - D/2, 0),
        (cx + W/2, cy - D/2, 0),
        (cx + W/2, cy + D/2, 0),
        (cx - W/2, cy + D/2, 0),
    ]
    corners_2d = [iso(x, y, z, sx, sy) for x, y, z in corners_3d]
    return Polygon(*corners_2d, **kwargs)


class SpatialLinesScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_intersect()
        self.scene_3_parallel()
        self.scene_4_skew()
        self.scene_5_skew_angle()
        self.scene_6_common_perp()
        self.scene_7_summary()
        self.scene_8_outro()

    # ============================================================
    def setup_geometry(self):
        """统一初始化所有几何数据（等角投影坐标）"""
        # ---- Scene 2: 相交直线 ----
        # 两直线在z=0平面上相交
        # 3D坐标 → 2D (使用 iso)
        self.s2_P  = iso(0, 0, 0)        # 交点
        self.s2_A1 = iso(-2, -1, 0)      # 直线a端点1
        self.s2_A2 = iso( 2,  1, 0)      # 直线a端点2
        self.s2_B1 = iso(-1.5, 1.2, 0)  # 直线b端点1
        self.s2_B2 = iso( 1.5, -1.2, 0) # 直线b端点2

        # ---- Scene 3: 平行直线 ----
        # 两平行直线都在z=0平面
        self.s3_A1 = iso(-2, 0.8, 0)
        self.s3_A2 = iso( 2, 0.8, 0)
        self.s3_B1 = iso(-2, -0.8, 0)
        self.s3_B2 = iso( 2, -0.8, 0)

        # ---- Scene 4: 异面直线 ----
        # 直线a 在z=0平面（"地面"）
        # 直线b 在z=1.5高度（"空中"）且方向不同
        self.s4_A1 = iso(-2,  0, 0)
        self.s4_A2 = iso( 2,  0, 0)
        self.s4_B1 = iso( 0, -2, 1.5)
        self.s4_B2 = iso( 0,  2, 1.5)
        # 地面平面角点
        self.s4_floor_corners = [
            iso(-2.5, -1.8, 0),
            iso( 2.5, -1.8, 0),
            iso( 2.5,  1.8, 0),
            iso(-2.5,  1.8, 0),
        ]

        # ---- Scene 5: 异面直线所成角 ----
        # 过O点分别作两直线的平行线
        self.s5_O    = iso(0, 0, 0)
        self.s5_OA1  = iso(-1.8, 0, 0)
        self.s5_OA2  = iso( 1.8, 0, 0)
        self.s5_OB1  = iso(0, -1.8, 1.5)
        self.s5_OB2  = iso(0,  1.8, 1.5)
        # 成角（需要用向量计算）
        dir_a = np.array([1, 0, 0])   # 直线a方向
        dir_b = np.array([0, 1, 0])   # 直线b方向（3D空间中）
        cos_theta = np.dot(dir_a, dir_b) / (np.linalg.norm(dir_a) * np.linalg.norm(dir_b))
        self.s5_angle_3d = np.degrees(np.arccos(np.clip(abs(cos_theta), 0, 1)))

        # ---- Scene 6: 公垂线 ----
        # 公垂线连接 s4_A 和 s4_B
        # 垂足在 a: iso(0, 0, 0), 垂足在 b: iso(0, 0, 1.5)
        self.s6_foot_a = iso(0, 0, 0)
        self.s6_foot_b = iso(0, 0, 1.5)

        # ---- 验证 ----
        assert abs(self.s5_angle_3d - 90.0) < 0.1, \
            f"异面直线所成角应为90°（示例），实际: {self.s5_angle_3d:.1f}°"
        print("✓ 几何数据初始化完成")
        print(f"  示例异面角 = {self.s5_angle_3d:.1f}°")

    # ============================================================
    # Scene 1: 开场
    # ============================================================
    def scene_1_opening(self):
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT_CN, font_size=18, color=C_GRAY
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text("空间两直线，关系有几种？",
                    font=FONT_CN, font_size=40, color=C_GOLD).move_to(UP * 5.5)
        self.play(Write(hook), run_time=0.8)

        # 三种关系预览：简单线段
        y_base = 3.5
        gap = 1.3
        labels_data = [("相交", C_LINE_A), ("平行", C_LINE_B), ("异面", C_SKEW)]
        prev_group = VGroup()
        for i, (txt, col) in enumerate(labels_data):
            lbl = Text(txt, font=FONT_CN, font_size=30, color=col)
            lbl.move_to(np.array([-2.5 + i * 2.5, y_base, 0]))
            prev_group.add(lbl)

        for l in prev_group:
            self.play(FadeIn(l, scale=0.8), run_time=0.3)

        self.wait(0.6)
        self.play(FadeOut(hook), FadeOut(prev_group), run_time=0.4)

    # ============================================================
    # Scene 2: 相交直线
    # ============================================================
    def scene_2_intersect(self):
        title = Text("① 相交直线", font=FONT_CN, font_size=36, color=C_LINE_A).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.5)

        # 地面平面
        floor = make_floor_plane(0, 0, W=4.5, D=2.5,
                                 color=C_FLOOR, fill_color=C_FLOOR,
                                 fill_opacity=0.10, stroke_width=1.5)
        self.play(Create(floor), run_time=0.7)

        # 直线 a
        line_a = Line(self.s2_A1, self.s2_A2, color=C_LINE_A, stroke_width=3)
        lbl_a  = MathTex("a", color=C_LINE_A, font_size=36).next_to(
            self.s2_A2, RIGHT, buff=0.12)
        # 直线 b
        line_b = Line(self.s2_B1, self.s2_B2, color=C_LINE_B, stroke_width=3)
        lbl_b  = MathTex("b", color=C_LINE_B, font_size=36).next_to(
            self.s2_B1, LEFT, buff=0.12)

        self.play(Create(line_a), Write(lbl_a), run_time=0.6)
        self.play(Create(line_b), Write(lbl_b), run_time=0.6)

        # 交点
        dot_P = Dot(self.s2_P, radius=0.12, color=C_POINT)
        lbl_P = Text("P", font=FONT_CN, font_size=22, color=C_POINT).next_to(
            self.s2_P, UP + RIGHT, buff=0.08)
        self.play(FadeIn(dot_P, scale=0.5), Write(lbl_P), run_time=0.4)
        self.play(Flash(dot_P, color=C_POINT, flash_radius=0.3), run_time=0.4)

        desc1 = Text("有且只有一个公共点", font=FONT_CN, font_size=26,
                     color=WHITE).move_to(DOWN * 3.0)
        desc2 = Text("两直线共面", font=FONT_CN, font_size=22,
                     color=C_GRAY).move_to(DOWN * 3.7)
        self.play(FadeIn(desc1, shift=UP*0.2), run_time=0.4)
        self.play(FadeIn(desc2), run_time=0.3)
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(floor),
            FadeOut(line_a), FadeOut(lbl_a),
            FadeOut(line_b), FadeOut(lbl_b),
            FadeOut(dot_P), FadeOut(lbl_P),
            FadeOut(desc1), FadeOut(desc2),
            run_time=0.5
        )

    # ============================================================
    # Scene 3: 平行直线
    # ============================================================
    def scene_3_parallel(self):
        title = Text("② 平行直线", font=FONT_CN, font_size=36, color=C_LINE_B).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.5)

        floor = make_floor_plane(0, 0, W=4.5, D=2.5,
                                 color=C_FLOOR, fill_color=C_FLOOR,
                                 fill_opacity=0.10, stroke_width=1.5)
        self.play(Create(floor), run_time=0.7)

        line_a = Line(self.s3_A1, self.s3_A2, color=C_LINE_A, stroke_width=3)
        lbl_a  = MathTex("a", color=C_LINE_A, font_size=36).next_to(
            self.s3_A2, RIGHT, buff=0.12)
        line_b = Line(self.s3_B1, self.s3_B2, color=C_LINE_B, stroke_width=3)
        lbl_b  = MathTex("b", color=C_LINE_B, font_size=36).next_to(
            self.s3_B2, RIGHT, buff=0.12)

        self.play(Create(line_a), Write(lbl_a), run_time=0.6)
        self.play(Create(line_b), Write(lbl_b), run_time=0.6)

        # 平行符号
        par_sym = MathTex("a \\ \\| \\ b", color=C_GOLD, font_size=38).move_to(
            np.array([0, -2.0, 0]))
        self.play(Write(par_sym), run_time=0.5)

        desc1 = Text("没有公共点，两直线共面", font=FONT_CN, font_size=26,
                     color=WHITE).move_to(DOWN * 3.2)
        desc2 = Text("方向完全相同", font=FONT_CN, font_size=22,
                     color=C_GRAY).move_to(DOWN * 3.9)
        self.play(FadeIn(desc1, shift=UP*0.2), run_time=0.4)
        self.play(FadeIn(desc2), run_time=0.3)
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(floor),
            FadeOut(line_a), FadeOut(lbl_a),
            FadeOut(line_b), FadeOut(lbl_b),
            FadeOut(par_sym), FadeOut(desc1), FadeOut(desc2),
            run_time=0.5
        )

    # ============================================================
    # Scene 4: 异面直线
    # ============================================================
    def scene_4_skew(self):
        title = Text("③ 异面直线", font=FONT_CN, font_size=36, color=C_SKEW).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.5)

        # 地面平面
        floor = Polygon(*self.s4_floor_corners,
                        color=C_FLOOR, fill_color=C_FLOOR,
                        fill_opacity=0.12, stroke_width=1.5)
        self.play(Create(floor), run_time=0.7)

        # 直线 a（在地面, z=0）
        line_a = Line(self.s4_A1, self.s4_A2, color=C_LINE_A, stroke_width=3)
        lbl_a  = MathTex("a", color=C_LINE_A, font_size=36).next_to(
            self.s4_A2, RIGHT, buff=0.12)
        # 直线 b（在空中, z=1.5, 方向垂直于a）
        line_b = Line(self.s4_B1, self.s4_B2, color=C_LINE_B, stroke_width=3)
        lbl_b  = MathTex("b", color=C_LINE_B, font_size=36).next_to(
            self.s4_B2, UP, buff=0.12)

        self.play(Create(line_a), Write(lbl_a), run_time=0.6)
        self.play(Create(line_b), Write(lbl_b), run_time=0.6)

        # 虚线：从 b 的端点投影到地面（辅助可视化）
        proj_B1 = iso(0, -2, 0)   # B1在地面的投影
        proj_B2 = iso(0,  2, 0)   # B2在地面的投影
        shadow  = DashedLine(proj_B1, proj_B2, color=C_SKEW,
                             dash_length=0.1, stroke_width=1.5)
        vert1   = DashedLine(self.s4_B1, proj_B1, color=C_GRAY,
                             dash_length=0.08, stroke_width=1.2)
        vert2   = DashedLine(self.s4_B2, proj_B2, color=C_GRAY,
                             dash_length=0.08, stroke_width=1.2)
        self.play(Create(shadow), Create(vert1), Create(vert2), run_time=0.7)

        desc1 = Text("不在同一平面内", font=FONT_CN, font_size=26,
                     color=C_SKEW).move_to(DOWN * 3.0)
        desc2 = Text("既不相交，也不平行", font=FONT_CN, font_size=22,
                     color=WHITE).move_to(DOWN * 3.7)
        desc3 = Text("判定方法：反证法", font=FONT_CN, font_size=20,
                     color=C_GRAY).move_to(DOWN * 4.4)
        self.play(FadeIn(desc1, shift=UP*0.2), run_time=0.4)
        self.play(FadeIn(desc2), run_time=0.3)
        self.play(FadeIn(desc3), run_time=0.3)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(floor),
            FadeOut(line_a), FadeOut(lbl_a),
            FadeOut(line_b), FadeOut(lbl_b),
            FadeOut(shadow), FadeOut(vert1), FadeOut(vert2),
            FadeOut(desc1), FadeOut(desc2), FadeOut(desc3),
            run_time=0.5
        )

    # ============================================================
    # Scene 5: 异面直线所成角
    # ============================================================
    def scene_5_skew_angle(self):
        title   = Text("异面直线所成角", font=FONT_CN, font_size=34, color=C_SKEW).move_to(UP * 6.0)
        method  = Text("过任意一点，分别作两直线的平行线",
                       font=FONT_CN, font_size=22, color=C_GRAY).move_to(UP * 5.3)
        self.play(Write(title), FadeIn(method), run_time=0.6)

        # 参考点 O
        O = self.s5_O
        dot_O = Dot(O, radius=0.12, color=C_POINT)
        lbl_O = Text("O", font=FONT_CN, font_size=24, color=C_POINT).next_to(
            O, DOWN+LEFT, buff=0.08)
        self.play(FadeIn(dot_O, scale=0.5), Write(lbl_O), run_time=0.4)

        # 过O作a的平行线 OA'
        oa1 = Line(O, self.s5_OA2, color=C_LINE_A, stroke_width=3)
        lbl_a2 = MathTex("a'", color=C_LINE_A, font_size=32).next_to(
            self.s5_OA2, RIGHT, buff=0.1)
        self.play(Create(oa1), Write(lbl_a2), run_time=0.6)

        # 过O作b的平行线 OB'
        ob1 = Line(O, self.s5_OB2, color=C_LINE_B, stroke_width=3)
        lbl_b2 = MathTex("b'", color=C_LINE_B, font_size=32).next_to(
            self.s5_OB2, UP, buff=0.1)
        self.play(Create(ob1), Write(lbl_b2), run_time=0.6)

        # 角度弧线（两向量在2D中的角度）
        v_a = self.s5_OA2 - O
        v_b = self.s5_OB2 - O
        cos2d = np.dot(v_a[:2], v_b[:2]) / (np.linalg.norm(v_a[:2]) * np.linalg.norm(v_b[:2]))
        cos2d = np.clip(cos2d, -1, 1)
        angle_2d = np.degrees(np.arccos(cos2d))

        start_angle_rad = np.arctan2(v_a[1], v_a[0])
        arc = Arc(radius=0.5, start_angle=start_angle_rad,
                  angle=np.arccos(cos2d), color=C_ANGLE, stroke_width=2.5)
        arc.move_arc_center_to(O)
        # Calculate the angle label position properly to avoid broadcasting error
        mid_dir_2d = v_a[:2]/np.linalg.norm(v_a[:2]) + v_b[:2]/np.linalg.norm(v_b[:2])
        if np.linalg.norm(mid_dir_2d) > 0.01:
            mid_dir_2d = mid_dir_2d / np.linalg.norm(mid_dir_2d)
        theta_pos = O + np.array([mid_dir_2d[0], mid_dir_2d[1], 0]) * 0.75
        theta_label = MathTex(r"\theta", color=C_ANGLE, font_size=30).move_to(theta_pos)


        self.play(Create(arc), Write(theta_label), run_time=0.7)

        note = Text("取锐角或直角", font=FONT_CN, font_size=22,
                    color=WHITE).move_to(DOWN * 3.0)
        range_txt = MathTex(r"\theta \in (0,\,\tfrac{\pi}{2}]",
                            color=C_GOLD, font_size=36).move_to(DOWN * 3.8)
        self.play(FadeIn(note), Write(range_txt), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(method),
            FadeOut(dot_O), FadeOut(lbl_O),
            FadeOut(oa1), FadeOut(lbl_a2),
            FadeOut(ob1), FadeOut(lbl_b2),
            FadeOut(arc), FadeOut(theta_label),
            FadeOut(note), FadeOut(range_txt),
            run_time=0.5
        )

    # ============================================================
    # Scene 6: 公垂线
    # ============================================================
    def scene_6_common_perp(self):
        title  = Text("公垂线", font=FONT_CN, font_size=36, color=C_SKEW).move_to(UP * 6.0)
        defn   = Text("与两异面直线都垂直相交的直线",
                      font=FONT_CN, font_size=24, color=C_GRAY).move_to(UP * 5.3)
        self.play(Write(title), FadeIn(defn), run_time=0.6)

        # 重画异面直线
        floor = Polygon(*self.s4_floor_corners,
                        color=C_FLOOR, fill_color=C_FLOOR,
                        fill_opacity=0.10, stroke_width=1.2)
        line_a = Line(self.s4_A1, self.s4_A2, color=C_LINE_A, stroke_width=3)
        line_b = Line(self.s4_B1, self.s4_B2, color=C_LINE_B, stroke_width=3)
        lbl_a  = MathTex("a", color=C_LINE_A, font_size=32).next_to(self.s4_A2, RIGHT, buff=0.1)
        lbl_b  = MathTex("b", color=C_LINE_B, font_size=32).next_to(self.s4_B2, UP, buff=0.1)
        self.play(Create(floor), Create(line_a), Create(line_b),
                  Write(lbl_a), Write(lbl_b), run_time=0.8)

        # 公垂线 l (连接两垂足)
        foot_a = self.s6_foot_a
        foot_b = self.s6_foot_b
        common_perp = Line(foot_a, foot_b, color=C_GOLD, stroke_width=3.5)
        lbl_l = MathTex("l", color=C_GOLD, font_size=34).next_to(
            foot_b, RIGHT, buff=0.1)

        dot_fa = Dot(foot_a, radius=0.10, color=C_POINT)
        dot_fb = Dot(foot_b, radius=0.10, color=C_POINT)
        lbl_fa = Text("M", font=FONT_CN, font_size=20, color=C_POINT).next_to(
            foot_a, DOWN+LEFT, buff=0.06)
        lbl_fb = Text("N", font=FONT_CN, font_size=20, color=C_POINT).next_to(
            foot_b, UP+RIGHT, buff=0.06)

        self.play(
            Create(common_perp), Write(lbl_l),
            FadeIn(dot_fa), FadeIn(dot_fb),
            Write(lbl_fa), Write(lbl_fb),
            run_time=0.8
        )
        self.play(Flash(dot_fa, color=C_GOLD, flash_radius=0.25),
                  Flash(dot_fb, color=C_GOLD, flash_radius=0.25), run_time=0.4)

        desc1 = Text("MN 即为公垂线段", font=FONT_CN, font_size=24,
                     color=WHITE).move_to(DOWN * 3.2)
        desc2 = Text("MN 的长度 = 两异面直线的距离",
                     font=FONT_CN, font_size=22, color=C_GRAY).move_to(DOWN * 3.9)
        self.play(FadeIn(desc1, shift=UP*0.2), run_time=0.4)
        self.play(FadeIn(desc2), run_time=0.3)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(defn),
            FadeOut(floor), FadeOut(line_a), FadeOut(line_b),
            FadeOut(lbl_a), FadeOut(lbl_b),
            FadeOut(common_perp), FadeOut(lbl_l),
            FadeOut(dot_fa), FadeOut(dot_fb),
            FadeOut(lbl_fa), FadeOut(lbl_fb),
            FadeOut(desc1), FadeOut(desc2),
            run_time=0.5
        )

    # ============================================================
    # Scene 7: 总结对比
    # ============================================================
    def scene_7_summary(self):
        title = Text("三种位置关系总结", font=FONT_CN, font_size=32, color=C_GOLD).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        rows = [
            ("① 相交", "唯一公共点", "共面", C_LINE_A),
            ("② 平行", "无公共点",  "共面", C_LINE_B),
            ("③ 异面", "无公共点",  "不共面", C_SKEW),
        ]
        y = 4.0
        groups = VGroup()
        for (name, pts, plane, col) in rows:
            t1 = Text(name, font=FONT_CN, font_size=26, color=col)
            t2 = Text(pts,  font=FONT_CN, font_size=22, color=WHITE)
            t3 = Text(plane, font=FONT_CN, font_size=22, color=C_GRAY)
            row = VGroup(t1, t2, t3).arrange(RIGHT, buff=0.5)
            row.move_to(np.array([0, y, 0]))
            groups.add(row)
            self.play(FadeIn(row, shift=RIGHT*0.3), run_time=0.4)
            y -= 1.4

        key = Text("空间直线位置关系 ≠ 平面直线位置关系",
                   font=FONT_CN, font_size=22, color=C_GOLD).move_to(DOWN * 1.8)
        key2 = Text("多了「异面」这一特殊情况！",
                    font=FONT_CN, font_size=24, color=C_SKEW).move_to(DOWN * 2.6)
        self.play(FadeIn(key), run_time=0.4)
        self.play(Write(key2), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(groups), FadeOut(key), FadeOut(key2), run_time=0.5)

    # ============================================================
    # Scene 8: 片尾
    # ============================================================
    def scene_8_outro(self):
        big = Text("上海初高中数学直通车", font=FONT_CN, font_size=38, color=WHITE).move_to(UP * 1.5)
        uid = Text("@emptyandcalm", font=FONT_CN, font_size=28, color=C_GRAY).move_to(UP * 0.5)
        flw = Text("关注我，获得更多数学技巧！",
                   font=FONT_CN, font_size=30, color=C_GOLD).move_to(DOWN * 0.5)
        self.play(Transform(self.author, big), run_time=0.6)
        self.play(FadeIn(uid, shift=UP*0.2), run_time=0.4)
        self.play(FadeIn(flw, scale=1.05), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(self.author), FadeOut(uid), FadeOut(flw), run_time=0.8)