"""
right_triangle_properties.py
直角三角形的性质 - 教学动画 (TikTok 竖屏)

目标: 八年级, 介绍直角三角形4大性质
格式: 1080x1920, 9x16 逻辑坐标
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===================================================
# 全局配置
# ===================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

FONT_CN = "Noto Sans CJK SC"


class RightTriangleProperties(Scene):
    """直角三角形性质教学动画 (7 scenes, ~65 seconds)"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COL_TITLE = GOLD
        self.COL_ANG_A = "#4fc3f7"     # 浅蓝 - ∠A
        self.COL_ANG_B = "#f48fb1"     # 粉红 - ∠B
        self.COL_MEDIAN = "#ff8a65"    # 橙色 - 中线
        self.COL_HYPO = "#a5d6a7"      # 浅绿 - 斜边/30°
        self.COL_FORMULA = "#ce93d8"   # 紫色 - 关键公式

        # 初始化几何数据
        self.setup_geometry()

        # 创建持久三角形 (贯穿多个场景)
        self._rebuild_main_triangle()

        # 执行各场景
        self.scene_opening()
        self.scene_prop1_complementary()
        self.scene_prop2_median()
        self.scene_prop3_thirty_degrees()
        self.scene_prop4_pythagorean()
        self.scene_summary()
        self.scene_outro()

    # ===================================================
    # 几何数据初始化
    # ===================================================
    def setup_geometry(self):
        """
        统一初始化所有几何坐标 (精确计算，不臆想)

        主三角形: 3-4-5 直角三角形
          - 直角顶点 C (左下)
          - A (右下), B (左上)
          - CA=4 (底边), CB=3 (左边), AB=5 (斜边)

        30-60-90 三角形 (专用于性质③):
          - 直角顶点 C30, 30°在 A30
          - 斜边 AB30 = 3, 30°对边 CB30 = 1.5 = 斜边/2
        """
        # ---- 主三角形 ----
        self.C = np.array([-2.0, -0.5, 0])   # 直角
        self.A = np.array([2.0, -0.5, 0])     # ∠A ≈ 36.87°
        self.B = np.array([-2.0, 2.5, 0])     # ∠B ≈ 53.13°

        self.len_CA = np.linalg.norm(self.A - self.C)   # 4
        self.len_CB = np.linalg.norm(self.B - self.C)   # 3
        self.len_AB = np.linalg.norm(self.B - self.A)   # 5
        self.M = (self.A + self.B) / 2                   # 斜边中点 (0, 1.0, 0)
        self.len_CM = np.linalg.norm(self.M - self.C)   # 2.5

        # ---- 30-60-90 三角形 ----
        s3 = np.sqrt(3)
        sc = 0.75
        off30 = np.array([0, 1.2, 0])
        self.C30 = np.array([-s3 * sc, 0, 0]) + off30   # (-1.299, 1.2, 0) 直角
        self.A30 = np.array([s3 * sc, 0, 0]) + off30    # (1.299, 1.2, 0)  30°
        self.B30 = np.array([-s3 * sc, 2 * sc, 0]) + off30  # (-1.299, 2.7, 0) 60°

        self.len_C30A30 = np.linalg.norm(self.A30 - self.C30)  # ≈ 2.598
        self.len_C30B30 = np.linalg.norm(self.B30 - self.C30)  # 1.5
        self.len_A30B30 = np.linalg.norm(self.B30 - self.A30)  # 3.0

        # ---- 验证 ----
        assert abs(self.len_CA**2 + self.len_CB**2 - self.len_AB**2) < 1e-9, "勾股定理失败"
        assert abs(self.len_CM - self.len_AB / 2) < 1e-9, "斜边中线性质失败"
        assert abs(self.len_C30B30 / self.len_A30B30 - 0.5) < 1e-6, "30°性质失败"
        print("✓ 几何验证通过: 3-4-5直角三角形 + 30-60-90三角形")

    # ===================================================
    # 辅助方法
    # ===================================================
    def _right_angle_mark(self, corner, p1, p2, size=0.22):
        """在 corner 处创建直角标记 (小正方形)"""
        v1 = (p1 - corner) / np.linalg.norm(p1 - corner) * size
        v2 = (p2 - corner) / np.linalg.norm(p2 - corner) * size
        return Polygon(
            corner, corner + v1, corner + v1 + v2, corner + v2,
            color=YELLOW, stroke_width=2, fill_opacity=0
        )

    def _vertex_labels(self, C, A, B, size=22):
        """创建顶点标签 C/A/B"""
        lC = Text("C", font=FONT_CN, font_size=size, color=WHITE).next_to(C, DL, buff=0.12)
        lA = Text("A", font=FONT_CN, font_size=size, color=WHITE).next_to(A, DR, buff=0.12)
        lB = Text("B", font=FONT_CN, font_size=size, color=WHITE).next_to(B, UL, buff=0.12)
        return VGroup(lC, lA, lB)

    def _section_header(self, num_str, title_str, title_size=28):
        """创建场景标题"""
        num = Text(num_str, font=FONT_CN, font_size=34, color=self.COL_TITLE
                  ).move_to(UP * 5.6 + LEFT * 2.5)
        title = Text(title_str, font=FONT_CN, font_size=title_size, color=WHITE
                    ).next_to(num, RIGHT, buff=0.25)
        return num, title

    def _rebuild_main_triangle(self):
        """重建主三角形的 Manim 对象"""
        self.tri = Polygon(self.C, self.A, self.B, color=WHITE, stroke_width=3)
        self.ra = self._right_angle_mark(self.C, self.A, self.B)
        self.vtx = self._vertex_labels(self.C, self.A, self.B)

    def _bisector_direction(self, vertex, p1, p2):
        """计算 p1-vertex-p2 角的内角平分线方向 (单位向量)"""
        v1 = (p1 - vertex) / np.linalg.norm(p1 - vertex)
        v2 = (p2 - vertex) / np.linalg.norm(p2 - vertex)
        bis = v1 + v2
        return bis / np.linalg.norm(bis)

    # ===================================================
    # Scene 1: 开场钩子 (~0-4s)
    # ===================================================
    def scene_opening(self):
        # 作者标识 (y=7.0, 在安全区内)
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT_CN, font_size=17, color=GRAY_B
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author), run_time=0.3)

        # 钩子标题
        hook1 = Text("直角三角形", font=FONT_CN, font_size=52, color=self.COL_TITLE
                    ).move_to(UP * 6.0)
        hook2 = Text("4 大神奇性质", font=FONT_CN, font_size=40, color=WHITE
                    ).move_to(UP * 5.1)
        self.play(Write(hook1), run_time=0.7)
        self.play(FadeIn(hook2, shift=UP * 0.2), run_time=0.4)

        # 画主三角形
        self.play(Create(self.tri), run_time=1.0)
        self.play(
            FadeIn(self.ra),
            FadeIn(self.vtx),
            run_time=0.5
        )

        # 直角标注
        ra_text = MathTex(r"90^\circ", font_size=22, color=YELLOW
                         ).next_to(self.C, UR, buff=0.42)
        self.play(FadeIn(ra_text), run_time=0.3)

        # 4条性质预览
        prop_list = VGroup(
            Text("① 两锐角互余", font=FONT_CN, font_size=23, color=self.COL_ANG_A),
            Text("② 斜边中线 = 斜边/2", font=FONT_CN, font_size=23, color=self.COL_MEDIAN),
            Text("③ 30°对边 = 斜边/2", font=FONT_CN, font_size=23, color=self.COL_HYPO),
            Text("④ 勾股定理 a²+b²=c²", font=FONT_CN, font_size=23, color=self.COL_FORMULA),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(DOWN * 4.5)

        for p in prop_list:
            self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.25)

        self.wait(0.5)
        self.play(
            FadeOut(prop_list), FadeOut(hook1),
            FadeOut(hook2), FadeOut(ra_text),
            run_time=0.5
        )

    # ===================================================
    # Scene 2: 性质① - 两锐角互余 (~4-14s)
    # ===================================================
    def scene_prop1_complementary(self):
        num, title = self._section_header("性质①", "两锐角互余")
        self.play(Write(num), FadeIn(title), run_time=0.6)

        # 直角标记高亮
        self.play(Flash(self.ra, color=YELLOW, flash_radius=0.3), run_time=0.5)

        # ∠A 弧: from_three_points(B, A, C) → CCW 36.87° ✓ (cross_z=12 > 0)
        ang_A = Angle.from_three_points(
            self.B, self.A, self.C, radius=0.55, color=self.COL_ANG_A
        )

        # ∠B 弧: from_three_points(C, B, A) → CCW 53.13° ✓ (cross_z=12 > 0)
        ang_B = Angle.from_three_points(
            self.C, self.B, self.A, radius=0.55, color=self.COL_ANG_B
        )

        # 角标签: 放在角平分线方向上
        bis_A = self._bisector_direction(self.A, self.B, self.C)
        lbl_A = MathTex(r"\angle A", color=self.COL_ANG_A, font_size=26
                       ).move_to(self.A + bis_A * 0.95)

        bis_B = self._bisector_direction(self.B, self.C, self.A)
        lbl_B = MathTex(r"\angle B", color=self.COL_ANG_B, font_size=26
                       ).move_to(self.B + bis_B * 0.95)

        self.play(Create(ang_A), FadeIn(lbl_A), run_time=0.8)
        self.play(Create(ang_B), FadeIn(lbl_B), run_time=0.8)

        # 说明文字
        explain = Text(
            "∠C=90°，三角形内角和=180°",
            font=FONT_CN, font_size=21, color=GRAY_A
        ).move_to(DOWN * 3.7)
        self.play(FadeIn(explain), run_time=0.5)

        # 主要公式
        formula = MathTex(
            r"\angle A + \angle B = 90^\circ",
            color=self.COL_FORMULA, font_size=44
        ).move_to(DOWN * 5.1)
        self.play(Write(formula), run_time=1.0)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(num), FadeOut(title),
            FadeOut(ang_A), FadeOut(lbl_A),
            FadeOut(ang_B), FadeOut(lbl_B),
            FadeOut(explain), FadeOut(formula),
            run_time=0.5
        )

    # ===================================================
    # Scene 3: 性质② - 斜边中线 (~14-24s)
    # ===================================================
    def scene_prop2_median(self):
        num, title = self._section_header("性质②", "斜边上的中线 = 斜边/2", title_size=25)
        self.play(Write(num), FadeIn(title), run_time=0.6)

        # 斜边高亮
        hypo = Line(self.A, self.B, color=self.COL_HYPO, stroke_width=5)
        hypo_lbl = Text("斜边 AB = 5", font=FONT_CN, font_size=22, color=self.COL_HYPO
                       ).move_to(DOWN * 3.6)
        self.play(Create(hypo), FadeIn(hypo_lbl), run_time=0.6)

        # 标记中点 M
        m_dot = Dot(self.M, color=self.COL_MEDIAN, radius=0.1)
        m_lbl = Text("M", font=FONT_CN, font_size=22, color=self.COL_MEDIAN
                    ).next_to(self.M, RIGHT, buff=0.18)
        self.play(FadeIn(m_dot, scale=0.5), run_time=0.4)
        self.play(Flash(m_dot, color=self.COL_MEDIAN, flash_radius=0.25), run_time=0.3)
        self.play(FadeIn(m_lbl), run_time=0.3)

        mid_text = Text("M 是 AB 的中点", font=FONT_CN, font_size=21, color=GRAY_A
                       ).move_to(DOWN * 4.3)
        self.play(FadeIn(mid_text), run_time=0.3)

        # 画中线 CM
        median = Line(self.C, self.M, color=self.COL_MEDIAN, stroke_width=4)
        self.play(Create(median), run_time=0.8)

        # CM 长度标签: 放在中线中点旁, 指向三角形外侧
        cm_mid = (self.C + self.M) / 2
        cm_vec = self.M - self.C
        cm_perp = np.array([-cm_vec[1], cm_vec[0], 0])
        cm_perp_unit = cm_perp / np.linalg.norm(cm_perp)
        tri_cen = (self.C + self.A + self.B) / 3
        # 确保方向朝三角形外侧
        if np.dot(cm_perp_unit[:2], (cm_mid - tri_cen)[:2]) < 0:
            cm_perp_unit = -cm_perp_unit
        cm_lbl = MathTex(r"CM = 2.5", color=self.COL_MEDIAN, font_size=28
                        ).move_to(cm_mid + cm_perp_unit * 0.7)
        self.play(FadeIn(cm_lbl), run_time=0.5)

        # 主公式
        formula = MathTex(
            r"CM = \frac{AB}{2} = \frac{5}{2} = 2.5",
            color=self.COL_FORMULA, font_size=36
        ).move_to(DOWN * 5.5)
        self.play(Write(formula), run_time=1.1)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(num), FadeOut(title),
            FadeOut(hypo), FadeOut(hypo_lbl),
            FadeOut(m_dot), FadeOut(m_lbl), FadeOut(mid_text),
            FadeOut(median), FadeOut(cm_lbl),
            FadeOut(formula),
            run_time=0.5
        )

    # ===================================================
    # Scene 4: 性质③ - 30°对边 (~24-34s)
    # ===================================================
    def scene_prop3_thirty_degrees(self):
        num, title = self._section_header("性质③", "30°角对边 = 斜边/2", title_size=26)
        self.play(Write(num), FadeIn(title), run_time=0.6)

        # 淡出主三角形，切换到 30-60-90 三角形
        self.play(
            FadeOut(self.tri), FadeOut(self.ra), FadeOut(self.vtx),
            run_time=0.4
        )

        # 创建 30-60-90 三角形
        tri30 = Polygon(self.C30, self.A30, self.B30, color=WHITE, stroke_width=3)
        ra30 = self._right_angle_mark(self.C30, self.A30, self.B30)
        vtx30 = self._vertex_labels(self.C30, self.A30, self.B30, size=20)
        self.play(Create(tri30), FadeIn(ra30), FadeIn(vtx30), run_time=0.9)

        # ∠A30 弧: from_three_points(B30, A30, C30) → CCW 30° ✓ (cross_z > 0)
        ang30 = Angle.from_three_points(
            self.B30, self.A30, self.C30, radius=0.5, color=self.COL_HYPO
        )
        # 30° 标签放在角平分线方向
        bis_A30 = self._bisector_direction(self.A30, self.B30, self.C30)
        lbl_30 = MathTex(r"30^\circ", color=self.COL_HYPO, font_size=30
                        ).move_to(self.A30 + bis_A30 * 0.88)
        self.play(Create(ang30), Write(lbl_30), run_time=0.8)

        # 高亮30°对边 C30B30
        opp = Line(self.C30, self.B30, color=self.COL_HYPO, stroke_width=5)
        opp_lbl = Text("对边 CB", font=FONT_CN, font_size=20, color=self.COL_HYPO
                      ).next_to((self.C30 + self.B30) / 2, LEFT, buff=0.2)
        self.play(Create(opp), FadeIn(opp_lbl), run_time=0.5)

        # 高亮斜边 A30B30
        hyp30 = Line(self.A30, self.B30, color=YELLOW, stroke_width=5)
        hyp30_lbl = Text("斜边 AB", font=FONT_CN, font_size=20, color=YELLOW
                        ).next_to((self.A30 + self.B30) / 2, RIGHT, buff=0.2)
        self.play(Create(hyp30), FadeIn(hyp30_lbl), run_time=0.5)

        # 说明
        explain30 = Text(
            "30°角的对边 = 斜边的一半！",
            font=FONT_CN, font_size=24, color=GRAY_A
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(explain30), run_time=0.4)

        # 公式
        formula30 = MathTex(
            r"CB = \frac{AB}{2}",
            color=self.COL_FORMULA, font_size=42
        ).move_to(DOWN * 5.1)
        self.play(Write(formula30), run_time=1.0)
        self.wait(1.5)

        # 清理，恢复主三角形
        self.play(
            FadeOut(num), FadeOut(title),
            FadeOut(tri30), FadeOut(ra30), FadeOut(vtx30),
            FadeOut(ang30), FadeOut(lbl_30),
            FadeOut(opp), FadeOut(opp_lbl),
            FadeOut(hyp30), FadeOut(hyp30_lbl),
            FadeOut(explain30), FadeOut(formula30),
            run_time=0.5
        )

        self._rebuild_main_triangle()
        self.play(
            FadeIn(self.tri), FadeIn(self.ra), FadeIn(self.vtx),
            run_time=0.5
        )

    # ===================================================
    # Scene 5: 性质④ - 勾股定理 (~34-48s)
    # ===================================================
    def scene_prop4_pythagorean(self):
        num, title = self._section_header("性质④", "勾股定理")
        self.play(Write(num), FadeIn(title), run_time=0.6)

        # 标注三边
        side_b = Line(self.C, self.A, color=self.COL_ANG_A, stroke_width=5)
        lbl_b = MathTex(r"b=4", color=self.COL_ANG_A, font_size=30
                       ).next_to((self.C + self.A) / 2, DOWN, buff=0.25)

        side_a = Line(self.C, self.B, color=self.COL_ANG_B, stroke_width=5)
        lbl_a = MathTex(r"a=3", color=self.COL_ANG_B, font_size=30
                       ).next_to((self.C + self.B) / 2, LEFT, buff=0.25)

        side_c = Line(self.A, self.B, color=self.COL_HYPO, stroke_width=5)
        lbl_c = MathTex(r"c=5", color=self.COL_HYPO, font_size=30
                       ).next_to((self.A + self.B) / 2, RIGHT, buff=0.28)

        self.play(Create(side_b), Write(lbl_b), run_time=0.5)
        self.play(Create(side_a), Write(lbl_a), run_time=0.5)
        self.play(Create(side_c), Write(lbl_c), run_time=0.5)

        # 通用公式
        f_gen = MathTex(
            r"a^2 + b^2 = c^2",
            color=self.COL_FORMULA, font_size=46
        ).move_to(DOWN * 3.8)
        self.play(Write(f_gen), run_time=1.0)
        self.wait(0.4)

        # 代入数字
        f_nums = MathTex(
            r"3^2 + 4^2 = 5^2",
            color=WHITE, font_size=40
        ).move_to(DOWN * 5.0)
        self.play(Write(f_nums), run_time=0.8)

        # 验证计算
        f_verify = MathTex(
            r"9 + 16 = 25",
            color=GREEN_B, font_size=40
        ).move_to(DOWN * 5.9)
        ok_text = Text("✓ 正确！", font=FONT_CN, font_size=30, color=GREEN_B
                      ).next_to(f_verify, RIGHT, buff=0.3)
        self.play(Write(f_verify), FadeIn(ok_text, shift=LEFT * 0.2), run_time=0.8)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(num), FadeOut(title),
            FadeOut(side_a), FadeOut(lbl_a),
            FadeOut(side_b), FadeOut(lbl_b),
            FadeOut(side_c), FadeOut(lbl_c),
            FadeOut(f_gen), FadeOut(f_nums),
            FadeOut(f_verify), FadeOut(ok_text),
            run_time=0.5
        )

    # ===================================================
    # Scene 6: 总结 (~48-58s)
    # ===================================================
    def scene_summary(self):
        # 淡出主三角形
        self.play(
            FadeOut(self.tri), FadeOut(self.ra), FadeOut(self.vtx),
            run_time=0.5
        )

        sum_title = Text("总结", font=FONT_CN, font_size=46, color=self.COL_TITLE
                        ).move_to(UP * 5.5)
        sum_sub = Text("直角三角形 4 大性质", font=FONT_CN, font_size=28, color=GRAY_A
                      ).move_to(UP * 4.75)
        self.play(Write(sum_title), FadeIn(sum_sub), run_time=0.7)

        # 4条性质卡片 (文字 + 公式)
        rows = [
            ("① 两锐角互余",   r"\angle A + \angle B = 90^\circ", self.COL_ANG_A, UP * 3.2),
            ("② 斜边中线",     r"CM = \frac{AB}{2}",               self.COL_MEDIAN, UP * 1.4),
            ("③ 30°对边",     r"CB = \frac{AB}{2}",               self.COL_HYPO,   DOWN * 0.4),
            ("④ 勾股定理",    r"a^2 + b^2 = c^2",                 self.COL_FORMULA, DOWN * 2.2),
        ]

        sum_objs = VGroup()
        for text_str, formula_str, color, pos in rows:
            # 小圆点
            dot = Dot(radius=0.08, color=color).move_to(pos + LEFT * 3.5)
            t_obj = Text(text_str, font=FONT_CN, font_size=26, color=color
                        ).next_to(dot, RIGHT, buff=0.2)
            f_obj = MathTex(formula_str, color=color, font_size=30
                           ).next_to(t_obj, RIGHT, buff=0.3)
            group = VGroup(dot, t_obj, f_obj)
            self.play(FadeIn(group, shift=RIGHT * 0.4), run_time=0.45)
            sum_objs.add(group)

        self.wait(2.0)

        self.play(
            FadeOut(sum_title), FadeOut(sum_sub), FadeOut(sum_objs),
            run_time=0.5
        )

    # ===================================================
    # Scene 7: 片尾 (~58-65s)
    # ===================================================
    def scene_outro(self):
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT_CN, font_size=38, color=WHITE
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font=FONT_CN, font_size=28, color=GRAY_B
        ).move_to(UP * 1.0)

        follow = Text(
            "关注我，获得更多数学技巧!",
            font=FONT_CN, font_size=30, color=self.COL_TITLE
        ).move_to(DOWN * 0.3)

        self.play(Transform(self.author, author_big), run_time=0.6)
        self.play(FadeIn(author_id), FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # 小三角形装饰
        def small_tri(angle_offset):
            v = [
                np.array([0, 0.22, 0]),
                np.array([-0.19, -0.11, 0]),
                np.array([0.19, -0.11, 0]),
            ]
            c = np.cos(angle_offset)
            s_a = np.sin(angle_offset)
            rot = np.array([[c, -s_a, 0], [s_a, c, 0], [0, 0, 1]])
            v_rot = [rot @ p for p in v]
            return Polygon(*v_rot, color=GOLD, fill_opacity=0.85, stroke_width=0)

        tris = VGroup(*[
            small_tri(i * PI / 3).move_to(
                follow.get_center() + np.array([np.cos(i * PI / 3) * 2.8, np.sin(i * PI / 3) * 0.6 - 1.5, 0])
            )
            for i in range(6)
        ])

        self.play(*[FadeIn(t, scale=0.5) for t in tris], run_time=0.5)
        self.play(Rotate(tris, angle=PI, run_time=1.2))
        self.wait(1.0)

        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(tris),
            run_time=0.8
        )


# ===================================================
# 渲染命令:
# 快速预览: manim -pql right_triangle_properties.py RightTriangleProperties
# 高质量:   manim -qh right_triangle_properties.py RightTriangleProperties
# ===================================================