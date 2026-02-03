"""
三角形的三边关系 — 教学动画
Triangle Three-Side Relationship — Teaching Animation

知识点: 三角形任意两边之和大于第三边，任意两边之差小于第三边
目标受众: 七年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景顺序:
  1. 开场钩子
  2. 画三角形 + 标记三边
  3. 核心定理：两边之和 > 第三边（数轴拼线演示）
  4. 推论：两边之差 < 第三边（综合不等式）
  5. 实例验证（能组 vs 不能组）
  6. 总结卡
  7. 片尾
"""

from manim import *
import numpy as np

# ──────────────────────────────────────────────
# 全局配置 — TikTok 竖屏
# ──────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ──────────────────────────────────────────────
# 颜色常量
# ──────────────────────────────────────────────
BG_COLOR        = "#1a1a2e"
COLOR_SIDE_A    = "#e74c3c"   # 红 — 边a(BC)
COLOR_SIDE_B    = "#3498db"   # 蓝 — 边b(CA)
COLOR_SIDE_C    = "#2ecc71"   # 绿 — 边c(AB)
COLOR_HIGHLIGHT = YELLOW
COLOR_AUX       = GRAY_B
COLOR_OK        = "#2ecc71"   # 绿 ✓
COLOR_FAIL      = "#e74c3c"   # 红 ✗
FONT            = "Noto Sans CJK SC"


class TriangleSideRelation(Scene):
    """三角形三边关系教学动画"""

    # ──── 构建入口 ─────────────────────────────
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()          # 阶段1: 统一几何初始化
        self.scene_1_hook()            # 开场钩子
        self.scene_2_triangle()        # 画三角形+标记
        self.scene_3_sum_rule()        # 两边之和 > 第三边
        self.scene_4_diff_rule()       # 两边之差 < 第三边
        self.scene_5_examples()        # 实例验证
        self.scene_6_summary()         # 总结
        self.scene_7_outro()           # 片尾

    # ──── 阶段1: 统一几何初始化 ─────────────────
    def setup_geometry(self):
        """所有几何数据在此统一计算，后续场景仅引用"""

        # ── 三角形顶点（余弦定理反推，与 verify_geometry.py 一致） ──
        a_target, b_target = 4.5, 3.8
        A_raw = np.array([-2.6, -0.8, 0])
        B_raw = np.array([ 2.6, -0.8, 0])
        c_len = np.linalg.norm(B_raw - A_raw)  # 5.2

        cos_A = (b_target**2 + c_len**2 - a_target**2) / (2 * b_target * c_len)
        sin_A = np.sqrt(1 - cos_A**2)
        C_raw = A_raw + b_target * np.array([cos_A, sin_A, 0])

        OFFSET = np.array([0, 1.2, 0])
        self.A = A_raw + OFFSET
        self.B = B_raw + OFFSET
        self.C = C_raw + OFFSET

        # ── 边长缓存 ──
        self.len_a = np.linalg.norm(self.C - self.B)  # BC
        self.len_b = np.linalg.norm(self.A - self.C)  # CA
        self.len_c = np.linalg.norm(self.B - self.A)  # AB

        # ── 角度与叉积（用于Angle方向判断） ──
        # ∠A: from B, vertex A, to C → cross_z > 0 → CCW → other_angle=False
        # ∠B: from A, vertex B, to C → cross_z < 0 → CW  → other_angle=True
        # ∠C: from A, vertex C, to B → cross_z > 0 → CCW → other_angle=False

        # ── 中点 ──
        self.M_AB = (self.A + self.B) / 2
        self.M_BC = (self.B + self.C) / 2
        self.M_CA = (self.C + self.A) / 2

        # ── 实例数据 ──
        self.examples = [
            {"name": "例1", "sides": [3, 4, 5], "can": True},
            {"name": "例2", "sides": [1, 2, 4], "can": False},
            {"name": "例3", "sides": [2, 3, 4], "can": True},
        ]

        print("✓ setup_geometry 完成")

    # ================================================================
    # Scene 1: 开场钩子 (3-4s)
    # ================================================================
    def scene_1_hook(self):
        # 作者信息（始终保留在顶部）
        self.author_tag = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_tag, shift=DOWN * 0.3), run_time=0.4)

        # 钩子问题
        hook = Text(
            "3 条线段能拼成三角形吗？",
            font=FONT, font_size=34, color=COLOR_HIGHLIGHT, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(Write(hook), run_time=0.8)
        self.wait(0.4)

        # 画3条长度不同的线段，暗示有悬疑
        seg_y = 3.8
        seg1 = Line([-3.2, seg_y, 0], [-0.2, seg_y, 0], color=COLOR_SIDE_A, stroke_width=4)   # 长3.0
        seg2 = Line([-1.8, seg_y - 1.2, 0], [0.6, seg_y - 1.2, 0], color=COLOR_SIDE_B, stroke_width=4)  # 长2.4
        seg3 = Line([-2.5, seg_y - 2.4, 0], [2.5, seg_y - 2.4, 0], color=COLOR_SIDE_C, stroke_width=4)  # 长5.0 (长!)

        self.play(Create(seg1), run_time=0.4)
        self.play(Create(seg2), run_time=0.4)
        self.play(Create(seg3), run_time=0.4)
        self.wait(1.2)  # 让学生看一看

        # 清除
        self.play(FadeOut(seg1), FadeOut(seg2), FadeOut(seg3), FadeOut(hook), run_time=0.5)

    # ================================================================
    # Scene 2: 画三角形 + 标记三边 (7-8s)
    # ================================================================
    def scene_2_triangle(self):
        # 标题
        title = Text("三角形的三边关系", font=FONT, font_size=34, color=WHITE, weight=BOLD).move_to(UP * 5.8)
        self.play(FadeIn(title), run_time=0.4)

        # 画三角形三边（分别着色）
        side_a = Line(self.B, self.C, color=COLOR_SIDE_A, stroke_width=4)  # BC = a
        side_b = Line(self.C, self.A, color=COLOR_SIDE_B, stroke_width=4)  # CA = b
        side_c = Line(self.A, self.B, color=COLOR_SIDE_C, stroke_width=4)  # AB = c

        self.play(Create(side_c), run_time=0.6)
        self.play(Create(side_a), run_time=0.6)
        self.play(Create(side_b), run_time=0.6)

        # 顶点标签
        lbl_A = Text("A", font=FONT, font_size=28, color=WHITE, weight=BOLD).next_to(self.A, DL, buff=0.25)
        lbl_B = Text("B", font=FONT, font_size=28, color=WHITE, weight=BOLD).next_to(self.B, DR, buff=0.25)
        lbl_C = Text("C", font=FONT, font_size=28, color=WHITE, weight=BOLD).next_to(self.C, UP, buff=0.25)
        self.play(Write(lbl_A), Write(lbl_B), Write(lbl_C), run_time=0.5)

        # 顶点小点
        dot_A = Dot(self.A, color=WHITE, radius=0.06)
        dot_B = Dot(self.B, color=WHITE, radius=0.06)
        dot_C = Dot(self.C, color=WHITE, radius=0.06)
        self.play(FadeIn(dot_A), FadeIn(dot_B), FadeIn(dot_C), run_time=0.3)

        # 边长标注（用Text放在边的中点附近）
        mid_a = (self.B + self.C) / 2
        mid_b = (self.C + self.A) / 2
        mid_c = (self.A + self.B) / 2

        # 计算法线方向把标签放在边的外侧
        def outward_normal(P1, P2, opposite):
            """计算边P1P2的朝外法线方向"""
            edge = P2 - P1
            n = np.array([-edge[1], edge[0], 0])
            n = n / np.linalg.norm(n)
            # 确保指向远离对边顶点的方向
            if np.dot(n, opposite - (P1+P2)/2) > 0:
                n = -n
            return n

        n_a = outward_normal(self.B, self.C, self.A)
        n_b = outward_normal(self.C, self.A, self.B)
        n_c = outward_normal(self.A, self.B, self.C)

        offset_dist = 0.45
        lbl_a = Text("a", font=FONT, font_size=26, color=COLOR_SIDE_A, weight=BOLD).move_to(mid_a + n_a * offset_dist)
        lbl_b = Text("b", font=FONT, font_size=26, color=COLOR_SIDE_B, weight=BOLD).move_to(mid_b + n_b * offset_dist)
        lbl_c = Text("c", font=FONT, font_size=26, color=COLOR_SIDE_C, weight=BOLD).move_to(mid_c + n_c * offset_dist)

        self.play(FadeIn(lbl_a), FadeIn(lbl_b), FadeIn(lbl_c), run_time=0.5)

        # 底部说明
        explain = Text("a = BC,  b = CA,  c = AB", font=FONT, font_size=21, color=GRAY_A).move_to(DOWN * 3.8)
        self.play(FadeIn(explain), run_time=0.4)
        self.wait(1.5)

        # 保存引用以便后续场景使用
        self.side_a, self.side_b, self.side_c = side_a, side_b, side_c
        self.lbl_A, self.lbl_B, self.lbl_C = lbl_A, lbl_B, lbl_C
        self.dot_A, self.dot_B, self.dot_C = dot_A, dot_B, dot_C
        self.lbl_a, self.lbl_b, self.lbl_c = lbl_a, lbl_b, lbl_c
        self.title_s2 = title
        self.explain_s2 = explain

    # ================================================================
    # Scene 3: 核心定理 — 两边之和 > 第三边 (12-14s)
    # ================================================================
    def scene_3_sum_rule(self):
        # 清除底部说明
        self.play(FadeOut(self.explain_s2), run_time=0.3)

        # 更新标题
        new_title = Text("两边之和 > 第三边", font=FONT, font_size=30, color=COLOR_HIGHLIGHT, weight=BOLD).move_to(UP * 5.8)
        self.play(ReplacementTransform(self.title_s2, new_title), run_time=0.5)

        # ── 步骤1: 写出三个不等式 ──
        ineq1 = VGroup(
            Text("a + b", font=FONT, font_size=24, color=WHITE),
            Text(">", font=FONT, font_size=24, color=COLOR_HIGHLIGHT),
            Text("c", font=FONT, font_size=24, color=COLOR_SIDE_C),
        ).arrange(RIGHT, buff=0.15).move_to(np.array([-2.2, -2.8, 0]))

        ineq2 = VGroup(
            Text("b + c", font=FONT, font_size=24, color=WHITE),
            Text(">", font=FONT, font_size=24, color=COLOR_HIGHLIGHT),
            Text("a", font=FONT, font_size=24, color=COLOR_SIDE_A),
        ).arrange(RIGHT, buff=0.15).move_to(np.array([0.0, -2.8, 0]))

        ineq3 = VGroup(
            Text("a + c", font=FONT, font_size=24, color=WHITE),
            Text(">", font=FONT, font_size=24, color=COLOR_HIGHLIGHT),
            Text("b", font=FONT, font_size=24, color=COLOR_SIDE_B),
        ).arrange(RIGHT, buff=0.15).move_to(np.array([2.2, -2.8, 0]))

        # 居中排列三个不等式
        ineq_group = VGroup(ineq1, ineq2, ineq3).arrange(RIGHT, buff=0.6).move_to(np.array([0, -2.8, 0]))

        self.play(FadeIn(ineq1), run_time=0.5)
        self.play(FadeIn(ineq2), run_time=0.5)
        self.play(FadeIn(ineq3), run_time=0.5)
        self.wait(1.0)

        # ── 步骤2: 数轴上直观演示 a + b vs c ──
        # "把 a 和 b 拼在一起，比较总长度与 c"
        demo_text = Text("把 a 和 b 拼成一段，与 c 比较：", font=FONT, font_size=21, color=GRAY_A).move_to(np.array([0, -4.2, 0]))
        self.play(FadeIn(demo_text), run_time=0.4)

        # 数轴参数
        NL_Y = -5.5
        NL_LEFT = -3.5
        NL_RIGHT = 3.5
        NL_RANGE = 10.0  # 数值范围 [0, 10]

        def val_to_x(v):
            return NL_LEFT + (v / NL_RANGE) * (NL_RIGHT - NL_LEFT)

        # 画数轴底线
        axis_line = Line([NL_LEFT, NL_Y, 0], [NL_RIGHT, NL_Y, 0], color=GRAY_B, stroke_width=1.5)
        # 零点标记
        tick_0 = Line([NL_LEFT, NL_Y - 0.08, 0], [NL_LEFT, NL_Y + 0.08, 0], color=GRAY_B, stroke_width=2)
        label_0 = Text("0", font=FONT, font_size=16, color=GRAY_B).move_to(np.array([NL_LEFT, NL_Y - 0.3, 0]))
        self.play(Create(axis_line), FadeIn(tick_0), FadeIn(label_0), run_time=0.4)

        # a 段（红色）
        a_val = self.len_a  # 4.5
        b_val = self.len_b  # 3.8
        c_val = self.len_c  # 5.2

        x_a_end = val_to_x(a_val)
        seg_a_demo = Line([NL_LEFT, NL_Y, 0], [x_a_end, NL_Y, 0], color=COLOR_SIDE_A, stroke_width=6)
        lbl_a_demo = Text("a", font=FONT, font_size=20, color=COLOR_SIDE_A, weight=BOLD).move_to(
            np.array([(NL_LEFT + x_a_end)/2, NL_Y + 0.3, 0])
        )
        self.play(Create(seg_a_demo), run_time=0.6)
        self.play(FadeIn(lbl_a_demo), run_time=0.3)

        # b 段（蓝色，接在a后面）
        x_ab_end = val_to_x(a_val + b_val)
        seg_b_demo = Line([x_a_end, NL_Y, 0], [x_ab_end, NL_Y, 0], color=COLOR_SIDE_B, stroke_width=6)
        lbl_b_demo = Text("b", font=FONT, font_size=20, color=COLOR_SIDE_B, weight=BOLD).move_to(
            np.array([(x_a_end + x_ab_end)/2, NL_Y + 0.3, 0])
        )
        self.play(Create(seg_b_demo), run_time=0.6)
        self.play(FadeIn(lbl_b_demo), run_time=0.3)

        # a+b 总长标注
        x_ab_mid = (NL_LEFT + x_ab_end) / 2
        lbl_sum = Text("a + b", font=FONT, font_size=18, color=WHITE).move_to(
            np.array([x_ab_mid, NL_Y - 0.45, 0])
        )
        self.play(FadeIn(lbl_sum), run_time=0.3)
        self.wait(0.5)

        # c 段（绿色虚线，从0开始画，用于对比）
        # 画在数轴上方一点，错开位置便于比较
        C_Y = NL_Y + 0.85
        x_c_end = val_to_x(c_val)
        seg_c_demo = DashedLine([NL_LEFT, C_Y, 0], [x_c_end, C_Y, 0], color=COLOR_SIDE_C, stroke_width=5, dash_length=0.15)
        lbl_c_demo = Text("c", font=FONT, font_size=20, color=COLOR_SIDE_C, weight=BOLD).move_to(
            np.array([(NL_LEFT + x_c_end)/2, C_Y + 0.25, 0])
        )
        self.play(Create(seg_c_demo), run_time=0.6)
        self.play(FadeIn(lbl_c_demo), run_time=0.3)
        self.wait(0.4)

        # 箭头指示 a+b 超出 c 的部分（视觉突出）
        arrow_mark = Arrow(start=[x_c_end, C_Y, 0], end=[x_ab_end, NL_Y, 0],
                           color=COLOR_HIGHLIGHT, stroke_width=2.5, tip_length=0.18)
        gt_text = Text("a+b > c  ✓", font=FONT, font_size=22, color=COLOR_HIGHLIGHT, weight=BOLD).move_to(
            np.array([2.5, NL_Y - 0.85, 0])
        )
        self.play(Create(arrow_mark), run_time=0.5)
        self.play(FadeIn(gt_text), run_time=0.4)
        self.wait(1.8)  # 关键停留

        # 清除数轴区域
        demo_elements = [axis_line, tick_0, label_0, seg_a_demo, lbl_a_demo,
                         seg_b_demo, lbl_b_demo, lbl_sum, seg_c_demo, lbl_c_demo,
                         arrow_mark, gt_text, demo_text]
        self.play(*[FadeOut(e) for e in demo_elements], run_time=0.5)

        # 保存引用
        self.new_title = new_title
        self.ineq_group = ineq_group

    # ================================================================
    # Scene 4: 推论 — 两边之差 < 第三边 (8-10s)
    # ================================================================
    def scene_4_diff_rule(self):
        # 更新标题
        diff_title = Text("两边之差 < 第三边", font=FONT, font_size=30, color=COLOR_SIDE_B, weight=BOLD).move_to(UP * 5.8)
        self.play(ReplacementTransform(self.new_title, diff_title), run_time=0.5)

        # 淡出三个不等式
        self.play(FadeOut(self.ineq_group), run_time=0.4)

        # 推导过程（简化展示）
        step1 = VGroup(
            Text("由", font=FONT, font_size=22, color=GRAY_A),
            Text("a + b > c", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(np.array([0, -2.0, 0]))

        arrow_derive = Text("⟹", font=FONT, font_size=24, color=COLOR_HIGHLIGHT).move_to(np.array([0, -2.9, 0]))

        step2 = VGroup(
            Text("c < a + b", font=FONT, font_size=22, color=WHITE),
            Text("且", font=FONT, font_size=20, color=GRAY_A),
            Text("c > |a − b|", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.25).move_to(np.array([0, -3.7, 0]))

        self.play(FadeIn(step1), run_time=0.5)
        self.wait(0.6)
        self.play(FadeIn(arrow_derive), run_time=0.3)
        self.play(FadeIn(step2), run_time=0.6)
        self.wait(0.8)

        # ── 核心综合公式 ──
        # |a - b| < c < a + b
        formula_box = RoundedRectangle(width=6.2, height=1.1, corner_radius=0.2,
                                       fill_color="#16213e", fill_opacity=0.9,
                                       stroke_color=COLOR_HIGHLIGHT, stroke_width=2.5
                                       ).move_to(np.array([0, -5.2, 0]))

        formula = VGroup(
            Text("|a − b|", font=FONT, font_size=26, color=COLOR_SIDE_A),
            Text("< c <", font=FONT, font_size=26, color=COLOR_HIGHLIGHT),
            Text("a + b", font=FONT, font_size=26, color=COLOR_SIDE_B),
        ).arrange(RIGHT, buff=0.2).move_to(np.array([0, -5.2, 0]))

        self.play(Create(formula_box), run_time=0.4)
        self.play(FadeIn(formula), run_time=0.6)
        self.wait(2.0)  # 核心公式停留

        # 清除推导步骤
        self.play(FadeOut(step1), FadeOut(arrow_derive), FadeOut(step2), run_time=0.4)

        # 保存
        self.diff_title = diff_title
        self.formula_box = formula_box
        self.formula = formula

    # ================================================================
    # Scene 5: 实例验证 (12-14s)
    # ================================================================
    def scene_5_examples(self):
        # 清除三角形和公式
        triangle_elements = [self.side_a, self.side_b, self.side_c,
                             self.lbl_A, self.lbl_B, self.lbl_C,
                             self.dot_A, self.dot_B, self.dot_C,
                             self.lbl_a, self.lbl_b, self.lbl_c,
                             self.formula_box, self.formula]
        self.play(*[FadeOut(e) for e in triangle_elements], run_time=0.5)

        # 更新标题
        ex_title = Text("判断：能否组成三角形？", font=FONT, font_size=30, color=WHITE, weight=BOLD).move_to(UP * 5.8)
        self.play(ReplacementTransform(self.diff_title, ex_title), run_time=0.4)

        # 判断规则提示
        rule_hint = Text("关键：最短两边之和 > 最长边", font=FONT, font_size=20, color=COLOR_HIGHLIGHT).move_to(np.array([0, 4.8, 0]))
        self.play(FadeIn(rule_hint), run_time=0.4)

        # ── 例题数据 ──
        examples = [
            {"sides": [3, 4, 5], "can": True,  "check": "3 + 4 = 7 > 5", "y": 3.2},
            {"sides": [1, 2, 4], "can": False, "check": "1 + 2 = 3 < 4", "y": 1.4},
            {"sides": [2, 3, 4], "can": True,  "check": "2 + 3 = 5 > 4", "y": -0.4},
        ]

        all_example_mobs = []

        for i, ex in enumerate(examples):
            y = ex["y"]
            s = sorted(ex["sides"])

            # 边长显示
            sides_text = Text(
                f"{ex['sides'][0]},  {ex['sides'][1]},  {ex['sides'][2]}",
                font=FONT, font_size=26, color=WHITE, weight=BOLD
            ).move_to(np.array([-2.8, y, 0]))

            # 验证过程
            check_text = Text(ex["check"], font=FONT, font_size=22, color=GRAY_A
                              ).move_to(np.array([0.3, y, 0]))

            # 结果标记
            if ex["can"]:
                result = Text("✓ 能", font=FONT, font_size=26, color=COLOR_OK, weight=BOLD)
            else:
                result = Text("✗ 不能", font=FONT, font_size=26, color=COLOR_FAIL, weight=BOLD)
            result.move_to(np.array([3.2, y, 0]))

            # 左侧序号
            num_label = Text(f"例{i+1}", font=FONT, font_size=22, color=GRAY_B).move_to(np.array([-4.0, y, 0]))

            # 逐步展示
            self.play(FadeIn(num_label), FadeIn(sides_text), run_time=0.4)
            self.wait(0.4)
            self.play(FadeIn(check_text), run_time=0.5)
            self.wait(0.3)
            self.play(FadeIn(result, scale=1.2), run_time=0.4)
            self.wait(0.8)

            all_example_mobs.extend([num_label, sides_text, check_text, result])

        self.wait(1.0)

        # 清除实例
        self.play(*[FadeOut(e) for e in all_example_mobs], FadeOut(rule_hint), run_time=0.5)

        # 保存标题引用
        self.ex_title = ex_title

    # ================================================================
    # Scene 6: 总结卡 (4-5s)
    # ================================================================
    def scene_6_summary(self):
        # 更新标题
        sum_title = Text("总结", font=FONT, font_size=32, color=COLOR_HIGHLIGHT, weight=BOLD).move_to(UP * 5.8)
        self.play(ReplacementTransform(self.ex_title, sum_title), run_time=0.4)

        # 核心公式卡片
        card_bg = RoundedRectangle(width=7.0, height=4.8, corner_radius=0.3,
                                   fill_color="#16213e", fill_opacity=0.95,
                                   stroke_color=COLOR_HIGHLIGHT, stroke_width=2.5
                                   ).move_to(np.array([0, 1.0, 0]))
        self.play(Create(card_bg), run_time=0.4)

        # 定理1
        t1_title = Text("① 两边之和 > 第三边", font=FONT, font_size=24, color=COLOR_HIGHLIGHT, weight=BOLD).move_to(np.array([0, 2.8, 0]))
        t1_body = VGroup(
            Text("a + b > c", font=FONT, font_size=22, color=WHITE),
            Text("b + c > a", font=FONT, font_size=22, color=WHITE),
            Text("a + c > b", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.5).move_to(np.array([0, 2.0, 0]))

        self.play(FadeIn(t1_title), run_time=0.3)
        self.play(FadeIn(t1_body), run_time=0.4)

        # 分隔线
        sep = Line([-3.2, 1.3, 0], [3.2, 1.3, 0], color=GRAY_B, stroke_width=1)
        self.play(Create(sep), run_time=0.2)

        # 定理2
        t2_title = Text("② 两边之差 < 第三边", font=FONT, font_size=24, color=COLOR_SIDE_B, weight=BOLD).move_to(np.array([0, 0.7, 0]))
        t2_body = VGroup(
            Text("|a − b|", font=FONT, font_size=22, color=COLOR_SIDE_A),
            Text("< c <", font=FONT, font_size=22, color=COLOR_HIGHLIGHT),
            Text("a + b", font=FONT, font_size=22, color=COLOR_SIDE_B),
        ).arrange(RIGHT, buff=0.2).move_to(np.array([0, -0.1, 0]))

        self.play(FadeIn(t2_title), run_time=0.3)
        self.play(FadeIn(t2_body), run_time=0.4)

        # 判断口诀
        sep2 = Line([-3.2, -0.65, 0], [3.2, -0.65, 0], color=GRAY_B, stroke_width=1)
        self.play(Create(sep2), run_time=0.2)

        trick = Text("💡 判断技巧：只需验证最短两边之和 > 最长边", font=FONT, font_size=20, color=YELLOW).move_to(np.array([0, -1.3, 0]))
        self.play(FadeIn(trick), run_time=0.5)
        self.wait(2.5)  # 总结停留

        # 保存
        self.sum_title = sum_title
        self.card_bg = card_bg
        self.summary_elements = [t1_title, t1_body, sep, t2_title, t2_body, sep2, trick]

    # ================================================================
    # Scene 7: 片尾 (3-4s)
    # ================================================================
    def scene_7_outro(self):
        # 清除总结卡
        self.play(FadeOut(self.card_bg), *[FadeOut(e) for e in self.summary_elements], run_time=0.5)

        # 放大作者信息
        author_big = Text("上海初高中数学直通车", font=FONT, font_size=38, color=WHITE, weight=BOLD).move_to(UP * 1.5)
        author_id  = Text("@emptyandcalm", font=FONT, font_size=28, color=GRAY_B).move_to(UP * 0.6)
        self.play(
            ReplacementTransform(self.author_tag, author_big),
            FadeOut(self.sum_title),
            run_time=0.6
        )
        self.play(FadeIn(author_id), run_time=0.4)

        # 关注提示
        follow = Text("关注我，获得更多数学技巧！", font=FONT, font_size=28, color=COLOR_HIGHLIGHT, weight=BOLD).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # 小三角形装饰（一圈）
        tri_positions = [UP*1.8, UP*1.8+RIGHT*1.5, DOWN*1.2+RIGHT*1.8,
                         DOWN*2.0, DOWN*1.2+LEFT*1.8, UP*1.8+LEFT*1.5]
        small_tris = VGroup()
        for pos in tri_positions:
            pts = [np.array([0, 0.2, 0]), np.array([-0.17, -0.1, 0]), np.array([0.17, -0.1, 0])]
            tri = Polygon(*pts, color=GOLD, fill_color=GOLD, fill_opacity=0.7, stroke_width=1.5)
            tri.move_to(pos + DOWN * 0.5)
            small_tris.add(tri)

        self.play(*[FadeIn(t, scale=0.3) for t in small_tris], run_time=0.5)
        self.wait(2.0)

        # 全部淡出
        self.play(FadeOut(author_big), FadeOut(author_id), FadeOut(follow), FadeOut(small_tris), run_time=0.8)


# ──────────────────────────────────────────────
# 渲染命令:
#   预览: manim -pql main.py TriangleSideRelation
#   高画质: manim -qh main.py TriangleSideRelation
# ──────────────────────────────────────────────