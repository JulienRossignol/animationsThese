from manim import *
from manim_slides import Slide


class FirstExemple(Slide):
    def construct(self):
        ax = Axes(x_range = (-3,3), y_range=(-3,3))
        curve = ax.plot(lambda x: (x+2)*(x)*(x-2)/2, color=RED)
        area = ax.get_area(curve, x_range=(-2,0))
        self.play(Create(ax),Create(curve), run_time=3)
        self.play(FadeIn(area))
        self.next_slide()
        
       
        