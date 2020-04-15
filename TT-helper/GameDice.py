import random 

# Dice defs:

def d4():
    return (random.randint(1,4))

def d6():
    return int(random.random()*6)+1


def xd6(x):
    return sum(random.randint(1,6) for _ in range(x))

# parse roll(xdy)
# i.e. roll(3d6), roll(4d10)
#
def roll(r_elem):
    x = int(r_elem.split("d")[0])
    y = int(r_elem.split("d")[1])
    total = 0
    for i in range(0,x):
        total += int(random.random()*y)+1
#    print((str(total)), end=' ')
    return total
