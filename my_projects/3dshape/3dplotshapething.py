from manimlib.imports import *

class MyThreeDAxes(ThreeDAxes):
    CONFIG = {
        "x_min": 0,
        "x_max": 5,
        "y_min": 0,
        "y_max": 5,
        "z_min": -0,
        "z_max": 3,
    }

class Thing(ThreeDScene):
    

    def construct(self):
        d_coords = np.array([3,3,1])
        axes = MyThreeDAxes()
        vec = Vector(direction=d_coords)
        point1 = Dot(point = d_coords/3)
        point2 = Dot(point = 2*d_coords/3)
        self.set_camera_orientation(phi=20 * DEGREES,theta=-86*DEGREES,distance=2)
        
        self.play(ShowCreation(axes))
        self.play(ShowCreation(vec))
        self.wait(2)
        self.play(ShowCreation(point1))
        self.play(ShowCreation(point2))
        self.wait(2)
        