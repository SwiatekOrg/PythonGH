class Position():
    def __init__(self):
        self._x = 50
        self._y = 50
        self._mapName = "Krakow"

    def move(self,x):
        if x == "polnoc":
            self._x += 1
        elif x == "poludnie":
            self._x += -1
        elif x == "wschod":
             self_y += 1
        elif x == "zachod":
             self._y += -1
        else:
            print("Podaj prawidłowy kierunek")
        print("Twoje polożenie to " + str(self._x) + "," + str(self._y))

    def changeMap(self, mapname):
        self._mapName = mapname

    def show(self):
        print(self._x,self._y,self._mapName)

pozycja_gracza = Position()

while True:
    print("W którą stronę ruch?(polnoc,poludnie,wschod,zachod)")
    x = input()
    pozycja_gracza.move(x)


