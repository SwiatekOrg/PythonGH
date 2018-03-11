import RPi.GPIO as GPIO
from SimpleMFRC522 import SimpleMFRC522 as RFID
from time import sleep
import sys

GPIO.setwarnings(False)
rfid = RFID()


class Shop():
    def ShowMenu(self):
        print(" ")
        print("1. Sprawdz stan konta")
        print("2. Dodaj srodki do konta")
        print("3. Pokaz moje dane")
        print("4. Wyplac srodki")
        print("5. Sklep")
        print(" ")

    def getlogIn(self,id):
        pin = input("Podaj PIN: ")
        if id == 807818262888 and pin == 1234:
            user.uzytkownik = "Mateusz Swiatek"
            user.money = 50.00
        elif id == 277909100046 and pin == 6969:
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
        try:
            pause = input("Wcisnij klaiwsz by wrocic do menu...")
        except SyntaxError:
            pass


class Story():
    def __init__(self):
        self.ListName = ["Banan","Baton","Karta Graficzna"]
        self.ListPrice = [0.59,1.99,500]
        self.what_do = 0

    def ShowStory(self):
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
        self.ItemList.append(story.ListName[number])
        self.ItemsValue += story.ListPrice[number]

    def DeleteFromCart(self,numer):
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
        dodac_srodki = input("Ile chcesz dodac srodow?: ")
        self.money += dodac_srodki

    def TakeMoney(self):
        ile = int(input("Jaka kwote chcesz wyplacic: "))
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
    co_robic = input("Wybierz numer: ")
    print(" ")
    if co_robic == 1:
        user.MonetState()
        shop.Back()
        continue
    elif co_robic == 2:
        user.AddMoney()
        user.MonetState()
        shop.Back()
        continue
    elif co_robic == 3:
        shop.ShowData()
        shop.Back()
        continue
    elif co_robic == 4:
        user.TakeMoney()
        shop.Back()
        continue
    elif co_robic == 5:
        story.ShowStory()
        story.ShowOptions()
        while True:
            story.what_do = input("Co chcesz zrobic?: ")
            if story.what_do == 1:
                koszyk.End()
            elif story.what_do == 2:
                numer = input("Podaj numer przedmiotu z listy: ")
                koszyk.AddToCart(numer)
            elif story.what_do == 3:
                numer = input("Podaj numer przedmiotu z koszyka: ")
                koszyk.DeleteFromCart(numer)
            elif story.what_do == 4:
                koszyk.ShowCart()
            elif story.what_do == 5:
                break
        continue
