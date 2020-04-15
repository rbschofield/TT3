__author__ = 'Robert Schofield'

import random, pickle
from GameDice import *
from TTChars import *

##### Initialization #####
# Initialize character:

global MyCharacter
MyCharacter = TTChars.Hero(12,12,12,12,12,12)

# Load dungeon elements:

global dungeonarray
dungeonarray = []
file = open( "TTDungeon.txt", "r" )
for line in file:
    if line.startswith("#"):
        pass
    else:
        dungeonarray.append(line)
file.close()


##### Character Menu #####

CharMenuDict = {"1":"TTChars.char", "2":"TTChars.showchar", "3":"TTChars.edit", "4":"TTChars.saveme", "5":"TTChars.loadme", "6":"TTChars.race", "m":"menu"}


def charmenu():
    while True:
        print()
        print ("1) Create Character")
        print ("2) Show Character")
        print ("3) Edit Character")
        print ("4) Save Character")
        print ("5) Load Character")
        print ("6) Assign Race (Dwarf, Elf, Hobbit)")
        print()
        print ("m) Main Menu")

        try:
            choice = str(input ("Choice? >> "))
        except ValueError:
            print ("Invalid choice")

        if choice.lower() == "m":
            break

        print(CharMenuDict[choice])

        try:
            eval(CharMenuDict[choice])()
        except Exception as e:
            print(("Error - Char Menu: "+str(e)))


##### Main Functions #####

def monster():
    global Monster
    global mr

    MonsterList = [["Orc",10], ["Skeleton",15], ["Goblin",20], ["Ghoul",28], ["Ogre",29], ["Vampire",30], ["Flame Demon",35], ["Dragon",50]]
    roll = int(random.random()*len(MonsterList))

    Monster = MonsterList[roll][0]
    mr = MonsterList[roll][1]

    print(Monster)
    print(mr)

def treasure():
    TreasureDict = {1:["Gem",15], 2:["Jewels",25], 3:["Gold",40], 4:["Amulet",75]}
    roll = d4()
    print(("Treasure: " + TreasureDict[roll][0]))
    print(("Value: " + str(TreasureDict[roll][1])))
    print(("\nYou get " + str(TreasureDict[roll][1]) + " Adventure Points!"))
    MyCharacter.AP = MyCharacter.AP + TreasureDict[roll][1]

def dungeon():
#    print dungeonarray
    randelement = int(random.random()*len(dungeonarray))
#    print dungeonarray[randelement]
    parseline = dungeonarray[randelement].split("*")
    for piece in parseline:
        if piece == "10xd6":
            print((10*d6()), end=' ')
        elif piece == "1d4":
            print((d4()), end=' ')
        else:
            print((piece), end=' ')

def combat():
    global mr
    global MyCharacter
    currentcon = MyCharacter.co
    startmr = mr
    print((MyCharacter.name + " with " + MyCharacter.weapon + "\n  vs"))
    print((Monster + ", MR: " + str(mr) + "\n--Fight!--"))
    while mr > 0:
        MyRoll = xd6(MyCharacter.wdice) + MyCharacter.wadds + MyCharacter.adds
        MRroll = xd6(int(mr/10)+1) + (int(mr/2))
        print((MyCharacter.name + ": "+str(MyRoll)))
        print((Monster + ": "+str(MRroll)))
        if MyRoll >= MRroll:
            mr = mr - (MyRoll - MRroll)
            print((Monster + " now: "+str(mr) + "\n----------"))
        else:
            currentcon = currentcon - max((MRroll - MyRoll) - MyCharacter.armortakes, 0)
            print((MyCharacter.name+" Constitution: "+str(currentcon) + "\n----------"))
            if currentcon <= 0:
                print("You died!")
                break
    if currentcon > 0:
        print((MyCharacter.name + " Constitution: "+str(currentcon)))
        print((Monster + " died!"))
        print(("\nYou get " + str(startmr) + " Adventure Points!"))
        MyCharacter.AP = MyCharacter.AP + startmr


def test():
    print ("\nTest Function:")

    for item in vars(MyCharacter):
        print((item, getattr(MyCharacter, item)))

#    for item in MyCharacter.__dict__:
#        print(item,":",MyCharacter.__dict__[item])

##### End Main Functions #####
##### Main Menu #####

MenuDict = {"1":"charmenu", "2":"monster", "3":"dungeon", "4":"treasure", "5":"combat", "9":"test", "x":"done"}

def Menu():
    print()
    print ("1) Character Menu")
    print()
    print ("2) Random Monster")
    print ("3) Dungeon Element")
    print ("4) Random Treasure")
    print ("5) Combat! [current Character vs Monster]")
    print()
    print ("9-test")
    print ("x) EXIT")

    choice = input ("Choice?  >> ")
    return str(choice)

##### Main #####

def Main():
    while True:
        choice = Menu()
        if choice.lower() == "x":
            break
        try:
            eval(MenuDict[choice])()
        except Exception as e:
            print("Error - Main: "+str(e))

if __name__ == "__main__":
    Main()