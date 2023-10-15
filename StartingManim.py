from manim import *
from manim_slides import Slide

class Pith(Scene):
    def construct(self):
        sq = Square(side_length=2, fill_color=BLUE, fill_opacity=1)
        self.play(Create(sq))
        self.wait(1)
        self.play(sq.animate.shift(UP*2))
        self.wait(1)
        self.play(sq.animate.shift(LEFT*2))
        self.wait(1)
        self.play(sq.animate.shift(DOWN*2))
        self.wait()

class Testing(Scene):
    def construct(self):
        name = Tex("Testing").to_edge(UL, buff=0.5)
        sq = Square(side_length=0.5, fill_color=GREEN, fill_opacity=1).shift(LEFT*3)
        tri = Triangle(fill_color=RED, fill_opacity=1).scale(0.6).to_edge(DR)

        self.play(Write(name))
        self.play(DrawBorderThenFill(sq), runt_time=2)
        self.play(Create(tri))
        self.wait()

        self.play(name.animate.to_edge(UR), run_time=2)
        self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time=3)
        self.wait()

class GettersandUpdaters(Scene):
    def construct(self):
        rect = Rectangle(color = WHITE, height = 3, width = 2.5).to_edge(UL)
        circ = Circle().to_edge(DOWN)
        #Updater
        arrow = always_redraw(lambda: Arrow(
            rect.get_bottom(), circ.get_top(), buff=0.2))
        self.play(Create(VGroup(rect, circ,arrow)))
        self.wait()
        self.play(rect.animate.to_edge(UR), circ.animate.scale(0.5), run_time=4)

class Updaters(Scene):
    def construct(self):
        num = MathTex("ln(2)")
        box = always_redraw(lambda : SurroundingRectangle(num, color = BLUE, fill_opacity = 0.4, fill_color = RED, buff=0.5))
        nm = always_redraw(lambda : Tex("Euler's Number").next_to(box, DOWN, buff=0.25))
        self.play(Create(VGroup(num, box, nm))) 
        self.play(num.animate.shift(RIGHT*2), run_time=2)

class ValueTrackers(Scene):
    def construct(self):
        k = ValueTracker(3.5)
        num = always_redraw(lambda : DecimalNumber().set_value(k.get_value()))
        self.play(FadeIn(num))
        self.wait()
        self.play(k.animate.set_value(5.5), run_time=3, rate_func=there_and_back)

class Graphing(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-4,4,2], x_length = 7, y_range=[0,16,4], y_length = 5).to_edge(DOWN).add_coordinates()
        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")
        parab = FunctionGraph(lambda x: x**2, color = RED, x_range=[-3,3])
        func_label = MathTex("f(x) = {x}^{2}").scale(0.6).next_to(parab, UR, buff=0.25).set_color(GREEN)
        #area = plane.get_riemann_rectangles(parab, x_range=[-3,3], dx=0.1, input_sample_type="left", stroke_width=0.5, fill_opacity=0.5)
        self.play(DrawBorderThenFill(plane))
        self.play(Create(VGroup(labels, parab,func_label)))
        #self.wait()
        #self.play(Create(area))
        self.wait()


class EnsembleMethods(Scene):
    def construct(self):
        # Create the title "Ensemble Methods"
        title = Tex("Ensemble Methods", color=WHITE).scale(1.5)
        ens = Tex("'Ensemble'", color=BLUE).scale(1.5)
        self.play(Write(title))
        self.wait()

        # Move the title to the top of the screen and simultaneously fade in an svg image called "orchestra.svg" in the middle of the page
        d = SVGMobject("Drums.svg").shift(LEFT*2)
        g = SVGMobject("Guitar.svg").shift(RIGHT*2)
        t = SVGMobject("Trumpet.svg").shift(DOWN*2)
        self.play(Transform(title, ens), run_time=1)
        self.play(title.animate.to_edge(UP), FadeIn(d), FadeIn(g), FadeIn(t), run_time=1)

        self.wait()

        # Move all three images in the middle of the screen while transforming them to "orchestra.svg"
        orchestra = SVGMobject("Orchestra.svg").scale(2)
        self.play(d.animate.shift(LEFT*2), g.animate.shift(RIGHT*2), t.animate.shift(DOWN*2), Transform(d, orchestra), Transform(g, orchestra), Transform(t, orchestra), run_time=1)
        
        self.wait()

        #Create a identical structures using rectangles and arrows and leaves with rounded corners that look like decision trees with one split, side by side, and combine them into a single tree in the middle of the screen
        self.play(FadeOut(orchestra))
        
        rect1 = Rectangle(height=1, width=1, color=BLUE).shift(LEFT*2)
        leaf1 = RoundedRectangle(height=1, width=1, color=BLUE, corner_radius=0.2).shift(LEFT*4, DOWN)
        leaf2 = RoundedRectangle(height=1, width=1, color=BLUE, corner_radius=0.2).shift(LEFT*1, DOWN)
        rect2 = Rectangle(height=1, width=1, color=BLUE).shift(RIGHT*2)
        leaf3 = RoundedRectangle(height=1, width=1, color=BLUE, corner_radius=0.2).shift(RIGHT*4, DOWN)
        leaf4 = RoundedRectangle(height=1, width=1, color=BLUE, corner_radius=0.2).shift(RIGHT*1, DOWN)
        
        arrow1 = Arrow(rect1.get_top(), leaf1.get_top(), color=BLUE)
        arrow2 = Arrow(rect1.get_top(), leaf2.get_top(), color=BLUE)
        arrow3 = Arrow(rect2.get_top(), leaf3.get_top(), color=BLUE)
        arrow4 = Arrow(rect2.get_top(), leaf4.get_top(), color=BLUE)
        
        self.play(FadeIn(VGroup(rect1,leaf1,leaf2,arrow1,arrow2)), FadeIn(VGroup(rect2,leaf3,leaf4,arrow3,arrow4)))
        


        self.wait()