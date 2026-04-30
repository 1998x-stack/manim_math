"""
向量的加法与减法 - Vector Addition and Subtraction
使用 Manim 创建的中学数学教学视频

内容: 向量加法的三角形法则和平行四边形法则，向量减法
目标观众: 八年级学生
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


class VectorAdditionSubtraction(Scene):
    """
    向量加减法教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出向量运算
    2. 向量基础 - 介绍向量概念
    3. 三角形法则 - 首尾相接
    4. 平行四边形法则 - 同起点
    5. 两种法则等价性
    6. 相反向量概念
    7. 向量减法运算
    8. 总结 + 片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_VECTOR_A = "#e74c3c"        # 红色 - 向量a
        self.COLOR_VECTOR_B = "#3498db"        # 蓝色 - 向量b
        self.COLOR_VECTOR_SUM = "#2ecc71"      # 绿色 - 和向量
        self.COLOR_VECTOR_DIFF = "#f39c12"     # 橙色 - 差向量
        self.COLOR_VECTOR_NEG = "#9b59b6"      # 紫色 - 相反向量
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_POLYGON = WHITE
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_vector_basics()
        self.show_triangle_law()
        self.show_parallelogram_law()
        self.show_equivalence()
        self.show_opposite_vector()
        self.show_vector_subtraction()
        self.show_summary_and_outro()
    
    def setup_geometry(self):
        """初始化所有向量和几何数据"""
        # 原点
        self.O = np.array([0, 0, 0])
        
        # 向量定义（相对于原点的位移）
        self.vec_a = np.array([2.5, 1.5, 0])
        self.vec_b = np.array([1.8, 0.8, 0])
        
        # 向量a的终点
        self.A = self.O + self.vec_a
        
        # 向量b的终点（平行四边形法则）
        self.B = self.O + self.vec_b
        
        # 三角形法则：向量b从A点开始
        self.C = self.A + self.vec_b  # = O + vec_a + vec_b
        
        # 平行四边形的第四个顶点
        self.D = self.O + self.vec_a + self.vec_b  # 应该等于C
        
        # 相反向量
        self.vec_neg_b = -self.vec_b
        self.neg_B = self.O + self.vec_neg_b
        
        # 差向量终点
        self.diff_point = self.A + self.vec_neg_b
        
        # 缩放和偏移（让图形居中在主内容区）
        self.SCALE = 0.85
        self.OFFSET = UP * 1.0
        
        # 应用缩放和偏移到所有点
        self.O = self.O * self.SCALE + self.OFFSET
        self.A = self.A * self.SCALE + self.OFFSET
        self.B = self.B * self.SCALE + self.OFFSET
        self.C = self.C * self.SCALE + self.OFFSET
        self.D = self.D * self.SCALE + self.OFFSET
        self.neg_B = self.neg_B * self.SCALE + self.OFFSET
        self.diff_point = self.diff_point * self.SCALE + self.OFFSET
        
        # 同时缩放向量
        self.vec_a = self.vec_a * self.SCALE
        self.vec_b = self.vec_b * self.SCALE
        self.vec_neg_b = self.vec_neg_b * self.SCALE
        
        # 验证几何关系
        self.verify_geometry()
        
        print("✓ 几何数据初始化完成")
    
    def verify_geometry(self):
        """验证几何关系的正确性"""
        epsilon = 1e-6
        errors = []
        
        # 验证1: 平行四边形对边平行且相等
        # OA 应该平行且等于 BD
        vec_OA = self.A - self.O
        vec_BD = self.D - self.B
        
        if not np.allclose(vec_OA, vec_BD, atol=epsilon):
            errors.append(f"平行四边形错误: OA ≠ BD")
        
        # OB 应该平行且等于 AD
        vec_OB = self.B - self.O
        vec_AD = self.D - self.A
        
        if not np.allclose(vec_OB, vec_AD, atol=epsilon):
            errors.append(f"平行四边形错误: OB ≠ AD")
        
        # 验证2: C和D应该是同一点（两种方法结果相同）
        if not np.allclose(self.C, self.D, atol=epsilon):
            errors.append(f"三角形法则和平行四边形法则结果不一致")
        
        # 验证3: 相反向量长度相等
        len_b = np.linalg.norm(self.vec_b)
        len_neg_b = np.linalg.norm(self.vec_neg_b)
        
        if not np.isclose(len_b, len_neg_b, atol=epsilon):
            errors.append(f"相反向量长度不等: |b|={len_b:.6f}, |-b|={len_neg_b:.6f}")
        
        # 验证4: 相反向量方向相反（点积应该为负）
        dot_product = np.dot(self.vec_b[:2], self.vec_neg_b[:2])
        expected_dot = -len_b * len_neg_b
        
        if not np.isclose(dot_product, expected_dot, atol=epsilon):
            errors.append(f"相反向量方向错误: 点积={dot_product:.6f}")
        
        # 输出结果
        if errors:
            print("❌ 几何验证失败:")
            for e in errors:
                print(f"  - {e}")
            raise ValueError("几何验证失败！")
        else:
            print("✓ 几何验证通过")
    
    def create_vector_arrow(self, start, end, color, stroke_width=6):
        """创建向量箭头"""
        return Arrow(
            start=start,
            end=end,
            buff=0,
            stroke_width=stroke_width,
            max_tip_length_to_length_ratio=0.15,
            max_stroke_width_to_length_ratio=10,
            color=color
        )
    
    def get_vector_label_position(self, start, end, direction=UP, buff=0.2):
        midpoint = (start + end) / 2
        vec = end - start
        perp = np.array([-vec[1], vec[0], 0])
        perp_normalized = perp / np.linalg.norm(perp) if np.linalg.norm(perp) > 0 else np.array([0, 1, 0])

        # 根据direction调整 — use np.allclose to compare arrays safely
        if np.allclose(direction, DOWN):
            perp_normalized = -perp_normalized

        return midpoint + perp_normalized * buff
    
    def show_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息 (顶部，持续显示)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题 - 主标题
        hook_title = Text(
            "箭头能加减吗?",
            font="PingFang SC",
            font_size=46,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        # 副标题
        hook_subtitle = Text(
            "向量运算，其实很简单！",
            font="PingFang SC",
            font_size=30,
            color=GRAY_A
        ).move_to(UP * 4.6)
        
        self.play(Write(hook_title), run_time=0.8)
        self.play(FadeIn(hook_subtitle, shift=UP * 0.2), run_time=0.4)
        
        # 几个箭头快闪演示
        demo_arrows = VGroup(
            Arrow(LEFT * 1.5, RIGHT * 0.5, color=self.COLOR_VECTOR_A, stroke_width=5),
            Arrow(ORIGIN, UP, color=self.COLOR_VECTOR_B, stroke_width=5),
            Arrow(RIGHT * 0.5, RIGHT * 1.5 + UP * 1.2, color=self.COLOR_VECTOR_SUM, stroke_width=5)
        ).move_to(UP * 1)
        
        self.play(*[GrowArrow(arrow) for arrow in demo_arrows], run_time=0.8)
        
        # 问号
        question = Text(
            "?",
            font="PingFang SC",
            font_size=60,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(Flash(question, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.3)
        self.play(FadeIn(question, scale=1.5), run_time=0.3)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_title),
            FadeOut(hook_subtitle),
            FadeOut(demo_arrows),
            FadeOut(question),
            run_time=0.4
        )
    
    def show_vector_basics(self):
        """场景2: 向量基础 (5-12秒)"""
        # 标题
        title = Text(
            "什么是向量?",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 原点
        self.origin_dot = Dot(self.O, radius=0.08, color=WHITE)
        origin_label = MathTex("O", font_size=24, color=WHITE).next_to(self.origin_dot, DL, buff=0.15)
        
        self.play(FadeIn(self.origin_dot), FadeIn(origin_label), run_time=0.4)
        
        # 绘制向量a
        self.vector_a = self.create_vector_arrow(self.O, self.A, self.COLOR_VECTOR_A)
        
        # 向量标签（使用向量符号）
        vector_a_label = MathTex(
            r"\vec{a}",
            font_size=28,
            color=self.COLOR_VECTOR_A
        ).move_to(self.get_vector_label_position(self.O, self.A, UP, 0.35))
        
        self.play(GrowArrow(self.vector_a), run_time=1.0)
        self.play(Write(vector_a_label), run_time=0.5)
        
        # 终点标记
        point_a_dot = Dot(self.A, radius=0.06, color=self.COLOR_VECTOR_A)
        point_a_label = MathTex("A", font_size=20, color=WHITE).next_to(point_a_dot, UR, buff=0.1)
        
        self.play(FadeIn(point_a_dot), FadeIn(point_a_label), run_time=0.3)
        
        # 说明文字
        explanation = VGroup(
            Text("向量：既有大小又有方向", font="PingFang SC", font_size=22, color=WHITE),
            Text("用箭头表示", font="PingFang SC", font_size=20, color=GRAY_A)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(origin_label),
            FadeOut(point_a_dot),
            FadeOut(point_a_label),
            run_time=0.3
        )
        
        # 保存向量a的标签供后续使用
        self.vector_a_label = vector_a_label
    
    def show_triangle_law(self):
        """场景3: 三角形法则 (12-28秒)"""
        # 标题
        title = Text(
            "三角形法则",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_VECTOR_SUM,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 公式
        formula = MathTex(
            r"\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}",
            font_size=26,
            color=WHITE
        ).move_to(UP * 5.8)
        
        self.play(Write(formula), run_time=1.0)
        
        # 向量b（从A点开始）
        vector_b_triangle = self.create_vector_arrow(self.A, self.C, self.COLOR_VECTOR_B)
        
        vector_b_label = MathTex(
            r"\vec{b}",
            font_size=28,
            color=self.COLOR_VECTOR_B
        ).move_to(self.get_vector_label_position(self.A, self.C, UP, 0.35))
        
        # 标注 "首尾相接"
        annotation = Text(
            "首尾相接",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).next_to(self.A, RIGHT, buff=0.4)
        annotation_arrow = Arrow(
            annotation.get_left(),
            self.A + RIGHT * 0.15,
            buff=0.05,
            stroke_width=2,
            color=self.COLOR_HIGHLIGHT,
            max_tip_length_to_length_ratio=0.2
        )
        
        self.play(GrowArrow(vector_b_triangle), run_time=1.2)
        self.play(Write(vector_b_label), run_time=0.4)
        self.play(FadeIn(annotation), GrowArrow(annotation_arrow), run_time=0.6)
        
        # 绘制和向量（从O到C）
        sum_vector_triangle = self.create_vector_arrow(
            self.O, self.C,
            self.COLOR_VECTOR_SUM,
            stroke_width=7
        )
        
        sum_label = MathTex(
            r"\vec{a} + \vec{b}",
            font_size=28,
            color=self.COLOR_VECTOR_SUM
        ).move_to(self.get_vector_label_position(self.O, self.C, DOWN, 0.4))
        
        # C点标记
        point_c_dot = Dot(self.C, radius=0.08, color=self.COLOR_VECTOR_SUM)
        point_c_label = MathTex("C", font_size=22, color=WHITE).next_to(point_c_dot, UR, buff=0.12)
        
        self.play(GrowArrow(sum_vector_triangle), run_time=1.5)
        self.play(Write(sum_label), run_time=0.5)
        self.play(FadeIn(point_c_dot), FadeIn(point_c_label), run_time=0.3)
        
        # 高亮三角形路径
        triangle_path = DashedVMobject(
            Polygon(self.O, self.A, self.C, self.O),
            num_dashes=30,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        
        self.play(Create(triangle_path), run_time=1.0)
        
        # 说明文字
        explanation = VGroup(
            Text("第二个向量起点接在第一个终点", font="PingFang SC", font_size=20, color=WHITE),
            Text("结果：从第一个起点到第二个终点", font="PingFang SC", font_size=20, color=self.COLOR_VECTOR_SUM)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.8)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(annotation),
            FadeOut(annotation_arrow),
            FadeOut(triangle_path),
            FadeOut(explanation),
            FadeOut(vector_b_triangle),
            FadeOut(vector_b_label),
            FadeOut(sum_vector_triangle),
            FadeOut(sum_label),
            FadeOut(point_c_dot),
            FadeOut(point_c_label),
            run_time=0.6
        )
    
    def show_parallelogram_law(self):
        """场景4: 平行四边形法则 (28-44秒)"""
        # 标题
        title = Text(
            "平行四边形法则",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_VECTOR_SUM,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 公式
        formula = MathTex(
            r"\overrightarrow{OA} + \overrightarrow{OB} = \overrightarrow{OC}",
            font_size=26,
            color=WHITE
        ).move_to(UP * 5.8)
        
        self.play(Write(formula), run_time=1.0)
        
        # 向量b（从O点开始）
        vector_b_para = self.create_vector_arrow(self.O, self.B, self.COLOR_VECTOR_B)
        
        vector_b_label_para = MathTex(
            r"\vec{b}",
            font_size=28,
            color=self.COLOR_VECTOR_B
        ).move_to(self.get_vector_label_position(self.O, self.B, DOWN, 0.3))
        
        # B点标记
        point_b_dot = Dot(self.B, radius=0.06, color=self.COLOR_VECTOR_B)
        point_b_label = MathTex("B", font_size=20, color=WHITE).next_to(point_b_dot, DR, buff=0.1)
        
        # 标注 "同起点"
        annotation = Text(
            "同起点",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).next_to(self.O, LEFT, buff=0.4)
        annotation_arrow = Arrow(
            annotation.get_right(),
            self.O + LEFT * 0.15,
            buff=0.05,
            stroke_width=2,
            color=self.COLOR_HIGHLIGHT,
            max_tip_length_to_length_ratio=0.2
        )
        
        self.play(GrowArrow(vector_b_para), run_time=1.2)
        self.play(Write(vector_b_label_para), FadeIn(point_b_dot), FadeIn(point_b_label), run_time=0.4)
        self.play(FadeIn(annotation), GrowArrow(annotation_arrow), run_time=0.6)
        
        # 构造平行四边形 O-A-D-B
        parallelogram = Polygon(
            self.O, self.A, self.D, self.B,
            color=self.COLOR_AUXILIARY,
            stroke_width=2,
            fill_opacity=0
        )
        
        # D点标记
        point_d_dot = Dot(self.D, radius=0.06, color=self.COLOR_AUXILIARY)
        
        self.play(Create(parallelogram), FadeIn(point_d_dot), run_time=1.5)
        
        # 绘制对角线（和向量）
        sum_vector_diag = self.create_vector_arrow(
            self.O, self.D,
            self.COLOR_VECTOR_SUM,
            stroke_width=7
        )
        
        sum_label_diag = MathTex(
            r"\vec{a} + \vec{b}",
            font_size=28,
            color=self.COLOR_VECTOR_SUM
        ).move_to(self.get_vector_label_position(self.O, self.D, UP, 0.45))
        
        self.play(GrowArrow(sum_vector_diag), run_time=1.5)
        self.play(Write(sum_label_diag), run_time=0.5)
        
        # 高亮对角线
        self.play(Indicate(sum_vector_diag, scale_factor=1.1, color=self.COLOR_HIGHLIGHT), run_time=0.8)
        
        # 说明文字
        explanation = VGroup(
            Text("两向量从同一点出发", font="PingFang SC", font_size=20, color=WHITE),
            Text("和向量是平行四边形的对角线", font="PingFang SC", font_size=20, color=self.COLOR_VECTOR_SUM)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.8)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(annotation),
            FadeOut(annotation_arrow),
            FadeOut(parallelogram),
            FadeOut(point_b_dot),
            FadeOut(point_b_label),
            FadeOut(point_d_dot),
            FadeOut(vector_b_para),
            FadeOut(vector_b_label_para),
            FadeOut(sum_vector_diag),
            FadeOut(sum_label_diag),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_equivalence(self):
        """场景5: 两种法则等价性 (44-52秒)"""
        # 标题
        title = Text(
            "两种方法，结果相同！",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 左侧：三角形法则简图
        left_group = VGroup()
        o_left = LEFT * 2.5 + UP * 1
        a_left = o_left + RIGHT * 1.2 + UP * 0.7
        c_left = a_left + RIGHT * 0.9 + UP * 0.4
        
        vec_a_left = Arrow(o_left, a_left, buff=0, color=self.COLOR_VECTOR_A, stroke_width=4)
        vec_b_left = Arrow(a_left, c_left, buff=0, color=self.COLOR_VECTOR_B, stroke_width=4)
        vec_sum_left = Arrow(o_left, c_left, buff=0, color=self.COLOR_VECTOR_SUM, stroke_width=5)
        
        label_left = Text("三角形法则", font="PingFang SC", font_size=18, color=WHITE).move_to(o_left + DOWN * 1.2)
        
        left_group.add(vec_a_left, vec_b_left, vec_sum_left, label_left)
        
        # 右侧：平行四边形法则简图
        right_group = VGroup()
        o_right = RIGHT * 2.5 + UP * 1
        a_right = o_right + RIGHT * 1.2 + UP * 0.7
        b_right = o_right + RIGHT * 0.9 + UP * 0.4
        d_right = a_right + (b_right - o_right)
        
        vec_a_right = Arrow(o_right, a_right, buff=0, color=self.COLOR_VECTOR_A, stroke_width=4)
        vec_b_right = Arrow(o_right, b_right, buff=0, color=self.COLOR_VECTOR_B, stroke_width=4)
        para_right = Polygon(o_right, a_right, d_right, b_right, color=GRAY_B, stroke_width=2)
        vec_sum_right = Arrow(o_right, d_right, buff=0, color=self.COLOR_VECTOR_SUM, stroke_width=5)
        
        label_right = Text("平行四边形法则", font="PingFang SC", font_size=18, color=WHITE).move_to(o_right + DOWN * 1.2)
        
        right_group.add(para_right, vec_a_right, vec_b_right, vec_sum_right, label_right)
        
        # 动画展示
        self.play(Create(left_group), run_time=1.2)
        self.play(Create(right_group), run_time=1.2)
        
        # 等号
        equals_sign = MathTex("=", font_size=40, color=self.COLOR_HIGHLIGHT).move_to(UP * 1)
        self.play(FadeIn(equals_sign, scale=1.3), run_time=0.5)
        
        # 高亮结果向量
        self.play(
            Indicate(vec_sum_left, scale_factor=1.15, color=self.COLOR_HIGHLIGHT),
            Indicate(vec_sum_right, scale_factor=1.15, color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 说明文字
        explanation = Text(
            "可根据题目选择合适方法",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(left_group),
            FadeOut(right_group),
            FadeOut(equals_sign),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_opposite_vector(self):
        """场景6: 相反向量概念 (52-64秒)"""
        # 标题
        title = Text(
            "相反向量",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_VECTOR_NEG,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 向量b
        vector_b = self.create_vector_arrow(self.O, self.B, self.COLOR_VECTOR_B)
        vector_b_label = MathTex(r"\vec{b}", font_size=28, color=self.COLOR_VECTOR_B).next_to(vector_b, UP, buff=0.2)
        
        self.play(GrowArrow(vector_b), run_time=0.8)
        self.play(Write(vector_b_label), run_time=0.4)
        
        # 公式
        formula_neg = VGroup(
            MathTex(r"-\vec{b}", font_size=24, color=self.COLOR_VECTOR_NEG),
            Text("：与", font="PingFang SC", font_size=24, color=WHITE),
            MathTex(r"\vec{b}", font_size=24, color=WHITE),
            Text("长度相等，方向相反", font="PingFang SC", font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 5.5)
        
        self.play(Write(formula_neg), run_time=0.8)
        
        # 相反向量
        vector_neg_b = self.create_vector_arrow(self.O, self.neg_B, self.COLOR_VECTOR_NEG)
        vector_neg_b_label = MathTex(r"-\vec{b}", font_size=28, color=self.COLOR_VECTOR_NEG).next_to(vector_neg_b, DOWN, buff=0.2)
        
        self.play(GrowArrow(vector_neg_b), run_time=1.0)
        self.play(Write(vector_neg_b_label), run_time=0.4)
        
        # 对比标注
        comparison_brace_b = Brace(vector_b, direction=RIGHT, buff=0.1, color=self.COLOR_VECTOR_B)
        comparison_brace_neg = Brace(vector_neg_b, direction=LEFT, buff=0.1, color=self.COLOR_VECTOR_NEG)
        
        len_b = np.linalg.norm(self.vec_b)
        len_label = MathTex(f"L", font_size=20, color=WHITE)
        len_label_b = len_label.copy().next_to(comparison_brace_b, RIGHT, buff=0.05)
        len_label_neg = len_label.copy().next_to(comparison_brace_neg, LEFT, buff=0.05)
        
        self.play(
            FadeIn(comparison_brace_b),
            FadeIn(comparison_brace_neg),
            FadeIn(len_label_b),
            FadeIn(len_label_neg),
            run_time=0.8
        )
        
        # 说明文字
        explanation = VGroup(
            Text("长度相等", font="PingFang SC", font_size=22, color=WHITE),
            Text("方向相反（掉头）", font="PingFang SC", font_size=22, color=self.COLOR_VECTOR_NEG)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.8)
        
        # 长度相等演示
        self.play(
            Indicate(comparison_brace_b, scale_factor=1.15),
            Indicate(comparison_brace_neg, scale_factor=1.15),
            run_time=0.8
        )
        
        # 方向相反演示 - 旋转动画
        temp_arrow = vector_b.copy().set_color(YELLOW)
        self.play(FadeIn(temp_arrow), run_time=0.3)
        self.play(Rotate(temp_arrow, angle=PI, about_point=self.O), run_time=1.0)
        self.play(FadeOut(temp_arrow), run_time=0.3)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_neg),
            FadeOut(vector_b),
            FadeOut(vector_b_label),
            FadeOut(comparison_brace_b),
            FadeOut(comparison_brace_neg),
            FadeOut(len_label_b),
            FadeOut(len_label_neg),
            FadeOut(explanation),
            run_time=0.6
        )
        
        # 保留相反向量用于下一场景
        self.vector_neg_b = vector_neg_b
        self.vector_neg_b_label = vector_neg_b_label
    
    def show_vector_subtraction(self):
        """场景7: 向量减法运算 (64-76秒)"""
        # 标题
        title = Text(
            "向量减法",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_VECTOR_DIFF,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 公式
        formula_subtraction = MathTex(
            r"\vec{a} - \vec{b} = \vec{a} + (-\vec{b})",
            font_size=28,
            color=WHITE
        ).move_to(UP * 5.8)
        formula_subtraction[0][0:2].set_color(self.COLOR_VECTOR_A)
        formula_subtraction[0][3:5].set_color(self.COLOR_VECTOR_B)
        formula_subtraction[0][6:8].set_color(self.COLOR_VECTOR_A)
        formula_subtraction[0][9:13].set_color(self.COLOR_VECTOR_NEG)
        
        self.play(Write(formula_subtraction), run_time=1.0)
        
        # 向量a（重新绘制，因为之前可能被清理了）
        if not hasattr(self, 'vector_a') or self.vector_a not in self.mobjects:
            self.vector_a = self.create_vector_arrow(self.O, self.A, self.COLOR_VECTOR_A)
            self.vector_a_label = MathTex(r"\vec{a}", font_size=28, color=self.COLOR_VECTOR_A).move_to(
                self.get_vector_label_position(self.O, self.A, UP, 0.35)
            )
            self.play(GrowArrow(self.vector_a), Write(self.vector_a_label), run_time=0.5)
        
        self.wait(0.5)
        
        # 移动-b到从A开始（三角形法则）
        vector_neg_b_from_A = self.create_vector_arrow(self.A, self.diff_point, self.COLOR_VECTOR_NEG)
        vector_neg_b_label_moved = MathTex(r"-\vec{b}", font_size=28, color=self.COLOR_VECTOR_NEG).move_to(
            self.get_vector_label_position(self.A, self.diff_point, UP, 0.35)
        )
        
        # 淡出原位置的-b，在新位置显示
        self.play(
            FadeOut(self.vector_neg_b),
            FadeOut(self.vector_neg_b_label),
            run_time=0.4
        )
        
        self.play(
            GrowArrow(vector_neg_b_from_A),
            Write(vector_neg_b_label_moved),
            run_time=1.2
        )
        
        # 应用三角形法则
        annotation = Text(
            "应用三角形法则",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(annotation), run_time=0.5)
        self.wait(0.5)
        
        # 绘制差向量
        diff_vector = self.create_vector_arrow(
            self.O, self.diff_point,
            self.COLOR_VECTOR_DIFF,
            stroke_width=7
        )
        
        diff_label = MathTex(
            r"\vec{a} - \vec{b}",
            font_size=28,
            color=self.COLOR_VECTOR_DIFF
        ).move_to(self.get_vector_label_position(self.O, self.diff_point, DOWN, 0.4))
        
        self.play(GrowArrow(diff_vector), run_time=1.5)
        self.play(Write(diff_label), run_time=0.5)
        
        # 完整公式标注
        complete_formula = MathTex(
            r"\vec{a} - \vec{b} = \vec{a} + (-\vec{b})",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(complete_formula, shift=UP * 0.2), run_time=0.6)
        
        # 说明文字
        explanation = Text(
            "减法 = 加上相反向量",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.6)
        self.wait(2.0)
        
        # 清理所有场景元素
        self.play(
            FadeOut(title),
            FadeOut(formula_subtraction),
            FadeOut(annotation),
            FadeOut(complete_formula),
            FadeOut(explanation),
            FadeOut(self.vector_a),
            FadeOut(self.vector_a_label),
            FadeOut(vector_neg_b_from_A),
            FadeOut(vector_neg_b_label_moved),
            FadeOut(diff_vector),
            FadeOut(diff_label),
            FadeOut(self.origin_dot),
            run_time=0.6
        )
    
    def show_summary_and_outro(self):
        """场景8: 总结 + 片尾 (76-85秒)"""
        # 标题
        title = Text(
            "向量运算总结",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 三张卡片
        card1 = self.create_summary_card(
            "三角形法则",
            "首尾相接，首到尾",
            r"\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}",
            self.COLOR_VECTOR_SUM,
            UP * 3
        )
        
        card2 = self.create_summary_card(
            "平行四边形法则",
            "同起点，对角线",
            r"\overrightarrow{OA} + \overrightarrow{OB} = \overrightarrow{OC}",
            self.COLOR_VECTOR_SUM,
            UP * 0.8
        )
        
        card3 = self.create_summary_card(
            "向量减法",
            "加相反向量",
            r"\vec{a} - \vec{b} = \vec{a} + (-\vec{b})",
            self.COLOR_VECTOR_DIFF,
            DOWN * 1.4
        )
        
        cards = VGroup(card1, card2, card3)
        
        # 卡片从左侧滑入
        for card in cards:
            card.shift(LEFT * 10)
        
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 公式汇总闪烁
        for card in cards:
            self.play(Flash(card, color=self.COLOR_HIGHLIGHT, flash_radius=0.8), run_time=0.2)
        
        self.wait(1.0)
        
        # 清理准备片尾
        self.play(
            FadeOut(title),
            FadeOut(cards),
            run_time=0.5
        )
        
        # 作者信息放大
        author_name = Text(
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
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.5)
        
        # 向量箭头装饰
        vector_icons = VGroup(
            Arrow(LEFT * 0.6, LEFT * 0.2, buff=0, color=self.COLOR_VECTOR_A, stroke_width=4),
            Arrow(LEFT * 0.2, RIGHT * 0.2, buff=0, color=self.COLOR_VECTOR_B, stroke_width=4),
            Arrow(RIGHT * 0.2, RIGHT * 0.6, buff=0, color=self.COLOR_VECTOR_SUM, stroke_width=4)
        ).arrange(RIGHT, buff=0).scale(1.5).move_to(DOWN * 2)
        
        self.play(
            *[GrowArrow(icon) for icon in vector_icons],
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(vector_icons),
            run_time=1.0
        )
    
    def create_summary_card(self, title_text, content_text, formula_tex, color, position):
        """创建总结卡片"""
        # 标题
        title = Text(
            title_text,
            font="PingFang SC",
            font_size=24,
            color=color,
            weight=BOLD
        )
        
        # 内容
        content = Text(
            content_text,
            font="PingFang SC",
            font_size=18,
            color=WHITE
        )
        
        # 公式
        formula = MathTex(
            formula_tex,
            font_size=20,
            color=GRAY_A
        )
        
        # 组合
        card_content = VGroup(title, content, formula).arrange(DOWN, buff=0.2)
        
        # 背景框
        card_bg = RoundedRectangle(
            width=card_content.width + 0.8,
            height=card_content.height + 0.5,
            corner_radius=0.12,
            color=color,
            stroke_width=2,
            fill_opacity=0.08
        )
        
        card = VGroup(card_bg, card_content).move_to(position)
        
        return card


# 运行命令:
# manim -pql vector_addition_subtraction.py VectorAdditionSubtraction  # 快速预览
# manim -qh vector_addition_subtraction.py VectorAdditionSubtraction   # 高质量 1080p
# manim -qk vector_addition_subtraction.py VectorAdditionSubtraction   # 4K质量