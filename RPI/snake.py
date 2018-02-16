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
    time.sleep(0.2)
    screen.pixel((x+6)%8,y, False, redraw=True)
    x += 1
    screen.pixel(x%8, y, True, redraw=True)

