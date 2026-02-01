"""
欧拉线 (Euler Line) - Manim 教学动画
Mathematical Animation of the Euler Line Theorem

定理: 三角形的外心O、重心G、垂心H、九点圆圆心N四点共线。
     且 OG:GH = 1:2, N是OH的中点。

作者: 上海初高中数学直通车 @emptyandcalm
目标: TikTok竖屏短视频 (1080×1920)
时长: 90-110秒
"""

from manim import *
import numpy as np

# ===== 全局配置 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class GeometryCalculator:
    """几何计算工具类 - 确保所有计算精确"""
    
    @staticmethod
    def circumcenter(A, B, C):
        """计算三角形外心"""
        ax, ay = A[0], A[1]
        bx, by = B[0], B[1]
        cx, cy = C[0], C[1]
        
        D = 2 * (ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
        
        if abs(D) < 1e-10:
            return (A + B + C) / 3  # 退化情况
        
        ux = ((ax**2+ay**2)*(by-cy) + (bx**2+by**2)*(cy-ay) + (cx**2+cy**2)*(ay-by)) / D
        uy = ((ax**2+ay**2)*(cx-bx) + (bx**2+by**2)*(ax-cx) + (cx**2+cy**2)*(bx-ax)) / D
        
        return np.array([ux, uy, 0])
    
    @staticmethod
    def centroid(A, B, C):
        """计算重心"""
        return (A + B + C) / 3
    
    @staticmethod
    def orthocenter(A, B, C, O=None):
        """
        计算垂心
        使用欧拉公式: H = A + B + C - 2O
        """
        if O is None:
            O = GeometryCalculator.circumcenter(A, B, C)
        return A + B + C - 2 * O
    
    @staticmethod
    def nine_point_center(O, H):
        """计算九点圆圆心 (OH中点)"""
        return (O + H) / 2
    
    @staticmethod
    def foot_of_perpendicular(point, line_start, line_end):
        """计算点到直线的垂足"""
        line_vec = line_end - line_start
        point_vec = point - line_start
        t = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)
        return line_start + t * line_vec
    
    @staticmethod
    def triangle_area(P1, P2, P3):
        """计算三角形面积 (用于验证共线性)"""
        return 0.5 * abs(
            P1[0]*(P2[1]-P3[1]) + P2[0]*(P3[1]-P1[1]) + P3[0]*(P1[1]-P2[1])
        )
    
    @staticmethod
    def perpendicular_bisector_points(P1, P2, extension=2.0):
        """计算垂直平分线的两个端点"""
        mid = (P1 + P2) / 2
        direction = P2 - P1
        perp = np.array([-direction[1], direction[0], 0])
        perp_normalized = perp / np.linalg.norm(perp)
        
        return mid - extension * perp_normalized, mid + extension * perp_normalized


class EulerLineScene(Scene):
    """欧拉线主场景"""
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 定义颜色方案
        self.COLOR_TRIANGLE = WHITE
        self.COLOR_CIRCUMCENTER = "#e74c3c"  # 外心O (红色)
        self.COLOR_CENTROID = "#2ecc71"  # 重心G (绿色)
        self.COLOR_ORTHOCENTER = "#f39c12"  # 垂心H (橙色)
        self.COLOR_NINE_POINT_CENTER = "#9b59b6"  # 九点圆圆心N (紫色)
        self.COLOR_EULER_LINE = "#3498db"  # 欧拉线 (蓝色)
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化所有几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_theorem_statement()
        self.scene_3_construct_circumcenter()
        self.scene_4_construct_centroid()
        self.scene_5_construct_orthocenter()
        self.scene_6_euler_line_reveal()
        self.scene_7_nine_point_center()
        self.scene_10_outro()
    
    def setup_geometry(self):
        """统一初始化所有几何元素"""
        print("\n===== 初始化几何数据 =====")
        
        # 基准参数
        self.SCALE = 1.3
        self.OFFSET = UP * 1.5
        
        # 三角形顶点 (使用锐角不等边三角形)
        self.A = np.array([-2.3, -1.0, 0]) * self.SCALE + self.OFFSET
        self.B = np.array([2.5, -0.8, 0]) * self.SCALE + self.OFFSET
        self.C = np.array([0.2, 2.2, 0]) * self.SCALE + self.OFFSET
        
        # 计算四个中心
        self.O = GeometryCalculator.circumcenter(self.A, self.B, self.C)
        self.G = GeometryCalculator.centroid(self.A, self.B, self.C)
        self.H = GeometryCalculator.orthocenter(self.A, self.B, self.C, self.O)
        self.N = GeometryCalculator.nine_point_center(self.O, self.H)
        
        # 外接圆半径
        self.R = np.linalg.norm(self.A - self.O)
        
        # 九点圆半径
        self.R_nine = self.R / 2
        
        # 验证几何关系
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        eps = 1e-6
        
        print("验证几何关系...")
        
        # 1. 验证外心
        r_A = np.linalg.norm(self.A - self.O)
        r_B = np.linalg.norm(self.B - self.O)
        r_C = np.linalg.norm(self.C - self.O)
        
        if abs(r_A - self.R) < eps and abs(r_B - self.R) < eps and abs(r_C - self.R) < eps:
            print(f"✓ 外心正确: R = {self.R:.4f}")
        else:
            print(f"WARNING: 外心错误! rA={r_A:.6f}, rB={r_B:.6f}, rC={r_C:.6f}")
        
        # 2. 验证重心
        G_check = (self.A + self.B + self.C) / 3
        if np.linalg.norm(self.G - G_check) < eps:
            print("✓ 重心正确: G = (A+B+C)/3")
        else:
            print("WARNING: 重心计算错误!")
        
        # 3. 验证垂心 (使用欧拉公式)
        H_check = self.A + self.B + self.C - 2 * self.O
        if np.linalg.norm(self.H - H_check) < eps:
            print("✓ 垂心正确: H = A+B+C-2O")
        else:
            print("WARNING: 垂心计算错误!")
        
        # 4. 验证共线性 (核心定理!)
        area_OGH = GeometryCalculator.triangle_area(self.O, self.G, self.H)
        if area_OGH < 1e-8:
            print("✓✓✓ O, G, H 共线! 欧拉线验证成功!")
        else:
            print(f"WARNING: O, G, H 不共线! 面积 = {area_OGH:.10f}")
        
        # 5. 验证比例关系 OG:GH = 1:2
        OG = np.linalg.norm(self.G - self.O)
        GH = np.linalg.norm(self.H - self.G)
        ratio = OG / GH if GH > eps else 0
        
        if abs(ratio - 0.5) < eps:
            print(f"✓ 比例关系正确: OG:GH = 1:2 (实际={ratio:.4f})")
        else:
            print(f"WARNING: 比例错误! OG/GH = {ratio:.4f}")
        
        # 6. 验证九点圆圆心
        N_check = (self.O + self.H) / 2
        if np.linalg.norm(self.N - N_check) < eps:
            print("✓ 九点圆圆心正确: N = (O+H)/2")
        else:
            print("WARNING: 九点圆圆心错误!")
        
        # 7. 验证N在欧拉线上
        area_OGN = GeometryCalculator.triangle_area(self.O, self.G, self.N)
        if area_OGN < 1e-8:
            print("✓ N 在欧拉线上")
        else:
            print(f"WARNING: N 不在欧拉线上! 面积 = {area_OGN:.10f}")
        
        print("===== 几何验证完成 =====\n")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_B
        ).move_to(UP * 7.3)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook_text = Text(
            "四个中心竟然共线?",
            font="Noto Sans CJK SC",
            font_size=46,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(hook_text, run_time=0.9))
        
        # 三角形
        self.triangle = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_TRIANGLE,
            stroke_width=2.5
        )
        
        self.play(Create(self.triangle), run_time=0.9)
        
        # 四个中心依次闪烁
        centers = [
            (self.O, self.COLOR_CIRCUMCENTER, "O"),
            (self.G, self.COLOR_CENTROID, "G"),
            (self.H, self.COLOR_ORTHOCENTER, "H"),
            (self.N, self.COLOR_NINE_POINT_CENTER, "N")
        ]
        
        center_dots = []
        for pos, color, label in centers:
            dot = Dot(pos, color=color, radius=0.09)
            self.play(FadeIn(dot, scale=0.5), run_time=0.4)
            self.play(Flash(dot, color=color, flash_radius=0.28), run_time=0.35)
            center_dots.append(dot)
        
        # 欧拉线戏剧性出现
        extension = 2.5
        OH_vec = self.H - self.O
        OH_normalized = OH_vec / np.linalg.norm(OH_vec)
        
        euler_line_preview = Line(
            self.O - extension * OH_normalized,
            self.H + extension * OH_normalized,
            color=self.COLOR_EULER_LINE,
            stroke_width=3.5
        )
        
        self.play(Create(euler_line_preview), run_time=1.0)
        self.play(Flash(euler_line_preview, color=self.COLOR_EULER_LINE, flash_radius=0.6), run_time=0.5)
        
        # 惊叹文字
        surprise = Text(
            "这就是欧拉线!",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 5.5)
        
        self.play(Write(surprise), run_time=0.7)
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(surprise),
            *[FadeOut(dot) for dot in center_dots],
            FadeOut(euler_line_preview),
            run_time=0.6
        )
    
    def scene_2_theorem_statement(self):
        """场景2: 定理陈述"""
        # 标题
        title = Text(
            "欧拉线定理",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_EULER_LINE,
            weight=BOLD
        ).move_to(UP * 6.2)
        
        subtitle = Text(
            "Euler Line Theorem (1765)",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.6)
        
        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 四个中心说明
        centers_desc = VGroup(
            Text("• 外心O: 外接圆圆心", font="Noto Sans CJK SC", font_size=20, color=WHITE),
            Text("• 重心G: 中线交点", font="Noto Sans CJK SC", font_size=20, color=WHITE),
            Text("• 垂心H: 高线交点", font="Noto Sans CJK SC", font_size=20, color=WHITE),
            Text("• 九点圆圆心N", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(UP * 4)
        
        for desc in centers_desc:
            self.play(FadeIn(desc, shift=UP * 0.2), run_time=0.5)
            self.wait(0.2)
        
        # 核心结论
        conclusion = Text(
            "O, G, H, N 四点共线!",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 2.3)
        
        self.play(Write(conclusion), run_time=0.9)
        
        # 比例关系
        ratio = Text(
            "OG : GH = 1 : 2",
            font_size=28,
            color=WHITE
        ).move_to(UP * 1.5)
        
        midpoint_text = Text(
            "N 是 OH 的中点",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 0.8)
        
        self.play(FadeIn(ratio), run_time=0.6)
        self.play(FadeIn(midpoint_text), run_time=0.6)
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(centers_desc),
            FadeOut(conclusion),
            FadeOut(ratio),
            FadeOut(midpoint_text),
            run_time=0.7
        )
    
    def scene_3_construct_circumcenter(self):
        """场景3: 构造外心O"""
        # 步骤标题
        step_title = Text(
            "步骤1: 作外心O",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        explanation = Text(
            "三边垂直平分线的交点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.3)
        
        self.play(FadeIn(step_title), FadeIn(explanation), run_time=0.6)
        
        # AB的垂直平分线
        AB_mid = (self.A + self.B) / 2
        perp_AB_start, perp_AB_end = GeometryCalculator.perpendicular_bisector_points(self.A, self.B, 2.5)
        
        self.play(Indicate(Line(self.A, self.B), color=self.COLOR_HIGHLIGHT), run_time=0.6)
        
        M1_dot = Dot(AB_mid, color=self.COLOR_AUXILIARY, radius=0.05)
        self.play(FadeIn(M1_dot), run_time=0.4)
        
        perp_bisector_1 = DashedLine(
            perp_AB_start, perp_AB_end,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        self.play(Create(perp_bisector_1), run_time=0.8)
        
        # BC的垂直平分线
        BC_mid = (self.B + self.C) / 2
        perp_BC_start, perp_BC_end = GeometryCalculator.perpendicular_bisector_points(self.B, self.C, 2.5)
        
        self.play(Indicate(Line(self.B, self.C), color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        M2_dot = Dot(BC_mid, color=self.COLOR_AUXILIARY, radius=0.05)
        self.play(FadeIn(M2_dot), run_time=0.4)
        
        perp_bisector_2 = DashedLine(
            perp_BC_start, perp_BC_end,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        self.play(Create(perp_bisector_2), run_time=0.8)
        
        # 外心O出现
        O_dot = Dot(self.O, color=self.COLOR_CIRCUMCENTER, radius=0.11)
        O_label = VGroup(
            Text("O", font_size=26, color=self.COLOR_CIRCUMCENTER),
            Text("外心", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_CIRCUMCENTER)
        ).arrange(DOWN, buff=0.05)
        O_label.next_to(O_dot, RIGHT, buff=0.15)
        
        self.play(FadeIn(O_dot, scale=0.5), run_time=0.5)
        self.play(Flash(O_dot, color=self.COLOR_CIRCUMCENTER, flash_radius=0.3), run_time=0.4)
        self.play(Write(O_label), run_time=0.5)
        
        # 外接圆
        circumcircle = Circle(
            radius=self.R,
            color=self.COLOR_CIRCUMCENTER,
            stroke_width=1.5,
            stroke_opacity=0.4
        ).move_to(self.O)
        
        self.play(Create(circumcircle), run_time=1.2)
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(explanation),
            FadeOut(perp_bisector_1),
            FadeOut(perp_bisector_2),
            FadeOut(M1_dot),
            FadeOut(M2_dot),
            circumcircle.animate.set_stroke(opacity=0.15),  # 淡化为背景
            run_time=0.5
        )
        
        # 保留
        self.O_dot_ref = O_dot
        self.O_label_ref = O_label
        self.circumcircle_ref = circumcircle
    
    def scene_4_construct_centroid(self):
        """场景4: 构造重心G"""
        step_title = Text(
            "步骤2: 作重心G",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        explanation = Text(
            "三条中线的交点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.3)
        
        self.play(FadeIn(step_title), FadeIn(explanation), run_time=0.5)
        
        # 中线 AD (A到BC中点)
        D = (self.B + self.C) / 2
        D_dot = Dot(D, color=self.COLOR_AUXILIARY, radius=0.06)
        
        self.play(FadeIn(D_dot), run_time=0.3)
        
        median_AD = Line(self.A, D, color=self.COLOR_AUXILIARY, stroke_width=2)
        self.play(Create(median_AD), run_time=0.7)
        
        # 中线 BE (B到CA中点)
        E = (self.C + self.A) / 2
        E_dot = Dot(E, color=self.COLOR_AUXILIARY, radius=0.06)
        
        self.play(FadeIn(E_dot), run_time=0.3)
        
        median_BE = Line(self.B, E, color=self.COLOR_AUXILIARY, stroke_width=2)
        self.play(Create(median_BE), run_time=0.7)
        
        # 重心G出现
        G_dot = Dot(self.G, color=self.COLOR_CENTROID, radius=0.11)
        G_label = VGroup(
            Text("G", font_size=26, color=self.COLOR_CENTROID),
            Text("重心", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_CENTROID)
        ).arrange(DOWN, buff=0.05)
        G_label.next_to(G_dot, LEFT, buff=0.15)
        
        self.play(FadeIn(G_dot, scale=0.5), run_time=0.5)
        self.play(Flash(G_dot, color=self.COLOR_CENTROID, flash_radius=0.3), run_time=0.4)
        self.play(Write(G_label), run_time=0.5)
        
        # 2:1比例标注
        ratio_text = Text(
            "AG:GD = 2:1",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(ratio_text), run_time=0.5)
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(explanation),
            FadeOut(median_AD),
            FadeOut(median_BE),
            FadeOut(D_dot),
            FadeOut(E_dot),
            FadeOut(ratio_text),
            run_time=0.4
        )
        
        # 保留
        self.G_dot_ref = G_dot
        self.G_label_ref = G_label
    
    def scene_5_construct_orthocenter(self):
        """场景5: 构造垂心H"""
        step_title = Text(
            "步骤3: 作垂心H",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        explanation = Text(
            "三条高线的交点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.3)
        
        self.play(FadeIn(step_title), FadeIn(explanation), run_time=0.5)
        
        # 高线1: A到BC
        foot_BC = GeometryCalculator.foot_of_perpendicular(self.A, self.B, self.C)
        
        self.play(Indicate(Line(self.B, self.C), color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        altitude_A = Line(self.A, foot_BC, color=self.COLOR_AUXILIARY, stroke_width=2)
        self.play(Create(altitude_A), run_time=0.7)
        
        foot_BC_dot = Dot(foot_BC, color=self.COLOR_AUXILIARY, radius=0.05)
        self.play(FadeIn(foot_BC_dot), run_time=0.3)
        
        # 直角标记
        right_angle_1 = self.create_right_angle_mark(foot_BC, self.A, self.B, size=0.15)
        self.play(FadeIn(right_angle_1), run_time=0.3)
        
        # 高线2: B到CA
        foot_CA = GeometryCalculator.foot_of_perpendicular(self.B, self.C, self.A)
        
        self.play(Indicate(Line(self.C, self.A), color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        altitude_B = Line(self.B, foot_CA, color=self.COLOR_AUXILIARY, stroke_width=2)
        self.play(Create(altitude_B), run_time=0.7)
        
        foot_CA_dot = Dot(foot_CA, color=self.COLOR_AUXILIARY, radius=0.05)
        self.play(FadeIn(foot_CA_dot), run_time=0.3)
        
        right_angle_2 = self.create_right_angle_mark(foot_CA, self.B, self.C, size=0.15)
        self.play(FadeIn(right_angle_2), run_time=0.3)
        
        # 垂心H出现
        H_dot = Dot(self.H, color=self.COLOR_ORTHOCENTER, radius=0.11)
        H_label = VGroup(
            Text("H", font_size=26, color=self.COLOR_ORTHOCENTER),
            Text("垂心", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_ORTHOCENTER)
        ).arrange(DOWN, buff=0.05)
        H_label.next_to(H_dot, UP + RIGHT, buff=0.12)
        
        self.play(FadeIn(H_dot, scale=0.5), run_time=0.5)
        self.play(Flash(H_dot, color=self.COLOR_ORTHOCENTER, flash_radius=0.3), run_time=0.4)
        self.play(Write(H_label), run_time=0.5)
        
        self.wait(0.6)
        
        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(explanation),
            FadeOut(altitude_A),
            FadeOut(altitude_B),
            FadeOut(foot_BC_dot),
            FadeOut(foot_CA_dot),
            FadeOut(right_angle_1),
            FadeOut(right_angle_2),
            run_time=0.4
        )
        
        # 保留
        self.H_dot_ref = H_dot
        self.H_label_ref = H_label
    
    def scene_6_euler_line_reveal(self):
        """场景6: 欧拉线的显现"""
        # 提问
        question = Text(
            "这三个点有什么关系?",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(FadeIn(question), run_time=0.6)
        
        # O, G, H高亮
        self.play(
            AnimationGroup(
                Indicate(self.O_dot_ref, color=self.COLOR_HIGHLIGHT),
                Indicate(self.G_dot_ref, color=self.COLOR_HIGHLIGHT),
                Indicate(self.H_dot_ref, color=self.COLOR_HIGHLIGHT),
                lag_ratio=0.2
            ),
            run_time=1.2
        )
        
        # 连接O-G虚线
        OG_dashed = DashedLine(self.O, self.G, color=GRAY_A, dash_length=0.1, stroke_width=2)
        self.play(Create(OG_dashed), run_time=0.7)
        
        # 连接G-H虚线
        GH_dashed = DashedLine(self.G, self.H, color=GRAY_A, dash_length=0.1, stroke_width=2)
        self.play(Create(GH_dashed), run_time=0.7)
        
        # 惊叹
        surprise = Text(
            "它们共线!",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Transform(question, surprise), run_time=0.5)
        
        # 欧拉线戏剧性出现
        extension = 2.5
        OH_vec = self.H - self.O
        OH_normalized = OH_vec / np.linalg.norm(OH_vec)
        
        euler_line = Line(
            self.O - extension * OH_normalized,
            self.H + extension * OH_normalized,
            color=self.COLOR_EULER_LINE,
            stroke_width=4
        )
        
        self.play(
            Transform(VGroup(OG_dashed, GH_dashed), euler_line),
            run_time=1.0
        )
        
        self.remove(OG_dashed, GH_dashed)
        self.add(euler_line)
        
        # 发光效果
        self.play(
            Flash(euler_line, color=self.COLOR_EULER_LINE, flash_radius=0.8),
            run_time=0.6
        )
        
        # 标签
        euler_label = Text(
            "欧拉线",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_EULER_LINE,
            weight=BOLD
        )
        
        # 标签位置 (在线的一侧)
        label_pos = self.G + UP * 0.6 + LEFT * 0.5
        euler_label.move_to(label_pos)
        
        self.play(Write(euler_label), run_time=0.7)
        
        # 比例关系标注
        ratio_text = Text(
            "OG : GH = 1 : 2",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(ratio_text), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(question),
            FadeOut(ratio_text),
            run_time=0.5
        )
        
        # 保留
        self.euler_line_ref = euler_line
        self.euler_label_ref = euler_label
    
    def scene_7_nine_point_center(self):
        """场景7: 九点圆圆心N"""
        step_title = Text(
            "步骤4: 九点圆圆心N",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        explanation = Text(
            "通过9个特殊点的圆",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.3)
        
        self.play(FadeIn(step_title), FadeIn(explanation), run_time=0.6)
        
        # 九个点 (简化版: 只显示三边中点)
        nine_points = [
            (self.B + self.C) / 2,  # BC中点
            (self.C + self.A) / 2,  # CA中点
            (self.A + self.B) / 2,  # AB中点
        ]
        
        nine_dots = VGroup(*[Dot(p, color=self.COLOR_NINE_POINT_CENTER, radius=0.05) for p in nine_points])
        
        self.play(
            AnimationGroup(
                *[Flash(dot, color=self.COLOR_NINE_POINT_CENTER) for dot in nine_dots],
                lag_ratio=0.2
            ),
            run_time=1.2
        )
        self.play(FadeIn(nine_dots), run_time=0.5)
        
        # 九点圆
        nine_point_circle = Circle(
            radius=self.R_nine,
            color=self.COLOR_NINE_POINT_CENTER,
            stroke_width=1.5,
            stroke_opacity=0.4
        ).move_to(self.N)
        
        self.play(Create(nine_point_circle), run_time=1.5)
        
        # 九点圆圆心N
        N_dot = Dot(self.N, color=self.COLOR_NINE_POINT_CENTER, radius=0.11)
        N_label = VGroup(
            Text("N", font_size=26, color=self.COLOR_NINE_POINT_CENTER),
            Text("九点圆圆心", font="Noto Sans CJK SC", font_size=16, color=self.COLOR_NINE_POINT_CENTER)
        ).arrange(DOWN, buff=0.05)
        N_label.next_to(N_dot, DOWN + LEFT, buff=0.12)
        
        self.play(FadeIn(N_dot, scale=0.5), run_time=0.5)
        self.play(Flash(N_dot, color=self.COLOR_NINE_POINT_CENTER, flash_radius=0.3), run_time=0.4)
        self.play(Write(N_label), run_time=0.5)
        
        # 惊叹
        surprise = Text(
            "N也在欧拉线上!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(Write(surprise), run_time=0.7)
        
        # N在欧拉线上高亮
        self.play(
            Indicate(VGroup(N_dot, self.euler_line_ref), color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 中点性质
        midpoint_text = Text(
            "N 是 OH 的中点",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(midpoint_text), run_time=0.6)
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(explanation),
            FadeOut(nine_dots),
            FadeOut(surprise),
            FadeOut(midpoint_text),
            nine_point_circle.animate.set_stroke(opacity=0.15),
            run_time=0.6
        )
        
        # 保留
        self.N_dot_ref = N_dot
        self.N_label_ref = N_label
        self.nine_point_circle_ref = nine_point_circle
    
    def scene_10_outro(self):
        """场景10: 片尾总结与关注"""
        # 清空场景 (保留四个点和欧拉线)
        self.play(
            FadeOut(self.triangle),
            FadeOut(self.circumcircle_ref),
            FadeOut(self.nine_point_circle_ref),
            run_time=0.8
        )
        
        # 总结标题
        summary_title = Text(
            "欧拉线 - 要点总结",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_EULER_LINE,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 要点列表
        points = VGroup(
            Text("✓ 四个中心: O, G, H, N", font="Noto Sans CJK SC", font_size=24, color=WHITE),
            Text("✓ 四点共线，构成欧拉线", font="Noto Sans CJK SC", font_size=24, color=WHITE),
            Text("✓ 比例关系: OG:GH = 1:2", font="Noto Sans CJK SC", font_size=24, color=WHITE),
            Text("✓ 中点性质: N是OH的中点", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(UP * 4)
        
        for point in points:
            self.play(FadeIn(point, shift=UP * 0.2), run_time=0.6)
            self.wait(0.3)
        
        # 小图示意 (缩小版)
        mini_scale = 0.35
        mini_tri = Polygon(
            self.A * mini_scale,
            self.B * mini_scale,
            self.C * mini_scale,
            color=WHITE,
            stroke_width=1.5
        ).move_to(UP * 1)
        
        mini_O = Dot(self.O * mini_scale + UP * 1, color=self.COLOR_CIRCUMCENTER, radius=0.05)
        mini_G = Dot(self.G * mini_scale + UP * 1, color=self.COLOR_CENTROID, radius=0.05)
        mini_H = Dot(self.H * mini_scale + UP * 1, color=self.COLOR_ORTHOCENTER, radius=0.05)
        mini_N = Dot(self.N * mini_scale + UP * 1, color=self.COLOR_NINE_POINT_CENTER, radius=0.05)
        
        OH_vec = self.H - self.O
        OH_norm = OH_vec / np.linalg.norm(OH_vec)
        mini_euler = Line(
            (self.O - 1.5 * OH_norm) * mini_scale + UP * 1,
            (self.H + 1.5 * OH_norm) * mini_scale + UP * 1,
            color=self.COLOR_EULER_LINE,
            stroke_width=2
        )
        
        mini_diagram = VGroup(mini_tri, mini_O, mini_G, mini_H, mini_N, mini_euler)
        
        self.play(FadeIn(mini_diagram), run_time=0.8)
        
        # 历史卡片
        history = VGroup(
            Text("瑞士数学家", font="Noto Sans CJK SC", font_size=20, color=GRAY_A),
            Text("莱昂哈德·欧拉", font="Noto Sans CJK SC", font_size=22, color=WHITE, weight=BOLD),
            Text("Leonhard Euler", font_size=18, color=GRAY_A),
            Text("1765年首次发现并证明", font="Noto Sans CJK SC", font_size=18, color=GRAY_A)
        ).arrange(DOWN, buff=0.15).move_to(DOWN * 1.5)
        
        self.play(FadeIn(history), run_time=0.8)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 3.8)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 4.6)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多几何技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 5.8)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.7)
        
        # 装饰元素
        deco_circles = VGroup(*[
            Circle(
                radius=0.15,
                color=GOLD,
                fill_opacity=0.6,
                stroke_width=0
            ).move_to(
                follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 4), np.sin(i * PI / 4), 0])
            )
            for i in range(8)
        ])
        
        self.play(*[FadeIn(c, scale=0.5) for c in deco_circles], run_time=0.6)
        self.play(Rotate(deco_circles, angle=PI, run_time=2.0))
        
        self.wait(3.0)
        
        # 全部淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.2
        )
    
    def create_right_angle_mark(self, corner, point1, point2, size=0.15):
        """创建直角标记"""
        vec1 = point1 - corner
        vec1 = vec1 / np.linalg.norm(vec1) * size
        
        vec2 = point2 - corner
        vec2 = vec2 / np.linalg.norm(vec2) * size
        
        square = Polygon(
            corner,
            corner + vec1,
            corner + vec1 + vec2,
            corner + vec2,
            color=YELLOW,
            stroke_width=1.8,
            fill_opacity=0
        )
        
        return square


# ===== 运行说明 =====
"""
渲染命令:

1. 快速预览 (480p, 15fps):
   manim -pql euler_line.py EulerLineScene

2. 高质量渲染 (1080p, 60fps):
   manim -qh euler_line.py EulerLineScene

3. 4K质量:
   manim -qk euler_line.py EulerLineScene

预计渲染时间:
- 低质量: 2-3分钟
- 高质量: 12-18分钟
"""