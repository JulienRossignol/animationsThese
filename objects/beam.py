from manim import *
import math
import numpy as np

class Beam(Animation):
    def __init__(self, length=1, start=[0,0,0], end = [1,1,0], color = WHITE, stroke_width = 6, pixel=None, counter=None, reference_length = 0, **kwargs):
        self.mobject = Arrow(start=start, end=end, color=color, stroke_width=stroke_width)
        super().__init__(self.mobject,**kwargs)
        self.source = np.array(self.mobject.get_start())
        self.end = np.array(self.mobject.get_end())
        self.length = length
        self.direction = self.end - self.source
        self.directionUnitary = self.direction/np.linalg.norm(self.direction)
        self.falseStart = self.source - (self.directionUnitary*self.length)
        self.currentLength = self.length
        self.currentStart = self.source
        self.pixel = pixel
        self.counter = counter
        self.reference_length = reference_length
        self.incremented = False
    
    def _setup_scene(self,scene):
        scene.add(self.mobject)
        super()._setup_scene(scene)
    
    def clean_up_from_scene(self,scene):
        super().clean_up_from_scene(scene)
        scene.remove(self.mobject)
    
    def begin(self):
        self.interpolate_mobject(0)
        super().begin()
    
    def interpolate_mobject(self, alpha):
        alpha = self.rate_func(alpha)
        
        if(self.reference_length != 0):
            alpha = alpha/(np.linalg.norm(self.direction+self.length)/self.reference_length)
            if(alpha > 1):
                alpha = 1
        
        self.currentEnd = self.falseStart + (self.directionUnitary*self.length) + (alpha*(self.direction+(self.directionUnitary*self.length)))

        lengthToEnd = np.linalg.norm(self.currentEnd - self.source)
        if(lengthToEnd > 0.001):
            if(lengthToEnd <= self.length):
                self.currentStart = self.source
                self.mobject.set_opacity(1)
            else:
                self.currentStart = self.falseStart + (alpha*(self.direction+(self.directionUnitary*self.length)))
                self.mobject.set_opacity(1)
            self.mobject.put_start_and_end_on(self.currentStart,self.currentEnd)
        else:
            self.mobject.set_opacity(0)
        
        lengthCurrentStartToEnd = np.linalg.norm(self.end-self.currentStart)
        
        if(lengthCurrentStartToEnd <= 0.001):
            self.mobject.set_opacity(0)
            if(self.pixel != None):
                self.pixel.set_opacity(1)

        elif(lengthCurrentStartToEnd  <= self.length):
            self.mobject.scale(lengthCurrentStartToEnd/self.currentLength, scale_tips = True)
            self.currentLength = lengthCurrentStartToEnd
            self.mobject.set_opacity(1)           
            self.mobject.put_start_and_end_on(self.currentStart,self.end)
            if(self.pixel != None):
                self.pixel.set_opacity(1-(lengthCurrentStartToEnd/self.length))
            if(self.counter != None and self.incremented == False):
                self.counter.increment_value(1)
                self.incremented = True
            


class Scattering(Animation):
    def __init__(self, length=1, start=[0,0,0], scatteringPoint = [1,1,0], end = [0,1,0], color = WHITE, scattering_color = RED, stroke_width = 6, pixel=None, counter=None, reference_length = 0, **kwargs):
        self.mobject = Arrow(start=start, end=scatteringPoint, color=color, stroke_width=stroke_width)
        self.scatteringArrow = Arrow(start=scatteringPoint, end=end, color=scattering_color, stroke_width=stroke_width, fill_opacity = 0)
        self.residualArrow = Line(start=start, end=scatteringPoint, color=color, stroke_width=stroke_width, fill_opacity=0)
        super().__init__(self.mobject,**kwargs)
        
        self.source = np.array(start)
        self.scatteringPoint = np.array(scatteringPoint)
        self.end = np.array(end)
        
        self.length = length
                
        self.directionBefore = self.scatteringPoint - self.source
        self.directionBeforeUnitary = self.directionBefore/np.linalg.norm(self.directionBefore)
        self.lengthBefore = np.linalg.norm(self.directionBefore)
        
        self.directionAfter = self.end - self.scatteringPoint
        self.directionAfterUnitary = self.directionAfter/np.linalg.norm(self.directionAfter)
        self.lengthAfter = np.linalg.norm(self.directionAfter)
        
        self.totalDistance = self.lengthBefore + self.lengthAfter + self.length
        
        self.falseStart = self.source - (self.directionBeforeUnitary*self.length)
        self.currentLength = self.length
        self.pixel = pixel
        self.counter = counter
        self.reference_length = reference_length
        self.incremented = False
    
    def _setup_scene(self,scene):
        scene.add(self.mobject)
        scene.add(self.scatteringArrow)
        scene.add(self.residualArrow)
        super()._setup_scene(scene)
    
    def clean_up_from_scene(self,scene):
        super().clean_up_from_scene(scene)
        scene.remove(self.mobject)
        scene.remove(self.scatteringArrow)
        scene.remove(self.residualArrow)
    
    def begin(self):
        self.interpolate_mobject(0)
        super().begin()
    
    def interpolate_mobject(self, alpha):
        alpha = self.rate_func(alpha)
        
        if(self.reference_length != 0):
            alpha = alpha/(np.linalg.norm(self.totalDistance)/self.reference_length)
            if(alpha > 1):
                alpha = 1
        
        travelledLength = self.totalDistance*alpha
        
        if(travelledLength < 0.001):
            #No movement yet
            self.mobject.set_opacity(0)
            self.scatteringArrow.set_opacity(0)
            self.residualArrow.set_opacity(0)
        elif(self.totalDistance - travelledLength < 0.01):
            #End of animation
            self.mobject.set_opacity(0)
            self.scatteringArrow.set_opacity(0)
            self.residualArrow.set_opacity(0)   
        elif(travelledLength < self.lengthBefore):
            #Only primary arrow
            if(travelledLength < self.length):
                currentStart = self.source
            else:
                currentStart = self.source + (travelledLength-self.length)*self.directionBeforeUnitary
            currentEnd = self.source + travelledLength*self.directionBeforeUnitary
            
            self.mobject.put_start_and_end_on(currentStart,currentEnd)
            self.mobject.set_opacity(1)
            self.scatteringArrow.set_opacity(0)
            self.residualArrow.set_opacity(0) 
        elif(travelledLength > self.lengthBefore + self.length):
            #Only scatteringArrow
            currentStart = self.scatteringPoint + ((travelledLength-self.lengthBefore)-self.length)*self.directionAfterUnitary
            
            if(travelledLength > self.lengthBefore+self.lengthAfter):
                #End of course
                currentEnd = self.end
                self.scatteringArrow.put_start_and_end_on(currentStart,currentEnd)
                #Scale arrow at the end of course
                lengthToEnd = self.totalDistance - travelledLength
                self.scatteringArrow.scale(lengthToEnd/self.currentLength, scale_tips = True)
                self.currentLength = lengthToEnd                
                self.scatteringArrow.put_start_and_end_on(currentStart,currentEnd)
                
                if(self.pixel != None):
                    self.pixel.set_opacity(1-(lengthToEnd/self.length))
                if(self.counter != None and self.incremented == False):
                    self.counter.increment_value(1)
                    self.incremented = True
            else:
                currentEnd = self.scatteringPoint + (travelledLength-self.lengthBefore)*self.directionAfterUnitary
                self.scatteringArrow.put_start_and_end_on(currentStart,currentEnd)
            
            self.mobject.set_opacity(0)
            self.scatteringArrow.set_opacity(1)
            self.residualArrow.set_opacity(0) 
        else:
            #Both arrow
            primaryArrowStart = self.source + (travelledLength-self.length)*self.directionBeforeUnitary
            self.residualArrow.put_start_and_end_on(primaryArrowStart, self.scatteringPoint)
            
            scatteredArrowEnd = self.scatteringPoint + (travelledLength-self.lengthBefore)*self.directionAfterUnitary
            self.scatteringArrow.put_start_and_end_on(self.scatteringPoint, scatteredArrowEnd)
            
            self.mobject.set_opacity(0)
            self.scatteringArrow.set_opacity(1)
            self.residualArrow.set_opacity(1)

