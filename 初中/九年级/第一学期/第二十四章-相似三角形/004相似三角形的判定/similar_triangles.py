"""
相似三角形的判定 - Similar Triangle Determination Theorems
使用 Manim 创建的九年级几何教学视频

内容: AA, SAS, SSS 三种判定方法
目标观众: 九年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ==================== 全局配置 ====================

# TikTok 竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class SimilarTriangles(Scene):
    """相似三角形判定定理动画场景"""
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主三角形
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 次三角形
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮重点
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助元素
        self.COLOR_SUCCESS = "#2ecc71"       # 绿色 - 判定成功
        
        # 字体大小规范
        self.FONT_SIZES = {
            "title": 36,
            "subtitle": 28,
            "body": 22,
            "label": 20,
            "small": 18,
            "author": 20,
            "formula": 28,
        }
        
        # 初始化所有几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_overview()
        self.scene_3_aa_determination()
        self.scene_4_sas_determination()
        self.scene_5_sss_determination()
        self.scene_6_summary()
        self.scene_7_tips()
        self.scene_8_outro()
    
    def setup_geometry(self):
        """统一初始化所有几何数据"""
        print("正在初始化几何数据...")
        
        # ========== Scene 1: 开场三角形 ==========
        self.intro_A = np.array([-2.5, 0, 0]) * 0.8 + UP * 2.5
        self.intro_B = np.array([2.5, 0, 0]) * 0.8 + UP * 2.5
        self.intro_C = np.array([0, 3, 0]) * 0.8 + UP * 2.5
        
        intro_centroid = (self.intro_A + self.intro_B + self.intro_C) / 3
        scale = 0.5
        offset = DOWN * 1.0
        self.intro_D = (self.intro_A - intro_centroid) * scale + offset
        self.intro_E = (self.intro_B - intro_centroid) * scale + offset
        self.intro_F = (self.intro_C - intro_centroid) * scale + offset
        
        # ========== Scene 3: AA判定 ==========
        # △ABC
        self.AA_A = np.array([-2.0, 0, 0]) + UP * 2
        self.AA_B = np.array([2.0, 0, 0]) + UP * 2
        
        angle_A_deg = 60
        angle_B_deg = 50
        angle_C_deg = 180 - angle_A_deg - angle_B_deg
        
        self.AA_angle_A_rad = np.radians(angle_A_deg)
        self.AA_angle_B_rad = np.radians(angle_B_deg)
        self.AA_angle_C_rad = np.radians(angle_C_deg)
        
        c_length = np.linalg.norm(self.AA_B - self.AA_A)
        a_length = c_length * np.sin(self.AA_angle_A_rad) / np.sin(self.AA_angle_C_rad)
        b_length = c_length * np.sin(self.AA_angle_B_rad) / np.sin(self.AA_angle_C_rad)
        
        direction_AC = np.array([np.cos(self.AA_angle_A_rad), np.sin(self.AA_angle_A_rad), 0])
        self.AA_C = self.AA_A + b_length * direction_AC
        
        # △DEF
        scale_ratio = 0.6
        offset = np.array([0, -3.0, 0])
        centroid_ABC = (self.AA_A + self.AA_B + self.AA_C) / 3
        
        self.AA_D = (self.AA_A - centroid_ABC) * scale_ratio + offset
        self.AA_E = (self.AA_B - centroid_ABC) * scale_ratio + offset
        self.AA_F = (self.AA_C - centroid_ABC) * scale_ratio + offset
        
        # ========== Scene 4: SAS判定 ==========
        self.SAS_A = np.array([-2.5, 1.0, 0])
        self.SAS_angle_A_rad = np.radians(70)
        self.SAS_length_AB = 3.5
        self.SAS_length_AC = 2.8
        
        self.SAS_B = self.SAS_A + self.SAS_length_AB * RIGHT
        self.SAS_C = self.SAS_A + self.SAS_length_AC * np.array([
            np.cos(self.SAS_angle_A_rad), 
            np.sin(self.SAS_angle_A_rad), 
            0
        ])
        
        # △DEF
        k = 0.65
        self.SAS_length_DE = self.SAS_length_AB * k
        self.SAS_length_DF = self.SAS_length_AC * k
        offset = np.array([0.3, -2.0, 0])
        
        self.SAS_D = np.array([-2.5, -1.0, 0]) + offset
        self.SAS_E = self.SAS_D + self.SAS_length_DE * RIGHT
        self.SAS_F = self.SAS_D + self.SAS_length_DF * np.array([
            np.cos(self.SAS_angle_A_rad),
            np.sin(self.SAS_angle_A_rad),
            0
        ])
        
        self.SAS_ratio = 1 / k
        
        # ========== Scene 5: SSS判定 ==========
        self.SSS_A = np.array([-2.5, 1.5, 0])
        self.SSS_B = np.array([2.5, -0.5, 0])
        
        self.SSS_length_AB = np.linalg.norm(self.SSS_B - self.SSS_A)
        self.SSS_length_BC = 4.0
        self.SSS_length_CA = 3.5
        
        # 通过余弦定理计算C点
        cos_B = (self.SSS_length_AB**2 + self.SSS_length_BC**2 - self.SSS_length_CA**2) / \
                (2 * self.SSS_length_AB * self.SSS_length_BC)
        angle_B = np.arccos(np.clip(cos_B, -1.0, 1.0))
        
        direction_BA = (self.SSS_A - self.SSS_B) / self.SSS_length_AB
        cos_ang = np.cos(angle_B)
        sin_ang = np.sin(angle_B)
        rotation_matrix = np.array([
            [cos_ang, -sin_ang, 0],
            [sin_ang, cos_ang, 0],
            [0, 0, 1]
        ])
        direction_BC = rotation_matrix @ direction_BA
        self.SSS_C = self.SSS_B + self.SSS_length_BC * direction_BC
        
        # △DEF
        k = 0.7
        offset = np.array([0, -2.3, 0])
        centroid_ABC = (self.SSS_A + self.SSS_B + self.SSS_C) / 3
        
        self.SSS_D = (self.SSS_A - centroid_ABC) * k + offset
        self.SSS_E = (self.SSS_B - centroid_ABC) * k + offset
        self.SSS_F = (self.SSS_C - centroid_ABC) * k + offset
        
        self.SSS_ratio = 1 / k
        
        print("✓ 几何数据初始化完成")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=self.FONT_SIZES["author"],
            color=GRAY_B
        ).move_to(UP * 7.3)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook = Text(
            "如何判断两个三角形相似?",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook), run_time=0.8)
        
        # 创建两个三角形
        triangle1 = Polygon(
            self.intro_A, self.intro_B, self.intro_C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        triangle2 = Polygon(
            self.intro_D, self.intro_E, self.intro_F,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        )
        
        self.play(Create(triangle1), run_time=0.8)
        self.play(Create(triangle2), run_time=0.8)
        
        # 相似符号
        similarity = MathTex(r"\sim", font_size=60, color=YELLOW).move_to(ORIGIN)
        self.play(FadeIn(similarity, scale=1.2), run_time=0.4)
        
        self.wait(1.0)
        
        # 提示文字
        hint = Text(
            "三种判定方法",
            font="PingFang SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=WHITE
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(triangle1),
            FadeOut(triangle2),
            FadeOut(similarity),
            FadeOut(hint),
            run_time=0.5
        )
    
    def scene_2_overview(self):
        """场景2: 判定定理总览"""
        title = Text(
            "相似三角形判定定理",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建三个判定方法卡片
        card_aa = self.create_method_card("AA", "两角对应相等", self.COLOR_PRIMARY, UP * 3)
        card_sas = self.create_method_card("SAS", "两边成比例且夹角相等", self.COLOR_SECONDARY, UP * 1)
        card_sss = self.create_method_card("SSS", "三边对应成比例", self.COLOR_SUCCESS, DOWN * 1)
        
        # 卡片初始位置在左侧外
        for card in [card_aa, card_sas, card_sss]:
            card.shift(LEFT * 10)
        
        # 依次滑入
        self.play(card_aa.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.3)
        self.play(card_sas.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.3)
        self.play(card_sss.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(card_aa),
            FadeOut(card_sas),
            FadeOut(card_sss),
            run_time=0.5
        )
    
    def create_method_card(self, method, description, color, position):
        """创建判定方法卡片"""
        # 图标圆
        icon = Circle(radius=0.25, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 方法名
        method_text = Text(
            method,
            font="PingFang SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=WHITE,
            weight=BOLD
        )
        
        # 说明
        desc_text = Text(
            description,
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, method_text, desc_text).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        
        return card
    
    def scene_3_aa_determination(self):
        """场景3: AA判定详解"""
        title = Text(
            "判定方法一: AA (角-角)",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 创建△ABC
        triangle_abc = Polygon(
            self.AA_A, self.AA_B, self.AA_C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        self.play(Create(triangle_abc), run_time=1.0)
        
        # 顶点标签
        label_a = Text("A", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.AA_A, DL, buff=0.1)
        label_b = Text("B", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.AA_B, DR, buff=0.1)
        label_c = Text("C", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.AA_C, UP, buff=0.1)
        
        self.play(Write(VGroup(label_a, label_b, label_c)), run_time=0.6)
        
        # 标记∠A
        line_ab = Line(self.AA_A, self.AA_B)
        line_ac = Line(self.AA_A, self.AA_C)
        angle_a = Angle(line_ab, line_ac, radius=0.4, color=self.COLOR_HIGHLIGHT)
        angle_a_label = MathTex("60^\\circ", font_size=self.FONT_SIZES["small"], color=self.COLOR_HIGHLIGHT)\
            .next_to(angle_a, RIGHT, buff=0.15)
        
        self.play(Create(angle_a), run_time=0.6)
        self.play(FadeIn(angle_a_label), run_time=0.4)
        
        # 标记∠B
        line_ba = Line(self.AA_B, self.AA_A)
        line_bc = Line(self.AA_B, self.AA_C)
        angle_b = Angle(line_bc, line_ba, radius=0.4, color=self.COLOR_HIGHLIGHT, other_angle=True)
        angle_b_label = MathTex("50^\\circ", font_size=self.FONT_SIZES["small"], color=self.COLOR_HIGHLIGHT)\
            .next_to(angle_b, LEFT, buff=0.15)
        
        self.play(Create(angle_b), run_time=0.6)
        self.play(FadeIn(angle_b_label), run_time=0.4)
        
        self.wait(0.5)
        
        # 创建△DEF
        triangle_def = Polygon(
            self.AA_D, self.AA_E, self.AA_F,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        )
        
        self.play(Create(triangle_def), run_time=1.0)
        
        # 顶点标签
        label_d = Text("D", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.AA_D, DL, buff=0.1)
        label_e = Text("E", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.AA_E, DR, buff=0.1)
        label_f = Text("F", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.AA_F, UP, buff=0.1)
        
        self.play(Write(VGroup(label_d, label_e, label_f)), run_time=0.6)
        
        # 标记∠D
        line_de = Line(self.AA_D, self.AA_E)
        line_df = Line(self.AA_D, self.AA_F)
        angle_d = Angle(line_de, line_df, radius=0.25, color=self.COLOR_HIGHLIGHT)
        angle_d_label = MathTex("60^\\circ", font_size=self.FONT_SIZES["small"], color=self.COLOR_HIGHLIGHT)\
            .next_to(angle_d, RIGHT, buff=0.1)
        
        self.play(Create(angle_d), FadeIn(angle_d_label), run_time=0.8)
        
        # 高亮角度相等
        self.play(
            Flash(angle_a, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            Flash(angle_d, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            run_time=0.6
        )
        
        # 标记∠E
        line_ed = Line(self.AA_E, self.AA_D)
        line_ef = Line(self.AA_E, self.AA_F)
        angle_e = Angle(line_ef, line_ed, radius=0.25, color=self.COLOR_HIGHLIGHT, other_angle=True)
        angle_e_label = MathTex("50^\\circ", font_size=self.FONT_SIZES["small"], color=self.COLOR_HIGHLIGHT)\
            .next_to(angle_e, LEFT, buff=0.1)
        
        self.play(Create(angle_e), FadeIn(angle_e_label), run_time=0.8)
        
        # 高亮角度相等
        self.play(
            Flash(angle_b, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            Flash(angle_e, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            run_time=0.6
        )
        
        # 显示判定公式
        formula = MathTex(
            r"\angle A = \angle D, \ \angle B = \angle E",
            r"\Rightarrow",
            r"\triangle ABC \sim \triangle DEF",
            font_size=self.FONT_SIZES["formula"]
        ).move_to(DOWN * 5.5)
        formula[0].set_color(self.COLOR_HIGHLIGHT)
        formula[2].set_color(self.COLOR_SUCCESS)
        
        self.play(Write(formula), run_time=1.0)
        
        # 结论
        conclusion = Text(
            "✓ 两角对应相等 → 三角形相似",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(conclusion, scale=1.1), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(triangle_abc),
            FadeOut(triangle_def),
            FadeOut(VGroup(label_a, label_b, label_c, label_d, label_e, label_f)),
            FadeOut(VGroup(angle_a, angle_b, angle_d, angle_e)),
            FadeOut(VGroup(angle_a_label, angle_b_label, angle_d_label, angle_e_label)),
            FadeOut(formula),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def scene_4_sas_determination(self):
        """场景4: SAS判定详解"""
        title = Text(
            "判定方法二: SAS (边-角-边)",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_SECONDARY
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 创建△ABC
        triangle_abc = Polygon(
            self.SAS_A, self.SAS_B, self.SAS_C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        self.play(Create(triangle_abc), run_time=1.0)
        
        # 顶点标签
        label_a = Text("A", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.SAS_A, LEFT, buff=0.1)
        label_b = Text("B", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.SAS_B, RIGHT, buff=0.1)
        label_c = Text("C", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.SAS_C, UP, buff=0.1)
        
        self.play(Write(VGroup(label_a, label_b, label_c)), run_time=0.6)
        
        # 高亮AB边
        line_ab = Line(self.SAS_A, self.SAS_B, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        label_ab = MathTex("3.5", font_size=self.FONT_SIZES["small"], color=self.COLOR_HIGHLIGHT)\
            .next_to((self.SAS_A + self.SAS_B) / 2, DOWN, buff=0.2)
        
        self.play(Create(line_ab), FadeIn(label_ab), run_time=0.7)
        self.play(line_ab.animate.set_color(self.COLOR_PRIMARY), run_time=0.3)
        
        # 高亮AC边
        line_ac = Line(self.SAS_A, self.SAS_C, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        label_ac = MathTex("2.8", font_size=self.FONT_SIZES["small"], color=self.COLOR_HIGHLIGHT)\
            .next_to((self.SAS_A + self.SAS_C) / 2, LEFT, buff=0.2)
        
        self.play(Create(line_ac), FadeIn(label_ac), run_time=0.7)
        self.play(line_ac.animate.set_color(self.COLOR_PRIMARY), run_time=0.3)
        
        # 标记夹角∠A
        line_ab_for_angle = Line(self.SAS_A, self.SAS_B)
        line_ac_for_angle = Line(self.SAS_A, self.SAS_C)
        angle_a = Angle(line_ab_for_angle, line_ac_for_angle, radius=0.4, color=self.COLOR_HIGHLIGHT)
        angle_a_label = MathTex("70^\\circ", font_size=self.FONT_SIZES["small"], color=self.COLOR_HIGHLIGHT)\
            .next_to(angle_a, UR, buff=0.15)
        
        self.play(Create(angle_a), FadeIn(angle_a_label), run_time=0.7)
        
        self.wait(0.5)
        
        # 创建△DEF
        triangle_def = Polygon(
            self.SAS_D, self.SAS_E, self.SAS_F,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        )
        
        self.play(Create(triangle_def), run_time=1.0)
        
        # 顶点标签
        label_d = Text("D", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.SAS_D, LEFT, buff=0.1)
        label_e = Text("E", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.SAS_E, RIGHT, buff=0.1)
        label_f = Text("F", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.SAS_F, UP, buff=0.1)
        
        self.play(Write(VGroup(label_d, label_e, label_f)), run_time=0.6)
        
        # 高亮DE边和DF边，显示边长
        line_de = Line(self.SAS_D, self.SAS_E, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        label_de = MathTex("2.28", font_size=self.FONT_SIZES["small"], color=self.COLOR_HIGHLIGHT)\
            .next_to((self.SAS_D + self.SAS_E) / 2, DOWN, buff=0.2)
        
        line_df = Line(self.SAS_D, self.SAS_F, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        label_df = MathTex("1.82", font_size=self.FONT_SIZES["small"], color=self.COLOR_HIGHLIGHT)\
            .next_to((self.SAS_D + self.SAS_F) / 2, LEFT, buff=0.2)
        
        self.play(Create(line_de), FadeIn(label_de), run_time=0.7)
        self.play(line_de.animate.set_color(self.COLOR_SECONDARY), run_time=0.3)
        self.play(Create(line_df), FadeIn(label_df), run_time=0.7)
        self.play(line_df.animate.set_color(self.COLOR_SECONDARY), run_time=0.3)
        
        # 显示比例关系
        ratio_text = MathTex(
            r"\frac{AB}{DE} = \frac{AC}{DF} \approx 1.54",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(Write(ratio_text), run_time=1.0)
        
        # 标记夹角∠D
        line_de_for_angle = Line(self.SAS_D, self.SAS_E)
        line_df_for_angle = Line(self.SAS_D, self.SAS_F)
        angle_d = Angle(line_de_for_angle, line_df_for_angle, radius=0.25, color=self.COLOR_HIGHLIGHT)
        angle_d_label = MathTex("70^\\circ", font_size=self.FONT_SIZES["small"], color=self.COLOR_HIGHLIGHT)\
            .next_to(angle_d, UR, buff=0.1)
        
        self.play(Create(angle_d), FadeIn(angle_d_label), run_time=0.7)
        
        # 高亮角度相等
        self.play(
            Flash(angle_a, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            Flash(angle_d, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            run_time=0.6
        )
        
        # 显示判定公式
        formula = MathTex(
            r"\frac{AB}{DE} = \frac{AC}{DF}, \ \angle A = \angle D",
            r"\Rightarrow",
            r"\triangle ABC \sim \triangle DEF",
            font_size=self.FONT_SIZES["formula"] - 4
        ).move_to(DOWN * 5.8)
        formula[0].set_color(self.COLOR_HIGHLIGHT)
        formula[2].set_color(self.COLOR_SUCCESS)
        
        self.play(Write(formula), run_time=1.0)
        
        # 结论
        conclusion = Text(
            "✓ 两边成比例 + 夹角相等 → 三角形相似",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 6.8)
        
        self.play(FadeIn(conclusion, scale=1.1), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, triangle_abc, triangle_def,
                label_a, label_b, label_c, label_d, label_e, label_f,
                line_ab, line_ac, line_de, line_df,
                label_ab, label_ac, label_de, label_df,
                angle_a, angle_d, angle_a_label, angle_d_label,
                ratio_text, formula, conclusion
            )),
            run_time=0.6
        )
    
    def scene_5_sss_determination(self):
        """场景5: SSS判定详解"""
        title = Text(
            "判定方法三: SSS (边-边-边)",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_SUCCESS
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 创建△ABC
        triangle_abc = Polygon(
            self.SSS_A, self.SSS_B, self.SSS_C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        self.play(Create(triangle_abc), run_time=1.0)
        
        # 顶点标签
        label_a = Text("A", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.SSS_A, LEFT, buff=0.1)
        label_b = Text("B", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.SSS_B, RIGHT, buff=0.1)
        label_c = Text("C", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.SSS_C, DOWN, buff=0.1)
        
        self.play(Write(VGroup(label_a, label_b, label_c)), run_time=0.6)
        
        # 依次高亮三边
        edges_abc = [
            (self.SSS_A, self.SSS_B, "5.39", DOWN),
            (self.SSS_B, self.SSS_C, "4.00", RIGHT),
            (self.SSS_C, self.SSS_A, "3.50", LEFT)
        ]
        
        edge_lines = []
        edge_labels = []
        
        for start, end, length_str, direction in edges_abc:
            line = Line(start, end, color=self.COLOR_HIGHLIGHT, stroke_width=4)
            label = MathTex(length_str, font_size=self.FONT_SIZES["small"], color=self.COLOR_HIGHLIGHT)\
                .next_to((start + end) / 2, direction, buff=0.2)
            
            self.play(Create(line), FadeIn(label), run_time=0.6)
            self.play(line.animate.set_color(self.COLOR_PRIMARY), run_time=0.2)
            
            edge_lines.append(line)
            edge_labels.append(label)
        
        self.wait(0.3)
        
        # 创建△DEF
        triangle_def = Polygon(
            self.SSS_D, self.SSS_E, self.SSS_F,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        )
        
        self.play(Create(triangle_def), run_time=1.0)
        
        # 顶点标签
        label_d = Text("D", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.SSS_D, LEFT, buff=0.1)
        label_e = Text("E", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.SSS_E, RIGHT, buff=0.1)
        label_f = Text("F", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=WHITE)\
            .next_to(self.SSS_F, DOWN, buff=0.1)
        
        self.play(Write(VGroup(label_d, label_e, label_f)), run_time=0.6)
        
        # 依次高亮三边
        edges_def = [
            (self.SSS_D, self.SSS_E, "3.77", DOWN),
            (self.SSS_E, self.SSS_F, "2.80", RIGHT),
            (self.SSS_F, self.SSS_D, "2.45", LEFT)
        ]
        
        edge_lines_def = []
        edge_labels_def = []
        
        for start, end, length_str, direction in edges_def:
            line = Line(start, end, color=self.COLOR_HIGHLIGHT, stroke_width=4)
            label = MathTex(length_str, font_size=self.FONT_SIZES["small"], color=self.COLOR_HIGHLIGHT)\
                .next_to((start + end) / 2, direction, buff=0.2)
            
            self.play(Create(line), FadeIn(label), run_time=0.6)
            self.play(line.animate.set_color(self.COLOR_SECONDARY), run_time=0.2)
            
            edge_lines_def.append(line)
            edge_labels_def.append(label)
        
        # 显示三个比例
        ratio1 = MathTex(r"\frac{AB}{DE} \approx 1.43", font_size=self.FONT_SIZES["body"], 
                         color=self.COLOR_HIGHLIGHT).move_to(DOWN * 4.0)
        ratio2 = MathTex(r"\frac{BC}{EF} \approx 1.43", font_size=self.FONT_SIZES["body"], 
                         color=self.COLOR_HIGHLIGHT).move_to(DOWN * 4.8)
        ratio3 = MathTex(r"\frac{CA}{FD} \approx 1.43", font_size=self.FONT_SIZES["body"], 
                         color=self.COLOR_HIGHLIGHT).move_to(DOWN * 5.6)
        
        self.play(Write(ratio1), run_time=0.6)
        self.play(Write(ratio2), run_time=0.6)
        self.play(Write(ratio3), run_time=0.6)
        
        self.wait(0.5)
        
        # 合并比例
        unified_ratio = MathTex(
            r"\frac{AB}{DE} = \frac{BC}{EF} = \frac{CA}{FD} \approx 1.43",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.8)
        
        self.play(
            Transform(VGroup(ratio1, ratio2, ratio3), unified_ratio),
            run_time=0.8
        )
        
        # 显示判定公式
        formula = MathTex(
            r"\frac{AB}{DE} = \frac{BC}{EF} = \frac{CA}{FD}",
            r"\Rightarrow",
            r"\triangle ABC \sim \triangle DEF",
            font_size=self.FONT_SIZES["formula"] - 4
        ).move_to(DOWN * 6.2)
        formula[0].set_color(self.COLOR_HIGHLIGHT)
        formula[2].set_color(self.COLOR_SUCCESS)
        
        self.play(Write(formula), run_time=1.0)
        
        # 结论
        conclusion = Text(
            "✓ 三边对应成比例 → 三角形相似",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 7.2)
        
        self.play(FadeIn(conclusion, scale=1.1), run_time=0.6)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, triangle_abc, triangle_def,
                label_a, label_b, label_c, label_d, label_e, label_f,
                *edge_lines, *edge_labels, *edge_lines_def, *edge_labels_def,
                ratio1, ratio2, ratio3, unified_ratio, formula, conclusion
            )),
            run_time=0.6
        )
    
    def scene_6_summary(self):
        """场景6: 三种方法对比汇总"""
        title = Text(
            "三种判定方法对比",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title), run_time=0.6)
        
        # 创建对比卡片
        card_aa = self.create_summary_card(
            "AA", "两角对应相等 → 最简单",
            self.COLOR_PRIMARY, UP * 3.5
        )
        card_sas = self.create_summary_card(
            "SAS", "两边成比例 + 夹角相等 → 常用",
            self.COLOR_SECONDARY, UP * 1.5
        )
        card_sss = self.create_summary_card(
            "SSS", "三边对应成比例 → 最严格",
            self.COLOR_SUCCESS, DOWN * 0.5
        )
        
        # 初始位置在左侧
        for card in [card_aa, card_sas, card_sss]:
            card.shift(LEFT * 10)
        
        # 依次滑入
        self.play(card_aa.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.2)
        self.play(card_sas.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.2)
        self.play(card_sss.animate.shift(RIGHT * 10), run_time=0.5)
        
        # 高亮关键词
        self.wait(0.5)
        self.play(
            Flash(card_aa[1], color=self.COLOR_PRIMARY, flash_radius=0.5),
            run_time=0.4
        )
        self.play(
            Flash(card_sas[1], color=self.COLOR_SECONDARY, flash_radius=0.5),
            run_time=0.4
        )
        self.play(
            Flash(card_sss[1], color=self.COLOR_SUCCESS, flash_radius=0.5),
            run_time=0.4
        )
        
        # 总结提示
        summary = Text(
            "记住对应关系，灵活运用!",
            font="PingFang SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(summary, shift=UP * 0.3), run_time=0.8)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(title, card_aa, card_sas, card_sss, summary)),
            run_time=0.6
        )
    
    def create_summary_card(self, method, description, color, position):
        """创建汇总对比卡片"""
        # 方法名
        method_text = Text(
            method,
            font="PingFang SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=color,
            weight=BOLD
        )
        
        # 描述
        desc_text = Text(
            description,
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(method_text, desc_text).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        card.move_to(position)
        
        return card
    
    def scene_7_tips(self):
        """场景7: 应用提示"""
        title = Text(
            "判定技巧",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 三个技巧
        tip1 = Text(
            "1. 优先找角度 - AA最快",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(UP * 3)
        
        tip2 = Text(
            "2. 注意对应关系 - 顺序很重要",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(UP * 1.5)
        
        tip3 = Text(
            "3. 比例要统一 - k值必须相同",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(ORIGIN)
        
        self.play(FadeIn(tip1, shift=UP * 0.3), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(tip2, shift=UP * 0.3), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(tip3, shift=UP * 0.3), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(title, tip1, tip2, tip3)),
            run_time=0.6
        )
    
    def scene_8_outro(self):
        """场景8: 片尾关注"""
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多几何技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 三角形装饰
        triangles = VGroup(*[
            Polygon(ORIGIN, RIGHT * 0.3, UP * 0.3, color=GOLD, fill_opacity=0.8)
            .scale(0.5)
            .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(*[FadeIn(tri, scale=0.5) for tri in triangles], run_time=0.6)
        self.play(Rotate(triangles, angle=PI, run_time=1.5))
        
        self.wait(0.5)
        
        # 全部淡出
        self.play(
            FadeOut(VGroup(self.author_info, author_id, follow_text, triangles)),
            run_time=1.0
        )


# ==================== 渲染说明 ====================
"""
运行命令:
manim -pql similar_triangles.py SimilarTriangles  # 快速预览 (480p)
manim -qh similar_triangles.py SimilarTriangles   # 高质量 (1080p)
manim -qk similar_triangles.py SimilarTriangles   # 4K质量

预计总时长: ~80秒
文件大小: ~15-20MB (1080p)
"""