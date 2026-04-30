"""
平面向量的应用 - Manim 教学动画
知识点: 向量的5大应用 (平行/垂直/夹角/共线/面积)
目标: 高二第一学期
格式: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===== 全局配置 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

FONT = "PingFang SC"
C_BG = "#1a1a2e"
C_PARA = "#e74c3c"
C_PERP = "#3498db"
C_ANGLE = "#2ecc71"
C_COLL = "#f39c12"
C_VEC_A = "#ff6b6b"
C_VEC_B = "#74b9ff"
C_AXIS = "#888888"
C_GOLD = "#ffd700"
C_AUTHOR = "#aaaaaa"


class VectorApplications(Scene):
    """
    向量应用 TikTok 竖屏教学动画
    
    场景:
    1. 开场钩子
    2. 建立坐标系
    3. 平行条件
    4. 垂直条件
    5. 夹角计算
    6. 三点共线
    7. 总结 + 结尾
    """

    def construct(self):
        self.camera.background_color = C_BG
        self.setup_geometry()
        self.scene_1_opening()
        self.scene_2_coordinates()
        self.scene_3_parallel()
        self.scene_4_perpendicular()
        self.scene_5_angle()
        self.scene_6_collinear()
        self.scene_7_summary_outro()

    # ============================================================
    #  几何数据初始化
    # ============================================================
    def setup_geometry(self):
        """统一初始化所有几何数据"""
        # --- 坐标系配置 ---
        self.AXES_ORIGIN = np.array([0.0, 1.0, 0.0])   # 坐标系逻辑原点在屏幕上的位置
        self.UNIT = 0.8   # 1个坐标单位 = 0.8逻辑单位

        def to_screen(coord):
            """坐标系坐标 -> 屏幕坐标"""
            return self.AXES_ORIGIN + np.array([coord[0], coord[1], 0]) * self.UNIT

        self.to_screen = to_screen

        # --- 向量 a = (3, 1) ---
        self.va = np.array([3.0, 1.0])
        self.va_screen = to_screen(self.va)

        # --- 平行向量 b = 0.5 * a = (1.5, 0.5) ---
        self.vb_para = np.array([1.5, 0.5])
        self.vb_para_start = to_screen(np.array([0.5, 0.5]))  # 从稍偏的位置出发
        self.vb_para_end = self.vb_para_start + np.array([self.vb_para[0], self.vb_para[1], 0]) * self.UNIT

        # --- 垂直向量 b = (-1, 3), 点积 = 3*(-1)+1*3 = 0 ---
        self.vb_perp = np.array([-1.0, 3.0])
        self.vb_perp_end = to_screen(self.vb_perp)

        # --- 夹角: a=(3,1), c=(2,1.5) ---
        self.vc = np.array([2.0, 1.5])
        self.vc_end = to_screen(self.vc)
        dot_ac = float(np.dot(self.va, self.vc))
        mag_a = float(np.linalg.norm(self.va))
        mag_c = float(np.linalg.norm(self.vc))
        self.cos_theta = dot_ac / (mag_a * mag_c)
        self.theta_deg = float(np.degrees(np.arccos(np.clip(self.cos_theta, -1, 1))))
        self.dot_ac = dot_ac
        self.mag_a = mag_a
        self.mag_c = mag_c

        # --- 叉积z分量 (判断Angle方向) ---
        self.cross_z_ac = self.va[0] * self.vc[1] - self.va[1] * self.vc[0]  # > 0 => 逆时针

        # --- 共线点: A=(-2,-1), B=(0,0), C=(2,1) ---
        self.P_A = np.array([-2.0, -1.0])
        self.P_B = np.array([0.0, 0.0])
        self.P_C = np.array([2.0, 1.0])

        # 验证 AB = 0.5 * AC
        AB = self.P_B - self.P_A   # (2, 1)
        AC = self.P_C - self.P_A   # (4, 2)
        self.lambda_collinear = AB[0] / AC[0]   # 0.5

        self._verify()

    def _verify(self):
        eps = 1e-9
        # 平行行列式
        det = self.va[0] * self.vb_para[1] - self.vb_para[0] * self.va[1]
        assert abs(det) < eps, f"平行行列式: {det}"
        # 垂直点积
        dot = float(np.dot(self.va, self.vb_perp))
        assert abs(dot) < eps, f"垂直点积: {dot}"
        # 共线
        AB = self.P_B - self.P_A
        AC = self.P_C - self.P_A
        check = self.lambda_collinear * AC - AB
        assert np.linalg.norm(check) < eps, "共线验证失败"
        print("✓ 几何验证通过")

    # ============================================================
    #  工具方法
    # ============================================================
    def make_axes(self):
        """创建坐标系"""
        axes = Axes(
            x_range=[-1.5, 4.5, 1],
            y_range=[-1.0, 4.0, 1],
            x_length=4.8,
            y_length=4.0,
            axis_config={
                "color": C_AXIS,
                "stroke_width": 1.5,
                "include_ticks": True,
                "tick_size": 0.05,
            },
            tips=True,
        ).move_to(self.AXES_ORIGIN)
        return axes

    def make_vector_arrow(self, start, end, color, stroke_width=4):
        """创建向量箭头"""
        return Arrow(
            start=start,
            end=end,
            buff=0,
            color=color,
            stroke_width=stroke_width,
            max_tip_length_to_length_ratio=0.15,
        )

    def tex(self, s, size=28, color=WHITE):
        return MathTex(s, font_size=size, color=color)

    def txt(self, s, size=22, color=WHITE):
        return Text(s, font=FONT, font_size=size, color=color)

    def section_title(self, text, color=WHITE):
        return Text(text, font=FONT, font_size=34, color=color, weight=BOLD)

    def formula_box(self, formula_str, color=YELLOW, bg_color="#2d2d4e"):
        formula = MathTex(formula_str, font_size=30, color=color)
        box = SurroundingRectangle(
            formula,
            color=color,
            fill_color=bg_color,
            fill_opacity=0.6,
            buff=0.18,
            corner_radius=0.1,
        )
        return VGroup(box, formula)

    # ============================================================
    #  Scene 1: 开场钩子
    # ============================================================
    def scene_1_opening(self):
        # 作者信息
        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT,
            font_size=20,
            color=C_AUTHOR,
        ).move_to(UP * 7)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.4)

        # 大标题
        title_line1 = Text("向量能做什么?", font=FONT, font_size=48, color=C_GOLD)
        title_line2 = Text("5大应用全掌握!", font=FONT, font_size=36, color=WHITE)
        title_grp = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.3)
        title_grp.move_to(UP * 5.5)
        self.play(Write(title_line1), run_time=0.8)
        self.play(FadeIn(title_line2, shift=UP * 0.2), run_time=0.5)

        # 5个向量爆发
        center = ORIGIN
        angles = [30, 75, 120, 165, 210]
        colors = [C_PARA, C_PERP, C_ANGLE, C_COLL, PURPLE]
        arrows = VGroup()
        for i, (angle_deg, c) in enumerate(zip(angles, colors)):
            angle_rad = np.radians(angle_deg)
            direction = np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
            arr = Arrow(
                center,
                center + direction * 1.6,
                buff=0,
                color=c,
                stroke_width=5,
                max_tip_length_to_length_ratio=0.18,
            )
            arrows.add(arr)
        arrows.move_to(UP * 2.5)
        self.play(
            *[GrowArrow(a) for a in arrows],
            run_time=1.0,
        )

        # 5条应用标签
        labels_data = [
            ("① 证明平行", C_PARA),
            ("② 证明垂直", C_PERP),
            ("③ 求夹角", C_ANGLE),
            ("④ 判断共线", C_COLL),
            ("⑤ 求面积", PURPLE),
        ]
        labels = VGroup()
        for i, (txt, c) in enumerate(labels_data):
            t = Text(txt, font=FONT, font_size=24, color=c)
            labels.add(t)
        labels.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        labels.move_to(DOWN * 0.5)
        self.play(LaggedStart(*[FadeIn(l, shift=LEFT * 0.3) for l in labels], lag_ratio=0.15), run_time=1.2)

        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(title_grp),
            FadeOut(arrows),
            FadeOut(labels),
            run_time=0.5,
        )

    # ============================================================
    #  Scene 2: 坐标系 + 向量基础
    # ============================================================
    def scene_2_coordinates(self):
        scene_title = self.section_title("坐标表示", color=BLUE_B)
        scene_title.move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.5)

        # 建立坐标系
        self.axes = self.make_axes()
        self.play(Create(self.axes), run_time=1.0)

        # 向量 a = (3,1)
        org = self.AXES_ORIGIN
        va_end = self.va_screen
        vec_a_arrow = self.make_vector_arrow(org, va_end, C_VEC_A, stroke_width=5)
        self.arrow_a = vec_a_arrow

        self.play(GrowArrow(vec_a_arrow), run_time=0.8)

        # 标签 a = (3, 1)
        label_a = self.tex(r"\vec{a} = (3, 1)", size=26, color=C_VEC_A)
        label_a.next_to(va_end, UR, buff=0.12)
        self.play(Write(label_a), run_time=0.5)

        # 分解线 (虚线)
        x_foot = self.to_screen(np.array([self.va[0], 0]))
        dash_x = DashedLine(org, x_foot, color=GRAY_B, dash_length=0.08)
        dash_y = DashedLine(x_foot, va_end, color=GRAY_B, dash_length=0.08)
        coord_x = MathTex("3", font_size=22, color=GRAY_A).next_to(x_foot, DOWN, buff=0.1)
        coord_y = MathTex("1", font_size=22, color=GRAY_A).next_to(va_end, RIGHT, buff=0.1)
        self.play(
            Create(dash_x), Create(dash_y),
            FadeIn(coord_x), FadeIn(coord_y),
            run_time=0.7
        )

        explain = self.txt("向量终点坐标即为向量的坐标表示", size=20, color=GRAY_A)
        explain.move_to(DOWN * 4.5)
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.0)

        # 清理辅助元素
        self.play(
            FadeOut(scene_title),
            FadeOut(dash_x), FadeOut(dash_y),
            FadeOut(coord_x), FadeOut(coord_y),
            FadeOut(explain), FadeOut(label_a),
            run_time=0.4
        )
        # 保留 axes 和 arrow_a

    # ============================================================
    #  Scene 3: 平行条件
    # ============================================================
    def scene_3_parallel(self):
        scene_title = self.section_title("① 平行证明", color=C_PARA)
        scene_title.move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.5)

        # 向量 b = (1.5, 0.5)，从偏移点出发
        vb_start = self.to_screen(np.array([0.5, 0.3]))
        vb_end = vb_start + np.array([self.vb_para[0] * self.UNIT, self.vb_para[1] * self.UNIT, 0])
        vec_b_arrow = self.make_vector_arrow(vb_start, vb_end, C_VEC_B, stroke_width=5)
        self.play(GrowArrow(vec_b_arrow), run_time=0.7)

        # 两个向量标签
        lbl_a = self.tex(r"\vec{a} = (3,\ 1)", size=24, color=C_VEC_A)
        lbl_b = self.tex(r"\vec{b} = (1.5,\ 0.5)", size=24, color=C_VEC_B)
        lbl_a.move_to(DOWN * 3.2 + LEFT * 1.5)
        lbl_b.move_to(DOWN * 3.8 + LEFT * 1.5)
        self.play(FadeIn(lbl_a), FadeIn(lbl_b), run_time=0.5)

        # 展示 b = 0.5 a
        eq_b_is_half_a = self.tex(r"\vec{b} = 0.5 \cdot \vec{a}", size=26, color=YELLOW)
        eq_b_is_half_a.move_to(DOWN * 4.6)
        self.play(Write(eq_b_is_half_a), run_time=0.7)
        self.wait(0.5)

        # 平行判定公式
        formula1 = self.tex(r"\vec{a} \parallel \vec{b} \Leftrightarrow \vec{a} = \lambda \vec{b}", size=26)
        formula1.move_to(DOWN * 5.5)
        self.play(FadeIn(formula1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.4)

        # 行列式判定
        det_formula = self.formula_box(
            r"x_1 y_2 - x_2 y_1 = 0",
            color=C_PARA
        )
        det_formula.move_to(DOWN * 6.3)
        self.play(FadeIn(det_formula, shift=UP * 0.2), run_time=0.5)

        # 代入数字
        calc_lbl = self.txt("代入验证: 3×0.5 - 1.5×1 = 0 ✓", size=20, color=GRAY_A)
        calc_lbl.move_to(DOWN * 7.0)
        self.play(FadeIn(calc_lbl), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(vec_b_arrow),
            FadeOut(lbl_a), FadeOut(lbl_b),
            FadeOut(eq_b_is_half_a),
            FadeOut(formula1),
            FadeOut(det_formula),
            FadeOut(calc_lbl),
            run_time=0.5
        )

    # ============================================================
    #  Scene 4: 垂直条件
    # ============================================================
    def scene_4_perpendicular(self):
        scene_title = self.section_title("② 垂直证明", color=C_PERP)
        scene_title.move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.5)

        org = self.AXES_ORIGIN

        # 向量 b = (-1, 3)
        vb_perp_end = self.to_screen(self.vb_perp)
        vec_b_arrow = self.make_vector_arrow(org, vb_perp_end, C_VEC_B, stroke_width=5)
        self.play(GrowArrow(vec_b_arrow), run_time=0.8)

        # 直角标记
        # 计算直角标记位置
        va_unit = self.va / np.linalg.norm(self.va)
        vb_unit = self.vb_perp / np.linalg.norm(self.vb_perp)
        size = 0.18
        corner = org
        p1 = corner + np.array([va_unit[0], va_unit[1], 0]) * size
        p2 = corner + np.array([vb_unit[0], vb_unit[1], 0]) * size
        p_mid = p1 + np.array([vb_unit[0], vb_unit[1], 0]) * size
        right_mark = Polygon(
            corner, p1, p_mid, p2,
            color=YELLOW, stroke_width=2, fill_opacity=0
        )
        self.play(Create(right_mark), run_time=0.4)

        # 标签
        lbl_a = self.tex(r"\vec{a} = (3,\ 1)", size=24, color=C_VEC_A)
        lbl_b = self.tex(r"\vec{b} = (-1,\ 3)", size=24, color=C_VEC_B)
        lbl_a.move_to(DOWN * 3.2 + LEFT * 1.5)
        lbl_b.move_to(DOWN * 3.8 + LEFT * 1.5)
        self.play(FadeIn(lbl_a), FadeIn(lbl_b), run_time=0.5)

        # 点积公式
        formula_dot = self.tex(
            r"\vec{a} \perp \vec{b} \Leftrightarrow \vec{a} \cdot \vec{b} = 0",
            size=26
        )
        formula_dot.move_to(DOWN * 4.8)
        self.play(FadeIn(formula_dot, shift=UP * 0.2), run_time=0.6)

        # 展开计算
        calc_text = self.tex(
            r"\vec{a} \cdot \vec{b} = 3 \times (-1) + 1 \times 3 = 0",
            size=24, color=YELLOW
        )
        calc_text.move_to(DOWN * 5.8)
        self.play(Write(calc_text), run_time=0.8)
        self.wait(0.5)

        # 框定结论
        conclusion_box = self.formula_box(
            r"\vec{a} \perp \vec{b}\ \checkmark",
            color=C_PERP
        )
        conclusion_box.move_to(DOWN * 6.7)
        self.play(FadeIn(conclusion_box, scale=0.9), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(vec_b_arrow),
            FadeOut(right_mark),
            FadeOut(lbl_a), FadeOut(lbl_b),
            FadeOut(formula_dot),
            FadeOut(calc_text),
            FadeOut(conclusion_box),
            run_time=0.5
        )

    # ============================================================
    #  Scene 5: 夹角计算
    # ============================================================
    def scene_5_angle(self):
        scene_title = self.section_title("③ 夹角计算", color=C_ANGLE)
        scene_title.move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.5)

        org = self.AXES_ORIGIN

        # 向量 c = (2, 1.5)
        vc_end = self.vc_end
        vec_c_arrow = self.make_vector_arrow(org, vc_end, C_VEC_B, stroke_width=5)
        self.play(GrowArrow(vec_c_arrow), run_time=0.8)

        # 角度弧
        # 叉积 > 0 => a到c逆时针 => other_angle=False
        line_a = Line(org, self.va_screen)
        line_c = Line(org, vc_end)
        # 使用smaller angle (theta ≈ 18.4°)
        angle_arc = Angle(
            line_a, line_c,
            radius=0.5,
            color=C_ANGLE,
            other_angle=False if self.cross_z_ac > 0 else True
        )
        theta_label = MathTex(r"\theta", font_size=24, color=C_ANGLE)
        theta_label.next_to(angle_arc, RIGHT, buff=0.08)
        theta_label.shift(UP * 0.05)
        self.play(Create(angle_arc), FadeIn(theta_label), run_time=0.6)

        # 向量标签
        lbl_a = self.tex(r"\vec{a} = (3,\ 1)", size=24, color=C_VEC_A)
        lbl_c = self.tex(r"\vec{c} = (2,\ 1.5)", size=24, color=C_VEC_B)
        lbl_a.move_to(DOWN * 3.0 + LEFT * 1.5)
        lbl_c.move_to(DOWN * 3.6 + LEFT * 1.5)
        self.play(FadeIn(lbl_a), FadeIn(lbl_c), run_time=0.4)

        # 夹角公式
        formula_cos = self.tex(
            r"\cos\theta = \frac{\vec{a} \cdot \vec{c}}{|\vec{a}||\vec{c}|}",
            size=28
        )
        formula_cos.move_to(DOWN * 4.5)
        self.play(Write(formula_cos), run_time=0.8)
        self.wait(0.5)

        # 展开
        expand = self.tex(
            r"= \frac{3 \times 2 + 1 \times 1.5}{\sqrt{10} \cdot 2.5}",
            size=26, color=GRAY_A
        )
        expand.move_to(DOWN * 5.4)
        self.play(FadeIn(expand, shift=UP * 0.15), run_time=0.6)

        # 结果
        result = self.tex(
            r"= \frac{7.5}{2.5\sqrt{10}} = \frac{3}{\sqrt{10}}",
            size=26, color=YELLOW
        )
        result.move_to(DOWN * 6.2)
        self.play(Write(result), run_time=0.7)

        theta_val = self.txt(f"θ ≈ {self.theta_deg:.1f}°", size=24, color=C_ANGLE)
        theta_val.move_to(DOWN * 7.0)
        self.play(FadeIn(theta_val), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(vec_c_arrow),
            FadeOut(angle_arc), FadeOut(theta_label),
            FadeOut(lbl_a), FadeOut(lbl_c),
            FadeOut(formula_cos),
            FadeOut(expand),
            FadeOut(result),
            FadeOut(theta_val),
            run_time=0.5
        )

    # ============================================================
    #  Scene 6: 三点共线
    # ============================================================
    def scene_6_collinear(self):
        scene_title = self.section_title("④ 三点共线", color=C_COLL)
        scene_title.move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.5)

        # 点坐标映射
        A_s = self.to_screen(self.P_A)
        B_s = self.to_screen(self.P_B)
        C_s = self.to_screen(self.P_C)

        # 绘制三点
        dot_A = Dot(A_s, color=C_COLL, radius=0.1)
        dot_B = Dot(B_s, color=C_COLL, radius=0.1)
        dot_C = Dot(C_s, color=C_COLL, radius=0.1)
        lbl_A = MathTex("A", font_size=22, color=C_COLL).next_to(dot_A, DL, buff=0.1)
        lbl_B = MathTex("B", font_size=22, color=C_COLL).next_to(dot_B, UR, buff=0.1)
        lbl_C = MathTex("C", font_size=22, color=C_COLL).next_to(dot_C, UR, buff=0.1)

        self.play(
            FadeIn(dot_A), FadeIn(dot_B), FadeIn(dot_C),
            FadeIn(lbl_A), FadeIn(lbl_B), FadeIn(lbl_C),
            run_time=0.7
        )

        # 向量箭头 AB, AC
        AB_arr = self.make_vector_arrow(A_s, B_s, C_ANGLE, stroke_width=4)
        AC_arr = self.make_vector_arrow(A_s, C_s, PURPLE_B, stroke_width=4)
        self.play(GrowArrow(AB_arr), run_time=0.6)
        self.play(GrowArrow(AC_arr), run_time=0.6)

        # 坐标标注
        coords_text = self.txt(
            "A(-2,-1)  B(0,0)  C(2,1)",
            size=20, color=GRAY_A
        )
        coords_text.move_to(DOWN * 3.2)
        self.play(FadeIn(coords_text), run_time=0.4)

        # 共线条件公式
        formula_coll = self.tex(
            r"\overrightarrow{AB} = \lambda \overrightarrow{AC}",
            size=28
        )
        formula_coll.move_to(DOWN * 4.2)
        self.play(Write(formula_coll), run_time=0.7)

        # 计算展示
        calc1 = self.tex(
            r"\overrightarrow{AB} = (2, 1),\quad \overrightarrow{AC} = (4, 2)",
            size=22, color=GRAY_A
        )
        calc1.move_to(DOWN * 5.1)
        self.play(FadeIn(calc1, shift=UP * 0.1), run_time=0.5)

        calc2 = self.tex(
            r"\overrightarrow{AB} = \frac{1}{2}\,\overrightarrow{AC}",
            size=24, color=YELLOW
        )
        calc2.move_to(DOWN * 5.9)
        self.play(Write(calc2), run_time=0.6)

        # 结论
        concl = self.txt("∴ A, B, C 三点共线 ✓", size=24, color=C_COLL)
        concl.move_to(DOWN * 6.7)
        self.play(FadeIn(concl, scale=0.9), run_time=0.5)

        # 直线穿过三点动画
        line_through = Line(
            A_s + LEFT * 0.2, C_s + RIGHT * 0.2,
            color=C_COLL, stroke_width=2
        )
        self.play(Create(line_through), run_time=0.8)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(dot_A), FadeOut(dot_B), FadeOut(dot_C),
            FadeOut(lbl_A), FadeOut(lbl_B), FadeOut(lbl_C),
            FadeOut(AB_arr), FadeOut(AC_arr),
            FadeOut(coords_text),
            FadeOut(formula_coll),
            FadeOut(calc1), FadeOut(calc2),
            FadeOut(concl), FadeOut(line_through),
            run_time=0.5
        )

    # ============================================================
    #  Scene 7: 总结 + 结尾
    # ============================================================
    def scene_7_summary_outro(self):
        # 淡出坐标系和向量a
        self.play(
            FadeOut(self.axes),
            FadeOut(self.arrow_a),
            run_time=0.5
        )

        # 总结标题
        summary_title = Text("向量应用 总结", font=FONT, font_size=40, color=C_GOLD, weight=BOLD)
        summary_title.move_to(UP * 5.5)
        self.play(Write(summary_title), run_time=0.7)

        # 5条总结卡片
        card_data = [
            ("① 平行", r"\vec{a} \parallel \vec{b}: x_1 y_2 - x_2 y_1 = 0", C_PARA),
            ("② 垂直", r"\vec{a} \perp \vec{b}: \vec{a} \cdot \vec{b} = 0", C_PERP),
            ("③ 夹角", r"\cos\theta = \dfrac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|}", C_ANGLE),
            ("④ 共线", r"\overrightarrow{AB} = \lambda \overrightarrow{AC}", C_COLL),
            ("⑤ 面积", r"S = \dfrac{1}{2}|x_1 y_2 - x_2 y_1|", PURPLE_B),
        ]

        cards = VGroup()
        for label, formula_str, color in card_data:
            icon = Text(label, font=FONT, font_size=22, color=color, weight=BOLD)
            formula = MathTex(formula_str, font_size=22, color=WHITE)
            row = VGroup(icon, formula).arrange(RIGHT, buff=0.3)
            # Add a subtle background bar
            bg = BackgroundRectangle(row, fill_opacity=0.12, fill_color=color, buff=0.12)
            card = VGroup(bg, row)
            cards.add(card)

        cards.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        cards.move_to(UP * 1.5)
        cards.set_x(0)

        self.play(
            LaggedStart(*[FadeIn(c, shift=RIGHT * 0.2) for c in cards], lag_ratio=0.15),
            run_time=1.5
        )
        self.wait(1.0)

        # 口号
        slogan = Text("记公式，理思路，向量不怕了!", font=FONT, font_size=26, color=YELLOW)
        slogan.move_to(DOWN * 3.8)
        self.play(FadeIn(slogan, scale=0.95), run_time=0.6)
        self.wait(0.5)

        # 作者信息放大
        outro_name = Text("上海初高中数学直通车", font=FONT, font_size=36, color=WHITE, weight=BOLD)
        outro_id = Text("@emptyandcalm", font=FONT, font_size=26, color=GRAY_B)
        outro_grp = VGroup(outro_name, outro_id).arrange(DOWN, buff=0.2)
        outro_grp.move_to(DOWN * 5.5)
        self.play(
            FadeOut(self.author_bar),
            FadeIn(outro_grp, shift=UP * 0.3),
            run_time=0.7
        )

        follow_text = Text("关注我, 获得更多数学技巧!", font=FONT, font_size=28, color=C_ANGLE)
        follow_text.move_to(DOWN * 6.8)
        self.play(FadeIn(follow_text, shift=UP * 0.2), run_time=0.5)

        self.wait(1.5)

        # 最终淡出
        self.play(
            FadeOut(summary_title),
            FadeOut(cards),
            FadeOut(slogan),
            FadeOut(outro_grp),
            FadeOut(follow_text),
            run_time=1.0
        )

# # 快速预览
# manim -pql vector_applications.py VectorApplications

# # 高质量输出
# manim -qh vector_applications.py VectorApplications