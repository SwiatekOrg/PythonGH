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
            a = randint(1, 10)
            while True:
                licznik += 1
                DoPrzodu()
                print(licznik)
                if licznik == a:
                    licznik = 0
                    break
        elif z == 2:
            a = randint(1, 10)
            while True:
                licznik += 1
                DoTylu()
                print(licznik)
                if licznik == a:
                    licznik = 1
                    break
        elif z == 3:
            a = randint(1, 10)
            while True:
                licznik += 1
                WGore()
                print(licznik)
                if licznik == a:
                    licznik = 0
                    break
        elif z == 4:
            a = randint(1, 10)
            while True:
                licznik += 1
                WDol()
                print(licznik)
                if licznik == a:
                    licznik = 0
                    break



licznik=1

while True:
    DoPrzodu()
    licznik += 1
    print(licznik)
    if licznik == randint(1,10):
        Losowo()

