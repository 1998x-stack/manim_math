"""
复数的概念 - Complex Numbers Teaching Animation
高二数学 · 第十三章 · 复数

TikTok 竖屏格式 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ═══ 全局配置 ═══
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ═══ 颜色常量 ═══
BG_COLOR   = "#1a1a2e"
C_REAL     = "#4fc3f7"   # 实部 - 亮蓝
C_IMAG     = "#ef5350"   # 虚部 - 红
C_I        = "#ffca28"   # 虚数单位 i - 橙黄
C_Z        = "#66bb6a"   # 复数 z - 绿
C_CONJ     = "#ce93d8"   # 共轭 - 紫
C_AXIS     = "#90caf9"   # 坐标轴 - 淡蓝
C_TITLE    = "#ffffff"
C_BODY     = "#cfd8dc"
C_ACCENT   = "#ffca28"
C_GRAY     = "#78909c"

FONT = "PingFang SC"


class ComplexNumbers(Scene):
    """
    复数的概念教学动画
    场景顺序:
      1. 开场钩子
      2. 虚数单位 i
      3. 复数定义 z = a + bi
      4. 复数分类
      5. 复数相等条件
      6. 复数平面（高斯平面）
      7. 共轭复数
      8. 片尾关注
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── 常驻作者信息 ──
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=C_GRAY
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        # ── 场景执行 ──
        self.scene1_hook()
        self.scene2_imaginary_unit()
        self.scene3_definition()
        self.scene4_classification()
        self.scene5_equality()
        self.scene6_complex_plane()
        self.scene7_conjugate()
        self.scene8_outro()

    # ═══════════════════════════════════════════
    # Scene 1: 开场钩子
    # ═══════════════════════════════════════════
    def scene1_hook(self):
        title = Text("你能解这个方程吗?", font=FONT, font_size=40, color=C_TITLE)
        title.move_to(UP * 5.5)

        eq = MathTex(r"x^2 + 1 = 0", font_size=72, color=C_ACCENT)
        eq.move_to(UP * 3.8)

        # 抛物线 y = x²+1（始终在x轴上方）
        axes = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[0, 7, 1],
            x_length=5.5, y_length=3.5,
            axis_config={"color": C_AXIS, "stroke_width": 2,
                         "include_ticks": False},
        ).move_to(UP * 1.2)

        parabola = axes.plot(lambda x: x**2 + 1, color=C_Z, stroke_width=3)
        x_axis_label = Text("x", font=FONT, font_size=20, color=C_AXIS).next_to(axes, RIGHT, buff=0.1)
        y_axis_label = Text("y", font=FONT, font_size=20, color=C_AXIS).next_to(axes, UP, buff=0.1)

        no_sol = Text("⚠ 与x轴无交点!", font=FONT, font_size=28, color=C_IMAG)
        no_sol.move_to(DOWN * 1.5)

        no_real = Text("∴ 在实数范围内无解!", font=FONT, font_size=26, color=C_BODY)
        no_real.move_to(DOWN * 2.5)

        self.play(Write(title), run_time=0.7)
        self.play(Write(eq), run_time=0.8)
        self.play(Create(axes), Write(x_axis_label), Write(y_axis_label), run_time=0.8)
        self.play(Create(parabola), run_time=1.0)
        self.play(FadeIn(no_sol, shift=UP * 0.3, scale=1.1), run_time=0.5)
        self.play(FadeIn(no_real), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(eq),
            FadeOut(axes), FadeOut(parabola),
            FadeOut(x_axis_label), FadeOut(y_axis_label),
            FadeOut(no_sol), FadeOut(no_real),
            run_time=0.5
        )

    # ═══════════════════════════════════════════
    # Scene 2: 虚数单位 i
    # ═══════════════════════════════════════════
    def scene2_imaginary_unit(self):
        intro = Text("数学家引入了新概念:", font=FONT, font_size=30, color=C_BODY)
        intro.move_to(UP * 5.5)

        # 虚数单位定义
        i_def_cn = Text("虚数单位", font=FONT, font_size=44, color=C_I)
        i_def_cn.move_to(UP * 4.2)

        i_def = MathTex(r"i^2 = -1", font_size=80, color=C_I)
        i_def.move_to(UP * 2.8)

        # 或等价地
        or_text = Text("即:", font=FONT, font_size=26, color=C_BODY)
        or_text.move_to(UP * 1.5)

        i_sqrt = MathTex(r"i = \sqrt{-1}", font_size=60, color=C_I)
        i_sqrt.move_to(UP * 0.4)

        # 幂次规律
        rule_title = Text("i 的幂次规律:", font=FONT, font_size=26, color=C_BODY)
        rule_title.move_to(DOWN * 1.0)

        powers = MathTex(
            r"i^1 = i \quad i^2 = -1 \quad i^3 = -i \quad i^4 = 1",
            font_size=32, color=C_TITLE
        )
        powers.move_to(DOWN * 2.0)

        cycle_text = Text("↻ 以4为周期循环", font=FONT, font_size=22, color=C_ACCENT)
        cycle_text.move_to(DOWN * 3.0)

        self.play(FadeIn(intro), run_time=0.5)
        self.play(Write(i_def_cn), run_time=0.6)
        self.play(Write(i_def), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(or_text), run_time=0.3)
        self.play(Write(i_sqrt), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(rule_title), run_time=0.4)
        self.play(Write(powers), run_time=0.8)
        self.play(FadeIn(cycle_text, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(intro), FadeOut(i_def_cn),
            FadeOut(i_def), FadeOut(or_text),
            FadeOut(i_sqrt), FadeOut(rule_title),
            FadeOut(powers), FadeOut(cycle_text),
            run_time=0.5
        )

    # ═══════════════════════════════════════════
    # Scene 3: 复数定义
    # ═══════════════════════════════════════════
    def scene3_definition(self):
        title = Text("复数的定义", font=FONT, font_size=40, color=C_TITLE)
        title.move_to(UP * 5.5)

        # 使用单个字符串，并确保 b 和 i 之间有空格（使其成为独立子对象）
        formula = MathTex(r"z = a + b i", font_size=88, color=C_TITLE)
        formula.move_to(UP * 3.8)

        # 获取各个组成部分
        a_part = formula.get_part_by_tex("a")          # 实部 a
        b_part = formula.get_part_by_tex("b")          # 虚部 b
        i_part = formula.get_part_by_tex("i")          # 虚数单位 i

        # 将虚数单位 i 设置为专用颜色（橙色）
        if i_part is not None:
            i_part.set_color(C_I)

        # 为实部 a 添加下方括号和标签
        a_brace = Brace(a_part, DOWN, color=C_REAL, buff=0.05)
        a_label = Text("实部", font=FONT, font_size=24, color=C_REAL)
        a_label_math = MathTex(r"\mathrm{Re}(z)=a", font_size=24, color=C_REAL)
        a_group = VGroup(a_label, a_label_math).arrange(DOWN, buff=0.05)
        a_brace.put_at_tip(a_group)

        # 为虚部 b 添加下方括号和标签
        b_brace = Brace(b_part, DOWN, color=C_IMAG, buff=0.05)
        b_label = Text("虚部", font=FONT, font_size=24, color=C_IMAG)
        b_label_math = MathTex(r"\mathrm{Im}(z)=b", font_size=24, color=C_IMAG)
        b_group = VGroup(b_label, b_label_math).arrange(DOWN, buff=0.05)
        b_brace.put_at_tip(b_group)

        # 条件说明
        cond = MathTex(
            r"a, b \in \mathbb{R}, \quad i^2 = -1",
            font_size=34, color=C_BODY
        )
        cond.move_to(UP * 0.5)

        # 数系包含关系
        set_text = Text("复数集 C ⊃ 实数集 R", font=FONT, font_size=26, color=C_ACCENT)
        set_text.move_to(DOWN * 0.8)

        # 动画播放
        self.play(Write(title), run_time=0.6)
        self.play(Write(formula), run_time=1.0)
        self.wait(0.3)

        # 高亮实部
        self.play(a_part.animate.set_color(C_REAL), run_time=0.4)
        self.play(GrowFromCenter(a_brace), FadeIn(a_group), run_time=0.6)
        self.wait(0.4)

        # 高亮虚部
        self.play(b_part.animate.set_color(C_IMAG), run_time=0.4)
        self.play(GrowFromCenter(b_brace), FadeIn(b_group), run_time=0.6)
        self.wait(0.4)

        # 显示条件和数系说明
        self.play(Write(cond), run_time=0.6)
        self.play(FadeIn(set_text, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理场景
        self.play(
            FadeOut(title), FadeOut(formula),
            FadeOut(a_brace), FadeOut(a_group),
            FadeOut(b_brace), FadeOut(b_group),
            FadeOut(cond), FadeOut(set_text),
            run_time=0.5
        )

    # ═══════════════════════════════════════════
    # Scene 4: 复数分类
    # ═══════════════════════════════════════════
    def scene4_classification(self):
        title = Text("复数的分类", font=FONT, font_size=40, color=C_TITLE)
        title.move_to(UP * 5.5)

        # 顶层公式
        z_top = MathTex(r"z = a + bi", font_size=44, color=C_Z)
        z_top.move_to(UP * 4.2)

        # 分支文字 ── 坐标精确布局
        branch_y = 2.8

        # b=0 分支 (左)
        cond_real = MathTex(r"b = 0", font_size=34, color=C_REAL)
        cond_real.move_to(np.array([-2.8, branch_y, 0]))

        arrow_real = Arrow(
            z_top.get_bottom() + DOWN * 0.05,
            cond_real.get_top() + UP * 0.05,
            color=C_REAL, buff=0.1, stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )

        label_real = Text("实数", font=FONT, font_size=30, color=C_REAL)
        label_real.move_to(np.array([-2.8, 1.8, 0]))

        ex_real = MathTex(r"3, \; -\frac{1}{2}, \; \pi", font_size=26, color=C_BODY)
        ex_real.move_to(np.array([-2.8, 1.0, 0]))

        # b≠0 分支 (右)
        cond_imag = MathTex(r"b \neq 0", font_size=34, color=C_IMAG)
        cond_imag.move_to(np.array([2.0, branch_y, 0]))

        arrow_imag = Arrow(
            z_top.get_bottom() + DOWN * 0.05,
            cond_imag.get_top() + UP * 0.05,
            color=C_IMAG, buff=0.1, stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )

        label_imag = Text("虚数", font=FONT, font_size=30, color=C_IMAG)
        label_imag.move_to(np.array([2.0, 1.8, 0]))

        ex_imag = MathTex(r"2 + 3i, \; -i", font_size=26, color=C_BODY)
        ex_imag.move_to(np.array([2.0, 1.0, 0]))

        # 纯虚数 (右下子分支)
        cond_pure = MathTex(r"a = 0,\; b \neq 0", font_size=28, color=C_I)
        cond_pure.move_to(np.array([2.0, -0.2, 0]))

        label_pure = Text("纯虚数", font=FONT, font_size=26, color=C_I)
        label_pure.move_to(np.array([2.0, -1.0, 0]))

        ex_pure = MathTex(r"5i, \; -3i", font_size=24, color=C_BODY)
        ex_pure.move_to(np.array([2.0, -1.7, 0]))

        arrow_pure = Arrow(
            label_imag.get_bottom() + DOWN * 0.05,
            cond_pure.get_top() + UP * 0.05,
            color=C_I, buff=0.05, stroke_width=2,
            max_tip_length_to_length_ratio=0.15
        )

        # 重点提示
        tip = Text("虚数 ⊃ 纯虚数", font=FONT, font_size=24, color=C_ACCENT)
        tip.move_to(DOWN * 2.8)

        self.play(Write(title), run_time=0.5)
        self.play(Write(z_top), run_time=0.6)

        # 左分支: 实数
        self.play(
            GrowArrow(arrow_real),
            FadeIn(cond_real),
            run_time=0.6
        )
        self.play(Write(label_real), Write(ex_real), run_time=0.5)

        # 右分支: 虚数
        self.play(
            GrowArrow(arrow_imag),
            FadeIn(cond_imag),
            run_time=0.6
        )
        self.play(Write(label_imag), Write(ex_imag), run_time=0.5)

        # 纯虚数子分支
        self.play(GrowArrow(arrow_pure), FadeIn(cond_pure), run_time=0.6)
        self.play(Write(label_pure), Write(ex_pure), run_time=0.5)

        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(z_top),
            FadeOut(arrow_real), FadeOut(cond_real),
            FadeOut(label_real), FadeOut(ex_real),
            FadeOut(arrow_imag), FadeOut(cond_imag),
            FadeOut(label_imag), FadeOut(ex_imag),
            FadeOut(arrow_pure), FadeOut(cond_pure),
            FadeOut(label_pure), FadeOut(ex_pure),
            FadeOut(tip),
            run_time=0.5
        )

    # ═══════════════════════════════════════════
    # Scene 5: 复数相等条件
    # ═══════════════════════════════════════════
    def scene5_equality(self):
        title = Text("复数相等的条件", font=FONT, font_size=38, color=C_TITLE)
        title.move_to(UP * 5.5)

        q = Text("什么时候两个复数相等?", font=FONT, font_size=30, color=C_BODY)
        q.move_to(UP * 4.2)

        # 条件公式
        iff = MathTex(
            r"a + bi = c + di",
            font_size=56, color=C_TITLE
        )
        iff.move_to(UP * 2.8)

        iff_arrow = MathTex(r"\Longleftrightarrow", font_size=56, color=C_ACCENT)
        iff_arrow.move_to(UP * 1.5)

        cond1 = MathTex(r"a = c", font_size=52, color=C_REAL)
        cond1.move_to(np.array([-1.8, 0.2, 0]))

        and_text = Text("且", font=FONT, font_size=36, color=C_BODY)
        and_text.move_to(np.array([0, 0.2, 0]))

        cond2 = MathTex(r"b = d", font_size=52, color=C_IMAG)
        cond2.move_to(np.array([1.8, 0.2, 0]))

        # 解释
        exp1 = Text("实部相等", font=FONT, font_size=26, color=C_REAL)
        exp1.move_to(np.array([-1.8, -0.9, 0]))

        exp2 = Text("虚部相等", font=FONT, font_size=26, color=C_IMAG)
        exp2.move_to(np.array([1.8, -0.9, 0]))

        # 示例
        example_title = Text("例:", font=FONT, font_size=28, color=C_BODY)
        example_title.move_to(np.array([-3.5, -2.0, 0]))

        example = MathTex(
            r"(2x+1) + 3i = 5 + (y-1)i",
            font_size=34, color=C_BODY
        )
        example.move_to(UP * (-2.0))

        sol_title = Text("解:", font=FONT, font_size=24, color=C_ACCENT)
        sol_title.move_to(np.array([-3.5, -3.1, 0]))

        sol = MathTex(
            r"2x+1 = 5 \Rightarrow x=2 \quad \text{and} \quad y-1=3 \Rightarrow y=4",
            font_size=26, color=C_ACCENT
        )
        sol.move_to(DOWN * 3.1)

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(q), run_time=0.4)
        self.play(Write(iff), run_time=0.7)
        self.play(Write(iff_arrow), run_time=0.4)
        self.play(
            Write(cond1), Write(and_text), Write(cond2),
            run_time=0.7
        )
        self.play(FadeIn(exp1), FadeIn(exp2), run_time=0.4)
        self.wait(0.8)

        self.play(FadeIn(example_title), Write(example), run_time=0.7)
        self.play(FadeIn(sol_title), Write(sol), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(q),
            FadeOut(iff), FadeOut(iff_arrow),
            FadeOut(cond1), FadeOut(and_text), FadeOut(cond2),
            FadeOut(exp1), FadeOut(exp2),
            FadeOut(example_title), FadeOut(example),
            FadeOut(sol_title), FadeOut(sol),
            run_time=0.5
        )

    # ═══════════════════════════════════════════
    # Scene 6: 复数平面（高斯平面）
    # ═══════════════════════════════════════════
    def scene6_complex_plane(self):
        title = Text("复数平面（高斯平面）", font=FONT, font_size=36, color=C_TITLE)
        title.move_to(UP * 5.5)

        subtitle = Text("每个复数对应平面上唯一一点", font=FONT, font_size=24, color=C_BODY)
        subtitle.move_to(UP * 4.7)

        # ── 坐标轴（放置在中部） ──
        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-3.5, 3.5, 1],
            x_length=6.0, y_length=6.0,
            axis_config={
                "color": C_AXIS, "stroke_width": 2,
                "include_tip": True,
                "tip_width": 0.15, "tip_height": 0.15,
                "include_ticks": True,
            },
        ).move_to(UP * 1.0)

        # 轴标签
        x_label = Text("实轴", font=FONT, font_size=22, color=C_REAL)
        x_label.next_to(axes.x_axis.get_right(), RIGHT, buff=0.1)

        y_label = Text("虚轴", font=FONT, font_size=22, color=C_IMAG)
        y_label.next_to(axes.y_axis.get_top(), UP, buff=0.05)

        o_label = MathTex("O", font_size=22, color=C_AXIS)
        o_label.next_to(axes.get_origin(), DL, buff=0.1)

        # ── 示例点 z = 3 + 2i ──
        z_val = np.array([3.0, 2.0])  # 实部3, 虚部2
        z_pos = axes.c2p(z_val[0], z_val[1])

        z_dot = Dot(z_pos, color=C_Z, radius=0.12)
        z_label = MathTex(r"z = 3+2i", font_size=28, color=C_Z)
        z_label.next_to(z_dot, UR, buff=0.15)

        # 从原点到z的向量（箭头）
        origin_pos = axes.c2p(0, 0)
        z_arrow = Arrow(
            origin_pos, z_pos,
            color=C_Z, buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.12
        )

        # 辅助虚线（投影到实轴和虚轴）
        proj_x_pos = axes.c2p(z_val[0], 0)
        proj_y_pos = axes.c2p(0, z_val[1])

        proj_to_x = DashedLine(z_pos, proj_x_pos, color=C_REAL, dash_length=0.08, stroke_width=1.5)
        proj_to_y = DashedLine(z_pos, proj_y_pos, color=C_IMAG, dash_length=0.08, stroke_width=1.5)

        # 实部虚部标注
        real_brace = BraceBetweenPoints(
            axes.c2p(0, 0), axes.c2p(z_val[0], 0),
            direction=DOWN, color=C_REAL
        )
        real_brace_label = MathTex(r"a=3", font_size=22, color=C_REAL)
        real_brace.put_at_tip(real_brace_label)

        imag_brace = BraceBetweenPoints(
            axes.c2p(0, 0), axes.c2p(0, z_val[1]),
            direction=LEFT, color=C_IMAG
        )
        imag_brace_label = MathTex(r"b=2", font_size=22, color=C_IMAG)
        imag_brace.put_at_tip(imag_brace_label)

        # 底部说明
        note = Text("z = 3+2i  对应点  (3, 2)", font=FONT, font_size=24, color=C_BODY)
        note.move_to(DOWN * 3.8)

        # ── 动画 ──
        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(subtitle), run_time=0.4)
        self.play(Create(axes), Write(x_label), Write(y_label), Write(o_label), run_time=1.0)
        self.wait(0.3)

        self.play(FadeIn(z_dot, scale=0.5), run_time=0.4)
        self.play(GrowArrow(z_arrow), run_time=0.7)
        self.play(Write(z_label), run_time=0.5)

        self.play(Create(proj_to_x), Create(proj_to_y), run_time=0.6)
        self.play(
            GrowFromCenter(real_brace), FadeIn(real_brace_label),
            GrowFromCenter(imag_brace), FadeIn(imag_brace_label),
            run_time=0.7
        )

        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)

        # 保留坐标轴供下一场景使用
        self.axes_obj = axes
        self.axes_x_label = x_label
        self.axes_y_label = y_label
        self.axes_o_label = o_label

        self.play(
            FadeOut(subtitle),
            FadeOut(z_dot), FadeOut(z_arrow), FadeOut(z_label),
            FadeOut(proj_to_x), FadeOut(proj_to_y),
            FadeOut(real_brace), FadeOut(real_brace_label),
            FadeOut(imag_brace), FadeOut(imag_brace_label),
            FadeOut(note),
            run_time=0.5
        )
        # 保留 title 和 axes 给下一场景
        self.scene6_title = title

    # ═══════════════════════════════════════════
    # Scene 7: 共轭复数
    # ═══════════════════════════════════════════
    def scene7_conjugate(self):
        axes = self.axes_obj
        title = self.scene6_title

        # 更新标题
        new_title = Text("共轭复数", font=FONT, font_size=40, color=C_TITLE)
        new_title.move_to(UP * 5.5)
        self.play(Transform(title, new_title), run_time=0.4)

        origin_pos = axes.c2p(0, 0)

        # z = 3 + 2i
        z_val = np.array([3.0, 2.0])
        z_pos = axes.c2p(z_val[0], z_val[1])
        z_dot = Dot(z_pos, color=C_Z, radius=0.12)
        z_arrow = Arrow(origin_pos, z_pos, color=C_Z, buff=0,
                        stroke_width=3, max_tip_length_to_length_ratio=0.12)
        z_label = MathTex(r"z = 3+2i", font_size=30, color=C_Z)
        z_label.next_to(z_dot, UR, buff=0.15)

        # z̄ = 3 - 2i (关于实轴对称)
        zbar_val = np.array([3.0, -2.0])
        zbar_pos = axes.c2p(zbar_val[0], zbar_val[1])
        zbar_dot = Dot(zbar_pos, color=C_CONJ, radius=0.12)
        zbar_arrow = Arrow(origin_pos, zbar_pos, color=C_CONJ, buff=0,
                           stroke_width=3, max_tip_length_to_length_ratio=0.12)
        zbar_label = MathTex(r"\bar{z} = 3-2i", font_size=30, color=C_CONJ)
        zbar_label.next_to(zbar_dot, DR, buff=0.15)

        # 对称轴标注（实轴上的双箭头）
        sym_line = DashedLine(z_pos, zbar_pos, color=C_ACCENT, dash_length=0.1, stroke_width=2)
        sym_label = Text("关于实轴对称", font=FONT, font_size=22, color=C_ACCENT)
        sym_label.next_to(sym_line, RIGHT, buff=0.2)

        # 定义框
        def_box = MathTex(
            r"\bar{z} = a - bi",
            font_size=44, color=C_CONJ
        )
        def_box.move_to(DOWN * 3.6)

        def_note = Text("z 与 z̄ 互为共轭复数", font=FONT, font_size=24, color=C_BODY)
        def_note.move_to(DOWN * 4.5)

        # 性质
        prop = MathTex(r"z \cdot \bar{z} = a^2 + b^2", font_size=32, color=C_BODY)
        prop.move_to(DOWN * 5.3)

        # 动画
        self.play(FadeIn(z_dot, scale=0.5), GrowArrow(z_arrow), Write(z_label), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(zbar_dot, scale=0.5), GrowArrow(zbar_arrow), Write(zbar_label), run_time=0.7)
        self.play(Create(sym_line), FadeIn(sym_label), run_time=0.6)
        self.wait(0.4)
        self.play(Write(def_box), run_time=0.6)
        self.play(FadeIn(def_note), run_time=0.4)
        self.play(Write(prop), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(self.axes_x_label), FadeOut(self.axes_y_label), FadeOut(self.axes_o_label),
            FadeOut(z_dot), FadeOut(z_arrow), FadeOut(z_label),
            FadeOut(zbar_dot), FadeOut(zbar_arrow), FadeOut(zbar_label),
            FadeOut(sym_line), FadeOut(sym_label),
            FadeOut(def_box), FadeOut(def_note), FadeOut(prop),
            run_time=0.6
        )

    # ═══════════════════════════════════════════
    # Scene 8: 片尾关注
    # ═══════════════════════════════════════════
    def scene8_outro(self):
        # 总结复数公式
        summary_title = Text("复数核心公式", font=FONT, font_size=36, color=C_ACCENT)
        summary_title.move_to(UP * 5.0)

        formulas = VGroup(
            MathTex(r"z = a + bi \quad (a,b \in \mathbb{R},\; i^2=-1)", font_size=34, color=C_TITLE),
            MathTex(r"\mathrm{Re}(z)=a, \quad \mathrm{Im}(z)=b", font_size=30, color=C_BODY),
            MathTex(r"\bar{z} = a - bi", font_size=30, color=C_CONJ),
            MathTex(r"z\bar{z} = a^2 + b^2", font_size=30, color=C_BODY),
        ).arrange(DOWN, buff=0.45)
        formulas.move_to(UP * 2.5)

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=36, color=C_TITLE
        ).move_to(DOWN * 1.0)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=C_GRAY
        ).move_to(DOWN * 1.9)

        follow_text = Text(
            "关注我，学更多高中数学!",
            font=FONT, font_size=30, color=C_ACCENT
        ).move_to(DOWN * 3.2)

        self.play(Write(summary_title), run_time=0.5)
        for f in formulas:
            self.play(Write(f), run_time=0.5)
        self.wait(0.5)

        self.play(
            Transform(self.author, author_big),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(follow_text, scale=1.05), run_time=0.5)

        # 装饰性闪烁
        stars = VGroup(*[
            MathTex(r"i", font_size=28, color=C_I)
            .move_to(np.array([
                2.5 * np.cos(k * TAU / 5),
                2.5 * np.sin(k * TAU / 5) - 4.5,
                0
            ]))
            for k in range(5)
        ])
        self.play(*[FadeIn(s, scale=0.5) for s in stars], run_time=0.5)
        self.play(*[s.animate.set_color(C_ACCENT) for s in stars], run_time=0.5)
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)

# manim -pql complex_numbers.py ComplexNumbers   # 快速预览
# manim -qh  complex_numbers.py ComplexNumbers   # 高质量输出