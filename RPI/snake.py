from pad4pi import rpi_gpio
import max7219.led as led
from luma.core.interface.serial import spi, noop
from random import randint
import time


screen = led.matrix(cascaded = 1)
SIZE_LED = 8
x = 0
y = 4

screen.pixel(x, y, True, redraw=True)

def DoPrzodu():
    global x,y
    time.sleep(0.4)
    screen.pixel(x%SIZE_LED, y%SIZE_LED, False, redraw=True)
    x += 1
    screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)
def SkretLewo():
    global x,y
    time.sleep(0.4)
    screen.pixel(x%SIZE_LED, y%SIZE_LED, False, redraw=True)
    y += 1
    screen.pixel(x%SIZE_LED, y%SIZE_LED, True, redraw=True)

while True:
    DoPrzodu()
    if x == 4:
        while True:
            SkretLewo()