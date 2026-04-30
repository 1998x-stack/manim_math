"""
SSS全等三角形判定 - Manim教学动画
知识点: 三边分别对应相等的两个三角形全等

作者: 上海初高中数学直通车 @emptyandcalm
目标格式: TikTok竖屏 (1080×1920)
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class SSSCongruence(Scene):
    """
    SSS全等三角形判定动画
    
    场景顺序:
    1. 开场钩子 (0-4秒)
    2. 引入两个三角形 (4-10秒)
    3. 标注第一对边相等 AB=DE (10-16秒)
    4. 标注第二对边相等 BC=EF (16-22秒)
    5. 标注第三对边相等 CA=FD (22-28秒)
    6. 演示全等（重合） (28-38秒)
    7. 总结SSS判定 (38-50秒)
    8. 片尾关注 (50-60秒)
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_TRIANGLE_1 = BLUE
        self.COLOR_TRIANGLE_2 = RED
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_EQUAL_MARK = GREEN
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_SUCCESS = GREEN
        
        # 初始化几何数据（使用验证脚本的精确坐标）
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_introduce_triangles()
        self.scene_3_first_pair_AB_DE()
        self.scene_4_second_pair_BC_EF()
        self.scene_5_third_pair_CA_FD()
        self.scene_6_demonstrate_congruence()
        self.scene_7_summary()
        self.scene_8_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据（精确坐标来自验证脚本）"""
        
        # ===== 精确坐标（验证通过） =====
        self.A = np.array([-3.4, 1.0, 0.0])
        self.B = np.array([-1.8, 1.0, 0.0])
        self.C = np.array([-2.6, 2.2, 0.0])
        self.D = np.array([1.8, 1.0, 0.0])
        self.E = np.array([3.4, 1.0, 0.0])
        self.F = np.array([2.6, 2.2, 0.0])
        
        # ===== 边长（已验证） =====
        self.AB_length = 1.6
        self.BC_length = 1.442221
        self.CA_length = 1.442221
        
        # ===== 中点（用于等号标记） =====
        self.M_AB = (self.A + self.B) / 2
        self.M_BC = (self.B + self.C) / 2
        self.M_CA = (self.C + self.A) / 2
        self.M_DE = (self.D + self.E) / 2
        self.M_EF = (self.E + self.F) / 2
        self.M_FD = (self.F + self.D) / 2
        
        print("✓ 几何数据初始化完成（坐标已验证）")
    
    def create_equal_mark(self, start, end, num_ticks=1, color=None):
        """
        创建等号标记（刻度线）
        num_ticks: 1=单刻度, 2=双刻度, 3=三刻度
        """
        if color is None:
            color = self.COLOR_EQUAL_MARK
        
        # 计算中点和垂直方向
        midpoint = (start + end) / 2
        edge_vec = end - start
        perp_vec = np.array([-edge_vec[1], edge_vec[0], 0])
        perp_vec = perp_vec / np.linalg.norm(perp_vec) * 0.15  # 刻度线长度
        
        # 创建刻度线组
        ticks = VGroup()
        
        if num_ticks == 1:
            # 单刻度线
            tick = Line(
                midpoint - perp_vec,
                midpoint + perp_vec,
                color=color,
                stroke_width=3
            )
            ticks.add(tick)
        
        elif num_ticks == 2:
            # 双刻度线
            offset = edge_vec / np.linalg.norm(edge_vec) * 0.08
            tick1 = Line(
                midpoint - offset - perp_vec,
                midpoint - offset + perp_vec,
                color=color,
                stroke_width=3
            )
            tick2 = Line(
                midpoint + offset - perp_vec,
                midpoint + offset + perp_vec,
                color=color,
                stroke_width=3
            )
            ticks.add(tick1, tick2)
        
        elif num_ticks == 3:
            # 三刻度线
            offset = edge_vec / np.linalg.norm(edge_vec) * 0.12
            tick1 = Line(
                midpoint - offset - perp_vec,
                midpoint - offset + perp_vec,
                color=color,
                stroke_width=3
            )
            tick2 = Line(
                midpoint - perp_vec,
                midpoint + perp_vec,
                color=color,
                stroke_width=3
            )
            tick3 = Line(
                midpoint + offset - perp_vec,
                midpoint + offset + perp_vec,
                color=color,
                stroke_width=3
            )
            ticks.add(tick1, tick2, tick3)
        
        return ticks
    
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
            "两个三角形什么时候全等？",
            font="PingFang SC",
            font_size=38,
            color=YELLOW
        ).move_to(UP * 6)
        
        subtitle = Text(
            "只知道边长就够了！",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(Write(hook_text), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 两个神秘三角形轮廓
        triangle_ABC_ghost = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_TRIANGLE_1,
            fill_opacity=0.2,
            stroke_width=2
        )
        
        triangle_DEF_ghost = Polygon(
            self.D, self.E, self.F,
            color=self.COLOR_TRIANGLE_2,
            fill_opacity=0.2,
            stroke_width=2
        )
        
        self.play(
            FadeIn(triangle_ABC_ghost),
            FadeIn(triangle_DEF_ghost),
            run_time=0.8
        )
        
        self.play(
            Indicate(VGroup(triangle_ABC_ghost, triangle_DEF_ghost), color=YELLOW),
            run_time=0.6
        )
        
        self.wait(1.1)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(subtitle),
            FadeOut(triangle_ABC_ghost),
            FadeOut(triangle_DEF_ghost),
            run_time=0.6
        )
    
    def scene_2_introduce_triangles(self):
        """场景2: 引入两个三角形"""
        
        # 标题
        title = Text(
            "SSS判定法则",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        
        definition = Text(
            "三边分别相等 → 全等",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 三角形ABC
        self.triangle_ABC = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_TRIANGLE_1,
            stroke_width=3
        )
        
        self.play(Create(self.triangle_ABC), run_time=1.0)
        
        # ABC标签
        self.label_A = Text("A", font="PingFang SC", font_size=20, color=WHITE).next_to(self.A, DL, buff=0.1)
        self.label_B = Text("B", font="PingFang SC", font_size=20, color=WHITE).next_to(self.B, DR, buff=0.1)
        self.label_C = Text("C", font="PingFang SC", font_size=20, color=WHITE).next_to(self.C, UP, buff=0.1)
        
        self.play(
            Write(self.label_A),
            Write(self.label_B),
            Write(self.label_C),
            run_time=0.6
        )
        
        # 三角形DEF
        self.triangle_DEF = Polygon(
            self.D, self.E, self.F,
            color=self.COLOR_TRIANGLE_2,
            stroke_width=3
        )
        
        self.play(Create(self.triangle_DEF), run_time=1.0)
        
        # DEF标签
        self.label_D = Text("D", font="PingFang SC", font_size=20, color=WHITE).next_to(self.D, DL, buff=0.1)
        self.label_E = Text("E", font="PingFang SC", font_size=20, color=WHITE).next_to(self.E, DR, buff=0.1)
        self.label_F = Text("F", font="PingFang SC", font_size=20, color=WHITE).next_to(self.F, UP, buff=0.1)
        
        self.play(
            Write(self.label_D),
            Write(self.label_E),
            Write(self.label_F),
            run_time=0.6
        )
        
        self.play(FadeIn(definition), run_time=0.5)
        self.wait(1.8)
        
        # 清理
        self.play(FadeOut(title), FadeOut(definition), run_time=0.5)
    
    def scene_3_first_pair_AB_DE(self):
        """场景3: 标注第一对边相等 AB=DE"""
        
        # 步骤提示
        step_text = Text(
            "第一步：比较AB和DE",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(step_text), run_time=0.4)
        
        # 高亮AB边
        ab_line = Line(self.A, self.B, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        self.play(Create(ab_line), run_time=0.5)
        
        # 高亮DE边
        de_line = Line(self.D, self.E, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        self.play(Create(de_line), run_time=0.5)
        
        # 边长标注
        length_AB = MathTex(f"{self.AB_length:.2f}", font_size=18, color=WHITE).next_to(self.M_AB, DOWN, buff=0.15)
        length_DE = MathTex(f"{self.AB_length:.2f}", font_size=18, color=WHITE).next_to(self.M_DE, DOWN, buff=0.15)
        
        self.play(FadeIn(length_AB), run_time=0.4)
        self.play(FadeIn(length_DE), run_time=0.4)
        
        # 等号标记（双刻度线）
        self.equal_mark_AB = self.create_equal_mark(self.A, self.B, num_ticks=2)
        self.equal_mark_DE = self.create_equal_mark(self.D, self.E, num_ticks=2)
        
        self.play(
            Create(self.equal_mark_AB),
            Create(self.equal_mark_DE),
            run_time=0.6
        )
        
        # 公式
        self.formula_1 = MathTex("AB = DE", font_size=28, color=self.COLOR_EQUAL_MARK).move_to(DOWN * 5.5)
        
        self.play(Write(self.formula_1), run_time=0.6)
        self.play(Flash(self.formula_1, color=self.COLOR_EQUAL_MARK), run_time=0.4)
        
        self.wait(2.2)
        
        # 恢复边的颜色
        self.play(
            FadeOut(ab_line),
            FadeOut(de_line),
            FadeOut(length_AB),
            FadeOut(length_DE),
            FadeOut(step_text),
            run_time=0.4
        )
        
        # 公式移至汇总区（左侧）
        self.play(
            self.formula_1.animate.scale(0.7).move_to(LEFT * 3.5 + DOWN * 5.5),
            run_time=0.3
        )
    
    def scene_4_second_pair_BC_EF(self):
        """场景4: 标注第二对边相等 BC=EF"""
        
        # 步骤提示
        step_text = Text(
            "第二步：比较BC和EF",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(step_text), run_time=0.4)
        
        # 高亮BC边
        bc_line = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        self.play(Create(bc_line), run_time=0.5)
        
        # 高亮EF边
        ef_line = Line(self.E, self.F, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        self.play(Create(ef_line), run_time=0.5)
        
        # 边长标注
        length_BC = MathTex(f"{self.BC_length:.2f}", font_size=18, color=WHITE).next_to(self.M_BC, RIGHT, buff=0.15)
        length_EF = MathTex(f"{self.BC_length:.2f}", font_size=18, color=WHITE).next_to(self.M_EF, LEFT, buff=0.15)
        
        self.play(FadeIn(length_BC), run_time=0.4)
        self.play(FadeIn(length_EF), run_time=0.4)
        
        # 等号标记（三刻度线）
        self.equal_mark_BC = self.create_equal_mark(self.B, self.C, num_ticks=3)
        self.equal_mark_EF = self.create_equal_mark(self.E, self.F, num_ticks=3)
        
        self.play(
            Create(self.equal_mark_BC),
            Create(self.equal_mark_EF),
            run_time=0.6
        )
        
        # 公式
        self.formula_2 = MathTex("BC = EF", font_size=28, color=self.COLOR_EQUAL_MARK).move_to(DOWN * 5.5)
        
        self.play(Write(self.formula_2), run_time=0.6)
        self.play(Flash(self.formula_2, color=self.COLOR_EQUAL_MARK), run_time=0.4)
        
        self.wait(2.2)
        
        # 清理
        self.play(
            FadeOut(bc_line),
            FadeOut(ef_line),
            FadeOut(length_BC),
            FadeOut(length_EF),
            FadeOut(step_text),
            run_time=0.4
        )
        
        # 公式移至汇总区
        self.play(
            self.formula_2.animate.scale(0.7).move_to(ORIGIN + DOWN * 5.5),
            run_time=0.3
        )
    
    def scene_5_third_pair_CA_FD(self):
        """场景5: 标注第三对边相等 CA=FD"""
        
        # 步骤提示
        step_text = Text(
            "第三步：比较CA和FD",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(step_text), run_time=0.4)
        
        # 高亮CA边
        ca_line = Line(self.C, self.A, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        self.play(Create(ca_line), run_time=0.5)
        
        # 高亮FD边
        fd_line = Line(self.F, self.D, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        self.play(Create(fd_line), run_time=0.5)
        
        # 边长标注
        length_CA = MathTex(f"{self.CA_length:.2f}", font_size=18, color=WHITE).next_to(self.M_CA, LEFT, buff=0.15)
        length_FD = MathTex(f"{self.CA_length:.2f}", font_size=18, color=WHITE).next_to(self.M_FD, RIGHT, buff=0.15)
        
        self.play(FadeIn(length_CA), run_time=0.4)
        self.play(FadeIn(length_FD), run_time=0.4)
        
        # 等号标记（单刻度线）
        self.equal_mark_CA = self.create_equal_mark(self.C, self.A, num_ticks=1)
        self.equal_mark_FD = self.create_equal_mark(self.F, self.D, num_ticks=1)
        
        self.play(
            Create(self.equal_mark_CA),
            Create(self.equal_mark_FD),
            run_time=0.6
        )
        
        # 公式
        self.formula_3 = MathTex("CA = FD", font_size=28, color=self.COLOR_EQUAL_MARK).move_to(DOWN * 5.5)
        
        self.play(Write(self.formula_3), run_time=0.6)
        self.play(Flash(self.formula_3, color=self.COLOR_EQUAL_MARK), run_time=0.4)
        
        self.wait(2.2)
        
        # 清理
        self.play(
            FadeOut(ca_line),
            FadeOut(fd_line),
            FadeOut(length_CA),
            FadeOut(length_FD),
            FadeOut(step_text),
            run_time=0.4
        )
        
        # 公式移至汇总区
        self.play(
            self.formula_3.animate.scale(0.7).move_to(RIGHT * 3.5 + DOWN * 5.5),
            run_time=0.3
        )
    
    def scene_6_demonstrate_congruence(self):
        """场景6: 演示全等（重合）"""
        
        # 提示文字
        hint = Text(
            "三边相等，两个三角形...",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(hint), run_time=0.5)
        
        # 所有等号标记闪烁
        all_marks = VGroup(
            self.equal_mark_AB, self.equal_mark_DE,
            self.equal_mark_BC, self.equal_mark_EF,
            self.equal_mark_CA, self.equal_mark_FD
        )
        
        self.play(Indicate(all_marks, color=YELLOW), run_time=0.6)
        
        # 创建DEF的副本用于移动
        triangle_DEF_copy = self.triangle_DEF.copy().set_opacity(0.6)
        
        self.play(FadeIn(triangle_DEF_copy), run_time=0.3)
        
        # 计算变换：使D对齐A
        # DEF和ABC形状完全相同，只需平移
        translation = self.A - self.D
        
        # 移动并重合
        self.play(
            triangle_DEF_copy.animate.shift(translation),
            run_time=2.0
        )
        
        # 完全重合，变为绿色
        self.play(
            triangle_DEF_copy.animate.set_color(self.COLOR_SUCCESS).set_opacity(1),
            run_time=0.8
        )
        
        # 全等符号
        congruence_symbol = MathTex(r"\cong", font_size=48, color=YELLOW).move_to(DOWN * 3.5)
        
        self.play(Write(congruence_symbol), run_time=0.6)
        
        # 完整公式
        final_formula = MathTex(
            r"\triangle ABC \cong \triangle DEF \text{ (SSS)}",
            font_size=32,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 4.8)
        
        # 修正：中文不能在MathTex中，需要分离
        final_formula_parts = VGroup(
            MathTex(r"\triangle ABC \cong \triangle DEF", font_size=32, color=self.COLOR_SUCCESS),
            Text("(SSS)", font="PingFang SC", font_size=28, color=self.COLOR_SUCCESS)
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 4.8)
        
        self.play(Write(final_formula_parts), run_time=1.0)
        
        # 庆祝闪光
        self.play(
            Flash(triangle_DEF_copy, color=self.COLOR_SUCCESS, flash_radius=1.5),
            run_time=0.8
        )
        
        self.wait(3.4)
        
        # 清理
        self.play(
            FadeOut(triangle_DEF_copy),
            FadeOut(hint),
            FadeOut(congruence_symbol),
            FadeOut(all_marks),
            FadeOut(self.formula_1),
            FadeOut(self.formula_2),
            FadeOut(self.formula_3),
            run_time=0.6
        )
        
        self.final_formula = final_formula_parts  # 保留
    
    def scene_7_summary(self):
        """场景7: 总结SSS判定法则"""
        
        # 清理屏幕
        self.play(
            FadeOut(self.triangle_ABC),
            FadeOut(self.triangle_DEF),
            FadeOut(self.label_A),
            FadeOut(self.label_B),
            FadeOut(self.label_C),
            FadeOut(self.label_D),
            FadeOut(self.label_E),
            FadeOut(self.label_F),
            FadeOut(self.final_formula),
            run_time=0.6
        )
        
        # 标题卡片
        title_card = VGroup(
            Text("SSS判定法则", font="PingFang SC", font_size=42, color=GOLD),
            Text("Side-Side-Side", font="PingFang SC", font_size=24, color=GRAY_A)
        ).arrange(DOWN, buff=0.3).move_to(UP * 4)
        
        self.play(FadeIn(title_card, shift=DOWN * 0.3), run_time=0.5)
        
        # 定义
        definition = Text(
            "三边分别对应相等的两个三角形全等",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(Write(definition), run_time=1.2)
        
        # 口诀卡片
        slogan = VGroup(
            Text("边边边", font="PingFang SC", font_size=36, color=YELLOW),
            Text("三边等", font="PingFang SC", font_size=36, color=YELLOW),
            Text("全等定！", font="PingFang SC", font_size=36, color=YELLOW)
        ).arrange(RIGHT, buff=0.5).move_to(UP * 0.3)
        
        # 从左侧滑入
        slogan.shift(LEFT * 10)
        self.play(slogan.animate.shift(RIGHT * 10), run_time=0.8)
        
        # 要点列表
        point_1 = VGroup(
            Text("✓", font="PingFang SC", font_size=24, color=GREEN),
            Text("只需证明三对边相等", font="PingFang SC", font_size=22, color=GRAY_A)
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.5)
        
        point_2 = VGroup(
            Text("✓", font="PingFang SC", font_size=24, color=GREEN),
            Text("不需要证明角的关系", font="PingFang SC", font_size=22, color=GRAY_A)
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.5)
        
        point_3 = VGroup(
            Text("✓", font="PingFang SC", font_size=24, color=GREEN),
            Text("注意对应关系要正确", font="PingFang SC", font_size=22, color=GRAY_A)
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.5)
        
        self.play(FadeIn(point_1, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(point_2, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(point_3, shift=UP * 0.2), run_time=0.5)
        
        # 强调框
        emphasis_box = SurroundingRectangle(
            VGroup(point_1, point_2, point_3),
            color=YELLOW,
            buff=0.3,
            corner_radius=0.1
        )
        
        self.play(Create(emphasis_box), run_time=0.6)
        
        self.wait(5.8)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title_card, definition, slogan,
                point_1, point_2, point_3, emphasis_box
            )),
            run_time=0.8
        )
    
    def scene_8_outro(self):
        """场景8: 片尾关注"""
        
        # 作者名放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        
        # 账号ID
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注文字
        follow_text = Text(
            "关注我，掌握更多全等判定方法！",
            font="PingFang SC",
            font_size=28,
            color=YELLOW
        ).move_to(DOWN * 0.8)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        
        # 三角形装饰（旋转）
        decoration_triangles = VGroup(*[
            Polygon(ORIGIN, RIGHT * 0.3, UP * 0.3, color=GOLD, fill_opacity=0.8)
            .scale(0.4)
            .move_to(follow_text.get_center() + 1.8 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in decoration_triangles],
            run_time=0.6
        )
        
        self.play(Rotate(decoration_triangles, angle=PI, run_time=1.5))
        
        # SSS图标
        sss_icons = VGroup(
            Text("S", font="PingFang SC", font_size=32, color=BLUE),
            Text("S", font="PingFang SC", font_size=32, color=RED),
            Text("S", font="PingFang SC", font_size=32, color=GREEN)
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 2.5)
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in sss_icons],
            run_time=0.8
        )
        
        # 结束语
        outro_text = Text(
            "SAS、ASA、AAS...下期见！",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Write(outro_text), run_time=1.0)
        
        self.wait(4.0)
        
        # 最终淡出
        self.play(
            FadeOut(VGroup(
                self.author_info, author_id, follow_text,
                decoration_triangles, sss_icons, outro_text
            )),
            run_time=1.0
        )


# 运行命令:
# manim -pql sss_congruence.py SSSCongruence    # 快速预览 (480p 15fps)
# manim -qm sss_congruence.py SSSCongruence     # 中等质量 (720p 30fps)
# manim -qh sss_congruence.py SSSCongruence     # 高质量 (1080p 60fps)