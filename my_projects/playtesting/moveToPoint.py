import numpy as np
from manimlib.animation.movement import Homotopy

class MoveToPointAndRotate(Homotopy):
    def __init__(self, point, angle, mobject):
        mx, my, mz = mobject.get_center()
        x, y, z = point
        delta_coords =  np.array([[x-mx], [y-my], [z-mz]])
        theta = np.deg2rad(angle)
        def moveFunc(x, y, z, t):
            vector = np.array([x, y, z, 1])
            rotMat = np.array([np.cos(t*theta), -np.sin(t*theta), 0],
                              [np.sin(t*theta),  np.cos(t*theta), 0],
                              [              0,                0, 1]])
            rotTransMat = np.hstack((np.identity(3), t*delta_coords))
            return np.matmul(rotTransMat, vector)
        Homotopy.__init__(self, moveFunc, mobject)


class MoveToPoint(MoveToPointAndRotate):
    def __init__(self, point, mobject):
        MoveToPointAndRotate.__init__(self, point=point, angle=0, mobject=mobject)