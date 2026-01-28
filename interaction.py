from manim import *
from PIL import Image
import math
import numpy as np
from objects.beam import *  


class Scanner(ThreeDScene):
    def construct(self):        
        self.pixelHeight = 1
        self.pixelSize = 1
        
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES)
        #self.set_camera_orientation(phi=0*DEGREES, theta=0*DEGREES)
        
        #self.activatedPixels = ValueTracker(0)
        
        phantomCylinder2 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[BLUE,BLUE], stroke_width = 0)
        #phantomCylinder3 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[WHITE,WHITE], stroke_width = 0)
        #phantomCylinder2.shift(UP*0.5)
        #phantomCylinder3.shift(DOWN*0.5)
        #phantom = VGroup(phantomCylinder2,phantomCylinder3)
        
        counter1 = ValueTracker(0)
        
        detectorShape = Prism(dimensions=[self.pixelSize,self.pixelSize,self.pixelHeight], fill_opacity=0.5, fill_color=ORANGE, stroke_width=3)
        detectorCount = Integer(0, color=WHITE, font_size = 120, stroke_width=1.5, stroke_color=BLACK)
        detectorCount.shift(self.pixelHeight*OUT/2)
        detectorCount.rotate(PI/2, axis=[0,0,1])
        detectorCount.tracker = counter1
        
        detector = VGroup(detectorShape,detectorCount)
        self.add(detector)

        detector.shift(5*LEFT)
        detector.rotate(PI/2,axis=[0,1,0])
        
        def detectorUpdater(mobj):
            facecorners = mobj[0][1].get_vertices()
            u = facecorners[2]-facecorners[3]
            v = facecorners[1]-facecorners[3]
            nDetector = np.cross(u, v)
            theta = np.arccos(nDetector[2]/np.linalg.norm(nDetector))
            phi = np.arctan(nDetector[1]/nDetector[0])
            
            font_size = 120
            if(mobj[1].tracker.get_value() >= 10):
                font_size = 100
            
            mobj[1].become(
                Integer(
                    mobj[1].tracker.get_value(),
                    color=WHITE, font_size = font_size,
                    stroke_width=1.5, stroke_color=BLACK
                ).rotate(90*DEGREES, OUT) # around z-axis
                .rotate(theta, UP) # around Y-axis
                .rotate(phi, OUT) # around Z-axis           
                .shift((facecorners[1]+facecorners[3])/2 )
            )
            
            
        detector.add_updater(detectorUpdater)

        self.add(phantomCylinder2)
        transmission = Text("Transmission")
        photoelectrique = Text("Photoelectric effect")
        diffusion = Text("Scattering")
        text = VGroup(transmission, photoelectrique, diffusion)
        text.rotate(angle=135*DEGREES, axis=[0,1,0])
        text.rotate(angle=90*DEGREES, axis=[1,0,0])
        text.shift(3*OUT)
        
        self.add(transmission)
        self.wait()
        self.play(AnimationGroup(*[Beam(start=[7,0,0], end = [-5,0,0], length=3, counter=counter1) for i in range(9)], lag_ratio = 0.6))

        self.next_section()
        
        self.wait()
        
        self.remove(transmission)
        self.add(photoelectrique)
        counter1.set_value(0)
        self.next_section()
        
        self.play(AnimationGroup(*[Beam(start=[7,0,0], end = [0,0,0], length=3) for i in range(10)], lag_ratio = 0.6))
        self.wait()
        self.next_section()
        
        counter1.set_value(0)
        self.remove(photoelectrique)
        self.add(diffusion)
        self.play(AnimationGroup(*[Scattering(start=[7,0,0], end=[-5,2,i], scatteringPoint = [0,0,0], length=3) for i in range(10)], lag_ratio = 0.6))
        self.wait()
        
