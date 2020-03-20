from manimlib.mobject.geometry import Dot
from my_projects.frisbee.frisbeeConstants import *
from my_projects.frisbee.frisbeeUtils import calculate_relative_mark_position_vstack

class FrisbeePlayer(Dot):

    def __init__(self, direction, mode, formation, role, scale=FRISBEE_DEFAULT_SCALE, force=FLICK, **kwargs):
        Dot.__init__(self,**kwargs)
        self.direction = direction
        self.mode = mode
        self.formation = formation
        self.role = role
        self.force = force
        self.scale = scale
           

    def move_to(self, point):
        self.move_arc_center_to(point)

    
    def get_position(self):
        return self.get_center()
    
    def mark_player(self, player):
        player_pos = player.get_position()
        player_role = player.role
        rel_mark_pos = calculate_relative_mark_position_vstack(player_role, self.force, self.direction)
        self.destination = player_pos + self.scale*rel_mark_pos
        return self.destination

