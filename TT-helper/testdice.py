from GameDice import *
from print_slow import *

d4roll = d4()
print_slow("1d4: " + str(d4roll))

print("1d6: " + str(d6()))

print("5d6: " + str(xd6(5)))

print("4d6: " + str(roll("4d6")))
