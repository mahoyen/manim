from my_projects.frisbee.imports import *
from manimlib.imports import *

class MovementTest(Scene):

    def construct(self):
        frisbeePitch = FrisbeePitch()
        redTeam = FrisbeeTeam(LEFT, "offense", color=RED)
        blueTeam = FrisbeeTeam(RIGHT, "defense", color=BLUE)

        self.add(
            frisbeePitch.pitch,
        )
        self.play(
            FadeInFromPoint(blueTeam.players, LEFT_SIDE),
            FadeInFromPoint(redTeam.players, RIGHT_SIDE),
        )
        self.wait()

        redTeam.vstack_formation(45, BRICK_MARK_POSITION*-redTeam.direction*FRISBEE_DEFAULT_SCALE)
       
        self.play(
            
        )
        self.wait(5)