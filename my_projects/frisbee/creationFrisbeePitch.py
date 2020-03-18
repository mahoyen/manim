from manimlib.imports import *
from my_projects.frisbee.frisbeepitch import FrisbeePitch
from my_projects.frisbee.frisbeeTeam import FrisbeeTeam
from my_projects.frisbee.frisbeeDisk import FrisbeeDisk

class CreationFrisbeePitch(Scene):

    def construct(self):
        title = TextMobject("The Frisbee Pitch Overview")

        pitchLabel = TextMobject("Pitch")
        endzoneLabel = TextMobject("End Zones")
        brickmarkLabel = TextMobject("Brick Marks")
        teamLabel = TextMobject("Teams")
        diskLabel = TextMobject("Disk")

        pitchLabel.to_edge(UP)
        endzoneLabel.to_edge(UP)
        brickmarkLabel.to_edge(UP)
        teamLabel.to_edge(UP)
        diskLabel.to_edge(UP)
        

        frisbeePitch = FrisbeePitch()
        self.play(
            Write(title,run_time = 4)
        )
        self.wait()
        self.play(
            FadeOut(title),
        )
        self.add(frisbeePitch.pitch, frisbeePitch.brickMarks)
        self.play(
            FadeIn (pitchLabel),
            ShowCreationThenFadeAround(frisbeePitch.pitch)
        )

        self.wait(1)
        self.play(FadeOut(pitchLabel))

        self.wait(1)
        

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
        self.wait(1)
        
        blueteam = FrisbeeTeam(RIGHT,"offense",color=BLUE)
        redteam = FrisbeeTeam(LEFT, "defense", color=RED)

        self.play(
            FadeInFromPoint(blueteam.players, LEFT_SIDE),
            FadeInFromPoint(redteam.players, RIGHT_SIDE),
            FadeIn(teamLabel),
        )
        self.wait(1)
        self.play(FadeOut(teamLabel))
        self.wait()
        currentPlayer = blueteam.players[0]
        offsetDirection = np.cross(currentPlayer.direction, Z_AXIS) + currentPlayer.direction
        diskPosition = currentPlayer.get_position() + offsetDirection*0.5*currentPlayer.radius
        disk = FrisbeeDisk(point=diskPosition)
        self.play(
            FadeIn(disk),
            FadeIn(diskLabel)
        )
        self.wait()
        self.play(
            FadeOut(diskLabel),
            )
        self.wait(5)
        