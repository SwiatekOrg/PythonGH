from pad4pi import rpi_gpio
import sys
import max7219.led as led
from luma.core.interface.serial import spi, noop
from random import randint


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

        self.x = randint(0,7)
        self.y = randint(0,7)
        self.screen1.pixel(self.x, self.y, True, redraw=True)
        self.factory = rpi_gpio.KeypadFactory()
        self.keypad = self.factory.create_keypad(keypad=self.KEYPAD, row_pins=self.ROW_PINS, col_pins=self.COL_PINS)
        self.keypad.registerKeyPressHandler(self.processKey)

class MyKeyboard(Keyboard):

    screen1 = led.matrix(cascaded=1)

    def processKey(self, key):
        self.screen1.clear()
        if key == "2":
            if self.y == 0 and key == "2":
                self.screen1.pixel(self.x, 7, True, redraw=True)
                self.y = 8
            self.y = self.y - 1
            self.screen1.pixel(self.x,self.y,True, redraw=True)
        elif key == "4":
            if self.x == 0 and key == "4":
                self.screen1.pixel( 7, self.y, True, redraw=True)
                self.x = 8
            self.x = self.x - 1
            self.screen1.pixel(self.x,self.y,True, redraw=True)
        elif key == "6":
            if self.x == 7 and key == "6":
                self.screen1.pixel(0, self.y, True, redraw=True)
                self.x = -1
            self.x = self.x + 1
            self.screen1.pixel(self.x,self.y,True, redraw=True)
        elif key == "8":
            if self.y == 7 and key == "8":
                self.screen1.pixel(self.x, 0, True, redraw=True)
                self.y = -1
            self.y = self.y + 1
            self.screen1.pixel(self.x,self.y,True, redraw=True)
        else:
            self.screen1.pixel(self.x,self.y,True, redraw=True)


screen1 = led.matrix(cascaded=1)
keyboard2 = MyKeyboard(6, 5, 22, 27, 17, 4, 3, 2)


while True:
    pass