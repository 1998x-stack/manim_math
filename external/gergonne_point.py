"""
热尔岗点（Gergonne Point）教学动画
使用 Manim 创建的中学几何教学视频

内容: 热尔岗点的定义、构造和性质（塞瓦定理验证）
目标观众: 初中-高中学生
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


class GergonnePoint(Scene):
    """
    热尔岗点教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 定义介绍
    3. 构造过程 - 找切点
    4. 连接线段
    5. 热尔岗点出现
    6. 塞瓦定理验证
    7. 特性总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_TRIANGLE = WHITE
        self.COLOR_INCIRCLE = "#3498db"     # 蓝色 - 内切圆
        self.COLOR_INCENTER = "#e74c3c"     # 红色 - 内心
        self.COLOR_GERGONNE = "#f39c12"    # 橙色 - 热尔岗点
        self.COLOR_TANGENT = "#9b59b6"     # 紫色 - 切点
        self.COLOR_CEVIAN = "#2ecc71"      # 绿色 - 连线
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_HIGHLIGHT = YELLOW
        
        # 初始化几何数据（已验证）
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()         # Scene 1: 开场钩子 (0-5s)
        self.show_definition()      # Scene 2: 定义介绍 (5-12s)
        self.show_tangent_points()  # Scene 3: 找切点 (12-22s)
        self.show_cevians()         # Scene 4: 连接线段 (22-32s)
        self.show_gergonne_point()  # Scene 5: 热尔岗点 (32-42s)
        self.show_ceva_theorem()    # Scene 6: 塞瓦定理 (42-55s)
        self.show_outro()           # Scene 7: 总结与片尾 (55-75s)
    
    def setup_geometry(self):
        """初始化三角形和所有几何元素（使用验证过的坐标）"""
        
        # === 验证过的精确坐标 ===
        self.A = np.array([-2.1250000000, 0.9800000000, 0])
        self.B = np.array([2.3800000000, 0.7250000000, 0])
        self.C = np.array([0.2550000000, 4.1250000000, 0])
        
        # 边长
        self.a = 4.0094419811  # BC
        self.b = 3.9440366378  # CA
        self.c = 4.5122112096  # AB
        
        # 内心与内切圆
        self.I = np.array([0.1618327485, 2.0377172297, 0])
        self.r = 1.1852633270
        
        # 切点
        self.D = np.array([1.1669340396, 2.6659055366, 0])  # BC边切点
        self.E = np.array([-0.7833037971, 2.7529556966, 0])  # CA边切点
        self.F = np.array([0.0948495922, 0.8543481363, 0])  # AB边切点
        
        # 热尔岗点
        self.Ge = np.array([0.1582595838, 2.1493308334, 0])
        
        # 切线长
        self.x = 2.2888082765  # BD = BF
        self.y = 1.7206337046  # CD = CE
        self.z = 2.2234029331  # AE = AF
        
        # 创建三角形对象（但不添加到场景）
        self.triangle = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_TRIANGLE,
            stroke_width=3
        )
    
    def show_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_line1 = Text(
            "连接顶点与内切圆切点，",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        )
        hook_line2 = Text(
            "这三条线会交于一点？",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        )
        hook_text = VGroup(hook_line1, hook_line2).arrange(DOWN, buff=0.3).move_to(UP * 5.5)
        
        self.play(Write(hook_line1), run_time=0.8)
        self.play(FadeIn(hook_line2, shift=UP * 0.2), run_time=0.6)
        
        # 三角形快速创建
        self.play(Create(self.triangle), run_time=1.0)
        
        # 内切圆快速出现
        incircle_preview = Circle(
            radius=self.r,
            color=self.COLOR_INCIRCLE,
            stroke_width=2
        ).move_to(self.I)
        
        self.play(GrowFromCenter(incircle_preview), run_time=0.8)
        
        # 三个切点闪烁
        d_dot = Dot(self.D, radius=0.08, color=self.COLOR_TANGENT)
        e_dot = Dot(self.E, radius=0.08, color=self.COLOR_TANGENT)
        f_dot = Dot(self.F, radius=0.08, color=self.COLOR_TANGENT)
        
        self.play(
            Flash(d_dot, color=self.COLOR_TANGENT, flash_radius=0.3),
            Flash(e_dot, color=self.COLOR_TANGENT, flash_radius=0.3),
            Flash(f_dot, color=self.COLOR_TANGENT, flash_radius=0.3),
            run_time=0.6
        )
        self.add(d_dot, e_dot, f_dot)
        
        # 神秘点出现
        ge_preview = Dot(self.Ge, radius=0.1, color=self.COLOR_GERGONNE)
        self.play(FadeIn(ge_preview, scale=0.5), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(incircle_preview),
            FadeOut(d_dot),
            FadeOut(e_dot),
            FadeOut(f_dot),
            FadeOut(ge_preview),
            run_time=0.4
        )
    
    def show_definition(self):
        """场景2: 定义介绍 (5-12秒)"""
        
        # 标题
        title = Text(
            "热尔岗点",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_GERGONNE
        ).move_to(UP * 6.5)
        
        title_en = Text(
            "Gergonne Point",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(title_en), run_time=0.4)
        
        # 定义文字
        def_line1 = Text("连接三角形顶点与", font="PingFang SC", font_size=24, color=GRAY_A)
        def_line2 = Text("内切圆在对边上切点的", font="PingFang SC", font_size=24, color=GRAY_A)
        def_line3 = Text("三条线段的交点", font="PingFang SC", font_size=24, color=WHITE)
        
        definition = VGroup(def_line1, def_line2, def_line3).arrange(DOWN, buff=0.2).move_to(UP * 4.8)
        
        self.play(FadeIn(definition), run_time=0.5)
        
        # 内切圆及内心
        self.incircle = Circle(
            radius=self.r,
            color=self.COLOR_INCIRCLE,
            stroke_width=2
        ).move_to(self.I)
        
        self.play(Create(self.incircle), run_time=1.2)
        
        self.i_dot = Dot(self.I, color=self.COLOR_INCENTER, radius=0.08)
        i_label = Text("I", font="PingFang SC", font_size=20, color=self.COLOR_INCENTER)
        i_label.next_to(self.i_dot, RIGHT, buff=0.1)
        i_label_cn = Text("内心", font="PingFang SC", font_size=16, color=self.COLOR_INCENTER)
        i_label_cn.next_to(i_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.i_label_group = VGroup(i_label, i_label_cn)
        
        self.play(FadeIn(self.i_dot), run_time=0.3)
        self.play(Write(self.i_label_group), run_time=0.4)
        
        self.wait(1.5)
        
        # 清理文字
        self.play(
            FadeOut(title),
            FadeOut(title_en),
            FadeOut(definition),
            run_time=0.4
        )
    
    def show_tangent_points(self):
        """场景3: 构造过程 - 找切点 (12-22秒)"""
        
        # 步骤标题
        step_text = Text(
            "步骤1: 找到内切圆与三边的切点",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 5.8)
        
        self.play(FadeIn(step_text), run_time=0.5)
        
        explain_text = Text(
            "内心到切点垂直于边",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explain_text), run_time=0.5)
        
        # === BC边的切点D ===
        # 高亮BC边
        bc_line = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        self.play(Create(bc_line), run_time=0.3)
        
        # 切点D出现
        self.d_dot = Dot(self.D, radius=0.08, color=self.COLOR_TANGENT)
        self.play(FadeIn(self.d_dot, scale=0.5), run_time=0.5)
        
        # 垂线ID
        perp_id = DashedLine(self.I, self.D, color=self.COLOR_AUXILIARY, dash_length=0.08)
        self.play(Create(perp_id), run_time=0.6)
        
        # 标签D
        d_label = Text("D", font="PingFang SC", font_size=20, color=self.COLOR_TANGENT)
        d_label.next_to(self.d_dot, UR, buff=0.1)
        self.d_label = d_label
        self.play(FadeIn(d_label), run_time=0.3)
        
        # BC恢复
        self.play(bc_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.2)
        
        # === CA边的切点E ===
        ca_line = Line(self.C, self.A, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        self.play(Create(ca_line), FadeOut(bc_line), run_time=0.3)
        
        self.e_dot = Dot(self.E, radius=0.08, color=self.COLOR_TANGENT)
        self.play(FadeIn(self.e_dot, scale=0.5), run_time=0.5)
        
        perp_ie = DashedLine(self.I, self.E, color=self.COLOR_AUXILIARY, dash_length=0.08)
        self.play(Create(perp_ie), run_time=0.6)
        
        e_label = Text("E", font="PingFang SC", font_size=20, color=self.COLOR_TANGENT)
        e_label.next_to(self.e_dot, UL, buff=0.1)
        self.e_label = e_label
        self.play(FadeIn(e_label), run_time=0.3)
        
        self.play(ca_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.2)
        
        # === AB边的切点F ===
        ab_line = Line(self.A, self.B, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        self.play(Create(ab_line), FadeOut(ca_line), run_time=0.3)
        
        self.f_dot = Dot(self.F, radius=0.08, color=self.COLOR_TANGENT)
        self.play(FadeIn(self.f_dot, scale=0.5), run_time=0.5)
        
        perp_if = DashedLine(self.I, self.F, color=self.COLOR_AUXILIARY, dash_length=0.08)
        self.play(Create(perp_if), run_time=0.6)
        
        f_label = Text("F", font="PingFang SC", font_size=20, color=self.COLOR_TANGENT)
        f_label.next_to(self.f_dot, DOWN, buff=0.1)
        self.f_label = f_label
        self.play(FadeIn(f_label), run_time=0.3)
        
        self.play(ab_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.2)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(step_text),
            FadeOut(explain_text),
            FadeOut(perp_id),
            FadeOut(perp_ie),
            FadeOut(perp_if),
            FadeOut(ab_line),
            run_time=0.4
        )
    
    def show_cevians(self):
        """场景4: 连接线段 (22-32秒)"""
        
        # 步骤标题
        step2_text = Text(
            "步骤2: 连接顶点到对边切点",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 5.8)
        
        self.play(FadeIn(step2_text), run_time=0.5)
        
        explain_line1 = Text("A的对边是BC，切点是D", font="PingFang SC", font_size=20, color=GRAY_A)
        explain_line2 = Text("B的对边是CA，切点是E", font="PingFang SC", font_size=20, color=GRAY_A)
        explain_opposite = VGroup(explain_line1, explain_line2).arrange(DOWN, buff=0.2).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explain_opposite), run_time=0.5)
        
        # === 连接A到D ===
        # A点闪烁
        a_dot_temp = Dot(self.A, radius=0.1, color=self.COLOR_HIGHLIGHT)
        self.play(Flash(a_dot_temp, color=self.COLOR_HIGHLIGHT, flash_radius=0.3), run_time=0.3)
        
        # 线段AD
        self.line_ad = Line(self.A, self.D, color=self.COLOR_CEVIAN, stroke_width=2.5)
        self.play(Create(self.line_ad), run_time=0.8)
        
        # === 连接B到E ===
        b_dot_temp = Dot(self.B, radius=0.1, color=self.COLOR_HIGHLIGHT)
        self.play(Flash(b_dot_temp, color=self.COLOR_HIGHLIGHT, flash_radius=0.3), run_time=0.3)
        
        self.line_be = Line(self.B, self.E, color=self.COLOR_CEVIAN, stroke_width=2.5)
        self.play(Create(self.line_be), run_time=0.8)
        
        # === 连接C到F ===
        c_dot_temp = Dot(self.C, radius=0.1, color=self.COLOR_HIGHLIGHT)
        self.play(Flash(c_dot_temp, color=self.COLOR_HIGHLIGHT, flash_radius=0.3), run_time=0.3)
        
        self.line_cf = Line(self.C, self.F, color=self.COLOR_CEVIAN, stroke_width=2.5)
        self.play(Create(self.line_cf), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(step2_text),
            FadeOut(explain_opposite),
            run_time=0.4
        )
    
    def show_gergonne_point(self):
        """场景5: 热尔岗点出现 (32-42秒)"""
        
        # 内切圆淡化
        self.play(self.incircle.animate.set_opacity(0.3), run_time=0.4)
        
        # 三线高亮
        cevians = VGroup(self.line_ad, self.line_be, self.line_cf)
        self.play(cevians.animate.set_stroke(width=3.5), run_time=0.5)
        
        # 热尔岗点出现
        self.ge_dot = Dot(self.Ge, radius=0.12, color=self.COLOR_GERGONNE)
        self.play(FadeIn(self.ge_dot, scale=0.5), run_time=0.6)
        self.play(Flash(self.ge_dot, color=self.COLOR_GERGONNE, flash_radius=0.4), run_time=0.5)
        
        # 标签
        ge_label = Text("Ge", font="PingFang SC", font_size=24, color=self.COLOR_GERGONNE)
        ge_label.next_to(self.ge_dot, LEFT, buff=0.15)
        ge_label_cn = Text("热尔岗点", font="PingFang SC", font_size=18, color=self.COLOR_GERGONNE)
        ge_label_cn.next_to(ge_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.ge_label_group = VGroup(ge_label, ge_label_cn)
        
        self.play(Write(ge_label), run_time=0.5)
        self.play(FadeIn(ge_label_cn), run_time=0.4)
        
        # 惊叹文字
        amazing_text = Text(
            "三线共点！",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(amazing_text, scale=1.2), run_time=0.6)
        self.wait(1.5)
        
        # 性质文字
        prop_line1 = Text("这就是热尔岗点", font="PingFang SC", font_size=26, color=WHITE)
        prop_line2 = Text("三角形的一个特殊中心", font="PingFang SC", font_size=24, color=GRAY_A)
        property_text = VGroup(prop_line1, prop_line2).arrange(DOWN, buff=0.2).move_to(DOWN * 5.5)
        
        self.play(FadeIn(property_text), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(amazing_text),
            FadeOut(property_text),
            run_time=0.4
        )
    
    def show_ceva_theorem(self):
        """场景6: 塞瓦定理验证 (42-55秒)"""
        
        # 标题
        ceva_title = Text(
            "塞瓦定理验证",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(ceva_title), run_time=0.8)
        
        # 塞瓦定理公式
        ceva_formula = MathTex(
            r"\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1",
            font_size=36
        ).move_to(UP * 5)
        
        self.play(Write(ceva_formula), run_time=1.2)
        
        # 计算说明
        calc_line1 = Text("根据切线长定理:", font="PingFang SC", font_size=22, color=GRAY_A)
        calc_line2 = Text("BD=BF=x, CD=CE=y, AE=AF=z", font="PingFang SC", font_size=22, color=WHITE)
        calc_explain = VGroup(calc_line1, calc_line2).arrange(DOWN, buff=0.2).move_to(UP * 3.8)
        
        self.play(FadeIn(calc_explain), run_time=0.8)
        self.wait(0.8)
        
        # 计算步骤1
        calc_step1 = MathTex(
            r"\frac{x}{y} \cdot \frac{y}{z} \cdot \frac{z}{x}",
            font_size=40
        ).move_to(UP * 2.3)
        
        self.play(FadeIn(calc_step1), run_time=0.8)
        self.wait(0.8)
        
        # 计算步骤2
        calc_step2 = MathTex(
            r"= \frac{xyz}{xyz}",
            font_size=40
        ).move_to(UP * 1.2)
        
        self.play(Write(calc_step2), run_time=1.0)
        self.wait(0.8)
        
        # 结果
        result = MathTex(
            r"= 1",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN)
        
        self.play(FadeIn(result, scale=1.2), run_time=0.8)
        self.play(result.animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.3)
        
        # 成功文字
        success_text = Text(
            "证明成立！",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(success_text), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(ceva_title),
            FadeOut(ceva_formula),
            FadeOut(calc_explain),
            FadeOut(calc_step1),
            FadeOut(calc_step2),
            FadeOut(result),
            FadeOut(success_text),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 特性总结与片尾 (55-75秒)"""
        
        # 三角形和点缩小移上
        all_geometry = VGroup(
            self.triangle,
            self.incircle,
            self.i_dot,
            self.i_label_group,
            self.d_dot,
            self.e_dot,
            self.f_dot,
            self.d_label,
            self.e_label,
            self.f_label,
            self.line_ad,
            self.line_be,
            self.line_cf,
            self.ge_dot,
            self.ge_label_group
        )
        
        self.play(
            all_geometry.animate.scale(0.55).move_to(UP * 4.5),
            run_time=1.0
        )
        
        # 特性标题
        properties_title = Text(
            "热尔岗点的特性",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_GERGONNE
        ).move_to(UP * 2)
        
        self.play(Write(properties_title), run_time=0.6)
        
        # 特性列表
        prop1 = self.create_property_card("✓ 三线共点（塞瓦定理）", UP * 0.8)
        prop2 = self.create_property_card("✓ 内心的等角共轭点", UP * 0)
        prop3 = self.create_property_card("✓ 切点三角形的类似重心", DOWN * 0.8)
        prop4 = self.create_property_card("✓ Kimberling中心 X₇", DOWN * 1.6)
        
        properties_group = VGroup(prop1, prop2, prop3, prop4)
        
        # 依次滑入
        for prop in properties_group:
            self.play(prop.animate.shift(RIGHT * 10), run_time=0.4)
            self.wait(0.2)
        
        self.wait(2.5)
        
        # 清理图形
        self.play(
            FadeOut(all_geometry),
            FadeOut(properties_title),
            FadeOut(properties_group),
            run_time=0.8
        )
        
        # 作者名放大
        large_author = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(
            Transform(self.author_info, large_author),
            run_time=0.8
        )
        
        # ID出现
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注文字
        follow_text = Text(
            "关注我，学更多几何奇点！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰三角形
        triangles = VGroup(*[
            Polygon(
                ORIGIN, RIGHT * 0.3, UP * 0.3,
                color=GOLD,
                fill_opacity=0.8
            ).scale(0.5).move_to(
                follow_text.get_center() + 2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles],
            run_time=0.6
        )
        self.play(Rotate(triangles, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles),
            run_time=1.0
        )
    
    def create_property_card(self, text, position):
        """创建特性卡片"""
        card = Text(
            text,
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        return card


# 运行命令:
# manim -pql gergonne_point.py GergonnePoint  # 快速预览
# manim -qh gergonne_point.py GergonnePoint   # 高质量渲染