from pad4pi import rpi_gpio
import max7219.led as led
from luma.core.interface.serial import spi, noop
from random import randint
import time


class Keyboard():
    SIZE_LED = 8
    def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8):
        self.KEYPAD = [
            ["1", "2", "3", "A"],
            ["4", "5", "6", "B"],
            ["7", "8", "9", "C"],
            ["*", "0", "#", "D"]
        ]

        self.ROW_PINS = [p1, p2, p3, p4]
        self.COL_PINS = [p5, p6, p7, p8]
        self.x = randint(0,self.SIZE_LED-1)
        self.y = randint(0,self.SIZE_LED-1)
        self.tablica =[]
        self.screen = led.matrix(cascaded=1)
        self.screen.pixel(self.x, self.y, True, redraw=True)
        self.factory = rpi_gpio.KeypadFactory()
        self.keypad = self.factory.create_keypad(keypad=self.KEYPAD, row_pins=self.ROW_PINS, col_pins=self.COL_PINS)
        self.keypad.registerKeyPressHandler(self.processKey)
        while True:
            self.screen.pixel(self.x, self.y, True, redraw=True)
            time.sleep(0.5)
            self.screen.pixel(self.x, self.y, False, redraw=True)
            time.sleep(0.5)

    def processKey(self, key):
        self.screen.pixel(self.x, self.y, False, redraw=True)
        if key == "2":
            self.y = (self.y - 1) % self.SIZE_LED
        elif key == "4":
            self.x = (self.x - 1) % self.SIZE_LED
        elif key == "6":
            self.x = (self.x + 1) % self.SIZE_LED
        elif key == "8":
            self.y = (self.y + 1) % self.SIZE_LED
        self.screen.pixel(self.x, self.y, True, redraw=True)


        if str(str(self.x)+str(self.y)) in self.tablica and key == "5":
            self.screen.pixel(self.x, self.y, False, redraw=True)
            self.tablica.remove(str(str(self.x)+str(self.y)))
            self.screen.pixel(self.x, self.y, False, redraw=True)
        elif key == "5":
            self.tablica.append(str(str(self.x)+str(self.y)))
        for i in range(0,len(self.tablica)):
            a = int(self.tablica[i])//10
            b = int(self.tablica[i])%10
            self.screen.pixel( a, b, True, redraw=True)
        self.screen.pixel(self.x, self.y, True, redraw=True)

keyboard = Keyboard(6, 5, 22, 27, 17, 4, 3, 2)
screen = led.matrix(cascaded = 1)

screen.show_message("LED Paint")
while True:
    pass