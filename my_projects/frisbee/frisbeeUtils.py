import numpy as np
from manimlib.constants import Z_AXIS, ORIGIN
from my_projects.frisbee.frisbeeConstants import *

def calculate_relative_mark_position_vstack(playerRole, markForce, markDirection):
    forceSide = 1 if markForce == FLICK else -1
    if playerRole == HANDLER:
        return HANDLER_MARK_DISTANCE_VSTACK*(forceSide*np.cross(markDirection, Z_AXIS)-markDirection)
    elif playerRole == DUMP:
        return DUMP_MARK_DISTANCE_VSTACK*(np.sin(DUMP_MARK_ANGLE_VSTACK)*forceSide*np.cross(markDirection, Z_AXIS)-markDirection)
    else:
        return CUTTER_MARK_DISTANCE_VSTACK*(-forceSide*np.cross(markDirection, Z_AXIS)+markDirection)
    return ORIGIN