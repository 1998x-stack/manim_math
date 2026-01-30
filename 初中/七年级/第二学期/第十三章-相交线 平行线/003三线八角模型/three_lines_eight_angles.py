"""
三线八角模型动画 - Three Lines Eight Angles Model Animation
使用 Manim 创建的中学几何教学视频

内容: 两条直线被第三条直线所截形成的8个角，以及同位角、内错角、同旁内角的定义
目标观众: 七年级学生
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


class ThreeLinesEightAngles(Scene):
    """
    三线八角模型教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 构建三线八角
    3. 同位角
    4. 内错角
    5. 同旁内角
    6. 知识总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_LINE_1 = "#3498db"      # 蓝色 - 被截线1
        self.COLOR_LINE_2 = "#e74c3c"      # 红色 - 被截线2
        self.COLOR_LINE_3 = "#2ecc71"      # 绿色 - 截线
        self.COLOR_SAME_SIDE = "#f39c12"   # 橙色 - 同位角
        self.COLOR_ALTERNATE = "#9b59b6"   # 紫色 - 内错角
        self.COLOR_CONSECUTIVE = "#e67e22" # 深橙 - 同旁内角
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_construction()
        self.show_corresponding_angles()
        self.show_alternate_angles()
        self.show_consecutive_angles()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化三线八角的几何元素"""
        # 主要配置
        self.MAIN_OFFSET = UP * 1.5  # 整体图形的垂直偏移
        
        # 被截线1 (左上到右下，倾斜)
        self.L1_start = np.array([-3.5, 2.5, 0]) + self.MAIN_OFFSET
        self.L1_end = np.array([3.5, 0.5, 0]) + self.MAIN_OFFSET
        
        # 被截线2 (平行于L1，下方)
        offset_vector = np.array([0, -2, 0])
        self.L2_start = self.L1_start + offset_vector
        self.L2_end = self.L1_end + offset_vector
        
        # 截线 (左下到右上，穿过两条被截线)
        self.L3_start = np.array([-2.5, -1, 0]) + self.MAIN_OFFSET
        self.L3_end = np.array([2.5, 3, 0]) + self.MAIN_OFFSET
        
        # 计算交点
        self.P = self.calculate_line_intersection(
            self.L1_start, self.L1_end - self.L1_start,
            self.L3_start, self.L3_end - self.L3_start
        )
        
        self.Q = self.calculate_line_intersection(
            self.L2_start, self.L2_end - self.L2_start,
            self.L3_start, self.L3_end - self.L3_start
        )
        
        # 验证计算
        self.verify_geometry()
        
        # 创建线对象（但不添加到场景）
        self.line1 = Line(self.L1_start, self.L1_end, color=self.COLOR_LINE_1, stroke_width=4)
        self.line2 = Line(self.L2_start, self.L2_end, color=self.COLOR_LINE_2, stroke_width=4)
        self.line3 = Line(self.L3_start, self.L3_end, color=self.COLOR_LINE_3, stroke_width=4)
    
    def calculate_line_intersection(self, P1, D1, P2, D2):
        """
        计算两直线交点
        直线1: P1 + t*D1
        直线2: P2 + s*D2
        """
        A = np.array([[D1[0], -D2[0]], [D1[1], -D2[1]]])
        b = np.array([P2[0] - P1[0], P2[1] - P1[1]])
        
        det = np.linalg.det(A)
        if np.abs(det) < 1e-10:
            return None  # 平行，无交点
        
        params = np.linalg.solve(A, b)
        intersection = P1 + params[0] * D1
        return np.array([intersection[0], intersection[1], 0])
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证P在line1上
        vec_L1 = self.L1_end - self.L1_start
        vec_P = self.P - self.L1_start
        cross_product_1 = np.cross(vec_L1[:2], vec_P[:2])
        
        if abs(cross_product_1) > epsilon:
            print(f"WARNING: P不在line1上! 叉积: {cross_product_1}")
        
        # 验证Q在line2上
        vec_L2 = self.L2_end - self.L2_start
        vec_Q = self.Q - self.L2_start
        cross_product_2 = np.cross(vec_L2[:2], vec_Q[:2])
        
        if abs(cross_product_2) > epsilon:
            print(f"WARNING: Q不在line2上! 叉积: {cross_product_2}")
        
        print("✓ 几何验证完成")
    
    def create_angle_arc(self, vertex, start_point, end_point, radius=0.4, color=WHITE):
        """创建角度的弧线标记"""
        # 计算两个方向向量
        vec1 = start_point - vertex
        vec2 = end_point - vertex
        
        # 计算起始和结束角度
        angle1 = np.arctan2(vec1[1], vec1[0])
        angle2 = np.arctan2(vec2[1], vec2[0])
        
        # 确保角度在正确的范围内
        if angle2 < angle1:
            angle2 += 2 * PI
        
        # 创建圆弧
        arc = Arc(
            radius=radius,
            start_angle=angle1,
            angle=angle2 - angle1,
            color=color,
            stroke_width=2
        ).move_arc_center_to(vertex)
        
        return arc
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "两条线被一条线截",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        hook_question = Text(
            "会产生几个角?",
            font="Noto Sans CJK SC",
            font_size=44,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 5.2)
        
        self.play(Write(hook_text), run_time=0.8)
        self.play(Write(hook_question), run_time=0.7)
        
        # 简单草图
        sketch_line1 = Line([-2, 1.5, 0], [2, 0.5, 0], color=self.COLOR_LINE_1, stroke_width=3)
        sketch_line2 = Line([-2, -0.5, 0], [2, -1.5, 0], color=self.COLOR_LINE_2, stroke_width=3)
        sketch_line3 = Line([-1.5, -2, 0], [1.5, 2, 0], color=self.COLOR_LINE_3, stroke_width=3)
        
        sketch_group = VGroup(sketch_line1, sketch_line2, sketch_line3).move_to(DOWN * 0.5)
        
        self.play(Create(sketch_group), run_time=1.2)
        
        # 问号闪烁
        question_mark = Text("?", font_size=100, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 3.5)
        self.play(FadeIn(question_mark, scale=0.5), run_time=0.4)
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.8), run_time=0.5)
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(hook_question),
            FadeOut(sketch_group),
            FadeOut(question_mark),
            run_time=0.5
        )
    
    def show_construction(self):
        """场景2: 构建三线八角"""
        # 标题
        title = Text(
            "三线八角模型",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.6)
        
        # Step 1: 被截线1
        explain1 = Text(
            "两条被截线",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        self.play(Create(self.line1), run_time=0.8)
        self.wait(0.3)
        
        # Step 2: 被截线2
        self.play(Create(self.line2), FadeIn(explain1), run_time=0.8)
        self.wait(0.5)
        
        # Step 3: 截线
        explain2 = Text(
            "截线与两条线形成两个交点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        self.play(
            Create(self.line3),
            Transform(explain1, explain2),
            run_time=1.0
        )
        
        # Step 4: 标记交点
        dot_P = Dot(self.P, color=YELLOW, radius=0.08)
        label_P = Text("P", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(dot_P, LEFT, buff=0.15)
        
        dot_Q = Dot(self.Q, color=YELLOW, radius=0.08)
        label_Q = Text("Q", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(dot_Q, LEFT, buff=0.15)
        
        self.play(FadeIn(dot_P), FadeIn(label_P), run_time=0.4)
        self.play(FadeIn(dot_Q), FadeIn(label_Q), run_time=0.4)
        self.wait(0.5)
        
        # Step 5: 标记8个角
        # 在点P处的4个角 (∠1, ∠2, ∠3, ∠4)
        # 在点Q处的4个角 (∠5, ∠6, ∠7, ∠8)
        
        # 计算角的位置
        # P点的角度方向
        vec_P_L1_left = self.L1_start - self.P  # P向L1左方向
        vec_P_L1_right = self.L1_end - self.P   # P向L1右方向
        vec_P_L3_up = self.L3_end - self.P      # P向L3上方向
        vec_P_L3_down = self.L3_start - self.P  # P向L3下方向
        
        # 标准化
        vec_P_L1_left = vec_P_L1_left / np.linalg.norm(vec_P_L1_left) * 0.6
        vec_P_L1_right = vec_P_L1_right / np.linalg.norm(vec_P_L1_right) * 0.6
        vec_P_L3_up = vec_P_L3_up / np.linalg.norm(vec_P_L3_up) * 0.6
        vec_P_L3_down = vec_P_L3_down / np.linalg.norm(vec_P_L3_down) * 0.6
        
        # P点的角平分线方向（用于放置标签）
        dir_angle_1 = (vec_P_L3_up + vec_P_L1_left) / 2
        dir_angle_2 = (vec_P_L1_left + vec_P_L3_down) / 2
        dir_angle_3 = (vec_P_L3_down + vec_P_L1_right) / 2
        dir_angle_4 = (vec_P_L1_right + vec_P_L3_up) / 2
        
        # 创建角度标记（使用更小的圆弧）
        arc_1 = self.create_angle_arc(self.P, self.P + vec_P_L1_left, self.P + vec_P_L3_up, radius=0.35, color=WHITE)
        arc_2 = self.create_angle_arc(self.P, self.P + vec_P_L3_down, self.P + vec_P_L1_left, radius=0.35, color=WHITE)
        arc_3 = self.create_angle_arc(self.P, self.P + vec_P_L1_right, self.P + vec_P_L3_down, radius=0.35, color=WHITE)
        arc_4 = self.create_angle_arc(self.P, self.P + vec_P_L3_up, self.P + vec_P_L1_right, radius=0.35, color=WHITE)
        
        label_1 = MathTex(r"\angle 1", font_size=20, color=WHITE).move_to(self.P + dir_angle_1 * 0.25)
        label_2 = MathTex(r"\angle 2", font_size=20, color=WHITE).move_to(self.P + dir_angle_2 * 0.25)
        label_3 = MathTex(r"\angle 3", font_size=20, color=WHITE).move_to(self.P + dir_angle_3 * 0.25)
        label_4 = MathTex(r"\angle 4", font_size=20, color=WHITE).move_to(self.P + dir_angle_4 * 0.25)
        
        # Q点的角度方向
        vec_Q_L2_left = self.L2_start - self.Q
        vec_Q_L2_right = self.L2_end - self.Q
        vec_Q_L3_up = self.L3_end - self.Q
        vec_Q_L3_down = self.L3_start - self.Q
        
        # 标准化
        vec_Q_L2_left = vec_Q_L2_left / np.linalg.norm(vec_Q_L2_left) * 0.6
        vec_Q_L2_right = vec_Q_L2_right / np.linalg.norm(vec_Q_L2_right) * 0.6
        vec_Q_L3_up = vec_Q_L3_up / np.linalg.norm(vec_Q_L3_up) * 0.6
        vec_Q_L3_down = vec_Q_L3_down / np.linalg.norm(vec_Q_L3_down) * 0.6
        
        # Q点的角平分线方向
        dir_angle_5 = (vec_Q_L3_up + vec_Q_L2_left) / 2
        dir_angle_6 = (vec_Q_L2_left + vec_Q_L3_down) / 2
        dir_angle_7 = (vec_Q_L3_down + vec_Q_L2_right) / 2
        dir_angle_8 = (vec_Q_L2_right + vec_Q_L3_up) / 2
        
        # 创建Q点的角度标记
        arc_5 = self.create_angle_arc(self.Q, self.Q + vec_Q_L2_left, self.Q + vec_Q_L3_up, radius=0.35, color=WHITE)
        arc_6 = self.create_angle_arc(self.Q, self.Q + vec_Q_L3_down, self.Q + vec_Q_L2_left, radius=0.35, color=WHITE)
        arc_7 = self.create_angle_arc(self.Q, self.Q + vec_Q_L2_right, self.Q + vec_Q_L3_down, radius=0.35, color=WHITE)
        arc_8 = self.create_angle_arc(self.Q, self.Q + vec_Q_L3_up, self.Q + vec_Q_L2_right, radius=0.35, color=WHITE)
        
        label_5 = MathTex(r"\angle 5", font_size=20, color=WHITE).move_to(self.Q + dir_angle_5 * 0.25)
        label_6 = MathTex(r"\angle 6", font_size=20, color=WHITE).move_to(self.Q + dir_angle_6 * 0.25)
        label_7 = MathTex(r"\angle 7", font_size=20, color=WHITE).move_to(self.Q + dir_angle_7 * 0.25)
        label_8 = MathTex(r"\angle 8", font_size=20, color=WHITE).move_to(self.Q + dir_angle_8 * 0.25)
        
        # 保存角度元素供后续使用
        self.angle_arcs = [arc_1, arc_2, arc_3, arc_4, arc_5, arc_6, arc_7, arc_8]
        self.angle_labels = [label_1, label_2, label_3, label_4, label_5, label_6, label_7, label_8]
        
        # 依次显示8个角
        for i in range(8):
            self.play(
                Create(self.angle_arcs[i]),
                FadeIn(self.angle_labels[i], scale=0.8),
                run_time=0.3
            )
        
        self.wait(0.3)
        
        # 总结文字
        summary = Text(
            "共形成8个角",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(summary, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explain1),
            FadeOut(summary),
            FadeOut(dot_P),
            FadeOut(label_P),
            FadeOut(dot_Q),
            FadeOut(label_Q),
            run_time=0.6
        )
    
    def show_corresponding_angles(self):
        """场景3: 同位角"""
        # 标题
        title = Text(
            "同位角",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_SAME_SIDE
        ).move_to(UP * 6.5)
        
        english = Text(
            "Corresponding Angles",
            font_size=20,
            color=GRAY_A
        ).next_to(title, DOWN, buff=0.1)
        
        self.play(Write(title), FadeIn(english), run_time=0.7)
        
        # 定义
        definition = Text(
            "在截线同侧，被截两线的同侧",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        position_hint = Text(
            "位置相同的角",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.9)
        
        self.play(FadeIn(definition), run_time=0.5)
        self.play(FadeIn(position_hint), run_time=0.5)
        self.wait(0.5)
        
        # 同位角对: (∠1, ∠5), (∠2, ∠6), (∠3, ∠7), (∠4, ∠8)
        corresponding_pairs = [(0, 4), (1, 5), (2, 6), (3, 7)]
        
        for i, (idx1, idx2) in enumerate(corresponding_pairs):
            # 高亮这一对角
            self.play(
                self.angle_arcs[idx1].animate.set_color(self.COLOR_SAME_SIDE).set_stroke(width=4),
                self.angle_labels[idx1].animate.set_color(self.COLOR_SAME_SIDE).scale(1.3),
                self.angle_arcs[idx2].animate.set_color(self.COLOR_SAME_SIDE).set_stroke(width=4),
                self.angle_labels[idx2].animate.set_color(self.COLOR_SAME_SIDE).scale(1.3),
                run_time=0.5
            )
            
            # 显示说明
            if i == 0:
                pair_label = Text(
                    f"∠{idx1+1} 与 ∠{idx2+1} 同位",
                    font="Noto Sans CJK SC",
                    font_size=22,
                    color=self.COLOR_SAME_SIDE
                ).move_to(DOWN * 4.5)
                self.play(FadeIn(pair_label), run_time=0.4)
            
            self.wait(0.6)
            
            # 恢复原色
            if i < len(corresponding_pairs) - 1:
                self.play(
                    self.angle_arcs[idx1].animate.set_color(WHITE).set_stroke(width=2),
                    self.angle_labels[idx1].animate.set_color(WHITE).scale(1/1.3),
                    self.angle_arcs[idx2].animate.set_color(WHITE).set_stroke(width=2),
                    self.angle_labels[idx2].animate.set_color(WHITE).scale(1/1.3),
                    FadeOut(pair_label) if i == 0 else Wait(0),
                    run_time=0.3
                )
        
        # 总结
        summary_box = Rectangle(
            width=3.5, height=0.8,
            color=self.COLOR_SAME_SIDE,
            fill_opacity=0.2,
            stroke_width=2
        ).move_to(DOWN * 5.5)
        
        summary_text = Text(
            "4对同位角",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_SAME_SIDE,
            weight=BOLD
        ).move_to(summary_box.get_center())
        
        key_point = Text(
            "记忆口诀: 位置相同",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 6.5)
        
        self.play(
            Create(summary_box),
            FadeIn(summary_text),
            run_time=0.6
        )
        self.play(FadeIn(key_point), run_time=0.5)
        self.wait(1.5)
        
        # 清理 - 恢复所有角为白色
        fade_out_group = VGroup(
            title, english, definition, position_hint,
            summary_box, summary_text, key_point
        )
        
        self.play(FadeOut(fade_out_group), run_time=0.5)
        
        # 恢复最后一对角的颜色
        self.play(
            self.angle_arcs[3].animate.set_color(WHITE).set_stroke(width=2),
            self.angle_labels[3].animate.set_color(WHITE).scale(1/1.3),
            self.angle_arcs[7].animate.set_color(WHITE).set_stroke(width=2),
            self.angle_labels[7].animate.set_color(WHITE).scale(1/1.3),
            run_time=0.3
        )
    
    def show_alternate_angles(self):
        """场景4: 内错角"""
        # 标题
        title = Text(
            "内错角",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_ALTERNATE
        ).move_to(UP * 6.5)
        
        english = Text(
            "Alternate Interior Angles",
            font_size=20,
            color=GRAY_A
        ).next_to(title, DOWN, buff=0.1)
        
        self.play(Write(title), FadeIn(english), run_time=0.7)
        
        # 定义
        definition = Text(
            "在截线两侧，被截两线之间",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        position_hint = Text(
            "内部交错的角",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.9)
        
        self.play(FadeIn(definition), run_time=0.5)
        self.play(FadeIn(position_hint), run_time=0.5)
        
        # 标记"内部"区域
        # 内部区域是两条被截线之间的部分
        interior_top = (self.P[1] + self.Q[1]) / 2 + 0.5
        interior_bottom = (self.P[1] + self.Q[1]) / 2 - 0.5
        
        interior_region = Rectangle(
            width=8, height=abs(interior_top - interior_bottom),
            color=self.COLOR_ALTERNATE,
            fill_opacity=0.1,
            stroke_width=0
        ).move_to([0, (interior_top + interior_bottom) / 2, 0])
        
        interior_label = Text(
            "内部区域",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_ALTERNATE
        ).move_to([3.5, (interior_top + interior_bottom) / 2, 0])
        
        self.play(FadeIn(interior_region), FadeIn(interior_label), run_time=0.6)
        self.wait(0.5)
        
        # 内错角对: (∠3, ∠5), (∠4, ∠6)
        alternate_pairs = [(2, 4), (3, 5)]
        
        for i, (idx1, idx2) in enumerate(alternate_pairs):
            # 高亮这一对角
            self.play(
                self.angle_arcs[idx1].animate.set_color(self.COLOR_ALTERNATE).set_stroke(width=4),
                self.angle_labels[idx1].animate.set_color(self.COLOR_ALTERNATE).scale(1.3),
                self.angle_arcs[idx2].animate.set_color(self.COLOR_ALTERNATE).set_stroke(width=4),
                self.angle_labels[idx2].animate.set_color(self.COLOR_ALTERNATE).scale(1.3),
                run_time=0.5
            )
            
            # Z字形示意（第一对时显示）
            if i == 0:
                # 创建Z字形路径
                z_path = VMobject(color=self.COLOR_ALTERNATE, stroke_width=3)
                z_path.set_points_as_corners([
                    self.P + (self.L1_end - self.P) / np.linalg.norm(self.L1_end - self.P) * 0.8,
                    self.P,
                    self.Q,
                    self.Q + (self.L2_start - self.Q) / np.linalg.norm(self.L2_start - self.Q) * 0.8
                ])
                
                pair_label = Text(
                    f"∠{idx1+1} 与 ∠{idx2+1} 内错",
                    font="Noto Sans CJK SC",
                    font_size=22,
                    color=self.COLOR_ALTERNATE
                ).move_to(DOWN * 4.5)
                
                self.play(Create(z_path), FadeIn(pair_label), run_time=0.6)
                self.wait(0.8)
                self.play(FadeOut(z_path), FadeOut(pair_label), run_time=0.3)
            
            self.wait(0.6)
            
            # 恢复原色
            if i < len(alternate_pairs) - 1:
                self.play(
                    self.angle_arcs[idx1].animate.set_color(WHITE).set_stroke(width=2),
                    self.angle_labels[idx1].animate.set_color(WHITE).scale(1/1.3),
                    self.angle_arcs[idx2].animate.set_color(WHITE).set_stroke(width=2),
                    self.angle_labels[idx2].animate.set_color(WHITE).scale(1/1.3),
                    run_time=0.3
                )
        
        # 总结
        summary_box = Rectangle(
            width=3.5, height=0.8,
            color=self.COLOR_ALTERNATE,
            fill_opacity=0.2,
            stroke_width=2
        ).move_to(DOWN * 5.5)
        
        summary_text = Text(
            "2对内错角",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_ALTERNATE,
            weight=BOLD
        ).move_to(summary_box.get_center())
        
        key_point = Text(
            "记忆口诀: 内部交错",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 6.5)
        
        self.play(
            Create(summary_box),
            FadeIn(summary_text),
            run_time=0.6
        )
        self.play(FadeIn(key_point), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        fade_out_group = VGroup(
            title, english, definition, position_hint,
            interior_region, interior_label,
            summary_box, summary_text, key_point
        )
        
        self.play(FadeOut(fade_out_group), run_time=0.5)
        
        # 恢复最后一对角的颜色
        self.play(
            self.angle_arcs[3].animate.set_color(WHITE).set_stroke(width=2),
            self.angle_labels[3].animate.set_color(WHITE).scale(1/1.3),
            self.angle_arcs[5].animate.set_color(WHITE).set_stroke(width=2),
            self.angle_labels[5].animate.set_color(WHITE).scale(1/1.3),
            run_time=0.3
        )
    
    def show_consecutive_angles(self):
        """场景5: 同旁内角"""
        # 标题
        title = Text(
            "同旁内角",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_CONSECUTIVE
        ).move_to(UP * 6.5)
        
        english = Text(
            "Consecutive Interior Angles",
            font_size=20,
            color=GRAY_A
        ).next_to(title, DOWN, buff=0.1)
        
        self.play(Write(title), FadeIn(english), run_time=0.7)
        
        # 定义
        definition = Text(
            "在截线同侧，被截两线之间",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        position_hint = Text(
            "同侧内部的角",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.9)
        
        self.play(FadeIn(definition), run_time=0.5)
        self.play(FadeIn(position_hint), run_time=0.5)
        
        # 标记"内部"区域
        interior_top = (self.P[1] + self.Q[1]) / 2 + 0.5
        interior_bottom = (self.P[1] + self.Q[1]) / 2 - 0.5
        
        interior_region = Rectangle(
            width=8, height=abs(interior_top - interior_bottom),
            color=self.COLOR_CONSECUTIVE,
            fill_opacity=0.1,
            stroke_width=0
        ).move_to([0, (interior_top + interior_bottom) / 2, 0])
        
        self.play(FadeIn(interior_region), run_time=0.6)
        self.wait(0.5)
        
        # 同旁内角对: (∠3, ∠6), (∠4, ∠5)
        consecutive_pairs = [(2, 5), (3, 4)]
        
        for i, (idx1, idx2) in enumerate(consecutive_pairs):
            # 高亮这一对角
            self.play(
                self.angle_arcs[idx1].animate.set_color(self.COLOR_CONSECUTIVE).set_stroke(width=4),
                self.angle_labels[idx1].animate.set_color(self.COLOR_CONSECUTIVE).scale(1.3),
                self.angle_arcs[idx2].animate.set_color(self.COLOR_CONSECUTIVE).set_stroke(width=4),
                self.angle_labels[idx2].animate.set_color(self.COLOR_CONSECUTIVE).scale(1.3),
                run_time=0.5
            )
            
            # U字形示意（第一对时显示）
            if i == 0:
                # 创建U字形路径
                u_path = VMobject(color=self.COLOR_CONSECUTIVE, stroke_width=3)
                u_path.set_points_as_corners([
                    self.P + (self.L1_end - self.P) / np.linalg.norm(self.L1_end - self.P) * 0.8,
                    self.P,
                    self.Q,
                    self.Q + (self.L2_end - self.Q) / np.linalg.norm(self.L2_end - self.Q) * 0.8
                ])
                
                # 说明文字 - 注意使用Text和MathTex组合
                pair_text = Text(
                    f"∠{idx1+1} 与 ∠{idx2+1} 同旁内角",
                    font="Noto Sans CJK SC",
                    font_size=22,
                    color=self.COLOR_CONSECUTIVE
                ).move_to(DOWN * 4.5)
                
                self.play(Create(u_path), FadeIn(pair_text), run_time=0.6)
                self.wait(0.8)
                self.play(FadeOut(u_path), FadeOut(pair_text), run_time=0.3)
            
            self.wait(0.6)
            
            # 恢复原色
            if i < len(consecutive_pairs) - 1:
                self.play(
                    self.angle_arcs[idx1].animate.set_color(WHITE).set_stroke(width=2),
                    self.angle_labels[idx1].animate.set_color(WHITE).scale(1/1.3),
                    self.angle_arcs[idx2].animate.set_color(WHITE).set_stroke(width=2),
                    self.angle_labels[idx2].animate.set_color(WHITE).scale(1/1.3),
                    run_time=0.3
                )
        
        # 总结
        summary_box = Rectangle(
            width=3.5, height=0.8,
            color=self.COLOR_CONSECUTIVE,
            fill_opacity=0.2,
            stroke_width=2
        ).move_to(DOWN * 5.5)
        
        summary_text = Text(
            "2对同旁内角",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_CONSECUTIVE,
            weight=BOLD
        ).move_to(summary_box.get_center())
        
        key_point = Text(
            "记忆口诀: 同侧内部",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 6.5)
        
        self.play(
            Create(summary_box),
            FadeIn(summary_text),
            run_time=0.6
        )
        self.play(FadeIn(key_point), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        fade_out_group = VGroup(
            title, english, definition, position_hint,
            interior_region,
            summary_box, summary_text, key_point
        )
        
        self.play(FadeOut(fade_out_group), run_time=0.5)
        
        # 恢复最后一对角的颜色
        self.play(
            self.angle_arcs[3].animate.set_color(WHITE).set_stroke(width=2),
            self.angle_labels[3].animate.set_color(WHITE).scale(1/1.3),
            self.angle_arcs[4].animate.set_color(WHITE).set_stroke(width=2),
            self.angle_labels[4].animate.set_color(WHITE).scale(1/1.3),
            run_time=0.3
        )
    
    def show_summary(self):
        """场景6: 知识总结"""
        # 标题
        title = Text(
            "三线八角 - 知识总结",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 7)
        
        self.play(Write(title), run_time=0.6)
        
        # 将三条线和角度标记缩小并移至上方
        lines_group = VGroup(self.line1, self.line2, self.line3)
        angles_group = VGroup(*self.angle_arcs, *self.angle_labels)
        all_geometry = VGroup(lines_group, angles_group)
        
        self.play(
            all_geometry.animate.scale(0.5).move_to(UP * 5),
            run_time=0.8
        )
        
        # 三张卡片
        card_y_start = 2.5
        card_spacing = 1.8
        
        # 卡片1: 同位角
        card1 = self.create_summary_card(
            "同位角",
            "4对",
            "位置相同",
            self.COLOR_SAME_SIDE,
            UP * card_y_start
        )
        
        # 卡片2: 内错角
        card2 = self.create_summary_card(
            "内错角",
            "2对",
            "内部交错",
            self.COLOR_ALTERNATE,
            UP * (card_y_start - card_spacing)
        )
        
        # 卡片3: 同旁内角
        card3 = self.create_summary_card(
            "同旁内角",
            "2对",
            "同侧内部",
            self.COLOR_CONSECUTIVE,
            UP * (card_y_start - 2 * card_spacing)
        )
        
        # 卡片从左侧滑入
        for card in [card1, card2, card3]:
            card.shift(LEFT * 10)
        
        self.play(card1.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.2)
        self.play(card2.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.2)
        self.play(card3.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.5)
        
        # 记忆口诀
        mnemonic_title = Text(
            "记忆口诀:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 2.5 + LEFT * 1.5)
        
        mnemonic_content = Text(
            "位置相同、内部交错、同侧内部",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).next_to(mnemonic_title, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(mnemonic_title),
            FadeIn(mnemonic_content),
            run_time=0.7
        )
        self.wait(0.8)
        
        # 应用提示
        application = Text(
            "三线八角是平行线判定与性质的基础",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(application, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)
        
        # 全部闪烁
        self.play(
            Flash(card1, color=self.COLOR_SAME_SIDE),
            Flash(card2, color=self.COLOR_ALTERNATE),
            Flash(card3, color=self.COLOR_CONSECUTIVE),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(all_geometry),
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(card3),
            FadeOut(mnemonic_title),
            FadeOut(mnemonic_content),
            FadeOut(application),
            run_time=0.8
        )
    
    def create_summary_card(self, title, count, mnemonic, color, position):
        """创建总结卡片"""
        # 图标
        icon = Circle(radius=0.25, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE,
            weight=BOLD
        )
        
        # 数量
        count_text = Text(
            count,
            font="Noto Sans CJK SC",
            font_size=22,
            color=color
        )
        
        # 口诀
        mnemonic_text = Text(
            mnemonic,
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        )
        
        # 组合
        card_content = VGroup(
            VGroup(title_text, count_text).arrange(RIGHT, buff=0.3),
            mnemonic_text
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        
        card = VGroup(icon, card_content).arrange(RIGHT, buff=0.4)
        card.move_to(position)
        
        return card
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=44,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 几何图标装饰
        icon_size = 0.4
        icons = VGroup(
            # 角度符号
            Arc(radius=icon_size, start_angle=0, angle=PI/3, color=self.COLOR_SAME_SIDE, stroke_width=4).shift(LEFT * 2.5),
            Arc(radius=icon_size, start_angle=0, angle=PI/2, color=self.COLOR_ALTERNATE, stroke_width=4).shift(LEFT * 1.2),
            Arc(radius=icon_size, start_angle=0, angle=2*PI/3, color=self.COLOR_CONSECUTIVE, stroke_width=4),
            Arc(radius=icon_size, start_angle=0, angle=PI/4, color=GOLD, stroke_width=4).shift(RIGHT * 1.2),
            Arc(radius=icon_size, start_angle=0, angle=PI/3, color=BLUE, stroke_width=4).shift(RIGHT * 2.5)
        ).move_to(DOWN * 2.5)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        self.play(Rotate(icons, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql three_lines_eight_angles.py ThreeLinesEightAngles  # 快速预览
# manim -qh three_lines_eight_angles.py ThreeLinesEightAngles   # 高质量渲染