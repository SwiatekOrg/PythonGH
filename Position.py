class Position():
    def __init__(self):
        self._x = 50
        self._y = 50
        self._mapName = "Krakow"

    def move(self,x):
        if x == "polnoc":
            self._x += 25
            if self._x > 100 or self._x < 0:
                self._x -= 25
                print ("Nie mozesz wyjsc poza mapę")
        elif x == "poludnie":
            self._x += -25
            if self._x > 100 or self._x < 0:
                self._x += 25
                print ("Nie mozesz wyjsc poza mapę")
        elif x == "wschod":
             self._y += 25
             if self._y > 100 or self._y < 0:
                 self._y -= 25
                 print ("Nie mozesz wyjsc poza mapę")
        elif x == "zachod":
             self._y += -25
             if self._y > 100 or self._y < 0:
                 self._y += 25
                 print ("Nie mozesz wyjsc poza mapę")
        else:
            print("Podaj prawidłowy kierunek")
        print("Twoje polożenie to " + str(self._x) + "," + str(self._y))

    def changeMap(self, mapname):
        self._mapName = mapname

    def show(self):
        print(self._x,self._y,self._mapName)

pozycja_gracza = Position()

while True:
    print("W którą stronę iść??(polnoc,poludnie,wschod,zachod)")
    x = input()
    pozycja_gracza.move(x)



