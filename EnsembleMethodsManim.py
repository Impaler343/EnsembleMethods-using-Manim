from manim import *
from manim_slides import Slide

class F1(Slide, MovingCameraScene):
    def construct(self):
        # Create the title "Ensemble Methods"
        title = Tex("Ensemble Methods", color=WHITE).scale(1.5)
        ens = Tex("Ensemble", color=BLUE).scale(1.5)
        self.play(Write(title))
        self.next_slide()

        # Move the title to the top of the screen and simultaneously fade in an svg image called "orchestra.svg" in the middle of the page
        d = SVGMobject("Drums.svg").shift(LEFT*2)
        g = SVGMobject("Guitar.svg").shift(RIGHT*2)
        t = SVGMobject("Trumpet.svg").shift(DOWN*2)
        self.play(Transform(title, ens), run_time=1)
        self.play(title.animate.to_edge(UP), FadeIn(d), FadeIn(g), FadeIn(t), run_time=1)

        self.next_slide()

        # Move all three images in the middle of the screen while transforming them to "orchestra.svg"
        orchestra = SVGMobject("Orchestra.svg").scale(2)
        self.play(d.animate.shift(LEFT*2), g.animate.shift(RIGHT*2), t.animate.shift(DOWN*2), Transform(d, orchestra), Transform(g, orchestra), Transform(t, orchestra), run_time=1)
        
        self.next_slide()

        #Create a identical structures using rectangles and arrows and leaves with rounded corners that look like decision trees with one split, side by side, and combine them into a single tree in the middle of the screen
        self.play(FadeOut(orchestra, d, g, t))

        text1 = Tex("Tree 1", color=WHITE).shift(LEFT*3, UP*2)
        rect1= SurroundingRectangle(text1, color= YELLOW, fill_opacity = 0.4, fill_color = RED, buff=0.5)
        l1 = Tex("Leaf", color=WHITE).shift(LEFT*5, DOWN)
        leaf1= SurroundingRectangle(l1, color= YELLOW, fill_opacity = 0.4, fill_color = RED)
        l2 = Tex("Leaf", color=WHITE).shift(LEFT*1, DOWN)
        leaf2= SurroundingRectangle(l2, color= YELLOW, fill_opacity = 0.4, fill_color = RED)
        text2 = Tex("Tree 2", color=WHITE).shift(RIGHT*3, UP*2)
        rect2= SurroundingRectangle(text2, color= YELLOW, fill_opacity = 0.4, fill_color = GREEN, buff=0.5)
        l3 = Tex("Leaf", color=WHITE).shift(RIGHT*5, DOWN)
        leaf3= SurroundingRectangle(l3, color= YELLOW, fill_opacity = 0.4, fill_color = GREEN)
        l4 = Tex("Leaf", color=WHITE).shift(RIGHT*1, DOWN)
        leaf4= SurroundingRectangle(l4, color= YELLOW, fill_opacity = 0.4, fill_color = GREEN)
        
        arrow1 = Arrow(rect1.get_bottom(), leaf1.get_top(), color=BLUE)
        arrow2 = Arrow(rect1.get_bottom(), leaf2.get_top(), color=BLUE)
        arrow3 = Arrow(rect2.get_bottom(), leaf3.get_top(), color=BLUE)
        arrow4 = Arrow(rect2.get_bottom(), leaf4.get_top(), color=BLUE)
        
        self.play(FadeIn(VGroup(rect1, text1,rect2, text2)), FadeIn(VGroup(leaf1, l1,leaf2, l2,leaf3, l3,leaf4, l4)), FadeIn(VGroup(arrow1, arrow2, arrow3, arrow4)), run_time=2)
        
        self.next_slide()

        # Move both trees to the middle of the screen and combine them into a single tree

        text3 = Tex("Stronger Tree", color=WHITE).shift(UP*2)
        rect3= SurroundingRectangle(text3, color= GREEN, fill_opacity = 0.4, fill_color = BLUE, buff=0.5)
        l5 = Tex("Leaf", color=WHITE).shift(LEFT*1, DOWN)
        leaf5= SurroundingRectangle(l5, color= GREEN, fill_opacity = 0.4, fill_color = BLUE)
        l6 = Tex("Leaf", color=WHITE).shift(RIGHT*1, DOWN)
        leaf6= SurroundingRectangle(l6, color= GREEN, fill_opacity = 0.4, fill_color = BLUE)

        arrow5 = Arrow(rect3.get_bottom(), leaf5.get_top(), color=BLUE)
        arrow6 = Arrow(rect3.get_bottom(), leaf6.get_top(), color=BLUE)

        # Use Transform to combine the two trees into a single tree

        self.play(Transform(VGroup(rect1, text1,rect2, text2, leaf1, l1,leaf2, l2,leaf3, l3,leaf4, l4, arrow1, arrow2, arrow3, arrow4), VGroup(rect3, text3, leaf5, l5,leaf6, l6, arrow5, arrow6)), run_time=2)

        self.next_slide()

        self.play(FadeOut(title, VGroup(rect3, text3, leaf5, l5,leaf6, l6, arrow5, arrow6), VGroup(rect1, text1,rect2, text2, leaf1, l1,leaf2, l2,leaf3, l3,leaf4, l4, arrow1, arrow2, arrow3, arrow4)))

        title = Tex("Ensemble Methods", color=WHITE)
        title2 = Tex("Ensemble Methods", color=WHITE)
        bagging = Tex("Bagging", color=WHITE).shift(LEFT*2)
        boosting = Tex("Boosting", color=WHITE).shift(RIGHT*2)

        # Create title, then transform it into the other two texts

        self.play(Create(title))
        self.play(Transform(title, bagging), Transform(title2, boosting), run_time=2)

        self.next_slide()

        self.play(FadeOut(title2), title.animate.shift(UP*3,RIGHT*2).scale(1.5))
        rect = SurroundingRectangle(title, color= YELLOW, fill_opacity = 0.4, fill_color = RED, buff=0.3)
        self.play(Create(rect))

        self.next_slide()

        self.play(FadeOut(rect,title))

        heading = Tex("Original Data", color=WHITE).scale(0.75).shift(UP*3.5)

        circ1 = Dot(color = RED).shift(LEFT*2, UP*3)
        circ2 = Dot(color = BLUE).shift(LEFT*1.5, UP*3)
        circ3 = Dot(color = RED).shift(LEFT*1, UP*3)
        circ4 = Dot(color = GREEN).shift(LEFT*0.5, UP*3)
        circ5 = Dot(color = GREEN).shift(LEFT*0, UP*3)
        circ6 = Dot(color = PINK).shift(RIGHT*0.5, UP*3)
        circ7 = Dot(color = DARK_BROWN).shift(RIGHT*1, UP*3)
        circ8 = Dot(color = RED).shift(RIGHT*1.5, UP*3)
        circ9 = Dot(color = ORANGE).shift(RIGHT*2, UP*3)
        circ10 = Dot(color = GOLD).shift(LEFT*2, UP*2.5) 
        circ11 = Dot(color = YELLOW).shift(LEFT*1.5, UP*2.5)
        circ12 = Dot(color = WHITE).shift(LEFT*1, UP*2.5)
        circ13 = Dot(color = RED).shift(LEFT*0.5, UP*2.5)
        circ14 = Dot(color = GOLD).shift(LEFT*0, UP*2.5)
        circ15 = Dot(color = PURPLE).shift(RIGHT*0.5, UP*2.5)
        circ16 = Dot(color = PINK).shift(RIGHT*1, UP*2.5)
        circ17 = Dot(color = DARK_BROWN).shift(RIGHT*1.5, UP*2.5)
        circ18 = Dot(color = PURPLE).shift(RIGHT*2, UP*2.5)

        data_rect = SurroundingRectangle(VGroup(circ1, circ2, circ3, circ4, circ5, circ6, circ7, circ8, circ9, circ10, circ11, circ12, circ13, circ14, circ15, circ16, circ17, circ18), color= YELLOW, buff=0.1)
        
        circ19 = Dot(color = WHITE).shift(LEFT*6, UP*1)
        circ20 = Dot(color = ORANGE).shift(LEFT*5.5, UP*1)
        circ21 = Dot(color = RED).shift(LEFT*5, UP*1)
        circ22 = Dot(color = GREEN).shift(LEFT*4.5, UP*1)
        circ23 = Dot(color = PURPLE).shift(LEFT*4, UP*1)

        data_rect2 = SurroundingRectangle(VGroup(circ19, circ20, circ21, circ22, circ23), color= YELLOW, buff=0.1)

        circ24 = Dot(color = RED).shift(LEFT*1, UP*1)
        circ25 = Dot(color = ORANGE).shift(LEFT*0.5, UP*1)
        circ26 = Dot(color = PINK).shift(LEFT*0, UP*1)
        circ27 = Dot(color = DARK_BROWN).shift(RIGHT*0.5, UP*1)
        circ28 = Dot(color = WHITE).shift(RIGHT*1, UP*1)

        data_rect3 = SurroundingRectangle(VGroup(circ24, circ25, circ26, circ27, circ28), color= YELLOW, buff=0.1)

        circ29 = Dot(color = GOLD).shift(RIGHT*6, UP*1)
        circ30 = Dot(color = GREEN).shift(RIGHT*5.5, UP*1)
        circ31 = Dot(color = GOLD).shift(RIGHT*5, UP*1)
        circ32 = Dot(color = PINK).shift(RIGHT*4.5, UP*1)
        circ33 = Dot(color = ORANGE).shift(RIGHT*4, UP*1)

        data_rect4 = SurroundingRectangle(VGroup(circ29, circ30, circ31, circ32, circ33), color= YELLOW, buff=0.1)

        arr1 = Arrow(data_rect.get_bottom(), data_rect2.get_top(), color=BLUE, buff=0.5)
        arr2 = Arrow(data_rect.get_bottom(), data_rect3.get_top(), color=BLUE)
        arr3 = Arrow(data_rect.get_bottom(), data_rect4.get_top(), color=BLUE, buff=0.5)

        t1 = Tex("Model 1", color=WHITE).shift(LEFT*5, DOWN*1)
        t2 = Tex("Model 2", color=WHITE).shift(LEFT*0, DOWN*1)
        t3 = Tex("Model 3", color=WHITE).shift(RIGHT*5, DOWN*1)

        data_rect5 = SurroundingRectangle(t1, color= YELLOW, buff=0.5, fill_opacity=0.4, fill_color=RED)
        data_rect6 = SurroundingRectangle(t2, color= YELLOW, buff=0.5, fill_opacity=0.4, fill_color=RED)
        data_rect7 = SurroundingRectangle(t3, color= YELLOW, buff=0.5, fill_opacity=0.4, fill_color=RED)

        c1 = Tex("Classifier 1", color=WHITE).shift(LEFT*5, DOWN*1)
        c2 = Tex("Classifier 2", color=WHITE).shift(LEFT*0, DOWN*1)
        c3 = Tex("Classifier 3", color=WHITE).shift(RIGHT*5, DOWN*1)

        r1 = Tex("Regressor 1", color=WHITE).shift(LEFT*5, DOWN*1)
        r2 = Tex("Regressor 2", color=WHITE).shift(LEFT*0, DOWN*1)
        r3 = Tex("Regressor 3", color=WHITE).shift(RIGHT*5, DOWN*1)

        arr4 = Arrow(data_rect2.get_bottom(), data_rect5.get_top(), color=BLUE)
        arr5 = Arrow(data_rect3.get_bottom(), data_rect6.get_top(), color=BLUE)
        arr6 = Arrow(data_rect4.get_bottom(), data_rect7.get_top(), color=BLUE)

        en_mod = Tex("Ensemble Model", color=WHITE).shift(DOWN*3)
        en_modr = SurroundingRectangle(en_mod, color= YELLOW, buff=0.3, fill_opacity=0.4, fill_color=GREEN, corner_radius=0.2)

        arr7 = Arrow(data_rect5.get_bottom(), en_modr.get_top(), color=BLUE, buff=0.7)
        arr8 = Arrow(data_rect6.get_bottom(), en_modr.get_top(), color=BLUE, buff=0.7)
        arr9 = Arrow(data_rect7.get_bottom(), en_modr.get_top(), color=BLUE, buff=0.7)

        self.play(FadeIn(heading))
        self.play(Create(data_rect), Create(VGroup(circ1, circ2, circ3, circ4, circ5, circ6, circ7, circ8, circ9, circ10, circ11, circ12, circ13, circ14, circ15, circ16, circ17, circ18)))
        self.play(Create(arr1), Create(arr2), Create(arr3))
        self.play(Create(data_rect2), Create(VGroup(circ19, circ20, circ21, circ22, circ23)), Create(data_rect3), Create(VGroup(circ24, circ25, circ26, circ27, circ28)), Create(data_rect4), Create(VGroup(circ29, circ30, circ31, circ32, circ33)))
        self.play(Create(arr4), Create(arr5), Create(arr6))
        self.play(FadeIn(t1), FadeIn(t2), FadeIn(t3), DrawBorderThenFill(data_rect5), DrawBorderThenFill(data_rect6), DrawBorderThenFill(data_rect7))
        self.play(Create(arr7), Create(arr8), Create(arr9))
        self.play(FadeIn(en_mod), DrawBorderThenFill(en_modr))

        self.next_slide()

        self.play(Transform(t1,c1), Transform(t2,c2), Transform(t3,c3))

        self.next_slide()

        self.play(Transform(t1,r1), Transform(t2,r2), Transform(t3,r3))

        self.next_slide()

        disrect = Rectangle(height=1.5, width=13, color=WHITE).shift(UP*1.5)
        disrect1 = Rectangle(height=0.5, width=10, color=WHITE).shift(DOWN*2)
        boot = Tex("Bootstrapping", color=WHITE).shift(UP*3, LEFT*4)
        aggr = Tex("Aggregation", color=WHITE).shift(UP*3, LEFT*4)

        self.play(Create(disrect), Write(boot))
        self.play(Uncreate(disrect))

        self.next_slide()

        self.play(Create(disrect1), Transform(boot, aggr))
        self.play(Uncreate(disrect1))

        self.next_slide()

        self.play(FadeOut(VGroup(heading, data_rect, circ1, circ2, circ3, circ4, circ5, circ6, circ7, circ8, circ9, circ10, circ11, circ12, circ13, circ14, circ15, circ16, circ17, circ18, arr1, arr2, arr3, data_rect2, circ19, circ20, circ21, circ22, circ23, data_rect3, circ24, circ25, circ26, circ27, circ28, data_rect4, circ29, circ30, circ31, circ32, circ33, arr4, arr5, arr6, t1, t2, t3, data_rect5, data_rect6, data_rect7, arr7, arr8, arr9, en_mod, en_modr, r1, r2, r3, disrect, disrect1, boot, aggr)))

        heading = Tex("Bootstrapping", color=WHITE).shift(UP*3)
        table = Table(
            [["Gender", "Age", "Weight", "Height"],
            ["Male", "19", "70", "180"],
            ["Female", "20", "60", "170"],
            ["Female", "21", "55", "175"],
            ["Male", "22", "80", "185"],
            ["Female", "23", "50", "160"],
            ["Male", "24", "75", "190"],
            ["Male", "25", "85", "195"]],
            include_outer_lines=True).scale(0.4).to_edge(LEFT)
        table.add_highlighted_cell((1,1), color=GREEN)
        table.add_highlighted_cell((1,2), color=RED)
        table.add_highlighted_cell((1,3), color=YELLOW)
        table.add_highlighted_cell((1,4), color=BLUE)

        v = table.get_vertical_lines().copy().next_to(table, ORIGIN)
        tops = table.get_rows()[0].copy()
        htops = table.get_horizontal_lines()[:2].copy()
        part1 = table.get_rows()[1].copy()
        h1 = table.get_horizontal_lines()[2:4].copy()
        part2 = table.get_rows()[3].copy()
        h2 = table.get_horizontal_lines()[4:6].copy()
        part3 = table.get_rows()[3].copy()
        h3 = table.get_horizontal_lines()[4:6].copy()
        part4 = table.get_rows()[2].copy()
        h4 = table.get_horizontal_lines()[3:5].copy()
        part5 = table.get_rows()[5].copy()
        h5 = table.get_horizontal_lines()[6:8].copy()
        part6 = table.get_rows()[6].copy()
        h6 = table.get_horizontal_lines()[7:9].copy()

        row1 = VGroup(part1, h1)
        row2 = VGroup(part2, h2)
        row3 = VGroup(part3, h3)
        row4 = VGroup(part4, h4)
        row5 = VGroup(part5, h5)
        row6 = VGroup(part6, h6)
        v1 = VGroup(v, tops, htops)

        self.play(FadeIn(heading), Write(table))

        self.next_slide()

        self.play(row1.animate.shift(RIGHT*7))
        self.play(row2.animate.next_to(row1, DOWN, buff=0))
        self.play(row3.animate.next_to(row2, DOWN, buff=0))

        self.next_slide()

        subset1 = VGroup(row1, row2, row3)
        
        h = Tex("Aggregation", color=WHITE).shift(UP*3)
        self.play(Transform(heading,Tex("Aggregation", color=WHITE).shift(UP*3)), subset1.animate.shift(LEFT*7), FadeOut(table), FadeIn(v1))

        self.next_slide()
         
        self.play(Transform(heading, Tex("Classification", color=WHITE).shift(UP*3, LEFT*4)), Transform(h, Tex("Regression", color=WHITE).shift(UP*3, RIGHT*4)))

        self.next_slide()

        data = [["Diabetes Prediction"],
            ["..."],
            ["..."],
            ["..."],
            ]
        pred = Table(data,
            include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
        brace = Brace(pred, direction=RIGHT, color=RED)

        arr1 = Arrow(start=row2.get_right(), end=pred.get_entries((2,1)), color=WHITE)
        arr2 = Arrow(start=row2.get_right(), end=pred.get_entries((3,1)), color=WHITE)
        arr3 = Arrow(start=row2.get_right(), end=pred.get_entries((4,1)), color=WHITE)

        self.play(FadeOut(h), heading.animate.shift(RIGHT*4))

        self.next_slide()

        self.play(Create(arr1))
        data[1][0] = "Yes"
        pred = Table(data,
            include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
        pred.add_highlighted_cell((1,1), color=PINK)
        pred.add_highlighted_cell((2,1), color=RED)
        self.play(FadeIn(pred))
        self.next_slide()
        
        self.play(FadeOut(pred,arr1), Create(arr2), Transform(row1,row4), Transform(row2,row5), Transform(row3,row6))
        data[2][0] = "Yes"
        pred = Table(data,
            include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
        pred.add_highlighted_cell((1,1), color=PINK)
        pred.add_highlighted_cell((2,1), color=RED)
        pred.add_highlighted_cell((3,1), color=RED)
        self.play(FadeIn(pred))
        self.next_slide()

        self.play(FadeOut(pred,arr2), Create(arr3), Transform(row1,row5), Transform(row2,row3), Transform(row3,row1))
        data[3][0] = "No"
        pred = Table(data,
            include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
        pred.add_highlighted_cell((1,1), color=PINK)
        pred.add_highlighted_cell((2,1), color=RED)
        pred.add_highlighted_cell((3,1), color=RED)
        pred.add_highlighted_cell((4,1), color=GREEN)
        self.play(FadeIn(pred))

        self.next_slide()

        self.play(GrowFromCenter(brace))

        p = pred.get_entries((3,1)).copy()
        self.play(p.animate.shift(RIGHT*3))

        predictions = LabeledDot(Tex("Yes", color=WHITE), color=RED, radius=0.5).next_to(p, ORIGIN)

        srect = SurroundingRectangle(heading, color=WHITE, fill_opacity=0.5, fill_color=PINK, buff=0.3)

        self.play(Transform(heading, Tex("Max Voting", color=WHITE).shift(UP*3)), DrawBorderThenFill(srect),GrowFromCenter(predictions), FadeOut(p))

        self.next_slide()

        self.play(FadeOut(pred, brace, arr3, predictions, srect, row1, row2, row3), Transform(heading, Tex("Regression", color=WHITE).shift(UP*3)))
        
        pred1 = Table(data,
            include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
        data1 = [["Income"],
            ["..."],
            ["..."],
            ["..."],
            ]
        self.next_slide()

        self.play(Create(arr1), FadeIn(row1), FadeIn(row6), FadeIn(row4))   
        data1[1][0] = "2.5"
        pred1 = Table(data1,
            include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
        pred1.add_highlighted_cell((1,1), color=PINK)
        self.play(FadeIn(pred1))

        self.next_slide()    

        self.play(FadeOut(pred1, arr1), Create(arr2), Transform(row1,row5), Transform(row6,row2), Transform(row4,row3))
        data1[2][0] = "1"
        pred1 = Table(data1,
            include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
        pred1.add_highlighted_cell((1,1), color=PINK)
        self.play(FadeIn(pred1))

        self.next_slide()

        self.play(FadeOut(pred1, arr2), Create(arr3), Transform(row1,row3), Transform(row6,row4), Transform(row4,row6))
        data1[3][0] = "3.5"
        pred1 = Table(data1,
            include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
        pred1.add_highlighted_cell((1,1), color=PINK)
        self.play(FadeIn(pred1))

        self.next_slide()

        p1 = pred1.get_entries((2,1)).copy()
        p2 = pred1.get_entries((3,1)).copy()
        p3 = pred1.get_entries((4,1)).copy()
        frac1 = MathTex(r"\frac{2.5 + 1 + 3.5}{3}", color=WHITE).shift(RIGHT*5, UP*1)
        self.play(Transform(p1, frac1), Transform(p2, frac1), Transform(p3, frac1))
        
        self.play(FadeOut(p1,p2), Transform(p3, Tex("2.33").shift(RIGHT*5, UP*1)), Transform(heading, Tex("Averaging").shift(UP*3)), DrawBorderThenFill(srect))

        self.next_slide()

        self.play(FadeOut(p3, heading, srect, row1, row4, row6, arr3, v1, pred1))

        heading = Tex("Bootstrapping Advantages", color=WHITE).shift(UP*3).scale(1.5)
        self.play(Write(heading))

        self.next_slide()
        
        dot = Dot(color=WHITE).to_edge(LEFT).shift(UP*2)
        txt = Tex("Reduces algebraic calculations", color=WHITE).next_to(dot, RIGHT).scale(0.75)

        self.play(GrowFromCenter(dot), Write(txt))

        self.next_slide()

        thous = Tex("Thousand Heights", color=WHITE).shift(LEFT*5, UP*0.5).scale(0.75)
        variance = MathTex(r"Var(\bar{X}) = \frac{\sum_{i=1}^{1000}(x_i - \mu)^2}{1000}", color=WHITE).shift(UP*0.5, RIGHT*3).scale(0.75)
        arr = Arrow (start=thous.get_right(), end=variance.get_left(), color=WHITE).scale(0.75)
        comp = Tex("Computing Variance", color=WHITE).next_to(arr, UP, buff=0).scale(0.75)

        self.play(GrowFromCenter(thous), GrowFromCenter(variance), GrowArrow(arr), Write(comp))

        self.next_slide()

        mast = VGroup(thous, variance, arr, comp)
        f = Tex("Five Heights", color=WHITE).shift(LEFT*5, UP*0.5).scale(0.75)
        f1 = VGroup(f.copy().scale(0.75), MathTex(r"Var(\bar{X}_1) = \frac{\sum_{i=1}^{5}(x_i - \mu)^2}{5}", color=WHITE).shift(UP*0.5, RIGHT*3).scale(0.75), arr.copy().scale(0.75), comp.copy().scale(0.75)).shift(UP*0)
        f2 = VGroup(f.copy().scale(0.75), MathTex(r"Var(\bar{X}_2) = \frac{\sum_{i=1}^{5}(x_i - \mu)^2}{5}", color=WHITE).shift(UP*0.5, RIGHT*3).scale(0.75), arr.copy().scale(0.75), comp.copy().scale(0.75)).shift( DOWN*1)
        f3 = VGroup(f.copy().scale(0.75), MathTex(r"Var(\bar{X}_3) = \frac{\sum_{i=1}^{5}(x_i - \mu)^2}{5}", color=WHITE).shift(UP*0.5, RIGHT*3).scale(0.75), arr.copy().scale(0.75), comp.copy().scale(0.75)).shift( DOWN*2)
        f4 = VGroup(f.copy().scale(0.75), MathTex(r"Var(\bar{X}_4) = \frac{\sum_{i=1}^{5}(x_i - \mu)^2}{5}", color=WHITE).shift(UP*0.5, RIGHT*3).scale(0.75), arr.copy().scale(0.75), comp.copy().scale(0.75)).shift( DOWN*3)
        f5 = VGroup(f.copy().scale(0.75), MathTex(r"Var(\bar{X}_5) = \frac{\sum_{i=1}^{5}(x_i - \mu)^2}{5}", color=WHITE).shift(UP*0.5, RIGHT*3).scale(0.75), arr.copy().scale(0.75), comp.copy().scale(0.75)).shift( DOWN*4)

        self.play(TransformFromCopy(mast, f1), TransformFromCopy(mast, f2), TransformFromCopy(mast, f3), TransformFromCopy(mast, f4), Transform(mast, f5))

        self.next_slide()

        resvar = MathTex(r"Var(\bar{X}) = \frac{\sum_{i=1}^{5}Var(\bar{X}_i)}{5}", color=WHITE)

        self.play(Transform(f1, resvar), Transform(f2, resvar), Transform(f3, resvar), Transform(f4, resvar), Transform(f5, resvar), Transform(mast, resvar))

        self.next_slide()

        self.play(FadeOut(f1, f2, f3, f4, f5, mast, resvar, dot, txt))

        txt = Tex("Reduces Variance", color=WHITE).shift(UP*2).scale(0.75)

        self.play(Write(txt))

        self.next_slide()

        # Create two y = x^2 side by side and show the variance by plotting points in both the graphs and joining them with a red line

        plane = NumberPlane(x_range=(-3,3,1), x_length=12, y_range=(-1,10,1), y_length=6, color=WHITE, background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.2
            }).add_coordinates()
        graph = plane.plot(lambda x: x**2, x_range=[-3, 3], color=BLUE)
        

        self.play(Write(plane), Write(graph), FadeOut(txt))

        self.next_slide()
        # Plot points on the graph and show the variance

        dots = VGroup()
        
        for i in range(30):
            x = np.random.uniform(-3, 3)
            dots.add(Dot(color=PINK).move_to(plane.c2p(x, x**2 + np.random.uniform(-2, 2))).scale(0.5))

        self.play(GrowFromCenter(dots))

        # Draw a spline function passing through all the points

        self.next_slide()

        # Sort the points in dots with respect to x coordinate

        dots.sort(lambda p: p[0])
        spline = VMobject()
        spline.set_points_smoothly([dot.get_center() for dot in dots])
        spline.set_color(RED)

        # Always redraw the spline function passing through all the points when the points are changed

        self.play(Create(spline), Transform(heading, Tex("Overfitting", color=WHITE).shift(UP*3.5).scale(1)))
        self.wait(2)

        self.next_slide()

        self.play(Transform(heading, Tex("High Variance", color=WHITE).shift(UP*3.5).scale(1)))

        # Add five new points to dots
        for i in range(5):
            x = np.random.uniform(-3, 3)
            dots.add(Dot(color=PINK).move_to(plane.c2p(x, x**2 + np.random.uniform(-1, 1))).scale(0.5))
            dots.sort(lambda p: p[0])
            spline.set_points_smoothly([dot.get_center() for dot in dots])
            self.play(Create(spline))
            self.next_slide()

        self.play(FadeOut(spline))

        # Draw a straight line trying to fit all the points
        
        line = Line(plane.c2p(-2, 0), plane.c2p(3, 3), color=RED)

        self.play(Create(line),Transform(heading, Tex("Underfitting", color=WHITE).shift(UP*3.5).scale(1)))

        self.next_slide()

        self.play(Transform(heading, Tex("High Bias", color=WHITE).shift(UP*3.5).scale(1)))

        self.next_slide()

        self.play(FadeOut(plane, graph, dots, line, heading))

        heading = Tex("Random Forests", color=WHITE).shift(UP*3).scale(1.5)

        self.play(Transform(heading, Tex("Random Forests", color=WHITE).shift(UP*3).scale(1.5)))

        self.next_slide()

        dot = Dot(color=WHITE).to_edge(LEFT).shift(UP*2).to_edge(LEFT)
        txt = Tex("Bagging applied on a bunch of Decision Trees", color=WHITE).shift(UP*2, LEFT*2).scale(0.75)

        self.play(GrowFromCenter(dot), Write(txt))

        self.next_slide()

        table = Table(
            [["Gender", "Age", "Weight", "Height"],
            ["Male", "30", "70", "180"],
            ["Female", "35", "60", "170"],
            ["Female", "41", "55", "175"],
            ["Male", "25", "80", "185"],
            ["Female", "56", "50", "160"],
            ["Male", "58", "75", "190"],
            ["Male", "46", "85", "195"]],
            row_labels=[Text("Features"), Text("R1"), Text("R2"), Text("R3"), Text("R4"), Text("R5"), Text("R6"), Text("R7")],
            col_labels=[Text("F1"), Text("F2"), Text("F3"), Text("F4")],
            include_outer_lines=True).scale(0.4).scale(0.8).to_edge(LEFT).shift(DOWN)
        table.add_highlighted_cell((2,2), color=GREEN)
        table.add_highlighted_cell((2,3), color=RED)
        table.add_highlighted_cell((2,4), color=YELLOW)
        table.add_highlighted_cell((2,5), color=BLUE)

        self.play(Write(table))

        self.next_slide()

        h1 = table.get_highlighted_cell((3,2), color=PINK, fill_opacity=0.5)
        h2 = table.get_highlighted_cell((4,2), color=PINK, fill_opacity=0.5)
        h3 = table.get_highlighted_cell((5,2), color=PINK, fill_opacity=0.5)
        h4 = table.get_highlighted_cell((6,2), color=PINK, fill_opacity=0.5)
        h5 = table.get_highlighted_cell((7,2), color=PINK, fill_opacity=0.5)
        h6 = table.get_highlighted_cell((8,2), color=PINK, fill_opacity=0.5)
        h7 = table.get_highlighted_cell((9,2), color=PINK, fill_opacity=0.5)
        h8 = table.get_highlighted_cell((9,3), color=PINK, fill_opacity=0.5)
        h9 = table.get_highlighted_cell((3,3), color=PINK, fill_opacity=0.5)
        h10 = table.get_highlighted_cell((4,3), color=PINK, fill_opacity=0.5)
        h11 = table.get_highlighted_cell((5,3), color=PINK, fill_opacity=0.5)
        h12 = table.get_highlighted_cell((6,3), color=PINK, fill_opacity=0.5)
        h13 = table.get_highlighted_cell((7,3), color=PINK, fill_opacity=0.5)
        h14 = table.get_highlighted_cell((8,3), color=PINK, fill_opacity=0.5)
        h15 = table.get_highlighted_cell((9,4), color=PINK, fill_opacity=0.5)
        h16 = table.get_highlighted_cell((3,4), color=PINK, fill_opacity=0.5)
        h17 = table.get_highlighted_cell((4,4), color=PINK, fill_opacity=0.5)
        h18 = table.get_highlighted_cell((5,4), color=PINK, fill_opacity=0.5)
        h19 = table.get_highlighted_cell((6,4), color=PINK, fill_opacity=0.5)
        h20 = table.get_highlighted_cell((7,4), color=PINK, fill_opacity=0.5)
        h21 = table.get_highlighted_cell((8,4), color=PINK, fill_opacity=0.5)
        h22 = table.get_highlighted_cell((9,5), color=PINK, fill_opacity=0.5)
        h23 = table.get_highlighted_cell((3,5), color=PINK, fill_opacity=0.5)
        h24 = table.get_highlighted_cell((4,5), color=PINK, fill_opacity=0.5)
        h25 = table.get_highlighted_cell((5,5), color=PINK, fill_opacity=0.5)
        h26 = table.get_highlighted_cell((6,5), color=PINK, fill_opacity=0.5)
        h27 = table.get_highlighted_cell((7,5), color=PINK, fill_opacity=0.5)
        h28 = table.get_highlighted_cell((8,5), color=PINK, fill_opacity=0.5)

        self.play(Transform(txt, Tex("Bootstrapping includes row as well as feature sampling", color=WHITE).shift(UP*2, LEFT*1.75).scale(0.75)))

        self.next_slide()

        d1 = LabeledDot(MathTex(r"D_1", color=BLACK), color=GOLD, radius=0.7).shift(UP*0.5)
        d2 = LabeledDot(MathTex(r"D_2", color=BLACK), color=GOLD, radius=0.7).shift(UP*0.5, RIGHT*2)
        d3 = LabeledDot(MathTex(r"D_3", color=BLACK), color=GOLD, radius=0.7).shift(UP*0.5, RIGHT*4)
        d4 = LabeledDot(MathTex(r"D_4", color=BLACK), color=GOLD, radius=0.7).shift(UP*0.5, RIGHT*6)
        dt = Tex("Decision Trees", color=WHITE).shift(RIGHT*3, UP*1.5).scale(0.75)

        r1 = Tex("R2,R2,R4,R5").next_to(d1, DOWN*0.05).scale(0.5)
        r2 = Tex("R1,R3,R6,R7").next_to(d2, DOWN*0.05).scale(0.5)
        r3 = Tex("R1,R1,R4,R6").next_to(d3, DOWN*0.05).scale(0.5)
        r4 = Tex("R2,R5,R7,R7").next_to(d4, DOWN*0.05).scale(0.5)

        c1 = Tex("C2,C3,C4").next_to(d1, UP*0.05).scale(0.5)
        c2 = Tex("C1,C3,C4").next_to(d2, UP*0.05).scale(0.5) 
        c3 = Tex("C1,C2,C4").next_to(d3, UP*0.05).scale(0.5)
        c4 = Tex("C1,C2,C3").next_to(d4, UP*0.05).scale(0.5)

        self.play(Write(dt), FadeIn(d1, d2, d3, d4), Transform(txt, Tex("The number of rows and columns that are sampled must be constant", color=WHITE).shift(UP*2).scale(0.75))) 

        self.next_slide()


        a1 = Arrow(start=LEFT, end=RIGHT, color=WHITE).shift(LEFT*6.8, DOWN*0.1).scale(0.25)
        a2 = Arrow(start=LEFT, end=RIGHT, color=WHITE).shift(LEFT*6.8, DOWN*0.55).scale(0.25)
        a3 = Arrow(start=LEFT, end=RIGHT, color=WHITE).shift(LEFT*6.8, DOWN*1.0).scale(0.25)
        a4 = Arrow(start=LEFT, end=RIGHT, color=WHITE).shift(LEFT*6.8, DOWN*1.45).scale(0.25)
        a5 = Arrow(start=LEFT, end=RIGHT, color=WHITE).shift(LEFT*6.8, DOWN*1.9).scale(0.25)
        a6 = Arrow(start=LEFT, end=RIGHT, color=WHITE).shift(LEFT*6.8, DOWN*2.35).scale(0.25)
        a7 = Arrow(start=LEFT, end=RIGHT, color=WHITE).shift(LEFT*6.8, DOWN*2.8).scale(0.25)


        a8 = Arrow(start=UP, end=DOWN, color=WHITE).shift(UP*1.2, LEFT*4.8).scale(0.25)
        a9 = Arrow(start=UP, end=DOWN, color=WHITE).shift(UP*1.2, LEFT*3.9).scale(0.25)
        a10 = Arrow(start=UP, end=DOWN, color=WHITE).shift(UP*1.2, LEFT*2.9).scale(0.25)
        a11 = Arrow(start=UP, end=DOWN, color=WHITE).shift(UP*1.2, LEFT*1.9).scale(0.25)

        self.play(FadeOut(dt), FadeIn(r1, c1, a2, a4, a5, a9, a10, a11), FadeIn(h10, h17, h24, h13, h20, h27, h12, h19, h26))

        self.next_slide()

        self.play(FadeOut(h10, h17, h24, h13, h20, h27, h12, h19, h26, a2, a4, a5, a9, a10, a11))

        self.next_slide()

        self.play(FadeIn(h1, h16, h23, h3, h18, h25, h6, h21, h28, h7, h15, h22), FadeIn(r2, c2, a1, a3, a6, a7, a8, a10, a11))

        self.next_slide()

        self.play(FadeOut(h1, h16, h23, h3, h18, h25, h6, h21, h28, h7, h15, h22, a1, a3, a6, a7, a8, a10, a11))

        self.next_slide()

        self.play(FadeIn(h1, h9, h23, h4, h12, h26, h6, h14, h28), FadeIn(r3, c3, a1, a4, a6, a8, a9, a11))

        self.next_slide()

        self.play(FadeOut(h1, h9, h23, h4, h12, h26, h6, h14, h28, a1, a4, a6, a8, a9, a11))

        self.next_slide()

        self.play(FadeIn(h2, h10, h17, h5, h13, h20, h7, h8, h15), FadeIn(r4, c4, a2, a8, a5, a7, a9, a10))

        self.next_slide()

        self.play(FadeOut(h2, h10, h17, h5, h13, h20, h7, h8, h15, a2, a8, a5, a7, a9, a10))

        self.next_slide()

        p1 = Tex("Yes").shift(DOWN*2.5)
        p2 = Tex("No").shift(DOWN*2.5, RIGHT*2)
        p3 = Tex("No").shift(DOWN*2.5, RIGHT*4)
        p4 = Tex("No").shift(DOWN*2.5, RIGHT*6)

        arr1 = Arrow(start=r1.get_bottom(), end=p1.get_top(), color=WHITE)
        arr2 = Arrow(start=r2.get_bottom(), end=p2.get_top(), color=WHITE)
        arr3 = Arrow(start=r3.get_bottom(), end=p3.get_top(), color=WHITE)
        arr4 = Arrow(start=r4.get_bottom(), end=p4.get_top(), color=WHITE)

        self.play(GrowArrow(arr1), Write(p1))
        self.play(GrowArrow(arr2), Write(p2))
        self.play(GrowArrow(arr3), Write(p3))
        self.play(GrowArrow(arr4), Write(p4))

        self.next_slide()

        prediction = LabeledDot(Tex("No", color=WHITE), color=GREEN).scale(1.5).shift(RIGHT*5)
        dbpred = Tex("Diabetes Prediction").scale(1.5).next_to(prediction, LEFT*8)
        aa = Arrow(start=dbpred.get_right(), end=prediction.get_left(), color=WHITE)

        self.play(FadeOut(arr1, arr2, arr3, arr4, r1, r2, r3, r4, c1, c2, c3, c4, d1, d2, d3, d4, table, txt, dot), FadeIn(dbpred), GrowArrow(aa), Transform(p1, prediction), Transform(p2, prediction), Transform(p3, prediction), Transform(p4, prediction), GrowFromCenter(prediction))
        
        self.next_slide()

        self.play(FadeOut(p1,p2,p3,p4,prediction, dbpred, aa, heading))

        heading = Tex("Boosting", color=WHITE).shift(UP*3).scale(1.5)
        # Create a regular hexagon in the middle of the screen using only lines and not using Polygon

        l1 = Line(start=RIGHT*1, end=RIGHT*0.5+UP*0.866, color=RED)
        l2 = Line(start=RIGHT*0.5+UP*0.866, end=LEFT*0.5+UP*0.866, color=RED)
        l3 = Line(start=LEFT*0.5+UP*0.866, end=LEFT*1, color=RED)
        l4 = Line(start=LEFT*1, end=LEFT*0.5+DOWN*0.866, color=RED)
        l5 = Line(start=LEFT*0.5+DOWN*0.866, end=RIGHT*0.5+DOWN*0.866, color=RED)
        l6 = Line(start=RIGHT*0.5+DOWN*0.866, end=RIGHT*1, color=RED)


        arc1 = Arc(radius=1, start_angle=PI, angle=-PI,color= YELLOW) 
        circ1 = Circle(radius=1, color=YELLOW)

        self.play(Write(heading), FadeIn(l1, l2, l3, l4, l5, l6), Create(circ1))
        self.play(Uncreate(circ1))
        
        self.next_slide()

        self.play(Transform(l1, arc1), Transform(l2, arc1), Transform(l3, arc1))

        self.next_slide()
        g1 = VGroup(l4,l5,l6)

        self.play(self.camera.frame.animate.set_width(2.5).move_to(g1))

        self.next_slide()

        arc2 = Arc(radius=1, start_angle=PI, angle=PI/3,color= YELLOW)
        g2 = VGroup(l5,l6)

        self.play(Transform(l4, arc2))

        self.next_slide()

        self.play(self.camera.frame.animate.set_width(2).move_to(g2))

        self.next_slide()

        arc3 = Arc(radius=1, start_angle=(4*PI)/3, angle=PI/3,color= YELLOW)

        self.play(Transform(l5, arc3))

        self.next_slide()
        
        g3 = VGroup(l6)

        self.play(self.camera.frame.animate.set_width(2).move_to(g3))

        self.next_slide()

        arc4 = Arc(radius=1, start_angle=(5*PI)/3, angle=PI/6,color= YELLOW)

        self.play(Transform(l6, arc4))

        self.next_slide()

        self.play(self.camera.frame.animate.set_width(15).move_to(ORIGIN))

        self.next_slide()

        self.play(FadeOut(l1, l2, l3, l4, l5, l6, arc1, arc2, arc3, arc4))

        txt = Tex("Adaptive Boosting", color=WHITE).shift(UP*2).scale(0.75)
        imgg = ImageMobject("AA.png").shift(DOWN*1)

        self.play(Transform(heading, Tex("AdaBoost", color=WHITE).shift(UP*3).scale(1.5)), FadeIn(imgg), Write(txt))

        self.next_slide()

        self.play(Transform(txt, Tex("Combines weak learners of low variance to produce a strong learner of high variance", color=WHITE).shift(UP*2).scale(0.5)))

        self.next_slide()

        self.play(Transform(txt, Tex("A model(due to underfitting or overfitting) which has poor accuracy", color=WHITE).shift(UP*2).scale(0.5)), Transform(heading, Tex("Weak Learner", color=WHITE).shift(UP*3).scale(1.5)), FadeOut(imgg))

        self.next_slide()

        stump = Tex("Stumps", color=WHITE).shift(UP*1, LEFT*4).scale(0.75)
        s1 = SurroundingRectangle(stump, color=PURPLE, fill_color=BLUE, fill_opacity=0.5)
        linm = Tex("Linear Models", color=WHITE).shift(UP*1).scale(0.75)
        s2 = SurroundingRectangle(linm, color=PURPLE, fill_color=BLUE, fill_opacity=0.5)
        knn = Tex("KNNs", color=WHITE).shift(UP*1, RIGHT*4).scale(0.75)
        s3 = SurroundingRectangle(knn, color=PURPLE, fill_color=BLUE, fill_opacity=0.5)

        decnod = Tex("Decision Node", color=WHITE).shift(LEFT*4).scale(0.5)
        srect1 = SurroundingRectangle(decnod, color=RED)
        l1 = Tex("Leaf Node", color=WHITE).shift(DOWN*2, LEFT*5).scale(0.5)
        srect2 = SurroundingRectangle(l1, color=GREEN, corner_radius=0.2)
        l2 = Tex("Leaf Node", color=WHITE).shift(DOWN*2, LEFT*3).scale(0.5)
        srect3 = SurroundingRectangle(l2, color=GREEN, corner_radius=0.2)
        a1 = Arrow(start=decnod.get_bottom(), end=l1.get_top(), color=WHITE)
        a2 = Arrow(start=decnod.get_bottom(), end=l2.get_top(), color=WHITE)

        st = VGroup(decnod, l1, l2, a1, a2, srect1, srect2, srect3, stump, s1)

        self.play(Write(st))

        axes1 = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=3, y_length=3, axis_config={"color": WHITE}).add_coordinates().shift(DOWN*1)
        line = Line(start=axes1.c2p(1, 0), end=axes1.c2p(4, 4), color=BLUE)

        lg = VGroup(axes1, line, linm, s2)

        self.play(Create(lg))

        axes2 = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=3, y_length=3, axis_config={"color": WHITE}).add_coordinates().shift(RIGHT*4, DOWN*1)
        # Plot 5 points in the range x=0 to x=2.5 and y=0 to y=2.5

        dots = VGroup()
        for i in range(5):
            dots.add(Dot(point=axes2.c2p(np.random.uniform(0, 2.5), np.random.uniform(0, 2.5)), color=RED))

        # Plot 5 points in the range x=2.5 to x=5 and y=2.5 to y=5

        for i in range(5):
            dots.add(Dot(point=axes2.c2p(np.random.uniform(2.5, 5), np.random.uniform(2.5, 5)), color=GREEN))

        dotplot = Dot(point=axes2.c2p(2.5, 2.5), color=PINK)
        dashedcirc = DashedVMobject(Circle(stroke_color=PINK, radius=1).move_to(dotplot), num_dashes=20) 

        knng = VGroup(axes2, dots, dotplot, knn, s3, dashedcirc)

        self.play(Create(knng))
        
        self.next_slide()

        self.play(FadeOut(lg, knng, txt, heading), st.animate.move_to(ORIGIN).scale(1.5))

        self.next_slide()

        self.play(FadeOut(st))

        heading = Tex("AdaBoost", color=WHITE).shift(UP*3).scale(1.5)
        table = MathTable(
            [["Gender", "Age", "Weight", "Height", "Diabetes", "Sample Weights"],
            ["Male", "30", "70", "180", "Yes", "1/7"],
            ["Female", "35", "60", "170", "Yes", "1/7"],
            ["Female", "41", "55", "175", "No", "1/7"],
            ["Male", "25", "80", "185", "Yes", "1/7"],
            ["Female", "56", "50", "160", "No", "1/7"],
            ["Male", "58", "75", "190", "No", "1/7"],
            ["Male", "46", "85", "195", "Yes", "1/7"]],
            include_outer_lines=True).scale(0.35).to_edge(LEFT, buff=0.5)
        table.add_highlighted_cell((1,1), color=GREEN)
        table.add_highlighted_cell((1,2), color=RED)
        table.add_highlighted_cell((1,3), color=YELLOW)
        table.add_highlighted_cell((1,4), color=BLUE)
        table.add_highlighted_cell((1,5), color=PINK)
        table.add_highlighted_cell((1,6), color=PURPLE)

        self.play(Write(table), Write(heading))

        self.next_slide()
        r1 = SurroundingRectangle(table.get_columns()[0], color=PINK)
        r2 = SurroundingRectangle(table.get_columns()[1], color=PINK)
        r3 = SurroundingRectangle(table.get_columns()[2], color=PINK)
        r4 = SurroundingRectangle(table.get_columns()[3], color=PINK)

        self.play(Create(r1))
        self.play(Uncreate(r1))
        self.play(Create(r2))
        self.play(Uncreate(r2))
        self.play(Create(r3))
        self.play(Uncreate(r3))
        self.play(Create(r4))
        self.play(Uncreate(r4))

        self.next_slide()

        txt1 = Tex("Feature with Least Gini Impurity").shift(UP*1, RIGHT*4).scale(0.75)
        txt2 = Tex("Weight").next_to(txt1, DOWN*3).scale(0.75)
        srect = SurroundingRectangle(txt2, color=WHITE, fill_color=YELLOW, fill_opacity=0.5)
        ar1 = Arrow(start=txt1.get_bottom(), end=txt2.get_top(), color=WHITE)

        self.play(Write(txt1), Write(txt2), GrowArrow(ar1), DrawBorderThenFill(srect))

        self.next_slide()

        l1 = Tex("Diabetes", color=WHITE).shift(UP*1, RIGHT*5).scale(0.5)
        cor1 = Tex("3", color=GREEN).shift(UP*0.5, RIGHT*4.5).scale(0.5)
        wro1 = Tex("1", color=RED).shift(UP*0.5, RIGHT*5.5).scale(0.5)

        g1 = VGroup(l1, cor1, wro1)
        srect1 = SurroundingRectangle(g1, color=YELLOW, corner_radius=0.2)

        l2 = Tex("No Diabetes", color=WHITE).shift(UP*1, RIGHT*3).scale(0.5)
        cor2 = Tex("2", color=GREEN).shift(UP*0.5, RIGHT*2.5).scale(0.5)
        wro2 = Tex("1", color=RED).shift(UP*0.5, RIGHT*3.5).scale(0.5)

        g2 = VGroup(l2, cor2, wro2)
        srect2 = SurroundingRectangle(g2, color=YELLOW, corner_radius=0.2)

        self.play(Transform(txt2, MathTex(r"Weight > 69", color=WHITE).shift(UP*2, RIGHT*4).scale(0.75)), FadeOut(txt1, ar1, srect), Create(srect1), Create(srect2), Create(g1), Create(g2))
        srect = SurroundingRectangle(txt2, color=WHITE, fill_color=YELLOW, fill_opacity=0.5)
        a1 = Arrow(start=srect.get_bottom(), end=srect1.get_top(), color=WHITE)
        a2 = Arrow(start=srect.get_bottom(), end=srect2.get_top(), color=WHITE)
        self.play(DrawBorderThenFill(srect), Create(a1), Create(a2))

        self.next_slide()

        r5 = SurroundingRectangle(table.get_rows()[2], color=YELLOW)
        r6 = SurroundingRectangle(table.get_rows()[6], color=YELLOW)

        self.play(Create(r5), Create(r6))

        self.next_slide()

        txt3 = MathTex(r"\frac{1}{7} + \frac{1}{7}").shift(RIGHT*4).scale(0.75)
        ar1 = Arrow(start=txt2.get_bottom(), end=txt3.get_top(), color=WHITE)
        self.play(Uncreate(r5), Uncreate(r6), Transform(txt2, MathTex(r"Total Error", color=WHITE).shift(UP*2, RIGHT*4).scale(0.75)), FadeOut(srect, a1, a2, srect1, srect2, g1, g2), FadeIn(txt3), GrowArrow(ar1))

        self.next_slide()

        self.play(Transform(txt3, MathTex(r"0.286", color=WHITE).shift(RIGHT*4).scale(0.75)))

        self.next_slide()

        self.play(Transform(txt2, Tex("Amount of Say", color=WHITE).shift(UP*2, RIGHT*4).scale(0.75)), Transform(txt3, MathTex(r"\frac{1}{2}log_{2}\frac{1 - T.E.}{T.E.}", color=WHITE).shift(RIGHT*4).scale(0.75)))
        
        self.next_slide()

        self.play(Transform(txt3, MathTex(r"\frac{1}{2}log_{2}(\frac{1 - 0.286}{0.286})", color=WHITE).shift(RIGHT*4).scale(0.75)))

        self.next_slide()

        self.play(Transform(txt3, MathTex(r"0.92", color=WHITE).shift(RIGHT*4).scale(0.75)))

        self.next_slide()

        head = Tex("Weight Updation", color=WHITE).shift(UP*1, RIGHT*3.5).scale(0.75)
        corr = Tex("Correctly Predicted", color=GREEN).next_to(head, DOWN*1).scale(0.5)
        corrform = MathTex(r"New Sample Weight = Old Sample Weight \times e^{-Amount of Say}", color=WHITE).next_to(corr, DOWN*0.5).scale(0.5)
        incorr = Tex("Incorrectly Predicted", color=RED).next_to(corrform, DOWN*2).scale(0.5)
        incorrform = MathTex(r"New Sample Weight = Old Sample Weight \times e^{Amount of Say}", color=WHITE).next_to(incorr, DOWN*0.5).scale(0.5)

        self.play(FadeOut(txt2, txt3, ar1), Write(head), Write(corr), Write(corrform), Write(incorr), Write(incorrform))

        self.next_slide()

        self.play(Transform(corrform, MathTex(r"New Sample Weight = 0.286 \times e^{-0.92}", color=WHITE).next_to(corr, DOWN*0.5).scale(0.5)), Transform(incorrform, MathTex(r"New Sample Weight = 0.286 \times e^{0.92}", color=WHITE).next_to(incorr, DOWN*0.5).scale(0.5)))

        self.next_slide()

        self.play(Transform(corrform, MathTex(r"New Sample Weight = 0.14", color=WHITE).next_to(corr, DOWN*0.5).scale(0.5)), Transform(incorrform, MathTex(r"New Sample Weight = 0.72", color=WHITE).next_to(incorr, DOWN*0.5).scale(0.5)))

        def replace_table_element(row, col, new_text, table:Table, scale=0.25, color=WHITE):
            elem = table.get_entries_without_labels((row,col))
            new_element = Text(new_text, color=color).scale(scale)
            new_element.move_to(elem)
            return Transform(elem, new_element)
        
        self.next_slide()

        self.play(replace_table_element(2, 6, "0.14", table), replace_table_element(3, 6, "0.72", table), replace_table_element(4, 6, "0.14", table), replace_table_element(5, 6, "0.14", table), replace_table_element(6, 6, "0.14", table), replace_table_element(7, 6, "0.72", table), replace_table_element(8, 6, "0.14", table))

        self.next_slide()

        self.play(Transform(head, Tex("Weight Normalization", color=WHITE).shift(UP*1, RIGHT*3.5).scale(0.75)), Transform(corrform, MathTex(r"New Sample Weight = \frac{Old Sample Weight}{Total Weight}", color=WHITE).next_to(corr, DOWN*0.5).scale(0.5)), Transform(incorrform, MathTex(r"New Sample Weight = \frac{Old Sample Weight}{Total Weight}", color=WHITE).next_to(incorr, DOWN*0.5).scale(0.5)))

        self.next_slide()

        self.play(Transform(corrform, MathTex(r"New Sample Weight = \frac{0.14}{1.86}", color=WHITE).next_to(corr, DOWN*0.5).scale(0.5)), Transform(incorrform, MathTex(r"New Sample Weight = \frac{0.72}{1.86}", color=WHITE).next_to(incorr, DOWN*0.5).scale(0.5)))

        self.next_slide()

        self.play(Transform(corrform, MathTex(r"New Sample Weight = 0.075", color=WHITE).next_to(corr, DOWN*0.5).scale(0.5)), Transform(incorrform, MathTex(r"New Sample Weight = 0.387", color=WHITE).next_to(incorr, DOWN*0.5).scale(0.5)))

        self.next_slide()

        self.play(replace_table_element(2, 6, "0.075", table), replace_table_element(3, 6, "0.387", table), replace_table_element(4, 6, "0.075", table), replace_table_element(5, 6, "0.075", table), replace_table_element(6, 6, "0.075", table), replace_table_element(7, 6, "0.387", table), replace_table_element(8, 6, "0.075", table))

        self.next_slide()

        self.play(Transform(head, Tex("Weighted Gini Impurity", color=WHITE).shift(UP*2, RIGHT*3.5).scale(0.75)), FadeOut(corrform, incorrform, corr), Transform(incorr, MathTex(r"Sample Weight \times Gini Impurity", color=WHITE).next_to(corrform, DOWN*2).scale(0.5)))
        ar1 = Arrow(start=head.get_bottom(), end=incorr.get_top(), color=WHITE)
        self.play(GrowArrow(ar1))

        self.next_slide()

        self.play(FadeOut(incorr, head, ar1, table))

        pred = MathTable(
            [["Gender", "Age", "Weight", "Height", "Diabetes"],
            ["Male", "36", "78", "170", "?"]],
            include_outer_lines=True).scale(0.4).to_edge(LEFT, buff=0.5).shift(UP*1.5)
        pred.add_highlighted_cell((1,1), color=GREEN)
        pred.add_highlighted_cell((1,2), color=RED)
        pred.add_highlighted_cell((1,3), color=YELLOW)
        pred.add_highlighted_cell((1,4), color=BLUE)
        pred.add_highlighted_cell((1,5), color=PINK)

        self.play(Write(pred))

        self.next_slide()

        s1 = LabeledDot(MathTex(r"S_1", color=BLACK), color=GOLD, radius=0.7).next_to(pred, RIGHT*1.5)
        s2 = LabeledDot(MathTex(r"S_2", color=BLACK), color=GOLD, radius=0.7).next_to(s1, RIGHT*2)
        s3 = LabeledDot(MathTex(r"S_3", color=BLACK), color=GOLD, radius=0.7).next_to(s2, RIGHT*2)
        s4 = LabeledDot(MathTex(r"S_4", color=BLACK), color=GOLD, radius=0.7).next_to(s3, RIGHT*2)

        arr = Arrow(start=pred.get_right(), end=s1.get_left(), color=WHITE)

        txt1 = MathTex(r"-0.98", color=RED).next_to(s1, DOWN*5).scale(0.5)
        txt2 = MathTex(r"0.75", color=GREEN).next_to(s2, DOWN*5).scale(0.5)
        txt3 = MathTex(r"0.16", color=GREEN).next_to(s3, DOWN*5).scale(0.5)
        txt4 = MathTex(r"0.13", color=GREEN).next_to(s4, DOWN*5).scale(0.5)

        a1 = Arrow(start=s1.get_bottom(), end=txt1.get_top(), color=WHITE)
        a2 = Arrow(start=s2.get_bottom(), end=txt2.get_top(), color=WHITE)
        a3 = Arrow(start=s3.get_bottom(), end=txt3.get_top(), color=WHITE)
        a4 = Arrow(start=s4.get_bottom(), end=txt4.get_top(), color=WHITE)

        plus1 = MathTex(r"+", color=WHITE).next_to(txt1, RIGHT*2)
        plus2 = MathTex(r"+", color=WHITE).next_to(txt2, RIGHT*2)
        plus3 = MathTex(r"+", color=WHITE).next_to(txt3, RIGHT*2)

        ans = MathTex(r"0.06", color=GREEN).next_to(plus2, ORIGIN)

        self.play(GrowFromCenter(s1), GrowFromCenter(s2), GrowFromCenter(s3), GrowFromCenter(s4), GrowArrow(arr))

        self.next_slide()

        self.play(Write(txt1), Write(txt2), Write(txt3), Write(txt4), GrowArrow(a1), GrowArrow(a2), GrowArrow(a3), GrowArrow(a4))

        self.next_slide()

        pos = Tex("Positive Sign = 'Yes' Prediction", color=WHITE).next_to(pred, DOWN*2).scale(0.75)
        neg = Tex("Negative Sign = 'No' Prediction", color=WHITE).next_to(pos, DOWN*4).scale(0.75)

        self.play(Write(pos), Write(neg))

        self.next_slide()

        self.play(Write(plus1), Write(plus2), Write(plus3))

        self.next_slide()

        g = VGroup(txt1, txt2, txt3, txt4, plus1, plus2, plus3)
        self.play(Transform(g, ans))

        self.next_slide()

        elem = pred.get_entries_without_labels((2,5))
        new_element = Text("Yes", color=BLUE).scale(0.5)
        new_element.move_to(elem) 

        self.play(Transform(elem,new_element))

        self.next_slide()

        self.play(FadeOut(pred, s1, s2, s3, s4, arr, txt1, txt2, txt3, txt4, a1, a2, a3, a4, plus1, plus2, plus3, ans, pos, neg, elem, new_element, heading))

        heading = Tex("XGBoost", color=WHITE).shift(UP*3).scale(1.5)

        self.play(Write(heading))

        self.next_slide()

        plane = NumberPlane(x_range=(-3,3,1), x_length=12, y_range=(-1,10,1), y_length=6, color=WHITE, background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.2
            }).add_coordinates()
        graph = plane.plot(lambda x: x**2, x_range=[-3, 3], color=BLUE)
        

        self.play(Write(plane), Write(graph), Transform(heading, Tex("Gradient Boosting", color=WHITE).shift(UP*3.5).scale(1.5)))

        self.next_slide()

        dots = VGroup()
        
        for i in range(8,-1, -1):
            x = i/3 if i%2==0 else -i/3
            dots.add(Dot(color=PINK).move_to(plane.c2p(x, (x)**2)))

        # Make a curve joining all of these dots with only straight lines
        straight_curve = VGroup()
        for i in range(0,8):
            ll = Line(dots[i].get_center(), dots[i+1].get_center(), color=RED)
            self.play(Create(ll))
            straight_curve.add(ll)

        self.play(Create(dots))

        self.next_slide()

        self.play(FadeOut(dots, straight_curve, graph, plane))

        data = [["Gender", "Age", "House Size", "Income"],
            ["Male", "30", "3000", "4"],
            ["Female", "35", "5000", "3"],
            ["Female", "41", "2000", "1"],
            ["Male", "25", "1000", "0.5"],
            ["Female", "56", "2500", "3.5"],
            ["Male", "58", "6000", "7.5"],
            ["Male", "46", "2400", "1.5"]]
        table = Table(data,include_outer_lines=True).scale(0.35).to_edge(LEFT, buff=0.5)
        table.add_highlighted_cell((1,1), color=GREEN)
        table.add_highlighted_cell((1,2), color=GREEN)
        table.add_highlighted_cell((1,3), color=GREEN)
        table.add_highlighted_cell((1,4), color=PINK)

        self.play(Write(table))

        self.next_slide()

        data = [["Gender", "Age", "House Size", "Income", "Prediction"],
            ["Male", "30", "3000", "4", "3"],
            ["Female", "35", "5000", "3", "3"],
            ["Female", "41", "2000", "1", "3"],
            ["Male", "25", "1000", "0.5", "3"],
            ["Female", "56", "2500", "3.5", "3"],
            ["Male", "58", "6000", "7.5", "3"],
            ["Male", "46", "2400", "1.5", "3"]]
    
        table2 = Table(data,include_outer_lines=True).scale(0.35).to_edge(LEFT, buff=0.5)
        table2.add_highlighted_cell((1,1), color=GREEN)
        table2.add_highlighted_cell((1,2), color=GREEN)
        table2.add_highlighted_cell((1,3), color=GREEN)
        table2.add_highlighted_cell((1,4), color=PINK)
        table2.add_highlighted_cell((1,5), color=BLUE)

        txt = Tex("Income Average", color=WHITE).shift(UP*1.5, RIGHT*4).scale(0.75)
        srect = always_redraw(lambda : Rectangle(height=txt.get_height()+0.5, width=txt.get_width()+0.5, color=RED, fill_color=GREEN, fill_opacity=0.5).move_to(txt))
        form = MathTex(r"\frac{4 + 3 + 1 + 0.5 + 3.5 + 7.5 + 1.5}{7}").scale(0.75).next_to(txt, DOWN*5)
        ar1 = Arrow(txt.get_bottom(), form.get_top(), color=WHITE)

        self.play(Write(txt), Write(form), GrowArrow(ar1), DrawBorderThenFill(srect))

        self.next_slide()

        self.play(Transform(form, MathTex(r"3").scale(0.75).next_to(txt, DOWN*5)))
        
        self.next_slide()

        self.play(Transform(table, table2))

        self.next_slide()

        self.play(Transform(form, Tex("(Actual Income - Prediction)", color=WHITE).scale(0.75).next_to(txt, DOWN*5)), Transform(txt, Tex("Residuals", color=WHITE).shift(UP*2, RIGHT*4).scale(0.75)))

        self.next_slide()

        data = [["Gender", "Age", "House Size", "Income", "Prediction", "Residuals"],
            ["Male", "30", "3000", "4", "3", "1"],
            ["Female", "35", "5000", "3", "3", "0"],
            ["Female", "41", "2000", "1", "3", "-2"],
            ["Male", "25", "1000", "0.5", "3", "-2.5"],
            ["Female", "56", "2500", "3.5", "3", "0.5"],
            ["Male", "58", "6000", "7.5", "3", "4.5"],
            ["Male", "46", "2400", "1.5", "3", "-1.5"]]

        table2 = Table(data,include_outer_lines=True).scale(0.35).to_edge(LEFT, buff=0.5)
        table2.add_highlighted_cell((1,1), color=GREEN)
        table2.add_highlighted_cell((1,2), color=GREEN)
        table2.add_highlighted_cell((1,3), color=GREEN)
        table2.add_highlighted_cell((1,4), color=PINK)
        table2.add_highlighted_cell((1,5), color=BLUE)
        table2.add_highlighted_cell((1,6), color=RED)

        self.play(Transform(table, table2))

        self.next_slide()

        trainer_rect = SurroundingRectangle(table2.get_columns()[:3], color=PINK)
        res_rect = SurroundingRectangle(table2.get_columns()[5], color=PINK)

        self.play(Create(trainer_rect), Create(res_rect))

        self.next_slide()

        self.play(Uncreate(trainer_rect), Uncreate(res_rect))

        self.next_slide()

        self.play(table.animate.scale(0.8).to_edge(LEFT, buff=0.5), FadeOut(form, txt, ar1, srect))

        dec1 = MathTex("House Size > 2000", color=WHITE).shift(UP*1.5, RIGHT*3).scale(0.4)
        drect1 = SurroundingRectangle(dec1, color=RED, fill_color=GREEN, fill_opacity=0.5)

        dec2 = MathTex("Age<40", color=WHITE).shift(UP*0.5+RIGHT*1.5).scale(0.4)
        drect2 = SurroundingRectangle(dec2, color=RED, fill_color=GREEN, fill_opacity=0.5)

        dec3 = MathTex("Gender=M", color=WHITE).next_to(dec2, RIGHT*4).scale(0.4)
        drect3 = SurroundingRectangle(dec3, color=RED, fill_color=GREEN, fill_opacity=0.5)

        leaf1 = Tex("1, 0", color=WHITE).next_to(dec2, DOWN*2+LEFT*0.5).scale(0.4)
        lrect1 = always_redraw(lambda : RoundedRectangle(height=leaf1.get_height()+0.25, width=leaf1.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf1))

        leaf2 = Tex("0.5, 4.5, -1.5", color=WHITE).next_to(leaf1, RIGHT*1.5).scale(0.4)
        lrect2 = always_redraw(lambda : RoundedRectangle(height=leaf2.get_height()+0.25, width=leaf2.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf2))

        leaf3 = Tex("-2.5", color=WHITE).next_to(leaf2, RIGHT*1).scale(0.4)
        lrect3 = always_redraw(lambda : RoundedRectangle(height=leaf3.get_height()+0.25, width=leaf3.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf3))

        leaf4 = Tex("-2", color=WHITE).next_to(leaf3, RIGHT*6).scale(0.4)
        lrect4 = always_redraw(lambda : RoundedRectangle(height=leaf4.get_height()+0.25, width=leaf4.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf4))

        a1 = always_redraw(lambda : Arrow(drect1.get_bottom(), drect2.get_top(), color=WHITE))
        a2 = always_redraw(lambda : Arrow(drect2.get_bottom(), lrect1.get_top(), color=WHITE))
        a3 = always_redraw(lambda : Arrow(drect2.get_bottom(), lrect2.get_top(), color=WHITE))
        a4 = always_redraw(lambda : Arrow(drect3.get_bottom(), lrect3.get_top(), color=WHITE))
        a5 = always_redraw(lambda : Arrow(drect3.get_bottom(), lrect4.get_top(), color=WHITE))
        a6 = always_redraw(lambda : Arrow(drect1.get_bottom(), drect3.get_top(), color=WHITE))

        g = VGroup(dec1, dec2, dec3, leaf1, leaf2, leaf3, leaf4, drect1, drect2, drect3, lrect1, lrect2, lrect3, lrect4, a1, a2, a3, a4, a5, a6)
        self.play(Write(g))

        self.next_slide()

        txt = MathTex(r"Learning Rate(\alpha) = 0.1", color=WHITE).shift(DOWN*3, LEFT*3.5).scale(0.75)
        trect = always_redraw(lambda : Rectangle(height=txt.get_height()+0.25, width=txt.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5).move_to(txt))

        self.play(Write(txt), DrawBorderThenFill(trect))

        self.next_slide()

        self.play(Transform(leaf1, Tex("0.5", color=WHITE).next_to(dec2, DOWN*2+LEFT*0.5).scale(0.4)))
        self.play(Transform(leaf2, Tex("1.17", color=WHITE).next_to(leaf1, RIGHT*4).scale(0.4)))
        self.play(Transform(leaf3, Tex("-2.5", color=WHITE).next_to(leaf2, RIGHT*2).scale(0.4)))

        self.next_slide()

        newt = MathTex(r"New Prediction = Old Prediction + (\alpha \times Predicted Residual) ").shift(DOWN*3, RIGHT*3.5).scale(0.4)

        self.play(Write(newt))

        self.next_slide()

        h1 = SurroundingRectangle(table.get_rows()[1], color=PINK)
        h3 = SurroundingRectangle(table.get_rows()[3], color=PINK)

        l1 = SurroundingRectangle(leaf1, color=PINK)
        l2 = SurroundingRectangle(leaf2, color=PINK)
        l3 = SurroundingRectangle(leaf3, color=PINK)
        l4 = SurroundingRectangle(leaf4, color=PINK)

        self.play(Create(h1))
        self.play(Uncreate(h1))

        self.next_slide()

        self.play(Create(l1))
        self.play(Uncreate(l1))

        self.next_slide()

        self.play(Transform(newt, MathTex(r"New Prediction = 3 + (0.1 \times (0.5))", color=WHITE).shift(DOWN*3, RIGHT*3.5).scale(0.75)))

        self.next_slide()

        self.play(Transform(newt, MathTex(r"New Prediction = 3.05", color=WHITE).shift(DOWN*3, RIGHT*3.5).scale(0.75)))

        self.next_slide()
        
        self.play(replace_table_element(2, 3, "3.05", table))

        self.next_slide()

        self.play(Create(h3))
        self.play(Uncreate(h3))

        self.next_slide()

        self.play(Create(l4))
        self.play(Uncreate(l4))

        self.next_slide()

        self.play(Transform(newt, MathTex(r"New Prediction = 3 + (0.1 \times (-2))", color=WHITE).shift(DOWN*3, RIGHT*3.5).scale(0.75)))

        self.next_slide()

        self.play(Transform(newt, MathTex(r"New Prediction = 2.8", color=WHITE).shift(DOWN*3, RIGHT*3.5).scale(0.75)))

        self.next_slide()
        
        self.play(replace_table_element(4, 3, "2.8", table))

        self.next_slide()

        self.play(replace_table_element(3,3,"3.05",table), replace_table_element(5,3,"2.75",table), replace_table_element(6,3,"3.117",table), replace_table_element(7,3,"3.117",table), replace_table_element(8,3,"3.117",table) )

        self.next_slide()

        self.play(Transform(txt, Tex("Trees have fixed number of leaves(8 to 32)").scale(0.5).shift(DOWN*3, LEFT*3.5)))

        self.play(replace_table_element(2,4,"0.95", table), replace_table_element(3,4,"0.25",table), replace_table_element(4,4,"-1.8",table), replace_table_element(5,4,"-2.25",table), replace_table_element(6,4,"0.383",table), replace_table_element(7,4,"4.383",table), replace_table_element(8,4,"-1.617",table))

        self.next_slide()
        self.play(FadeOut(table, txt, trect, g, newt))

        pred = MathTable(
            [["Gender", "Age", "House Size", "Income", "Prediction"],
            ["Male", "36", "2500", "2.5", "?"]],
            include_outer_lines=True).scale(0.4).to_edge(LEFT, buff=0.5).shift(UP*1.5)
        pred.add_highlighted_cell((1,1), color=GREEN)
        pred.add_highlighted_cell((1,2), color=GREEN)
        pred.add_highlighted_cell((1,3), color=GREEN)
        pred.add_highlighted_cell((1,4), color=PINK)
        pred.add_highlighted_cell((1,5), color=RED)

        self.play(Write(pred))

        self.next_slide()

        s1 = LabeledDot(MathTex(r"D_1", color=BLACK), color=GOLD, radius=0.7).next_to(pred, RIGHT*1.5)
        s2 = LabeledDot(MathTex(r"D_2", color=BLACK), color=GOLD, radius=0.7).next_to(s1, RIGHT*2)
        s3 = LabeledDot(MathTex(r"D_3", color=BLACK), color=GOLD, radius=0.7).next_to(s2, RIGHT*2)
        s4 = LabeledDot(MathTex(r"D_4", color=BLACK), color=GOLD, radius=0.7).next_to(s3, RIGHT*2)

        txt1 = MathTex(r"\alpha \times (-5.0)", color=RED).next_to(s1, DOWN*5).scale(0.5)
        txt0 = MathTex(r"3", color=WHITE).next_to(txt1, LEFT*3).scale(0.5)
        txt2 = MathTex(r"\alpha \times (3.5)", color=GREEN).next_to(s2, DOWN*5).scale(0.5)
        txt3 = MathTex(r"\alpha \times (1.5)", color=GREEN).next_to(s3, DOWN*5).scale(0.5)
        txt4 = MathTex(r"\alpha \times -(7.5)", color=RED).next_to(s4, DOWN*5).scale(0.5)

        a1 = Arrow(start=s1.get_bottom(), end=txt1.get_top(), color=WHITE)
        a2 = Arrow(start=s2.get_bottom(), end=txt2.get_top(), color=WHITE)
        a3 = Arrow(start=s3.get_bottom(), end=txt3.get_top(), color=WHITE)
        a4 = Arrow(start=s4.get_bottom(), end=txt4.get_top(), color=WHITE)

        plus0 = MathTex(r"+", color=WHITE).next_to(txt0, RIGHT*1)
        plus1 = MathTex(r"+", color=WHITE).next_to(txt1, RIGHT*1)
        plus2 = MathTex(r"+", color=WHITE).next_to(txt2, RIGHT*1)
        plus3 = MathTex(r"+", color=WHITE).next_to(txt3, RIGHT*1)

        ans = MathTex(r"2.25", color=GREEN).next_to(plus2, ORIGIN)

        self.play(GrowFromCenter(s1), GrowFromCenter(s2), GrowFromCenter(s3), GrowFromCenter(s4))

        self.next_slide()

        self.play(Write(txt0), Write(txt1), Write(txt2), Write(txt3), Write(txt4), GrowArrow(a1), GrowArrow(a2), GrowArrow(a3), GrowArrow(a4))

        self.next_slide()

        self.play(Write(plus0), Write(plus1), Write(plus2), Write(plus3))

        self.next_slide()

        g = VGroup(txt0, txt1, txt2, txt3, txt4, plus0, plus1, plus2, plus3)
        self.play(Transform(g, ans))

        self.next_slide()

        elem = pred.get_entries_without_labels((2,5))
        new_element = Text("2.25", color=GREEN).scale(0.5)
        new_element.move_to(elem) 

        self.play(Transform(elem,new_element))

        self.next_slide()

        self.play(FadeOut(pred, s1, s2, s3, s4, txt0, txt1, txt2, txt3, txt4, a1, a2, a3, a4, plus0, plus1, plus2, plus3, ans, elem, new_element))
        self.play(Transform(heading, Tex("XGBoost", color=WHITE).shift(UP*3).scale(1.5)))

        txt = Tex("Optimized version of Gradient Boosting").shift(LEFT*3.5, UP*2).scale(0.75)

        self.play(Write(txt))

        self.next_slide()

        self.play(Transform(txt, Tex("Efficient, Fast and Scalable").shift(LEFT*3.5, UP*2).scale(0.75)))

        self.next_slide()

        self.play(Transform(txt, Tex("Advanced Tree Pruning, Regularization and Parallel Processing").shift(LEFT*2.5, UP*2).scale(0.5)))

        self.next_slide()

        text1 = Tex("Tree 1", color=WHITE).shift(UP*1).scale(0.5)
        rect1= SurroundingRectangle(text1, color= GREEN, fill_opacity = 0.4, fill_color = RED, buff=0.3)
        l1 = Tex("Leaf", color=WHITE).next_to(rect1, LEFT*1+DOWN*2).scale(0.5)
        leaf1= SurroundingRectangle(l1, color= YELLOW, fill_opacity = 0.4, fill_color = RED)
        l2 = Tex("Leaf", color=WHITE).next_to(rect1, RIGHT*1+DOWN*2).scale(0.5)
        leaf2 = SurroundingRectangle(l2, color= YELLOW, fill_opacity = 0.4, fill_color = RED)
        a4 = Arrow(start=rect1.get_bottom(), end=leaf1.get_top(), color=WHITE, buff=0.1)
        a5 = Arrow(start=rect1.get_bottom(), end=leaf2.get_top(), color=WHITE, buff=0.1)

        g1 = VGroup(text1, rect1, l1, leaf1, l2, leaf2, a4, a5)

        txt1 = Tex("Random Forests, Gradient Boosting").shift(LEFT*3, DOWN*1.5).scale(0.5)
        txt2 = Tex("AdaBoost").shift(LEFT*3, DOWN*2).scale(0.5)
        txt3 = Tex("XGBoost").shift(LEFT*3, DOWN*2.5).scale(0.5)

        m1 = Tex("Gini Index").shift(RIGHT*3, DOWN*1.5).scale(0.5)
        mrect1 = SurroundingRectangle(m1, color= GREEN, fill_opacity = 0.4, fill_color = RED)
        m2 = Tex("Weighted Gini Index").shift(RIGHT*3, DOWN*2).scale(0.5)
        mrect2 = SurroundingRectangle(m2, color= GREEN, fill_opacity = 0.4, fill_color = RED)
        m3 = Tex("Similarity Score with Regularization").shift(RIGHT*3, DOWN*2.5).scale(0.5)
        mrect3 = SurroundingRectangle(m3, color= GREEN, fill_opacity = 0.4, fill_color = RED)

        a1 = Arrow(start=txt1.get_right(), end=mrect1.get_left(), color=WHITE)
        a2 = Arrow(start=txt2.get_right(), end=mrect2.get_left(), color=WHITE)
        a3 = Arrow(start=txt3.get_right(), end=mrect3.get_left(), color=WHITE)

        g2 = VGroup(txt1, m1, mrect1, a1)
        g3 = VGroup(txt2, m2, mrect2, a2)
        g4 = VGroup(txt3, m3, mrect3, a3)

        self.play(FadeOut(txt), Write(g1))

        self.next_slide()

        self.play(Write(g2), Write(g3), Write(g4))

        self.next_slide()

        self.play(FadeOut(g1,g2,g3), g4.animate.shift(UP*2.5,LEFT*1).scale(1.5))

        self.next_slide()

        self.play(FadeOut(g4))

        heading = Tex("XGBoost", color=WHITE).shift(UP*3).scale(1.5)

        dec1 = MathTex("House Size > 2000", color=WHITE).shift(UP*1.5, LEFT*3).scale(0.6)
        drect1 = SurroundingRectangle(dec1, color=RED, fill_color=GREEN, fill_opacity=0.5)

        dec2 = MathTex("Age<40", color=WHITE).shift(UP*0.5+LEFT*4.5).scale(0.6)
        drect2 = SurroundingRectangle(dec2, color=RED, fill_color=GREEN, fill_opacity=0.5)

        dec3 = MathTex("Gender=M", color=WHITE).next_to(dec2, RIGHT*4).scale(0.6)
        drect3 = SurroundingRectangle(dec3, color=RED, fill_color=GREEN, fill_opacity=0.5)

        leaf1 = Tex("1, 0", color=WHITE).next_to(dec2, DOWN*2+LEFT*0.5).scale(0.6)
        lrect1 = always_redraw(lambda : RoundedRectangle(height=leaf1.get_height()+0.25, width=leaf1.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf1))

        leaf2 = Tex("0.5, 4.5, -1.5", color=WHITE).next_to(leaf1, RIGHT*1.5).scale(0.6)
        lrect2 = always_redraw(lambda : RoundedRectangle(height=leaf2.get_height()+0.25, width=leaf2.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf2))

        leaf3 = Tex("-2.5", color=WHITE).next_to(leaf2, RIGHT*1).scale(0.6)
        lrect3 = always_redraw(lambda : RoundedRectangle(height=leaf3.get_height()+0.25, width=leaf3.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf3))

        leaf4 = Tex("-2", color=WHITE).next_to(leaf3, RIGHT*5).scale(0.6)
        lrect4 = always_redraw(lambda : RoundedRectangle(height=leaf4.get_height()+0.25, width=leaf4.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf4))

        a1 = always_redraw(lambda : Arrow(drect1.get_bottom(), drect2.get_top(), color=WHITE))
        a2 = always_redraw(lambda : Arrow(drect2.get_bottom(), lrect1.get_top(), color=WHITE))
        a3 = always_redraw(lambda : Arrow(drect2.get_bottom(), lrect2.get_top(), color=WHITE))
        a4 = always_redraw(lambda : Arrow(drect3.get_bottom(), lrect3.get_top(), color=WHITE))
        a5 = always_redraw(lambda : Arrow(drect3.get_bottom(), lrect4.get_top(), color=WHITE))
        a6 = always_redraw(lambda : Arrow(drect1.get_bottom(), drect3.get_top(), color=WHITE))

        g = VGroup(dec1, drect1, dec2, drect2, dec3, drect3, leaf1, lrect1, leaf2, lrect2, leaf3, lrect3, leaf4, lrect4, a1, a2, a3, a4, a5, a6)
        self.play(Write(g))

        txt1 = Tex("Similarity Score = ", color=BLUE).shift(UP*0.5, RIGHT*1.5).scale(0.6)
        form1 = MathTex(r"\frac{Square of Sum of Residuals}{No. of Residuals + }", color=WHITE).shift(UP*0.5,RIGHT*4.75).scale(0.6)
        lmb = MathTex(r"\lambda", color=RED).shift(RIGHT*6.1, UP*0.3).scale(0.6)
        g1 = VGroup(txt1, form1, lmb)
        srect1 = SurroundingRectangle(g1, color=GREEN, fill_opacity=0.4, fill_color=GOLD)

        txt2 = Tex("Information Gain =", color=BLUE).shift(DOWN*1, RIGHT*2).scale(0.6)
        form2 = MathTex(r"S_{parent}-S_{right}", color=WHITE).shift(DOWN*1,RIGHT*4.75).scale(0.6)
        form2alt = MathTex(r"S_{parent}-S_{left}", color=WHITE).shift(DOWN*1,RIGHT*4.75).scale(0.6)
        g2 = VGroup(txt2, form2)
        srect2 = SurroundingRectangle(g2, color=GREEN, fill_opacity=0.4, fill_color=GOLD)

        self.next_slide()

        self.play(Write(txt1), Write(form1), DrawBorderThenFill(srect1), Write(lmb))

        self.next_slide()

        self.play(Write(txt2), Write(form2), DrawBorderThenFill(srect2))

        self.next_slide()

        self.play(Transform(form2, form2alt))

        self.next_slide()

        txt3 = Tex("Pruning Parameter = ", color=BLUE).shift(DOWN*2, RIGHT*3).scale(0.6)
        form3 = MathTex(r"\gamma", color=WHITE).shift(DOWN*2,RIGHT*4.75).scale(0.6)
        g3 = VGroup(txt3, form3)
        srect3 = SurroundingRectangle(g3, color=GREEN, fill_opacity=0.4, fill_color=GOLD)

        self.play(Write(txt3), Write(form3), DrawBorderThenFill(srect3))

        self.next_slide()
        
        s1 = SurroundingRectangle(leaf2, color=PINK)
        self.play(Create(s1))
        self.play(Uncreate(s1))
        self.play(Transform(form1, MathTex(r"\frac{(0.5 + 4.5 - 1.5)^2}{3 + 1}", color=WHITE).shift(UP*0.5,RIGHT*4.75).scale(0.6)), FadeOut(lmb))

        self.next_slide()

        self.play(Transform(form1, MathTex(r"3.38", color=WHITE).shift(UP*0.5,RIGHT*4.75).scale(0.6)))

        ls2 = Tex("3.06").next_to(leaf2, DOWN).scale(0.6)

        self.next_slide()

        self.play(Write(ls2), Transform(form1, MathTex(r"\frac{Square of Sum of Residuals}{No. of Residuals + }", color=WHITE).shift(UP*0.5,RIGHT*4.75).scale(0.6)), FadeIn(lmb))

        self.next_slide()

        ds2 = Tex("3.38").next_to(dec2, LEFT).scale(0.6)

        self.play(Write(ds2))

        self.next_slide()

        self.play(Transform(form2, MathTex(r"3.38-3.06", color=WHITE).shift(DOWN*1,RIGHT*4.75).scale(0.6)))

        self.next_slide()

        self.play(Transform(form2, MathTex(r"0.32", color=WHITE).shift(DOWN*1,RIGHT*4.75).scale(0.6)))

        self.next_slide()

        ig1 = Tex("0.32", color=BLUE).next_to(a3, RIGHT).scale(0.5)
        self.play(Write(ig1), Transform(form2, MathTex(r"S_{parent}-S_{right}", color=WHITE).shift(DOWN*1,RIGHT*4.75).scale(0.6)))

        self.next_slide()

        form4 = MathTex(r"\lambda =", color=RED).next_to(leaf1, DOWN*6).scale(0.6)
        txt4 = Tex("Regularization Parameter", color=WHITE).next_to(leaf2, DOWN*6).scale(0.6)

        self.play(Write(form4), Write(txt4))

        self.next_slide()

        self.play(Transform(txt4, Tex("Prune when $$\\gamma > I.G.$$").next_to(dec2, DOWN*7).scale(0.6)), FadeOut(form4))

        self.next_slide()

        self.play(form2.animate.scale(0.5))
        self.play(txt2.animate.scale(0.5))

        self.next_slide()

        self.play(FadeOut(g, g1, g2, g3, srect1, srect2, srect3, txt4, ig1, ds2, ls2, heading))

# class A(Slide):
#     def construct(self):
#         # Create the title "Ensemble Methods"
#         title = Tex("Ensemble Methods", color=WHITE).scale(1.5)
#         ens = Tex("'Ensemble'", color=BLUE).scale(1.5)
#         self.play(Write(title))
#         self.next_slide()

#         # Move the title to the top of the screen and simultaneously fade in an svg image called "orchestra.svg" in the middle of the page
#         d = SVGMobject("Drums.svg").shift(LEFT*2)
#         g = SVGMobject("Guitar.svg").shift(RIGHT*2)
#         t = SVGMobject("Trumpet.svg").shift(DOWN*2)
#         self.play(Transform(title, ens), run_time=1)
#         self.play(title.animate.to_edge(UP), FadeIn(d), FadeIn(g), FadeIn(t), run_time=1)

#         self.next_slide()

#         # Move all three images in the middle of the screen while transforming them to "orchestra.svg"
#         orchestra = SVGMobject("Orchestra.svg").scale(2)
#         self.play(d.animate.shift(LEFT*2), g.animate.shift(RIGHT*2), t.animate.shift(DOWN*2), Transform(d, orchestra), Transform(g, orchestra), Transform(t, orchestra), run_time=1)
        
#         self.next_slide()

#         #Create a identical structures using rectangles and arrows and leaves with rounded corners that look like decision trees with one split, side by side, and combine them into a single tree in the middle of the screen
#         self.play(FadeOut(orchestra, d, g, t, ens))
        
# class B(Slide):
#     def construct(self):
        
#         text1 = Tex("Tree 1", color=WHITE).shift(LEFT*3, UP*2)
#         rect1= SurroundingRectangle(text1, color= YELLOW, fill_opacity = 0.4, fill_color = RED, buff=0.5)
#         l1 = Tex("Leaf", color=WHITE).shift(LEFT*5, DOWN)
#         leaf1= SurroundingRectangle(l1, color= YELLOW, fill_opacity = 0.4, fill_color = RED)
#         l2 = Tex("Leaf", color=WHITE).shift(LEFT*1, DOWN)
#         leaf2= SurroundingRectangle(l2, color= YELLOW, fill_opacity = 0.4, fill_color = RED)
#         text2 = Tex("Tree 2", color=WHITE).shift(RIGHT*3, UP*2)
#         rect2= SurroundingRectangle(text2, color= YELLOW, fill_opacity = 0.4, fill_color = GREEN, buff=0.5)
#         l3 = Tex("Leaf", color=WHITE).shift(RIGHT*5, DOWN)
#         leaf3= SurroundingRectangle(l3, color= YELLOW, fill_opacity = 0.4, fill_color = GREEN)
#         l4 = Tex("Leaf", color=WHITE).shift(RIGHT*1, DOWN)
#         leaf4= SurroundingRectangle(l4, color= YELLOW, fill_opacity = 0.4, fill_color = GREEN)
        
#         arrow1 = Arrow(rect1.get_bottom(), leaf1.get_top(), color=BLUE)
#         arrow2 = Arrow(rect1.get_bottom(), leaf2.get_top(), color=BLUE)
#         arrow3 = Arrow(rect2.get_bottom(), leaf3.get_top(), color=BLUE)
#         arrow4 = Arrow(rect2.get_bottom(), leaf4.get_top(), color=BLUE)
        
#         self.play(FadeIn(VGroup(rect1, text1,rect2, text2)), FadeIn(VGroup(leaf1, l1,leaf2, l2,leaf3, l3,leaf4, l4)), FadeIn(VGroup(arrow1, arrow2, arrow3, arrow4)), run_time=2)
        
#         self.next_slide()

#         # Move both trees to the middle of the screen and combine them into a single tree

#         text3 = Tex("Stronger Tree", color=WHITE).shift(UP*2)
#         rect3= SurroundingRectangle(text3, color= GREEN, fill_opacity = 0.4, fill_color = BLUE, buff=0.5)
#         l5 = Tex("Leaf", color=WHITE).shift(LEFT*1, DOWN)
#         leaf5= SurroundingRectangle(l5, color= GREEN, fill_opacity = 0.4, fill_color = BLUE)
#         l6 = Tex("Leaf", color=WHITE).shift(RIGHT*1, DOWN)
#         leaf6= SurroundingRectangle(l6, color= GREEN, fill_opacity = 0.4, fill_color = BLUE)

#         arrow5 = Arrow(rect3.get_bottom(), leaf5.get_top(), color=BLUE)
#         arrow6 = Arrow(rect3.get_bottom(), leaf6.get_top(), color=BLUE)

#         # Use Transform to combine the two trees into a single tree

#         self.play(Transform(VGroup(rect1, text1,rect2, text2, leaf1, l1,leaf2, l2,leaf3, l3,leaf4, l4, arrow1, arrow2, arrow3, arrow4), VGroup(rect3, text3, leaf5, l5,leaf6, l6, arrow5, arrow6)), run_time=2)

#         self.next_slide()

#         self.play(FadeOut(VGroup(rect3, text3, leaf5, l5,leaf6, l6, arrow5, arrow6)))

# class C(Slide):
#     def construct(self):
        
#         title = Tex("Ensemble Methods", color=WHITE)
#         title2 = Tex("Ensemble Methods", color=WHITE)
#         bagging = Tex("Bagging", color=WHITE).shift(LEFT*2)
#         boosting = Tex("Boosting", color=WHITE).shift(RIGHT*2)

#         # Create title, then transform it into the other two texts

#         self.play(Create(title))
#         self.play(Transform(title, bagging), Transform(title2, boosting), run_time=2)

#         self.next_slide()

#         self.play(FadeOut(title2), title.animate.shift(UP*3,RIGHT*2).scale(1.5))
#         rect = SurroundingRectangle(title, color= YELLOW, fill_opacity = 0.4, fill_color = RED, buff=0.3)
#         self.play(Create(rect))

#         self.next_slide()

class D(Slide):
    def construct(self):
        
        heading = Tex("Original Data", color=WHITE).scale(0.75).shift(UP*3.5)

        circ1 = Dot(color = RED).shift(LEFT*2, UP*3)
        circ2 = Dot(color = BLUE).shift(LEFT*1.5, UP*3)
        circ3 = Dot(color = RED).shift(LEFT*1, UP*3)
        circ4 = Dot(color = GREEN).shift(LEFT*0.5, UP*3)
        circ5 = Dot(color = GREEN).shift(LEFT*0, UP*3)
        circ6 = Dot(color = PINK).shift(RIGHT*0.5, UP*3)
        circ7 = Dot(color = DARK_BROWN).shift(RIGHT*1, UP*3)
        circ8 = Dot(color = RED).shift(RIGHT*1.5, UP*3)
        circ9 = Dot(color = ORANGE).shift(RIGHT*2, UP*3)
        circ10 = Dot(color = GOLD).shift(LEFT*2, UP*2.5) 
        circ11 = Dot(color = YELLOW).shift(LEFT*1.5, UP*2.5)
        circ12 = Dot(color = WHITE).shift(LEFT*1, UP*2.5)
        circ13 = Dot(color = RED).shift(LEFT*0.5, UP*2.5)
        circ14 = Dot(color = GOLD).shift(LEFT*0, UP*2.5)
        circ15 = Dot(color = PURPLE).shift(RIGHT*0.5, UP*2.5)
        circ16 = Dot(color = PINK).shift(RIGHT*1, UP*2.5)
        circ17 = Dot(color = DARK_BROWN).shift(RIGHT*1.5, UP*2.5)
        circ18 = Dot(color = PURPLE).shift(RIGHT*2, UP*2.5)

        data_rect = SurroundingRectangle(VGroup(circ1, circ2, circ3, circ4, circ5, circ6, circ7, circ8, circ9, circ10, circ11, circ12, circ13, circ14, circ15, circ16, circ17, circ18), color= YELLOW, buff=0.1)
        
        circ19 = Dot(color = WHITE).shift(LEFT*6, UP*1)
        circ20 = Dot(color = ORANGE).shift(LEFT*5.5, UP*1)
        circ21 = Dot(color = RED).shift(LEFT*5, UP*1)
        circ22 = Dot(color = GREEN).shift(LEFT*4.5, UP*1)
        circ23 = Dot(color = PURPLE).shift(LEFT*4, UP*1)

        data_rect2 = SurroundingRectangle(VGroup(circ19, circ20, circ21, circ22, circ23), color= YELLOW, buff=0.1)

        circ24 = Dot(color = RED).shift(LEFT*1, UP*1)
        circ25 = Dot(color = ORANGE).shift(LEFT*0.5, UP*1)
        circ26 = Dot(color = PINK).shift(LEFT*0, UP*1)
        circ27 = Dot(color = DARK_BROWN).shift(RIGHT*0.5, UP*1)
        circ28 = Dot(color = WHITE).shift(RIGHT*1, UP*1)

        data_rect3 = SurroundingRectangle(VGroup(circ24, circ25, circ26, circ27, circ28), color= YELLOW, buff=0.1)

        circ29 = Dot(color = GOLD).shift(RIGHT*6, UP*1)
        circ30 = Dot(color = GREEN).shift(RIGHT*5.5, UP*1)
        circ31 = Dot(color = GOLD).shift(RIGHT*5, UP*1)
        circ32 = Dot(color = PINK).shift(RIGHT*4.5, UP*1)
        circ33 = Dot(color = ORANGE).shift(RIGHT*4, UP*1)

        data_rect4 = SurroundingRectangle(VGroup(circ29, circ30, circ31, circ32, circ33), color= YELLOW, buff=0.1)

        arr1 = Arrow(data_rect.get_bottom(), data_rect2.get_top(), color=BLUE, buff=0.5)
        arr2 = Arrow(data_rect.get_bottom(), data_rect3.get_top(), color=BLUE)
        arr3 = Arrow(data_rect.get_bottom(), data_rect4.get_top(), color=BLUE, buff=0.5)

        t1 = Tex("Model 1", color=WHITE).shift(LEFT*5, DOWN*1)
        t2 = Tex("Model 2", color=WHITE).shift(LEFT*0, DOWN*1)
        t3 = Tex("Model 3", color=WHITE).shift(RIGHT*5, DOWN*1)

        data_rect5 = SurroundingRectangle(t1, color= YELLOW, buff=0.5, fill_opacity=0.4, fill_color=RED)
        data_rect6 = SurroundingRectangle(t2, color= YELLOW, buff=0.5, fill_opacity=0.4, fill_color=RED)
        data_rect7 = SurroundingRectangle(t3, color= YELLOW, buff=0.5, fill_opacity=0.4, fill_color=RED)

        c1 = Tex("Classifier 1", color=WHITE).shift(LEFT*5, DOWN*1)
        c2 = Tex("Classifier 2", color=WHITE).shift(LEFT*0, DOWN*1)
        c3 = Tex("Classifier 3", color=WHITE).shift(RIGHT*5, DOWN*1)

        r1 = Tex("Regressor 1", color=WHITE).shift(LEFT*5, DOWN*1)
        r2 = Tex("Regressor 2", color=WHITE).shift(LEFT*0, DOWN*1)
        r3 = Tex("Regressor 3", color=WHITE).shift(RIGHT*5, DOWN*1)

        arr4 = Arrow(data_rect2.get_bottom(), data_rect5.get_top(), color=BLUE)
        arr5 = Arrow(data_rect3.get_bottom(), data_rect6.get_top(), color=BLUE)
        arr6 = Arrow(data_rect4.get_bottom(), data_rect7.get_top(), color=BLUE)

        en_mod = Tex("Ensemble Model", color=WHITE).shift(DOWN*3)
        en_modr = SurroundingRectangle(en_mod, color= YELLOW, buff=0.3, fill_opacity=0.4, fill_color=GREEN, corner_radius=0.2)

        arr7 = Arrow(data_rect5.get_bottom(), en_modr.get_top(), color=BLUE, buff=0.7)
        arr8 = Arrow(data_rect6.get_bottom(), en_modr.get_top(), color=BLUE, buff=0.7)
        arr9 = Arrow(data_rect7.get_bottom(), en_modr.get_top(), color=BLUE, buff=0.7)

        self.play(FadeIn(heading))
        self.play(Create(data_rect), Create(VGroup(circ1, circ2, circ3, circ4, circ5, circ6, circ7, circ8, circ9, circ10, circ11, circ12, circ13, circ14, circ15, circ16, circ17, circ18)))
        self.play(Create(arr1), Create(arr2), Create(arr3))
        self.play(Create(data_rect2), Create(VGroup(circ19, circ20, circ21, circ22, circ23)), Create(data_rect3), Create(VGroup(circ24, circ25, circ26, circ27, circ28)), Create(data_rect4), Create(VGroup(circ29, circ30, circ31, circ32, circ33)))
        self.play(Create(arr4), Create(arr5), Create(arr6))
        self.play(FadeIn(t1), FadeIn(t2), FadeIn(t3), DrawBorderThenFill(data_rect5), DrawBorderThenFill(data_rect6), DrawBorderThenFill(data_rect7))
        self.play(Create(arr7), Create(arr8), Create(arr9))
        self.play(FadeIn(en_mod), DrawBorderThenFill(en_modr))

        self.next_slide()

        self.play(Transform(t1,c1), Transform(t2,c2), Transform(t3,c3))

        self.next_slide()

        self.play(Transform(t1,r1), Transform(t2,r2), Transform(t3,r3))

        self.next_slide()

        disrect = Rectangle(height=1.5, width=13, color=WHITE).shift(UP*1.5)
        disrect1 = Rectangle(height=0.5, width=10, color=WHITE).shift(DOWN*2)
        boot = Tex("Bootstrapping", color=WHITE).shift(UP*3, LEFT*4)
        aggr = Tex("Aggregation", color=WHITE).shift(UP*3, LEFT*4)

        self.play(Create(disrect), Write(boot))
        self.play(Uncreate(disrect))

        self.next_slide()

        self.play(Create(disrect1), Transform(boot, aggr))
        self.play(Uncreate(disrect1))

        self.next_slide()

        self.play(FadeOut(VGroup(heading, data_rect, circ1, circ2, circ3, circ4, circ5, circ6, circ7, circ8, circ9, circ10, circ11, circ12, circ13, circ14, circ15, circ16, circ17, circ18, arr1, arr2, arr3, data_rect2, circ19, circ20, circ21, circ22, circ23, data_rect3, circ24, circ25, circ26, circ27, circ28, data_rect4, circ29, circ30, circ31, circ32, circ33, arr4, arr5, arr6, t1, t2, t3, data_rect5, data_rect6, data_rect7, arr7, arr8, arr9, en_mod, en_modr, c1, c2, c3, r1, r2, r3, disrect, disrect1, boot, aggr)))


# class F2(Slide):
#     def construct(self):
#         heading = Tex("Bootstrapping", color=WHITE).shift(UP*3)
#         table = Table(
#             [["Gender", "Age", "Weight", "Height"],
#             ["Male", "19", "70", "180"],
#             ["Female", "20", "60", "170"],
#             ["Female", "21", "55", "175"],
#             ["Male", "22", "80", "185"],
#             ["Female", "23", "50", "160"],
#             ["Male", "24", "75", "190"],
#             ["Male", "25", "85", "195"]],
#             include_outer_lines=True).scale(0.4).to_edge(LEFT)
#         table.add_highlighted_cell((1,1), color=GREEN)
#         table.add_highlighted_cell((1,2), color=RED)
#         table.add_highlighted_cell((1,3), color=YELLOW)
#         table.add_highlighted_cell((1,4), color=BLUE)

#         v = table.get_vertical_lines().copy().next_to(table, ORIGIN)
#         tops = table.get_rows()[0].copy()
#         htops = table.get_horizontal_lines()[:2].copy()
#         part1 = table.get_rows()[1].copy()
#         h1 = table.get_horizontal_lines()[2:4].copy()
#         part2 = table.get_rows()[3].copy()
#         h2 = table.get_horizontal_lines()[4:6].copy()
#         part3 = table.get_rows()[3].copy()
#         h3 = table.get_horizontal_lines()[4:6].copy()
#         part4 = table.get_rows()[2].copy()
#         h4 = table.get_horizontal_lines()[3:5].copy()
#         part5 = table.get_rows()[5].copy()
#         h5 = table.get_horizontal_lines()[6:8].copy()
#         part6 = table.get_rows()[6].copy()
#         h6 = table.get_horizontal_lines()[7:9].copy()

#         row1 = VGroup(part1, h1)
#         row2 = VGroup(part2, h2)
#         row3 = VGroup(part3, h3)
#         row4 = VGroup(part4, h4)
#         row5 = VGroup(part5, h5)
#         row6 = VGroup(part6, h6)
#         v1 = VGroup(v, tops, htops)

#         self.play(FadeIn(heading), Write(table))

#         self.next_slide()

#         self.play(row1.animate.shift(RIGHT*7))
#         self.play(row2.animate.next_to(row1, DOWN, buff=0))
#         self.play(row3.animate.next_to(row2, DOWN, buff=0))

#         self.next_slide()

#         subset1 = VGroup(row1, row2, row3)
        
#         h = Tex("Aggregation", color=WHITE).shift(UP*3)
#         self.play(Transform(heading,Tex("Aggregation", color=WHITE).shift(UP*3)), subset1.animate.shift(LEFT*7), FadeOut(table), FadeIn(v1))

#         self.next_slide()
         
#         self.play(Transform(heading, Tex("Classification", color=WHITE).shift(UP*3, LEFT*4)), Transform(h, Tex("Regression", color=WHITE).shift(UP*3, RIGHT*4)))

#         self.next_slide()

#         data = [["Diabetes Prediction"],
#             ["..."],
#             ["..."],
#             ["..."],
#             ]
#         pred = Table(data,
#             include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
#         brace = Brace(pred, direction=RIGHT, color=RED)

#         arr1 = Arrow(start=row2.get_right(), end=pred.get_entries((2,1)), color=WHITE)
#         arr2 = Arrow(start=row2.get_right(), end=pred.get_entries((3,1)), color=WHITE)
#         arr3 = Arrow(start=row2.get_right(), end=pred.get_entries((4,1)), color=WHITE)

#         self.play(FadeOut(h), heading.animate.shift(RIGHT*4))

#         self.next_slide()

#         self.play(Create(arr1))
#         data[1][0] = "Yes"
#         pred = Table(data,
#             include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
#         pred.add_highlighted_cell((1,1), color=PINK)
#         pred.add_highlighted_cell((2,1), color=RED)
#         self.play(FadeIn(pred))
#         self.next_slide()
        
#         self.play(FadeOut(pred,arr1), Create(arr2), Transform(row1,row4), Transform(row2,row5), Transform(row3,row6))
#         data[2][0] = "Yes"
#         pred = Table(data,
#             include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
#         pred.add_highlighted_cell((1,1), color=PINK)
#         pred.add_highlighted_cell((2,1), color=RED)
#         pred.add_highlighted_cell((3,1), color=RED)
#         self.play(FadeIn(pred))
#         self.next_slide()

#         self.play(FadeOut(pred,arr2), Create(arr3), Transform(row1,row5), Transform(row2,row3), Transform(row3,row1))
#         data[3][0] = "No"
#         pred = Table(data,
#             include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
#         pred.add_highlighted_cell((1,1), color=PINK)
#         pred.add_highlighted_cell((2,1), color=RED)
#         pred.add_highlighted_cell((3,1), color=RED)
#         pred.add_highlighted_cell((4,1), color=GREEN)
#         self.play(FadeIn(pred))

#         self.next_slide()

#         self.play(GrowFromCenter(brace))

#         p = pred.get_entries((3,1)).copy()
#         self.play(p.animate.shift(RIGHT*3))

#         predictions = LabeledDot(Tex("Yes", color=WHITE), color=RED, radius=0.5).next_to(p, ORIGIN)

#         srect = SurroundingRectangle(heading, color=WHITE, fill_opacity=0.5, fill_color=PINK, buff=0.3)

#         self.play(Transform(heading, Tex("Max Voting", color=WHITE).shift(UP*3)), DrawBorderThenFill(srect),GrowFromCenter(predictions), FadeOut(p))

#         self.next_slide()

#         self.play(FadeOut(pred, brace, arr3, predictions, srect, row1, row2, row3), Transform(heading, Tex("Regression", color=WHITE).shift(UP*3)))
        
#         pred1 = Table(data,
#             include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
#         data1 = [["Income"],
#             ["..."],
#             ["..."],
#             ["..."],
#             ]
#         self.next_slide()

#         self.play(Create(arr1), FadeIn(row1), FadeIn(row6), FadeIn(row4))   
#         data1[1][0] = "2.5"
#         pred1 = Table(data1,
#             include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
#         pred1.add_highlighted_cell((1,1), color=PINK)
#         self.play(FadeIn(pred1))

#         self.next_slide()    

#         self.play(FadeOut(pred1, arr1), Create(arr2), Transform(row1,row5), Transform(row6,row2), Transform(row4,row3))
#         data1[2][0] = "1"
#         pred1 = Table(data1,
#             include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
#         pred1.add_highlighted_cell((1,1), color=PINK)
#         self.play(FadeIn(pred1))

#         self.next_slide()

#         self.play(FadeOut(pred1, arr2), Create(arr3), Transform(row1,row3), Transform(row6,row4), Transform(row4,row6))
#         data1[3][0] = "3.5"
#         pred1 = Table(data1,
#             include_outer_lines=True).scale(0.4).shift(UP*1, RIGHT*1)
#         pred1.add_highlighted_cell((1,1), color=PINK)
#         self.play(FadeIn(pred1))

#         self.next_slide()

#         p1 = pred1.get_entries((2,1)).copy()
#         p2 = pred1.get_entries((3,1)).copy()
#         p3 = pred1.get_entries((4,1)).copy()
#         frac1 = MathTex(r"\frac{2.5 + 1 + 3.5}{3}", color=WHITE).shift(RIGHT*5, UP*1)
#         self.play(Transform(p1, frac1), Transform(p2, frac1), Transform(p3, frac1))
        
#         self.play(FadeOut(p1,p2), Transform(p3, Tex("2.33").shift(RIGHT*5, UP*1)), Transform(heading, Tex("Averaging").shift(UP*3)), DrawBorderThenFill(srect))

#         self.next_slide()

#         self.play(FadeOut(p3, heading, srect, row1, row4, row6, arr3, v1, pred1))



# class F3(Slide):
#     def construct(self):
#         heading = Tex("Bootstrapping Advantages", color=WHITE).shift(UP*3).scale(1.5)
#         self.play(Write(heading))

#         self.next_slide()
        
#         dot = Dot(color=WHITE).to_edge(LEFT).shift(UP*2)
#         txt = Tex("Reduces algebraic calculations", color=WHITE).next_to(dot, RIGHT).scale(0.75)

#         self.play(GrowFromCenter(dot), Write(txt))

#         self.next_slide()

#         thous = Tex("Thousand Heights", color=WHITE).shift(LEFT*5, UP*0.5).scale(0.75)
#         variance = MathTex(r"Var(\bar{X}) = \frac{\sum_{i=1}^{1000}(x_i - \mu)^2}{1000}", color=WHITE).shift(UP*0.5, RIGHT*3).scale(0.75)
#         arr = Arrow (start=thous.get_right(), end=variance.get_left(), color=WHITE).scale(0.75)
#         comp = Tex("Computing Variance", color=WHITE).next_to(arr, UP, buff=0).scale(0.75)

#         self.play(GrowFromCenter(thous), GrowFromCenter(variance), GrowArrow(arr), Write(comp))

#         self.next_slide()

#         mast = VGroup(thous, variance, arr, comp)
#         f = Tex("Five Heights", color=WHITE).shift(LEFT*5, UP*0.5).scale(0.75)
#         f1 = VGroup(f.copy().scale(0.75), MathTex(r"Var(\bar{X}_1) = \frac{\sum_{i=1}^{5}(x_i - \mu)^2}{5}", color=WHITE).shift(UP*0.5, RIGHT*3).scale(0.75), arr.copy().scale(0.75), comp.copy().scale(0.75)).shift(UP*0)
#         f2 = VGroup(f.copy().scale(0.75), MathTex(r"Var(\bar{X}_2) = \frac{\sum_{i=1}^{5}(x_i - \mu)^2}{5}", color=WHITE).shift(UP*0.5, RIGHT*3).scale(0.75), arr.copy().scale(0.75), comp.copy().scale(0.75)).shift( DOWN*1)
#         f3 = VGroup(f.copy().scale(0.75), MathTex(r"Var(\bar{X}_3) = \frac{\sum_{i=1}^{5}(x_i - \mu)^2}{5}", color=WHITE).shift(UP*0.5, RIGHT*3).scale(0.75), arr.copy().scale(0.75), comp.copy().scale(0.75)).shift( DOWN*2)
#         f4 = VGroup(f.copy().scale(0.75), MathTex(r"Var(\bar{X}_4) = \frac{\sum_{i=1}^{5}(x_i - \mu)^2}{5}", color=WHITE).shift(UP*0.5, RIGHT*3).scale(0.75), arr.copy().scale(0.75), comp.copy().scale(0.75)).shift( DOWN*3)
#         f5 = VGroup(f.copy().scale(0.75), MathTex(r"Var(\bar{X}_5) = \frac{\sum_{i=1}^{5}(x_i - \mu)^2}{5}", color=WHITE).shift(UP*0.5, RIGHT*3).scale(0.75), arr.copy().scale(0.75), comp.copy().scale(0.75)).shift( DOWN*4)

#         self.play(TransformFromCopy(mast, f1), TransformFromCopy(mast, f2), TransformFromCopy(mast, f3), TransformFromCopy(mast, f4), Transform(mast, f5))

#         self.next_slide()

#         resvar = MathTex(r"Var(\bar{X}) = \frac{\sum_{i=1}^{5}Var(\bar{X}_i)}{5}", color=WHITE)

#         self.play(Transform(f1, resvar), Transform(f2, resvar), Transform(f3, resvar), Transform(f4, resvar), Transform(f5, resvar), Transform(mast, resvar))

#         self.next_slide()

#         self.play(FadeOut(f1, f2, f3, f4, f5, mast, resvar, dot, txt))

#         txt = Tex("Reduces Variance", color=WHITE).shift(UP*2).scale(0.75)

#         self.play(Write(txt))

#         self.next_slide()

#         # Create two y = x^2 side by side and show the variance by plotting points in both the graphs and joining them with a red line

#         plane = NumberPlane(x_range=(-3,3,1), x_length=12, y_range=(-1,10,1), y_length=6, color=WHITE, background_line_style={
#                 "stroke_color": WHITE,
#                 "stroke_width": 1,
#                 "stroke_opacity": 0.2
#             }).add_coordinates()
#         graph = plane.plot(lambda x: x**2, x_range=[-3, 3], color=BLUE)
        

#         self.play(Write(plane), Write(graph), FadeOut(txt))

#         self.next_slide()
#         # Plot points on the graph and show the variance

#         dots = VGroup()
        
#         for i in range(30):
#             x = np.random.uniform(-3, 3)
#             dots.add(Dot(color=PINK).move_to(plane.c2p(x, x**2 + np.random.uniform(-2, 2))).scale(0.5))

#         self.play(GrowFromCenter(dots))

#         # Draw a spline function passing through all the points

#         self.next_slide()

#         # Sort the points in dots with respect to x coordinate

#         dots.sort(lambda p: p[0])
#         spline = VMobject()
#         spline.set_points_smoothly([dot.get_center() for dot in dots])
#         spline.set_color(RED)

#         # Always redraw the spline function passing through all the points when the points are changed

#         self.play(Create(spline), Transform(heading, Tex("Overfitting", color=WHITE).shift(UP*3.5).scale(1)))
#         self.wait(2)

#         self.next_slide()

#         self.play(Transform(heading, Tex("High Variance", color=WHITE).shift(UP*3.5).scale(1)))

#         # Add five new points to dots
#         for i in range(5):
#             x = np.random.uniform(-3, 3)
#             dots.add(Dot(color=PINK).move_to(plane.c2p(x, x**2 + np.random.uniform(-1, 1))).scale(0.5))
#             dots.sort(lambda p: p[0])
#             spline.set_points_smoothly([dot.get_center() for dot in dots])
#             self.play(Create(spline))
#             self.next_slide()

#         self.play(FadeOut(spline))

#         # Draw a straight line trying to fit all the points
        
#         line = Line(plane.c2p(-2, 0), plane.c2p(3, 3), color=RED)

#         self.play(Create(line),Transform(heading, Tex("Underfitting", color=WHITE).shift(UP*3.5).scale(1)))

#         self.next_slide()

#         self.play(Transform(heading, Tex("High Bias", color=WHITE).shift(UP*3.5).scale(1)))

#         self.next_slide()

#         self.play(FadeOut(plane, graph, dots, line, heading))

# class F4(Slide):
#     def construct(self):
#         heading = Tex("Random Forests", color=WHITE).shift(UP*3).scale(1.5)

#         self.play(Write(heading))

#         self.next_slide()

#         dot = Dot(color=WHITE).to_edge(LEFT).shift(UP*2).to_edge(LEFT)
#         txt = Tex("Bagging applied on a bunch of Decision Trees", color=WHITE).shift(UP*2, LEFT*2).scale(0.75)

#         self.play(GrowFromCenter(dot), Write(txt))

#         self.next_slide()

#         table = Table(
#             [["Gender", "Age", "Weight", "Height"],
#             ["Male", "30", "70", "180"],
#             ["Female", "35", "60", "170"],
#             ["Female", "41", "55", "175"],
#             ["Male", "25", "80", "185"],
#             ["Female", "56", "50", "160"],
#             ["Male", "58", "75", "190"],
#             ["Male", "46", "85", "195"]],
#             row_labels=[Text("Features"), Text("R1"), Text("R2"), Text("R3"), Text("R4"), Text("R5"), Text("R6"), Text("R7")],
#             col_labels=[Text("F1"), Text("F2"), Text("F3"), Text("F4")],
#             include_outer_lines=True).scale(0.4).scale(0.8).to_edge(LEFT).shift(DOWN)
#         table.add_highlighted_cell((2,2), color=GREEN)
#         table.add_highlighted_cell((2,3), color=RED)
#         table.add_highlighted_cell((2,4), color=YELLOW)
#         table.add_highlighted_cell((2,5), color=BLUE)

#         self.play(Write(table))

#         self.next_slide()

#         h1 = table.get_highlighted_cell((3,2), color=PINK, fill_opacity=0.5)
#         h2 = table.get_highlighted_cell((4,2), color=PINK, fill_opacity=0.5)
#         h3 = table.get_highlighted_cell((5,2), color=PINK, fill_opacity=0.5)
#         h4 = table.get_highlighted_cell((6,2), color=PINK, fill_opacity=0.5)
#         h5 = table.get_highlighted_cell((7,2), color=PINK, fill_opacity=0.5)
#         h6 = table.get_highlighted_cell((8,2), color=PINK, fill_opacity=0.5)
#         h7 = table.get_highlighted_cell((9,2), color=PINK, fill_opacity=0.5)
#         h8 = table.get_highlighted_cell((9,3), color=PINK, fill_opacity=0.5)
#         h9 = table.get_highlighted_cell((3,3), color=PINK, fill_opacity=0.5)
#         h10 = table.get_highlighted_cell((4,3), color=PINK, fill_opacity=0.5)
#         h11 = table.get_highlighted_cell((5,3), color=PINK, fill_opacity=0.5)
#         h12 = table.get_highlighted_cell((6,3), color=PINK, fill_opacity=0.5)
#         h13 = table.get_highlighted_cell((7,3), color=PINK, fill_opacity=0.5)
#         h14 = table.get_highlighted_cell((8,3), color=PINK, fill_opacity=0.5)
#         h15 = table.get_highlighted_cell((9,4), color=PINK, fill_opacity=0.5)
#         h16 = table.get_highlighted_cell((3,4), color=PINK, fill_opacity=0.5)
#         h17 = table.get_highlighted_cell((4,4), color=PINK, fill_opacity=0.5)
#         h18 = table.get_highlighted_cell((5,4), color=PINK, fill_opacity=0.5)
#         h19 = table.get_highlighted_cell((6,4), color=PINK, fill_opacity=0.5)
#         h20 = table.get_highlighted_cell((7,4), color=PINK, fill_opacity=0.5)
#         h21 = table.get_highlighted_cell((8,4), color=PINK, fill_opacity=0.5)
#         h22 = table.get_highlighted_cell((9,5), color=PINK, fill_opacity=0.5)
#         h23 = table.get_highlighted_cell((3,5), color=PINK, fill_opacity=0.5)
#         h24 = table.get_highlighted_cell((4,5), color=PINK, fill_opacity=0.5)
#         h25 = table.get_highlighted_cell((5,5), color=PINK, fill_opacity=0.5)
#         h26 = table.get_highlighted_cell((6,5), color=PINK, fill_opacity=0.5)
#         h27 = table.get_highlighted_cell((7,5), color=PINK, fill_opacity=0.5)
#         h28 = table.get_highlighted_cell((8,5), color=PINK, fill_opacity=0.5)

#         self.play(Transform(txt, Tex("Bootstrapping includes row as well as feature sampling", color=WHITE).shift(UP*2, LEFT*1.75).scale(0.75)))

#         self.next_slide()

#         d1 = LabeledDot(MathTex(r"D_1", color=BLACK), color=GOLD, radius=0.7).shift(UP*0.5)
#         d2 = LabeledDot(MathTex(r"D_2", color=BLACK), color=GOLD, radius=0.7).shift(UP*0.5, RIGHT*2)
#         d3 = LabeledDot(MathTex(r"D_3", color=BLACK), color=GOLD, radius=0.7).shift(UP*0.5, RIGHT*4)
#         d4 = LabeledDot(MathTex(r"D_4", color=BLACK), color=GOLD, radius=0.7).shift(UP*0.5, RIGHT*6)
#         dt = Tex("Decision Trees", color=WHITE).shift(RIGHT*3, UP*1.5).scale(0.75)

#         r1 = Tex("R2,R2,R4,R5").next_to(d1, DOWN*0.05).scale(0.5)
#         r2 = Tex("R1,R3,R6,R7").next_to(d2, DOWN*0.05).scale(0.5)
#         r3 = Tex("R1,R1,R4,R6").next_to(d3, DOWN*0.05).scale(0.5)
#         r4 = Tex("R2,R5,R7,R7").next_to(d4, DOWN*0.05).scale(0.5)

#         c1 = Tex("C2,C3,C4").next_to(d1, UP*0.05).scale(0.5)
#         c2 = Tex("C1,C3,C4").next_to(d2, UP*0.05).scale(0.5) 
#         c3 = Tex("C1,C2,C4").next_to(d3, UP*0.05).scale(0.5)
#         c4 = Tex("C1,C2,C3").next_to(d4, UP*0.05).scale(0.5)

#         self.play(Write(dt), FadeIn(d1, d2, d3, d4), Transform(txt, Tex("The number of rows and columns that are sampled must be constant", color=WHITE).shift(UP*2).scale(0.75))) 

#         self.next_slide()


#         a1 = Arrow(start=LEFT, end=RIGHT, color=WHITE).shift(LEFT*6.8, DOWN*0.1).scale(0.25)
#         a2 = Arrow(start=LEFT, end=RIGHT, color=WHITE).shift(LEFT*6.8, DOWN*0.55).scale(0.25)
#         a3 = Arrow(start=LEFT, end=RIGHT, color=WHITE).shift(LEFT*6.8, DOWN*1.0).scale(0.25)
#         a4 = Arrow(start=LEFT, end=RIGHT, color=WHITE).shift(LEFT*6.8, DOWN*1.45).scale(0.25)
#         a5 = Arrow(start=LEFT, end=RIGHT, color=WHITE).shift(LEFT*6.8, DOWN*1.9).scale(0.25)
#         a6 = Arrow(start=LEFT, end=RIGHT, color=WHITE).shift(LEFT*6.8, DOWN*2.35).scale(0.25)
#         a7 = Arrow(start=LEFT, end=RIGHT, color=WHITE).shift(LEFT*6.8, DOWN*2.8).scale(0.25)


#         a8 = Arrow(start=UP, end=DOWN, color=WHITE).shift(UP*1.2, LEFT*4.8).scale(0.25)
#         a9 = Arrow(start=UP, end=DOWN, color=WHITE).shift(UP*1.2, LEFT*3.9).scale(0.25)
#         a10 = Arrow(start=UP, end=DOWN, color=WHITE).shift(UP*1.2, LEFT*2.9).scale(0.25)
#         a11 = Arrow(start=UP, end=DOWN, color=WHITE).shift(UP*1.2, LEFT*1.9).scale(0.25)

#         self.play(FadeOut(dt), FadeIn(r1, c1, a2, a4, a5, a9, a10, a11), FadeIn(h10, h17, h24, h13, h20, h27, h12, h19, h26))

#         self.next_slide()

#         self.play(FadeOut(h10, h17, h24, h13, h20, h27, h12, h19, h26, a2, a4, a5, a9, a10, a11))

#         self.next_slide()

#         self.play(FadeIn(h1, h16, h23, h3, h18, h25, h6, h21, h28, h7, h15, h22), FadeIn(r2, c2, a1, a3, a6, a7, a8, a10, a11))

#         self.next_slide()

#         self.play(FadeOut(h1, h16, h23, h3, h18, h25, h6, h21, h28, h7, h15, h22, a1, a3, a6, a7, a8, a10, a11))

#         self.next_slide()

#         self.play(FadeIn(h1, h9, h23, h4, h12, h26, h6, h14, h28), FadeIn(r3, c3, a1, a4, a6, a8, a9, a11))

#         self.next_slide()

#         self.play(FadeOut(h1, h9, h23, h4, h12, h26, h6, h14, h28, a1, a4, a6, a8, a9, a11))

#         self.next_slide()

#         self.play(FadeIn(h2, h10, h17, h5, h13, h20, h7, h8, h15), FadeIn(r4, c4, a2, a8, a5, a7, a9, a10))

#         self.next_slide()

#         self.play(FadeOut(h2, h10, h17, h5, h13, h20, h7, h8, h15, a2, a8, a5, a7, a9, a10))

#         self.next_slide()

#         p1 = Tex("Yes").shift(DOWN*2.5)
#         p2 = Tex("No").shift(DOWN*2.5, RIGHT*2)
#         p3 = Tex("No").shift(DOWN*2.5, RIGHT*4)
#         p4 = Tex("No").shift(DOWN*2.5, RIGHT*6)

#         arr1 = Arrow(start=r1.get_bottom(), end=p1.get_top(), color=WHITE)
#         arr2 = Arrow(start=r2.get_bottom(), end=p2.get_top(), color=WHITE)
#         arr3 = Arrow(start=r3.get_bottom(), end=p3.get_top(), color=WHITE)
#         arr4 = Arrow(start=r4.get_bottom(), end=p4.get_top(), color=WHITE)

#         self.play(GrowArrow(arr1), Write(p1))
#         self.play(GrowArrow(arr2), Write(p2))
#         self.play(GrowArrow(arr3), Write(p3))
#         self.play(GrowArrow(arr4), Write(p4))

#         self.next_slide()

#         prediction = LabeledDot(Tex("No", color=WHITE), color=GREEN).scale(1.5).shift(RIGHT*5)
#         dbpred = Tex("Diabetes Prediction").scale(1.5).next_to(prediction, LEFT*8)
#         aa = Arrow(start=dbpred.get_right(), end=prediction.get_left(), color=WHITE)

#         self.play(FadeOut(arr1, arr2, arr3, arr4, r1, r2, r3, r4, c1, c2, c3, c4, d1, d2, d3, d4, table, txt, dot), FadeIn(dbpred), GrowArrow(aa), Transform(p1, prediction), Transform(p2, prediction), Transform(p3, prediction), Transform(p4, prediction), GrowFromCenter(prediction))
        
#         self.next_slide()

#         self.play(FadeOut(p1,p2,p3,p4,prediction, dbpred, aa, heading))

# class F5(MovingCameraScene, Slide):
#     def construct(self):
#         heading = Tex("Boosting", color=WHITE).shift(UP*3).scale(1.5)
#         # Create a regular hexagon in the middle of the screen using only lines and not using Polygon

#         l1 = Line(start=RIGHT*1, end=RIGHT*0.5+UP*0.866, color=RED)
#         l2 = Line(start=RIGHT*0.5+UP*0.866, end=LEFT*0.5+UP*0.866, color=RED)
#         l3 = Line(start=LEFT*0.5+UP*0.866, end=LEFT*1, color=RED)
#         l4 = Line(start=LEFT*1, end=LEFT*0.5+DOWN*0.866, color=RED)
#         l5 = Line(start=LEFT*0.5+DOWN*0.866, end=RIGHT*0.5+DOWN*0.866, color=RED)
#         l6 = Line(start=RIGHT*0.5+DOWN*0.866, end=RIGHT*1, color=RED)


#         arc1 = Arc(radius=1, start_angle=PI, angle=-PI,color= YELLOW) 
#         circ1 = Circle(radius=1, color=YELLOW)

#         self.play(Write(heading), FadeIn(l1, l2, l3, l4, l5, l6), Create(circ1))
#         self.play(Uncreate(circ1))
        
#         self.next_slide()

#         self.play(Transform(l1, arc1), Transform(l2, arc1), Transform(l3, arc1))

#         self.next_slide()
#         g1 = VGroup(l4,l5,l6)

#         self.play(self.camera.frame.animate.set_width(2.5).move_to(g1))

#         self.next_slide()

#         arc2 = Arc(radius=1, start_angle=PI, angle=PI/3,color= YELLOW)
#         g2 = VGroup(l5,l6)

#         self.play(Transform(l4, arc2))

#         self.next_slide()

#         self.play(self.camera.frame.animate.set_width(2).move_to(g2))

#         self.next_slide()

#         arc3 = Arc(radius=1, start_angle=(4*PI)/3, angle=PI/3,color= YELLOW)

#         self.play(Transform(l5, arc3))

#         self.next_slide()
        
#         g3 = VGroup(l6)

#         self.play(self.camera.frame.animate.set_width(2).move_to(g3))

#         self.next_slide()

#         arc4 = Arc(radius=1, start_angle=(5*PI)/3, angle=PI/6,color= YELLOW)

#         self.play(Transform(l6, arc4))

#         self.next_slide()

#         self.play(self.camera.frame.animate.set_width(15).move_to(ORIGIN))

#         self.next_slide()

#         self.play(FadeOut(l1, l2, l3, l4, l5, l6, arc1, arc2, arc3, arc4))

#         txt = Tex("Adaptive Boosting", color=WHITE).shift(UP*2).scale(0.75)
#         imgg = ImageMobject("AA.png").shift(DOWN*1)

#         self.play(Transform(heading, Tex("AdaBoost", color=WHITE).shift(UP*3).scale(1.5)), FadeIn(imgg), Write(txt))

#         self.next_slide()

#         self.play(Transform(txt, Tex("Combines weak learners of low variance to produce a strong learner of high variance", color=WHITE).shift(UP*2).scale(0.5)))

#         self.next_slide()

#         self.play(Transform(txt, Tex("A model(due to underfitting or overfitting) which has poor accuracy", color=WHITE).shift(UP*2).scale(0.5)), Transform(heading, Tex("Weak Learner", color=WHITE).shift(UP*3).scale(1.5)), FadeOut(imgg))

#         self.next_slide()

#         stump = Tex("Stumps", color=WHITE).shift(UP*1, LEFT*4).scale(0.75)
#         s1 = SurroundingRectangle(stump, color=PURPLE, fill_color=BLUE, fill_opacity=0.5)
#         linm = Tex("Linear Models", color=WHITE).shift(UP*1).scale(0.75)
#         s2 = SurroundingRectangle(linm, color=PURPLE, fill_color=BLUE, fill_opacity=0.5)
#         knn = Tex("KNNs", color=WHITE).shift(UP*1, RIGHT*4).scale(0.75)
#         s3 = SurroundingRectangle(knn, color=PURPLE, fill_color=BLUE, fill_opacity=0.5)

#         decnod = Tex("Decision Node", color=WHITE).shift(LEFT*4).scale(0.5)
#         srect1 = SurroundingRectangle(decnod, color=RED)
#         l1 = Tex("Leaf Node", color=WHITE).shift(DOWN*2, LEFT*5).scale(0.5)
#         srect2 = SurroundingRectangle(l1, color=GREEN, corner_radius=0.2)
#         l2 = Tex("Leaf Node", color=WHITE).shift(DOWN*2, LEFT*3).scale(0.5)
#         srect3 = SurroundingRectangle(l2, color=GREEN, corner_radius=0.2)
#         a1 = Arrow(start=decnod.get_bottom(), end=l1.get_top(), color=WHITE)
#         a2 = Arrow(start=decnod.get_bottom(), end=l2.get_top(), color=WHITE)

#         st = VGroup(decnod, l1, l2, a1, a2, srect1, srect2, srect3, stump, s1)

#         self.play(Write(st))

#         axes1 = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=3, y_length=3, axis_config={"color": WHITE}).add_coordinates().shift(DOWN*1)
#         line = Line(start=axes1.c2p(1, 0), end=axes1.c2p(4, 4), color=BLUE)

#         lg = VGroup(axes1, line, linm, s2)

#         self.play(Create(lg))

#         axes2 = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=3, y_length=3, axis_config={"color": WHITE}).add_coordinates().shift(RIGHT*4, DOWN*1)
#         # Plot 5 points in the range x=0 to x=2.5 and y=0 to y=2.5

#         dots = VGroup()
#         for i in range(5):
#             dots.add(Dot(point=axes2.c2p(np.random.uniform(0, 2.5), np.random.uniform(0, 2.5)), color=RED))

#         # Plot 5 points in the range x=2.5 to x=5 and y=2.5 to y=5

#         for i in range(5):
#             dots.add(Dot(point=axes2.c2p(np.random.uniform(2.5, 5), np.random.uniform(2.5, 5)), color=GREEN))

#         dotplot = Dot(point=axes2.c2p(2.5, 2.5), color=PINK)
#         dashedcirc = DashedVMobject(Circle(stroke_color=PINK, radius=1).move_to(dotplot), num_dashes=20) 

#         knng = VGroup(axes2, dots, dotplot, knn, s3, dashedcirc)

#         self.play(Create(knng))
        
#         self.next_slide()

#         self.play(FadeOut(lg, knng, txt, heading), st.animate.move_to(ORIGIN).scale(1.5))

#         self.next_slide()

#         self.play(FadeOut(st))

# class F6(Slide):
#     def construct(self):
#         heading = Tex("AdaBoost", color=WHITE).shift(UP*3).scale(1.5)
#         table = MathTable(
#             [["Gender", "Age", "Weight", "Height", "Diabetes", "Sample Weights"],
#             ["Male", "30", "70", "180", "Yes", "1/7"],
#             ["Female", "35", "60", "170", "Yes", "1/7"],
#             ["Female", "41", "55", "175", "No", "1/7"],
#             ["Male", "25", "80", "185", "Yes", "1/7"],
#             ["Female", "56", "50", "160", "No", "1/7"],
#             ["Male", "58", "75", "190", "No", "1/7"],
#             ["Male", "46", "85", "195", "Yes", "1/7"]],
#             include_outer_lines=True).scale(0.35).to_edge(LEFT, buff=0.5)
#         table.add_highlighted_cell((1,1), color=GREEN)
#         table.add_highlighted_cell((1,2), color=RED)
#         table.add_highlighted_cell((1,3), color=YELLOW)
#         table.add_highlighted_cell((1,4), color=BLUE)
#         table.add_highlighted_cell((1,5), color=PINK)
#         table.add_highlighted_cell((1,6), color=PURPLE)

#         self.play(Write(table), Write(heading))

#         self.next_slide()
#         r1 = SurroundingRectangle(table.get_columns()[0], color=PINK)
#         r2 = SurroundingRectangle(table.get_columns()[1], color=PINK)
#         r3 = SurroundingRectangle(table.get_columns()[2], color=PINK)
#         r4 = SurroundingRectangle(table.get_columns()[3], color=PINK)

#         self.play(Create(r1))
#         self.play(Uncreate(r1))
#         self.play(Create(r2))
#         self.play(Uncreate(r2))
#         self.play(Create(r3))
#         self.play(Uncreate(r3))
#         self.play(Create(r4))
#         self.play(Uncreate(r4))

#         self.next_slide()

#         txt1 = Tex("Feature with Least Gini Impurity").shift(UP*1, RIGHT*4).scale(0.75)
#         txt2 = Tex("Weight").next_to(txt1, DOWN*3).scale(0.75)
#         srect = SurroundingRectangle(txt2, color=WHITE, fill_color=YELLOW, fill_opacity=0.5)
#         ar1 = Arrow(start=txt1.get_bottom(), end=txt2.get_top(), color=WHITE)

#         self.play(Write(txt1), Write(txt2), GrowArrow(ar1), DrawBorderThenFill(srect))

#         self.next_slide()

#         l1 = Tex("Diabetes", color=WHITE).shift(UP*1, RIGHT*5).scale(0.5)
#         cor1 = Tex("3", color=GREEN).shift(UP*0.5, RIGHT*4.5).scale(0.5)
#         wro1 = Tex("1", color=RED).shift(UP*0.5, RIGHT*5.5).scale(0.5)

#         g1 = VGroup(l1, cor1, wro1)
#         srect1 = SurroundingRectangle(g1, color=YELLOW, corner_radius=0.2)

#         l2 = Tex("No Diabetes", color=WHITE).shift(UP*1, RIGHT*3).scale(0.5)
#         cor2 = Tex("2", color=GREEN).shift(UP*0.5, RIGHT*2.5).scale(0.5)
#         wro2 = Tex("1", color=RED).shift(UP*0.5, RIGHT*3.5).scale(0.5)

#         g2 = VGroup(l2, cor2, wro2)
#         srect2 = SurroundingRectangle(g2, color=YELLOW, corner_radius=0.2)

#         self.play(Transform(txt2, MathTex(r"Weight > 69", color=WHITE).shift(UP*2, RIGHT*4).scale(0.75)), FadeOut(txt1, ar1, srect), Create(srect1), Create(srect2), Create(g1), Create(g2))
#         srect = SurroundingRectangle(txt2, color=WHITE, fill_color=YELLOW, fill_opacity=0.5)
#         a1 = Arrow(start=srect.get_bottom(), end=srect1.get_top(), color=WHITE)
#         a2 = Arrow(start=srect.get_bottom(), end=srect2.get_top(), color=WHITE)
#         self.play(DrawBorderThenFill(srect), Create(a1), Create(a2))

#         self.next_slide()

#         r5 = SurroundingRectangle(table.get_rows()[2], color=YELLOW)
#         r6 = SurroundingRectangle(table.get_rows()[6], color=YELLOW)

#         self.play(Create(r5), Create(r6))

#         self.next_slide()

#         txt3 = MathTex(r"\frac{1}{7} + \frac{1}{7}").shift(RIGHT*4).scale(0.75)
#         ar1 = Arrow(start=txt2.get_bottom(), end=txt3.get_top(), color=WHITE)
#         self.play(Uncreate(r5), Uncreate(r6), Transform(txt2, MathTex(r"Total Error", color=WHITE).shift(UP*2, RIGHT*4).scale(0.75)), FadeOut(srect, a1, a2, srect1, srect2, g1, g2), FadeIn(txt3), GrowArrow(ar1))

#         self.next_slide()

#         self.play(Transform(txt3, MathTex(r"0.286", color=WHITE).shift(RIGHT*4).scale(0.75)))

#         self.next_slide()

#         self.play(Transform(txt2, Tex("Amount of Say", color=WHITE).shift(UP*2, RIGHT*4).scale(0.75)), Transform(txt3, MathTex(r"\frac{1}{2}log_{2}\frac{1 - T.E.}{T.E.}", color=WHITE).shift(RIGHT*4).scale(0.75)))
        
#         self.next_slide()

#         self.play(Transform(txt3, MathTex(r"\frac{1}{2}log_{2}(\frac{1 - 0.286}{0.286})", color=WHITE).shift(RIGHT*4).scale(0.75)))

#         self.next_slide()

#         self.play(Transform(txt3, MathTex(r"0.92", color=WHITE).shift(RIGHT*4).scale(0.75)))

#         self.next_slide()

#         head = Tex("Weight Updation", color=WHITE).shift(UP*1, RIGHT*3.5).scale(0.75)
#         corr = Tex("Correctly Predicted", color=GREEN).next_to(head, DOWN*1).scale(0.5)
#         corrform = MathTex(r"New Sample Weight = Old Sample Weight \times e^{-Amount of Say}", color=WHITE).next_to(corr, DOWN*0.5).scale(0.5)
#         incorr = Tex("Incorrectly Predicted", color=RED).next_to(corrform, DOWN*2).scale(0.5)
#         incorrform = MathTex(r"New Sample Weight = Old Sample Weight \times e^{Amount of Say}", color=WHITE).next_to(incorr, DOWN*0.5).scale(0.5)

#         self.play(FadeOut(txt2, txt3, ar1), Write(head), Write(corr), Write(corrform), Write(incorr), Write(incorrform))

#         self.next_slide()

#         self.play(Transform(corrform, MathTex(r"New Sample Weight = 0.286 \times e^{-0.92}", color=WHITE).next_to(corr, DOWN*0.5).scale(0.5)), Transform(incorrform, MathTex(r"New Sample Weight = 0.286 \times e^{0.92}", color=WHITE).next_to(incorr, DOWN*0.5).scale(0.5)))

#         self.next_slide()

#         self.play(Transform(corrform, MathTex(r"New Sample Weight = 0.14", color=WHITE).next_to(corr, DOWN*0.5).scale(0.5)), Transform(incorrform, MathTex(r"New Sample Weight = 0.72", color=WHITE).next_to(incorr, DOWN*0.5).scale(0.5)))

#         def replace_table_element(row, col, new_text, table:Table, scale=0.25, color=WHITE):
#             elem = table.get_entries_without_labels((row,col))
#             new_element = Text(new_text, color=color).scale(scale)
#             new_element.move_to(elem)
#             return Transform(elem, new_element)
        
#         self.next_slide()

#         self.play(replace_table_element(2, 6, "0.14", table), replace_table_element(3, 6, "0.72", table), replace_table_element(4, 6, "0.14", table), replace_table_element(5, 6, "0.14", table), replace_table_element(6, 6, "0.14", table), replace_table_element(7, 6, "0.72", table), replace_table_element(8, 6, "0.14", table))

#         self.next_slide()

#         self.play(Transform(head, Tex("Weight Normalization", color=WHITE).shift(UP*1, RIGHT*3.5).scale(0.75)), Transform(corrform, MathTex(r"New Sample Weight = \frac{Old Sample Weight}{Total Weight}", color=WHITE).next_to(corr, DOWN*0.5).scale(0.5)), Transform(incorrform, MathTex(r"New Sample Weight = \frac{Old Sample Weight}{Total Weight}", color=WHITE).next_to(incorr, DOWN*0.5).scale(0.5)))

#         self.next_slide()

#         self.play(Transform(corrform, MathTex(r"New Sample Weight = \frac{0.14}{1.86}", color=WHITE).next_to(corr, DOWN*0.5).scale(0.5)), Transform(incorrform, MathTex(r"New Sample Weight = \frac{0.72}{1.86}", color=WHITE).next_to(incorr, DOWN*0.5).scale(0.5)))

#         self.next_slide()

#         self.play(Transform(corrform, MathTex(r"New Sample Weight = 0.075", color=WHITE).next_to(corr, DOWN*0.5).scale(0.5)), Transform(incorrform, MathTex(r"New Sample Weight = 0.387", color=WHITE).next_to(incorr, DOWN*0.5).scale(0.5)))

#         self.next_slide()

#         self.play(replace_table_element(2, 6, "0.075", table), replace_table_element(3, 6, "0.387", table), replace_table_element(4, 6, "0.075", table), replace_table_element(5, 6, "0.075", table), replace_table_element(6, 6, "0.075", table), replace_table_element(7, 6, "0.387", table), replace_table_element(8, 6, "0.075", table))

#         self.next_slide()

#         self.play(Transform(head, Tex("Weighted Gini Impurity", color=WHITE).shift(UP*2, RIGHT*3.5).scale(0.75)), FadeOut(corrform, incorrform, corr), Transform(incorr, MathTex(r"Sample Weight \times Gini Impurity", color=WHITE).next_to(corrform, DOWN*2).scale(0.5)))
#         ar1 = Arrow(start=head.get_bottom(), end=incorr.get_top(), color=WHITE)
#         self.play(GrowArrow(ar1))

#         self.next_slide()

#         self.play(FadeOut(incorr, head, ar1, table))

#         pred = MathTable(
#             [["Gender", "Age", "Weight", "Height", "Diabetes"],
#             ["Male", "36", "78", "170", "?"]],
#             include_outer_lines=True).scale(0.4).to_edge(LEFT, buff=0.5).shift(UP*1.5)
#         pred.add_highlighted_cell((1,1), color=GREEN)
#         pred.add_highlighted_cell((1,2), color=RED)
#         pred.add_highlighted_cell((1,3), color=YELLOW)
#         pred.add_highlighted_cell((1,4), color=BLUE)
#         pred.add_highlighted_cell((1,5), color=PINK)

#         self.play(Write(pred))

#         self.next_slide()

#         s1 = LabeledDot(MathTex(r"S_1", color=BLACK), color=GOLD, radius=0.7).next_to(pred, RIGHT*1.5)
#         s2 = LabeledDot(MathTex(r"S_2", color=BLACK), color=GOLD, radius=0.7).next_to(s1, RIGHT*2)
#         s3 = LabeledDot(MathTex(r"S_3", color=BLACK), color=GOLD, radius=0.7).next_to(s2, RIGHT*2)
#         s4 = LabeledDot(MathTex(r"S_4", color=BLACK), color=GOLD, radius=0.7).next_to(s3, RIGHT*2)

#         arr = Arrow(start=pred.get_right(), end=s1.get_left(), color=WHITE)

#         txt1 = MathTex(r"-0.98", color=RED).next_to(s1, DOWN*5).scale(0.5)
#         txt2 = MathTex(r"0.75", color=GREEN).next_to(s2, DOWN*5).scale(0.5)
#         txt3 = MathTex(r"0.16", color=GREEN).next_to(s3, DOWN*5).scale(0.5)
#         txt4 = MathTex(r"0.13", color=GREEN).next_to(s4, DOWN*5).scale(0.5)

#         a1 = Arrow(start=s1.get_bottom(), end=txt1.get_top(), color=WHITE)
#         a2 = Arrow(start=s2.get_bottom(), end=txt2.get_top(), color=WHITE)
#         a3 = Arrow(start=s3.get_bottom(), end=txt3.get_top(), color=WHITE)
#         a4 = Arrow(start=s4.get_bottom(), end=txt4.get_top(), color=WHITE)

#         plus1 = MathTex(r"+", color=WHITE).next_to(txt1, RIGHT*2)
#         plus2 = MathTex(r"+", color=WHITE).next_to(txt2, RIGHT*2)
#         plus3 = MathTex(r"+", color=WHITE).next_to(txt3, RIGHT*2)

#         ans = MathTex(r"0.06", color=GREEN).next_to(plus2, ORIGIN)

#         self.play(GrowFromCenter(s1), GrowFromCenter(s2), GrowFromCenter(s3), GrowFromCenter(s4), GrowArrow(arr))

#         self.next_slide()

#         self.play(Write(txt1), Write(txt2), Write(txt3), Write(txt4), GrowArrow(a1), GrowArrow(a2), GrowArrow(a3), GrowArrow(a4))

#         self.next_slide()

#         pos = Tex("Positive Sign = 'Yes' Prediction", color=WHITE).next_to(pred, DOWN*2).scale(0.75)
#         neg = Tex("Negative Sign = 'No' Prediction", color=WHITE).next_to(pos, DOWN*4).scale(0.75)

#         self.play(Write(pos), Write(neg))

#         self.next_slide()

#         self.play(Write(plus1), Write(plus2), Write(plus3))

#         self.next_slide()

#         g = VGroup(txt1, txt2, txt3, txt4, plus1, plus2, plus3)
#         self.play(Transform(g, ans))

#         self.next_slide()

#         elem = pred.get_entries_without_labels((2,5))
#         new_element = Text("Yes", color=BLUE).scale(0.5)
#         new_element.move_to(elem) 

#         self.play(Transform(elem,new_element))

#         self.next_slide()

#         self.play(FadeOut(pred, s1, s2, s3, s4, arr, txt1, txt2, txt3, txt4, a1, a2, a3, a4, plus1, plus2, plus3, ans, pos, neg, elem, new_element, heading))


# class M(Slide):
#     def construct(self):
#         heading = Tex("XGBoost", color=WHITE).shift(UP*3).scale(1.5)

#         self.play(Write(heading))

#         self.next_slide()

#         plane = NumberPlane(x_range=(-3,3,1), x_length=12, y_range=(-1,10,1), y_length=6, color=WHITE, background_line_style={
#                 "stroke_color": WHITE,
#                 "stroke_width": 1,
#                 "stroke_opacity": 0.2
#             }).add_coordinates()
#         graph = plane.plot(lambda x: x**2, x_range=[-3, 3], color=BLUE)
        

#         self.play(Write(plane), Write(graph), Transform(heading, Tex("Gradient Boosting", color=WHITE).shift(UP*3.5).scale(1.5)))

#         self.next_slide()

#         dots = VGroup()
        
#         for i in range(8,-1, -1):
#             x = i/3 if i%2==0 else -i/3
#             dots.add(Dot(color=PINK).move_to(plane.c2p(x, (x)**2)))

#         # Make a curve joining all of these dots with only straight lines
#         straight_curve = VGroup()
#         for i in range(0,8):
#             ll = Line(dots[i].get_center(), dots[i+1].get_center(), color=RED)
#             self.play(Create(ll))
#             straight_curve.add(ll)

#         self.play(Create(dots))

#         self.next_slide()

#         self.play(FadeOut(dots, straight_curve, graph, plane))


# class N(Slide):
#     def construct(self):
#         data = [["Gender", "Age", "House Size", "Income"],
#             ["Male", "30", "3000", "4"],
#             ["Female", "35", "5000", "3"],
#             ["Female", "41", "2000", "1"],
#             ["Male", "25", "1000", "0.5"],
#             ["Female", "56", "2500", "3.5"],
#             ["Male", "58", "6000", "7.5"],
#             ["Male", "46", "2400", "1.5"]]
#         table = Table(data,include_outer_lines=True).scale(0.35).to_edge(LEFT, buff=0.5)
#         table.add_highlighted_cell((1,1), color=GREEN)
#         table.add_highlighted_cell((1,2), color=GREEN)
#         table.add_highlighted_cell((1,3), color=GREEN)
#         table.add_highlighted_cell((1,4), color=PINK)

#         self.play(Write(table))

#         self.next_slide()

#         def replace_table_element(row, col, new_text, table:Table, scale=0.25, color=WHITE):
#             elem = table.get_entries_without_labels((row,col))
#             new_element = Text(new_text, color=color).scale(scale)
#             new_element.move_to(elem)
#             return Transform(elem, new_element)

#         data = [["Gender", "Age", "House Size", "Income", "Prediction"],
#             ["Male", "30", "3000", "4", "3"],
#             ["Female", "35", "5000", "3", "3"],
#             ["Female", "41", "2000", "1", "3"],
#             ["Male", "25", "1000", "0.5", "3"],
#             ["Female", "56", "2500", "3.5", "3"],
#             ["Male", "58", "6000", "7.5", "3"],
#             ["Male", "46", "2400", "1.5", "3"]]
    
#         table2 = Table(data,include_outer_lines=True).scale(0.35).to_edge(LEFT, buff=0.5)
#         table2.add_highlighted_cell((1,1), color=GREEN)
#         table2.add_highlighted_cell((1,2), color=GREEN)
#         table2.add_highlighted_cell((1,3), color=GREEN)
#         table2.add_highlighted_cell((1,4), color=PINK)
#         table2.add_highlighted_cell((1,5), color=BLUE)

#         txt = Tex("Income Average", color=WHITE).shift(UP*1.5, RIGHT*4).scale(0.75)
#         srect = always_redraw(lambda : Rectangle(height=txt.get_height()+0.5, width=txt.get_width()+0.5, color=RED, fill_color=GREEN, fill_opacity=0.5).move_to(txt))
#         form = MathTex(r"\frac{4 + 3 + 1 + 0.5 + 3.5 + 7.5 + 1.5}{7}").scale(0.75).next_to(txt, DOWN*5)
#         ar1 = Arrow(txt.get_bottom(), form.get_top(), color=WHITE)

#         self.play(Write(txt), Write(form), GrowArrow(ar1), DrawBorderThenFill(srect))

#         self.next_slide()

#         self.play(Transform(form, MathTex(r"3").scale(0.75).next_to(txt, DOWN*5)))
        
#         self.next_slide()

#         self.play(Transform(table, table2))

#         self.next_slide()

#         self.play(Transform(form, Tex("(Actual Income - Prediction)", color=WHITE).scale(0.75).next_to(txt, DOWN*5)), Transform(txt, Tex("Residuals", color=WHITE).shift(UP*2, RIGHT*4).scale(0.75)))

#         self.next_slide()

#         data = [["Gender", "Age", "House Size", "Income", "Prediction", "Residuals"],
#             ["Male", "30", "3000", "4", "3", "1"],
#             ["Female", "35", "5000", "3", "3", "0"],
#             ["Female", "41", "2000", "1", "3", "-2"],
#             ["Male", "25", "1000", "0.5", "3", "-2.5"],
#             ["Female", "56", "2500", "3.5", "3", "0.5"],
#             ["Male", "58", "6000", "7.5", "3", "4.5"],
#             ["Male", "46", "2400", "1.5", "3", "-1.5"]]

#         table2 = Table(data,include_outer_lines=True).scale(0.35).to_edge(LEFT, buff=0.5)
#         table2.add_highlighted_cell((1,1), color=GREEN)
#         table2.add_highlighted_cell((1,2), color=GREEN)
#         table2.add_highlighted_cell((1,3), color=GREEN)
#         table2.add_highlighted_cell((1,4), color=PINK)
#         table2.add_highlighted_cell((1,5), color=BLUE)
#         table2.add_highlighted_cell((1,6), color=RED)

#         self.play(Transform(table, table2))

#         self.next_slide()

#         trainer_rect = SurroundingRectangle(table2.get_columns()[:3], color=PINK)
#         res_rect = SurroundingRectangle(table2.get_columns()[5], color=PINK)

#         self.play(Create(trainer_rect), Create(res_rect))

#         self.next_slide()

#         self.play(Uncreate(trainer_rect), Uncreate(res_rect))

#         self.next_slide()

#         self.play(table.animate.scale(0.8).to_edge(LEFT, buff=0.5), FadeOut(form, txt, ar1, srect))

#         dec1 = MathTex("House Size > 2000", color=WHITE).shift(UP*1.5, RIGHT*3).scale(0.4)
#         drect1 = SurroundingRectangle(dec1, color=RED, fill_color=GREEN, fill_opacity=0.5)

#         dec2 = MathTex("Age<40", color=WHITE).shift(UP*0.5+RIGHT*1.5).scale(0.4)
#         drect2 = SurroundingRectangle(dec2, color=RED, fill_color=GREEN, fill_opacity=0.5)

#         dec3 = MathTex("Gender=M", color=WHITE).next_to(dec2, RIGHT*4).scale(0.4)
#         drect3 = SurroundingRectangle(dec3, color=RED, fill_color=GREEN, fill_opacity=0.5)

#         leaf1 = Tex("1, 0", color=WHITE).next_to(dec2, DOWN*2+LEFT*0.5).scale(0.4)
#         lrect1 = always_redraw(lambda : RoundedRectangle(height=leaf1.get_height()+0.25, width=leaf1.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf1))

#         leaf2 = Tex("0.5, 4.5, -1.5", color=WHITE).next_to(leaf1, RIGHT*1.5).scale(0.4)
#         lrect2 = always_redraw(lambda : RoundedRectangle(height=leaf2.get_height()+0.25, width=leaf2.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf2))

#         leaf3 = Tex("-2.5", color=WHITE).next_to(leaf2, RIGHT*1).scale(0.4)
#         lrect3 = always_redraw(lambda : RoundedRectangle(height=leaf3.get_height()+0.25, width=leaf3.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf3))

#         leaf4 = Tex("-2", color=WHITE).next_to(leaf3, RIGHT*6).scale(0.4)
#         lrect4 = always_redraw(lambda : RoundedRectangle(height=leaf4.get_height()+0.25, width=leaf4.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf4))

#         a1 = always_redraw(lambda : Arrow(drect1.get_bottom(), drect2.get_top(), color=WHITE))
#         a2 = always_redraw(lambda : Arrow(drect2.get_bottom(), lrect1.get_top(), color=WHITE))
#         a3 = always_redraw(lambda : Arrow(drect2.get_bottom(), lrect2.get_top(), color=WHITE))
#         a4 = always_redraw(lambda : Arrow(drect3.get_bottom(), lrect3.get_top(), color=WHITE))
#         a5 = always_redraw(lambda : Arrow(drect3.get_bottom(), lrect4.get_top(), color=WHITE))
#         a6 = always_redraw(lambda : Arrow(drect1.get_bottom(), drect3.get_top(), color=WHITE))

#         g = VGroup(dec1, dec2, dec3, leaf1, leaf2, leaf3, leaf4, drect1, drect2, drect3, lrect1, lrect2, lrect3, lrect4, a1, a2, a3, a4, a5, a6)
#         self.play(Write(g))

#         self.next_slide()

#         txt = MathTex(r"Learning Rate(\alpha) = 0.1", color=WHITE).shift(DOWN*3, LEFT*3.5).scale(0.75)
#         trect = always_redraw(lambda : Rectangle(height=txt.get_height()+0.25, width=txt.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5).move_to(txt))

#         self.play(Write(txt), DrawBorderThenFill(trect))

#         self.next_slide()

#         self.play(Transform(leaf1, Tex("0.5", color=WHITE).next_to(dec2, DOWN*2+LEFT*0.5).scale(0.4)))
#         self.play(Transform(leaf2, Tex("1.17", color=WHITE).next_to(leaf1, RIGHT*4).scale(0.4)))
#         self.play(Transform(leaf3, Tex("-2.5", color=WHITE).next_to(leaf2, RIGHT*2).scale(0.4)))

#         self.next_slide()

#         newt = MathTex(r"New Prediction = Old Prediction + (\alpha \times Predicted Residual) ").shift(DOWN*3, RIGHT*3.5).scale(0.4)

#         self.play(Write(newt))

#         self.next_slide()

#         h1 = SurroundingRectangle(table.get_rows()[1], color=PINK)
#         h3 = SurroundingRectangle(table.get_rows()[3], color=PINK)

#         l1 = SurroundingRectangle(leaf1, color=PINK)
#         l2 = SurroundingRectangle(leaf2, color=PINK)
#         l3 = SurroundingRectangle(leaf3, color=PINK)
#         l4 = SurroundingRectangle(leaf4, color=PINK)

#         self.play(Create(h1))
#         self.play(Uncreate(h1))

#         self.next_slide()

#         self.play(Create(l1))
#         self.play(Uncreate(l1))

#         self.next_slide()

#         self.play(Transform(newt, MathTex(r"New Prediction = 3 + (0.1 \times (0.5))", color=WHITE).shift(DOWN*3, RIGHT*3.5).scale(0.75)))

#         self.next_slide()

#         self.play(Transform(newt, MathTex(r"New Prediction = 3.05", color=WHITE).shift(DOWN*3, RIGHT*3.5).scale(0.75)))

#         self.next_slide()
        
#         self.play(replace_table_element(2, 3, "3.05", table))

#         self.next_slide()

#         self.play(Create(h3))
#         self.play(Uncreate(h3))

#         self.next_slide()

#         self.play(Create(l4))
#         self.play(Uncreate(l4))

#         self.next_slide()

#         self.play(Transform(newt, MathTex(r"New Prediction = 3 + (0.1 \times (-2))", color=WHITE).shift(DOWN*3, RIGHT*3.5).scale(0.75)))

#         self.next_slide()

#         self.play(Transform(newt, MathTex(r"New Prediction = 2.8", color=WHITE).shift(DOWN*3, RIGHT*3.5).scale(0.75)))

#         self.next_slide()
        
#         self.play(replace_table_element(4, 3, "2.8", table))

#         self.next_slide()

#         self.play(replace_table_element(3,3,"3.05",table), replace_table_element(5,3,"2.75",table), replace_table_element(6,3,"3.117",table), replace_table_element(7,3,"3.117",table), replace_table_element(8,3,"3.117",table) )

#         self.next_slide()

#         self.play(Transform(txt, Tex("Trees have fixed number of leaves(8 to 32)").scale(0.5).shift(DOWN*3, LEFT*3.5)))

#         self.play(replace_table_element(2,4,"0.95", table), replace_table_element(3,4,"0.25",table), replace_table_element(4,4,"-1.8",table), replace_table_element(5,4,"-2.25",table), replace_table_element(6,4,"0.383",table), replace_table_element(7,4,"4.383",table), replace_table_element(8,4,"-1.617",table))

#         self.next_slide()
#         self.play(FadeOut(table, txt, trect, g, newt))

# class O(Slide):
#     def construct(self):
#         heading = Tex("Gradient Boosting", color=WHITE).shift(UP*3).scale(1.5)

#         pred = MathTable(
#             [["Gender", "Age", "House Size", "Income", "Prediction"],
#             ["Male", "36", "2500", "2.5", "?"]],
#             include_outer_lines=True).scale(0.4).to_edge(LEFT, buff=0.5).shift(UP*1.5)
#         pred.add_highlighted_cell((1,1), color=GREEN)
#         pred.add_highlighted_cell((1,2), color=GREEN)
#         pred.add_highlighted_cell((1,3), color=GREEN)
#         pred.add_highlighted_cell((1,4), color=PINK)
#         pred.add_highlighted_cell((1,5), color=RED)

#         self.play(Write(pred))

#         self.next_slide()

#         s1 = LabeledDot(MathTex(r"D_1", color=BLACK), color=GOLD, radius=0.7).next_to(pred, RIGHT*1.5)
#         s2 = LabeledDot(MathTex(r"D_2", color=BLACK), color=GOLD, radius=0.7).next_to(s1, RIGHT*2)
#         s3 = LabeledDot(MathTex(r"D_3", color=BLACK), color=GOLD, radius=0.7).next_to(s2, RIGHT*2)
#         s4 = LabeledDot(MathTex(r"D_4", color=BLACK), color=GOLD, radius=0.7).next_to(s3, RIGHT*2)

#         txt1 = MathTex(r"\alpha \times (-5.0)", color=RED).next_to(s1, DOWN*5).scale(0.5)
#         txt0 = MathTex(r"3", color=WHITE).next_to(txt1, LEFT*3).scale(0.5)
#         txt2 = MathTex(r"\alpha \times (3.5)", color=GREEN).next_to(s2, DOWN*5).scale(0.5)
#         txt3 = MathTex(r"\alpha \times (1.5)", color=GREEN).next_to(s3, DOWN*5).scale(0.5)
#         txt4 = MathTex(r"\alpha \times -(7.5)", color=RED).next_to(s4, DOWN*5).scale(0.5)

#         a1 = Arrow(start=s1.get_bottom(), end=txt1.get_top(), color=WHITE)
#         a2 = Arrow(start=s2.get_bottom(), end=txt2.get_top(), color=WHITE)
#         a3 = Arrow(start=s3.get_bottom(), end=txt3.get_top(), color=WHITE)
#         a4 = Arrow(start=s4.get_bottom(), end=txt4.get_top(), color=WHITE)

#         plus0 = MathTex(r"+", color=WHITE).next_to(txt0, RIGHT*1)
#         plus1 = MathTex(r"+", color=WHITE).next_to(txt1, RIGHT*1)
#         plus2 = MathTex(r"+", color=WHITE).next_to(txt2, RIGHT*1)
#         plus3 = MathTex(r"+", color=WHITE).next_to(txt3, RIGHT*1)

#         ans = MathTex(r"2.25", color=GREEN).next_to(plus2, ORIGIN)

#         self.play(GrowFromCenter(s1), GrowFromCenter(s2), GrowFromCenter(s3), GrowFromCenter(s4))

#         self.next_slide()

#         self.play(Write(txt0), Write(txt1), Write(txt2), Write(txt3), Write(txt4), GrowArrow(a1), GrowArrow(a2), GrowArrow(a3), GrowArrow(a4))

#         self.next_slide()

#         self.play(Write(plus0), Write(plus1), Write(plus2), Write(plus3))

#         self.next_slide()

#         g = VGroup(txt0, txt1, txt2, txt3, txt4, plus0, plus1, plus2, plus3)
#         self.play(Transform(g, ans))

#         self.next_slide()

#         elem = pred.get_entries_without_labels((2,5))
#         new_element = Text("2.25", color=GREEN).scale(0.5)
#         new_element.move_to(elem) 

#         self.play(Transform(elem,new_element))

#         self.next_slide()

#         self.play(FadeOut(pred, s1, s2, s3, s4, txt0, txt1, txt2, txt3, txt4, a1, a2, a3, a4, plus0, plus1, plus2, plus3, ans, elem, new_element))
#         self.play(Transform(heading, Tex("XGBoost", color=WHITE).shift(UP*3).scale(1.5)))


# class P(Slide):
#     def construct(self):
#         txt = Tex("Optimized version of Gradient Boosting").shift(LEFT*3.5, UP*2).scale(0.75)

#         self.play(Write(txt))

#         self.next_slide()

#         self.play(Transform(txt, Tex("Efficient, Fast and Scalable").shift(LEFT*3.5, UP*2).scale(0.75)))

#         self.next_slide()

#         self.play(Transform(txt, Tex("Advanced Tree Pruning, Regularization and Parallel Processing").shift(LEFT*2.5, UP*2).scale(0.5)))

#         self.next_slide()

#         text1 = Tex("Tree 1", color=WHITE).shift(UP*1).scale(0.5)
#         rect1= SurroundingRectangle(text1, color= GREEN, fill_opacity = 0.4, fill_color = RED, buff=0.3)
#         l1 = Tex("Leaf", color=WHITE).next_to(rect1, LEFT*1+DOWN*2).scale(0.5)
#         leaf1= SurroundingRectangle(l1, color= YELLOW, fill_opacity = 0.4, fill_color = RED)
#         l2 = Tex("Leaf", color=WHITE).next_to(rect1, RIGHT*1+DOWN*2).scale(0.5)
#         leaf2 = SurroundingRectangle(l2, color= YELLOW, fill_opacity = 0.4, fill_color = RED)
#         a4 = Arrow(start=rect1.get_bottom(), end=leaf1.get_top(), color=WHITE, buff=0.1)
#         a5 = Arrow(start=rect1.get_bottom(), end=leaf2.get_top(), color=WHITE, buff=0.1)

#         g1 = VGroup(text1, rect1, l1, leaf1, l2, leaf2, a4, a5)

#         txt1 = Tex("Random Forests, Gradient Boosting").shift(LEFT*3, DOWN*1.5).scale(0.5)
#         txt2 = Tex("AdaBoost").shift(LEFT*3, DOWN*2).scale(0.5)
#         txt3 = Tex("XGBoost").shift(LEFT*3, DOWN*2.5).scale(0.5)

#         m1 = Tex("Gini Index").shift(RIGHT*3, DOWN*1.5).scale(0.5)
#         mrect1 = SurroundingRectangle(m1, color= GREEN, fill_opacity = 0.4, fill_color = RED)
#         m2 = Tex("Weighted Gini Index").shift(RIGHT*3, DOWN*2).scale(0.5)
#         mrect2 = SurroundingRectangle(m2, color= GREEN, fill_opacity = 0.4, fill_color = RED)
#         m3 = Tex("Similarity Score with Regularization").shift(RIGHT*3, DOWN*2.5).scale(0.5)
#         mrect3 = SurroundingRectangle(m3, color= GREEN, fill_opacity = 0.4, fill_color = RED)

#         a1 = Arrow(start=txt1.get_right(), end=mrect1.get_left(), color=WHITE)
#         a2 = Arrow(start=txt2.get_right(), end=mrect2.get_left(), color=WHITE)
#         a3 = Arrow(start=txt3.get_right(), end=mrect3.get_left(), color=WHITE)

#         g2 = VGroup(txt1, m1, mrect1, a1)
#         g3 = VGroup(txt2, m2, mrect2, a2)
#         g4 = VGroup(txt3, m3, mrect3, a3)

#         self.play(FadeOut(txt), Write(g1))

#         self.next_slide()

#         self.play(Write(g2), Write(g3), Write(g4))

#         self.next_slide()

#         self.play(FadeOut(g1,g2,g3), g4.animate.shift(UP*2.5,LEFT*1).scale(1.5))

#         self.next_slide()

#         self.play(FadeOut(g4))


# class Q(Slide):
#     def construct(self):
#         heading = Tex("XGBoost", color=WHITE).shift(UP*3).scale(1.5)

#         dec1 = MathTex("House Size > 2000", color=WHITE).shift(UP*1.5, LEFT*3).scale(0.6)
#         drect1 = SurroundingRectangle(dec1, color=RED, fill_color=GREEN, fill_opacity=0.5)

#         dec2 = MathTex("Age<40", color=WHITE).shift(UP*0.5+LEFT*4.5).scale(0.6)
#         drect2 = SurroundingRectangle(dec2, color=RED, fill_color=GREEN, fill_opacity=0.5)

#         dec3 = MathTex("Gender=M", color=WHITE).next_to(dec2, RIGHT*4).scale(0.6)
#         drect3 = SurroundingRectangle(dec3, color=RED, fill_color=GREEN, fill_opacity=0.5)

#         leaf1 = Tex("1, 0", color=WHITE).next_to(dec2, DOWN*2+LEFT*0.5).scale(0.6)
#         lrect1 = always_redraw(lambda : RoundedRectangle(height=leaf1.get_height()+0.25, width=leaf1.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf1))

#         leaf2 = Tex("0.5, 4.5, -1.5", color=WHITE).next_to(leaf1, RIGHT*1.5).scale(0.6)
#         lrect2 = always_redraw(lambda : RoundedRectangle(height=leaf2.get_height()+0.25, width=leaf2.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf2))

#         leaf3 = Tex("-2.5", color=WHITE).next_to(leaf2, RIGHT*1).scale(0.6)
#         lrect3 = always_redraw(lambda : RoundedRectangle(height=leaf3.get_height()+0.25, width=leaf3.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf3))

#         leaf4 = Tex("-2", color=WHITE).next_to(leaf3, RIGHT*5).scale(0.6)
#         lrect4 = always_redraw(lambda : RoundedRectangle(height=leaf4.get_height()+0.25, width=leaf4.get_width()+0.25, color=GREEN, fill_color=RED, fill_opacity=0.5, corner_radius=0.2).move_to(leaf4))

#         a1 = always_redraw(lambda : Arrow(drect1.get_bottom(), drect2.get_top(), color=WHITE))
#         a2 = always_redraw(lambda : Arrow(drect2.get_bottom(), lrect1.get_top(), color=WHITE))
#         a3 = always_redraw(lambda : Arrow(drect2.get_bottom(), lrect2.get_top(), color=WHITE))
#         a4 = always_redraw(lambda : Arrow(drect3.get_bottom(), lrect3.get_top(), color=WHITE))
#         a5 = always_redraw(lambda : Arrow(drect3.get_bottom(), lrect4.get_top(), color=WHITE))
#         a6 = always_redraw(lambda : Arrow(drect1.get_bottom(), drect3.get_top(), color=WHITE))

#         g = VGroup(dec1, drect1, dec2, drect2, dec3, drect3, leaf1, lrect1, leaf2, lrect2, leaf3, lrect3, leaf4, lrect4, a1, a2, a3, a4, a5, a6)
#         self.play(Write(g))

#         txt1 = Tex("Similarity Score = ", color=BLUE).shift(UP*0.5, RIGHT*1.5).scale(0.6)
#         form1 = MathTex(r"\frac{Square of Sum of Residuals}{No. of Residuals + }", color=WHITE).shift(UP*0.5,RIGHT*4.75).scale(0.6)
#         lmb = MathTex(r"\lambda", color=RED).shift(RIGHT*6.1, UP*0.3).scale(0.6)
#         g1 = VGroup(txt1, form1, lmb)
#         srect1 = SurroundingRectangle(g1, color=GREEN, fill_opacity=0.4, fill_color=GOLD)

#         txt2 = Tex("Information Gain =", color=BLUE).shift(DOWN*1, RIGHT*2).scale(0.6)
#         form2 = MathTex(r"S_{parent}-S_{right}", color=WHITE).shift(DOWN*1,RIGHT*4.75).scale(0.6)
#         form2alt = MathTex(r"S_{parent}-S_{left}", color=WHITE).shift(DOWN*1,RIGHT*4.75).scale(0.6)
#         g2 = VGroup(txt2, form2)
#         srect2 = SurroundingRectangle(g2, color=GREEN, fill_opacity=0.4, fill_color=GOLD)

#         self.next_slide()

#         self.play(Write(txt1), Write(form1), DrawBorderThenFill(srect1), Write(lmb))

#         self.next_slide()

#         self.play(Write(txt2), Write(form2), DrawBorderThenFill(srect2))

#         self.next_slide()

#         self.play(Transform(form2, form2alt))

#         self.next_slide()

#         txt3 = Tex("Pruning Parameter = ", color=BLUE).shift(DOWN*2, RIGHT*3).scale(0.6)
#         form3 = MathTex(r"\gamma", color=WHITE).shift(DOWN*2,RIGHT*4.75).scale(0.6)
#         g3 = VGroup(txt3, form3)
#         srect3 = SurroundingRectangle(g3, color=GREEN, fill_opacity=0.4, fill_color=GOLD)

#         self.play(Write(txt3), Write(form3), DrawBorderThenFill(srect3))

#         self.next_slide()
        
#         s1 = SurroundingRectangle(leaf2, color=PINK)
#         self.play(Create(s1))
#         self.play(Uncreate(s1))
#         self.play(Transform(form1, MathTex(r"\frac{(0.5 + 4.5 - 1.5)^2}{3 + 1}", color=WHITE).shift(UP*0.5,RIGHT*4.75).scale(0.6)), FadeOut(lmb))

#         self.next_slide()

#         self.play(Transform(form1, MathTex(r"3.38", color=WHITE).shift(UP*0.5,RIGHT*4.75).scale(0.6)))

#         ls2 = Tex("3.06").next_to(leaf2, DOWN).scale(0.6)

#         self.next_slide()

#         self.play(Write(ls2), Transform(form1, MathTex(r"\frac{Square of Sum of Residuals}{No. of Residuals + }", color=WHITE).shift(UP*0.5,RIGHT*4.75).scale(0.6)), FadeIn(lmb))

#         self.next_slide()

#         ds2 = Tex("3.38").next_to(dec2, LEFT).scale(0.6)

#         self.play(Write(ds2))

#         self.next_slide()

#         self.play(Transform(form2, MathTex(r"3.38-3.06", color=WHITE).shift(DOWN*1,RIGHT*4.75).scale(0.6)))

#         self.next_slide()

#         self.play(Transform(form2, MathTex(r"0.32", color=WHITE).shift(DOWN*1,RIGHT*4.75).scale(0.6)))

#         self.next_slide()

#         ig1 = Tex("0.32", color=BLUE).next_to(a3, RIGHT).scale(0.5)
#         self.play(Write(ig1), Transform(form2, MathTex(r"S_{parent}-S_{right}", color=WHITE).shift(DOWN*1,RIGHT*4.75).scale(0.6)))

#         self.next_slide()

#         form4 = MathTex(r"\lambda =", color=RED).next_to(leaf1, DOWN*6).scale(0.6)
#         txt4 = Tex("Regularization Parameter", color=WHITE).next_to(leaf2, DOWN*6).scale(0.6)

#         self.play(Write(form4), Write(txt4))

#         self.next_slide()

#         self.play(Transform(txt4, Tex("Prune when $$\\gamma > I.G.$$").next_to(dec2, DOWN*7).scale(0.6)), FadeOut(form4))

#         self.next_slide()

#         self.play(form2.animate.scale(0.5))
#         self.play(txt2.animate.scale(0.5))

#         self.next_slide()

#         self.play(FadeOut(g, g1, g2, g3, srect1, srect2, srect3, txt4, ig1, ds2, ls2, heading))

        










        





        









        










        


        





        




        