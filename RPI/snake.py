from pad4pi import rpi_gpio
import max7219.led as led
from luma.core.interface.serial import spi, noop
from random import randint
import time


screen = led.matrix(cascaded = 1)
SIZE_LED = 8
SIZE_SNAKE = 3
x = 1
y = 4

screen.pixel(x, y, True, redraw=True)
x+=1
screen.pixel(x, y, True, redraw=True)
x+=1
screen.pixel(x, y, True, redraw=True)


while True:
    time.sleep(0.4)
    screen.pixel((x+6)%SIZE_LED,y, False, redraw=True)
    x += 1
    screen.pixel(x%SIZE_LED, y, True, redraw=True)
    if x == 5:
        time.sleep(0.4)
        screen.pixel((x + 6) % SIZE_LED, y, False, redraw=True)
        y += 1
        screen.pixel(x, y % SIZE_LED, True, redraw=True)
        time.sleep(0.4)
        screen.pixel((x + 7) % SIZE_LED, y-1, False, redraw=True)
        y += 1
        screen.pixel(x, y % SIZE_LED, True, redraw=True)
        while True:
            time.sleep(0.4)
            screen.pixel(x, (y+6)%SIZE_LED, False, redraw=True)
            y += 1
            screen.pixel(x, y%SIZE_LED, True, redraw=True)
