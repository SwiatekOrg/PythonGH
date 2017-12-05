
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

    def _eq_(self, other):
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

ekwipunek_gracza = Ekwipunek()
pozycja_gracza = Position()
pozycja_gracza.setPosition(5,5)
pozycja_przedmiotu = Position()
pozycja_przedmiotu.setPosition(5,6)
print(pozycja_przedmiotu.show(),pozycja_gracza.show())
while True:
    print("W którą stronę iść?(polnoc,poludnie,wschod,zachod)")
    x = input()
    pozycja_gracza.move(x)
    if pozycja_gracza == pozycja_przedmiotu:
        ekwipunek_gracza.addEq("kartka", 1)
        print("Znalazłeś kartkę!")
    ekwipunek_gracza.showEq()
