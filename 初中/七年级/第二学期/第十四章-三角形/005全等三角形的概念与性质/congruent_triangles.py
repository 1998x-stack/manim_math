"""
全等三角形的概念与性质 - Congruent Triangles Concept and Properties
使用 Manim 创建的中学几何教学视频

内容: 全等三角形的定义、符号、对应关系、性质
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


class CongruentTriangles(Scene):
    """
    全等三角形教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 定义全等三角形
    3. 演示重合过程
    4. 介绍全等符号
    5. 标注对应关系
    6. 性质1 - 对应边相等
    7. 性质2 - 对应角相等
    8. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_TRIANGLE_1 = "#3498db"       # 蓝色 - ABC
        self.COLOR_TRIANGLE_2 = "#e74c3c"       # 红色 - DEF
        self.COLOR_CONGRUENT = "#2ecc71"        # 绿色 - 重合
        self.COLOR_HIGHLIGHT = YELLOW           # 高亮
        self.COLOR_AUXILIARY = GRAY_B           # 辅助
        self.COLOR_CORRESPONDENCE = "#f39c12"   # 橙色 - 对应关系
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_overlap()
        self.scene_4_symbol()
        self.scene_5_correspondence()
        self.scene_6_property_sides()
        self.scene_7_property_angles()
        self.scene_8_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据"""
        # 基准参数
        self.SCALE = 0.9
        self.OFFSET = UP * 1.5
        
        # 三角形ABC顶点（基准三角形）
        self.A = np.array([-2.5, 0.5, 0]) * self.SCALE + self.OFFSET
        self.B = np.array([1.0, -1.5, 0]) * self.SCALE + self.OFFSET
        self.C = np.array([-0.5, 2.0, 0]) * self.SCALE + self.OFFSET
        
        # 三角形DEF初始位置（右侧）
        offset_right = RIGHT * 5
        self.D_init = self.A + offset_right
        self.E_init = self.B + offset_right
        self.F_init = self.C + offset_right
        
        # 三角形DEF目标位置（与ABC重合）
        self.D_target = self.A
        self.E_target = self.B
        self.F_target = self.C
        
        # 计算边长
        self.AB = np.linalg.norm(self.B - self.A)
        self.BC = np.linalg.norm(self.C - self.B)
        self.CA = np.linalg.norm(self.A - self.C)
        
        # 计算角度（弧度）
        self.angle_A = self.calculate_angle(self.C, self.A, self.B)
        self.angle_B = self.calculate_angle(self.A, self.B, self.C)
        self.angle_C = self.calculate_angle(self.B, self.C, self.A)
        
        # 验证几何
        self.verify_geometry()
        
        print("✓ 几何初始化完成")
        print(f"  边长: AB={self.AB:.3f}, BC={self.BC:.3f}, CA={self.CA:.3f}")
        print(f"  角度: ∠A={np.degrees(self.angle_A):.1f}°, ∠B={np.degrees(self.angle_B):.1f}°, ∠C={np.degrees(self.angle_C):.1f}°")
    
    def calculate_angle(self, P1, vertex, P2):
        """计算角度（以vertex为顶点）"""
        v1 = P1 - vertex
        v2 = P2 - vertex
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        return np.arccos(cos_angle)
    
    def verify_geometry(self):
        """验证几何计算"""
        epsilon = 1e-6
        
        # 验证角度和
        angle_sum = self.angle_A + self.angle_B + self.angle_C
        if abs(angle_sum - np.pi) > epsilon:
            print(f"WARNING: 角度和 = {np.degrees(angle_sum):.2f}° (应为180°)")
        
        # 验证DEF与ABC全等（目标位置）
        DE = np.linalg.norm(self.E_target - self.D_target)
        EF = np.linalg.norm(self.F_target - self.E_target)
        FD = np.linalg.norm(self.D_target - self.F_target)
        
        if abs(self.AB - DE) > epsilon or abs(self.BC - EF) > epsilon or abs(self.CA - FD) > epsilon:
            print("WARNING: DEF与ABC边长不一致")
        
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
        hook_text = Text(
            "这两个三角形有什么关系?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 创建三角形ABC（左侧）
        self.triangle_ABC = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_TRIANGLE_1,
            stroke_width=4
        ).shift(LEFT * 2)
        
        # 创建三角形DEF（右侧）
        self.triangle_DEF = Polygon(
            self.D_init, self.E_init, self.F_init,
            color=self.COLOR_TRIANGLE_2,
            stroke_width=4
        ).shift(LEFT * 2)
        
        self.play(Create(self.triangle_ABC), run_time=1.0)
        self.play(Create(self.triangle_DEF), run_time=1.0)
        
        self.wait(0.8)
        
        # 清理
        self.play(FadeOut(hook_text), run_time=0.4)
    
    def scene_2_definition(self):
        """场景2: 定义全等三角形"""
        # 标题
        title = Text(
            "全等三角形",
            font="PingFang SC",
            font_size=44,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 5)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 定义
        definition = Text(
            "能够完全重合的两个三角形",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 4)
        
        self.play(Write(definition), run_time=1.2)
        
        # 强调"完全重合"
        key_words = definition[4:8]  # "完全重合"
        self.play(
            Indicate(key_words, color=self.COLOR_HIGHLIGHT, scale_factor=1.2),
            run_time=1.0
        )
        
        self.wait(1.5)
        
        # 标题缩小并移到顶部
        self.title_small = Text(
            "全等三角形",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 6.5)
        
        self.play(
            Transform(title, self.title_small),
            FadeOut(definition),
            run_time=0.6
        )
        
        self.title = title  # 保存引用
    
    def scene_3_overlap(self):
        """场景3: 演示重合过程"""
        # 提示文字
        hint_text = Text(
            "让我们试试能否重合",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(hint_text), run_time=0.8)
        
        # DEF平移到ABC位置
        target_center = self.triangle_ABC.get_center()
        self.play(
            self.triangle_DEF.animate.move_to(target_center),
            run_time=1.5
        )
        
        # 计算需要的旋转角度
        # 使用AB和DE的方向向量
        AB_vec = self.B - self.A
        current_D = self.triangle_DEF.get_vertices()[0]
        current_E = self.triangle_DEF.get_vertices()[1]
        DE_vec = current_E - current_D
        
        # 计算旋转角度
        angle_AB = np.arctan2(AB_vec[1], AB_vec[0])
        angle_DE = np.arctan2(DE_vec[1], DE_vec[0])
        rotation_angle = angle_AB - angle_DE
        
        # 旋转对齐
        self.play(
            Rotate(self.triangle_DEF, rotation_angle, about_point=target_center),
            run_time=1.7
        )
        
        # 完全重合闪光效果
        self.play(
            Flash(target_center, color=self.COLOR_CONGRUENT, flash_radius=1.5),
            run_time=0.5
        )
        
        # 改变颜色表示重合
        self.play(
            self.triangle_DEF.animate.set_color(self.COLOR_CONGRUENT).set_opacity(0.7),
            run_time=1.0
        )
        
        success_text = Text(
            "完全重合!",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_CONGRUENT,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(
            FadeOut(hint_text),
            FadeIn(success_text, scale=1.2),
            run_time=0.5
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(FadeOut(success_text), run_time=0.4)
    
    def scene_4_symbol(self):
        """场景4: 介绍全等符号"""
        # 将两三角形分开
        self.play(
            self.triangle_ABC.animate.shift(LEFT * 2),
            self.triangle_DEF.animate.shift(RIGHT * 2).set_color(self.COLOR_TRIANGLE_2).set_opacity(1.0),
            run_time=1.2
        )
        
        # 全等符号公式
        congruence_formula = MathTex(
            r"\triangle ABC \cong \triangle DEF",
            font_size=38
        ).move_to(ORIGIN)
        
        self.play(Write(congruence_formula), run_time=1.5)
        
        # 读法说明
        reading_text = Text(
            "读作：三角形ABC全等于三角形DEF",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(reading_text), run_time=0.5)
        
        self.wait(1.2)
        
        # 清理
        self.play(FadeOut(reading_text), run_time=0.4)
        
        # 公式移到顶部
        self.congruence_small = MathTex(
            r"\triangle ABC \cong \triangle DEF",
            font_size=26
        ).move_to(UP * 5.8)
        
        self.play(
            Transform(congruence_formula, self.congruence_small),
            run_time=0.6
        )
        
        self.congruence_formula = congruence_formula
    
    def scene_5_correspondence(self):
        """场景5: 标注对应关系"""
        # 调整三角形位置
        self.play(
            self.triangle_ABC.animate.shift(UP * 0.5),
            self.triangle_DEF.animate.shift(UP * 0.5),
            run_time=0.6
        )
        
        # 获取当前顶点位置
        vertices_ABC = self.triangle_ABC.get_vertices()
        vertices_DEF = self.triangle_DEF.get_vertices()
        
        # 顶点标签
        label_A = Text("A", font="PingFang SC", font_size=24, color=WHITE).next_to(vertices_ABC[0], LEFT, buff=0.2)
        label_B = Text("B", font="PingFang SC", font_size=24, color=WHITE).next_to(vertices_ABC[1], RIGHT, buff=0.2)
        label_C = Text("C", font="PingFang SC", font_size=24, color=WHITE).next_to(vertices_ABC[2], UP, buff=0.2)
        
        label_D = Text("D", font="PingFang SC", font_size=24, color=WHITE).next_to(vertices_DEF[0], LEFT, buff=0.2)
        label_E = Text("E", font="PingFang SC", font_size=24, color=WHITE).next_to(vertices_DEF[1], RIGHT, buff=0.2)
        label_F = Text("F", font="PingFang SC", font_size=24, color=WHITE).next_to(vertices_DEF[2], UP, buff=0.2)
        
        self.labels_ABC = VGroup(label_A, label_B, label_C)
        self.labels_DEF = VGroup(label_D, label_E, label_F)
        
        self.play(
            FadeIn(self.labels_ABC, lag_ratio=0.2),
            FadeIn(self.labels_DEF, lag_ratio=0.2),
            run_time=1.0
        )
        
        # 说明文字
        correspondence_text = Text(
            "确定对应关系很重要!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(correspondence_text), run_time=0.5)
        self.wait(0.5)
        
        # 对应关系箭头
        arrow_AD = CurvedArrow(
            label_A.get_right() + DOWN * 0.1,
            label_D.get_left() + DOWN * 0.1,
            color=self.COLOR_CORRESPONDENCE,
            angle=-TAU / 8
        )
        
        arrow_BE = CurvedArrow(
            label_B.get_left() + DOWN * 0.1,
            label_E.get_right() + DOWN * 0.1,
            color=self.COLOR_CORRESPONDENCE,
            angle=-TAU / 8
        )
        
        arrow_CF = CurvedArrow(
            label_C.get_bottom() + RIGHT * 0.1,
            label_F.get_bottom() + LEFT * 0.1,
            color=self.COLOR_CORRESPONDENCE,
            angle=-TAU / 12
        )
        
        self.play(Create(arrow_AD), run_time=0.7)
        self.play(Create(arrow_BE), run_time=0.7)
        self.play(Create(arrow_CF), run_time=0.7)
        
        # 高亮对应关系
        self.play(
            Indicate(VGroup(label_A, label_D), color=self.COLOR_HIGHLIGHT),
            Indicate(VGroup(label_B, label_E), color=self.COLOR_HIGHLIGHT),
            Indicate(VGroup(label_C, label_F), color=self.COLOR_HIGHLIGHT),
            run_time=1.5
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(arrow_AD),
            FadeOut(arrow_BE),
            FadeOut(arrow_CF),
            FadeOut(correspondence_text),
            run_time=0.6
        )
    
    def scene_6_property_sides(self):
        """场景6: 性质1 - 对应边相等"""
        # 性质标题
        property_title = Text(
            "性质1：对应边相等",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_CONGRUENT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(property_title, shift=UP * 0.3), run_time=0.8)
        
        # 获取当前顶点
        vertices_ABC = self.triangle_ABC.get_vertices()
        vertices_DEF = self.triangle_DEF.get_vertices()
        
        # 边AB和DE
        self.play(
            self.triangle_ABC.animate.set_color(self.COLOR_TRIANGLE_1),
            run_time=0.3
        )
        
        line_AB = Line(vertices_ABC[0], vertices_ABC[1], color=self.COLOR_HIGHLIGHT, stroke_width=6)
        line_DE = Line(vertices_DEF[0], vertices_DEF[1], color=self.COLOR_HIGHLIGHT, stroke_width=6)
        
        self.play(Create(line_AB), Create(line_DE), run_time=0.5)
        
        eq1 = MathTex(r"AB = DE", font_size=28).move_to(DOWN * 4)
        self.play(Write(eq1), run_time=0.5)
        self.wait(0.5)
        
        self.play(FadeOut(line_AB), FadeOut(line_DE), run_time=0.3)
        
        # 边BC和EF
        line_BC = Line(vertices_ABC[1], vertices_ABC[2], color=self.COLOR_HIGHLIGHT, stroke_width=6)
        line_EF = Line(vertices_DEF[1], vertices_DEF[2], color=self.COLOR_HIGHLIGHT, stroke_width=6)
        
        self.play(Create(line_BC), Create(line_EF), run_time=0.5)
        
        eq2 = MathTex(r"BC = EF", font_size=28).next_to(eq1, DOWN, buff=0.3)
        self.play(Write(eq2), run_time=0.5)
        self.wait(0.5)
        
        self.play(FadeOut(line_BC), FadeOut(line_EF), run_time=0.3)
        
        # 边CA和FD
        line_CA = Line(vertices_ABC[2], vertices_ABC[0], color=self.COLOR_HIGHLIGHT, stroke_width=6)
        line_FD = Line(vertices_DEF[2], vertices_DEF[0], color=self.COLOR_HIGHLIGHT, stroke_width=6)
        
        self.play(Create(line_CA), Create(line_FD), run_time=0.5)
        
        eq3 = MathTex(r"CA = FD", font_size=28).next_to(eq2, DOWN, buff=0.3)
        self.play(Write(eq3), run_time=0.5)
        self.wait(0.5)
        
        self.play(FadeOut(line_CA), FadeOut(line_FD), run_time=0.3)
        
        # 组合展示
        equations = VGroup(eq1, eq2, eq3)
        self.play(Indicate(equations, color=self.COLOR_CONGRUENT, scale_factor=1.1), run_time=0.8)
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(property_title),
            FadeOut(equations),
            run_time=0.6
        )
    
    def scene_7_property_angles(self):
        """场景7: 性质2 - 对应角相等"""
        # 性质标题
        property_title = Text(
            "性质2：对应角相等",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_CONGRUENT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(property_title, shift=UP * 0.3), run_time=0.8)
        
        # 获取当前顶点
        vertices_ABC = self.triangle_ABC.get_vertices()
        vertices_DEF = self.triangle_DEF.get_vertices()
        
        # 角A和角D
        angle_A_arc = Angle.from_three_points(
            vertices_ABC[2], vertices_ABC[0], vertices_ABC[1],
            radius=0.4,
            color=self.COLOR_HIGHLIGHT,
            other_angle=True  # 顺时针方向
        )
        
        angle_D_arc = Angle.from_three_points(
            vertices_DEF[2], vertices_DEF[0], vertices_DEF[1],
            radius=0.4,
            color=self.COLOR_HIGHLIGHT,
            other_angle=True  # 顺时针方向
        )
        
        self.play(Create(angle_A_arc), Create(angle_D_arc), run_time=0.5)
        
        eq1 = MathTex(r"\angle A = \angle D", font_size=28).move_to(DOWN * 4)
        self.play(Write(eq1), run_time=0.5)
        self.wait(0.5)
        
        self.play(FadeOut(angle_A_arc), FadeOut(angle_D_arc), run_time=0.3)
        
        # 角B和角E
        angle_B_arc = Angle.from_three_points(
            vertices_ABC[0], vertices_ABC[1], vertices_ABC[2],
            radius=0.4,
            color=self.COLOR_HIGHLIGHT,
            other_angle=True  # 顺时针方向
        )
        
        angle_E_arc = Angle.from_three_points(
            vertices_DEF[0], vertices_DEF[1], vertices_DEF[2],
            radius=0.4,
            color=self.COLOR_HIGHLIGHT,
            other_angle=True  # 顺时针方向
        )
        
        self.play(Create(angle_B_arc), Create(angle_E_arc), run_time=0.5)
        
        eq2 = MathTex(r"\angle B = \angle E", font_size=28).next_to(eq1, DOWN, buff=0.3)
        self.play(Write(eq2), run_time=0.5)
        self.wait(0.5)
        
        self.play(FadeOut(angle_B_arc), FadeOut(angle_E_arc), run_time=0.3)
        
        # 角C和角F
        angle_C_arc = Angle.from_three_points(
            vertices_ABC[1], vertices_ABC[2], vertices_ABC[0],
            radius=0.4,
            color=self.COLOR_HIGHLIGHT,
            other_angle=True  # 顺时针方向
        )
        
        angle_F_arc = Angle.from_three_points(
            vertices_DEF[1], vertices_DEF[2], vertices_DEF[0],
            radius=0.4,
            color=self.COLOR_HIGHLIGHT,
            other_angle=True  # 顺时针方向
        )
        
        self.play(Create(angle_C_arc), Create(angle_F_arc), run_time=0.5)
        
        eq3 = MathTex(r"\angle C = \angle F", font_size=28).next_to(eq2, DOWN, buff=0.3)
        self.play(Write(eq3), run_time=0.5)
        self.wait(0.5)
        
        self.play(FadeOut(angle_C_arc), FadeOut(angle_F_arc), run_time=0.3)
        
        # 组合展示
        equations = VGroup(eq1, eq2, eq3)
        self.play(Indicate(equations, color=self.COLOR_CONGRUENT, scale_factor=1.1), run_time=0.8)
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(property_title),
            FadeOut(equations),
            run_time=0.6
        )
    
    def scene_8_outro(self):
        """场景8: 总结与片尾"""
        # 重点提示
        warning_text = Text(
            "重要提示",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 3)
        
        self.play(FadeIn(warning_text, scale=1.1), run_time=0.5)
        
        note = Text(
            "对应顶点的书写顺序要对应!",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 2)
        
        self.play(FadeIn(note), run_time=0.5)
        self.wait(0.5)
        
        # 正确示例
        correct_example = VGroup(
            Text("✓ 正确:", font="PingFang SC", font_size=24, color=GREEN),
            MathTex(r"\triangle ABC \cong \triangle DEF", font_size=26, color=GREEN)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 0.5)
        
        # 错误示例
        wrong_example = VGroup(
            Text("✗ 错误:", font="PingFang SC", font_size=24, color=RED),
            MathTex(r"\triangle ABC \cong \triangle EDF", font_size=26, color=RED)
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.5)
        
        self.play(FadeIn(correct_example), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(wrong_example), run_time=0.5)
        
        # 对比闪烁
        self.play(
            Flash(correct_example, color=GREEN),
            Indicate(wrong_example, color=RED, scale_factor=1.1),
            run_time=1.0
        )
        
        self.wait(1.0)
        
        # 清理所有三角形和标签
        self.play(
            FadeOut(self.triangle_ABC),
            FadeOut(self.triangle_DEF),
            FadeOut(self.labels_ABC),
            FadeOut(self.labels_DEF),
            FadeOut(self.title),
            FadeOut(self.congruence_formula),
            FadeOut(warning_text),
            FadeOut(note),
            FadeOut(correct_example),
            FadeOut(wrong_example),
            run_time=0.5
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多几何技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 小三角形装饰
        triangles = VGroup(*[
            Polygon(
                ORIGIN, RIGHT * 0.3, UP * 0.3,
                color=self.COLOR_CONGRUENT,
                fill_opacity=0.8
            ).scale(0.5).move_to(
                follow_text.get_center() + 2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles],
            run_time=0.6
        )
        self.play(Rotate(triangles, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles),
            run_time=1.0
        )


# 运行命令:
# manim -pql congruent_triangles.py CongruentTriangles  # 快速预览
# manim -qh congruent_triangles.py CongruentTriangles   # 高质量渲染