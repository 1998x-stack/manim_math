"""
向量数量积 - Vector Dot Product Teaching Animation
高二数学第八章 - 平面向量的坐标表示

内容: 向量数量积的定义、坐标公式、垂直条件、模长公式
目标观众: 高二学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class VectorDotProduct(Scene):
    """
    向量数量积教学动画

    场景顺序:
    1. 开场钩子
    2. 几何定义 a·b = |a||b|cosθ
    3. 坐标公式 a·b = x1x2 + y1y2
    4. 数值验证
    5. 向量垂直条件
    6. 模长公式
    7. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_VEC_A = "#e74c3c"       # 红色 - 向量a
        self.COLOR_VEC_B = "#3498db"       # 蓝色 - 向量b
        self.COLOR_ANGLE = "#f39c12"       # 橙色 - 夹角
        self.COLOR_RESULT = "#2ecc71"      # 绿色 - 数量积/结果
        self.COLOR_FORMULA = YELLOW        # 公式高亮
        self.COLOR_AUX = "#95a5a6"         # 辅助线

        # 初始化几何数据
        self.setup_geometry()

        # 执行各场景
        self.scene_1_hook()
        self.scene_2_geometric_def()
        self.scene_3_coordinate_formula()
        self.scene_4_verify()
        self.scene_5_perpendicular()
        self.scene_6_magnitude()
        self.scene_7_outro()

    # =========================================================
    # 几何初始化
    # =========================================================
    def setup_geometry(self):
        """统一初始化所有几何数据"""
        # ---- 坐标系参数 ----
        self.AXES_ORIGIN = np.array([0, 0.5, 0])  # 坐标系在场景中的位置
        self.AXES_SCALE = 1.2                       # 坐标轴缩放

        # ---- 向量定义 (原始坐标) ----
        self.VEC_A_COORDS = np.array([2.0, 1.0, 0])   # a = (2, 1)
        self.VEC_B_COORDS = np.array([0.5, 2.0, 0])   # b = (0.5, 2)

        # 缩放到场景单位
        S = self.AXES_SCALE
        self.vec_a_end = self.AXES_ORIGIN + self.VEC_A_COORDS * S
        self.vec_b_end = self.AXES_ORIGIN + self.VEC_B_COORDS * S

        # ---- 数量积计算 ----
        a = self.VEC_A_COORDS[:2]
        b = self.VEC_B_COORDS[:2]

        self.dot_product = float(np.dot(a, b))          # x1x2 + y1y2
        self.mag_a = float(np.linalg.norm(a))
        self.mag_b = float(np.linalg.norm(b))
        self.cos_theta = self.dot_product / (self.mag_a * self.mag_b)
        self.cos_theta = np.clip(self.cos_theta, -1.0, 1.0)
        self.theta = float(np.arccos(self.cos_theta))   # 夹角弧度

        # ---- 垂直向量 (Scene 5) ----
        self.VEC_P_COORDS = np.array([1.5, 0, 0])       # p = (1.5, 0) 水平
        self.VEC_Q_COORDS = np.array([0, 1.5, 0])       # q = (0, 1.5) 垂直
        # p · q = 1.5*0 + 0*1.5 = 0  ✓

        self.vec_p_end = self.AXES_ORIGIN + self.VEC_P_COORDS * S
        self.vec_q_end = self.AXES_ORIGIN + self.VEC_Q_COORDS * S

        # ---- 验证 ----
        self._verify_geometry()

    def _verify_geometry(self):
        """验证几何数据"""
        epsilon = 1e-8

        # 验证数量积两种算法一致
        geo_dot = self.mag_a * self.mag_b * self.cos_theta
        coord_dot = self.dot_product
        assert abs(geo_dot - coord_dot) < 1e-6, f"数量积不一致: {geo_dot} vs {coord_dot}"

        # 验证垂直向量点积为0
        p = self.VEC_P_COORDS[:2]
        q = self.VEC_Q_COORDS[:2]
        assert abs(np.dot(p, q)) < epsilon, "垂直向量点积不为0"

        # 验证余弦在合理范围
        assert -1 <= self.cos_theta <= 1, f"余弦值超出范围: {self.cos_theta}"

        print(f"✓ 几何验证通过")
        print(f"  a = {self.VEC_A_COORDS[:2]}, b = {self.VEC_B_COORDS[:2]}")
        print(f"  a·b = {self.dot_product:.4f}")
        print(f"  |a| = {self.mag_a:.4f}, |b| = {self.mag_b:.4f}")
        print(f"  cos θ = {self.cos_theta:.4f}, θ = {np.degrees(self.theta):.2f}°")

    # =========================================================
    # 辅助方法
    # =========================================================
    def make_axes(self, x_range=(-1, 4), y_range=(-1, 4), scale=1.2):
        """创建坐标系"""
        axes = Axes(
            x_range=[x_range[0], x_range[1], 1],
            y_range=[y_range[0], y_range[1], 1],
            x_length=(x_range[1] - x_range[0]) * scale,
            y_length=(y_range[1] - y_range[0]) * scale,
            axis_config={
                "color": WHITE,
                "stroke_width": 2,
                "include_tip": True,
                "tip_length": 0.15,
            },
            x_axis_config={"include_numbers": False},
            y_axis_config={"include_numbers": False},
        ).move_to(self.AXES_ORIGIN)
        return axes

    # =========================================================
    # Scene 1: 开场钩子
    # =========================================================
    def scene_1_hook(self):
        # 作者信息
        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B,
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook_line1 = Text(
            "两个向量能相乘吗？",
            font="Noto Sans CJK SC",
            font_size=40,
            color=YELLOW,
        ).move_to(UP * 5.5)

        hook_line2 = Text(
            "结果是什么？",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE,
        ).move_to(UP * 4.7)

        self.play(Write(hook_line1), run_time=0.8)
        self.play(FadeIn(hook_line2, shift=UP * 0.2), run_time=0.5)

        # 示意两个向量
        preview_axes = self.make_axes(scale=0.9)
        preview_axes.move_to(DOWN * 0.5)

        origin_pt = preview_axes.c2p(0, 0)

        vec_a_arrow = Arrow(
            start=origin_pt,
            end=preview_axes.c2p(2, 1),
            color=self.COLOR_VEC_A,
            buff=0,
            max_tip_length_to_length_ratio=0.12,
            stroke_width=5,
        )
        vec_b_arrow = Arrow(
            start=origin_pt,
            end=preview_axes.c2p(0.5, 2),
            color=self.COLOR_VEC_B,
            buff=0,
            max_tip_length_to_length_ratio=0.12,
            stroke_width=5,
        )

        label_a = MathTex(r"\vec{a}", color=self.COLOR_VEC_A, font_size=36).next_to(
            preview_axes.c2p(2, 1), RIGHT, buff=0.15
        )
        label_b = MathTex(r"\vec{b}", color=self.COLOR_VEC_B, font_size=36).next_to(
            preview_axes.c2p(0.5, 2), UP, buff=0.1
        )

        self.play(Create(preview_axes), run_time=0.6)
        self.play(
            GrowArrow(vec_a_arrow),
            GrowArrow(vec_b_arrow),
            run_time=0.8,
        )
        self.play(Write(label_a), Write(label_b), run_time=0.5)

        # 问号中间动画
        q_mark = Text("?", font_size=80, color=YELLOW).move_to(ORIGIN + DOWN * 0.5)
        self.wait(0.5)

        # 清理，保留坐标系和向量给下一场景
        self.play(
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            run_time=0.4,
        )

        # 存储供后续使用
        self.preview_axes = preview_axes
        self.vec_a_arrow = vec_a_arrow
        self.vec_b_arrow = vec_b_arrow
        self.label_a = label_a
        self.label_b = label_b

    # =========================================================
    # Scene 2: 几何定义
    # =========================================================
    def scene_2_geometric_def(self):
        # 标题
        title = Text(
            "数量积的定义",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_FORMULA,
        ).move_to(UP * 6.2)

        subtitle = Text(
            "（点积 / 内积）",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_B,
        ).next_to(title, DOWN, buff=0.1)

        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.5)

        # 在坐标轴上标出夹角
        # 夹角弧 - 使用 Angle.from_three_points
        origin_pt = self.preview_axes.c2p(0, 0)
        tip_a = self.preview_axes.c2p(2, 1)
        tip_b = self.preview_axes.c2p(0.5, 2)

        # 计算叉积判断方向
        va = np.array([2, 1, 0])
        vb = np.array([0.5, 2, 0])
        cross_z = va[0] * vb[1] - va[1] * vb[0]  # 2*2 - 1*0.5 = 3.5 > 0 => 逆时针

        angle_arc = Angle.from_three_points(
            tip_a,
            origin_pt,
            tip_b,
            radius=0.6,
            color=self.COLOR_ANGLE,
            other_angle=(cross_z < 0),
        )

        theta_label = MathTex(r"\theta", color=self.COLOR_ANGLE, font_size=32)
        # 标签位于弧中间位置
        mid_angle = self.theta / 2
        angle_of_a = np.arctan2(va[1], va[0])
        label_angle = angle_of_a + mid_angle
        label_radius = 0.85
        theta_label.move_to(
            origin_pt
            + label_radius
            * np.array([np.cos(label_angle), np.sin(label_angle), 0])
        )

        self.play(Create(angle_arc), run_time=0.6)
        self.play(Write(theta_label), run_time=0.4)

        self.wait(0.3)

        # 核心公式
        formula_box = RoundedRectangle(
            corner_radius=0.2,
            width=7.5,
            height=1.2,
            color=self.COLOR_ANGLE,
            stroke_width=2,
            fill_color="#1a1a2e",
            fill_opacity=0.9,
        ).move_to(DOWN * 3.8)

        formula = MathTex(
            r"\vec{a} \cdot \vec{b}",
            r"=",
            r"|\vec{a}|",
            r"|\vec{b}|",
            r"\cos\theta",
            font_size=40,
        ).move_to(DOWN * 3.8)
        formula[0].set_color(self.COLOR_FORMULA)
        formula[2].set_color(self.COLOR_VEC_A)
        formula[3].set_color(self.COLOR_VEC_B)
        formula[4].set_color(self.COLOR_ANGLE)

        self.play(Create(formula_box), run_time=0.4)
        self.play(Write(formula), run_time=1.0)
        self.wait(0.5)

        # 说明1: θ的范围
        range_text = Text(
            "夹角范围：0 ≤ θ ≤ π",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A,
        ).move_to(DOWN * 5.0)

        self.play(FadeIn(range_text, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 说明2: 结果是标量！
        scalar_highlight = RoundedRectangle(
            corner_radius=0.15,
            width=5.0,
            height=0.6,
            color=self.COLOR_RESULT,
            stroke_width=2,
            fill_color=self.COLOR_RESULT,
            fill_opacity=0.15,
        ).move_to(DOWN * 5.9)

        scalar_text = Text(
            "结果是标量（数），不是向量！",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_RESULT,
        ).move_to(DOWN * 5.9)

        self.play(Create(scalar_highlight), Write(scalar_text), run_time=0.7)
        self.wait(2.0)  # 关键概念，多停留

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(angle_arc),
            FadeOut(theta_label),
            FadeOut(range_text),
            FadeOut(scalar_highlight),
            FadeOut(scalar_text),
            run_time=0.5,
        )

        # 保留 formula 和 formula_box
        self.formula_geo = formula
        self.formula_box_geo = formula_box

    # =========================================================
    # Scene 3: 坐标公式
    # =========================================================
    def scene_3_coordinate_formula(self):
        title = Text(
            "坐标计算公式",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_FORMULA,
        ).move_to(UP * 6.2)

        self.play(FadeIn(title), run_time=0.4)

        # 标注坐标
        axes = self.preview_axes
        origin_pt = axes.c2p(0, 0)

        # 坐标标注
        a_coord = MathTex(
            r"\vec{a} = (2, 1)",
            color=self.COLOR_VEC_A,
            font_size=30,
        ).move_to(UP * 5.2)

        b_coord = MathTex(
            r"\vec{b} = (0.5, 2)",
            color=self.COLOR_VEC_B,
            font_size=30,
        ).next_to(a_coord, DOWN, buff=0.2)

        self.play(Write(a_coord), run_time=0.6)
        self.play(Write(b_coord), run_time=0.6)
        self.wait(0.3)

        # 坐标公式框
        coord_formula_box = RoundedRectangle(
            corner_radius=0.2,
            width=7.5,
            height=1.2,
            color=self.COLOR_VEC_B,
            stroke_width=2,
            fill_color="#1a1a2e",
            fill_opacity=0.9,
        ).move_to(DOWN * 2.5)

        coord_formula = MathTex(
            r"\vec{a} \cdot \vec{b}",
            r"=",
            r"x_1 x_2",
            r"+",
            r"y_1 y_2",
            font_size=38,
        ).move_to(DOWN * 2.5)
        coord_formula[0].set_color(self.COLOR_FORMULA)
        coord_formula[2].set_color(self.COLOR_VEC_A)
        coord_formula[4].set_color(self.COLOR_VEC_B)

        self.play(Create(coord_formula_box), run_time=0.4)
        self.play(Write(coord_formula), run_time=1.0)
        self.wait(0.3)

        # 代入数值计算
        calc_step1 = MathTex(
            r"= 2 \times 0.5 + 1 \times 2",
            font_size=34,
            color=WHITE,
        ).move_to(DOWN * 4.0)

        calc_step2 = MathTex(
            r"= 1 + 2",
            font_size=34,
            color=WHITE,
        ).move_to(DOWN * 5.0)

        calc_result = MathTex(
            r"= 3",
            font_size=40,
            color=self.COLOR_RESULT,
        ).next_to(calc_step2, DOWN, buff=0.3)

        self.play(Write(calc_step1), run_time=0.8)
        self.play(Write(calc_step2), run_time=0.6)
        self.play(Write(calc_result), run_time=0.5)

        # 高亮结果
        result_circle = Circle(
            radius=0.4,
            color=self.COLOR_RESULT,
            stroke_width=3,
        ).move_to(calc_result)
        self.play(Create(result_circle), run_time=0.5)
        self.wait(1.5)

        # 清理计算步骤，保留公式
        self.play(
            FadeOut(title),
            FadeOut(a_coord),
            FadeOut(b_coord),
            FadeOut(calc_step1),
            FadeOut(calc_step2),
            FadeOut(calc_result),
            FadeOut(result_circle),
            run_time=0.5,
        )

        self.coord_formula = coord_formula
        self.coord_formula_box = coord_formula_box

    # =========================================================
    # Scene 4: 数值验证 两种公式对比
    # =========================================================
    def scene_4_verify(self):
        title = Text(
            "两种公式，结果相同！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_FORMULA,
        ).move_to(UP * 6.2)

        self.play(FadeIn(title), run_time=0.4)

        # 移动已有公式到上方
        self.play(
            self.formula_box_geo.animate.move_to(UP * 4.2).scale(0.85),
            self.formula_geo.animate.move_to(UP * 4.2).scale(0.85),
            self.coord_formula_box.animate.move_to(UP * 2.8).scale(0.85),
            self.coord_formula.animate.move_to(UP * 2.8).scale(0.85),
            run_time=0.8,
        )

        # 等于号连接
        equal_text = Text(
            "都等于",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A,
        ).move_to(UP * 1.6)

        result_big = MathTex(
            r"\vec{a} \cdot \vec{b} = 3",
            font_size=52,
            color=self.COLOR_RESULT,
        ).move_to(UP * 0.8)

        self.play(FadeIn(equal_text), run_time=0.3)
        self.play(Write(result_big), run_time=0.7)
        self.wait(0.5)

        # 几何公式验证数值
        verify_geo = MathTex(
            r"\sqrt{5} \cdot \sqrt{4.25} \cdot \cos\theta \approx 3",
            font_size=26,
            color=GRAY_A,
        ).move_to(DOWN * 0.3)

        self.play(FadeIn(verify_geo), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(equal_text),
            FadeOut(result_big),
            FadeOut(verify_geo),
            FadeOut(self.formula_box_geo),
            FadeOut(self.formula_geo),
            FadeOut(self.coord_formula_box),
            FadeOut(self.coord_formula),
            run_time=0.6,
        )

    # =========================================================
    # Scene 5: 向量垂直条件
    # =========================================================
    def scene_5_perpendicular(self):
        # 清除旧坐标系和向量
        self.play(
            FadeOut(self.preview_axes),
            FadeOut(self.vec_a_arrow),
            FadeOut(self.vec_b_arrow),
            FadeOut(self.label_a),
            FadeOut(self.label_b),
            run_time=0.4,
        )

        title = Text(
            "向量垂直的条件",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_FORMULA,
        ).move_to(UP * 6.2)

        self.play(FadeIn(title), run_time=0.4)

        # 新坐标系，居中偏上
        axes2 = Axes(
            x_range=[-0.5, 3, 1],
            y_range=[-0.5, 3, 1],
            x_length=3.5 * self.AXES_SCALE,
            y_length=3.5 * self.AXES_SCALE,
            axis_config={
                "color": WHITE,
                "stroke_width": 2,
                "include_tip": True,
                "tip_length": 0.15,
            },
        ).move_to(UP * 2.0)

        origin_pt = axes2.c2p(0, 0)
        p_tip = axes2.c2p(1.5, 0)
        q_tip = axes2.c2p(0, 1.5)

        vec_p = Arrow(
            start=origin_pt,
            end=p_tip,
            color=self.COLOR_VEC_A,
            buff=0,
            max_tip_length_to_length_ratio=0.15,
            stroke_width=5,
        )
        vec_q = Arrow(
            start=origin_pt,
            end=q_tip,
            color=self.COLOR_VEC_B,
            buff=0,
            max_tip_length_to_length_ratio=0.15,
            stroke_width=5,
        )

        label_p = MathTex(r"\vec{p} = (1.5,\ 0)", color=self.COLOR_VEC_A, font_size=28).next_to(
            p_tip, RIGHT, buff=0.1
        )
        label_q = MathTex(r"\vec{q} = (0,\ 1.5)", color=self.COLOR_VEC_B, font_size=28).next_to(
            q_tip, UP, buff=0.1
        )

        # 直角标记
        right_angle_mark = self._make_right_angle(origin_pt, p_tip, q_tip, size=0.22)

        self.play(Create(axes2), run_time=0.5)
        self.play(GrowArrow(vec_p), GrowArrow(vec_q), run_time=0.7)
        self.play(Write(label_p), Write(label_q), run_time=0.5)
        self.play(Create(right_angle_mark), run_time=0.4)

        # 计算点积
        calc_perp = MathTex(
            r"\vec{p} \cdot \vec{q} = 1.5 \times 0 + 0 \times 1.5 = 0",
            font_size=30,
            color=WHITE,
        ).move_to(DOWN * 1.5)

        self.play(Write(calc_perp), run_time=0.8)
        self.wait(0.5)

        # 垂直条件框
        perp_box = RoundedRectangle(
            corner_radius=0.2,
            width=7.8,
            height=1.5,
            color=self.COLOR_RESULT,
            stroke_width=3,
            fill_color="#1a2a1a",
            fill_opacity=0.9,
        ).move_to(DOWN * 3.4)

        perp_formula_line1 = MathTex(
            r"\vec{a} \perp \vec{b}",
            r"\ \Longleftrightarrow\ ",
            r"\vec{a} \cdot \vec{b} = 0",
            font_size=36,
        ).move_to(DOWN * 3.0)
        perp_formula_line1[0].set_color(self.COLOR_VEC_A)
        perp_formula_line1[2].set_color(self.COLOR_RESULT)

        perp_formula_line2 = MathTex(
            r"\Longleftrightarrow\ x_1 x_2 + y_1 y_2 = 0",
            font_size=30,
            color=GRAY_A,
        ).move_to(DOWN * 3.85)

        self.play(Create(perp_box), run_time=0.4)
        self.play(Write(perp_formula_line1), run_time=0.8)
        self.play(Write(perp_formula_line2), run_time=0.7)
        self.wait(2.0)

        # 强调
        self.play(
            perp_formula_line1[0].animate.set_color(YELLOW),
            perp_formula_line1[2].animate.set_color(YELLOW),
            run_time=0.5,
        )
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(axes2),
            FadeOut(vec_p),
            FadeOut(vec_q),
            FadeOut(label_p),
            FadeOut(label_q),
            FadeOut(right_angle_mark),
            FadeOut(calc_perp),
            FadeOut(perp_box),
            FadeOut(perp_formula_line1),
            FadeOut(perp_formula_line2),
            run_time=0.6,
        )

    def _make_right_angle(self, corner, p1, p2, size=0.2):
        """创建直角标记"""
        v1 = (p1 - corner)
        v1 = v1 / (np.linalg.norm(v1) + 1e-10) * size
        v2 = (p2 - corner)
        v2 = v2 / (np.linalg.norm(v2) + 1e-10) * size
        sq = Polygon(
            corner + v1,
            corner + v1 + v2,
            corner + v2,
            color=YELLOW,
            stroke_width=2,
            fill_opacity=0,
        )
        return sq

    # =========================================================
    # Scene 6: 模长公式
    # =========================================================
    def scene_6_magnitude(self):
        title = Text(
            "向量的模长",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_FORMULA,
        ).move_to(UP * 6.2)

        self.play(FadeIn(title), run_time=0.4)

        # 关键公式 a·a = |a|²
        formula1 = MathTex(
            r"\vec{a} \cdot \vec{a} = |\vec{a}|^2",
            font_size=44,
            color=self.COLOR_VEC_A,
        ).move_to(UP * 4.0)

        # 因为 θ=0 时 cosθ=1
        explain = MathTex(
            r"(\theta = 0,\ \cos 0 = 1)",
            font_size=28,
            color=GRAY_A,
        ).next_to(formula1, DOWN, buff=0.25)

        self.play(Write(formula1), run_time=0.8)
        self.play(FadeIn(explain), run_time=0.4)
        self.wait(0.5)

        # 模长公式
        mag_box = RoundedRectangle(
            corner_radius=0.2,
            width=6.5,
            height=1.4,
            color=self.COLOR_RESULT,
            stroke_width=3,
            fill_color="#1a1a2e",
            fill_opacity=0.9,
        ).move_to(UP * 1.8)

        mag_formula = MathTex(
            r"|\vec{a}| = \sqrt{\vec{a} \cdot \vec{a}} = \sqrt{x^2 + y^2}",
            font_size=34,
        ).move_to(UP * 1.8)
        mag_formula.set_color(self.COLOR_RESULT)

        self.play(Create(mag_box), run_time=0.4)
        self.play(Write(mag_formula), run_time=1.0)
        self.wait(0.5)

        # cos θ公式
        cos_box = RoundedRectangle(
            corner_radius=0.2,
            width=6.5,
            height=1.4,
            color=self.COLOR_ANGLE,
            stroke_width=2,
            fill_color="#1a1a2e",
            fill_opacity=0.9,
        ).move_to(DOWN * 0.2)

        cos_formula = MathTex(
            r"\cos\theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}|\ |\vec{b}|}",
            font_size=36,
            color=self.COLOR_ANGLE,
        ).move_to(DOWN * 0.2)

        self.play(Create(cos_box), run_time=0.4)
        self.play(Write(cos_formula), run_time=0.8)
        self.wait(2.5)

        # 总结卡片
        summary_title = Text(
            "核心公式总结",
            font="Noto Sans CJK SC",
            font_size=30,
            color=YELLOW,
        ).move_to(DOWN * 2.2)

        summary_items = VGroup(
            MathTex(
                r"\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta",
                font_size=26,
            ),
            MathTex(
                r"\vec{a} \cdot \vec{b} = x_1 x_2 + y_1 y_2",
                font_size=26,
            ),
            MathTex(
                r"\vec{a} \perp \vec{b} \Leftrightarrow \vec{a}\cdot\vec{b}=0",
                font_size=26,
            ),
        ).arrange(DOWN, buff=0.35).move_to(DOWN * 4.2)

        summary_items[0].set_color(self.COLOR_VEC_A)
        summary_items[1].set_color(self.COLOR_VEC_B)
        summary_items[2].set_color(self.COLOR_RESULT)

        self.play(FadeIn(summary_title), run_time=0.4)
        for item in summary_items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.4)

        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula1),
            FadeOut(explain),
            FadeOut(mag_box),
            FadeOut(mag_formula),
            FadeOut(cos_box),
            FadeOut(cos_formula),
            FadeOut(summary_title),
            FadeOut(summary_items),
            run_time=0.6,
        )

    # =========================================================
    # Scene 7: 片尾
    # =========================================================
    def scene_7_outro(self):
        # 作者信息放大
        outro_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=42,
            color=WHITE,
        ).move_to(UP * 2.0)

        outro_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B,
        ).next_to(outro_name, DOWN, buff=0.3)

        self.play(
            Transform(self.author_bar, outro_name),
            run_time=0.8,
        )
        self.play(FadeIn(outro_id, shift=UP * 0.2), run_time=0.5)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=YELLOW,
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(follow_text, scale=1.05), run_time=0.7)

        # 装饰：三个向量闪烁
        deco_arrows = VGroup(
            Arrow(ORIGIN, RIGHT * 1.2, color=self.COLOR_VEC_A, buff=0, stroke_width=4),
            Arrow(ORIGIN, UP * 1.2, color=self.COLOR_VEC_B, buff=0, stroke_width=4),
            Arrow(ORIGIN, (RIGHT + UP) * 0.85, color=self.COLOR_RESULT, buff=0, stroke_width=4),
        ).arrange(RIGHT, buff=0.8).move_to(DOWN * 2.5)

        dot_symbol = MathTex(r"\cdot", font_size=60, color=YELLOW).move_to(DOWN * 4.2)

        for arrow in deco_arrows:
            self.play(GrowArrow(arrow), run_time=0.3)
        self.play(Write(dot_symbol), run_time=0.4)

        self.wait(1.5)

        self.play(
            FadeOut(self.author_bar),
            FadeOut(outro_id),
            FadeOut(follow_text),
            FadeOut(deco_arrows),
            FadeOut(dot_symbol),
            run_time=1.0,
        )


# 运行命令:
# manim -pql vector_dot_product.py VectorDotProduct   # 快速预览
# manim -qh vector_dot_product.py VectorDotProduct    # 高质量