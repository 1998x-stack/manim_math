"""
立方根 - Manim 教学动画
年级: 七年级第二学期 第十二章
知识点: 立方根的概念与计算
格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ============================================================
# 全局配置 — TikTok 竖屏
# ============================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ============================================================
# 颜色常量
# ============================================================
COLOR_BG       = "#1a1a2e"
COLOR_CUBE_POS = "#4fc3f7"   # 天蓝  — 正数相关
COLOR_CUBE_NEG = "#ff7043"   # 橙红  — 负数相关
COLOR_CUBE_ZRO = "#ce93d8"   # 紫色  — 零
COLOR_POS      = "#66bb6a"   # 绿    — 正数结果
COLOR_NEG      = "#ff7043"   # 橙红  — 负数结果
COLOR_FORMULA  = "#ffd54f"   # 金黄  — 公式高亮
COLOR_COMPARE  = "#80cbc4"   # 青绿  — 对比色
COLOR_AXIS     = "#b0bec5"   # 灰白  — 数轴
COLOR_AUTHOR   = "#78909c"
FONT = "PingFang SC"


# ============================================================
# 工具函数
# ============================================================
def make_cube_2d(side: float, color=COLOR_CUBE_POS, fill_opacity=0.25) -> VGroup:
    """
    用三个平行四边形模拟2D等轴测正方体。
    side: 正面正方形的边长（屏幕单位）
    返回 VGroup（前面、顶面、侧面）
    """
    s = side
    # 偏移向量（等轴测投影）
    ox = s * 0.45   # 右上偏移 x 分量
    oy = s * 0.25   # 右上偏移 y 分量

    # 前面正方形（左下角为原点）
    front = Polygon(
        np.array([0, 0, 0]),
        np.array([s, 0, 0]),
        np.array([s, s, 0]),
        np.array([0, s, 0]),
        color=color,
        fill_color=color,
        fill_opacity=fill_opacity + 0.1,
        stroke_width=2
    )

    # 顶面（前面顶部 + 等轴测偏移）
    top = Polygon(
        np.array([0, s, 0]),
        np.array([s, s, 0]),
        np.array([s + ox, s + oy, 0]),
        np.array([ox,  s + oy, 0]),
        color=color,
        fill_color=color,
        fill_opacity=fill_opacity + 0.05,
        stroke_width=2
    )

    # 右侧面
    right = Polygon(
        np.array([s, 0, 0]),
        np.array([s, s, 0]),
        np.array([s + ox, s + oy, 0]),
        np.array([s + ox, oy, 0]),
        color=color,
        fill_color=color,
        fill_opacity=fill_opacity,
        stroke_width=2
    )

    grp = VGroup(front, top, right)
    # 将原点移至正方体中心（前面的中心）
    grp.move_to(ORIGIN)
    return grp


class CubeRootConcept(Scene):
    """
    立方根概念教学动画

    场景顺序:
    1. 开场钩子  — 体积推边长
    2. 立方根定义 — x³=a → x=³√a
    3. 三种情况  — 正/零/负
    4. 计算练习  — 常见立方根
    5. 与平方根对比
    6. 总结 + 片尾
    """

    def construct(self):
        self.camera.background_color = COLOR_BG
        self.scene_opening()
        self.scene_definition()
        self.scene_three_cases()
        self.scene_practice()
        self.scene_comparison()
        self.scene_outro()

    # ──────────────────────────────────────────────
    # Scene 1  开场钩子
    # ──────────────────────────────────────────────
    def scene_opening(self):
        # 作者信息（顶部固定）
        author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=20, color=COLOR_AUTHOR
        ).move_to(UP * 7.3)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.author_obj = author

        # 章节标题
        title = Text("立方根", font=FONT, font_size=52, color=GOLD)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        # 钩子问题
        hook_line1 = Text("一个正方体的体积是 8，", font=FONT, font_size=30, color=WHITE)
        hook_line2 = Text("它的边长是多少？", font=FONT, font_size=30, color=YELLOW)
        hook = VGroup(hook_line1, hook_line2).arrange(DOWN, buff=0.2)
        hook.move_to(UP * 5.0)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.6)

        # 画一个等轴测正方体（边长=2在屏幕上取 s=1.8 单位）
        cube = make_cube_2d(1.8, color=COLOR_CUBE_POS, fill_opacity=0.28)
        cube.move_to(UP * 2.5)
        self.play(FadeIn(cube, scale=0.6), run_time=0.8)

        # 体积标注
        vol_label = MathTex(r"V = 8", font_size=38, color=COLOR_FORMULA)
        vol_label.next_to(cube, RIGHT, buff=0.4)
        self.play(Write(vol_label), run_time=0.5)

        # 边长问号
        side_q = MathTex(r"x = \,?", font_size=40, color=YELLOW)
        side_q.next_to(cube, DOWN, buff=0.45)
        self.play(FadeIn(side_q, scale=0.8), run_time=0.4)
        self.play(Indicate(side_q, scale_factor=1.2, color=YELLOW), run_time=0.5)

        self.wait(1.0)
        self.play(FadeOut(VGroup(title, hook, cube, vol_label, side_q)), run_time=0.5)

    # ──────────────────────────────────────────────
    # Scene 2  立方根定义
    # ──────────────────────────────────────────────
    def scene_definition(self):
        sec_title = Text("什么是立方根？", font=FONT, font_size=38, color=GOLD)
        sec_title.move_to(UP * 6.2)
        self.play(Write(sec_title), run_time=0.5)

        # ── 核心关系式：x³ = a  ──
        eq1 = MathTex(r"x^3 = a", font_size=52, color=WHITE)
        eq1.move_to(UP * 5.0)
        self.play(Write(eq1), run_time=0.7)

        explain1 = Text("那么  x  叫做  a  的立方根", font=FONT, font_size=28, color=COLOR_COMPARE)
        explain1.move_to(UP * 4.1)
        self.play(FadeIn(explain1, shift=UP * 0.2), run_time=0.5)

        # ── 符号引入 ──
        symbol = MathTex(r"x = \sqrt[3]{a}", font_size=52, color=COLOR_FORMULA)
        symbol.move_to(UP * 3.0)
        box_sym = SurroundingRectangle(symbol, color=COLOR_FORMULA, buff=0.2, corner_radius=0.12)
        self.play(Write(symbol), Create(box_sym), run_time=0.8)

        tip_3 = Text("根指数 3", font=FONT, font_size=22, color=YELLOW)
        tip_3.next_to(symbol, UP + LEFT * 0.5, buff=0.25)
        arrow_3 = Arrow(
            tip_3.get_bottom(),
            symbol.get_left() + UP * 0.25,
            color=YELLOW, buff=0.08, stroke_width=2,
            max_tip_length_to_length_ratio=0.25
        )
        self.play(FadeIn(tip_3, shift=DOWN * 0.1), Create(arrow_3), run_time=0.5)

        self.wait(0.5)

        # ── 具体例子：2³ = 8 → ³√8 = 2 ──
        example_cube = make_cube_2d(1.5, color=COLOR_CUBE_POS, fill_opacity=0.3)
        example_cube.move_to(LEFT * 2.2 + UP * 0.8)

        side_brace = Brace(example_cube, direction=DOWN, buff=0.08, color=COLOR_POS)
        side_label = side_brace.get_tex(r"2").set_color(COLOR_POS)
        side_label[0].scale(1.2)

        self.play(FadeIn(example_cube, scale=0.7), run_time=0.6)
        self.play(FadeIn(side_brace), Write(side_label), run_time=0.4)

        vol_text = MathTex(r"V = 2^3 = 8", font_size=34, color=COLOR_CUBE_POS)
        vol_text.next_to(example_cube, RIGHT, buff=0.4)
        self.play(Write(vol_text), run_time=0.5)

        # 推导箭头
        derive_arrow = Arrow(
            vol_text.get_bottom() + DOWN * 0.1,
            vol_text.get_bottom() + DOWN * 0.9,
            color=WHITE, buff=0.05, stroke_width=2,
            max_tip_length_to_length_ratio=0.25
        )
        result = MathTex(r"\sqrt[3]{8} = 2", font_size=40, color=COLOR_FORMULA)
        result.next_to(derive_arrow, DOWN, buff=0.1)
        result.align_to(vol_text, LEFT)

        self.play(Create(derive_arrow), run_time=0.3)
        self.play(Write(result), run_time=0.6)
        self.wait(0.5)

        # 一般公式 ³√(a³) = a
        gen_formula = MathTex(r"\sqrt[3]{a^3} = a", font_size=40, color=WHITE)
        gen_formula.move_to(DOWN * 2.5)
        box_gen = SurroundingRectangle(gen_formula, color=GOLD, buff=0.18, corner_radius=0.1)
        explain_gen = Text("互为逆运算", font=FONT, font_size=24, color=GOLD)
        explain_gen.next_to(box_gen, DOWN, buff=0.2)
        self.play(
            Write(gen_formula), Create(box_gen),
            run_time=0.6
        )
        self.play(FadeIn(explain_gen, shift=UP * 0.2), run_time=0.4)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            sec_title, eq1, explain1, symbol, box_sym,
            tip_3, arrow_3, example_cube, side_brace, side_label,
            vol_text, derive_arrow, result, gen_formula, box_gen, explain_gen
        )), run_time=0.5)

    # ──────────────────────────────────────────────
    # Scene 3  正 / 零 / 负 三种情况
    # ──────────────────────────────────────────────
    def scene_three_cases(self):
        sec_title = Text("立方根的三种情况", font=FONT, font_size=34, color=GOLD)
        sec_title.move_to(UP * 7.0)
        self.play(Write(sec_title), run_time=0.5)

        # ── 定义三列数据 ──
        cases = [
            # (被开方数, 立方根, 颜色, 列描述, cube_color)
            (r"a > 0", r"\sqrt[3]{8} = 2",  COLOR_POS,     "正数的立方根\n是正数", COLOR_CUBE_POS),
            (r"a = 0", r"\sqrt[3]{0} = 0",  COLOR_CUBE_ZRO,"零的立方根\n是零",    COLOR_CUBE_ZRO),
            (r"a < 0", r"\sqrt[3]{-8} = -2",COLOR_NEG,     "负数的立方根\n是负数", COLOR_CUBE_NEG),
        ]

        x_positions = [-3.0, 0.0, 3.0]
        all_col_mobs = VGroup()

        for (cond, formula, color, desc_str, cube_col), x in zip(cases, x_positions):
            # 条件标签
            cond_tex = MathTex(cond, font_size=28, color=color)
            cond_tex.move_to(UP * 5.8 + RIGHT * x)

            # 小正方体（等轴测，缩小）
            cube = make_cube_2d(1.0, color=cube_col, fill_opacity=0.32)
            cube.move_to(UP * 4.4 + RIGHT * x)

            # 公式
            f_tex = MathTex(formula, font_size=30, color=color)
            f_tex.move_to(UP * 2.9 + RIGHT * x)
            f_box = SurroundingRectangle(f_tex, color=color, buff=0.12, corner_radius=0.08)

            # 描述（用Text，不含LaTeX）
            desc_lines = desc_str.split("\n")
            desc_mobs = VGroup(*[
                Text(line, font=FONT, font_size=20, color=color)
                for line in desc_lines
            ]).arrange(DOWN, buff=0.08)
            desc_mobs.move_to(UP * 1.9 + RIGHT * x)

            col_group = VGroup(cond_tex, cube, f_tex, f_box, desc_mobs)
            all_col_mobs.add(col_group)

            self.play(
                FadeIn(cond_tex, shift=DOWN * 0.2),
                FadeIn(cube, scale=0.6),
                run_time=0.4
            )
            self.play(
                Write(f_tex), Create(f_box),
                FadeIn(desc_mobs),
                run_time=0.5
            )

        # ── 关键特性：唯一性 ──
        unique_line = Text("任何实数都有唯一的立方根！", font=FONT, font_size=28, color=YELLOW)
        unique_line.move_to(UP * 0.6)
        box_u = SurroundingRectangle(unique_line, color=YELLOW, buff=0.18, corner_radius=0.1)
        self.play(FadeIn(unique_line), Create(box_u), run_time=0.6)

        # ── 与平方根对比（简洁提示）──
        compare_hint = Text("不同于平方根，负数也可以开立方根！",
                            font=FONT, font_size=24, color=COLOR_COMPARE)
        compare_hint.move_to(DOWN * 0.5)
        self.play(FadeIn(compare_hint, shift=UP * 0.2), run_time=0.5)

        # 数轴上验证
        nl = NumberLine(
            x_range=[-4, 4, 1], length=7.5,
            include_numbers=True, include_tip=True,
            numbers_to_exclude=[],
            color=COLOR_AXIS, font_size=24,
            tip_width=0.18, tip_height=0.18,
        )
        nl.move_to(DOWN * 1.8)
        self.play(Create(nl), run_time=0.8)

        # 在数轴上标出 -2, 0, 2
        nl_points = [
            (-2, r"-2", COLOR_NEG, UP),
            (0,  r"0",  COLOR_CUBE_ZRO, UP),
            (2,  r"2",  COLOR_POS, UP),
        ]
        dots = VGroup()
        dot_labels = VGroup()
        for val, lbl, col, direction in nl_points:
            pt = nl.number_to_point(val)
            d = Dot(pt, radius=0.12, color=col)
            t = MathTex(lbl, font_size=28, color=col)
            t.next_to(d, direction, buff=0.3)
            dots.add(d)
            dot_labels.add(t)
            self.play(FadeIn(d, scale=0.5), FadeIn(t), run_time=0.3)

        note_nl = Text("立方根在数轴上均能找到对应点",
                       font=FONT, font_size=22, color=WHITE)
        note_nl.move_to(DOWN * 3.5)
        self.play(FadeIn(note_nl, shift=UP * 0.2), run_time=0.4)

        self.wait(1.5)
        self.play(FadeOut(VGroup(
            sec_title, all_col_mobs,
            unique_line, box_u, compare_hint,
            nl, dots, dot_labels, note_nl
        )), run_time=0.6)

    # ──────────────────────────────────────────────
    # Scene 4  计算练习
    # ──────────────────────────────────────────────
    def scene_practice(self):
        sec_title = Text("立方根计算练习", font=FONT, font_size=36, color=GOLD)
        sec_title.move_to(UP * 7.0)
        self.play(Write(sec_title), run_time=0.5)

        hint = Text("记住：先想 x³ = a，反推 x", font=FONT, font_size=26, color=WHITE)
        hint.move_to(UP * 6.0)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.4)

        # 例题数据
        examples = [
            # (问题, 思路文字, 答案, 颜色)
            (r"\sqrt[3]{27}",
             "因为  3³ = 27",
             r"= 3",
             COLOR_POS),
            (r"\sqrt[3]{-27}",
             "因为  (-3)³ = -27",
             r"= -3",
             COLOR_NEG),
            (r"\sqrt[3]{\dfrac{1}{8}}",
             r"因为  (½)³ = 1/8",
             r"= \dfrac{1}{2}",
             COLOR_POS),
            (r"\sqrt[3]{1000}",
             "因为  10³ = 1000",
             r"= 10",
             COLOR_POS),
        ]

        y_positions = [4.8, 3.0, 1.0, -1.0]
        all_ex_mobs = VGroup()

        for (problem, reasoning, answer, color), y in zip(examples, y_positions):
            # 序号圆圈
            circle = Circle(radius=0.22, fill_color=color, fill_opacity=0.9,
                            stroke_width=0)
            circle.move_to(LEFT * 3.8 + UP * y)

            # 问题
            prob_tex = MathTex(problem, font_size=38, color=WHITE)
            prob_tex.move_to(LEFT * 2.2 + UP * y)

            # 推理
            reason_text = Text(reasoning, font=FONT, font_size=20, color=GRAY_A)
            reason_text.move_to(UP * (y - 0.45))
            reason_text.align_to(prob_tex, LEFT)

            # 答案
            ans_tex = MathTex(answer, font_size=38, color=color)
            ans_tex.next_to(prob_tex, RIGHT, buff=0.2)

            # 连接等号
            eq_sign = MathTex(problem + answer, font_size=38, color=WHITE)
            # 直接将 problem + answer 合并显示
            full_eq = MathTex(problem + r"\;", answer, font_size=38)
            full_eq[0].set_color(WHITE)
            full_eq[1].set_color(color)
            full_eq.move_to(RIGHT * 0.0 + UP * y)

            # 分步动画
            self.play(FadeIn(circle), run_time=0.2)
            self.play(Write(full_eq[0]), run_time=0.4)
            self.play(FadeIn(reason_text, shift=UP * 0.1), run_time=0.3)
            self.play(Write(full_eq[1]), run_time=0.4)

            all_ex_mobs.add(circle, full_eq, reason_text)

        self.wait(1.2)
        self.play(FadeOut(VGroup(sec_title, hint, all_ex_mobs)), run_time=0.5)

    # ──────────────────────────────────────────────
    # Scene 5  与平方根对比
    # ──────────────────────────────────────────────
    def scene_comparison(self):
        sec_title = Text("立方根 vs 平方根", font=FONT, font_size=36, color=GOLD)
        sec_title.move_to(UP * 7.0)
        self.play(Write(sec_title), run_time=0.5)

        # ── 表头 ──
        header_left  = Text("对比项", font=FONT, font_size=26, color=WHITE)
        header_mid   = Text("平方根  √a", font=FONT, font_size=26, color=COLOR_COMPARE)
        header_right = Text("立方根  ³√a", font=FONT, font_size=26, color=COLOR_FORMULA)

        header_left.move_to(LEFT * 3.2  + UP * 6.0)
        header_mid.move_to(RIGHT * 0.3  + UP * 6.0)
        header_right.move_to(RIGHT * 3.2 + UP * 6.0)

        # 分隔线
        sep_h = Line(LEFT * 4.2 + UP * 5.55, RIGHT * 4.2 + UP * 5.55,
                     color=GRAY, stroke_width=1)
        sep_v1 = Line(LEFT * 1.8 + UP * 7.0, LEFT * 1.8 + DOWN * 1.5,
                      color=GRAY, stroke_width=1)
        sep_v2 = Line(RIGHT * 1.5 + UP * 7.0, RIGHT * 1.5 + DOWN * 1.5,
                      color=GRAY, stroke_width=1)

        self.play(
            FadeIn(header_left), FadeIn(header_mid), FadeIn(header_right),
            Create(sep_h), Create(sep_v1), Create(sep_v2),
            run_time=0.5
        )

        # ── 表格行数据 ──
        rows_data = [
            # (对比项, 平方根描述, 立方根描述, 平方根颜色, 立方根颜色)
            ("负数能开吗",
             "❌  不能",
             "✅  能",
             COLOR_NEG, COLOR_POS),
            ("结果唯一吗",
             "正数有 ±2 个",
             "唯一 1 个",
             YELLOW, COLOR_POS),
            ("关键公式",
             None,   # MathTex
             None,
             COLOR_COMPARE, COLOR_FORMULA),
        ]

        row_formulas = [
            None,
            None,
            (r"\sqrt{a^2} = |a|",  r"\sqrt[3]{a^3} = a"),
        ]

        y_start = 4.8
        all_rows = VGroup()

        for i, ((item, sq_desc, cb_desc, sq_color, cb_color), formulas) in enumerate(
                zip(rows_data, row_formulas)):
            y = y_start - i * 1.6

            item_text = Text(item, font=FONT, font_size=22, color=WHITE)
            item_text.move_to(LEFT * 3.2 + UP * y)

            if formulas is None:
                sq_mob = Text(sq_desc, font=FONT, font_size=22, color=sq_color)
                sq_mob.move_to(RIGHT * 0.3 + UP * y)
                cb_mob = Text(cb_desc, font=FONT, font_size=22, color=cb_color)
                cb_mob.move_to(RIGHT * 3.2 + UP * y)
            else:
                sq_mob = MathTex(formulas[0], font_size=26, color=sq_color)
                sq_mob.move_to(RIGHT * 0.3 + UP * y)
                cb_mob = MathTex(formulas[1], font_size=26, color=cb_color)
                cb_mob.move_to(RIGHT * 3.2 + UP * y)

            sep_row = Line(LEFT * 4.2 + UP * (y - 0.7), RIGHT * 4.2 + UP * (y - 0.7),
                           color=GRAY, stroke_width=0.8, stroke_opacity=0.5)

            self.play(
                FadeIn(item_text, shift=RIGHT * 0.2),
                FadeIn(sq_mob, shift=UP * 0.1),
                FadeIn(cb_mob, shift=UP * 0.1),
                Create(sep_row),
                run_time=0.55
            )
            all_rows.add(item_text, sq_mob, cb_mob, sep_row)

        # 重点高亮 — 负数可开立方根
        highlight_box = RoundedRectangle(
            width=3.2, height=0.65,
            corner_radius=0.12,
            color=COLOR_FORMULA, stroke_width=2,
            fill_color=COLOR_FORMULA, fill_opacity=0.15
        )
        highlight_box.move_to(RIGHT * 3.2 + UP * 4.8)
        self.play(Create(highlight_box), run_time=0.4)
        self.play(Flash(highlight_box, color=YELLOW, flash_radius=0.6), run_time=0.4)

        key_note = Text("立方根没有正负之分，结果唯一！",
                        font=FONT, font_size=24, color=YELLOW)
        key_note.move_to(DOWN * 1.8)
        box_kn = SurroundingRectangle(key_note, color=YELLOW, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(key_note), Create(box_kn), run_time=0.6)

        self.wait(1.5)
        self.play(FadeOut(VGroup(
            sec_title,
            header_left, header_mid, header_right,
            sep_h, sep_v1, sep_v2,
            all_rows, highlight_box,
            key_note, box_kn
        )), run_time=0.5)

    # ──────────────────────────────────────────────
    # Scene 6  总结 + 片尾
    # ──────────────────────────────────────────────
    def scene_outro(self):
        # 总结标题
        sum_title = Text("本节要点", font=FONT, font_size=36, color=GOLD)
        sum_title.move_to(UP * 7.0)
        self.play(Write(sum_title), run_time=0.4)

        points = [
            (r"x^3 = a \Rightarrow x = \sqrt[3]{a}", True,  COLOR_FORMULA),
            ("正数的立方根是正数",                     False, COLOR_POS),
            ("负数的立方根是负数",                     False, COLOR_NEG),
            ("零的立方根是零",                         False, COLOR_CUBE_ZRO),
            ("任何实数都有唯一的立方根",               False, YELLOW),
        ]

        y_start = 5.6
        point_mobs = VGroup()
        for i, (content, is_math, color) in enumerate(points):
            y = y_start - i * 1.1
            if is_math:
                bullet_content = MathTex(content, font_size=32, color=color)
            else:
                bullet_content = Text(content, font=FONT, font_size=26, color=color)
            bullet_content.move_to(UP * y + RIGHT * 0.4)
            bullet_content.align_to(LEFT * 0.2, LEFT)

            dot_bullet = Dot(radius=0.07, color=color)
            dot_bullet.next_to(bullet_content, LEFT, buff=0.2)

            grp = VGroup(dot_bullet, bullet_content)
            point_mobs.add(grp)
            self.play(FadeIn(grp, shift=RIGHT * 0.2), run_time=0.35)

        self.wait(1.5)
        self.play(FadeOut(VGroup(sum_title, point_mobs)), run_time=0.5)

        # ── 片尾关注 ──
        author_big = Text("上海初高中数学直通车", font=FONT, font_size=40, color=WHITE)
        author_big.move_to(UP * 2.0)
        author_id = Text("@emptyandcalm", font=FONT, font_size=30, color=COLOR_AUTHOR)
        author_id.next_to(author_big, DOWN, buff=0.3)

        self.play(
            Transform(self.author_obj, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = Text("关注我，获得更多数学技巧！", font=FONT, font_size=30, color=YELLOW)
        follow.move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰：三个旋转小正方体
        deco_cubes = VGroup()
        for i, (angle, x, size, col) in enumerate([
            (PI / 6,  -2.5, 0.5, COLOR_CUBE_POS),
            (PI / 4,   0.0, 0.6, COLOR_FORMULA),
            (PI / 3,   2.5, 0.5, COLOR_CUBE_NEG),
        ]):
            c = make_cube_2d(size, color=col, fill_opacity=0.5)
            c.move_to(DOWN * 2.2 + RIGHT * x)
            deco_cubes.add(c)

        self.play(*[FadeIn(c, scale=0.5) for c in deco_cubes], run_time=0.5)
        self.play(
            Rotate(deco_cubes[0], angle=PI / 12, about_point=deco_cubes[0].get_center()),
            Rotate(deco_cubes[2], angle=-PI / 12, about_point=deco_cubes[2].get_center()),
            run_time=0.8
        )

        # 公式展示
        finale_formula = MathTex(r"\sqrt[3]{a^3} = a", font_size=44, color=COLOR_FORMULA)
        finale_formula.move_to(DOWN * 3.8)
        self.play(Write(finale_formula), run_time=0.7)

        self.wait(2.0)
        self.play(FadeOut(VGroup(
            self.author_obj, author_id, follow,
            deco_cubes, finale_formula
        )), run_time=1.0)


# ============================================================
# 渲染命令:
#   manim -pql cube_root.py CubeRootConcept   # 快速预览 480p
#   manim -qh  cube_root.py CubeRootConcept   # 高质量 1080p
# ============================================================