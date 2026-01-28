from manim import *
from PIL import Image
import math
import numpy as np
from objects.beam import * 



class Detector(Scene):
    def construct(self):        
                
        poi = Dot3D([-5,0,0], color=RED)
        poa = Dot3D([5,0,0], color=BLUE)
        sArrow = Arrow3D(start=[-5,0,0], end=[-4,0,0], color=GREEN)
        sArrow2 = Arrow3D(start=[5,0,0], end=[6,0,0], color=GREEN)
        
        beamArrow = Arrow3D(start=[-5,0,0], end=[5,0,0])
        
        lineBreakout = [Line(start=[-4.75 + i*0.25, -1, 0], end=[-4.75 + i*0.25, 1, 0], color=BLACK) for i in range(39)]
        
        lines=VGroup(*lineBreakout)
        
        self.add(poi,beamArrow,sArrow, poa, sArrow2)
        self.wait()
        self.play(Create(lines), run_time=3)
        self.wait()
        

        
        
        
