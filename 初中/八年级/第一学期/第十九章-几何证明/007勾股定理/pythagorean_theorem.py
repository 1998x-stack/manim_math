"""
勾股定理 - 数学教学动画
Pythagorean Theorem - Math Teaching Animation

年级: 八年级第一学期
章节: 第十九章 几何证明
知识点: 勾股定理 a² + b² = c²

格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# TikTok竖屏全局配置
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class PythagoreanTheorem(Scene):
    """
    勾股定理教学动画
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 构造三个正方形 - 可视化 a², b², c²
    3. 面积揭示定理 - a² + b² = c²
    4. 数值验证 - 3-4-5 勾股数
    5. 公式变形 - 求不同边长
    6. 片尾 - 作者信息
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # ===== 配色方案 =====
        self.C_SIDE_A = "#4FC3F7"    # 浅蓝 - 直角边a
        self.C_SIDE_B = "#81C784"    # 浅绿 - 直角边b
        self.C_SIDE_C = "#FFB74D"    # 浅橙 - 斜边c
        self.C_SQ_A = "#1565C0"      # 深蓝 - a²方块
        self.C_SQ_B = "#2E7D32"      # 深绿 - b²方块
        self.C_SQ_C = "#E65100"      # 深橙 - c²方块
        self.C_RIGHT = "#E53935"     # 红色 - 直角标记
        self.C_FORMULA = "#FFD700"   # 金色 - 公式
        self.C_HIGHLIGHT = "#FF4081" # 粉红 - 高亮

        # ===== 统一初始化几何数据 =====
        self.setup_geometry()

        # ===== 执行各场景 =====
        self.scene_1_opening()
        self.scene_2_squares()
        self.scene_3_reveal_theorem()
        self.scene_4_numeric_verify()
        self.scene_5_formula_variants()
        self.scene_6_outro()

    # ============================================================
    # 几何初始化
    # ============================================================

    def setup_geometry(self):
        """
        统一初始化所有几何坐标
        使用 3:4:5 勾股数比例，放大1.5倍 → 1.8 : 2.4 : 3.0
        """
        # ========== 基准参数 ==========
        # 3:4:5 → 1.8:2.4:3.0 (缩放0.6倍便于显示)
        self.a_len = 1.8   # CA = 直角边a (水平)
        self.b_len = 2.4   # CB = 直角边b (垂直)
        self.c_len = 3.0   # AB = 斜边c

        # 验证勾股关系
        assert abs(self.a_len**2 + self.b_len**2 - self.c_len**2) < 1e-10, \
            f"勾股关系错误: {self.a_len}²+{self.b_len}²≠{self.c_len}²"

        # ========== 主三角形顶点 ==========
        # 将三角形置于主内容区中部偏上
        self.TRIANGLE_CENTER = np.array([0.0, 1.5, 0.0])

        # C: 直角顶点 (左下)
        self.C = np.array([-self.a_len / 2, 0.0, 0.0]) + self.TRIANGLE_CENTER
        # A: a边端点 (右下)
        self.A = np.array([self.a_len / 2, 0.0, 0.0]) + self.TRIANGLE_CENTER
        # B: b边端点 (左上)
        self.B = np.array([-self.a_len / 2, self.b_len, 0.0]) + self.TRIANGLE_CENTER

        # 具体坐标: C=(-0.9, 1.5), A=(0.9, 1.5), B=(-0.9, 3.9)

        # ========== 边长验证 ==========
        self.measured_a = np.linalg.norm(self.A - self.C)
        self.measured_b = np.linalg.norm(self.B - self.C)
        self.measured_c = np.linalg.norm(self.B - self.A)

        assert abs(self.measured_a - self.a_len) < 1e-10, "a边长不匹配"
        assert abs(self.measured_b - self.b_len) < 1e-10, "b边长不匹配"
        assert abs(self.measured_c - self.c_len) < 1e-10, \
            f"c边长不匹配: {self.measured_c} vs {self.c_len}"

        # ========== 三个正方形顶点计算 ==========
        # 正方形a: 在CA边外侧(向下展开)
        dir_CA = self.A - self.C
        dir_CA_norm = dir_CA / np.linalg.norm(dir_CA)
        # 外法向量: 向下(y负)
        outer_a = np.array([0.0, -1.0, 0.0])
        self.sq_a_pts = [
            self.C.copy(),
            self.A.copy(),
            self.A + outer_a * self.a_len,
            self.C + outer_a * self.a_len,
        ]

        # 正方形b: 在CB边外侧(向左展开)
        dir_CB = self.B - self.C
        dir_CB_norm = dir_CB / np.linalg.norm(dir_CB)
        # 外法向量: 向左(x负)
        outer_b = np.array([-1.0, 0.0, 0.0])
        self.sq_b_pts = [
            self.C.copy(),
            self.B.copy(),
            self.B + outer_b * self.b_len,
            self.C + outer_b * self.b_len,
        ]

        # 正方形c: 在AB(斜边)外侧展开
        # AB向量: B - A = (-1.8, 2.4, 0)
        dir_AB = self.B - self.A
        # 外法向量: 向右上方(逆时针转90°)
        # 旋转90°逆时针: (x,y) → (-y, x)
        outer_c_raw = np.array([-dir_AB[1], dir_AB[0], 0.0])
        outer_c = outer_c_raw / np.linalg.norm(outer_c_raw)  # 单位化
        # 注意: 向量长度为c_len
        self.sq_c_pts = [
            self.A.copy(),
            self.B.copy(),
            self.B + outer_c * self.c_len,
            self.A + outer_c * self.c_len,
        ]

        # 验证正方形c的顶点
        # AB边长 = c_len ✓
        # A到sq_c_pts[3]距离应该= c_len
        dist_check = np.linalg.norm(self.sq_c_pts[3] - self.A)
        assert abs(dist_check - self.c_len) < 1e-10, \
            f"正方形c顶点距离错误: {dist_check}"

        # 验证正方形c是正方形 (所有边等长)
        for i in range(4):
            p1 = self.sq_c_pts[i]
            p2 = self.sq_c_pts[(i + 1) % 4]
            d = np.linalg.norm(p2 - p1)
            assert abs(d - self.c_len) < 1e-10, \
                f"正方形c第{i}边长度错误: {d} vs {self.c_len}"

        # ========== 直角标记参数 ==========
        self.RIGHT_ANGLE_SIZE = 0.2

        print("✓ 几何初始化验证通过")
        print(f"  三角形顶点: C={self.C}, A={self.A}, B={self.B}")
        print(f"  边长: a={self.measured_a:.4f}, b={self.measured_b:.4f}, c={self.measured_c:.4f}")
        print(f"  勾股验证: {self.measured_a**2:.4f} + {self.measured_b**2:.4f} = {self.measured_c**2:.4f}")

    # ============================================================
    # 辅助方法
    # ============================================================

    def create_right_angle_mark(self, corner, p1, p2, size=0.2, color=None):
        """
        创建直角标记小方块
        corner: 直角顶点
        p1, p2: 两条边上的点（方向参考）
        """
        if color is None:
            color = self.C_RIGHT
        v1 = (p1 - corner)
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = (p2 - corner)
        v2 = v2 / np.linalg.norm(v2) * size
        square = Polygon(
            corner,
            corner + v1,
            corner + v1 + v2,
            corner + v2,
            color=color,
            stroke_width=2.0,
            fill_opacity=0,
        )
        return square

    def create_main_triangle(self, stroke_width=3):
        """创建主三角形"""
        tri = Polygon(
            self.A, self.B, self.C,
            color=WHITE,
            stroke_width=stroke_width,
            fill_opacity=0,
        )
        return tri

    def create_square(self, pts, color, fill_opacity=0.35, stroke_width=2.5):
        """由4个顶点创建正方形"""
        sq = Polygon(*pts, color=color, stroke_width=stroke_width,
                     fill_color=color, fill_opacity=fill_opacity)
        return sq

    def get_square_center(self, pts):
        """计算正方形中心"""
        return sum(pts) / len(pts)

    # ============================================================
    # Scene 1: 开场钩子
    # ============================================================

    def scene_1_opening(self):
        """开场: 抓住注意力，引出勾股定理"""

        # ── 作者信息 ──
        self.author_info = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color=GRAY_B,
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        # ── 钩子问题 ──
        hook_line1 = Text(
            "直角三角形的三边",
            font="PingFang SC",
            font_size=34,
            color=WHITE,
        ).move_to(UP * 6.0)
        hook_line2 = Text(
            "之间有什么神奇关系？",
            font="PingFang SC",
            font_size=34,
            color=self.C_FORMULA,
        ).move_to(UP * 5.3)

        self.play(Write(hook_line1), run_time=0.7)
        self.play(Write(hook_line2), run_time=0.7)
        self.wait(0.3)

        # ── 主三角形 ──
        triangle = self.create_main_triangle()
        right_mark = self.create_right_angle_mark(self.C, self.A, self.B)

        self.play(Create(triangle), run_time=1.0)
        self.play(Create(right_mark), run_time=0.4)

        # ── 标注三边 a, b, c ──
        # a: CA边 中点下方
        mid_CA = (self.C + self.A) / 2
        label_a = Text("a", font="PingFang SC", font_size=28,
                       color=self.C_SIDE_A).move_to(mid_CA + DOWN * 0.35)

        # b: CB边 中点左方
        mid_CB = (self.C + self.B) / 2
        label_b = Text("b", font="PingFang SC", font_size=28,
                       color=self.C_SIDE_B).move_to(mid_CB + LEFT * 0.35)

        # c: AB边 中点右方偏上
        mid_AB = (self.A + self.B) / 2
        label_c = Text("c", font="PingFang SC", font_size=28,
                       color=self.C_SIDE_C).move_to(mid_AB + RIGHT * 0.4)

        self.play(
            FadeIn(label_a, shift=DOWN * 0.2),
            FadeIn(label_b, shift=LEFT * 0.2),
            FadeIn(label_c, shift=RIGHT * 0.2),
            run_time=0.7,
        )

        # 直角标注
        right_text = Text("直角", font="PingFang SC", font_size=20,
                          color=self.C_RIGHT).move_to(self.C + DOWN * 0.35 + LEFT * 0.35)
        self.play(FadeIn(right_text), run_time=0.4)
        self.wait(0.5)

        # ── 引入公式悬念 ──
        question = Text("a, b, c 之间有什么关系？",
                        font="PingFang SC", font_size=26,
                        color=self.C_HIGHLIGHT).move_to(DOWN * 3.5)
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        # ── 清理钩子 ──
        self.play(
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            FadeOut(question),
            FadeOut(right_text),
            run_time=0.5,
        )

        # 保存引用供后续场景使用
        self.main_triangle = triangle
        self.right_mark = right_mark
        self.label_a = label_a
        self.label_b = label_b
        self.label_c = label_c

    # ============================================================
    # Scene 2: 构造三个正方形
    # ============================================================

    def scene_2_squares(self):
        """构造三个正方形，可视化 a², b², c²"""

        # ── 标题 ──
        title = Text("勾股定理", font="PingFang SC", font_size=38,
                     color=self.C_FORMULA).move_to(UP * 5.8)
        subtitle = Text("在三条边上分别画正方形",
                        font="PingFang SC", font_size=24,
                        color=GRAY_A).move_to(UP * 5.1)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(subtitle), run_time=0.4)

        # ── 正方形 a² ──
        hint_a = Text("以直角边 a 为边，向外作正方形",
                      font="PingFang SC", font_size=22,
                      color=self.C_SIDE_A).move_to(DOWN * 4.8)
        self.play(FadeIn(hint_a), run_time=0.4)

        self.sq_a = self.create_square(self.sq_a_pts, self.C_SIDE_A)
        self.play(Create(self.sq_a), run_time=1.0)

        # a² 标注
        center_sq_a = self.get_square_center(self.sq_a_pts)
        label_a2 = MathTex(r"a^2", font_size=30,
                           color=self.C_SIDE_A).move_to(center_sq_a)
        self.play(Write(label_a2), run_time=0.5)
        self.play(FadeOut(hint_a), run_time=0.3)

        # ── 正方形 b² ──
        hint_b = Text("以直角边 b 为边，向外作正方形",
                      font="PingFang SC", font_size=22,
                      color=self.C_SIDE_B).move_to(DOWN * 4.8)
        self.play(FadeIn(hint_b), run_time=0.4)

        self.sq_b = self.create_square(self.sq_b_pts, self.C_SIDE_B)
        self.play(Create(self.sq_b), run_time=1.0)

        # b² 标注
        center_sq_b = self.get_square_center(self.sq_b_pts)
        label_b2 = MathTex(r"b^2", font_size=30,
                           color=self.C_SIDE_B).move_to(center_sq_b)
        self.play(Write(label_b2), run_time=0.5)
        self.play(FadeOut(hint_b), run_time=0.3)

        # ── 正方形 c² ──
        hint_c = Text("以斜边 c 为边，向外作正方形",
                      font="PingFang SC", font_size=22,
                      color=self.C_SIDE_C).move_to(DOWN * 4.8)
        self.play(FadeIn(hint_c), run_time=0.4)

        self.sq_c = self.create_square(self.sq_c_pts, self.C_SIDE_C)
        self.play(Create(self.sq_c), run_time=1.2)

        # c² 标注
        center_sq_c = self.get_square_center(self.sq_c_pts)
        label_c2 = MathTex(r"c^2", font_size=30,
                           color=self.C_SIDE_C).move_to(center_sq_c)
        self.play(Write(label_c2), run_time=0.5)
        self.play(FadeOut(hint_c), run_time=0.3)

        # ── 三个正方形同时高亮 ──
        self.play(
            self.sq_a.animate.set_fill(self.C_SIDE_A, opacity=0.6),
            self.sq_b.animate.set_fill(self.C_SIDE_B, opacity=0.6),
            self.sq_c.animate.set_fill(self.C_SIDE_C, opacity=0.6),
            run_time=0.6,
        )
        self.play(
            self.sq_a.animate.set_fill(self.C_SIDE_A, opacity=0.3),
            self.sq_b.animate.set_fill(self.C_SIDE_B, opacity=0.3),
            self.sq_c.animate.set_fill(self.C_SIDE_C, opacity=0.3),
            run_time=0.6,
        )

        key_question = Text("三个正方形的面积有什么关系？",
                            font="PingFang SC", font_size=26,
                            color=self.C_HIGHLIGHT).move_to(DOWN * 4.5)
        self.play(FadeIn(key_question, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(key_question),
            run_time=0.5,
        )

        # 保存标注引用
        self.label_a2 = label_a2
        self.label_b2 = label_b2
        self.label_c2 = label_c2

    # ============================================================
    # Scene 3: 揭示定理
    # ============================================================

    def scene_3_reveal_theorem(self):
        """揭示 a² + b² = c²"""

        # ── 面积数值展示 (以3:4:5为例) ──
        title = Text("面积关系", font="PingFang SC", font_size=36,
                     color=self.C_FORMULA).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        # 面积数字
        area_a = Text("面积 = 9", font="PingFang SC", font_size=22,
                      color=self.C_SIDE_A)
        area_b = Text("面积 = 16", font="PingFang SC", font_size=22,
                      color=self.C_SIDE_B)
        area_c = Text("面积 = 25", font="PingFang SC", font_size=22,
                      color=self.C_SIDE_C)

        # 放在对应正方形旁边
        center_sq_a = self.get_square_center(self.sq_a_pts)
        center_sq_b = self.get_square_center(self.sq_b_pts)
        center_sq_c = self.get_square_center(self.sq_c_pts)

        area_a.next_to(self.label_a2, DOWN, buff=0.15)
        area_b.next_to(self.label_b2, DOWN, buff=0.15)
        area_c.next_to(self.label_c2, DOWN, buff=0.15)

        self.play(FadeIn(area_a), run_time=0.6)
        self.play(FadeIn(area_b), run_time=0.6)
        self.play(FadeIn(area_c), run_time=0.6)
        self.wait(0.5)

        # ── 核心等式 ──
        eq_nums = MathTex(r"9 + 16 = 25",
                          font_size=40, color=WHITE).move_to(DOWN * 3.0)
        self.play(Write(eq_nums), run_time=1.0)
        self.wait(0.5)

        # ── 升华为通用公式 ──
        formula = MathTex(
            r"a^2 + b^2 = c^2",
            font_size=52,
        )
        # 给公式各部分着色
        formula.set_color_by_tex("a", self.C_SIDE_A)
        formula.set_color_by_tex("b", self.C_SIDE_B)
        formula.set_color_by_tex("c", self.C_SIDE_C)
        formula.move_to(DOWN * 4.2)

        self.play(
            TransformMatchingTex(eq_nums, formula),
            run_time=1.0,
        )
        self.wait(0.5)

        # 公式高亮框
        formula_box = SurroundingRectangle(
            formula, color=self.C_FORMULA, corner_radius=0.15,
            buff=0.15, stroke_width=3,
        )
        self.play(Create(formula_box), run_time=0.5)

        # 公式名称
        theorem_name = Text("勾股定理", font="PingFang SC",
                            font_size=28, color=self.C_FORMULA).next_to(formula_box, DOWN, buff=0.2)
        self.play(FadeIn(theorem_name, shift=UP * 0.2), run_time=0.5)

        # 停留让学生记忆
        self.play(
            Flash(formula, color=self.C_FORMULA, flash_radius=1.2),
            run_time=0.8,
        )
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(area_a), FadeOut(area_b), FadeOut(area_c),
            run_time=0.4,
        )

        # 保存引用
        self.main_formula = formula
        self.formula_box = formula_box
        self.theorem_name = theorem_name

    # ============================================================
    # Scene 4: 数值验证
    # ============================================================

    def scene_4_numeric_verify(self):
        """用 3-4-5 数值验证定理"""

        # 淡出正方形和之前的标注
        self.play(
            FadeOut(self.sq_a), FadeOut(self.label_a2),
            FadeOut(self.sq_b), FadeOut(self.label_b2),
            FadeOut(self.sq_c), FadeOut(self.label_c2),
            FadeOut(self.main_formula), FadeOut(self.formula_box),
            FadeOut(self.theorem_name),
            run_time=0.6,
        )

        # ── 标题 ──
        title = Text("数值验证", font="PingFang SC", font_size=36,
                     color=self.C_FORMULA).move_to(UP * 5.8)
        subtitle = Text("经典勾股数: 3, 4, 5",
                        font="PingFang SC", font_size=26,
                        color=GRAY_A).move_to(UP * 5.1)
        self.play(Write(title), FadeIn(subtitle), run_time=0.6)

        # 在三角形边上标注具体数值
        mid_CA = (self.C + self.A) / 2
        mid_CB = (self.C + self.B) / 2
        mid_AB = (self.A + self.B) / 2

        val_a = Text("a = 3", font="PingFang SC", font_size=26,
                     color=self.C_SIDE_A).move_to(mid_CA + DOWN * 0.4)
        val_b = Text("b = 4", font="PingFang SC", font_size=26,
                     color=self.C_SIDE_B).move_to(mid_CB + LEFT * 0.5)
        val_c = Text("c = ?", font="PingFang SC", font_size=26,
                     color=self.C_SIDE_C).move_to(mid_AB + RIGHT * 0.5)

        # 更新边标注
        self.play(
            ReplacementTransform(self.label_a, val_a),
            ReplacementTransform(self.label_b, val_b),
            ReplacementTransform(self.label_c, val_c),
            run_time=0.7,
        )

        # ── 逐步计算 ──
        steps = VGroup()

        step1 = MathTex(r"a^2 = 3^2 = 9", font_size=34)
        step1[0][0:2].set_color(self.C_SIDE_A)
        step1.move_to(DOWN * 2.5)

        step2 = MathTex(r"b^2 = 4^2 = 16", font_size=34)
        step2[0][0:2].set_color(self.C_SIDE_B)
        step2.move_to(DOWN * 3.3)

        step3 = MathTex(r"a^2 + b^2 = 9 + 16 = 25", font_size=32)
        step3[0][0:2].set_color(self.C_SIDE_A)
        step3[0][3:5].set_color(self.C_SIDE_B)
        step3.move_to(DOWN * 4.2)

        step4 = MathTex(r"c = \sqrt{25} = 5", font_size=34)
        step4[0][0].set_color(self.C_SIDE_C)
        step4.move_to(DOWN * 5.1)

        self.play(Write(step1), run_time=0.7)
        self.wait(0.3)
        self.play(Write(step2), run_time=0.7)
        self.wait(0.3)
        self.play(Write(step3), run_time=0.9)
        self.wait(0.3)
        self.play(Write(step4), run_time=0.7)
        self.wait(0.3)

        # 更新 c 标注
        val_c_ans = Text("c = 5", font="PingFang SC", font_size=26,
                         color=self.C_SIDE_C).move_to(mid_AB + RIGHT * 0.5)
        self.play(ReplacementTransform(val_c, val_c_ans), run_time=0.5)

        # 验证符号
        checkmark = Text("✓  验证成立！", font="PingFang SC",
                         font_size=32, color="#4CAF50").move_to(DOWN * 6.0)
        self.play(FadeIn(checkmark, scale=1.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(val_a), FadeOut(val_b), FadeOut(val_c_ans),
            FadeOut(step1), FadeOut(step2), FadeOut(step3), FadeOut(step4),
            FadeOut(checkmark),
            run_time=0.6,
        )

    # ============================================================
    # Scene 5: 公式变形
    # ============================================================

    def scene_5_formula_variants(self):
        """展示公式的三种变形"""

        # ── 标题 ──
        title = Text("公式变形", font="PingFang SC", font_size=36,
                     color=self.C_FORMULA).move_to(UP * 5.8)
        subtitle = Text("已知两边，求第三边",
                        font="PingFang SC", font_size=26,
                        color=GRAY_A).move_to(UP * 5.1)
        self.play(Write(title), FadeIn(subtitle), run_time=0.6)

        # 基础公式
        base = MathTex(r"a^2 + b^2 = c^2",
                       font_size=46, color=WHITE).move_to(UP * 3.8)
        self.play(Write(base), run_time=0.8)
        self.wait(0.4)

        # 变形1: 求斜边c
        arrow1 = MathTex(r"\Downarrow", font_size=36, color=GRAY_A).move_to(UP * 2.9)
        label1 = Text("已知 a, b 求斜边 c",
                      font="PingFang SC", font_size=22,
                      color=self.C_SIDE_C).move_to(UP * 2.1)
        var1 = MathTex(r"c = \sqrt{a^2 + b^2}",
                       font_size=40, color=self.C_SIDE_C).move_to(UP * 1.3)

        self.play(FadeIn(arrow1), FadeIn(label1), run_time=0.4)
        self.play(Write(var1), run_time=0.8)
        self.wait(0.4)

        # 变形2: 求直角边a
        arrow2 = MathTex(r"\Downarrow", font_size=36, color=GRAY_A).move_to(UP * 0.4)
        label2 = Text("已知 b, c 求直角边 a",
                      font="PingFang SC", font_size=22,
                      color=self.C_SIDE_A).move_to(DOWN * 0.4)
        var2 = MathTex(r"a = \sqrt{c^2 - b^2}",
                       font_size=40, color=self.C_SIDE_A).move_to(DOWN * 1.2)

        self.play(FadeIn(arrow2), FadeIn(label2), run_time=0.4)
        self.play(Write(var2), run_time=0.8)
        self.wait(0.4)

        # 变形3: 求直角边b
        arrow3 = MathTex(r"\Downarrow", font_size=36, color=GRAY_A).move_to(DOWN * 2.1)
        label3 = Text("已知 a, c 求直角边 b",
                      font="PingFang SC", font_size=22,
                      color=self.C_SIDE_B).move_to(DOWN * 2.9)
        var3 = MathTex(r"b = \sqrt{c^2 - a^2}",
                       font_size=40, color=self.C_SIDE_B).move_to(DOWN * 3.7)

        self.play(FadeIn(arrow3), FadeIn(label3), run_time=0.4)
        self.play(Write(var3), run_time=0.8)
        self.wait(2.0)

        # ── 核心记忆点 ──
        memory_tip = Text("记住: 直角边² + 直角边² = 斜边²",
                          font="PingFang SC", font_size=24,
                          color=self.C_FORMULA).move_to(DOWN * 5.0)
        self.play(FadeIn(memory_tip, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(base),
            FadeOut(arrow1), FadeOut(label1), FadeOut(var1),
            FadeOut(arrow2), FadeOut(label2), FadeOut(var2),
            FadeOut(arrow3), FadeOut(label3), FadeOut(var3),
            FadeOut(memory_tip),
            FadeOut(self.main_triangle), FadeOut(self.right_mark),
            run_time=0.7,
        )

    # ============================================================
    # Scene 6: 片尾
    # ============================================================

    def scene_6_outro(self):
        """片尾: 核心公式强化 + 作者信息"""

        # ── 核心公式大字展示 ──
        big_formula = MathTex(
            r"a^2 + b^2 = c^2",
            font_size=72,
        )
        big_formula.set_color(self.C_FORMULA)
        big_formula.move_to(UP * 2.5)

        self.play(Write(big_formula), run_time=1.0)

        # 装饰线
        deco_line_l = Line(LEFT * 3.5, LEFT * 0.5,
                           color=self.C_FORMULA, stroke_width=2).move_to(UP * 1.5)
        deco_line_r = Line(RIGHT * 0.5, RIGHT * 3.5,
                           color=self.C_FORMULA, stroke_width=2).move_to(UP * 1.5)

        text_core = Text("勾股定理", font="PingFang SC",
                         font_size=34, color=WHITE).move_to(UP * 1.5)
        self.play(
            Create(deco_line_l), Create(deco_line_r),
            FadeIn(text_core),
            run_time=0.7,
        )

        # 三个小方块装饰
        deco_sq_a = Square(side_length=0.5, fill_color=self.C_SIDE_A,
                           fill_opacity=0.8, stroke_width=0).move_to(LEFT * 2.0 + UP * 0.3)
        deco_sq_b = Square(side_length=0.5, fill_color=self.C_SIDE_B,
                           fill_opacity=0.8, stroke_width=0).move_to(ORIGIN + UP * 0.3)
        deco_sq_c = Square(side_length=0.5, fill_color=self.C_SIDE_C,
                           fill_opacity=0.8, stroke_width=0).move_to(RIGHT * 2.0 + UP * 0.3)

        deco_a = MathTex(r"a^2", font_size=22,
                         color=WHITE).move_to(deco_sq_a.get_center())
        deco_b = MathTex(r"b^2", font_size=22,
                         color=WHITE).move_to(deco_sq_b.get_center())
        deco_c = MathTex(r"c^2", font_size=22,
                         color=WHITE).move_to(deco_sq_c.get_center())

        deco_plus = MathTex(r"+", font_size=30, color=WHITE).move_to(LEFT * 1.0 + UP * 0.3)
        deco_eq = MathTex(r"=", font_size=30, color=WHITE).move_to(RIGHT * 1.0 + UP * 0.3)

        self.play(
            FadeIn(deco_sq_a), FadeIn(deco_sq_b), FadeIn(deco_sq_c),
            FadeIn(deco_a), FadeIn(deco_b), FadeIn(deco_c),
            FadeIn(deco_plus), FadeIn(deco_eq),
            run_time=0.7,
        )

        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=self.C_HIGHLIGHT,
        ).move_to(DOWN * 1.2)
        self.play(FadeIn(follow_text, scale=1.05), run_time=0.6)

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=32,
            color=WHITE,
        ).move_to(DOWN * 2.2)
        author_id_big = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=26,
            color=GRAY_B,
        ).move_to(DOWN * 3.0)

        self.play(
            Transform(self.author_info, author_big),
            run_time=0.6,
        )
        self.play(FadeIn(author_id_big, shift=UP * 0.2), run_time=0.5)

        # 旋转小方块动画
        self.play(
            Rotate(deco_sq_a, angle=PI / 2),
            Rotate(deco_sq_b, angle=PI / 2),
            Rotate(deco_sq_c, angle=PI / 2),
            run_time=1.0,
        )
        self.wait(0.8)

        # 全部淡出
        self.play(
            FadeOut(big_formula),
            FadeOut(deco_line_l), FadeOut(deco_line_r), FadeOut(text_core),
            FadeOut(deco_sq_a), FadeOut(deco_sq_b), FadeOut(deco_sq_c),
            FadeOut(deco_a), FadeOut(deco_b), FadeOut(deco_c),
            FadeOut(deco_plus), FadeOut(deco_eq),
            FadeOut(follow_text),
            FadeOut(self.author_info),
            FadeOut(author_id_big),
            run_time=1.0,
        )


# ============================================================
# 渲染命令
# ============================================================
# 快速预览:  manim -pql pythagorean_theorem.py PythagoreanTheorem
# 高质量:    manim -qh  pythagorean_theorem.py PythagoreanTheorem
# 4K输出:    manim -qk  pythagorean_theorem.py PythagoreanTheorem