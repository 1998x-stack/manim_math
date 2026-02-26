"""
perm_comb_app_animation.py - 排列组合应用 教学动画
高三数学第十六章：捆绑法 / 插空法 / 圆排列
manim -qh  perm_comb_app_animation.py PermCombApp   # 高质量输出
格式: TikTok 竖屏 (1080×1920)，约 70 秒
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ======================== 全局配置 ========================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ======================== 颜色常量 ========================
BG_COLOR  = "#1a1a2e"
C_A       = "#ff6b6b"   # 红  - 特殊元素 A
C_B       = "#f6c90e"   # 黄  - 特殊元素 B
C_C       = "#45b7d1"   # 蓝
C_D       = "#96ceb4"   # 绿
C_E       = "#c084fc"   # 紫
C_HL      = "#f6c90e"   # 高亮 / 答案
C_FMT     = "#4ecdc4"   # 公式
C_ORANGE  = "#f4a261"
C_GRAY    = "#a0a0b0"
FONT_CN   = "Noto Sans CJK SC"

# 5人颜色表
PERSON_COLORS = [C_A, C_B, C_C, C_D, C_E]
PERSON_LABELS = ["A", "B", "C", "D", "E"]

# 圆排列预计算坐标（来自 verify_geometry.py 输出）
CIRCLE_R   = 1.5
CIRCLE_CY  = 1.0   # 圆心 y
CIRCLE_POS = []    # 运行时计算
for k in range(5):
    angle = np.pi / 2 + k * 2 * np.pi / 5
    CIRCLE_POS.append(np.array([
        CIRCLE_R * np.cos(angle),
        CIRCLE_CY + CIRCLE_R * np.sin(angle),
        0
    ]))
# A(0, 2.5), B(-1.427,1.464), C(-0.882,-0.214), D(0.882,-0.214), E(1.427,1.464)


# ======================== 辅助函数 ========================
def make_person_block(label, color, side=0.65):
    """创建带字母标签的彩色方块"""
    rect = RoundedRectangle(
        width=side, height=side, corner_radius=0.1,
        color=color, fill_color=color, fill_opacity=0.85,
        stroke_width=2.5
    )
    text = Text(label, font=FONT_CN, font_size=26, color=WHITE, weight=BOLD)
    return VGroup(rect, text)


def make_person_circle(label, color, radius=0.35):
    """创建带字母标签的彩色圆（用于圆排列场景）"""
    circ = Circle(radius=radius, color=color,
                  fill_color=color, fill_opacity=0.88, stroke_width=2.5)
    text = Text(label, font=FONT_CN, font_size=22, color=WHITE, weight=BOLD)
    return VGroup(circ, text)


def make_answer_box(formula_str, color, width=3.8):
    """创建答案高亮框"""
    box = RoundedRectangle(
        width=width, height=1.0, corner_radius=0.2,
        color=color, stroke_width=2.5,
        fill_color=color, fill_opacity=0.12
    )
    formula = MathTex(formula_str, font_size=40, color=color)
    return VGroup(box, formula)


def make_method_card(title_str, desc_str, formula_str, color, width=7.5, height=1.35):
    """创建方法总结卡片"""
    box = RoundedRectangle(
        width=width, height=height, corner_radius=0.2,
        color=color, stroke_width=1.8,
        fill_color=color, fill_opacity=0.10
    )
    title = Text(title_str, font=FONT_CN, font_size=22, color=color, weight=BOLD)
    desc = Text(desc_str, font=FONT_CN, font_size=17, color=C_GRAY)
    formula = MathTex(formula_str, font_size=22, color=WHITE)

    title.move_to(box.get_center() + UP * 0.38 + LEFT * 1.8)
    desc.next_to(title, DOWN, buff=0.08, aligned_edge=LEFT)
    formula.move_to(box.get_center() + RIGHT * 1.8)
    return VGroup(box, title, desc, formula)


# ======================== 主场景 ========================
class PermCombApp(Scene):
    """
    排列组合应用技巧 - 完整教学动画
    场景: 开场→捆绑法→插空法→圆排列→总结→片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 全程作者标识
        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT_CN, font_size=18, color=C_GRAY
        ).move_to(UP * 7.0)
        self.add(self.author_bar)

        self.scene1_hook()
        self.scene2_bundle()
        self.scene3_gap()
        self.scene4_circle()
        self.scene5_summary()
        self.scene6_outro()

    # ─────────────────────────────────────────────────
    # Scene 1: 开场钩子 (0~6s)
    # ─────────────────────────────────────────────────
    def scene1_hook(self):
        # 主标题
        title = Text("解题3大技巧",
                     font=FONT_CN, font_size=46, color=C_HL
                     ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 5人方块依次落入
        blocks = VGroup(*[
            make_person_block(PERSON_LABELS[i], PERSON_COLORS[i])
            .move_to(np.array([-1.7 + i * 0.85, 1.5, 0]))
            for i in range(5)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(b) for b in blocks], lag_ratio=0.15),
            run_time=0.9
        )

        # 三个技巧 bullet 依次滑入
        bullets = [
            ("① 相邻问题", "→ 捆绑法", C_A),
            ("② 不相邻问题", "→ 插空法", C_C),
            ("③ 圆桌问题", "→ 圆排列", C_E),
        ]
        bullet_group = VGroup()
        for i, (q, a, col) in enumerate(bullets):
            y = 4.8 - i * 0.9
            qt = Text(q, font=FONT_CN, font_size=24, color=WHITE
                      ).move_to(np.array([-1.2, y, 0]))
            at = Text(a, font=FONT_CN, font_size=24, color=col, weight=BOLD
                      ).move_to(np.array([1.5, y, 0]))
            row = VGroup(qt, at)
            bullet_group.add(row)
            self.play(FadeIn(row, shift=LEFT * 0.3), run_time=0.4)

        self.wait(1.2)

        # 清场
        self.play(FadeOut(VGroup(title, blocks, bullet_group)), run_time=0.4)

    # ─────────────────────────────────────────────────
    # Scene 2: 捆绑法 (6~23s)
    # ─────────────────────────────────────────────────
    def scene2_bundle(self):
        # ── 标题区 ──
        method_tag = RoundedRectangle(
            width=4.2, height=0.75, corner_radius=0.18,
            color=C_A, fill_color=C_A, fill_opacity=0.25, stroke_width=2
        ).move_to(UP * 6.1)
        method_title = Text("捆绑法", font=FONT_CN, font_size=34, color=C_A,
                            weight=BOLD).move_to(method_tag.get_center())

        self.play(FadeIn(method_tag), Write(method_title), run_time=0.5)

        # ── 题目 ──
        eg = Text("5人排成一排，A 和 B 必须相邻",
                  font=FONT_CN, font_size=22, color=WHITE
                  ).move_to(UP * 5.0)
        question = Text("共有多少种排法？",
                        font=FONT_CN, font_size=24, color=C_HL
                        ).move_to(UP * 4.35)
        self.play(FadeIn(eg), run_time=0.4)
        self.play(FadeIn(question), run_time=0.35)

        # ── Step 1: 展示5个方块 ──
        step1_label = Text("① 将 A、B 视为一个整体：",
                           font=FONT_CN, font_size=22, color=C_GRAY
                           ).move_to(UP * 3.3)
        self.play(FadeIn(step1_label), run_time=0.35)

        # 5个方块原始排列
        BLOCK_Y = 2.3
        SPACING = 0.85
        xs_5 = [-1.7 + i * SPACING for i in range(5)]
        blocks5 = VGroup(*[
            make_person_block(PERSON_LABELS[i], PERSON_COLORS[i])
            .move_to(np.array([xs_5[i], BLOCK_Y, 0]))
            for i in range(5)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(b) for b in blocks5], lag_ratio=0.12),
            run_time=0.7
        )

        # 大括号框住 A 和 B（前两个方块）
        brace = Brace(
            VGroup(blocks5[0], blocks5[1]),
            direction=DOWN, color=C_HL
        )
        brace_label = Text("[AB]", font=FONT_CN, font_size=22, color=C_HL,
                           weight=BOLD).next_to(brace, DOWN, buff=0.08)
        self.play(FadeIn(brace), Write(brace_label), run_time=0.6)
        self.wait(0.4)

        # ── Step 2: 变为4单元 ──
        step2_label = Text("② 共 4 个单元，全排列：",
                           font=FONT_CN, font_size=22, color=C_GRAY
                           ).move_to(UP * 0.8)
        self.play(FadeIn(step2_label), run_time=0.35)

        # 创建4单元方块（[AB]宽度稍大）
        unit_y = 0.0
        unit_spacing = 1.0
        xs_4 = [-1.5 + i * unit_spacing for i in range(4)]

        # [AB] 整体块
        ab_rect = RoundedRectangle(
            width=1.1, height=0.65, corner_radius=0.1,
            color=C_HL, fill_color=C_HL, fill_opacity=0.85, stroke_width=2.5
        )
        ab_text = Text("[AB]", font=FONT_CN, font_size=20, color=BG_COLOR, weight=BOLD)
        ab_block = VGroup(ab_rect, ab_text).move_to(np.array([xs_4[0], unit_y, 0]))

        other_blocks = VGroup(*[
            make_person_block(PERSON_LABELS[i + 2], PERSON_COLORS[i + 2])
            .move_to(np.array([xs_4[i + 1], unit_y, 0]))
            for i in range(3)
        ])

        four_units = VGroup(ab_block, other_blocks)
        self.play(
            FadeOut(VGroup(brace, brace_label, blocks5)),
            run_time=0.3
        )
        self.play(
            GrowFromCenter(ab_block),
            LaggedStart(*[GrowFromCenter(b) for b in other_blocks], lag_ratio=0.12),
            run_time=0.7
        )

        # Step 2 公式
        f1 = MathTex(r"A(4,4) = 4! = 24",
                     font_size=32, color=WHITE).move_to(UP * -0.9)
        self.play(Write(f1), run_time=0.6)

        # ── Step 3: [AB]内部 2! 种 ──
        step3_label = Text("③ [AB] 内部可互换：",
                           font=FONT_CN, font_size=22, color=C_GRAY
                           ).move_to(DOWN * 2.0)
        self.play(FadeIn(step3_label), run_time=0.35)

        # 显示 A|B ↔ B|A
        ab_demo = VGroup(
            make_person_block("A", C_A).scale(0.85),
            make_person_block("B", C_B).scale(0.85)
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 3.1 + LEFT * 1.5)

        arrow_swap = Text("↔", font=FONT_CN, font_size=30, color=C_GRAY
                          ).move_to(DOWN * 3.1)

        ba_demo = VGroup(
            make_person_block("B", C_B).scale(0.85),
            make_person_block("A", C_A).scale(0.85)
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 3.1 + RIGHT * 1.5)

        f2 = MathTex(r"2! = 2", font_size=28, color=C_A).move_to(DOWN * 4.0)

        self.play(
            FadeIn(ab_demo), FadeIn(arrow_swap), FadeIn(ba_demo),
            run_time=0.5
        )
        self.play(Write(f2), run_time=0.4)

        # ── 总公式 + 答案 ──
        formula_box = RoundedRectangle(
            width=7.0, height=0.85, corner_radius=0.18,
            color=C_FMT, stroke_width=2, fill_color=C_FMT, fill_opacity=0.1
        ).move_to(DOWN * 5.0)
        total_f = MathTex(r"4! \times 2! = 24 \times 2 = 48",
                          font_size=30, color=C_FMT).move_to(DOWN * 5.0)
        self.play(FadeIn(formula_box), Write(total_f), run_time=0.7)

        # Handle Chinese characters properly - don't use \text{} in MathTex
        ans_num = MathTex(r"48", font_size=42, color=C_HL)
        ans_unit = Text("种", font=FONT_CN, font_size=36, color=C_HL)
        ans_inner = VGroup(ans_num, ans_unit).arrange(RIGHT, buff=0.12)
        ans_rect = RoundedRectangle(
            width=3.5, height=1.0, corner_radius=0.2,
            color=C_HL, stroke_width=2.5, fill_color=C_HL, fill_opacity=0.12
        )
        ans_total = VGroup(ans_rect, ans_inner).move_to(DOWN * 6.2)
        ans_inner.move_to(ans_rect.get_center())
        
        self.play(FadeIn(ans_total, scale=1.05), run_time=0.5)
        self.play(Flash(ans_rect, color=C_HL, flash_radius=0.6), run_time=0.5)
        self.wait(1.2)

        # 用 Text 替代 \text{种}
        ans_num = MathTex(r"48", font_size=42, color=C_HL)
        ans_unit = Text("种", font=FONT_CN, font_size=36, color=C_HL)
        ans_inner = VGroup(ans_num, ans_unit).arrange(RIGHT, buff=0.12)
        ans_rect = RoundedRectangle(
            width=3.5, height=1.0, corner_radius=0.2,
            color=C_HL, stroke_width=2.5, fill_color=C_HL, fill_opacity=0.12
        )
        ans_total = VGroup(ans_rect, ans_inner).move_to(DOWN * 6.2)
        ans_inner.move_to(ans_rect.get_center())

        self.play(FadeIn(ans_total, scale=1.05), run_time=0.5)
        self.play(Flash(ans_rect, color=C_HL, flash_radius=0.6), run_time=0.5)
        self.wait(1.2)

        # 清场
        self.play(
            FadeOut(VGroup(
                method_tag, method_title, eg, question,
                step1_label, step2_label, step3_label,
                four_units, f1, ab_demo, arrow_swap, ba_demo, f2,
                formula_box, total_f, ans_total
            )),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 3: 插空法 (23~40s)
    # ─────────────────────────────────────────────────
    def scene3_gap(self):
        # ── 标题 ──
        method_tag = RoundedRectangle(
            width=4.2, height=0.75, corner_radius=0.18,
            color=C_C, fill_color=C_C, fill_opacity=0.25, stroke_width=2
        ).move_to(UP * 6.1)
        method_title = Text("插空法", font=FONT_CN, font_size=34, color=C_C,
                            weight=BOLD).move_to(method_tag.get_center())
        self.play(FadeIn(method_tag), Write(method_title), run_time=0.5)

        eg = Text("5人排成一排，A 和 B 不相邻",
                  font=FONT_CN, font_size=22, color=WHITE).move_to(UP * 5.0)
        question = Text("共有多少种排法？",
                        font=FONT_CN, font_size=24, color=C_HL).move_to(UP * 4.35)
        self.play(FadeIn(eg), FadeIn(question), run_time=0.5)

        # ── Step 1: 先排 C D E ──
        step1_lbl = Text("① 先排 C、D、E（不含特殊元素）：",
                         font=FONT_CN, font_size=22, color=C_GRAY
                         ).move_to(UP * 3.3)
        self.play(FadeIn(step1_lbl), run_time=0.35)

        CDE_Y = 2.3
        CDE_SPACING = 1.3
        cde_blocks = VGroup(*[
            make_person_block(PERSON_LABELS[i + 2], PERSON_COLORS[i + 2])
            .move_to(np.array([(i - 1) * CDE_SPACING, CDE_Y, 0]))
            for i in range(3)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(b) for b in cde_blocks], lag_ratio=0.2),
            run_time=0.6
        )

        f_step1 = MathTex(r"3! = 6", font_size=30, color=WHITE
                          ).move_to(UP * 1.3)
        self.play(Write(f_step1), run_time=0.5)

        # ── Step 2: 显示4个空位 ──
        step2_lbl = Text("② 产生 4 个空位（头尾及间隙）：",
                         font=FONT_CN, font_size=22, color=C_GRAY
                         ).move_to(UP * 0.5)
        self.play(FadeIn(step2_lbl), run_time=0.35)

        # 空位标记：_ 符号，x 位置在 CDE 块的间隔及两端
        gap_xs = [-1.95, -0.65, 0.65, 1.95]
        gap_markers = VGroup()
        gap_nums = VGroup()
        for idx, gx in enumerate(gap_xs):
            marker = Text("▼", font=FONT_CN, font_size=28, color=C_FMT
                          ).move_to(np.array([gx, CDE_Y + 0.5, 0]))
            num = Text(str(idx + 1), font=FONT_CN, font_size=16, color=C_FMT
                       ).move_to(np.array([gx, CDE_Y + 0.92, 0]))
            gap_markers.add(marker)
            gap_nums.add(num)

        self.play(
            LaggedStart(*[FadeIn(m, shift=DOWN * 0.2) for m in gap_markers],
                        lag_ratio=0.15),
            run_time=0.5
        )
        self.play(
            LaggedStart(*[FadeIn(n) for n in gap_nums], lag_ratio=0.1),
            run_time=0.3
        )

        # ── Step 3: A 插入空位1，B 插入空位3（示例）──
        step3_lbl = Text("③ A、B 各选一个空位插入：",
                         font=FONT_CN, font_size=22, color=C_GRAY
                         ).move_to(DOWN * 0.8)
        self.play(FadeIn(step3_lbl), run_time=0.35)

        # A 从上方落入空位1（x=-1.95）
        a_block = make_person_block("A", C_A).move_to(
            np.array([gap_xs[0], CDE_Y + 2.5, 0])
        )
        self.play(GrowFromCenter(a_block), run_time=0.3)
        self.play(a_block.animate.move_to(np.array([gap_xs[0], CDE_Y, 0])),
                  run_time=0.5)

        # B 落入空位3（x=0.65）
        b_block = make_person_block("B", C_B).move_to(
            np.array([gap_xs[2], CDE_Y + 2.5, 0])
        )
        self.play(GrowFromCenter(b_block), run_time=0.3)
        self.play(b_block.animate.move_to(np.array([gap_xs[2], CDE_Y, 0])),
                  run_time=0.5)

        f_step3 = MathTex(r"A(4,2) = 4 \times 3 = 12",
                          font_size=30, color=WHITE).move_to(DOWN * 2.0)
        self.play(Write(f_step3), run_time=0.6)

        # ── 总公式 + 答案 ──
        formula_box = RoundedRectangle(
            width=7.0, height=0.85, corner_radius=0.18,
            color=C_FMT, stroke_width=2, fill_color=C_FMT, fill_opacity=0.1
        ).move_to(DOWN * 3.2)
        total_f = MathTex(r"3! \times A(4,2) = 6 \times 12 = 72",
                          font_size=28, color=C_FMT).move_to(DOWN * 3.2)
        self.play(FadeIn(formula_box), Write(total_f), run_time=0.7)

        # 答案
        ans_num = MathTex(r"72", font_size=42, color=C_HL)
        ans_unit = Text("种", font=FONT_CN, font_size=36, color=C_HL)
        ans_inner = VGroup(ans_num, ans_unit).arrange(RIGHT, buff=0.12)
        ans_rect = RoundedRectangle(
            width=3.5, height=1.0, corner_radius=0.2,
            color=C_HL, stroke_width=2.5, fill_color=C_HL, fill_opacity=0.12
        )
        ans_total = VGroup(ans_rect, ans_inner).move_to(DOWN * 4.6)
        ans_inner.move_to(ans_rect.get_center())

        self.play(FadeIn(ans_total, scale=1.05), run_time=0.5)
        self.play(Flash(ans_rect, color=C_HL, flash_radius=0.6), run_time=0.5)
        self.wait(1.2)

        # 清场
        self.play(
            FadeOut(VGroup(
                method_tag, method_title, eg, question,
                step1_lbl, cde_blocks, f_step1,
                step2_lbl, gap_markers, gap_nums,
                step3_lbl, a_block, b_block, f_step3,
                formula_box, total_f, ans_total
            )),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 4: 圆排列 (40~57s)
    # ─────────────────────────────────────────────────
    def scene4_circle(self):
        # ── 标题 ──
        method_tag = RoundedRectangle(
            width=4.2, height=0.75, corner_radius=0.18,
            color=C_E, fill_color=C_E, fill_opacity=0.25, stroke_width=2
        ).move_to(UP * 6.1)
        method_title = Text("圆排列", font=FONT_CN, font_size=34, color=C_E,
                            weight=BOLD).move_to(method_tag.get_center())
        self.play(FadeIn(method_tag), Write(method_title), run_time=0.5)

        eg = Text("5人围坐圆桌，共有多少种坐法？",
                  font=FONT_CN, font_size=23, color=WHITE).move_to(UP * 5.0)
        self.play(FadeIn(eg), run_time=0.4)

        # ── 圆桌（大圆圈轮廓）──
        table_circle = Circle(
            radius=1.85, color=C_GRAY, stroke_width=3, fill_opacity=0.05,
            fill_color="#2a2a4a"
        ).move_to(np.array([0, CIRCLE_CY, 0]))
        self.play(Create(table_circle), run_time=0.8)

        # ── 5个座位（彩圈）逐个出现 ──
        seats = VGroup(*[
            make_person_circle(PERSON_LABELS[i], PERSON_COLORS[i])
            .move_to(CIRCLE_POS[i])
            for i in range(5)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(s) for s in seats], lag_ratio=0.2),
            run_time=0.9
        )
        self.wait(0.3)

        # ── 固定 A（锁定提示）──
        step1_lbl = Text("① 固定 A，消除重复旋转",
                         font=FONT_CN, font_size=22, color=C_A
                         ).move_to(DOWN * 1.8)
        self.play(FadeIn(step1_lbl), run_time=0.35)

        # A 高亮边框
        a_highlight = Circle(
            radius=0.45, color=C_HL, stroke_width=3, fill_opacity=0
        ).move_to(CIRCLE_POS[0])
        lock_icon = Text("🔒", font_size=20).move_to(CIRCLE_POS[0] + UP * 0.65)

        self.play(Create(a_highlight), run_time=0.4)
        self.play(FadeIn(lock_icon), run_time=0.3)

        # ── 其余4人旋转演示 ──
        step2_lbl = Text("② 其余 4 人全排列",
                         font=FONT_CN, font_size=22, color=C_GRAY
                         ).move_to(DOWN * 2.6)
        self.play(FadeIn(step2_lbl), run_time=0.35)

        # 其余4人（BCDE）旋转一次换位示意
        other_seats = VGroup(*[seats[i] for i in range(1, 5)])
        self.play(
            Rotate(other_seats, angle=2 * np.pi / 5,
                   about_point=np.array([0, CIRCLE_CY, 0])),
            run_time=1.0
        )
        self.play(
            Rotate(other_seats, angle=-2 * np.pi / 5,
                   about_point=np.array([0, CIRCLE_CY, 0])),
            run_time=0.7
        )

        # ── 公式推导 ──
        f1 = MathTex(r"(n-1)!", font_size=34, color=C_FMT
                     ).move_to(DOWN * 3.7)
        arrow = Text("→ n=5 时：", font=FONT_CN, font_size=22, color=C_GRAY
                     ).next_to(f1, RIGHT, buff=0.3)
        self.play(Write(f1), FadeIn(arrow), run_time=0.6)

        f2 = MathTex(r"(5-1)! = 4! = 24",
                     font_size=32, color=C_FMT).move_to(DOWN * 4.8)
        self.play(Write(f2), run_time=0.6)

        # 答案
        ans_num = MathTex(r"24", font_size=42, color=C_HL)
        ans_unit = Text("种", font=FONT_CN, font_size=36, color=C_HL)
        ans_inner = VGroup(ans_num, ans_unit).arrange(RIGHT, buff=0.12)
        ans_rect = RoundedRectangle(
            width=3.5, height=1.0, corner_radius=0.2,
            color=C_HL, stroke_width=2.5, fill_color=C_HL, fill_opacity=0.12
        )
        ans_total = VGroup(ans_rect, ans_inner).move_to(DOWN * 6.0)
        ans_inner.move_to(ans_rect.get_center())

        self.play(FadeIn(ans_total, scale=1.05), run_time=0.5)
        self.play(Flash(ans_rect, color=C_HL, flash_radius=0.6), run_time=0.5)
        self.wait(1.3)

        # 清场
        self.play(
            FadeOut(VGroup(
                method_tag, method_title, eg,
                table_circle, seats, a_highlight, lock_icon,
                step1_lbl, step2_lbl,
                f1, arrow, f2, ans_total
            )),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 5: 方法总结 (57~65s)
    # ─────────────────────────────────────────────────
    def scene5_summary(self):
        title = Text("解题技巧速查",
                     font=FONT_CN, font_size=40, color=C_HL
                     ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # 三张卡片
        cards_data = [
            (
                "捆绑法",
                "特殊元素相邻 → 视为整体",
                r"(n-k+1)! \times k!",
                C_A, UP * 4.3
            ),
            (
                "插空法",
                "特殊元素不相邻 → 先排其余",
                r"(n-m)! \times A(n-m+1,\ m)",
                C_C, UP * 2.6
            ),
            (
                "圆排列",
                "圆桌问题 → 固定一人",
                r"(n-1)!",
                C_E, UP * 0.9
            ),
        ]

        card_group = VGroup()
        for (t, d, f, col, pos) in cards_data:
            card = make_method_card(t, d, f, col)
            card.move_to(pos)
            card_group.add(card)
            self.play(FadeIn(card, shift=LEFT * 0.4), run_time=0.45)

        self.wait(0.5)

        # 关键提示
        tip_box = RoundedRectangle(
            width=7.5, height=1.2, corner_radius=0.2,
            color=C_HL, stroke_width=1.5, fill_color=C_HL, fill_opacity=0.08
        ).move_to(DOWN * 1.5)
        tip1 = Text("判断关键：有无顺序？可否重复？",
                    font=FONT_CN, font_size=22, color=C_HL, weight=BOLD
                    ).move_to(DOWN * 1.35)
        tip2 = Text("特殊元素 / 特殊位置 → 优先处理！",
                    font=FONT_CN, font_size=20, color=WHITE
                    ).move_to(DOWN * 1.85)
        self.play(FadeIn(tip_box), Write(tip1), run_time=0.5)
        self.play(FadeIn(tip2), run_time=0.35)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, card_group, tip_box, tip1, tip2)),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 6: 片尾 (65~72s)
    # ─────────────────────────────────────────────────
    def scene6_outro(self):
        # 三个方法回顾动画（三个圆圈闪出）
        recap = VGroup(
            Circle(radius=0.6, color=C_A, fill_opacity=0.8
                   ).move_to(LEFT * 2.2 + UP * 0.5),
            Circle(radius=0.6, color=C_C, fill_opacity=0.8
                   ).move_to(UP * 0.5),
            Circle(radius=0.6, color=C_E, fill_opacity=0.8
                   ).move_to(RIGHT * 2.2 + UP * 0.5),
        )
        recap_labels = VGroup(
            Text("捆绑", font=FONT_CN, font_size=20, color=WHITE
                 ).move_to(LEFT * 2.2 + UP * 0.5),
            Text("插空", font=FONT_CN, font_size=20, color=WHITE
                 ).move_to(UP * 0.5),
            Text("圆排", font=FONT_CN, font_size=20, color=WHITE
                 ).move_to(RIGHT * 2.2 + UP * 0.5),
        )
        self.play(
            LaggedStart(*[GrowFromCenter(c) for c in recap], lag_ratio=0.2),
            run_time=0.7
        )
        self.play(FadeIn(recap_labels), run_time=0.3)

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT_CN, font_size=40, color=WHITE
        ).move_to(DOWN * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT_CN, font_size=28, color=C_GRAY
        ).move_to(DOWN * 3.0)
        cta = Text(
            "关注我，获得更多数学技巧！",
            font=FONT_CN, font_size=28, color=C_HL
        ).move_to(DOWN * 4.2)

        self.play(FadeIn(author_big, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(FadeIn(cta, scale=1.08), run_time=0.5)

        # 彩点装饰
        sparkles = VGroup()
        for i, col in enumerate([C_A, C_B, C_C, C_D, C_E]):
            angle = i * 2 * np.pi / 5
            pos = np.array([np.cos(angle) * 1.8, -4.2 + np.sin(angle) * 0.5, 0])
            dot = Dot(pos, radius=0.12, color=col, fill_opacity=0.9)
            sparkles.add(dot)

        self.play(
            LaggedStart(*[GrowFromCenter(s) for s in sparkles], lag_ratio=0.1),
            run_time=0.5
        )
        self.play(Rotate(sparkles, angle=PI, run_time=1.2))
        self.wait(1.0)

        # 最终淡出
        self.play(
            FadeOut(VGroup(recap, recap_labels,
                           author_big, author_id, cta, sparkles)),
            run_time=0.8
        )