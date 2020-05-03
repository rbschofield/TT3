import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

dungeonarray = []
file = open( "TTDungeon.txt", "r" )
for line in file:
    if line.startswith("#"):
        pass
    else:
        dungeonarray.append(line)
file.close()
print(dungeonarray)

def dungeon():
#    print dungeonarray
    randelement = int(random.random()*len(dungeonarray))
    return dungeonarray[randelement]
#    parseline = dungeonarray[randelement].split("*")
#    for piece in parseline:
#        if piece == "10xd6":
#            print((10*d6()), end=' ')
#        elif piece == "1d4":
#            print((d4()), end=' ')
#        else:
#            print((piece), end=' ')

@app.route('/dungeon/rnd/element')
def get_element():
    return dungeon()

if __name__ == '__main__':
    app.run(debug=True)
