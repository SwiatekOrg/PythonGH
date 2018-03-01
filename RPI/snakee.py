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
        self.poprzedni = 0

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

while True:
    time.sleep(keyboard.PRZERWA)
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
