h_author__ = 'Robert Schofield'

import pickle
from GameDice import *

### Character Functions ###`

def getadds(st, dx, lk):
    plusadds = (max(st-12,0)+max(dx-12,0)+max(lk-12,0))
    negadds = (max(9-st,0)+max(9-dx,0)+max(9-lk,0))
    adds = plusadds - negadds
    return adds

def savechar(Character):
    file = open("MyTT-Character", "wb")
    pickle.dump(Character, file)
    file.close()

def show(Character):
    attr_tuple = ("name","words","race","level","AP","gold","st","dx","iq","lk","co","ch","adds","weapon","wdice","wadds","armor","armortakes","items")
    for attr in attr_tuple:
        print((attr + ": " + str(getattr(Character, attr))))


#def loadchar():
#    global MyCharacter
#    file = open("MyTT-Character", "rb")
#    print(pickle.load(file))
#    return pickle.load(file)
#    print(MyCharacter)
#    file.close()
