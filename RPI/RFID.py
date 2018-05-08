import RPi.GPIO as GPIO
from SimpleMFRC522 import SimpleMFRC522 as RFID
from time import sleep
import sys

GPIO.setwarnings(False)
rfid = RFID()


class Shop():
    def __init__(self):
        self.verify = 0


    def ShowMenu(self):
        print(" ")
        print("1. Sprawdz stan konta")
        print("2. Dodaj srodki do konta")
        print("3. Pokaz moje dane")
        print("4. Wyplac srodki")
        print("5. Sklep")
        print(" ")

    def getlogIn(self,id):
        try:
            pin = input("Podaj PIN: ")
        except:
            print("Zly pin")
            sys.exit()

        if id == 807818262888 and int(pin) == 1234:
            user.uzytkownik = "Mateusz Swiatek"
            user.money = 50.00
        elif id == 277909100046 and int(pin) == 6969:
            user.uzytkownik = "Kacper Krzoska"
            user.money = 100.00
        else:
            print("Zly PIN!")
            sys.exit()

    def ShowData(self):
        print("ID: "+ str(user.id))
        print("User: "+ str(user.uzytkownik))
        print("Money: "+ str(user.money))

    def Back(self):
        pause = raw_input("Wcisnij klaiwsz by wrocic do menu...")

    def Secutiry(self):
        print("Przyloz karte aby zweryfikowac...")
        ID = rfid.read_id()
        if user.id == ID:
            self.verify = 1
        else:
            self.verify = 0


class Story():
    def __init__(self):
        self.ListName = ["Banan","Baton","Karta Graficzna"]
        self.ListPrice = [0.59,1.99,500]
        self.what_do = 0

    def ShowStory(self):
        print(" ")
        print("****PRZEDMIOTY****")
        for i in range(0,len(self.ListName)):
            print(str(i)+ ". " +self.ListName[i] + " - Cena: " + str(self.ListPrice[i]) + " zl")

    def ShowOptions(self):
        print(" ")
        print("1. Zaplac za koszyk")
        print("2. Dodaj przedmiot do koszyka")
        print("3. Usun przedmiot z koszyka")
        print("4. Zobacz koszyk i jego wartosc")
        print("5. Wroc do menu")
        print(" ")

class Cart():
    def __init__(self):
        self.ItemList = []
        self.ItemsValue = 0

    def AddToCart(self,number):
        if number > len(story.ListName)-1 or number < 0:
            print("Zly numer")
            shop.Back()
        else:
            self.ItemList.append(story.ListName[number])
            self.ItemsValue += story.ListPrice[number]

    def DeleteFromCart(self,numer):
        if numer > len(self.ItemList)-1 or numer < 0:
            print("Zly numer")
            shop.Back()
        else:
            self.ItemsValue -= story.ListPrice[story.ListName.index(self.ItemList[numer])]
            self.ItemList.remove(self.ItemList[numer])

    def ShowCart(self):
        for i in range(0,len(self.ItemList)):
            print(str(i)+". "+self.ItemList[i])
        if len(self.ItemList) == 0:
            print("Koszyk pusty")
        print("Wartosc koszyka: "+ str(self.ItemsValue) +" zl" )

    def End(self):
        if user.money < self.ItemsValue:
            print("Masz za malo pieniedzy!")
        else:
            user.money -= self.ItemsValue
            self.ItemList[:] = []
            print("Zakupy udane, kwota zdjeta z konta")

class User():
    def __init__(self,id):
        self.id = id
        self.uzytkownik = "None"
        self.money = 0

    def MonetState(self):
        print("Twoje srodki na koncie to: " + str(self.money) + "zl")

    def AddMoney(self):
        dodac_srodki = int(raw_input("Ile chcesz dodac srodow?: "))
        self.money += dodac_srodki

    def TakeMoney(self):
        ile = int(raw_input("Jaka kwote chcesz wyplacic: "))
        if ile > self.money:
            print("Za malo srodkow na konice")
        else:
            self.money -= ile
            self.MonetState()


shop = Shop()
story = Story()
koszyk = Cart()

print("Przyloz karte ,by zidentyfikowac uztykownika")
user = User(rfid.read_id())
shop.getlogIn(user.id)
print("Zalogowany jako " + str(user.uzytkownik))

while True:
    shop.ShowMenu()
    co_robic = str(raw_input("Wybierz numer: "))
    print(" ")
    if co_robic == "1":
        user.MonetState()
        shop.Back()
    elif co_robic == "2":
        user.AddMoney()
        user.MonetState()
        shop.Back()
    elif co_robic == "3":
        shop.ShowData()
        shop.Back()
    elif co_robic == "4":
        shop.Secutiry()
        if shop.verify:
            print("Pomyslnie")
        else:
            print("Zla karta, powrot...")
            shop.Back()
            continue
        user.TakeMoney()
        shop.Back()
    elif co_robic == "5":
        while True:
            story.ShowStory()
            story.ShowOptions()
            story.what_do = str(raw_input("Co chcesz zrobic?: "))
            print(" ")
            if story.what_do == "1":
                shop.Secutiry()
                if shop.verify:
                    print("Pomyslnie")
                else:
                    print("Zla karta, powrot...")
                    shop.Back()
                    continue
                koszyk.End()
                shop.Back()
            elif story.what_do == "2":
                numer = int(raw_input("Podaj numer przedmiotu z listy: "))
                koszyk.AddToCart(numer)
            elif story.what_do == "3":
                numer = int(raw_input("Podaj numer przedmiotu z koszyka: "))
                koszyk.DeleteFromCart(numer)
            elif story.what_do == "4":
                koszyk.ShowCart()
                shop.Back()
            elif story.what_do == "5":
                break
            else:
                print("Zly numer")
                print(" ")

    else:
        print("Zly numer")


