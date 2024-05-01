from manim import *
from manim_slides import ThreeDSlide
from PIL import Image
import math
import numpy as np
from beam import * 


class Scanner(ThreeDScene):
    def construct(self):        
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES)
        #self.set_camera_orientation(phi=0*DEGREES, theta=0*DEGREES)
        
        #self.activatedPixels = ValueTracker(0)
        
        phantomCylinder2 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[BLUE,BLUE], stroke_width = 0)
        #phantomCylinder3 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[WHITE,WHITE], stroke_width = 0)
        #phantomCylinder2.shift(UP*0.5)
        #phantomCylinder3.shift(DOWN*0.5)
        #phantom = VGroup(phantomCylinder2,phantomCylinder3)
        

        self.add(phantomCylinder2)
        transmission = Text("Transmission")
        photoelectrique = Text("Effet photoélectrique")
        diffusion = Text("Diffusion")
        text = VGroup(transmission, photoelectrique, diffusion)
        text.rotate(angle=135*DEGREES, axis=[0,1,0])
        text.rotate(angle=90*DEGREES, axis=[1,0,0])
        text.shift(3*OUT)
        
        self.play(Write(transmission))
        self.wait()
        self.play(Beam(start=[7,0,0], end = [-5,0,0], length=3), run_time=3)
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
        #self.next_slide()
        
