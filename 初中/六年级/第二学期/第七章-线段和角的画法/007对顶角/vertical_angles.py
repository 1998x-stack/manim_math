"""
对顶角教学动画 - Vertical Angles Teaching Animation
使用 Manim 创建的六年级几何教学视频

内容: 对顶角的定义、性质和简单证明
目标观众: 六年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np
from math import pi, sin, cos, atan2


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class VerticalAngles(Scene):
    """
    对顶角教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 引入相交线
    3. 引入四个角
    4. 对顶角定义
    5. 对顶角性质 - 测量
    6. 对顶角性质 - 证明思路
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_LINE1 = "#3498db"        # 蓝色 - 第一条直线
        self.COLOR_LINE2 = "#e74c3c"        # 红色 - 第二条直线
        self.COLOR_ANGLE1 = "#f39c12"       # 橙色 - ∠1
        self.COLOR_ANGLE2 = "#9b59b6"       # 紫色 - ∠2
        self.COLOR_ANGLE3 = "#2ecc71"       # 绿色 - ∠3
        self.COLOR_ANGLE4 = "#e67e22"       # 深橙色 - ∠4
        self.COLOR_HIGHLIGHT = YELLOW       # 高亮色
        self.COLOR_AUXILIARY = GRAY_B       # 辅助色
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_intersecting_lines()
        self.scene_3_four_angles()
        self.scene_4_vertical_angle_definition()
        self.scene_5_vertical_angle_property()
        self.scene_6_proof_idea()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化几何元素和精确计算所有坐标"""
        # 交点位置（画面中心偏上）
        self.O = np.array([0, 1.5, 0])
        
        # 两条直线的方向（使用60度交叉角）
        angle1 = 30 * DEGREES  # 第一条直线相对于水平线的角度
        angle2 = -30 * DEGREES  # 第二条直线相对于水平线的角度
        
        # 直线长度
        line_length = 4.0
        
        # 计算第一条直线的两个端点
        dir1 = np.array([cos(angle1), sin(angle1), 0])
        self.A1 = self.O + dir1 * line_length
        self.A2 = self.O - dir1 * line_length
        
        # 计算第二条直线的两个端点
        dir2 = np.array([cos(angle2), sin(angle2), 0])
        self.B1 = self.O + dir2 * line_length
        self.B2 = self.O - dir2 * line_length
        
        # 计算四个角的精确角度（弧度）
        # ∠1: 从A1方向到B1方向（逆时针）
        vec_A1 = self.A1 - self.O
        vec_B1 = self.B1 - self.O
        vec_A2 = self.A2 - self.O
        vec_B2 = self.B2 - self.O
        
        # 角度计算（使用atan2获取精确角度）
        self.angle1_start = atan2(vec_A1[1], vec_A1[0])
        self.angle1_end = atan2(vec_B1[1], vec_B1[0])
        
        self.angle2_start = atan2(vec_B1[1], vec_B1[0])
        self.angle2_end = atan2(vec_A2[1], vec_A2[0])
        
        self.angle3_start = atan2(vec_A2[1], vec_A2[0])
        self.angle3_end = atan2(vec_B2[1], vec_B2[0])
        
        self.angle4_start = atan2(vec_B2[1], vec_B2[0])
        self.angle4_end = atan2(vec_A1[1], vec_A1[0])
        
        # 计算角度值（度数）- 用于显示
        # ∠1和∠3应该相等（对顶角）
        self.angle1_value = 60  # 度
        self.angle3_value = 60  # 度
        self.angle2_value = 120  # 度
        self.angle4_value = 120  # 度
        
        # 验证几何关系
        self.verify_geometry()
        
        # 创建基本几何对象（但不添加到场景）
        self.line1 = Line(self.A2, self.A1, color=self.COLOR_LINE1, stroke_width=3)
        self.line2 = Line(self.B2, self.B1, color=self.COLOR_LINE2, stroke_width=3)
        
        print("✓ 几何设置完成")
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-2
        
        # 验证邻补角：∠1 + ∠2 应该约等于180°
        sum_12 = self.angle1_value + self.angle2_value
        assert abs(sum_12 - 180) < epsilon, f"邻补角验证失败: {sum_12}°"
        
        # 验证对顶角：∠1 应该等于 ∠3
        assert abs(self.angle1_value - self.angle3_value) < epsilon, \
            f"对顶角验证失败: ∠1={self.angle1_value}°, ∠3={self.angle3_value}°"
        
        print("✓ 几何验证通过")
    
    def create_angle_arc(self, center, start_angle, end_angle, radius=0.5, color=WHITE):
        """创建角的圆弧标注"""
        # 确保角度在正确范围内
        if end_angle < start_angle:
            end_angle += 2 * PI
        
        arc = Arc(
            radius=radius,
            start_angle=start_angle,
            angle=end_angle - start_angle,
            color=color,
            stroke_width=3
        ).move_arc_center_to(center)
        
        return arc
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "这两个角相等吗？",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 两条相交直线
        self.play(
            Create(self.line1),
            Create(self.line2),
            run_time=1.0
        )
        
        # 创建∠1和∠3的圆弧（暂时不标注数字）
        arc1 = self.create_angle_arc(
            self.O,
            self.angle1_start,
            self.angle1_end,
            radius=0.6,
            color=self.COLOR_ANGLE1
        )
        
        arc3 = self.create_angle_arc(
            self.O,
            self.angle3_start,
            self.angle3_end,
            radius=0.6,
            color=self.COLOR_ANGLE3
        )
        
        self.play(Create(arc1), run_time=0.5)
        self.play(Flash(arc1, color=self.COLOR_ANGLE1, flash_radius=0.8), run_time=0.5)
        
        self.play(Create(arc3), run_time=0.5)
        self.play(Flash(arc3, color=self.COLOR_ANGLE3, flash_radius=0.8), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(arc1),
            FadeOut(arc3),
            run_time=0.5
        )
    
    def scene_2_intersecting_lines(self):
        """场景2: 引入相交线 (5-12秒)"""
        # 标题
        title = Text(
            "两条直线相交",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 直线1高亮和标注
        self.play(self.line1.animate.set_stroke(width=6), run_time=0.4)
        
        label_l1_chinese = Text("直线", font="PingFang SC", font_size=20, color=WHITE)
        label_l1_math = MathTex(r"l_1", color=self.COLOR_LINE1, font_size=28)
        label_l1 = VGroup(label_l1_chinese, label_l1_math).arrange(RIGHT, buff=0.1)
        label_l1.next_to(self.A1, RIGHT, buff=0.2)
        
        self.play(Write(label_l1), run_time=0.3)
        self.play(self.line1.animate.set_stroke(width=3), run_time=0.2)
        
        # 直线2高亮和标注
        self.play(self.line2.animate.set_stroke(width=6), run_time=0.4)
        
        label_l2_chinese = Text("直线", font="PingFang SC", font_size=20, color=WHITE)
        label_l2_math = MathTex(r"l_2", color=self.COLOR_LINE2, font_size=28)
        label_l2 = VGroup(label_l2_chinese, label_l2_math).arrange(RIGHT, buff=0.1)
        label_l2.next_to(self.B1, UP, buff=0.2)
        
        self.play(Write(label_l2), run_time=0.3)
        self.play(self.line2.animate.set_stroke(width=3), run_time=0.2)
        
        # 交点O标注
        point_O = Dot(self.O, color=YELLOW, radius=0.1)
        label_O = Text("O", font="PingFang SC", font_size=24, color=YELLOW).next_to(point_O, DOWN + RIGHT, buff=0.15)
        
        self.play(
            FadeIn(point_O, scale=0.5),
            Flash(point_O, color=YELLOW, flash_radius=0.5),
            run_time=0.6
        )
        self.play(Write(label_O), run_time=0.3)
        
        # 说明文字
        explain_text = Text(
            "交于点O",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain_text), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explain_text),
            FadeOut(label_l1),
            FadeOut(label_l2),
            run_time=0.5
        )
        
        # 保留交点标记
        self.point_O = point_O
        self.label_O = label_O
    
    def scene_3_four_angles(self):
        """场景3: 引入四个角 (12-20秒)"""
        # 标题
        title = Text(
            "形成四个角",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 创建四个角的圆弧
        arc_radius = 0.5
        
        self.arc1 = self.create_angle_arc(
            self.O,
            self.angle1_start,
            self.angle1_end,
            radius=arc_radius,
            color=self.COLOR_ANGLE1
        )
        
        self.arc2 = self.create_angle_arc(
            self.O,
            self.angle2_start,
            self.angle2_end,
            radius=arc_radius,
            color=self.COLOR_ANGLE2
        )
        
        self.arc3 = self.create_angle_arc(
            self.O,
            self.angle3_start,
            self.angle3_end,
            radius=arc_radius,
            color=self.COLOR_ANGLE3
        )
        
        self.arc4 = self.create_angle_arc(
            self.O,
            self.angle4_start,
            self.angle4_end,
            radius=arc_radius,
            color=self.COLOR_ANGLE4
        )
        
        # 创建角标签
        # ∠1 (右上)
        angle1_mid = (self.angle1_start + self.angle1_end) / 2
        label1_pos = self.O + np.array([cos(angle1_mid), sin(angle1_mid), 0]) * 0.9
        self.label1 = MathTex(r"\angle 1", color=self.COLOR_ANGLE1, font_size=24).move_to(label1_pos)
        
        # ∠2 (右下)
        angle2_mid = (self.angle2_start + self.angle2_end) / 2
        label2_pos = self.O + np.array([cos(angle2_mid), sin(angle2_mid), 0]) * 0.9
        self.label2 = MathTex(r"\angle 2", color=self.COLOR_ANGLE2, font_size=24).move_to(label2_pos)
        
        # ∠3 (左下)
        angle3_mid = (self.angle3_start + self.angle3_end) / 2
        label3_pos = self.O + np.array([cos(angle3_mid), sin(angle3_mid), 0]) * 0.9
        self.label3 = MathTex(r"\angle 3", color=self.COLOR_ANGLE3, font_size=24).move_to(label3_pos)
        
        # ∠4 (左上)
        angle4_mid = (self.angle4_start + self.angle4_end) / 2
        label4_pos = self.O + np.array([cos(angle4_mid), sin(angle4_mid), 0]) * 0.9
        self.label4 = MathTex(r"\angle 4", color=self.COLOR_ANGLE4, font_size=24).move_to(label4_pos)
        
        # 依次创建角
        self.play(Create(self.arc1), run_time=0.6)
        self.play(Write(self.label1), run_time=0.3)
        
        self.play(Create(self.arc2), run_time=0.6)
        self.play(Write(self.label2), run_time=0.3)
        
        self.play(Create(self.arc3), run_time=0.6)
        self.play(Write(self.label3), run_time=0.3)
        
        self.play(Create(self.arc4), run_time=0.6)
        self.play(Write(self.label4), run_time=0.3)
        
        self.wait(1.5)
        
        # 清理标题
        self.play(FadeOut(title), run_time=0.4)
    
    def scene_4_vertical_angle_definition(self):
        """场景4: 对顶角定义 (20-30秒)"""
        # 标题
        title = Text(
            "什么是对顶角？",
            font="PingFang SC",
            font_size=32,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 淡化所有角
        all_arcs = VGroup(self.arc1, self.arc2, self.arc3, self.arc4)
        all_labels = VGroup(self.label1, self.label2, self.label3, self.label4)
        
        self.play(
            all_arcs.animate.set_opacity(0.3),
            all_labels.animate.set_opacity(0.3),
            run_time=0.4
        )
        
        # 高亮∠1和∠3
        self.play(
            self.arc1.animate.set_opacity(1),
            self.label1.animate.set_opacity(1),
            self.arc3.animate.set_opacity(1),
            self.label3.animate.set_opacity(1),
            run_time=0.5
        )
        
        # 虚线连接对顶角（穿过点O）
        dashed_line_13 = DashedLine(
            self.O + (self.A1 - self.O) * 0.3,
            self.O + (self.A2 - self.O) * 0.3,
            color=YELLOW,
            dash_length=0.1,
            stroke_width=2
        )
        
        self.play(Create(dashed_line_13), run_time=0.6)
        
        # 定义文字
        def_text1 = Text(
            "有公共顶点",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(def_text1), run_time=0.5)
        
        # 点O闪烁
        self.play(
            Flash(self.point_O, color=YELLOW, flash_radius=0.5),
            run_time=0.4
        )
        
        def_text2 = Text(
            "没有公共边",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 4.8)
        
        self.play(FadeIn(def_text2), run_time=0.5)
        self.wait(1.0)
        
        # 恢复所有角
        self.play(
            all_arcs.animate.set_opacity(1),
            all_labels.animate.set_opacity(1),
            run_time=0.4
        )
        
        # 高亮∠2和∠4
        self.play(
            self.arc2.animate.set_stroke(width=5),
            self.arc4.animate.set_stroke(width=5),
            run_time=0.6
        )
        
        hint_text = Text(
            "∠2和∠4也是对顶角",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.8)
        
        self.play(FadeIn(hint_text), run_time=0.8)
        
        # 恢复粗细
        self.play(
            self.arc2.animate.set_stroke(width=3),
            self.arc4.animate.set_stroke(width=3),
            run_time=0.3
        )
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(def_text1),
            FadeOut(def_text2),
            FadeOut(hint_text),
            FadeOut(dashed_line_13),
            run_time=0.6
        )
    
    def scene_5_vertical_angle_property(self):
        """场景5: 对顶角性质 - 测量 (30-45秒)"""
        # 标题
        title = Text(
            "对顶角有什么性质？",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 淡化∠2和∠4
        self.play(
            self.arc2.animate.set_opacity(0.2),
            self.label2.animate.set_opacity(0.2),
            self.arc4.animate.set_opacity(0.2),
            self.label4.animate.set_opacity(0.2),
            run_time=0.4
        )
        
        # 放大∠1
        self.play(
            self.arc1.animate.scale(1.5),
            self.label1.animate.scale(1.2),
            run_time=0.5
        )
        
        # 测量动画 - 简化版量角器
        protractor = Arc(
            radius=0.8,
            start_angle=self.angle1_start,
            angle=self.angle1_end - self.angle1_start,
            color=YELLOW,
            stroke_width=2
        ).move_arc_center_to(self.O)
        
        self.play(Create(protractor), run_time=1.0)
        
        # 度数显示 - 使用计数动画
        angle1_value_text = MathTex(
            r"\angle 1 = 60^\circ",
            color=self.COLOR_ANGLE1,
            font_size=32
        ).move_to(UP * 3.5)
        
        # 创建一个计数器效果
        counter = Integer(0, color=self.COLOR_ANGLE1, font_size=32).move_to(UP * 3.5)
        self.add(counter)
        self.play(
            counter.animate.set_value(60),
            run_time=1.2,
            rate_func=linear
        )
        self.remove(counter)
        self.play(Write(angle1_value_text), run_time=0.3)
        
        # 恢复∠1大小
        self.play(
            self.arc1.animate.scale(1 / 1.5),
            self.label1.animate.scale(1 / 1.2),
            FadeOut(protractor),
            run_time=0.5
        )
        
        self.wait(0.3)
        
        # 移动到∠3
        self.play(
            self.arc3.animate.scale(1.5),
            self.label3.animate.scale(1.2),
            run_time=0.5
        )
        
        # 测量∠3
        protractor3 = Arc(
            radius=0.8,
            start_angle=self.angle3_start,
            angle=self.angle3_end - self.angle3_start,
            color=YELLOW,
            stroke_width=2
        ).move_arc_center_to(self.O)
        
        self.play(Create(protractor3), run_time=1.0)
        
        # 度数显示
        angle3_value_text = MathTex(
            r"\angle 3 = 60^\circ",
            color=self.COLOR_ANGLE3,
            font_size=32
        ).move_to(DOWN * 3)
        
        counter3 = Integer(0, color=self.COLOR_ANGLE3, font_size=32).move_to(DOWN * 3)
        self.add(counter3)
        self.play(
            counter3.animate.set_value(60),
            run_time=1.2,
            rate_func=linear
        )
        self.remove(counter3)
        self.play(Write(angle3_value_text), run_time=0.3)
        
        # 恢复大小
        self.play(
            self.arc3.animate.scale(1 / 1.5),
            self.label3.animate.scale(1 / 1.2),
            FadeOut(protractor3),
            run_time=0.5
        )
        
        # 惊叹符号
        exclaim = Text("!", font_size=60, color=YELLOW).move_to(RIGHT * 3.5 + UP * 2)
        self.play(
            FadeIn(exclaim, scale=2),
            Flash(exclaim, color=YELLOW),
            run_time=0.5
        )
        
        # 结论
        conclusion = Text(
            "∠1 = ∠3 = 60°",
            font="PingFang SC",
            font_size=28,
            color=GOLD
        ).move_to(ORIGIN)
        
        conclusion_box = SurroundingRectangle(conclusion, color=GOLD, buff=0.3, corner_radius=0.1)
        
        self.play(
            FadeIn(conclusion),
            Create(conclusion_box),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(angle1_value_text),
            FadeOut(angle3_value_text),
            FadeOut(exclaim),
            FadeOut(conclusion),
            FadeOut(conclusion_box),
            self.arc2.animate.set_opacity(1),
            self.label2.animate.set_opacity(1),
            self.arc4.animate.set_opacity(1),
            self.label4.animate.set_opacity(1),
            run_time=0.6
        )
    
    def scene_6_proof_idea(self):
        """场景6: 对顶角性质 - 证明思路 (45-58秒)"""
        # 标题
        title = Text(
            "为什么对顶角相等？",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 高亮∠1和∠2
        self.play(
            self.arc1.animate.set_color(YELLOW),
            self.arc2.animate.set_color(YELLOW),
            run_time=0.5
        )
        
        # 公式1
        formula1_chinese = Text("因为", font="PingFang SC", font_size=22, color=WHITE)
        formula1_math = MathTex(r"\angle 1 + \angle 2 = 180^\circ", font_size=28, color=WHITE)
        formula1 = VGroup(formula1_chinese, formula1_math).arrange(RIGHT, buff=0.2).move_to(DOWN * 3)
        
        self.play(Write(formula1), run_time=1.0)
        
        # 说明文字
        explain1 = Text(
            "(这是一条直线)",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).next_to(formula1, DOWN, buff=0.2)
        
        self.play(FadeIn(explain1), run_time=0.6)
        
        # 恢复颜色，高亮∠3和∠2
        self.play(
            self.arc1.animate.set_color(self.COLOR_ANGLE1),
            self.arc2.animate.set_color(YELLOW),
            self.arc3.animate.set_color(YELLOW),
            run_time=0.5
        )
        
        # 公式2
        formula2_chinese = Text("同理", font="PingFang SC", font_size=22, color=WHITE)
        formula2_math = MathTex(r"\angle 3 + \angle 2 = 180^\circ", font_size=28, color=WHITE)
        formula2 = VGroup(formula2_chinese, formula2_math).arrange(RIGHT, buff=0.2).move_to(DOWN * 4.2)
        
        self.play(Write(formula2), run_time=1.0)
        
        # 恢复颜色
        self.play(
            self.arc2.animate.set_color(self.COLOR_ANGLE2),
            self.arc3.animate.set_color(self.COLOR_ANGLE3),
            run_time=0.3
        )
        
        # 箭头指向结论
        arrow = Arrow(
            formula2.get_bottom() + DOWN * 0.3,
            DOWN * 5.5,
            color=GOLD,
            buff=0.1,
            stroke_width=4
        )
        
        self.play(Create(arrow), run_time=0.5)
        
        # 结论
        conclusion_chinese = Text("所以", font="PingFang SC", font_size=24, color=WHITE)
        conclusion_math = MathTex(r"\angle 1 = \angle 3", font_size=32, color=GOLD)
        conclusion = VGroup(conclusion_chinese, conclusion_math).arrange(RIGHT, buff=0.2).move_to(DOWN * 6)
        
        self.play(Write(conclusion), run_time=1.0)
        
        # 高亮结论
        self.play(
            conclusion.animate.set_color(GOLD).scale(1.2),
            run_time=0.6
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula1),
            FadeOut(formula2),
            FadeOut(explain1),
            FadeOut(arrow),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def scene_7_outro(self):
        """场景7: 总结与片尾 (58-75秒)"""
        # 将主图形缩小并移到角落
        main_group = VGroup(
            self.line1, self.line2,
            self.point_O, self.label_O,
            self.arc1, self.arc2, self.arc3, self.arc4,
            self.label1, self.label2, self.label3, self.label4
        )
        
        self.play(
            main_group.animate.scale(0.4).to_corner(UL, buff=0.5),
            run_time=0.8
        )
        
        # 知识卡片
        card_title = Text(
            "对顶角",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        )
        
        card_def_label = Text(
            "定义：",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        card_def_content = Text(
            "有公共顶点但没有公共边的两个角",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        )
        card_def = VGroup(card_def_label, card_def_content).arrange(RIGHT, buff=0.2, aligned_edge=UP)
        
        card_prop_label = Text(
            "性质：",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        card_prop_content = Text(
            "对顶角相等",
            font="PingFang SC",
            font_size=20,
            color=GOLD
        )
        card_prop = VGroup(card_prop_label, card_prop_content).arrange(RIGHT, buff=0.2, aligned_edge=UP)
        
        card_content = VGroup(card_title, card_def, card_prop).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        card_content.move_to(UP * 1)
        
        card_box = SurroundingRectangle(card_content, color=GOLD, buff=0.5, corner_radius=0.2)
        card = VGroup(card_box, card_content)
        
        self.play(FadeIn(card, shift=UP), run_time=0.8)
        self.play(Write(card_content), run_time=1.5)
        
        # 移动卡片到上方
        self.play(
            card.animate.move_to(UP * 3).scale(0.7),
            run_time=0.8
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 0.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(Write(author_id), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=GOLD
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰 - 小角度符号环绕
        angle_symbols = VGroup(*[
            MathTex(r"\angle", color=GOLD, font_size=30)
            .move_to(follow_text.get_center() + 2.5 * np.array([cos(i * PI / 4), sin(i * PI / 4), 0]))
            for i in range(8)
        ])
        
        self.play(
            *[FadeIn(sym, scale=0.5) for sym in angle_symbols],
            run_time=0.6
        )
        
        self.play(
            Rotate(angle_symbols, angle=PI, about_point=follow_text.get_center()),
            run_time=1.5
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(main_group),
            FadeOut(card),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(angle_symbols),
            run_time=1.0
        )


# 运行命令:
# manim -pql vertical_angles.py VerticalAngles  # 快速预览
# manim -qh vertical_angles.py VerticalAngles   # 高质量渲染
# manim -qk vertical_angles.py VerticalAngles   # 4K渲染