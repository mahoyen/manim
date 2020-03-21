from my_projects.frisbee.imports import *
from my_projects.my_utils.imports import *
from manimlib.imports import *

class VStackFormation(Scene):

    def construct(self):
        frisbeePitch = FrisbeePitch()
        redTeam = FrisbeeTeam(LEFT, "offense", color=RED)
        offenseLabel = TextMobject("Offense Team")
        offenseLabel.to_corner(UL)

        blueTeam = FrisbeeTeam(RIGHT, "defense", color=BLUE)
        defenseLabel = TextMobject("Defense Team")
        defenseLabel.to_corner(UR)

        ODLabelVGroup = VGroup(offenseLabel, defenseLabel)

        title = TextMobject("Vertical Stack Formation")
        title.to_edge(UP)
        self.add(
            frisbeePitch.pitch,
        )
        self.play(
            FadeIn(ODLabelVGroup),
            FadeInFromPoint(blueTeam.players, LEFT_SIDE),
            FadeInFromPoint(redTeam.players, RIGHT_SIDE),
        )
        self.wait()

        blueTeam.vstack_formation(0, BRICK_MARK_POSITION*-blueTeam.direction*FRISBEE_DEFAULT_SCALE)
        redTeam.mark_players(blueTeam)
        self.play(
            Write(title, run_time=3),
            *[MoveToPoint(player.destination, player) for player in redTeam.players],
            *[MoveToPoint(player.destination, player) for player in blueTeam.players],
        )
        self.wait(5)