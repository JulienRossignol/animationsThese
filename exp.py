from manim import *
from PIL import Image
import math
import numpy as np
from objects.beam import * 


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
                    self.pixels[i*self.panelHeight+j].generate_target()
                    self.pixels[i*self.panelHeight+j].targetColor = manimColor
                    self.pixels[i*self.panelHeight+j].set_opacity(1)
                    self.imagePixels.append(Square(side_length=self.pixelSize, fill_color=manimColor, fill_opacity=0, stroke_width=0))
            
            if(valueTracker):
                for i in range(len(self.imagePixels)):
                    self.pixels[i].pixelId = i
                    self.pixels[i].add_updater(lambda mob :  mob.set_color(mob.targetColor) if(int(self.activatedPixels.get_value()>mob.pixelId)) else mob)
                 
                    
    def construct(self):
        self.pixelHeight = 0.5
        self.pixelSize = 0.1
        self.panelWidth = 16
        self.panelHeight = 1
        imagePath = "images/phantom.PNG"
        self.sourcePos = [7,0,0]
        
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES)
        
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
        
        self.sourceArrow = [Arrow(start=[7,self.pixelCenter[i][1],self.pixelCenter[i][2]], end=self.pixelCenter[i], color=WHITE) for i in range(1,16,4)]
        sourceArrows = VGroup(*self.sourceArrow)       
        #self.begin_ambient_camera_rotation(rate=PI / 30, about="theta")
        
        #self.add(detector,phantom,source,image)
        self.add(image)
        self.add(detector)
        self.add(phantom)
        self.add(sourceArrows)
        self.next_section();
        self.play(phantom.animate.shift(UP*2), run_time=4)
        self.play(phantom.animate.shift(DOWN*2))
        self.wait()
        self.next_section()
        self.play(phantom.animate.rotate(PI/2,axis=[0,0,1]))
        self.play(phantom.animate.rotate(PI/2,axis=[0,0,1]))
        self.play(phantom.animate.rotate(PI/2,axis=[0,0,1]))
        self.play(phantom.animate.rotate(PI/2,axis=[0,0,1]))
        self.next_section()
        
        self.play(Uncreate(sourceArrows))
        
        self.sourceArrow = [Arrow(start=[7,self.pixelCenter[i][1],self.pixelCenter[i][2]], end=[-10,self.pixelCenter[i][1],self.pixelCenter[i][2]], color=WHITE) for i in range(1,16,4)]
        sourceArrows = VGroup(*self.sourceArrow)  
        self.play(detector.animate.shift(OUT*0.25), run_time=2)
        self.play(Create(sourceArrows))
        self.wait()
        self.next_section()
        self.diffusionArrow = [Arrow(start=[0,self.pixelCenter[i][1],self.pixelCenter[i][2]], end=[-5,self.pixelCenter[i][1],self.pixelCenter[i][2]+0.25], color=RED) for i in range(1,16,4)]
        diffusionArrows = VGroup(*self.diffusionArrow)
        self.play(Create(diffusionArrows), run_time=2)
        self.wait()