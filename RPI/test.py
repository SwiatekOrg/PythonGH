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

        self.ROW_PINS = [p1, p2, p3, p4]
        self.COL_PINS = [p5, p6, p7, p8]
        self.x = randint(0,7)
        self.y = randint(0,7)
        self.paint =[]
        self.screen = led.matrix(cascaded=1)
        self.screen.pixel(self.x, self.y, True, redraw=True)
        self.factory = rpi_gpio.KeypadFactory()
        self.keypad = self.factory.create_keypad(keypad=self.KEYPAD, row_pins=self.ROW_PINS, col_pins=self.COL_PINS)
        self.keypad.registerKeyPressHandler(self.processKey)

    def processKey(self, key):
        self.screen.pixel(self.x, self.y, False, redraw=True)
        if key == "2":
            self.y = (self.y - 1) % 8
        elif key == "4":
            self.x = (self.x - 1) % 8
        elif key == "6":
            self.x = (self.x + 1) % 8
        elif key == "8":
            self.y = (self.y + 1) % 8
        self.screen.pixel(self.x, self.y, True, redraw=True)
        if key == "5":
            self.paint.append(self.x)
            self.paint.append(self.y)
        for i in range(0,(len(self.paint))//2):
            self.screen.pixel(self.paint[2*i], self.paint[2*i+1], True, redraw=True)

keyboard = Keyboard(6, 5, 22, 27, 17, 4, 3, 2)

while True:
    pass