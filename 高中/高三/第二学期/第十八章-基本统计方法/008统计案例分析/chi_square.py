"""
独立性检验（卡方检验）教学动画
Chi-Square Independence Test - Teaching Animation

格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
知识点: 高三统计 - 独立性检验
案例: 吸烟与肺癌是否相关？

验证数据 (已通过 verify_chi2.py):
  a=43, b=162, c=5, d=192, n=402
  χ² ≈ 32.48  >> 6.635
  结论: 吸烟与肺癌在0.01水平下显著相关
"""

from manim import *
import numpy as np

# ============================================================
# 全局配置 - TikTok 竖屏
# ============================================================
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ============================================================
# 颜色常量
# ============================================================
BG_COLOR       = "#1a1a2e"
COLOR_CELL_A   = "#e74c3c"   # 红  - 吸烟&患癌
COLOR_CELL_B   = "#3498db"   # 蓝  - 吸烟&未患癌
COLOR_CELL_C   = "#2ecc71"   # 绿  - 不吸烟&患癌
COLOR_CELL_D   = "#f39c12"   # 橙  - 不吸烟&未患癌
COLOR_CHI      = "#9b59b6"   # 紫  - χ²统计量
COLOR_CRIT     = "#e67e22"   # 橙红 - 临界值
COLOR_REJECT   = "#e74c3c"   # 红  - 拒绝域
COLOR_ACCEPT   = "#2ecc71"   # 绿  - 接受域
COLOR_HEADER   = "#bdc3c7"   # 浅灰 - 表头
FONT_CN        = "Noto Sans CJK SC"

# 数据 (已验证)
A_VAL, B_VAL, C_VAL, D_VAL = 43, 162, 5, 192
N_VAL    = A_VAL + B_VAL + C_VAL + D_VAL  # 402
CHI2_VAL = 32.48
CRIT_005 = 3.841
CRIT_001 = 6.635


# ============================================================
# 辅助：创建表格
# ============================================================
def build_contingency_table(scale=0.85):
    """
    手动构建 2×2 列联表 (3行4列含标题)
    返回 VGroup，包含所有格子和文字
    """
    # 列宽/行高
    col_widths  = [2.2, 1.7, 1.7, 1.7]   # 行标题列 + 3数据列
    row_heights = [0.75, 0.75, 0.75, 0.75]  # 列标题行 + 3数据行

    total_w = sum(col_widths)
    total_h = sum(row_heights)

    cells_group = VGroup()
    texts_group = VGroup()

    # 单元格内容: [行][列]
    contents = [
        ["",          "患肺癌",  "未患肺癌",  "合计"],
        ["吸烟",      "43",      "162",       "205"],
        ["不吸烟",    "5",       "192",       "197"],
        ["合计",      "48",      "354",       "402"],
    ]

    # 单元格颜色 (行,列)
    data_colors = {
        (1, 1): COLOR_CELL_A,
        (1, 2): COLOR_CELL_B,
        (2, 1): COLOR_CELL_C,
        (2, 2): COLOR_CELL_D,
    }

    # 行标题列颜色
    row_header_colors = {
        (1, 0): COLOR_CELL_A,  # 吸烟
        (2, 0): COLOR_CELL_C,  # 不吸烟
    }

    # 从左上角开始摆放
    y_start = total_h / 2
    x_start = -total_w / 2

    accumulated_y = y_start
    for r, rh in enumerate(row_heights):
        accumulated_x = x_start
        for c, cw in enumerate(col_widths):
            # 格子中心
            cx = accumulated_x + cw / 2
            cy = accumulated_y - rh / 2

            # 背景色
            fill_col = DARK_BLUE
            fill_opacity = 0.0

            if r == 0 or c == 0:
                fill_col    = "#2c3e50"
                fill_opacity = 0.8
            if (r, c) in data_colors:
                fill_col    = data_colors[(r, c)]
                fill_opacity = 0.15
            if (r, c) in row_header_colors:
                fill_col    = row_header_colors[(r, c)]
                fill_opacity = 0.25

            rect = Rectangle(
                width=cw, height=rh,
                color=COLOR_HEADER,
                fill_color=fill_col,
                fill_opacity=fill_opacity,
                stroke_width=1.5
            ).move_to([cx, cy, 0])
            cells_group.add(rect)

            # 文字
            text_content = contents[r][c]
            if text_content:
                # 数字用白色, 标题用灰白
                if r == 0 or c == 0:
                    txt_color = COLOR_HEADER
                    fs = 22
                elif (r, c) in data_colors:
                    txt_color = data_colors[(r, c)]
                    fs = 26
                else:
                    txt_color = WHITE
                    fs = 22

                t = Text(
                    text_content,
                    font=FONT_CN,
                    font_size=fs,
                    color=txt_color
                ).move_to([cx, cy, 0])
                texts_group.add(t)

            accumulated_x += cw
        accumulated_y -= rh

    table_group = VGroup(cells_group, texts_group)
    table_group.scale(scale)
    return table_group, cells_group, texts_group


# ============================================================
# 主场景
# ============================================================
class ChiSquareScene(Scene):
    """独立性检验（卡方检验）完整教学动画"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_data()

        self.scene_1_opening()
        self.scene_2_contingency_table()
        self.scene_3_hypothesis_idea()
        self.scene_4_chi2_formula()
        self.scene_5_calculation()
        self.scene_6_critical_value()
        self.scene_7_conclusion()
        self.scene_8_outro()

    # --------------------------------------------------------
    def setup_data(self):
        """统一存储所有数据（已由verify_chi2.py验证）"""
        self.a, self.b = A_VAL, B_VAL
        self.c, self.d = C_VAL, D_VAL
        self.n         = N_VAL
        self.chi2      = CHI2_VAL
        self.crit_005  = CRIT_005
        self.crit_001  = CRIT_001

        # 派生
        self.row1 = self.a + self.b   # 205
        self.row2 = self.c + self.d   # 197
        self.col1 = self.a + self.c   # 48
        self.col2 = self.b + self.d   # 354
        self.ad_minus_bc = self.a * self.d - self.b * self.c  # 7446

        # 验证
        assert self.row1 + self.row2 == self.n
        assert self.col1 + self.col2 == self.n

    # --------------------------------------------------------
    # Scene 1: 开场钩子
    # --------------------------------------------------------
    def scene_1_opening(self):
        # 作者信息
        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT_CN, font_size=18, color=GRAY_B
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.3)

        # 主钩子
        hook = Text(
            "吸烟真的会\n导致肺癌吗？",
            font=FONT_CN, font_size=52, color=YELLOW,
            line_spacing=1.2
        ).move_to(UP * 5.2)
        self.play(Write(hook), run_time=1.0)

        sub = Text(
            "用数学来检验！",
            font=FONT_CN, font_size=34, color=WHITE
        ).move_to(UP * 3.5)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=0.5)

        # 两个图标：吸烟 vs 不吸烟（用圆圈+文字简化）
        icon_smoke = self._make_icon("吸烟者", "200人", COLOR_CELL_A, LEFT * 2.0 + UP * 1.5)
        icon_none  = self._make_icon("不吸烟者", "197人", COLOR_CELL_C, RIGHT * 2.0 + UP * 1.5)
        self.play(FadeIn(icon_smoke), FadeIn(icon_none), run_time=0.6)

        # 问号箭头
        q_arrow = Arrow(
            icon_smoke.get_right() + RIGHT * 0.1,
            icon_none.get_left()   + LEFT * 0.1,
            color=YELLOW, stroke_width=3, buff=0.05
        )
        q_text = Text("相关？", font=FONT_CN, font_size=28, color=YELLOW
                      ).next_to(q_arrow, UP, buff=0.15)
        self.play(GrowArrow(q_arrow), FadeIn(q_text), run_time=0.6)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(hook), FadeOut(sub),
            FadeOut(icon_smoke), FadeOut(icon_none),
            FadeOut(q_arrow), FadeOut(q_text),
            run_time=0.4
        )

    def _make_icon(self, label, count, color, pos):
        circle = Circle(radius=0.55, color=color,
                        fill_color=color, fill_opacity=0.15, stroke_width=2)
        t1 = Text(label, font=FONT_CN, font_size=20, color=color)
        t2 = Text(count,  font=FONT_CN, font_size=18, color=WHITE)
        inner = VGroup(t1, t2).arrange(DOWN, buff=0.08)
        group = VGroup(circle, inner).move_to(pos)
        return group

    # --------------------------------------------------------
    # Scene 2: 列联表
    # --------------------------------------------------------
    def scene_2_contingency_table(self):
        title = Text("2×2 列联表", font=FONT_CN, font_size=40, color=YELLOW
                     ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        subtitle = Text("整理调查数据", font=FONT_CN, font_size=26, color=GRAY_A
                        ).move_to(UP * 5.4)
        self.play(FadeIn(subtitle), run_time=0.3)

        # 构建列联表
        self.table_group, cells_g, texts_g = build_contingency_table(scale=0.92)
        self.table_group.move_to(UP * 2.8)

        # 先画框架
        self.play(Create(cells_g), run_time=0.8)
        # 再逐一写入文字
        for t in texts_g:
            self.play(FadeIn(t, scale=0.8), run_time=0.12)

        self.wait(0.4)

        # 数据含义说明
        explain = VGroup(
            self._explain_row("a = 43", "吸烟者中患肺癌人数", COLOR_CELL_A),
            self._explain_row("b = 162", "吸烟者中未患肺癌人数", COLOR_CELL_B),
            self._explain_row("c = 5",   "不吸烟者中患肺癌人数", COLOR_CELL_C),
            self._explain_row("d = 192", "不吸烟者中未患肺癌人数", COLOR_CELL_D),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to(DOWN * 1.5)

        for row in explain:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.25)

        # 总人数
        n_label = Text("共调查 402 人", font=FONT_CN, font_size=26, color=WHITE
                       ).move_to(DOWN * 4.2)
        self.play(FadeIn(n_label), run_time=0.4)
        self.wait(1.0)

        # 清理说明文字，保留列联表
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(explain), FadeOut(n_label),
            run_time=0.5
        )
        # 列联表移到顶部小一点
        self.play(
            self.table_group.animate.scale(0.78).move_to(UP * 5.0),
            run_time=0.6
        )

    def _explain_row(self, formula, desc, color):
        f = Text(formula, font=FONT_CN, font_size=22, color=color)
        d = Text(desc,    font=FONT_CN, font_size=20, color=GRAY_A)
        return VGroup(f, d).arrange(RIGHT, buff=0.3)

    # --------------------------------------------------------
    # Scene 3: 假设检验思想
    # --------------------------------------------------------
    def scene_3_hypothesis_idea(self):
        title = Text("独立性检验的思路", font=FONT_CN, font_size=36, color=YELLOW
                     ).move_to(UP * 3.2)
        self.play(Write(title), run_time=0.7)

        steps = [
            ("①", "提出假设 H₀", "假设吸烟与肺癌无关（独立）", WHITE),
            ("②", "计算统计量", "由数据算出 χ² 值", WHITE),
            ("③", "对比临界值", "与显著性水平对应的临界值比较", WHITE),
            ("④", "得出结论",   "χ² 越大 → 越可能相关", YELLOW),
        ]

        step_group = VGroup()
        y_pos = 2.2
        arrows = VGroup()

        for num, step_title, step_desc, color in steps:
            num_t  = Text(num,        font=FONT_CN, font_size=28, color=color)
            name_t = Text(step_title, font=FONT_CN, font_size=26, color=color)
            desc_t = Text(step_desc,  font=FONT_CN, font_size=20, color=GRAY_A)

            row = VGroup(
                VGroup(num_t, name_t).arrange(RIGHT, buff=0.25),
                desc_t
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            row.move_to(UP * y_pos + LEFT * 0.3)
            step_group.add(row)
            y_pos -= 1.6

        # 添加步骤间箭头
        for i in range(len(steps) - 1):
            arr = Arrow(
                step_group[i].get_bottom() + DOWN * 0.05,
                step_group[i + 1].get_top() + UP * 0.05,
                color=GRAY_B, stroke_width=2, max_tip_length_to_length_ratio=0.2,
                buff=0.05
            )
            arrows.add(arr)

        for i, row in enumerate(step_group):
            self.play(FadeIn(row, shift=RIGHT * 0.4), run_time=0.4)
            if i < len(steps) - 1:
                self.play(GrowArrow(arrows[i]), run_time=0.25)

        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(step_group), FadeOut(arrows),
            run_time=0.5
        )

    # --------------------------------------------------------
    # Scene 4: χ² 公式与字母对应
    # --------------------------------------------------------
    def scene_4_chi2_formula(self):
        title = Text("χ² 计算公式", font=FONT_CN, font_size=38, color=YELLOW
                     ).move_to(UP * 3.5)
        self.play(Write(title), run_time=0.6)

        # 主公式
        formula = MathTex(
            r"\chi^2 = \frac{n(ad-bc)^2}{(a+b)(c+d)(a+c)(b+d)}",
            font_size=38, color=WHITE
        ).move_to(UP * 2.2)
        self.play(Write(formula), run_time=1.2)
        self.wait(0.4)

        # 字母含义说明（颜色对应列联表）
        legend_items = [
            (r"a", "= 吸烟 & 患肺癌  = 43",   COLOR_CELL_A),
            (r"b", "= 吸烟 & 未患肺癌 = 162",  COLOR_CELL_B),
            (r"c", "= 不吸 & 患肺癌  = 5",     COLOR_CELL_C),
            (r"d", "= 不吸 & 未患肺癌 = 192",  COLOR_CELL_D),
            (r"n", "= 总人数 = 402",            WHITE),
        ]

        legend_rows = VGroup()
        for letter, desc, color in legend_items:
            lt = MathTex(letter, font_size=26, color=color)
            dt = Text(desc, font=FONT_CN, font_size=21, color=color)
            row = VGroup(lt, dt).arrange(RIGHT, buff=0.25)
            legend_rows.add(row)

        legend_rows.arrange(DOWN, buff=0.28, aligned_edge=LEFT
                            ).move_to(DOWN * 0.3 + LEFT * 0.5)

        sep = Line(LEFT * 3.5, RIGHT * 3.5, stroke_width=1, color=GRAY_B
                   ).next_to(formula, DOWN, buff=0.3)
        self.play(Create(sep), run_time=0.3)

        for row in legend_rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.22)

        self.wait(1.0)

        # 高亮公式中的 a, b, c, d 与列联表颜色联动
        highlight_rects = VGroup(
            SurroundingRectangle(formula[0][5],  color=COLOR_CELL_A, buff=0.05),  # a
            SurroundingRectangle(formula[0][7],  color=COLOR_CELL_D, buff=0.05),  # d
            SurroundingRectangle(formula[0][9],  color=COLOR_CELL_B, buff=0.05),  # b
            SurroundingRectangle(formula[0][11], color=COLOR_CELL_C, buff=0.05),  # c
        )
        self.play(*[Create(r) for r in highlight_rects], run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(sep),
            FadeOut(legend_rows), FadeOut(highlight_rects),
            run_time=0.4
        )
        # 保留公式供下一场景用
        self.formula_main = formula
        self.play(
            self.formula_main.animate.scale(0.75).move_to(UP * 2.7),
            run_time=0.4
        )

    # --------------------------------------------------------
    # Scene 5: 代入数据计算
    # --------------------------------------------------------
    def scene_5_calculation(self):
        title = Text("代入数据，计算 χ²",
                     font=FONT_CN, font_size=34, color=YELLOW).move_to(UP * 1.8)
        self.play(Write(title), run_time=0.6)

        # Step 1: ad - bc
        step1_label = Text("① 计算 ad - bc",
                           font=FONT_CN, font_size=24, color=COLOR_CELL_A).move_to(UP * 0.9 + LEFT * 1.0)
        step1 = MathTex(
            r"ad - bc = 43 \times 192 - 162 \times 5",
            font_size=28, color=WHITE
        ).move_to(UP * 0.2)
        step1b = MathTex(
            r"= 8256 - 810 = 7446",
            font_size=30, color=COLOR_CELL_A
        ).next_to(step1, DOWN, buff=0.25)

        self.play(FadeIn(step1_label), run_time=0.3)
        self.play(Write(step1), run_time=0.7)
        self.play(Write(step1b), run_time=0.5)
        self.wait(0.3)

        # Step 2: 分母
        step2_label = Text("② 计算分母",
                           font=FONT_CN, font_size=24, color=GRAY_A
                           ).next_to(step1b, DOWN, buff=0.45).shift(LEFT * 1.5)
        step2 = MathTex(
            r"205 \times 197 \times 48 \times 354 \approx 6.86 \times 10^8",
            font_size=26, color=GRAY_A
        ).next_to(step2_label, DOWN, buff=0.25)

        self.play(FadeIn(step2_label), Write(step2), run_time=0.7)

        # Step 3: χ²
        step3_label = Text("③ 代入公式",
                           font=FONT_CN, font_size=24, color=COLOR_CHI
                           ).next_to(step2, DOWN, buff=0.45).shift(LEFT * 1.5)
        step3 = MathTex(
            r"\chi^2 = \frac{402 \times 7446^2}{6.86 \times 10^8}",
            font_size=32, color=WHITE
        ).next_to(step3_label, DOWN, buff=0.28)
        step3b = MathTex(
            r"\approx 32.48",
            font_size=42, color=COLOR_CHI
        ).next_to(step3, DOWN, buff=0.3)

        self.play(FadeIn(step3_label), Write(step3), run_time=0.8)
        self.play(Write(step3b), run_time=0.6)

        # 结果高亮框
        result_box = SurroundingRectangle(
            step3b, color=COLOR_CHI, buff=0.18, corner_radius=0.12
        )
        self.play(Create(result_box), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(title),
            FadeOut(step1_label), FadeOut(step1), FadeOut(step1b),
            FadeOut(step2_label), FadeOut(step2),
            FadeOut(step3_label), FadeOut(step3),
            FadeOut(self.formula_main),
            FadeOut(result_box),
            run_time=0.5
        )

        # 将χ²结果移到顶部常驻
        self.chi2_display = MathTex(
            r"\chi^2 \approx 32.48",
            font_size=34, color=COLOR_CHI
        ).move_to(UP * 2.0)
        self.play(ReplacementTransform(step3b, self.chi2_display), run_time=0.5)

    # --------------------------------------------------------
    # Scene 6: 临界值比较（数轴可视化）
    # --------------------------------------------------------
    def scene_6_critical_value(self):
        title = Text("与临界值比较", font=FONT_CN, font_size=36, color=YELLOW
                     ).move_to(UP * 0.9)
        self.play(Write(title), run_time=0.6)

        # 临界值表格
        crit_info = VGroup(
            self._crit_row("P(χ² ≥ 3.841) ≈ 0.05", "α=0.05 临界值: 3.841", COLOR_CRIT),
            self._crit_row("P(χ² ≥ 6.635) ≈ 0.01", "α=0.01 临界值: 6.635", RED),
        ).arrange(DOWN, buff=0.3).move_to(UP * 0.0)

        self.play(*[FadeIn(r, shift=RIGHT * 0.3) for r in crit_info], run_time=0.6)
        self.wait(0.3)

        # ---- 数轴 ----
        # 范围 [0, 40]，屏幕宽度 = 7 单位
        AXIS_W   = 7.0
        AXIS_Y   = -1.8
        CHI2_MAX = 40.0

        def val_to_x(v):
            return -AXIS_W / 2 + (v / CHI2_MAX) * AXIS_W

        axis_line = Line(
            LEFT * AXIS_W / 2 + UP * AXIS_Y,
            RIGHT * AXIS_W / 2 + UP * AXIS_Y,
            color=COLOR_HEADER, stroke_width=2
        )
        axis_tip = Arrow(
            RIGHT * (AXIS_W / 2 - 0.1) + UP * AXIS_Y,
            RIGHT * (AXIS_W / 2 + 0.3) + UP * AXIS_Y,
            color=COLOR_HEADER, stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.5
        )
        axis_label = MathTex(r"\chi^2", font_size=24, color=COLOR_HEADER
                             ).next_to(axis_tip, RIGHT, buff=0.1)

        self.play(Create(axis_line), GrowArrow(axis_tip), FadeIn(axis_label), run_time=0.6)

        # 0 刻度
        zero_tick = Line(
            [val_to_x(0), AXIS_Y - 0.12, 0],
            [val_to_x(0), AXIS_Y + 0.12, 0],
            color=GRAY_B
        )
        zero_lbl = Text("0", font=FONT_CN, font_size=18, color=GRAY_A
                        ).move_to([val_to_x(0), AXIS_Y - 0.4, 0])
        self.play(Create(zero_tick), FadeIn(zero_lbl), run_time=0.2)

        # 接受域 [0, 6.635]
        accept_x0 = val_to_x(0)
        accept_x1 = val_to_x(self.crit_001)
        accept_bar = Rectangle(
            width=accept_x1 - accept_x0, height=0.35,
            color=COLOR_ACCEPT, fill_color=COLOR_ACCEPT, fill_opacity=0.3,
            stroke_width=0
        ).move_to([(accept_x0 + accept_x1) / 2, AXIS_Y, 0])
        accept_lbl = Text("接受域", font=FONT_CN, font_size=17, color=COLOR_ACCEPT
                          ).next_to(accept_bar, UP, buff=0.1)
        self.play(FadeIn(accept_bar), FadeIn(accept_lbl), run_time=0.4)

        # 拒绝域 [6.635, 40]
        rej_x0  = val_to_x(self.crit_001)
        rej_x1  = val_to_x(CHI2_MAX)
        reject_bar = Rectangle(
            width=rej_x1 - rej_x0, height=0.35,
            color=COLOR_REJECT, fill_color=COLOR_REJECT, fill_opacity=0.25,
            stroke_width=0
        ).move_to([(rej_x0 + rej_x1) / 2, AXIS_Y, 0])
        reject_lbl = Text("拒绝域", font=FONT_CN, font_size=17, color=COLOR_REJECT
                          ).next_to(reject_bar, UP, buff=0.1)
        self.play(FadeIn(reject_bar), FadeIn(reject_lbl), run_time=0.4)

        # 临界值 3.841
        x_005 = val_to_x(self.crit_005)
        tick_005 = DashedLine(
            [x_005, AXIS_Y - 0.5, 0],
            [x_005, AXIS_Y + 0.5, 0],
            color=COLOR_CRIT, dash_length=0.08
        )
        lbl_005 = Text("3.841", font=FONT_CN, font_size=16, color=COLOR_CRIT
                       ).move_to([x_005, AXIS_Y - 0.65, 0])
        self.play(Create(tick_005), FadeIn(lbl_005), run_time=0.4)

        # 临界值 6.635
        x_001 = val_to_x(self.crit_001)
        tick_001 = DashedLine(
            [x_001, AXIS_Y - 0.5, 0],
            [x_001, AXIS_Y + 0.5, 0],
            color=RED, dash_length=0.08
        )
        lbl_001 = Text("6.635", font=FONT_CN, font_size=16, color=RED
                       ).move_to([x_001, AXIS_Y - 0.65, 0])
        self.play(Create(tick_001), FadeIn(lbl_001), run_time=0.4)

        # χ² = 32.48 标记（从上方落下）
        x_chi2 = val_to_x(self.chi2)
        chi2_dot = Dot([x_chi2, AXIS_Y, 0], radius=0.14, color=COLOR_CHI)
        chi2_tick = Line(
            [x_chi2, AXIS_Y - 0.25, 0],
            [x_chi2, AXIS_Y + 0.25, 0],
            color=COLOR_CHI, stroke_width=3
        )
        chi2_lbl = MathTex(r"\chi^2=32.48", font_size=22, color=COLOR_CHI
                           ).move_to([x_chi2, AXIS_Y + 0.85, 0])
        chi2_arr = Arrow(
            [x_chi2, AXIS_Y + 0.5, 0],
            [x_chi2, AXIS_Y + 0.1, 0],
            color=COLOR_CHI, stroke_width=2, buff=0,
            max_tip_length_to_length_ratio=0.4
        )

        # χ²点从屏幕外飞入
        chi2_dot_start = chi2_dot.copy().move_to([x_chi2, AXIS_Y + 2.0, 0])
        self.play(FadeIn(chi2_dot_start), run_time=0.1)
        self.play(
            chi2_dot_start.animate.move_to([x_chi2, AXIS_Y, 0]),
            run_time=0.5
        )
        self.play(
            Flash(chi2_dot_start, color=COLOR_CHI, flash_radius=0.35),
            FadeIn(chi2_lbl), GrowArrow(chi2_arr),
            run_time=0.6
        )
        self.wait(0.3)

        # 对比提示
        compare = Text(
            "32.48 >> 6.635",
            font=FONT_CN, font_size=30, color=YELLOW
        ).move_to(DOWN * 3.0)
        compare2 = Text(
            "χ² 远超0.01显著性水平临界值",
            font=FONT_CN, font_size=24, color=WHITE
        ).next_to(compare, DOWN, buff=0.3)
        self.play(Write(compare), run_time=0.5)
        self.play(FadeIn(compare2), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(crit_info),
            FadeOut(axis_line), FadeOut(axis_tip), FadeOut(axis_label),
            FadeOut(zero_tick), FadeOut(zero_lbl),
            FadeOut(accept_bar), FadeOut(accept_lbl),
            FadeOut(reject_bar), FadeOut(reject_lbl),
            FadeOut(tick_005), FadeOut(lbl_005),
            FadeOut(tick_001), FadeOut(lbl_001),
            FadeOut(chi2_dot_start), FadeOut(chi2_lbl), FadeOut(chi2_arr),
            FadeOut(compare), FadeOut(compare2),
            run_time=0.5
        )

    def _crit_row(self, formula, desc, color):
        f = MathTex(formula, font_size=24, color=color)
        d = Text(desc, font=FONT_CN, font_size=20, color=color)
        return VGroup(f, d).arrange(RIGHT, buff=0.4)

    # --------------------------------------------------------
    # Scene 7: 结论
    # --------------------------------------------------------
    def scene_7_conclusion(self):
        # χ²结果保留，其余清理
        self.play(FadeOut(self.chi2_display), FadeOut(self.table_group), run_time=0.4)

        # 大结论
        reject_box = RoundedRectangle(
            width=7.5, height=1.5, corner_radius=0.25,
            color=COLOR_REJECT, stroke_width=3,
            fill_color=COLOR_REJECT, fill_opacity=0.12
        ).move_to(UP * 2.5)
        reject_text = Text(
            "拒绝独立性假设！",
            font=FONT_CN, font_size=44, color=COLOR_REJECT
        ).move_to(reject_box.get_center())

        self.play(Create(reject_box), run_time=0.4)
        self.play(Write(reject_text), run_time=0.7)
        self.play(Flash(reject_box, color=COLOR_REJECT, flash_radius=0.5), run_time=0.4)

        # 结论文字
        conclusion1 = Text(
            "有 99% 的把握认为：",
            font=FONT_CN, font_size=30, color=WHITE
        ).move_to(UP * 1.1)
        conclusion2 = Text(
            "吸烟与患肺癌存在关联！",
            font=FONT_CN, font_size=36, color=YELLOW
        ).next_to(conclusion1, DOWN, buff=0.3)

        self.play(FadeIn(conclusion1, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(conclusion2, shift=UP * 0.2), run_time=0.5)

        # 数据强调
        data_box = VGroup(
            Text("吸烟者患肺癌率：20.98%", font=FONT_CN, font_size=24, color=COLOR_CELL_A),
            Text("不吸烟者患肺癌率：2.54%",  font=FONT_CN, font_size=24, color=COLOR_CELL_C),
            Text("风险相差约 8.3 倍",         font=FONT_CN, font_size=26, color=YELLOW),
        ).arrange(DOWN, buff=0.28).move_to(DOWN * 0.5)

        self.play(*[FadeIn(l, shift=RIGHT * 0.3) for l in data_box], run_time=0.6)
        self.wait(0.5)

        # 注意事项
        note_box = RoundedRectangle(
            width=7.2, height=1.2, corner_radius=0.2,
            color=GRAY_B, stroke_width=1.5,
            fill_color=GRAY_D, fill_opacity=0.2
        ).move_to(DOWN * 2.5)
        note_text = Text(
            "注意：相关≠因果\n需结合实际背景分析",
            font=FONT_CN, font_size=22, color=GRAY_A,
            line_spacing=1.2
        ).move_to(note_box.get_center())

        self.play(Create(note_box), FadeIn(note_text), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(reject_box), FadeOut(reject_text),
            FadeOut(conclusion1), FadeOut(conclusion2),
            FadeOut(data_box), FadeOut(note_box), FadeOut(note_text),
            run_time=0.5
        )

    # --------------------------------------------------------
    # Scene 8: 总结片尾
    # --------------------------------------------------------
    def scene_8_outro(self):
        # 知识要点
        summary_title = Text("独立性检验 · 核心要点",
                             font=FONT_CN, font_size=34, color=YELLOW).move_to(UP * 4.5)
        self.play(Write(summary_title), run_time=0.6)

        points = [
            (r"\chi^2 = \frac{n(ad-bc)^2}{(a+b)(c+d)(a+c)(b+d)}",  "卡方公式",  36),
            (r"\chi^2 \geq 6.635 \Rightarrow \text{99\%把握}",        "强相关判断", 30),
            (r"\chi^2 \geq 3.841 \Rightarrow \text{95\%把握}",        "中等判断",   30),
        ]

        point_group = VGroup()
        for tex, note, fs in points:
            f = MathTex(tex, font_size=fs, color=WHITE)
            n = Text(note, font=FONT_CN, font_size=20, color=GRAY_A)
            row = VGroup(f, n).arrange(RIGHT, buff=0.4)
            point_group.add(row)

        point_group.arrange(DOWN, buff=0.55, aligned_edge=LEFT
                            ).move_to(UP * 2.5 + LEFT * 0.3)

        for row in point_group:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.35)

        self.wait(0.4)

        # 作者大字
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT_CN, font_size=38, color=WHITE
        ).move_to(DOWN * 1.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT_CN, font_size=28, color=GRAY_B
        ).next_to(author_big, DOWN, buff=0.4)
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT_CN, font_size=28, color=YELLOW
        ).next_to(author_id, DOWN, buff=0.5)

        self.play(Transform(self.author_bar, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow, scale=1.1), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(summary_title), FadeOut(point_group),
            FadeOut(self.author_bar), FadeOut(author_id), FadeOut(follow),
            run_time=0.8
        )


# ============================================================
# 渲染命令:
#   manim -pql chi_square.py ChiSquareScene    # 快速预览 480p
#   manim -qh  chi_square.py ChiSquareScene    # 高质量 1080p
# ============================================================