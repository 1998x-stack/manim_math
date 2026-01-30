"""
尺规作图基础教学动画 - Compass and Straightedge Construction Basics
使用 Manim 创建的小学六年级几何教学视频

内容: 四个基本尺规作图（作等线段、作等角、作中点、作角平分线）
目标观众: 六年级学生
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


class CompassStraightedge(Scene):
    """
    尺规作图基础教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 什么是尺规作图
    3. 作图1: 作一条线段等于已知线段
    4. 作图2: 作一个角等于已知角
    5. 作图3: 作线段的中点
    6. 作图4: 作角的平分线
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_RULER = "#3498db"         # 蓝色 - 直尺
        self.COLOR_COMPASS = "#e74c3c"       # 红色 - 圆规
        self.COLOR_CONSTRUCTION = "#2ecc71"  # 绿色 - 作图痕迹
        self.COLOR_RESULT = "#f39c12"        # 橙色 - 最终结果
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_equal_segment()
        self.scene_4_equal_angle()
        self.scene_5_midpoint()
        self.scene_6_angle_bisector()
        self.scene_7_summary()
    
    def setup_geometry(self):
        """初始化所有几何数据"""
        
        # ===== Scene 3: 作等线段 =====
        self.A_seg = np.array([-2.0, 2.5, 0])
        self.B_seg = np.array([2.0, 2.5, 0])
        self.seg_length = np.linalg.norm(self.B_seg - self.A_seg)
        self.C_seg = np.array([-2.5, 0, 0])
        self.D_seg = self.C_seg + np.array([self.seg_length, 0, 0])
        
        # ===== Scene 4: 作等角 =====
        self.O_angle = np.array([-1.0, 3.0, 0])
        angle_size = 55 * DEGREES
        self.P1_angle = self.O_angle + np.array([2.0, 0, 0])
        self.P2_angle = self.O_angle + np.array([2.0 * np.cos(angle_size), 2.0 * np.sin(angle_size), 0])
        
        self.r1 = 1.2
        self.I1_angle = self.O_angle + np.array([self.r1, 0, 0])
        self.I2_angle = self.O_angle + self.r1 * np.array([np.cos(angle_size), np.sin(angle_size), 0])
        self.chord_length = np.linalg.norm(self.I2_angle - self.I1_angle)
        
        self.O_new = np.array([-2.0, -0.5, 0])
        self.P1_new = self.O_new + np.array([2.0, 0, 0])
        self.I1_new = self.O_new + np.array([self.r1, 0, 0])
        
        # 计算I2_new: 两圆交点
        # 圆1: 以O_new为圆心，r1为半径（已经得到I1_new）
        # 圆2: 以I1_new为圆心，chord_length为半径
        # 这里需要精确计算交点
        self.I2_new = None  # 将在scene_4中动态计算
        
        # ===== Scene 5: 作中点 =====
        self.A_mid = np.array([-2.5, 2.0, 0])
        self.B_mid = np.array([2.5, 2.0, 0])
        self.M = (self.A_mid + self.B_mid) / 2
        
        self.AB_length = np.linalg.norm(self.B_mid - self.A_mid)
        self.r_mid = self.AB_length * 0.7
        
        dir_AB = self.normalize(self.B_mid - self.A_mid)
        perpendicular = np.array([-dir_AB[1], dir_AB[0], 0])
        h = np.sqrt(self.r_mid**2 - (self.AB_length/2)**2)
        self.P_mid = self.M + perpendicular * h
        self.Q_mid = self.M - perpendicular * h
        
        # ===== Scene 6: 作角平分线 =====
        self.O_bisect = np.array([0, 1.5, 0])
        angle_bisect = 70 * DEGREES
        self.A_bisect = self.O_bisect + np.array([2.5 * np.cos(20*DEGREES), 2.5 * np.sin(20*DEGREES), 0])
        self.B_bisect = self.O_bisect + np.array([2.5 * np.cos(-50*DEGREES), 2.5 * np.sin(-50*DEGREES), 0])
        
        self.r_bisect = 1.5
        vec_OA_unit = self.normalize(self.A_bisect - self.O_bisect)
        vec_OB_unit = self.normalize(self.B_bisect - self.O_bisect)
        self.M_bisect = self.O_bisect + vec_OA_unit * self.r_bisect
        self.N_bisect = self.O_bisect + vec_OB_unit * self.r_bisect
        
        # 计算MN的长度
        self.MN_length = np.linalg.norm(self.N_bisect - self.M_bisect)
        self.r2_bisect = self.MN_length * 0.65
        
        # P_bisect: 两圆交点
        # 圆1: 以M_bisect为圆心，r2_bisect为半径
        # 圆2: 以N_bisect为圆心，r2_bisect为半径
        # 选择远离O的交点（角平分线方向）
        self.P_bisect = None  # 将在scene_6中动态计算
        
        print("✓ 几何初始化完成")
    
    def normalize(self, vec):
        """归一化向量"""
        norm = np.linalg.norm(vec)
        if norm < 1e-10:
            return vec
        return vec / norm
    
    def circle_circle_intersection(self, center1, r1, center2, r2, choose_upper=True):
        """
        计算两圆交点（精确计算）
        
        参数:
            center1: 第一个圆的圆心
            r1: 第一个圆的半径
            center2: 第二个圆的圆心
            r2: 第二个圆的半径
            choose_upper: True选择上方交点，False选择下方交点
        
        返回:
            交点坐标（如果存在）
        """
        # 两圆心距离
        d = np.linalg.norm(center2 - center1)
        
        # 检查是否有交点
        if d > r1 + r2 or d < abs(r1 - r2) or d < 1e-10:
            # 无交点或重合，返回近似值
            print(f"警告: 两圆无交点或重合, d={d:.4f}, r1={r1:.4f}, r2={r2:.4f}")
            if choose_upper:
                return center1 + np.array([0, r1, 0])
            else:
                return center1 + np.array([0, -r1, 0])
        
        # 计算交点
        # 使用解析几何公式
        # 设两圆心连线上的一点P，满足 |P-center1| = a, |P-center2| = d-a
        # 由勾股定理: a = (d^2 + r1^2 - r2^2) / (2*d)
        a = (d**2 + r1**2 - r2**2) / (2 * d)
        
        # P点坐标
        P = center1 + a * (center2 - center1) / d
        
        # 从P点垂直方向的距离
        h = np.sqrt(r1**2 - a**2)
        
        # 垂直方向单位向量
        direction = center2 - center1
        perpendicular = np.array([-direction[1], direction[0], 0]) / d
        
        # 两个交点
        if choose_upper:
            return P + h * perpendicular
        else:
            return P - h * perpendicular
    
    def angle_of_vector(self, vec):
        """计算向量相对于正x轴的角度（弧度）"""
        return np.arctan2(vec[1], vec[0])
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（持续存在）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_B
        ).move_to(UP * 7.3)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "只用直尺和圆规\n能画出什么？",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(UP * 5)
        
        self.play(Write(hook_text), run_time=1.2)
        self.wait(0.3)
        
        # 直尺图标
        ruler = Rectangle(
            width=3, height=0.4,
            color=self.COLOR_RULER,
            fill_opacity=0.3,
            stroke_width=3
        ).move_to(UP * 1.5)
        
        ruler_label = Text("直尺", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(ruler, DOWN, buff=0.2)
        
        # 圆规图标（简化）
        compass_circle = Circle(radius=0.8, color=self.COLOR_COMPASS, stroke_width=3).move_to(DOWN * 1.5)
        compass_leg1 = Line(compass_circle.get_center() + UP * 0.3, compass_circle.get_top(), color=self.COLOR_COMPASS, stroke_width=3)
        compass_leg2 = Line(compass_circle.get_center() + UP * 0.3, compass_circle.get_center() + DOWN * 0.8 + LEFT * 0.3, color=self.COLOR_COMPASS, stroke_width=3)
        compass = VGroup(compass_circle, compass_leg1, compass_leg2)
        
        compass_label = Text("圆规", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(compass, DOWN, buff=0.2)
        
        self.play(
            FadeIn(ruler, shift=RIGHT * 0.5),
            FadeIn(ruler_label),
            run_time=0.5
        )
        
        self.play(
            FadeIn(compass, shift=LEFT * 0.5),
            FadeIn(compass_label),
            run_time=0.5
        )
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(ruler),
            FadeOut(ruler_label),
            FadeOut(compass),
            FadeOut(compass_label),
            run_time=0.5
        )
    
    def scene_2_definition(self):
        """场景2: 什么是尺规作图"""
        title = Text(
            "尺规作图",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        definition = Text(
            "只用没有刻度的直尺和圆规\n进行的几何作图",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A,
            line_spacing=1.3
        ).move_to(UP * 4)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(definition, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        
        # 规则1
        rule1_title = Text(
            "直尺",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_RULER,
            weight=BOLD
        ).move_to(UP * 2)
        
        rule1_text = Text(
            "无刻度，只能连接两点画直线",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).next_to(rule1_title, DOWN, buff=0.3)
        
        # 演示：两点连线
        p1 = Dot(rule1_text.get_center() + DOWN * 0.8 + LEFT * 1.5, color=WHITE, radius=0.06)
        p2 = Dot(rule1_text.get_center() + DOWN * 0.8 + RIGHT * 1.5, color=WHITE, radius=0.06)
        line_demo = Line(p1.get_center(), p2.get_center(), color=self.COLOR_RULER, stroke_width=2)
        
        self.play(FadeIn(rule1_title), run_time=0.4)
        self.play(FadeIn(rule1_text), run_time=0.4)
        self.play(FadeIn(p1), FadeIn(p2), run_time=0.3)
        self.play(Create(line_demo), run_time=0.6)
        
        self.wait(0.5)
        
        # 规则2
        rule2_title = Text(
            "圆规",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_COMPASS,
            weight=BOLD
        ).move_to(DOWN * 0.5)
        
        rule2_text = Text(
            "可以画圆和弧",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).next_to(rule2_title, DOWN, buff=0.3)
        
        # 演示：画圆
        center = Dot(rule2_text.get_center() + DOWN * 1.2, color=WHITE, radius=0.06)
        circle_demo = Circle(radius=0.8, color=self.COLOR_COMPASS, stroke_width=2).move_to(center.get_center())
        
        self.play(FadeIn(rule2_title), run_time=0.4)
        self.play(FadeIn(rule2_text), run_time=0.4)
        self.play(FadeIn(center), run_time=0.3)
        self.play(Create(circle_demo), run_time=1.0)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(rule1_title),
            FadeOut(rule1_text),
            FadeOut(rule2_title),
            FadeOut(rule2_text),
            FadeOut(p1), FadeOut(p2), FadeOut(line_demo),
            FadeOut(center), FadeOut(circle_demo),
            run_time=0.6
        )
    
    def scene_3_equal_segment(self):
        """场景3: 作一条线段等于已知线段"""
        title = Text(
            "作图1: 作等长线段",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_RESULT
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 步骤1: 已知线段AB
        step1 = Text(
            "已知: 线段AB",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        segment_AB = Line(self.A_seg, self.B_seg, color=WHITE, stroke_width=4)
        dot_A = Dot(self.A_seg, color=WHITE, radius=0.08)
        dot_B = Dot(self.B_seg, color=WHITE, radius=0.08)
        label_A = Text("A", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(dot_A, LEFT, buff=0.15)
        label_B = Text("B", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(dot_B, RIGHT, buff=0.15)
        
        self.play(FadeIn(step1), run_time=0.4)
        self.play(Create(segment_AB), run_time=0.7)
        self.play(
            FadeIn(dot_A), FadeIn(dot_B),
            FadeIn(label_A), FadeIn(label_B),
            run_time=0.5
        )
        
        self.wait(0.8)
        
        # 步骤2: 取点C
        step2 = Text(
            "作法: 取点C",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        dot_C = Dot(self.C_seg, color=self.COLOR_RESULT, radius=0.08)
        label_C = Text("C", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(dot_C, LEFT, buff=0.15)
        
        self.play(Transform(step1, step2), run_time=0.4)
        self.play(FadeIn(dot_C, scale=0.5), FadeIn(label_C), run_time=0.5)
        
        self.wait(0.5)
        
        # 步骤3: 圆规量取AB长度
        step3 = Text(
            "用圆规量取AB长度",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        # 圆规示意（简化）
        compass_at_AB = Arc(
            radius=self.seg_length,
            start_angle=0,
            angle=PI/3,
            color=self.COLOR_COMPASS,
            stroke_width=2
        ).move_arc_center_to(self.A_seg)
        
        self.play(Transform(step1, step3), run_time=0.4)
        self.play(Create(compass_at_AB), run_time=1.0)
        
        self.wait(0.5)
        
        # 步骤4: 以C为圆心，AB为半径画弧
        step4 = Text(
            "以C为圆心，AB为半径画弧",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        # 计算圆弧的精确角度：从C指向D的方向
        angle_C_to_D = self.angle_of_vector(self.D_seg - self.C_seg)
        
        arc_C = Arc(
            radius=self.seg_length,
            start_angle=angle_C_to_D - 20*DEGREES,
            angle=40*DEGREES,
            color=self.COLOR_CONSTRUCTION,
            stroke_width=3
        ).move_arc_center_to(self.C_seg)
        
        self.play(
            Transform(step1, step4),
            FadeOut(compass_at_AB),
            run_time=0.4
        )
        self.play(Create(arc_C), run_time=1.2)
        
        self.wait(0.5)
        
        # 步骤5: 在弧上取点D
        step5 = Text(
            "在弧上取点D",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        dot_D = Dot(self.D_seg, color=self.COLOR_RESULT, radius=0.08)
        label_D = Text("D", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(dot_D, RIGHT, buff=0.15)
        
        self.play(Transform(step1, step5), run_time=0.4)
        self.play(
            FadeIn(dot_D, scale=0.5),
            Flash(dot_D, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            FadeIn(label_D),
            run_time=0.6
        )
        
        self.wait(0.5)
        
        # 步骤6: 连接CD
        segment_CD = Line(self.C_seg, self.D_seg, color=self.COLOR_RESULT, stroke_width=4)
        
        self.play(Create(segment_CD), run_time=0.8)
        
        self.wait(0.5)
        
        # 结论
        result = Text(
            "CD = AB ✓",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(result, scale=1.1), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(step1),
            FadeOut(segment_AB), FadeOut(dot_A), FadeOut(dot_B),
            FadeOut(label_A), FadeOut(label_B),
            FadeOut(dot_C), FadeOut(label_C),
            FadeOut(arc_C), FadeOut(dot_D), FadeOut(label_D),
            FadeOut(segment_CD), FadeOut(result),
            run_time=0.6
        )
    
    def scene_4_equal_angle(self):
        """场景4: 作一个角等于已知角"""
        
        # 预先计算I2_new（两圆交点）
        I2_new = self.circle_circle_intersection(
            self.O_new, self.r1,
            self.I1_new, self.chord_length,
            choose_upper=True
        )
        
        title = Text(
            "作图2: 作等大的角",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_RESULT
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 步骤1: 已知角∠AOB
        step1 = Text(
            "已知: 角AOB",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        ray_OA = Line(self.O_angle, self.P1_angle, color=WHITE, stroke_width=3)
        ray_OB = Line(self.O_angle, self.P2_angle, color=WHITE, stroke_width=3)
        dot_O = Dot(self.O_angle, color=WHITE, radius=0.08)
        label_O = Text("O", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(dot_O, DOWN, buff=0.15)
        
        self.play(FadeIn(step1), run_time=0.4)
        self.play(
            Create(ray_OA), Create(ray_OB),
            FadeIn(dot_O), FadeIn(label_O),
            run_time=0.8
        )
        
        self.wait(0.6)
        
        # 步骤2: 以O为圆心画弧
        step2 = Text(
            "以O为圆心画弧，交两边于M、N",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        angle_size = np.arctan2((self.P2_angle - self.O_angle)[1], (self.P2_angle - self.O_angle)[0])
        arc1 = Arc(
            radius=self.r1,
            start_angle=0,
            angle=angle_size,
            color=self.COLOR_CONSTRUCTION,
            stroke_width=3
        ).move_arc_center_to(self.O_angle)
        
        dot_M = Dot(self.I1_angle, color=self.COLOR_CONSTRUCTION, radius=0.07)
        dot_N = Dot(self.I2_angle, color=self.COLOR_CONSTRUCTION, radius=0.07)
        label_M = Text("M", font="Noto Sans CJK SC", font_size=18, color=WHITE).next_to(dot_M, RIGHT, buff=0.1)
        label_N = Text("N", font="Noto Sans CJK SC", font_size=18, color=WHITE).next_to(dot_N, UP, buff=0.1)
        
        self.play(Transform(step1, step2), run_time=0.4)
        self.play(Create(arc1), run_time=1.0)
        self.play(
            FadeIn(dot_M), FadeIn(dot_N),
            FadeIn(label_M), FadeIn(label_N),
            run_time=0.5
        )
        
        self.wait(0.6)
        
        # 步骤3: 画射线O'A'
        step3 = Text(
            "画射线O'A'",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        ray_new = Line(self.O_new, self.P1_new, color=WHITE, stroke_width=3)
        dot_O_new = Dot(self.O_new, color=WHITE, radius=0.08)
        label_O_new = Text("O'", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(dot_O_new, DOWN, buff=0.15)
        
        self.play(Transform(step1, step3), run_time=0.4)
        self.play(
            Create(ray_new),
            FadeIn(dot_O_new), FadeIn(label_O_new),
            run_time=0.7
        )
        
        self.wait(0.5)
        
        # 步骤4: 以O'为圆心，同样半径画弧
        step4 = Text(
            "以O'为圆心，相同半径画弧",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        # 计算圆弧角度：从I1_new(M')的方向
        angle_to_M_new = self.angle_of_vector(self.I1_new - self.O_new)
        # 延伸到I2_new(N')的方向
        angle_to_N_new = self.angle_of_vector(I2_new - self.O_new)
        angle_span = angle_to_N_new - angle_to_M_new
        if angle_span < 0:
            angle_span += 2 * PI
        
        arc2 = Arc(
            radius=self.r1,
            start_angle=angle_to_M_new - 10*DEGREES,
            angle=angle_span + 20*DEGREES,
            color=self.COLOR_CONSTRUCTION,
            stroke_width=3
        ).move_arc_center_to(self.O_new)
        
        dot_M_new = Dot(self.I1_new, color=self.COLOR_CONSTRUCTION, radius=0.07)
        label_M_new = Text("M'", font="Noto Sans CJK SC", font_size=18, color=WHITE).next_to(dot_M_new, RIGHT, buff=0.1)
        
        self.play(Transform(step1, step4), run_time=0.4)
        self.play(Create(arc2), run_time=1.0)
        self.play(FadeIn(dot_M_new), FadeIn(label_M_new), run_time=0.4)
        
        self.wait(0.5)
        
        # 步骤5: 以M'为圆心，MN为半径画弧
        step5 = Text(
            "以M'为圆心，MN为半径画弧",
            font="Noto Sans CJK SC",
            font_size=19,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        # 计算圆弧角度：从I1_new指向I2_new的方向
        angle_M_to_N = self.angle_of_vector(I2_new - self.I1_new)
        
        arc3 = Arc(
            radius=self.chord_length,
            start_angle=angle_M_to_N - 30*DEGREES,
            angle=60*DEGREES,
            color=self.COLOR_CONSTRUCTION,
            stroke_width=3
        ).move_arc_center_to(self.I1_new)
        
        self.play(Transform(step1, step5), run_time=0.4)
        self.play(Create(arc3), run_time=1.2)
        
        self.wait(0.5)
        
        # 步骤6: 两弧交点N'（已经在函数开头计算）
        dot_N_new = Dot(I2_new, color=self.COLOR_RESULT, radius=0.08)
        label_N_new = Text("N'", font="Noto Sans CJK SC", font_size=18, color=WHITE).next_to(dot_N_new, UP, buff=0.1)
        
        self.play(
            FadeIn(dot_N_new, scale=0.5),
            Flash(dot_N_new, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            FadeIn(label_N_new),
            run_time=0.7
        )
        
        self.wait(0.5)
        
        # 步骤7: 连接O'N'
        ray_ON_new = Line(self.O_new, I2_new, color=self.COLOR_RESULT, stroke_width=3)
        
        self.play(Create(ray_ON_new), run_time=0.8)
        
        self.wait(0.5)
        
        # 结论
        result = Text(
            "∠A'O'N' = ∠AOB ✓",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(result, scale=1.1), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(step1),
            FadeOut(ray_OA), FadeOut(ray_OB), FadeOut(dot_O), FadeOut(label_O),
            FadeOut(arc1), FadeOut(dot_M), FadeOut(dot_N),
            FadeOut(label_M), FadeOut(label_N),
            FadeOut(ray_new), FadeOut(dot_O_new), FadeOut(label_O_new),
            FadeOut(arc2), FadeOut(dot_M_new), FadeOut(label_M_new),
            FadeOut(arc3), FadeOut(dot_N_new), FadeOut(label_N_new),
            FadeOut(ray_ON_new), FadeOut(result),
            run_time=0.6
        )
    
    def scene_5_midpoint(self):
        """场景5: 作线段的中点"""
        title = Text(
            "作图3: 作线段中点",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_RESULT
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 步骤1: 线段AB
        step1 = Text(
            "已知: 线段AB",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        segment = Line(self.A_mid, self.B_mid, color=WHITE, stroke_width=4)
        dot_A_mid = Dot(self.A_mid, color=WHITE, radius=0.08)
        dot_B_mid = Dot(self.B_mid, color=WHITE, radius=0.08)
        label_A_mid = Text("A", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(dot_A_mid, LEFT, buff=0.15)
        label_B_mid = Text("B", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(dot_B_mid, RIGHT, buff=0.15)
        
        self.play(FadeIn(step1), run_time=0.4)
        self.play(Create(segment), run_time=0.7)
        self.play(
            FadeIn(dot_A_mid), FadeIn(dot_B_mid),
            FadeIn(label_A_mid), FadeIn(label_B_mid),
            run_time=0.5
        )
        
        self.wait(0.6)
        
        # 步骤2: 以A为圆心画弧（上下）
        step2 = Text(
            "以A为圆心，大于AB一半的长度画弧",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        # 计算圆弧的精确角度范围
        # 上弧：从P_mid方向画弧
        angle_to_P = self.angle_of_vector(self.P_mid - self.A_mid)
        # 下弧：从Q_mid方向画弧
        angle_to_Q = self.angle_of_vector(self.Q_mid - self.A_mid)
        
        # 上弧：包含P点
        arc_A_upper = Arc(
            radius=self.r_mid,
            start_angle=angle_to_P - 30*DEGREES,
            angle=60*DEGREES,
            color=self.COLOR_CONSTRUCTION,
            stroke_width=3
        ).move_arc_center_to(self.A_mid)
        
        # 下弧：包含Q点
        arc_A_lower = Arc(
            radius=self.r_mid,
            start_angle=angle_to_Q - 30*DEGREES,
            angle=60*DEGREES,
            color=self.COLOR_CONSTRUCTION,
            stroke_width=3
        ).move_arc_center_to(self.A_mid)
        
        self.play(Transform(step1, step2), run_time=0.4)
        self.play(
            Create(arc_A_upper),
            Create(arc_A_lower),
            run_time=1.5
        )
        
        self.wait(0.5)
        
        # 步骤3: 以B为圆心画弧（上下）
        step3 = Text(
            "以B为圆心，相同长度画弧",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        # 计算圆弧的精确角度范围
        # 上弧：从P_mid方向画弧
        angle_to_P_B = self.angle_of_vector(self.P_mid - self.B_mid)
        # 下弧：从Q_mid方向画弧
        angle_to_Q_B = self.angle_of_vector(self.Q_mid - self.B_mid)
        
        # 上弧：包含P点
        arc_B_upper = Arc(
            radius=self.r_mid,
            start_angle=angle_to_P_B - 30*DEGREES,
            angle=60*DEGREES,
            color=self.COLOR_CONSTRUCTION,
            stroke_width=3
        ).move_arc_center_to(self.B_mid)
        
        # 下弧：包含Q点
        arc_B_lower = Arc(
            radius=self.r_mid,
            start_angle=angle_to_Q_B - 30*DEGREES,
            angle=60*DEGREES,
            color=self.COLOR_CONSTRUCTION,
            stroke_width=3
        ).move_arc_center_to(self.B_mid)
        
        self.play(Transform(step1, step3), run_time=0.4)
        self.play(
            Create(arc_B_upper),
            Create(arc_B_lower),
            run_time=1.5
        )
        
        self.wait(0.5)
        
        # 步骤4: 标记交点P、Q
        dot_P = Dot(self.P_mid, color=self.COLOR_RESULT, radius=0.08)
        dot_Q = Dot(self.Q_mid, color=self.COLOR_RESULT, radius=0.08)
        label_P = Text("P", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(dot_P, UP, buff=0.12)
        label_Q = Text("Q", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(dot_Q, DOWN, buff=0.12)
        
        self.play(
            FadeIn(dot_P, scale=0.5),
            FadeIn(dot_Q, scale=0.5),
            Flash(dot_P, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            Flash(dot_Q, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            FadeIn(label_P), FadeIn(label_Q),
            run_time=0.8
        )
        
        self.wait(0.5)
        
        # 步骤5: 连接PQ
        line_PQ = Line(self.P_mid, self.Q_mid, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        self.play(Create(line_PQ), run_time=0.8)
        
        self.wait(0.5)
        
        # 步骤6: 标记中点M
        dot_M = Dot(self.M, color=self.COLOR_RESULT, radius=0.1)
        label_M = Text("M", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_HIGHLIGHT).next_to(dot_M, DOWN, buff=0.2)
        
        self.play(
            FadeIn(dot_M, scale=0.5),
            Flash(dot_M, color=self.COLOR_HIGHLIGHT, flash_radius=0.4),
            FadeIn(label_M),
            run_time=0.8
        )
        
        self.wait(0.5)
        
        # 结论
        result = Text(
            "M是AB的中点 ✓",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(result, scale=1.1), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(step1),
            FadeOut(segment), FadeOut(dot_A_mid), FadeOut(dot_B_mid),
            FadeOut(label_A_mid), FadeOut(label_B_mid),
            FadeOut(arc_A_upper), FadeOut(arc_A_lower),
            FadeOut(arc_B_upper), FadeOut(arc_B_lower),
            FadeOut(dot_P), FadeOut(dot_Q),
            FadeOut(label_P), FadeOut(label_Q),
            FadeOut(line_PQ), FadeOut(dot_M), FadeOut(label_M),
            FadeOut(result),
            run_time=0.6
        )
    
    def scene_6_angle_bisector(self):
        """场景6: 作角的平分线"""
        
        # 预先计算P点（两圆交点）
        P_bisect_calculated = self.circle_circle_intersection(
            self.M_bisect, self.r2_bisect,
            self.N_bisect, self.r2_bisect,
            choose_upper=True
        )
        
        title = Text(
            "作图4: 作角平分线",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_RESULT
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 步骤1: 角∠AOB
        step1 = Text(
            "已知: 角AOB",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        ray_OA_bisect = Line(self.O_bisect, self.A_bisect, color=WHITE, stroke_width=3)
        ray_OB_bisect = Line(self.O_bisect, self.B_bisect, color=WHITE, stroke_width=3)
        dot_O_bisect = Dot(self.O_bisect, color=WHITE, radius=0.08)
        label_O_bisect = Text("O", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(dot_O_bisect, LEFT, buff=0.15)
        
        self.play(FadeIn(step1), run_time=0.4)
        self.play(
            Create(ray_OA_bisect), Create(ray_OB_bisect),
            FadeIn(dot_O_bisect), FadeIn(label_O_bisect),
            run_time=0.8
        )
        
        self.wait(0.6)
        
        # 步骤2: 以O为圆心画弧
        step2 = Text(
            "以O为圆心画弧，交两边于M、N",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        angle_start = np.arctan2((self.B_bisect - self.O_bisect)[1], (self.B_bisect - self.O_bisect)[0])
        angle_end = np.arctan2((self.A_bisect - self.O_bisect)[1], (self.A_bisect - self.O_bisect)[0])
        angle_span = angle_end - angle_start
        
        arc_bisect = Arc(
            radius=self.r_bisect,
            start_angle=angle_start,
            angle=angle_span,
            color=self.COLOR_CONSTRUCTION,
            stroke_width=3
        ).move_arc_center_to(self.O_bisect)
        
        dot_M_bisect = Dot(self.M_bisect, color=self.COLOR_CONSTRUCTION, radius=0.07)
        dot_N_bisect = Dot(self.N_bisect, color=self.COLOR_CONSTRUCTION, radius=0.07)
        label_M_bisect = Text("M", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(dot_M_bisect, UR, buff=0.1)
        label_N_bisect = Text("N", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(dot_N_bisect, DR, buff=0.1)
        
        self.play(Transform(step1, step2), run_time=0.4)
        self.play(Create(arc_bisect), run_time=1.0)
        self.play(
            FadeIn(dot_M_bisect), FadeIn(dot_N_bisect),
            FadeIn(label_M_bisect), FadeIn(label_N_bisect),
            run_time=0.5
        )
        
        self.wait(0.6)
        
        # 步骤3: 以M为圆心画弧
        step3 = Text(
            "以M为圆心画弧",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        # 计算圆弧的精确角度：从M指向P的方向
        angle_M_to_P = self.angle_of_vector(P_bisect_calculated - self.M_bisect)
        
        arc_M = Arc(
            radius=self.r2_bisect,
            start_angle=angle_M_to_P - 40*DEGREES,
            angle=80*DEGREES,
            color=self.COLOR_CONSTRUCTION,
            stroke_width=3
        ).move_arc_center_to(self.M_bisect)
        
        self.play(Transform(step1, step3), run_time=0.4)
        self.play(Create(arc_M), run_time=1.0)
        
        self.wait(0.5)
        
        # 步骤4: 以N为圆心画弧（同半径）
        step4 = Text(
            "以N为圆心，相同半径画弧",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        # 计算圆弧的精确角度：从N指向P的方向
        angle_N_to_P = self.angle_of_vector(P_bisect_calculated - self.N_bisect)
        
        arc_N = Arc(
            radius=self.r2_bisect,
            start_angle=angle_N_to_P - 40*DEGREES,
            angle=80*DEGREES,
            color=self.COLOR_CONSTRUCTION,
            stroke_width=3
        ).move_arc_center_to(self.N_bisect)
        
        self.play(Transform(step1, step4), run_time=0.4)
        self.play(Create(arc_N), run_time=1.0)
        
        self.wait(0.5)
        
        # 步骤5: 两弧交于P（已经在函数开头计算）
        dot_P_bisect = Dot(P_bisect_calculated, color=self.COLOR_RESULT, radius=0.08)
        label_P_bisect = Text("P", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(dot_P_bisect, RIGHT, buff=0.15)
        
        self.play(
            FadeIn(dot_P_bisect, scale=0.5),
            Flash(dot_P_bisect, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            FadeIn(label_P_bisect),
            run_time=0.7
        )
        
        self.wait(0.5)
        
        # 步骤6: 连接OP
        bisector = Line(self.O_bisect, P_bisect_calculated, color=self.COLOR_RESULT, stroke_width=3)
        
        self.play(Create(bisector), run_time=0.8)
        
        self.wait(0.5)
        
        # 结论
        result = Text(
            "OP平分∠AOB ✓",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(result, scale=1.1), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(step1),
            FadeOut(ray_OA_bisect), FadeOut(ray_OB_bisect),
            FadeOut(dot_O_bisect), FadeOut(label_O_bisect),
            FadeOut(arc_bisect), FadeOut(dot_M_bisect), FadeOut(dot_N_bisect),
            FadeOut(label_M_bisect), FadeOut(label_N_bisect),
            FadeOut(arc_M), FadeOut(arc_N),
            FadeOut(dot_P_bisect), FadeOut(label_P_bisect),
            FadeOut(bisector), FadeOut(result),
            run_time=0.6
        )
    
    def scene_7_summary(self):
        """场景7: 总结与片尾"""
        # 标题
        title = Text(
            "四个基本尺规作图",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        self.wait(0.4)
        
        # 四个小图标卡片
        icon_y_positions = [3.5, 1.8, 0.1, -1.6]
        
        # 图标1: 作等线段
        icon1_title = Text("1. 作等长线段", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        icon1_line = Line(LEFT * 0.8, RIGHT * 0.8, color=self.COLOR_RESULT, stroke_width=3)
        icon1 = VGroup(icon1_title, icon1_line).arrange(RIGHT, buff=0.3).move_to(UP * icon_y_positions[0])
        
        # 图标2: 作等角
        icon2_title = Text("2. 作等大的角", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        icon2_angle = VGroup(
            Line(ORIGIN, RIGHT * 0.6, color=self.COLOR_RESULT, stroke_width=2),
            Line(ORIGIN, UR * 0.6, color=self.COLOR_RESULT, stroke_width=2)
        )
        icon2 = VGroup(icon2_title, icon2_angle).arrange(RIGHT, buff=0.3).move_to(UP * icon_y_positions[1])
        
        # 图标3: 作中点
        icon3_title = Text("3. 作线段中点", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        icon3_point = Dot(ORIGIN, color=self.COLOR_RESULT, radius=0.08)
        icon3_line = Line(LEFT * 0.6, RIGHT * 0.6, color=GRAY_B, stroke_width=2)
        icon3 = VGroup(icon3_title, VGroup(icon3_line, icon3_point)).arrange(RIGHT, buff=0.3).move_to(UP * icon_y_positions[2])
        
        # 图标4: 作角平分线
        icon4_title = Text("4. 作角平分线", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        icon4_angle = VGroup(
            Line(ORIGIN, RIGHT * 0.6, color=GRAY_B, stroke_width=2),
            Line(ORIGIN, UP * 0.6, color=GRAY_B, stroke_width=2),
            Line(ORIGIN, (RIGHT + UP) * 0.42, color=self.COLOR_RESULT, stroke_width=2)
        )
        icon4 = VGroup(icon4_title, icon4_angle).arrange(RIGHT, buff=0.3).move_to(UP * icon_y_positions[3])
        
        # 依次出现
        icons = [icon1, icon2, icon3, icon4]
        for icon in icons:
            icon.shift(LEFT * 10)  # 初始位置在左侧外
        
        for icon in icons:
            self.play(icon.animate.shift(RIGHT * 10), run_time=0.5)
            self.wait(0.2)
        
        self.wait(0.8)
        
        # 关键提示
        hint = Text(
            "记住：作图痕迹要保留！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(hint, scale=1.1), run_time=0.6)
        self.wait(1.0)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=34,
            color=WHITE
        ).move_to(DOWN * 5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 5.8)
        
        self.play(
            FadeOut(title),
            FadeOut(icon1), FadeOut(icon2), FadeOut(icon3), FadeOut(icon4),
            FadeOut(hint),
            run_time=0.5
        )
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        
        # 关注文字
        follow_text = Text(
            "关注我，学更多几何技巧！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 7)
        
        self.play(Write(follow_text), run_time=0.8)
        
        # 装饰：旋转的小圆规图标
        decorations = VGroup()
        for i in range(6):
            angle = i * 60 * DEGREES
            small_compass = Circle(
                radius=0.15,
                color=self.COLOR_COMPASS,
                fill_opacity=0.6,
                stroke_width=2
            ).shift(1.5 * np.array([np.cos(angle), np.sin(angle), 0]))
            decorations.add(small_compass)
        
        decorations.move_to(UP * 0.5)
        
        self.play(
            *[FadeIn(dec, scale=0.5) for dec in decorations],
            run_time=0.6
        )
        
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        
        self.wait(0.8)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


# 运行命令:
# manim -pql compass_straightedge.py CompassStraightedge  # 快速预览
# manim -qh compass_straightedge.py CompassStraightedge   # 高质量渲染 (1080p)