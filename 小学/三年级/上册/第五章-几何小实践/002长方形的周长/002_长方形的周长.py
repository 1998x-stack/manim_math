"""
长方形的周长 - Rectangle Perimeter Lesson
三年级上册 第五章 几何小实践

内容：
1. 什么是周长
2. 长方形四条边相加推导公式
3. 周长公式：(长+宽)×2
4. 例题：已知长和宽求周长
5. 逆向思维：已知周长和长求宽

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
BG_COLOR      = "#1a1a2e"
COLOR_RECT    = "#4fc3f7"   # 浅蓝 —— 长方形轮廓
COLOR_LEN     = "#f9a825"   # 金黄 —— 长（a）
COLOR_WID     = "#66bb6a"   # 绿色 —— 宽（b）
COLOR_FORMULA = "#ce93d8"   # 紫色 —— 公式高亮
COLOR_EXAMPLE = "#ff8a65"   # 橙色 —— 例题数字
COLOR_HINT    = "#80cbc4"   # 青色 —— 说明文字


class RectPerimeterLesson(Scene):
    """
    长方形周长教学动画
    场景顺序：
      0. 开场钩子
      1. 长方形认识
      2. 四边相加推导
      3. 公式化简
      4. 例题计算
      5. 逆向问题
      6. 片尾
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
        self.scene_intro_rect()
        self.scene_four_sides()
        self.scene_formula()
        self.scene_example()
        self.scene_reverse()
        self.scene_outro()

    # ────────────────────────────────────────────────────
    def setup_geometry(self):
        """统一初始化长方形顶点坐标（精确计算）"""
        # 主长方形尺寸（逻辑单位）
        self.RECT_W = 3.6   # 长（横向）
        self.RECT_H = 2.2   # 宽（纵向）
        self.RECT_CENTER = UP * 1.5

        # 四个顶点（精确）
        half_w = self.RECT_W / 2
        half_h = self.RECT_H / 2
        cx, cy = self.RECT_CENTER[0], self.RECT_CENTER[1]

        self.A = np.array([cx - half_w, cy - half_h, 0])  # 左下
        self.B = np.array([cx + half_w, cy - half_h, 0])  # 右下
        self.C = np.array([cx + half_w, cy + half_h, 0])  # 右上
        self.D = np.array([cx - half_w, cy + half_h, 0])  # 左上

        # 各边中点（用于 Brace）
        self.M_bottom = (self.A + self.B) / 2
        self.M_right  = (self.B + self.C) / 2
        self.M_top    = (self.D + self.C) / 2
        self.M_left   = (self.A + self.D) / 2

        # 验证矩形
        ab = np.linalg.norm(self.B - self.A)
        dc = np.linalg.norm(self.C - self.D)
        ad = np.linalg.norm(self.D - self.A)
        bc = np.linalg.norm(self.C - self.B)
        assert abs(ab - dc) < 1e-9, "上下边不等"
        assert abs(ad - bc) < 1e-9, "左右边不等"
        assert abs(ab - self.RECT_W) < 1e-9, "宽度不符"
        assert abs(ad - self.RECT_H) < 1e-9, "高度不符"

    # ────────────────────────────────────────────────────
    #  场景 0 — 开场钩子
    # ────────────────────────────────────────────────────
    def scene_hook(self):
        question = Text(
            "知道长和宽，能算出周长吗？",
            font="PingFang SC",
            font_size=34,
            color=YELLOW,
        ).move_to(UP * 5.5)

        rect_preview = Rectangle(width=self.RECT_W, height=self.RECT_H,
                                  color=COLOR_RECT, stroke_width=4)
        rect_preview.move_to(self.RECT_CENTER)

        self.play(Write(question), run_time=0.9)
        self.play(Create(rect_preview), run_time=0.8)
        self.wait(0.6)
        self.play(FadeOut(question), FadeOut(rect_preview), run_time=0.5)

    # ────────────────────────────────────────────────────
    #  场景 1 — 认识长方形
    # ────────────────────────────────────────────────────
    def scene_intro_rect(self):
        title = Text(
            "长方形的特点",
            font="PingFang SC",
            font_size=38,
            color=COLOR_RECT,
        ).move_to(UP * 6.2)

        # 长方形
        rect = self._make_rect()
        self.play(Write(title), run_time=0.6)
        self.play(Create(rect), run_time=0.8)

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

        # 说明：对边相等
        hint = Text(
            "长方形：对边相等，四个直角",
            font="PingFang SC",
            font_size=26,
            color=COLOR_HINT,
        ).move_to(DOWN * 4.8)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # 清场
        self.play(
            FadeOut(title), FadeOut(hint),
            FadeOut(dots), FadeOut(vertex_labels),
            run_time=0.5,
        )
        self.rect_obj = rect  # 保留长方形对象

    # ────────────────────────────────────────────────────
    #  场景 2 — 四条边相加推导
    # ────────────────────────────────────────────────────
    def scene_four_sides(self):
        rect = self.rect_obj

        title = Text(
            "周长 = 四条边之和",
            font="PingFang SC",
            font_size=34,
            color=YELLOW,
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 逐边高亮并添加标注
        sides = [
            ("底边（长）", self.A, self.B, DOWN, COLOR_LEN),
            ("右边（宽）", self.B, self.C, RIGHT, COLOR_WID),
            ("顶边（长）", self.D, self.C, UP,   COLOR_LEN),
            ("左边（宽）", self.A, self.D, LEFT,  COLOR_WID),
        ]

        side_lines = VGroup()
        side_braces = VGroup()
        side_labels = VGroup()

        label_chars = ["a", "b", "a", "b"]

        for i, (name, p1, p2, direction, color) in enumerate(sides):
            line = Line(p1, p2, color=color, stroke_width=5)

            # Brace 朝外
            brace = Brace(line, direction=direction, buff=0.1, color=color)
            lbl = MathTex(label_chars[i], font_size=32, color=color)
            brace.put_at_tip(lbl, buff=0.12)

            self.play(
                line.animate.set_stroke(color=color, width=5),
                Create(brace),
                Write(lbl),
                run_time=0.55,
            )
            side_lines.add(line)
            side_braces.add(brace)
            side_labels.add(lbl)
            self.wait(0.2)

        # 四边相加公式（纯数学，无中文）
        formula_raw = MathTex(
            r"C = a + b + a + b",
            font_size=36,
            color=WHITE,
        ).move_to(DOWN * 3.8)

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
    #  场景 3 — 公式化简
    # ────────────────────────────────────────────────────
    def scene_formula(self):
        rect = self.rect_obj

        title = Text(
            "化简得到公式",
            font="PingFang SC",
            font_size=36,
            color=COLOR_FORMULA,
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # 第一步：a+b+a+b
        step1 = MathTex(
            r"C", r"=", r"a", r"+", r"b", r"+", r"a", r"+", r"b",
            font_size=38,
        ).move_to(DOWN * 2.5)
        step1.set_color_by_tex("a", COLOR_LEN)
        step1.set_color_by_tex("b", COLOR_WID)
        step1.set_color_by_tex("C", WHITE)

        self.play(Write(step1), run_time=0.8)
        self.wait(0.5)

        # 第二步：(a+b)×2
        step2 = MathTex(
            r"C", r"=", r"(", r"a", r"+", r"b", r")", r"\times", r"2",
            font_size=38,
        ).move_to(DOWN * 3.8)
        step2.set_color_by_tex("a", COLOR_LEN)
        step2.set_color_by_tex("b", COLOR_WID)
        step2.set_color_by_tex("C", WHITE)
        step2[7].set_color(YELLOW)   # ×
        step2[8].set_color(YELLOW)   # 2

        arrow = MathTex(r"\Rightarrow", font_size=34, color=GRAY_A)
        arrow.move_to(DOWN * 3.15)

        self.play(Write(arrow), run_time=0.3)
        self.play(Write(step2), run_time=0.8)
        self.wait(0.5)

        # 框出最终公式
        box = SurroundingRectangle(step2, color=COLOR_FORMULA, buff=0.15,
                                    stroke_width=3)
        self.play(Create(box), run_time=0.5)

        # 文字说明（用 Text，不放 MathTex）
        explain = Text(
            "将(长+宽)看成一组，共 2 组",
            font="PingFang SC",
            font_size=24,
            color=COLOR_HINT,
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(step1), FadeOut(arrow),
            FadeOut(step2), FadeOut(box), FadeOut(explain),
            run_time=0.5,
        )

    # ────────────────────────────────────────────────────
    #  场景 4 — 例题（已知长和宽求周长）
    # ────────────────────────────────────────────────────
    def scene_example(self):
        rect = self.rect_obj

        # 例题尺寸：长 6 cm，宽 4 cm
        a_val, b_val = 6, 4

        title = Text(
            "例题：求长方形的周长",
            font="PingFang SC",
            font_size=34,
            color=COLOR_EXAMPLE,
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 在图形上标注数值
        brace_bottom = Brace(
            Line(self.A, self.B), direction=DOWN, buff=0.08, color=COLOR_LEN
        )
        lbl_a = VGroup(
            MathTex("a", r"=", font_size=28, color=COLOR_LEN),
            Text(f"{a_val} cm", font="PingFang SC",
                 font_size=28, color=COLOR_LEN),
        ).arrange(RIGHT, buff=0.05)
        brace_bottom.put_at_tip(lbl_a, buff=0.1)

        brace_right = Brace(
            Line(self.B, self.C), direction=RIGHT, buff=0.08, color=COLOR_WID
        )
        lbl_b = VGroup(
            MathTex("b", r"=", font_size=28, color=COLOR_WID),
            Text(f"{b_val} cm", font="PingFang SC",
                 font_size=28, color=COLOR_WID),
        ).arrange(RIGHT, buff=0.05)
        brace_right.put_at_tip(lbl_b, buff=0.1)

        self.play(
            Create(brace_bottom), Write(lbl_a),
            Create(brace_right), Write(lbl_b),
            run_time=0.7,
        )
        self.wait(0.4)

        # 代入公式逐步计算
        # 公式行
        form_line = MathTex(
            r"C", r"=", r"(", r"a", r"+", r"b", r")", r"\times", r"2",
            font_size=36,
        ).move_to(DOWN * 3.3)
        form_line.set_color_by_tex("a", COLOR_LEN)
        form_line.set_color_by_tex("b", COLOR_WID)

        self.play(Write(form_line), run_time=0.7)

        # 代入数值
        sub_line = MathTex(
            r"=", r"(", r"6", r"+", r"4", r")", r"\times", r"2",
            font_size=36,
        ).next_to(form_line, DOWN, buff=0.4, aligned_edge=LEFT)
        sub_line[2].set_color(COLOR_LEN)   # 6
        sub_line[4].set_color(COLOR_WID)   # 4
        sub_line[6].set_color(YELLOW)      # ×
        sub_line[7].set_color(YELLOW)      # 2

        self.play(Write(sub_line), run_time=0.7)

        # 中间结果
        mid_line = MathTex(
            r"=", r"10", r"\times", r"2",
            font_size=36,
        ).next_to(sub_line, DOWN, buff=0.3, aligned_edge=LEFT)
        mid_line[2].set_color(YELLOW)
        mid_line[3].set_color(YELLOW)

        self.play(Write(mid_line), run_time=0.5)

        # 最终答案
        ans_line = MathTex(r"= 20 \text{ cm}", font_size=40,
                            color=COLOR_EXAMPLE)
        ans_line.next_to(mid_line, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(ans_line), run_time=0.5)
        self.play(Indicate(ans_line, color=YELLOW, scale_factor=1.15),
                  run_time=0.6)

        ans_text = Text(
            "周长为 20 厘米",
            font="PingFang SC",
            font_size=28,
            color=YELLOW,
        ).move_to(DOWN * 7.0)
        self.play(FadeIn(ans_text, shift=UP * 0.3), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(title),
            FadeOut(brace_bottom), FadeOut(lbl_a),
            FadeOut(brace_right), FadeOut(lbl_b),
            FadeOut(form_line), FadeOut(sub_line),
            FadeOut(mid_line), FadeOut(ans_line),
            FadeOut(ans_text),
            run_time=0.6,
        )

    # ────────────────────────────────────────────────────
    #  场景 5 — 逆向问题（已知周长和长，求宽）
    # ────────────────────────────────────────────────────
    def scene_reverse(self):
        rect = self.rect_obj

        title = Text(
            "逆向思维：已知周长求宽",
            font="PingFang SC",
            font_size=32,
            color=COLOR_FORMULA,
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 问题描述（用两个 Text 拼合，避免中文+数学混排）
        q1 = Text(
            "周长 = 24 cm，长 = 8 cm",
            font="PingFang SC",
            font_size=30,
            color=WHITE,
        ).move_to(UP * 5.0)
        q2 = Text(
            "宽 = ?",
            font="PingFang SC",
            font_size=32,
            color=YELLOW,
        ).next_to(q1, DOWN, buff=0.25)

        self.play(FadeIn(q1), FadeIn(q2), run_time=0.6)
        self.wait(0.5)

        # 解题步骤
        # 步骤标题
        step_title = Text(
            "解题步骤：",
            font="PingFang SC",
            font_size=28,
            color=COLOR_HINT,
        ).move_to(UP * 3.5)
        self.play(Write(step_title), run_time=0.4)

        # 1. 长+宽 = 周长÷2
        s1_left = Text("长 + 宽", font="PingFang SC",
                        font_size=30, color=WHITE)
        s1_eq   = MathTex(r"= 24 \div 2 = 12", font_size=30, color=COLOR_EXAMPLE)
        s1 = VGroup(s1_left, s1_eq).arrange(RIGHT, buff=0.15)
        s1.move_to(UP * 2.5)
        self.play(Write(s1), run_time=0.6)

        # 2. 宽 = 12 - 8
        s2_left = Text("宽", font="PingFang SC",
                        font_size=30, color=COLOR_WID)
        s2_eq   = MathTex(r"= 12 - 8 = 4", font_size=30,
                           color=COLOR_EXAMPLE)
        s2 = VGroup(s2_left, s2_eq).arrange(RIGHT, buff=0.15)
        s2.move_to(UP * 1.5)
        self.play(Write(s2), run_time=0.6)

        # 最终答案框
        ans_text = Text(
            "宽 = 4 厘米",
            font="PingFang SC",
            font_size=36,
            color=COLOR_WID,
        ).move_to(UP * 0.4)
        ans_box = SurroundingRectangle(ans_text, color=COLOR_WID,
                                        buff=0.18, stroke_width=3)
        self.play(Write(ans_text), run_time=0.5)
        self.play(Create(ans_box), run_time=0.4)
        self.wait(1.2)

        # 验证
        verify = Text(
            "验证：(8 + 4) × 2 = 24 ✓",
            font="PingFang SC",
            font_size=26,
            color=COLOR_HINT,
        ).move_to(DOWN * 0.6)
        self.play(FadeIn(verify, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(q1), FadeOut(q2),
            FadeOut(step_title), FadeOut(s1), FadeOut(s2),
            FadeOut(ans_text), FadeOut(ans_box), FadeOut(verify),
            run_time=0.6,
        )

    # ────────────────────────────────────────────────────
    #  场景 6 — 片尾
    # ────────────────────────────────────────────────────
    def scene_outro(self):
        # 先淡出剩余长方形
        self.play(FadeOut(self.rect_obj), run_time=0.4)

        # 公式复习卡
        card_title = Text(
            "长方形周长公式",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
        ).move_to(UP * 3.5)

        formula_big = MathTex(
            r"C = (a + b) \times 2",
            font_size=52,
            color=COLOR_FORMULA,
        ).move_to(UP * 2.2)

        legend_a = VGroup(
            MathTex("a", font_size=30, color=COLOR_LEN),
            Text("：长", font="PingFang SC",
                 font_size=28, color=COLOR_LEN),
        ).arrange(RIGHT, buff=0.08)

        legend_b = VGroup(
            MathTex("b", font_size=30, color=COLOR_WID),
            Text("：宽", font="PingFang SC",
                 font_size=28, color=COLOR_WID),
        ).arrange(RIGHT, buff=0.08)

        legend = VGroup(legend_a, legend_b).arrange(RIGHT, buff=0.6)
        legend.move_to(UP * 1.1)

        self.play(Write(card_title), run_time=0.5)
        self.play(Write(formula_big), run_time=0.8)
        self.play(FadeIn(legend, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=30,
            color=YELLOW,
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 作者大字
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
        ).move_to(DOWN * 2.2)
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color="#6b7280",
        ).move_to(DOWN * 3.0)

        self.play(
            FadeIn(author_big, shift=UP * 0.2),
            run_time=0.5,
        )
        self.play(FadeIn(author_id), run_time=0.4)
        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(card_title), FadeOut(formula_big),
            FadeOut(legend), FadeOut(follow),
            FadeOut(author_big), FadeOut(author_id),
            run_time=0.8,
        )

    # ────────────────────────────────────────────────────
    #  工具方法
    # ────────────────────────────────────────────────────
    def _make_rect(self):
        """用四个顶点精确创建长方形多边形（避免 corner_radius）"""
        return Polygon(
            self.A, self.B, self.C, self.D,
            color=COLOR_RECT,
            stroke_width=4,
        )
