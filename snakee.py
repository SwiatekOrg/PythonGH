from pad4pi import rpi_gpio
import max7219.led as led
from luma.core.interface.serial import spi, noop
from random import randint
import time

screen = led.matrix(cascaded = 1)

class Keyboard():

    def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8):
        self.KEYPAD = [
            ["1", "2", "3", "A"],
            ["4", "5", "6", "B"],
            ["7", "8", "9", "C"],
            ["*", "0", "#", "D"]
        ]

        self.ROW_PINS = [p1, p2, p3, p4]  # BCM numbering (GPIO.. number), first 4 pins
        self.COL_PINS = [p5, p6, p7, p8]  # next 4 left pins

        self.SIZE_LED = 8
        self.SNAKE_SIZE = 3
        self.STARTX = 0
        self.STARTY = 5
        self.x = self.STARTX
        self.y = self.STARTY
        self.pozycje = []
        self.poprzedni = "0"
        self.screen = led.matrix(cascaded=1)


        self.factory = rpi_gpio.KeypadFactory()
        self.keypad = self.factory.create_keypad(keypad=self.KEYPAD, row_pins=self.ROW_PINS, col_pins=self.COL_PINS)
        self.keypad.registerKeyPressHandler(self.processKey)

    def Poczatek(self):

        self.screen.clear()
        i = 0
        for i in range(0, self.SNAKE_SIZE):
            self.Dodaj()
            self.screen.pixel(self.x % self.SIZE_LED, self.y % self.SIZE_LED, True, redraw=True)
            if i < self.SNAKE_SIZE - 1:
                self.x += 1

    def Dodaj(self):
        self.pozycje.append((str(self.x % self.SIZE_LED) + str(self.y % self.SIZE_LED)))

    def Usun(self):
        a = int(self.pozycje[0]) // 10
        b = int(self.pozycje[0]) % 10
        self.screen.pixel(a, b, False, redraw=True)
        self.pozycje.remove(self.pozycje[0])

    def DoPrzodu(self):
        time.sleep(0.4)
        self.Usun()
        self.x += 1
        self.screen.pixel(self.x % self.SIZE_LED, self.y % self.SIZE_LED, True, redraw=True)
        self.Dodaj()

    def DoTylu(self):
        time.sleep(0.4)
        self.Usun()
        self.x -= 1
        self.screen.pixel(self.x % self.SIZE_LED, self.y % self.SIZE_LED, True, redraw=True)
        self.Dodaj()

    def WGore(self):
        time.sleep(0.4)
        self.Usun()
        self.y -= 1
        self.screen.pixel(self.x % self.SIZE_LED, self.y % self.SIZE_LED, True, redraw=True)
        self.Dodaj()

    def WDol(self):
        time.sleep(0.4)
        self.Usun()
        self.y += 1
        self.screen.pixel(self.x % self.SIZE_LED, self.y % self.SIZE_LED, True, redraw=True)
        self.Dodaj()

    def Sterwoanie(self,key):
        if key == "6":
            self.DoPrzodu()
        elif key == "4":
            self.DoTylu()
        elif key == "2":
            self.WGore()
        elif key == "8":
            self.WDol()


    def processKey(self, key):
        if key == "6":
            self.Sterwoanie(key)
        elif key == "4":
            self.Sterwoanie(key)
        elif key == "2":
            self.Sterwoanie(key)
        elif key == "8":
            self.Sterwoanie(key)





keyboard = Keyboard(2, 3, 4, 17, 27, 22, 5, 6)
keyboard.Poczatek()
while True:
    pass