from TTClasses import *
from TTChars import *

Character = Hero(12,13,14,15,16,17)

def save(char = Character):
    show(char)
    print()
    savetype = input ("Attribute? (st, dx, iq, lk, co, ch) >> ")
    try:
        print(eval("char."+savetype))
    except Exception as e:
        print(("Error - SavingRoll: "+str(e)))
    savelevel = input ("Level of Save to attempt? (1,2,3,etc.) >> ")
    try:
        savelevel = int(savelevel)
        print(savelevel)
    except Exception as e:
        print("Invalid")
    print()
    print("Attempting a L"+str(savelevel)+" Save against "+savetype+" ("+str(eval("char."+savetype))+")")
    target = int(savelevel) * 5 + 15
    print("Target: "+str(target))



if __name__ == "__main__":
    save()
