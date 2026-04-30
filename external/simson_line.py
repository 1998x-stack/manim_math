"""
西姆松线 (Simson Line) - Manim 教学动画
Mathematical Animation of the Simson Line Theorem

定理: 从三角形外接圆上任意一点向三边作垂线，三个垂足共线。
这条直线称为该点的西姆松线。

作者: 上海初高中数学直通车 @emptyandcalm
目标: TikTok竖屏短视频 (1080×1920)
时长: 75-90秒
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
    def foot_of_perpendicular(point, line_start, line_end):
        """计算点到直线的垂足"""
        line_vec = line_end - line_start
        point_vec = point - line_start
        t = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)
        return line_start + t * line_vec
    
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
    def triangle_area(P1, P2, P3):
        """计算三角形面积 (用于验证共线性)"""
        return 0.5 * abs(
            P1[0]*(P2[1]-P3[1]) + P2[0]*(P3[1]-P1[1]) + P3[0]*(P1[1]-P2[1])
        )
    
    @staticmethod
    def are_collinear(P1, P2, P3, eps=1e-6):
        """验证三点是否共线"""
        area = GeometryCalculator.triangle_area(P1, P2, P3)
        return area < eps
    
    @staticmethod
    def are_perpendicular(V1, V2, eps=1e-8):
        """验证两向量是否垂直"""
        return abs(np.dot(V1[:2], V2[:2])) < eps


class SimsonLineScene(Scene):
    """西姆松线主场景"""
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 定义颜色方案
        self.COLOR_TRIANGLE = WHITE
        self.COLOR_CIRCUMCIRCLE = "#3498db"  # 蓝色
        self.COLOR_POINT_P = "#e74c3c"  # 红色
        self.COLOR_PERPENDICULARS = "#f39c12"  # 橙色
        self.COLOR_FEET = "#2ecc71"  # 绿色
        self.COLOR_SIMSON_LINE = "#9b59b6"  # 紫色
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化所有几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_theorem_statement()
        self.scene_3_construct_perpendicular_1()
        self.scene_4_construct_perpendicular_2()
        self.scene_5_construct_perpendicular_3()
        self.scene_6_simson_line_reveal()
        self.scene_7_dynamic_demonstration()
        self.scene_9_outro()
    
    def setup_geometry(self):
        """统一初始化所有几何元素"""
        print("\n===== 初始化几何数据 =====")
        
        # 基准参数
        self.SCALE = 1.2
        self.OFFSET = UP * 1.8
        
        # 三角形顶点 (使用不等边三角形)
        self.A = np.array([-2.5, -1.0, 0]) * self.SCALE + self.OFFSET
        self.B = np.array([2.2, -1.2, 0]) * self.SCALE + self.OFFSET
        self.C = np.array([0.3, 2.0, 0]) * self.SCALE + self.OFFSET
        
        # 计算外心和外接圆半径
        self.O = GeometryCalculator.circumcenter(self.A, self.B, self.C)
        self.R = np.linalg.norm(self.A - self.O)
        
        # 点P的初始位置 (外接圆上, 角度约150度)
        self.P_angle = 2.6  # 弧度
        self.P = self.O + self.R * np.array([np.cos(self.P_angle), np.sin(self.P_angle), 0])
        
        # 计算三个垂足
        self.D = GeometryCalculator.foot_of_perpendicular(self.P, self.B, self.C)
        self.E = GeometryCalculator.foot_of_perpendicular(self.P, self.C, self.A)
        self.F = GeometryCalculator.foot_of_perpendicular(self.P, self.A, self.B)
        
        # 西姆松线方向
        self.simson_direction = self.E - self.D
        self.simson_direction_normalized = self.simson_direction / np.linalg.norm(self.simson_direction)
        
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
        
        if not (abs(r_A - self.R) < eps and abs(r_B - self.R) < eps and abs(r_C - self.R) < eps):
            print(f"WARNING: 外心计算错误! R={self.R:.6f}, rA={r_A:.6f}, rB={r_B:.6f}, rC={r_C:.6f}")
        else:
            print(f"✓ 外心正确: R = {self.R:.4f}")
        
        # 2. 验证P在圆上
        r_P = np.linalg.norm(self.P - self.O)
        if abs(r_P - self.R) > eps:
            print(f"WARNING: P不在圆上! |OP| = {r_P:.6f}, R = {self.R:.6f}")
        else:
            print(f"✓ P在圆上: |OP| = {r_P:.4f}")
        
        # 3. 验证垂直性
        PD_vec = self.D - self.P
        BC_vec = self.C - self.B
        if not GeometryCalculator.are_perpendicular(PD_vec, BC_vec):
            dot = np.dot(PD_vec[:2], BC_vec[:2])
            print(f"WARNING: PD不垂直于BC! 点积 = {dot:.6f}")
        else:
            print("✓ PD ⊥ BC")
        
        PE_vec = self.E - self.P
        CA_vec = self.A - self.C
        if not GeometryCalculator.are_perpendicular(PE_vec, CA_vec):
            dot = np.dot(PE_vec[:2], CA_vec[:2])
            print(f"WARNING: PE不垂直于CA! 点积 = {dot:.6f}")
        else:
            print("✓ PE ⊥ CA")
        
        PF_vec = self.F - self.P
        AB_vec = self.B - self.A
        if not GeometryCalculator.are_perpendicular(PF_vec, AB_vec):
            dot = np.dot(PF_vec[:2], AB_vec[:2])
            print(f"WARNING: PF不垂直于AB! 点积 = {dot:.6f}")
        else:
            print("✓ PF ⊥ AB")
        
        # 4. 验证共线性 (核心定理!)
        if GeometryCalculator.are_collinear(self.D, self.E, self.F):
            print("✓ D, E, F 共线! (西姆松定理验证通过)")
        else:
            area = GeometryCalculator.triangle_area(self.D, self.E, self.F)
            print(f"WARNING: D, E, F 不共线! 三角形面积 = {area:.6f}")
        
        print("===== 几何验证完成 =====\n")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color=GRAY_B
        ).move_to(UP * 7.3)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook_text = Text(
            "三个垂足竟然共线?",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        subtitle = Text(
            "这就是神奇的西姆松线!",
            font="PingFang SC",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(Write(hook_text, run_time=0.8))
        self.play(FadeIn(subtitle), run_time=0.5)
        
        # 三角形和外接圆
        self.triangle = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_TRIANGLE,
            stroke_width=2.5
        )
        
        self.circumcircle = Circle(
            radius=self.R,
            color=self.COLOR_CIRCUMCIRCLE,
            stroke_width=2
        ).move_to(self.O)
        
        self.play(Create(self.triangle), run_time=1.0)
        self.play(Create(self.circumcircle), run_time=1.0)
        
        # 点P闪烁出现
        P_dot = Dot(self.P, color=self.COLOR_POINT_P, radius=0.10)
        self.play(FadeIn(P_dot, scale=0.5), run_time=0.5)
        self.play(Flash(P_dot, color=self.COLOR_POINT_P, flash_radius=0.3), run_time=0.4)
        
        # 三条垂线快速预览
        PD_preview = DashedLine(self.P, self.D, color=self.COLOR_PERPENDICULARS, dash_length=0.08)
        PE_preview = DashedLine(self.P, self.E, color=self.COLOR_PERPENDICULARS, dash_length=0.08)
        PF_preview = DashedLine(self.P, self.F, color=self.COLOR_PERPENDICULARS, dash_length=0.08)
        
        self.play(
            AnimationGroup(
                Create(PD_preview),
                Create(PE_preview),
                Create(PF_preview),
                lag_ratio=0.2
            ),
            run_time=1.0
        )
        
        # 垂足闪烁
        feet_group = VGroup(
            Dot(self.D, color=self.COLOR_FEET, radius=0.06),
            Dot(self.E, color=self.COLOR_FEET, radius=0.06),
            Dot(self.F, color=self.COLOR_FEET, radius=0.06)
        )
        self.play(FadeIn(feet_group), run_time=0.5)
        
        # 西姆松线戏剧性闪现
        extension = 2.5
        simson_preview = Line(
            self.D - extension * self.simson_direction_normalized,
            self.E + extension * self.simson_direction_normalized,
            color=self.COLOR_SIMSON_LINE,
            stroke_width=3
        )
        
        self.play(Create(simson_preview), run_time=0.8)
        self.play(Flash(simson_preview, color=self.COLOR_SIMSON_LINE, flash_radius=0.6), run_time=0.5)
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(subtitle),
            FadeOut(PD_preview),
            FadeOut(PE_preview),
            FadeOut(PF_preview),
            FadeOut(feet_group),
            FadeOut(simson_preview),
            FadeOut(P_dot),
            run_time=0.6
        )
    
    def scene_2_theorem_statement(self):
        """场景2: 定理陈述"""
        # 标题
        title = Text(
            "西姆松线定理",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_SIMSON_LINE,
            weight=BOLD
        ).move_to(UP * 6)
        
        subtitle_eng = Text(
            "Simson Line Theorem",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.4)
        
        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(subtitle_eng), run_time=0.4)
        
        # 条件说明
        cond1 = Text(
            "① 三角形△ABC及其外接圆Γ",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 4.5 + LEFT * 0.5)
        
        self.play(FadeIn(cond1, shift=UP * 0.2), run_time=0.5)
        self.play(Indicate(VGroup(self.triangle, self.circumcircle), color=self.COLOR_HIGHLIGHT), run_time=0.8)
        
        # 点P出现并移动
        cond2 = Text(
            "② P为Γ上任意一点",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 3.9 + LEFT * 0.5)
        
        self.play(FadeIn(cond2, shift=UP * 0.2), run_time=0.5)
        
        P_dot = Dot(self.P, color=self.COLOR_POINT_P, radius=0.10)
        P_label = Text("P", font="PingFang SC", font_size=24, color=self.COLOR_POINT_P).next_to(P_dot, UR, buff=0.1)
        
        self.play(FadeIn(P_dot, scale=0.5), FadeIn(P_label), run_time=0.5)
        
        # 演示P可以在圆上任意位置
        arc_path = Arc(
            radius=self.R,
            start_angle=self.P_angle,
            angle=PI/2,
            arc_center=self.O
        )
        
        self.play(
            MoveAlongPath(P_dot, arc_path),
            P_label.animate.move_to(self.O + self.R * 1.2 * np.array([np.cos(self.P_angle + PI/2), np.sin(self.P_angle + PI/2), 0])),
            run_time=1.5,
            rate_func=there_and_back
        )
        
        # 条件3: 作垂线
        cond3 = Text(
            "③ 从P向三边作垂线，垂足为D, E, F",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 3.3 + LEFT * 0.5)
        
        self.play(FadeIn(cond3, shift=UP * 0.2), run_time=0.5)
        
        # 绘制三条垂线
        PD_line = DashedLine(self.P, self.D, color=self.COLOR_PERPENDICULARS, dash_length=0.08, stroke_width=2)
        PE_line = DashedLine(self.P, self.E, color=self.COLOR_PERPENDICULARS, dash_length=0.08, stroke_width=2)
        PF_line = DashedLine(self.P, self.F, color=self.COLOR_PERPENDICULARS, dash_length=0.08, stroke_width=2)
        
        self.play(
            Succession(
                Create(PD_line),
                Create(PE_line),
                Create(PF_line)
            ),
            run_time=1.5
        )
        
        # 垂足标记
        feet_dots = VGroup(
            Dot(self.D, color=self.COLOR_FEET, radius=0.07),
            Dot(self.E, color=self.COLOR_FEET, radius=0.07),
            Dot(self.F, color=self.COLOR_FEET, radius=0.07)
        )
        
        feet_labels = VGroup(
            Text("D", font="PingFang SC", font_size=20, color=self.COLOR_FEET).next_to(self.D, DOWN, buff=0.1),
            Text("E", font="PingFang SC", font_size=20, color=self.COLOR_FEET).next_to(self.E, LEFT, buff=0.1),
            Text("F", font="PingFang SC", font_size=20, color=self.COLOR_FEET).next_to(self.F, UR, buff=0.1)
        )
        
        self.play(FadeIn(feet_dots), FadeIn(feet_labels), run_time=0.5)
        
        # 结论
        conclusion = Text(
            "则 D, E, F 三点共线!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 2.5)
        
        self.play(Write(conclusion), run_time=0.8)
        
        # 西姆松线出现
        extension = 2.5
        simson_line = Line(
            self.D - extension * self.simson_direction_normalized,
            self.E + extension * self.simson_direction_normalized,
            color=self.COLOR_SIMSON_LINE,
            stroke_width=3.5
        )
        
        self.play(GrowFromCenter(simson_line), run_time=1.0)
        self.play(Flash(simson_line, color=self.COLOR_SIMSON_LINE, flash_radius=0.6), run_time=0.5)
        
        simson_label = Text(
            "西姆松线",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_SIMSON_LINE
        ).move_to(self.E + extension * 0.7 * self.simson_direction_normalized + UP * 0.3)
        
        self.play(FadeIn(simson_label), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle_eng),
            FadeOut(cond1),
            FadeOut(cond2),
            FadeOut(cond3),
            FadeOut(conclusion),
            FadeOut(PD_line),
            FadeOut(PE_line),
            FadeOut(PF_line),
            FadeOut(feet_dots),
            FadeOut(feet_labels),
            FadeOut(simson_line),
            FadeOut(simson_label),
            FadeOut(P_dot),
            FadeOut(P_label),
            run_time=0.7
        )
    
    def scene_3_construct_perpendicular_1(self):
        """场景3: 构造第一条垂线PD"""
        # 恢复点P
        P_dot = Dot(self.P, color=self.COLOR_POINT_P, radius=0.10)
        P_label = Text("P", font="PingFang SC", font_size=24, color=self.COLOR_POINT_P).next_to(P_dot, UR, buff=0.1)
        
        self.play(FadeIn(P_dot), FadeIn(P_label), run_time=0.3)
        
        # 步骤标题
        step_title = Text(
            "步骤1: 向BC作垂线",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(step_title), run_time=0.5)
        
        # 高亮BC边
        BC_line = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        self.play(Indicate(BC_line, color=self.COLOR_HIGHLIGHT), run_time=0.7)
        
        # 绘制垂线
        PD_line = Line(self.P, self.D, color=self.COLOR_PERPENDICULARS, stroke_width=3)
        
        self.play(Create(PD_line), run_time=1.0)
        
        # 垂足标记
        D_dot = Dot(self.D, color=self.COLOR_FEET, radius=0.08)
        D_label = Text("D", font="PingFang SC", font_size=22, color=self.COLOR_FEET).next_to(D_dot, DOWN, buff=0.12)
        
        self.play(
            FadeIn(D_dot, scale=0.5),
            FadeIn(D_label),
            run_time=0.5
        )
        self.play(Flash(D_dot, color=self.COLOR_FEET, flash_radius=0.25), run_time=0.4)
        
        # 直角标记
        right_angle_D = self.create_right_angle_mark(self.D, self.P, self.B, size=0.18)
        self.play(FadeIn(right_angle_D), run_time=0.4)
        
        # 说明文字
        explain = Text(
            "PD ⊥ BC",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explain), run_time=0.4)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(BC_line),
            FadeOut(explain),
            run_time=0.4
        )
        
        # 保留元素
        self.P_dot_ref = P_dot
        self.P_label_ref = P_label
        self.PD_line_ref = PD_line
        self.D_dot_ref = D_dot
        self.D_label_ref = D_label
        self.right_angle_D_ref = right_angle_D
    
    def scene_4_construct_perpendicular_2(self):
        """场景4: 构造第二条垂线PE"""
        step_title = Text(
            "步骤2: 向CA作垂线",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(step_title), run_time=0.4)
        
        # 高亮CA边
        CA_line = Line(self.C, self.A, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        self.play(Indicate(CA_line, color=self.COLOR_HIGHLIGHT), run_time=0.6)
        
        # 绘制垂线
        PE_line = Line(self.P, self.E, color=self.COLOR_PERPENDICULARS, stroke_width=3)
        self.play(Create(PE_line), run_time=1.0)
        
        # 垂足标记
        E_dot = Dot(self.E, color=self.COLOR_FEET, radius=0.08)
        E_label = Text("E", font="PingFang SC", font_size=22, color=self.COLOR_FEET).next_to(E_dot, LEFT, buff=0.12)
        
        self.play(FadeIn(E_dot, scale=0.5), FadeIn(E_label), run_time=0.5)
        self.play(Flash(E_dot, color=self.COLOR_FEET, flash_radius=0.25), run_time=0.4)
        
        # 直角标记
        right_angle_E = self.create_right_angle_mark(self.E, self.P, self.C, size=0.18)
        self.play(FadeIn(right_angle_E), run_time=0.4)
        
        # 说明
        explain = Text(
            "PE ⊥ CA",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explain), run_time=0.4)
        
        self.wait(0.8)
        
        # 清理
        self.play(FadeOut(step_title), FadeOut(CA_line), FadeOut(explain), run_time=0.4)
        
        # 保留
        self.PE_line_ref = PE_line
        self.E_dot_ref = E_dot
        self.E_label_ref = E_label
        self.right_angle_E_ref = right_angle_E
    
    def scene_5_construct_perpendicular_3(self):
        """场景5: 构造第三条垂线PF"""
        step_title = Text(
            "步骤3: 向AB作垂线",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(step_title), run_time=0.4)
        
        # 高亮AB边
        AB_line = Line(self.A, self.B, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        self.play(Indicate(AB_line, color=self.COLOR_HIGHLIGHT), run_time=0.6)
        
        # 绘制垂线
        PF_line = Line(self.P, self.F, color=self.COLOR_PERPENDICULARS, stroke_width=3)
        self.play(Create(PF_line), run_time=1.0)
        
        # 垂足标记
        F_dot = Dot(self.F, color=self.COLOR_FEET, radius=0.08)
        F_label = Text("F", font="PingFang SC", font_size=22, color=self.COLOR_FEET).next_to(F_dot, UR, buff=0.12)
        
        self.play(FadeIn(F_dot, scale=0.5), FadeIn(F_label), run_time=0.5)
        self.play(Flash(F_dot, color=self.COLOR_FEET, flash_radius=0.25), run_time=0.4)
        
        # 直角标记
        right_angle_F = self.create_right_angle_mark(self.F, self.P, self.A, size=0.18)
        self.play(FadeIn(right_angle_F), run_time=0.4)
        
        # 说明
        explain = Text(
            "PF ⊥ AB",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explain), run_time=0.4)
        
        # 三个垂足同时闪烁
        self.play(
            AnimationGroup(
                Flash(self.D_dot_ref, color=self.COLOR_FEET),
                Flash(self.E_dot_ref, color=self.COLOR_FEET),
                Flash(F_dot, color=self.COLOR_FEET),
                lag_ratio=0.15
            ),
            run_time=1.0
        )
        
        self.wait(0.8)
        
        # 清理
        self.play(FadeOut(step_title), FadeOut(AB_line), FadeOut(explain), run_time=0.4)
        
        # 保留
        self.PF_line_ref = PF_line
        self.F_dot_ref = F_dot
        self.F_label_ref = F_label
        self.right_angle_F_ref = right_angle_F
    
    def scene_6_simson_line_reveal(self):
        """场景6: 西姆松线的戏剧性显现"""
        # 提问文字
        question = Text(
            "神奇的事情发生了...",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.6)
        self.wait(0.4)
        
        # 连接D-E的虚线
        DE_dashed = DashedLine(self.D, self.E, color=GRAY_A, dash_length=0.1, stroke_width=2)
        self.play(Create(DE_dashed), run_time=0.8)
        
        # 连接E-F的虚线
        EF_dashed = DashedLine(self.E, self.F, color=GRAY_A, dash_length=0.1, stroke_width=2)
        self.play(Create(EF_dashed), run_time=0.8)
        
        # 惊叹文字
        surprise = Text(
            "它们在同一直线上!",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Transform(question, surprise), run_time=0.5)
        
        # 西姆松线戏剧性出现
        extension = 2.5
        simson_line = Line(
            self.D - extension * self.simson_direction_normalized,
            self.E + extension * self.simson_direction_normalized,
            color=self.COLOR_SIMSON_LINE,
            stroke_width=4
        )
        
        self.play(
            Transform(VGroup(DE_dashed, EF_dashed), simson_line),
            run_time=1.0
        )
        
        # 闪烁发光效果
        self.play(
            Flash(simson_line, color=self.COLOR_SIMSON_LINE, flash_radius=0.8, line_length=0.3),
            run_time=0.6
        )
        
        self.remove(DE_dashed, EF_dashed)
        self.add(simson_line)
        
        # 标签
        simson_label = Text(
            "西姆松线",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_SIMSON_LINE,
            weight=BOLD
        )
        
        # 标签位置 (在线的中间偏上方)
        label_position = (self.D + self.E) / 2 + UP * 0.4
        simson_label.move_to(label_position)
        
        self.play(Write(simson_label), run_time=0.7)
        
        # 定义文字
        definition = Text(
            "点P的西姆松线 (Simson Line)",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(definition), run_time=0.5)
        
        self.wait(1.8)
        
        # 清理 (准备动态演示)
        self.play(
            FadeOut(question),
            FadeOut(definition),
            FadeOut(self.PD_line_ref),
            FadeOut(self.PE_line_ref),
            FadeOut(self.PF_line_ref),
            FadeOut(self.right_angle_D_ref),
            FadeOut(self.right_angle_E_ref),
            FadeOut(self.right_angle_F_ref),
            run_time=0.6
        )
        
        # 保留
        self.simson_line_ref = simson_line
        self.simson_label_ref = simson_label
    
    def scene_7_dynamic_demonstration(self):
        """场景7: 动态演示 - P点移动"""
        # 提示文字
        hint = Text(
            "当P在圆上移动时...",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(FadeIn(hint), run_time=0.5)
        
        # 使用ValueTracker控制P的角度
        angle_tracker = ValueTracker(self.P_angle)
        
        # 定义动态更新函数
        def get_P_pos(angle):
            return self.O + self.R * np.array([np.cos(angle), np.sin(angle), 0])
        
        def get_feet_and_simson(angle):
            P = get_P_pos(angle)
            D = GeometryCalculator.foot_of_perpendicular(P, self.B, self.C)
            E = GeometryCalculator.foot_of_perpendicular(P, self.C, self.A)
            F = GeometryCalculator.foot_of_perpendicular(P, self.A, self.B)
            
            direction = E - D
            direction_norm = direction / np.linalg.norm(direction)
            
            return D, E, F, direction_norm
        
        # 使用always_redraw创建动态元素
        P_dot_dynamic = always_redraw(lambda: Dot(
            get_P_pos(angle_tracker.get_value()),
            color=self.COLOR_POINT_P,
            radius=0.10
        ))
        
        P_label_dynamic = always_redraw(lambda: Text(
            "P",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_POINT_P
        ).next_to(get_P_pos(angle_tracker.get_value()), UR, buff=0.1))
        
        D_dot_dynamic = always_redraw(lambda: Dot(
            get_feet_and_simson(angle_tracker.get_value())[0],
            color=self.COLOR_FEET,
            radius=0.07
        ))
        
        E_dot_dynamic = always_redraw(lambda: Dot(
            get_feet_and_simson(angle_tracker.get_value())[1],
            color=self.COLOR_FEET,
            radius=0.07
        ))
        
        F_dot_dynamic = always_redraw(lambda: Dot(
            get_feet_and_simson(angle_tracker.get_value())[2],
            color=self.COLOR_FEET,
            radius=0.07
        ))
        
        D_label_dynamic = always_redraw(lambda: Text(
            "D",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_FEET
        ).next_to(get_feet_and_simson(angle_tracker.get_value())[0], DOWN, buff=0.1))
        
        E_label_dynamic = always_redraw(lambda: Text(
            "E",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_FEET
        ).next_to(get_feet_and_simson(angle_tracker.get_value())[1], LEFT, buff=0.1))
        
        F_label_dynamic = always_redraw(lambda: Text(
            "F",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_FEET
        ).next_to(get_feet_and_simson(angle_tracker.get_value())[2], UR, buff=0.1))
        
        simson_dynamic = always_redraw(lambda: Line(
            get_feet_and_simson(angle_tracker.get_value())[0] - 2.5 * get_feet_and_simson(angle_tracker.get_value())[3],
            get_feet_and_simson(angle_tracker.get_value())[1] + 2.5 * get_feet_and_simson(angle_tracker.get_value())[3],
            color=self.COLOR_SIMSON_LINE,
            stroke_width=3.5
        ))
        
        # 移除静态元素，添加动态元素
        self.remove(
            self.P_dot_ref,
            self.P_label_ref,
            self.D_dot_ref,
            self.E_dot_ref,
            self.F_dot_ref,
            self.D_label_ref,
            self.E_label_ref,
            self.F_label_ref,
            self.simson_line_ref,
            self.simson_label_ref
        )
        
        self.add(
            P_dot_dynamic,
            P_label_dynamic,
            D_dot_dynamic,
            E_dot_dynamic,
            F_dot_dynamic,
            D_label_dynamic,
            E_label_dynamic,
            F_label_dynamic,
            simson_dynamic
        )
        
        # P点移动动画 (沿圆周移动约270度)
        self.play(
            angle_tracker.animate.set_value(self.P_angle + 1.5 * PI),
            run_time=10,
            rate_func=linear
        )
        
        # 说明文字
        property_text = Text(
            "西姆松线随P点旋转变化",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(property_text), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理动态元素
        self.remove(
            P_dot_dynamic,
            P_label_dynamic,
            D_dot_dynamic,
            E_dot_dynamic,
            F_dot_dynamic,
            D_label_dynamic,
            E_label_dynamic,
            F_label_dynamic,
            simson_dynamic
        )
        
        self.play(
            FadeOut(hint),
            FadeOut(property_text),
            run_time=0.5
        )
    
    def scene_9_outro(self):
        """场景9: 片尾总结与关注"""
        # 清空场景
        self.play(
            FadeOut(self.triangle),
            FadeOut(self.circumcircle),
            run_time=0.8
        )
        
        # 总结标题
        summary_title = Text(
            "西姆松线 - 要点总结",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_SIMSON_LINE,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 要点
        point1 = Text(
            "✓ 三角形 + 外接圆 + 圆上一点P",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 4)
        
        point2 = Text(
            "✓ 从P向三边作垂线，得垂足D, E, F",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 3.2)
        
        point3 = Text(
            "✓ D, E, F 三点必共线!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 2.2)
        
        self.play(FadeIn(point1, shift=UP * 0.2), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(point2, shift=UP * 0.2), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(point3, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        
        # 小图示意
        mini_scale = 0.4
        mini_triangle = Polygon(
            self.A * mini_scale,
            self.B * mini_scale,
            self.C * mini_scale,
            color=WHITE,
            stroke_width=1.5
        ).move_to(UP * 0.5)
        
        mini_circle = Circle(
            radius=self.R * mini_scale,
            color=self.COLOR_CIRCUMCIRCLE,
            stroke_width=1.5
        ).move_to(self.O * mini_scale + UP * 0.5)
        
        mini_P = Dot(self.P * mini_scale + UP * 0.5, color=self.COLOR_POINT_P, radius=0.05)
        mini_D = Dot(self.D * mini_scale + UP * 0.5, color=self.COLOR_FEET, radius=0.04)
        mini_E = Dot(self.E * mini_scale + UP * 0.5, color=self.COLOR_FEET, radius=0.04)
        mini_F = Dot(self.F * mini_scale + UP * 0.5, color=self.COLOR_FEET, radius=0.04)
        
        mini_simson = Line(
            (self.D - 2 * self.simson_direction_normalized) * mini_scale + UP * 0.5,
            (self.E + 2 * self.simson_direction_normalized) * mini_scale + UP * 0.5,
            color=self.COLOR_SIMSON_LINE,
            stroke_width=2
        )
        
        mini_diagram = VGroup(mini_triangle, mini_circle, mini_P, mini_D, mini_E, mini_F, mini_simson)
        
        self.play(FadeIn(mini_diagram), run_time=0.8)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 2.8)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多几何技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.7)
        
        # 装饰三角形
        deco_triangles = VGroup(*[
            Polygon(
                ORIGIN,
                RIGHT * 0.25,
                UP * 0.25,
                color=GOLD,
                fill_opacity=0.8,
                stroke_width=0
            ).scale(0.6).move_to(
                follow_text.get_center() + 2.2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0])
            )
            for i in range(6)
        ])
        
        self.play(*[FadeIn(tri, scale=0.5) for tri in deco_triangles], run_time=0.6)
        self.play(Rotate(deco_triangles, angle=PI, run_time=1.8))
        
        self.wait(2.5)
        
        # 全部淡出 - 使用*解包而不是VGroup
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.2
        )
    
    def create_right_angle_mark(self, corner, point1, point2, size=0.18):
        """创建直角标记 (小方框)"""
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
   manim -pql simson_line.py SimsonLineScene

2. 高质量渲染 (1080p, 60fps):
   manim -qh simson_line.py SimsonLineScene

3. 4K质量 (仅用于最终发布):
   manim -qk simson_line.py SimsonLineScene

4. 测试单个场景:
   # 修改construct()方法中的场景调用，注释掉其他场景

预计渲染时间:
- 低质量: 2-3分钟
- 高质量: 10-15分钟
- 4K: 30-45分钟
"""