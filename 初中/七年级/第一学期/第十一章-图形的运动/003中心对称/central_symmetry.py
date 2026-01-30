"""
中心对称 (Central Symmetry) 教学动画
使用 Manim 创建的初中几何教学视频

内容: 中心对称的定义、性质和应用
目标观众: 七年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
  manim -pql central_symmetry.py CentralSymmetry      # 快速预览
  manim -qh central_symmetry.py CentralSymmetry       # 高质量渲染
"""

from manim import *
import numpy as np


# ==================== 全局配置 ====================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CentralSymmetry(Scene):
    """
    中心对称教学动画主场景
    
    场景顺序:
    1. 开场钩子
    2. 定义引入
    3. 性质1 - 对应点连线过对称中心
    4. 性质2 - 对称中心平分连线
    5. 应用1 - 中心对称图形（字母）
    6. 应用2 - 平行四边形对角线
    7. 总结与关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#e74c3c"        # 红色 - 原图形
        self.COLOR_SECONDARY = "#3498db"      # 蓝色 - 对称图形
        self.COLOR_CENTER = "#f39c12"         # 橙色 - 对称中心
        self.COLOR_CONNECTION = "#2ecc71"     # 绿色 - 连线
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 创建全局作者信息
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_property_1()
        self.scene_4_property_2()
        self.scene_5_application_letters()
        self.scene_6_application_parallelogram()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据"""
        # 全局缩放和偏移
        self.SCALE = 1.0
        self.MAIN_OFFSET = UP * 1.5
        
        # 对称中心 (多个场景共用)
        self.O = ORIGIN + self.MAIN_OFFSET
        
        # === 场景2-4: 三角形 ===
        # 原三角形顶点 (斜三角形)
        self.A = np.array([-2.0, 1.5, 0]) * self.SCALE + self.MAIN_OFFSET
        self.B = np.array([1.5, 2.0, 0]) * self.SCALE + self.MAIN_OFFSET
        self.C = np.array([0.5, -1.0, 0]) * self.SCALE + self.MAIN_OFFSET
        
        # 对称三角形顶点 (关于O中心对称)
        self.A_sym = 2 * self.O - self.A
        self.B_sym = 2 * self.O - self.B
        self.C_sym = 2 * self.O - self.C
        
        # 验证对应点连线中点
        self.mid_A = (self.A + self.A_sym) / 2
        self.mid_B = (self.B + self.B_sym) / 2
        self.mid_C = (self.C + self.C_sym) / 2
        
        # === 场景6: 平行四边形 ===
        self.P1 = np.array([-2.5, 1.5, 0]) + self.MAIN_OFFSET
        self.P2 = np.array([0.5, 2.5, 0]) + self.MAIN_OFFSET
        self.P3 = np.array([2.5, 0.5, 0]) + self.MAIN_OFFSET
        self.P4 = np.array([-0.5, -0.5, 0]) + self.MAIN_OFFSET
        
        # 对角线交点
        self.diag_center = self.calculate_line_intersection(
            self.P1, self.P3 - self.P1,
            self.P2, self.P4 - self.P2
        )
        
        # 验证几何正确性
        self.verify_geometry()
    
    def calculate_line_intersection(self, P1, D1, P2, D2):
        """计算两直线交点"""
        A = np.array([[D1[0], -D2[0]], [D1[1], -D2[1]]])
        b = np.array([P2[0] - P1[0], P2[1] - P1[1]])
        if np.abs(np.linalg.det(A)) < 1e-10:
            return None  # 平行
        params = np.linalg.solve(A, b)
        return np.array([*(P1[:2] + params[0] * D1[:2]), 0])
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证三角形中点等于O
        assert np.linalg.norm(self.mid_A - self.O) < epsilon, "中点A验证失败"
        assert np.linalg.norm(self.mid_B - self.O) < epsilon, "中点B验证失败"
        assert np.linalg.norm(self.mid_C - self.O) < epsilon, "中点C验证失败"
        
        # 验证平行四边形对角线交点是中点
        mid_AC = (self.P1 + self.P3) / 2
        mid_BD = (self.P2 + self.P4) / 2
        assert np.linalg.norm(mid_AC - mid_BD) < epsilon, "平行四边形对角线中点不重合"
        
        print("✓ 几何验证通过")
    
    # ==================== Scene 1: 开场钩子 ====================
    def scene_1_opening(self):
        """场景1: 开场钩子 (3-4秒)"""
        # 作者信息淡入
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook = Text(
            "这两个图形有什么关系?",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook), run_time=0.8)
        
        # 两个三角形（暗示中心对称）
        tri1 = Polygon(
            np.array([-1.5, 0.5, 0]),
            np.array([0, 1.5, 0]),
            np.array([-0.5, -0.5, 0]),
            color=self.COLOR_PRIMARY,
            fill_opacity=0.3,
            stroke_width=3
        ).move_to(LEFT * 1.5 + UP * 2)
        
        tri2 = Polygon(
            np.array([1.5, -0.5, 0]),
            np.array([0, -1.5, 0]),
            np.array([0.5, 0.5, 0]),
            color=self.COLOR_SECONDARY,
            fill_opacity=0.3,
            stroke_width=3
        ).move_to(RIGHT * 1.5 + UP * 2)
        
        center_dot = Dot(UP * 2, color=self.COLOR_CENTER, radius=0.1)
        
        self.play(
            Create(tri1),
            Create(tri2),
            FadeIn(center_dot),
            run_time=1.0
        )
        
        # 旋转展示
        tri_group = VGroup(tri1, tri2)
        self.play(Rotate(tri_group, PI, about_point=UP * 2), run_time=1.5)
        
        # 问题文字
        question = Text(
            "它们是中心对称的!",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(tri1),
            FadeOut(tri2),
            FadeOut(center_dot),
            FadeOut(question),
            run_time=0.5
        )
    
    # ==================== Scene 2: 定义引入 ====================
    def scene_2_definition(self):
        """场景2: 定义引入 (8-10秒)"""
        # 标题
        title = Text(
            "什么是中心对称?",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 三角形
        triangle_ABC = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            stroke_width=3,
            fill_opacity=0.2
        )
        
        self.play(Create(triangle_ABC), run_time=1.0)
        
        # 对称中心
        dot_O = Dot(self.O, color=self.COLOR_CENTER, radius=0.12)
        label_O_text = Text("O", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_CENTER)
        label_O_sub = Text("对称中心", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_CENTER)
        label_O = VGroup(label_O_text, label_O_sub).arrange(DOWN, buff=0.05).next_to(dot_O, DOWN, buff=0.2)
        
        self.play(FadeIn(dot_O), run_time=0.3)
        self.play(Flash(dot_O, color=self.COLOR_CENTER, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(label_O), run_time=0.4)
        
        # 定义文字框
        def_line1 = Text("定义: 如果把一个图形绕某点", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        
        # Line 2 with highlight - split into parts
        def_line2_part1 = Text("旋转", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        def_line2_part2 = Text("180°", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        def_line2_part3 = Text("后能与另一个图形", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        def_line2 = VGroup(def_line2_part1, def_line2_part2, def_line2_part3).arrange(RIGHT, buff=0.05)
        
        def_line3 = Text("重合, 则这两个图形", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        def_line4 = Text("关于这点中心对称。", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        
        definition_box = VGroup(def_line1, def_line2, def_line3, def_line4).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        definition_box.move_to(DOWN * 4.5)
        
        bg_rect = SurroundingRectangle(
            definition_box,
            color=self.COLOR_AUXILIARY,
            buff=0.3,
            corner_radius=0.1,
            fill_opacity=0.1
        )
        
        self.play(FadeIn(bg_rect), FadeIn(definition_box), run_time=0.8)
        self.wait(1.5)
        
        # 高亮"180°"
        self.play(def_line2_part2.animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.5)
        
        # 旋转演示
        triangle_copy = triangle_ABC.copy()
        self.play(
            Rotate(triangle_copy, PI, about_point=self.O),
            run_time=2.0,
            rate_func=smooth
        )
        
        # 对称三角形淡入（虚线）
        triangle_sym_solid = Polygon(
            self.A_sym, self.B_sym, self.C_sym,
            color=self.COLOR_SECONDARY,
            stroke_width=3,
            stroke_opacity=0.7
        )
        triangle_sym = DashedVMobject(triangle_sym_solid, num_dashes=20)
        
        self.play(FadeIn(triangle_sym, scale=1.05), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition_box),
            FadeOut(bg_rect),
            FadeOut(triangle_ABC),
            FadeOut(triangle_copy),
            FadeOut(triangle_sym),
            run_time=0.6
        )
        
        # 保留对称中心（缩小）
        self.dot_O_small = Dot(self.O, color=self.COLOR_CENTER, radius=0.05, fill_opacity=0.5)
        self.play(
            Transform(dot_O, self.dot_O_small),
            FadeOut(label_O),
            run_time=0.3
        )
        self.remove(dot_O)
        self.add(self.dot_O_small)
    
    # ==================== Scene 3: 性质1 ====================
    def scene_3_property_1(self):
        """场景3: 性质1 - 对应点连线过对称中心 (10-12秒)"""
        # 性质标题
        property_title = Text(
            "性质1: 对应点连线过对称中心",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(property_title), run_time=0.6)
        
        # 三角形
        triangle_1 = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        triangle_2 = Polygon(
            self.A_sym, self.B_sym, self.C_sym,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        )
        
        self.play(Create(triangle_1), run_time=0.8)
        self.play(Create(triangle_2), run_time=0.8)
        
        # 顶点标签
        label_A = Text("A", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(self.A, LEFT, buff=0.1)
        label_B = Text("B", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(self.B, UP, buff=0.1)
        label_C = Text("C", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(self.C, DOWN, buff=0.1)
        
        label_A_sym = Text("A'", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(self.A_sym, RIGHT, buff=0.1)
        label_B_sym = Text("B'", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(self.B_sym, DOWN, buff=0.1)
        label_C_sym = Text("C'", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(self.C_sym, UP, buff=0.1)
        
        labels_ABC = VGroup(label_A, label_B, label_C)
        labels_sym = VGroup(label_A_sym, label_B_sym, label_C_sym)
        
        self.play(FadeIn(labels_ABC), run_time=0.5)
        self.play(FadeIn(labels_sym), run_time=0.5)
        
        # 说明文字
        explain_1 = Text(
            "连接对应点...",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain_1), run_time=0.5)
        
        # 对应点连线
        line_AA = Line(self.A, self.A_sym, color=self.COLOR_CONNECTION, stroke_width=2)
        line_BB = Line(self.B, self.B_sym, color=self.COLOR_CONNECTION, stroke_width=2)
        line_CC = Line(self.C, self.C_sym, color=self.COLOR_CONNECTION, stroke_width=2)
        
        # 对称中心（放大）
        dot_O = Dot(self.O, color=self.COLOR_CENTER, radius=0.1)
        
        # 连线AA'
        self.play(Create(line_AA), run_time=0.8)
        self.play(Flash(dot_O, color=self.COLOR_CENTER), run_time=0.4)
        
        # 连线BB'
        self.play(Create(line_BB), run_time=0.8)
        self.play(Flash(dot_O, color=self.COLOR_CENTER), run_time=0.4)
        
        # 连线CC'
        self.play(Create(line_CC), run_time=0.8)
        self.play(Flash(dot_O, color=self.COLOR_CENTER), run_time=0.4)
        
        self.play(FadeOut(explain_1), run_time=0.3)
        
        # 性质文字
        property_text_1 = Text(
            "所有连线都经过对称中心O!",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(property_text_1), run_time=0.8)
        
        # 高亮所有连线
        lines = VGroup(line_AA, line_BB, line_CC)
        self.play(lines.animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.6)
        
        self.wait(1.5)
        
        # 保留元素用于下一场景
        self.play(FadeOut(property_title), FadeOut(property_text_1), run_time=0.3)
        
        # 存储元素供下一场景使用
        self.triangle_1 = triangle_1
        self.triangle_2 = triangle_2
        self.labels_ABC = labels_ABC
        self.labels_sym = labels_sym
        self.line_AA = line_AA
        self.line_BB = line_BB
        self.line_CC = line_CC
        self.dot_O_visible = dot_O
    
    # ==================== Scene 4: 性质2 ====================
    def scene_4_property_2(self):
        """场景4: 性质2 - 对称中心平分连线 (10-12秒)"""
        # 恢复连线颜色
        lines = VGroup(self.line_AA, self.line_BB, self.line_CC)
        self.play(lines.animate.set_color(self.COLOR_CONNECTION), run_time=0.3)
        
        # 性质标题
        property_title_2 = Text(
            "性质2: 对称中心平分连线",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(property_title_2), run_time=0.6)
        
        # 高亮线段AA'
        self.play(self.line_AA.animate.set_stroke(width=4, color=self.COLOR_HIGHLIGHT), run_time=0.4)
        
        # 计算垂直方向（用于大括号）
        vec_AA = self.A_sym - self.A
        perp_dir = normalize(np.array([-vec_AA[1], vec_AA[0], 0]))
        
        # 大括号和标签 (线段AO)
        brace_AO = Brace(Line(self.A, self.O), direction=perp_dir * 0.5, color=YELLOW)
        label_AO = Text("AO", font="Noto Sans CJK SC", font_size=20, color=YELLOW).next_to(brace_AO, perp_dir * 0.5, buff=0.1)
        
        self.play(Create(brace_AO), FadeIn(label_AO), run_time=0.8)
        
        # 大括号和标签 (线段OA')
        brace_OA = Brace(Line(self.O, self.A_sym), direction=perp_dir * 0.5, color=YELLOW)
        label_OA = Text("OA'", font="Noto Sans CJK SC", font_size=20, color=YELLOW).next_to(brace_OA, perp_dir * 0.5, buff=0.1)
        
        self.play(Create(brace_OA), FadeIn(label_OA), run_time=0.8)
        
        # 等式
        equation_1 = MathTex(r"AO = OA'", font_size=32, color=YELLOW).move_to(DOWN * 4)
        self.play(FadeIn(equation_1), run_time=0.6)
        
        # 标记中点重合
        self.play(Flash(self.dot_O_visible, color=YELLOW, flash_radius=0.4), run_time=0.5)
        
        # 清理AA'的标注
        self.play(
            FadeOut(brace_AO),
            FadeOut(label_AO),
            FadeOut(brace_OA),
            FadeOut(label_OA),
            FadeOut(equation_1),
            self.line_AA.animate.set_stroke(width=2, color=self.COLOR_CONNECTION),
            run_time=0.3
        )
        
        # 快速演示BB'和CC'
        # BB'
        self.play(self.line_BB.animate.set_stroke(width=4, color=self.COLOR_HIGHLIGHT), run_time=0.3)
        
        vec_BB = self.B_sym - self.B
        perp_dir_B = normalize(np.array([-vec_BB[1], vec_BB[0], 0]))
        
        braces_B = VGroup(
            Brace(Line(self.B, self.O), direction=perp_dir_B * 0.5, color=YELLOW),
            Brace(Line(self.O, self.B_sym), direction=perp_dir_B * 0.5, color=YELLOW)
        )
        
        self.play(Create(braces_B), run_time=0.6)
        self.play(
            FadeOut(braces_B),
            self.line_BB.animate.set_stroke(width=2, color=self.COLOR_CONNECTION),
            run_time=0.3
        )
        
        # CC'
        self.play(self.line_CC.animate.set_stroke(width=4, color=self.COLOR_HIGHLIGHT), run_time=0.3)
        
        vec_CC = self.C_sym - self.C
        perp_dir_C = normalize(np.array([-vec_CC[1], vec_CC[0], 0]))
        
        braces_C = VGroup(
            Brace(Line(self.C, self.O), direction=perp_dir_C * 0.5, color=YELLOW),
            Brace(Line(self.O, self.C_sym), direction=perp_dir_C * 0.5, color=YELLOW)
        )
        
        self.play(Create(braces_C), run_time=0.6)
        self.play(
            FadeOut(braces_C),
            self.line_CC.animate.set_stroke(width=2, color=self.COLOR_CONNECTION),
            run_time=0.3
        )
        
        # 性质总结文字
        property_text_2 = Text(
            "对称中心是对应点连线的中点!",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(property_text_2), run_time=0.8)
        
        # 公式框
        formula_line1 = Text("通用公式:", font="Noto Sans CJK SC", font_size=22, color=GRAY_A)
        formula_line2 = MathTex(r"OA = OA'", font_size=28)
        formula_line3 = Text("且 O 在线段 AA' 上", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        
        formula_box = VGroup(formula_line1, formula_line2, formula_line3).arrange(DOWN, buff=0.2).move_to(DOWN * 6.5)
        
        self.play(FadeIn(formula_box), run_time=0.8)
        self.wait(2.0)
        
        # 清理所有元素
        self.play(
            FadeOut(property_title_2),
            FadeOut(self.triangle_1),
            FadeOut(self.triangle_2),
            FadeOut(self.labels_ABC),
            FadeOut(self.labels_sym),
            FadeOut(lines),
            FadeOut(self.dot_O_visible),
            FadeOut(property_text_2),
            FadeOut(formula_box),
            run_time=0.6
        )
    
    # ==================== Scene 5: 应用1 - 字母 ====================
    def scene_5_application_letters(self):
        """场景5: 应用1 - 中心对称图形（字母） (8-10秒)"""
        # 标题
        title = Text(
            "应用: 识别中心对称图形",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 说明
        explain = Text(
            "旋转180°后能与自己重合的图形",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(FadeIn(explain), run_time=0.5)
        
        # 字母N
        letter_N = Text("N", font="Arial", font_size=80, color=self.COLOR_PRIMARY).move_to(UP * 2.5 + LEFT * 3)
        self.play(FadeIn(letter_N), run_time=0.4)
        
        # 旋转验证
        letter_N_copy = letter_N.copy().set_color(self.COLOR_SECONDARY).set_opacity(0.5)
        self.play(
            Rotate(letter_N_copy, PI, about_point=letter_N.get_center()),
            run_time=1.2
        )
        
        # 打勾
        check_N = Text("✓", font_size=40, color=GREEN).next_to(letter_N, DOWN, buff=0.3)
        self.play(FadeIn(check_N, scale=1.5), run_time=0.3)
        self.remove(letter_N_copy)
        
        # 字母S
        letter_S = Text("S", font="Arial", font_size=80, color=self.COLOR_PRIMARY).next_to(letter_N, RIGHT, buff=1.5)
        self.play(FadeIn(letter_S), run_time=0.4)
        
        letter_S_copy = letter_S.copy().set_color(self.COLOR_SECONDARY).set_opacity(0.5)
        self.play(
            Rotate(letter_S_copy, PI, about_point=letter_S.get_center()),
            run_time=1.2
        )
        
        check_S = Text("✓", font_size=40, color=GREEN).next_to(letter_S, DOWN, buff=0.3)
        self.play(FadeIn(check_S, scale=1.5), run_time=0.3)
        self.remove(letter_S_copy)
        
        # 字母Z
        letter_Z = Text("Z", font="Arial", font_size=80, color=self.COLOR_PRIMARY).next_to(letter_S, RIGHT, buff=1.5)
        self.play(FadeIn(letter_Z), run_time=0.4)
        
        letter_Z_copy = letter_Z.copy().set_color(self.COLOR_SECONDARY).set_opacity(0.5)
        self.play(
            Rotate(letter_Z_copy, PI, about_point=letter_Z.get_center()),
            run_time=1.2
        )
        
        check_Z = Text("✓", font_size=40, color=GREEN).next_to(letter_Z, DOWN, buff=0.3)
        self.play(FadeIn(check_Z, scale=1.5), run_time=0.3)
        self.remove(letter_Z_copy)
        
        # 字母A（反例）
        letter_A = Text("A", font="Arial", font_size=80, color=GRAY).move_to(DOWN * 1 + LEFT * 1.5)
        self.play(FadeIn(letter_A), run_time=0.4)
        
        letter_A_copy = letter_A.copy().set_color(RED).set_opacity(0.5)
        self.play(
            Rotate(letter_A_copy, PI, about_point=letter_A.get_center()),
            run_time=1.0
        )
        
        cross_A = Text("✗", font_size=40, color=RED).next_to(letter_A, DOWN, buff=0.3)
        self.play(FadeIn(cross_A, scale=1.5), run_time=0.3)
        self.remove(letter_A_copy)
        
        # 总结
        summary = Text(
            "N, S, Z 是中心对称图形!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(summary), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explain),
            FadeOut(letter_N),
            FadeOut(letter_S),
            FadeOut(letter_Z),
            FadeOut(letter_A),
            FadeOut(check_N),
            FadeOut(check_S),
            FadeOut(check_Z),
            FadeOut(cross_A),
            FadeOut(summary),
            run_time=0.6
        )
    
    # ==================== Scene 6: 应用2 - 平行四边形 ====================
    def scene_6_application_parallelogram(self):
        """场景6: 应用2 - 平行四边形对角线互相平分 (10-12秒)"""
        # 标题
        title = Text(
            "应用: 平行四边形对角线互相平分",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 平行四边形
        parallelogram = Polygon(
            self.P1, self.P2, self.P3, self.P4,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        self.play(Create(parallelogram), run_time=1.0)
        
        # 顶点标签
        label_P1 = Text("A", font="Noto Sans CJK SC", font_size=22).next_to(self.P1, LEFT)
        label_P2 = Text("B", font="Noto Sans CJK SC", font_size=22).next_to(self.P2, UP)
        label_P3 = Text("C", font="Noto Sans CJK SC", font_size=22).next_to(self.P3, RIGHT)
        label_P4 = Text("D", font="Noto Sans CJK SC", font_size=22).next_to(self.P4, DOWN)
        labels = VGroup(label_P1, label_P2, label_P3, label_P4)
        
        self.play(FadeIn(labels), run_time=0.5)
        
        # 对角线
        diag_AC = Line(self.P1, self.P3, color=self.COLOR_CONNECTION, stroke_width=2)
        diag_BD = Line(self.P2, self.P4, color=self.COLOR_CONNECTION, stroke_width=2)
        
        self.play(Create(diag_AC), run_time=0.8)
        self.play(Create(diag_BD), run_time=0.8)
        
        # 交点O
        dot_O = Dot(self.diag_center, color=self.COLOR_CENTER, radius=0.1)
        label_O = Text("O", font="Noto Sans CJK SC", font_size=20).next_to(dot_O, DOWN * 0.5 + RIGHT * 0.5, buff=0.05)
        
        self.play(FadeIn(dot_O), run_time=0.3)
        self.play(Flash(dot_O, color=self.COLOR_CENTER), run_time=0.4)
        self.play(FadeIn(label_O), run_time=0.3)
        
        # 说明
        explain_1 = Text(
            "平行四边形关于对角线交点中心对称",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain_1), run_time=0.8)
        
        # 高亮A和C
        self.play(
            label_P1.animate.set_color(YELLOW),
            label_P3.animate.set_color(YELLOW),
            run_time=0.5
        )
        
        # 高亮对角线AC
        self.play(diag_AC.animate.set_color(YELLOW).set_stroke(width=4), run_time=0.4)
        
        # 标注AO=OC (简化版)
        eq_AC = MathTex(r"AO = OC", font_size=24, color=YELLOW).move_to(DOWN * 5.5 + LEFT * 1.5)
        self.play(FadeIn(eq_AC), run_time=0.6)
        
        # 恢复颜色
        self.play(
            label_P1.animate.set_color(WHITE),
            label_P3.animate.set_color(WHITE),
            diag_AC.animate.set_color(self.COLOR_CONNECTION).set_stroke(width=2),
            run_time=0.3
        )
        
        # 高亮B和D
        self.play(
            label_P2.animate.set_color(YELLOW),
            label_P4.animate.set_color(YELLOW),
            run_time=0.5
        )
        
        # 高亮对角线BD
        self.play(diag_BD.animate.set_color(YELLOW).set_stroke(width=4), run_time=0.4)
        
        # 标注BO=OD
        eq_BD = MathTex(r"BO = OD", font_size=24, color=YELLOW).move_to(DOWN * 5.5 + RIGHT * 1.5)
        self.play(FadeIn(eq_BD), run_time=0.6)
        
        # 恢复
        self.play(
            label_P2.animate.set_color(WHITE),
            label_P4.animate.set_color(WHITE),
            diag_BD.animate.set_color(self.COLOR_CONNECTION).set_stroke(width=2),
            FadeOut(explain_1),
            run_time=0.3
        )
        
        # 结论
        conclusion_line1 = Text("根据中心对称性质:", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        conclusion_line2 = MathTex(r"AO = OC,\quad BO = OD", font_size=28, color=self.COLOR_HIGHLIGHT)
        conclusion_line3 = Text("对角线互相平分!", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_HIGHLIGHT)
        
        conclusion = VGroup(conclusion_line1, conclusion_line2, conclusion_line3).arrange(DOWN, buff=0.2).move_to(DOWN * 6.2)
        
        self.play(FadeIn(conclusion), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(parallelogram),
            FadeOut(labels),
            FadeOut(diag_AC),
            FadeOut(diag_BD),
            FadeOut(dot_O),
            FadeOut(label_O),
            FadeOut(eq_AC),
            FadeOut(eq_BD),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    # ==================== Scene 7: 总结与关注 ====================
    def scene_7_outro(self):
        """场景7: 总结与关注 (6-8秒)"""
        # 总结标题
        summary_title = Text(
            "中心对称 - 核心要点",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 知识卡片
        card_1_icon = Circle(radius=0.2, color=self.COLOR_PRIMARY, fill_opacity=1, stroke_width=0)
        card_1_text = Text("定义: 旋转180°重合", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        card_1 = VGroup(card_1_icon, card_1_text).arrange(RIGHT, buff=0.3).move_to(UP * 3).shift(LEFT * 10)
        
        card_2_icon = Circle(radius=0.2, color=self.COLOR_SECONDARY, fill_opacity=1, stroke_width=0)
        card_2_text = Text("性质: 对应点连线过对称中心且被平分", font="Noto Sans CJK SC", font_size=22, color=WHITE)
        card_2 = VGroup(card_2_icon, card_2_text).arrange(RIGHT, buff=0.3).move_to(UP * 1.5).shift(LEFT * 10)
        
        card_3_icon = Circle(radius=0.2, color=self.COLOR_HIGHLIGHT, fill_opacity=1, stroke_width=0)
        card_3_text = Text("应用: 平行四边形、字母N/S/Z", font="Noto Sans CJK SC", font_size=22, color=WHITE)
        card_3 = VGroup(card_3_icon, card_3_text).arrange(RIGHT, buff=0.3).move_to(ORIGIN).shift(LEFT * 10)
        
        # 卡片滑入
        self.play(card_1.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.2)
        self.play(card_2.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.2)
        self.play(card_3.animate.shift(RIGHT * 10), run_time=0.5)
        
        self.wait(1.5)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author, author_large),
            FadeOut(summary_title),
            FadeOut(card_1),
            FadeOut(card_2),
            FadeOut(card_3),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注文字
        follow_text = Text(
            "关注我, 学更多几何技巧!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰图形（小三角形旋转）
        decorations = VGroup(*[
            Polygon(
                ORIGIN, RIGHT * 0.3, UP * 0.3,
                color=GOLD,
                fill_opacity=0.6,
                stroke_width=0
            )
            .scale(0.4)
            .move_to(follow_text.get_center() + 1.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(*[FadeIn(tri, scale=0.5) for tri in decorations], run_time=0.6)
        self.play(Rotate(decorations, angle=PI, run_time=1.2))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


# 运行提示
if __name__ == "__main__":
    print("=" * 60)
    print("中心对称 (Central Symmetry) 教学动画")
    print("=" * 60)
    print("\n渲染命令:")
    print("  快速预览: manim -pql central_symmetry.py CentralSymmetry")
    print("  高质量:   manim -qh central_symmetry.py CentralSymmetry")
    print("\n目标格式: TikTok 竖屏 (1080×1920)")
    print("预计时长: 60 秒")
    print("=" * 60)