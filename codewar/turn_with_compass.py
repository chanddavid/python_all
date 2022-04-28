

from cv2 import find4QuadCornerSubpix


direction=['S','SW','W','NW','N','NE','E','SE']
turns='45'
def direction(facing, turn):
    # your smart code here
    turns=turns//45
    start_ind=direction.index(facing)
    end_ind=(start_ind+turns)%len(direction)
    return direction[end_ind]

