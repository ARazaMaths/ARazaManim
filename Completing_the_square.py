from turtle import left
from manim import *


class CompletingTheSquare(Scene):
    def construct(self):
        title = Tex(r"Completing the Square")
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_corner(UP))
        self.wait(1)
        text = Tex(r"We will show: $x^2 + bx = \left(x + \tfrac{b}{2}\right)^2 - \frac{b^2}{4}$")
        self.play(Write(text), run_time = 2)
        self.wait(2)
        self.play(FadeOut(title))
        self.play(text.animate.to_corner(UP))
        self.wait()
        xsquare = Square()
        xsquare.scale(2).set_stroke(color = YELLOW)
        self.play(Create(xsquare))
        self.wait()
        self.play(FadeOut(text), run_time = 1)
        self.wait()
        xsquarebracesd = Brace(xsquare, DOWN)
        xsquaretextd = xsquarebracesd.get_tex(r"x")
        xsquarebracesl = Brace(xsquare, LEFT)
        xsquaretextl = xsquarebracesl.get_tex(r"x")
        self.play(  GrowFromCenter(xsquarebracesd),
                    Write(xsquaretextd),
                    GrowFromCenter(xsquarebracesl),
                    Write(xsquaretextl))
        self.wait()
        text1 = MathTex(r"x^2")
        self.play(  xsquare.animate.set_fill(YELLOW, opacity = 0.5),
                    FadeIn(text1))
        self.wait()
        #self.play(  Uncreate(xsquarebracesd),
        #            Uncreate(xsquarebracesl),
        #            Unwrite(xsquaretextd),
        #            Unwrite(xsquaretextl))
        group1 = VGroup(    xsquare,
                            xsquarebracesd,
                            xsquaretextd,
                            xsquarebracesl,
                            xsquaretextl,
                            text1)
        self.play(group1.animate.shift(2*LEFT))
        self.wait()
        points = [[1, -2, 0], [1, 2, 0], [3, 2, 0], [3, -2, 0]]
        rectangle = Polygon(*points, stroke_color = GREEN)
        self.play(Create(rectangle))
        self.wait()
        xrecbraces = Brace(rectangle, RIGHT)
        xrecbracestext = xrecbraces.get_tex(r"x")
        brecbraces = Brace(rectangle, DOWN)
        brecbracestext = brecbraces.get_tex(r"b")
        self.play(  GrowFromCenter(xrecbraces),
                    Write(xrecbracestext),
                    GrowFromCenter(brecbraces),
                    Write(brecbracestext))
        self.wait()
        points2 = [[1, -2, 0], [1, 2, 0], [2, 2, 0], [2, -2, 0]]
        points3 = [[2, -2, 0], [2, 2, 0], [3, 2, 0], [3, -2, 0]]
        rec2 = Polygon(*points2, stroke_color = GREEN)
        rec3 = Polygon(*points3, stroke_color = GREEN)
        self.play(  Create(rec2),
                    Create(rec3),
                    Uncreate(brecbraces),
                    Unwrite(brecbracestext))
        self.play(Uncreate(rectangle))
        rec2braces = Brace(rec2, DOWN)
        rec2bracestext = rec2braces.get_tex(r"\tfrac{b}{2}")
        rec3braces = Brace(rec3, DOWN)
        rec3bracestext = rec3braces.get_tex(r"\tfrac{b}{2}")
        self.play(  GrowFromCenter(rec2braces),
                    Write(rec2bracestext),
                    GrowFromCenter(rec3braces),
                    Write(rec3bracestext))
        text2 = MathTex(r"\tfrac{b}{2}x").move_to(1.5*RIGHT)
        text3 = MathTex(r"\tfrac{b}{2}x").move_to(2.5*RIGHT)
        self.play(  Write(text2),
                    Write(text3),
                    rec2.animate.set_fill(GREEN, opacity=0.5),
                    rec3.animate.set_fill(GREEN, opacity=0.5))
        group2 = VGroup(rec3, rec3braces, text3, rec3bracestext)
        self.add(group2, xsquare)
        self.wait()
        group3 = VGroup(rec2, rec2braces, rec2bracestext, text2)
        points4 = [[-4, 2, 0], [-4, 3, 0],[0, 3, 0], [0, 2, 0]]
        rec4 = Polygon(*points4, stroke_color = GREEN)
        rec4.set_fill(GREEN, opacity=0.5)
        rec4braces = Brace(rec4, LEFT)
        rec4bracestext = rec4braces.get_tex(r"\tfrac{b}{2}")
        text4 = MathTex(r"\tfrac{b}{2}x").move_to(2*LEFT + 2.5*UP)
        group4 = VGroup(rec4, rec4braces, rec4bracestext, text4)
        self.play(Transform(group3, group4))
        self.wait()
        self.play(  group2.animate.move_to(xsquare.get_critical_point(UR),UL),
                    Uncreate(xrecbraces), 
                    Uncreate(xrecbracestext))
        biggroup = VGroup(group1, group2, group3)
        self.play(Uncreate(group4), run_time = 0)
        self.play(biggroup.animate.shift(2*RIGHT))
        self.wait()
        points5 = [[2, 2, 0], [2, 3, 0], [3, 3, 0], [3, 2, 0]]
        smolsquare = Polygon(*points5, stroke_color = PINK)
        smolsquare.set_fill(PINK, opacity = 0.5)
        text5 = MathTex(r"\tfrac{b^2}{4}").move_to(2.5*RIGHT + 2.5*UP)
        points6 = [[-2, -2, 0], [-2, 3, 0], [3, 3, 0], [3, -2, 0]]
        bigsquare = Polygon(*points6, stroke_color = WHITE)
        self.play(  text1.animate.set_color(RED),
                    text2.animate.set_color(RED),
                    text3.animate.set_color(RED))
        self.wait()
        group5 = VGroup(text1, text2, text3)
        group5.set_color(RED)
        text7 = MathTex(r"x^2 + bx =").to_corner(DOWN).shift(1*LEFT).set_color(RED)
        self.play(Transform(group5, text7))
        text6 = Text("Now, we complete the square.", t2c={"complete": PINK}, font_size = 24).to_corner(UP).shift(0.5*RIGHT)
        self.play(Write(text6))
        self.wait()
        self.play(  Create(smolsquare),
                    Write(text5))
        self.wait()
        self.play(Create(bigsquare))
        self.play(Unwrite(text6))
        self.wait()
        group6 = VGroup(rec2bracestext,
                        rec3bracestext,
                        xsquaretextd,
                        xsquaretextl,
                        rec2braces,
                        rec3braces,
                        xsquarebracesd,
                        xsquarebracesl)
        self.play(  rec2bracestext.animate.set_color(BLUE),
                    rec3bracestext.animate.set_color(BLUE),
                    xsquaretextd.animate.set_color(BLUE),
                    xsquaretextl.animate.set_color(BLUE))
        group6.set_color(BLUE)
        text8 = MathTex(r"\left(x + \tfrac{b}{2}\right)^2").to_corner(DOWN).shift(0.1*DOWN + 1.1*RIGHT).set_color(BLUE)
        self.play(Transform(group6, text8))
        self.wait()
        text9 = MathTex(r"- \tfrac{b^2}{4}").to_corner(DOWN).shift(0.1*DOWN + 2.3*RIGHT).set_color(BLUE)
        self.play(Transform(text5, text9))
        self.wait(2)
        self.play(  FadeOut(group6),
                    FadeOut(group5),
                    FadeOut(text5),
                    xsquare.animate.set_fill(YELLOW, opacity = 0),
                    rec2.animate.set_fill(GREEN, opacity = 0),
                    rec3.animate.set_fill(GREEN, opacity = 0),
                    smolsquare.animate.set_fill(PINK, opacity = 0))
        text10 = Tex("Animated by Adil Raza").move_to(3*DOWN)
        self.play(Write(text10), run_time = 2)
        self.wait(4)
