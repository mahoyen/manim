from manimlib.imports import *
from my_projects.frisbee.frisbeepitch import FrisbeePitch

class CreationFrisbeePitch(Scene):

    def construct(self):
        
        frisbeePitch = FrisbeePitch()
        self.add(frisbeePitch.pitch, frisbeePitch.brickMarks)
        self.play(
            ShowCreationThenFadeAround(frisbeePitch.pitch)
        )
        self.wait(1)
        endZoneIndicateScaleFactor = 1.02
        self.play(
            Indicate(frisbeePitch.leftEndZone, scale_factor=endZoneIndicateScaleFactor),
            Indicate(frisbeePitch.rightEndZone, scale_factor=endZoneIndicateScaleFactor)
        )
        self.wait(1)
        self.play(
            Indicate(frisbeePitch.brickLeft),
            Indicate(frisbeePitch.brickRight)
        )
        self.wait(3)
        
        