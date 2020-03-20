from my_projects.frisbee.imports import *
from my_projects.my_utils.imports import *
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

        redTeam.vstack_formation(0, BRICK_MARK_POSITION*-redTeam.direction*FRISBEE_DEFAULT_SCALE)
       
        self.play(
            *[MoveToPoint(player.destination, player) for player in redTeam.players],
        )
        
        blueTeam.players[0].mark_player(redTeam.players[0])
        self.play(
            MoveToPoint(blueTeam.players[0].destination, blueTeam.players[0])
        )
        self.wait(5)