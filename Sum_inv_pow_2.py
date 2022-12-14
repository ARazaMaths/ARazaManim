from manim import *


class TrialScene(Scene):
    def construct(self):
        title = MathTex(r"\sum_{n=1}^\infty \frac{1}{2^n} = 1")
        self.play(Write(title), run_time = 2)
        self.wait()
        transform_title = MathTex(r"\sum_{n=1}^\infty \frac{1}{2^n} = 1")
        transform_title.to_corner(UP)
        self.play(Transform(title, transform_title))
        self.wait()
        square = Square()
        square.set_stroke(color=YELLOW)
        square.scale(2)
        self.play(Create(square))
        self.wait()
        self.play(FadeOut(title), run_time = 1)
        self.wait()
        text1 = MathTex(r"1")
        self.play(Write(text1), square.animate.set_fill(RED, opacity = 0.5))
        self.wait(2)
        self.play(Unwrite(text1), square.animate.set_fill(opacity = 0))
        self.wait()
        p1 = [0, 2, 0]
        p2 = [0, -2, 0]
        line1 = Line(p1, p2, color = BLUE)
        text1 = MathTex(r"\frac{1}{2}").move_to(1*LEFT)
        self.play(Create(line1), Write(text1))
        self.wait()
        p1 = [0, 0, 0]
        p2 = [2, 0, 0]
        text2 = MathTex(r"\tfrac{1}{4}").move_to(1*RIGHT+1*UP)
        line2 = Line(p1, p2, color = BLUE)
        self.play(Create(line2), Write(text2))
        self.wait()
        p1 = [1, 0 ,0]
        p2 = [1, -2, 0]
        text3 = MathTex(r"\tfrac{1}{8}").move_to(0.5*RIGHT+1*DOWN)
        line3 = Line(p1, p2, color = BLUE)
        self.play(Create(line3), Write(text3))
        self.wait()
        p1 = [1, -1, 0]
        p2 = [2, -1, 0]
        text4 = MathTex(r"\tfrac{1}{16}").move_to(1.5*RIGHT+0.5*DOWN)
        line4 = Line(p1, p2, color = BLUE)
        self.play(Create(line4), Write(text4))
        self.wait()
        text5 = MathTex(r"\ddots", color = BLUE).move_to(1.5*RIGHT+1.5*DOWN)
        self.play(Write(text5))
        self.wait()
        text1copy = text1.copy()
        self.play(text1copy.animate.shift(3*LEFT+3*DOWN))
        textplus1 = MathTex(r"+").move_to(3.5*LEFT+3*DOWN)
        self.play(FadeIn(textplus1), run_time = 0.25)
        transform_text2 = MathTex(r"\frac{1}{4}").move_to(3*LEFT+3*DOWN)
        text2copy = text2.copy()
        self.play(Transform(text2copy, transform_text2))
        textplus2 = MathTex(r"+").move_to(2.5*LEFT+3*DOWN)
        self.play(FadeIn(textplus2), run_time = 0.25)
        transform_text3 = MathTex(r"\frac{1}{8}").move_to(2*LEFT+3*DOWN)
        text3copy = text3.copy()
        self.play(Transform(text3copy, transform_text3))
        textplus3 = MathTex(r"+").move_to(1.5*LEFT + 3*DOWN)
        self.play(FadeIn(textplus3), run_time = 0.25)
        transform_text4 = MathTex(r"\frac{1}{16}").move_to(1*LEFT+3*DOWN)
        text4copy = text4.copy()
        self.play(Transform(text4copy, transform_text4))
        textplus4 = MathTex(r"+").move_to(0.5*LEFT + 3*DOWN)
        self.play(FadeIn(textplus4), run_time = 0.25)
        transform_text5 = MathTex(r"\cdots").move_to(0.1*RIGHT+3*DOWN)
        text5copy = text5.copy()
        self.play(Transform(text5copy, transform_text5))
        text6 = MathTex(r"= \sum_{n=1}^\infty \frac{1}{2^n}").move_to(-1.5*LEFT+3*DOWN)
        self.play(FadeIn(text6), run_time = 1)
        text7 = MathTex(r"= 1").move_to(3*RIGHT+2.92*DOWN)
        self.play(FadeIn(text7), run_time = 1)
        self.wait(2)
        self.play(FadeOut(text1, text2, text3, text4, text6, text7, text1copy, textplus1, text2copy, textplus2, text3copy, textplus3, text4copy, textplus4, text4copy, text5copy), run_time = 2)
        text8 = Tex("Animated by ARazaMaths").move_to(3*DOWN)
        self.play(Write(text8), run_time = 2)
        self.wait(4)
