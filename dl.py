from manim import *
from PIL import Image
import math
import numpy as np
from objects.beam import * 



class Detector(Scene):
    def construct(self):        
        
        LeftPart = Tex(r"$\frac{1}{c}\frac{\partial L(\vec{r},\hat{s},t,E)}{\partial t} + \frac{\partial L(\vec{r}, \hat{s},t,E)}{\partial l} =$",font_size=34)
        FirstRightPart = Tex(r"$- \mu_a (\vec{r},E) L(\vec{r}, \hat{s},t,E)$",font_size=34)
        SecondRightPart = Tex(r"$+ \mu_s (\vec{r},E) \int_{4\pi} L(\vec{r}, \hat{s}^\prime, t, E) P(\hat{s}^\prime \cdot \hat{s},E) d\Omega^\prime$",font_size=34)
        ThirdRightPart = Tex(r"$+ q(\vec{r}, \hat{s},t, E)$",font_size=34)
        
        ellipse1 = Ellipse(width=2.0, height=4.0, color=BLUE, fill_opacity=0.2,fill_color=BLUE)
        ellipse2 = Ellipse(width=2.0, height=4.0, color=BLUE)
        ellipse1.shift(LEFT*2)
        ellipse2.shift(RIGHT*2)
        lineTop = Line(start=[-2,2,0],end=[2,2,0],color=BLUE)
        lineBottom = Line(start=[-2,-2,0],end=[2,-2,0],color=BLUE)
        dl = VGroup(ellipse1,ellipse2, lineTop, lineBottom)
        
        dotL = Dot([-2,0,0], color= RED)
        arrowS = Arrow(start=[-2.2,0,0], end=[-1,0,0], color=GREEN)
        L = VGroup(dotL, arrowS)
        
        arrowPass = Arrow(start=[-5,-1.5,0], end=[5,-1.5,0])
        arrowPE = Arrow(start=[-5,-1,0], end=[0.4,-1,0])
        dotPE = Dot([0.2,-1,0], color=RED)
        PE = VGroup(arrowPE,dotPE)
        
        scatteringOutArrow = Arrow(start=[-5,1,0], end=[-0.2,1,0])
        scatteringOutDot = Dot([-0.4,1,0], color=RED, z_index=1)
        scatteringOutArrow2 = Arrow(start=[-0.15,0.8,-0.1],end=[-3,3,0])
        scatteringOut= VGroup(scatteringOutArrow,scatteringOutDot, scatteringOutArrow2)

        scatteringInDot = Dot([-0.1,1.5,0], color=RED, z_index=1)
        scatteringInArrow = Arrow(end=[0.1,1.3,-0.1],start=[-2.2,3,0])
        scatteringInArrow2 = Arrow(start=[-0.3,1.5,0],end=[5,1.5,0])
        scatteringIn = VGroup(scatteringInArrow,scatteringInDot,scatteringInArrow2)

        sourceDot = Dot([0.7,0,0], color=RED, z_index=1)
        sourceArrow = Arrow(end=[5,0,0],start=[0.50,0,0])
        source = VGroup(sourceDot,sourceArrow)

        self.play(Create(dl))
        LeftPart.move_to([-3,3.65,0])
        self.play(Write(LeftPart))
        
        self.wait()
        self.play(Create(L))
        
        self.next_section()
        self.wait()
        self.play(Create(arrowPass))
        
        self.next_section()
        self.wait()
        self.play(Create(PE))
        
        self.next_section()
        self.wait()
        self.play(Create(scatteringOut))
        FirstRightPart.next_to(LeftPart)
        
        self.play(Write(FirstRightPart))
        
        self.next_section()
        self.wait()
        self.play(Create(scatteringIn))
        SecondRightPart.next_to(FirstRightPart,DOWN)
        SecondRightPart.shift(RIGHT*1.4)
        self.play(Write(SecondRightPart))
        
        self.next_section()
        self.wait()
        self.play(Create(source))
        ThirdRightPart.next_to(SecondRightPart,DOWN)
        ThirdRightPart.shift(LEFT*2.05)
        self.play(Write(ThirdRightPart))
        self.wait()
        
        self.next_section()
        LeftPart2 = Tex(r"$\frac{1}{c}\frac{\partial L(\vec{r},\hat{s},t,E)}{\partial t} + \hat{s}\cdot \nabla L(\vec{r},\hat{s},t, E) =$",font_size=34)
        LeftPart2.move_to([-3.5,3.65,0])
        self.play(Transform(LeftPart,LeftPart2,run_time=2))
        self.wait()
 
        self.next_section()
        line = Line(start = [-0.8,2.40,0], end=[1.25,2.40,0], color=RED)
        self.play(Create(line))
        self.wait()
        sourceGroup = VGroup(line,ThirdRightPart,sourceDot,sourceArrow)
        self.play(FadeOut(sourceGroup), run_time=2)
        self.wait()
        
        self.next_section()
        FirstRightPart2 = Tex(r"$ - (\mu_{pe} (\vec{r},E)+\mu_C (\vec{r},E)+\mu_R (\vec{r},E))L(\vec{r}, \hat{s},t, E)$",font_size=34)
        FirstRightPart2.next_to(LeftPart2)
        self.play(Transform(FirstRightPart,FirstRightPart2,run_time=2))
        self.wait()
        
        self.next_section()
        SecondRightPart2 = Tex(r"$ +\int_{4\pi} \mu_C (\vec{r},E^\prime) L(\vec{r}, \hat{s}^\prime, t, E^\prime) P_C(\hat{s}^\prime \cdot \hat{s}, E^\prime) d\Omega^\prime$",font_size=34)
        SecondRightPart2.next_to(FirstRightPart2,DOWN)
        SecondRightPart2.shift(LEFT*0.25)
        self.play(Transform(SecondRightPart,SecondRightPart2,run_time=2))
        
        EqE = Tex(r"$E^\prime = \frac{E}{1-\frac{E}{m_e c^2}(1 - \hat{s}^\prime \cdot \hat{s})}$", font_size=34, color=GREEN)
        EqE.next_to(LeftPart2,DOWN*2)
        EqE.shift(LEFT)
        self.play(Create(EqE))        
        self.wait()
        
        self.next_section()
        ThirdRightPart2 = Tex(r"$ +\mu_R (\vec{r},E) \int_{4\pi} L(\vec{r}, \hat{s}^\prime, t, E) P_R(\hat{s}^\prime \cdot \hat{s}, E) d\Omega^\prime$",font_size=34)
        ThirdRightPart2.next_to(SecondRightPart2,DOWN)
        ThirdRightPart2.shift(LEFT*0.18)
        self.play(Write(ThirdRightPart2,run_time=2))
        self.wait()
        
        self.next_section()
        arrowSteadyState = Line(start=[-6,3.2,0], end = [-4, 4.2, 0], color=RED)
        self.play(Create(arrowSteadyState), run_time=2)
        
        self.next_section()
        groupDl = VGroup(dl, L, PE, scatteringIn, scatteringOut,arrowPass)
        self.play(FadeOut(groupDl))
        self.wait()
        
        Ed = Tex(r"$E_d(\vec{r}) =  \int(\mu_{pe} (\vec{r},E)+\mu_C (\vec{r},E)+\mu_R (\vec{r},E))\int_{4\pi}L(\vec{r}, \hat{s},E)d\Omega dE$", font_size=34)
        Ed2 = Tex(r"$-\int\int_{4\pi}\int_{4\pi} \mu_C (\vec{r},E^\prime) L(\vec{r}, \hat{s}^\prime, E^\prime) P_C(\hat{s}^\prime \cdot \hat{s}, E^\prime) d\Omega^\prime d\Omega dE$", font_size=34)
        Ed3 = Tex(r"$-\int\int_{4\pi}\mu_R (\vec{r},E) \int_{4\pi} L(\vec{r}, \hat{s}^\prime, E) P_R(\hat{s}^\prime \cdot \hat{s}, E) d\Omega^\prime d\Omega dE$", font_size=34)
        Ed.shift(0*LEFT)
        Ed2.next_to(Ed,DOWN)
        Ed2.shift(0.8*RIGHT)
        Ed3.next_to(Ed2,DOWN)
        Ed3.shift(0.1*LEFT)
        
        EdText = VGroup(Ed,Ed2,Ed3)
        self.play(Write(EdText), run_time=2)
        self.wait()
        self.next_section()
        Ed4 = Tex(r"$E_d(\vec{r}) = \int(\mu_{pe} (\vec{r},E)+\mu_C (\vec{r},E)\xi(E))\Phi(\vec{r},E)dE$", font_size=34, color=GREEN)
        Ed4.next_to(Ed3,DOWN*3)
        Ed4.shift(LEFT)
        self.play(Write(Ed4))
        self.wait()
        self.next_section()
        
        

        