YARDS_PITCH_WIDTH= 40
YARDS_PITCH_HEIGHT = 120
YARDS_ENDZONE_DEPTH = 25
YARDS_BRICK_MARK = 45

FRISBEE_DEFAULT_SCALE = 14

PITCH_WIDTH_RATIO = YARDS_PITCH_WIDTH/YARDS_PITCH_HEIGHT
PITCH_HEIGHT_RATIO = YARDS_PITCH_HEIGHT/YARDS_PITCH_HEIGHT
ENDZONE_DEPTH_RATIO = YARDS_ENDZONE_DEPTH/YARDS_PITCH_HEIGHT
BRICK_MARK_RATIO = YARDS_BRICK_MARK/YARDS_PITCH_HEIGHT


BRICK_MARK_POSITION = (PITCH_HEIGHT_RATIO/2-BRICK_MARK_RATIO)
ENDZONE_BACK = PITCH_HEIGHT_RATIO/2
ENDZONE_FRONT = PITCH_HEIGHT_RATIO/2 - ENDZONE_DEPTH_RATIO
ENDZONE_MID = PITCH_HEIGHT_RATIO/2 - ENDZONE_DEPTH_RATIO/2
SIDE_LINE_POSITION = PITCH_WIDTH_RATIO/2

# Position Constants
HANDLER = "handler"
DUMP = "dump"
STACK_SETTER = "stack_setter"
CUTTER_4 = "fourth_cut"
CUTTER_3 = "third_cut"
CUTTER_2 = "second_cut"
CUTTER_1 = "first_cut"

# Vstack defense constatnts
HANDLER_MARK_DISTANCE_VSTACK = 0.01
DUMP_MARK_DISTANCE_VSTACK = 5*HANDLER_MARK_DISTANCE_VSTACK
DUMP_MARK_ANGLE_VSTACK = 0.3 #RADIANS
CUTTER_MARK_DISTANCE_VSTACK = HANDLER_MARK_DISTANCE_VSTACK
FLICK = "flick"