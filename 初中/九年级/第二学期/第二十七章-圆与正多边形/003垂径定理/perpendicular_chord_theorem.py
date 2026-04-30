"""
垂径定理动画 - Perpendicular Chord Theorem Animation
使用 Manim 创建的九年级数学教学视频

内容: 垂径定理的定义、证明和性质
目标观众: 九年级学生
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


class GeometryCalculator:
    """几何计算工具类 - 所有计算必须使用此类"""
    
    @staticmethod
    def midpoint(P1, P2):
        """计算中点"""
        return (P1 + P2) / 2
    
    @staticmethod
    def foot_of_perpendicular(point, line_start, line_end):
        """
        计算点到直线的垂足
        参数:
            point: 要投影的点
            line_start, line_end: 定义直线的两点
        返回:
            垂足坐标
        """
        line_vec = line_end - line_start
        point_vec = point - line_start
        t = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)
        return line_start + t * line_vec
    
    @staticmethod
    def angle_between(V1, V2):
        """计算两向量夹角（弧度）"""
        cos_angle = np.dot(V1, V2) / (np.linalg.norm(V1) * np.linalg.norm(V2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        return np.arccos(cos_angle)
    
    @staticmethod
    def angle_at_vertex(A, B, C):
        """计算∠ABC的角度（弧度），B是顶点"""
        BA = A - B
        BC = C - B
        return GeometryCalculator.angle_between(BA, BC)


class PerpendicularChordTheorem(Scene):
    """
    垂径定理教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 绘制直径
    3. 证明平分弦
    4. 证明平分优弧
    5. 证明平分劣弧
    6. 定理总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CIRCLE = "#3498db"       # 蓝色 - 圆
        self.COLOR_DIAMETER = "#e74c3c"     # 红色 - 直径
        self.COLOR_CHORD = "#f39c12"        # 橙色 - 弦
        self.COLOR_HIGHLIGHT = YELLOW       # 高亮黄色
        self.COLOR_AUXILIARY = GRAY_B       # 辅助灰色
        self.COLOR_ARC_MAJOR = "#9b59b6"    # 紫色 - 大弧
        self.COLOR_ARC_MINOR = "#2ecc71"    # 绿色 - 小弧
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_draw_diameter()
        self.scene_3_bisect_chord()
        self.scene_4_bisect_major_arc()
        self.scene_5_bisect_minor_arc()
        self.scene_6_theorem_summary()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素的坐标"""
        # 基准参数
        self.SCALE = 0.85
        self.OFFSET = UP * 1.0
        
        # 圆心和半径
        self.O = np.array([0, 0, 0]) + self.OFFSET
        self.radius = 2.5 * self.SCALE
        
        # 弦AB的端点（圆周上）
        # 选择角度使得弦不水平，便于展示垂直关系
        angle_A = 150 * DEGREES  # 左上
        angle_B = 30 * DEGREES   # 右下
        
        self.A = self.O + self.radius * np.array([np.cos(angle_A), np.sin(angle_A), 0])
        self.B = self.O + self.radius * np.array([np.cos(angle_B), np.sin(angle_B), 0])
        
        # 弦AB的中点M
        self.M = GeometryCalculator.midpoint(self.A, self.B)
        
        # 垂足D（从圆心O到弦AB的垂足）
        self.D = GeometryCalculator.foot_of_perpendicular(self.O, self.A, self.B)
        
        # 验证D = M（垂径定理的核心）
        distance_DM = np.linalg.norm(self.D - self.M)
        if distance_DM > 1e-6:
            print(f"警告: 垂足D与中点M不重合，距离 = {distance_DM}")
        
        # 直径CD（过垂足D）
        # 方向向量：从O指向D
        if np.linalg.norm(self.D - self.O) < 1e-10:
            # 退化情况：弦过圆心（直径）
            OD_unit = np.array([1, 0, 0])
        else:
            OD_vec = self.D - self.O
            OD_unit = OD_vec / np.linalg.norm(OD_vec)
        
        # 直径的两个端点
        self.C = self.O + OD_unit * self.radius
        self.D_ext = self.O - OD_unit * self.radius  # 直径另一端
        
        # 计算圆心角（用于弧的验证）
        self.angle_AOC = GeometryCalculator.angle_at_vertex(self.A, self.O, self.C)
        self.angle_BOC = GeometryCalculator.angle_at_vertex(self.B, self.O, self.C)
        
        # 验证几何关系
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        eps = 1e-6
        errors = []
        
        # 1. 验证A, B在圆上
        dist_OA = np.linalg.norm(self.A - self.O)
        dist_OB = np.linalg.norm(self.B - self.O)
        if abs(dist_OA - self.radius) > eps:
            errors.append(f"点A不在圆上: |OA| = {dist_OA:.6f}, r = {self.radius:.6f}")
        if abs(dist_OB - self.radius) > eps:
            errors.append(f"点B不在圆上: |OB| = {dist_OB:.6f}, r = {self.radius:.6f}")
        
        # 2. 验证C, D_ext在圆上
        dist_OC = np.linalg.norm(self.C - self.O)
        dist_OD_ext = np.linalg.norm(self.D_ext - self.O)
        if abs(dist_OC - self.radius) > eps:
            errors.append(f"点C不在圆上: |OC| = {dist_OC:.6f}")
        if abs(dist_OD_ext - self.radius) > eps:
            errors.append(f"点D_ext不在圆上: |OD_ext| = {dist_OD_ext:.6f}")
        
        # 3. 验证D是AB的中点
        AM = np.linalg.norm(self.M - self.A)
        MB = np.linalg.norm(self.B - self.M)
        if abs(AM - MB) > eps:
            errors.append(f"中点错误: AM = {AM:.6f}, MB = {MB:.6f}")
        
        # 4. 验证OD ⊥ AB
        vec_OD = self.D - self.O
        vec_AB = self.B - self.A
        dot_product = np.dot(vec_OD[:2], vec_AB[:2])
        if abs(dot_product) > 1e-8:
            errors.append(f"不垂直: OD·AB = {dot_product:.8f}")
        
        # 5. 验证圆心角相等（弧相等）
        angle_diff = abs(self.angle_AOC - self.angle_BOC)
        if angle_diff > eps:
            errors.append(f"圆心角不相等: ∠AOC = {np.degrees(self.angle_AOC):.2f}°, ∠BOC = {np.degrees(self.angle_BOC):.2f}°")
        
        # 输出验证结果
        if errors:
            print("❌ 几何验证失败:")
            for e in errors:
                print(f"  - {e}")
            raise ValueError("几何验证失败！请检查计算。")
        else:
            print("✓ 几何验证通过")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "如何快速平分一条弦?",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(hook_question), run_time=0.8)
        
        # 绘制圆
        self.circle = Circle(
            radius=self.radius,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.O)
        
        self.play(Create(self.circle), run_time=1.0)
        
        # 绘制弦AB（高亮橙色）
        self.chord_AB = Line(
            self.A, self.B,
            color=self.COLOR_CHORD,
            stroke_width=5
        )
        
        self.play(Create(self.chord_AB), run_time=0.6)
        
        # 标记点A, B
        self.dot_A = Dot(self.A, color=WHITE, radius=0.08)
        self.dot_B = Dot(self.B, color=WHITE, radius=0.08)
        
        self.label_A = Text("A", font="PingFang SC", font_size=22, color=WHITE).next_to(self.dot_A, UL, buff=0.15)
        self.label_B = Text("B", font="PingFang SC", font_size=22, color=WHITE).next_to(self.dot_B, DR, buff=0.15)
        
        self.play(
            FadeIn(self.dot_A, scale=0.5),
            FadeIn(self.dot_B, scale=0.5),
            run_time=0.4
        )
        self.play(
            Flash(self.dot_A, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            Flash(self.dot_B, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            run_time=0.4
        )
        self.play(Write(self.label_A), Write(self.label_B), run_time=0.3)
        
        # 等待思考
        self.wait(1.0)
        
        # 提示
        hint_text = Text(
            "用垂径定理!",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(hint_text, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(hint_text),
            run_time=0.4
        )
    
    def scene_2_draw_diameter(self):
        """场景2: 绘制垂直于弦的直径"""
        # 标题
        self.title = Text(
            "垂径定理",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_DIAMETER,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(self.title), run_time=0.6)
        
        # 说明文字
        instruction = Text(
            "作垂直于AB的直径",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(instruction), run_time=0.5)
        
        # 从O到弦AB画虚线（辅助线）
        dash_line_OD = DashedLine(
            self.O, self.D,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1,
            stroke_width=2
        )
        
        self.play(Create(dash_line_OD), run_time=0.8)
        
        # 标记垂足D
        self.dot_D = Dot(self.D, color=self.COLOR_DIAMETER, radius=0.08)
        self.label_D = Text("D", font="PingFang SC", font_size=22, color=self.COLOR_DIAMETER).next_to(self.dot_D, DOWN, buff=0.15)
        
        self.play(FadeIn(self.dot_D, scale=0.5), run_time=0.3)
        self.play(Write(self.label_D), run_time=0.3)
        
        # 垂直符号（直角标记）
        # 计算直角符号的方向
        vec_DO = self.O - self.D
        vec_DA = self.A - self.D
        
        # 单位化
        vec_DO_unit = vec_DO / np.linalg.norm(vec_DO) if np.linalg.norm(vec_DO) > 1e-10 else np.array([0, 1, 0])
        vec_DA_unit = vec_DA / np.linalg.norm(vec_DA) if np.linalg.norm(vec_DA) > 1e-10 else np.array([1, 0, 0])
        
        # 直角符号大小
        right_angle_size = 0.2
        
        corner1 = self.D + vec_DO_unit * right_angle_size
        corner2 = corner1 + vec_DA_unit * right_angle_size
        corner3 = self.D + vec_DA_unit * right_angle_size
        
        self.right_angle_mark = Polygon(
            self.D, corner1, corner2, corner3,
            color=YELLOW,
            stroke_width=2,
            fill_opacity=0
        )
        
        self.play(Create(self.right_angle_mark), run_time=0.4)
        
        # 延长到圆周：绘制完整直径
        self.diameter_line = Line(
            self.C, self.D_ext,
            color=self.COLOR_DIAMETER,
            stroke_width=4
        )
        
        self.play(Create(self.diameter_line), run_time=1.0)
        
        # 标记圆心O
        self.dot_O = Dot(self.O, color=RED, radius=0.10)
        self.label_O = Text("O", font="PingFang SC", font_size=24, color=RED).next_to(self.dot_O, LEFT, buff=0.15)
        
        self.play(
            FadeIn(self.dot_O, scale=0.5),
            Write(self.label_O),
            run_time=0.5
        )
        
        # 标记C和D_ext
        self.dot_C = Dot(self.C, color=WHITE, radius=0.08)
        self.dot_D_ext = Dot(self.D_ext, color=WHITE, radius=0.08)
        
        self.label_C = Text("C", font="PingFang SC", font_size=22, color=WHITE).next_to(self.dot_C, UP, buff=0.12)
        
        self.play(
            FadeIn(self.dot_C, scale=0.5),
            FadeIn(self.dot_D_ext, scale=0.5),
            run_time=0.4
        )
        self.play(Write(self.label_C), run_time=0.3)
        
        # 高亮直径
        self.play(
            self.diameter_line.animate.set_stroke(width=6),
            Flash(self.diameter_line, color=self.COLOR_HIGHLIGHT, line_length=0.3),
            run_time=0.3
        )
        
        # 等待理解
        self.wait(1.2)
        
        # 清理辅助线和说明
        self.play(
            FadeOut(instruction),
            FadeOut(dash_line_OD),
            run_time=0.3
        )
    
    def scene_3_bisect_chord(self):
        """场景3: 证明平分弦"""
        # 说明文字
        step1_text = Text(
            "首先，证明平分弦",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 4.2)
        
        self.play(FadeIn(step1_text), run_time=0.5)
        
        # 中点M标记（与D重合）
        dot_M = Dot(self.M, color=self.COLOR_HIGHLIGHT, radius=0.10)
        label_M = Text("M", font="PingFang SC", font_size=24, color=self.COLOR_HIGHLIGHT).next_to(dot_M, RIGHT, buff=0.15)
        
        self.play(FadeIn(dot_M, scale=0.5), run_time=0.3)
        self.play(Flash(dot_M, color=self.COLOR_HIGHLIGHT, flash_radius=0.35), run_time=0.4)
        self.play(Write(label_M), run_time=0.3)
        
        # 计算Brace方向（垂直于AB向外）
        vec_AB = self.B - self.A
        perp_vec = np.array([-vec_AB[1], vec_AB[0], 0])
        perp_unit = perp_vec / np.linalg.norm(perp_vec)
        
        # 创建Brace标注AM
        brace_AM = Brace(Line(self.A, self.M), direction=perp_unit, buff=0.1, color=self.COLOR_CHORD)
        label_AM_text = Text("AM", font="PingFang SC", font_size=20, color=self.COLOR_CHORD)
        label_AM_text.next_to(brace_AM, direction=perp_unit, buff=0.05)
        
        self.play(Create(brace_AM), run_time=0.5)
        self.play(Write(label_AM_text), run_time=0.3)
        
        # 创建Brace标注MB
        brace_MB = Brace(Line(self.M, self.B), direction=perp_unit, buff=0.1, color=self.COLOR_CHORD)
        label_MB_text = Text("MB", font="PingFang SC", font_size=20, color=self.COLOR_CHORD)
        label_MB_text.next_to(brace_MB, direction=perp_unit, buff=0.05)
        
        self.play(Create(brace_MB), run_time=0.5)
        self.play(Write(label_MB_text), run_time=0.3)
        
        # 高亮两段（颜色变化）
        self.play(
            brace_AM.animate.set_color(YELLOW),
            brace_MB.animate.set_color(YELLOW),
            label_AM_text.animate.set_color(YELLOW),
            label_MB_text.animate.set_color(YELLOW),
            run_time=0.4
        )
        
        # 等式AM = MB
        equation_AM_MB = MathTex(
            r"AM = MB",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(Write(equation_AM_MB), run_time=0.8)
        self.play(Flash(equation_AM_MB, color=YELLOW, line_length=0.3), run_time=0.4)
        
        # 等待理解
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(step1_text),
            FadeOut(brace_AM),
            FadeOut(brace_MB),
            FadeOut(label_AM_text),
            FadeOut(label_MB_text),
            FadeOut(equation_AM_MB),
            FadeOut(dot_M),
            FadeOut(label_M),
            run_time=0.5
        )
    
    def scene_4_bisect_major_arc(self):
        """场景4: 证明平分优弧"""
        # 说明文字
        step2_text = Text(
            "其次，平分优弧",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 4.2)
        
        self.play(FadeIn(step2_text), run_time=0.5)
        
        # 计算优弧ACB（从A经过C到B，不经过D_ext）
        # 使用Arc需要计算起止角度
        angle_A_deg = np.arctan2(self.A[1] - self.O[1], self.A[0] - self.O[0])
        angle_C_deg = np.arctan2(self.C[1] - self.O[1], self.C[0] - self.O[0])
        angle_B_deg = np.arctan2(self.B[1] - self.O[1], self.B[0] - self.O[0])
        
        # 计算从A到C的角度（优弧方向）
        # 需要确定是顺时针还是逆时针
        # 从A经过C到B
        
        # 弧AC
        angle_AC = angle_C_deg - angle_A_deg
        if angle_AC < 0:
            angle_AC += 2 * PI
        
        arc_AC = Arc(
            radius=self.radius,
            start_angle=angle_A_deg,
            angle=angle_AC,
            arc_center=self.O,
            color=self.COLOR_ARC_MAJOR,
            stroke_width=5
        )
        
        # 弧CB
        angle_CB = angle_B_deg - angle_C_deg
        if angle_CB < 0:
            angle_CB += 2 * PI
        
        arc_CB = Arc(
            radius=self.radius,
            start_angle=angle_C_deg,
            angle=angle_CB,
            arc_center=self.O,
            color=self.COLOR_ARC_MAJOR,
            stroke_width=5
        )
        
        # 先绘制完整优弧（淡色）
        arc_major_total = Arc(
            radius=self.radius,
            start_angle=angle_A_deg,
            angle=angle_AC + angle_CB,
            arc_center=self.O,
            color=self.COLOR_ARC_MAJOR,
            stroke_width=4,
            stroke_opacity=0.5
        )
        
        self.play(Create(arc_major_total), run_time=1.2)
        
        # 分段显示并变色
        self.play(
            ReplacementTransform(arc_major_total, VGroup(arc_AC, arc_CB)),
            run_time=0.8
        )
        
        # 分别高亮
        self.play(arc_AC.animate.set_stroke(opacity=1, width=6), run_time=0.3)
        self.play(arc_CB.animate.set_stroke(opacity=1, width=6), run_time=0.3)
        
        # 绘制圆心角∠AOC
        line_OA = Line(self.O, self.A, color=self.COLOR_AUXILIARY, stroke_width=2)
        line_OC = Line(self.O, self.C, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        angle_AOC_arc = Angle.from_three_points(
            self.A, self.O, self.C,
            radius=0.4,
            color=YELLOW,
            stroke_width=2
        )
        
        self.play(Create(line_OA), Create(line_OC), run_time=0.5)
        self.play(Create(angle_AOC_arc), run_time=0.5)
        
        # 绘制圆心角∠BOC
        line_OB = Line(self.O, self.B, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        angle_BOC_arc = Angle.from_three_points(
            self.B, self.O, self.C,
            radius=0.4,
            color=YELLOW,
            stroke_width=2
        )
        
        self.play(Create(line_OB), run_time=0.3)
        self.play(Create(angle_BOC_arc), run_time=0.5)
        
        # 标注角度
        label_angle_AOC = MathTex(r"\angle AOC", font_size=20, color=YELLOW).move_to(
            self.O + 0.8 * (self.A + self.C - 2*self.O) / np.linalg.norm(self.A + self.C - 2*self.O)
        )
        
        label_angle_BOC = MathTex(r"\angle BOC", font_size=20, color=YELLOW).move_to(
            self.O + 0.8 * (self.B + self.C - 2*self.O) / np.linalg.norm(self.B + self.C - 2*self.O)
        )
        
        self.play(Write(label_angle_AOC), run_time=0.4)
        self.play(Write(label_angle_BOC), run_time=0.4)
        
        # 等式
        equation_angles = MathTex(
            r"\angle AOC = \angle BOC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(Write(equation_angles), run_time=0.8)
        self.play(Flash(equation_angles, color=YELLOW), run_time=0.4)
        
        # 结论
        # 注意：中文用Text，不能用MathTex
        conclusion_text = Text(
            "弧AC = 弧BC",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        )
        conclusion_symbol = MathTex(r"\therefore", font_size=28, color=self.COLOR_HIGHLIGHT)
        conclusion_group = VGroup(conclusion_symbol, conclusion_text).arrange(RIGHT, buff=0.2).move_to(DOWN * 6.5)
        
        self.play(FadeIn(conclusion_group, shift=UP * 0.3), run_time=0.6)
        
        # 等待理解
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(step2_text),
            FadeOut(arc_AC),
            FadeOut(arc_CB),
            FadeOut(line_OA),
            FadeOut(line_OB),
            FadeOut(line_OC),
            FadeOut(angle_AOC_arc),
            FadeOut(angle_BOC_arc),
            FadeOut(label_angle_AOC),
            FadeOut(label_angle_BOC),
            FadeOut(equation_angles),
            FadeOut(conclusion_group),
            run_time=0.5
        )
    
    def scene_5_bisect_minor_arc(self):
        """场景5: 证明平分劣弧"""
        # 说明文字
        step3_text = Text(
            "同时，平分劣弧",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 4.2)
        
        self.play(FadeIn(step3_text), run_time=0.5)
        
        # 计算劣弧AB（从A经过D_ext到B，不经过C）
        angle_A_deg = np.arctan2(self.A[1] - self.O[1], self.A[0] - self.O[0])
        angle_D_ext_deg = np.arctan2(self.D_ext[1] - self.O[1], self.D_ext[0] - self.O[0])
        angle_B_deg = np.arctan2(self.B[1] - self.O[1], self.B[0] - self.O[0])
        
        # 弧AD_ext
        angle_AD = angle_D_ext_deg - angle_A_deg
        # 确保是劣弧方向（较短的弧）
        if angle_AD > PI:
            angle_AD -= 2 * PI
        elif angle_AD < -PI:
            angle_AD += 2 * PI
        
        arc_AD = Arc(
            radius=self.radius,
            start_angle=angle_A_deg,
            angle=angle_AD,
            arc_center=self.O,
            color=self.COLOR_ARC_MINOR,
            stroke_width=5
        )
        
        # 弧D_extB
        angle_DB = angle_B_deg - angle_D_ext_deg
        if angle_DB > PI:
            angle_DB -= 2 * PI
        elif angle_DB < -PI:
            angle_DB += 2 * PI
        
        arc_DB = Arc(
            radius=self.radius,
            start_angle=angle_D_ext_deg,
            angle=angle_DB,
            arc_center=self.O,
            color=self.COLOR_ARC_MINOR,
            stroke_width=5
        )
        
        # 先绘制完整劣弧
        arc_minor_total = Arc(
            radius=self.radius,
            start_angle=angle_A_deg,
            angle=angle_AD + angle_DB,
            arc_center=self.O,
            color=self.COLOR_ARC_MINOR,
            stroke_width=4,
            stroke_opacity=0.5
        )
        
        self.play(Create(arc_minor_total), run_time=1.0)
        
        # 分段显示
        self.play(
            ReplacementTransform(arc_minor_total, VGroup(arc_AD, arc_DB)),
            run_time=0.6
        )
        
        # 分别高亮
        self.play(arc_AD.animate.set_stroke(opacity=1, width=6), run_time=0.3)
        self.play(arc_DB.animate.set_stroke(opacity=1, width=6), run_time=0.3)
        
        # 对称性指示（闪烁D_ext点）
        self.play(
            Flash(self.dot_D_ext, color=self.COLOR_HIGHLIGHT, flash_radius=0.4),
            Flash(self.dot_D, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            run_time=0.6
        )
        
        # 结论
        conclusion_text = Text(
            "弧AD = 弧DB",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        )
        conclusion_symbol = MathTex(r"\therefore", font_size=28, color=self.COLOR_HIGHLIGHT)
        conclusion_group = VGroup(conclusion_symbol, conclusion_text).arrange(RIGHT, buff=0.2).move_to(DOWN * 5.5)
        
        self.play(FadeIn(conclusion_group, shift=UP * 0.3), run_time=0.5)
        
        # 等待
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(step3_text),
            FadeOut(arc_AD),
            FadeOut(arc_DB),
            FadeOut(conclusion_group),
            run_time=0.5
        )
    
    def scene_6_theorem_summary(self):
        """场景6: 定理总结"""
        # 标题变化
        summary_title = Text(
            "垂径定理",
            font="PingFang SC",
            font_size=38,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Transform(self.title, summary_title), run_time=0.5)
        
        # 定理陈述（分行）
        theorem_line1 = Text(
            "垂直于弦的直径",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        )
        
        theorem_line2 = Text(
            "平分这条弦",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        )
        
        theorem_line3 = Text(
            "并且平分弦所对的两条弧",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        )
        
        theorem_group = VGroup(theorem_line1, theorem_line2, theorem_line3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        theorem_group.move_to(UP * 3)
        
        # 逐行显示
        self.play(Write(theorem_line1), run_time=1.2)
        
        # 高亮关键词"垂直"
        # 需要手动定位关键词
        self.wait(0.3)
        
        self.play(Write(theorem_line2), run_time=0.8)
        
        # 高亮"平分"
        self.wait(0.3)
        
        self.play(Write(theorem_line3), run_time=1.0)
        
        # 高亮"两条弧"
        self.wait(0.3)
        
        # 公式
        # 注意：数学符号用MathTex，中文用Text分离
        formula_part1 = MathTex(r"CD \perp AB", font_size=30, color=self.COLOR_DIAMETER)
        formula_arrow = MathTex(r"\Rightarrow", font_size=30, color=YELLOW)
        formula_part2 = MathTex(r"AM = MB", font_size=30, color=self.COLOR_CHORD)
        
        formula_and = Text("且", font="PingFang SC", font_size=24, color=GRAY_A)
        
        formula_part3_1 = Text("弧", font="PingFang SC", font_size=24, color=self.COLOR_ARC_MAJOR)
        formula_part3_2 = MathTex(r"AC", font_size=28, color=self.COLOR_ARC_MAJOR)
        formula_part3_3 = MathTex(r"=", font_size=28, color=YELLOW)
        formula_part3_4 = Text("弧", font="PingFang SC", font_size=24, color=self.COLOR_ARC_MAJOR)
        formula_part3_5 = MathTex(r"BC", font_size=28, color=self.COLOR_ARC_MAJOR)
        
        formula_line1 = VGroup(formula_part1, formula_arrow, formula_part2).arrange(RIGHT, buff=0.2)
        formula_line2 = VGroup(formula_and, formula_part3_1, formula_part3_2, formula_part3_3, formula_part3_4, formula_part3_5).arrange(RIGHT, buff=0.1)
        
        formula_complete = VGroup(formula_line1, formula_line2).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        
        self.play(Write(formula_complete), run_time=0.8)
        
        # 图示快闪回顾
        self.play(
            Indicate(self.diameter_line, scale_factor=1.1, color=self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        self.play(
            Indicate(self.chord_AB, scale_factor=1.1, color=self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        self.play(
            Flash(self.dot_D, color=YELLOW, flash_radius=0.4),
            run_time=0.5
        )
        
        # 等待记忆
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(theorem_group),
            FadeOut(formula_complete),
            run_time=0.5
        )
    
    def scene_7_outro(self):
        """场景7: 片尾关注"""
        # 淡出所有几何图形
        all_geometry = VGroup(
            self.circle,
            self.chord_AB,
            self.diameter_line,
            self.right_angle_mark,
            self.dot_A, self.dot_B, self.dot_C, self.dot_D, self.dot_D_ext, self.dot_O,
            self.label_A, self.label_B, self.label_C, self.label_D, self.label_O,
            self.title
        )
        
        self.play(FadeOut(all_geometry), run_time=0.6)
        
        # 作者名放大并移动到中心
        author_name_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=42,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 1.5)
        
        self.play(
            Transform(self.author_info, author_name_large),
            run_time=0.8
        )
        
        # 账号ID
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=34,
            color=GRAY_B
        ).move_to(UP * 0.3)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注引导语
        follow_text = Text(
            "关注我，学更多几何技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.5)
        
        # 圆形装饰（6个小圆围绕）
        decoration_circles = VGroup(*[
            Circle(
                radius=0.25,
                color=self.COLOR_CIRCLE,
                fill_opacity=0.6,
                stroke_width=0
            ).shift(2.2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ]).move_to(DOWN * 3)
        
        self.play(
            *[FadeIn(circle, scale=0.5) for circle in decoration_circles],
            run_time=0.6
        )
        self.play(Rotate(decoration_circles, angle=PI, run_time=1.0))
        
        # 关键词闪烁
        keyword = Text(
            "垂径定理",
            font="PingFang SC",
            font_size=36,
            color=GOLD,
            weight=BOLD
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(keyword, scale=0.8), run_time=0.5)
        self.play(Flash(keyword, color=YELLOW, line_length=0.4), run_time=0.5)
        
        # 等待
        self.wait(1.5)
        
        # 全部淡出
        everything = VGroup(
            self.author_info,
            author_id,
            follow_text,
            decoration_circles,
            keyword
        )
        
        self.play(FadeOut(everything), run_time=1.0)


# 运行命令:
# manim -pql perpendicular_chord_theorem.py PerpendicularChordTheorem  # 快速预览
# manim -qh perpendicular_chord_theorem.py PerpendicularChordTheorem   # 高质量渲染