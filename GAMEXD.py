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

    def BackXY(self):
        return self._x ,self._y

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
            Kartka = Position(randint(0,MAP_SIZE),randint(0,MAP_SIZE))
            self.TablicaKartek.insert(i,Kartka)

    def ShowKartki(self):
        print("Kartki znajdują się na pozycjach (twoja to " + str(pozycja_gracza._x)+","+str(pozycja_gracza._y) +"):")
        for i in range(len(kartki.TablicaKartek)):
            kartki.TablicaKartek[i].show()

    def SprawdzKartki(self):
        x = 0
        y = 1
        for i in range(10000):
            if x == len(self.TablicaKartek)-1:
                break
            if self.TablicaKartek[x] == self.TablicaKartek[y]:
                self.TablicaKartek[x].setPosition(randint(0, MAP_SIZE), randint(0, MAP_SIZE))
                self.SprawdzKartki()
            if y == len(self.TablicaKartek)-1:
                x+=1
                y = x + 1
                continue
            y += 1






ekwipunek_gracza = Ekwipunek()
pozycja_gracza = Position(5,5)
kartki = Item()
kartki.SetKartki(99)
kartki.SprawdzKartki()





kartki.ShowKartki()
while True:
    print("W którą stronę iść?(polnoc,poludnie,wschod,zachod)")
    x = input()
    pozycja_gracza.move(x)
    for i in range(len(kartki.TablicaKartek)):
        if pozycja_gracza == kartki.TablicaKartek[i]:
            ekwipunek_gracza.addEq("kartka", 1)
            print("Znalazłeś kartkę! Masz już "+str(ekwipunek_gracza.showValue('kartka')) + " kartek")