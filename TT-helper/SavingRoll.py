__author__ = 'Robert Schofield'

from TTClasses import *
from TTChars import *
import random

Character = Hero(12,13,14,15,16,17)

############################################
# for interactive saves- displayed to player

def save(char = Character):
    show(char)
    print()
    savetype = input ("Attribute? (st, dx, iq, lk, co, ch) >> ")
    try:
        print(eval("char."+savetype))
        saveattr = eval("char."+savetype)
    except Exception as e:
        print(("Error - SavingRoll: "+str(e)))
    savelevel = input ("Level of Save to attempt? (1,2,3,etc.) >> ")
    try:
        savelevel = int(savelevel)
        print(savelevel)
    except Exception as e:
        print("Invalid")
    print()
    print("Attempting a L"+str(savelevel)+" Save against "+savetype+" ("+str(+saveattr)+")")
    target = (savelevel*5)+15
    print("Target: "+str(target))
    die1 = 0
    die2 = 0
    rollnum = 0
    rolltotal = saveattr
    while die1 == die2:
        rollnum = rollnum + 1
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        rolltotal = rolltotal + (die1 + die2)
        print("Roll number "+str(rollnum)+"  "+str(die1)+"+"+str(die2)+"="+str(die1+die2)+"  Total: "+str(rolltotal))
    if rolltotal >= target:
        print("Success!!")
    else:
        print("You failed the Save.")


########### Saving roll ###########
# for internal, non-displayed saves

def save_roll(level, attribute):
    target = (5*level)+15
    r1 = 0; r2 = 0; total = 0
    while r1 == r2:
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        total = total+(r1+r2)
    roll = total + attribute
#    print((total, attribute, roll))
    if roll >= target:
        return True
    else:
        return False



if __name__ == "__main__":
    save()
