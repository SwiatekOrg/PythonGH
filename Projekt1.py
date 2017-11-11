import random

print("Losowac?")
czy_losowac = input()
while czy_losowac == "tak":
    from random import randint
    kostka = randint(1, 6)
    print(kostka)
    print("Losowac dalej?")
    czy_losowac = input()
    if czy_losowac=="nie":
        break
    elif czy_losowac=="tak":
        continue
    else:
        print("Wpisz tak/nie")
        czy_losowac = input()
print("Exit")
