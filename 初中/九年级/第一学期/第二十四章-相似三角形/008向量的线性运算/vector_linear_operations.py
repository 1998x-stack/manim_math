"""九年级上学期：向量的线性运算。

首尾相接法与平行四边形法共用终点；斜基底分解按两条实际基向量
求系数并按真实基向量方向绘制，拒绝共线基底。
"""

import math

import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

A = (2.0, 1.0)
B = (1.0, 2.0)
E1 = (1.0, 0.0)
E2 = (0.5, 1.0)


def addition_model(a=A, b=B, origin=(-1.65, 0.2)):
    """统一返回起点、两个分向量端点、首尾相接点和真实和向量端点。"""
    if (len(a) != 2 or len(b) != 2 or len(origin) != 2
            or not all(math.isfinite(v) for p in (a, b, origin) for v in p)):
        raise ValueError("加法只接受有限的二维向量")
    if min(math.hypot(*a), math.hypot(*b),
           math.hypot(a[0]+b[0], a[1]+b[1])) <= 1e-10:
        raise ValueError("本课的箭头演示不接受零长度向量")
    p = tuple(float(x) for x in origin)
    pa = tuple(p[i]+a[i] for i in range(2))
    pb = tuple(p[i]+b[i] for i in range(2))
    sum_end = tuple(p[i]+a[i]+b[i] for i in range(2))
    path_a_then_b = tuple(pa[i]+b[i] for i in range(2))
    path_b_then_a = tuple(pb[i]+a[i] for i in range(2))
    if any(not math.isclose(sum_end[i], other[i], abs_tol=1e-10)
           for other in (path_a_then_b, path_b_then_a) for i in range(2)):
        raise ValueError("加法箭头与平行四边形对角线不吻合")
    return dict(origin=p, a_end=pa, b_end=pb, sum_end=sum_end,
                a_then_b=path_a_then_b, b_then_a=path_b_then_a)


def basis_decomposition(target=A, e1=E1, e2=E2):
    """按实际非共线基向量计算 λ1、λ2 和真实分量；禁止假画正交分量。"""
    if (len(target) != 2 or len(e1) != 2 or len(e2) != 2
            or not all(math.isfinite(x) for vec in (target, e1, e2) for x in vec)):
        raise ValueError("基底与目标向量必须为有限二维向量")
    determinant = e1[0]*e2[1] - e1[1]*e2[0]
    if abs(determinant) <= 1e-10:
        raise ValueError("两基向量共线，无法形成二维基底")
    first = (target[0]*e2[1] - target[1]*e2[0])/determinant
    second = (e1[0]*target[1] - e1[1]*target[0])/determinant
    v1 = tuple(first * x for x in e1)
    v2 = tuple(second * x for x in e2)
    if not all(math.isclose(v1[i]+v2[i], target[i], abs_tol=1e-10)
               for i in range(2)):
        raise ValueError("绘制的斜基底分量与目标向量不一致")
    return first, second, v1, v2


def parallel_relation(a, b):
    """只对非零向量分类同向、反向或不平行，零向量约定另作说明。"""
    if len(a) != 2 or len(b) != 2 or not all(
            math.isfinite(x) for v in (a, b) for x in v):
        raise ValueError("向量应为有限二维坐标")
    lengths = math.hypot(*a)*math.hypot(*b)
    if lengths <= 1e-12:
        raise ValueError("零向量不参与本例非零方向比较")
    cross = a[0]*b[1]-a[1]*b[0]
    if not math.isclose(cross, 0.0, abs_tol=1e-10*lengths):
        return "not_parallel"
    dot = a[0]*b[0]+a[1]*b[1]
    return "same" if dot > 0 else "opposite"


def point3(p):
    return np.array((p[0], p[1], 0.0), dtype=float)


class VectorLinearOperations(Scene):
    FONT = "PingFang SC"
    RED = "#e74c3c"
    BLUE = "#3498db"
    GREEN = "#2ecc71"
    GOLD = "#f39c12"
    PURPLE = "#9b59b6"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = Text("上海初高中数学直通车 @emptyandcalm",
                                font=self.FONT, font_size=19,
                                color=GRAY_B).move_to(UP*7.0)
        self.add(self.author_info)
        self.addition = addition_model()
        self.coefficients = basis_decomposition()
        if (self.coefficients[0], self.coefficients[1]) != (1.5, 1.0):
            raise ValueError("斜基底分解数据与教学例题不一致")
        if parallel_relation((1.2, .6), (2.4, 1.2)) != "same":
            raise ValueError("平行向量的正倍数例题不一致")
        self.show_opening()
        self.show_vector_addition()
        self.show_scalar_multiplication()
        self.show_basis_concept()
        self.show_vector_decomposition()
        self.show_parallel_vectors()
        self.show_summary()

    def clear_section(self, keep_author=True):
        visible = [mob for mob in self.mobjects
                   if not keep_author or mob is not self.author_info]
        if visible:
            self.play(*[FadeOut(mob) for mob in visible], run_time=0.45)

    def heading(self, title, subtitle=None):
        self.play(Write(Text(title, font=self.FONT, font_size=32,
                             color=YELLOW).move_to(UP*5.8)), run_time=0.55)
        if subtitle:
            self.play(FadeIn(Text(subtitle, font=self.FONT, font_size=23,
                                  color=GRAY_A).move_to(UP*4.9)), run_time=0.35)

    def arrow(self, start, end, color):
        if math.dist(start, end) <= 1e-10:
            raise ValueError("不能用退化 Arrow 展示零向量")
        return Arrow(point3(start), point3(end), color=color,
                     stroke_width=5, buff=0)

    def show_opening(self):
        self.heading("向量可以相加、数乘和分解")
        p = self.addition
        arrows = VGroup(
            self.arrow(p["origin"], p["a_end"], self.RED),
            self.arrow(p["origin"], p["b_end"], self.BLUE),
            self.arrow(p["origin"], p["sum_end"], self.GREEN),
        )
        self.play(*[GrowArrow(arrow) for arrow in arrows], run_time=1)
        self.wait(0.65)
        self.clear_section()

    def show_vector_addition(self):
        self.heading("向量加法：首尾相接与平行四边形法则")
        p = self.addition
        a_arrow = self.arrow(p["origin"], p["a_end"], self.RED)
        b_arrow = self.arrow(p["origin"], p["b_end"], self.BLUE)
        label_a = MathTex(r"\vec a", color=self.RED,
                          font_size=29).next_to(a_arrow, DOWN, buff=0.1)
        label_b = MathTex(r"\vec b", color=self.BLUE,
                          font_size=29).next_to(b_arrow, LEFT, buff=0.1)
        self.play(GrowArrow(a_arrow), GrowArrow(b_arrow),
                  Write(label_a), Write(label_b), run_time=0.85)
        translated = self.arrow(p["a_end"], p["a_then_b"], self.BLUE)
        self.play(GrowArrow(translated), run_time=0.65)
        resultant = self.arrow(p["origin"], p["sum_end"], self.GREEN)
        self.play(GrowArrow(resultant), run_time=0.65)
        # 另一条平行四边形边由 b 终点平移 a 得到。
        fourth = DashedLine(point3(p["b_end"]), point3(p["b_then_a"]),
                            color=GRAY_A, dash_length=0.12)
        self.play(Create(fourth), run_time=0.5)
        formula = MathTex(r"\vec a+\vec b=(3,3)",
                          font_size=37, color=YELLOW).move_to(DOWN*3.8)
        self.play(Write(formula), run_time=0.7)
        self.wait(0.9)
        self.clear_section()

    def show_scalar_multiplication(self):
        self.heading("数乘：系数决定长度和方向")
        original = (1.3, .7)
        start = (-1.7, .55)
        base = self.arrow(start, tuple(start[i]+original[i] for i in range(2)),
                          self.RED)
        doubled = self.arrow(start, tuple(start[i]+2*original[i] for i in range(2)),
                             self.BLUE)
        opposite = self.arrow(start, tuple(start[i]-original[i] for i in range(2)),
                              self.PURPLE)
        self.play(GrowArrow(base), run_time=0.6)
        self.play(GrowArrow(doubled), run_time=0.7)
        self.play(GrowArrow(opposite), run_time=0.7)
        formula = MathTex(r"|2\vec a|=2|\vec a|,\quad|-\vec a|=|\vec a|",
                          font_size=31, color=YELLOW).move_to(DOWN*3.75)
        note = Text("2 倍同向，负 1 倍反向", font=self.FONT,
                    font_size=25).move_to(DOWN*4.9)
        self.play(Write(formula), FadeIn(note), run_time=0.8)
        self.wait(0.85)
        self.clear_section()

    def show_basis_concept(self):
        self.heading("二维基底：两条不共线的向量", "本例使用 e₁=(1,0)，e₂=(0.5,1)")
        first, second, _, _ = self.coefficients
        if not math.isclose(first, 1.5) or not math.isclose(second, 1):
            raise ValueError("基底系数不匹配")
        origin = (-1.8, .3)
        e1 = self.arrow(origin, (origin[0]+E1[0], origin[1]+E1[1]), self.GOLD)
        e2 = self.arrow(origin, (origin[0]+E2[0], origin[1]+E2[1]), self.PURPLE)
        texts = VGroup(
            MathTex(r"\vec e_1=(1,0)", font_size=32, color=self.GOLD),
            MathTex(r"\vec e_2=(0.5,1)", font_size=32, color=self.PURPLE),
        ).arrange(DOWN, buff=0.6).move_to(DOWN*3.4)
        self.play(GrowArrow(e1), GrowArrow(e2), run_time=0.85)
        self.play(*[Write(text) for text in texts], run_time=0.75)
        self.wait(0.85)
        self.clear_section()

    def show_vector_decomposition(self):
        self.heading("斜基底分解：沿真实 e₁、e₂ 方向", "先求系数，再画向量首尾相接")
        first, second, v1, v2 = self.coefficients
        origin = (-1.8, .3)
        first_end = tuple(origin[i]+v1[i] for i in range(2))
        result_end = tuple(first_end[i]+v2[i] for i in range(2))
        if not all(math.isclose(result_end[i], origin[i]+A[i], abs_tol=1e-10)
                   for i in range(2)):
            raise ValueError("分量图示的终点与目标向量不吻合")
        first_arrow = self.arrow(origin, first_end, self.GOLD)
        second_arrow = self.arrow(first_end, result_end, self.PURPLE)
        target = self.arrow(origin, result_end, self.RED)
        self.play(GrowArrow(first_arrow), run_time=0.65)
        self.play(GrowArrow(second_arrow), run_time=0.65)
        self.play(GrowArrow(target), run_time=0.65)
        formula = MathTex(r"\vec a=1.5\vec e_1+\vec e_2=(2,1)",
                          font_size=32, color=YELLOW).move_to(DOWN*3.8)
        note = Text("第二分量是 (0.5,1)，不是 (0,1)", font=self.FONT,
                    font_size=23).move_to(DOWN*4.9)
        self.play(Write(formula), FadeIn(note), run_time=0.8)
        self.wait(0.9)
        self.clear_section()

    def show_parallel_vectors(self):
        self.heading("非零平行向量：方向相同或相反")
        base = (1.2, .6)
        origin = (-1.6, .3)
        first = self.arrow(origin, tuple(origin[i]+base[i] for i in range(2)),
                           self.RED)
        positive = self.arrow(origin, tuple(origin[i]+2*base[i] for i in range(2)),
                              self.BLUE)
        negative = self.arrow(origin, tuple(origin[i]-base[i] for i in range(2)),
                              self.PURPLE)
        if (parallel_relation(base, tuple(2*x for x in base)) != "same"
                or parallel_relation(base, tuple(-x for x in base)) != "opposite"):
            raise ValueError("平行向量的屏幕方向错误")
        self.play(GrowArrow(first), GrowArrow(positive), run_time=0.9)
        self.play(GrowArrow(negative), run_time=0.65)
        formula = MathTex(r"\vec b=2\vec a,\quad \vec c=-\vec a",
                          font_size=33, color=YELLOW).move_to(DOWN*3.85)
        note = Text("本镜只比较非零向量的方向", font=self.FONT,
                    font_size=23).move_to(DOWN*4.9)
        self.play(Write(formula), FadeIn(note), run_time=0.8)
        self.wait(0.9)
        self.clear_section()

    def show_summary(self):
        self.heading("线性运算总结")
        notes = VGroup(
            Text("加法：首尾相接，平行四边形对角线", font=self.FONT,
                 font_size=25),
            Text("数乘：实数决定伸缩与方向", font=self.FONT, font_size=25),
            Text("二维基底：两条不共线向量", font=self.FONT, font_size=25),
            Text("分解：系数乘实际基向量后相加", font=self.FONT,
                 font_size=25),
        ).arrange(DOWN, buff=0.75).move_to(UP*.4)
        self.play(*[FadeIn(note) for note in notes], run_time=1)
        self.wait(0.75)
        self.clear_section(keep_author=False)


# manim -ql vector_linear_operations.py VectorLinearOperations
