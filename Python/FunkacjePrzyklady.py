#Zadanie4
import random
from random import randint
print("Podaj dlugosc listy z ktorej mam wyliczyc srednia")
dlugosc_listy = int(input())
a = 0
b = 0
c = 0
d = 0
def srednia(dlugosc_listy,a,b,c,d):
    lista = []
    while a<dlugosc_listy:
        b = randint(0,100)
        lista.append(b)
        a = a + 1
        c = c + b
    print("Nasza lista ma w sobie liczby")
    print(lista)
    d = c/a
    print("A srednia z niej to")
    print(d)

srednia(dlugosc_listy,a,b,c,d)

#Zadanie3

import random
from random import randint
i = 0
size = 0
randmin = 0
randmax = 0
def createList2(size, randmin, randmax ):
    global i
    lista = []
    print("Podaj rozmiar tablicy")
    size= int(input())
    print("Podaj najmniejszą warttość tablicy")
    randmin=int(input())
    print("podaj najwięszką wartość tablicy")
    randmax=int(input())
    while i<size:
        a = randint(randmin,randmax)
        lista.append(a)
        i = i + 1
    print(lista)

createList2(size, randmin, randmax)
