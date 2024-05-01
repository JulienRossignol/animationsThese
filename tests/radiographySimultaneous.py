from manim import *
from manim_slides import ThreeDSlide
from PIL import Image
import math
import numpy as np
from beam import * 


class Scanner(ThreeDScene):
    def setImageTarget(self, imageFilepath, valueTracker = False):
        with Image.open(imageFilepath) as image:         
            smallImage = image.resize((self.panelWidth,self.panelHeight))
            bitmap = smallImage.load()
            self.imagePixels = []
            for i in range(self.panelWidth):
                for j in range(self.panelHeight):
                    color = bitmap[i,j]
                    colorScale = tuple(x/255 for x in color)
                    manimColor = rgba_to_color(colorScale)
                    self.imagePixels.append(Square(side_length=self.pixelSize, fill_color=manimColor, fill_opacity=0, stroke_width=0))
            
            if(valueTracker):
                for i in range(len(self.imagePixels)):
                    self.imagePixels[i].pixelId = i
                    self.imagePixels[i].add_updater(lambda mob : mob.set_opacity(int(self.activatedPixels.get_value()>mob.pixelId)))
                 
                    
    def construct(self):
        self.pixelHeight = 0.5
        self.pixelSize = 0.25
        self.panelWidth = 20
        self.panelHeight = 20
        imagePath = "phantom.PNG"
        self.sourcePos = [7,0,0]
        
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES)
        #self.set_camera_orientation(phi=0*DEGREES, theta=0*DEGREES)
        
        #self.activatedPixels = ValueTracker(0)
        
        axes = ThreeDAxes()
        self.pixels = [Prism(dimensions=[self.pixelSize,self.pixelSize,self.pixelHeight], fill_opacity=0.5, fill_color=ORANGE, stroke_width=3) for _ in range(self.panelWidth*self.panelHeight)]
        self.setImageTarget(imagePath)
        
        detector = VGroup(*self.pixels)
        detector.arrange_in_grid(self.panelWidth,self.panelHeight, buff=0)      
        image = VGroup(*self.imagePixels)
        image.arrange_in_grid(self.panelWidth,self.panelHeight,buff=0.00)
        image.shift(self.pixelHeight*OUT/2)
               
        detectorAndImage = VGroup(detector,image)
        detectorAndImage.shift(5*LEFT)
        detectorAndImage.rotate(PI/2,axis=[0,1,0])
        
        self.pixelCenter = [pixel.get_center() for pixel in self.imagePixels]
       
        phantomCylinder1 = Cylinder(radius = 1.5, height = 2.5, fill_opacity = 0.6, fill_color=BLUE, checkerboard_colors=[BLUE,BLUE], stroke_width = 0)
        phantomCylinder2 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[WHITE,WHITE], stroke_width = 0)
        phantomCylinder3 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[WHITE,WHITE], stroke_width = 0)
        phantomCylinder2.shift(UP*0.5)
        phantomCylinder3.shift(DOWN*0.5)
        phantom = VGroup(phantomCylinder1,phantomCylinder2,phantomCylinder3)
        
        
        sourceFocalPoint = Sphere(center =[7,0,0], radius = 0.05 ,fill_opacity = 1)
        sourceFocalPoint.set_color(WHITE)
        sourceCone = Cone(base_radius=4, height=12, direction=X_AXIS, fill_opacity=0.1, stroke_width = 0.1)
        sourceCone.shift(self.sourcePos)
        source = VGroup(sourceFocalPoint,sourceCone)
        
        
        #self.begin_ambient_camera_rotation(rate=PI / 30, about="theta")
        
        #self.add(detector,phantom,source,image)
        self.add(image, detector, phantom, source)
        self.play(AnimationGroup(*[Beam(start=self.sourcePos, end=pixel.get_center(), pixel=pixel, length=3) for pixel in self.imagePixels], lag_ratio=0,rate_func=linear, run_time=3))
        self.wait()
        #self.next_slide()
        
