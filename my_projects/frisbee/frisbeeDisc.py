from manimlib.constants import *
from manimlib.mobject.geometry import *
from my_projects.frisbee.frisbeeConstants import *

class FrisbeeDisc(Dot):

    def __init__(self,scale=FRISBEE_DEFAULT_SCALE,**kwargs):
        Dot.__init__(self,radius=DEFAULT_DOT_RADIUS/1.1,color=GREEN,**kwargs)
        self.scale = scale
    