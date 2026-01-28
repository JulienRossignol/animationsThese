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
        
        
        detectorShape = Prism(dimensions=[self.pixelSize,self.pixelSize,self.pixelHeight], fill_opacity=0.5, fill_color=ORANGE, stroke_width=3)
        detectorCount = Integer(40, color=WHITE, font_size = 40, unit="\%", unit_buff_per_font_unit=0.001, stroke_width=1, stroke_color=BLACK)
        detectorCount.shift(self.pixelHeight*OUT/2)
        detectorCount.rotate(PI/2, axis=[0,0,1])
        
        detector = VGroup(detectorShape,detectorCount)
        self.add(detector)

      
        
        detector.shift(5*LEFT)
        detector.rotate(PI/2,axis=[0,1,0])
        
        
        phantomCylinder2 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[BLUE,BLUE], stroke_width = 0)
        lost = Text("60%")
        lost.rotate(angle=135*DEGREES, axis=[0,1,0])
        lost.rotate(angle=90*DEGREES, axis=[1,0,0])
        lost.shift(3*OUT)
               

        self.add(phantomCylinder2)
        self.add(lost)
        
        self.pixels = [Prism(dimensions=[self.pixelSize,self.pixelSize,self.pixelHeight], fill_opacity=0.5, fill_color=ORANGE, stroke_width=3) for _ in range(25)]
        
        detectors = VGroup(*self.pixels)
        detectors.arrange_in_grid(5,5, buff=0)      
        
        detectors.shift(5*LEFT)
        detectors.rotate(PI/2,axis=[0,1,0])
        detectors.set_z_index(-1)
        prob = [0.1,0.1,0.2,0.1,0.1,0.1,0.2,0.3,0.2,0.1,0.2,0.3,40,0.3,0.2,0.1,0.2,0.3,0.2,0.1,0.1,0.1,0.2,0.1,0.1]
        detectorCounts = [DecimalNumber(prob[i], num_decimal_places=1,color=WHITE, font_size = 40, unit="\%", unit_buff_per_font_unit=0.001, stroke_width=1, stroke_color=BLACK) for i in range(25)]
        detectorCounts[12] = DecimalNumber(40, num_decimal_places=0,color=WHITE, font_size = 40, unit="\%", unit_buff_per_font_unit=0.001, stroke_width=1, stroke_color=BLACK)
        counts = VGroup(*detectorCounts)
        counts.arrange_in_grid(5,5, buff=(0.17,0.70))  
        counts.shift(self.pixelHeight*OUT/2)
        counts.rotate(PI/2, axis=[0,0,1])
        counts.rotate(PI/2, axis=[0,1,0])
        counts.shift(5*LEFT)
        counts.shift(0.7*IN)
        counts.shift(0.4*DOWN)

        self.remove(lost)
        self.play(FadeOut(detector))
        
 
        lost = Text("56%")
        lost.rotate(angle=135*DEGREES, axis=[0,1,0])
        lost.rotate(angle=90*DEGREES, axis=[1,0,0])
        lost.shift(3*OUT)
        
        
        self.play(Create(detectors))
        self.play(Create(counts))
        self.play(Create(lost))
        
        
                       
        
        self.wait()
