from manim import *
from PIL import Image
import math
import numpy as np
from objects.beam import * 
from random import *



class Detector(ThreeDScene):

    def GetRandomBeam(self,source, detector, phantomCenter, probabilities, counter, reference_length,  length = 1):
        rng = uniform(0,100)
        if(rng <= probabilities[0]):
            #Transmission
            return Beam(length=length,start=source, end=detector[1].get_center(), counter=counter, reference_length=reference_length)
        elif(rng <= probabilities[1]):
            #Absorption
            return Beam(length=length,start=source, end=phantomCenter, reference_length=reference_length)
        else:
            #Scattering
            rng = uniform(0,2*np.pi)
            r = 4
            return Scattering(length=length, start=source, scatteringPoint=phantomCenter, end=[-3,r*np.cos(rng),r*np.sin(rng)], reference_length=reference_length)
        

    def construct(self):        
    
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
            
            
        self.pixelHeight = 1
        self.pixelSize = 1
        
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES)
        
        
        counter1 = ValueTracker(0)
        detectorShape1 = Prism(dimensions=[self.pixelSize,self.pixelSize,self.pixelHeight], fill_opacity=0.5, fill_color=ORANGE, stroke_width=3)
        detectorCount1 = Integer(0, color=WHITE, font_size = 120, stroke_width=1.5, stroke_color=BLACK)
        detectorShape1.shift(0.8*UP)
        detectorCount1.tracker = counter1
        detector1 = VGroup(detectorShape1,detectorCount1)
        detector1.add_updater(detectorUpdater)
        detectorUpdater(detector1)
        
        counter2 = ValueTracker(0)
        detectorShape2 = Prism(dimensions=[self.pixelSize,self.pixelSize,self.pixelHeight], fill_opacity=0.5, fill_color=ORANGE, stroke_width=3)
        detectorCount2 = Integer(0, color=WHITE, font_size = 120, stroke_width=1.5, stroke_color=BLACK)
        detectorShape2.shift(0.8*DOWN)
        detectorCount2.tracker = counter2
        detector2 = VGroup(detectorShape2,detectorCount2)
        detector2.add_updater(detectorUpdater)
        detectorUpdater(detector2)
      
        detector = VGroup(detector1, detector2)
        self.add(detector)
        
        
        detector.shift(5*LEFT)
        detector.rotate(PI/2,axis=[0,1,0])
        
        
        phantomCylinder1 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[WHITE,WHITE], stroke_width = 0)
        phantomCylinder2 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[WHITE,WHITE], stroke_width = 0)
        phantomCylinder1.shift(UP*0.8)
        phantomCylinder2.shift(DOWN*0.8)
        
        self.add(phantomCylinder1)
        self.add(phantomCylinder2)
        
        os = Text("Bone")
        eau = Text("Bone")
        text = VGroup(os, eau)
        text.rotate(angle=135*DEGREES, axis=[0,1,0])
        text.rotate(angle=90*DEGREES, axis=[1,0,0])
        text.shift(2*OUT)
        os.shift(0.8*UP)
        eau.shift(0.8*DOWN)
        
        self.add(text)
        
        self.wait()
        
        numberOfEvents = 100
        osAnimation = AnimationGroup(*[self.GetRandomBeam([7,0.8,0], detector1, phantomCylinder1.get_center(), [40,80,100], counter1, reference_length = 15) for _ in range(numberOfEvents)], lag_ratio = 0.4)
        eauAnimation = AnimationGroup(*[self.GetRandomBeam([7,-0.8,0], detector2, phantomCylinder2.get_center(), [40,80,100], counter2, reference_length = 15) for _ in range(numberOfEvents)], lag_ratio = 0.4)
        
        self.play(osAnimation, eauAnimation)
        self.wait()
        
