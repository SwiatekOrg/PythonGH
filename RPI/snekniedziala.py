
from pad4pi import rpi_gpio
import max7219.led as led
from luma.core.interface.serial import spi, noop
from random import randint
import time

screen = led.matrix(cascaded = 1)
SIZE_LED = 8
STARTX = 0
STARTY = 4
x = STARTX
y = STARTY
screen.pixel(x, y, True, redraw=True)

def Idz(os, kierunek):
    global x, y
    time.sleep(0.4)
    screen.pixel(x % SIZE_LED, y % SIZE_LED, False, redraw=True)
    os += kierunek
    screen.pixel(x % SIZE_LED, y % SIZE_LED, True, redraw=True)


def Wkolko():
    while True:
        Idz(x,1)
        if x == STARTX + 4:
            while True:
                Idz(y,-1)
                if y == STARTY - 4:
                    while True:
                        Idz(x,-1)
                        if x == STARTX:
                            while True:
                                Idz(y,1)
                                if y == STARTY:
                                   return None



while True:
   Wkolko()