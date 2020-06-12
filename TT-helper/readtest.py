def ReadList(Listname = "MonsterList", Readfile = "TTMonsters.txt"):
    print(Listname)
    ReadList.Listname = []
    file = open(Readfile,"r")
    for line in file:
        if line.startswith("#"):
            pass
        else:
            ReadList.Listname.append(line.split(","))
    file.close()
    print(ReadList.Listname)
    return(ReadList.Listname)

MonsterList = ReadList()
print(MonsterList)
print()
TreasureList = ReadList("TreasureList", "TTTreasure.txt")
print(TreasureList)
