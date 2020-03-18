from manimlib.constants import *
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.mobject.types.vectorized_mobject import VMobject
from manimlib.mobject.geometry import *
from my_projects.frisbee.frisbeeConstants import *

class FrisbeePitch(VMobject):
    CONFIG = {
        "color": WHITE,
        "height": 2.0,
        "width": 4.0,
        "mark_paths_closed": True,
        "close_new_points": True,
    }

    def __init__(self,scale=14, **kwargs):
        VMobject.__init__(self, **kwargs)
        self.scale = scale
        self.inner_pitch = Rectangle(height=PITCH_WIDTH_RATIO*self.scale, width=(PITCH_HEIGHT_RATIO-2*ENDZONE_DEPTH_RATIO)*self.scale,stroke_width=2)
        self.leftEndZone = Rectangle(height=PITCH_WIDTH_RATIO*self.scale, width=ENDZONE_DEPTH_RATIO*self.scale,stroke_width=2)
        self.rightEndZone = Rectangle(height=PITCH_WIDTH_RATIO*self.scale, width=ENDZONE_DEPTH_RATIO*self.scale,stroke_width=2)
        self.leftEndZone.next_to(self.inner_pitch, LEFT, buff=0)
        self.rightEndZone.next_to(self.inner_pitch, RIGHT, buff=0)
        self.pitch = VGroup(
            self.leftEndZone,
            self.inner_pitch,
            self.rightEndZone
        )
        self.brickLeft = Dot(point=(PITCH_HEIGHT_RATIO/2-BRICK_MARK_RATIO)*self.scale*LEFT, radius=DEFAULT_DOT_RADIUS/2)
        self.brickRight = Dot(point=(PITCH_HEIGHT_RATIO/2-BRICK_MARK_RATIO)*self.scale*RIGHT, radius=DEFAULT_DOT_RADIUS/2)
        self.brickMarks = VGroup(
            self.brickLeft,
            self.brickRight,
        )



