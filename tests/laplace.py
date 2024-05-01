from manim import *

class Laplace(ThreeDScene):
    
    def func(self,t):
        s = 2+1j
        return np.array([t,np.imag(np.exp(s*t)+np.exp(-1*s*t)),np.real(np.exp(s*t)+np.exp(-1*s*t))])

    def construct(self):
        self.set_camera_orientation(phi=45, theta=225)
        axes = ThreeDAxes()
        
        graph = ParametricFunction(self.func, t_range=[-10,10]).set_color(RED)
        
        self.add(axes,graph)
        self.begin_ambient_camera_rotation(rate=PI/10, about="theta")
        self.wait(5)