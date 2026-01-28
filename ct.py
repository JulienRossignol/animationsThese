from manim import *
from PIL import Image
import math
import numpy as np
from objects.beam import * 


class Scanner(ThreeDScene):
    def setImageTarget(self, imageFilepath):
        with Image.open(imageFilepath) as image:         
            smallImage = image.resize((self.panelWidth,self.panelHeight))
            bitmap = smallImage.load()
            for i in range(self.panelWidth):
                for j in range(self.panelHeight):
                    color = bitmap[i,j]
                    colorScale = (color/255, color/255, color/255)
                    manimColor = rgb_to_color(colorScale)
                    self.pixels[i*self.panelHeight+j].set_color(manimColor)
                    self.pixels[i*self.panelHeight+j][3].set_opacity(1)
                    
                    
    def construct(self):
        self.pixelHeight = 0.5
        self.pixelSize = 0.1
        self.panelWidth = 50
        self.panelHeight = 50
        imagePath = "ctImages/"
        self.sourcePos = [7,0,0]
        
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES)
        #self.set_camera_orientation(phi=0*DEGREES, theta=0*DEGREES)
        
        #self.activatedPixels = ValueTracker(0)
        
        axes = ThreeDAxes()
        self.pixels = [Prism(dimensions=[self.pixelSize,self.pixelSize,self.pixelHeight], fill_opacity=0.5, fill_color=ORANGE, stroke_width=3) for _ in range(self.panelWidth*self.panelHeight)]
        
        detector = VGroup(*self.pixels)
        detector.arrange_in_grid(self.panelWidth,self.panelHeight, buff=0)      
        
        detector.shift(5*LEFT)
        detector.rotate(PI/2,axis=[0,1,0])
        detector.set_z_index(-1)
        
       
        phantomCylinder1 = Cylinder(radius = 1.5, height = 2.5, fill_opacity = 0.6, fill_color=BLUE, checkerboard_colors=[BLUE,BLUE], stroke_width = 0)
        phantomCylinder2 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[WHITE,WHITE], stroke_width = 0)
        phantomCylinder3 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[WHITE,WHITE], stroke_width = 0)
        phantomCylinder2.shift(UP*0.5)
        phantomCylinder3.shift(DOWN*0.5)
        phantom = VGroup(phantomCylinder1,phantomCylinder2,phantomCylinder3)
        phantomCylinder1.set_z_index(2)
        phantomCylinder2.set_z_index(1)
        phantomCylinder3.set_z_index(1)
        
        
        sourceFocalPoint = Sphere(center =[7,0,0], radius = 0.05 ,fill_opacity = 1)
        sourceFocalPoint.set_color(WHITE)
        sourceCone = Cone(base_radius=4, height=12, direction=X_AXIS, fill_opacity=0.1, stroke_width = 0.1)
        sourceCone.shift(self.sourcePos)
        source = VGroup(sourceFocalPoint,sourceCone)
        
        #self.begin_ambient_camera_rotation(rate=PI / 3000000, about="theta")
        
        #self.add(detector,phantom,source,image)
        ctScanner = VGroup(detector,source)
        self.add(ctScanner)
        self.add(phantom)
        for i in range(0,360):
            self.setImageTarget(imagePath+str(i)+".png")
            self.play(Rotate(ctScanner, DEGREES, about_point=[0,0,0]), run_time=10/360)
                
        self.wait()
        
