from manimlib.mobject.geometry import Dot
from my_projects.frisbee.frisbeeConstants import *

class FrisbeePlayer(Dot):

    def __init__(self, direction, mode, formation, role, **kwargs):
        Dot.__init__(self,**kwargs)
        self.direction = direction
        self.mode = mode
        self.formation = formation
        self.role = role

    def __str__(self):
        variableString = ["position: "+str(self.arc_center),
            "direction: " + str(self.direction),
            "mode:      " + str(self.mode),
            "formation: " + str(self.formation),
            "role:      " + str(self.role),
            "direction: " + str(self.direction)]
        return "\n".join(variableString)
            

    def move_to(self, point):
        self.dot.move_arc_center_to(point)
    