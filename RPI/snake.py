from pad4pi import rpi_gpio
import max7219.led as led
from luma.core.interface.serial import spi, noop
from random import randint
import random
import time

screen = led.matrix(cascaded = 1)
screen.clear()

SIZE_LED = 8
SNAKE_SIZE = 3
STARTX = 0
STARTY = 5
PRZERWA = 0.4

dlugosc = SNAKE_SIZE
x = STARTX
y = STARTY
pozycje = []
kierunek = randint(0,4)

def Poczatek():
    global x,y
    for i in range(0,SNAKE_SIZE):
        Dodaj()
        screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)
        if i<SNAKE_SIZE-1:
          x += 1

def Dodaj():
    screen.pixel(x % SIZE_LED, y % SIZE_LED, True, redraw=True)
    pozycje.append((str(x%SIZE_LED)+str(y%SIZE_LED)))

def Usun():
    screen.pixel((int(pozycje[0]) // 10),(int(pozycje[0]) % 10), False, redraw=True)
    pozycje.remove(pozycje[0])

def DoPrzodu():
    global x
    Usun()
    x += 1
    Dodaj()

def DoTylu():
    global x
    Usun()
    x -= 1
    Dodaj()

def WGore():
    global y
    Usun()
    y -= 1
    Dodaj()

def WDol():
    global y
    Usun()
    y += 1
    Dodaj()

poprzedni = 0
Poczatek()
DoPrzodu()
while True:
    time.sleep(PRZERWA)
    kierunek = randint(0,3)

    if kierunek == 0:  #DoPrzodu
        if poprzedni == 1:
            DoTylu()
            poprzedni = 1
            print("KUR")
        else:
            DoPrzodu()
            poprzedni = 0
    elif kierunek == 1: #DoTylu
        if poprzedni == 0:
            DoPrzodu()
            poprzedni = 0
            print("KUR")
        else:
            DoTylu()
            poprzedni = 1
    elif kierunek == 2:  #WGore
        if poprzedni == 3:
            WDol()
            poprzedni = 3
            print("KUR")
        else:
            WGore()
            poprzedni = 2
    elif kierunek == 3:   #WDol
        if poprzedni == 2:
            WGore()
            poprzedni = 2
            print("KUR")
        else:
            WDol()
            poprzedni = 3