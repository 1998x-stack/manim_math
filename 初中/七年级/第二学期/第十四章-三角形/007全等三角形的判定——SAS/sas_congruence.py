"""
SAS全等判定教学动画
使用 Manim 创建的中学几何教学视频

内容: SAS（边角边）全等判定法则
目标观众: 七年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

知识点:
- 两边及其夹角分别对应相等的两个三角形全等
- 强调"夹角"的重要性
- 警告SSA不能判定全等
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class SASCongruence(Scene):
    """
    SAS全等判定教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 引入SAS概念
    3. 标记第一条边AB=DE
    4. 标记夹角∠A=∠D
    5. 标记第二条边AC=DF
    6. 重合验证
    7. SSA错误示例
    8. 片尾总结
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_TRIANGLE_1 = "#3498db"      # 蓝色 - 第一个三角形
        self.COLOR_TRIANGLE_2 = "#e74c3c"      # 红色 - 第二个三角形
        self.COLOR_HIGHLIGHT = YELLOW          # 高亮颜色
        self.COLOR_EQUAL_MARK = "#2ecc71"      # 绿色 - 相等标记
        self.COLOR_ANGLE_MARK = "#f39c12"      # 橙色 - 角度标记
        self.COLOR_AUXILIARY = GRAY_B          # 辅助线
        self.COLOR_WRONG = "#c0392b"           # 错误示例红色
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_introduce_sas()
        self.scene_3_mark_first_side()
        self.scene_4_mark_angle()
        self.scene_5_mark_second_side()
        self.scene_6_overlap_verification()
        self.scene_7_ssa_warning()
        self.scene_8_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据"""
        # 基准参数
        self.SCALE = 0.85
        self.OFFSET = UP * 1.5
        
        # 三角形ABC（蓝色）- 左侧
        # 使用等腰直角三角形便于展示
        base_A = np.array([-2.5, 0, 0])
        base_B = np.array([2.5, 0, 0])
        base_C = np.array([0, 2.5, 0])
        
        left_shift = LEFT * 2.5
        
        self.A1 = base_A * self.SCALE + self.OFFSET + left_shift
        self.B1 = base_B * self.SCALE + self.OFFSET + left_shift
        self.C1 = base_C * self.SCALE + self.OFFSET + left_shift
        
        # 计算边长
        self.AB1 = np.linalg.norm(self.B1 - self.A1)
        self.AC1 = np.linalg.norm(self.C1 - self.A1)
        self.BC1 = np.linalg.norm(self.C1 - self.B1)
        
        # 计算角度
        self.angle_A1 = self.calc_angle(self.B1, self.A1, self.C1)
        
        # 三角形DEF（红色）- 右侧
        # 使用SAS构造: DE = AB, ∠D = ∠A, DF = AC
        right_shift = RIGHT * 2.5
        base_D = np.array([0.5, -2.5, 0])
        
        self.D = base_D * self.SCALE + self.OFFSET + right_shift
        
        # 构造E点: 使DE = AB1，水平向右
        DE_direction = np.array([1, 0, 0])
        self.E = self.D + DE_direction * self.AB1
        
        # 构造F点: 使DF = AC1, 且∠D = ∠A
        DF_direction = self.rotate_vector(DE_direction, self.angle_A1)
        self.F = self.D + DF_direction * self.AC1
        
        # 创建三角形对象（初始不添加）
        self.triangle_ABC = Polygon(
            self.A1, self.B1, self.C1,
            color=self.COLOR_TRIANGLE_1,
            stroke_width=3
        )
        
        self.triangle_DEF = Polygon(
            self.D, self.E, self.F,
            color=self.COLOR_TRIANGLE_2,
            stroke_width=3
        )
        
        # 验证几何
        self.verify_geometry()
    
    @staticmethod
    def calc_angle(point1, vertex, point2):
        """计算从vertex指向point1和point2的两条射线之间的夹角（弧度）"""
        v1 = point1 - vertex
        v2 = point2 - vertex
        
        v1_norm = np.linalg.norm(v1)
        v2_norm = np.linalg.norm(v2)
        
        if v1_norm < 1e-10 or v2_norm < 1e-10:
            return 0.0
        
        v1_unit = v1 / v1_norm
        v2_unit = v2 / v2_norm
        
        cos_angle = np.dot(v1_unit, v2_unit)
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        
        return np.arccos(cos_angle)
    
    @staticmethod
    def rotate_vector(vec, angle):
        """将2D向量旋转angle弧度（逆时针）"""
        cos_a = np.cos(angle)
        sin_a = np.sin(angle)
        
        rotation_matrix = np.array([
            [cos_a, -sin_a, 0],
            [sin_a, cos_a, 0],
            [0, 0, 1]
        ])
        
        return rotation_matrix @ vec
    
    def verify_geometry(self):
        """验证几何计算"""
        epsilon = 1e-6
        
        # 验证DE和AB
        DE = np.linalg.norm(self.E - self.D)
        assert abs(self.AB1 - DE) < epsilon, f"AB ≠ DE: {self.AB1} ≠ {DE}"
        
        # 验证DF和AC
        DF = np.linalg.norm(self.F - self.D)
        assert abs(self.AC1 - DF) < epsilon, f"AC ≠ DF: {self.AC1} ≠ {DF}"
        
        # 验证角度
        angle_D = self.calc_angle(self.E, self.D, self.F)
        assert abs(self.angle_A1 - angle_D) < epsilon, f"∠A ≠ ∠D"
        
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
        hook = Text(
            "两个三角形什么时候全等？",
            font="PingFang SC",
            font_size=40,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook), run_time=1.0)
        self.wait(0.5)
        
        # 三角形淡入
        self.play(
            Create(self.triangle_ABC),
            Create(self.triangle_DEF),
            run_time=1.5
        )
        
        # 顶点标签
        label_A = Text("A", font="PingFang SC", font_size=20, color=WHITE).next_to(self.A1, DL, buff=0.15)
        label_B = Text("B", font="PingFang SC", font_size=20, color=WHITE).next_to(self.B1, DR, buff=0.15)
        label_C = Text("C", font="PingFang SC", font_size=20, color=WHITE).next_to(self.C1, UP, buff=0.15)
        
        label_D = Text("D", font="PingFang SC", font_size=20, color=WHITE).next_to(self.D, DL, buff=0.15)
        label_E = Text("E", font="PingFang SC", font_size=20, color=WHITE).next_to(self.E, DR, buff=0.15)
        label_F = Text("F", font="PingFang SC", font_size=20, color=WHITE).next_to(self.F, UP, buff=0.15)
        
        self.labels_ABC = VGroup(label_A, label_B, label_C)
        self.labels_DEF = VGroup(label_D, label_E, label_F)
        
        self.play(
            FadeIn(self.labels_ABC),
            FadeIn(self.labels_DEF),
            run_time=0.5
        )
        
        self.wait(0.8)
        
        # 清理钩子
        self.play(FadeOut(hook), run_time=0.5)
    
    def scene_2_introduce_sas(self):
        """场景2: 引入SAS概念"""
        # 标题
        title = Text(
            "SAS 判定法则",
            font="PingFang SC",
            font_size=42,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义
        definition = VGroup(
            Text("边", font="PingFang SC", font_size=28, color=self.COLOR_EQUAL_MARK),
            Text("-", font="PingFang SC", font_size=28, color=WHITE),
            Text("角", font="PingFang SC", font_size=28, color=self.COLOR_ANGLE_MARK),
            Text("-", font="PingFang SC", font_size=28, color=WHITE),
            Text("边", font="PingFang SC", font_size=28, color=self.COLOR_EQUAL_MARK)
        ).arrange(RIGHT, buff=0.15).move_to(UP * 4.5)
        
        self.play(FadeIn(definition), run_time=0.6)
        
        # 说明文字
        explanation = Text(
            "两边及其夹角分别对应相等",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 3.8)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 强调"夹角"
        emphasis = Text(
            "关键: 必须是夹角！",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 3.1)
        
        self.play(Write(emphasis), run_time=0.6)
        self.play(Indicate(emphasis, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        # 数学公式
        formula = MathTex(
            r"AB", r"=", r"DE", r",\,",
            r"\angle A", r"=", r"\angle D", r",\,",
            r"AC", r"=", r"DF",
            r"\Rightarrow",
            r"\triangle ABC \cong \triangle DEF"
        ).scale(0.8).move_to(UP * 2.2)
        
        # 着色
        formula[0].set_color(self.COLOR_EQUAL_MARK)   # AB
        formula[2].set_color(self.COLOR_EQUAL_MARK)   # DE
        formula[4].set_color(self.COLOR_ANGLE_MARK)   # ∠A
        formula[6].set_color(self.COLOR_ANGLE_MARK)   # ∠D
        formula[8].set_color(self.COLOR_EQUAL_MARK)   # AC
        formula[10].set_color(self.COLOR_EQUAL_MARK)  # DF
        
        self.play(Write(formula), run_time=1.2)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(explanation),
            FadeOut(emphasis),
            FadeOut(formula),
            run_time=0.6
        )
    
    def scene_3_mark_first_side(self):
        """场景3: 标记第一条边AB=DE"""
        # 步骤标题
        step_title = Text(
            "① 第一条边",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_EQUAL_MARK
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.5)
        
        # 高亮AB边
        line_AB = Line(self.A1, self.B1, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        self.play(Create(line_AB), run_time=0.5)
        
        # 高亮DE边
        line_DE = Line(self.D, self.E, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        self.play(Create(line_DE), run_time=0.5)
        
        # 相等标记（单短线）
        mark_AB = self.create_equal_mark(self.A1, self.B1, num_marks=1, color=self.COLOR_EQUAL_MARK)
        mark_DE = self.create_equal_mark(self.D, self.E, num_marks=1, color=self.COLOR_EQUAL_MARK)
        
        self.play(
            Create(mark_AB),
            Create(mark_DE),
            run_time=0.6
        )
        
        # 长度标注
        length_text = Text(
            f"AB = DE = {self.AB1:.2f}",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(length_text), run_time=0.5)
        self.wait(1.5)
        
        # 清理高亮但保留标记
        self.play(
            FadeOut(line_AB),
            FadeOut(line_DE),
            FadeOut(length_text),
            FadeOut(step_title),
            run_time=0.5
        )
        
        # 保存标记以备后用
        self.marks_AB = mark_AB
        self.marks_DE = mark_DE
    
    def scene_4_mark_angle(self):
        """场景4: 标记夹角∠A=∠D"""
        # 步骤标题
        step_title = Text(
            "② 夹角",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_ANGLE_MARK,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.5)
        
        # 创建角度弧 - 注意方向
        # 根据verify_geometry.py的警告，∠B需要other_angle=True
        angle_A = Angle.from_three_points(
            self.B1, self.A1, self.C1,
            radius=0.5,
            color=self.COLOR_ANGLE_MARK,
            stroke_width=3
        )
        
        angle_D = Angle.from_three_points(
            self.E, self.D, self.F,
            radius=0.5,
            color=self.COLOR_ANGLE_MARK,
            stroke_width=3
        )
        
        self.play(
            Create(angle_A),
            Create(angle_D),
            run_time=1.0
        )
        
        # 角度标记（单弧线）
        arc_mark_A = Arc(
            radius=0.35,
            start_angle=0,
            angle=self.angle_A1,
            color=self.COLOR_ANGLE_MARK,
            stroke_width=2
        ).move_arc_center_to(self.A1)
        
        arc_mark_D = Arc(
            radius=0.35,
            start_angle=0,
            angle=self.angle_A1,
            color=self.COLOR_ANGLE_MARK,
            stroke_width=2
        ).move_arc_center_to(self.D)
        
        self.play(
            Create(arc_mark_A),
            Create(arc_mark_D),
            run_time=0.6
        )
        
        # 角度值标注
        angle_deg = np.degrees(self.angle_A1)
        angle_text = MathTex(
            r"\angle A = \angle D = " + f"{angle_deg:.0f}^\\circ"
        ).scale(0.8).move_to(DOWN * 5)
        
        self.play(FadeIn(angle_text), run_time=0.5)
        
        # 强调"夹角"
        emphasis = Text(
            "这是AB和AC的夹角！",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6)
        
        self.play(Write(emphasis), run_time=0.6)
        self.play(Flash(emphasis, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(angle_A),
            FadeOut(angle_D),
            FadeOut(angle_text),
            FadeOut(emphasis),
            FadeOut(step_title),
            run_time=0.5
        )
        
        # 保存角度标记
        self.arc_mark_A = arc_mark_A
        self.arc_mark_D = arc_mark_D
    
    def scene_5_mark_second_side(self):
        """场景5: 标记第二条边AC=DF"""
        # 步骤标题
        step_title = Text(
            "③ 第二条边",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_EQUAL_MARK
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.5)
        
        # 高亮AC边
        line_AC = Line(self.A1, self.C1, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        self.play(Create(line_AC), run_time=0.5)
        
        # 高亮DF边
        line_DF = Line(self.D, self.F, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        self.play(Create(line_DF), run_time=0.5)
        
        # 相等标记（双短线，区别于AB）
        mark_AC = self.create_equal_mark(self.A1, self.C1, num_marks=2, color=self.COLOR_EQUAL_MARK)
        mark_DF = self.create_equal_mark(self.D, self.F, num_marks=2, color=self.COLOR_EQUAL_MARK)
        
        self.play(
            Create(mark_AC),
            Create(mark_DF),
            run_time=0.6
        )
        
        # 长度标注
        length_text = Text(
            f"AC = DF = {self.AC1:.2f}",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(length_text), run_time=0.5)
        
        # SAS汇总
        summary = VGroup(
            Text("✓ 两边: AB=DE, AC=DF", font="PingFang SC", font_size=22, color=self.COLOR_EQUAL_MARK),
            Text("✓ 夹角: ∠A=∠D", font="PingFang SC", font_size=22, color=self.COLOR_ANGLE_MARK),
            Text("∴ △ABC ≌ △DEF (SAS)", font="PingFang SC", font_size=24, color=GOLD, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(DOWN * 6.2)
        
        self.play(FadeIn(summary, shift=UP * 0.3), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(line_AC),
            FadeOut(line_DF),
            FadeOut(length_text),
            FadeOut(summary),
            FadeOut(step_title),
            run_time=0.6
        )
        
        # 保存标记
        self.marks_AC = mark_AC
        self.marks_DF = mark_DF
    
    def scene_6_overlap_verification(self):
        """场景6: 重合验证"""
        # 标题
        title = Text(
            "验证: 完美重合",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 复制triangle_DEF
        triangle_copy = self.triangle_DEF.copy()
        triangle_copy.set_stroke(color=self.COLOR_TRIANGLE_2, width=4, opacity=0.8)
        
        # 计算变换：先旋转再平移
        # 需要让D与A1重合，E与B1重合
        
        # 计算旋转角度（从DE方向到AB方向）
        vec_DE = self.E - self.D
        vec_AB = self.B1 - self.A1
        
        angle_DE = np.arctan2(vec_DE[1], vec_DE[0])
        angle_AB = np.arctan2(vec_AB[1], vec_AB[0])
        rotation_angle = angle_AB - angle_DE
        
        # 先绕D点旋转
        self.play(
            Rotate(triangle_copy, rotation_angle, about_point=self.D),
            run_time=1.2
        )
        
        # 再平移到A1
        translation = self.A1 - self.D
        self.play(
            triangle_copy.animate.shift(translation),
            run_time=1.5
        )
        
        # 调整透明度显示重合
        self.play(
            triangle_copy.animate.set_fill(opacity=0.3),
            run_time=0.6
        )
        
        # 全等符号
        congruence = MathTex(
            r"\triangle ABC \cong \triangle DEF",
            font_size=48,
            color=GOLD
        ).move_to(DOWN * 5)
        
        self.play(Write(congruence), run_time=0.8)
        self.play(Flash(congruence, color=GOLD, flash_radius=0.8), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(triangle_copy),
            FadeOut(congruence),
            FadeOut(title),
            FadeOut(self.marks_AB),
            FadeOut(self.marks_DE),
            FadeOut(self.marks_AC),
            FadeOut(self.marks_DF),
            FadeOut(self.arc_mark_A),
            FadeOut(self.arc_mark_D),
            run_time=0.6
        )
    
    def scene_7_ssa_warning(self):
        """场景7: SSA错误示例"""
        # 清理现有三角形
        self.play(
            FadeOut(self.triangle_ABC),
            FadeOut(self.triangle_DEF),
            FadeOut(self.labels_ABC),
            FadeOut(self.labels_DEF),
            run_time=0.5
        )
        
        # 警告标题
        warning_title = Text(
            "⚠️ 注意：SSA 不能判定全等！",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_WRONG,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(warning_title), run_time=0.8)
        self.play(Indicate(warning_title, color=self.COLOR_WRONG), run_time=0.6)
        
        # 说明
        explanation = Text(
            "边-边-角 的顺序",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        # SSA示例 - 构造反例
        # 相同的两边和一个非夹角，可能有两个不同的三角形
        
        # 第一个三角形
        P1 = np.array([-3, 0, 0])
        Q1 = np.array([3, 0, 0])
        R1 = np.array([0, 2.5, 0])
        
        tri_1 = Polygon(P1, Q1, R1, color=self.COLOR_TRIANGLE_1, stroke_width=3)
        
        # 第二个三角形（不同的R点位置）
        R2 = np.array([0, 1.0, 0])
        tri_2 = Polygon(P1, Q1, R2, color=self.COLOR_WRONG, stroke_width=3)
        
        self.play(Create(tri_1), run_time=0.8)
        self.play(Create(tri_2), run_time=0.8)
        
        # 标记相同的边和角
        # PQ边相同
        mark_PQ = self.create_equal_mark(P1, Q1, num_marks=1, color=self.COLOR_EQUAL_MARK, offset=0.3)
        
        # PR边相同
        PR1_len = np.linalg.norm(R1 - P1)
        # 在tri_2上也标记相同长度
        mark_PR1 = self.create_equal_mark(P1, R1, num_marks=2, color=self.COLOR_EQUAL_MARK)
        mark_PR2 = self.create_equal_mark(P1, R2, num_marks=2, color=self.COLOR_EQUAL_MARK)
        
        self.play(
            Create(mark_PQ),
            Create(mark_PR1),
            Create(mark_PR2),
            run_time=0.6
        )
        
        # 强调非夹角
        wrong_angle_text = Text(
            "∠Q 不是 PQ 和 PR 的夹角！",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_WRONG
        ).move_to(DOWN * 4)
        
        wrong_result = Text(
            "→ 两个不同的三角形！",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_WRONG,
            weight=BOLD
        ).move_to(DOWN * 5)
        
        self.play(
            FadeIn(wrong_angle_text),
            FadeIn(wrong_result),
            run_time=0.8
        )
        
        # 闪烁两个三角形的不同
        self.play(
            tri_1.animate.set_stroke(color=YELLOW),
            run_time=0.3
        )
        self.play(
            tri_1.animate.set_stroke(color=self.COLOR_TRIANGLE_1),
            tri_2.animate.set_stroke(color=YELLOW),
            run_time=0.3
        )
        self.play(
            tri_2.animate.set_stroke(color=self.COLOR_WRONG),
            run_time=0.3
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(warning_title),
            FadeOut(explanation),
            FadeOut(tri_1),
            FadeOut(tri_2),
            FadeOut(mark_PQ),
            FadeOut(mark_PR1),
            FadeOut(mark_PR2),
            FadeOut(wrong_angle_text),
            FadeOut(wrong_result),
            run_time=0.6
        )
    
    def scene_8_outro(self):
        """场景8: 片尾总结"""
        # 核心要点
        key_points = VGroup(
            Text("SAS 判定要点:", font="PingFang SC", font_size=32, color=GOLD, weight=BOLD),
            Text("", font_size=8),  # 空行
            Text("✓ 两边对应相等", font="PingFang SC", font_size=26, color=self.COLOR_EQUAL_MARK),
            Text("✓ 夹角对应相等", font="PingFang SC", font_size=26, color=self.COLOR_ANGLE_MARK),
            Text("✓ 顺序: 边-角-边", font="PingFang SC", font_size=26, color=WHITE),
            Text("✗ SSA 不能判定全等", font="PingFang SC", font_size=26, color=self.COLOR_WRONG)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(UP * 2)
        
        self.play(FadeIn(key_points, shift=UP * 0.5), run_time=1.0)
        self.wait(2.0)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 3)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，轻松掌握几何！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(follow_text, scale=1.1), run_time=0.6)
        
        # 装饰三角形
        triangles = VGroup(*[
            Polygon(
                ORIGIN,
                RIGHT * 0.3,
                UP * 0.3,
                color=GOLD,
                fill_opacity=0.6,
                stroke_width=0
            ).scale(0.4).move_to(
                follow_text.get_center() + 
                1.8 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles],
            run_time=0.6
        )
        self.play(Rotate(triangles, angle=PI/3, run_time=1.5))
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(key_points),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles),
            run_time=1.0
        )
    
    def create_equal_mark(self, point1, point2, num_marks=1, color=GREEN, offset=0.2):
        """
        创建相等标记（短线）
        num_marks: 短线数量（1表示=, 2表示==）
        """
        midpoint = (point1 + point2) / 2
        
        # 计算垂直方向
        vec = point2 - point1
        perp = np.array([-vec[1], vec[0], 0])
        perp_unit = perp / np.linalg.norm(perp)
        
        # 标记长度
        mark_length = 0.15
        
        marks = VGroup()
        
        if num_marks == 1:
            # 单短线
            line = Line(
                midpoint - perp_unit * mark_length / 2,
                midpoint + perp_unit * mark_length / 2,
                color=color,
                stroke_width=3
            )
            marks.add(line)
        else:
            # 多短线
            spacing = 0.08
            for i in range(num_marks):
                offset_vec = perp_unit * ((i - (num_marks - 1) / 2) * spacing)
                parallel_offset = (point2 - point1) / np.linalg.norm(point2 - point1) * offset
                
                start = midpoint + offset_vec - perp_unit * mark_length / 2 + parallel_offset * 0.05 * i
                end = midpoint + offset_vec + perp_unit * mark_length / 2 + parallel_offset * 0.05 * i
                
                line = Line(start, end, color=color, stroke_width=3)
                marks.add(line)
        
        return marks


# 运行命令:
# manim -pql sas_congruence.py SASCongruence  # 快速预览 480p
# manim -qh sas_congruence.py SASCongruence   # 高质量 1080p
# manim -qk sas_congruence.py SASCongruence   # 4K质量
