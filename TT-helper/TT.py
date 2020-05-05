__author__ = 'Robert Schofield'

#import random, pickle
import random
from GameDice import *
from TTClasses import *
from TTChars import *
from print_slow import *

##### Initialization #####
# Initialize character:

global MyCharacter
MyCharacter = Hero(12,12,12,12,12,12)

# Load dungeon elements:

global dungeonarray
dungeonarray = []
file = open("TTDungeon.txt","r")
for line in file:
    if line.startswith("#"):
        pass
    else:
        dungeonarray.append(line)
file.close()

# Load monster list:

global MonsterList
MonsterList = []
file = open("TTMonsters.txt","r")
for line in file:
    if line.startswith("#"):
        pass
    else:
        MonsterList.append(line.split(","))
file.close()

##### Initialization Complete #####
banner = open("banner.ascii","r")

for line in banner:
    print(line, end='')
banner.close()
print()
print_slow("Game Master Helper, or Solo Play................. GO!")

##### Character Functions #####


def char():
    MyCharacter.race = "Human"
    keep = "n"
    while keep != "y":
        MyCharacter.st = xd6(3)
        MyCharacter.dx = xd6(3)
        MyCharacter.iq = xd6(3)
        MyCharacter.lk = xd6(3)
        MyCharacter.co = xd6(3)
        MyCharacter.ch = xd6(3)
        MyCharacter.gold = xd6(3)*10
        print(("Strength:     "+str(MyCharacter.st)))
        print(("Dexterity:    "+str(MyCharacter.dx)))
        print(("Intelligence: "+str(MyCharacter.iq)))
        print(("Luck:         "+str(MyCharacter.lk)))
        print(("Constitution: "+str(MyCharacter.co)))
        print(("Charisma:     "+str(MyCharacter.ch)))
        print(("Gold: "+str(MyCharacter.gold)))
        MyCharacter.adds = getadds(MyCharacter.st, MyCharacter.dx, MyCharacter.lk)
        print(("\nAdds: "+str(MyCharacter.adds)))
        keep = input("Keep? (y)es/(n)o  >")

    name = input ("Name Me >> ")
    MyCharacter.name = str(name)
    words = input ("Favorite Saying >> ")
    MyCharacter.words = str(words)
    weapon = input ("My Weapon >> ")
    MyCharacter.weapon = str(weapon)
    try:
        MyCharacter.wdice = int(input ("Weapon Dice >> "))
    except ValueError:
        print ("Need a number.  Using 0")
        MyCharacter.wdice = 0
    try:
        MyCharacter.wadds = int(input ("Weapon Adds >> "))
    except ValueError:
        print ("Need a number.  Using 0")
        MyCharacter.wadds = 0
    armor = input ("Armor >> ")
    MyCharacter.armor = str(armor)
    try:
        MyCharacter.armortakes = int(input ("Armor Absorbs >> "))
    except ValueError:
        print ("Need a number.  Using 0")
        MyCharacter.armortakes = 0
    items = input ("List Any Items >> ")
    MyCharacter.items = str(items)
    MyCharacter.AP = 0

    print(("\n"+MyCharacter.name+" is Born!"))
    print((MyCharacter.words))

    print(Hero.saywords(MyCharacter))


def showchar():
    show(MyCharacter)

def saveme():
    savechar(MyCharacter)
    
#def loadme():
#    MyCharacter = loadchar()

def loadme():
    global MyCharacter
    file = open("MyTT-Character", "rb")
    MyCharacter = pickle.load(file)
    file.close()


def edit():
    global MyCharacter
    for item in MyCharacter.__dict__:
        print((item, MyCharacter.__dict__[item]))
        change = str(input('Change? ("y" to change) >>'))
        if change.lower() == "y":
            newvalue = input("New value? >>")
            try:
                MyCharacter.__dict__[item] = newvalue
            except:
                print("Bad value.  Not changed.")
                pass
#### strings to integers
    MyCharacter.st = int(MyCharacter.st)
    MyCharacter.dx = int(MyCharacter.dx)
    MyCharacter.iq = int(MyCharacter.iq)
    MyCharacter.lk = int(MyCharacter.lk)
    MyCharacter.co = int(MyCharacter.co)
    MyCharacter.ch = int(MyCharacter.ch)
    MyCharacter.AP = int(MyCharacter.AP)
    MyCharacter.wdice = int(MyCharacter.wdice)
    MyCharacter.wadds = int(MyCharacter.wadds)
    MyCharacter.armortakes = int(MyCharacter.armortakes)

    print("Recalculating adds")
    MyCharacter.adds = getadds(MyCharacter.st, MyCharacter.dx, MyCharacter.lk)
    print(("Adds: ") + str(MyCharacter.adds))


def race():
    global MyCharacter
    if MyCharacter.race != "Human":
        print("Race already assigned.")
        return
    if MyCharacter.AP > 0:
        print("New characters only.")
        return
    print("Assign character race, one time only.")
    print("Select Race:")
    print()
    print("d) Dwarf  - St x 2, Co x 2, Ch x 2/3")
    print("e) Elf    - Dx x 3/2, Iq x 3/2, Co x 2/3, Ch x 2")
    print("h) Hobbit - St x 1/2, Dx x 3/2, Co x 2")
    print("x) Don't change - Exit.")

    try:
        choice = str(input ("Choice? >> "))
    except ValueError:
        print ("Invalid choice.  Nothing changed.")
        return
    else:
        if choice.lower() == "x":
            return
        elif choice.lower() == "d":
            print("Making Dwarf")
            MyCharacter = Dwarf(MyCharacter)
            Dwarf(MyCharacter).dwarfsays()
        elif choice.lower() == "e":
            print("Making Elf")
            MyCharacter = Elf(MyCharacter)
            Elf(MyCharacter).elfsays()
        elif choice.lower() == "h":
            print("Making Hobbit")
            MyCharacter = Hobbit(MyCharacter)
            Hobbit(MyCharacter).hobbitsays()
        else:
            return
    finally:
        MyCharacter.adds = getadds(MyCharacter.st, MyCharacter.dx, MyCharacter.lk)

#        (newst, newco, newch) = Hero.makedwarf(MyCharacter, MyCharacter.st, MyCharacter.co, MyCharacter.ch)


##### End Character Functions #####
##### Character Menu #####

CharMenuDict = {"1":"char", "2":"showchar", "3":"edit", "4":"saveme", "5":"loadme", "6":"race", "m":"menu"}

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

##        print(CharMenuDict[choice])

        try:
            eval(CharMenuDict[choice])()
        except Exception as e:
            print(("Error - Char Menu: "+str(e)))


##### Main Functions #####

def monster():
    global Monster
    global mr

#    MonsterList = [["Orc",10], ["Skeleton",15], ["Goblin",20], ["Ghoul",28], ["Ogre",29], ["Vampire",30], ["Flame Demon",35], ["Dragon",50]]
    roll = int(random.random()*len(MonsterList))

    Monster = MonsterList[roll][0]
    mr = int(MonsterList[roll][1].strip())

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
    print_slow ("\nTest Function:")

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
