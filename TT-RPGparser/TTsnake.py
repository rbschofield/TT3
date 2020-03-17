import random

# Read file into a dictionary

DungeonArray = {}

f = open("TTsnake.txt", "r")
for line in f:
    if line.startswith("#"):
        pass
    else:
        inline = line.strip().split(":")
#        print(inline[0],inline[1])
        DungeonArray[inline[0]] = inline[1]

#print(DungeonArray)
location = "99"

# Dice defs:

def d4():
    return int(random.random()*4)+1

def d6():
    return int(random.random()*6)+1

def xd6(x):
    total = 0
    for i in range(0,x):
        total += d6()
    return total

# parse xdy
def parserand(r_elem):
    x = int(r_elem.split("d")[0])
    y = int(r_elem.split("d")[1])
    total = 0
    for i in range(0,x):
        total += int(random.random()*y)+1
    print((str(total)), end=' ')
    return total

# Saving roll
def saveroll(level, attribute):
    target = (5*level)+15
    r1 = 0; r2 = 0; total = 0
    while r1 == r2:
        r1 = d6()
        r2 = d6()
        total = total+(r1+r2)
    roll = total + attribute
    print((total, attribute, roll))
    if roll >= target:
        return True
    else:
        return False

# Parse "Found Something"
# Found Something: State (is it here now or not?) is Available or Gone
#   If Available, a Yes / No question will be asked
#   A Yes answer will set the state to Gone, then go to a location
#   If No, will leave the State the same, and will then go to a location
#
# !xx:State; Available text; Gone text; Avail+Yes Loc; Avail+No Loc; Gone Loc
#
# !99:Available;This gemstone is worth 100gp. Do you take it?;There is an empty socket where a gemstone once rested;>99;>99;>99

def parse_found(FoundArray):
    found_element = FoundArray.split(";")
    if found_element[0] == "Available":
        print((found_element[1]))
        choice = "None"
        while choice == "None":
            print("(Y)es, or (N)o?")
            choice = input(">> ")
            if choice.upper() != "Y" and choice.upper() != "N":
                print("Invalid choice.")
                choice = "None"
        if choice.upper() == "Y":
            return "SetNo", found_element[3]
        else: # Available, answered No
            return "NoChange", found_element[4]
    else:  # not Available
        print((found_element[2] + "\n"))
        return "NoChange", found_element[5]


# Parse input choice
#   >x go to that room location
#   !x found something (item, treasure, monster...)
#   ^x parse trap
#   @x try saving roll
#
def parse_choice(choice):
    global DungeonArray
#    print("parsing: " + choice)
    if choice[0] == ">":
        location = choice[1:]
#        print("location = ")+location
        return location
    elif choice[0] == "!":
#        print("process = ")+DungeonArray[choice]
        statechange, location = parse_found(DungeonArray[choice])
#        print(statechange, location)
        if statechange == "SetNo":
#            print(DungeonArray[choice])
#            print(DungeonArray[choice].split(";")[0])
            DungeonArray[choice] = "Gone"+DungeonArray[choice][9:]
#            print(DungeonArray[choice])
        return location[1:]
        

# Parse the Dungeon
def dungeon(location):
#    randlocation = int(random.random()*len(DungeonArray))
#    print DungeonArray[randlocation]
    choicelist = [] #; choice = 0
    controlchar = (">","^","!","@")
#    print(DungeonArray[location])
    parseloc = DungeonArray[location].split("*")
    for element in parseloc:
        if element[0] in controlchar:
            choicelist.append(element)
        elif element[0] == "%":
            parserand(element.split("%")[1])
        else:
            print((element), end=' ')
    print("\r")
    choice = 0
    while choice == 0:
        print("Choose:")
        print(("1 - "+str(len(choicelist))))
        try:
            choice = int(input(">> "))
            if choice < 1 or choice > len(choicelist):
                raise Exception
        except Exception as e:
            print(("Invalid choice: "+str(e)))
            choice = 0
    location = parse_choice(choicelist[choice - 1])
    dungeon(location)

#    srl = int(raw_input("level: "))
#    sra = int(raw_input("attribute: "))
#    print(saveroll(srl, sra))


if __name__ == "__main__":
    dungeon(location)
