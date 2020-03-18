from manimlib.constants import *
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.mobject.geometry import *
from my_projects.frisbee.frisbeeConstants import *
from my_projects.frisbee.frisbeePlayer import FrisbeePlayer

class FrisbeeTeam(VMobject):

    def __init__(self,direction,mode,nPlayers=7,scale=FRISBEE_DEFAULT_SCALE, **kwargs):
        VMobject.__init__(self, **kwargs)
        self.scale = scale
        self.direction = direction
        self.mode = mode
        self.formation = "START"
        playerslist = [0]*nPlayers
        for iPlayer in range(nPlayers):
            relativePositionOfPlayer = (iPlayer+1)*PITCH_WIDTH_RATIO/(nPlayers+1) - SIDE_LINE_POSITION
            positionOfPlayer = -direction*ENDZONE_MID*self.scale+np.cross(-direction, Z_AXIS)*relativePositionOfPlayer *self.scale
            playerslist[iPlayer] = FrisbeePlayer(self.direction, self.mode, self.formation, role=str(iPlayer),point = positionOfPlayer, **kwargs)
        self.players = VGroup(*playerslist)
    