import random
from random import randint

class Position():
    def __init__(self):
        self._x = 0
        self._y = 0

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

    def SetKartki(self,ile):
        for i in range(ile):
            kartka = Position()



ekwipunek_gracza = Ekwipunek()
pozycja_gracza = Position()
pozycja_gracza.setPosition(5,5)

kartka1 = Position()
kartka2 = Position()
kartka3 = Position()
kartka4 = Position()
tablica_przedmiotow = [kartka1 , kartka2 , kartka3 , kartka4]

for i in range(0,len(tablica_przedmiotow)):
    tablica_przedmiotow[i].setPosition(randint(0,10),randint(0,10))
    i = i + 1

print("Kartki znajdują się na pozycjach(twoja to 5 5):")
for i in range(0,len(tablica_przedmiotow)):
    tablica_przedmiotow[i].show()
    i = i + 1

while True:
    print("W którą stronę iść?(polnoc,poludnie,wschod,zachod)")
    x = input()
    pozycja_gracza.move(x)
    for i in range(0,len(tablica_przedmiotow)):
        if pozycja_gracza == tablica_przedmiotow[i]:
            ekwipunek_gracza.addEq("kartka", 1)
            print("Znalazłeś kartkę! Masz już "+str(ekwipunek_gracza.showValue('kartka')) + " kartek")
        i = i + 1

