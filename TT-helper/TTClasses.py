__author__ = 'Robert Schofield'

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

#    def makedwarf(self, st, co, ch):
#        self.st = st * 2
#        self.co = co * 2
#        self.ch = int(round((ch * 2) / 3))
#        return self.st, self.co, self.ch

#    def makeelf(self, dx, iq, co, ch):
#        self.st = (dx * 3) / 2
#        self.iq = (iq * 3) / 2
#        self.co = (co * 2) / 3
#        self.ch = ch * 2
#        return self.dx, self.iq, self.co, self.ch

#    def makehobbit(self, st, dx, co):
#        self.st = st / 2
#        self.dx = (dx *3) / 2
#        self.co = co * 2
#        return self.st, self.dx, self.co


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
        self.ch = int(round((Hero.ch * 2) / 3))
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
        self.dx = int(round((Hero.dx * 3) / 2))
        self.iq = int(round((Hero.iq * 3) / 2))
        self.lk = Hero.lk
        self.co = int(round((Hero.co * 2) / 3))
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
        self.dx = int(round((Hero.dx * 3) / 2))
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


#MyCharacter = Hero(12,12,12,12,12,12)
#print(MyCharacter)
