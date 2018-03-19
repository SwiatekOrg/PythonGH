from random import randint

MAP_SIZE =10


class Position():
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def move(self, x):
        if x == "polnoc":
            if self._x == 10 or self._x == 0:
                print ("Nie mozesz wyjsc poza mapę")
            else:
                self._x += 1
        elif x == "poludnie":
            if self._x == 10 or self._x == 0:
                print ("Nie mozesz wyjsc poza mapę")
            else:
                self._x -= 1
        elif x == "wschod":
             if self._y == 10 or self._y == 0:
                 print ("Nie mozesz wyjsc poza mapę")
             else:
                 self._y += 1
        elif x == "zachod":
             if self._y == 10 or self._y == 0:
                 print ("Nie mozesz wyjsc poza mapę")
             else:
                 self._y -= 1
        else:
            print("Podaj prawidłowy kierunek")
        print("Twoje polożenie to " + str(self._x) + "," + str(self._y))

    def show(self):
        print(self._x ,self._y)

    def setPosition(self,x,y):
        self._x = x
        self._y = y

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

class Ekwipunek():
    def __init__(self):
        self.equipmnent = {'sword': 1, 'bow':1 ,'arrow':20, 'knife':1}

    def showEq(self):
        print(self.equipmnent)

    def addEq(self,name, count):
        self.name = {}
        self.count = {}
        if name in self.equipmnent.keys():
            self.equipmnent[name] += count
        else:
            self.equipmnent[name] = count

    def showValue(self,key):
        if key in self.equipmnent:
           return (self.equipmnent[key])


class Item():
    def __init__(self):
        self.TablicaKartek = []


    def SetKartki(self,ile):
        for i in range(ile):
            kartka = Position(randint(0,MAP_SIZE),randint(0,MAP_SIZE))
            self.TablicaKartek[i] = kartka
            if len(self.TablicaKartek) > 1:
                for z in range(len(self.TablicaKartek)):
                    if self.TablicaKartek[i].show == self.TablicaKartek[z+1]:
                        self.TablicaKartek[i].setPosition(randint(MAP_SIZE),randint(MAP_SIZE))


kartki = Item()
kartki.SetKartki(4)
print(kartki.TablicaKartek)



