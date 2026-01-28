from manim import *
from PIL import Image
import math
import numpy as np
from objects.beam import * 


class Detector(ThreeDScene):
    def construct(self):    
        self.set_camera_orientation(phi=45, theta=-45)
        axes = ThreeDAxes()
        
        L = Tex(r"$L($")
        r = Tex(r"$\vec{r}$", color=BLACK)
        r2 = Tex(r"$\vec{r}$", color=BLUE)
        comma1 = Tex(r"$,$", color=BLACK)
        s = Tex(r"$\hat{s}$", color=BLACK)
        s2 = Tex(r"$\hat{s}$", color=GREEN)
        comma2 = Tex(r"$,$", color=BLACK)
        t = Tex(r"$t$", color=BLACK)
        t2 = Tex(r"$t =$", color=RED)
        comma3 = Tex(r"$,$", color=BLACK)
        e = Tex(r"$E$", color=BLACK)
        e2 = Tex(r"$E =$", color=YELLOW_E)
        closing = Tex(r"$)$")
        
        self.add_fixed_in_frame_mobjects(L,r,s,t,closing,comma1,comma2, comma3, e)
        
        L.move_to(5*LEFT + 3*UP)
        r.next_to(L,RIGHT)
        comma1.next_to(r,RIGHT*0.25)
        comma1.shift(DOWN*0.25)
        s.next_to(comma1,RIGHT)
        s.shift(UP*0.25)
        comma2.next_to(s,RIGHT*0.25)
        comma2.shift(DOWN*0.25)
        t.next_to(comma2,RIGHT)
        t.shift(UP*0.25)
        comma3.next_to(t,RIGHT*0.25)
        comma3.shift(DOWN*0.25)
        e.next_to(comma3,RIGHT)
        e.shift(UP*0.25)
        closing.next_to(e,RIGHT)
        
        dot = Dot3D([3,2,1], color=BLUE)
        vectorR = Vector([3,2,1], color=BLUE)
        
        sourcePos = []
        sourcePos.append(np.array([11,-5,0]))
        sourcePos.append(np.array([-12,5,1]))
        sourcePos.append(np.array([13,10,6]))
        sourcePos.append(np.array([-14,-3,5]))
        sourcePos.append(np.array([10,-6,1]))
        sourcePos.append(np.array([-11,6,2]))
        sourcePos.append(np.array([12,8,2]))
        sourcePos.append(np.array([-13,12,3]))
        sourcePos.append(np.array([14,2,3]))
        sourcePos.append(np.array([-15,5,4]))
        sourcePos.append(np.array([10,7,4]))
        sourcePos.append(np.array([-11,-3,-1]))
        sourcePos.append(np.array([12,0,-2]))
        sourcePos.append(np.array([-13,2,-3]))
        sourcePos.append(np.array([14,9,-3]))
        
        endPos = []
        point = np.array([3,2,1])
        for i in range(15):
            endPos.append(point-(sourcePos[i]-point))
        
        
        vectorS = Arrow3D(start=point, end = [4,2,1], color=GREEN)
        timer = ValueTracker(0)
        timeValue = DecimalNumber(0,num_decimal_places = 3, color=RED,  unit="s", unit_buff_per_font_unit=0.001)
        energyTracker = ValueTracker(10)
        energyValue = Integer(10, color=YELLOW_E,  unit="keV", unit_buff_per_font_unit=0.001)
        
        def timeValueUpdater(mob):
            mob.set_value(timer.get_value())
            self.add_fixed_in_frame_mobjects(mob)
            mob.next_to(t2)
            
        def energyValueUpdater(mob):
            mob.set_value(energyTracker.get_value())
            self.add_fixed_in_frame_mobjects(mob)
            mob.next_to(e2)
        
        timeValue.add_updater(timeValueUpdater)
        energyValue.add_updater(energyValueUpdater)
        
        self.play(Create(axes), run_time=2)
        self.wait()
        self.next_section()
        self.play(Create(dot))
        self.wait()

        
        self.play(Create(vectorR))
        self.add_fixed_in_frame_mobjects(r2)
        r2.next_to(vectorR, UP)
        r2.shift(DOWN*1.6)
        r.set_color(BLUE)
        self.wait()
        self.next_section()
        
        self.wait()
        self.play(AnimationGroup(*[Beam(start=sourcePos[i], end=endPos[i], length=5) for i in range(15)], lag_ratio=0,rate_func=linear, run_time=3))      
        self.wait()
        
        
        self.play(Create(vectorS))
        self.add_fixed_in_frame_mobjects(s2)
        s2.next_to(vectorS, UP)
        s2.shift(DOWN*1.3+0.5*RIGHT)
        comma1.set_color(WHITE)
        s.set_color(GREEN)
        self.wait()
        self.next_section()
        
        self.wait()
        comma2.set_color(WHITE)
        t.set_color(RED)
        self.add_fixed_in_frame_mobjects(t2,timeValue)
        t2.next_to(s2)
        t2.shift(DOWN + LEFT*0.8)
        timeValue.next_to(t2)
        self.play(timer.animate.set_value(4), run_time=4)
        self.next_section()
        
        self.wait()
        comma3.set_color(WHITE)
        e.set_color(YELLOW_E)
        self.add_fixed_in_frame_mobjects(e2,energyValue)
        e2.next_to(t2,DOWN)
        energyValue.next_to(e2)
        self.play(energyTracker.animate.set_value(100), run_time=4)
        self.wait()
        
        