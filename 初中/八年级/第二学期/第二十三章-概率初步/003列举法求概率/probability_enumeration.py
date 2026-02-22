"""
列举法求概率 — 教学动画
目标受众: 八年级学生
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


class ProbabilityEnumeration(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.C_TITLE  = "#f9ca24"
        self.C_MAIN   = "#22a6b3"
        self.C_RED    = "#eb4d4b"
        self.C_GREEN  = "#6ab04c"
        self.C_PURPLE = "#a29bfe"
        self.C_ORANGE = "#f0932b"
        self.C_RESULT = "#badc58"

        self.scene_opening()
        self.scene_steps()
        self.scene_table_method()
        self.scene_table_solve()
        self.scene_tree_method()
        self.scene_tree_solve()
        self.scene_comparison()
        self.scene_quick_practice()
        self.scene_summary()
        self.scene_outro()

    def card(self, w, h, col, pos, fill="#16213e", alpha=0.85):
        return RoundedRectangle(
            corner_radius=0.28, width=w, height=h,
            color=col, stroke_width=2,
            fill_color=fill, fill_opacity=alpha,
        ).move_to(pos)

    def fade_rest(self):
        self.play(*[FadeOut(m) for m in self.mobjects
                    if m is not self.author], run_time=0.45)

    # ─────────── Scene 1 ───────────
    def scene_opening(self):
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC", font_size=18, color=GRAY_B,
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        chapter = Text("八年级 · 第二十三章 · 概率初步",
                       font="Noto Sans CJK SC", font_size=20, color=GRAY_B,
                       ).move_to(UP * 6.55)
        self.play(FadeIn(chapter), run_time=0.3)

        hook = Text("同时投两枚硬币，\n两枚都是正面的概率是多少？",
                    font="Noto Sans CJK SC", font_size=28, color=self.C_TITLE,
                    ).move_to(UP * 5.5)
        self.play(Write(hook), run_time=0.7)

        wrong_bg = self.card(6.0, 1.4, self.C_RED, UP * 3.9, fill="#2d0a0a")
        wrong_l  = Text("直觉：1/2  ×", font="Noto Sans CJK SC",
                        font_size=30, color=WHITE).move_to(UP * 3.9)
        self.play(Create(wrong_bg), Write(wrong_l), run_time=0.5)

        right_bg = self.card(6.0, 1.4, self.C_GREEN, UP * 2.7,
                             fill="#0a2e1a")
        right_l  = Text("正确：1/4  ✓", font="Noto Sans CJK SC",
                        font_size=30, color=WHITE).move_to(UP * 2.7)
        self.play(Create(right_bg), Write(right_l), run_time=0.5)

        method = Text("用列举法，一个都不漏！",
                      font="Noto Sans CJK SC", font_size=28, color=self.C_TITLE,
                      ).move_to(UP * 1.4)
        self.play(FadeIn(method, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(chapter), FadeOut(hook), FadeOut(wrong_bg),
                  FadeOut(wrong_l), FadeOut(right_bg), FadeOut(right_l),
                  FadeOut(method), run_time=0.4)

    # ─────────── Scene 2 ───────────
    def scene_steps(self):
        title = Text("列举法四步走",
                     font="Noto Sans CJK SC", font_size=44, color=self.C_TITLE,
                     ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        steps = [
            (self.C_MAIN,   UP * 5.4,  "Step 1", "列出所有等可能的结果"),
            (self.C_ORANGE, UP * 3.9,  "Step 2", "数出事件 A 的结果数 m"),
            (self.C_PURPLE, UP * 2.4,  "Step 3", "数出总结果数 n"),
            (self.C_GREEN,  UP * 0.9,  "Step 4",
             "计算 P(A) = m / n"),
        ]
        for col, pos, tag, desc in steps:
            bg   = self.card(7.5, 1.35, col, pos)
            tag_t = Text(tag,  font="Noto Sans CJK SC", font_size=24, color=col)
            desc_t = Text(desc, font="Noto Sans CJK SC", font_size=24,
                          color=WHITE)
            VGroup(tag_t, desc_t).arrange(RIGHT, buff=0.3).move_to(pos)
            self.play(Create(bg), Write(tag_t), Write(desc_t), run_time=0.45)

        tool_bg = self.card(7.5, 1.5, self.C_TITLE, DOWN * 0.65,
                            fill="#1a1000")
        tool_t  = Text("工具：列表法（两步）/ 树状图（多步）",
                       font="Noto Sans CJK SC", font_size=24,
                       color=self.C_TITLE).move_to(DOWN * 0.65)
        self.play(Create(tool_bg), Write(tool_t), run_time=0.5)
        self.wait(1.8)
        self.fade_rest()

    # ─────────── Scene 3: Table ───────────
    def scene_table_method(self):
        title = Text("列表法  投两枚硬币",
                     font="Noto Sans CJK SC", font_size=36, color=self.C_TITLE,
                     ).move_to(UP * 6.5)
        prob_bg = self.card(7.2, 1.3, self.C_MAIN, UP * 5.6)
        prob_t  = Text("同时投两枚硬币，列出所有可能结果",
                       font="Noto Sans CJK SC", font_size=24, color=WHITE,
                       ).move_to(UP * 5.6)
        self.play(Write(title), Create(prob_bg), Write(prob_t), run_time=0.6)

        # 手工构建 2×2 表格 + 标题行/列
        # 单元格宽1.5，高0.75；表格左上角 (-1.5, +4.6)
        cw, ch = 1.5, 0.75
        labels_row = ["H", "T"]
        labels_col = ["H", "T"]

        # 表头行
        header_row_t = Text("硬币 2 →", font="Noto Sans CJK SC",
                             font_size=18, color=GRAY_A,
                             ).move_to(np.array([-2.5, 4.6, 0]))
        header_col_t = Text("硬币\n1↓", font="Noto Sans CJK SC",
                             font_size=18, color=GRAY_A,
                             ).move_to(np.array([-2.5, 3.7, 0]))
        self.play(Write(header_row_t), Write(header_col_t), run_time=0.4)

        # 列标题
        for j, lbl in enumerate(labels_row):
            x = -0.75 + j * cw
            t = Text(lbl, font="Noto Sans CJK SC", font_size=24,
                     color=self.C_ORANGE).move_to(np.array([x, 4.6, 0]))
            self.play(Write(t), run_time=0.18)

        # 行标题 + 内容格
        results = [["HH", "HT"], ["TH", "TT"]]
        result_mobs = []
        for i, (row_lbl, row) in enumerate(zip(labels_col, results)):
            y = 3.85 - i * ch
            rl = Text(row_lbl, font="Noto Sans CJK SC",
                      font_size=24, color=self.C_ORANGE,
                      ).move_to(np.array([-2.5, y, 0]))
            self.play(Write(rl), run_time=0.18)
            for j, cell in enumerate(row):
                x = -0.75 + j * cw
                col = self.C_GREEN if "H" in cell[:1] and "H" in cell[1:] else GRAY_A
                rect = Rectangle(width=cw - 0.1, height=ch - 0.08,
                                 color=col, stroke_width=1.5,
                                 fill_color="#16213e", fill_opacity=0.9,
                                 ).move_to(np.array([x, y, 0]))
                ct = Text(cell, font="Noto Sans CJK SC",
                          font_size=22, color=col,
                          ).move_to(np.array([x, y, 0]))
                result_mobs.append((rect, ct, col))
                self.play(Create(rect), Write(ct), run_time=0.22)

        note = Text("共 4 种等可能结果（n=4）",
                    font="Noto Sans CJK SC", font_size=24, color=self.C_MAIN,
                    ).move_to(UP * 2.6)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.5)
        self.fade_rest()

    # ─────────── Scene 4: Table solve ───────────
    def scene_table_solve(self):
        title = Text("列表法  求解",
                     font="Noto Sans CJK SC", font_size=38, color=self.C_TITLE,
                     ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.4)

        # 重建小表（紧凑版）
        cw, ch = 1.5, 0.72
        results = [["HH", "HT"], ["TH", "TT"]]
        highlight = {"HH"}

        mobs = []
        for i, row in enumerate(results):
            for j, cell in enumerate(row):
                x = -0.75 + j * cw
                y = 5.35 - i * ch
                col = self.C_GREEN if cell in highlight else GRAY_B
                rect = Rectangle(width=cw - 0.1, height=ch - 0.08,
                                 color=col, stroke_width=1.5,
                                 fill_color="#0a2e1a" if cell in highlight
                                 else "#16213e",
                                 fill_opacity=0.9,
                                 ).move_to(np.array([x, y, 0]))
                ct = Text(cell, font="Noto Sans CJK SC",
                          font_size=22, color=col,
                          ).move_to(np.array([x, y, 0]))
                mobs.append(rect); mobs.append(ct)

        self.play(*[Create(m) if isinstance(m, Rectangle)
                    else Write(m) for m in mobs], run_time=0.6)

        note_n = Text("总结果数 n = 4",
                      font="Noto Sans CJK SC", font_size=26, color=GRAY_A,
                      ).move_to(UP * 4.0)
        note_m = Text("两正 HH 只有 1 种，m = 1",
                      font="Noto Sans CJK SC", font_size=26, color=self.C_GREEN,
                      ).move_to(UP * 3.1)
        self.play(Write(note_n), run_time=0.35)
        self.play(Write(note_m), run_time=0.35)

        step = MathTex(r"P(\text{HH}) = \dfrac{1}{4}",
                       font_size=52, color=self.C_TITLE).move_to(UP * 2.0)
        self.play(Write(step), run_time=0.6)

        ans_bg = self.card(6.5, 1.5, self.C_RESULT, UP * 0.8,
                           fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"P(\text{both heads}) = \dfrac{1}{4}",
                         font_size=42, color=WHITE).move_to(UP * 0.8)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.5)
        self.play(Indicate(ans_f, color=self.C_RESULT, scale_factor=1.07),
                  run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 5: Tree ───────────
    def scene_tree_method(self):
        title = Text("树状图法  投两枚硬币",
                     font="Noto Sans CJK SC", font_size=34, color=self.C_TITLE,
                     ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        # 树形结构坐标
        root_pos   = np.array([0,    5.5, 0])
        l1_l_pos   = np.array([-2.2, 4.0, 0])
        l1_r_pos   = np.array([ 2.2, 4.0, 0])
        l2_ll_pos  = np.array([-3.2, 2.5, 0])
        l2_lr_pos  = np.array([-1.2, 2.5, 0])
        l2_rl_pos  = np.array([ 1.2, 2.5, 0])
        l2_rr_pos  = np.array([ 3.2, 2.5, 0])
        leaf_y = 1.1

        # 根节点
        root_dot = Dot(root_pos, radius=0.15, color=WHITE)
        root_lbl = Text("Start", font="Noto Sans CJK SC",
                        font_size=20, color=GRAY_A,
                        ).next_to(root_dot, UP, buff=0.1)
        self.play(GrowFromCenter(root_dot), Write(root_lbl), run_time=0.4)

        # 第一层
        l1_data = [
            (l1_l_pos, "H", self.C_MAIN),
            (l1_r_pos, "T", self.C_ORANGE),
        ]
        l1_dots, l1_arrows = [], []
        for pos, lbl, col in l1_data:
            d = Dot(pos, radius=0.13, color=col)
            a = Arrow(root_pos, pos, buff=0.2, color=col,
                      stroke_width=2.5, max_tip_length_to_length_ratio=0.15)
            t = Text(lbl, font="Noto Sans CJK SC",
                     font_size=22, color=col).next_to(d, UP, buff=0.08)
            l1_dots.append((d, t)); l1_arrows.append(a)
            self.play(Create(a), GrowFromCenter(d), Write(t), run_time=0.35)

        # 第二层
        l2_data = [
            (l2_ll_pos, l1_l_pos, "H", self.C_MAIN,   "HH", self.C_GREEN),
            (l2_lr_pos, l1_l_pos, "T", self.C_ORANGE,  "HT", GRAY_A),
            (l2_rl_pos, l1_r_pos, "H", self.C_MAIN,   "TH", GRAY_A),
            (l2_rr_pos, l1_r_pos, "T", self.C_ORANGE,  "TT", GRAY_A),
        ]
        for pos, parent, lbl, col, leaf_lbl, leaf_col in l2_data:
            d = Dot(pos, radius=0.12, color=col)
            a = Arrow(parent, pos, buff=0.15, color=col,
                      stroke_width=2, max_tip_length_to_length_ratio=0.15)
            t = Text(lbl, font="Noto Sans CJK SC",
                     font_size=20, color=col).next_to(d, UP, buff=0.06)
            leaf = Text(leaf_lbl, font="Noto Sans CJK SC",
                        font_size=22, color=leaf_col,
                        ).move_to(np.array([pos[0], leaf_y, 0]))
            self.play(Create(a), GrowFromCenter(d), Write(t),
                      Write(leaf), run_time=0.32)

        note = Text("共 4 个叶节点 = 4 种结果",
                    font="Noto Sans CJK SC", font_size=24, color=self.C_MAIN,
                    ).move_to(DOWN * 0.3)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.8)
        self.fade_rest()

    # ─────────── Scene 6: Tree solve ───────────
    def scene_tree_solve(self):
        title = Text("树状图  求解",
                     font="Noto Sans CJK SC", font_size=38, color=self.C_TITLE,
                     ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.4)

        # 快速展示4个叶节点结果
        leaves = ["HH", "HT", "TH", "TT"]
        leaf_colors = [self.C_GREEN, GRAY_A, GRAY_A, GRAY_A]
        xs = [-3.0, -1.0, 1.0, 3.0]
        leaf_y = 5.3
        for x, lbl, col in zip(xs, leaves, leaf_colors):
            box = RoundedRectangle(corner_radius=0.15, width=1.2, height=0.7,
                                   color=col, fill_color="#16213e",
                                   fill_opacity=0.85, stroke_width=2,
                                   ).move_to(np.array([x, leaf_y, 0]))
            t = Text(lbl, font="Noto Sans CJK SC",
                     font_size=22, color=col,
                     ).move_to(np.array([x, leaf_y, 0]))
            self.play(Create(box), Write(t), run_time=0.22)

        n_bg = self.card(7.2, 1.2, self.C_PURPLE, UP * 4.1)
        n_t  = Text("总叶节点数 n = 4",
                    font="Noto Sans CJK SC", font_size=26, color=WHITE,
                    ).move_to(UP * 4.1)
        self.play(Create(n_bg), Write(n_t), run_time=0.4)

        m_bg = self.card(7.2, 1.2, self.C_GREEN, UP * 2.95)
        m_t  = Text("两正 HH 仅 1 种，m = 1",
                    font="Noto Sans CJK SC", font_size=26, color=WHITE,
                    ).move_to(UP * 2.95)
        self.play(Create(m_bg), Write(m_t), run_time=0.4)

        # 换题：至少一正
        q2_bg = self.card(7.2, 1.3, self.C_MAIN, UP * 1.7)
        q2_t  = Text("P(至少一正) = ?",
                     font="Noto Sans CJK SC", font_size=28, color=WHITE,
                     ).move_to(UP * 1.7)
        self.play(Create(q2_bg), Write(q2_t), run_time=0.4)

        step = MathTex(r"P(\text{at least 1H}) = \dfrac{3}{4}",
                       font_size=46, color=self.C_TITLE).move_to(UP * 0.6)
        note = Text("HH, HT, TH 都算 → m=3",
                    font="Noto Sans CJK SC", font_size=22, color=GRAY_A,
                    ).move_to(UP * 0.0)
        self.play(Write(step), FadeIn(note), run_time=0.6)

        ans_bg = self.card(7.0, 1.5, self.C_RESULT, DOWN * 1.1,
                           fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"P(\text{at least 1H}) = \dfrac{3}{4}",
                         font_size=44, color=WHITE).move_to(DOWN * 1.1)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.5)
        self.play(Indicate(ans_f, color=self.C_RESULT, scale_factor=1.07),
                  run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 7: Comparison ───────────
    def scene_comparison(self):
        title = Text("两种方法对比",
                     font="Noto Sans CJK SC", font_size=42, color=self.C_TITLE,
                     ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        # 左：列表法
        left_bg = self.card(3.6, 4.0, self.C_MAIN, UP * 4.4 + LEFT * 1.9)
        left_title = Text("列表法", font="Noto Sans CJK SC",
                          font_size=28, color=self.C_MAIN).move_to(
            UP * 5.8 + LEFT * 1.9)
        l1 = Text("适合：两步试验",
                  font="Noto Sans CJK SC", font_size=20, color=WHITE)
        l2 = Text("形式：表格",
                  font="Noto Sans CJK SC", font_size=20, color=WHITE)
        l3 = Text("优点：直观清晰",
                  font="Noto Sans CJK SC", font_size=20, color=WHITE)
        l4 = Text("例：投两枚骰子",
                  font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        VGroup(l1, l2, l3, l4).arrange(DOWN, buff=0.28).move_to(
            UP * 4.4 + LEFT * 1.9)

        # 右：树状图
        right_bg = self.card(3.6, 4.0, self.C_PURPLE, UP * 4.4 + RIGHT * 1.9)
        right_title = Text("树状图", font="Noto Sans CJK SC",
                           font_size=28, color=self.C_PURPLE).move_to(
            UP * 5.8 + RIGHT * 1.9)
        r1 = Text("适合：多步试验",
                  font="Noto Sans CJK SC", font_size=20, color=WHITE)
        r2 = Text("形式：分支图",
                  font="Noto Sans CJK SC", font_size=20, color=WHITE)
        r3 = Text("优点：不遗漏",
                  font="Noto Sans CJK SC", font_size=20, color=WHITE)
        r4 = Text("例：连续抛硬币",
                  font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        VGroup(r1, r2, r3, r4).arrange(DOWN, buff=0.28).move_to(
            UP * 4.4 + RIGHT * 1.9)

        self.play(Create(left_bg), Create(right_bg),
                  Write(left_title), Write(right_title), run_time=0.5)
        self.play(*[Write(t) for t in [l1, l2, l3, l4, r1, r2, r3, r4]],
                  run_time=0.8)

        common_bg = self.card(7.4, 1.5, self.C_TITLE, UP * 2.1,
                              fill="#1a1000")
        common_t  = Text("共同目标：列出所有结果，一个不漏！",
                         font="Noto Sans CJK SC", font_size=24,
                         color=self.C_TITLE).move_to(UP * 2.1)
        self.play(Create(common_bg), Write(common_t), run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 8: Practice ───────────
    def scene_quick_practice(self):
        title = Text("综合练习",
                     font="Noto Sans CJK SC", font_size=44, color=self.C_TITLE,
                     ).move_to(UP * 6.6)
        self.play(Write(title), run_time=0.4)

        items = [
            ("投两枚硬币，P(一正一反)",
             r"P = \dfrac{2}{4} = \dfrac{1}{2}",
             self.C_MAIN, "HT, TH 共2种"),
            ("掷两骰（1~3），P(和=4)",
             r"P = \dfrac{3}{9} = \dfrac{1}{3}",
             self.C_PURPLE, "(1,3),(2,2),(3,1)"),
        ]
        card_h = 2.0
        start_y = 5.2
        for i, (q, res, col, hint) in enumerate(items):
            pos = UP * (start_y - i * 2.3)
            bg  = self.card(7.6, card_h, col, pos)
            qt  = Text(q, font="Noto Sans CJK SC", font_size=23, color=WHITE)
            rf  = MathTex(res, font_size=34, color=self.C_RESULT)
            ht  = Text(hint, font="Noto Sans CJK SC",
                       font_size=19, color=GRAY_A)
            VGroup(qt, rf, ht).arrange(DOWN, buff=0.18).move_to(pos)
            self.play(Create(bg), Write(qt), run_time=0.35)
            self.play(Write(rf), FadeIn(ht), run_time=0.35)
            self.wait(0.4)

        self.wait(1.5)
        self.fade_rest()

    # ─────────── Scene 9: Summary ───────────
    def scene_summary(self):
        title = Text("知识点总结",
                     font="Noto Sans CJK SC", font_size=46, color=self.C_TITLE,
                     ).move_to(UP * 6.6)
        self.play(Write(title), run_time=0.4)

        blocks = [
            (self.C_MAIN,   UP * 5.5, "公式",
             r"P(A)=\dfrac{m}{n}"),
            (self.C_ORANGE, UP * 4.0, "Step 1-4",
             r"\text{list} \rightarrow \text{count m} \rightarrow \text{count n} \rightarrow P"),
            (self.C_MAIN,   UP * 2.5, "列表法",
             r"\text{2-step trials} \rightarrow \text{grid table}"),
            (self.C_PURPLE, UP * 1.0, "树状图",
             r"\text{multi-step} \rightarrow \text{branch tree}"),
            (self.C_RESULT, DOWN * 0.5,"核心例题",
             r"P(\text{HH})=\frac{1}{4},\ P(\geq\text{1H})=\frac{3}{4}"),
        ]
        for col, pos, lbl, fml in blocks:
            bg = self.card(7.6, 1.3, col, pos)
            lt = Text(lbl, font="Noto Sans CJK SC", font_size=22, color=col)
            ft = MathTex(fml, font_size=26, color=WHITE)
            VGroup(lt, ft).arrange(RIGHT, buff=0.4).move_to(pos)
            self.play(Create(bg), Write(lt), Write(ft), run_time=0.42)

        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 10 ───────────
    def scene_outro(self):
        big = Text("上海初高中数学直通车",
                   font="Noto Sans CJK SC", font_size=38, color=WHITE,
                   ).move_to(UP * 2.5)
        uid = Text("@emptyandcalm",
                   font="Noto Sans CJK SC", font_size=28, color=GRAY_B,
                   ).move_to(UP * 1.7)
        self.play(Transform(self.author, big), run_time=0.8)
        self.play(FadeIn(uid, shift=UP * 0.2), run_time=0.4)

        follow = Text("关注我，学更多数学知识！",
                      font="Noto Sans CJK SC", font_size=30,
                      color=self.C_TITLE).move_to(UP * 0.3)
        self.play(FadeIn(follow, scale=1.1), run_time=0.6)

        deco = VGroup(
            MathTex(r"P(\text{HH})=\dfrac{1}{4}", font_size=30,
                    color=self.C_MAIN),
            MathTex(r"P(\geq 1H)=\dfrac{3}{4}", font_size=30,
                    color=self.C_GREEN),
        ).arrange(DOWN, buff=0.45).move_to(DOWN * 1.8)
        self.play(*[Write(f) for f in deco], run_time=0.9)
        self.play(*[Indicate(f, color=self.C_TITLE) for f in deco], run_time=0.8)
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)


# manim -pql probability_enumeration.py ProbabilityEnumeration
# manim -qh  probability_enumeration.py ProbabilityEnumeration