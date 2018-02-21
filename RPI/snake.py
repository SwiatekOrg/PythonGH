from pad4pi import rpi_gpio
import max7219.led as led
from luma.core.interface.serial import spi, noop
from random import randint
import time

screen = led.matrix(cascaded = 1)
SIZE_LED = 8
SNAKE_SIZE = 3
STARTX = 0
STARTY = 5
x = STARTX
y = STARTY
pozycje = []

def Poczatek():
    global x,y
    i = 0
    for i in range(0,SNAKE_SIZE):
        Dodaj()
        screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)
        if i<SNAKE_SIZE-1:
          x += 1

def Dodaj():
    pozycje.append((str(x%SIZE_LED)+str(y%SIZE_LED)))


def Usun():
    a = int(pozycje[0]) // 10
    b = int(pozycje[0]) % 10
    screen.pixel(a, b, False, redraw=True)
    pozycje.remove(pozycje[0])

def DoPrzodu():
    global x,y
    time.sleep(0.4)
    Usun()
    x += 1
    screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)
    Dodaj()
def DoTylu():
    global x, y
    time.sleep(0.4)
    Usun()
    x -= 1
    screen.pixel(x % SIZE_LED, y % SIZE_LED, True, redraw=True)
    Dodaj()
def WGore():
    global x,y
    time.sleep(0.4)
    Usun()
    y -= 1
    screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)
    Dodaj()
def WDol():
    global x,y
    time.sleep(0.4)
    Usun()
    y += 1
    screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)
    Dodaj()


Poczatek()

while True:
    print(pozycje)
    DoPrzodu()
    print(pozycje)
    DoPrzodu()
    print(pozycje)
    DoPrzodu()
    print(pozycje)
    DoPrzodu()
    print(pozycje)
    WGore()
    print(pozycje)
    WGore()
    print(pozycje)
    DoTylu()
    print(pozycje)
    WDol()
    print(pozycje)
