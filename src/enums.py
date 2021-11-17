from enum import IntEnum

class Hashes(IntEnum):
    SKILL_W_IS_CASTING = 2345
    SKILL_W_IS_UP = 9378
    SKILL_W_IS_ATTACHED = 9953
    RED_SIDE_BLUE_CHECK = 848
    RED_SIDE_RED_CHECK = 215
    BLUE_SIDE_BLUE_CHECK = 2051
    BLUE_SIDE_RED_CHECK = 133
    EMPTY_PIXEL_BAR = 3
    EMPTY_PIXEL_BAR_ALLY = 20
    
    LevelBoxHashDict = {
    3494: 1,
    5626: 2, 
    5302: 3, 
    5303: 4, 
    6306: 5,
    7416: 6,
    4093: 7,
    7067: 8,
    6970: 9,
    7203: 10, 
    3914: 11,
    6793: 12,
    6926: 13, 
    6088: 14, 
    7421: 15, 
    7920: 16,
    4856: 17, 
    7523: 18
    }

class Buffers(IntEnum):
    BUFFER_ACTION_DELAY = .5
    BUFFER_MOUSE_MOVEMENT = .02
    BUFFER_SKILL_LEVELING = .03
    BUFFER_ABILITY_CASTED = .03
    BUFFER_WINDOW_FOCUSED = .02
    
