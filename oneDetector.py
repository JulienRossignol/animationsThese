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
        
        
        self.counter = ValueTracker(0)
        detectorShape = Prism(dimensions=[self.pixelSize,self.pixelSize,self.pixelHeight], fill_opacity=0.5, fill_color=ORANGE, stroke_width=3)
        detectorCount = Integer(0, color=WHITE, font_size = 120, stroke_width=1.5, stroke_color=BLACK)
        detectorCount.shift(self.pixelHeight*OUT/2)
        detectorCount.rotate(PI/2, axis=[0,0,1])
        
        detector = VGroup(detectorShape,detectorCount)
        self.add(detector)

        def detectorUpdater(mobj):
            facecorners = mobj[0][1].get_vertices()
            u = facecorners[2]-facecorners[3]
            v = facecorners[1]-facecorners[3]
            nDetector = np.cross(u, v)
            theta = np.arccos(nDetector[2]/np.linalg.norm(nDetector))
            phi = np.arctan(nDetector[1]/nDetector[0])
            mobj[1].become(
                Integer(
                    self.counter.get_value(),
                    color=WHITE, font_size = 120,
                    stroke_width=1.5, stroke_color=BLACK
                ).rotate(90*DEGREES, OUT) # around z-axis
                .rotate(theta, UP) # around Y-axis
                .rotate(phi, OUT) # around Z-axis           
                .shift((facecorners[1]+facecorners[3])/2 )
            )
            
        detector.add_updater(detectorUpdater)
      
        
        detector.shift(5*LEFT)
        detector.rotate(PI/2,axis=[0,1,0])
        
        
        phantomCylinder2 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[BLUE,BLUE], stroke_width = 0)
        

        self.add(phantomCylinder2)
        
        transmission = Text("Transmission")
        photoelectrique = Text("Photoelectric effect")
        diffusion = Text("Scattering")
        text = VGroup(transmission, photoelectrique, diffusion)
        text.rotate(angle=135*DEGREES, axis=[0,1,0])
        text.rotate(angle=90*DEGREES, axis=[1,0,0])
        text.shift(3*OUT)
        
        self.play(Write(transmission))
        self.wait()
        self.play(Beam(start=[7,0,0], end = [-5,0,0], length=3, counter=self.counter), run_time=3)
        self.play(FadeOut(transmission))
        self.wait()
        self.play(Write(photoelectrique))
        self.wait()
        self.play(Beam(start=[7,0,0], end = [0,0,0], length=3), run_time=1.5)
        self.play(FadeOut(photoelectrique))
        self.wait()
        self.play(Write(diffusion))
        self.wait()
        self.play(Scattering(start=[7,0,0], end=[-5,2,5], scatteringPoint = [0,0,0], length=3), run_time=3.5)
        self.play(FadeOut(diffusion))
        self.wait()
        
