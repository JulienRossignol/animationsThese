from manim import *
from PIL import Image
import math
import numpy as np
from objects.beam import * 



class Detector(ThreeDScene):
    def construct(self):        
        self.pixelHeight = 1
        self.pixelSize = 1
        
        self.set_camera_orientation(phi=90*DEGREES, theta=90*DEGREES)
        
        detectorShape = [Prism(dimensions=[self.pixelSize,self.pixelSize,self.pixelHeight], fill_opacity=0.5, fill_color=ORANGE, stroke_width=3) for i in range(5)]
        detectorShape[0].shift(LEFT*2)
        detectorShape[1].shift(LEFT*1)
        detectorShape[3].shift(RIGHT*1)
        detectorShape[4].shift(RIGHT*2)
        detectorShapes = VGroup(*detectorShape)
        value = [0.1,0.2,40,0.2,0.1]
        decimalPlace = [1,1,0,1,1]
        detectorCount = [DecimalNumber(value[i],num_decimal_places =decimalPlace[i], color=WHITE, font_size = 40, unit="\%", unit_buff_per_font_unit=0.001, stroke_width=1, stroke_color=BLACK) for i in range(5)]
        detectorCount[0].shift(DOWN*2)
        detectorCount[1].shift(DOWN*1)
        detectorCount[3].shift(UP*1)
        detectorCount[4].shift(UP*2)
        detectorCounts = VGroup(*detectorCount)
        detectorCounts.shift(self.pixelHeight*DOWN/2)
        detectorCounts.rotate(PI/2, axis=[0,0,1])
        detectorCounts.rotate(-PI/2, axis=[1,0,0])
        
        detector = VGroup(*detectorShapes,*detectorCounts)
        
        self.add(detector)
      
        detector.shift(1*RIGHT)
        detector.rotate(PI/2,axis=[0,1,0])
        
        
        phantomCylinder2 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[BLUE,BLUE], stroke_width = 0)
        phantomCylinder2.shift(3*RIGHT)
       
        axes = [Axes(x_range=[0, 10, 100],y_range=[0, 1, 10],x_length=2.5, y_length=self.pixelSize*0.8, tips=False) for i in range(5)]
        axes[0].shift(DOWN*2)
        axes[1].shift(DOWN*1)
        axes[3].shift(UP*1)
        axes[4].shift(UP*2)
        x_axis = Text("Time", font_size =12)
        y_axis = Text("Detected photon count", font_size =12)
        
              
        plot = VGroup(*axes,x_axis,y_axis)
        self.add(plot)
        plot.rotate(angle=PI/2, axis=[1,0,0])
        plot.rotate(angle=PI,axis=[0,0,1])
        plot.shift(LEFT*1.25)
        y_axis.shift(RIGHT*0.4 + OUT*2.55)
        x_axis.shift(LEFT*1.5 + IN*2.55)
        
        x0 = [0, 1, 2, 3, 4, 6.1, 6.2, 6.3, 6.5, 7, 8, 9, 10]
        y0 = [0,0,0,0,0,0,0.7,0.4,0.3,0.2,0.2,0.1,0]
        
        x1 = [0,1,2,3,4,5.5,5.6,5.7,6,7,8,9,10]
        y1 = [0,0,0,0,0,0,0.8,0.3,0.2,0.1,0.1,0.1,0]
        
        x2 = [0, 1, 2, 3, 4,4.9, 5,5.1, 6, 7, 8, 9, 10]
        y2 = [0,0,0,0,0,0,1,0.2,0.15,0.08,0.05,0.01,0]
        
        x3 = [0,1,2,3,4,5.5,5.6,5.7,6,7,8,9,10]
        y3 = [0,0,0,0,0,0,0.8,0.3,0.2,0.1,0.1,0.1,0]
        
        x4 = [0, 1, 2, 3, 4, 6.1, 6.2, 6.3, 6.5, 7, 8, 9, 10]
        y4 = [0,0,0,0,0,0,0.7,0.4,0.3,0.2,0.2,0.1,0]
        
        graph = [0,0,0,0,0]
        graph[0] = axes[0].plot_line_graph(x0, y0, line_color = RED,add_vertex_dots=False,stroke_width = 4)
        graph[1] = axes[1].plot_line_graph(x1, y1, line_color = RED,add_vertex_dots=False,stroke_width = 4)
        graph[2] = axes[2].plot_line_graph(x2, y2, line_color = RED,add_vertex_dots=False,stroke_width = 4)
        graph[3] = axes[3].plot_line_graph(x3, y3, line_color = RED,add_vertex_dots=False,stroke_width = 4)
        graph[4] = axes[4].plot_line_graph(x4, y4, line_color = RED,add_vertex_dots=False,stroke_width = 4)
        
        
        self.add(phantomCylinder2)
                       
        #self.play(Beam(start=[7,0,0], end = [1,0,0], length=3), run_time=3)
        #self.play(Beam(start=[7,0,0], end = [3,0,0], length=3), run_time=1.5)
        #self.play(Scattering(start=[7,0,0], end=[1,2,5], scatteringPoint = [3,0,0], length=3), run_time=3.5)
        #self.wait()
        #self.play(Write(lost))
        self.play(AnimationGroup(*[Write(graph[i]) for i in range(5)]))           
        self.wait(3)