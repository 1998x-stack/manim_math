"""
面积单位的换算 - Area Unit Conversion Animation
三年级下册 第六章 几何小实践

内容: 面积单位换算 (1dm²=100cm², 1m²=100dm²)
目标观众: 三年级小学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class AreaUnitConvertLesson(Scene):
    """
    面积单位换算教学动画

    场景顺序:
    1. 开场钩子 - 提问引入
    2. 复习面积单位
    3. 1dm² = 100cm² 可视化证明
    4. 1m² = 100dm² 可视化证明
    5. 进率是100的原因 (二维度量)
    6. 换算练习
    7. 片尾总结
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.COLOR_DM = "#3498db"         # 蓝色 - 分米
        self.COLOR_CM = "#e74c3c"         # 红色 - 厘米
        self.COLOR_M = "#2ecc71"          # 绿色 - 米
        self.COLOR_HIGHLIGHT = "#f1c40f"  # 黄色 - 高亮
        self.COLOR_TEXT = WHITE
        self.COLOR_SUBTEXT = "#95a5a6"

        # 品牌信息 (顶部固定)
        self.author_brand = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)

        self.play(FadeIn(self.author_brand, shift=DOWN * 0.2), run_time=0.4)

        # 执行各场景
        self.scene_1_hook()
        self.scene_2_review_units()
        self.scene_3_dm_to_cm()
        self.scene_4_m_to_dm()
        self.scene_5_why_100()
        self.scene_6_practice()
        self.scene_7_outro()

    # ================================================================
    # 场景1: 开场钩子
    # ================================================================
    def scene_1_hook(self):
        """开场钩子 - 引出问题"""

        hook_q = Text(
            "你知道吗?",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)

        hook_line1 = Text(
            "1分米 × 1分米",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_TEXT
        ).move_to(UP * 4.5)

        hook_line2 = Text(
            "= 100 平方厘米",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_CM
        ).move_to(UP * 3.7)

        hook_line3 = Text(
            "为什么不是10?",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.8)

        self.play(Write(hook_q), run_time=0.6)
        self.play(FadeIn(hook_line1, shift=UP * 0.3), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(hook_line2, shift=UP * 0.3), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(hook_line3, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(hook_q),
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            FadeOut(hook_line3),
            run_time=0.5
        )

    # ================================================================
    # 场景2: 复习面积单位
    # ================================================================
    def scene_2_review_units(self):
        """复习三个面积单位"""

        title = Text(
            "面积单位",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)

        self.play(Write(title), run_time=0.6)

        # 平方厘米卡片
        sq_cm_box = Square(
            side_length=1.2,
            color=self.COLOR_CM,
            fill_color=self.COLOR_CM,
            fill_opacity=0.15
        )
        sq_cm_label_top = Text("1cm", font="PingFang SC", font_size=20, color=self.COLOR_CM)
        sq_cm_label_top.next_to(sq_cm_box, UP, buff=0.1)
        sq_cm_label_side = Text("1cm", font="PingFang SC", font_size=20, color=self.COLOR_CM)
        sq_cm_label_side.next_to(sq_cm_box, LEFT, buff=0.1)
        sq_cm_name = Text("平方厘米", font="PingFang SC", font_size=22, color=self.COLOR_CM)
        sq_cm_name.next_to(sq_cm_box, DOWN, buff=0.15)
        sq_cm_symbol = MathTex(r"\text{cm}^2", font_size=28, color=self.COLOR_CM)
        sq_cm_symbol.next_to(sq_cm_name, DOWN, buff=0.08)
        cm_group = VGroup(sq_cm_box, sq_cm_label_top, sq_cm_label_side, sq_cm_name, sq_cm_symbol)

        # 平方分米卡片
        sq_dm_box = Square(
            side_length=1.8,
            color=self.COLOR_DM,
            fill_color=self.COLOR_DM,
            fill_opacity=0.15
        )
        sq_dm_label_top = Text("1dm", font="PingFang SC", font_size=20, color=self.COLOR_DM)
        sq_dm_label_top.next_to(sq_dm_box, UP, buff=0.1)
        sq_dm_label_side = Text("1dm", font="PingFang SC", font_size=20, color=self.COLOR_DM)
        sq_dm_label_side.next_to(sq_dm_box, LEFT, buff=0.1)
        sq_dm_name = Text("平方分米", font="PingFang SC", font_size=22, color=self.COLOR_DM)
        sq_dm_name.next_to(sq_dm_box, DOWN, buff=0.15)
        sq_dm_symbol = MathTex(r"\text{dm}^2", font_size=28, color=self.COLOR_DM)
        sq_dm_symbol.next_to(sq_dm_name, DOWN, buff=0.08)
        dm_group = VGroup(sq_dm_box, sq_dm_label_top, sq_dm_label_side, sq_dm_name, sq_dm_symbol)

        # 位置排列
        cm_group.move_to(LEFT * 2.2 + UP * 2.2)
        dm_group.move_to(RIGHT * 2.2 + UP * 2.2)

        self.play(Create(sq_cm_box), Create(sq_dm_box), run_time=0.8)
        self.play(
            FadeIn(sq_cm_label_top), FadeIn(sq_cm_label_side),
            FadeIn(sq_dm_label_top), FadeIn(sq_dm_label_side),
            run_time=0.5
        )
        self.play(
            FadeIn(sq_cm_name), FadeIn(sq_cm_symbol),
            FadeIn(sq_dm_name), FadeIn(sq_dm_symbol),
            run_time=0.5
        )
        self.wait(0.5)

        # 平方米卡片 (下方)
        sq_m_box = Square(
            side_length=2.2,
            color=self.COLOR_M,
            fill_color=self.COLOR_M,
            fill_opacity=0.12
        )
        sq_m_label_top = Text("1m", font="PingFang SC", font_size=20, color=self.COLOR_M)
        sq_m_label_top.next_to(sq_m_box, UP, buff=0.1)
        sq_m_label_side = Text("1m", font="PingFang SC", font_size=20, color=self.COLOR_M)
        sq_m_label_side.next_to(sq_m_box, LEFT, buff=0.1)
        sq_m_name = Text("平方米", font="PingFang SC", font_size=22, color=self.COLOR_M)
        sq_m_name.next_to(sq_m_box, DOWN, buff=0.15)
        sq_m_symbol = MathTex(r"\text{m}^2", font_size=28, color=self.COLOR_M)
        sq_m_symbol.next_to(sq_m_name, DOWN, buff=0.08)
        m_group = VGroup(sq_m_box, sq_m_label_top, sq_m_label_side, sq_m_name, sq_m_symbol)
        m_group.move_to(DOWN * 2.0)

        self.play(Create(sq_m_box), run_time=0.7)
        self.play(
            FadeIn(sq_m_label_top), FadeIn(sq_m_label_side),
            FadeIn(sq_m_name), FadeIn(sq_m_symbol),
            run_time=0.5
        )
        self.wait(0.5)

        arrow_hint = Text(
            "它们之间如何换算?",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.2)

        self.play(FadeIn(arrow_hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(title),
            FadeOut(cm_group),
            FadeOut(dm_group),
            FadeOut(m_group),
            FadeOut(arrow_hint),
            run_time=0.6
        )

    # ================================================================
    # 场景3: 1dm² = 100cm² 可视化证明
    # ================================================================
    def scene_3_dm_to_cm(self):
        """可视化证明 1dm² = 100cm²"""

        title = Text(
            "1平方分米 = 多少平方厘米?",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.3)

        self.play(Write(title), run_time=0.7)

        # 1dm × 1dm 正方形
        dm_square_size = 3.8
        dm_square = Square(
            side_length=dm_square_size,
            color=self.COLOR_DM,
            fill_color=self.COLOR_DM,
            fill_opacity=0.08,
            stroke_width=3
        ).move_to(UP * 2.0)

        dm_label_top = Text(
            "1 分米 = 10 厘米",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_DM
        ).next_to(dm_square, UP, buff=0.18)

        dm_label_left = Text(
            "1 分米\n= 10 厘米",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_DM
        ).next_to(dm_square, LEFT, buff=0.18)

        self.play(Create(dm_square), run_time=0.8)
        self.play(FadeIn(dm_label_top), FadeIn(dm_label_left), run_time=0.5)
        self.wait(0.4)

        key_note = Text(
            "因为 1dm = 10cm",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.0)

        self.play(FadeIn(key_note, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 画 10×10 网格
        grid_lines = VGroup()
        dm_center = dm_square.get_center()
        dm_left_x = dm_center[0] - dm_square_size / 2
        dm_right_x = dm_center[0] + dm_square_size / 2
        dm_top_y = dm_center[1] + dm_square_size / 2
        dm_bottom_y = dm_center[1] - dm_square_size / 2

        n_divisions = 10
        cell_size = dm_square_size / n_divisions

        # 纵线
        for i in range(1, n_divisions):
            x = dm_left_x + i * cell_size
            grid_lines.add(Line(
                np.array([x, dm_bottom_y, 0]),
                np.array([x, dm_top_y, 0]),
                color=self.COLOR_CM,
                stroke_width=0.8,
                stroke_opacity=0.55
            ))

        # 横线
        for j in range(1, n_divisions):
            y = dm_bottom_y + j * cell_size
            grid_lines.add(Line(
                np.array([dm_left_x, y, 0]),
                np.array([dm_right_x, y, 0]),
                color=self.COLOR_CM,
                stroke_width=0.8,
                stroke_opacity=0.55
            ))

        self.play(Create(grid_lines), run_time=1.2)

        # 标注网格数量
        label_10h = Text("10格", font="PingFang SC", font_size=20, color=self.COLOR_CM)
        label_10h.next_to(dm_square, DOWN, buff=0.12)
        label_10v = Text("10格", font="PingFang SC", font_size=20, color=self.COLOR_CM)
        label_10v.next_to(dm_square, RIGHT, buff=0.12)

        self.play(FadeIn(label_10h), FadeIn(label_10v), run_time=0.4)
        self.wait(0.4)

        # 高亮左下角一个小方格
        highlight_cell = Square(
            side_length=cell_size,
            color=self.COLOR_CM,
            fill_color=self.COLOR_CM,
            fill_opacity=0.75,
            stroke_width=2
        ).move_to(np.array([dm_left_x + cell_size / 2, dm_bottom_y + cell_size / 2, 0]))

        cell_label = Text(
            "1cm²",
            font="PingFang SC",
            font_size=13,
            color=WHITE
        ).move_to(highlight_cell.get_center())

        self.play(FadeIn(highlight_cell), run_time=0.4)
        self.play(FadeIn(cell_label), run_time=0.3)
        self.wait(0.4)

        # 计算过程
        calc_text = Text(
            "每行 10 格，共 10 行",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_TEXT
        ).move_to(DOWN * 5.0)

        self.play(FadeIn(calc_text, shift=UP * 0.2), run_time=0.4)

        calc_formula = MathTex(
            r"10 \times 10 = 100",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.9)

        self.play(Write(calc_formula), run_time=0.6)
        self.wait(0.5)

        conclusion = Text(
            "1平方分米 = 100平方厘米",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 7.0)

        self.play(FadeIn(conclusion, scale=1.1), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(dm_square),
            FadeOut(dm_label_top),
            FadeOut(dm_label_left),
            FadeOut(grid_lines),
            FadeOut(key_note),
            FadeOut(label_10h),
            FadeOut(label_10v),
            FadeOut(highlight_cell),
            FadeOut(cell_label),
            FadeOut(calc_text),
            FadeOut(calc_formula),
            FadeOut(conclusion),
            run_time=0.7
        )

    # ================================================================
    # 场景4: 1m² = 100dm² 可视化证明
    # ================================================================
    def scene_4_m_to_dm(self):
        """可视化证明 1m² = 100dm²"""

        title = Text(
            "1平方米 = 多少平方分米?",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.3)

        self.play(Write(title), run_time=0.7)

        # 1m × 1m 正方形
        m_square_size = 3.8
        m_square = Square(
            side_length=m_square_size,
            color=self.COLOR_M,
            fill_color=self.COLOR_M,
            fill_opacity=0.08,
            stroke_width=3
        ).move_to(UP * 2.0)

        m_label_top = Text(
            "1 米 = 10 分米",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_M
        ).next_to(m_square, UP, buff=0.18)

        m_label_left = Text(
            "1 米\n= 10 分米",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_M
        ).next_to(m_square, LEFT, buff=0.18)

        self.play(Create(m_square), run_time=0.8)
        self.play(FadeIn(m_label_top), FadeIn(m_label_left), run_time=0.5)

        key_note = Text(
            "因为 1m = 10dm",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.0)

        self.play(FadeIn(key_note, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 画 10×10 网格
        grid_lines = VGroup()
        m_center = m_square.get_center()
        m_left_x = m_center[0] - m_square_size / 2
        m_right_x = m_center[0] + m_square_size / 2
        m_top_y = m_center[1] + m_square_size / 2
        m_bottom_y = m_center[1] - m_square_size / 2

        n_div = 10
        cell_size = m_square_size / n_div

        for i in range(1, n_div):
            x = m_left_x + i * cell_size
            grid_lines.add(Line(
                np.array([x, m_bottom_y, 0]),
                np.array([x, m_top_y, 0]),
                color=self.COLOR_DM,
                stroke_width=1.0,
                stroke_opacity=0.65
            ))

        for j in range(1, n_div):
            y = m_bottom_y + j * cell_size
            grid_lines.add(Line(
                np.array([m_left_x, y, 0]),
                np.array([m_right_x, y, 0]),
                color=self.COLOR_DM,
                stroke_width=1.0,
                stroke_opacity=0.65
            ))

        self.play(Create(grid_lines), run_time=1.2)

        label_10h = Text("10格", font="PingFang SC", font_size=20, color=self.COLOR_DM)
        label_10h.next_to(m_square, DOWN, buff=0.12)
        label_10v = Text("10格", font="PingFang SC", font_size=20, color=self.COLOR_DM)
        label_10v.next_to(m_square, RIGHT, buff=0.12)

        self.play(FadeIn(label_10h), FadeIn(label_10v), run_time=0.4)
        self.wait(0.4)

        # 高亮一个1dm²小方格
        highlight_cell = Square(
            side_length=cell_size,
            color=self.COLOR_DM,
            fill_color=self.COLOR_DM,
            fill_opacity=0.85,
            stroke_width=2
        ).move_to(np.array([m_left_x + cell_size / 2, m_bottom_y + cell_size / 2, 0]))

        cell_label = Text(
            "1dm²",
            font="PingFang SC",
            font_size=12,
            color=WHITE
        ).move_to(highlight_cell.get_center())

        self.play(FadeIn(highlight_cell), run_time=0.4)
        self.play(FadeIn(cell_label), run_time=0.3)
        self.wait(0.4)

        calc_text = Text(
            "每行 10 格，共 10 行",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_TEXT
        ).move_to(DOWN * 5.0)

        self.play(FadeIn(calc_text, shift=UP * 0.2), run_time=0.4)

        calc_formula = MathTex(
            r"10 \times 10 = 100",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.9)

        self.play(Write(calc_formula), run_time=0.6)
        self.wait(0.5)

        conclusion = Text(
            "1平方米 = 100平方分米",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 7.0)

        self.play(FadeIn(conclusion, scale=1.1), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(m_square),
            FadeOut(m_label_top),
            FadeOut(m_label_left),
            FadeOut(grid_lines),
            FadeOut(key_note),
            FadeOut(label_10h),
            FadeOut(label_10v),
            FadeOut(highlight_cell),
            FadeOut(cell_label),
            FadeOut(calc_text),
            FadeOut(calc_formula),
            FadeOut(conclusion),
            run_time=0.7
        )

    # ================================================================
    # 场景5: 为什么进率是100 (二维度量)
    # ================================================================
    def scene_5_why_100(self):
        """解释进率是100而非10的原因"""

        title = Text(
            "为什么进率是100，不是10?",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.3)

        self.play(Write(title), run_time=0.7)

        # --- 长度对比 ---
        len_title = Text(
            "长度单位: 1dm = 10cm",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_DM
        ).move_to(UP * 5.4)

        self.play(FadeIn(len_title), run_time=0.5)

        # 画1dm线段 (表示长度)
        line_y = 4.6
        line_start = np.array([-2.8, line_y, 0])
        line_end = np.array([2.8, line_y, 0])
        line_dm = Line(line_start, line_end, color=self.COLOR_DM, stroke_width=5)

        self.play(Create(line_dm), run_time=0.5)

        # 刻度线 (10等分)
        n = 10
        seg = (2.8 - (-2.8)) / n
        tick_marks = VGroup()
        for i in range(1, n):
            x = -2.8 + i * seg
            tick_marks.add(Line(
                np.array([x, line_y - 0.15, 0]),
                np.array([x, line_y + 0.15, 0]),
                color=self.COLOR_CM,
                stroke_width=2
            ))

        self.play(Create(tick_marks), run_time=0.5)

        # 标注一格
        first_seg_label = Text(
            "1cm",
            font="PingFang SC",
            font_size=17,
            color=self.COLOR_CM
        ).move_to(np.array([-2.8 + seg / 2, line_y + 0.45, 0]))

        self.play(FadeIn(first_seg_label), run_time=0.3)

        len_result = Text(
            "一维: 进率 = 10",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_TEXT
        ).move_to(UP * 3.7)

        self.play(FadeIn(len_result), run_time=0.4)
        self.wait(0.5)

        # 分割线
        divider = Line(
            np.array([-3.8, 3.1, 0]),
            np.array([3.8, 3.1, 0]),
            color=GRAY_B,
            stroke_width=1
        )
        self.play(Create(divider), run_time=0.3)

        # --- 面积对比 ---
        area_title = Text(
            "面积单位: 两个方向都 ×10",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_CM
        ).move_to(UP * 2.6)

        self.play(FadeIn(area_title), run_time=0.5)

        # 小正方形示意
        sq = Square(
            side_length=1.6,
            color=self.COLOR_DM,
            fill_color=self.COLOR_DM,
            fill_opacity=0.12,
            stroke_width=2
        ).move_to(UP * 0.8)

        # 横向箭头
        arr_h = Arrow(
            start=sq.get_left() + LEFT * 0.2,
            end=sq.get_right() + RIGHT * 0.2,
            color=self.COLOR_CM,
            buff=0,
            stroke_width=3
        ).move_to(np.array([0, 0.8 + 1.1, 0]))

        arr_h_label = Text(
            "横向 ×10",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_CM
        ).next_to(arr_h, UP, buff=0.08)

        # 纵向箭头
        arr_v = Arrow(
            start=sq.get_top() + UP * 0.2,
            end=sq.get_bottom() + DOWN * 0.2,
            color=self.COLOR_DM,
            buff=0,
            stroke_width=3
        ).move_to(np.array([1.3, 0.8, 0]))

        arr_v_label = Text(
            "纵向 ×10",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_DM
        ).next_to(arr_v, RIGHT, buff=0.08)

        self.play(Create(sq), run_time=0.5)
        self.play(
            Create(arr_h), FadeIn(arr_h_label),
            Create(arr_v), FadeIn(arr_v_label),
            run_time=0.6
        )
        self.wait(0.4)

        # 核心公式
        core_formula = MathTex(
            r"10 \times 10 = 100",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)

        self.play(Write(core_formula), run_time=0.7)
        self.wait(0.4)

        conclusion_text = Text(
            "面积是二维的！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.7)

        conclusion_sub = Text(
            "所以进率 = 10 × 10 = 100",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_TEXT
        ).move_to(DOWN * 3.5)

        self.play(FadeIn(conclusion_text, scale=1.05), run_time=0.5)
        self.play(FadeIn(conclusion_sub), run_time=0.5)
        self.wait(1.2)

        # 记忆口诀
        mnemonic = Text(
            "记住: 面积进率是 100",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.0)

        self.play(FadeIn(mnemonic, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title),
            FadeOut(len_title),
            FadeOut(line_dm),
            FadeOut(tick_marks),
            FadeOut(first_seg_label),
            FadeOut(len_result),
            FadeOut(divider),
            FadeOut(area_title),
            FadeOut(sq),
            FadeOut(arr_h), FadeOut(arr_h_label),
            FadeOut(arr_v), FadeOut(arr_v_label),
            FadeOut(core_formula),
            FadeOut(conclusion_text),
            FadeOut(conclusion_sub),
            FadeOut(mnemonic),
            run_time=0.7
        )

    # ================================================================
    # 场景6: 换算练习
    # ================================================================
    def scene_6_practice(self):
        """换算练习"""

        title = Text(
            "换算练习",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.3)

        self.play(Write(title), run_time=0.6)

        # 核心公式提示框
        formula_bg = Rectangle(
            width=7.2, height=1.6,
            fill_color="#16213e",
            fill_opacity=1,
            stroke_color=self.COLOR_DM,
            stroke_width=2
        ).move_to(UP * 5.1)

        formula1 = Text(
            "1dm² = 100cm²",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_DM
        ).move_to(UP * 5.45)

        formula2 = Text(
            "1m² = 100dm²",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_M
        ).move_to(UP * 4.75)

        self.play(FadeIn(formula_bg), run_time=0.3)
        self.play(Write(formula1), Write(formula2), run_time=0.6)
        self.wait(0.4)

        # 练习题1: 大→小
        q1_bg = Rectangle(
            width=7.5, height=2.0,
            fill_color="#0f3460",
            fill_opacity=0.6,
            stroke_color=self.COLOR_CM,
            stroke_width=1.5
        ).move_to(UP * 3.2)

        q1_text = Text(
            "5dm² = ____ cm²",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_TEXT
        ).move_to(UP * 3.5)

        q1_hint = Text(
            "1dm²=100cm², 所以×100",
            font="PingFang SC",
            font_size=17,
            color=self.COLOR_SUBTEXT
        ).move_to(UP * 2.9)

        self.play(FadeIn(q1_bg), run_time=0.3)
        self.play(Write(q1_text), run_time=0.5)
        self.play(FadeIn(q1_hint), run_time=0.4)
        self.wait(0.7)

        q1_answer = Text(
            "5 × 100 = 500cm²",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_CM
        ).move_to(UP * 2.1)

        self.play(FadeIn(q1_answer, shift=UP * 0.3, scale=1.1), run_time=0.5)
        self.wait(0.5)

        # 练习题2
        q2_bg = Rectangle(
            width=7.5, height=2.0,
            fill_color="#0f3460",
            fill_opacity=0.6,
            stroke_color=self.COLOR_DM,
            stroke_width=1.5
        ).move_to(UP * 0.9)

        q2_text = Text(
            "3m² = ____ dm²",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_TEXT
        ).move_to(UP * 1.2)

        q2_hint = Text(
            "1m²=100dm², 所以×100",
            font="PingFang SC",
            font_size=17,
            color=self.COLOR_SUBTEXT
        ).move_to(UP * 0.6)

        self.play(FadeIn(q2_bg), run_time=0.3)
        self.play(Write(q2_text), run_time=0.5)
        self.play(FadeIn(q2_hint), run_time=0.4)
        self.wait(0.7)

        q2_answer = Text(
            "3 × 100 = 300dm²",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_DM
        ).move_to(DOWN * 0.2)

        self.play(FadeIn(q2_answer, shift=UP * 0.3, scale=1.1), run_time=0.5)
        self.wait(0.5)

        # 练习题3: 小→大
        q3_bg = Rectangle(
            width=7.5, height=2.0,
            fill_color="#0f3460",
            fill_opacity=0.6,
            stroke_color=self.COLOR_M,
            stroke_width=1.5
        ).move_to(DOWN * 1.5)

        q3_text = Text(
            "200cm² = ____ dm²",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_TEXT
        ).move_to(DOWN * 1.2)

        q3_hint = Text(
            "100cm²=1dm², 所以÷100",
            font="PingFang SC",
            font_size=17,
            color=self.COLOR_SUBTEXT
        ).move_to(DOWN * 1.8)

        self.play(FadeIn(q3_bg), run_time=0.3)
        self.play(Write(q3_text), run_time=0.5)
        self.play(FadeIn(q3_hint), run_time=0.4)
        self.wait(0.7)

        q3_answer = Text(
            "200 ÷ 100 = 2dm²",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_M
        ).move_to(DOWN * 2.6)

        self.play(FadeIn(q3_answer, shift=UP * 0.3, scale=1.1), run_time=0.5)
        self.wait(0.8)

        # 换算技巧提示
        tip1 = Text(
            "大单位 → 小单位：× 100",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.8)

        tip2 = Text(
            "小单位 → 大单位：÷ 100",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.6)

        self.play(FadeIn(tip1), run_time=0.4)
        self.play(FadeIn(tip2), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(title),
            FadeOut(formula_bg),
            FadeOut(formula1),
            FadeOut(formula2),
            FadeOut(q1_bg), FadeOut(q1_text), FadeOut(q1_hint), FadeOut(q1_answer),
            FadeOut(q2_bg), FadeOut(q2_text), FadeOut(q2_hint), FadeOut(q2_answer),
            FadeOut(q3_bg), FadeOut(q3_text), FadeOut(q3_hint), FadeOut(q3_answer),
            FadeOut(tip1), FadeOut(tip2),
            run_time=0.7
        )

    # ================================================================
    # 场景7: 片尾总结
    # ================================================================
    def scene_7_outro(self):
        """片尾总结和关注提示"""

        summary_title = Text(
            "面积单位换算 · 总结",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.8)

        self.play(Write(summary_title), run_time=0.7)

        # 核心知识点三张卡片
        card1_bg = Rectangle(
            width=7.2, height=1.35,
            fill_color=self.COLOR_DM,
            fill_opacity=0.15,
            stroke_color=self.COLOR_DM,
            stroke_width=2
        ).move_to(UP * 4.3)

        card1_text = Text(
            "1dm² = 100cm²",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_DM
        ).move_to(UP * 4.3)

        card2_bg = Rectangle(
            width=7.2, height=1.35,
            fill_color=self.COLOR_M,
            fill_opacity=0.15,
            stroke_color=self.COLOR_M,
            stroke_width=2
        ).move_to(UP * 2.6)

        card2_text = Text(
            "1m² = 100dm²",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_M
        ).move_to(UP * 2.6)

        card3_bg = Rectangle(
            width=7.2, height=1.35,
            fill_color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.12,
            stroke_color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_to(UP * 0.9)

        card3_text = Text(
            "面积进率: 100",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.9)

        self.play(FadeIn(card1_bg), Write(card1_text), run_time=0.5)
        self.play(FadeIn(card2_bg), Write(card2_text), run_time=0.5)
        self.play(FadeIn(card3_bg), Write(card3_text), run_time=0.5)
        self.wait(0.4)

        # 原因说明
        reason = Text(
            "原因: 面积是二维，10×10=100",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_SUBTEXT
        ).move_to(DOWN * 0.4)

        self.play(FadeIn(reason), run_time=0.5)
        self.wait(0.7)

        # 换算方向箭头
        arr_right = Arrow(
            start=np.array([-1.8, -1.8, 0]),
            end=np.array([1.8, -1.8, 0]),
            color=self.COLOR_CM,
            buff=0,
            stroke_width=4
        )
        arr_right_label = Text(
            "大→小  ×100",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_CM
        ).next_to(arr_right, UP, buff=0.1)

        arr_left = Arrow(
            start=np.array([1.8, -2.7, 0]),
            end=np.array([-1.8, -2.7, 0]),
            color=self.COLOR_M,
            buff=0,
            stroke_width=4
        )
        arr_left_label = Text(
            "小→大  ÷100",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_M
        ).next_to(arr_left, DOWN, buff=0.1)

        self.play(Create(arr_right), FadeIn(arr_right_label), run_time=0.5)
        self.play(Create(arr_left), FadeIn(arr_left_label), run_time=0.5)
        self.wait(0.8)

        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.2)

        self.play(FadeIn(follow_text, scale=1.08), run_time=0.6)

        # 作者信息放大显示
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 5.3)

        author_id_big = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_SUBTEXT
        ).move_to(DOWN * 6.1)

        self.play(FadeIn(author_big, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(author_id_big), run_time=0.4)
        self.wait(2.0)

        # 最终淡出
        self.play(
            FadeOut(summary_title),
            FadeOut(card1_bg), FadeOut(card1_text),
            FadeOut(card2_bg), FadeOut(card2_text),
            FadeOut(card3_bg), FadeOut(card3_text),
            FadeOut(reason),
            FadeOut(arr_right), FadeOut(arr_right_label),
            FadeOut(arr_left), FadeOut(arr_left_label),
            FadeOut(follow_text),
            FadeOut(author_big),
            FadeOut(author_id_big),
            FadeOut(self.author_brand),
            run_time=1.0
        )


# 运行命令:
# manim -qm 004_面积单位的换算.py AreaUnitConvertLesson
