from pad4pi import rpi_gpio
import max7219.led as led
from luma.core.interface.serial import spi, noop
from random import randint
import random
import time


class Snake():

    def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8):
        self.screen = led.matrix(cascaded = 1)
        self.screen.clear()

        self.SIZE_LED = 8
        self.SNAKE_SIZE = 3
        self.STARTX = 0
        self.STARTY = 5
        self.PRZERWA = 0.4

        self.kierunek = "prawo"
        self.x = self.STARTX
        self.y = self.STARTY
        self.pozycje = []
        self.punkt = str(randint(0,self.SIZE_LED-1))+str(randint(0,self.SIZE_LED-1))
        self.poprzedni = 0
        self.miganie = 0

        self.KEYPAD = [
            ["1", "2", "3", "A"],
            ["4", "5", "6", "B"],
            ["7", "8", "9", "C"],
            ["*", "0", "#", "D"]
        ]

        self.ROW_PINS = [p1, p2, p3, p4]
        self.COL_PINS = [p5, p6, p7, p8]

        self.factory = rpi_gpio.KeypadFactory()
        self.keypad = self.factory.create_keypad(keypad=self.KEYPAD, row_pins=self.ROW_PINS, col_pins=self.COL_PINS)
        self.keypad.registerKeyPressHandler(self.processKey)

    def Poczatek(self):
        for i in range(0,self.SNAKE_SIZE):
            self.Dodaj()
            self.screen.pixel(self.x%self.SIZE_LED, self.y%self.SIZE_LED, True, redraw=True)
            if i<self.SNAKE_SIZE-1:
                self.x += 1

    def Dodaj(self):
        self.screen.pixel(self.x % self.SIZE_LED, self.y % self.SIZE_LED, True, redraw=True)
        self.pozycje.append((str(self.x%self.SIZE_LED)+str(self.y%self.SIZE_LED)))

    def Usun(self):
        self.screen.pixel((int(self.pozycje[0]) // 10),(int(self.pozycje[0]) % 10), False, redraw=True)
        self.pozycje.remove(self.pozycje[0])

    def DoPrzodu(self):
        self.x += 1

    def DoTylu(self):
        self.x -= 1

    def WGore(self):
        self.y -= 1

    def WDol(self):
        self.y += 1

    def Punkt(self):
        self.punkt = (str(randint(0, self.SIZE_LED - 1)) + str(randint(0, self.SIZE_LED - 1)))

        while self.punkt in self.pozycje:
            self.punkt = str(randint(0, self.SIZE_LED - 1)) + str(randint(0, self.SIZE_LED - 1))
            if self.pozycje not in self.pozycje:
                break

        self.screen.pixel(int(self.punkt) // 10, int(self.punkt) % 10, True, redraw=True)

    def Miganie(self):
        if self.miganie % 2 == 1:
            self.screen.pixel(int(self.punkt) // 10, int(self.punkt) % 10, True, redraw=True)
        elif self.miganie % 2 == 0:
            self.screen.pixel(int(self.punkt) // 10, int(self.punkt) % 10, False, redraw=True)
        self.miganie += 1

    def Jedz(self):
        if self.punkt == self.pozycje[-1]:
            if self.kierunek == "gora":
                self.pozycje.append(str(str((self.x%self.SIZE_LED))+str(((self.y-1)%self.SIZE_LED))))
            elif self.kierunek == "dol":
                self.pozycje.append(str(str((self.x % self.SIZE_LED)) + str(((self.y + 1) % self.SIZE_LED))))
            elif self.kierunek == "lewo":
                self.pozycje.append(str(str(((self.x-1) % self.SIZE_LED)) + str(((self.y) % self.SIZE_LED))))
            elif self.kierunek == "prawo":
                self.pozycje.append(str(str(((self.x+1) % self.SIZE_LED)) + str(((self.y) % self.SIZE_LED))))
            else:
                return 0
            self.screen.pixel((int(self.pozycje[-1]) // 10), (int(self.pozycje[-1]) % 10), True, redraw=True)
            self.Punkt()

    def processKey(self, key):
        if key == "6":
            self.kierunek = "prawo"
        elif key == "4":
            self.kierunek = "lewo"
        elif key == "2":
            self.kierunek = "gora"
        elif key == "8":
            self.kierunek = "dol"


keyboard = Snake(6, 5, 22, 27, 17, 4, 3, 2)

keyboard.Poczatek()
keyboard.Punkt()
while True:

    time.sleep(keyboard.PRZERWA)
    keyboard.Jedz()
    keyboard.Miganie()
    keyboard.Usun()
    if keyboard.kierunek == "dol":
        keyboard.WDol()
    elif keyboard.kierunek == "gora":
        keyboard.WGore()
    elif keyboard.kierunek == "prawo":
        keyboard.DoPrzodu()
    elif keyboard.kierunek == "lewo":
        keyboard.DoTylu()
    keyboard.Dodaj()
