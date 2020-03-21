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
        self.basePoint = -direction*ENDZONE_MID*self.scale
        self.nPlayers = nPlayers
        playerslist = [0]*nPlayers
        pos_list = start_positions(self.basePoint, self.direction, scale=self.scale, nPlayers=nPlayers)
        for iPlayer in range(nPlayers):
            playerslist[iPlayer] = FrisbeePlayer(self.direction, self.mode, self.formation, role=str(iPlayer),point = pos_list[iPlayer], **kwargs)
        self.players = VGroup(*playerslist)

    def start_formation(self, basePoint=None):
        if basePoint is not None:
            self.basePoint = basePoint
        positions = start_positions(self.basePoint, self.direction)
        for player, position in zip(self.players, positions):
            player.destination = position

    def vstack_formation(self,angle=0, basePoint=None):
        if basePoint is not None:
            self.basePoint = basePoint
        roles = [HANDLER, DUMP, STACK_SETTER]
        cutterRolesAvailable = [CUTTER_1, CUTTER_2, CUTTER_3, CUTTER_4]
        nBasicRoles = len(roles)
        for iPlayer in range(self.nPlayers-nBasicRoles):
            roles.insert(nBasicRoles,cutterRolesAvailable[iPlayer])
        positions = vstack_positions(self.basePoint, self.direction,angle=angle, nPlayers=self.nPlayers)
        for player, role, position in zip(self.players, roles, positions):
            player.role = role
            player.destination = position

    def mark_players(self, enemyTeam):
        for teamPlayer, enemyPlayer in zip(self.players, enemyTeam.players):
            teamPlayer.mark_player(enemyPlayer)

def start_positions(basePoint, direction, scale=FRISBEE_DEFAULT_SCALE, nPlayers=7):
    pos_list = []
    for iPlayer in range(nPlayers):
        relativePositionOfPlayer = ((iPlayer+1)*PITCH_WIDTH_RATIO/(nPlayers+1) - SIDE_LINE_POSITION)*scale
        positionOfPlayer = basePoint+np.cross(-direction, Z_AXIS)*relativePositionOfPlayer
        pos_list.append(positionOfPlayer)
    return pos_list

    
def vstack_positions(basePoint, direction, angle=0, distance=0.04, scale=FRISBEE_DEFAULT_SCALE, nPlayers=7):
    rel_handler_pos = -SIDE_LINE_POSITION/2*np.cross(direction, Z_AXIS)
    rel_dump_pos = SIDE_LINE_POSITION/3*-direction
    rel_stack_setter = SIDE_LINE_POSITION/1.4*direction
    rel_stack = [rel_stack_setter]

    # Create rotation matrix for angling the stack
    theta = np.deg2rad(-angle)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [            0,              0, 1] 
    ])

    # Positions for rest of stack
    for iPlayerPos in range(nPlayers-3):    
        rel_stack.append(rel_stack[iPlayerPos] + distance*np.matmul(rotation_matrix,direction))

    all_rel_pos = np.vstack((rel_handler_pos, rel_dump_pos, np.array(rel_stack)))


    all_pos = all_rel_pos*scale + basePoint
    
    # convert from ndarray to list
    pos_list = [pos for pos in all_pos]
    return pos_list