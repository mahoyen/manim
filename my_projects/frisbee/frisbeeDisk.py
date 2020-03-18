from manimlib.constants import *
from manimlib.mobject.geometry import *
from my_projects.frisbee.frisbeeConstants import *

class FrisbeeDisk(Dot):

    def __init__(self,scale=FRISBEE_DEFAULT_SCALE,**kwargs):
        Dot.__init__(self,radius=DEFAULT_DOT_RADIUS/1.5,color=PINK,**kwargs)
        self.scale = scale
        self.playerPossesion = None

    def positionDisk(self):
        if self.playerPossesion is None:
            return
        currentPlayer = self.playerPossesion
        print(currentPlayer)
        offsetDirection = np.cross(currentPlayer.direction, Z_AXIS) + currentPlayer.direction
        diskPosition = currentPlayer.get_position() + offsetDirection*0.5*currentPlayer.radius
        print(diskPosition)
        print(type(diskPosition))
        Dot.arc_center = diskPosition