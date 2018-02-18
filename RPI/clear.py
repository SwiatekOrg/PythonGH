from pad4pi import rpi_gpio
import max7219.led as led
from luma.core.interface.serial import spi, noop

screen = led.matrix(cascaded = 1)
screen.clear()