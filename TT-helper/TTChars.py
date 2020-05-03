__author__ = 'Robert Schofield'

from GameDice import *

### Character Functions ###`

def getadds(st, dx, lk):
    plusadds = (max(st-12,0)+max(dx-12,0)+max(lk-12,0))
    negadds = (max(9-st,0)+max(9-dx,0)+max(9-lk,0))
    adds = plusadds - negadds
    return adds

