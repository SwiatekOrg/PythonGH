class Position():
    def __init__(self):
        self._x = 5
        self._y = 5
        self._mapName = "Krakow"

    def move(self,x):
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

    def changeMap(self, mapname):
        self._mapName = mapname

    def show(self):
        print(self._x,self._y,self._mapName)

pozycja_gracza = Position()

while True:
    print("W którą stronę iść?(polnoc,poludnie,wschod,zachod)")
    x = input()
    pozycja_gracza.move(x)



