import random

# Read file into a dictionary

AdventureArray = {}

f = open("RPGadventure.txt", "r")
for line in f:
    if line.startswith("#"):
        pass
    else:
        inline = line.strip().split(":")
        AdventureArray[inline[0]] = inline[1]

location = "99"

# Dice defs:

def xd6(x):
    total = 0
    for i in range(0,x):
        total += d6()
    return total

# parse xdy
def parse_xdy(r_elem):
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

# Parse "Event"
# Event: State (is Event Pending, or Done?)  True or False (T|F)
#   If Pending, a Yes / No question will be asked
#   A Yes answer will set the state to Done, then go to a location
#   If No, will leave the State the same, and will then go to a location
#
# !xx:State; Pending text; Yes Loc; No Loc; Done text; Done Loc
#
#   Pending text and Done text can include random numbers
#     (e.g. some text including a randome number = *%4d6* and more text.)
#
# !99:T;This gemstone is worth *%1d20*gp. Do you take it?;>99;>99;There is an empty socket where a gemstone once rested;>99

def parse_event(EventArray):
    event_element = EventArray.split(";")
    if event_element[0] == "T":
        print((event_element[1]))  ### need to add random parser
        choice = "None"
        while choice == "None":
            print("(Y)es, or (N)o?")
            choice = input(">> ")
            if choice.upper() != "Y" and choice.upper() != "N":
                print("Invalid choice.")
                choice = "None"
        if choice.upper() == "Y":
            return "SetFalse", event_element[2]
        else: # Event True, answered No
            return "NoChange", event_element[3]
    else:  # Event False
        print((event_element[4] + "\n"))  ### need to add random parser
        return "NoChange", found_element[5]


# Parse input choice
#   >x go to that Location
#   !x event occurred (found an item, treasure, encountered  monster...)
#
def parse_choice(choice):
    global AdventureArray
#    print("parsing: " + choice)
    if choice[0] == ">":
        location = choice[1:]
#        print("location = ")+location
        return location
    elif choice[0] == "!":
#        print("process = ")+DungeonArray[choice]
        statechange, location = parse_event(AdventureArray[choice])
#        print(statechange, location)
        if statechange == "SetFalse":
#            print(DungeonArray[choice])
#            print(DungeonArray[choice].split(";")[0])
            AdventureArray[choice] = "F"+AdventureArray[choice][1:]
#            print(DungeonArray[choice])
        return location[1:]
        

# Parse a Location
def adventure(location):
#    randlocation = int(random.random()*len(AdventureArray))
#    print AdventureArray[randlocation]
    choicelist = [] #; choice = 0
    controlchar = (">","!")
#    print(AdventureArray[location])
    parseloc = AdventureArray[location].split("*")
    for element in parseloc:
        if element[0] in controlchar:
            choicelist.append(element)
###        elif element[0] == "%":
###            parserand(element.split("%")[1])
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
    adventure(location)

#    srl = int(raw_input("level: "))
#    sra = int(raw_input("attribute: "))
#    print(saveroll(srl, sra))


if __name__ == "__main__":
    adventure(location)
