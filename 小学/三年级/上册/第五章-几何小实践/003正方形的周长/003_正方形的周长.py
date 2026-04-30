"""
正方形的周长 - Square Perimeter Lesson
三年级上册 第五章 几何小实践

内容：
1. 开场钩子：引出问题
2. 认识正方形：四条边都相等
3. 四边相加推导：边+边+边+边
4. 公式化简：边长×4，C=4a
5. 例题计算：已知边长求周长
6. 逆向思维：已知周长求边长
7. 片尾总结

目标观众：三年级学生
格式：TikTok竖屏 (1080×1920)
作者：上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ─── 全局配置 TikTok 竖屏 ────────────────────────────────
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ─── 颜色常量 ────────────────────────────────────────────
BG_COLOR       = "#1a1a2e"
COLOR_SQUARE   = "#4fc3f7"   # 浅蓝 —— 正方形轮廓
COLOR_SIDE     = "#f9a825"   # 金黄 —— 边长 a
COLOR_FORMULA  = "#ce93d8"   # 紫色 —— 公式高亮
COLOR_EXAMPLE  = "#ff8a65"   # 橙色 —— 例题数字
COLOR_HINT     = "#80cbc4"   # 青色 —— 说明文字
COLOR_ANSWER   = "#66bb6a"   # 绿色 —— 答案


class SquarePerimeterLesson(Scene):
    """
    正方形周长教学动画
    场景顺序：
      0. 开场钩子
      1. 认识正方形（四边相等）
      2. 四条边相加推导
      3. 公式化简 C = 4a
      4. 例题（已知边长求周长）
      5. 逆向问题（已知周长求边长）
      6. 片尾总结
    """

    # ────────────────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG_COLOR

        # 品牌标识（全程保留）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.add(self.author)

        # 几何预计算
        self.setup_geometry()

        # 场景序列
        self.scene_hook()
        self.scene_intro_square()
        self.scene_four_sides()
        self.scene_formula()
        self.scene_example()
        self.scene_reverse()
        self.scene_outro()

    # ────────────────────────────────────────────────────
    def setup_geometry(self):
        """统一初始化正方形顶点坐标（精确计算）"""
        # 主正方形边长（逻辑单位）
        self.SIDE = 3.0
        self.SQ_CENTER = UP * 1.5

        # 四个顶点（精确，从中心计算）
        half = self.SIDE / 2
        cx, cy = self.SQ_CENTER[0], self.SQ_CENTER[1]

        self.A = np.array([cx - half, cy - half, 0])  # 左下
        self.B = np.array([cx + half, cy - half, 0])  # 右下
        self.C = np.array([cx + half, cy + half, 0])  # 右上
        self.D = np.array([cx - half, cy + half, 0])  # 左上

        # 各边中点（用于 Brace）
        self.M_bottom = (self.A + self.B) / 2
        self.M_right  = (self.B + self.C) / 2
        self.M_top    = (self.D + self.C) / 2
        self.M_left   = (self.A + self.D) / 2

        # 验证：正方形四边相等
        ab = np.linalg.norm(self.B - self.A)
        bc = np.linalg.norm(self.C - self.B)
        cd = np.linalg.norm(self.D - self.C)
        da = np.linalg.norm(self.A - self.D)
        assert abs(ab - self.SIDE) < 1e-9, "AB边长不符"
        assert abs(bc - self.SIDE) < 1e-9, "BC边长不符"
        assert abs(cd - self.SIDE) < 1e-9, "CD边长不符"
        assert abs(da - self.SIDE) < 1e-9, "DA边长不符"
        assert abs(ab - bc) < 1e-9, "正方形四边不等"

    # ────────────────────────────────────────────────────
    #  场景 0 — 开场钩子
    # ────────────────────────────────────────────────────
    def scene_hook(self):
        question = Text(
            "知道边长，能算出周长吗？",
            font="PingFang SC",
            font_size=36,
            color=YELLOW,
        ).move_to(UP * 5.5)

        sq_preview = self._make_square()
        sq_preview.move_to(self.SQ_CENTER)

        self.play(Write(question), run_time=0.9)
        self.play(Create(sq_preview), run_time=0.8)
        self.wait(0.6)
        self.play(FadeOut(question), FadeOut(sq_preview), run_time=0.5)

    # ────────────────────────────────────────────────────
    #  场景 1 — 认识正方形
    # ────────────────────────────────────────────────────
    def scene_intro_square(self):
        title = Text(
            "正方形的特点",
            font="PingFang SC",
            font_size=38,
            color=COLOR_SQUARE,
        ).move_to(UP * 6.2)

        sq = self._make_square()
        self.play(Write(title), run_time=0.6)
        self.play(Create(sq), run_time=0.8)

        # 标注顶点
        dots = VGroup(*[
            Dot(pt, radius=0.08, color=WHITE)
            for pt in [self.A, self.B, self.C, self.D]
        ])
        labels_text = ["A", "B", "C", "D"]
        label_dirs  = [DL, DR, UR, UL]
        vertex_labels = VGroup(*[
            MathTex(lbl, font_size=28, color=WHITE)
            .next_to(pt, d, buff=0.12)
            for lbl, pt, d in zip(labels_text,
                                  [self.A, self.B, self.C, self.D],
                                  label_dirs)
        ])
        self.play(FadeIn(dots), Write(vertex_labels), run_time=0.6)

        # 标注"四条边相等"的等号小刻度
        tick_groups = VGroup()
        side_mids = [self.M_bottom, self.M_right, self.M_top, self.M_left]
        side_dirs_perp = [UP, LEFT, DOWN, RIGHT]  # 垂直于各边的朝外方向
        for mid, perp in zip(side_mids, side_dirs_perp):
            # 单刻度（小短线垂直于边）
            perp_vec = np.array([perp[0], perp[1], 0])
            tick_start = mid + perp_vec * 0.1
            tick_end   = mid - perp_vec * 0.1
            # 两条小刻度线
            t1 = Line(tick_start + np.array([-0.08, -0.08, 0]) * abs(perp_vec[1] + perp_vec[0]),
                      tick_end   + np.array([-0.08, -0.08, 0]) * abs(perp_vec[1] + perp_vec[0]),
                      color=COLOR_SIDE, stroke_width=2.5)
            t2 = Line(tick_start + np.array([0.08, 0.08, 0]) * abs(perp_vec[1] + perp_vec[0]),
                      tick_end   + np.array([0.08, 0.08, 0]) * abs(perp_vec[1] + perp_vec[0]),
                      color=COLOR_SIDE, stroke_width=2.5)
            tick_groups.add(VGroup(t1, t2))

        # 说明文字
        hint = Text(
            "正方形：四条边都相等，四个直角",
            font="PingFang SC",
            font_size=26,
            color=COLOR_HINT,
        ).move_to(DOWN * 4.8)

        self.play(FadeIn(tick_groups), run_time=0.5)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清场（保留正方形）
        self.play(
            FadeOut(title), FadeOut(hint),
            FadeOut(dots), FadeOut(vertex_labels),
            FadeOut(tick_groups),
            run_time=0.5,
        )
        self.sq_obj = sq  # 保留正方形对象

    # ────────────────────────────────────────────────────
    #  场景 2 — 四条边相加推导
    # ────────────────────────────────────────────────────
    def scene_four_sides(self):
        title = Text(
            "周长 = 四条边之和",
            font="PingFang SC",
            font_size=34,
            color=YELLOW,
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 逐边高亮并添加标注
        sides = [
            (self.A, self.B, DOWN,  COLOR_SIDE),
            (self.B, self.C, RIGHT, COLOR_SIDE),
            (self.D, self.C, UP,    COLOR_SIDE),
            (self.A, self.D, LEFT,  COLOR_SIDE),
        ]

        side_lines  = VGroup()
        side_braces = VGroup()
        side_labels = VGroup()

        for i, (p1, p2, direction, color) in enumerate(sides):
            line = Line(p1, p2, color=color, stroke_width=5)

            brace = Brace(line, direction=direction, buff=0.12, color=color)
            lbl = MathTex("a", font_size=32, color=color)
            brace.put_at_tip(lbl, buff=0.12)

            self.play(
                Create(line),
                Create(brace),
                Write(lbl),
                run_time=0.5,
            )
            side_lines.add(line)
            side_braces.add(brace)
            side_labels.add(lbl)
            self.wait(0.15)

        # 四边相加公式
        formula_raw = MathTex(
            r"C = a + a + a + a",
            font_size=36,
            color=WHITE,
        ).move_to(DOWN * 3.8)
        formula_raw.set_color_by_tex("a", COLOR_SIDE)

        self.play(Write(formula_raw), run_time=0.8)
        self.wait(0.8)

        # 清理辅助线和标注
        self.play(
            FadeOut(title),
            FadeOut(side_lines),
            FadeOut(side_braces),
            FadeOut(side_labels),
            FadeOut(formula_raw),
            run_time=0.5,
        )

    # ────────────────────────────────────────────────────
    #  场景 3 — 公式化简 C = 4a
    # ────────────────────────────────────────────────────
    def scene_formula(self):
        title = Text(
            "化简得到公式",
            font="PingFang SC",
            font_size=36,
            color=COLOR_FORMULA,
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # 第一步：a+a+a+a
        step1 = MathTex(
            r"C", r"=", r"a", r"+", r"a", r"+", r"a", r"+", r"a",
            font_size=38,
        ).move_to(DOWN * 2.2)
        step1.set_color_by_tex("a", COLOR_SIDE)
        step1[0].set_color(WHITE)

        self.play(Write(step1), run_time=0.8)
        self.wait(0.5)

        # 说明：因为正方形四边相等
        explain0 = Text(
            "因为四条边都等于 a",
            font="PingFang SC",
            font_size=26,
            color=COLOR_HINT,
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(explain0, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # 箭头
        arrow = MathTex(r"\Rightarrow", font_size=34, color=GRAY_A)
        arrow.move_to(DOWN * 3.8)
        self.play(FadeOut(explain0), Write(arrow), run_time=0.4)

        # 第二步：a × 4
        step2 = MathTex(
            r"C", r"=", r"a", r"\times", r"4",
            font_size=42,
        ).move_to(DOWN * 4.6)
        step2.set_color_by_tex("a", COLOR_SIDE)
        step2[0].set_color(WHITE)
        step2[3].set_color(YELLOW)   # ×
        step2[4].set_color(YELLOW)   # 4

        self.play(Write(step2), run_time=0.8)
        self.wait(0.5)

        # 简写形式 C = 4a
        step3 = MathTex(
            r"C = 4a",
            font_size=52,
            color=COLOR_FORMULA,
        ).move_to(DOWN * 5.8)

        self.play(Write(step3), run_time=0.6)

        # 框出最终公式
        box = SurroundingRectangle(step3, color=COLOR_FORMULA, buff=0.18,
                                    stroke_width=3)
        self.play(Create(box), run_time=0.5)
        self.play(Indicate(step3, color=YELLOW, scale_factor=1.1), run_time=0.6)
        self.wait(1.2)

        # 文字图例
        legend = VGroup(
            MathTex("a", font_size=30, color=COLOR_SIDE),
            Text("：边长", font="PingFang SC",
                 font_size=26, color=COLOR_SIDE),
        ).arrange(RIGHT, buff=0.08)
        legend.move_to(DOWN * 7.0)
        self.play(FadeIn(legend, shift=UP * 0.2), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(step1), FadeOut(arrow),
            FadeOut(step2), FadeOut(step3), FadeOut(box),
            FadeOut(legend),
            run_time=0.5,
        )

    # ────────────────────────────────────────────────────
    #  场景 4 — 例题（已知边长求周长）
    # ────────────────────────────────────────────────────
    def scene_example(self):
        # 例题数值：边长 5 cm
        a_val = 5

        title = Text(
            "例题：求正方形的周长",
            font="PingFang SC",
            font_size=34,
            color=COLOR_EXAMPLE,
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 在图形底边标注边长
        brace_bottom = Brace(
            Line(self.A, self.B), direction=DOWN, buff=0.08, color=COLOR_SIDE
        )
        lbl_a = VGroup(
            MathTex("a", r"=", font_size=28, color=COLOR_SIDE),
            Text(f"{a_val} cm", font="PingFang SC",
                 font_size=28, color=COLOR_SIDE),
        ).arrange(RIGHT, buff=0.05)
        brace_bottom.put_at_tip(lbl_a, buff=0.1)

        self.play(Create(brace_bottom), Write(lbl_a), run_time=0.6)
        self.wait(0.4)

        # 代入公式逐步计算
        form_line = MathTex(
            r"C", r"=", r"4", r"a",
            font_size=38,
        ).move_to(DOWN * 3.0)
        form_line[2].set_color(YELLOW)
        form_line[3].set_color(COLOR_SIDE)

        self.play(Write(form_line), run_time=0.6)

        # 代入数值
        sub_line = MathTex(
            r"=", r"4", r"\times", r"5",
            font_size=38,
        ).next_to(form_line, DOWN, buff=0.4, aligned_edge=LEFT)
        sub_line[1].set_color(YELLOW)   # 4
        sub_line[2].set_color(YELLOW)   # ×
        sub_line[3].set_color(COLOR_EXAMPLE)  # 5

        self.play(Write(sub_line), run_time=0.6)

        # 最终答案
        result = a_val * 4
        ans_line = MathTex(
            rf"= {result}",
            font_size=42,
            color=COLOR_ANSWER,
        ).next_to(sub_line, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(ans_line), run_time=0.5)
        self.play(Indicate(ans_line, color=YELLOW, scale_factor=1.15), run_time=0.6)

        ans_text = Text(
            f"周长为 {result} 厘米",
            font="PingFang SC",
            font_size=30,
            color=YELLOW,
        ).move_to(DOWN * 6.6)
        self.play(FadeIn(ans_text, shift=UP * 0.3), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(title),
            FadeOut(brace_bottom), FadeOut(lbl_a),
            FadeOut(form_line), FadeOut(sub_line),
            FadeOut(ans_line), FadeOut(ans_text),
            run_time=0.6,
        )

    # ────────────────────────────────────────────────────
    #  场景 5 — 逆向问题（已知周长求边长）
    # ────────────────────────────────────────────────────
    def scene_reverse(self):
        title = Text(
            "逆向思维：已知周长求边长",
            font="PingFang SC",
            font_size=30,
            color=COLOR_FORMULA,
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 问题描述
        q1 = Text(
            "周长 = 32 cm",
            font="PingFang SC",
            font_size=32,
            color=WHITE,
        ).move_to(UP * 5.0)
        q2 = Text(
            "边长 = ?",
            font="PingFang SC",
            font_size=34,
            color=YELLOW,
        ).next_to(q1, DOWN, buff=0.25)

        self.play(FadeIn(q1), FadeIn(q2), run_time=0.6)
        self.wait(0.5)

        # 解题步骤标题
        step_title = Text(
            "解题步骤：",
            font="PingFang SC",
            font_size=28,
            color=COLOR_HINT,
        ).move_to(UP * 3.6)
        self.play(Write(step_title), run_time=0.4)

        # C = 4a  →  a = C ÷ 4
        s1_left = Text("由公式", font="PingFang SC",
                        font_size=28, color=WHITE)
        s1_mid  = MathTex(r"C = 4a", font_size=28, color=COLOR_FORMULA)
        s1_right = Text("得：", font="PingFang SC",
                         font_size=28, color=WHITE)
        s1 = VGroup(s1_left, s1_mid, s1_right).arrange(RIGHT, buff=0.12)
        s1.move_to(UP * 2.7)
        self.play(Write(s1), run_time=0.6)

        s2_left = Text("边长", font="PingFang SC",
                        font_size=30, color=COLOR_SIDE)
        s2_eq   = MathTex(r"= C \div 4 = 32 \div 4 = 8",
                           font_size=30, color=COLOR_EXAMPLE)
        s2 = VGroup(s2_left, s2_eq).arrange(RIGHT, buff=0.12)
        s2.move_to(UP * 1.7)
        self.play(Write(s2), run_time=0.7)

        # 最终答案框
        ans_text = Text(
            "边长 = 8 厘米",
            font="PingFang SC",
            font_size=36,
            color=COLOR_ANSWER,
        ).move_to(UP * 0.5)
        ans_box = SurroundingRectangle(ans_text, color=COLOR_ANSWER,
                                        buff=0.18, stroke_width=3)
        self.play(Write(ans_text), run_time=0.5)
        self.play(Create(ans_box), run_time=0.4)
        self.wait(1.0)

        # 验证
        verify = Text(
            "验证：8 × 4 = 32 ✓",
            font="PingFang SC",
            font_size=26,
            color=COLOR_HINT,
        ).move_to(DOWN * 0.6)
        self.play(FadeIn(verify, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(q1), FadeOut(q2),
            FadeOut(step_title), FadeOut(s1), FadeOut(s2),
            FadeOut(ans_text), FadeOut(ans_box), FadeOut(verify),
            run_time=0.6,
        )

    # ────────────────────────────────────────────────────
    #  场景 6 — 片尾总结
    # ────────────────────────────────────────────────────
    def scene_outro(self):
        # 淡出剩余正方形
        self.play(FadeOut(self.sq_obj), run_time=0.4)

        # 公式复习卡
        card_title = Text(
            "正方形周长公式",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
        ).move_to(UP * 3.5)

        formula_big = MathTex(
            r"C = 4a",
            font_size=64,
            color=COLOR_FORMULA,
        ).move_to(UP * 2.0)

        # 说明
        legend = VGroup(
            MathTex("a", font_size=32, color=COLOR_SIDE),
            Text("：边长", font="PingFang SC",
                 font_size=28, color=COLOR_SIDE),
        ).arrange(RIGHT, buff=0.08)
        legend.move_to(UP * 0.9)

        # 记忆口诀
        tip = Text(
            "四条边都相等 → 边长乘以 4",
            font="PingFang SC",
            font_size=26,
            color=COLOR_HINT,
        ).move_to(UP * 0.0)

        self.play(Write(card_title), run_time=0.5)
        self.play(Write(formula_big), run_time=0.8)
        self.play(FadeIn(legend, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.4)
        self.wait(0.8)

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=30,
            color=YELLOW,
        ).move_to(DOWN * 1.2)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 作者大字
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
        ).move_to(DOWN * 2.4)
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color="#6b7280",
        ).move_to(DOWN * 3.2)

        self.play(FadeIn(author_big, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(author_id), run_time=0.4)
        self.wait(2.0)

        # 全部淡出
        self.play(
            FadeOut(card_title), FadeOut(formula_big),
            FadeOut(legend), FadeOut(tip), FadeOut(follow),
            FadeOut(author_big), FadeOut(author_id),
            run_time=0.8,
        )

    # ────────────────────────────────────────────────────
    #  工具方法
    # ────────────────────────────────────────────────────
    def _make_square(self):
        """用四个顶点精确创建正方形多边形"""
        return Polygon(
            self.A, self.B, self.C, self.D,
            color=COLOR_SQUARE,
            stroke_width=4,
        )
