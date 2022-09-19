from manim import *
from math import sqrt

class AMGM(Scene):
    def construct(self):
        circle = Circle(radius=2)
        diam = Line([-2, 0, 0], [2, 0, 0], color=BLUE)
        texta = MathTex(r"a").move_to(0.25*DOWN + 0.5*RIGHT)
        texta.font_size=40
        textb = MathTex(r"b").move_to(0.25*DOWN + 1.5*LEFT)
        textb.font_size=40
        texte = MathTex(r"e").move_to((sqrt(3)/2)*UP + 0.75*LEFT)
        texte.font_size=40
        line1 = Line([-1, 0, 0], [-1, sqrt(3), 0], color=BLUE)
        self.add(circle, diam, texta, textb, texte, line1)       
        line2 = Line([-1, sqrt(3), 0], [-2, 0, 0], color=BLUE)
        line3 = Line([-1, sqrt(3), 0], [2, 0, 0], color=BLUE)
        self.play(Create(line2), Create(line3))
        self.wait()
        rightangle1 = RightAngle(line1, diam, length=0.25)
        rightangle2 = RightAngle(line1, diam, length=0.25, quadrant=(1,-1))
        self.play(Create(rightangle1), Create(rightangle2))
        