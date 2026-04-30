"""
圆的确定 - Circle Determination (Three Points Determine a Circle)
使用 Manim 创建的九年级几何教学视频

内容: 不在同一直线上的三点确定一个圆、外接圆、外心
目标观众: 九年级学生
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


class CircleDetermination(Scene):
    """
    圆的确定教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 共线检查（反例）
    3. 非共线三点
    4. 垂直平分线AB
    5. 垂直平分线BC
    6. 外心出现
    7. 外接圆绘制
    8. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_TRIANGLE = "#3498db"      # 蓝色 - 三角形
        self.COLOR_CIRCLE = "#e74c3c"        # 红色 - 外接圆
        self.COLOR_CIRCUMCENTER = "#f39c12"  # 橙色 - 外心
        self.COLOR_PERP_BISECTOR = "#2ecc71" # 绿色 - 垂直平分线
        self.COLOR_RADIUS = "#9b59b6"        # 紫色 - 半径
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_collinear_check()
        self.show_non_collinear()
        self.show_perpendicular_bisector_AB()
        self.show_perpendicular_bisector_BC()
        self.show_circumcenter()
        self.show_circumcircle()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化三角形及所有几何元素"""
        # 基准参数
        self.SCALE = 0.85
        self.OFFSET = UP * 1.5
        
        # 三角形顶点（使用斜三角形）
        self.A = np.array([-2.5, 0, 0]) * self.SCALE + self.OFFSET
        self.B = np.array([2.5, -1, 0]) * self.SCALE + self.OFFSET
        self.C = np.array([0, 2.5, 0]) * self.SCALE + self.OFFSET
        
        # 计算中点
        self.M_AB = (self.A + self.B) / 2
        self.M_BC = (self.B + self.C) / 2
        self.M_CA = (self.C + self.A) / 2
        
        # 计算外心
        self.O = self.calculate_circumcenter(self.A, self.B, self.C)
        self.radius = np.linalg.norm(self.O - self.A)
        
        # 验证几何关系
        self.verify_geometry()
        
        print("✓ 几何初始化完成")
    
    def calculate_circumcenter(self, A, B, C):
        """使用解析公式精确计算外心"""
        ax, ay = A[0], A[1]
        bx, by = B[0], B[1]
        cx, cy = C[0], C[1]
        
        # 计算行列式
        D = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        
        if abs(D) < 1e-10:
            # 三点共线，退化情况
            print("WARNING: 三点接近共线！")
            return (A + B + C) / 3
        
        # 计算外心坐标
        ux = ((ax**2 + ay**2) * (by - cy) + 
              (bx**2 + by**2) * (cy - ay) + 
              (cx**2 + cy**2) * (ay - by)) / D
        
        uy = ((ax**2 + ay**2) * (cx - bx) + 
              (bx**2 + by**2) * (ax - cx) + 
              (cx**2 + cy**2) * (bx - ax)) / D
        
        return np.array([ux, uy, 0])
    
    def are_collinear(self, P1, P2, P3):
        """验证三点是否共线"""
        area = 0.5 * abs(
            P1[0] * (P2[1] - P3[1]) + 
            P2[0] * (P3[1] - P1[1]) + 
            P3[0] * (P1[1] - P2[1])
        )
        return area < 1e-6
    
    def perpendicular_bisector_endpoints(self, P1, P2, length=3.5):
        """计算垂直平分线的端点"""
        midpoint = (P1 + P2) / 2
        segment = P2 - P1
        # 垂直方向（旋转90度）
        perpendicular = np.array([-segment[1], segment[0], 0])
        perpendicular = perpendicular / np.linalg.norm(perpendicular)
        
        start = midpoint - perpendicular * length / 2
        end = midpoint + perpendicular * length / 2
        
        return start, end, midpoint
    
    def create_right_angle_mark(self, corner, point1, point2, size=0.2):
        """创建直角标记"""
        vec1 = (point1 - corner)
        vec1 = vec1 / np.linalg.norm(vec1) * size
        vec2 = (point2 - corner)
        vec2 = vec2 / np.linalg.norm(vec2) * size
        
        return Polygon(
            corner,
            corner + vec1,
            corner + vec1 + vec2,
            corner + vec2,
            color=YELLOW,
            stroke_width=1.5,
            fill_opacity=0
        )
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 1. 验证三点不共线
        if self.are_collinear(self.A, self.B, self.C):
            print("WARNING: 三角形顶点共线！")
        
        # 2. 验证外心到三顶点距离相等
        dist_OA = np.linalg.norm(self.O - self.A)
        dist_OB = np.linalg.norm(self.O - self.B)
        dist_OC = np.linalg.norm(self.O - self.C)
        
        if abs(dist_OA - dist_OB) > epsilon:
            print(f"WARNING: 外心到A和B距离不等! OA={dist_OA:.6f}, OB={dist_OB:.6f}")
        if abs(dist_OB - dist_OC) > epsilon:
            print(f"WARNING: 外心到B和C距离不等! OB={dist_OB:.6f}, OC={dist_OC:.6f}")
        
        # 3. 验证外心在AB垂直平分线上
        start_AB, end_AB, mid_AB = self.perpendicular_bisector_endpoints(self.A, self.B)
        # 计算点到直线的距离
        line_vec = end_AB - start_AB
        point_vec = self.O - start_AB
        cross_product = abs(np.cross(point_vec[:2], line_vec[:2]))
        dist_to_line = cross_product / np.linalg.norm(line_vec)
        
        if dist_to_line > epsilon:
            print(f"WARNING: 外心不在AB垂直平分线上! 距离={dist_to_line:.6f}")
        
        print("✓ 几何验证通过")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "三个点，能画出一个圆吗？",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 三个点依次出现（临时位置）
        temp_A = LEFT * 2 + UP * 0.5
        temp_B = RIGHT * 2 + DOWN * 0.5
        temp_C = UP * 2
        
        self.dot_A = Dot(temp_A, color=WHITE, radius=0.12)
        self.dot_B = Dot(temp_B, color=WHITE, radius=0.12)
        self.dot_C = Dot(temp_C, color=WHITE, radius=0.12)
        
        self.play(
            FadeIn(self.dot_A, scale=0.5),
            run_time=0.4
        )
        self.play(
            FadeIn(self.dot_B, scale=0.5),
            run_time=0.4
        )
        self.play(
            FadeIn(self.dot_C, scale=0.5),
            run_time=0.4
        )
        
        # 问号
        question_mark = Text("?", font_size=60, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 2)
        self.play(FadeIn(question_mark, scale=1.2), run_time=0.4)
        self.play(Indicate(question_mark, scale_factor=1.3), run_time=0.5)
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_mark),
            run_time=0.4
        )
    
    def show_collinear_check(self):
        """场景2: 共线检查（反例）"""
        # 小标题
        subtitle = Text(
            "条件：三点不能共线",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.5)
        
        # 将点移动到共线位置
        collinear_A = LEFT * 3
        collinear_B = ORIGIN
        collinear_C = RIGHT * 3
        
        self.play(
            self.dot_A.animate.move_to(collinear_A),
            self.dot_B.animate.move_to(collinear_B),
            self.dot_C.animate.move_to(collinear_C),
            run_time=1.0
        )
        
        # 连接成线
        collinear_line = Line(
            collinear_A, collinear_C,
            color=self.COLOR_AUXILIARY,
            stroke_width=3
        )
        self.play(Create(collinear_line), run_time=0.5)
        
        # 叉号
        cross_mark = VGroup(
            Line(UL * 0.5, DR * 0.5, color=RED, stroke_width=8),
            Line(UR * 0.5, DL * 0.5, color=RED, stroke_width=8)
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(cross_mark, scale=0.5), run_time=0.4)
        
        # 说明文字
        explanation = Text(
            "共线的点无法确定圆",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(collinear_line),
            FadeOut(cross_mark),
            FadeOut(explanation),
            FadeOut(subtitle),
            run_time=0.5
        )
    
    def show_non_collinear(self):
        """场景3: 非共线三点"""
        # 说明
        explanation = Text(
            "不共线的三点 ✓",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 移动到正确位置
        self.play(
            self.dot_A.animate.move_to(self.A),
            self.dot_B.animate.move_to(self.B),
            self.dot_C.animate.move_to(self.C),
            run_time=1.0
        )
        
        # 对勾
        check_mark = VGroup(
            Line(ORIGIN, RIGHT * 0.3 + DOWN * 0.3, color=GREEN, stroke_width=8),
            Line(RIGHT * 0.3 + DOWN * 0.3, RIGHT * 0.8 + UP * 0.5, color=GREEN, stroke_width=8)
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(check_mark, scale=0.5), run_time=0.4)
        
        # 连接成三角形
        self.triangle = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_TRIANGLE,
            stroke_width=3
        )
        
        self.play(Create(self.triangle), run_time=1.0)
        
        # 顶点标注
        label_A = Text("A", font="PingFang SC", font_size=20, color=WHITE).next_to(
            self.dot_A, LEFT, buff=0.15
        )
        label_B = Text("B", font="PingFang SC", font_size=20, color=WHITE).next_to(
            self.dot_B, RIGHT, buff=0.15
        )
        label_C = Text("C", font="PingFang SC", font_size=20, color=WHITE).next_to(
            self.dot_C, UP, buff=0.15
        )
        
        self.play(
            FadeIn(label_A),
            FadeIn(label_B),
            FadeIn(label_C),
            run_time=0.5
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(explanation),
            FadeOut(check_mark),
            FadeOut(label_A),
            FadeOut(label_B),
            FadeOut(label_C),
            run_time=0.5
        )
    
    def show_perpendicular_bisector_AB(self):
        """场景4: 垂直平分线AB"""
        # 小标题
        subtitle = Text(
            "寻找外心 - 垂直平分线",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_CIRCUMCENTER
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # AB边高亮
        line_AB = Line(self.A, self.B, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        self.play(Create(line_AB), run_time=0.6)
        
        # 中点M
        dot_M = Dot(self.M_AB, color=WHITE, radius=0.08)
        label_M = Text("M", font="PingFang SC", font_size=18, color=WHITE).next_to(
            dot_M, DOWN, buff=0.1
        )
        
        self.play(
            FadeIn(dot_M, scale=0.5),
            FadeIn(label_M),
            run_time=0.6
        )
        
        # 垂直平分线
        start_AB, end_AB, _ = self.perpendicular_bisector_endpoints(self.A, self.B, length=3.5)
        
        self.perp_bisector_AB = DashedLine(
            start_AB, end_AB,
            color=self.COLOR_PERP_BISECTOR,
            dash_length=0.1,
            stroke_width=3
        )
        
        self.play(GrowFromCenter(self.perp_bisector_AB), run_time=1.0)
        
        # 直角标记
        right_angle_mark = self.create_right_angle_mark(
            self.M_AB,
            self.A,
            start_AB,
            size=0.15
        )
        
        self.play(FadeIn(right_angle_mark), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "垂直平分线上的点到A、B距离相等",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.7)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(line_AB),
            FadeOut(explanation),
            FadeOut(right_angle_mark),
            FadeOut(label_M),
            run_time=0.5
        )
        
        # 保留: perp_bisector_AB, dot_M, subtitle
        self.dot_M_AB = dot_M
    
    def show_perpendicular_bisector_BC(self):
        """场景5: 垂直平分线BC"""
        # BC边高亮
        line_BC = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        self.play(Create(line_BC), run_time=0.6)
        
        # 中点N
        dot_N = Dot(self.M_BC, color=WHITE, radius=0.08)
        label_N = Text("N", font="PingFang SC", font_size=18, color=WHITE).next_to(
            dot_N, RIGHT, buff=0.1
        )
        
        self.play(
            FadeIn(dot_N, scale=0.5),
            FadeIn(label_N),
            run_time=0.6
        )
        
        # 垂直平分线
        start_BC, end_BC, _ = self.perpendicular_bisector_endpoints(self.B, self.C, length=3.5)
        
        self.perp_bisector_BC = DashedLine(
            start_BC, end_BC,
            color=self.COLOR_PERP_BISECTOR,
            dash_length=0.1,
            stroke_width=3
        )
        
        self.play(GrowFromCenter(self.perp_bisector_BC), run_time=1.0)
        
        # 直角标记
        right_angle_mark_2 = self.create_right_angle_mark(
            self.M_BC,
            self.B,
            start_BC,
            size=0.15
        )
        
        self.play(FadeIn(right_angle_mark_2), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "两条垂直平分线相交",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(line_BC),
            FadeOut(explanation),
            FadeOut(right_angle_mark_2),
            FadeOut(label_N),
            run_time=0.5
        )
        
        # 保留: perp_bisector_BC, dot_N
        self.dot_N_BC = dot_N
    
    def show_circumcenter(self):
        """场景6: 外心出现"""
        # 交点闪光
        self.play(Flash(self.O, color=self.COLOR_CIRCUMCENTER, flash_radius=0.5), run_time=0.5)
        
        # 外心点
        dot_O = Dot(self.O, color=self.COLOR_CIRCUMCENTER, radius=0.14)
        self.play(FadeIn(dot_O, scale=0.5), run_time=0.5)
        
        # 标注"O"
        label_O = Text("O", font="PingFang SC", font_size=24, color=self.COLOR_CIRCUMCENTER).next_to(
            dot_O, LEFT, buff=0.15
        )
        self.play(FadeIn(label_O), run_time=0.5)
        
        # 标签"外心"
        label_circumcenter = Text(
            "外心",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_CIRCUMCENTER
        ).next_to(label_O, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(FadeIn(label_circumcenter), run_time=0.5)
        
        self.wait(1.0)
        
        # 三条半径依次出现
        radius_OA = DashedLine(self.O, self.A, color=self.COLOR_RADIUS, dash_length=0.08, stroke_width=2)
        radius_OB = DashedLine(self.O, self.B, color=self.COLOR_RADIUS, dash_length=0.08, stroke_width=2)
        radius_OC = DashedLine(self.O, self.C, color=self.COLOR_RADIUS, dash_length=0.08, stroke_width=2)
        
        self.play(Create(radius_OA), run_time=0.6)
        self.play(Create(radius_OB), run_time=0.6)
        self.play(Create(radius_OC), run_time=0.6)
        
        # 公式
        formula = MathTex(
            r"OA = OB = OC",
            font_size=30,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(formula), run_time=0.6)
        
        # 半径同时高亮
        radii_group = VGroup(radius_OA, radius_OB, radius_OC)
        self.play(
            Indicate(radii_group, color=self.COLOR_HIGHLIGHT, scale_factor=1.05),
            run_time=1.0
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(self.perp_bisector_AB),
            FadeOut(self.perp_bisector_BC),
            FadeOut(self.dot_M_AB),
            FadeOut(self.dot_N_BC),
            FadeOut(formula),
            run_time=0.6
        )
        
        # 保留: dot_O, label_O, label_circumcenter, radii
        self.dot_O = dot_O
        self.label_O = label_O
        self.label_circumcenter = label_circumcenter
        self.radii_group = radii_group
    
    def show_circumcircle(self):
        """场景7: 外接圆绘制"""
        # 外接圆
        self.circumcircle = Circle(
            radius=self.radius,
            color=self.COLOR_CIRCLE,
            stroke_width=4
        ).move_to(self.O)
        
        self.play(Create(self.circumcircle), run_time=2.0)
        
        # 说明文字
        explanation = Text(
            "这就是三角形的外接圆",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.7)
        
        self.wait(1.0)
        
        # 三个顶点依次闪烁
        self.play(Indicate(self.dot_A, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        self.play(Indicate(self.dot_B, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        self.play(Indicate(self.dot_C, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        self.play(FadeOut(explanation), run_time=0.4)
        
        # 主公式
        main_formula = Text(
            "不共线的三点确定一个圆",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(main_formula, shift=UP * 0.3), run_time=0.7)
        
        # 圆旋转（视觉效果）
        self.play(
            Rotate(self.circumcircle, PI/2, about_point=self.O),
            run_time=1.5
        )
        
        self.wait(1.5)
        
        # 清理半径线
        self.play(FadeOut(self.radii_group), run_time=0.5)
        
        # 保留: circumcircle, triangle, dot_O, labels, main_formula
        self.main_formula = main_formula
    
    def show_summary(self):
        """场景8: 总结与片尾"""
        # 整体缩小并上移
        all_objects = VGroup(
            self.triangle,
            self.circumcircle,
            self.dot_A,
            self.dot_B,
            self.dot_C,
            self.dot_O,
            self.label_O,
            self.label_circumcenter
        )
        
        self.play(
            all_objects.animate.scale(0.5).move_to(UP * 4.5),
            FadeOut(self.main_formula),
            run_time=1.0
        )
        
        # 知识卡片
        cards = VGroup()
        
        # 卡片1
        card_1 = self.create_knowledge_card(
            "不共线三点确定圆",
            "三点不能在同一直线上",
            self.COLOR_TRIANGLE,
            UP * 2
        )
        cards.add(card_1)
        
        # 卡片2
        card_2 = self.create_knowledge_card(
            "外心：垂直平分线交点",
            "三边垂直平分线相交于一点",
            self.COLOR_PERP_BISECTOR,
            UP * 0.5
        )
        cards.add(card_2)
        
        # 卡片3
        card_3 = self.create_knowledge_card(
            "外心性质：OA = OB = OC",
            "外心到三顶点距离相等",
            self.COLOR_CIRCUMCENTER,
            DOWN * 1
        )
        cards.add(card_3)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 0), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.3)
        
        self.wait(1.0)
        
        # 总结文字
        summary_text = Text(
            "掌握外接圆\n解锁几何新技能！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(summary_text, shift=UP * 0.3, scale=1.05), run_time=0.6)
        
        self.wait(1.0)
        
        # 清理并准备片尾
        self.play(
            FadeOut(all_objects),
            FadeOut(cards),
            FadeOut(summary_text),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多几何技巧！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 小圆形装饰
        circles = VGroup(*[
            Circle(radius=0.15, color=self.COLOR_CIRCLE, fill_opacity=0.8)
            .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(circ, scale=0.5) for circ in circles],
            run_time=0.6
        )
        self.play(Rotate(circles, angle=PI, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(circles),
            run_time=1.0
        )
    
    def create_knowledge_card(self, title, content, color, position):
        """创建知识卡片"""
        # 图标圆
        icon = Circle(radius=0.15, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="PingFang SC",
            font_size=22,
            color=WHITE
        )
        
        # 内容
        content_text = Text(
            content,
            font="PingFang SC",
            font_size=16,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.25)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card


# 运行命令:
# manim -pql circle_determination.py CircleDetermination  # 快速预览
# manim -qh circle_determination.py CircleDetermination   # 高质量渲染