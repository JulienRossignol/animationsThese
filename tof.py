from manim import *
from PIL import Image
import math
import numpy as np
from objects.beam import * 
from random import *



class Detector(ThreeDScene):

    def construct(self):        
    
      
            
            
        self.pixelHeight = 1
        self.pixelSize = 1
        
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES)
        
        
        detectorShape1 = Prism(dimensions=[self.pixelSize,self.pixelSize,self.pixelHeight], fill_opacity=0.5, fill_color=ORANGE, stroke_width=3)
        detectorShape1.shift(0.8*UP)
        
        detectorShape2 = Prism(dimensions=[self.pixelSize,self.pixelSize,self.pixelHeight], fill_opacity=0.5, fill_color=ORANGE, stroke_width=3)
        detectorShape2.shift(0.8*DOWN)
        
        detector = VGroup(detectorShape1, detectorShape2)
        self.add(detector)
        
        
        detector.shift(5*LEFT)
        detector.rotate(PI/2,axis=[0,1,0])
        
        
        phantomCylinder1 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[WHITE,WHITE], stroke_width = 0)
        phantomCylinder2 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=BLUE,checkerboard_colors=[BLUE,BLUE], stroke_width = 0)
        phantomCylinder1.shift(UP*0.8)
        phantomCylinder2.shift(DOWN*0.8)
        
        self.add(phantomCylinder1)
        self.add(phantomCylinder2)
        
        
        self.play(Scattering(start=[7,0.8,0], scatteringPoint=phantomCylinder1.get_center(), end=detectorShape2.get_center(),length = 5, run_time=10),Beam(start=[7,-0.8,0], end=detectorShape2.get_center(), length = 5, run_time=9.75))  
        self.wait()


        
