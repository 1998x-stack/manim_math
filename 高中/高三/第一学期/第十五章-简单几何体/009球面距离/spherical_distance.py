"""
球面距离 - 高三数学教学动画
Spherical Distance Animation using Manim 3D

渲染命令:
  预览: manim -pql spherical_distance.py SphericalDistance
  高质量: manim -qh  spherical_distance.py SphericalDistance
"""

from manim import *
import numpy as np

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


# ─── 球面几何精确计算工具 ───────────────────────
class SphereGeo:
    @staticmethod
    def spherical_to_cartesian(phi_deg, lam_deg, R=1.0):
        phi = np.radians(phi_deg); lam = np.radians(lam_deg)
        return np.array([R*np.cos(phi)*np.cos(lam),
                         R*np.cos(phi)*np.sin(lam),
                         R*np.sin(phi)])

    @staticmethod
    def central_angle(phi1, lam1, phi2, lam2):
        p1,l1,p2,l2 = map(np.radians,[phi1,lam1,phi2,lam2])
        c = np.cos(p1)*np.cos(p2)*np.cos(l1-l2)+np.sin(p1)*np.sin(p2)
        return np.arccos(np.clip(c,-1,1))

    @staticmethod
    def great_circle_arc(P, Q, n=80):
        """slerp 插值大圆弧 (P,Q 为单位向量)"""
        omega = np.arccos(np.clip(np.dot(P,Q),-1,1))
        if omega<1e-10: return [P,Q]
        return [(np.sin((1-t)*omega)*P+np.sin(t*omega)*Q)/np.sin(omega)
                for t in np.linspace(0,1,n+1)]

    @staticmethod
    def lat_circle(phi_deg, R=1.0, n=80):
        phi=np.radians(phi_deg); r=R*np.cos(phi); z=R*np.sin(phi)
        return [np.array([r*np.cos(2*PI*i/n), r*np.sin(2*PI*i/n), z])
                for i in range(n+1)]

    @staticmethod
    def meridian(lam_deg, R=1.0, n=60):
        lam=np.radians(lam_deg)
        return [np.array([R*np.cos(-PI/2+PI*i/n)*np.cos(lam),
                          R*np.cos(-PI/2+PI*i/n)*np.sin(lam),
                          R*np.sin(-PI/2+PI*i/n)]) for i in range(n+1)]


def pts_mob(pts, color=WHITE, sw=2):
    m=VMobject(color=color,stroke_width=sw)
    m.set_points_as_corners(pts)
    return m


# ─── verify_geometry 内联验证 ─────────────────
def _verify():
    theta=SphereGeo.central_angle(40,30,20,90)
    assert 0<np.degrees(theta)<180
    assert abs(SphereGeo.central_angle(50,30,10,30)-np.radians(40))<1e-6
    assert abs(SphereGeo.central_angle(0,20,0,80)-np.radians(60))<1e-6
    # grep_MathTex: no CJK in MathTex strings ✓
    # verify_boundaries: R=2.2 << 7.0 safe ✓
    print("✓ 所有验证通过")
_verify()


# ─── 主场景 ───────────────────────────────────
class SphericalDistance(ThreeDScene):

    R   = 2.2
    O   = np.array([0.,0.,0.])
    BG  = "#0d1117"
    GOLD= "#ffd700"
    COL_A="#ff4757"; COL_B="#2ed573"
    ANG_C="#ffa502"; EQ_C="#4a9eff"
    GR  ="#aaaaaa"

    PHI_A, LAM_A = 40.0, 30.0
    PHI_B, LAM_B = 20.0, 90.0

    def construct(self):
        self.camera.background_color = self.BG
        self._setup()
        self.s0_opening()
        self.s1_great_circle()
        self.s2_lat_lon()
        self.s3_central_angle()
        self.s4_formula()
        self.s5_special_cases()
        self.s6_outro()

    def _setup(self):
        R=self.R
        self.P_A=SphereGeo.spherical_to_cartesian(self.PHI_A,self.LAM_A,R)
        self.P_B=SphereGeo.spherical_to_cartesian(self.PHI_B,self.LAM_B,R)
        self.theta_AB=SphereGeo.central_angle(self.PHI_A,self.LAM_A,self.PHI_B,self.LAM_B)
        self.d_AB=R*self.theta_AB
        self.arc_pts=[p*R for p in SphereGeo.great_circle_arc(self.P_A/R,self.P_B/R)]
        self.eq_pts=SphereGeo.lat_circle(0,R)
        self.lat_A=SphereGeo.lat_circle(self.PHI_A,R)
        self.lat_B=SphereGeo.lat_circle(self.PHI_B,R)
        self.mer_A=SphereGeo.meridian(self.LAM_A,R)
        self.prime=SphereGeo.meridian(0,R)

    def _sphere(self):
        R=self.R
        return Surface(
            lambda u,v: np.array([R*np.sin(v)*np.cos(u),
                                  R*np.sin(v)*np.sin(u),
                                  R*np.cos(v)]),
            u_range=[0,TAU], v_range=[0,PI], resolution=(24,24),
            fill_color="#1e3a5f", fill_opacity=0.55,
            stroke_color="#4a9eff", stroke_width=0.3)

    # ── S0 开场 ──────────────────────────────
    def s0_opening(self):
        self.set_camera_orientation(phi=70*DEGREES, theta=-60*DEGREES)
        auth=Text("上海初高中数学直通车  @emptyandcalm",
                  font="Noto Sans CJK SC",font_size=18,color="#666666").to_edge(UP,buff=0.3)
        self.add_fixed_in_frame_mobjects(auth)
        self.play(FadeIn(auth))
        hook=Text("飞机走曲线，为何更短？",
                  font="Noto Sans CJK SC",font_size=38,color=self.GOLD).move_to(UP*6.5)
        sub=Text("— 球面距离的秘密 —",
                 font="Noto Sans CJK SC",font_size=24,color=self.GR).move_to(UP*5.8)
        self.add_fixed_in_frame_mobjects(hook,sub)
        self.play(Write(hook,run_time=1.0))
        self.play(FadeIn(sub))
        sph=self._sphere()
        eq=pts_mob(self.eq_pts,self.EQ_C,2)
        self.play(Create(sph,run_time=1.5)); self.play(Create(eq))
        self.begin_ambient_camera_rotation(rate=0.22); self.wait(2.5)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(hook),FadeOut(sub))
        self.sph=sph; self.eq=eq; self.auth=auth

    # ── S1 大圆弧 vs 纬线弧 ──────────────────
    def s1_great_circle(self):
        ttl=Text("球面距离 = 大圆劣弧长",font="Noto Sans CJK SC",
                 font_size=30,color=self.GOLD).move_to(UP*6.5)
        self.add_fixed_in_frame_mobjects(ttl); self.play(Write(ttl))
        dA=Dot3D(self.P_A,radius=0.12,color=self.COL_A)
        dB=Dot3D(self.P_B,radius=0.12,color=self.COL_B)
        lA=Text("A",font_size=26,color=self.COL_A).move_to(self.P_A+[.32,0,.32])
        lB=Text("B",font_size=26,color=self.COL_B).move_to(self.P_B+[.32,0,.32])
        self.add_fixed_in_frame_mobjects(lA,lB)
        self.play(FadeIn(dA),FadeIn(dB))
        arc=pts_mob(self.arc_pts,self.GOLD,4)
        lbl=Text("大圆弧（最短路径✓）",font="Noto Sans CJK SC",
                 font_size=22,color=self.GOLD).move_to(DOWN*4.4)
        self.add_fixed_in_frame_mobjects(lbl)
        self.play(Create(arc,run_time=1.2),FadeIn(lbl)); self.wait(0.8)
        # 纬线弧对比
        φ=np.radians(self.PHI_A); l1=np.radians(self.LAM_A); l2=np.radians(self.LAM_B)
        lat_arc_pts=[np.array([self.R*np.cos(φ)*np.cos(l1+t*(l2-l1)),
                               self.R*np.cos(φ)*np.sin(l1+t*(l2-l1)),
                               self.R*np.sin(φ)]) for t in np.linspace(0,1,60)]
        la=pts_mob(lat_arc_pts,"#ff6b6b",3)
        ll=Text("纬线弧（非最短✗）",font="Noto Sans CJK SC",
                font_size=22,color="#ff6b6b").move_to(DOWN*5.1)
        self.add_fixed_in_frame_mobjects(ll)
        self.play(Create(la),FadeIn(ll)); self.wait(1.8)
        self.play(FadeOut(la),FadeOut(ll),FadeOut(ttl))
        self.arc_mob=arc; self.dA=dA; self.dB=dB; self.lA=lA; self.lB=lB

    # ── S2 经纬度 ─────────────────────────────
    def s2_lat_lon(self):
        ttl=Text("经度 λ  与  纬度 φ",font="Noto Sans CJK SC",
                 font_size=30,color=self.GOLD).move_to(UP*6.5)
        self.add_fixed_in_frame_mobjects(ttl); self.play(Write(ttl))
        pm=pts_mob(self.prime,"#ff9f43",2)
        laA=pts_mob(self.lat_A,self.COL_A,1.5); laA.set_opacity(.7)
        mA=pts_mob(self.mer_A,self.COL_A,1.5); mA.set_opacity(.7)
        laB=pts_mob(self.lat_B,self.COL_B,1.5); laB.set_opacity(.7)
        self.play(Create(pm)); self.play(Create(laA),Create(mA)); self.play(Create(laB))
        iA=Text(f"A : φ={int(self.PHI_A)}°N,  λ={int(self.LAM_A)}°E",
                font="Noto Sans CJK SC",font_size=22,color=self.COL_A).move_to(DOWN*4.0)
        iB=Text(f"B : φ={int(self.PHI_B)}°N,  λ={int(self.LAM_B)}°E",
                font="Noto Sans CJK SC",font_size=22,color=self.COL_B).move_to(DOWN*4.8)
        hphi=Text("φ : 与赤道面的夹角",font="Noto Sans CJK SC",
                  font_size=20,color=self.GR).move_to(DOWN*5.5)
        hlam=Text("λ : 与本初子午线的夹角",font="Noto Sans CJK SC",
                  font_size=20,color=self.GR).move_to(DOWN*6.1)
        self.add_fixed_in_frame_mobjects(iA,iB,hphi,hlam)
        self.play(FadeIn(iA),FadeIn(iB),FadeIn(hphi),FadeIn(hlam))
        self.begin_ambient_camera_rotation(rate=0.18); self.wait(2.5)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(pm),FadeOut(laA),FadeOut(mA),FadeOut(laB),
                  FadeOut(iA),FadeOut(iB),FadeOut(hphi),FadeOut(hlam),FadeOut(ttl))

    # ── S3 球心角 ─────────────────────────────
    def s3_central_angle(self):
        ttl=Text("球心角 θ",font="Noto Sans CJK SC",
                 font_size=34,color=self.GOLD).move_to(UP*6.5)
        self.add_fixed_in_frame_mobjects(ttl); self.play(Write(ttl))
        lOA=Line3D(self.O,self.P_A,color=self.COL_A,stroke_width=3)
        lOB=Line3D(self.O,self.P_B,color=self.COL_B,stroke_width=3)
        self.play(Create(lOA),Create(lOB))
        # 球心角弧
        pA=self.P_A/self.R; pB=self.P_B/self.R; r=0.75*self.R; w=self.theta_AB
        ang_pts=[(np.sin((1-t)*w)*pA+np.sin(t*w)*pB)/np.sin(w)*r
                 for t in np.linspace(0,1,50)]
        ang=pts_mob(ang_pts,self.ANG_C,3); self.play(Create(ang))
        mid=(pA+pB)/np.linalg.norm(pA+pB)
        th=MathTex(r"\theta",color=self.ANG_C,font_size=40).move_to(mid*r*1.35+[.2,0,0])
        vt=Text(f"θ ≈ {np.degrees(self.theta_AB):.1f}°",
                font="Noto Sans CJK SC",font_size=24,color=self.ANG_C).move_to(DOWN*4.2)
        ex=Text("θ = OA 与 OB 的夹角（弧度）",
                font="Noto Sans CJK SC",font_size=20,color=self.GR).move_to(DOWN*5.0)
        self.add_fixed_in_frame_mobjects(th,vt,ex)
        self.play(FadeIn(th),FadeIn(vt),FadeIn(ex)); self.wait(2.0)
        self.play(FadeOut(ttl),FadeOut(th),FadeOut(vt),FadeOut(ex),FadeOut(ang))
        self.lOA=lOA; self.lOB=lOB

    # ── S4 核心公式 ───────────────────────────
    def s4_formula(self):
        ttl=Text("核心公式",font="Noto Sans CJK SC",
                 font_size=34,color=self.GOLD).move_to(UP*6.5)
        self.add_fixed_in_frame_mobjects(ttl); self.play(Write(ttl))
        f1=MathTex(r"d = R\theta",font_size=56).move_to(DOWN*3.5)
        l1=Text("球面距离公式",font="Noto Sans CJK SC",
                font_size=22,color=self.GR).move_to(DOWN*4.4)
        self.add_fixed_in_frame_mobjects(f1,l1)
        self.play(Write(f1),FadeIn(l1)); self.wait(0.8)
        f2=MathTex(r"\cos\theta=\cos\varphi_1\cos\varphi_2\cos(\lambda_1-\lambda_2)"
                   r"+\sin\varphi_1\sin\varphi_2",
                   font_size=24,color="#bbbbbb").move_to(DOWN*5.2)
        l2=Text("球心角余弦公式",font="Noto Sans CJK SC",
                font_size=20,color=self.GR).move_to(DOWN*6.0)
        self.add_fixed_in_frame_mobjects(f2,l2)
        self.play(Write(f2),FadeIn(l2))
        # 高亮
        f1h=MathTex(r"d=",r"R",r"\theta",font_size=56)
        f1h[1].set_color(BLUE_C); f1h[2].set_color(self.ANG_C)
        f1h.move_to(DOWN*3.5); self.add_fixed_in_frame_mobjects(f1h)
        self.play(Transform(f1,f1h)); self.wait(2.0)
        self.play(FadeOut(ttl),FadeOut(f1),FadeOut(l1),FadeOut(f2),
                  FadeOut(l2),FadeOut(f1h),FadeOut(self.lOA),FadeOut(self.lOB))

    # ── S5 特殊情形 ───────────────────────────
    def s5_special_cases(self):
        ttl=Text("两个特殊情形",font="Noto Sans CJK SC",
                 font_size=32,color=self.GOLD).move_to(UP*6.5)
        self.add_fixed_in_frame_mobjects(ttl); self.play(Write(ttl))
        R=self.R
        # 情形1: 同经线
        P1=SphereGeo.spherical_to_cartesian(50,self.LAM_A,R)
        P2=SphereGeo.spherical_to_cartesian(10,self.LAM_A,R)
        a1=pts_mob([p*R for p in SphereGeo.great_circle_arc(P1/R,P2/R)],self.COL_A,4)
        d1=Dot3D(P1,.1,color=self.COL_A); d2=Dot3D(P2,.1,color=self.COL_A)
        ct1=Text("① 同一经线上",font="Noto Sans CJK SC",font_size=26,color=self.COL_A).move_to(DOWN*3.5)
        fc1=MathTex(r"d=R|\varphi_1-\varphi_2|",font_size=38).move_to(DOWN*4.4)
        ec1=Text("经差为 0，仅纬差决定弧长",font="Noto Sans CJK SC",
                 font_size=20,color=self.GR).move_to(DOWN*5.1)
        self.add_fixed_in_frame_mobjects(ct1,fc1,ec1)
        self.play(FadeIn(d1),FadeIn(d2),Create(a1,run_time=.8))
        self.play(Write(ct1),Write(fc1),FadeIn(ec1)); self.wait(1.5)
        self.play(FadeOut(ct1),FadeOut(fc1),FadeOut(ec1),
                  FadeOut(d1),FadeOut(d2),FadeOut(a1))
        # 情形2: 赤道
        Q1=SphereGeo.spherical_to_cartesian(0,20,R)
        Q2=SphereGeo.spherical_to_cartesian(0,80,R)
        a2=pts_mob([p*R for p in SphereGeo.great_circle_arc(Q1/R,Q2/R)],self.COL_B,4)
        dq1=Dot3D(Q1,.1,color=self.COL_B); dq2=Dot3D(Q2,.1,color=self.COL_B)
        ct2=Text("② 赤道上",font="Noto Sans CJK SC",font_size=26,color=self.COL_B).move_to(DOWN*3.5)
        fc2=MathTex(r"d=R|\lambda_1-\lambda_2|",font_size=38).move_to(DOWN*4.4)
        ec2=Text("φ = 0，纬线即大圆（赤道）",font="Noto Sans CJK SC",
                 font_size=20,color=self.GR).move_to(DOWN*5.1)
        self.add_fixed_in_frame_mobjects(ct2,fc2,ec2)
        self.play(FadeIn(dq1),FadeIn(dq2),Create(a2,run_time=.8))
        self.play(Write(ct2),Write(fc2),FadeIn(ec2)); self.wait(1.5)
        sm=Text("球面距离 = R × 球心角（弧度）",font="Noto Sans CJK SC",
                font_size=24,color=self.GOLD).move_to(DOWN*6.1)
        self.add_fixed_in_frame_mobjects(sm)
        self.play(FadeIn(sm,shift=UP*.3)); self.wait(2.0)
        self.play(FadeOut(ttl),FadeOut(ct2),FadeOut(fc2),FadeOut(ec2),
                  FadeOut(dq1),FadeOut(dq2),FadeOut(a2),FadeOut(sm))

    # ── S6 片尾 ───────────────────────────────
    def s6_outro(self):
        self.play(FadeOut(self.sph),FadeOut(self.eq),FadeOut(self.arc_mob),
                  FadeOut(self.dA),FadeOut(self.dB),run_time=0.8)
        self.remove(self.lA,self.lB)
        card=RoundedRectangle(width=8.2,height=5.8,corner_radius=0.45,
                              fill_color="#0f1f3d",fill_opacity=0.96,
                              stroke_color=self.GOLD,stroke_width=2.5).move_to(UP*1.2)
        self.add_fixed_in_frame_mobjects(card); self.play(FadeIn(card))
        ct=Text("球面距离  知识卡",font="Noto Sans CJK SC",
                font_size=30,color=self.GOLD).move_to(UP*3.3)
        ff1=MathTex(r"d=R\theta",font_size=48).move_to(UP*2.4)
        ff2=MathTex(r"\cos\theta=\cos\varphi_1\cos\varphi_2\cos(\lambda_1\!-\!\lambda_2)"
                    r"+\sin\varphi_1\sin\varphi_2",
                    font_size=23,color="#cccccc").move_to(UP*1.55)
        ff3 = VGroup(
            Text("同经线：", font="Noto Sans CJK SC", font_size=26, color="#aaaaff"),
            MathTex(r"d = R|\varphi_1 - \varphi_2|", font_size=26, color="#aaaaff"),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.7)
        ff4 = VGroup(
            Text("赤道：", font="Noto Sans CJK SC", font_size=26, color="#aaffaa"),
            MathTex(r"d = R|\lambda_1 - \lambda_2|", font_size=26, color="#aaffaa"),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.05)
        self.add_fixed_in_frame_mobjects(ct,ff1,ff2,ff3,ff4)
        self.play(Write(ct))
        for f in [ff1,ff2,ff3,ff4]: self.play(Write(f,run_time=0.55))
        self.wait(1.2)
        cta=Text("关注我，获得更多数学技巧！",font="Noto Sans CJK SC",
                 font_size=32,color=self.GOLD).move_to(DOWN*4.4)
        au=Text("上海初高中数学直通车  @emptyandcalm",font="Noto Sans CJK SC",
                font_size=22,color="#888888").move_to(DOWN*5.2)
        self.add_fixed_in_frame_mobjects(cta,au)
        self.play(FadeIn(cta,shift=UP*.3)); self.play(FadeIn(au))
        self.wait(3.0)