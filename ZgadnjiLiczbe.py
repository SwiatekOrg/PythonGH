import random

from random import randint
import sys

gramy = "tak"
while gramy == "tak":
    jeden = "1"
    numer = randint(1, 100)
    print("Sprobuj zganac wylosowany numer z zakresu 1 do 100, wylosowac numer?")
    grac = input()
    while jeden == "1":
        if grac == "nie":
            print("Exit")
            sys.exit()
        elif grac == "tak":
            break
        else:
            print("Wpisz tak/nie")
            grac = input()
    print("Sprobuj odgnac wylosowany numer")
    while grac == "tak":
        zgadnac = int(input())
        if numer == zgadnac:
            print("Brawo, odgadles numer!")
            break
        elif zgadnac > 100 or zgadnac < 1:
            print("Podaj liczbe z zakresu od do 100")
            print("Sprobuj ponowanie")
        elif zgadnac > numer:
            print("Wylosowana liczba jest mniejsza")
            print("Sprobuj ponowanie")
        elif zgadnac < numer:
            print("Wylosowana liczba jest wieksza")
            print("Sprobuj ponowanie")
    print("Chesz zagrac jeszcze raz?")
    gramy = input()
    while jeden == "1":
        if gramy == "nie":
            print("Exit")
            sys.exit()
        elif gramy == "tak":
            break
        else:
            print("Wpisz tak/nie")
            gramy = input()
