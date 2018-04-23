kod = input()
tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
tab2 = []
for i in range(len(kod)):
    for x in range(len(tab)):
        if kod[i] == " ":
            tab2.insert(i," ")
        elif ord(kod[i]) == ord(tab[x]):
            tab2.insert(i,tab[(x + 3) % len(tab)])
print("".join(tab2))