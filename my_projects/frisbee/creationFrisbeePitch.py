from manimlib.imports import *
from my_projects.frisbee.frisbeepitch import FrisbeePitch

class CreationFrisbeePitch(Scene):

    def construct(self):
        pitchLabel = TextMobject("Pitch")
        endzoneLabel = TextMobject("End Zones")
        brickmarkLabel = TextMobject("Brick Marks")

        pitchLabel.to_edge(UP)
        endzoneLabel.to_edge(UP)
        brickmarkLabel.to_edge(UP)
        

        frisbeePitch = FrisbeePitch()
        self.add(frisbeePitch.pitch, frisbeePitch.brickMarks)
        self.play(
            FadeIn (pitchLabel),
            ShowCreationThenFadeAround(frisbeePitch.pitch)
        )
        self.wait(1)
        self.play(FadeOut(pitchLabel))
        endZoneIndicateScaleFactor = 1.02
        self.play(
            FadeIn(endzoneLabel),
            Indicate(frisbeePitch.leftEndZone, scale_factor=endZoneIndicateScaleFactor),
            Indicate(frisbeePitch.rightEndZone, scale_factor=endZoneIndicateScaleFactor)
        )
        self.wait(1)
        self.play(FadeOut(endzoneLabel))
        brickMarkIndicateScaleFactor = 3
        self.play(
            FadeIn(brickmarkLabel),
            Indicate(frisbeePitch.brickLeft, scale_factor=brickMarkIndicateScaleFactor),
            Indicate(frisbeePitch.brickRight, scale_factor=brickMarkIndicateScaleFactor)
        )
        self.wait(1)
        self.play(FadeOut(brickmarkLabel))
        self.wait(3)
        
        