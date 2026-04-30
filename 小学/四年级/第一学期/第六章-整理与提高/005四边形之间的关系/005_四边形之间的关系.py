"""
四边形之间的关系 - Manim 教学动画
目标受众: 小学四年级学生
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ── 全局配置 ──────────────────────────────────────────────
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class QuadrilateralRelationLesson(Scene):
    """
    四边形之间的关系教学动画

    场景顺序:
    1. 开场钩子
    2. 认识各类四边形 (逐一展示)
    3. 集合图 -- 嵌套椭圆
    4. 特殊关系讲解
    5. 小结公式
    6. 片尾
    """

    # ── 颜色方案 ──────────────────────────────────────────
    C_BG        = "#1a1a2e"
    C_QUAD      = "#4a90d9"   # 四边形 -- 蓝
    C_PARA      = "#27ae60"   # 平行四边形 -- 绿
    C_TRAP      = "#e67e22"   # 梯形 -- 橙
    C_RECT      = "#9b59b6"   # 长方形 -- 紫
    C_SQ        = "#e74c3c"   # 正方形 -- 红
    C_LABEL     = "#f0f0f0"
    C_HIGHLIGHT = YELLOW
    C_DIM       = "#6b7280"

    def construct(self):
        self.camera.background_color = self.C_BG

        # 作者标识 -- 常驻顶部
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color=self.C_DIM,
        ).move_to(UP * 7.0)
        self.add(self.author)

        self.scene_1_hook()
        self.scene_2_shapes()
        self.scene_3_venn()
        self.scene_4_relations()
        self.scene_5_formula()
        self.scene_6_outro()

    # ═══════════════════════════════════════════════════════
    # Scene 1 -- 开场钩子
    # ═══════════════════════════════════════════════════════
    def scene_1_hook(self):
        question = Text(
            "正方形是长方形吗？",
            font="PingFang SC",
            font_size=44,
            color=self.C_HIGHLIGHT,
        ).move_to(UP * 5.2)

        sub = Text(
            "它们到底是什么关系？",
            font="PingFang SC",
            font_size=30,
            color=self.C_LABEL,
        ).move_to(UP * 4.2)

        # 一个小正方形 + 一个长方形并排做预告
        sq = Square(side_length=1.4, color=self.C_SQ, stroke_width=4).move_to(LEFT * 1.8 + UP * 2.2)
        rect = Rectangle(width=2.4, height=1.4, color=self.C_RECT, stroke_width=4).move_to(RIGHT * 1.6 + UP * 2.2)

        sq_lbl = Text("正方形", font="PingFang SC", font_size=22, color=self.C_SQ).next_to(sq, DOWN, buff=0.15)
        rect_lbl = Text("长方形", font="PingFang SC", font_size=22, color=self.C_RECT).next_to(rect, DOWN, buff=0.15)

        hint = Text(
            "今天一次搞清楚！",
            font="PingFang SC",
            font_size=32,
            color=self.C_LABEL,
        ).move_to(UP * 0.6)

        self.play(Write(question), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.6)
        self.play(
            Create(sq), Create(rect),
            FadeIn(sq_lbl), FadeIn(rect_lbl),
            run_time=1.0,
        )
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(question), FadeOut(sub),
            FadeOut(sq), FadeOut(rect),
            FadeOut(sq_lbl), FadeOut(rect_lbl),
            FadeOut(hint),
            run_time=0.5,
        )

    # ═══════════════════════════════════════════════════════
    # Scene 2 -- 逐一认识各类四边形
    # ═══════════════════════════════════════════════════════
    def scene_2_shapes(self):
        title = Text(
            "先认识四种四边形",
            font="PingFang SC",
            font_size=38,
            color=self.C_HIGHLIGHT,
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.7)

        # 每张卡片的数据: (形状, 名称, 特点, 颜色, 位置)
        shapes_info = [
            ("quad",   "四边形",    "四条边、四个角",           self.C_QUAD),
            ("trap",   "梯形",      "只有一组对边平行",         self.C_TRAP),
            ("para",   "平行四边形","两组对边分别平行",         self.C_PARA),
            ("rect",   "长方形",    "平行四边形 + 四个直角",    self.C_RECT),
            ("sq",     "正方形",    "长方形 + 四条边相等",      self.C_SQ),
        ]

        cards = VGroup()

        for i, (kind, name, prop, color) in enumerate(shapes_info):
            shape = self._make_shape(kind, color, scale=0.9)
            name_t = Text(name, font="PingFang SC", font_size=26, color=color)
            prop_t = Text(prop, font="PingFang SC", font_size=20, color=self.C_LABEL)
            card = VGroup(shape, name_t, prop_t).arrange(RIGHT, buff=0.25)
            cards.add(card)

        cards.arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        cards.move_to(ORIGIN + DOWN * 0.8)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.55)
            self.wait(0.35)

        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(cards), run_time=0.6)

    # ═══════════════════════════════════════════════════════
    # Scene 3 -- 集合图（嵌套椭圆）
    # ═══════════════════════════════════════════════════════
    def scene_3_venn(self):
        title = Text(
            "用集合图表示它们的关系",
            font="PingFang SC",
            font_size=34,
            color=self.C_HIGHLIGHT,
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        # 集合图的中心偏上
        center = UP * 1.2

        # ── 四边形（最大椭圆）
        e_quad = Ellipse(width=8.0, height=6.2, color=self.C_QUAD, stroke_width=3)
        e_quad.move_to(center)
        lbl_quad = Text("四边形", font="PingFang SC", font_size=24, color=self.C_QUAD)
        lbl_quad.move_to(center + UP * 2.8 + LEFT * 3.0)

        # ── 梯形（左侧椭圆，和平行四边形并列在四边形内）
        trap_center = center + LEFT * 2.3
        e_trap = Ellipse(width=3.2, height=3.8, color=self.C_TRAP, stroke_width=3)
        e_trap.move_to(trap_center)
        lbl_trap = Text("梯形", font="PingFang SC", font_size=22, color=self.C_TRAP)
        lbl_trap.move_to(trap_center + UP * 1.4)

        # 梯形例子
        trap_ex = self._make_shape("trap", self.C_TRAP, scale=0.5)
        trap_ex.move_to(trap_center)

        # ── 平行四边形（右侧椭圆）
        para_center = center + RIGHT * 1.7
        e_para = Ellipse(width=3.8, height=4.8, color=self.C_PARA, stroke_width=3)
        e_para.move_to(para_center)
        lbl_para = Text("平行四边形", font="PingFang SC", font_size=20, color=self.C_PARA)
        lbl_para.move_to(para_center + UP * 1.9)

        # 平行四边形例子（在平行四边形椭圆但在长方形外的区域）
        para_ex = self._make_shape("para", self.C_PARA, scale=0.5)
        para_ex.move_to(para_center + UP * 0.6)

        # ── 长方形（在平行四边形内的椭圆）
        rect_center = para_center + DOWN * 0.6
        e_rect = Ellipse(width=2.5, height=2.8, color=self.C_RECT, stroke_width=3)
        e_rect.move_to(rect_center)
        lbl_rect = Text("长方形", font="PingFang SC", font_size=18, color=self.C_RECT)
        lbl_rect.move_to(rect_center + UP * 1.0)

        # 长方形例子（在长方形椭圆但在正方形外的区域）
        rect_ex = self._make_shape("rect", self.C_RECT, scale=0.4)
        rect_ex.move_to(rect_center + UP * 0.15)

        # ── 正方形（最里层小椭圆）
        sq_center = rect_center + DOWN * 0.45
        e_sq = Ellipse(width=1.3, height=1.2, color=self.C_SQ, stroke_width=3)
        e_sq.move_to(sq_center)
        lbl_sq = Text("正方形", font="PingFang SC", font_size=16, color=self.C_SQ)
        lbl_sq.move_to(sq_center)

        # ── 逐层动画
        self.play(Create(e_quad), FadeIn(lbl_quad), run_time=0.9)
        self.wait(0.3)

        self.play(Create(e_trap), FadeIn(lbl_trap), run_time=0.8)
        self.play(FadeIn(trap_ex), run_time=0.4)
        self.wait(0.3)

        self.play(Create(e_para), FadeIn(lbl_para), run_time=0.8)
        self.play(FadeIn(para_ex), run_time=0.4)
        self.wait(0.3)

        self.play(Create(e_rect), FadeIn(lbl_rect), run_time=0.7)
        self.play(FadeIn(rect_ex), run_time=0.4)
        self.wait(0.3)

        self.play(Create(e_sq), FadeIn(lbl_sq), run_time=0.6)
        self.wait(1.5)

        self.venn_group = VGroup(
            e_quad, lbl_quad,
            e_trap, lbl_trap, trap_ex,
            e_para, lbl_para, para_ex,
            e_rect, lbl_rect, rect_ex,
            e_sq,   lbl_sq,
        )
        self.play(FadeOut(title), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(self.venn_group), run_time=0.7)

    # ═══════════════════════════════════════════════════════
    # Scene 4 -- 特殊关系逐步讲解
    # ═══════════════════════════════════════════════════════
    def scene_4_relations(self):
        """逐一解说包含关系"""

        def make_title(text, color=self.C_HIGHLIGHT):
            return Text(text, font="PingFang SC", font_size=34, color=color).move_to(UP * 6.0)

        # ── 4a. 长方形是特殊的平行四边形 ──────────────────
        t4a = make_title("长方形 ⊆ 平行四边形")
        explain_a1 = Text(
            "平行四边形: 两组对边平行",
            font="PingFang SC", font_size=24, color=self.C_PARA,
        ).move_to(UP * 5.0)
        explain_a2 = Text(
            "长方形: 还多了四个直角",
            font="PingFang SC", font_size=24, color=self.C_RECT,
        ).move_to(UP * 4.2)

        para_big = self._make_shape("para", self.C_PARA, scale=1.6).move_to(LEFT * 1.5 + UP * 1.5)
        rect_small = self._make_shape("rect", self.C_RECT, scale=1.2).move_to(LEFT * 1.5 + UP * 1.5)

        # 直角标记
        ra_marks = self._make_rect_right_angles(rect_small, size=0.22)

        arrow_a = Arrow(
            para_big.get_right() + LEFT * 0.1,
            para_big.get_right() + RIGHT * 1.2,
            color=self.C_HIGHLIGHT,
            buff=0,
        )
        note_a = Text(
            "长方形是\n特殊的平行四边形",
            font="PingFang SC", font_size=22, color=self.C_LABEL,
        ).next_to(arrow_a, RIGHT, buff=0.1)

        self.play(Write(t4a), run_time=0.7)
        self.play(FadeIn(explain_a1), run_time=0.5)
        self.play(Create(para_big), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(explain_a2), run_time=0.5)
        self.play(Create(rect_small), run_time=0.7)
        self.play(FadeIn(ra_marks), run_time=0.4)
        self.wait(0.4)
        self.play(GrowArrow(arrow_a), FadeIn(note_a), run_time=0.7)
        self.wait(1.5)
        self.play(
            FadeOut(t4a), FadeOut(explain_a1), FadeOut(explain_a2),
            FadeOut(para_big), FadeOut(rect_small), FadeOut(ra_marks),
            FadeOut(arrow_a), FadeOut(note_a),
            run_time=0.5,
        )

        # ── 4b. 正方形是特殊的长方形 ──────────────────────
        t4b = make_title("正方形 ⊆ 长方形")
        explain_b1 = Text(
            "长方形: 四个直角",
            font="PingFang SC", font_size=24, color=self.C_RECT,
        ).move_to(UP * 5.0)
        explain_b2 = Text(
            "正方形: 还多了四条边相等",
            font="PingFang SC", font_size=24, color=self.C_SQ,
        ).move_to(UP * 4.2)

        rect_big = self._make_shape("rect", self.C_RECT, scale=1.6).move_to(LEFT * 1.5 + UP * 1.5)
        sq_inner = self._make_shape("sq", self.C_SQ, scale=1.2).move_to(LEFT * 1.5 + UP * 1.5)
        sq_ra = self._make_rect_right_angles(sq_inner, size=0.22)

        # 等边标记
        equal_marks = self._make_equal_marks(sq_inner)

        arrow_b = Arrow(
            rect_big.get_right() + LEFT * 0.1,
            rect_big.get_right() + RIGHT * 1.2,
            color=self.C_HIGHLIGHT,
            buff=0,
        )
        note_b = Text(
            "正方形是\n特殊的长方形",
            font="PingFang SC", font_size=22, color=self.C_LABEL,
        ).next_to(arrow_b, RIGHT, buff=0.1)

        self.play(Write(t4b), run_time=0.7)
        self.play(FadeIn(explain_b1), run_time=0.5)
        self.play(Create(rect_big), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(explain_b2), run_time=0.5)
        self.play(Create(sq_inner), run_time=0.6)
        self.play(FadeIn(sq_ra), FadeIn(equal_marks), run_time=0.4)
        self.wait(0.4)
        self.play(GrowArrow(arrow_b), FadeIn(note_b), run_time=0.7)
        self.wait(1.5)
        self.play(
            FadeOut(t4b), FadeOut(explain_b1), FadeOut(explain_b2),
            FadeOut(rect_big), FadeOut(sq_inner), FadeOut(sq_ra), FadeOut(equal_marks),
            FadeOut(arrow_b), FadeOut(note_b),
            run_time=0.5,
        )

        # ── 4c. 梯形与平行四边形是并列关系 ───────────────
        t4c = make_title("梯形 和 平行四边形 并列")
        explain_c = Text(
            "都是四边形，但互不包含",
            font="PingFang SC", font_size=26, color=self.C_LABEL,
        ).move_to(UP * 4.8)

        trap_shape = self._make_shape("trap", self.C_TRAP, scale=1.4).move_to(LEFT * 2.0 + UP * 1.5)
        para_shape = self._make_shape("para", self.C_PARA, scale=1.4).move_to(RIGHT * 2.0 + UP * 1.5)

        trap_lbl = Text("梯形", font="PingFang SC", font_size=24, color=self.C_TRAP).next_to(trap_shape, DOWN, buff=0.2)
        para_lbl = Text("平行四边形", font="PingFang SC", font_size=22, color=self.C_PARA).next_to(para_shape, DOWN, buff=0.2)

        cross = Text("✗", font="PingFang SC", font_size=40, color=RED).move_to(ORIGIN + UP * 1.5)
        note_c = Text(
            "梯形只有一组对边平行\n平行四边形有两组对边平行",
            font="PingFang SC", font_size=20, color=self.C_LABEL,
        ).move_to(DOWN * 0.8)

        self.play(Write(t4c), run_time=0.7)
        self.play(FadeIn(explain_c), run_time=0.5)
        self.play(
            Create(trap_shape), Create(para_shape),
            FadeIn(trap_lbl), FadeIn(para_lbl),
            run_time=0.8,
        )
        self.play(FadeIn(cross, scale=1.3), run_time=0.5)
        self.play(FadeIn(note_c), run_time=0.5)
        self.wait(1.5)
        self.play(
            FadeOut(t4c), FadeOut(explain_c),
            FadeOut(trap_shape), FadeOut(para_shape),
            FadeOut(trap_lbl), FadeOut(para_lbl),
            FadeOut(cross), FadeOut(note_c),
            run_time=0.5,
        )

    # ═══════════════════════════════════════════════════════
    # Scene 5 -- 小结：包含关系公式
    # ═══════════════════════════════════════════════════════
    def scene_5_formula(self):
        title = Text(
            "包含关系总结",
            font="PingFang SC",
            font_size=38,
            color=self.C_HIGHLIGHT,
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        # 主链: 正方形 ⊂ 长方形 ⊂ 平行四边形 ⊂ 四边形
        chain_parts = [
            Text("正方形", font="PingFang SC", font_size=30, color=self.C_SQ),
            Text("⊂", font="PingFang SC", font_size=28, color=WHITE),
            Text("长方形", font="PingFang SC", font_size=30, color=self.C_RECT),
            Text("⊂", font="PingFang SC", font_size=28, color=WHITE),
            Text("平行四边形", font="PingFang SC", font_size=28, color=self.C_PARA),
            Text("⊂", font="PingFang SC", font_size=28, color=WHITE),
            Text("四边形", font="PingFang SC", font_size=30, color=self.C_QUAD),
        ]
        chain = VGroup(*chain_parts).arrange(RIGHT, buff=0.18)
        chain.move_to(UP * 4.8)

        # 梯形支链
        trap_parts = [
            Text("梯形", font="PingFang SC", font_size=30, color=self.C_TRAP),
            Text("⊂", font="PingFang SC", font_size=28, color=WHITE),
            Text("四边形", font="PingFang SC", font_size=30, color=self.C_QUAD),
        ]
        trap_chain = VGroup(*trap_parts).arrange(RIGHT, buff=0.18)
        trap_chain.move_to(UP * 3.8)

        self.play(
            LaggedStart(*[FadeIn(p, shift=UP * 0.2) for p in chain_parts], lag_ratio=0.2),
            run_time=1.8,
        )
        self.wait(0.5)
        self.play(
            LaggedStart(*[FadeIn(p, shift=UP * 0.2) for p in trap_parts], lag_ratio=0.25),
            run_time=1.0,
        )
        self.wait(0.5)

        # 集合图小版（复现，更紧凑）
        center = DOWN * 0.2
        eq1  = Ellipse(width=7.2, height=4.2, color=self.C_QUAD,  stroke_width=2.5).move_to(center)
        eq2l = Ellipse(width=2.6, height=3.0, color=self.C_TRAP,  stroke_width=2.5).move_to(center + LEFT * 2.1)
        eq2r = Ellipse(width=3.2, height=3.6, color=self.C_PARA,  stroke_width=2.5).move_to(center + RIGHT * 1.2)
        eq3  = Ellipse(width=2.0, height=2.4, color=self.C_RECT,  stroke_width=2.5).move_to(center + RIGHT * 1.2 + DOWN * 0.35)
        eq4  = Ellipse(width=1.1, height=1.0, color=self.C_SQ,    stroke_width=2.5).move_to(center + RIGHT * 1.2 + DOWN * 0.70)

        lq1  = Text("四边形", font="PingFang SC", font_size=20, color=self.C_QUAD).move_to(center + UP * 1.75 + LEFT * 2.8)
        lq2l = Text("梯形",   font="PingFang SC", font_size=18, color=self.C_TRAP).move_to(center + LEFT * 2.1 + UP * 1.1)
        lq2r = Text("平行\n四边形", font="PingFang SC", font_size=16, color=self.C_PARA).move_to(center + RIGHT * 1.2 + UP * 1.5)
        lq3  = Text("长方形", font="PingFang SC", font_size=15, color=self.C_RECT).move_to(center + RIGHT * 1.2 + UP * 0.7)
        lq4  = Text("正方形", font="PingFang SC", font_size=13, color=self.C_SQ).move_to(center + RIGHT * 1.2 + DOWN * 0.70)

        self.play(
            Create(eq1), FadeIn(lq1),
            run_time=0.7,
        )
        self.play(Create(eq2l), FadeIn(lq2l), Create(eq2r), FadeIn(lq2r), run_time=0.8)
        self.play(Create(eq3), FadeIn(lq3), run_time=0.6)
        self.play(Create(eq4), FadeIn(lq4), run_time=0.5)
        self.wait(2.0)

        # 关键点提示
        key1 = Text(
            "越靠里，条件越多，越特殊",
            font="PingFang SC", font_size=24, color=self.C_HIGHLIGHT,
        ).move_to(DOWN * 3.0)
        key2 = Text(
            "越靠外，条件越少，越一般",
            font="PingFang SC", font_size=24, color=self.C_LABEL,
        ).move_to(DOWN * 3.7)

        self.play(FadeIn(key1, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(key2, shift=UP * 0.2), run_time=0.6)
        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(chain), FadeOut(trap_chain),
            FadeOut(eq1), FadeOut(eq2l), FadeOut(eq2r), FadeOut(eq3), FadeOut(eq4),
            FadeOut(lq1), FadeOut(lq2l), FadeOut(lq2r), FadeOut(lq3), FadeOut(lq4),
            FadeOut(key1), FadeOut(key2),
            run_time=0.6,
        )

    # ═══════════════════════════════════════════════════════
    # Scene 6 -- 片尾
    # ═══════════════════════════════════════════════════════
    def scene_6_outro(self):
        summary_lines = [
            ("正方形 ⊂ 长方形", self.C_SQ),
            ("长方形 ⊂ 平行四边形", self.C_RECT),
            ("平行四边形 ⊂ 四边形", self.C_PARA),
            ("梯形 ⊂ 四边形", self.C_TRAP),
        ]
        summary_group = VGroup()
        for txt, col in summary_lines:
            t = Text(txt, font="PingFang SC", font_size=28, color=col)
            summary_group.add(t)
        summary_group.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary_group.move_to(UP * 2.5)

        self.play(
            LaggedStart(*[FadeIn(t, shift=RIGHT * 0.3) for t in summary_group], lag_ratio=0.3),
            run_time=1.5,
        )
        self.wait(1.0)

        # 作者大字
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
        ).move_to(DOWN * 1.0)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=26,
            color=self.C_DIM,
        ).move_to(DOWN * 1.8)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=self.C_HIGHLIGHT,
        ).move_to(DOWN * 3.0)

        self.play(FadeIn(author_big, shift=UP * 0.3), run_time=0.7)
        self.play(FadeIn(author_id), run_time=0.5)
        self.play(FadeIn(follow, scale=1.05), run_time=0.6)
        self.wait(2.5)

        self.play(
            FadeOut(summary_group),
            FadeOut(author_big),
            FadeOut(author_id),
            FadeOut(follow),
            run_time=0.8,
        )

    # ═══════════════════════════════════════════════════════
    # 工具方法
    # ═══════════════════════════════════════════════════════
    def _make_shape(self, kind: str, color: str, scale: float = 1.0) -> VMobject:
        """生成示意图形"""
        if kind == "quad":
            # 一般四边形（不规则）
            pts = np.array([
                [-1.0, -0.7, 0],
                [ 0.9, -0.7, 0],
                [ 1.2,  0.6, 0],
                [-0.7,  0.7, 0],
            ])
            shape = Polygon(*pts, color=color, stroke_width=3, fill_opacity=0.15, fill_color=color)
        elif kind == "trap":
            pts = np.array([
                [-1.0, -0.55, 0],
                [ 1.0, -0.55, 0],
                [ 0.55,  0.55, 0],
                [-0.55,  0.55, 0],
            ])
            shape = Polygon(*pts, color=color, stroke_width=3, fill_opacity=0.15, fill_color=color)
        elif kind == "para":
            pts = np.array([
                [-1.1, -0.55, 0],
                [ 0.9, -0.55, 0],
                [ 1.1,  0.55, 0],
                [-0.9,  0.55, 0],
            ])
            shape = Polygon(*pts, color=color, stroke_width=3, fill_opacity=0.15, fill_color=color)
        elif kind == "rect":
            shape = Rectangle(
                width=2.0, height=1.1,
                color=color, stroke_width=3,
                fill_opacity=0.15, fill_color=color,
            )
        elif kind == "sq":
            shape = Square(
                side_length=1.2,
                color=color, stroke_width=3,
                fill_opacity=0.15, fill_color=color,
            )
        else:
            shape = Square(side_length=1.0, color=color, stroke_width=3)

        shape.scale(scale)
        return shape

    def _make_rect_right_angles(self, rect_mob: VMobject, size: float = 0.2) -> VGroup:
        """在矩形四个角放直角标记（适配 Rectangle/Square）"""
        verts = rect_mob.get_vertices()
        # get_vertices() 返回 4 个角点（逆时针）
        group = VGroup()
        n = len(verts)
        for i in range(n):
            corner = verts[i]
            p_prev = verts[(i - 1) % n]
            p_next = verts[(i + 1) % n]
            v1 = (p_prev - corner)
            v2 = (p_next - corner)
            norm1 = np.linalg.norm(v1)
            norm2 = np.linalg.norm(v2)
            if norm1 < 1e-9 or norm2 < 1e-9:
                continue
            v1u = v1 / norm1 * size
            v2u = v2 / norm2 * size
            mark = Polygon(
                corner,
                corner + v1u,
                corner + v1u + v2u,
                corner + v2u,
                color=self.C_HIGHLIGHT,
                stroke_width=2,
                fill_opacity=0,
            )
            group.add(mark)
        return group

    def _make_equal_marks(self, sq_mob: VMobject) -> VGroup:
        """在正方形四条边中点放等号刻度线"""
        verts = sq_mob.get_vertices()
        group = VGroup()
        n = len(verts)
        for i in range(n):
            p1 = verts[i]
            p2 = verts[(i + 1) % n]
            mid = (p1 + p2) / 2
            direction = p2 - p1
            direction_norm = np.linalg.norm(direction)
            if direction_norm < 1e-9:
                continue
            perp = np.array([-direction[1], direction[0], 0]) / direction_norm
            tick_len = 0.12
            tick = Line(
                mid - perp * tick_len,
                mid + perp * tick_len,
                color=self.C_HIGHLIGHT,
                stroke_width=2.5,
            )
            group.add(tick)
        return group
