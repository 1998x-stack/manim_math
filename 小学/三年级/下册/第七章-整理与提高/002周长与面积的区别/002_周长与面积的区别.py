"""
002_周长与面积的区别.py — 周长与面积的区别 教学动画

知识点:
  - 周长: 一周的长度（一维），用长度单位 m、cm
  - 面积: 面的大小（二维），用平方单位 m²、cm²
  - 计算方法: 周长 = 边长之和; 面积 = 长 × 宽
  - 核心区别: 一个是"线"的概念，一个是"面"的概念

年级: 三年级下册
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
BG_COLOR      = "#1a1a2e"
COLOR_PERIMETER = "#3b82f6"   # 蓝色 — 周长
COLOR_AREA      = "#22c55e"   # 绿色 — 面积
COLOR_HL        = "#fbbf24"   # 黄色高亮
COLOR_RECT      = "#e2e8f0"   # 矩形边框色
COLOR_FILL      = "#22c55e"   # 填充色（面积）
COLOR_FORMULA   = "#f8fafc"   # 公式白色
COLOR_AUTHOR    = "#6b7280"   # 灰色作者
COLOR_UNIT_LEN  = "#60a5fa"   # 长度单位色
COLOR_UNIT_AREA = "#4ade80"   # 面积单位色
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class PerimeterAreaDiffLesson(Scene):
    """
    周长与面积的区别教学动画
    场景顺序:
      1. 开场钩子 — 周长和面积, 傻傻分不清?
      2. 认识周长 — 一周的长度
      3. 认识面积 — 面的大小
      4. 同一个矩形, 对比周长与面积
      5. 计算公式
      6. 单位对比
      7. 知识总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_perimeter()
        self.scene_3_area()
        self.scene_4_comparison()
        self.scene_5_formulas()
        self.scene_6_units()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化矩形几何数据"""
        # 主矩形参数 (逻辑单位)
        self.RECT_W = 4.0       # 宽 (格: 4)
        self.RECT_H = 2.5       # 高 (格: 2.5)
        self.RECT_CENTER = np.array([0.0, 1.5, 0.0])

        # 矩形四个顶点 (精确计算)
        hw = self.RECT_W / 2
        hh = self.RECT_H / 2
        cx, cy = self.RECT_CENTER[0], self.RECT_CENTER[1]

        self.BL = np.array([cx - hw, cy - hh, 0.0])  # 左下
        self.BR = np.array([cx + hw, cy - hh, 0.0])  # 右下
        self.TR = np.array([cx + hw, cy + hh, 0.0])  # 右上
        self.TL = np.array([cx - hw, cy + hh, 0.0])  # 左上

        # 周长和面积
        self.PERIMETER = 2 * (self.RECT_W + self.RECT_H)   # 13
        self.AREA      = self.RECT_W * self.RECT_H          # 10

        # 单元格大小 (面积演示用 1×1 格)
        self.CELL = 1.0

        # 验证
        self._verify_geometry()

    def _verify_geometry(self):
        """验证几何关系"""
        # 矩形边长验证
        w = np.linalg.norm(self.BR - self.BL)
        h = np.linalg.norm(self.TL - self.BL)
        assert abs(w - self.RECT_W) < 1e-10, f"宽度错误: {w}"
        assert abs(h - self.RECT_H) < 1e-10, f"高度错误: {h}"

        # 直角验证: BL→BR 与 BL→TL 垂直
        v1 = self.BR - self.BL
        v2 = self.TL - self.BL
        dot = np.dot(v1[:2], v2[:2])
        assert abs(dot) < 1e-10, f"矩形不是直角: dot={dot}"

        print("Geometry verification passed")

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT,
            font_size=18,
            color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def make_rect(self, w, h, center, color=COLOR_RECT, fill_color=None,
                  fill_opacity=0.0, stroke_width=3):
        """创建矩形 Mobject，中心对齐到 center"""
        rect = Rectangle(
            width=w, height=h,
            color=color,
            stroke_width=stroke_width,
            fill_color=fill_color if fill_color else color,
            fill_opacity=fill_opacity,
        )
        rect.move_to(center)
        return rect

    def make_grid(self, w, h, center, cell=1.0, color=COLOR_AREA, opacity=0.35):
        """在矩形内画网格线，用于面积演示"""
        lines = VGroup()
        cols = int(round(w / cell))
        rows = int(round(h / cell))
        x0 = center[0] - w / 2
        y0 = center[1] - h / 2

        for i in range(1, cols):
            x = x0 + i * cell
            lines.add(Line(
                np.array([x, y0, 0.0]),
                np.array([x, y0 + h, 0.0]),
                color=color, stroke_width=1.5, stroke_opacity=opacity,
            ))
        for j in range(1, rows):
            y = y0 + j * cell
            lines.add(Line(
                np.array([x0, y, 0.0]),
                np.array([x0 + w, y, 0.0]),
                color=color, stroke_width=1.5, stroke_opacity=opacity,
            ))
        return lines

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text(
            "周长 vs 面积",
            font=FONT, font_size=52, color=COLOR_HL,
        ).move_to(UP * 5.2)

        sub = Text(
            "你真的分清了吗?",
            font=FONT, font_size=30, color=GRAY_A,
        ).move_to(UP * 4.3)

        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)

        # 两个视觉概念同时显示
        # 左: 周长 (只画边)
        rect_outline = self.make_rect(3.2, 2.0, LEFT * 2.0 + UP * 1.8,
                                      color=COLOR_PERIMETER, stroke_width=5)

        label_peri = Text("周长", font=FONT, font_size=26, color=COLOR_PERIMETER)
        label_peri.next_to(rect_outline, DOWN, buff=0.3)

        # 右: 面积 (填充)
        rect_filled = self.make_rect(3.2, 2.0, RIGHT * 2.0 + UP * 1.8,
                                     color=COLOR_AREA, fill_color=COLOR_AREA,
                                     fill_opacity=0.5, stroke_width=3)

        label_area = Text("面积", font=FONT, font_size=26, color=COLOR_AREA)
        label_area.next_to(rect_filled, DOWN, buff=0.3)

        self.play(
            Create(rect_outline),
            Create(rect_filled),
            run_time=1.0,
        )
        self.play(
            FadeIn(label_peri),
            FadeIn(label_area),
            run_time=0.5,
        )

        question = Text(
            "它们有什么区别?",
            font=FONT, font_size=26, color=COLOR_FORMULA,
        ).move_to(DOWN * 3.8)

        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(hook), FadeOut(sub),
            FadeOut(rect_outline), FadeOut(rect_filled),
            FadeOut(label_peri), FadeOut(label_area),
            FadeOut(question),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 认识周长
    # ------------------------------------------------------------------

    def scene_2_perimeter(self):
        title = Text("什么是周长?", font=FONT, font_size=38, color=COLOR_PERIMETER)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 核心定义
        defn = Text(
            "周长 = 围着图形一圈的长度",
            font=FONT, font_size=26, color=GRAY_A,
        ).move_to(UP * 4.6)
        self.play(FadeIn(defn), run_time=0.5)

        # 画矩形 (只有轮廓)
        center = np.array([0.0, 1.8, 0.0])
        rect = self.make_rect(self.RECT_W, self.RECT_H, center,
                               color=COLOR_RECT, stroke_width=4)
        self.play(Create(rect), run_time=0.8)

        # 用动态描边动画沿着边走一圈, 表示"一周"
        # 构建路径: BL → BR → TR → TL → BL
        BL = self.BL + (center - self.RECT_CENTER)
        BR = self.BR + (center - self.RECT_CENTER)
        TR = self.TR + (center - self.RECT_CENTER)
        TL = self.TL + (center - self.RECT_CENTER)

        path_segments = [
            Line(BL, BR, color=COLOR_PERIMETER, stroke_width=8),
            Line(BR, TR, color=COLOR_PERIMETER, stroke_width=8),
            Line(TR, TL, color=COLOR_PERIMETER, stroke_width=8),
            Line(TL, BL, color=COLOR_PERIMETER, stroke_width=8),
        ]

        explain_walk = Text(
            "沿着边走一圈...",
            font=FONT, font_size=24, color=COLOR_PERIMETER,
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(explain_walk), run_time=0.3)

        for seg in path_segments:
            self.play(Create(seg), run_time=0.4)

        self.wait(0.5)
        self.play(FadeOut(explain_walk), run_time=0.3)

        # 标注每条边长
        brace_bottom = Brace(
            Line(BL, BR), direction=DOWN, color=COLOR_HL, buff=0.1,
        )
        brace_bottom_label = VGroup(
            Text("4", font=FONT, font_size=24, color=COLOR_HL),
            Text("cm", font=FONT, font_size=20, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.05)
        brace_bottom_label.next_to(brace_bottom, DOWN, buff=0.1)

        brace_right = Brace(
            Line(BR, TR), direction=RIGHT, color=COLOR_HL, buff=0.1,
        )
        brace_right_label = VGroup(
            Text("2.5", font=FONT, font_size=22, color=COLOR_HL),
            Text("cm", font=FONT, font_size=18, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.05)
        brace_right_label.next_to(brace_right, RIGHT, buff=0.1)

        self.play(
            FadeIn(brace_bottom), FadeIn(brace_bottom_label),
            FadeIn(brace_right), FadeIn(brace_right_label),
            run_time=0.7,
        )

        # 周长公式
        formula_line1 = VGroup(
            Text("周长", font=FONT, font_size=26, color=COLOR_PERIMETER),
            MathTex(r"= 4 + 2.5 + 4 + 2.5", font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 4.5)

        formula_line2 = VGroup(
            Text("周长", font=FONT, font_size=26, color=COLOR_PERIMETER),
            MathTex(r"= 13 \text{ cm}", font_size=26, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 5.3)

        self.play(FadeIn(formula_line1, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(formula_line2, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(defn),
            FadeOut(rect),
            *[FadeOut(s) for s in path_segments],
            FadeOut(brace_bottom), FadeOut(brace_bottom_label),
            FadeOut(brace_right), FadeOut(brace_right_label),
            FadeOut(formula_line1), FadeOut(formula_line2),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 认识面积
    # ------------------------------------------------------------------

    def scene_3_area(self):
        title = Text("什么是面积?", font=FONT, font_size=38, color=COLOR_AREA)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        defn = Text(
            "面积 = 图形所占面的大小",
            font=FONT, font_size=26, color=GRAY_A,
        ).move_to(UP * 4.6)
        self.play(FadeIn(defn), run_time=0.5)

        # 画矩形 (带填充)
        center = np.array([0.0, 1.8, 0.0])
        rect_fill = self.make_rect(
            self.RECT_W, self.RECT_H, center,
            color=COLOR_RECT, fill_color=COLOR_AREA,
            fill_opacity=0.0, stroke_width=4,
        )
        self.play(Create(rect_fill), run_time=0.6)

        # 填充动画: 面积是内部的"面"
        explain_fill = Text(
            "面积是里面的部分",
            font=FONT, font_size=24, color=COLOR_AREA,
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(explain_fill), run_time=0.4)
        self.play(
            rect_fill.animate.set_fill(color=COLOR_AREA, opacity=0.5),
            run_time=1.0,
        )
        self.wait(0.4)
        self.play(FadeOut(explain_fill), run_time=0.3)

        # 网格: 用1cm²小方块填满, 理解面积
        grid = self.make_grid(self.RECT_W, self.RECT_H, center,
                               cell=self.CELL, color=COLOR_AREA, opacity=0.6)
        self.play(Create(grid), run_time=0.8)

        grid_explain = Text(
            "用 1cm² 小方格来量",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(grid_explain), run_time=0.4)

        # 标注 4×2.5 = 10 个格
        brace_w = Brace(
            Line(
                center + LEFT * self.RECT_W/2 + DOWN * self.RECT_H/2,
                center + RIGHT * self.RECT_W/2 + DOWN * self.RECT_H/2,
            ),
            direction=DOWN, color=COLOR_HL, buff=0.1,
        )
        brace_w_label = VGroup(
            Text("4", font=FONT, font_size=24, color=COLOR_HL),
            Text("cm", font=FONT, font_size=20, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.05)
        brace_w_label.next_to(brace_w, DOWN, buff=0.1)

        brace_h = Brace(
            Line(
                center + LEFT * self.RECT_W/2 + DOWN * self.RECT_H/2,
                center + LEFT * self.RECT_W/2 + UP * self.RECT_H/2,
            ),
            direction=LEFT, color=COLOR_HL, buff=0.1,
        )
        brace_h_label = VGroup(
            Text("2.5", font=FONT, font_size=22, color=COLOR_HL),
            Text("cm", font=FONT, font_size=18, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.05)
        brace_h_label.next_to(brace_h, LEFT, buff=0.1)

        self.play(
            FadeIn(brace_w), FadeIn(brace_w_label),
            FadeIn(brace_h), FadeIn(brace_h_label),
            run_time=0.7,
        )

        # 面积公式
        formula_line1 = VGroup(
            Text("面积", font=FONT, font_size=26, color=COLOR_AREA),
            MathTex(r"= 4 \times 2.5", font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 4.8)

        formula_line2 = VGroup(
            Text("面积", font=FONT, font_size=26, color=COLOR_AREA),
            MathTex(r"= 10 \text{ cm}^2", font_size=26, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 5.6)

        self.play(FadeIn(formula_line1, shift=UP * 0.2), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(formula_line2, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(defn),
            FadeOut(rect_fill), FadeOut(grid),
            FadeOut(grid_explain),
            FadeOut(brace_w), FadeOut(brace_w_label),
            FadeOut(brace_h), FadeOut(brace_h_label),
            FadeOut(formula_line1), FadeOut(formula_line2),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 4: 对比演示 — 同一个矩形
    # ------------------------------------------------------------------

    def scene_4_comparison(self):
        title = Text("一起来对比!", font=FONT, font_size=36, color=COLOR_HL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        subtitle = Text(
            "同一个矩形, 两个不同的概念",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(UP * 4.8)
        self.play(FadeIn(subtitle), run_time=0.4)

        center = np.array([0.0, 2.0, 0.0])
        BL = center + np.array([-self.RECT_W/2, -self.RECT_H/2, 0])
        BR = center + np.array([ self.RECT_W/2, -self.RECT_H/2, 0])
        TR = center + np.array([ self.RECT_W/2,  self.RECT_H/2, 0])
        TL = center + np.array([-self.RECT_W/2,  self.RECT_H/2, 0])

        # 基础矩形
        rect_base = Rectangle(
            width=self.RECT_W, height=self.RECT_H,
            color=COLOR_RECT, stroke_width=4,
        ).move_to(center)

        self.play(Create(rect_base), run_time=0.8)

        # === 第一步: 高亮周长 (边) ===
        peri_label = Text(
            "周长: 边的总长度",
            font=FONT, font_size=26, color=COLOR_PERIMETER,
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(peri_label), run_time=0.4)

        # 四条边依次高亮
        edges = [
            Line(BL, BR, color=COLOR_PERIMETER, stroke_width=8),
            Line(BR, TR, color=COLOR_PERIMETER, stroke_width=8),
            Line(TR, TL, color=COLOR_PERIMETER, stroke_width=8),
            Line(TL, BL, color=COLOR_PERIMETER, stroke_width=8),
        ]
        for e in edges:
            self.play(Create(e), run_time=0.3)

        peri_value = VGroup(
            Text("周长", font=FONT, font_size=26, color=COLOR_PERIMETER),
            MathTex(r"= 13 \text{ cm}", font_size=28, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 4.2)
        self.play(FadeIn(peri_value, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 淡出周长高亮
        self.play(
            *[FadeOut(e) for e in edges],
            FadeOut(peri_label), FadeOut(peri_value),
            run_time=0.4,
        )

        # === 第二步: 高亮面积 (填充) ===
        area_label = Text(
            "面积: 里面的大小",
            font=FONT, font_size=26, color=COLOR_AREA,
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(area_label), run_time=0.4)

        rect_filled = Rectangle(
            width=self.RECT_W, height=self.RECT_H,
            color=COLOR_RECT, stroke_width=4,
            fill_color=COLOR_AREA, fill_opacity=0.0,
        ).move_to(center)

        self.play(
            rect_filled.animate.set_fill(opacity=0.55),
            run_time=1.0,
        )
        self.add(rect_base)  # ensure outline on top

        area_value = VGroup(
            Text("面积", font=FONT, font_size=26, color=COLOR_AREA),
            MathTex(r"= 10 \text{ cm}^2", font_size=28, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 4.2)
        self.play(FadeIn(area_value, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # === 第三步: 关键区别强调 ===
        self.play(FadeOut(area_label), FadeOut(area_value), run_time=0.3)

        key_box = RoundedRectangle(
            width=7.8, height=2.2,
            corner_radius=0.25,
            color=COLOR_HL, stroke_width=2,
            fill_color="#1e293b", fill_opacity=0.95,
        ).move_to(DOWN * 4.0)

        key_line1 = VGroup(
            Text("周长:", font=FONT, font_size=22, color=COLOR_PERIMETER),
            Text("线的长度（一维）", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.2)

        key_line2 = VGroup(
            Text("面积:", font=FONT, font_size=22, color=COLOR_AREA),
            Text("面的大小（二维）", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.2)

        key_content = VGroup(key_line1, key_line2).arrange(DOWN, buff=0.3)
        key_content.move_to(key_box.get_center())

        self.play(FadeIn(key_box), run_time=0.4)
        self.play(FadeIn(key_content, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(rect_base), FadeOut(rect_filled),
            FadeOut(key_box), FadeOut(key_content),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 5: 计算公式
    # ------------------------------------------------------------------

    def scene_5_formulas(self):
        title = Text("计算公式", font=FONT, font_size=38, color=COLOR_HL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 周长公式卡
        peri_card = RoundedRectangle(
            width=7.5, height=3.2,
            corner_radius=0.3,
            color=COLOR_PERIMETER, stroke_width=2.5,
            fill_color="#0c1a3a", fill_opacity=0.95,
        ).move_to(UP * 2.8)

        peri_icon = Text("周长", font=FONT, font_size=30, color=COLOR_PERIMETER)
        peri_icon.move_to(peri_card.get_top() + DOWN * 0.55)

        peri_formula_1 = VGroup(
            Text("周长", font=FONT, font_size=24, color=WHITE),
            MathTex(r"=", font_size=26, color=WHITE),
            Text("边长之和", font=FONT, font_size=24, color=COLOR_PERIMETER),
        ).arrange(RIGHT, buff=0.15)

        peri_formula_2 = VGroup(
            Text("长方形周长", font=FONT, font_size=22, color=GRAY_A),
            MathTex(r"= (l + w) \times 2", font_size=24, color=COLOR_PERIMETER),
        ).arrange(RIGHT, buff=0.15)

        peri_formulas = VGroup(peri_formula_1, peri_formula_2).arrange(DOWN, buff=0.3)
        peri_formulas.move_to(peri_card.get_center() + DOWN * 0.3)

        self.play(FadeIn(peri_card), run_time=0.4)
        self.play(Write(peri_icon), run_time=0.4)
        self.play(FadeIn(peri_formulas, shift=UP * 0.2), run_time=0.7)
        self.wait(0.5)

        # 面积公式卡
        area_card = RoundedRectangle(
            width=7.5, height=3.2,
            corner_radius=0.3,
            color=COLOR_AREA, stroke_width=2.5,
            fill_color="#0a2a1a", fill_opacity=0.95,
        ).move_to(DOWN * 1.0)

        area_icon = Text("面积", font=FONT, font_size=30, color=COLOR_AREA)
        area_icon.move_to(area_card.get_top() + DOWN * 0.55)

        area_formula_1 = VGroup(
            Text("面积", font=FONT, font_size=24, color=WHITE),
            MathTex(r"=", font_size=26, color=WHITE),
            Text("长", font=FONT, font_size=24, color=COLOR_AREA),
            MathTex(r"\times", font_size=26, color=WHITE),
            Text("宽", font=FONT, font_size=24, color=COLOR_AREA),
        ).arrange(RIGHT, buff=0.15)

        area_formula_2 = VGroup(
            Text("长方形面积", font=FONT, font_size=22, color=GRAY_A),
            MathTex(r"= l \times w", font_size=24, color=COLOR_AREA),
        ).arrange(RIGHT, buff=0.15)

        area_formulas = VGroup(area_formula_1, area_formula_2).arrange(DOWN, buff=0.3)
        area_formulas.move_to(area_card.get_center() + DOWN * 0.3)

        self.play(FadeIn(area_card), run_time=0.4)
        self.play(Write(area_icon), run_time=0.4)
        self.play(FadeIn(area_formulas, shift=UP * 0.2), run_time=0.7)
        self.wait(0.5)

        # 示例计算
        example_box = RoundedRectangle(
            width=7.5, height=2.0,
            corner_radius=0.2,
            color=COLOR_HL, stroke_width=1.5,
            fill_color="#1e1a00", fill_opacity=0.9,
        ).move_to(DOWN * 4.2)

        example_text = VGroup(
            Text("例: 长4cm 宽2.5cm 的长方形", font=FONT, font_size=20, color=GRAY_A),
        ).move_to(example_box.get_center() + UP * 0.3)

        example_values = VGroup(
            VGroup(
                Text("周长=", font=FONT, font_size=20, color=COLOR_PERIMETER),
                MathTex(r"13\text{cm}", font_size=22, color=COLOR_HL),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("面积=", font=FONT, font_size=20, color=COLOR_AREA),
                MathTex(r"10\text{cm}^2", font_size=22, color=COLOR_HL),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.8).move_to(example_box.get_center() + DOWN * 0.3)

        self.play(FadeIn(example_box), run_time=0.3)
        self.play(FadeIn(example_text), FadeIn(example_values), run_time=0.6)
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(peri_card), FadeOut(peri_icon), FadeOut(peri_formulas),
            FadeOut(area_card), FadeOut(area_icon), FadeOut(area_formulas),
            FadeOut(example_box), FadeOut(example_text), FadeOut(example_values),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 6: 单位对比
    # ------------------------------------------------------------------

    def scene_6_units(self):
        title = Text("单位不一样!", font=FONT, font_size=38, color=COLOR_HL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        subtitle = Text(
            "这是最容易搞错的地方",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 4.7)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 周长单位 (长度单位)
        peri_unit_title = Text("周长用 长度单位",
                                font=FONT, font_size=28, color=COLOR_PERIMETER)
        peri_unit_title.move_to(UP * 3.5)
        self.play(FadeIn(peri_unit_title, shift=RIGHT * 0.3), run_time=0.5)

        peri_units = VGroup(
            Text("cm", font=FONT, font_size=32, color=COLOR_UNIT_LEN),
            Text("m", font=FONT, font_size=32, color=COLOR_UNIT_LEN),
            Text("mm", font=FONT, font_size=32, color=COLOR_UNIT_LEN),
        ).arrange(RIGHT, buff=0.8).move_to(UP * 2.6)

        peri_unit_desc = Text(
            "（厘米、米、毫米……）",
            font=FONT, font_size=20, color=GRAY_B,
        ).move_to(UP * 1.9)

        # 直线示意: 周长是一维的
        line_demo = Line(
            LEFT * 2.5 + UP * 1.2,
            RIGHT * 2.5 + UP * 1.2,
            color=COLOR_PERIMETER, stroke_width=6,
        )
        line_brace = Brace(line_demo, direction=DOWN, color=COLOR_UNIT_LEN, buff=0.05)
        line_brace_label = Text("一维长度", font=FONT, font_size=20, color=COLOR_UNIT_LEN)
        line_brace_label.next_to(line_brace, DOWN, buff=0.1)

        self.play(FadeIn(peri_units), run_time=0.5)
        self.play(FadeIn(peri_unit_desc), run_time=0.4)
        self.play(Create(line_demo), run_time=0.5)
        self.play(FadeIn(line_brace), FadeIn(line_brace_label), run_time=0.4)
        self.wait(0.8)

        # 分隔线
        sep = Line(LEFT * 3.8, RIGHT * 3.8, color=GRAY_D, stroke_width=1.5)
        sep.move_to(DOWN * 0.3)
        self.play(Create(sep), run_time=0.3)

        # 面积单位 (平方单位)
        area_unit_title = Text("面积用 平方单位",
                                font=FONT, font_size=28, color=COLOR_AREA)
        area_unit_title.move_to(DOWN * 1.0)
        self.play(FadeIn(area_unit_title, shift=RIGHT * 0.3), run_time=0.5)

        area_units = VGroup(
            MathTex(r"\text{cm}^2", font_size=32, color=COLOR_UNIT_AREA),
            MathTex(r"\text{m}^2", font_size=32, color=COLOR_UNIT_AREA),
            MathTex(r"\text{mm}^2", font_size=32, color=COLOR_UNIT_AREA),
        ).arrange(RIGHT, buff=0.8).move_to(DOWN * 1.9)

        area_unit_desc = Text(
            "（平方厘米、平方米……）",
            font=FONT, font_size=20, color=GRAY_B,
        ).move_to(DOWN * 2.7)

        # 正方形示意: 面积是二维的
        sq_demo = Square(side_length=1.2, color=COLOR_AREA, stroke_width=3,
                          fill_color=COLOR_AREA, fill_opacity=0.4)
        sq_demo.move_to(DOWN * 4.0)

        sq_label = MathTex(r"1\text{cm}^2", font_size=22, color=COLOR_UNIT_AREA)
        sq_label.next_to(sq_demo, RIGHT, buff=0.2)

        sq_desc = Text("二维面积", font=FONT, font_size=20, color=COLOR_UNIT_AREA)
        sq_desc.next_to(sq_demo, DOWN, buff=0.15)

        self.play(FadeIn(area_units), run_time=0.5)
        self.play(FadeIn(area_unit_desc), run_time=0.4)
        self.play(FadeIn(sq_demo), FadeIn(sq_label), FadeIn(sq_desc), run_time=0.6)

        # 核心提示
        tip = Text(
            "单位写错, 整道题都错!",
            font=FONT, font_size=24, color=COLOR_HL,
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(peri_unit_title), FadeOut(peri_units), FadeOut(peri_unit_desc),
            FadeOut(line_demo), FadeOut(line_brace), FadeOut(line_brace_label),
            FadeOut(sep),
            FadeOut(area_unit_title), FadeOut(area_units), FadeOut(area_unit_desc),
            FadeOut(sq_demo), FadeOut(sq_label), FadeOut(sq_desc),
            FadeOut(tip),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 7: 知识总结
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        title = Text("知识总结", font=FONT, font_size=38, color=COLOR_HL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 大卡片背景
        card_bg = RoundedRectangle(
            width=8.0, height=9.5,
            corner_radius=0.35,
            color=GRAY_D, stroke_width=1.5,
            fill_color="#0f172a", fill_opacity=0.97,
        ).move_to(UP * 0.0)
        self.play(FadeIn(card_bg), run_time=0.4)

        # —— 对比表 ——
        header_peri = Text("周长", font=FONT, font_size=28, color=COLOR_PERIMETER)
        header_vs    = Text("VS", font=FONT, font_size=24, color=GRAY_A)
        header_area  = Text("面积", font=FONT, font_size=28, color=COLOR_AREA)
        header_row = VGroup(header_peri, header_vs, header_area).arrange(RIGHT, buff=1.0)
        header_row.move_to(UP * 3.8)
        self.play(FadeIn(header_row), run_time=0.5)

        # 分隔线
        div1 = Line(LEFT * 3.6, RIGHT * 3.6, color=GRAY_D, stroke_width=1)
        div1.move_to(UP * 3.0)
        self.play(Create(div1), run_time=0.3)

        # 行1: 含义
        row1_label = Text("含义", font=FONT, font_size=22, color=GRAY_A).move_to(UP * 2.4 + LEFT * 3.2)
        row1_peri  = Text("一周的长度", font=FONT, font_size=22, color=COLOR_PERIMETER).move_to(UP * 2.4 + LEFT * 0.5)
        row1_area  = Text("面的大小", font=FONT, font_size=22, color=COLOR_AREA).move_to(UP * 2.4 + RIGHT * 2.5)
        self.play(FadeIn(row1_label), FadeIn(row1_peri), FadeIn(row1_area), run_time=0.5)

        div2 = Line(LEFT * 3.6, RIGHT * 3.6, color=GRAY_D, stroke_width=0.8, stroke_opacity=0.5)
        div2.move_to(UP * 1.7)
        self.play(Create(div2), run_time=0.2)

        # 行2: 维度
        row2_label = Text("维度", font=FONT, font_size=22, color=GRAY_A).move_to(UP * 1.1 + LEFT * 3.2)
        row2_peri  = Text("一维（线）", font=FONT, font_size=22, color=COLOR_PERIMETER).move_to(UP * 1.1 + LEFT * 0.5)
        row2_area  = Text("二维（面）", font=FONT, font_size=22, color=COLOR_AREA).move_to(UP * 1.1 + RIGHT * 2.5)
        self.play(FadeIn(row2_label), FadeIn(row2_peri), FadeIn(row2_area), run_time=0.5)

        div3 = Line(LEFT * 3.6, RIGHT * 3.6, color=GRAY_D, stroke_width=0.8, stroke_opacity=0.5)
        div3.move_to(UP * 0.4)
        self.play(Create(div3), run_time=0.2)

        # 行3: 公式
        row3_label  = Text("公式", font=FONT, font_size=22, color=GRAY_A).move_to(DOWN * 0.2 + LEFT * 3.2)
        row3_peri   = VGroup(
            Text("边长", font=FONT, font_size=20, color=COLOR_PERIMETER),
            Text("之和", font=FONT, font_size=20, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 0.2 + LEFT * 0.5)
        row3_area   = VGroup(
            Text("长", font=FONT, font_size=20, color=COLOR_AREA),
            MathTex(r"\times", font_size=20, color=WHITE),
            Text("宽", font=FONT, font_size=20, color=COLOR_AREA),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 0.2 + RIGHT * 2.5)
        self.play(FadeIn(row3_label), FadeIn(row3_peri), FadeIn(row3_area), run_time=0.5)

        div4 = Line(LEFT * 3.6, RIGHT * 3.6, color=GRAY_D, stroke_width=0.8, stroke_opacity=0.5)
        div4.move_to(DOWN * 0.9)
        self.play(Create(div4), run_time=0.2)

        # 行4: 单位
        row4_label = Text("单位", font=FONT, font_size=22, color=GRAY_A).move_to(DOWN * 1.5 + LEFT * 3.2)
        row4_peri  = VGroup(
            Text("cm", font=FONT, font_size=22, color=COLOR_UNIT_LEN),
            Text("、m…", font=FONT, font_size=20, color=GRAY_A),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 1.5 + LEFT * 0.5)
        row4_area  = VGroup(
            MathTex(r"\text{cm}^2", font_size=22, color=COLOR_UNIT_AREA),
            Text("、", font=FONT, font_size=18, color=GRAY_A),
            MathTex(r"\text{m}^2", font_size=22, color=COLOR_UNIT_AREA),
            Text("…", font=FONT, font_size=18, color=GRAY_A),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 1.5 + RIGHT * 2.5)
        self.play(FadeIn(row4_label), FadeIn(row4_peri), FadeIn(row4_area), run_time=0.5)

        div5 = Line(LEFT * 3.6, RIGHT * 3.6, color=GRAY_D, stroke_width=0.8, stroke_opacity=0.5)
        div5.move_to(DOWN * 2.2)
        self.play(Create(div5), run_time=0.2)

        # 小图示 (下方)
        mini_outline = Rectangle(
            width=1.6, height=1.0, color=COLOR_PERIMETER, stroke_width=5,
        ).move_to(DOWN * 3.1 + LEFT * 1.5)
        mini_fill = Rectangle(
            width=1.6, height=1.0,
            color=COLOR_AREA, stroke_width=2,
            fill_color=COLOR_AREA, fill_opacity=0.5,
        ).move_to(DOWN * 3.1 + RIGHT * 1.5)
        mini_label_p = Text("边框=周长", font=FONT, font_size=17, color=COLOR_PERIMETER)
        mini_label_p.next_to(mini_outline, DOWN, buff=0.15)
        mini_label_a = Text("填充=面积", font=FONT, font_size=17, color=COLOR_AREA)
        mini_label_a.next_to(mini_fill, DOWN, buff=0.15)

        self.play(
            FadeIn(mini_outline), FadeIn(mini_fill),
            FadeIn(mini_label_p), FadeIn(mini_label_a),
            run_time=0.6,
        )

        # 记忆口诀
        tip_box = RoundedRectangle(
            width=7.6, height=1.2,
            corner_radius=0.2,
            color=COLOR_HL, stroke_width=1.5,
            fill_color="#1e1200", fill_opacity=0.9,
        ).move_to(DOWN * 5.0)

        tip_text = Text(
            "周长绕一圈, 面积铺满面!",
            font=FONT, font_size=24, color=COLOR_HL,
        ).move_to(tip_box.get_center())

        self.play(FadeIn(tip_box), FadeIn(tip_text, shift=UP * 0.2), run_time=0.6)
        self.wait(3.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(header_row),
            FadeOut(div1), FadeOut(div2), FadeOut(div3), FadeOut(div4), FadeOut(div5),
            FadeOut(row1_label), FadeOut(row1_peri), FadeOut(row1_area),
            FadeOut(row2_label), FadeOut(row2_peri), FadeOut(row2_area),
            FadeOut(row3_label), FadeOut(row3_peri), FadeOut(row3_area),
            FadeOut(row4_label), FadeOut(row4_peri), FadeOut(row4_area),
            FadeOut(mini_outline), FadeOut(mini_fill),
            FadeOut(mini_label_p), FadeOut(mini_label_a),
            FadeOut(tip_box), FadeOut(tip_text),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE,
        ).move_to(UP * 1.0)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_B,
        ).move_to(UP * 0.0)

        self.play(
            ReplacementTransform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 学更多小学数学!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 装饰: 小矩形（周长+面积）交替出现
        deco_group = VGroup()
        positions = [
            LEFT * 2.8 + DOWN * 3.2,
            LEFT * 1.0 + DOWN * 3.5,
            RIGHT * 0.8 + DOWN * 3.2,
            RIGHT * 2.6 + DOWN * 3.5,
        ]
        colors_list = [COLOR_PERIMETER, COLOR_AREA, COLOR_PERIMETER, COLOR_AREA]
        fills_list  = [0.0, 0.5, 0.0, 0.5]

        for pos, col, fill_op in zip(positions, colors_list, fills_list):
            r = Rectangle(
                width=0.9, height=0.6,
                color=col, stroke_width=3,
                fill_color=col, fill_opacity=fill_op,
            ).move_to(pos)
            deco_group.add(r)

        self.play(
            *[FadeIn(d, scale=0.5) for d in deco_group],
            run_time=0.8,
        )
        self.wait(2.0)

        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(deco_group),
            run_time=1.0,
        )


# ======================================================================
# 运行命令
# ======================================================================
# manim -pql 002_周长与面积的区别.py PerimeterAreaDiffLesson   # 快速预览
# manim -qm 002_周长与面积的区别.py PerimeterAreaDiffLesson    # 中等质量
# manim -qh 002_周长与面积的区别.py PerimeterAreaDiffLesson    # 高质量
