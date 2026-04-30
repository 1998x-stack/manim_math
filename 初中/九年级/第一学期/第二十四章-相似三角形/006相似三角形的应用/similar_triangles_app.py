"""
相似三角形的应用 - Similar Triangles Applications
使用 Manim 创建的九年级数学教学视频

内容: 相似三角形在实际中的应用
  ① 利用影子测量建筑物高度
  ② 构造相似三角形测量河流宽度
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


class SimilarTrianglesApp(Scene):
    """
    相似三角形应用教学动画

    场景顺序:
    1. 开场钩子
    2. 相似三角形回顾
    3. 应用① - 影子法测量建筑物高度
    4. 影子法步骤总结
    5. 应用② - 构造法测量河流宽度
    6. 构造法步骤总结
    7. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_BUILDING = "#3498db"
        self.COLOR_PERSON = "#e74c3c"
        self.COLOR_TRI_BIG = "#2ecc71"
        self.COLOR_TRI_SMALL = "#f39c12"
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_RIVER = "#1abc9c"
        self.COLOR_GROUND = "#7f8c8d"
        self.FONT = "PingFang SC"

        # 预计算所有几何数据
        self.setup_geometry()

        # 动画序列
        self.show_opening()
        self.show_similar_review()
        self.show_building_height()
        self.show_building_summary()
        self.show_river_width()
        self.show_river_summary()
        self.show_outro()

    # ====================================================================
    # 几何数据统一初始化
    # ====================================================================
    def setup_geometry(self):
        """所有几何坐标在此统一计算"""

        # ---------- Scene 2: 相似三角形回顾 ----------
        # 大三角形 (左侧)
        self.rev_A1 = np.array([-3.5, -1.0, 0])
        self.rev_B1 = np.array([-0.5, -1.0, 0])
        self.rev_C1 = np.array([-1.8, 1.8, 0])

        # 小三角形 (右侧, 缩放0.5平移)
        k = 0.55
        base = np.array([1.0, -0.3, 0])
        self.rev_A2 = base
        self.rev_B2 = base + (self.rev_B1 - self.rev_A1) * k
        self.rev_C2 = base + (self.rev_C1 - self.rev_A1) * k

        # ---------- Scene 3: 建筑物高度 ----------
        # 所有坐标经过 verify_geometry.py 验证
        GROUND_Y = -2.0
        self.bld_B = np.array([-2.0, GROUND_Y, 0])           # 建筑底
        self.bld_T = np.array([-2.0, GROUND_Y + 5.0, 0])     # 建筑顶 (高5)
        self.bld_S = np.array([1.0, GROUND_Y, 0])            # 建筑影端 (影长3)
        self.prs_P = np.array([0.0, GROUND_Y, 0])            # 人脚
        self.prs_E = np.array([0.0, GROUND_Y + 1.0, 0])      # 人头 (人高1)
        self.prs_S = np.array([0.6, GROUND_Y, 0])            # 人影端 (影长0.6)

        # ---------- Scene 5: 河流宽度 ----------
        # 场景居中布置，整体上移
        self.riv_offset = np.array([0.0, 1.0, 0])
        self.riv_A = np.array([0.0, 2.0, 0]) + self.riv_offset   # 对岸点
        self.riv_B = np.array([0.0, -1.0, 0]) + self.riv_offset  # 本岸点
        self.riv_C = np.array([2.0, -1.0, 0]) + self.riv_offset  # C点
        self.riv_D = np.array([4.0, -1.0, 0]) + self.riv_offset  # D点
        self.riv_E = np.array([4.0, -4.0, 0]) + self.riv_offset  # E点

    # ====================================================================
    # Scene 1: 开场钩子
    # ====================================================================
    def show_opening(self):
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=self.FONT, font_size=18, color=GRAY_B
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook = Text(
            "一栋楼有多高？",
            font=self.FONT, font_size=38, color=self.COLOR_HIGHLIGHT,
            weight="BOLD"
        ).move_to(UP * 5.5)
        hook2 = Text(
            "不用爬上去就能算出来！",
            font=self.FONT, font_size=28, color=GRAY_A
        ).move_to(UP * 4.7)

        self.play(Write(hook), run_time=0.7)
        self.play(FadeIn(hook2), run_time=0.4)

        # 简单示意: 一个建筑轮廓 + 问号
        bld_outline = Polygon(
            np.array([-0.8, -1.5, 0]),
            np.array([0.8, -1.5, 0]),
            np.array([0.8, 2.5, 0]),
            np.array([-0.8, 2.5, 0]),
            color=self.COLOR_BUILDING, stroke_width=2.5, fill_opacity=0.15
        )
        q_mark = Text("?", font=self.FONT, font_size=52, color=self.COLOR_HIGHLIGHT).move_to(UP * 3.5)
        self.play(Create(bld_outline), run_time=0.6)
        self.play(FadeIn(q_mark), run_time=0.3)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook), FadeOut(hook2),
            FadeOut(bld_outline), FadeOut(q_mark),
            run_time=0.5
        )

    # ====================================================================
    # Scene 2: 相似三角形回顾
    # ====================================================================
    def show_similar_review(self):
        title = Text(
            "相似三角形 回顾",
            font=self.FONT, font_size=34, color=GOLD
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 大三角形
        tri1 = Polygon(
            self.rev_A1, self.rev_B1, self.rev_C1,
            color=self.COLOR_TRI_BIG, stroke_width=2.5, fill_opacity=0.12
        )
        self.play(Create(tri1), run_time=0.7)

        # 大三角形标签
        lA1 = Text("A", font=self.FONT, font_size=20, color=WHITE).next_to(self.rev_A1, DL, buff=0.12)
        lB1 = Text("B", font=self.FONT, font_size=20, color=WHITE).next_to(self.rev_B1, DR, buff=0.12)
        lC1 = Text("C", font=self.FONT, font_size=20, color=WHITE).next_to(self.rev_C1, UP, buff=0.12)
        self.play(FadeIn(lA1), FadeIn(lB1), FadeIn(lC1), run_time=0.3)

        # 小三角形
        tri2 = Polygon(
            self.rev_A2, self.rev_B2, self.rev_C2,
            color=self.COLOR_TRI_SMALL, stroke_width=2.5, fill_opacity=0.12
        )
        self.play(Create(tri2), run_time=0.7)

        lA2 = Text("A'", font=self.FONT, font_size=18, color=WHITE).next_to(self.rev_A2, DL, buff=0.1)
        lB2 = Text("B'", font=self.FONT, font_size=18, color=WHITE).next_to(self.rev_B2, DR, buff=0.1)
        lC2 = Text("C'", font=self.FONT, font_size=18, color=WHITE).next_to(self.rev_C2, UP, buff=0.1)
        self.play(FadeIn(lA2), FadeIn(lB2), FadeIn(lC2), run_time=0.3)

        # 角度标注 (用颜色点标注对应角)
        # ∠A对应 - 红色点
        dot_a1 = Dot(self.rev_A1, radius=0.08, color=RED)
        dot_a2 = Dot(self.rev_A2, radius=0.07, color=RED)
        # ∠B对应 - 蓝色点
        dot_b1 = Dot(self.rev_B1, radius=0.08, color=BLUE)
        dot_b2 = Dot(self.rev_B2, radius=0.07, color=BLUE)
        # ∠C对应 - 绿色点
        dot_c1 = Dot(self.rev_C1, radius=0.08, color=GREEN)
        dot_c2 = Dot(self.rev_C2, radius=0.07, color=GREEN)

        self.play(
            FadeIn(dot_a1), FadeIn(dot_a2),
            FadeIn(dot_b1), FadeIn(dot_b2),
            FadeIn(dot_c1), FadeIn(dot_c2),
            run_time=0.5
        )

        # 标注文字
        cond_text = Text(
            "对应角相等 → AA相似判定",
            font=self.FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(cond_text), run_time=0.5)

        # 比例关系公式
        ratio_formula = MathTex(
            r"\frac{AB}{A'B'} = \frac{BC}{B'C'} = \frac{CA}{C'A'} = k"
        ).move_to(DOWN * 4.8)
        ratio_formula.set_color(self.COLOR_HIGHLIGHT)
        self.play(Write(ratio_formula), run_time=0.8)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(tri1), FadeOut(tri2),
            FadeOut(lA1), FadeOut(lB1), FadeOut(lC1),
            FadeOut(lA2), FadeOut(lB2), FadeOut(lC2),
            FadeOut(dot_a1), FadeOut(dot_a2),
            FadeOut(dot_b1), FadeOut(dot_b2),
            FadeOut(dot_c1), FadeOut(dot_c2),
            FadeOut(cond_text), FadeOut(ratio_formula),
            run_time=0.5
        )

    # ====================================================================
    # Scene 3: 应用① - 影子法测量建筑物高度
    # ====================================================================
    def show_building_height(self):
        title = Text(
            "应用① : 影子法测量高度",
            font=self.FONT, font_size=30, color=self.COLOR_TRI_BIG
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # --- 地面线 ---
        ground = Line(
            np.array([-4.0, -2.0, 0]),
            np.array([3.5, -2.0, 0]),
            color=self.COLOR_GROUND, stroke_width=2
        )
        self.play(Create(ground), run_time=0.3)

        # --- 建筑物 (矩形轮廓) ---
        building = Polygon(
            self.bld_B,
            np.array([self.bld_B[0] + 0.6, self.bld_B[1], 0]),
            np.array([self.bld_B[0] + 0.6, self.bld_T[1], 0]),
            self.bld_T,
            color=self.COLOR_BUILDING, stroke_width=2.5, fill_opacity=0.2
        )
        self.play(Create(building), run_time=0.7)

        # 建筑标签
        lbl_h = Text("h", font=self.FONT, font_size=22, color=self.COLOR_BUILDING).move_to(
            np.array([-2.7, 0.5, 0])
        )
        self.play(FadeIn(lbl_h), run_time=0.3)

        # --- 人 (简单线段) ---
        person_body = Line(self.prs_P, self.prs_E, color=self.COLOR_PERSON, stroke_width=3)
        person_head = Circle(radius=0.1, color=self.COLOR_PERSON).move_to(
            self.prs_E + np.array([0, 0.1, 0])
        )
        self.play(Create(person_body), Create(person_head), run_time=0.5)

        lbl_h2 = Text("h'", font=self.FONT, font_size=18, color=self.COLOR_PERSON).move_to(
            np.array([-0.45, -1.6, 0])
        )
        self.play(FadeIn(lbl_h2), run_time=0.2)

        # --- 影子线段 ---
        shadow_bld = Line(self.bld_B, self.bld_S, color="#95a5a6", stroke_width=2.5)
        shadow_prs = Line(self.prs_P, self.prs_S, color="#95a5a6", stroke_width=2.5)
        self.play(Create(shadow_bld), Create(shadow_prs), run_time=0.5)

        # 影长标签
        lbl_L = Text("L", font=self.FONT, font_size=18, color=GRAY_A).move_to(
            np.array([-0.5, -2.4, 0])
        )
        lbl_L2 = Text("L'", font=self.FONT, font_size=16, color=GRAY_A).move_to(
            np.array([0.3, -2.4, 0])
        )
        self.play(FadeIn(lbl_L), FadeIn(lbl_L2), run_time=0.3)

        # --- 太阳光线 (平行虚线) ---
        sun_dir = self.bld_S - self.bld_T  # (3, -5, 0)
        sun_dir_norm = sun_dir / np.linalg.norm(sun_dir)

        sun_ray1 = DashedLine(
            self.bld_T - sun_dir_norm * 0.8,
            self.bld_S,
            color=YELLOW, stroke_width=1.5, dash_length=0.15
        )
        sun_ray2 = DashedLine(
            self.prs_E - sun_dir_norm * 0.5,
            self.prs_S,
            color=YELLOW, stroke_width=1.5, dash_length=0.15
        )
        self.play(Create(sun_ray1), Create(sun_ray2), run_time=0.6)

        sun_label = Text(
            "太阳光线 平行",
            font=self.FONT, font_size=18, color=YELLOW
        ).move_to(np.array([1.8, 1.5, 0]))
        self.play(FadeIn(sun_label), run_time=0.4)
        self.wait(0.5)

        # --- 高亮大三角形 (绿色) ---
        big_tri = Polygon(
            self.bld_T, self.bld_B, self.bld_S,
            color=self.COLOR_TRI_BIG, stroke_width=3, fill_opacity=0.1
        )
        self.play(Create(big_tri), run_time=0.6)
        lbl_big = Text(
            "大 △", font=self.FONT, font_size=18, color=self.COLOR_TRI_BIG
        ).move_to(np.array([-0.8, -0.5, 0]))
        self.play(FadeIn(lbl_big), run_time=0.3)

        # --- 高亮小三角形 (橙色) ---
        small_tri = Polygon(
            self.prs_E, self.prs_P, self.prs_S,
            color=self.COLOR_TRI_SMALL, stroke_width=3, fill_opacity=0.15
        )
        self.play(Create(small_tri), run_time=0.5)
        lbl_small = Text(
            "小 △", font=self.FONT, font_size=16, color=self.COLOR_TRI_SMALL
        ).move_to(np.array([0.55, -1.75, 0]))
        self.play(FadeIn(lbl_small), run_time=0.3)

        # --- AA相似标注 ---
        similar_text = Text(
            "∠B = ∠P = 90  且  太阳角相等",
            font=self.FONT, font_size=20, color=WHITE
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(similar_text), run_time=0.5)

        aa_text = Text(
            "→  AA相似  ✓",
            font=self.FONT, font_size=24, color=self.COLOR_HIGHLIGHT,
            weight="BOLD"
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(aa_text), run_time=0.4)
        self.wait(0.8)

        # --- 比例关系与求解 ---
        # 清理部分底部文字
        self.play(FadeOut(similar_text), FadeOut(aa_text), run_time=0.3)

        formula1 = MathTex(
            r"\frac{h}{h'} = \frac{L}{L'}"
        ).move_to(DOWN * 3.8)
        formula1.set_color(self.COLOR_HIGHLIGHT)
        self.play(Write(formula1), run_time=0.7)

        formula2 = MathTex(
            r"\frac{h}{1} = \frac{3}{0.6}"
        ).move_to(DOWN * 4.6)
        self.play(Write(formula2), run_time=0.6)

        formula3 = MathTex(
            r"h = 5"
        ).move_to(DOWN * 5.4)
        formula3.set_color(self.COLOR_TRI_BIG)
        unit_label = Text(
            "(单位长度)", font=self.FONT, font_size=18, color=self.COLOR_TRI_BIG
        ).next_to(formula3, RIGHT, buff=0.2)
        self.play(Write(formula3), run_time=0.5)
        self.play(FadeIn(unit_label), run_time=0.3)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(ground), FadeOut(building),
            FadeOut(lbl_h), FadeOut(person_body), FadeOut(person_head),
            FadeOut(lbl_h2), FadeOut(shadow_bld), FadeOut(shadow_prs),
            FadeOut(lbl_L), FadeOut(lbl_L2),
            FadeOut(sun_ray1), FadeOut(sun_ray2), FadeOut(sun_label),
            FadeOut(big_tri), FadeOut(small_tri),
            FadeOut(lbl_big), FadeOut(lbl_small),
            FadeOut(formula1), FadeOut(formula2), FadeOut(formula3), FadeOut(unit_label),
            run_time=0.5
        )

    # ====================================================================
    # Scene 4: 影子法步骤总结
    # ====================================================================
    def show_building_summary(self):
        title = Text(
            "影子法 — 步骤总结",
            font=self.FONT, font_size=30, color=self.COLOR_TRI_BIG
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        steps = [
            "① 在阳光下，测量人影长 L'",
            "② 同时测量人的身高 h'",
            "③ 测量目标物的影长 L",
            "④ 利用相似比: h / h' = L / L'",
            "⑤ 求解目标高度 h",
        ]
        colors = [GRAY_A, GRAY_A, GRAY_A, self.COLOR_HIGHLIGHT, self.COLOR_TRI_BIG]
        y_positions = [4.5, 3.5, 2.5, 1.2, 0.0]

        step_objs = []
        for i, (s, c, y) in enumerate(zip(steps, colors, y_positions)):
            txt = Text(s, font=self.FONT, font_size=22, color=c).move_to(
                np.array([-0.2, y, 0])
            )
            txt.align_to(np.array([-3.5, y, 0]), LEFT)
            step_objs.append(txt)
            self.play(FadeIn(txt, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.15)

        # 关键公式
        key_formula = MathTex(
            r"h = h' \times \frac{L}{L'}"
        ).move_to(DOWN * 2.5)
        key_formula.set_color(self.COLOR_HIGHLIGHT)
        box = SurroundingRectangle(key_formula, color=self.COLOR_HIGHLIGHT, buff=0.3)
        self.play(Write(key_formula), run_time=0.6)
        self.play(Create(box), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(box), FadeOut(key_formula),
            *[FadeOut(s) for s in step_objs],
            run_time=0.5
        )

    # ====================================================================
    # Scene 5: 应用② - 构造法测量河流宽度
    # ====================================================================
    def show_river_width(self):
        title = Text(
            "应用② : 构造法测量河宽",
            font=self.FONT, font_size=30, color=self.COLOR_RIVER
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # --- 画河流 (蓝色带状区域) ---
        # 河流区域: 对岸y=3 到 本岸y=0 (带偏移后)
        river_top = self.riv_A[1] + 0.5
        river_bot = self.riv_B[1] - 0.3
        river = Polygon(
            np.array([-4.5, river_top, 0]),
            np.array([4.5, river_top, 0]),
            np.array([4.5, river_bot, 0]),
            np.array([-4.5, river_bot, 0]),
            color=self.COLOR_RIVER, fill_opacity=0.12, stroke_width=1.5
        )
        river_label = Text(
            "河流", font=self.FONT, font_size=18, color=self.COLOR_RIVER
        ).move_to(np.array([-3.5, (river_top + river_bot) / 2, 0]))

        self.play(Create(river), run_time=0.5)
        self.play(FadeIn(river_label), run_time=0.3)

        # --- 对岸线和本岸线 ---
        shore_top = Line(
            np.array([-4.5, river_top, 0]),
            np.array([4.5, river_top, 0]),
            color=self.COLOR_RIVER, stroke_width=2
        )
        shore_bot = Line(
            np.array([-4.5, river_bot, 0]),
            np.array([4.5, river_bot, 0]),
            color=self.COLOR_RIVER, stroke_width=2
        )
        self.play(Create(shore_top), Create(shore_bot), run_time=0.3)

        # --- 点 A (对岸) 和 B (本岸) ---
        dot_A = Dot(self.riv_A, radius=0.09, color=WHITE)
        dot_B = Dot(self.riv_B, radius=0.09, color=WHITE)
        lbl_A = Text("A", font=self.FONT, font_size=22, color=WHITE).next_to(self.riv_A, LEFT, buff=0.15)
        lbl_B = Text("B", font=self.FONT, font_size=22, color=WHITE).next_to(self.riv_B, LEFT, buff=0.15)

        self.play(FadeIn(dot_A), FadeIn(lbl_A), run_time=0.3)
        self.play(FadeIn(dot_B), FadeIn(lbl_B), run_time=0.3)

        # AB连线(虚线，表示无法测量)
        line_AB = DashedLine(self.riv_A, self.riv_B, color=RED, dash_length=0.15, stroke_width=2)
        no_measure = Text(
            "AB 无法直接测量",
            font=self.FONT, font_size=18, color=RED
        ).move_to(np.array([-2.2, (self.riv_A[1] + self.riv_B[1]) / 2, 0]))
        self.play(Create(line_AB), run_time=0.4)
        self.play(FadeIn(no_measure), run_time=0.3)
        self.wait(0.8)
        self.play(FadeOut(no_measure), run_time=0.2)

        # --- 步骤① : 画 BC ⊥ AB ---
        step1_txt = Text(
            "步骤①: 沿河岸取C, 使BC⊥AB",
            font=self.FONT, font_size=18, color=GRAY_A
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(step1_txt), run_time=0.3)

        dot_C = Dot(self.riv_C, radius=0.09, color=WHITE)
        lbl_C = Text("C", font=self.FONT, font_size=22, color=WHITE).next_to(self.riv_C, DOWN, buff=0.15)
        line_BC = Line(self.riv_B, self.riv_C, color=WHITE, stroke_width=2)

        self.play(Create(line_BC), run_time=0.5)
        self.play(FadeIn(dot_C), FadeIn(lbl_C), run_time=0.3)

        # 直角符号
        ra_size = 0.18
        vec_BA = self.riv_A - self.riv_B
        vec_BC_dir = self.riv_C - self.riv_B
        vec_BA_n = vec_BA / np.linalg.norm(vec_BA) * ra_size
        vec_BC_n = vec_BC_dir / np.linalg.norm(vec_BC_dir) * ra_size
        right_angle_B = Polygon(
            self.riv_B + vec_BA_n,
            self.riv_B + vec_BA_n + vec_BC_n,
            self.riv_B + vec_BC_n,
            color=YELLOW, stroke_width=1.5, fill_opacity=0
        )
        self.play(FadeIn(right_angle_B), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(step1_txt), run_time=0.2)

        # --- 步骤② : 取D使C为BD中点 ---
        step2_txt = Text(
            "步骤②: 在BC延长线上取D, 使BC=CD",
            font=self.FONT, font_size=18, color=GRAY_A
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(step2_txt), run_time=0.3)

        dot_D = Dot(self.riv_D, radius=0.09, color=WHITE)
        lbl_D = Text("D", font=self.FONT, font_size=22, color=WHITE).next_to(self.riv_D, DOWN, buff=0.15)
        line_CD = Line(self.riv_C, self.riv_D, color=WHITE, stroke_width=2)

        self.play(Create(line_CD), run_time=0.5)
        self.play(FadeIn(dot_D), FadeIn(lbl_D), run_time=0.3)

        # BC=CD标注
        bc_eq = Text(
            "BC = CD", font=self.FONT, font_size=16, color=self.COLOR_HIGHLIGHT
        ).move_to(np.array([2.0, self.riv_C[1] + 0.3, 0]))
        self.play(FadeIn(bc_eq), run_time=0.3)
        self.wait(0.4)
        self.play(FadeOut(step2_txt), run_time=0.2)

        # --- 步骤③ : 连接CA延长线交DE于E ---
        step3_txt = Text(
            "步骤③: 过D作DE⊥BD, 交CA延长线于E",
            font=self.FONT, font_size=18, color=GRAY_A
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(step3_txt), run_time=0.3)

        # CA延长线 (虚线, 从A延长到E方向)
        line_CA_ext = DashedLine(
            self.riv_A, self.riv_E,
            color=self.COLOR_AUXILIARY, dash_length=0.12, stroke_width=1.5
        )
        self.play(Create(line_CA_ext), run_time=0.5)

        # DE线段
        dot_E = Dot(self.riv_E, radius=0.09, color=WHITE)
        lbl_E = Text("E", font=self.FONT, font_size=22, color=WHITE).next_to(self.riv_E, RIGHT, buff=0.15)
        line_DE = Line(self.riv_D, self.riv_E, color=WHITE, stroke_width=2)

        self.play(Create(line_DE), run_time=0.5)
        self.play(FadeIn(dot_E), FadeIn(lbl_E), run_time=0.3)

        # 直角符号在D
        vec_DC = self.riv_C - self.riv_D
        vec_DE_dir = self.riv_E - self.riv_D
        vec_DC_n = vec_DC / np.linalg.norm(vec_DC) * ra_size
        vec_DE_n = vec_DE_dir / np.linalg.norm(vec_DE_dir) * ra_size
        right_angle_D = Polygon(
            self.riv_D + vec_DC_n,
            self.riv_D + vec_DC_n + vec_DE_n,
            self.riv_D + vec_DE_n,
            color=YELLOW, stroke_width=1.5, fill_opacity=0
        )
        self.play(FadeIn(right_angle_D), run_time=0.3)
        self.wait(0.4)
        self.play(FadeOut(step3_txt), run_time=0.2)

        # --- 高亮两个相似三角形 ---
        # △BCA (绿色)
        tri_BCA = Polygon(
            self.riv_B, self.riv_C, self.riv_A,
            color=self.COLOR_TRI_BIG, stroke_width=3, fill_opacity=0.12
        )
        self.play(Create(tri_BCA), run_time=0.6)
        lbl_tri1 = Text(
            "△BCA", font=self.FONT, font_size=16, color=self.COLOR_TRI_BIG
        ).move_to(np.array([0.5, 0.8, 0]))
        self.play(FadeIn(lbl_tri1), run_time=0.2)

        # △DCE (橙色)
        tri_DCE = Polygon(
            self.riv_D, self.riv_C, self.riv_E,
            color=self.COLOR_TRI_SMALL, stroke_width=3, fill_opacity=0.12
        )
        self.play(Create(tri_DCE), run_time=0.6)
        lbl_tri2 = Text(
            "△DCE", font=self.FONT, font_size=16, color=self.COLOR_TRI_SMALL
        ).move_to(np.array([3.2, -1.0, 0]))
        self.play(FadeIn(lbl_tri2), run_time=0.2)

        # --- 相似推导 ---
        derive1 = Text(
            "∠BCA = ∠DCE (对顶角)",
            font=self.FONT, font_size=18, color=GRAY_A
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(derive1), run_time=0.4)

        derive2 = Text(
            "∠ABC = ∠CDE = 90  →  AA相似",
            font=self.FONT, font_size=18, color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.3)
        self.play(FadeIn(derive2), run_time=0.4)

        derive3 = Text(
            "BC = CD  →  AB = DE",
            font=self.FONT, font_size=20, color=self.COLOR_TRI_BIG,
            weight="BOLD"
        ).move_to(DOWN * 6.2)
        self.play(FadeIn(derive3), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(river), FadeOut(river_label),
            FadeOut(shore_top), FadeOut(shore_bot),
            FadeOut(dot_A), FadeOut(dot_B), FadeOut(dot_C),
            FadeOut(dot_D), FadeOut(dot_E),
            FadeOut(lbl_A), FadeOut(lbl_B), FadeOut(lbl_C),
            FadeOut(lbl_D), FadeOut(lbl_E),
            FadeOut(line_AB), FadeOut(line_BC), FadeOut(line_CD),
            FadeOut(line_CA_ext), FadeOut(line_DE),
            FadeOut(right_angle_B), FadeOut(right_angle_D),
            FadeOut(bc_eq),
            FadeOut(tri_BCA), FadeOut(tri_DCE),
            FadeOut(lbl_tri1), FadeOut(lbl_tri2),
            FadeOut(derive1), FadeOut(derive2), FadeOut(derive3),
            run_time=0.6
        )

    # ====================================================================
    # Scene 6: 构造法步骤总结
    # ====================================================================
    def show_river_summary(self):
        title = Text(
            "构造法 — 步骤总结",
            font=self.FONT, font_size=30, color=self.COLOR_RIVER
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        steps = [
            "① 本岸取点B对着对岸目标A",
            "② 沿河岸取C, 测量BC (BC⊥AB)",
            "③ 延长BC取D, 使BC = CD",
            "④ 过D作DE⊥BD",
            "⑤ 连CA延长交DE于E, 测量DE",
            "⑥ 由相似比得: AB = DE",
        ]
        colors = [GRAY_A, GRAY_A, GRAY_A, GRAY_A, GRAY_A, self.COLOR_TRI_BIG]
        y_positions = [5.0, 4.1, 3.2, 2.3, 1.4, 0.2]

        step_objs = []
        for i, (s, c, y) in enumerate(zip(steps, colors, y_positions)):
            txt = Text(s, font=self.FONT, font_size=20, color=c).move_to(
                np.array([-0.2, y, 0])
            )
            txt.align_to(np.array([-3.5, y, 0]), LEFT)
            step_objs.append(txt)
            self.play(FadeIn(txt, shift=RIGHT * 0.3), run_time=0.35)
            self.wait(0.1)

        # 核心结论
        conclusion = Text(
            "核心思路: 通过构造全等/相似三角形",
            font=self.FONT, font_size=18, color=GRAY_A
        ).move_to(DOWN * 2.0)
        conclusion2 = Text(
            "将不可测量的距离转化为可测量的距离",
            font=self.FONT, font_size=20, color=self.COLOR_HIGHLIGHT,
            weight="BOLD"
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(conclusion), run_time=0.3)
        self.play(FadeIn(conclusion2), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(conclusion), FadeOut(conclusion2),
            *[FadeOut(s) for s in step_objs],
            run_time=0.5
        )

    # ====================================================================
    # Scene 7: 片尾
    # ====================================================================
    def show_outro(self):
        # 总结横幅
        summary = Text(
            "相似三角形应用核心公式",
            font=self.FONT, font_size=28, color=GOLD
        ).move_to(UP * 5.0)
        self.play(FadeIn(summary), run_time=0.4)

        f1 = Text(
            "影子法:  h = h' × L / L'",
            font=self.FONT, font_size=22, color=self.COLOR_TRI_BIG
        ).move_to(UP * 3.8)
        f2 = Text(
            "构造法:  转化为可测量距离",
            font=self.FONT, font_size=22, color=self.COLOR_RIVER
        ).move_to(UP * 2.9)
        self.play(FadeIn(f1), run_time=0.3)
        self.play(FadeIn(f2), run_time=0.3)
        self.wait(1.0)

        # 清理顶部
        self.play(
            FadeOut(summary), FadeOut(f1), FadeOut(f2),
            run_time=0.4
        )

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=self.FONT, font_size=38, color=WHITE
        ).move_to(UP * 1.5)
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT, font_size=28, color=GRAY_B
        ).move_to(UP * 0.6)

        self.play(
            Transform(self.author_info, author_big),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=self.FONT, font_size=26, color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # 装饰元素: 小三角形
        deco_tris = VGroup(*[
            Polygon(
                np.array([0, 0.25, 0]),
                np.array([-0.2, -0.1, 0]),
                np.array([0.2, -0.1, 0]),
                color=GOLD, fill_opacity=0.7, stroke_width=1
            ).move_to(np.array([
                1.8 * np.cos(i * PI / 3 + PI / 6),
                -2.5 + 1.4 * np.sin(i * PI / 3 + PI / 6),
                0
            ]))
            for i in range(6)
        ])
        self.play(
            *[FadeIn(t, scale=0.3) for t in deco_tris],
            run_time=0.6
        )
        self.wait(1.5)

        # 淡出
        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(deco_tris),
            run_time=1.0
        )


# 运行命令:
# manim -pql similar_triangles_app.py SimilarTrianglesApp   # 快速预览
# manim -qh similar_triangles_app.py SimilarTrianglesApp    # 高质量渲染