from manim import *
from PIL import Image
import math
import numpy as np
from objects.beam import * 



class Detector(ThreeDScene):
    def construct(self):        
        self.pixelHeight = 1
        self.pixelSize = 1
        
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES)
                
        detector = Prism(dimensions=[self.pixelSize,self.pixelSize,self.pixelHeight], fill_opacity=0.5, fill_color=ORANGE, stroke_width=3)
        detector.shift(5*LEFT)
        detector.rotate(PI/2,axis=[0,1,0])
        phantom = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[BLUE,BLUE], stroke_width = 0)
        scanner = VGroup(detector, phantom)
                
        poi = Dot3D([5,0,0], color=RED)
        sArrow = Arrow3D(start=[5,0,0], end=[4,0,0], color=GREEN)
        
        beamArrow = Arrow3D(start=[5,0,0], end=[-5,0,0])
        poa = Dot3D([-5,0,0], color=BLUE)
        
        
        self.play(Create(scanner))
        self.wait()
        self.play(Create(poi))
        self.wait()
        self.play(Create(beamArrow))
        self.add(poa)
        self.wait()
        self.play(Create(sArrow))
        self.wait()
        

        
        
        
