"""
001_小数的初步认识.py — 小数的初步认识 教学动画

知识点:
  - 从生活实例（人民币、长度）引入小数
  - 认识小数点, 会读写一位小数
  - 理解一位小数表示十分之几
  - 小数大小比较: 先比整数部分, 再比小数部分

年级: 三年级下册 第七章
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR    = "#1a1a2e"
COLOR_TITLE = "#fbbf24"   # 金黄 标题
COLOR_HL    = "#fbbf24"   # 高亮黄
COLOR_MONEY = "#22c55e"   # 绿色 人民币
COLOR_LEN   = "#3b82f6"   # 蓝色 长度
COLOR_FRAC  = "#e879f9"   # 紫色 分数
COLOR_NUM   = "#f97316"   # 橙色 数字/数轴
COLOR_CMP   = "#ef4444"   # 红色 比较
COLOR_GRAY  = GRAY_A
COLOR_AUTHOR = "#6b7280"
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class DecimalIntroLesson(Scene):
    """
    小数的初步认识教学动画
    场景顺序:
      1. 开场钩子 — 生活中的小数
      2. 认识小数点 — 读写一位小数
      3. 小数的含义 — 表示十分之几
      4. 数轴上的小数
      5. 小数大小比较
      6. 知识总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_reading_writing()
        self.scene_3_meaning()
        self.scene_4_number_line()
        self.scene_5_comparison()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 几何/布局初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """预计算布局坐标, 避免场景内臆想数值"""

        # ===== 数轴参数 =====
        self.nl_center  = np.array([0.0, 0.5, 0.0])   # 数轴中心
        self.nl_x_min   = -3.5
        self.nl_x_max   = 3.5
        self.nl_unit    = 3.0      # 每 1 单位对应的逻辑宽度
        self.nl_x_range = [0, 2, 1]  # Manim NumberLine x_range

        # 数轴 0→1 的像素宽度 = nl_unit / (x_range_span / step)
        # 这里 x_range[2]=1, 所以间距 = nl_unit
        # 0.1 对应 nl_unit * 0.1
        self.nl_tick_10 = self.nl_unit * 0.1   # 0.1 的刻度间距

        # ===== 分数条参数 =====
        self.bar_width  = 7.0
        self.bar_height = 0.7
        self.bar_origin = np.array([-3.5, 0.0, 0.0])  # 左端

        # ===== 验证 =====
        self._verify_geometry()

    def _verify_geometry(self):
        """验证关键几何数值"""
        assert abs(self.nl_unit - 3.0) < 1e-10, "nl_unit 不一致"
        assert abs(self.bar_width - (self.bar_origin[0] * -2)) < 1e-10, "bar_width/bar_origin 不匹配"
        print("Geometry verification passed")

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def make_title_label(self, text, color=WHITE, font_size=36, y=5.5):
        return Text(text, font=FONT, font_size=font_size, color=color).move_to(UP * y)

    def make_subtitle(self, text, y=4.8):
        return Text(text, font=FONT, font_size=22, color=COLOR_GRAY).move_to(UP * y)

    def coin_shape(self, value_str, center, radius=0.55, color=COLOR_MONEY):
        """创建一枚硬币形状（圆 + 数字文本）"""
        circle = Circle(
            radius=radius,
            color=color,
            stroke_width=3,
            fill_color=color,
            fill_opacity=0.18,
        ).move_to(center)
        label = Text(value_str, font=FONT, font_size=24, color=color).move_to(center)
        return VGroup(circle, label)

    def make_decimal_highlight(self, decimal_str, center, font_size=54):
        """创建高亮显示的小数, 小数点用特殊颜色"""
        # 拆分: 整数部分, 小数点, 小数部分
        parts = decimal_str.split(".")
        int_part  = Text(parts[0],  font=FONT, font_size=font_size, color=WHITE)
        dot_part  = Text(".",       font=FONT, font_size=font_size, color=COLOR_HL)
        frac_part = Text(parts[1],  font=FONT, font_size=font_size, color=COLOR_NUM)
        group = VGroup(int_part, dot_part, frac_part).arrange(RIGHT, buff=0.05)
        group.move_to(center)
        return group, dot_part

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        # 作者标识
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook = Text("买东西时看到过这些数吗?", font=FONT, font_size=32, color=COLOR_HL)
        hook.move_to(UP * 5.5)
        self.play(Write(hook), run_time=0.7)

        # 展示三个生活场景中的小数
        # --- 价格标签 3.5元 ---
        price_box = RoundedRectangle(
            width=3.2, height=1.4, corner_radius=0.2,
            color=COLOR_MONEY, stroke_width=2,
            fill_color=COLOR_MONEY, fill_opacity=0.1,
        ).move_to(LEFT * 2.8 + UP * 3.5)

        price_label = VGroup(
            Text("价格", font=FONT, font_size=18, color=COLOR_GRAY),
            Text("3.5 元", font=FONT, font_size=30, color=COLOR_MONEY),
        ).arrange(DOWN, buff=0.1).move_to(price_box.get_center())

        # --- 长度标签 1.2米 ---
        len_box = RoundedRectangle(
            width=3.2, height=1.4, corner_radius=0.2,
            color=COLOR_LEN, stroke_width=2,
            fill_color=COLOR_LEN, fill_opacity=0.1,
        ).move_to(RIGHT * 2.8 + UP * 3.5)

        len_label = VGroup(
            Text("身高", font=FONT, font_size=18, color=COLOR_GRAY),
            Text("1.2 米", font=FONT, font_size=30, color=COLOR_LEN),
        ).arrange(DOWN, buff=0.1).move_to(len_box.get_center())

        # --- 体重标签 0.5千克 ---
        weight_box = RoundedRectangle(
            width=3.2, height=1.4, corner_radius=0.2,
            color=COLOR_FRAC, stroke_width=2,
            fill_color=COLOR_FRAC, fill_opacity=0.1,
        ).move_to(LEFT * 2.8 + UP * 1.8)

        weight_label = VGroup(
            Text("重量", font=FONT, font_size=18, color=COLOR_GRAY),
            Text("0.5 千克", font=FONT, font_size=28, color=COLOR_FRAC),
        ).arrange(DOWN, buff=0.1).move_to(weight_box.get_center())

        # --- 气温 18.6度 ---
        temp_box = RoundedRectangle(
            width=3.2, height=1.4, corner_radius=0.2,
            color=COLOR_NUM, stroke_width=2,
            fill_color=COLOR_NUM, fill_opacity=0.1,
        ).move_to(RIGHT * 2.8 + UP * 1.8)

        temp_label = VGroup(
            Text("气温", font=FONT, font_size=18, color=COLOR_GRAY),
            VGroup(
                Text("18.6", font=FONT, font_size=30, color=COLOR_NUM),
                MathTex(r"^\circ\mathrm{C}", font_size=30, color=COLOR_NUM),
            ).arrange(RIGHT, buff=0.05),
        ).arrange(DOWN, buff=0.1).move_to(temp_box.get_center())

        self.play(
            FadeIn(price_box), FadeIn(price_label),
            FadeIn(len_box), FadeIn(len_label),
            run_time=0.7,
        )
        self.play(
            FadeIn(weight_box), FadeIn(weight_label),
            FadeIn(temp_box), FadeIn(temp_label),
            run_time=0.7,
        )

        # 点出"小数"二字
        reveal = Text(
            "这些都是小数!",
            font=FONT, font_size=36, color=COLOR_HL,
        ).move_to(DOWN * 0.2)

        arrow_up = Arrow(
            reveal.get_top() + UP * 0.1,
            reveal.get_top() + UP * 0.7,
            color=COLOR_HL, stroke_width=3,
            max_tip_length_to_length_ratio=0.25,
        )

        self.play(FadeIn(reveal, shift=UP * 0.3), run_time=0.6)
        self.wait(0.5)

        sub = Text(
            "今天我们一起认识小数!",
            font=FONT, font_size=26, color=COLOR_GRAY,
        ).move_to(DOWN * 1.2)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(price_box), FadeOut(price_label),
            FadeOut(len_box), FadeOut(len_label),
            FadeOut(weight_box), FadeOut(weight_label),
            FadeOut(temp_box), FadeOut(temp_label),
            FadeOut(reveal), FadeOut(sub),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 认识小数点 — 读写一位小数
    # ------------------------------------------------------------------

    def scene_2_reading_writing(self):
        title = self.make_title_label("认识小数点", color=COLOR_TITLE)
        self.play(Write(title), run_time=0.6)

        # 展示 3.5 元
        example_bg = RoundedRectangle(
            width=7.5, height=2.2, corner_radius=0.3,
            color=COLOR_MONEY, stroke_width=2,
            fill_color=COLOR_MONEY, fill_opacity=0.08,
        ).move_to(UP * 3.8)

        money_text = Text("3.5 元", font=FONT, font_size=52, color=COLOR_MONEY)
        money_text.move_to(UP * 3.8)

        self.play(FadeIn(example_bg), run_time=0.4)
        self.play(Write(money_text), run_time=0.8)

        # 用箭头标注小数点
        dot_pos = money_text.get_center() + LEFT * 0.22   # 大致小数点位置
        arrow_dot = Arrow(
            dot_pos + DOWN * 1.2,
            dot_pos + DOWN * 0.35,
            color=COLOR_HL,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.25,
        )
        label_dot = Text("小数点", font=FONT, font_size=26, color=COLOR_HL)
        label_dot.move_to(dot_pos + DOWN * 1.6)

        self.play(Create(arrow_dot), FadeIn(label_dot), run_time=0.6)
        self.wait(0.5)

        # 标注整数部分 和 小数部分
        int_brace = Brace(
            Line(money_text.get_left(), money_text.get_center() + LEFT * 0.25),
            direction=UP, color=COLOR_GRAY,
        )
        int_label = Text("整数部分", font=FONT, font_size=20, color=COLOR_GRAY)
        int_label.next_to(int_brace, UP, buff=0.15)

        dec_brace = Brace(
            Line(money_text.get_center() + RIGHT * 0.08, money_text.get_right()),
            direction=UP, color=COLOR_NUM,
        )
        dec_label = Text("小数部分", font=FONT, font_size=20, color=COLOR_NUM)
        dec_label.next_to(dec_brace, UP, buff=0.15)

        self.play(
            Create(int_brace), FadeIn(int_label),
            Create(dec_brace), FadeIn(dec_label),
            run_time=0.7,
        )
        self.wait(0.8)

        # 读法展示
        read_title = Text("读法:", font=FONT, font_size=26, color=WHITE).move_to(UP * 1.6 + LEFT * 2.5)
        read_text = VGroup(
            Text("3", font=FONT, font_size=36, color=COLOR_MONEY),
            Text(".", font=FONT, font_size=36, color=COLOR_HL),
            Text("5", font=FONT, font_size=36, color=COLOR_NUM),
        ).arrange(RIGHT, buff=0.05)

        arrow_row = VGroup(
            Text("三", font=FONT, font_size=30, color=COLOR_MONEY),
            Text("点", font=FONT, font_size=30, color=COLOR_HL),
            Text("五", font=FONT, font_size=30, color=COLOR_NUM),
        ).arrange(RIGHT, buff=0.15)

        read_group = VGroup(read_text, arrow_row).arrange(DOWN, buff=0.3)
        read_group.move_to(UP * 0.8 + RIGHT * 0.5)

        self.play(FadeIn(read_title), FadeIn(read_group), run_time=0.7)

        # 连线（读音对应）
        for i in range(3):
            arrow = Arrow(
                read_text[i].get_bottom() + DOWN * 0.05,
                arrow_row[i].get_top() + UP * 0.05,
                color=GRAY_B, stroke_width=2,
                max_tip_length_to_length_ratio=0.2,
                buff=0.05,
            )
            self.play(Create(arrow), run_time=0.3)

        read_rule = Text(
            '小数点读作"点", 小数部分逐位读',
            font=FONT, font_size=21, color=COLOR_GRAY,
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(read_rule), run_time=0.5)

        # 更多例子
        examples_title = Text("更多例子", font=FONT, font_size=24, color=COLOR_HL).move_to(DOWN * 1.8)
        self.play(FadeIn(examples_title), run_time=0.4)

        examples = VGroup(
            VGroup(
                Text("0.5", font=FONT, font_size=30, color=WHITE),
                Text("零点五", font=FONT, font_size=22, color=COLOR_GRAY),
            ).arrange(RIGHT, buff=0.4),
            VGroup(
                Text("1.2", font=FONT, font_size=30, color=WHITE),
                Text("一点二", font=FONT, font_size=22, color=COLOR_GRAY),
            ).arrange(RIGHT, buff=0.4),
            VGroup(
                Text("2.8", font=FONT, font_size=30, color=WHITE),
                Text("二点八", font=FONT, font_size=22, color=COLOR_GRAY),
            ).arrange(RIGHT, buff=0.4),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 3.0)

        for ex in examples:
            self.play(FadeIn(ex, shift=RIGHT * 0.3), run_time=0.4)

        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(example_bg), FadeOut(money_text),
            FadeOut(arrow_dot), FadeOut(label_dot),
            FadeOut(int_brace), FadeOut(int_label),
            FadeOut(dec_brace), FadeOut(dec_label),
            FadeOut(read_title), FadeOut(read_group),
            FadeOut(read_rule), FadeOut(examples_title), FadeOut(examples),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 3: 小数的含义 — 表示十分之几
    # ------------------------------------------------------------------

    def scene_3_meaning(self):
        title = self.make_title_label("小数表示十分之几", color=COLOR_TITLE)
        self.play(Write(title), run_time=0.6)

        subtitle = self.make_subtitle("把1元分成10等份, 每份是1角")
        self.play(FadeIn(subtitle), run_time=0.5)

        # -------- 画10等份的分数条 --------
        bar_y = 3.5
        bar_h = 0.65
        bar_w = 7.2
        bar_left = -bar_w / 2

        # 整体外框
        bar_bg = Rectangle(
            width=bar_w, height=bar_h,
            color=WHITE, stroke_width=2,
            fill_color=WHITE, fill_opacity=0.05,
        ).move_to(UP * bar_y)

        self.play(Create(bar_bg), run_time=0.6)

        # 10格
        cell_w = bar_w / 10
        cells = VGroup()
        for i in range(10):
            cell = Rectangle(
                width=cell_w - 0.04, height=bar_h - 0.04,
                color=COLOR_FRAC, stroke_width=1.5,
                fill_color=COLOR_FRAC, fill_opacity=0.0,
            ).move_to(UP * bar_y + LEFT * (bar_w / 2 - cell_w * (i + 0.5)))
            cells.add(cell)

        self.play(Create(cells), run_time=0.8)

        # 标注 1/10 1/10
        tenth_label = VGroup(
            Text("每份是", font=FONT, font_size=20, color=COLOR_GRAY),
            MathTex(r"\frac{1}{10}", font_size=28, color=COLOR_FRAC),
            Text("(即0.1)", font=FONT, font_size=20, color=COLOR_FRAC),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 2.6)

        self.play(FadeIn(tenth_label), run_time=0.5)

        # -------- 动态填色: 3格 → 显示 3/10 = 0.3 --------
        n = 3
        highlight_cells = VGroup()
        for i in range(n):
            hc = Rectangle(
                width=cell_w - 0.04, height=bar_h - 0.04,
                color=COLOR_MONEY, stroke_width=1.5,
                fill_color=COLOR_MONEY, fill_opacity=0.7,
            ).move_to(UP * bar_y + LEFT * (bar_w / 2 - cell_w * (i + 0.5)))
            highlight_cells.add(hc)

        self.play(
            *[FadeIn(hc, scale=0.9) for hc in highlight_cells],
            run_time=0.6,
        )

        # 标注 3/10 = 0.3
        eq1_group = VGroup(
            Text("3格", font=FONT, font_size=26, color=COLOR_MONEY),
            Text("就是", font=FONT, font_size=22, color=COLOR_GRAY),
            MathTex(r"\frac{3}{10}", font_size=36, color=COLOR_FRAC),
            Text("=", font=FONT, font_size=28, color=COLOR_GRAY),
            Text("0.3", font=FONT, font_size=36, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 1.6)

        self.play(FadeIn(eq1_group), run_time=0.7)

        # 人民币类比: 0.3元 = 3角
        money_eq = VGroup(
            Text("0.3 元", font=FONT, font_size=28, color=COLOR_MONEY),
            Text("=", font=FONT, font_size=26, color=COLOR_GRAY),
            Text("3 角", font=FONT, font_size=28, color=COLOR_MONEY),
            Text("=", font=FONT, font_size=26, color=COLOR_GRAY),
            MathTex(r"\frac{3}{10}", font_size=30, color=COLOR_FRAC),
            Text("元", font=FONT, font_size=26, color=COLOR_GRAY),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 0.7)

        self.play(FadeIn(money_eq), run_time=0.6)
        self.wait(0.8)

        # 切换到 0.5 示例
        # 先把3格恢复，再填5格
        new_n = 5
        new_highlight = VGroup()
        for i in range(new_n):
            hc = Rectangle(
                width=cell_w - 0.04, height=bar_h - 0.04,
                color=COLOR_LEN, stroke_width=1.5,
                fill_color=COLOR_LEN, fill_opacity=0.7,
            ).move_to(UP * bar_y + LEFT * (bar_w / 2 - cell_w * (i + 0.5)))
            new_highlight.add(hc)

        eq2_group = VGroup(
            Text("5格", font=FONT, font_size=26, color=COLOR_LEN),
            Text("就是", font=FONT, font_size=22, color=COLOR_GRAY),
            MathTex(r"\frac{5}{10}", font_size=36, color=COLOR_FRAC),
            Text("=", font=FONT, font_size=28, color=COLOR_GRAY),
            Text("0.5", font=FONT, font_size=36, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 1.6)

        money_eq2 = VGroup(
            Text("0.5 元", font=FONT, font_size=28, color=COLOR_LEN),
            Text("=", font=FONT, font_size=26, color=COLOR_GRAY),
            Text("5 角", font=FONT, font_size=28, color=COLOR_LEN),
            Text("=", font=FONT, font_size=26, color=COLOR_GRAY),
            MathTex(r"\frac{5}{10}", font_size=30, color=COLOR_FRAC),
            Text("元", font=FONT, font_size=26, color=COLOR_GRAY),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 0.7)

        self.play(
            ReplacementTransform(highlight_cells, new_highlight),
            ReplacementTransform(eq1_group, eq2_group),
            ReplacementTransform(money_eq, money_eq2),
            run_time=0.8,
        )
        self.wait(1.2)

        # 通用规律
        rule_bg = RoundedRectangle(
            width=7.5, height=1.3, corner_radius=0.25,
            color=COLOR_HL, stroke_width=2,
            fill_color=COLOR_HL, fill_opacity=0.08,
        ).move_to(DOWN * 0.6)

        rule = VGroup(
            Text("一位小数", font=FONT, font_size=26, color=COLOR_HL),
            Text("=", font=FONT, font_size=26, color=COLOR_GRAY),
            Text("十分之几", font=FONT, font_size=26, color=COLOR_FRAC),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.6)

        self.play(FadeIn(rule_bg), FadeIn(rule), run_time=0.6)

        ex_row = VGroup(
            VGroup(
                Text("0.1", font=FONT, font_size=24, color=WHITE),
                Text("=", font=FONT, font_size=20, color=COLOR_GRAY),
                MathTex(r"\frac{1}{10}", font_size=26, color=COLOR_FRAC),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("0.7", font=FONT, font_size=24, color=WHITE),
                Text("=", font=FONT, font_size=20, color=COLOR_GRAY),
                MathTex(r"\frac{7}{10}", font_size=26, color=COLOR_FRAC),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("0.9", font=FONT, font_size=24, color=WHITE),
                Text("=", font=FONT, font_size=20, color=COLOR_GRAY),
                MathTex(r"\frac{9}{10}", font_size=26, color=COLOR_FRAC),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(RIGHT, buff=0.6).move_to(DOWN * 1.8)

        self.play(FadeIn(ex_row), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(bar_bg), FadeOut(cells), FadeOut(new_highlight),
            FadeOut(tenth_label), FadeOut(eq2_group), FadeOut(money_eq2),
            FadeOut(rule_bg), FadeOut(rule), FadeOut(ex_row),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 4: 数轴上的小数
    # ------------------------------------------------------------------

    def scene_4_number_line(self):
        title = self.make_title_label("数轴上找小数", color=COLOR_TITLE)
        self.play(Write(title), run_time=0.6)

        subtitle = self.make_subtitle("0 和 1 之间有哪些小数?")
        self.play(FadeIn(subtitle), run_time=0.5)

        # -------- 画数轴 0~2 --------
        nl = NumberLine(
            x_range=[0, 2, 1],
            length=7.0,
            include_numbers=True,
            numbers_to_include=[0, 1, 2],
            label_direction=DOWN,
            font_size=32,
            color=WHITE,
            stroke_width=3,
        )
        nl.move_to(UP * 3.0)

        self.play(Create(nl), run_time=1.0)

        # 数字标签颜色调整
        for label in nl.numbers:
            label.set_color(COLOR_GRAY)

        # -------- 在 0~1 之间划出10等份刻度 --------
        tick_marks = VGroup()
        tick_y = UP * 3.0
        unit_len = nl.get_unit_size()   # 1单位在坐标系中的长度

        for i in range(1, 10):
            x_pos = nl.n2p(i * 0.1)
            tick = Line(
                x_pos + UP * 0.1,
                x_pos + DOWN * 0.1,
                color=COLOR_LEN,
                stroke_width=1.5,
            )
            tick_marks.add(tick)

        self.play(Create(tick_marks), run_time=0.7)

        # 标注 0.5 的位置
        pos_05 = nl.n2p(0.5)
        dot_05 = Dot(pos_05, radius=0.12, color=COLOR_HL)
        label_05 = Text("0.5", font=FONT, font_size=28, color=COLOR_HL)
        label_05.next_to(dot_05, UP, buff=0.25)

        arrow_05 = Arrow(
            label_05.get_bottom() + DOWN * 0.05,
            dot_05.get_top() + UP * 0.05,
            color=COLOR_HL, stroke_width=2,
            max_tip_length_to_length_ratio=0.3,
            buff=0.05,
        )

        self.play(FadeIn(dot_05, scale=0.5), run_time=0.4)
        self.play(Create(arrow_05), FadeIn(label_05), run_time=0.5)

        # 解释 0.5 在正中间
        mid_explain = Text(
            "0.5 在 0 和 1 的正中间",
            font=FONT, font_size=24, color=COLOR_GRAY,
        ).move_to(UP * 1.8)
        self.play(FadeIn(mid_explain), run_time=0.5)
        self.wait(0.8)

        # 标注 0.3
        pos_03 = nl.n2p(0.3)
        dot_03 = Dot(pos_03, radius=0.10, color=COLOR_MONEY)
        label_03 = Text("0.3", font=FONT, font_size=24, color=COLOR_MONEY)
        label_03.next_to(dot_03, DOWN, buff=0.3)

        # 标注 0.7
        pos_07 = nl.n2p(0.7)
        dot_07 = Dot(pos_07, radius=0.10, color=COLOR_FRAC)
        label_07 = Text("0.7", font=FONT, font_size=24, color=COLOR_FRAC)
        label_07.next_to(dot_07, DOWN, buff=0.3)

        self.play(
            FadeIn(dot_03, scale=0.5), FadeIn(label_03),
            FadeIn(dot_07, scale=0.5), FadeIn(label_07),
            run_time=0.6,
        )
        self.wait(0.8)

        # 展示 1 到 2 之间
        pos_15 = nl.n2p(1.5)
        dot_15 = Dot(pos_15, radius=0.10, color=COLOR_NUM)
        label_15 = Text("1.5", font=FONT, font_size=24, color=COLOR_NUM)
        label_15.next_to(dot_15, UP, buff=0.3)

        explain_2 = Text(
            "1.5 在 1 和 2 之间",
            font=FONT, font_size=24, color=COLOR_GRAY,
        ).move_to(UP * 1.8)

        self.play(
            ReplacementTransform(mid_explain, explain_2),
            FadeIn(dot_15, scale=0.5), FadeIn(label_15),
            run_time=0.7,
        )
        self.wait(1.5)

        # 关键规律
        rule = VGroup(
            Text("整数部分看范围,", font=FONT, font_size=22, color=COLOR_GRAY),
            Text("小数部分定位置!", font=FONT, font_size=22, color=COLOR_HL),
        ).arrange(DOWN, buff=0.15).move_to(UP * 0.6)

        self.play(FadeIn(rule), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(nl), FadeOut(tick_marks),
            FadeOut(dot_05), FadeOut(label_05), FadeOut(arrow_05),
            FadeOut(dot_03), FadeOut(label_03),
            FadeOut(dot_07), FadeOut(label_07),
            FadeOut(dot_15), FadeOut(label_15),
            FadeOut(explain_2), FadeOut(rule),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 5: 小数大小比较
    # ------------------------------------------------------------------

    def scene_5_comparison(self):
        title = self.make_title_label("怎么比较小数大小?", color=COLOR_TITLE)
        self.play(Write(title), run_time=0.6)

        # 规则卡片
        rule_bg = RoundedRectangle(
            width=7.8, height=2.4, corner_radius=0.3,
            color=COLOR_CMP, stroke_width=2,
            fill_color=COLOR_CMP, fill_opacity=0.08,
        ).move_to(UP * 4.0)

        rule_text = VGroup(
            VGroup(
                Text("第", font=FONT, font_size=22, color=COLOR_GRAY),
                Text("1", font=FONT, font_size=26, color=COLOR_HL),
                Text("步: 先比整数部分", font=FONT, font_size=22, color=COLOR_GRAY),
            ).arrange(RIGHT, buff=0.05),
            VGroup(
                Text("第", font=FONT, font_size=22, color=COLOR_GRAY),
                Text("2", font=FONT, font_size=26, color=COLOR_HL),
                Text("步: 整数相同再比小数部分", font=FONT, font_size=22, color=COLOR_GRAY),
            ).arrange(RIGHT, buff=0.05),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(UP * 4.0)

        self.play(FadeIn(rule_bg), FadeIn(rule_text), run_time=0.6)

        # -------- 例1: 1.3 vs 2.5 (整数部分不同) --------
        ex1_title = Text("例1", font=FONT, font_size=28, color=COLOR_HL).move_to(UP * 2.4 + LEFT * 3.0)
        self.play(FadeIn(ex1_title), run_time=0.4)

        num_13 = Text("1.3", font=FONT, font_size=44, color=WHITE).move_to(UP * 2.2 + LEFT * 1.5)
        vs_1   = Text("VS", font=FONT, font_size=36, color=COLOR_GRAY).move_to(UP * 2.2)
        num_25 = Text("2.5", font=FONT, font_size=44, color=WHITE).move_to(UP * 2.2 + RIGHT * 1.5)

        self.play(FadeIn(num_13), FadeIn(vs_1), FadeIn(num_25), run_time=0.5)

        # 高亮整数部分
        box_int_13 = SurroundingRectangle(num_13[0], color=COLOR_CMP, buff=0.1, stroke_width=2)
        box_int_25 = SurroundingRectangle(num_25[0], color=COLOR_CMP, buff=0.1, stroke_width=2)

        self.play(Create(box_int_13), Create(box_int_25), run_time=0.5)

        step1_ex1 = VGroup(
            Text("整数部分:", font=FONT, font_size=22, color=COLOR_GRAY),
            Text("1", font=FONT, font_size=28, color=WHITE),
            Text("<", font=FONT, font_size=28, color=COLOR_CMP),
            Text("2", font=FONT, font_size=28, color=WHITE),
            Text("→ 所以", font=FONT, font_size=22, color=COLOR_GRAY),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 1.3)

        result_ex1 = VGroup(
            Text("1.3", font=FONT, font_size=34, color=COLOR_MONEY),
            Text("<", font=FONT, font_size=36, color=COLOR_CMP),
            Text("2.5", font=FONT, font_size=34, color=COLOR_CMP),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.5)

        self.play(FadeIn(step1_ex1), run_time=0.5)
        self.play(FadeIn(result_ex1), run_time=0.5)
        self.wait(1.0)

        # 清理例1
        self.play(
            FadeOut(ex1_title), FadeOut(num_13), FadeOut(vs_1), FadeOut(num_25),
            FadeOut(box_int_13), FadeOut(box_int_25),
            FadeOut(step1_ex1), FadeOut(result_ex1),
            run_time=0.4,
        )

        # -------- 例2: 1.3 vs 1.7 (整数相同, 比小数部分) --------
        ex2_title = Text("例2", font=FONT, font_size=28, color=COLOR_HL).move_to(UP * 2.4 + LEFT * 3.0)
        self.play(FadeIn(ex2_title), run_time=0.4)

        num_13b = Text("1.3", font=FONT, font_size=44, color=WHITE).move_to(UP * 2.2 + LEFT * 1.5)
        vs_2    = Text("VS", font=FONT, font_size=36, color=COLOR_GRAY).move_to(UP * 2.2)
        num_17  = Text("1.7", font=FONT, font_size=44, color=WHITE).move_to(UP * 2.2 + RIGHT * 1.5)

        self.play(FadeIn(num_13b), FadeIn(vs_2), FadeIn(num_17), run_time=0.5)

        # 整数部分相同
        box_eq_13 = SurroundingRectangle(num_13b[0], color=COLOR_MONEY, buff=0.1, stroke_width=2)
        box_eq_17 = SurroundingRectangle(num_17[0], color=COLOR_MONEY, buff=0.1, stroke_width=2)

        self.play(Create(box_eq_13), Create(box_eq_17), run_time=0.4)

        step1_ex2 = VGroup(
            Text("整数部分:", font=FONT, font_size=22, color=COLOR_GRAY),
            Text("1", font=FONT, font_size=28, color=COLOR_MONEY),
            Text("=", font=FONT, font_size=28, color=COLOR_MONEY),
            Text("1", font=FONT, font_size=28, color=COLOR_MONEY),
            Text("→ 相同! 再比小数部分", font=FONT, font_size=22, color=COLOR_GRAY),
        ).arrange(RIGHT, buff=0.12).move_to(UP * 1.3)

        self.play(FadeIn(step1_ex2), run_time=0.5)

        # 小数部分高亮
        box_dec_13 = SurroundingRectangle(num_13b[2], color=COLOR_CMP, buff=0.1, stroke_width=2)
        box_dec_17 = SurroundingRectangle(num_17[2], color=COLOR_CMP, buff=0.1, stroke_width=2)

        self.play(Create(box_dec_13), Create(box_dec_17), run_time=0.4)

        step2_ex2 = VGroup(
            Text("小数部分:", font=FONT, font_size=22, color=COLOR_GRAY),
            Text("3", font=FONT, font_size=28, color=WHITE),
            Text("<", font=FONT, font_size=28, color=COLOR_CMP),
            Text("7", font=FONT, font_size=28, color=WHITE),
            Text("→ 所以", font=FONT, font_size=22, color=COLOR_GRAY),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 0.5)

        result_ex2 = VGroup(
            Text("1.3", font=FONT, font_size=34, color=COLOR_MONEY),
            Text("<", font=FONT, font_size=36, color=COLOR_CMP),
            Text("1.7", font=FONT, font_size=34, color=COLOR_CMP),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.35)

        self.play(FadeIn(step2_ex2), run_time=0.5)
        self.play(FadeIn(result_ex2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rule_bg), FadeOut(rule_text),
            FadeOut(ex2_title),
            FadeOut(num_13b), FadeOut(vs_2), FadeOut(num_17),
            FadeOut(box_eq_13), FadeOut(box_eq_17),
            FadeOut(step1_ex2),
            FadeOut(box_dec_13), FadeOut(box_dec_17),
            FadeOut(step2_ex2), FadeOut(result_ex2),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 6: 知识总结
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        title = self.make_title_label("知识总结", color=COLOR_TITLE)
        self.play(Write(title), run_time=0.6)

        # 总结卡片背景
        card_bg = RoundedRectangle(
            width=7.8, height=10.0, corner_radius=0.35,
            color=WHITE, stroke_width=2,
            fill_color=WHITE, fill_opacity=0.04,
        ).move_to(UP * 0.0)
        self.play(FadeIn(card_bg), run_time=0.4)

        # ---- 条目1: 小数点 ----
        item1_title = Text("1. 小数点", font=FONT, font_size=27, color=COLOR_HL)
        item1_body = VGroup(
            Text("小数点是小数的标志", font=FONT, font_size=20, color=COLOR_GRAY),
            VGroup(
                Text("例: 3.5", font=FONT, font_size=22, color=WHITE),
                Text("读作三点五", font=FONT, font_size=22, color=COLOR_GRAY),
            ).arrange(RIGHT, buff=0.4),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        item1 = VGroup(item1_title, item1_body).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        item1.move_to(UP * 3.8 + LEFT * 0.4)

        self.play(FadeIn(item1, shift=RIGHT * 0.3), run_time=0.5)

        # ---- 条目2: 含义 ----
        item2_title = Text("2. 含义", font=FONT, font_size=27, color=COLOR_FRAC)
        item2_body = VGroup(
            VGroup(
                Text("0.5", font=FONT, font_size=22, color=WHITE),
                Text("=", font=FONT, font_size=22, color=COLOR_GRAY),
                MathTex(r"\frac{5}{10}", font_size=28, color=COLOR_FRAC),
                Text("(五个十分之一)", font=FONT, font_size=20, color=COLOR_GRAY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("0.3 元", font=FONT, font_size=22, color=COLOR_MONEY),
                Text("=", font=FONT, font_size=20, color=COLOR_GRAY),
                Text("3 角", font=FONT, font_size=22, color=COLOR_MONEY),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        item2 = VGroup(item2_title, item2_body).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        item2.move_to(UP * 2.0 + LEFT * 0.4)

        self.play(FadeIn(item2, shift=RIGHT * 0.3), run_time=0.5)

        # ---- 条目3: 数轴 ----
        item3_title = Text("3. 数轴", font=FONT, font_size=27, color=COLOR_LEN)
        item3_body = VGroup(
            Text("0.5 在 0 和 1 的正中间", font=FONT, font_size=20, color=COLOR_GRAY),
            Text("整数部分确定范围, 小数部分定位", font=FONT, font_size=20, color=COLOR_GRAY),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        item3 = VGroup(item3_title, item3_body).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        item3.move_to(UP * 0.2 + LEFT * 0.4)

        self.play(FadeIn(item3, shift=RIGHT * 0.3), run_time=0.5)

        # ---- 条目4: 比较 ----
        item4_title = Text("4. 大小比较", font=FONT, font_size=27, color=COLOR_CMP)
        item4_body = VGroup(
            VGroup(
                Text("先比", font=FONT, font_size=20, color=COLOR_GRAY),
                Text("整数部分", font=FONT, font_size=20, color=COLOR_HL),
                Text("→ 大则大", font=FONT, font_size=20, color=COLOR_GRAY),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("相同再比", font=FONT, font_size=20, color=COLOR_GRAY),
                Text("小数部分", font=FONT, font_size=20, color=COLOR_HL),
                Text("→ 大则大", font=FONT, font_size=20, color=COLOR_GRAY),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        item4 = VGroup(item4_title, item4_body).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        item4.move_to(DOWN * 1.6 + LEFT * 0.4)

        self.play(FadeIn(item4, shift=RIGHT * 0.3), run_time=0.5)

        # ---- 底部重点 ----
        star = Text("★", font=FONT, font_size=24, color=COLOR_HL)
        key_text = Text(
            "一位小数 = 十分之几",
            font=FONT, font_size=26, color=COLOR_HL,
        )
        key_group = VGroup(star, key_text, star.copy()).arrange(RIGHT, buff=0.2)
        key_group.move_to(DOWN * 3.5)
        self.play(FadeIn(key_group), run_time=0.6)

        self.wait(3.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(item1), FadeOut(item2), FadeOut(item3), FadeOut(item4),
            FadeOut(key_group),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        # 大字作者
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_B,
        ).move_to(UP * 0.6)

        self.play(
            ReplacementTransform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 学更多小学数学!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.5)

        # 小数点装饰动画
        decorations = VGroup()
        for i in range(8):
            angle = i * TAU / 8
            r = 2.2
            pos = DOWN * 3.0 + r * np.array([np.cos(angle), np.sin(angle), 0.0])
            dot = Dot(pos, radius=0.12, color=COLOR_HL, fill_opacity=0.9)
            decorations.add(dot)

        self.play(*[FadeIn(d, scale=0.3) for d in decorations], run_time=0.6)

        # 旋转装饰
        self.play(Rotate(decorations, angle=TAU / 8, run_time=1.2, rate_func=smooth))

        # 展示核心公式
        core = VGroup(
            Text("0.5", font=FONT, font_size=48, color=COLOR_HL),
            Text("=", font=FONT, font_size=40, color=COLOR_GRAY),
            MathTex(r"\frac{5}{10}", font_size=52, color=COLOR_FRAC),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 5.0)

        self.play(FadeIn(core, scale=0.8), run_time=0.6)
        self.wait(2.0)

        # 全部淡出
        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(decorations),
            FadeOut(core),
            run_time=1.0,
        )


# 运行命令:
# manim -pql 001_小数的初步认识.py DecimalIntroLesson   # 快速预览
# manim -qm  001_小数的初步认识.py DecimalIntroLesson   # 中等质量
# manim -qh  001_小数的初步认识.py DecimalIntroLesson   # 高质量
