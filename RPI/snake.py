from pad4pi import rpi_gpio
import max7219.led as led
from luma.core.interface.serial import spi, noop
from random import randint
import time


screen = led.matrix(cascaded = 1)
SIZE_LED = 8
STARTX = 0
STARTY = 0
x = STARTX
y = STARTY
screen.pixel(x, y, True, redraw=True)


##### 1 WERSJA! ####
def DoPrzodu():
    global x,y
    time.sleep(0.4)
    screen.pixel(x%SIZE_LED, y%SIZE_LED, False, redraw=True)
    x += 1
    screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)
def DoTylu():
    global x, y
    time.sleep(0.4)
    screen.pixel(x % SIZE_LED, y % SIZE_LED, False, redraw=True)
    x -= 1
    screen.pixel(x % SIZE_LED, y % SIZE_LED, True, redraw=True)
def WGore():
    global x,y
    time.sleep(0.4)
    screen.pixel(x%SIZE_LED, y%SIZE_LED, False, redraw=True)
    y -= 1
    screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)
def WDol():
    global x,y
    time.sleep(0.4)
    screen.pixel(x%SIZE_LED, y%SIZE_LED, False, redraw=True)
    y += 1
    screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)

def Wkolko():
    while True:
        DoPrzodu()
        if x == STARTX + 4:
            while True:
                WGore()
                if y == STARTY - 4:
                    while True:
                        DoTylu()
                        if x == STARTX:
                            while True:
                                WDol()
                                if y == STARTY:
                                    return None

def Losowo():
    licznik = 0
    while True:
        z = randint(1,4)
        if z == 1:
            while True:
                licznik += 1
                DoPrzodu()
                if licznik == 4:
                    licznik = 0
                    break
        elif z == 2:
            while True:
                licznik += 1
                DoTylu()
                if licznik == 4:
                    licznik = 1
                    break
        elif z == 3:
            while True:
                licznik += 1
                WGore()
                if licznik == 4:
                    licznik = 0
                    break
        elif z == 4:
            while True:
                licznik += 1
                WDol()
                if licznik == 4:
                    licznik = 0
                    break



licznik=1

while True:
    DoPrzodu()
    licznik += 1
    if licznik == 4:
        Losowo()

