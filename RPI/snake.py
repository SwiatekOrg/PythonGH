from pad4pi import rpi_gpio
import max7219.led as led
from luma.core.interface.serial import spi, noop
from random import randint
import random
import time

class Snake():
    def __init__(self):
        self.screen = led.matrix(cascaded = 1)
        self.screen.clear()

        self.SIZE_LED = 8
        self.SNAKE_SIZE = 3
        self.STARTX = 0
        self.STARTY = 5
        self.PRZERWA = 0.4

        self.x = self.STARTX
        self.y = self.STARTY
        self.pozycje = []
        self.poprzedni = 0


    def Poczatek(self):
        for i in range(0,self.SNAKE_SIZE):
            self.Dodaj()
            self.screen.pixel(self.x%self.SIZE_LED, self.y%self.SIZE_LED, True, redraw=True)
            if i<self.SNAKE_SIZE-1:
                self.x += 1

    def Dodaj(self):
        self.screen.pixel(self.x % self.SIZE_LED, self.y % self.SIZE_LED, True, redraw=True)
        self.pozycje.append((str(self.x%self.SIZE_LED)+str(self.y%self.SIZE_LED)))

    def Usun(self):
        self.screen.pixel((int(self.pozycje[0]) // 10),(int(self.pozycje[0]) % 10), False, redraw=True)
        self.pozycje.remove(self.pozycje[0])

    def DoPrzodu(self):
        self.x += 1

    def DoTylu(self):
        self.x -= 1

    def WGore(self):
        self.y -= 1

    def WDol(self):
        self.y += 1

    def LosowoCoKrok(self):
        kierunek = randint(0,3)
        if kierunek == 0:  #DoPrzodu
            if self.poprzedni == 1:
                self.DoTylu()
                self.poprzedni = 1
            else:
                self.DoPrzodu()
                self.poprzedni = 0
        elif kierunek == 1: #DoTylu
            if self.poprzedni == 0:
                self.DoPrzodu()
                self.poprzedni = 0
            else:
                self.DoTylu()
                self.poprzedni = 1
        elif kierunek == 2:  #WGore
            if self.poprzedni == 3:
                self.WDol()
                self.poprzedni = 3
            else:
                self.WGore()
                self.poprzedni = 2
        elif kierunek == 3:   #WDol
            if self.poprzedni == 2:
                self.WGore()
                self.poprzedni = 2
            else:
                self.WDol()
                self.poprzedni = 3

    def SnakeLive(self):
        self.Poczatek()
        while True:
            time.sleep(self.PRZERWA)
            self.Usun()
            self.LosowoCoKrok()
            self.Dodaj()

snake = Snake()
snake.SnakeLive()