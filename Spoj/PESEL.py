pesel = int(input("Podaj PESEL(11 cyfr) do sprawdzenia: "))
tab = []
for i in range(11):
    tab.append(pesel % 10)
    pesel = (pesel-tab[i])/10
    print(tab[i])
tab.reverse()
suma = tab[0] * 1 + tab[1] * 3 + tab[2] * 7 + tab[3] * 9 + tab[4] * 1 + tab[5] * 3 + tab[6] * 7 + tab[7] * 9 + tab[8] * 1 + tab[9] * 3 + tab[10] * 1
if suma % 10 == 0:
    print("D")
else:
    print("N")

# http://pl.spoj.com/problems/JPESEL/