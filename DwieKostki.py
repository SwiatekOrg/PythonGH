import random

print("Iloma kostkami chcesz rzuac?")
liczba_kostek = input()
while liczba_kostek == "1":
    print("Losowac liczby?")
    czy_losowac = input()
    if czy_losowac == "tak":
        while czy_losowac == "tak":
            from random import randint
            kostka = randint(1, 6)
            print("Wylosowales:")
            print(kostka)
            print("Losowac jeszcze raz?")
            czy_losowac = input()
            if czy_losowac == "nie":
                print("Exit")
                break
            elif czy_losowac == "tak":
                continue
            else:
                print("Wpisz tak/nie")
                czy_losowac = input()
            break
    elif czy_losowac == "nie":
        print("Exit")
        break
    else:
        print("Niepoprawna odpowiedz")
    break
while liczba_kostek == "2":
    print("Losowac liczby?")
    czy_losowac = input()
    if czy_losowac == "tak":
        while czy_losowac == "tak":
            from random import randint
            kostka1 = randint(1, 6)
            kostka2 = randint(1, 6)
            print("Wylosowales:")
            print(kostka1, kostka2)
            print("Losowac jeszcze raz?")
            czy_losowac = input()
            if czy_losowac == "nie":
                print("Exit")
                break
            elif czy_losowac == "tak":
                continue
            else:
                print("Wpisz tak/nie")
                czy_losowac = input()
            break
    elif czy_losowac == "nie":
        print("Exit")
        break
    else:
        print("Niepoprawna odpowiedz")
    break
