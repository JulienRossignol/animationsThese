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
        
        detectorShape = Prism(dimensions=[self.pixelSize,self.pixelSize,self.pixelHeight], fill_opacity=0.5, fill_color=ORANGE, stroke_width=3)
        detectorCount = Integer(40, color=WHITE, font_size = 40, unit="\%", unit_buff_per_font_unit=0.001, stroke_width=1, stroke_color=BLACK)
        detectorCount.shift(self.pixelHeight*DOWN/2)
        detectorCount.rotate(PI/2, axis=[0,0,1])
        detectorCount.rotate(-PI/2, axis=[1,0,0])
        
        detector = VGroup(detectorShape,detectorCount)
        self.add(detector)
      
        
        detector.shift(1*RIGHT)
        detector.rotate(PI/2,axis=[0,1,0])
        
        
        phantomCylinder2 = Cylinder(radius = 0.25, height = 2.4, fill_opacity = 0.8, fill_color=WHITE,checkerboard_colors=[BLUE,BLUE], stroke_width = 0)
        phantomCylinder2.shift(3*RIGHT)
        lost = Text("60%")
        lost.rotate(angle=135*DEGREES, axis=[0,1,0])
        lost.rotate(angle=90*DEGREES, axis=[1,0,0])
        lost.shift(3*OUT)
        
        axes = Axes(x_range=[0, 20, 100],y_range=[0, 1, 10],x_length=5, y_length=self.pixelSize*0.8, tips=False)
        x_axis = Text("Time", font_size =12)
        y_axis = Text("Detected photon count", font_size =12)
        
              
        plot = VGroup(axes,x_axis,y_axis)
        self.add(plot)
        plot.rotate(angle=PI/2, axis=[1,0,0])
        plot.rotate(angle=PI,axis=[0,0,1])
        plot.shift(LEFT*2.40)
        y_axis.shift(RIGHT*1.7 + OUT*0.55)
        x_axis.shift(LEFT*2.5 + IN*0.55)
        
        axesS = Axes(x_range=[0, 20, 100],y_range=[0, 1, 10],x_length=5, y_length=self.pixelSize*0.8, tips=False)
        x_axisS = Text("Time", font_size =12)
        y_axisS = Text("Emitted photon count", font_size =12)
        
              
        plotS = VGroup(axesS,x_axisS,y_axisS)
        plotS.rotate(angle=PI/2, axis=[1,0,0])
        plotS.rotate(angle=PI,axis=[0,0,1])
        plotS.shift(LEFT*2.40 + OUT*2)
        y_axisS.shift(RIGHT*2 + OUT*0.55)
        x_axisS.shift(LEFT*2.5 + IN*0.55)
        
               
        x = [0, 1, 2, 3, 4,4.9, 5,5.1, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20]
        y = [0,0,0,0,0,0,1,0.2,0.15,0.08,0.05,0.01]
        graph = axes.plot_line_graph(x, y, line_color = RED,add_vertex_dots=False,stroke_width = 4)
        
        xS = [-0.1,0,0.1]
        yS = [0,1,0]
        graphS = axesS.plot_line_graph(xS, yS, line_color = RED,add_vertex_dots=False,stroke_width = 4)
        
        self.add(phantomCylinder2)
                       
        #self.play(Beam(start=[7,0,0], end = [1,0,0], length=3), run_time=3)
        #self.play(Beam(start=[7,0,0], end = [3,0,0], length=3), run_time=1.5)
        #self.play(Scattering(start=[7,0,0], end=[1,2,5], scatteringPoint = [3,0,0], length=3), run_time=3.5)
        #self.wait()
        #self.play(Write(lost))
        self.play(Write(graph))
        self.play(Create(plotS))
        self.play(Write(graphS))
        self.play(AnimationGroup(graph.animate.shift(LEFT*2.5),graphS.animate.shift(LEFT*2.5)), run_time=5)
        self.wait(3)
        self.next_section()
        
        
        graphS2 = axesS.plot_line_graph(xS, [i*0.5 for i in yS], line_color = BLUE,add_vertex_dots=False,stroke_width = 4)
        
        graph2 = axes.plot_line_graph(x, [i*0.5 for i in y], line_color = BLUE,add_vertex_dots=False,stroke_width = 4)
        self.play(Create(graphS2))
        self.play(Create(graph2), run_time=2)
        self.wait(3)
        self.next_section()
        
        xLong = np.arange(0,20,0.1)
        yLong = np.interp(xLong,x,[0,0,0,0,0,0,1,0.2,0.15,0.08,0.05,0.01,0,0,0,0,0,0,0,0,0,0,0])
        
        xS = [0.1,0.2,0.3,0.5,1.6,1.7,1.8,2.5,3,3.5,4.4,4.5,4.6,5]
        yS = [0  ,0.5,0  ,0  ,0  ,0.8  ,0  ,0  ,0,0  ,0  ,1  ,0  ,0]
        ySLong = np.interp(xLong,xS,yS)
        
        outConvolve = np.convolve(yLong,ySLong)
        outConvolve = outConvolve[0:200] / np.max(outConvolve)
        
        self.remove(graph)
        self.remove(graph2)
        self.remove(graphS)
        self.remove(graphS2)
        
        graph3 = axes.plot_line_graph(xLong,outConvolve, line_color = PURPLE,add_vertex_dots=False,stroke_width = 4)
        graph4 = axesS.plot_line_graph(xLong,ySLong,line_color = PURPLE,add_vertex_dots=False,stroke_width = 4)
        self.play(AnimationGroup(Write(graph3),Write(graph4)), run_time=4)
        self.wait(3)