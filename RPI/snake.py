from pad4pi import rpi_gpio
import max7219.led as led
from luma.core.interface.serial import spi, noop
from random import randint
import time

screen = led.matrix(cascaded = 1)
SIZE_LED = 8
STARTX = 0
STARTY = 5
x = STARTX
y = STARTY

screen.pixel(x, y, True, redraw=True)
x += 1
screen.pixel(x, y, True, redraw=True)
x += 1
screen.pixel(x, y, True, redraw=True)

def SkretWGore():
    global x,y
    time.sleep(0.4)
    screen.pixel((x-2)%SIZE_LED, y%SIZE_LED, False, redraw=True)
    y -= 1
    screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)
    time.sleep(0.4)
    screen.pixel((x-1)%SIZE_LED, (y+1)%SIZE_LED, False, redraw=True)
    y -= 1
    screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)


def DoPrzodu():
    global x,y
    time.sleep(0.4)
    screen.pixel((x-2)%SIZE_LED, y%SIZE_LED, False, redraw=True)
    x += 1
    screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)
def DoTylu():
    global x, y
    time.sleep(0.4)
    screen.pixel((x+2) % SIZE_LED, y % SIZE_LED, False, redraw=True)
    x -= 1
    screen.pixel(x % SIZE_LED, y % SIZE_LED, True, redraw=True)
def WGore():
    global x,y
    time.sleep(0.4)
    screen.pixel(x%SIZE_LED, (y+2)%SIZE_LED, False, redraw=True)
    y -= 1
    screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)
def WDol():
    global x,y
    time.sleep(0.4)
    screen.pixel(x%SIZE_LED, (y-2)%SIZE_LED, False, redraw=True)
    y += 1
    screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)

while True:
    DoPrzodu()
    if x == 5:
        SkretWGore()
        WGore()
        while True:
            WGore()
