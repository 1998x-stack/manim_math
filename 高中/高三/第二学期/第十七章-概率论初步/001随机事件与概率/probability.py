"""
随机事件与概率 - Manim 教学动画
年级: 高三第二学期   章节: 概率论初步

知识点：随机试验 / 随机事件 / 必然 & 不可能事件 /
         概率三公理 / 韦恩图 / 加法公式 / 互补公式

输出格式: TikTok 竖屏 (1080 × 1920)
作者: 上海初高中数学直通车  @emptyandcalm

渲染:
    manim -pql probability.py ProbabilityScene    # 快速预览
    manim -qh  probability.py ProbabilityScene    # 高质量
"""

from manim import *
import numpy as np

# ──────────────────────────────────────────────────────────
# 全局配置
# ──────────────────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ──────────────────────────────────────────────────────────
# 颜色方案
# ──────────────────────────────────────────────────────────
BG        = "#1a1a2e"
C_CERTAIN = "#2ecc71"    # 绿  — 必然事件
C_IMPOS   = "#e74c3c"    # 红  — 不可能事件
C_RAND    = "#3498db"    # 蓝  — 随机事件
C_A       = "#e67e22"    # 橙  — 事件 A
C_B       = "#9b59b6"    # 紫  — 事件 B
C_AB      = "#f1c40f"    # 黄  — 交集 A∩B
C_UNION   = "#1abc9c"    # 青  — 并集 A∪B
C_SS      = "#ecf0f1"    # 浅灰 — 样本空间框
C_HL      = YELLOW
C_AX      = "#7f8c8d"
C_CARD    = "#16213e"
FONT      = "Noto Sans CJK SC"


# ══════════════════════════════════════════════════════════
class ProbabilityScene(Scene):

    # ──────────────────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG
        self.setup_geometry()

        self.scene_opening()
        self.scene_random_trial()
        self.scene_prob_axis()
        self.scene_venn()
        self.scene_addition()
        self.scene_complement()
        self.scene_summary()
        self.scene_outro()

    # ──────────────────────────────────────────────────────
    # 统一几何数据初始化
    # ──────────────────────────────────────────────────────
    def setup_geometry(self):
        # 韦恩图
        self.V_R      = 1.3        # 圆半径
        self.V_OA     = np.array([-0.85, 0.0, 0.0])   # A 圆心
        self.V_OB     = np.array([ 0.85, 0.0, 0.0])   # B 圆心
        self.V_CENTER = np.array([ 0.0,  1.9, 0.0])   # 韦恩图整体中心

        # 圆心距
        dist = np.linalg.norm(self.V_OB[:2] - self.V_OA[:2])
        assert dist < 2 * self.V_R, "两圆不重叠！"
        assert dist > 0,            "两圆完全重合！"

        # 概率轴
        self.AXIS_Y    = 1.6        # 数轴 y 坐标
        self.AXIS_X0   = -3.2       # 左端
        self.AXIS_X1   =  3.2       # 右端

        # 概率轴三个关键 x 位置（线性映射 0→左端, 1→右端）
        self.p2x = lambda p: self.AXIS_X0 + p * (self.AXIS_X1 - self.AXIS_X0)

        print("✓ setup_geometry 完成")

    # ──────────────────────────────────────────────────────
    # 工具: 带圆角的文字卡片
    # ──────────────────────────────────────────────────────
    def make_card(self, lines, color, pos, width=7.6, lh=0.9):
        """
        lines: list of (text_or_MathTex_str, is_math, font_size)
        返回 VGroup
        """
        height = max(1.5, len(lines) * lh + 0.4)
        bg = RoundedRectangle(
            width=width, height=height, corner_radius=0.18,
            fill_color=C_CARD, fill_opacity=1,
            stroke_color=color, stroke_width=2.5
        ).move_to(pos)
        items = [bg]
        total_h = (len(lines) - 1) * lh
        for i, (txt, is_math, fs) in enumerate(lines):
            y_off = total_h / 2 - i * lh
            if is_math:
                obj = MathTex(txt, font_size=fs, color=WHITE)
            else:
                obj = Text(txt, font=FONT, font_size=fs, color=WHITE)
            obj.move_to(bg.get_center() + UP * y_off)
            items.append(obj)
        return VGroup(*items)

    # ──────────────────────────────────────────────────────
    # 工具: 韦恩图（两圆 + 样本空间框）
    # ──────────────────────────────────────────────────────
    def make_venn(self, center=None, r=None, fill=True):
        if center is None:
            center = self.V_CENTER
        if r is None:
            r = self.V_R
        OA = center + self.V_OA
        OB = center + self.V_OB

        ss = RoundedRectangle(
            width=6.0, height=3.5, corner_radius=0.2,
            stroke_color=C_SS, stroke_width=2.0,
            fill_opacity=0
        ).move_to(center)

        circ_A = Circle(radius=r, stroke_color=C_A, stroke_width=2.5,
                        fill_color=C_A, fill_opacity=0.25 if fill else 0
                        ).move_to(OA)
        circ_B = Circle(radius=r, stroke_color=C_B, stroke_width=2.5,
                        fill_color=C_B, fill_opacity=0.25 if fill else 0
                        ).move_to(OB)

        lbl_A = MathTex("A", font_size=34, color=C_A).move_to(OA + LEFT * 0.55 + UP * 0.3)
        lbl_B = MathTex("B", font_size=34, color=C_B).move_to(OB + RIGHT * 0.55 + UP * 0.3)
        lbl_S = MathTex("S", font_size=26, color=C_SS).move_to(
            center + np.array([2.6, 1.3, 0])
        )

        return VGroup(ss, circ_A, circ_B, lbl_A, lbl_B, lbl_S), OA, OB

    # ══════════════════════════════════════════════════════
    # Scene 1  开场
    # ══════════════════════════════════════════════════════
    def scene_opening(self):
        self.author_banner = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=20, color=GRAY_B
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_banner, shift=DOWN * 0.2), run_time=0.4)

        # 抛硬币图示（简洁符号）
        coin = Circle(radius=0.7, color=C_HL, stroke_width=4,
                      fill_color=C_CARD, fill_opacity=1).move_to(UP * 4.5)
        coin_q = Text("?", font=FONT, font_size=54, color=C_HL).move_to(coin.get_center())
        self.play(GrowFromCenter(coin), run_time=0.5)
        self.play(Write(coin_q), run_time=0.4)
        self.play(Rotate(coin, angle=PI, axis=RIGHT, run_time=0.5))

        # 标题
        title = Text("随机事件与概率", font=FONT, font_size=48, color=GOLD).move_to(UP * 3.2)
        subtitle = Text("不确定的世界，用数字来度量", font=FONT, font_size=26, color=GRAY_A
                        ).move_to(UP * 2.3)
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)

        # 四个关键词飘入
        kws = ["随机事件", "必然事件", "不可能事件", "概率"]
        cols = [C_RAND, C_CERTAIN, C_IMPOS, C_HL]
        kw_objs = []
        for i, (kw, col) in enumerate(zip(kws, cols)):
            obj = Text(kw, font=FONT, font_size=28, color=col).move_to(
                UP * (0.9 - i * 0.85)
            )
            obj.shift(RIGHT * 10)
            self.add(obj)
            self.play(obj.animate.shift(LEFT * 10), run_time=0.3)
            kw_objs.append(obj)

        self.wait(0.7)

        title_sm = Text("随机事件与概率", font=FONT, font_size=34, color=GOLD).move_to(UP * 6.3)
        self.play(
            Transform(title, title_sm),
            FadeOut(subtitle), FadeOut(coin), FadeOut(coin_q),
            *[FadeOut(o) for o in kw_objs],
            run_time=0.5,
        )
        self.title_obj = title

    # ══════════════════════════════════════════════════════
    # Scene 2  随机试验 & 三类事件
    # ══════════════════════════════════════════════════════
    def scene_random_trial(self):
        sec = Text("什么是随机事件？", font=FONT, font_size=36, color=C_RAND).move_to(UP * 5.5)
        self.play(Write(sec), run_time=0.5)

        # 三个情景框
        scenarios = [
            ("抛硬币", "正面 or 反面\n事先不确定", C_RAND, "随机事件"),
            ("太阳东升", "明天太阳\n一定从东方升起", C_CERTAIN, "必然事件"),
            ("抛硬币=2", "一枚硬币\n出现数字2面", C_IMPOS, "不可能事件"),
        ]

        boxes = []
        x_positions = [-2.6, 0.0, 2.6]
        center_y = 3.2

        for i, (title_t, body_t, col, tag) in enumerate(scenarios):
            xp = x_positions[i]
            bg = RoundedRectangle(
                width=2.4, height=3.0, corner_radius=0.2,
                fill_color=C_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2.5
            ).move_to(np.array([xp, center_y, 0]))

            t_title = Text(title_t, font=FONT, font_size=22, color=col).move_to(
                bg.get_top() + DOWN * 0.35
            )
            t_body = Text(body_t, font=FONT, font_size=17, color=WHITE,
                          line_spacing=1.2).move_to(bg.get_center())
            t_tag = Text(tag, font=FONT, font_size=18, color=col).move_to(
                bg.get_bottom() + UP * 0.35
            )
            box = VGroup(bg, t_title, t_body, t_tag)
            box.shift(DOWN * 10)
            boxes.append(box)

        for box in boxes:
            self.add(box)
            self.play(box.animate.shift(UP * 10), run_time=0.45)

        # 特征说明
        features = [
            ("① 可重复进行", C_RAND),
            ("② 结果已知但不确定", C_RAND),
            ("③ 可用数字描述可能性", C_HL),
        ]
        feat_y = -1.2
        feat_objs = []
        for txt, col in features:
            fo = Text(f"• {txt}", font=FONT, font_size=24, color=col).move_to(
                UP * feat_y
            )
            feat_y -= 0.85
            self.play(FadeIn(fo, shift=RIGHT * 0.3), run_time=0.4)
            feat_objs.append(fo)

        self.wait(1.2)

        self.play(
            *[FadeOut(b) for b in boxes],
            *[FadeOut(f) for f in feat_objs],
            FadeOut(sec),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════
    # Scene 3  概率数轴 & 三公理
    # ══════════════════════════════════════════════════════
    def scene_prob_axis(self):
        sec = Text("概率的大小：0 到 1 之间", font=FONT, font_size=34, color=C_HL
                   ).move_to(UP * 5.5)
        self.play(Write(sec), run_time=0.6)

        # ── 数轴 ──
        axis_y = self.AXIS_Y
        x0, x1 = self.AXIS_X0, self.AXIS_X1

        axis_line = Line(
            np.array([x0, axis_y, 0]),
            np.array([x1, axis_y, 0]),
            color=C_AX, stroke_width=3
        )
        arrow_r = Arrow(
            np.array([x1 - 0.05, axis_y, 0]),
            np.array([x1 + 0.3, axis_y, 0]),
            buff=0, color=C_AX, max_tip_length_to_length_ratio=0.8, stroke_width=3
        )

        self.play(Create(axis_line), FadeIn(arrow_r), run_time=0.7)

        # 刻度和标签
        ticks_data = [(0.0, "0", C_IMPOS), (0.5, "0.5", C_RAND), (1.0, "1", C_CERTAIN)]
        tick_objs = []
        for p, lbl, col in ticks_data:
            xp = self.p2x(p)
            tick = Line(
                np.array([xp, axis_y - 0.15, 0]),
                np.array([xp, axis_y + 0.15, 0]),
                color=col, stroke_width=3
            )
            dot = Dot(np.array([xp, axis_y, 0]), radius=0.1, color=col)
            label = Text(lbl, font=FONT, font_size=22, color=col).move_to(
                np.array([xp, axis_y - 0.45, 0])
            )
            tick_objs.extend([tick, dot, label])
            self.play(FadeIn(tick), FadeIn(dot), Write(label), run_time=0.35)

        # 三段标注
        seg_labels = [
            (0.0, C_IMPOS, "不可能", DOWN * 0.85),
            (0.5, C_RAND,  "随机",   DOWN * 0.85),
            (1.0, C_CERTAIN,"必然",  DOWN * 0.85),
        ]
        seg_objs = []
        for p, col, txt, off in seg_labels:
            xp = self.p2x(p)
            t = Text(txt, font=FONT, font_size=20, color=col).move_to(
                np.array([xp, axis_y, 0]) + off
            )
            self.play(FadeIn(t, shift=UP * 0.2), run_time=0.3)
            seg_objs.append(t)

        # 范围大括号
        range_brace = BraceBetweenPoints(
            np.array([x0, axis_y + 0.3, 0]),
            np.array([x1, axis_y + 0.3, 0]),
            direction=UP, color=C_HL
        )
        range_lbl = MathTex(r"0 \leq P(A) \leq 1", font_size=30, color=C_HL).next_to(
            range_brace, UP, buff=0.15
        )
        self.play(GrowFromCenter(range_brace), Write(range_lbl), run_time=0.7)
        self.wait(0.5)

        # 三公理卡片
        axioms = [
            (r"P(A) \geq 0", "非负性", C_RAND),
            (r"P(S) = 1",    "规范性", C_CERTAIN),
            (r"A \cap B = \varnothing \Rightarrow P(A\cup B)=P(A)+P(B)", "可加性", C_HL),
        ]
        axiom_y = -1.5
        axiom_objs = []
        for tex, name, col in axioms:
            bg = RoundedRectangle(
                width=7.8, height=1.0, corner_radius=0.15,
                fill_color=C_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=1.8
            ).move_to(UP * axiom_y)
            title_t = Text(name, font=FONT, font_size=22, color=col).move_to(
                bg.get_center() + LEFT * 2.8
            )
            formula_t = MathTex(tex, font_size=24, color=WHITE).move_to(
                bg.get_center() + RIGHT * 0.5
            )
            card = VGroup(bg, title_t, formula_t)
            card.shift(RIGHT * 11)
            axiom_objs.append(card)
            self.add(card)
            self.play(card.animate.shift(LEFT * 11), run_time=0.4)
            axiom_y += 1.05

        self.wait(1.3)

        self.play(
            FadeOut(sec),
            FadeOut(axis_line), FadeOut(arrow_r),
            *[FadeOut(o) for o in tick_objs],
            *[FadeOut(o) for o in seg_objs],
            FadeOut(range_brace), FadeOut(range_lbl),
            *[FadeOut(o) for o in axiom_objs],
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════
    # Scene 4  韦恩图 — 事件关系
    # ══════════════════════════════════════════════════════
    def scene_venn(self):
        sec = Text("事件的关系：韦恩图", font=FONT, font_size=36, color=C_A
                   ).move_to(UP * 5.5)
        self.play(Write(sec), run_time=0.5)

        # 构建韦恩图
        venn, OA, OB = self.make_venn()
        self.play(Create(venn[0]), run_time=0.5)          # 样本空间框
        self.play(GrowFromCenter(venn[1]), run_time=0.6)  # 圆 A
        self.play(Write(venn[3]), run_time=0.3)           # 标签 A
        self.play(GrowFromCenter(venn[2]), run_time=0.6)  # 圆 B
        self.play(Write(venn[4]), run_time=0.3)           # 标签 B
        self.play(FadeIn(venn[5]), run_time=0.3)          # 标签 S

        # 交集标注
        inter_pos = self.V_CENTER
        inter_dot = Dot(inter_pos, radius=0.08, color=C_AB)
        inter_lbl = MathTex(r"A \cap B", font_size=26, color=C_AB).move_to(
            inter_pos + DOWN * 0.55
        )
        self.play(FadeIn(inter_dot), Write(inter_lbl), run_time=0.5)

        # 说明文字
        explain1 = Text("交集 A∩B：两事件同时发生", font=FONT, font_size=23, color=C_AB
                        ).move_to(DOWN * 2.0)
        self.play(FadeIn(explain1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.7)

        # 并集高亮（两圆都变亮）
        self.play(
            venn[1].animate.set_fill(opacity=0.55),
            venn[2].animate.set_fill(opacity=0.55),
            run_time=0.5
        )
        explain2 = Text("并集 A∪B：A 或 B 至少发生一个", font=FONT, font_size=23, color=C_UNION
                        ).move_to(DOWN * 3.0)
        union_lbl = MathTex(r"A \cup B", font_size=26, color=C_UNION).move_to(
            inter_pos + UP * 0.7
        )
        self.play(FadeIn(explain2), Write(union_lbl), run_time=0.5)
        self.wait(0.7)

        # 恢复透明度
        self.play(
            venn[1].animate.set_fill(opacity=0.25),
            venn[2].animate.set_fill(opacity=0.25),
            run_time=0.4
        )

        self.wait(0.8)

        self.play(
            FadeOut(sec), FadeOut(venn),
            FadeOut(inter_dot), FadeOut(inter_lbl),
            FadeOut(union_lbl),
            FadeOut(explain1), FadeOut(explain2),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════
    # Scene 5  加法公式  P(A∪B) = P(A)+P(B)-P(A∩B)
    # ══════════════════════════════════════════════════════
    def scene_addition(self):
        sec = Text("加法公式", font=FONT, font_size=38, color=C_UNION).move_to(UP * 5.5)
        self.play(Write(sec), run_time=0.5)

        # 小型韦恩图（中心在 y=2.3）
        ctr = np.array([0.0, 2.4, 0.0])
        r   = 1.1
        OA  = ctr + np.array([-0.75, 0.0, 0.0])
        OB  = ctr + np.array([ 0.75, 0.0, 0.0])

        ss = RoundedRectangle(
            width=5.0, height=2.8, corner_radius=0.18,
            stroke_color=C_SS, stroke_width=2, fill_opacity=0
        ).move_to(ctr)
        cA = Circle(radius=r, stroke_color=C_A, stroke_width=2.5,
                    fill_color=C_A, fill_opacity=0.3).move_to(OA)
        cB = Circle(radius=r, stroke_color=C_B, stroke_width=2.5,
                    fill_color=C_B, fill_opacity=0.3).move_to(OB)

        lA = MathTex("A", font_size=30, color=C_A).move_to(OA + LEFT * 0.45 + UP * 0.25)
        lB = MathTex("B", font_size=30, color=C_B).move_to(OB + RIGHT * 0.45 + UP * 0.25)

        self.play(Create(ss), GrowFromCenter(cA), GrowFromCenter(cB), run_time=0.7)
        self.play(Write(lA), Write(lB), run_time=0.3)

        # P(A) 高亮
        self.play(cA.animate.set_fill(opacity=0.7), run_time=0.4)
        pa_lbl = MathTex(r"P(A)", font_size=26, color=C_A).move_to(UP * 0.6)
        self.play(FadeIn(pa_lbl), run_time=0.3)
        self.wait(0.3)

        # P(B) 高亮
        self.play(cB.animate.set_fill(opacity=0.7), run_time=0.4)
        pb_lbl = MathTex(r"+ P(B)", font_size=26, color=C_B).next_to(pa_lbl, RIGHT, buff=0.2)
        self.play(FadeIn(pb_lbl), run_time=0.3)
        self.wait(0.3)

        # 过度计算：交集被加了两次，需减去
        inter_center = ctr  # 交集在中间
        over_lbl = Text("重复计算！", font=FONT, font_size=22, color=C_HL
                        ).move_to(inter_center + DOWN * 0.05)
        self.play(
            Flash(Dot(inter_center, radius=0.05), color=C_HL, flash_radius=0.4),
            FadeIn(over_lbl),
            run_time=0.5
        )

        minus_lbl = MathTex(r"- P(A \cap B)", font_size=26, color=C_AB
                            ).next_to(pb_lbl, RIGHT, buff=0.2)
        self.play(FadeIn(minus_lbl), run_time=0.4)
        self.wait(0.5)

        # 完整公式
        formula = MathTex(
            r"P(A \cup B) = P(A) + P(B) - P(A \cap B)",
            font_size=30, color=WHITE
        ).move_to(DOWN * 1.2)
        box_f = SurroundingRectangle(formula, corner_radius=0.15,
                                     color=C_UNION, buff=0.2)
        self.play(
            cA.animate.set_fill(opacity=0.25),
            cB.animate.set_fill(opacity=0.25),
            FadeOut(pa_lbl), FadeOut(pb_lbl), FadeOut(minus_lbl), FadeOut(over_lbl),
            run_time=0.4
        )
        self.play(Write(formula), Create(box_f), run_time=0.8)

        # 数值示例
        ex_title = Text("例：P(A)=0.5, P(B)=0.4, P(A∩B)=0.2", font=FONT,
                        font_size=21, color=GRAY_A).move_to(DOWN * 2.5)
        ex_result = MathTex(
            r"P(A\cup B) = 0.5 + 0.4 - 0.2 = 0.7",
            font_size=26, color=C_HL
        ).move_to(DOWN * 3.4)
        self.play(FadeIn(ex_title), run_time=0.4)
        self.play(Write(ex_result), run_time=0.7)
        self.wait(1.3)

        self.play(
            FadeOut(sec),
            FadeOut(ss), FadeOut(cA), FadeOut(cB), FadeOut(lA), FadeOut(lB),
            FadeOut(formula), FadeOut(box_f),
            FadeOut(ex_title), FadeOut(ex_result),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════
    # Scene 6  互补公式  P(A) + P(Ā) = 1
    # ══════════════════════════════════════════════════════
    def scene_complement(self):
        sec = Text("互补公式", font=FONT, font_size=38, color=C_CERTAIN).move_to(UP * 5.5)
        self.play(Write(sec), run_time=0.5)

        # 矩形代表样本空间，一半 A 一半 Ā
        rect_w, rect_h = 6.0, 3.2
        rect_ctr = np.array([0.0, 2.2, 0.0])
        split = 0.65   # A 占左侧 65%

        rect_ss = Rectangle(
            width=rect_w, height=rect_h,
            stroke_color=C_SS, stroke_width=2.5,
            fill_opacity=0
        ).move_to(rect_ctr)

        # A 区域（左侧）
        w_A = rect_w * split
        rect_A = Rectangle(
            width=w_A, height=rect_h,
            fill_color=C_A, fill_opacity=0.45,
            stroke_width=0
        ).move_to(rect_ctr + LEFT * (rect_w / 2 - w_A / 2))

        # Ā 区域（右侧）
        w_Ac = rect_w * (1 - split)
        rect_Ac = Rectangle(
            width=w_Ac, height=rect_h,
            fill_color=C_IMPOS, fill_opacity=0.45,
            stroke_width=0
        ).move_to(rect_ctr + RIGHT * (rect_w / 2 - w_Ac / 2))

        lbl_A  = Text("A",  font=FONT, font_size=36, color=C_A).move_to(
            rect_ctr + LEFT * (rect_w * (1 - split) / 2 + 0.15)
        )
        lbl_Ac = MathTex(r"\bar{A}", font_size=36, color=C_IMPOS).move_to(
            rect_ctr + RIGHT * (rect_w * split / 2 + 0.15)
        )
        lbl_S_r = MathTex("S", font_size=24, color=C_SS).move_to(
            rect_ctr + np.array([rect_w / 2 - 0.3, rect_h / 2 - 0.3, 0])
        )

        self.play(Create(rect_ss), run_time=0.5)
        self.play(FadeIn(rect_A), run_time=0.5)
        self.play(FadeIn(rect_Ac), run_time=0.5)
        self.play(Write(lbl_A), Write(lbl_Ac), FadeIn(lbl_S_r), run_time=0.4)

        # 概率标注
        pa_val  = MathTex(r"P(A) = 0.65", font_size=26, color=C_A).move_to(UP * 0.3)
        pac_val = MathTex(r"P(\bar{A}) = 0.35", font_size=26, color=C_IMPOS).move_to(DOWN * 0.5)
        self.play(Write(pa_val), run_time=0.4)
        self.play(Write(pac_val), run_time=0.4)

        # 公式
        formula = MathTex(
            r"P(A) + P(\bar{A}) = 1",
            font_size=34, color=WHITE
        ).move_to(DOWN * 1.8)
        box_f = SurroundingRectangle(formula, corner_radius=0.15,
                                     color=C_CERTAIN, buff=0.2)
        self.play(Write(formula), Create(box_f), run_time=0.7)

        derive = MathTex(
            r"\therefore\ P(\bar{A}) = 1 - P(A)",
            font_size=30, color=C_CERTAIN
        ).move_to(DOWN * 3.1)
        self.play(FadeIn(derive, shift=UP * 0.2), run_time=0.5)

        tip = Text("已知 P(A) 求 P(Ā) 的秘诀！", font=FONT, font_size=23, color=C_HL
                   ).move_to(DOWN * 4.1)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.4)
        self.wait(1.4)

        self.play(
            FadeOut(sec),
            FadeOut(rect_ss), FadeOut(rect_A), FadeOut(rect_Ac),
            FadeOut(lbl_A), FadeOut(lbl_Ac), FadeOut(lbl_S_r),
            FadeOut(pa_val), FadeOut(pac_val),
            FadeOut(formula), FadeOut(box_f),
            FadeOut(derive), FadeOut(tip),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════
    # Scene 7  总结
    # ══════════════════════════════════════════════════════
    def scene_summary(self):
        title_s = Text("核心公式总结", font=FONT, font_size=40, color=GOLD).move_to(UP * 5.5)
        self.play(Write(title_s), run_time=0.6)

        rows = [
            ("非负性",    r"P(A) \geq 0",                           C_RAND),
            ("规范性",    r"P(S) = 1,\quad P(\varnothing) = 0",      C_CERTAIN),
            ("加法公式",  r"P(A\cup B)=P(A)+P(B)-P(A\cap B)",        C_UNION),
            ("互补公式",  r"P(\bar{A}) = 1 - P(A)",                  C_IMPOS),
            ("概率范围",  r"0 \leq P(A) \leq 1",                     C_HL),
        ]

        card_objs = []
        start_y = 4.0
        gap = 1.6
        for i, (name, tex, col) in enumerate(rows):
            y_pos = start_y - i * gap
            bg = RoundedRectangle(
                width=8.2, height=1.35, corner_radius=0.15,
                fill_color=C_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2.2
            ).move_to(UP * y_pos)
            nm = Text(name, font=FONT, font_size=22, color=col).move_to(
                bg.get_center() + LEFT * 2.7
            )
            fm = MathTex(tex, font_size=22, color=WHITE).move_to(
                bg.get_center() + RIGHT * 0.5
            )
            card = VGroup(bg, nm, fm)
            card.shift(LEFT * 12)
            self.add(card)
            self.play(card.animate.shift(RIGHT * 12), run_time=0.38)
            card_objs.append(card)

        # 概率是描述不确定性的工具
        insight = Text(
            "概率 = 用数字描述不确定性",
            font=FONT, font_size=26, color=C_HL
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(insight, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        self.play(
            *[FadeOut(c) for c in card_objs],
            FadeOut(title_s), FadeOut(insight),
            run_time=0.6
        )

    # ══════════════════════════════════════════════════════
    # Scene 8  片尾
    # ══════════════════════════════════════════════════════
    def scene_outro(self):
        self.play(FadeOut(self.title_obj), run_time=0.4)

        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=44, color=WHITE
        ).move_to(UP * 2.2)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 1.2)
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=C_HL
        ).move_to(DOWN * 0.1)

        self.play(Transform(self.author_banner, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow, scale=1.05, shift=UP * 0.2), run_time=0.6)

        # 五彩圆点（代表概率 0~1）
        n = 6
        deco_dots = VGroup(*[
            Dot(radius=0.2, color=interpolate_color(C_IMPOS, C_CERTAIN, i / (n - 1)),
                fill_opacity=0.9)
            for i in range(n)
        ]).arrange(RIGHT, buff=0.42).move_to(DOWN * 1.8)

        prob_vals = VGroup(*[
            Text(f"{i/(n-1):.1f}", font=FONT, font_size=16, color=GRAY_B).move_to(
                deco_dots[i].get_center() + DOWN * 0.42
            )
            for i in range(n)
        ])

        self.play(*[FadeIn(d, scale=0.5) for d in deco_dots], run_time=0.5)
        self.play(FadeIn(prob_vals), run_time=0.4)

        # 彩点跳动
        for _ in range(2):
            self.play(
                *[d.animate.shift(UP * (0.22 if j % 2 == 0 else 0))
                  for j, d in enumerate(deco_dots)],
                run_time=0.35
            )
            self.play(
                *[d.animate.shift(DOWN * (0.22 if j % 2 == 0 else 0))
                  for j, d in enumerate(deco_dots)],
                run_time=0.35
            )

        bottom = Text(
            "掌握概率，从容应对不确定！",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 3.1)
        self.play(FadeIn(bottom, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            *[FadeOut(o) for o in [
                self.author_banner, author_id, follow,
                deco_dots, prob_vals, bottom
            ]],
            run_time=1.0
        )