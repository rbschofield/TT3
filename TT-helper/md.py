import random

MonsterList = []
file = open("TTMonsters.txt", "r") 
for line in file:
    if line.startswith("#"):
        pass
    else:
        MonsterList.append(line.split(","))
file.close()

roll = int(random.random()*len(MonsterList))

Monster = MonsterList[roll][0]
mr = int(MonsterList[roll][1].strip())

print(Monster)
print(mr)
#print(mr+10)
