"""
function_concept.py
===================
函数的概念 — TikTok 竖屏教学动画
格式: 1080×1920  (frame_width=9, frame_height=16)
时长: ~65s
年级: 八年级第一学期

运行命令（推荐）:
    manim -pqh --resolution 1080,1920 --frame_rate 30 \\
          function_concept.py FunctionConcept

或在 manim.cfg 中添加:
    [CLI]
    pixel_width = 1080
    pixel_height = 1920
    frame_width = 9
    frame_height = 16
"""

from manim import *
import numpy as np

# ── 全局颜色 ──────────────────────────────────────────
BG           = "#0D1B2A"
C_WHITE      = WHITE
C_GOLD       = "#FFD700"
C_BLUE       = "#4FC3F7"
C_GREEN      = "#66BB6A"
C_ORANGE     = "#FFA726"
C_RED        = "#EF5350"
C_PURPLE     = "#CE93D8"
C_GRAY       = "#90A4AE"
C_DARKBOX    = "#1A2E45"


class FunctionConcept(Scene):
    """函数的概念 — 完整六场景教学动画"""

    def construct(self):
        self.camera.background_color = BG

        self.scene1_machine()
        self.scene2_definition()
        self.scene3_mapping()
        self.scene4_three_methods()
        self.scene5_domain_range()
        self.scene6_summary()

    # ══════════════════════════════════════════════════
    # 工具：统一标题
    # ══════════════════════════════════════════════════
    def _make_title(self, txt: str, color=C_WHITE, size=36) -> Text:
        return Text(txt, font_size=size, color=color,
                    font="PingFang SC").move_to(UP * 4.8)

    def _clear(self, *mobjs):
        if mobjs:
            self.play(*[FadeOut(m) for m in mobjs], run_time=0.5)

    # ══════════════════════════════════════════════════
    # Scene 1: 生活引入 — 函数机器 (0–8s)
    # ══════════════════════════════════════════════════
    def scene1_machine(self):
        title = self._make_title("函数是什么？", color=C_WHITE, size=40)

        # 机器外框
        box = RoundedRectangle(
            width=3.6, height=3.8,
            corner_radius=0.25,
            color=C_BLUE, fill_color=C_DARKBOX, fill_opacity=0.9,
            stroke_width=2.5,
        ).move_to(UP * 0.3)

        box_label = Text("函 数 机 器", font_size=28, color=C_GOLD,
                         font="PingFang SC").move_to(UP * 1.8)

        # 齿轮装饰（简单圆形代替）
        gear = Circle(radius=0.6, color=C_BLUE, fill_color="#1E3A5F",
                      fill_opacity=0.8, stroke_width=2).move_to(UP * 0.3)
        gear_f = MathTex(r"f", font_size=40, color=C_GOLD).move_to(UP * 0.3)

        # 输入端
        in_arrow = Arrow(
            start=LEFT * 3.5 + UP * 0.3,
            end=LEFT * 1.9 + UP * 0.3,
            color=C_GREEN, stroke_width=5, tip_length=0.25,
            buff=0,
        )
        in_label_top = Text("输入", font_size=24, color=C_GREEN,
                            font="PingFang SC").next_to(in_arrow, UP, buff=0.1)
        in_label_bot = MathTex(r"x", font_size=28, color=C_GREEN).next_to(
            in_arrow, DOWN, buff=0.1)

        # 输出端
        out_arrow = Arrow(
            start=RIGHT * 1.9 + UP * 0.3,
            end=RIGHT * 3.5 + UP * 0.3,
            color=C_ORANGE, stroke_width=5, tip_length=0.25,
            buff=0,
        )
        out_label_top = Text("输出", font_size=24, color=C_ORANGE,
                             font="PingFang SC").next_to(out_arrow, UP, buff=0.1)
        out_label_bot = MathTex(r"y", font_size=28, color=C_ORANGE).next_to(
            out_arrow, DOWN, buff=0.1)

        # 关键词
        key_text = Text("每个 x → 唯一确定的 y",
                        font_size=28, color=C_RED,
                        font="PingFang SC").move_to(DOWN * 2.0)
        key_box = SurroundingRectangle(key_text, color=C_RED, buff=0.18,
                                       corner_radius=0.1)

        # 动画
        self.play(Write(title), run_time=0.8)
        self.play(DrawBorderThenFill(box), run_time=0.6)
        self.play(FadeIn(box_label), GrowFromCenter(gear), FadeIn(gear_f),
                  run_time=0.5)
        self.play(Create(in_arrow), FadeIn(in_label_top, in_label_bot),
                  run_time=0.6)
        self.play(Create(out_arrow), FadeIn(out_label_top, out_label_bot),
                  run_time=0.6)
        self.play(FadeIn(key_text), Create(key_box), run_time=0.5)
        self.play(Indicate(key_text, color=C_GOLD, scale_factor=1.05),
                  run_time=0.8)
        self.wait(1.0)

        self._clear(title, box, box_label, gear, gear_f,
                    in_arrow, in_label_top, in_label_bot,
                    out_arrow, out_label_top, out_label_bot,
                    key_text, key_box)

    # ══════════════════════════════════════════════════
    # Scene 2: 数学定义 (8–18s)
    # ══════════════════════════════════════════════════
    def scene2_definition(self):
        title = self._make_title("② 函数的定义", color=C_GOLD, size=36)

        # 三行定义（用 Text，因为含中文）
        def_lines = VGroup(
            Text("有两个变量 x 和 y", font_size=28, color=C_WHITE,
                 font="PingFang SC"),
            Text("x 每取一个值，", font_size=28, color=C_WHITE,
                 font="PingFang SC"),
            Text("y 有唯一确定的值对应", font_size=28, color=C_GREEN,
                 font="PingFang SC"),
        ).arrange(DOWN, buff=0.35).move_to(UP * 2.2)

        # 编号圆圈
        def make_num_circle(n, color):
            c = Circle(radius=0.22, color=color,
                       fill_color=color, fill_opacity=0.85, stroke_width=0)
            t = Text(str(n), font_size=18, color=C_WHITE,
                     font="PingFang SC").move_to(c.get_center())
            return VGroup(c, t)

        nums = VGroup(*[
            make_num_circle(i+1, [C_BLUE, C_ORANGE, C_GREEN][i])
            for i in range(3)
        ])
        for i, num in enumerate(nums):
            num.next_to(def_lines[i], LEFT, buff=0.15)

        # 核心公式
        big_formula = MathTex(r"y = f(x)", font_size=64, color=C_GOLD)
        big_formula.move_to(DOWN * 1.2)
        formula_box = SurroundingRectangle(
            big_formula, color=C_GOLD, buff=0.28,
            corner_radius=0.14, stroke_width=2.5,
        )

        # 自变量标注
        x_brace_start = big_formula.get_part_by_tex("x").get_bottom()
        y_brace_start = big_formula.get_part_by_tex("y").get_bottom()

        arrow_x = Arrow(
            start=x_brace_start + DOWN * 0.1,
            end=x_brace_start + DOWN * 0.85,
            color=C_GREEN, stroke_width=3, tip_length=0.2, buff=0,
        )
        lbl_x = Text("自变量", font_size=22, color=C_GREEN,
                     font="PingFang SC").next_to(arrow_x, DOWN, buff=0.08)

        arrow_y = Arrow(
            start=y_brace_start + DOWN * 0.1,
            end=y_brace_start + DOWN * 0.85,
            color=C_ORANGE, stroke_width=3, tip_length=0.2, buff=0,
        )
        lbl_y = Text("因变量", font_size=22, color=C_ORANGE,
                     font="PingFang SC").next_to(arrow_y, DOWN, buff=0.08)

        # 动画
        self.play(Write(title), run_time=0.6)
        for i in range(3):
            self.play(
                FadeIn(nums[i]),
                Write(def_lines[i]),
                run_time=0.6,
            )
        self.play(Write(big_formula), Create(formula_box), run_time=0.8)
        self.play(
            Create(arrow_x), FadeIn(lbl_x),
            Create(arrow_y), FadeIn(lbl_y),
            run_time=0.6,
        )
        self.play(Circumscribe(big_formula, color=C_GOLD, run_time=1.0))
        self.wait(1.2)

        self._clear(title, def_lines, nums,
                    big_formula, formula_box,
                    arrow_x, lbl_x, arrow_y, lbl_y)

    # ══════════════════════════════════════════════════
    # Scene 3: 映射图 — 是否为函数 (18–28s)
    # ══════════════════════════════════════════════════
    def scene3_mapping(self):
        title = self._make_title("③ 判断：是函数吗？", color=C_WHITE, size=34)

        def make_dot_label(val, pos, color=C_WHITE):
            d = Circle(radius=0.3, color=color,
                       fill_color=C_DARKBOX, fill_opacity=1.0,
                       stroke_width=2).move_to(pos)
            t = MathTex(str(val), font_size=26, color=color).move_to(pos)
            return VGroup(d, t)

        lx, rx = -2.2, 2.2
        ys = [2.0, 1.0, 0.0]

        # ── 左列 x 值
        x_vals = [1, 2, 3]
        x_dots = VGroup(*[
            make_dot_label(x_vals[i], [lx, ys[i], 0], C_BLUE)
            for i in range(3)
        ])
        x_head = Text("x", font_size=28, color=C_BLUE,
                      font="PingFang SC").move_to([lx, 3.0, 0])

        # ── 右列 y 值（一对一）
        y_vals = [3, 5, 7]
        y_dots = VGroup(*[
            make_dot_label(y_vals[i], [rx, ys[i], 0], C_GREEN)
            for i in range(3)
        ])
        y_head = Text("y", font_size=28, color=C_GREEN,
                      font="PingFang SC").move_to([rx, 3.0, 0])

        # 映射箭头（绿色，一对一）
        good_arrows = VGroup(*[
            Arrow(
                start=[lx + 0.32, ys[i], 0],
                end=[rx - 0.32, ys[i], 0],
                color=C_GREEN, stroke_width=2.5,
                tip_length=0.2, buff=0,
            )
            for i in range(3)
        ])

        # 正确标记
        check = Text("✓ 这是函数！", font_size=30, color=C_GREEN,
                     font="PingFang SC").move_to(DOWN * 1.3)
        check_box = SurroundingRectangle(check, color=C_GREEN, buff=0.15,
                                         corner_radius=0.1)

        # 动画 Scene3a（一对一 = 函数）
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(x_head, y_head), run_time=0.4)
        self.play(FadeIn(x_dots), run_time=0.5)
        self.play(FadeIn(y_dots), run_time=0.4)
        for arr in good_arrows:
            self.play(Create(arr), run_time=0.3)
        self.play(Write(check), Create(check_box), run_time=0.5)
        self.wait(0.8)

        # ── 变换：展示"一对多"非函数 ─────────────────
        # x=2 再增加一个红色箭头指向 y=8
        bad_y_dot = make_dot_label(8, [rx, -0.9, 0], C_RED)
        bad_arrow = Arrow(
            start=[lx + 0.32, ys[1], 0],   # x=2 对应 y=1.0
            end=[rx - 0.32, -0.9, 0],
            color=C_RED, stroke_width=2.5,
            tip_length=0.2, buff=0,
        )
        bad_label = Text("×", font_size=40, color=C_RED,
                         font="PingFang SC").next_to(good_arrows[1], UP, buff=0.1)
        bad_cross = Text("✗", font_size=40, color=C_RED,
                         font="PingFang SC").next_to(bad_arrow, DOWN, buff=0.1)

        bad_warn = Text("一个x→多个y，不是函数！",
                        font_size=26, color=C_RED,
                        font="PingFang SC").move_to(DOWN * 2.5)
        bad_warn_box = SurroundingRectangle(bad_warn, color=C_RED, buff=0.14,
                                             corner_radius=0.1)

        # 淡出正确提示
        self.play(FadeOut(check, check_box), run_time=0.4)
        # 把 good_arrows[1] 变红（x=2对应的那条）
        self.play(good_arrows[1].animate.set_color(C_GOLD), run_time=0.3)
        # 新增非法箭头
        self.play(
            FadeIn(bad_y_dot),
            Create(bad_arrow),
            run_time=0.5,
        )
        self.play(
            bad_arrow.animate.set_color(C_RED),
            good_arrows[1].animate.set_color(C_RED),
            FadeIn(bad_cross),
            run_time=0.4,
        )
        self.play(Write(bad_warn), Create(bad_warn_box), run_time=0.5)
        self.play(Indicate(bad_warn, color=C_GOLD, scale_factor=1.04),
                  run_time=0.6)
        self.wait(1.0)

        self._clear(title, x_head, y_head, x_dots, y_dots,
                    good_arrows, bad_y_dot, bad_arrow,
                    bad_cross, bad_warn, bad_warn_box)

    # ══════════════════════════════════════════════════
    # Scene 4: 三种表示方法 (28–42s)
    # ══════════════════════════════════════════════════
    def scene4_three_methods(self):
        # ── 4a: 解析式法 ─────────────────────────────
        title_a = self._make_title("④ 三种表示方法", color=C_GOLD, size=34)
        sub_a   = Text("① 解析式法", font_size=28, color=C_BLUE,
                       font="PingFang SC").move_to(UP * 3.5)

        formula_big = MathTex(r"y = 2x + 1", font_size=56, color=C_GOLD)
        formula_big.move_to(UP * 1.5)
        f_box = SurroundingRectangle(formula_big, color=C_GOLD, buff=0.25,
                                     corner_radius=0.12)

        desc_a = Text("用数学式子表达对应关系",
                      font_size=26, color=C_GRAY,
                      font="PingFang SC").move_to(DOWN * 0.2)

        pros_a = Text("✓ 简洁  ✓ 便于计算",
                      font_size=24, color=C_GREEN,
                      font="PingFang SC").move_to(DOWN * 1.0)

        self.play(Write(title_a), run_time=0.6)
        self.play(FadeIn(sub_a), run_time=0.4)
        self.play(Write(formula_big), Create(f_box), run_time=0.7)
        self.play(FadeIn(desc_a), FadeIn(pros_a), run_time=0.5)
        self.wait(1.2)
        self._clear(sub_a, formula_big, f_box, desc_a, pros_a)

        # ── 4b: 列表法 ───────────────────────────────
        sub_b = Text("② 列表法", font_size=28, color=C_ORANGE,
                     font="PingFang SC").move_to(UP * 3.5)

        # 表格：用矩形+文字构建
        # x行 y=1.5，y行 y=0.6
        col_xs = [-2.0, -1.0, 0.0, 1.0, 2.0]
        x_data = [-1, 0, 1, 2, ""]
        y_data = [-1, 1, 3, 5, ""]
        row_ys = [1.5, 0.55]
        row_labels = ["x", "y"]
        row_colors = [C_BLUE, C_ORANGE]

        table_cells = VGroup()
        # 表头列
        for ri, (row_label, ry, rc) in enumerate(
                zip(row_labels, row_ys, row_colors)):
            cell_bg = Rectangle(width=0.8, height=0.7,
                                 color=rc, fill_color=C_DARKBOX,
                                 fill_opacity=0.9, stroke_width=1.5)
            cell_bg.move_to([-2.8, ry, 0])
            cell_txt = MathTex(row_label, font_size=28, color=rc)
            cell_txt.move_to([-2.8, ry, 0])
            table_cells.add(VGroup(cell_bg, cell_txt))

        # 数据列
        data_cells = VGroup()
        for ci, cx in enumerate(col_xs):
            for ri, (data_list, ry, rc) in enumerate(
                    zip([x_data, y_data], row_ys, row_colors)):
                val = data_list[ci]
                if val == "":
                    continue
                cell_bg = Rectangle(width=0.9, height=0.7,
                                     color=C_GRAY, fill_color=C_DARKBOX,
                                     fill_opacity=0.85, stroke_width=1.0)
                cell_bg.move_to([cx - 1.55, ry, 0])
                cell_txt = MathTex(str(val), font_size=26, color=rc)
                cell_txt.move_to([cx - 1.55, ry, 0])
                data_cells.add(VGroup(cell_bg, cell_txt))

        # 列分隔线
        h_line1 = Line([-3.25, 1.93, 0], [2.0, 1.93, 0],
                       color=C_GRAY, stroke_width=1)
        h_line2 = Line([-3.25, 1.1, 0], [2.0, 1.1, 0],
                       color=C_GRAY, stroke_width=1.5)
        h_line3 = Line([-3.25, 0.18, 0], [2.0, 0.18, 0],
                       color=C_GRAY, stroke_width=1)
        v_line  = Line([-3.22, 1.93, 0], [-3.22, 0.18, 0],
                       color=C_ORANGE, stroke_width=1.5)

        desc_b = Text("列出具体的对应数值",
                      font_size=26, color=C_GRAY,
                      font="PingFang SC").move_to(DOWN * 0.7)

        self.play(FadeIn(sub_b), run_time=0.4)
        self.play(FadeIn(table_cells), Create(h_line2),
                  Create(v_line), run_time=0.5)
        self.play(FadeIn(data_cells), Create(h_line1), Create(h_line3),
                  run_time=0.7)
        self.play(FadeIn(desc_b), run_time=0.4)
        self.wait(1.2)
        self._clear(sub_b, table_cells, data_cells,
                    h_line1, h_line2, h_line3, v_line, desc_b)

        # ── 4c: 图像法 ───────────────────────────────
        sub_c = Text("③ 图像法", font_size=28, color=C_GREEN,
                     font="PingFang SC").move_to(UP * 3.5)

        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.0, 6.0, 1],
            x_length=5.0,
            y_length=5.5,
            axis_config={"color": C_GRAY, "stroke_width": 2,
                         "include_tip": True, "tip_length": 0.18},
            x_axis_config={"numbers_to_include": [-2, -1, 1, 2],
                           "font_size": 18, "color": C_GRAY},
            y_axis_config={"numbers_to_include": [-1, 1, 2, 3, 4, 5],
                           "font_size": 18, "color": C_GRAY},
        ).move_to(DOWN * 0.6)

        ax_labels = axes.get_axis_labels(
            MathTex(r"x", font_size=24, color=C_GRAY),
            MathTex(r"y", font_size=24, color=C_GRAY),
        )

        # y=2x+1 直线
        line_graph = axes.plot(
            lambda x: 2 * x + 1,
            x_range=[-2.2, 2.2],
            color=C_GOLD,
            stroke_width=3,
        )
        line_label = MathTex(r"y=2x+1", font_size=24, color=C_GOLD)
        line_label.next_to(axes.c2p(1.6, 4.2), RIGHT, buff=0.1)

        # 关键点
        key_points_data = [(-1, -1), (0, 1), (1, 3)]
        key_dots = VGroup(*[
            Dot(axes.c2p(x, y), color=C_RED, radius=0.1)
            for x, y in key_points_data
        ])
        key_labels = VGroup(*[
            MathTex(f"({x},{y})", font_size=18, color=C_RED).next_to(
                axes.c2p(x, y), UP + RIGHT * 0.3, buff=0.06
            )
            for x, y in key_points_data
        ])

        self.play(FadeIn(sub_c), run_time=0.4)
        self.play(Create(axes), Write(ax_labels), run_time=0.8)
        self.play(Create(line_graph), Write(line_label), run_time=0.8)
        self.play(FadeIn(key_dots), Write(key_labels), run_time=0.6)
        self.wait(1.2)

        self._clear(title_a, sub_c, axes, ax_labels,
                    line_graph, line_label, key_dots, key_labels)

    # ══════════════════════════════════════════════════
    # Scene 5: 定义域与值域 (42–52s)
    # ══════════════════════════════════════════════════
    def scene5_domain_range(self):
        title = self._make_title("⑤ 定义域 & 值域", color=C_PURPLE, size=34)

        # 以 y=2x+1，x∈[-1,2] 为例
        example = VGroup(
            Text("例：y = 2x+1，x ∈ [-1, 2]",
                 font_size=26, color=C_WHITE,
                 font="PingFang SC"),
        ).move_to(UP * 3.6)

        # x 数轴（上方）
        x_axis = NumberLine(
            x_range=[-3, 3, 1],
            length=6.0,
            color=C_GRAY,
            include_numbers=True,
            font_size=20,
            numbers_to_include=[-3, -2, -1, 0, 1, 2, 3],
            label_direction=DOWN,
        ).move_to(UP * 1.5)

        x_label = Text("自变量 x（定义域）",
                       font_size=22, color=C_GREEN,
                       font="PingFang SC").next_to(x_axis, UP, buff=0.15)

        # 绿色区间 [-1, 2]（直接使用 n2p 计算端点）
        domain_seg = Line(
            x_axis.n2p(-1), x_axis.n2p(2),
            color=C_GREEN, stroke_width=6,
        )
        domain_bracket = MathTex(r"[-1,\ 2]", font_size=24, color=C_GREEN)
        domain_bracket.next_to(x_axis.n2p(0.5), UP, buff=0.35)

        dom_dot_l = Dot(x_axis.n2p(-1), color=C_GREEN, radius=0.1)
        dom_dot_r = Dot(x_axis.n2p(2),  color=C_GREEN, radius=0.1)

        # 映射箭头（从x数轴向下到y数轴）
        map_arrows = VGroup(*[
            CurvedArrow(
                x_axis.n2p(x),
                np.array([x_axis.n2p(x)[0], -0.55, 0]),
                color=C_PURPLE, angle=-TAU / 8,
                stroke_width=2,
                tip_length=0.15,
            )
            for x in [-1, 0, 1, 2]
        ])

        # y 数轴（下方）
        y_axis = NumberLine(
            x_range=[-3, 7, 1],
            length=6.0,
            color=C_GRAY,
            include_numbers=True,
            font_size=20,
            numbers_to_include=[-1, 0, 1, 3, 5],
            label_direction=DOWN,
        ).move_to(DOWN * 1.2)

        y_label = Text("因变量 y（值域）",
                       font_size=22, color=C_ORANGE,
                       font="PingFang SC").next_to(y_axis, UP, buff=0.15)

        # 橙色区间 [-1, 5]
        range_seg = Line(
            y_axis.n2p(-1), y_axis.n2p(5),
            color=C_ORANGE, stroke_width=6,
        )
        range_bracket = MathTex(r"[-1,\ 5]", font_size=24, color=C_ORANGE)
        range_bracket.next_to(y_axis.n2p(2), UP, buff=0.35)
        rng_dot_l = Dot(y_axis.n2p(-1), color=C_ORANGE, radius=0.1)
        rng_dot_r = Dot(y_axis.n2p(5),  color=C_ORANGE, radius=0.1)

        # 结论
        concl = Text("定义域决定值域范围！",
                     font_size=26, color=C_GOLD,
                     font="PingFang SC").move_to(DOWN * 2.6)

        # 动画
        self.play(Write(title), FadeIn(example), run_time=0.6)
        self.play(Create(x_axis), Write(x_label), run_time=0.6)
        self.play(
            Create(domain_seg), FadeIn(dom_dot_l, dom_dot_r),
            Write(domain_bracket), run_time=0.6,
        )
        self.play(Create(y_axis), Write(y_label), run_time=0.5)
        self.play(
            LaggedStart(*[Create(a) for a in map_arrows],
                        lag_ratio=0.2),
            run_time=0.8,
        )
        self.play(
            Create(range_seg), FadeIn(rng_dot_l, rng_dot_r),
            Write(range_bracket), run_time=0.6,
        )
        self.play(Write(concl), run_time=0.5)
        self.play(
            Indicate(domain_bracket, color=C_GREEN, scale_factor=1.08),
            Indicate(range_bracket, color=C_ORANGE, scale_factor=1.08),
            run_time=0.7,
        )
        self.wait(1.2)

        self._clear(title, example, x_axis, x_label,
                    domain_seg, domain_bracket, dom_dot_l, dom_dot_r,
                    map_arrows, y_axis, y_label,
                    range_seg, range_bracket, rng_dot_l, rng_dot_r,
                    concl)

    # ══════════════════════════════════════════════════
    # Scene 6: 总结口诀 (52–65s)
    # ══════════════════════════════════════════════════
    def scene6_summary(self):
        title = self._make_title("📌 记住这三句话", color=C_GOLD, size=36)

        # 核心口诀（三行，逐字出现）
        slogans = [
            ("自变量 x 随便取，", C_GREEN),
            ("因变量 y 唯一定，", C_ORANGE),
            ("这就叫做函数关系！", C_GOLD),
        ]
        slogan_grp = VGroup(*[
            Text(s, font_size=32, color=c, font="PingFang SC")
            for s, c in slogans
        ]).arrange(DOWN, buff=0.45).move_to(UP * 1.8)

        # 核心公式
        big_f = MathTex(r"y = f(x)", font_size=72, color=C_GOLD).move_to(
            DOWN * 0.8)
        big_box = SurroundingRectangle(
            big_f, color=C_GOLD, buff=0.3,
            corner_radius=0.15, stroke_width=3,
        )

        # 三种方法小图标行
        method_texts = VGroup(
            Text("解析式法", font_size=22, color=C_BLUE,
                 font="PingFang SC"),
            Text("列 表 法", font_size=22, color=C_ORANGE,
                 font="PingFang SC"),
            Text("图 像 法", font_size=22, color=C_GREEN,
                 font="PingFang SC"),
        ).arrange(RIGHT, buff=0.9).move_to(DOWN * 2.6)

        method_dividers = VGroup(*[
            Text("|", font_size=22, color=C_GRAY,
                 font="PingFang SC")
            for _ in range(2)
        ])
        for i, div in enumerate(method_dividers):
            div.move_to(
                (method_texts[i].get_right() + method_texts[i+1].get_left()) / 2
            )

        # 底部提示
        bottom = Text("学会了吗？👍",
                      font_size=28, color=C_WHITE,
                      font="PingFang SC").move_to(DOWN * 3.8)

        # 动画
        self.play(Write(title), run_time=0.6)
        for line in slogan_grp:
            self.play(Write(line), run_time=0.6)

        self.play(GrowFromCenter(big_f), Create(big_box), run_time=0.8)
        self.play(
            Flash(big_f, color=C_GOLD,
                  flash_radius=1.6, line_length=0.35,
                  num_lines=12),
            run_time=0.8,
        )
        self.play(
            FadeIn(method_texts), FadeIn(method_dividers),
            run_time=0.5,
        )
        self.play(Write(bottom), run_time=0.5)
        self.play(
            Indicate(slogan_grp[2], color=C_GOLD, scale_factor=1.06),
            run_time=0.7,
        )
        self.wait(2.0)