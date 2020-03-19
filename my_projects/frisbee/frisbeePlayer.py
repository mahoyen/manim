from manimlib.mobject.geometry import Dot
from my_projects.frisbee.frisbeeConstants import *

class FrisbeePlayer(Dot):

    def __init__(self, direction, mode, formation, role, **kwargs):
        Dot.__init__(self,**kwargs)
        self.direction = direction
        self.mode = mode
        self.formation = formation
        self.role = role
           

    def move_to(self, point):
        self.move_arc_center_to(point)

    
    def get_position(self):
        return self.get_center
    