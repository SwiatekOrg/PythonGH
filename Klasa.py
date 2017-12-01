class Player():
    def __init__(self):
        self._nickname = "Guest"
        self._gold = 100
    def chgnick(self, newnick):
        self._nickname = newnick
    def showNick(self):
        print("Twoj to " + self._nickname)
    def addGold(self ,gold):
        self._gold += gold

gracz = Player()
gracz.showNick()
gracz.chgnick("Kylo")
gracz.showNick()

class Ekwipunek():
    def __init__(self):
        self.equipmnent = {'sword': 1, 'bow':1 ,'arrow':20, 'knife':2}

    def showEq(self):
        print(self.equipmnent)

    def addEq(self,name, count):
        self.name = {}
        self.count = {}
        if name in self.equipmnent.keys():
            self.equipmnent[name] += count
        else:
            self.equipmnent[name] = count

eq1 = Ekwipunek()
eq1.showEq()
eq1.addEq("cos", 5)
eq1.showEq()

class Position():
    def __init__(self):
        self._x = 50
        self._y = 50
        self._mapName = "Krakow"
    def move(self,x,y):
        self.x = int(x)
        self.y = int(y)
        self._x += self.x
        self._y += self.y
    def setPosition(self,x2,y3):
        self.x2 = int(x2)
        self.y3 = int(y3)
        self._x = x2
        self._y = y3
    def changeMap(self, mapname):
        self._mapName = mapname

    def show(self):
        print(self._x,self._y,self._mapName)

pozycja = Position()
pozycja.move(6,3)
pozycja.show()
pozycja.changeMap("Miechow")
pozycja.setPosition(1,1)
pozycja.show()