__author__ = 'Robert Schofield'

import GameDice

##### Character Functions #####

def getadds(st, dx, lk):
    plusadds = (max(st-12,0)+max(dx-12,0)+max(lk-12,0))
    negadds = (max(9-st,0)+max(9-dx,0)+max(9-lk,0))
    adds = plusadds - negadds
    return adds

def char():
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

    print(("\n"+MyCharacter.name+" is Born!"))
    print((MyCharacter.words))

#    print(Hero.saywords(MyCharacter))


def showchar():
    attr_tuple = ("name","words","race","level","AP","gold","st","dx","iq","lk","co","ch","adds","weapon","wdice","wadds","armor","armortakes","items")
    for attr in attr_tuple:
        print((attr + ": " + str(getattr(MyCharacter, attr))))


def saveme():
    file = open("MyTT-Character", "wb")
    pickle.dump(MyCharacter, file)
    file.close()


def loadme():
    global MyCharacter
    file = open("MyTT-Character", "rb")
    MyCharacter = pickle.load(file)
    file.close()


def edit():
    for item in MyCharacter.__dict__:
        print((item, MyCharacter.__dict__[item]))
        try:
            change = str(input("Change? >>"))
        except:
            print("(y or n)")
        if change.lower() == "y":
            newvalue = input("New value? >>")
            try:
                MyCharacter.__dict__[item] = newvalue
            except:
                print("Bad value.  Not changed.")
                pass
#### fix integers
    MyCharacter.st = int(MyCharacter.st)
    MyCharacter.dx = int(MyCharacter.dx)
    MyCharacter.iq = int(MyCharacter.iq)
    MyCharacter.lk = int(MyCharacter.lk)
    MyCharacter.co = int(MyCharacter.co)
    MyCharacter.ch = int(MyCharacter.ch)
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


##### End Character Functions #####
##### Begin Race Conbversions #####

class Hero:
    def __init__(self,st,dx,iq,lk,co,ch):
        self.name = "Hero"
        self.words = "I'm a nobody"
        self.race = "Human"
        self.level = 1
        self.AP = 0
        self.gold = 0
        self.st = st
        self.dx = dx
        self.iq = iq
        self.lk = lk
        self.co = co
        self.ch = ch
        self.adds = 0
        self.weapon = "none"
        self.wdice = 0
        self.wadds = 0
        self.armor = "none"
        self.armortakes = 0
        self.items = "none"

    def saywords(self):
        print((self.name, "says: ",self.words))

    def makedwarf(self, st, co, ch):
        self.st = st * 2
        self.co = co * 2
        self.ch = (ch * 2) / 3
        return self.st, self.co, self.ch

    def makeelf(self, dx, iq, co, ch):
        self.st = (dx * 3) / 2
        self.iq = (iq * 3) / 2
        self.co = (co * 2) / 3
        self.ch = ch * 2
        return self.dx, self.iq, self.co, self.ch

    def makehobbit(self, st, dx, co):
        self.st = st / 2
        self.dx = (dx *3) / 2
        self.co = co * 2
        return self.st, self.dx, self.co


class Dwarf(Hero):
    def __init__(self, Hero):
        self.name = Hero.name
        self.words = Hero.words
        self.race = "Dwarf"
        self.level = Hero.level
        self.AP = Hero.AP
        self.gold = Hero.gold
        self.st = Hero.st * 2
        self.dx = Hero.dx
        self.iq = Hero.iq
        self.lk = Hero.lk
        self.co = Hero.co * 2
        self.ch = (Hero.ch * 2) / 3
        self.adds = Hero.adds
        self.weapon = Hero.weapon
        self.wdice = Hero.wdice
        self.wadds = Hero.wadds
        self.armor = Hero.armor
        self.armortakes = Hero.armortakes
        self.items = Hero.items

    def dwarfsays(self):
        print("I'm a Dwarf!")


class Elf(Hero):
    def __init__(self, Hero):
        self.name = Hero.name
        self.words = Hero.words
        self.race = "Elf"
        self.level = Hero.level
        self.AP = Hero.AP
        self.gold = Hero.gold
        self.st = Hero.st
        self.dx = (Hero.dx * 3) /2
        self.iq = (Hero.iq * 3) / 2
        self.lk = Hero.lk
        self.co = (Hero.co * 2) / 3
        self.ch = Hero.ch * 2
        self.adds = Hero.adds
        self.weapon = Hero.weapon
        self.wdice = Hero.wdice
        self.wadds = Hero.wadds
        self.armor = Hero.armor
        self.armortakes = Hero.armortakes
        self.items = Hero.items

    def elfsays(self):
        print("I like the woods")


class Hobbit(Hero):
    def __init__(self, Hero):
        self.name = Hero.name
        self.words = Hero.words
        self.race = "Hobbit"
        self.level = Hero.level
        self.AP = Hero.AP
        self.gold = Hero.gold
        self.st = Hero.st / 2
        self.dx = (Hero.dx * 3) / 2
        self.iq = Hero.iq
        self.lk = Hero.lk
        self.co = Hero.co * 2
        self.ch = Hero.ch
        self.adds = Hero.adds
        self.weapon = Hero.weapon
        self.wdice = Hero.wdice
        self.wadds = Hero.wadds
        self.armor = Hero.armor
        self.armortakes = Hero.armortakes
        self.items = Hero.items

    def hobbitsays(self):
        print("How's the weather up there!")
